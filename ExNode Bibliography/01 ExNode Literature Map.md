---
tags:
  - literature
  - type/paper
  - lit/sdl
title: ExNode Literature Map
type: concept-map
---

# ExNode Literature Map

## Central Positioning

ExNode is best framed as a missing execution boundary between:

- high-level SDL planning and orchestration, and
- low-level vendor-specific device control.

The literature supports this by showing that existing SDL systems solve important parts of the stack, but not the exact ExNode problem.

## Claim Map

### Claim 1: SDLs need reliable execution, not only planning

Supported by:

- [[02 Self-Driving Laboratory Context#Core SDL reviews]]
- `tom_self-driving_2024`
- `tobias_autonomous_2025`
- `hase_next-generation_2019`
- `canty_science_2025`

Use these references to establish the importance of closed-loop experimental systems and the need for reliable execution.

### Claim 2: Existing orchestration frameworks operate above device-level safety

Supported by:

- [[03 Orchestration and Workflow Systems]]
- `gottstein_foundational_2026`
- `sim_chemos_2024`
- `narayanan_orchestrating_2024`
- `strieth-kalthoff_delocalized_2024`

Use these references to argue that workflows and orchestration need a safe lower execution contract.

### Claim 3: Protocol standards and hardware abstraction do not fully solve execution authority

Supported by:

- [[04 Device Integration and Protocol Interfaces]]
- `bromig_sila_2022`
- `wierenga_pylabrobot_2023`
- `wolf_towards_2024`
- `rodriguez_rest_2016`

Use these references to distinguish communication from execution semantics.

### Claim 4: ExNode adds local safety and deterministic execution

Supported by:

- [[05 Execution Safety State and Scheduling]]
- `gamma_design_1994`
- `liu_scheduling_1973`
- `hou_model_2025`

These are not lab-specific references, but they support state-machine design, priority scheduling, and tool/agent boundary concerns.

## Gap Statement

Suggested manuscript sentence:

> Prior SDL and laboratory automation frameworks provide increasingly powerful abstractions for planning, orchestration, and device communication, but they rarely define the smallest local software authority responsible for serializing hardware access, validating execution state, arbitrating physical resources, and preserving manual operation through vendor-supported control layers.

## How ExNode Should Not Be Positioned

Avoid saying ExNode replaces:

- SiLA 2
- REST
- Prefect
- PyLabRobot
- ChemOS
- UniLabOS

Instead, position ExNode as complementary:

- SiLA 2 and REST are communication surfaces.
- Prefect is an external workflow orchestrator.
- PyLabRobot is a device control abstraction.
- ChemOS and UniLabOS are broader lab operating/orchestration systems.
- ExNode is the local execution authority that can sit below or beside those systems.

