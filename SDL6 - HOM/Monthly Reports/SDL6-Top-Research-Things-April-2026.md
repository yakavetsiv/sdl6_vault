---
type: session
title: "SDL6 Top Research Things — April 2026"
created: 2026-04-30
updated: 2026-06-05
tags:
  - sdl6
  - monthly-report
  - april-2026
  - exnode
  - ipsc
  - automation
  - biosensor
status: stable
related:
  - "[[ExNode Bibliography]]"
  - "[[OKR_SDL6]]"
---

# SDL6 Top Research Things — April 2026

## 1. New Multimodal Biosensor iPSC Lines

In collaboration with Prof. Yufeng Zhao's lab, Yimu Zhao and Rosanna Jiang generated two new stable iPSC reporter lines to establish a standardized workflow for multimodal biosensor engineering and non-invasive biological monitoring.

- **Line 1:** Constitutively expresses mScarlet
- **Line 2:** mScarlet + inducible ETV2 — doxycycline-controlled endothelial differentiation

These reporter systems generate high-quality longitudinal imaging datasets for biological foundation model training and autonomous analysis pipelines.

## 2. ExNode Framework Expansion

Maunica significantly expanded the [[ExNode Bibliography|ExNode]] framework to support three new instruments:

| Instrument | Type |
|-----------|------|
| Agilent VSpin | Centrifuge |
| inHECO | Incubator |
| PreciseFlex | Robotic arm |

Core managers for locations, resources, status, and task orchestration were implemented to enable safe and structured hardware execution. A dedicated Claude Skill was developed to accelerate future ExNode integrations — reducing deployment timelines **from weeks to hours**.

## 3. Hackathon: Rapid Automation with UniteLabs

During the workshop and hackathon organized by Willi, the SDL6 team collaborated with UniteLabs to automate an ABB robotic arm and an inHECO incubator using the ExNode framework.

- Contributors: Maunica, Edison, Daniel
- Highlight: robot waving from code **one day after installation**

## 4. SDL Platform v2.0 Upgrade

Ilya and Edison designing and building SDL platform v2.0.

**Completed milestones:**
- New ~450 kg automated table installed
- SCARA robot mounted on rail
- Plastic surfaces replaced with aluminum plates
- All devices reintegrated
- VSpin centrifuge, ABB arm, and plate hotel deployed

**Incoming:**
- Automated 4°C incubator

**Impact:**
- Automated media exchange for long-term cultures
- Reduced weekend maintenance
- 10G local subnet
- Multi-GPU AI workstation for bioimaging and closed-loop AI models
