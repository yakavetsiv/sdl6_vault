#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


EHS_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/EHS Wiki")

NOTE_NAME = "Canadian Biosafety Handbook Second Edition"
SOURCE_URL = "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines/handbook-second-edition.html"
PDF_URL = "https://publications.gc.ca/site/eng/9.801778/publication.html"


NOTE = f"""---
type: external-biosafety-reference
status: scraped-summary
source_url: "{SOURCE_URL}"
source_pdf_page: "{PDF_URL}"
source_organization: "Public Health Agency of Canada"
published: "2016-05-26"
tags:
  - ehs/external-reference
  - ehs/biosafety
  - biosafety
  - biosecurity
  - canada
---

# Canadian Biosafety Handbook, Second Edition

Source: {SOURCE_URL}

Published by the Public Health Agency of Canada on May 26, 2016.

Important currency note: the Canada.ca page states that the Canadian Biosafety Standard, Second Edition is no longer in effect as of April 1, 2023, and that the handbook is being updated to align with the Canadian Biosafety Standard, Third Edition.

The source page links to a PDF version of the handbook: 52 MB, 366 pages.

## Why This Is In The EHS Wiki

This is an external national biosafety reference. It should support background interpretation of UofT EHS biosafety notes, but it should not be treated as a UofT-specific requirement unless a UofT EHS page or permit document explicitly adopts it.

## Table Of Contents

- Preface
- Abbreviations and acronyms
- Chapter 1: Introduction
- Chapter 2: Biological material
- Chapter 3: Containment levels and containment zones
- Chapter 4: Risk factors, risk groups, and risk assessments
- Chapter 5: Biosafety program management
- Chapter 6: Biosecurity
- Chapter 7: Medical surveillance program
- Chapter 8: Training program
- Chapter 9: Personal protective equipment
- Chapter 10: Air handling
- Chapter 11: Biological safety cabinets
- Chapter 12: Safety considerations for equipment used for biological work
- Chapter 13: Animal work considerations
- Chapter 14: Large scale work
- Chapter 15: Decontamination
- Chapter 16: Waste management
- Chapter 17: Emergency response plan
- Chapter 18: Incident reporting and investigation
- Chapter 19: Regulatory oversight

## Benchmark Scope Note

Keep this note outside `Pages/` and `PDF Notes/` so the UofT biosafety benchmark builder does not accidentally generate answer keys from national reference material. The benchmark is intended to test UofT EHS source-specific knowledge.

## Semantic Links

### UofT Biosafety Context
- [[Biosafety Manual]]
- [[Biosafety]]
- [[Biosafety Permits]]
- [[Institutional Biosafety Biosecurity Committee]]

### Program Elements
- [[Biosafety Training]]
- [[Medical Surveillance and Immunoprophylaxis]]
- [[Biosafety Permit Holder]]
- [[Laboratory Users]]

### Containment And Work Practices
- [[Biosafety Cabinets]]
- [[General Laboratory Safety Practices]]
- [[Techniques for Minimizing Aerosols]]
- [[Working with Laboratory Animals]]

### Decontamination, Waste, And Emergency Response
- [[Decontamination]]
- [[Autoclaves Steam Sterilizers]]
- [[Biological Waste Disposal]]
- [[Biological Spills]]
- [[Emergency Procedures]]
"""


def replace_wikilink_targets(text: str, replacements: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group("target")
        suffix = match.group("suffix") or ""
        replacement = replacements.get(target)
        if not replacement:
            return match.group(0)
        return f"[[{replacement}{suffix}]]"

    pattern = re.compile(r"\[\[(?P<target>[^\]|#]+)(?P<suffix>(?:#[^\]|]+)?(?:\|[^\]]+)?)?\]\]")
    return pattern.sub(repl, text)


def append_unique_link(path: Path, heading: str, link: str) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    if f"[[{link}]]" in text:
        return False
    marker = f"## {heading}\n"
    if marker not in text:
        updated = text.rstrip() + f"\n\n{marker}\n- [[{link}]]\n"
    else:
        idx = text.index(marker) + len(marker)
        next_heading = text.find("\n## ", idx)
        if next_heading == -1:
            updated = text.rstrip() + f"\n- [[{link}]]\n"
        else:
            section = text[idx:next_heading]
            updated = text[:next_heading].rstrip() + f"\n- [[{link}]]\n" + text[next_heading:]
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--root", default=str(EHS_ROOT))
    args = parser.parse_args()

    root = Path(args.root)
    ref_dir = root / "External References"
    note_path = ref_dir / f"{NOTE_NAME}.md"

    changes: list[str] = []
    if not note_path.exists() or note_path.read_text(encoding="utf-8", errors="replace") != NOTE:
        changes.append(str(note_path.relative_to(root)))
        if args.write:
            ref_dir.mkdir(exist_ok=True)
            note_path.write_text(NOTE, encoding="utf-8")

    link_targets = [
        (root / "EHS Wiki Home.md", "External References"),
        (root / "EHS Knowledge Graph Index.md", "Entry Points"),
        (root / "Topics" / "EHS Topic - Biosafety.md", "External References"),
    ]
    for path, heading in link_targets:
        text = path.read_text(encoding="utf-8", errors="replace")
        if f"[[{NOTE_NAME}]]" not in text:
            changes.append(str(path.relative_to(root)))
            if args.write:
                append_unique_link(path, heading, NOTE_NAME)

    print(f"Root: {root}")
    print(f"Changed files: {len(changes)}")
    for change in changes:
        print(f"  changed: {change}")
    if not args.write:
        print("Dry run only. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
