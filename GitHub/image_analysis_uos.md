---
title: image_analysis_uos
date: 2026-06-04
type: github-repo
tags:
  - github
  - image-analysis
  - UOroboros
  - microscopy
  - manifests
---

# image_analysis_uos

**URL:** https://github.com/AC-SDL6/image_analysis_uos  
**Local path:** `/Users/iyakavets/Documents/Github/Uoroboros/image_analysis_uos`  
**Language:** Python  
**Package:** `image-analysis-uos`  

## Description
Domain package intended to expose microscopy image-analysis operations as UOroboros Unit Operations. It wraps stitching, channel merging, brightness/contrast enhancement, and Cellpose segmentation behind a shared `AnalysisRequest -> AnalysisResult` contract and provides JSON flow/workflow definitions.

## Intended UOs
- `stitch_tiles` — CSV-driven tile stitching into per-well/per-channel TIFFs and manifests.
- `stitch_and_merge` — combined stitching plus channel merging.
- `merge_channels` — combine multiple fluorescence channels into multichannel images.
- `adjust_brightness_contrast` — auto, CLAHE, manual, or normalization enhancement.
- `segment_cells` — Cellpose segmentation with masks, outlines, and measurement records.

## Current Compatibility Issues
- Import currently fails against the cloned `uostore` because error models call `@uoroboros_type(condition=..., code=..., message=...)`, but the current decorator only accepts `name` and `description`.
- The UO functions return unions such as `AnalysisResult | InvalidRequestError | StitchingError` but do not pass `outputs={...}` to `@unit_operation`. Under the current framework, missing output routes default to success and violate the single-success rule.
- Flow JSON files use `context.*` mappings for parameters. The local execution path appears to support `input` and `result` mapping data, so parameter passing should be moved into declared input fields or framework context support should be added deliberately.

## Recommended Fixes
- Remove routing kwargs from `@uoroboros_type`.
- Add explicit `OutputCondition` routes to every `@unit_operation`.
- Redesign flow inputs so parameter bundles pass through `input.*` or a validated manifest object.
- Add import, registration, and small synthetic-image integration tests.

## Sessions
- [[Daily/2026-06-04]] — Analyzed as first image-processing module for UOroboros.

## Related Notes
- [[GitHub/uostore]]
- [[UOroboros Image Pipeline Design Notes]]
