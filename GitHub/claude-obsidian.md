---
title: claude-obsidian
date: 2026-06-04
type: github-repo
tags:
  - github
  - obsidian
  - agent-skills
  - claude-code
  - PKM
  - knowledge-graph
---

# claude-obsidian

**URL:** https://github.com/AgriciDaniel/claude-obsidian  
**Author:** AgriciDaniel  
**Language:** Python  
**Description:** Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude reads, links, and files it into one connected knowledge graph of plain Markdown you own. AI note-taking, personal knowledge management (PKM), and an open-source Notion alternative. Based on Karpathy's LLM Wiki pattern.

## Skills Provided
| Skill | Purpose |
|---|---|
| `wiki` | Full wiki management |
| `wiki-cli` | CLI vault operations |
| `wiki-fold` | Fold/collapse content |
| `wiki-ingest` | Ingest external content into vault |
| `wiki-lint` | Lint vault notes |
| `wiki-mode` | Switch wiki editing mode |
| `wiki-query` | Query vault content |
| `wiki-retrieve` | Retrieve notes by context |
| `autoresearch` | Auto research + save to vault |
| `canvas` | Canvas/visual map management |
| `save` | Save content to vault |
| `think` | Reasoning step |
| `defuddle` | Clean markdown extraction |
| `obsidian-bases` | Database views |
| `obsidian-markdown` | Obsidian syntax |

> [!WARNING] Security Note
> `save` skill flagged High Risk by Snyk. Runs with full agent permissions — writes to vault. Use with awareness.

## Installation
```bash
npx skills install AgriciDaniel/claude-obsidian
```

## Sessions
- [[Daily/2026-06-04]] — Installed all 15 skills; used for SDL6 vault analysis and improvements
