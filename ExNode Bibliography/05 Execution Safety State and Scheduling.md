---
title: Execution Safety State and Scheduling
type: theme
---

# Execution Safety State and Scheduling

## Purpose In Paper

This cluster supports the architecture-level mechanisms inside ExNode:

- finite execution state,
- single execution authority,
- priority-aware task handling,
- explicit operation outcomes,
- resource safety.

## State Model And Software Architecture

### `gamma_design_1994`

Design Patterns.

Use for:

- General software design pattern background.
- State pattern or reusable object-oriented design concepts.

ExNode angle:

- Supports the use of explicit state models, but it is a broad software reference. If the paper leans heavily on finite-state execution safety, consider adding a more direct finite state machine or safety-critical systems reference.

## Scheduling

### `liu_scheduling_1973`

Hard real-time scheduling algorithms.

Use for:

- Priority scheduling background.
- Real-time task scheduling foundations.

ExNode angle:

- Supports priority-aware execution queues, but ExNode is not necessarily hard real-time. Phrase carefully:

> The task manager borrows from priority-aware scheduling principles, but ExNode does not claim hard real-time guarantees.

## SDL Safety And Accountability

### `tobias_autonomous_2025`

Use for:

- Safety and security concerns around SDLs.
- Human accountability.

### `canty_science_2025`

Use for:

- Collaborative and distributed SDL challenges.
- Human-machine collaboration.

## Safety Gap

The current bibliography lacks a direct safety-focused SDL citation. Consider adding one if the manuscript uses strong language such as "safety-aware" or "safety firewall".

Candidate already present in `includes/references.bib` but not currently cited:

- `leong_steering_2025` - Steering towards safe self-driving laboratories.

## Recommended Safety Framing

Use careful wording:

- Good: "software-mediated execution boundary"
- Good: "state validation and resource arbitration"
- Good: "reduces unsafe command interleavings"
- Avoid: "guarantees safety" without qualification
- Avoid: "E_STOP" as if it replaces physical emergency stop

Suggested manuscript sentence:

> ExNode provides software-mediated safety constraints, including state validation, resource arbitration, timeouts, and priority handling; these mechanisms complement, but do not replace, hardware-level safety systems.

