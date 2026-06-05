---
type: concept
title: "LabSense Paper Writing Style Profile"
created: 2026-06-04
updated: 2026-06-04
tags:
  - writing-style
  - scientific-writing
  - tutorial-paper
  - digital-discovery
  - deslop
  - SDL
status: active
related:
  - "[[Digital Discovery Tutorial Paper Writing Guide]]"
  - "[[Map - Digital Discovery Tutorial Papers]]"
project: lab_sensor
author: Ilya Yakavets
repo: yakavetsiv/lab_sensor
---

# LabSense Paper Writing Style Profile

Derived from editing `includes/include-body.tex` and `includes/include-abstract.tex` in the LabSense tutorial paper (targeting *Digital Discovery*, RSC, Tutorial Review format). Apply this profile when revising or continuing the manuscript.

---

## Voice and Register

- **Audience**: experimentalists (graduate students, postdocs, research engineers) with basic Python/CLI experience but new to embedded hardware, MQTT, or CV. Not software engineers; not pure biologists.
- **Tone**: precise, instrument-panel density. Purposeful. Not warm, not cold. The PRODUCT.md "well-calibrated instrument" framing applies.
- **Person**: first person plural ("we deployed", "we describe"). Avoid passive where possible.
- **Tense**: present for general claims and system descriptions; past for specific deployment events ("the classifier achieved 96.5%").
- **Register**: formal but not stiff. Tutorial sections use imperative for instructions ("Run", "Edit", "Confirm"). Result sections use declarative present.

---

## Deslop Rules (Applied)

All of these were actively caught and removed during this session:

### Banned patterns
| Pattern | Replace with |
|---------|-------------|
| `---` (em dash in prose) | parentheses, comma, semicolon, or colon |
| "This section provides..." | Cut; lead with the action |
| "This tutorial has provided..." | Cut meta-commentary; state the result directly |
| "Here we provide a structured..." | Cut; lead with what each tier does |
| "robust" | "reliable" |
| "despite growing recognition" | Cut; state the gap directly |
| "it is important to note" | Cut entirely |
| "A design decision central to this tutorial is the use of..." | "LabSense uses X as..." |
| "This homogeneous messaging model has three practical consequences" | "Three practical consequences follow" |
| Throat-clearing section openers ("In this section, we will...") | Cut; lead with substance |
| Duplicate sentences (same claim stated twice in adjacent paragraphs) | Remove second occurrence |
| Analogy filler ("This is analogous to...") | Cut if it adds no information |
| "is provided in Table X" (passive) | "Table X shows / situates / lists" |

### Em dash replacement guide
- **Parenthetical `X---appositive---Y`** → `X (appositive) Y`
- **List introduction `X---list`** → `X: list`
- **Single `X---continuation`** → `X, continuation` or `X; continuation`
- **Keep**: table `---` cells (N/A notation), `\subsection{Step N --- Name}` headers

### Allowed modifiers
- "structured" (as adjective for deployment recipes) — OK
- "step-by-step" — OK in tutorial context
- "practical" — OK sparingly

---

## Sentence Patterns

**Preferred:**
- Short declarative subject-verb-object: "LabSense uses MQTT as its universal messaging layer."
- Colon introduction for lists: "Three consequences follow for lab deployments:"
- Fact + implication structure: "The tank was empty during deployment. This pattern (stable near-zero readings with low variance) is qualitatively distinct from pipeline failure."
- Imperative for tutorial steps: "Run `mosquitto_sub -h...` from a laptop; confirm no timeout."
- Parenthetical for clarification: "Camera nodes (PoECAM-W) stream video over RTSP to Frigate NVR."

**Avoided:**
- Uniform paragraph lengths (vary 2–8 sentences)
- Starting multiple consecutive sentences with "The"
- Stacking three or more prepositional phrases

---

## Domain Vocabulary

Exact terms to use consistently throughout:

| Concept | Canonical term |
|---------|---------------|
| Physical-state sensing | physical-state sensing (hyphenated) |
| Self-driving lab | self-driving laboratory (SDL) |
| Three tiers | environmental tier / camera tier / instrument-state tier |
| MQTT topics | `labsense/env/<node_id>/data`, `labsense/camera/<node_id>/data`, `labsense/instrument/<id>/state` |
| Video bridge | Frigate NVR |
| CV inference orchestration | Prefect Camera Analysis |
| Validation step | Pydantic schema validation |
| Time-series DB | TimescaleDB (single source of truth) |
| Alert engine | n8n Alert Engine |
| Automation flows | SDL Flows / Prefect SDL Flows |
| LN2 level | LN\textsubscript{2} bar level (0–8) |
| CO2 gauge | CO\textsubscript{2} cylinder gauge |
| Carrier states | `no-tray` / `tray` / `tray+well` |
| Instrument vendor spelling | Thermo Fisher (Cytomat), BioTek/Agilent (Cytation), Inheco (ODTC) |
| User cost | under $130 CAD per environmental node; $60 CAD per camera node |
| Deployment period | 2026-05-24 to 2026-05-31 |
| Total readings | 280,525 |

---

## Digital Discovery Tutorial Review Format

Based on analysis of `gaidimas2026_computer_vision_materials_synthesis` and RSC format:

### Abstract (5-move structure, ~150 words)
1. **Field context** (1–2 sentences): what SDLs do + assumption they make
2. **Gap** (1 sentence): "No practical guide exists for X"
3. **Tutorial promise** (2–3 sentences): what this tutorial describes (3 tiers, recipe format)
4. **Case study result** (1 sentence): 7-day deployment, 280k readings, specific events detected
5. **Availability** (1 sentence): cost + open source + GitHub URL

### Section structure (LabSense)
1. Introduction (field acceleration → bottleneck → what tutorial provides → reusable artifacts)
2. Conceptual Framework (define physical-state sensing → 3-tier taxonomy → ISA-95/edge-fog note → MQTT bus)
3. Hardware and Software Stack (BOM table, software table, TimescaleDB schema table)
4. Tutorial: Deploying the Physical-State Layer (Steps 1–5, each with purpose/decisions/mistakes/validation)
5. Tutorial: Camera-Based Sensing Workflows (LN₂ / gauge / carrier — each as recipe)
6. Tutorial: Instrument-State Integration
7. Case Study: Seven-Day Deployment
8. Best Practices, Design Rules, and Troubleshooting
9. Limitations and Failure Modes
10. Future Directions
11. Conclusion + Significance Statement + Data/Code Availability + Author Contributions + AI Declaration + COI

### Step recipe format (§4–§6)
Each workflow step includes:
- `\paragraph{Purpose.}` — one sentence
- `\paragraph{Key decisions.}` — itemize (bold decision label + explanation)
- `\paragraph{Common mistakes.}` — concise, symptom → cause → fix
- `\paragraph{Validation check.}` — concrete command or observable outcome

### Figure convention
- `\iy{FIGURE: ...}` placeholder with detailed spec (panels A–D, what each shows, data source)
- Caption: `\textbf{Title.} \textbf{(A)}~description. \textbf{(B)}~description.`
- Pending validation noted as `\iy{VALIDATION: ...}` inside caption

### `\iy{}` annotation use
- `\iy{text}` = author note for revision (not shown in output)
- Used for: pending data, figure specs, unverified claims, version pinning TODOs
- Never use for prose that should appear in the paper

---

## Writing Quality Checklist (from session)

Before submitting any revision pass, check:

- [ ] No em dashes in prose (table N/A cells and subsection title separators are fine)
- [ ] No "this section provides" or "this paper presents" openers
- [ ] No passive "is provided in Table X" → rewrite to active
- [ ] No duplicate sentences (same claim stated twice)
- [ ] No filler analogies ("this is analogous to...")
- [ ] All `\iy{VERIFY ...}` and `\iy{PIN ...}` items resolved before submission
- [ ] All `$XX` placeholders filled
- [ ] MQTT topic schema verified against live firmware
- [ ] Phenol red / colorimetric monitoring references fully removed (cut from scope)
- [ ] Culture media / pH references removed from future directions + conclusion
- [ ] Figure captions use `\textbf{(A)}~` not `(A)` or **A**
- [ ] British/American spelling consistent (use American: "color" not "colour")
- [ ] Sensor names exact: SHT30, SCD40, SGP30, QMP6988, PMSA003, TEMT6000

---

## Pending `\iy{}` Annotations (as of 2026-06-04)

High priority (blocking submission):
- `\iy{VERIFY MQTT TOPIC SCHEMA}` — confirm `labsense/env/<id>/data` vs firmware
- `\iy{PIN: docker images}` for TimescaleDB and n8n exact versions
- `\iy{PIN LIBRARY VERSIONS}` for Arduino libraries
- `\iy{ADD SCRIPT: scripts/calibrate_roi.py}` — script missing from repo
- `\iy{ADD FUSION MODELS}` — 3D bracket models for camera mounts

Data pending:
- Task #2: LN₂ confusion matrix (ground-truth annotation)
- Task #3: Carrier held-out evaluation (95% CI on FPR)
- Task #4: CO₂ gauge RMSE (non-empty tank required)
- Task #7: Instrument latency measurement
- Task #8: Fill throughput/uptime numbers from deployment logs
- Task #10: Zenodo DOIs (replace GitHub URLs)

---

## Notes on Scope Decisions Made

- **Colorimetric media monitoring** (phenol red / closed-loop exchange) → **cut from tutorial** (Option B). Deferred to preprint v2 / future paper. Tasks #5 and #6 marked deferred.
- **Biomek liquid handler** → replaced with **Inheco ODTC** throughout (instrument table, intro list, alert routing table).
- **Camera MQTT JPEG publishing** → replaced with **RTSP → Frigate NVR → Prefect Camera Analysis → MQTT derived metrics**.
- **"any analog gauge"** → scoped to "CO₂ dual-scale regulator gauges as tested; other gauge models require re-calibration."
