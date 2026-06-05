---
type: session
title: "SDL6 Highlights — March 2026 (ML × Bioimaging × Automation)"
created: 2026-03-31
updated: 2026-06-05
tags:
  - sdl6
  - monthly-report
  - march-2026
  - ml
  - bioimaging
  - automation
  - vibecount
  - ipsc
  - virtual-staining
status: stable
related:
  - "[[OKR_SDL6]]"
  - "[[SDL6-Top-Research-Things-February-2026]]"
  - "[[SDL6-Top-Research-Things-April-2026]]"
---

# SDL6 Highlights — March 2026 (ML × Bioimaging × Automation)

## VibeCount *(in development)*

ML-based automated cell counting deployable on any existing microscope via phone.

- **Lead:** Ilya Yakavets; datasets by Rosanna Jiang
- **Model:** RT-DETR
- **Deployment:** AWS (by Maunica Toleti)
- **Performance:** 0.925 mAP; near-perfect viability estimation
- **Status:** Production-ready pipeline; tested on 2 cell types, aiming for higher accuracy across diverse cell types

## iPSC Colony Segmentation

Label-efficient Semi-Siamese U-Net architecture in collaboration with UConn.

- F1 ≥ 0.96 with minimal annotation

## Virtual Staining (Diffusion)

Brightfield → fluorescence prediction enabling label-free imaging.

- Lead: Daniel Hocevar

## Microtissue Contractility Analysis

Quantitative functional readouts from microtissue imaging.

- Developed by Yimu Zhao and Ilya Yakavets

## Report Hub *(available via Tailscale)*

Auto-generated ML reports from GitHub, served as interactive dashboards for reproducible research and project tracking.
