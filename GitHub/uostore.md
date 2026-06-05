---
title: uostore
date: 2026-06-04
type: github-repo
tags:
  - type/github-repo
  - github
  - UOroboros
  - workflow-orchestration
  - self-driving-labs
  - provenance
---

# uostore

**URL:** https://github.com/spgarcica/uostore  
**Local path:** `/Users/iyakavets/Documents/Github/Uoroboros/uostore`  
**Language:** Python  
**Package:** `uoroboros`  

## Description
UOroboros is a Python framework for defining, validating, registering, and executing typed Unit Operations, Flows, and Workflows for self-driving labs. It models procedures as composable graph artifacts with versioned modules, explicit Pydantic types, first-class error routing, provenance capture, CLI/API interfaces, and pluggable execution/database backends.

## Architecture Notes
- `model/` is the zero-dependency contract layer: records, blocks, mappings, routing, stop conditions, and runtime instance types.
- `registration/` handles decorators, module scanning, JSON schemas, structural validation, type validation, and immutable registration.
- `execution/` contains local and parallel DAG engines, workflow execution, provenance recording, backend abstraction, and a Prefect backend/codegen path.
- `db/` abstracts persistence and includes a Neo4j backend for graph storage.
- `cli/` and `api/` are thin user-facing wrappers around shared registration, execution, and DB operations.
- `environment/` supports local, Git, and PyPI module sources.

## Fit for Image Pipelines
Good conceptual fit for complex image-processing workflows where each operation is typed, versioned, auditable, and composed into larger DAGs. Best used to pass lightweight artifacts such as manifest paths, audit paths, measurements, and QC summaries rather than image arrays.

## Key Constraint
In the current framework version, Pydantic types are neutral. Routing metadata belongs on `@unit_operation(outputs={...})` using `OutputCondition`; it does not belong on `@uoroboros_type`.

## Sessions
- [[Daily/2026-06-04]] — Evaluated as orchestration/provenance layer for complex microscopy image-processing pipelines.

## Related Notes
- [[GitHub/image_analysis_uos]]
- [[UOroboros Image Pipeline Design Notes]]
