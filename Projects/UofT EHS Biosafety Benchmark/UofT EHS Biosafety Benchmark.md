---
title: "UofT EHS Biosafety Benchmark"
date: 2026-06-04
project: UofT-EHS-Benchmark
type: index
status: active
tags:
  - project
  - biosafety
  - uoft-ehs
  - benchmark
  - evaluation
related:
  - "[[EHS Wiki Home]]"
  - "[[Literature Wiki Home]]"
  - "[[ehs-biosafety-benchmark-workflow]]"
---

# UofT EHS Biosafety Benchmark

> [!summary]
> Built an iterative QA benchmark for questions about University of Toronto EHS biosafety requirements that default GPT-5.5 should not know without source access.

## Current State
- Seed dataset: `1000` QA rows.
- Round 2 dataset: `1000` QA rows, `1000` unique ids.
- Round 2 GPT-5.5 eval: `1000` rows, `1000` unique ids.
- Missing eval ids: `0`.
- Extra eval ids: `0`.

## Round 2 Review
| Label | Count |
|---|---:|
| likely_correct | 882 |
| partial_or_uncertain | 71 |
| likely_missed | 47 |

> [!warning]
> Round 2 execution is complete, but the heuristic scorer is too permissive. `851` of the `likely_correct` rows still contain uncertainty language such as "I don't know", "exact UofT", or "contact UofT". Generic answers with uncertainty should be partial or missed.

## Files Captured
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/.env.template|.env.template]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/EHS_BIOSAFETY_EVAL_README.md|EHS_BIOSAFETY_EVAL_README.md]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/EHS_WIKI_GRAPH_AUDIT.md|EHS_WIKI_GRAPH_AUDIT.md]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/build_ehs_biosafety_qa_dataset.py|build_ehs_biosafety_qa_dataset.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/run_gpt55_ehs_eval.py|run_gpt55_ehs_eval.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/refill_ehs_biosafety_questions.py|refill_ehs_biosafety_questions.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/iterate_ehs_biosafety_benchmark.py|iterate_ehs_biosafety_benchmark.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/rebuild_ehs_biosafety_semantic_graph.py|rebuild_ehs_biosafety_semantic_graph.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/dedupe_ehs_wiki_pages.py|dedupe_ehs_wiki_pages.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/clean_ehs_root_indexes.py|clean_ehs_root_indexes.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/add_canadian_biosafety_handbook_reference.py|add_canadian_biosafety_handbook_reference.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/download_canadian_biosafety_standards_guidelines.py|download_canadian_biosafety_standards_guidelines.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/crawl_canada_biosafety_references.py|crawl_canada_biosafety_references.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/update_literature_reading_notes.py|update_literature_reading_notes.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/convert_literature_pdfs_markitdown.py|convert_literature_pdfs_markitdown.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/repair_literature_note_spacing.py|repair_literature_note_spacing.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/refill_literature_reading_notes_from_markitdown.py|refill_literature_reading_notes_from_markitdown.py]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/ehs_biosafety_qa_seed_1000.jsonl|ehs_biosafety_qa_seed_1000.jsonl]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/ehs_biosafety_qa_round2.jsonl|ehs_biosafety_qa_round2.jsonl]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/ehs_biosafety_gpt55_eval_round1.jsonl|ehs_biosafety_gpt55_eval_round1.jsonl]]
- [[Projects/UofT EHS Biosafety Benchmark/_attachments/project-files/ehs_biosafety_gpt55_eval_round2.jsonl|ehs_biosafety_gpt55_eval_round2.jsonl]]

## Important Decisions
- Questions were rephrased to sound like staff and lab-user questions, not prompts about "knowledge", Obsidian, SDL6, or a specific source document.
- Metadata leakage and source URLs were filtered out of answers.
- Canada.ca biosafety standards/guidelines pages were crawled and added to the EHS Wiki as external references.
- EHS Wiki duplicates and root index clutter were cleaned.
- Literature Wiki PDFs were converted with MarkItDown into `_data/markitdown`; deterministic note refilling was tested but not applied because it left too many manual-review fields.

## Next Actions
- Tighten the evaluator so uncertainty language in the model answer penalizes the label.
- Refill from `likely_missed` and stricter `partial_or_uncertain` rows only.
- Run another GPT-5.5 round after the scorer is fixed.
- Use MarkItDown text as context for LLM-based Literature Wiki reading-note enrichment instead of deterministic extraction.

## Project Links
- [[EHS Wiki/EHS Wiki Home|EHS Wiki]]
- [[Literature Wiki/Literature Wiki Home|Literature Wiki]]
- [[ehs-biosafety-benchmark-workflow]]
