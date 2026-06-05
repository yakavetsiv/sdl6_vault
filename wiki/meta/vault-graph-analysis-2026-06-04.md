---
title: Vault Graph Analysis — 2026-06-04
date: 2026-06-04
type: meta
tags:
  - meta
  - graph
  - analysis
  - organization
status: active
---

# Vault Graph Analysis — 2026-06-04

Based on knowledge-graph MCP (obra/knowledge-graph): 345 communities, 763 nodes.

---

## Critical Structural Findings

### 1. EHS Wiki is a closed island (0 cross-section links)

EHS Wiki has **376 incoming links internally** but **zero outgoing links to any other section**. It is the largest section (369 files) and completely disconnected from Literature, SDL6, Projects.

The graph has no path from SDL6 → EHS even though SDL6 work requires:
- Biosafety cabinets (EHS)
- Nanomaterial handling guidelines (EHS)
- CL2 containment (EHS)

**Fix:** Create `EHS Wiki/SDL6-EHS-Bridge.md` — a connection note linking the 5 most relevant EHS pages to SDL6 work. Then link it from `SDL_access_facility_overview.md`.

---

### 2. Literature Wiki links OUT well but is barely linked TO

`Literature Wiki Home` has **147 outgoing links** (well-connected internally) but only **2 incoming links** from the whole vault (from `Knowledge_Mesh_Wiki` and `Map - AI Tools`). 

276 papers are effectively reachable only if you know to start from Literature Wiki Home. SDL6 notes link to individual papers directly but not to the wiki home — so the graph shows SDL6 and Literature as disconnected despite having 21 cross-links.

**Fix:** Add `[[Literature Wiki Home]]` to SDL6 README and Projects MOCs. One link makes the entire Literature section reachable from SDL6 subgraph.

---

### 3. 336 singleton communities (97% of communities have size=1)

Knowledge graph detected 345 communities; 336 have exactly 1 node. This means most nodes are not densely connected enough for community detection to cluster them — the vault reads as a collection of isolated documents rather than an interconnected knowledge base.

Root cause: most EHS pages link to EHS Topic pages but those topics don't link back. The "hub-and-spoke" pattern (PDF Notes Index has 228 incoming but only routes internally) creates clusters that don't talk to each other.

**Fix:** See below — hub bridge notes.

---

### 4. Paper duplicates with 86 incoming links each

6 papers all have exactly 86 incoming links:
- `Paper - 1-s2.0-S0272884222036471-main`
- `Paper - 10.48550 arxiv.2501.06039`
- `Paper - 1-s2.0-S259025712200030X-main`
- etc.

This uniform count (86 = suspicious) suggests these are referenced from a shared template or batch-ingested with identical links. Investigate: are these all in the same ExNode extraction batch? May be false links from extraction artifacts.

---

### 5. `Map — Nanomedicine SDL` has 26 outgoing links but 0 incoming

The best-connected SDL6 map has no node pointing to it. Nothing in the vault leads a reader here. 

**Fix:** Link from `Literature Wiki Home`, `SDL6 - HOM/README`, and `Projects/` MOC.

---

### 6. Projects section is the most connected (92 cross-links) but lacks a home node

`Projects/` has the highest cross-section connectivity but no `Projects/README.md` or `Projects Home` MOC to serve as entry point. The graph shows Projects nodes pointing everywhere but nothing pointing to Projects.

**Fix:** Create `Projects/README.md` as a MOC linking all active projects.

---

## Improvement Plan

### A. Create Bridge Notes (highest impact)

| File to create | Links | Purpose |
|---|---|---|
| `EHS Wiki/SDL6-EHS-Bridge.md` | Biosafety Manual, Biosafety Cabinets, Nanomaterials, CL2, Cell Culture | Connect EHS to SDL6 |
| `Projects/README.md` | All project READMEs | Entry point for Projects section |

### B. Add Missing Inbound Links

| Target | Add link from | Impact |
|---|---|---|
| `[[Literature Wiki Home]]` | SDL6 README, Projects READMEs, Daily | Makes 276 papers reachable from SDL6 subgraph |
| `[[Map — Nanomedicine SDL]]` | Literature Wiki Home, SDL6 README | Gives map its first inbound link |
| `[[EHS Wiki Home]]` | SDL6 facility overview, Projects README | Makes EHS reachable from work context |

### C. Fix Hub-and-Spoke Deadlock

EHS Topic pages (376 incoming links each) only link to each other. Add outgoing links from EHS Topics to:
- Relevant SDL6 notes (e.g. `EHS Topic - Biosafety` → `SDL_access_facility_overview`)
- Literature papers on cell culture safety

This breaks the island and increases community cohesion.

### D. Investigate 86-link anomaly

Check if 6 papers with identical 86 incoming link counts are extraction artifacts:
```bash
grep -r "Paper - 1-s2.0-S0272884222036471" vault/ExNode Bibliography/ | wc -l
```
If all 86 links come from one ExNode extraction file, those are false edges — clean them.

### E. Add `project:` to Literature Wiki concept notes

`Concept - Organoids`, `Concept - Self-Driving Labs`, `Concept - Lab Automation` are highly connected (31-38 incoming) but have no `project:` field. Tagging them connects them to Bases views.

---

## Graph Health Score

| Metric | Current | Target |
|---|---|---|
| Communities with >1 node | 9 / 345 (2.6%) | >15% |
| Cross-section links (EHS) | 0 | >10 |
| SDL6 subgraph depth-2 nodes | 98 | 150+ |
| `Map — Nanomedicine SDL` incoming | 0 | 3+ |
| Singleton communities | 336 | <250 |

---

## Quick Wins (implement now)

1. Create `Projects/README.md` MOC
2. Add `[[Literature Wiki Home]]` + `[[Map — Nanomedicine SDL]]` + `[[EHS Wiki Home]]` to SDL6 README
3. Create `EHS Wiki/SDL6-EHS-Bridge.md`
4. Add `[[Map — Nanomedicine SDL]]` to `Literature Wiki Home`
