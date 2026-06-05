---
type: meta
title: Lint Report 2026-06-04
created: 2026-06-04
updated: 2026-06-04
tags:
  - meta
  - lint
  - type/reference
  - vault
status: reviewed
---

# Lint Report: 2026-06-04

## Summary
- Pages scanned: 756
- Orphan pages: 247
- Dead wikilinks: 332
- No frontmatter: 23
- No tags: 191
- SDL6 notes with 0 outgoing links: 7 (fixed in this session)
- Relevant lit papers linked to SDL6: 20+

---

## Critical: SDL6 Notes — Zero Outgoing Links (FIXED)
All 7 SDL6 notes had no outgoing wikilinks. Cross-links added to literature and internal notes.

---

## Dead Links (332 total)

**Root cause — two patterns:**

1. **PDF attachment links** (`[[_attachments/...pdf]]`) — Obsidian embed syntax. PDFs tracked by git but path resolution fails. Not broken — Obsidian resolves these natively. Ignore.
2. **_data/markitdown duplicates** (`[[_data/markitdown/Paper - ...]]`) — duplicate index entries. Low priority.
3. **Knowledge_Mesh_Wiki.md** — 3 dead links to stub pages (`[[Codebase Inspection]]`, `[[Structured Notes]]`, `[[Project Scope & Goals]]`). Create stubs or remove.

**Action needed:** Only `Knowledge_Mesh_Wiki.md` dead links require fixing. PDF links are intentional.

---

## Orphans (247 total)

**Root cause — three patterns:**

1. **Literature Wiki papers** (~220) — individual paper notes not linked from any map page. Expected: papers are ingested atomically; Maps pages should link them but don't always.
2. **Root-level files** (`input.md`, `notshowninFigure1b.md`) — scratch files. Delete or file.
3. **Daily/2026-06-04.md** — no inbound links. Expected for daily notes.

**High priority:** Link SDL6-relevant papers to `Map - Biofabrication and Cell Systems` or create a new `Map - Nanomedicine SDL.md`.

---

## Frontmatter Gaps (23 files without any frontmatter)

Most are older Literature Wiki papers ingested before the frontmatter convention. Low priority — batch-add with wiki-ingest.

---

## Missing Cross-References (SDL6 ↔ Literature)

**Fixed this session** — see SDL6 notes for new `## Related Literature` sections.

**Still missing:** Literature papers don't link back to SDL6 notes. Suggest adding `related_projects: [SDL6-HOM]` frontmatter to relevant papers in a future batch pass.

---

## Semantic Tiling
Skipped — ollama not configured. Run `ollama pull nomic-embed-text` to enable.

---

## Recommended Next Actions

| Priority | Action |
|---|---|
| HIGH | Create `Map - Nanomedicine SDL.md` linking all 39 relevant papers |
| HIGH | Batch-add frontmatter to 23 untagged files |
| MED | Fix 3 dead links in `Knowledge_Mesh_Wiki.md` |
| MED | Add `related_projects` frontmatter to relevant lit papers |
| LOW | Clean up root scratch files (`input.md`, `notshowninFigure1b.md`) |
| LOW | Enable semantic tiling via ollama |
