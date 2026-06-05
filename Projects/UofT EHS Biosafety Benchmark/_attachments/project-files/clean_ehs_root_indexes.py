#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


EHS_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/EHS Wiki")


HOME_FRONTMATTER = """---
type: ehs-home
status: curated
source: "https://ehs.utoronto.ca"
tags:
  - ehs
  - safety
  - uoft
---
"""


PDF_INDEX_FRONTMATTER = """---
type: ehs-pdf-index
status: generated
tags:
  - ehs
  - pdf-index
---
"""


def render_home(root: Path) -> str:
    pages_count = len(list((root / "Pages").glob("*.md")))
    pdf_notes_count = len(list((root / "PDF Notes").glob("*.md")))
    pdfs_count = len([p for p in (root / "PDFs").glob("*") if p.is_file()])
    topics = sorted(path.stem for path in (root / "Topics").glob("*.md"))

    topic_lines = "\n".join(f"- [[{topic}]]" for topic in topics)

    return (
        HOME_FRONTMATTER
        + f"""
# EHS Wiki Home

Curated local knowledge base for public University of Toronto Environmental Health & Safety resources.

## Start Here

- [[EHS Knowledge Graph Index]]
- [[resources|Resources]]
- [[Environmental Health Safety Program Policies Procedures and Guidelines]]
- [[Biosafety Manual]]
- [[Laboratory Hazardous Waste Management and Disposal Manual]]
- [[Personal Protective Equipment PPE]]
- [[Standards]]
- [[X-ray Safety Program Manual]]
- [[PDF Notes Index]]

## Core Topics

{topic_lines}

## Biosafety Entry Points

- [[Biosafety]]
- [[Biosafety Manual]]
- [[Biosafety Permits]]
- [[Biosafety Training]]
- [[Institutional Biosafety Biosecurity Committee]]
- [[Biological Spills]]
- [[Biological Spill Kit]]
- [[Biological Waste Disposal]]
- [[Decontamination]]
- [[General Laboratory Safety Practices]]
- [[Biosafety Cabinets]]
- [[Autoclaves Steam Sterilizers]]
- [[Laboratory Users]]
- [[Biosafety Permit Holder]]

## Emergency and Waste Entry Points

- [[Emergency Procedures]]
- [[Biosafety Manual Emergency Procedures]]
- [[Spill Reporting Procedures]]
- [[Generic Lab Emergency Contact List]]
- [[Laboratory Waste Management]]
- [[5.4 Mixed Waste]]
- [[5.5 Sharp Waste Management]]
- [[Summary Guide for Packaging Handling Hazardous Waste]]

## Local Inventory

- Pages: {pages_count}
- PDF notes: {pdf_notes_count}
- Source PDFs: {pdfs_count}
- Topic notes: {len(topics)}

## Data

- `_data/ehs_pages_actual.csv`
- `_data/ehs_pdfs_actual.csv`
- `_data/ehs_graph_edges_stage2_final.csv`
- `_data/ehs_graph_edges_stage2_final.json`
"""
    ).lstrip()


def render_pdf_index(root: Path) -> str:
    notes = sorted((root / "PDF Notes").glob("*.md"), key=lambda path: path.stem.lower())
    lines = "\n".join(f"- [[{path.stem}]]" for path in notes)
    return (
        PDF_INDEX_FRONTMATTER
        + f"""
# PDF Notes Index

Converted source documents linked to local PDF note Markdown.

## Notes

{lines}
"""
    ).lstrip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--root", default=str(EHS_ROOT))
    args = parser.parse_args()

    root = Path(args.root)
    outputs = {
        root / "EHS Wiki Home.md": render_home(root),
        root / "PDF Notes Index.md": render_pdf_index(root),
    }

    changed = []
    for path, content in outputs.items():
        old = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
        if old != content:
            changed.append(path)
            if args.write:
                path.write_text(content, encoding="utf-8")

    print(f"Root: {root}")
    print(f"Changed files: {len(changed)}")
    for path in changed:
        print(f"  changed: {path.relative_to(root)}")
    if not args.write:
        print("Dry run only. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
