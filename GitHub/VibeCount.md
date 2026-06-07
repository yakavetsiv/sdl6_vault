---
title: VibeCount
date: 2026-06-04
project: VibeCount
type: github-repo
tags:
  - type/github-repo
  - project/vibecount
  - github
  - cell-counting
  - deep-learning
  - hemocytometer
  - transformer
  - hitl
  - preprint
---

# VibeCount

**URL:** https://github.com/yakavetsiv/VibeCount  
**Language:** LaTeX / Python  
**Last updated:** 2026-06-04

## Description
Transformer-based hemocytometer cell counting system with human-in-the-loop learning. Two-stage RF-DETR pipeline (grid detection + tiled cell detection), center-distance NMS, SAM2 morphometric analysis, mobile-cloud deployment.

## Patent Candidates
- **Center-distance NMS:** $d_{ij} < \tau \cdot (w+h)/2$ — 52% more duplicates removed vs IoU NMS, threshold-insensitive (τ 0.3–0.7 identical)
- **HITL correction loop:** COCO-format operator corrections → automatic dataset expansion → iterative retraining

## Key TODOs (pre-journal submission)
- [ ] Retrain grid model on ≥100 images (current mAP@50=0.23 not reportable)
- [ ] Cluster panel (Fig 3E): need human-annotated cluster image from T3
- [ ] SAM2 supplementary figure (cell_sizes.csv, 33,802 cells)
- [ ] Cross-hardware validation: smartphone + microscopy clip adapter
- [ ] Concentration-series accuracy figure
- [ ] File provisional patent before submission
- [ ] Rewrite Data/Code Availability section if commercializing

## Sessions
- [[Daily/2026-06-04]] — SAM2 integration updates, Yimu comments addressed, figure 1 regenerated, patent disclosure drafted
- [[Daily/2026-06-07]] — n=12 expansion: all stats updated, T2/T3 data imported, task order sensitivity, figures regenerated, deslop pass
