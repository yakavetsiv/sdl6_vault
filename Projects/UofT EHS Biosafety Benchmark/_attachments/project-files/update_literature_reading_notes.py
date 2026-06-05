#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path

from pdfminer.high_level import extract_text


LIT_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/Literature Wiki")
PAPERS = LIT_ROOT / "Papers"
DATA = LIT_ROOT / "_data"


READING_TEMPLATE_RE = re.compile(
    r"## Reading Notes\n"
    r"- Abstract:\s*\n"
    r"- Key figure:\s*\n"
    r"- Method:\s*\n"
    r"- Dataset/system:\s*\n"
    r"- Failure mode or limitation:\s*\n"
    r"- Reusable idea for SDL6 / automation:\s*",
    flags=re.M,
)


@dataclass
class ExtractedNotes:
    abstract: str
    key_figure: str
    method: str
    dataset_system: str
    limitation: str
    reusable_idea: str
    status: str


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*[\"']?(.+?)[\"']?\s*$", text, flags=re.M)
    return match.group(1).strip() if match else ""


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"(?<=[a-z])-\s+(?=[a-z])", "", text)
    return text.strip()


def sentence_split(text: str) -> list[str]:
    text = clean_text(text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [part.strip() for part in parts if 40 <= len(part.strip()) <= 500]


def first_sentences(text: str, max_sentences: int = 2, max_chars: int = 520) -> str:
    out = []
    for sentence in sentence_split(text):
        out.append(sentence)
        joined = " ".join(out)
        if len(out) >= max_sentences or len(joined) >= max_chars:
            return joined[:max_chars].rstrip()
    return clean_text(text)[:max_chars].rstrip()


def find_section(text: str, heading_patterns: list[str], next_heading_patterns: list[str] | None = None) -> str:
    lower = text.lower()
    starts = []
    for pattern in heading_patterns:
        match = re.search(pattern, lower, flags=re.I)
        if match:
            starts.append(match.end())
    if not starts:
        return ""
    start = min(starts)
    end_candidates = []
    next_patterns = next_heading_patterns or [
        r"\n\s*(?:\d+\.?\s*)?introduction\b",
        r"\n\s*(?:\d+\.?\s*)?methods?\b",
        r"\n\s*(?:\d+\.?\s*)?materials and methods\b",
        r"\n\s*(?:\d+\.?\s*)?results?\b",
        r"\n\s*(?:\d+\.?\s*)?discussion\b",
        r"\n\s*(?:\d+\.?\s*)?conclusions?\b",
        r"\n\s*(?:\d+\.?\s*)?references\b",
    ]
    for pattern in next_patterns:
        match = re.search(pattern, lower[start:], flags=re.I)
        if match and match.start() > 100:
            end_candidates.append(start + match.start())
    end = min(end_candidates) if end_candidates else min(len(text), start + 3500)
    return text[start:end]


def extract_abstract(text: str) -> str:
    section = find_section(
        text,
        [r"\n\s*abstract\s*\n", r"\n\s*summary\s*\n"],
        [r"\n\s*(?:keywords|introduction|1\.?\s*introduction|background)\b"],
    )
    return first_sentences(section, 3, 700) if section else "Needs manual review: abstract not found in extracted text."


def extract_method(text: str) -> str:
    section = find_section(
        text,
        [r"\n\s*(?:materials and methods|methods?|methodology|experimental|experimental section)\s*\n"],
        [r"\n\s*(?:results?|discussion|conclusions?|references)\b"],
    )
    if section:
        return first_sentences(section, 2, 420)
    lowered = text.lower()
    if "bayesian optimization" in lowered:
        return "Uses Bayesian optimization or model-guided search; confirm details from the methods section."
    if "agent" in lowered and ("tool" in lowered or "workflow" in lowered):
        return "Describes an agentic workflow involving tools or task orchestration; confirm implementation details manually."
    if "segmentation" in lowered or "image analysis" in lowered:
        return "Uses image analysis or segmentation methods; confirm model architecture and evaluation details manually."
    return "Needs manual review: method section not found in extracted text."


def extract_dataset_system(text: str, title: str) -> str:
    sentences = sentence_split(text[:12000])
    keywords = ("dataset", "data set", "benchmark", "system", "platform", "cell", "organoid", "microfluidic", "robot", "agent", "model")
    for sentence in sentences:
        lower = sentence.lower()
        if any(keyword in lower for keyword in keywords):
            return sentence[:420]
    return f"Needs manual review: dataset or system details were not obvious from extracted text for '{title}'."


def extract_limitation(text: str) -> str:
    sentences = sentence_split(text)
    keywords = ("limitation", "limited", "challenge", "future work", "not yet", "however", "constraint", "bottleneck")
    for sentence in sentences:
        lower = sentence.lower()
        if any(keyword in lower for keyword in keywords):
            return sentence[:420]
    return "Needs manual review: limitation not obvious from extracted text."


def reusable_idea(text: str, concepts: list[str]) -> str:
    lower = text.lower()
    if "self-driving" in lower or "closed-loop" in lower or "bayesian optimization" in lower:
        return "Use the paper's loop structure as a candidate pattern for experiment planning, execution, measurement, and model-guided next-step selection."
    if "agent" in lower:
        return "Extract the tool-orchestration pattern as a candidate design for automated research workflows."
    if "segmentation" in lower or "image" in lower:
        return "Adapt the measurement or image-analysis pipeline as a reusable assay readout component for automated experiments."
    if "microfluidic" in lower or "organ-on" in lower or "organoid" in lower:
        return "Treat the biological platform as a candidate automated experimental system; verify controllable inputs, readouts, and failure points."
    if concepts:
        return f"Relate this paper to {', '.join(concepts[:3])}; extract reusable workflow details during manual review."
    return "Needs manual review: reusable automation idea not obvious from extracted text."


def key_figure(text: str) -> str:
    for match in re.finditer(r"(figure|fig\.?)\s+(\d+[a-z]?)", text, flags=re.I):
        start = max(0, match.start() - 160)
        end = min(len(text), match.end() + 300)
        snippet = clean_text(text[start:end])
        if 50 <= len(snippet) <= 500:
            return snippet
    return "Needs manual review: key figure not identified from extracted text."


def parse_topics(text: str) -> list[str]:
    match = re.search(r"^topics:\s*\n((?:\s+- .+\n)+)", text, flags=re.M)
    if not match:
        return []
    return [line.strip()[2:].strip().strip('"') for line in match.group(1).splitlines()]


def extract_notes(note_text: str, title: str, pdf_path: Path) -> ExtractedNotes:
    if not pdf_path.exists():
        return ExtractedNotes(
            "Needs manual review: source PDF is missing.",
            "Needs manual review: source PDF is missing.",
            "Needs manual review: source PDF is missing.",
            "Needs manual review: source PDF is missing.",
            "Needs manual review: source PDF is missing.",
            "Needs manual review: source PDF is missing.",
            "missing_pdf",
        )
    try:
        text = extract_text(str(pdf_path), maxpages=8)
    except Exception as exc:
        return ExtractedNotes(
            f"Needs manual review: PDF text extraction failed ({exc}).",
            "Needs manual review: PDF text extraction failed.",
            "Needs manual review: PDF text extraction failed.",
            "Needs manual review: PDF text extraction failed.",
            "Needs manual review: PDF text extraction failed.",
            "Needs manual review: PDF text extraction failed.",
            "extract_failed",
        )
    if len(clean_text(text)) < 500:
        return ExtractedNotes(
            "Needs manual review: extracted text was too short to summarize reliably.",
            "Needs manual review: extracted text was too short.",
            "Needs manual review: extracted text was too short.",
            "Needs manual review: extracted text was too short.",
            "Needs manual review: extracted text was too short.",
            "Needs manual review: extracted text was too short.",
            "too_short",
        )
    topics = parse_topics(note_text)
    return ExtractedNotes(
        extract_abstract(text),
        key_figure(text),
        extract_method(text),
        extract_dataset_system(text, title),
        extract_limitation(text),
        reusable_idea(text, topics),
        "extracted",
    )


def render_reading_notes(notes: ExtractedNotes) -> str:
    return f"""## Reading Notes
- Abstract: {notes.abstract}
- Key figure: {notes.key_figure}
- Method: {notes.method}
- Dataset/system: {notes.dataset_system}
- Failure mode or limitation: {notes.limitation}
- Reusable idea for SDL6 / automation: {notes.reusable_idea}
"""


def update_status(text: str, status: str) -> str:
    return re.sub(r"^status:\s*.+$", f"status: {status}", text, count=1, flags=re.M)


def is_empty_template(text: str) -> bool:
    return bool(READING_TEMPLATE_RE.search(text))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--root", default=str(LIT_ROOT))
    args = parser.parse_args()

    root = Path(args.root)
    papers = sorted((root / "Papers").glob("*.md"), key=lambda p: p.name.lower())
    empty = [path for path in papers if is_empty_template(path.read_text(encoding="utf-8", errors="replace"))]
    if args.limit:
        empty = empty[: args.limit]

    report_rows = []
    changed = []
    for path in empty:
        text = path.read_text(encoding="utf-8", errors="replace")
        source_path = Path(frontmatter_value(text, "source_path"))
        title = re.search(r"^#\s+(.+)$", text, flags=re.M)
        title_text = title.group(1).strip() if title else path.stem
        notes = extract_notes(text, title_text, source_path)
        updated = READING_TEMPLATE_RE.sub(render_reading_notes(notes), text)
        updated = update_status(updated, "reading-notes-extracted" if notes.status == "extracted" else f"needs-review-{notes.status}")
        if updated != text:
            changed.append(path)
            if args.write:
                path.write_text(updated, encoding="utf-8")
        report_rows.append(
            {
                "note": str(path.relative_to(root)),
                "source_path": str(source_path),
                "status": notes.status,
                "abstract": notes.abstract[:180],
            }
        )

    report_path = DATA / "reading_notes_update_report.csv"
    if args.write:
        DATA.mkdir(parents=True, exist_ok=True)
        with report_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["note", "source_path", "status", "abstract"])
            writer.writeheader()
            writer.writerows(report_rows)
        (DATA / "reading_notes_update_report.json").write_text(json.dumps(report_rows, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Root: {root}")
    print(f"Paper notes: {len(papers)}")
    print(f"Empty reading-note templates selected: {len(empty)}")
    print(f"Changed notes: {len(changed)}")
    statuses = {}
    for row in report_rows:
        statuses[row["status"]] = statuses.get(row["status"], 0) + 1
    print(f"Statuses: {statuses}")
    if args.write:
        print(f"Report: {report_path}")
    else:
        print("Dry run only. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
