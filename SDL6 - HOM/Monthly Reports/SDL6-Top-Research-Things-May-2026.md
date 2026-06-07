---
type: session
title: "SDL6 Top Research Things — May 2026"
created: 2026-05-31
updated: 2026-06-05
tags:
  - sdl6
  - monthly-report
  - may-2026
  - vibecount
  - sdl-dashboard
  - 3d-map
  - labsense
status: stable
related:
  - "[[SDL6-Top-Research-Things-April-2026]]"
  - "[[SDL6-Top-Research-Things-March-2026]]"
  - "[[OKR_SDL6]]"
---

# SDL6 Top Research Things — May 2026

## 1. VibeCount — Manuscript Near Submission

RF-DETR + SAM2 two-stage pipeline validated across 5 cell lines, 55K+ detections, 2.3% correction rate. CellDrop viability comparison added. All figures regenerated to Nature specs. Yimu's comments addressed (density range 20–1,200 cells/zone, median 244, n=208). Remaining: grid model retraining to 100+ images, cluster panel, SAM2 supplementary figure.

## 2. SDL Dashboard — 3D Map, Unified UI & Imaging DB

Unified interface for monitoring, controlling, and understanding the SDL platform. Researchers can track instrument status, review imaging datasets, and supervise automation runs from a single dashboard, reducing context-switching and making lab state legible remotely.

- **3D lab map:** Three.js/React interactive lab map embedded in dashboard. Foundation for a full digital twin of the SDL.
- **Unified UI:** Mobile + desktop unified; CCTV, robot camera, admin, and 2D map all redesigned.
- **Galaxy data visualization**

## 3. UR5 Teleoperation via 3D Arm Interface

UR5 teleoperation via handheld controller mapped to a 3D virtual arm, with real-time pose mirroring without a teach pendant. Set up by the SDL0 robotics team (Kelvin Chow). Enables supervised robotic operation inside HEPA-filtered enclosures and biosafety-controlled workspaces, where direct human access disrupts sterility or containment. Operators can recover failed transfers, reposition labware, and assist setup without opening the enclosure. A practical bridge between manual workflows and full autonomy for complex biological protocols.

![[IMG_2668.HEIC]]

## 4. AI Workstation — Local Inference for Bioimaging

Threadripper PRO 9965WX workstation purchased and built by Quoted Tech (Toronto). Dedicated to local inference of bioimaging foundation models, VLMs, and ML lab tools, keeping latency low and imaging data on-site. Model training runs on the Balam cluster (SciNet). Spec: 256 GB DDR5 ECC, RTX PRO 4500 Blackwell, 1 TB NVMe, Ubuntu 24.04 LTS. Planned expansion to a 4-GPU system.

![[IMG_2612.HEIC]]

## 5. LabSense — Physical-State Sensor Dashboard

9-node lab monitoring system over Tailscale + TimescaleDB. Three sensor tiers: environmental (temp, humidity, CO₂, PM₂.₅), camera-derived (LN₂ level, gauge, carrier detection via Frigate), and instrument status (Cytomat, centrifuge). Almost a year of continuous traces; 280K readings/week. Video stays on local edge server, with only derived metrics pushed to DB.
