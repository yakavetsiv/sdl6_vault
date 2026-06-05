#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
from dataclasses import dataclass
from pathlib import Path


EHS_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/EHS Wiki")
DEFAULT_OUT = Path("ehs_biosafety_qa_seed_1000.jsonl")

BIOSAFETY_TERMS = (
    "biosafety",
    "biosecurity",
    "biological",
    "biological waste",
    "biohazard",
    "human pathogens",
    "pathogen",
    "risk group",
    "rg1",
    "rg2",
    "containment",
    "permit",
    "autoclave",
    "decontamination",
    "disinfection",
    "sharps",
    "needles",
    "syringes",
    "spill",
    "waste",
    "laboratory animals",
    "lentiviral",
    "viral vector",
    "aerosol",
    "centrifuge",
    "bsc",
    "biosafety cabinet",
    "medical surveillance",
    "immunoprophylaxis",
    "importation",
    "biological materials",
    "emergency procedures",
)

STRONG_BIOSAFETY_TERMS = (
    "biosafety",
    "biosecurity",
    "biological waste",
    "biohazard",
    "human pathogens",
    "pathogen",
    "risk group",
    "rg1",
    "rg2",
    "containment",
    "autoclave",
    "decontamination",
    "disinfection",
    "sharps",
    "needles",
    "syringes",
    "laboratory animals",
    "lentiviral",
    "viral vector",
    "bsc",
    "biosafety cabinet",
    "immunoprophylaxis",
    "biological materials",
)

METADATA_PREFIXES = (
    "aliases:",
    "captured_at:",
    "converter:",
    "created:",
    "domain:",
    "local_pdf:",
    "requires_knowledge_access:",
    "source:",
    "source_file:",
    "source_path:",
    "source_pdf:",
    "source_title:",
    "source_url:",
    "stage:",
    "status:",
    "tags:",
    "terms:",
    "title:",
    "topics:",
    "type:",
    "updated:",
    "url:",
)

STOP_TITLES = {
    "EHS Wiki Home",
    "PDF Notes Index",
    "EHS Knowledge Graph Index",
}

ANCHOR_STOP_WORDS = {
    "document",
    "documents",
    "documentation",
    "source",
    "sources",
    "knowledge",
    "obsidian",
    "sdl6",
}


@dataclass
class Evidence:
    title: str
    path: Path
    source_url: str
    source_file: str
    snippet: str
    terms: list[str]


def stable_id(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def clean_text(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*[\"']?(.+?)[\"']?\s*$", text, flags=re.M)
    return match.group(1).strip() if match else ""


def title_from_text(path: Path, text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def split_snippets(text: str) -> list[str]:
    lines = []
    skip_section = False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            skip_section = any(
                marker in line.lower()
                for marker in (
                    "source",
                    "connected ehs pages",
                    "topic links",
                    "knowledge graph",
                    "converted pdf notes",
                    "referring ehs page notes",
                )
            )
            continue
        if skip_section and line.startswith("#"):
            skip_section = False
        if skip_section:
            continue
        lower_line = line.lower()
        if not line or line.startswith("---") or lower_line.startswith(METADATA_PREFIXES):
            continue
        if line.startswith("#"):
            continue
        if (
            "EHS Topic -" in line
            or "PDF Notes/" in line
            or "source_file:" in lower_line
            or "source_url:" in lower_line
            or "http://ehs.utoronto.ca" in lower_line
            or "https://ehs.utoronto.ca" in lower_line
        ):
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"^\d+\.\s+", "", line)
        line = clean_text(line)
        if line.lower().startswith(("local pdf:", "source:", "captured:", "stage 1", "stage 2")):
            continue
        if re.match(r"^[a-z]{2,}\b", line):
            continue
        if re.search(r"\(\d{4}\)\.", line):
            continue
        if 70 <= len(line) <= 480:
            lines.append(line)

    snippets = []
    for line in lines:
        parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", line)
        for part in parts:
            part = part.strip()
            if 70 <= len(part) <= 360:
                snippets.append(part)
        if len(line) <= 300:
            snippets.append(line)
    return snippets


def terms_in(text: str) -> list[str]:
    lower = text.lower()
    return [term for term in BIOSAFETY_TERMS if term in lower]


def anchor_from_answer(answer: str, fallback: str) -> str:
    words = re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", answer)
    kept = [
        word
        for word in words
        if word.lower() not in ANCHOR_STOP_WORDS and not word.lower().startswith("document")
    ]
    return " ".join(kept[:8]) or fallback


def collect_evidence() -> list[Evidence]:
    evidence: list[Evidence] = []
    for folder in ("Pages", "PDF Notes"):
        for path in sorted((EHS_ROOT / folder).glob("*.md"), key=lambda p: p.name.lower()):
            text = path.read_text(encoding="utf-8", errors="replace")
            title = title_from_text(path, text)
            if title in STOP_TITLES:
                continue
            full_terms = terms_in(title + " " + text[:5000])
            if not full_terms:
                continue
            strong_terms = [term for term in STRONG_BIOSAFETY_TERMS if term in (title + " " + text[:5000]).lower()]
            if not strong_terms:
                continue
            source_url = frontmatter_value(text, "source_url")
            source_file = frontmatter_value(text, "source_file")
            for snippet in split_snippets(text):
                snippet_terms = terms_in(snippet)
                if not snippet_terms:
                    continue
                if not any(term in STRONG_BIOSAFETY_TERMS for term in snippet_terms):
                    continue
                evidence.append(
                    Evidence(
                        title=title,
                        path=path,
                        source_url=source_url,
                        source_file=source_file,
                        snippet=snippet,
                        terms=snippet_terms[:5],
                    )
                )
    return evidence


def make_questions(ev: Evidence) -> list[dict]:
    term = ev.terms[0]
    title = ev.title
    source = ev.source_url or ev.source_file or str(ev.path)
    relpath = str(ev.path.relative_to(EHS_ROOT))
    answer = ev.snippet
    anchor = anchor_from_answer(answer, term)
    questions = [
        (
            f"I need to handle a situation involving {anchor}. What does UofT EHS require?",
            answer,
            "staff_practical_action",
        ),
        (
            f"Our lab is dealing with {anchor}. What safety steps are required at UofT?",
            answer,
            "staff_rule_or_guidance",
        ),
        (
            f"What should our UofT lab do if the issue involves {anchor}?",
            answer,
            "lab_scenario_handling",
        ),
        (
            f"What should a supervisor tell lab personnel when {anchor}?",
            answer,
            "supervisor_instruction",
        ),
        (
            f"What UofT safety requirement applies when {anchor}?",
            answer,
            "safety_requirement",
        ),
        (
            f"For UofT biosafety compliance, what should I check or do if {anchor}?",
            answer,
            "compliance_check",
        ),
    ]
    rows = []
    for q, a, qtype in questions:
        qid = "ehs-bio-" + stable_id(q + a + relpath)
        rows.append(
            {
                "id": qid,
                "question": q,
                "answer": a,
                "source_title": title,
                "source_path": relpath,
                "source_url": source,
                "evidence": ev.snippet,
                "terms": ev.terms,
                "type": qtype,
                "domain": "UofT EHS biosafety",
                "requires_source_access": True,
            }
        )
    return rows


def diversify(rows: list[dict], limit: int, seed: int) -> list[dict]:
    rng = random.Random(seed)
    by_source: dict[str, list[dict]] = {}
    for row in rows:
        by_source.setdefault(row["source_path"], []).append(row)
    for bucket in by_source.values():
        rng.shuffle(bucket)

    selected = []
    sources = list(by_source)
    rng.shuffle(sources)
    while len(selected) < limit and any(by_source.values()):
        for source in list(sources):
            bucket = by_source[source]
            if bucket:
                selected.append(bucket.pop())
                if len(selected) >= limit:
                    break
    return selected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument("--limit", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=55)
    args = parser.parse_args()

    evidence = collect_evidence()
    rows = []
    seen = set()
    for ev in evidence:
        for row in make_questions(ev):
            key = row["question"].lower()
            if key not in seen:
                rows.append(row)
                seen.add(key)
    selected = diversify(rows, args.limit, args.seed)

    out = Path(args.out)
    with out.open("w", encoding="utf-8") as f:
        for row in selected:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Evidence snippets: {len(evidence)}")
    print(f"Candidate questions: {len(rows)}")
    print(f"Wrote: {len(selected)} -> {out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
