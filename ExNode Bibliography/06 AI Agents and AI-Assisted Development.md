---
title: AI Agents and AI-Assisted Development
type: theme
---

# AI Agents and AI-Assisted Development

## Purpose In Paper

This cluster supports two separate claims:

1. AI agents can interact with tools through protocols such as MCP.
2. AI-assisted coding can help scaffold ExNode implementations, but human validation remains necessary.

Keep these claims separate.

## MCP And Agent Tooling

### `hou_model_2025`

Model Context Protocol landscape and security threats.

Use for:

- MCP as an AI-agent tool protocol.
- Tool lifecycle and security concerns.
- Need for boundaries around tool invocation.

ExNode angle:

- Supports the claim that direct tool exposure is not enough; ExNode should act as an admission-control boundary between AI agents and hardware operations.

Suggested manuscript sentence:

> MCP exposes tools to agents, but ExNode constrains what those tools can do by routing requests through local state validation, resource checks, priority handling, and execution logging.

## AI-Assisted Coding

### `sarkar_vibe_2025`

Vibe coding / programming through conversation with AI.

Use for:

- AI-assisted software development.
- Human oversight, iterative verification, and context management.

ExNode angle:

- Supports the ExNodeFactory construction workflow only if the manuscript avoids overclaiming "zero-code".

Suggested wording:

> ExNodeFactory can support AI-assisted, template-guided construction, where candidate primitives and Unit Operations are proposed by an AI coding tool and validated by a human operator.

Avoid:

- "The system automatically generates safe drivers."
- "No domain expertise is required."
- "Zero-code construction" unless the evidence is very strong.

## Agent Safety Framing

The bibliography supports a conservative claim:

> AI agents may request operations, but they should not directly own hardware execution.

This is central to the ExNode argument.

