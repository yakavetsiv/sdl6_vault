#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    print("+ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Iteratively evaluate GPT-5.5 on UofT EHS biosafety QA and refill likely missed questions."
    )
    parser.add_argument("--start", default="ehs_biosafety_qa_seed_1000.jsonl")
    parser.add_argument("--rounds", type=int, default=1)
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument("--target", type=int, default=1000)
    parser.add_argument("--prefix", default="ehs_biosafety")
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--threshold", type=float, default=0.33)
    parser.add_argument("--seed", type=int, default=56)
    parser.add_argument("--limit", type=int, default=None, help="Optional smoke-test limit for each eval round.")
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set. Export it before running GPT evaluation.")

    current = Path(args.start)
    if not current.exists():
        raise SystemExit(f"Start dataset does not exist: {current}")
    if count_jsonl(current) != args.target and args.limit is None:
        print(f"Warning: {current} has {count_jsonl(current)} rows, target is {args.target}.", file=sys.stderr)

    seen_files = [current]
    for round_no in range(1, args.rounds + 1):
        eval_path = Path(f"{args.prefix}_gpt55_eval_round{round_no}.jsonl")
        next_path = Path(f"{args.prefix}_qa_round{round_no + 1}.jsonl")

        eval_cmd = [
            sys.executable,
            "run_gpt55_ehs_eval.py",
            "--input",
            str(current),
            "--output",
            str(eval_path),
            "--model",
            args.model,
            "--threshold",
            str(args.threshold),
            "--sleep",
            str(args.sleep),
        ]
        if args.limit is not None:
            eval_cmd.extend(["--limit", str(args.limit)])
        run(eval_cmd)

        refill_cmd = [
            sys.executable,
            "refill_ehs_biosafety_questions.py",
            "--base",
            str(current),
            "--eval",
            str(eval_path),
            "--out",
            str(next_path),
            "--target",
            str(args.target),
            "--seed",
            str(args.seed + round_no),
        ]
        for seen_file in seen_files:
            refill_cmd.extend(["--seen", str(seen_file)])
        run(refill_cmd)

        rows = count_jsonl(next_path)
        if rows != args.target and args.limit is None:
            raise SystemExit(f"{next_path} has {rows} rows; expected {args.target}.")
        print(f"Round {round_no} complete: eval={eval_path} next={next_path} rows={rows}", flush=True)

        current = next_path
        seen_files.append(eval_path)
        seen_files.append(next_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
