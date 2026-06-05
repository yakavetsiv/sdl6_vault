---
title: "ehs-biosafety-benchmark-workflow"
date: 2026-06-04
type: skill
status: developing
tags:
  - ai
  - type/skill
  - sdl6
  - evaluation
  - biosafety
  - obsidian
  - benchmark
---

# ehs-biosafety-benchmark-workflow

Use this workflow to build and iterate a QA benchmark where the target model should fail without access to a local source corpus.

## Trigger
Use when creating, refilling, or scoring a source-grounded benchmark from an Obsidian corpus such as [[EHS Wiki]].

## Workflow
1. Build source-grounded QA pairs from cleaned local notes.
2. Reject questions that mention the retrieval system, Obsidian, "knowledge access", SDL6, source URLs, or document-specific wording.
3. Phrase questions as realistic staff, supervisor, lab-user, or compliance scenarios.
4. Run the default target model without retrieval.
5. Score model answers against the source answer.
6. Penalize generic answers that say they do not know the exact UofT answer, recommend contacting EHS, or provide broad non-source-specific guidance.
7. Keep missed and genuinely uncertain examples; refill correct examples with new questions.
8. Repeat until the dataset is dominated by questions that require source access.

## Scoring Rule
> [!important]
> A model answer should not be marked correct merely because it contains overlapping safety words. If it lacks the UofT-specific requirement or explicitly says it cannot confirm the exact UofT answer, classify it as partial or missed.

## Current Project
- [[UofT EHS Biosafety Benchmark]]
- Captured scripts and JSONL artifacts are stored under `Projects/UofT EHS Biosafety Benchmark/_attachments/project-files`.
