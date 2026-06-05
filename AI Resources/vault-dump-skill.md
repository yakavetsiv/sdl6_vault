---
name: vault-dump
description: >
  Full session wrapper for any Claude Code session — code repos, grants, scripts,
  LaTeX, or literature work. On start (optional): runs graphify on code repos and
  wiki-ingest on key docs to build context. On end: dumps session to Obsidian vault,
  re-indexes knowledge graph, rebuilds Quartz, and pushes all changes to
  https://github.com/yakavetsiv/sdl6_vault.git.
  
  Two modes:
  - START: "open session", "start project", "graphify this", "ingest this repo"
  - END: "dump session", "save to vault", "commit vault", "push vault", "wrap up", "end session"
  
  Also trigger END mode proactively at the end of any session involving file creation,
  grant writing, literature review, LaTeX editing, or code work.
---

# vault-dump

Full session wrapper. START mode builds context from a repo or docs folder.
END mode saves session to vault, re-indexes, rebuilds site, and pushes to git.

## Vault
`/Users/iyakavets/Documents/obsidian/viprorok`

---

# START MODE — Open a repo or project

Run when user opens a new repo, script folder, or LaTeX project.

## START Step 1 — Graphify the repo

If the current working directory is a code/LaTeX/script repo (not the vault):

```bash
# Check if graphify-out/ already exists (skip if already indexed)
ls graphify-out/ 2>/dev/null && echo "already indexed" || echo "needs indexing"
```

If not yet indexed, invoke the `graphify` skill on the current directory.
Graphify creates `graphify-out/` with a persistent knowledge graph of the codebase.
Report: what the repo does, key files, structure summary.

## START Step 2 — Wiki-ingest key docs

Invoke `wiki-ingest` on:
- `README.md` if present
- Any `.md` docs in the repo
- Key source files the user mentions

This files the repo context into the vault as structured notes under `GitHub/REPO-NAME/`.

## START Step 3 — Create GitHub vault note (if not exists)

Create `GitHub/REPO-NAME.md` with repo metadata (see END Step 4 format).
Link to graphify output and ingested docs.

---

# END MODE — Save session and push

Run at end of any session.

## END Step 1 — Gather session context

Run these in parallel:

```bash
# Date
date +%Y-%m-%d

# Recent files modified in vault (last 4 hours)
find /Users/iyakavets/Documents/obsidian/viprorok -name "*.md" \
  -newer /tmp/.vault_session_marker 2>/dev/null \
  | grep -v ".obsidian" | sort

# Git status of any active repos (if in a git project)
git status --short 2>/dev/null | head -30

# Git log of today's commits
git log --oneline --since="12 hours ago" 2>/dev/null | head -10

# Any GitHub repos referenced (from recent bash history)
gh repo list --limit 5 2>/dev/null
```

Also:
- Note which skills were invoked this session (visible in conversation)
- Note what files were created/written via Write tool
- Note what docs/grants/papers were worked on

---

## END Step 2 — Identify active project(s)

Scan the conversation for project signals:
- Folder names created in vault (e.g. `SDL6 - HOM`)
- YAML `project:` frontmatter in files written
- Grant names, paper titles, or repo names discussed

Common projects and their MOC paths:
| Project | MOC/README path |
|---|---|
| SDL6-HOM | `SDL6 - HOM/Grants/CFI 2024/README.md` |
| Literature | `Literature Wiki/Literature Wiki Home.md` |
| EHS | `EHS Wiki/` |

---

## END Step 3 — Build the daily note

**Path:** `Daily/YYYY-MM-DD.md`  
Create if not exists; append if exists.

```markdown
---
title: Session — YYYY-MM-DD
date: YYYY-MM-DD
project: [list active projects]
tags:
  - daily
  - session-dump
  - [project tags]
---

# Session — YYYY-MM-DD HH:MM

## Summary
[2-3 sentence summary of what was accomplished this session]

## Files Created / Modified
[List as wikilinks for vault files, plain paths for external files]
- [[FileName]] — brief description
- `/path/to/external/file.md` — brief description

## Key Decisions
- [Decision or output 1]
- [Decision or output 2]

## Skills Used
- [skill-name]: [what it did]

## GitHub Repos Referenced
- [[GitHub/repo-name]] — [description]

## Project Links
- [[Project MOC or README]]

---
```

If the daily note already exists, append a new `## Session — HH:MM` section rather than overwriting.

---

## END Step 4 — GitHub repo notes (if repos referenced)

For each GitHub repo mentioned in the session:

```bash
gh repo view OWNER/REPO --json name,description,url,repositoryTopics,primaryLanguage,updatedAt
```

Create or update `GitHub/REPO-NAME.md`:

```markdown
---
title: REPO-NAME
date: YYYY-MM-DD
type: github-repo
tags:
  - github
  - [topics from repo]
---

# REPO-NAME

**URL:** https://github.com/OWNER/REPO  
**Language:** [primaryLanguage]  
**Topics:** [repositoryTopics]  
**Last updated:** [updatedAt]

## Description
[repo description]

## Sessions
- [[Daily/YYYY-MM-DD]] — [what was done with this repo]

## Related Notes
[wikilinks to any vault notes that reference this repo]
```

If the file exists, append to the `## Sessions` section only.

---

## END Step 5 — Update project MOC/README

For each active project, append a one-line session log entry to its MOC or README under a `## Session Log` section (create the section if absent):

```markdown
## Session Log
- **YYYY-MM-DD** — [[Daily/YYYY-MM-DD]]: [one-line summary of what was done]
```

Use Edit tool to append; never overwrite existing content.

---

## END Step 6 — Create daily folder if needed

```bash
mkdir -p /Users/iyakavets/Documents/obsidian/viprorok/Daily
mkdir -p /Users/iyakavets/Documents/obsidian/viprorok/GitHub
```

---

## END Step 7 — Re-index knowledge graph

Run after vault notes are written, before git commit.

```bash
cd /Users/iyakavets/Documents/knowledge-graph && \
  KG_VAULT_PATH="/Users/iyakavets/Documents/obsidian/viprorok" \
  npx tsx src/cli/index.ts index 2>/dev/null | tail -3
```

Report: nodes indexed, edges indexed, communities detected.

---

## END Step 8 — Rebuild Quartz site

```bash
cd /Users/iyakavets/Documents/quartz-vault && npx quartz build 2>&1 | tail -3
```

Preview locally (optional, don't block on this):
```bash
npx quartz serve
# → localhost:8080
```

---

## END Step 9 — Git commit and push all vault changes

This step always runs last, after all notes are written.

```bash
cd /Users/iyakavets/Documents/obsidian/viprorok

# Stage all new and modified files
git add -A

# Check if anything to commit
git diff --cached --quiet && echo "nothing to commit" && exit 0

# Build commit message from session context
# Format: "vault: YYYY-MM-DD — [project] [brief summary]"
# Example: "vault: 2026-06-04 — SDL6-HOM CFI equipment justification + vault setup"

git commit -m "vault: YYYY-MM-DD — [project] [one-line summary of session]"

# Push to origin main
git push origin main
```

Report the commit hash and number of files committed.

If push fails due to remote changes:
```bash
git pull --rebase origin main && git push origin main
```

---

## Output

Tell the user:
- Path to daily note created/updated
- List of vault files committed (count + key filenames)
- Git commit hash + push confirmation
- Knowledge graph: nodes indexed
- Quartz: files built
- If >10 files added this session, suggest running `/wiki-lint`

Keep it brief — one confirmation block.

---

## Notes

- Never overwrite existing daily note content — always append
- Wikilinks use filename without extension and without path: `[[FileName]]`
- If no GitHub repos were referenced, skip Step 4
- If no project is detected, still create the daily note — just omit project links
- Commit message should be meaningful — summarize the session work, not just "update"
- Touch `/tmp/.vault_session_marker` after push so next session detects new files:
  `touch /tmp/.vault_session_marker`
- If git push requires auth, tell user to run: `gh auth login` or set up SSH key
