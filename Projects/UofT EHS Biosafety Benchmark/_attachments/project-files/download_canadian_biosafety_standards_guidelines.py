#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin


EHS_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/EHS Wiki")
SOURCE_URL = "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines.html"
NOTE_TITLE = "Canadian Biosafety Standards and Guidelines"

FALLBACK_SNAPSHOT = f"""<main>
<h1>{NOTE_TITLE}</h1>
<p>Safe handling of human and animal pathogens, toxins and plant pests in laboratories and containment zones.</p>
<h2>Services and information</h2>
<h3>Canadian Biosafety Standard, Third Edition</h3>
<p>Requirements for regulated laboratories and containment zones handling human or terrestrial animal pathogens and toxins.</p>
<h3>Biosecurity Addendum to the Canadian Biosafety Standard, Third Edition</h3>
<p>Biosecurity requirements for regulated facilities where Risk Group 4 human or terrestrial animal pathogens are handled or stored.</p>
<h3>Canadian Biosafety Handbook, Second Edition</h3>
<p>View the biosafety handbook on safe and secure handling of pathogens and toxins in Canada.</p>
<h3>Canadian biosafety guidelines</h3>
<p>Guides to biosafety plans, handling, best practices and more in Canada.</p>
<h3>Biosafety directives and advisories</h3>
<p>Official communications about containment requirements for the safe handling of specific pathogens.</p>
<h3>Canadian Biosafety App</h3>
<p>Use the free app to find specific requirements using Apple and Android devices.</p>
<h3>Facilities handling aquatic animal pathogens</h3>
<p>Containment standards for facilities handling aquatic animal pathogens.</p>
<h3>Facilities handling plant pests</h3>
<p>Standards for facilities handling plant pests.</p>
<h3>Contact us</h3>
<p>How to contact Public Health Agency of Canada biosafety and biosecurity services.</p>
<h2>Page details</h2>
<p>2025-02-04</p>
</main>""".encode("utf-8")


class CanadaPageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_main = False
        self.skip_depth = 0
        self.current_tag = ""
        self.current_href = ""
        self.blocks: list[tuple[str, str, str]] = []
        self.buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key: value or "" for key, value in attrs}
        if tag == "main":
            self.in_main = True
        if not self.in_main:
            return
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in {"h1", "h2", "h3", "p", "li"}:
            self.flush()
            self.current_tag = tag
            self.current_href = ""
        elif tag == "a" and self.current_tag:
            self.current_href = attrs_dict.get("href", "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "main":
            self.flush()
            self.in_main = False
            return
        if not self.in_main:
            return
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "a" and self.current_href:
            self.current_href = ""
        if tag == self.current_tag:
            self.flush()

    def handle_data(self, data: str) -> None:
        if self.in_main and not self.skip_depth and self.current_tag:
            self.buffer.append(data)

    def flush(self) -> None:
        if not self.current_tag:
            return
        text = " ".join("".join(self.buffer).split())
        if text:
            self.blocks.append((self.current_tag, html.unescape(text), self.current_href))
        self.buffer = []
        self.current_tag = ""
        self.current_href = ""


def fetch(url: str) -> tuple[bytes, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.read(), "downloaded-html"
    except Exception:
        return FALLBACK_SNAPSHOT, "browser-verified-snapshot"


def parse_blocks(raw: bytes) -> list[tuple[str, str, str]]:
    parser = CanadaPageParser()
    parser.feed(raw.decode("utf-8", errors="replace"))
    parser.flush()
    return parser.blocks


def link_markdown(text: str, href: str) -> str:
    if not href:
        return text
    absolute = urljoin(SOURCE_URL, href)
    if absolute.startswith("#"):
        return text
    return f"[{text}]({absolute})"


def render_note(raw: bytes, status: str) -> str:
    blocks = parse_blocks(raw)
    date = ""
    body_lines: list[str] = []
    in_services = False
    services: list[str] = []

    for tag, text, href in blocks:
        if text == NOTE_TITLE:
            continue
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
            date = text
            continue
        if text == "Services and information":
            in_services = True
            continue
        if text in {"Page details", "About this site", "Public Health Agency of Canada", "Government of Canada"}:
            in_services = False
            continue
        if in_services:
            if tag == "h3":
                services.append(f"- {link_markdown(text, href)}")
            elif tag == "p" and services:
                services[-1] += f": {text}"
            continue
        if tag == "p":
            body_lines.append(text)

    services_text = "\n".join(services)
    summary = "\n\n".join(body_lines[:2])
    page_date = date or "unknown"

    return f"""---
type: external-biosafety-reference
status: "{status}"
source_url: "{SOURCE_URL}"
source_organization: "Public Health Agency of Canada"
page_date: "{page_date}"
tags:
  - ehs/external-reference
  - ehs/biosafety
  - biosafety
  - biosecurity
  - canada
---

# {NOTE_TITLE}

Source: {SOURCE_URL}

Page date: {page_date}

## Summary

{summary}

## Services And Information

{services_text}

## Benchmark Scope Note

This is an external national biosafety reference. It should support background interpretation of UofT EHS biosafety notes, but it should not be treated as a UofT-specific requirement unless a UofT EHS page or permit document explicitly adopts it.

Keep this note outside `Pages/` and `PDF Notes/` so the UofT biosafety benchmark builder does not accidentally generate answer keys from national reference material.

## Semantic Links

### UofT Biosafety Context
- [[Biosafety Manual]]
- [[Biosafety]]
- [[Biosafety Permits]]
- [[Institutional Biosafety Biosecurity Committee]]

### Related Program Areas
- [[Biosafety Training]]
- [[Medical Surveillance and Immunoprophylaxis]]
- [[General Laboratory Safety Practices]]
- [[Biosafety Cabinets]]
- [[Decontamination]]
- [[Biological Waste Disposal]]
- [[Biological Spills]]

### External Reference Family
- Canadian Biosafety Handbook, Second Edition
"""


def append_unique_link(path: Path, heading: str, link: str) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    if f"[[{link}]]" in text:
        return False
    marker = f"## {heading}\n"
    if marker not in text:
        updated = text.rstrip() + f"\n\n{marker}\n\n- [[{link}]]\n"
    else:
        idx = text.index(marker) + len(marker)
        next_heading = text.find("\n## ", idx)
        if next_heading == -1:
            updated = text.rstrip() + f"\n- [[{link}]]\n"
        else:
            updated = text[:next_heading].rstrip() + f"\n- [[{link}]]\n" + text[next_heading:]
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--root", default=str(EHS_ROOT))
    args = parser.parse_args()

    root = Path(args.root)
    raw, status = fetch(SOURCE_URL)
    note = render_note(raw, status)

    raw_path = root / "_data" / "external" / "canadian-biosafety-standards-guidelines.html"
    note_path = root / "External References" / f"{NOTE_TITLE}.md"
    changed: list[str] = []

    if not raw_path.exists() or raw_path.read_bytes() != raw:
        changed.append(str(raw_path.relative_to(root)))
        if args.write:
            raw_path.parent.mkdir(exist_ok=True)
            raw_path.write_bytes(raw)

    if not note_path.exists() or note_path.read_text(encoding="utf-8", errors="replace") != note:
        changed.append(str(note_path.relative_to(root)))
        if args.write:
            note_path.parent.mkdir(exist_ok=True)
            note_path.write_text(note, encoding="utf-8")

    link_targets = [
        (root / "EHS Wiki Home.md", "External References"),
        (root / "EHS Knowledge Graph Index.md", "Entry Points"),
        (root / "Topics" / "EHS Topic - Biosafety.md", "External References"),
    ]
    for path, heading in link_targets:
        if f"[[{NOTE_TITLE}]]" not in path.read_text(encoding="utf-8", errors="replace"):
            changed.append(str(path.relative_to(root)))
            if args.write:
                append_unique_link(path, heading, NOTE_TITLE)

    print(f"Fetch status: {status}")
    print(f"Source bytes: {len(raw)}")
    print(f"Root: {root}")
    print(f"Changed files: {len(changed)}")
    for change in changed:
        print(f"  changed: {change}")
    if not args.write:
        print("Dry run only. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
