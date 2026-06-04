---
title: Orchestration and Workflow Systems
type: theme
---

# Orchestration and Workflow Systems

## Purpose In Paper

This cluster separates orchestration from execution. It supports the central ExNode distinction:

- Orchestrators decide what should happen and in what order.
- ExNodes decide whether a local hardware operation is admissible and then execute it deterministically.

## Orchestrated Lab Representation

### `gottstein_foundational_2026`

Foundational representation for an orchestrated lab.

Use for:

- Primitive -> Unit Operation -> Flow -> Workflow hierarchy.
- Typed, declarative workflow structure.
- Validation and interoperability framing.

ExNode angle:

- ExNode should be framed as implementing the primitive and Unit Operation side of this hierarchy under a local execution authority.

Suggested sentence:

> ExNode operationalizes the lower layers of the primitive-to-workflow hierarchy by assigning primitives and Unit Operations to a local, stateful execution authority.

## ChemOS And Lab Operating Systems

### `sim_chemos_2024`

ChemOS 2.0 orchestration architecture.

Use for:

- SDL orchestration architecture.
- Coordination among modular lab components.

ExNode angle:

- ChemOS coordinates and manages an SDL; ExNode defines the local hardware execution contract that such systems could call.

### `gao_unilabos_2025`

UniLabOS AI-native operating system for autonomous laboratories.

Use for:

- Recent operating-system-level framing.
- Typed, stateful abstractions and transactional safeguards.
- Multi-node coordination.

ExNode angle:

- This is close conceptual territory. The paper should clearly distinguish ExNode as a minimal local execution boundary, not a full lab OS.

Potential risk:

- If UniLabOS is included, reviewers may ask how ExNode differs. The answer should be explicit.

## Workflow Engines

### `narayanan_orchestrating_2024`

Prefect chapter in a data engineering context.

Use for:

- General Prefect orchestration background.
- Workflow task execution, scheduling, and state management at the workflow layer.

ExNode angle:

- Prefect should be described as an external orchestrator that invokes ExNode adapters.
- Do not imply Prefect provides device-level resource safety.

## Distributed SDL Examples

### `strieth-kalthoff_delocalized_2024`

Use in this theme for:

- Cloud-based coordination.
- Asynchronous distributed workflows.

ExNode angle:

- Each physical laboratory or instrument group in a distributed SDL needs a local execution authority.

## Missing Orchestration References

The revised manuscript cites:

- `granda_labos_2018`
- `zhou_chemos_2017`

These keys are missing from the active BibTeX file. Add them or replace them with available entries such as `sim_chemos_2024`.

