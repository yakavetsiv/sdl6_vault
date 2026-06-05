---
tags:
  - literature
  - type/paper
  - lit/sdl
title: Device Integration and Protocol Interfaces
type: theme
---

# Device Integration and Protocol Interfaces

## Purpose In Paper

This cluster supports the claim that device integration is hard, but also helps avoid overclaiming. Many references solve communication or abstraction problems; ExNode should be positioned as solving local execution authority and safety semantics.

## Laboratory Device Standards

### `bromig_sila_2022`

SiLA 2 Manager for rapid device integration and workflow automation.

Use for:

- Device discovery and management.
- SiLA 2 as a lab device communication standard.
- Workflow integration through standard interfaces.

ExNode angle:

- SiLA 2 is a protocol surface. ExNode can expose or consume protocol adapters, but its contribution is stateful execution control beneath the adapter.

### `rodriguez_rest_2016`

REST API design and compliance.

Use for:

- General REST API background.
- Justifying REST as an integration surface.

ExNode angle:

- REST is an adapter, not the architecture.
- Avoid centering the contribution on REST alone.

## Hardware-Agnostic Drivers

### `wierenga_pylabrobot_2023`

PyLabRobot hardware-agnostic liquid-handling interface.

Use for:

- Open-source device abstraction.
- Cross-platform hardware control.
- Driver reuse.

ExNode angle:

- PyLabRobot supports direct device control, especially for liquid handling.
- ExNode adds a stateful execution boundary, priority handling, resource locks, and GUI/agent/orchestrator admission control.

## Robotic Laboratory Integration

### `wolf_towards_2024`

Reference architecture for laboratory robot integration.

Use for:

- Plug-and-play robotic integration.
- Pick-and-place labware transportation.
- Layered automation architecture.

ExNode angle:

- Supports the PF3400 robot arm example and the distinction between spatial coordination and sample/resource occupancy.

## Practical User Guides

### `maroulis_users_2025`

Guide to a first self-driving liquid handling lab.

Use for:

- Adoption barriers.
- Practical integration challenges.
- Low-cost and accessible SDL builds.

ExNode angle:

- Supports the claim that laboratories need lower-friction and reproducible integration pathways.

## Device-Specific Bibliography Gaps

For the three-device example, add references or documentation entries for:

- VSPIN automated centrifuge / ActiveX or vendor API.
- PF3400 robot arm.
- InHECO incubator.

These do not need to be academic papers if vendor manuals or documentation are the relevant source, but they should be cited or listed as implementation artifacts if claims depend on them.

