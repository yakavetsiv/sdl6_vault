---
name: vault-dump
description: >
  Full session wrapper for any Claude Code session — code repos, grants, scripts,
  LaTeX, or literature work. START mode: graphify + wiki-ingest on repo. END mode:
  daily note, GitHub notes, project log, KG re-index, Quartz rebuild, git push to
  https://github.com/yakavetsiv/sdl6_vault.git. Enforces YAML frontmatter rules.
  Trigger START: "open session", "start project", "graphify this".
  Trigger END: "dump session", "save to vault", "commit vault", "wrap up", "end session".
  Also trigger END proactively at end of any session with file creation, grant writing,
  literature review, LaTeX editing, or code work.
---

# vault-dump

## Vault
`/Users/iyakavets/Documents/obsidian/viprorok`  
**Git remote:** `https://github.com/yakavetsiv/sdl6_vault.git` (branch: `main`)

---

## YAML Frontmatter Rules (enforce on every new/edited file)

These rules prevent Quartz build failures. Apply when writing any vault note.

```yaml
# CORRECT — block list format
tags:
  - sdl6
  - type/paper

# WRONG — inline list (breaks Quartz YAML parser)
tags:   - sdl6   - type/paper

# WRONG — duplicate keys (breaks Quartz)
tags:
  - sdl6
tags:
  - type/paper
```

**Rules:**
- Tags always as block list: `tags:\n  - value`
- No duplicate frontmatter keys — merge into one block
- No `key:   - value` inline list syntax
- All files need: `title`, `date`, `type`, `tags`

---

## Vault Structure

```
viprorok/
├── Daily/              ← daily session notes (type: daily)
├── GitHub/             ← repo notes (type: github-repo)
├── Projects/           ← active project MOCs
│   ├── README.md       ← Projects MOC (entry point)
│   ├── LH_BO_Preprint/
│   ├── VibeCount/
│   ├── Lab Sensor/
│   └── UofT EHS Biosafety Benchmark/
├── SDL6 - HOM/         ← SDL6 project core
│   ├── Grants/CFI 2024/README.md  ← SDL6 grant MOC
│   └── Reproducibility ML Study/
├── Literature Wiki/    ← research papers + concepts + maps
├── EHS Wiki/           ← safety/compliance (369 files)
├── ExNode Bibliography/ ← extraction indexes
├── AI Resources/       ← tools, skills, style guides
│   └── Skills/         ← Claude Code skill files
├── wiki/meta/          ← lint reports, revision plans, graph analysis
├── graphify-out/       ← semantic graph (excluded from Quartz)
└── Daily/Daily.base    ← Bases views
```

## Active Projects

| Project | MOC path | project: tag |
|---|---|---|
| SDL6-HOM grant | `SDL6 - HOM/Grants/CFI 2024/README.md` | `project/sdl6-hom` |
| ML Reproducibility | `SDL6 - HOM/Reproducibility ML Study/ML Cell Counting Reproducibility Study.md` | `project/sdl6-hom` |
| LH_BO_Preprint | `Projects/LH_BO_Preprint/README.md` | `project/lh-bo-preprint` |
| VibeCount | `Projects/VibeCount/README.md` | `project/vibecount` |
| Lab Sensor | `Projects/Lab Sensor/README.md` | `project/lab-sensor` |
| UofT EHS Benchmark | `Projects/UofT EHS Biosafety Benchmark/UofT EHS Biosafety Benchmark.md` | `project/ehs-benchmark` |

## Tag Taxonomy

```
sdl6, sdl6/cfi, sdl6/nanomedicine, sdl6/organ-on-chip, sdl6/automation
literature, type/paper, type/concept, type/map
lit/sdl, lit/nanomedicine, lit/biofabrication, lit/ai-methods, lit/digital-discovery
ehs, ehs/biosafety, ehs/chemical-safety, ehs/laboratory-operations
ai, type/skill, type/reference, type/github-repo, type/index, type/daily, type/okr, type/output, type/source
project, project/sdl6-hom, project/lh-bo-preprint, project/vibecount, project/ehs-benchmark, project/lab-sensor
```

---

# START MODE — Open a repo or project

## START Step 1 — Graphify the repo

```bash
ls graphify-out/ 2>/dev/null && echo "already indexed" || echo "needs indexing"
```

If not indexed: invoke `graphify` skill on current directory.  
Report: repo purpose, key files, structure summary.

## START Step 2 — Wiki-ingest key docs

Invoke `wiki-ingest` on README.md + any .md docs + key source files.  
Files go to `GitHub/REPO-NAME/` in vault.

## START Step 3 — Create GitHub vault note

Create `GitHub/REPO-NAME.md` with frontmatter:
```yaml
---
title: REPO-NAME
date: YYYY-MM-DD
type: github-repo
tags:
  - type/github-repo
  - github
  - [relevant project tag]
---
```

---

# END MODE — Save session and push

## END Step 1 — Gather session context

```bash
date +%Y-%m-%d
find /Users/iyakavets/Documents/obsidian/viprorok -name "*.md" \
  -newer /tmp/.vault_session_marker 2>/dev/null | grep -v ".obsidian" | sort
git status --short 2>/dev/null | head -20
git log --oneline --since="12 hours ago" 2>/dev/null | head -10
```

Also note: skills invoked, files written via Write tool, docs/grants/papers worked on.

---

## END Step 2 — Identify active project(s)

Scan conversation for: folder names, `project:` frontmatter, grant/paper/repo names.  
Match against Projects table above.

---

## END Step 3 — Build the daily note

**Path:** `Daily/YYYY-MM-DD.md` — append if exists, create if not.

```markdown
---
title: "Session — YYYY-MM-DD"
date: YYYY-MM-DD
type: daily
project:
  - [active projects]
tags:
  - type/daily
  - session-dump
  - [project tags]
---

# Session — YYYY-MM-DD HH:MM

## Summary
[2-3 sentences]

## Files Created / Modified
- [[FileName]] — description
- `/external/path.md` — description

## Key Decisions
- [decision]

## Skills Used
- `skill-name`: what it did

## GitHub Repos Referenced
- [[GitHub/repo-name]] — description

## Project Links
- [[Projects/README]]
```

---

## END Step 4 — GitHub repo notes

```bash
gh repo view OWNER/REPO --json name,description,url,repositoryTopics,primaryLanguage,updatedAt \
  2>/dev/null || curl -s "https://api.github.com/repos/OWNER/REPO" | python3 -c "..."
```

Create `GitHub/REPO-NAME.md` or append `## Sessions` entry. Use YAML rules above.

---

## END Step 5 — Update project MOC

Append to `## Session Log` in the active project's MOC/README:
```markdown
- **YYYY-MM-DD** — [[Daily/YYYY-MM-DD]]: one-line summary
```

Also update `Projects/README.md` session log if new project work.

---

## END Step 6 — Ensure folders exist

```bash
mkdir -p /Users/iyakavets/Documents/obsidian/viprorok/Daily
mkdir -p /Users/iyakavets/Documents/obsidian/viprorok/GitHub
mkdir -p /Users/iyakavets/Documents/obsidian/viprorok/wiki/meta
```

---

## END Step 7 — Re-index knowledge graph

```bash
cd /Users/iyakavets/Documents/knowledge-graph && \
  KG_VAULT_PATH="/Users/iyakavets/Documents/obsidian/viprorok" \
  npx tsx src/cli/index.ts index 2>/dev/null | tail -3
```

---

## END Step 8 — Rebuild Quartz

```bash
cd /Users/iyakavets/Documents/quartz-vault && npx quartz build 2>&1 | grep -E "Done|Error|Emitted" | tail -3
```

If Quartz errors with YAML parse failure: check the failing file for duplicate keys or inline list syntax (`key:   - value`). Fix and retry.

---

## END Step 9 — Git commit and push

```bash
cd /Users/iyakavets/Documents/obsidian/viprorok

# Exclude .obsidian plugins from staging (large files, not needed)
git add -A
git reset HEAD '.obsidian/plugins/*' 2>/dev/null || true

git diff --cached --quiet && echo "nothing to commit" && exit 0
git commit -m "vault: YYYY-MM-DD — [project] [one-line summary]"
git push origin main
```

On push failure: `git pull --rebase origin main && git push origin main`

---

## Output

Report:
- Daily note path
- Files committed (count + key names)  
- Git commit hash
- KG: communities detected
- Quartz: files emitted
- Suggest `/wiki-lint` if >10 files added

---

## Notes

- Never overwrite existing daily note — always append
- Wikilinks: `[[FileName]]` without path or extension
- `graphify-out/` is excluded from Quartz via `quartz.config.yaml` — do not add files there expecting them to publish
- `.obsidian/plugins/` should NOT be committed — reset from staging if accidentally added
- Session marker: `touch /tmp/.vault_session_marker` after push
- Auth issues: `gh auth login` or set up SSH key
