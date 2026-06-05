#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


EHS_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/EHS Wiki")


# True duplicate pages: keep the canonical unsuffixed page and remove the suffixed copy.
DELETE_TO_CANONICAL = {
    "Biological Spills (2)": "Biological Spills",
    "Biological Waste Disposal (2)": "Biological Waste Disposal",
    "Chemical Spill Procedures (2)": "Chemical Spill Procedures",
    "Emergency Procedures (3)": "Emergency Procedures",
    "Environmental Health Safety Program Policies Procedures and Guidelines (2)": "Environmental Health Safety Program Policies Procedures and Guidelines",
    "Guidelines for Laboratory Closure (2)": "Guidelines for Laboratory Closure",
    "Guidelines for Laboratory Tours (2)": "Guidelines for Laboratory Tours",
    "Guidelines on the Use of Perfumes and Scented Products (2)": "Guidelines on the Use of Perfumes and Scented Products",
    "Institutional Biosafety Biosecurity Committee (2)": "Institutional Biosafety Biosecurity Committee",
    "Laboratory Hazardous Waste Management and Disposal Manual (2)": "Laboratory Hazardous Waste Management and Disposal Manual",
    "Laser Safety (2)": "Laser Safety",
    "Radiation Protection Service (2)": "Radiation Protection Service",
    "Training Matrix Laboratory Personnel (2)": "Training Matrix Laboratory Personnel",
    "Workplace Hazardous Materials Information System WHMIS (2)": "Workplace Hazardous Materials Information System WHMIS",
    "X-ray Permit Application and Machine Registration Procedures (2)": "X-ray Permit Application and Machine Registration Procedures",
    "X-ray Safety (2)": "X-ray Safety",
}


# This is not a duplicate of the general emergency page; it is the biosafety-manual emergency page.
RENAME_TO_CANONICAL = {
    "Emergency Procedures (2)": "Biosafety Manual Emergency Procedures",
}


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


def update_heading(path: Path, old_title: str, new_title: str, write: bool) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    updated = re.sub(rf"^# {re.escape(old_title)}$", f"# {new_title}", text, count=1, flags=re.M)
    if updated != text and write:
        path.write_text(updated, encoding="utf-8")
    return updated != text


def duplicate_groups(root: Path) -> dict[str, list[Path]]:
    pages = root / "Pages"
    groups: dict[str, list[Path]] = {}
    for path in pages.glob("*.md"):
        key = re.sub(r" \(\d+\)$", "", path.stem)
        groups.setdefault(key, []).append(path)
    return {key: sorted(paths) for key, paths in groups.items() if len(paths) > 1}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--root", default=str(EHS_ROOT))
    args = parser.parse_args()

    root = Path(args.root)
    pages = root / "Pages"
    replacements = {**DELETE_TO_CANONICAL, **RENAME_TO_CANONICAL}

    changed_links: list[Path] = []
    for path in root.glob("**/*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        updated = replace_wikilink_targets(text, replacements)
        if updated != text:
            changed_links.append(path)
            if args.write:
                path.write_text(updated, encoding="utf-8")

    renamed: list[tuple[Path, Path]] = []
    heading_updates: list[Path] = []
    for old_stem, new_stem in RENAME_TO_CANONICAL.items():
        old_path = pages / f"{old_stem}.md"
        new_path = pages / f"{new_stem}.md"
        if old_path.exists():
            if new_path.exists():
                raise SystemExit(f"Cannot rename {old_path}; destination already exists: {new_path}")
            changed_heading = update_heading(old_path, "Emergency Procedures", new_stem, args.write)
            if changed_heading:
                heading_updates.append(old_path)
            renamed.append((old_path, new_path))
            if args.write:
                old_path.rename(new_path)

    deleted: list[Path] = []
    for old_stem, canonical_stem in DELETE_TO_CANONICAL.items():
        old_path = pages / f"{old_stem}.md"
        canonical_path = pages / f"{canonical_stem}.md"
        if old_path.exists():
            if not canonical_path.exists():
                raise SystemExit(f"Canonical target does not exist for {old_path}: {canonical_path}")
            deleted.append(old_path)
            if args.write:
                old_path.unlink()

    remaining_dupes = duplicate_groups(root)
    print(f"Root: {root}")
    print(f"Link files changed: {len(changed_links)}")
    for path in changed_links:
        print(f"  links: {path.relative_to(root)}")
    print(f"Heading updates: {len(heading_updates)}")
    for path in heading_updates:
        print(f"  heading: {path.relative_to(root)}")
    print(f"Renames: {len(renamed)}")
    for old_path, new_path in renamed:
        print(f"  rename: {old_path.relative_to(root)} -> {new_path.relative_to(root)}")
    print(f"Deletes: {len(deleted)}")
    for path in deleted:
        print(f"  delete: {path.relative_to(root)}")
    print(f"Remaining duplicate title groups: {len(remaining_dupes)}")
    for key, paths in remaining_dupes.items():
        names = ", ".join(path.name for path in paths)
        print(f"  remaining: {key}: {names}")
    if not args.write:
        print("Dry run only. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
