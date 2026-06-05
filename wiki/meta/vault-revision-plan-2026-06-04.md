---
title: Vault Revision Plan 2026-06-04
date: 2026-06-04
type: meta
tags:
  - meta
  - revision
  - vault
  - type/reference
status: active
---

# Vault Revision Plan — 2026-06-04

## Current State

| Section | Files | Untyped | Orphans | Notes |
|---|---|---|---|---|
| EHS Wiki | 369 | 0 | 71 | Mature, well-tagged. Isolated — no cross-links |
| Literature Wiki | 276 | 106 | 4 | Good links internally. 106 untyped papers |
| ExNode Bibliography | 66 | 11 | 44 | 44 orphans — duplicate of Lit Wiki, underlinked |
| AI Resources | 32 | 3 | 7 | Skills + tools. 4 GitHub notes all orphaned |
| SDL6-HOM | 8 | 0 | 0 | Clean. Linked to lit. Project coverage good |
| GitHub | 4 | 0 | 4 | All 4 notes orphaned — nothing links to them |
| Daily | 1 | 1 | 1 | Missing frontmatter type |
| Root misc | 4 | 4 | 4 | Scratch files, no structure |

**Total: 763 files | 497 tagged | 136 orphans | 127 untyped**

---

## Revision Plan by Priority

### P1 — IMMEDIATE (this session or next)

#### 1. Fix GitHub notes — all 4 orphaned
All `GitHub/` notes have 0 incoming links. Nothing in vault points to them.
**Tool:** Add wikilinks from Daily notes and SDL6/AI Resources notes.
- `[[GitHub/LH_BO_Preprint]]` → link from Daily/2026-06-04.md ✓ (already there)
- `[[GitHub/VibeCount]]` → link from Daily/2026-06-04.md ✓ (already there)
- `[[GitHub/obsidian-skills]]` → link from `AI Resources/claude-skills.md`
- `[[GitHub/claude-obsidian]]` → link from `AI Resources/claude-skills.md`
**Fix:** Edit `AI Resources/claude-skills.md` to wikilink both GitHub notes

#### 2. Fix Daily note — missing `type:` frontmatter
`Daily/2026-06-04.md` has no `type:` field.
**Tool:** `obsidian-markdown` / direct Edit
**Fix:** Add `type: daily` to frontmatter

#### 3. Delete or file root scratch files
- `input.md` — empty or scratch
- `notshowninFigure1b.md` — unclear purpose
- `Semantic Scholar PDFs/` — 1 stray `.md`, PDFs gitignored
**Action:** Check content, delete or move to `Archive/`

---

### P2 — SHORT TERM (next 1-2 sessions)

#### 4. Type ExNode Bibliography (11 untyped + 44 orphans)
ExNode is a duplicate bibliography — papers appear in both `ExNode Bibliography/` and `Literature Wiki/`.
**Problem:** 44 ExNode notes are orphaned because nothing links to them; Lit Wiki has the primary copies.
**Tool:** `wiki-lint` to find exact duplicates; `wiki-ingest` to merge
**Plan:**
- Run `wiki-lint` to identify true duplicates vs. unique ExNode entries
- For duplicates: delete ExNode copy, ensure Lit Wiki copy is linked
- For unique entries: add `type: paper-note` frontmatter, link from relevant Map pages
- Long term: consolidate ExNode into Lit Wiki or keep as extraction-index only

#### 5. Type Literature Wiki papers (106 untyped)
Most are `Paper - ...` named notes without `type:` in frontmatter.
**Tool:** Batch script — add `type: literature-note` to all `Paper - *.md` missing type
**Benefit:** Makes Bases queries work (`type = "literature-note"`)

```bash
# Preview count
python3 -c "
import glob, os
for f in glob.glob('/Users/iyakavets/Documents/obsidian/viprorok/Literature Wiki/**/*.md', recursive=True):
    c = open(f,errors='ignore').read()
    if 'type:' not in c[:400] and os.path.basename(f).startswith('Paper'):
        print(f)
" | wc -l
```

#### 6. Create project `LH_BO_Preprint` section in vault
Daily note references `AC-SDL6/LH_BO_Preprint` extensively but no vault section exists.
**Tool:** `wiki-ingest` on repo README + key files
**Plan:** Create `Projects/LH_BO_Preprint/` with:
- README note
- Open TODOs list (from Daily/2026-06-04)
- Link to `GitHub/LH_BO_Preprint`

Same for `VibeCount` — daily note has full session but no project folder.

---

### P3 — MEDIUM TERM (ongoing)

#### 7. Create Obsidian Bases for key views
**Tool:** `obsidian-bases`
Views needed:
- `SDL6-HOM.base` — all `project: SDL6-HOM` notes, grouped by type
- `Literature.base` — all `type: literature-note` or `paper-note`, filterable by tag
- `Daily.base` — all daily notes sorted by date
- `GitHub.base` — all `type: github-repo` notes

#### 8. Run graphify on vault
**Tool:** `graphify`
Run `/graphify /Users/iyakavets/Documents/obsidian/viprorok` to build a cross-section knowledge graph separate from the knowledge-graph MCP. Generates `graphify-out/graph.html` for visual exploration.
Key insight expected: cross-community connections between EHS, Literature, and SDL6 that current link structure misses.

#### 9. Connect EHS Wiki to rest of vault
369 EHS files are completely isolated — 0 cross-links to Literature or SDL6.
**Opportunity:** Biosafety, organ-on-chip cell handling, nanoparticle safety procedures are relevant to SDL6-HOM.
**Tool:** `wiki-query` to find EHS topics overlapping SDL6 work; add wikilinks selectively.

#### 10. Add `project:` frontmatter to LH_BO_Preprint and VibeCount files
Currently only SDL6-HOM has project coverage. Other active projects (LH_BO_Preprint, VibeCount) have no `project:` field anywhere.
**Fix:** When ingesting those repos, set `project: LH_BO_Preprint` / `project: VibeCount`

---

### P4 — MAINTENANCE (recurring)

#### 11. vault-dump after every session
Skill is installed and updated. Run at session end — logs work, re-indexes KG, rebuilds Quartz, pushes to GitHub.

#### 12. wiki-lint after every 10+ file additions
Current lint report: `wiki/meta/lint-report-2026-06-04.md`
Next lint due after ~10 more files added.

#### 13. knowledge-graph re-index after structural vault changes
```bash
cd ~/Documents/knowledge-graph
KG_VAULT_PATH=~/Documents/obsidian/viprorok npx tsx src/cli/index.ts index
```

#### 14. Quartz rebuild for publishing
```bash
cd ~/Documents/quartz-vault && npx quartz build
```
Publish: push `quartz-vault` to a separate GitHub repo with Pages enabled at `yakavetsiv.github.io/sdl6_vault`

---

## Tool Assignment Summary

| Task | Tool |
|---|---|
| Batch frontmatter fixes | `obsidian-markdown` + Bash |
| ExNode dedup + merge | `wiki-lint` + `wiki-ingest` |
| Project sections (LH_BO, VibeCount) | `wiki-ingest` |
| Database views | `obsidian-bases` |
| Cross-section graph | `graphify` |
| Cross-link discovery | `wiki-query` + `knowledge-graph` |
| Session logging | `vault-dump` |
| Health checks | `wiki-lint` |
| Static site | Quartz |

---

## Quick Wins (do right now)

1. Add `type: daily` to `Daily/2026-06-04.md`
2. Link `GitHub/obsidian-skills` and `GitHub/claude-obsidian` from `claude-skills.md`
3. Batch-add `type: literature-note` to ~100 untyped Paper notes
4. Create `Projects/` folder structure for LH_BO_Preprint + VibeCount
