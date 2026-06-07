---
title: VibeCount
date: 2026-06-04
project: VibeCount
type: index
tags:
  - project
  - project/vibecount
  - type/index
  - preprint
  - computer-vision
  - cell-counting
  - SAM2
---

# VibeCount

Automated cell counting preprint. Pipeline: auto-rotation → grid detector → cell detector → SAM2 size analysis.

**Repo:** [[GitHub/VibeCount]]  
**Sessions:** [[Daily/2026-06-04]]

## Patent Candidates
- Center-distance NMS
- HITL correction loop

## Key Decisions
- Figure 1: 5-stage pipeline diagram (Panels A-D, no footer banner)
- Yimu Zhang co-author comments addressed (10 annotations)


## Recent Session - 2026-06-04 Reference, Export, and Product Notes

- Label Studio project exports are stored at `/Users/iyakavets/Documents/Github/cell_counting_images/labelstudio_exports/2026-05-25_projects/`.
- VibeCount deployment/product docs were added in Git commit `98e4c97`: `AWS_DEPLOYMENT.md` and `PRODUCT_COMPANY_AND_MANUSCRIPT_TODO.md`.
- Reference-connection notes were added in Git commit `3de5845` to `includes/include-body.tex` and `includes/include-review-r1.tex`.
- Zotero now contains imported references for Parasuraman and Manzey 2010, DINOv2, RF-DETR, Microsoft COCO, Deformable DETR, focal loss/RetinaNet, FCOS, YOLOv11, and YOLOv8.
- Bibliography cleanup still needed: resolve `obrien_imagej_2016`, resolve `parasuraman_humans_2010`, and replace the outdated `rfdetr_2025` entry with Robinson et al. 2026.

### Current Product Position
VibeCount is an AWS-hosted, research-use-only web service for editable AI-assisted hemocytometer cell counting. The current value proposition is faster, more reproducible research counting with human review, not clinical or GMP release testing.

## Session Log
- **2026-06-07** — [[Daily/2026-06-07]]: n=12 expansion, T2/T3 data import, task order analysis, figure regeneration, deslop
- **2026-06-07** — [[Daily/2026-06-07]]: Supp Fig S1 cluster panel finalized (overlap fix, stale draft removed), TODO closed; landing page F1 score corrected (0.960→0.938) in `cell_counting_images` waitlist-apple page
