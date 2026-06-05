#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


EHS_ROOT = Path("/Users/iyakavets/Documents/obsidian/viprorok/EHS Wiki")


@dataclass(frozen=True)
class Section:
    name: str
    links: tuple[str, ...]


@dataclass(frozen=True)
class NoteLinks:
    note: str
    sections: tuple[Section, ...]


def page(name: str) -> str:
    return f"Pages/{name}.md"


def pdf(name: str) -> str:
    return f"PDF Notes/{name}.md"


LINK_MAP = (
    NoteLinks(
        page("Biosafety Manual"),
        (
            Section("Program and governance", ("Biosafety", "Institutional Biosafety Biosecurity Committee", "Biosafety Permits")),
            Section("Roles", ("Biosafety Permit Holder", "Laboratory Users")),
            Section(
                "Core procedures",
                (
                    "Biosafety Training",
                    "Biological Spill Kit",
                    "Biological Spills",
                    "Decontamination",
                    "General Laboratory Safety Practices",
                    "Techniques for Minimizing Aerosols",
                    "Needles and Syringes",
                ),
            ),
            Section(
                "Equipment and materials",
                (
                    "Biosafety Cabinets",
                    "Fume Hoods",
                    "Autoclaves Steam Sterilizers",
                    "Working with Laboratory Animals",
                    "Importation Use and Distribution of Biological materials",
                ),
            ),
            Section("Health and waste", ("Medical Surveillance and Immunoprophylaxis", "Biological Waste Disposal")),
        ),
    ),
    NoteLinks(
        page("Biosafety"),
        (
            Section("Overview", ("Biosafety Manual", "Biosafety Permits", "Biosafety Training")),
            Section("Governance", ("Institutional Biosafety Biosecurity Committee", "Biosafety Permit Holder", "Laboratory Users")),
            Section("Common procedures", ("Biological Spills", "Biological Waste Disposal", "Decontamination")),
        ),
    ),
    NoteLinks(
        page("Biosafety Permits"),
        (
            Section("Roles and governance", ("Biosafety Manual", "Biosafety Permit Holder", "Laboratory Users", "Institutional Biosafety Biosecurity Committee")),
            Section(
                "Forms and guidance",
                (
                    "PDF - Level-1-and-2-Biosafety-Permit-Application",
                    "PDF - Level-1-and-2-Biosafety-Amendment-Application-Form",
                    "PDF - Guide-for-Completing-the-Level-1-and-2-Biosafety-Permit",
                    "PDF - Guide-to-Filling-the-Level-1-and-2-Amendment-July-28",
                ),
            ),
        ),
    ),
    NoteLinks(
        page("Biosafety Permit Holder"),
        (
            Section("Program context", ("Biosafety Manual", "Biosafety Permits", "Institutional Biosafety Biosecurity Committee")),
            Section("Responsibilities", ("Laboratory Users", "Biosafety Training", "General Laboratory Safety Practices")),
            Section("Operational controls", ("Biological Spills", "Decontamination", "Biological Waste Disposal")),
        ),
    ),
    NoteLinks(
        page("Laboratory Users"),
        (
            Section("Program context", ("Biosafety Manual", "Biosafety Permit Holder", "Biosafety Training")),
            Section("Required practices", ("General Laboratory Safety Practices", "Biological Spills", "Decontamination", "Needles and Syringes")),
            Section("Waste and equipment", ("Biological Waste Disposal", "Biosafety Cabinets", "Autoclaves Steam Sterilizers")),
        ),
    ),
    NoteLinks(
        page("Biosafety Training"),
        (
            Section("Program context", ("Biosafety Manual", "Biosafety Permits", "Biosafety Permit Holder", "Laboratory Users")),
            Section("Related training", ("Training Matrix Laboratory Personnel", "Workplace Hazardous Information System WHMIS Training")),
        ),
    ),
    NoteLinks(
        page("Biological Spills"),
        (
            Section("Emergency context", ("Biosafety Manual", "Biological Spill Kit", "Emergency Procedures", "Spill Reporting Procedures")),
            Section("Cleanup controls", ("Decontamination", "Biological Waste Disposal", "Biosafety Cabinets", "Techniques for Minimizing Aerosols")),
            Section("Sharps and exposure", ("Needles and Syringes", "Medical Surveillance and Immunoprophylaxis")),
        ),
    ),
    NoteLinks(
        page("Biological Spill Kit"),
        (
            Section("Emergency context", ("Biological Spills", "Biosafety Manual", "Emergency Procedures")),
            Section("Cleanup controls", ("Decontamination", "Biological Waste Disposal", "Needles and Syringes")),
        ),
    ),
    NoteLinks(
        page("Biological Waste Disposal"),
        (
            Section("Waste context", ("Biosafety Manual", "Laboratory Waste Management", "5.5 Sharp Waste Management", "5.4 Mixed Waste")),
            Section("Treatment and cleanup", ("Decontamination", "Autoclaves Steam Sterilizers", "Biological Spills")),
            Section("PDF procedures", ("PDF - In-Lab-Procedures-for-Biological-Waste-Handling_v3.3", "PDF - UTSC-Biological-Waste-Procedures")),
        ),
    ),
    NoteLinks(
        page("Decontamination"),
        (
            Section("Program context", ("Biosafety Manual", "General Laboratory Safety Practices")),
            Section("Related procedures", ("Biological Spills", "Biological Waste Disposal", "Autoclaves Steam Sterilizers", "Biosafety Cabinets")),
        ),
    ),
    NoteLinks(
        page("General Laboratory Safety Practices"),
        (
            Section("Program context", ("Biosafety Manual", "Laboratory Users", "Biosafety Training")),
            Section("Operational controls", ("Decontamination", "Biological Spills", "Techniques for Minimizing Aerosols", "Needles and Syringes")),
            Section("Equipment", ("Biosafety Cabinets", "Fume Hoods", "Autoclaves Steam Sterilizers")),
        ),
    ),
    NoteLinks(
        page("Biosafety Cabinets"),
        (
            Section("Program context", ("Biosafety Manual", "General Laboratory Safety Practices")),
            Section("Related procedures", ("Biological Spills", "Decontamination", "Techniques for Minimizing Aerosols")),
            Section("PDF guidance", ("PDF - BSC-Failure-or-Alarm-Poster",)),
        ),
    ),
    NoteLinks(
        page("Autoclaves Steam Sterilizers"),
        (
            Section("Program context", ("Biosafety Manual", "Biological Waste Disposal", "Decontamination")),
            Section("PDF guidance", ("PDF - Autoclave-SOP",)),
        ),
    ),
    NoteLinks(
        page("Working with Laboratory Animals"),
        (
            Section("Program context", ("Biosafety Manual", "Biosafety Permits", "Laboratory Users")),
            Section("Exposure response", ("Medical Surveillance and Immunoprophylaxis", "Standard Operating Procedure SOP Bites or Severe Scratches from Research Animals")),
        ),
    ),
    NoteLinks(
        page("Importation Use and Distribution of Biological materials"),
        (
            Section("Program context", ("Biosafety Manual", "Biosafety Permits", "Institutional Biosafety Biosecurity Committee")),
            Section("Related roles", ("Biosafety Permit Holder", "Laboratory Users")),
        ),
    ),
    NoteLinks(
        page("Needles and Syringes"),
        (
            Section("Program context", ("Biosafety Manual", "General Laboratory Safety Practices", "Laboratory Users")),
            Section("Waste and exposure", ("5.5 Sharp Waste Management", "Biological Waste Disposal", "Medical Surveillance and Immunoprophylaxis")),
        ),
    ),
    NoteLinks(
        page("Techniques for Minimizing Aerosols"),
        (
            Section("Program context", ("Biosafety Manual", "General Laboratory Safety Practices")),
            Section("Equipment and spills", ("Biosafety Cabinets", "Biological Spills", "Decontamination")),
            Section("PDF guidance", ("PDF - Safe-Work-Practices-Aerosol-Risk-Reduction-RG2-Biological-Agents",)),
        ),
    ),
    NoteLinks(
        page("Medical Surveillance and Immunoprophylaxis"),
        (
            Section("Program context", ("Biosafety Manual", "Biosafety Permits", "Laboratory Users")),
            Section("Exposure response", ("Biological Spills", "Working with Laboratory Animals", "Needles and Syringes")),
        ),
    ),
    NoteLinks(
        page("Emergency Procedures"),
        (
            Section("Biosafety emergencies", ("Biological Spills", "Biological Spill Kit", "Biosafety Manual", "Medical EmergencyFirst Aid")),
            Section("Related incident procedures", ("Spill Reporting Procedures", "Chemical Spill Procedures", "Mercury Spill Procedures", "Radioactive Material Spill Procedures")),
            Section("Emergency resources", ("Generic Lab Emergency Contact List", "Guide for General Laboratory Spill Kit Contents")),
        ),
    ),
    NoteLinks(
        page("Spill Reporting Procedures"),
        (
            Section("Emergency context", ("Emergency Procedures", "Biological Spills", "Chemical Spill Procedures")),
            Section("Biosafety context", ("Biosafety Manual", "Biological Waste Disposal", "Decontamination")),
        ),
    ),
    NoteLinks(
        page("Generic Lab Emergency Contact List"),
        (
            Section("Emergency context", ("Emergency Procedures", "Biological Spills", "Spill Reporting Procedures")),
            Section("Related resources", ("Biological Spill Kit", "Guide for General Laboratory Spill Kit Contents")),
        ),
    ),
    NoteLinks(
        page("Laboratory Waste Management"),
        (
            Section("Waste program", ("Laboratory Hazardous Waste Management and Disposal Manual", "Biological Waste Disposal", "Chemical Waste Disposal", "Radioactive Waste Disposal")),
            Section("Biosafety waste", ("Biosafety Manual", "Decontamination", "Autoclaves Steam Sterilizers", "5.5 Sharp Waste Management", "5.4 Mixed Waste")),
            Section("Packaging and disposal", ("Summary Guide for Packaging Handling Hazardous Waste", "Waste Minimization")),
        ),
    ),
    NoteLinks(
        page("5.4 Mixed Waste"),
        (
            Section("Waste program", ("Laboratory Waste Management", "Laboratory Hazardous Waste Management and Disposal Manual")),
            Section("Related waste streams", ("Biological Waste Disposal", "Chemical Waste Disposal", "Radioactive Waste Disposal", "5.5 Sharp Waste Management")),
        ),
    ),
    NoteLinks(
        page("5.5 Sharp Waste Management"),
        (
            Section("Waste program", ("Laboratory Waste Management", "Laboratory Hazardous Waste Management and Disposal Manual")),
            Section("Biosafety sharps", ("Needles and Syringes", "Biological Waste Disposal", "Biological Spills")),
        ),
    ),
    NoteLinks(
        page("Summary Guide for Packaging Handling Hazardous Waste"),
        (
            Section("Waste program", ("Laboratory Waste Management", "Laboratory Hazardous Waste Management and Disposal Manual")),
            Section("Waste streams", ("Biological Waste Disposal", "Chemical Waste Disposal", "Radioactive Waste Disposal", "5.4 Mixed Waste", "5.5 Sharp Waste Management")),
        ),
    ),
    NoteLinks(
        page("Vacuum Line Hazards"),
        (
            Section("Program context", ("Biosafety Manual", "General Laboratory Safety Practices", "Techniques for Minimizing Aerosols")),
            Section("Controls", ("Biosafety Cabinets", "Decontamination", "Biological Waste Disposal")),
        ),
    ),
    NoteLinks(
        page("Fume Hoods"),
        (
            Section("Program context", ("Biosafety Manual", "General Laboratory Safety Practices", "Chemical and Lab Safety")),
            Section("Related equipment", ("Biosafety Cabinets", "Vacuum Line Hazards")),
        ),
    ),
    NoteLinks(
        page("Training Matrix Laboratory Personnel"),
        (
            Section("Training context", ("Biosafety Training", "Laboratory Users", "Biosafety Permit Holder")),
            Section("Related programs", ("Biosafety Manual", "Workplace Hazardous Information System WHMIS Training", "First Aid Training")),
            Section("Program references", ("PDF - Laboratory-Safety-Program",)),
        ),
    ),
    NoteLinks(
        page("Institutional Biosafety Biosecurity Committee"),
        (
            Section("Program context", ("Biosafety Manual", "Biosafety", "Biosafety Permits")),
            Section("Roles", ("Biosafety Permit Holder", "Laboratory Users")),
            Section("Materials and oversight", ("Importation Use and Distribution of Biological materials", "Medical Surveillance and Immunoprophylaxis")),
        ),
    ),
    NoteLinks(
        pdf("PDF - Guideline-Operational-Practices-Level-2-Biosafety-Permits"),
        (
            Section("Parent concepts", ("Biosafety Manual", "Biosafety Permits", "Biosafety Permit Holder", "Laboratory Users")),
            Section("Operational practices", ("Biosafety Training", "Decontamination", "Biological Waste Disposal", "General Laboratory Safety Practices")),
            Section("Risk controls", ("Techniques for Minimizing Aerosols", "Biosafety Cabinets", "Medical Surveillance and Immunoprophylaxis")),
        ),
    ),
    NoteLinks(
        pdf("PDF - Guideline-Biosafety-Manual-and-Emergency-Response-Plan-for-Level-1-Permits"),
        (
            Section("Parent concepts", ("Biosafety Manual", "Biosafety Permits", "Biosafety Permit Holder")),
            Section("Emergency planning", ("Biological Spills", "Biological Spill Kit", "Emergency Procedures", "Decontamination")),
        ),
    ),
    NoteLinks(
        pdf("PDF - Guideline-Biosafety-Manual-and-Emergency-Response-Plan-for-Level-2-Permits-1"),
        (
            Section("Parent concepts", ("Biosafety Manual", "Biosafety Permits", "Biosafety Permit Holder")),
            Section("Operational practices", ("Laboratory Users", "Biosafety Training", "General Laboratory Safety Practices", "Decontamination")),
            Section("Emergency planning", ("Biological Spills", "Biological Spill Kit", "Emergency Procedures")),
        ),
    ),
    NoteLinks(
        pdf("PDF - Guide-for-Completing-the-Level-1-and-2-Biosafety-Permit"),
        (
            Section("Parent concepts", ("Biosafety Permits", "Biosafety Permit Holder", "Institutional Biosafety Biosecurity Committee")),
            Section("Related forms", ("PDF - Level-1-and-2-Biosafety-Permit-Application", "PDF - Level-1-and-2-Biosafety-Amendment-Application-Form")),
        ),
    ),
    NoteLinks(
        pdf("PDF - In-Lab-Procedures-for-Biological-Waste-Handling_v3.3"),
        (
            Section("Parent concepts", ("Biological Waste Disposal", "Biosafety Manual", "Decontamination")),
            Section("Related procedures", ("Autoclaves Steam Sterilizers", "Biological Spills", "5.5 Sharp Waste Management")),
        ),
    ),
    NoteLinks(
        pdf("PDF - Safe-Work-Practices-Aerosol-Risk-Reduction-RG2-Biological-Agents"),
        (
            Section("Parent concepts", ("Techniques for Minimizing Aerosols", "General Laboratory Safety Practices", "Biosafety Manual")),
            Section("Controls", ("Biosafety Cabinets", "Biological Spills", "Decontamination")),
        ),
    ),
    NoteLinks(
        pdf("PDF - Lentiviral_Vectors_Guideline_2019"),
        (
            Section("Parent concepts", ("Biosafety Manual", "Biosafety Permits", "Biosafety Cabinets")),
            Section("Operational controls", ("General Laboratory Safety Practices", "Decontamination", "Biological Waste Disposal")),
            Section("Related guidance", ("PDF - Lenti_Containment_Guidance",)),
        ),
    ),
    NoteLinks(
        pdf("PDF - Lenti_Containment_Guidance"),
        (
            Section("Parent concepts", ("Biosafety Manual", "Biosafety Permits", "Biosafety Cabinets")),
            Section("Related guidance", ("PDF - Lentiviral_Vectors_Guideline_2019", "Techniques for Minimizing Aerosols")),
        ),
    ),
    NoteLinks(
        pdf("PDF - SARS-CoV-2-Biosafety-Guideline-for-UofT-Labs_v2.0-Sept-4-2020"),
        (
            Section("Parent concepts", ("Biosafety Manual", "Biosafety Permits", "Biosafety Cabinets")),
            Section("Operational controls", ("General Laboratory Safety Practices", "Decontamination", "Biological Waste Disposal", "Biological Spills")),
        ),
    ),
    NoteLinks(
        pdf("PDF - UTSC-Biological-Waste-Procedures"),
        (
            Section("Parent concepts", ("Biological Waste Disposal", "Biosafety Manual", "Decontamination")),
            Section("Related procedures", ("Autoclaves Steam Sterilizers", "Biological Spills")),
        ),
    ),
)


def all_note_stems(root: Path) -> set[str]:
    return {path.stem for path in root.glob("**/*.md")}


def render_semantic_links(note_links: NoteLinks) -> str:
    lines = ["## Semantic Links", ""]
    for section in note_links.sections:
        lines.append(f"### {section.name}")
        for link in section.links:
            lines.append(f"- [[{link}]]")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def strip_existing_semantic_links(text: str) -> str:
    pattern = re.compile(r"\n*## Semantic Links\n.*?(?=\n## |\npost navigation|\nfont-size|\Z)", flags=re.S)
    return pattern.sub("\n", text).rstrip() + "\n"


def insertion_index(text: str) -> int:
    markers = ["\npost navigation", "\nfont-size"]
    indexes = [text.find(marker) for marker in markers if text.find(marker) != -1]
    return min(indexes) if indexes else len(text)


def update_note(path: Path, note_links: NoteLinks) -> tuple[bool, str]:
    original = path.read_text(encoding="utf-8", errors="replace")
    text = strip_existing_semantic_links(original)
    section = "\n" + render_semantic_links(note_links)
    idx = insertion_index(text)
    updated = text[:idx].rstrip() + "\n\n" + section + text[idx:].lstrip("\n")
    return updated != original, updated


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write semantic links. Default is dry-run.")
    parser.add_argument("--root", default=str(EHS_ROOT))
    args = parser.parse_args()

    root = Path(args.root)

    stems = all_note_stems(root)
    missing_targets = []
    missing_notes = []
    changed = []

    for item in LINK_MAP:
        path = root / item.note
        if not path.exists():
            missing_notes.append(item.note)
            continue
        for section in item.sections:
            for link in section.links:
                if link not in stems:
                    missing_targets.append((item.note, link))
        did_change, updated = update_note(path, item)
        if did_change:
            changed.append(item.note)
            if args.write:
                path.write_text(updated, encoding="utf-8")

    print(f"Root: {root}")
    print(f"Mapped notes: {len(LINK_MAP)}")
    print(f"Notes changed: {len(changed)}")
    for note in changed:
        print(f"  changed: {note}")
    print(f"Missing mapped notes: {len(missing_notes)}")
    for note in missing_notes:
        print(f"  missing note: {note}")
    print(f"Missing link targets: {len(missing_targets)}")
    for note, target in missing_targets:
        print(f"  missing target from {note}: [[{target}]]")
    if not args.write:
        print("Dry run only. Re-run with --write to apply.")
    return 1 if missing_notes or missing_targets else 0


if __name__ == "__main__":
    raise SystemExit(main())
