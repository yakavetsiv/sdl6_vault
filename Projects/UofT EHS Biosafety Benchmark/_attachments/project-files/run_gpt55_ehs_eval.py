#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path

from openai import OpenAI


SYSTEM = """You answer from general knowledge only. Do not use tools, web, files, or retrieval.
If the question asks for a source-specific University of Toronto EHS detail and you do not know it,
say you do not know. Keep the answer concise."""


def tokens(text: str) -> set[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9-]{2,}", text.lower())
    stop = {
        "the", "and", "for", "with", "that", "this", "from", "into", "about", "should",
        "shall", "must", "may", "are", "was", "were", "have", "has", "not", "all",
        "university", "toronto", "ehs", "document", "source", "according",
    }
    return {w for w in words if w not in stop}


def heuristic_score(expected: str, actual: str) -> float:
    exp = tokens(expected)
    act = tokens(actual)
    if not exp:
        return 0.0
    overlap = len(exp & act) / max(1, len(exp))
    if "i don't know" in actual.lower() or "do not know" in actual.lower():
        overlap *= 0.2
    return round(overlap, 4)


def classify(score: float, threshold: float) -> str:
    if score >= threshold:
        return "likely_correct"
    if score >= threshold * 0.55:
        return "partial_or_uncertain"
    return "likely_missed"


def ask(client: OpenAI, model: str, question: str) -> str:
    # Responses API is current in openai>=1.x; fallback to chat completions if needed.
    try:
        response = client.responses.create(
            model=model,
            input=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": question},
            ],
        )
        return response.output_text.strip()
    except Exception:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": question},
            ],
        )
        return response.choices[0].message.content.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="ehs_biosafety_qa_seed_1000.jsonl")
    parser.add_argument("--output", default="ehs_biosafety_gpt55_eval.jsonl")
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--threshold", type=float, default=0.33)
    parser.add_argument("--sleep", type=float, default=0.0)
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set. Export it before running GPT evaluation.")

    client = OpenAI()
    rows = [json.loads(line) for line in Path(args.input).read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.limit:
        rows = rows[: args.limit]

    done_ids = set()
    out = Path(args.output)
    if out.exists():
        for line in out.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done_ids.add(json.loads(line)["id"])

    with out.open("a", encoding="utf-8") as f:
        for i, row in enumerate(rows, start=1):
            if row["id"] in done_ids:
                continue
            actual = ask(client, args.model, row["question"])
            score = heuristic_score(row["answer"], actual)
            result = {
                **row,
                "model": args.model,
                "model_answer": actual,
                "heuristic_score": score,
                "eval_label": classify(score, args.threshold),
            }
            f.write(json.dumps(result, ensure_ascii=False) + "\n")
            f.flush()
            print(f"{i}/{len(rows)} {row['id']} {result['eval_label']} score={score}")
            if args.sleep:
                time.sleep(args.sleep)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
