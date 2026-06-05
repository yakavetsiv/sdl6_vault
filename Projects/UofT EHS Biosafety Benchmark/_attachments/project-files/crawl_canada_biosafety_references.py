#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
import re
from dataclasses import dataclass
from pathlib import Path

from crawl4ai import AsyncWebCrawler


EHS_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/EHS Wiki")


@dataclass(frozen=True)
class CrawlTarget:
    title: str
    url: str
    note_name: str
    summary: str


TARGETS = (
    CrawlTarget(
        "Canadian Biosafety Standards and Guidelines",
        "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines.html",
        "Canadian Biosafety Standards and Guidelines",
        "Landing page for Canadian biosafety standards, guidelines, directives, tools, and contacts.",
    ),
    CrawlTarget(
        "Canadian Biosafety Standard, Third Edition",
        "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines/third-edition.html",
        "Canadian Biosafety Standard Third Edition",
        "National standard for regulated laboratories and containment zones handling human or terrestrial animal pathogens and toxins.",
    ),
    CrawlTarget(
        "Biosecurity Addendum to the Canadian Biosafety Standard, Third Edition",
        "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines/biosecurity-addendum-canadian-biosafety-standard-third-edition.html",
        "Biosecurity Addendum to the Canadian Biosafety Standard Third Edition",
        "Additional biosecurity requirements for the highest containment facilities.",
    ),
    CrawlTarget(
        "Canadian Biosafety Handbook, Second Edition",
        "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines/handbook-second-edition.html",
        "Canadian Biosafety Handbook Second Edition",
        "Handbook on safe and secure handling of pathogens and toxins in Canada.",
    ),
    CrawlTarget(
        "Canadian biosafety guidelines",
        "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines/guidance.html",
        "Canadian Biosafety Guidelines",
        "Guides to biosafety plans, handling, best practices, risk assessments, and reporting in Canada.",
    ),
    CrawlTarget(
        "Canadian Biosafety App",
        "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines/cbs-biosafety-app.html",
        "Canadian Biosafety App",
        "App for finding Canadian Biosafety Standard requirements by facility setting and status.",
    ),
    CrawlTarget(
        "Contact Canadian Biosafety Standards and Guidelines",
        "https://www.canada.ca/en/public-health/services/canadian-biosafety-standards-guidelines/contact-us.html",
        "Contact Canadian Biosafety Standards and Guidelines",
        "Contact information for questions about Canadian biosafety standards, handbooks, guidelines, and future editions.",
    ),
)


def frontmatter(target: CrawlTarget, status: str) -> str:
    return f"""---
type: external-biosafety-reference
status: "{status}"
source_url: "{target.url}"
source_organization: "Public Health Agency of Canada"
tags:
  - ehs/external-reference
  - ehs/biosafety
  - biosafety
  - biosecurity
  - canada
---
"""


def clean_markdown(markdown: str, title: str) -> str:
    markdown = str(markdown)
    markdown = markdown.replace("\r\n", "\n")
    lines = markdown.splitlines()
    keep: list[str] = []
    started = False
    stop_patterns = (
        "## Page details",
        "## About this site",
        "### Public Health Agency of Canada",
        "### Government of Canada",
    )
    skip_prefixes = (
        "* [Skip to",
        "* [Switch to basic HTML",
        "## Language selection",
        "## Search",
        "## Menu",
        "Main Menu",
        "Search Canada.ca",
        "Search",
        "* * *",
    )
    for line in lines:
        stripped = line.strip()
        if not started:
            if stripped in {f"# {title}", f"#  {title}"} or stripped.startswith(f"# {title}"):
                started = True
                keep.append(f"# {title}")
            continue
        if any(stripped.startswith(pattern) for pattern in stop_patterns):
            break
        if not stripped:
            keep.append("")
            continue
        if any(stripped.startswith(prefix) for prefix in skip_prefixes):
            continue
        if stripped.startswith("You are here:") or stripped.startswith("## You are here"):
            continue
        keep.append(line.rstrip())

    cleaned = "\n".join(keep).strip()
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = re.sub(r"\[\[Next page\]\]", "Next page", cleaned)
    cleaned = re.sub(r"\[\[Next page\]\((https?://[^)]+)\)\]", r"[Next page](\1)", cleaned)
    return cleaned


def semantic_links(target: CrawlTarget) -> str:
    links = [
        "## Benchmark Scope Note",
        "",
        "This is external national biosafety reference material. It supports background interpretation of UofT EHS biosafety notes, but it should not be treated as a UofT-specific requirement unless a UofT EHS page or permit document explicitly adopts it.",
        "",
        "Keep this note outside `Pages/` and `PDF Notes/` so the UofT biosafety benchmark builder does not accidentally generate answer keys from national reference material.",
        "",
        "## Semantic Links",
        "",
        "### UofT Biosafety Context",
        "- [[Biosafety Manual]]",
        "- [[Biosafety]]",
        "- [[Biosafety Permits]]",
        "- [[Institutional Biosafety Biosecurity Committee]]",
        "",
        "### Related Program Areas",
        "- [[Biosafety Training]]",
        "- [[Medical Surveillance and Immunoprophylaxis]]",
        "- [[General Laboratory Safety Practices]]",
        "- [[Biosafety Cabinets]]",
        "- [[Decontamination]]",
        "- [[Biological Waste Disposal]]",
        "- [[Biological Spills]]",
        "",
        "### Canada Biosafety Reference Set",
    ]
    for item in TARGETS:
        if item.note_name != target.note_name:
            links.append(f"- [[{item.note_name}]]")
    return "\n".join(links)


def render_note(target: CrawlTarget, markdown: str, status: str) -> str:
    body = clean_markdown(markdown, target.title)
    if not body:
        body = f"# {target.title}\n\n{target.summary}"
    return (
        frontmatter(target, status)
        + f"\n# {target.note_name}\n\n"
        + f"Source: {target.url}\n\n"
        + f"Summary: {target.summary}\n\n"
        + "## Converted Canada.ca Content\n\n"
        + body.removeprefix(f"# {target.title}").strip()
        + "\n\n"
        + semantic_links(target)
        + "\n"
    )


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


async def crawl_targets() -> list[tuple[CrawlTarget, object]]:
    async with AsyncWebCrawler() as crawler:
        results = []
        for target in TARGETS:
            result = await crawler.arun(url=target.url)
            results.append((target, result))
        return results


async def main_async(args: argparse.Namespace) -> int:
    root = Path(args.root)
    raw_dir = root / "_data" / "external" / "canada-biosafety"
    note_dir = root / "External References"
    changes: list[str] = []
    manifest = []

    results = await crawl_targets()
    for target, result in results:
        success = bool(getattr(result, "success", False))
        status = "crawl4ai-converted" if success else "crawl4ai-failed"
        markdown = str(getattr(result, "markdown", "") or "")
        note = render_note(target, markdown, status)
        raw_payload = {
            "title": target.title,
            "url": target.url,
            "success": success,
            "status_code": getattr(result, "status_code", None),
            "markdown": markdown,
            "error_message": getattr(result, "error_message", None),
        }
        manifest.append({k: raw_payload[k] for k in ("title", "url", "success", "status_code", "error_message")})

        raw_path = raw_dir / f"{target.note_name}.json"
        note_path = note_dir / f"{target.note_name}.md"
        raw_text = json.dumps(raw_payload, ensure_ascii=False, indent=2)

        if not raw_path.exists() or raw_path.read_text(encoding="utf-8", errors="replace") != raw_text:
            changes.append(str(raw_path.relative_to(root)))
            if args.write:
                raw_path.parent.mkdir(parents=True, exist_ok=True)
                raw_path.write_text(raw_text, encoding="utf-8")
        if not note_path.exists() or note_path.read_text(encoding="utf-8", errors="replace") != note:
            changes.append(str(note_path.relative_to(root)))
            if args.write:
                note_path.parent.mkdir(parents=True, exist_ok=True)
                note_path.write_text(note, encoding="utf-8")

    manifest_path = raw_dir / "manifest.json"
    manifest_text = json.dumps(manifest, ensure_ascii=False, indent=2)
    if not manifest_path.exists() or manifest_path.read_text(encoding="utf-8", errors="replace") != manifest_text:
        changes.append(str(manifest_path.relative_to(root)))
        if args.write:
            manifest_path.parent.mkdir(parents=True, exist_ok=True)
            manifest_path.write_text(manifest_text, encoding="utf-8")

    for path, heading in (
        (root / "EHS Wiki Home.md", "External References"),
        (root / "EHS Knowledge Graph Index.md", "Entry Points"),
        (root / "Topics" / "EHS Topic - Biosafety.md", "External References"),
    ):
        for target in TARGETS:
            if f"[[{target.note_name}]]" not in path.read_text(encoding="utf-8", errors="replace"):
                changes.append(str(path.relative_to(root)))
                if args.write:
                    append_unique_link(path, heading, target.note_name)

    print(f"Targets crawled: {len(results)}")
    print(f"Successful crawls: {sum(bool(getattr(result, 'success', False)) for _, result in results)}")
    print(f"Root: {root}")
    print(f"Changed files: {len(changes)}")
    for change in changes:
        print(f"  changed: {change}")
    if not args.write:
        print("Dry run only. Re-run with --write to apply.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--root", default=str(EHS_ROOT))
    args = parser.parse_args()
    return asyncio.run(main_async(args))


if __name__ == "__main__":
    raise SystemExit(main())
