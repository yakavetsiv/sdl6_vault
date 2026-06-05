#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from update_literature_reading_notes import (
    ExtractedNotes,
    extract_abstract,
    extract_dataset_system,
    extract_limitation,
    extract_method,
    key_figure,
    parse_topics,
    render_reading_notes,
    reusable_idea,
    update_status,
)


LIT_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/Literature Wiki")
REPORT = LIT_ROOT / "_data" / "markitdown_conversion_report.csv"

READING_SECTION_RE = re.compile(r"## Reading Notes\n.*?(?=\n## |\Z)", flags=re.S)


def title_from_note(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.M)
    return match.group(1).strip() if match else fallback


def load_report(report_path: Path) -> list[dict[str, str]]:
    if not report_path.exists():
        return []
    with report_path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def extract_from_markdown(note_text: str, markdown_text: str, title: str) -> ExtractedNotes:
    topics = parse_topics(note_text)
    return ExtractedNotes(
        extract_abstract(markdown_text),
        key_figure(markdown_text),
        extract_method(markdown_text),
        extract_dataset_system(markdown_text, title),
        extract_limitation(markdown_text),
        reusable_idea(markdown_text, topics),
        "markitdown_extracted",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Refill weak Literature Wiki reading notes from MarkItDown Markdown.")
    parser.add_argument("--root", default=str(LIT_ROOT))
    parser.add_argument("--report", default=str(REPORT))
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    root = Path(args.root)
    rows = [row for row in load_report(Path(args.report)) if row.get("status") == "converted"]
    if args.limit is not None:
        rows = rows[: args.limit]

    changed = []
    still_manual = []
    for row in rows:
        note_path = root / row["note"]
        markdown_path = root / row["output_path"]
        if not note_path.exists() or not markdown_path.exists():
            continue
        note_text = note_path.read_text(encoding="utf-8", errors="replace")
        if "Needs manual review:" not in note_text:
            continue
        markdown_text = markdown_path.read_text(encoding="utf-8", errors="replace")
        title = title_from_note(note_text, note_path.stem)
        notes = extract_from_markdown(note_text, markdown_text, title)
        replacement = render_reading_notes(notes).rstrip()
        updated = READING_SECTION_RE.sub(replacement, note_text, count=1)
        updated = update_status(updated, "reading-notes-markitdown")
        if "Needs manual review:" in replacement:
            still_manual.append(str(note_path.relative_to(root)))
        if updated != note_text:
            changed.append(str(note_path.relative_to(root)))
            if args.write:
                note_path.write_text(updated, encoding="utf-8")

    print(f"Root: {root}")
    print(f"Converted MarkItDown rows selected: {len(rows)}")
    print(f"Paper notes changed: {len(changed)}")
    print(f"Changed notes still containing manual-review fields: {len(still_manual)}")
    if not args.write:
        print("Dry run only. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
