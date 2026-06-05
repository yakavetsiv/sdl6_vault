#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


LIT_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/Literature Wiki")


def repair_text(text: str) -> str:
    text = re.sub(r"(Reusable idea for SDL6 / automation: .+?)## Knowledge Graph Edges", r"\1\n\n## Knowledge Graph Edges", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair spacing in generated Literature Wiki paper notes.")
    parser.add_argument("--root", default=str(LIT_ROOT))
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    root = Path(args.root)
    changed = []
    for path in sorted((root / "Papers").glob("*.md"), key=lambda p: p.name.lower()):
        original = path.read_text(encoding="utf-8", errors="replace")
        updated = repair_text(original)
        if updated != original:
            changed.append(path)
            if args.write:
                path.write_text(updated, encoding="utf-8")

    print(f"Root: {root}")
    print(f"Paper notes changed: {len(changed)}")
    if not args.write:
        print("Dry run only. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
