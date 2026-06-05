---
type: concept
title: "VibeCount Manuscript Writing Style Profile"
created: 2026-06-04
updated: 2026-06-04
tags:
  - writing-style
  - vibecount
  - scientific-writing
  - manuscript
  - latex
status: active
related:
  - "[[GitHub/VibeCount]]"
  - "[[LabSense Paper Writing Style Profile]]"
  - "[[SDL High-Impact Writing Patterns]]"
---

# VibeCount Manuscript Writing Style Profile

Style guide for the VibeCount preprint and journal submission. Covers prose tone, LaTeX comment conventions, co-author annotation system, and patent disclosure format.

---

## Prose Style

- **No filler.** Drop "actually," "simply," "importantly," "notably," "here we show."
- **No AI slop.** Run `/deslop` before any submitted paragraph. Watch for: "Two novel components differentiate it from prior art," numbered lists masking prose, formulaic structure.
- Active voice, declarative present tense. "The model achieves" not "was achieved."
- Numbers exact. Never round mAP, p-values, or effect sizes.
- Units: pp (percentage points), s (seconds), µm, cells/mL, ×10⁶.
- Abbreviations defined at first use — every one, including CNN, YOLO, NMS, IoU, mAP, COCO, HITL, ML, AWS, SAM~2, iPSC, P0/P16.

---

## LaTeX Comment Conventions

### `\iy{}` — Internal review notes (I. Yakavets)
Private annotations for IP protection, methodology concerns, and revision flags. **Not visible in compiled PDF** (requires `\newcommand{\iy}[1]{}` in preamble). Example:

```latex
\iy{IP-PROTECT: Training recipe is the most sensitive section...}
```

Tags used:
- `IP-PROTECT` — commercialization risk; action required before submission
- `IP-PROTECT CRITICAL` — blocks submission until resolved
- `REVIEW [CRITICAL]` / `REVIEW [MAJOR]` — peer review anticipation notes

### `\yz{}` — Co-author comments (Yimu Zhang)
Inline suggestions and requests from YZ. Address each before journal submission. Format:

```latex
\yz{benchmark: you should first talk about the accuracy achieved by how many images...}
```

### `% TODO` block — Top of file
Structured TODO block at top of `include-body.tex` tracks pending actions grouped by priority:
- `GRID MODEL` — retraining plan
- `CELL SIZE DATA` — supplementary figure pipeline
- `METHODS FIXES` — trypan blue, concentration figure, cross-hardware
- `CLUSTER PANEL` — Fig 3E, needs human-annotated cluster image
- `IP PROTECTION` — priority 1/2/3 before submission

---

## Structure Preferences

### Introduction paragraph order
1. Problem (manual counting unreliable, slow, operator-dependent)
2. Motivation for automation (standardization across institutions, high-throughput)
3. Dedicated counters (Countess, Vi-CELL) — good reproducibility, bad cost/flexibility
4. Software alternatives — fail at native resolution; CNN/YOLO history
5. DETR/transformer advantage
6. Three bottlenecks (resolution, tile seams, static models)
7. **Contributions: accuracy metrics first, then human benchmark** (Yimu request)

### System Overview paragraph order
1. Hemocytometer = most common bio lab tool (Yimu request — emphasize)
2. VibeCount: instrument-agnostic, cell-type-agnostic claim
3. Density range: "up to 1,200 cells per counting zone (median 244, n=208)"
4. Pipeline description (two-stage RF-DETR + SAM2)
5. Figure 1 (Panels A–D, no footer banner)
6. Detection workflow (auto-rotation → grid detect → tiled cell detect → center-distance NMS)
7. HITL loop
8. Mobile-cloud architecture

---

## Key Figures

| Figure | File | Status |
|--------|------|--------|
| Fig 1: System overview | `figures/figure1.png` | ✓ 5-stage pipeline, Panels A–D, no footer |
| Fig 2: Detection strategy | `figures/fig3.png` | TODO: add Panel E (cluster handling) |
| Fig 4: Model performance | `figures/fig4_model_performance.png` | ✓ |
| Fig S1: SAM2 size analysis | TBD | TODO: cell_sizes.csv, 33,802 cells |
| GUI figure | `figures/gui.png` | ✓ Panel B = diameter histogram |
| Correction analysis | `figures/fig_correction_analysis.png` | ✓ class-aware correction colors |

---

## Patent Disclosure Format (concise, 2-paragraph)

When writing patent invention descriptions:
1. Para 1: system overview + two-stage pipeline + two novel components (center-distance NMS with precision numbers, HITL loop with correction rate). No equations.
2. Para 2: reproducibility study results + SAM2 morphometry + deployment stats.

Key numbers to always include: mAP@50=0.954, F1=0.938, 2.6× SD reduction, 618 s saved, 2.3% correction rate, 1.5× unseen cell line overhead, 52% more duplicates removed vs IoU NMS (precision 0.863 vs 0.796).

---

## SAM2 Description

Correct metric: **equivalent circular diameter** $d = \sqrt{4A/\pi}$ where $A$ = mask area in pixels. NOT major/minor axis.  
Model: sam2.1-hiera-small.  
Endpoint: `POST /api/detect/cells/refine-masks`.  
Fallback: bbox dimensions if SAM2 unavailable.  
UI: diameter histogram stratified by live/dead, adjustable threshold (default 30 µm), snap + sample scope.

---

## Pre-Submission Checklist

- [ ] File provisional patent: center-distance NMS + HITL loop
- [ ] Retrain grid model on ≥100 images (current mAP@50=0.23 not reportable)
- [ ] Rewrite Data/Code Availability (currently open-sources everything — blocks commercialization)
- [ ] Update Conflict of Interest if commercial entity exists
- [ ] Remove exact training hyperparameters (LR=5e-5, patience=15, tile=560)
- [ ] Remove copy-paste augmentation ratio (35%)
- [ ] Change "AWS" to "cloud infrastructure"
- [ ] Add cluster panel Fig 3E (needs human-annotated cluster image)
- [ ] Add SAM2 supplementary figure (cell_sizes.csv)
- [ ] Add concentration-series accuracy figure
- [ ] Cross-hardware validation: smartphone + microscopy clip adapter
