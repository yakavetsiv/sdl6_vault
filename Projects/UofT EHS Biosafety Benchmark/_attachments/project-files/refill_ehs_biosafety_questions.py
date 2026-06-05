#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
from pathlib import Path

import build_ehs_biosafety_qa_dataset as builder


QA_FIELDS = (
    "id",
    "question",
    "answer",
    "source_title",
    "source_path",
    "source_url",
    "evidence",
    "terms",
    "type",
    "domain",
    "requires_source_access",
)


SOURCE_PATH_REPLACEMENTS = {
    "Pages/Biological Spills (2).md": "Pages/Biological Spills.md",
    "Pages/Biological Waste Disposal (2).md": "Pages/Biological Waste Disposal.md",
    "Pages/Chemical Spill Procedures (2).md": "Pages/Chemical Spill Procedures.md",
    "Pages/Emergency Procedures (2).md": "Pages/Biosafety Manual Emergency Procedures.md",
    "Pages/Emergency Procedures (3).md": "Pages/Emergency Procedures.md",
    "Pages/Environmental Health Safety Program Policies Procedures and Guidelines (2).md": "Pages/Environmental Health Safety Program Policies Procedures and Guidelines.md",
    "Pages/Guidelines for Laboratory Closure (2).md": "Pages/Guidelines for Laboratory Closure.md",
    "Pages/Guidelines for Laboratory Tours (2).md": "Pages/Guidelines for Laboratory Tours.md",
    "Pages/Guidelines on the Use of Perfumes and Scented Products (2).md": "Pages/Guidelines on the Use of Perfumes and Scented Products.md",
    "Pages/Institutional Biosafety Biosecurity Committee (2).md": "Pages/Institutional Biosafety Biosecurity Committee.md",
    "Pages/Laboratory Hazardous Waste Management and Disposal Manual (2).md": "Pages/Laboratory Hazardous Waste Management and Disposal Manual.md",
    "Pages/Laser Safety (2).md": "Pages/Laser Safety.md",
    "Pages/Radiation Protection Service (2).md": "Pages/Radiation Protection Service.md",
    "Pages/Training Matrix Laboratory Personnel (2).md": "Pages/Training Matrix Laboratory Personnel.md",
    "Pages/Workplace Hazardous Materials Information System WHMIS (2).md": "Pages/Workplace Hazardous Materials Information System WHMIS.md",
    "Pages/X-ray Permit Application and Machine Registration Procedures (2).md": "Pages/X-ray Permit Application and Machine Registration Procedures.md",
    "Pages/X-ray Safety (2).md": "Pages/X-ray Safety.md",
}


BANNED_QUESTION_TERMS = (
    "knowledge",
    "sdl6",
    "obsidian",
    "source-specific",
    "specific document",
    "knowledge base",
    "q&a system",
)


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def stable_id(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def qa_only(row: dict) -> dict:
    clean = {key: row[key] for key in QA_FIELDS if key in row}
    if "requires_source_access" not in clean and row.get("requires_knowledge_access") is not None:
        clean["requires_source_access"] = bool(row.get("requires_knowledge_access"))
    return clean


def anchor_from_row(row: dict) -> str:
    question = row.get("question", "")
    match = re.search(r"connected to '([^']+)'", question)
    if match:
        return match.group(1)
    match = re.search(r"context of '([^']+)'", question)
    if match:
        return match.group(1)
    answer = row.get("answer", "")
    return builder.anchor_from_answer(answer, (row.get("terms") or ["biosafety"])[0])


def sanitize_question(row: dict) -> dict:
    row = qa_only(row)
    terms = row.get("terms") or ["biosafety"]
    term = terms[0]
    qtype = row.get("type", "")
    anchor = anchor_from_row(row)

    if qtype in {"direct_guidance", "staff_practical_action"}:
        question = f"I need to handle a situation involving {anchor}. What does UofT EHS require?"
        qtype = "staff_practical_action"
    elif qtype in {"source_specific_statement", "staff_rule_or_guidance"}:
        question = f"Our lab is dealing with {anchor}. What safety steps are required at UofT?"
        qtype = "staff_rule_or_guidance"
    elif qtype in {"hidden_in_source", "specific_requirement", "lab_scenario_handling"}:
        question = f"What should our UofT lab do if the issue involves {anchor}?"
        qtype = "lab_scenario_handling"
    elif qtype in {"anchored_source_detail", "supervisor_instruction"}:
        question = f"What should a supervisor tell lab personnel when {anchor}?"
        qtype = "supervisor_instruction"
    elif qtype in {"contextual_biosafety_answer", "contextual_biosafety_detail", "safety_requirement"}:
        question = f"What UofT safety requirement applies when {anchor}?"
        qtype = "safety_requirement"
    elif qtype in {"precise_supported_statement", "compliance_check"}:
        question = f"For UofT biosafety compliance, what should I check or do if {anchor}?"
        qtype = "compliance_check"
    else:
        question = f"Our lab is dealing with {anchor}. What safety steps are required at UofT?"
        qtype = "staff_rule_or_guidance"

    row["question"] = question
    row["type"] = qtype
    row["source_path"] = SOURCE_PATH_REPLACEMENTS.get(row.get("source_path", ""), row.get("source_path", ""))
    row["id"] = "ehs-bio-" + stable_id(row["question"] + row.get("answer", "") + row.get("source_path", ""))
    return row


def has_banned_question_terms(row: dict) -> bool:
    question = row.get("question", "").lower()
    return any(term in question for term in BANNED_QUESTION_TERMS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="ehs_biosafety_qa_seed_1000.jsonl")
    parser.add_argument("--eval", default="ehs_biosafety_gpt55_eval.jsonl")
    parser.add_argument("--out", default="ehs_biosafety_qa_next_round.jsonl")
    parser.add_argument("--target", type=int, default=1000)
    parser.add_argument("--keep-label", action="append", default=["likely_missed", "partial_or_uncertain"])
    parser.add_argument(
        "--seen",
        action="append",
        default=[],
        help="Prior QA or eval JSONL files whose questions should not be reused as new filler.",
    )
    parser.add_argument("--seed", type=int, default=56)
    args = parser.parse_args()

    base_rows = load_jsonl(Path(args.base))
    eval_rows = load_jsonl(Path(args.eval))
    seen_rows = []
    for seen_path in args.seen:
        seen_rows.extend(load_jsonl(Path(seen_path)))
    keep_labels = set(args.keep_label)

    retained = [sanitize_question(row) for row in eval_rows if row.get("eval_label") in keep_labels]
    retained = [row for row in retained if not has_banned_question_terms(row)]
    used_questions = {row["question"].lower() for row in [*base_rows, *eval_rows, *seen_rows]}

    evidence = builder.collect_evidence()
    candidates = []
    candidate_questions = set()
    for ev in evidence:
        for row in builder.make_questions(ev):
            row["source_path"] = SOURCE_PATH_REPLACEMENTS.get(row.get("source_path", ""), row.get("source_path", ""))
            question_key = row["question"].lower()
            if question_key not in used_questions and question_key not in candidate_questions and not has_banned_question_terms(row):
                candidates.append(row)
                candidate_questions.add(question_key)

    # Prefer sources/terms where GPT missed.
    missed_terms = {}
    missed_sources = {}
    for row in retained:
        for term in row.get("terms", []):
            missed_terms[term] = missed_terms.get(term, 0) + 1
        missed_sources[row.get("source_path", "")] = missed_sources.get(row.get("source_path", ""), 0) + 1

    def weight(row: dict) -> int:
        return 1 + sum(missed_terms.get(t, 0) for t in row.get("terms", [])) + missed_sources.get(row.get("source_path", ""), 0)

    rng = random.Random(args.seed)
    rng.shuffle(candidates)
    candidates.sort(key=weight, reverse=True)

    output = []
    seen = set()
    seen_questions = set()
    for row in retained:
        question_key = row["question"].lower()
        if row["id"] not in seen and question_key not in seen_questions:
            output.append(qa_only(row))
            seen.add(row["id"])
            seen_questions.add(question_key)
        if len(output) >= args.target:
            break
    for row in candidates:
        question_key = row["question"].lower()
        if row["id"] not in seen and question_key not in seen_questions:
            output.append(row)
            seen.add(row["id"])
            seen_questions.add(question_key)
        if len(output) >= args.target:
            break

    out = Path(args.out)
    with out.open("w", encoding="utf-8") as f:
        for row in output:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Retained from eval: {len(retained)}")
    print(f"Wrote next round: {len(output)} -> {out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
