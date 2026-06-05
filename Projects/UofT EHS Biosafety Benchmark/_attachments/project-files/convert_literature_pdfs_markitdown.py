#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

from markitdown import MarkItDown


LIT_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/Literature Wiki")
PAPERS_DIR = "Papers"
DATA_DIR = "_data"
OUT_DIR = "markitdown"


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*[\"']?(.+?)[\"']?\s*$", text, flags=re.M)
    return match.group(1).strip() if match else ""


def safe_name(name: str) -> str:
    name = re.sub(r"[^\w .,-]+", "-", name, flags=re.A).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:180].rstrip(" .") or "paper"


def paper_notes(root: Path) -> list[Path]:
    return sorted((root / PAPERS_DIR).glob("*.md"), key=lambda p: p.name.lower())


def selected_notes(root: Path, limit: int | None, only_needs_review: bool) -> list[Path]:
    notes = paper_notes(root)
    if only_needs_review:
        notes = [
            path
            for path in notes
            if "Needs manual review:" in path.read_text(encoding="utf-8", errors="replace")
        ]
    if limit is not None:
        notes = notes[:limit]
    return notes


def convert_one(converter: MarkItDown, note_path: Path, root: Path, out_root: Path, write: bool) -> dict[str, str | int]:
    note_text = note_path.read_text(encoding="utf-8", errors="replace")
    source = frontmatter_value(note_text, "source_path")
    pdf_path = Path(source)
    row: dict[str, str | int] = {
        "note": str(note_path.relative_to(root)),
        "source_path": source,
        "output_path": "",
        "status": "",
        "characters": 0,
        "error": "",
    }
    if not source:
        row["status"] = "missing_source_path"
        return row
    if not pdf_path.exists():
        row["status"] = "missing_pdf"
        return row

    try:
        result = converter.convert(str(pdf_path))
        text = result.text_content or ""
    except Exception as exc:
        row["status"] = "convert_failed"
        row["error"] = str(exc)
        return row

    output_path = out_root / f"{safe_name(note_path.stem)}.md"
    row["output_path"] = str(output_path.relative_to(root))
    row["characters"] = len(text)
    row["status"] = "converted" if len(text.strip()) >= 500 else "too_short"

    if write:
        out_root.mkdir(parents=True, exist_ok=True)
        header = [
            "---",
            f'source_note: "{note_path.relative_to(root)}"',
            f'source_pdf: "{pdf_path}"',
            'converter: "microsoft/markitdown"',
            "---",
            "",
        ]
        output_path.write_text("\n".join(header) + text.rstrip() + "\n", encoding="utf-8")
    return row


def write_report(root: Path, rows: list[dict[str, str | int]]) -> None:
    data_root = root / DATA_DIR
    data_root.mkdir(parents=True, exist_ok=True)
    csv_path = data_root / "markitdown_conversion_report.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["note", "source_path", "output_path", "status", "characters", "error"])
        writer.writeheader()
        writer.writerows(rows)
    (data_root / "markitdown_conversion_report.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert Literature Wiki source PDFs with MarkItDown.")
    parser.add_argument("--root", default=str(LIT_ROOT))
    parser.add_argument("--write", action="store_true", help="Write converted Markdown and reports into the vault.")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--only-needs-review",
        action="store_true",
        help="Convert notes whose current reading notes still contain 'Needs manual review'.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    out_root = root / DATA_DIR / OUT_DIR
    notes = selected_notes(root, args.limit, args.only_needs_review)
    converter = MarkItDown(enable_plugins=False)

    rows = [convert_one(converter, note, root, out_root, args.write) for note in notes]
    counts: dict[str, int] = {}
    for row in rows:
        status = str(row["status"])
        counts[status] = counts.get(status, 0) + 1
    if args.write:
        write_report(root, rows)

    print(f"Root: {root}")
    print(f"Paper notes selected: {len(notes)}")
    print(f"Status counts: {counts}")
    if args.write:
        print(f"Markdown output: {out_root}")
        print(f"Report: {root / DATA_DIR / 'markitdown_conversion_report.csv'}")
    else:
        print("Dry run only. Re-run with --write to save converted Markdown.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
