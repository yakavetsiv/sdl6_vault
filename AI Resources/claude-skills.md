---
title: Claude Code Skills
date: 2026-06-04
type: reference
tags:
  - claude-code
  - skills
  - setup
  - AI
project: SDL6-HOM
---

# Claude Code Skills

All agent skills installed for this environment. Install via `npx skills install <source>`.

> [!INFO] Reinstall
> If skills are lost after a system reset: `npx skills install <source>` for each GitHub source below. Custom skills (`vault-dump`) must be recreated manually or restored from vault.

---

## Installed Skills

### kepano/obsidian-skills
**Source:** `npx skills install kepano/obsidian-skills`  
**Install path:** `~/.agents/skills/`

| Skill | Purpose |
|---|---|
| `obsidian-markdown` | Create/edit Obsidian-flavored markdown: wikilinks, callouts, frontmatter |
| `obsidian-bases` | Create `.base` database views with filters, formulas, summaries |
| `obsidian-cli` | Vault operations via CLI: read, write, search, manage notes |
| `json-canvas` | Create/edit `.canvas` files: nodes, edges, visual maps |
| `defuddle` | Strip clutter from web pages → clean markdown |

---

### AgriciDaniel/claude-obsidian
**Source:** `npx skills install AgriciDaniel/claude-obsidian`  
**Install path:** `~/Documents/untitled folder/.agents/skills/`

| Skill | Purpose |
|---|---|
| `wiki` | Full wiki management: setup, scaffold, route to sub-skills |
| `wiki-cli` | Vault transport layer (Obsidian CLI or filesystem fallback) |
| `wiki-fold` | Rollup log entries into meta-pages |
| `wiki-ingest` | Ingest files/URLs into vault as structured notes |
| `wiki-lint` | Vault health check: orphans, dead links, frontmatter gaps |
| `wiki-mode` | Switch wiki editing mode |
| `wiki-query` | Query vault content |
| `wiki-retrieve` | Retrieve notes by context |
| `autoresearch` | Autonomous research loop → files results into wiki |
| `canvas` | Visual layer: add images/notes/PDFs to canvas files |
| `save` | Save conversation/answer to vault as structured note |
| `think` | 10-principle structured thinking loop |
| `defuddle` | Clean web pages (duplicate of kepano version) |
| `obsidian-bases` | Bases views (duplicate) |
| `obsidian-markdown` | Obsidian markdown (duplicate) |

> [!WARNING] Security
> `save` skill flagged High Risk by Snyk — runs with full agent permissions, writes to vault.

---

### safishamsi/graphify
**Source:** `npx skills install safishamsi/graphify`  
**Install path:** `~/Documents/untitled folder/.agents/skills/`

| Skill | Purpose |
|---|---|
| `graphify` | Turn any code folder (Python, R, shell, LaTeX, docs) into a queryable knowledge graph. Creates `graphify-out/` in project. Use for script collections and LaTeX repos. |

**Usage:** Open project folder in Claude Code, then `/graphify` or ask "what does this codebase do?"

---

### Custom: vault-dump
**Source:** Local only — `~/.claude/skills/vault-dump/SKILL.md`  
**Not on GitHub** — recreate from vault if lost.

| Skill | Purpose |
|---|---|
| `vault-dump` | Dump session to Obsidian vault: daily note + GitHub notes + project log + KG re-index + Quartz rebuild + git commit + push to `yakavetsiv/sdl6_vault` |

**Trigger phrases:** "dump session", "save to vault", "commit vault", "push vault", "wrap up"

---

## Tools (non-skill)

### obra/knowledge-graph
**Source:** `git clone https://github.com/obra/knowledge-graph.git ~/Documents/knowledge-graph`  
**Type:** CLI + Claude Code MCP  
**Config:** `KG_VAULT_PATH=/Users/iyakavets/Documents/obsidian/viprorok`

```bash
# Re-index after vault changes
cd ~/Documents/knowledge-graph
KG_VAULT_PATH=~/Documents/obsidian/viprorok npx tsx src/cli/index.ts index

# Search
KG_VAULT_PATH=~/Documents/obsidian/viprorok npx tsx src/cli/index.ts search "your query"
```

MCP registered in `~/.claude.json` — loads automatically in Claude Code sessions.

### Quartz
**Source:** `git clone https://github.com/jackyzha0/quartz.git ~/Documents/quartz-vault`  
**Content:** Symlinked to `~/Documents/obsidian/viprorok`  
**Config:** `quartz.config.yaml` — title "SDL6 Knowledge Base", baseUrl `yakavetsiv.github.io/sdl6_vault`

```bash
cd ~/Documents/quartz-vault
npx quartz build     # build static site → public/
npx quartz serve     # preview at localhost:8080
```

---

## Vault Git Repo
**Remote:** `https://github.com/yakavetsiv/sdl6_vault.git`  
**Branch:** `main`  
**Ignored:** `.obsidian/workspace.json`, `.obsidian/cache`, `EHS Wiki/PDFs/`, `Semantic Scholar PDFs/`, `.DS_Store`

```bash
cd ~/Documents/obsidian/viprorok
git add -A && git commit -m "vault: description" && git push origin main
```
