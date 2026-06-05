---
title: UOroboros Image Pipeline Design Notes
date: 2026-06-04
type: design-note
project: UOroboros image pipelines
tags:
  - UOroboros
  - image-analysis
  - manifests
  - audit
  - retention
  - distributed-execution
---

# UOroboros Image Pipeline Design Notes

## Position
Use UOroboros for orchestration, validation, versioning, execution provenance, and typed stage boundaries. Do not use it to pass large image arrays between steps. Images should stay on disk, shared storage, or object storage; UOs pass manifest paths, audit paths, output directories, and summaries.

## Manifest Strategy
Keep the original rich metadata CSV immutable. Use a JSON run manifest as the pipeline state object and write derived per-stage CSV snapshots for human inspection and downstream tools.

Recommended run layout:

```text
runs/run_001/
  00_input_metadata.csv
  manifest.json
  stages/
    01_stitch/
      input_manifest.csv
      output_manifest.csv
      audit.json
      logs.txt
      outputs/
    02_enhance/
      input_manifest.csv
      output_manifest.csv
      audit.json
      outputs/
    03_segment/
      input_manifest.csv
      output_manifest.csv
      audit.json
      outputs/
```

## UO Contract
Prefer a stable file-manifest contract:

```python
class ManifestRequest(BaseModel):
    manifest_path: str
    parameters: dict = {}

class ManifestResult(BaseModel):
    manifest_path: str
    audit_path: str
    output_dir: str
    status: str
    summary: dict = {}
```

The rich image/file/well/channel state lives inside the manifest, not in the orchestration schema.

## Audit Requirements
Each UO should write a stage `audit.json` containing:
- stage name and run ID
- start/end timestamps and status
- code module, version, and git commit
- exact parameters
- input/output manifest paths and SHA-256 hashes
- per-file input/output paths, checksums, status, and warnings
- QC metrics such as dimensions, channels, tile counts, cell counts, confluence, and failed files
- environment information when relevant, especially for Cellpose/GPU runs

## Retention Policy
A 7-day retention policy is reasonable for recomputable intermediate images if these are retained long-term:
- source metadata CSV
- run manifest JSON
- per-stage manifests
- audit records
- raw/source image references
- hashes/checksums
- code commits and package versions
- environment lock files
- final measurements and QC summaries

Manifest records should keep deleted file entries with `status: deleted`, `expires_at`, `retention_class`, `recomputable`, and `derived_from`.

## Dimensionality Changes
The manifest must support many-to-one and one-to-many transformations. Stitching and merging are many-to-one operations:

```text
raw tiles:       well + channel + site + tile
stitched image:  well + channel
merged image:    well + channels[]
segmentation:    well + mask/object/measurement records
```

Important fields:
- `kind`: raw_tile, stitched_image, merged_image, mask, outline, measurement
- `axes`: examples include `YX`, `YXC`, `CYX`
- `shape`: image dimensions
- `channel`: scalar channel where applicable
- `channels`: list after merging
- `site` and `tile`: nullable after stitching
- `derived_from`: required lineage list
- `transform`: offsets, merge order, model, or algorithm-specific metadata

## Database Split
UOroboros/Neo4j should store registered definitions, workflow graph, run provenance, block-level inputs/outputs, manifest paths, audit paths, and summaries.

Filesystem or object storage should store images, manifests, audits, logs, derived CSVs, masks, and outlines.

If file-level metadata must be searchable, add a dedicated manifest database such as Postgres or SQLite for file rows, wells, channels, QC metrics, measurements, and retention state.

## Multi-Machine Execution
Multi-machine execution is possible through a distributed execution backend such as Prefect. Required shared infrastructure:
- shared image/manifest storage visible to all workers
- shared UOroboros database
- worker environments with matching image-processing dependencies
- partitioning by well, plate chunk, or site rather than arbitrary files when stitching/merging requires grouped inputs

## Related Repos
- [[GitHub/uostore]]
- [[GitHub/image_analysis_uos]]
