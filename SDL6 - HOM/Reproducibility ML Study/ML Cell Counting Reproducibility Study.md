---
title: ML Cell Counting Reproducibility Study
date: 2026-06-06
project: SDL6-HOM
type: index
tags:
  - sdl6
  - reproducibility
  - ML
  - cell-counting
  - LiveCount
  - LabelStudio
aliases:
  - ML reproducibility study
  - Cell-counting reproducibility pilot
---

# ML Cell Counting Reproducibility Study

Pilot reproducibility study comparing manual hemocytometer counting, LiveCount ML-assisted counting, and LabelStudio live/dead image annotation.

**Repo:** [[GitHub/reproducibility]]  
**Local repo path:** `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility`  
**Project summary:** `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility/ML/docs/project_summary_and_hypotheses.md`

## Current Session Update

Added participant 7 (`p7`) to the ML study. The participant performed Task 2 LiveCount first, then Task 1 manual; the extracted CSV preserves task identity and stores actual execution order in extraction notes.

### Participant 7 Source Data

- ![[p7.png|350]]
- [[_attachments/p7.pdf|p7 source PDF]]
- Repo copy: `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility/ML/data/participant_pdfs/originals/p7.pdf`

### p7 Extracted Values

| Field | Value |
|---|---:|
| SOP understood | Yes |
| Similar experiments | No |
| Wet-lab experience | 8 years |
| Session date/time | 2026-05-29 11:40 |
| Manual total concentration | 5.355M cells/mL |
| Manual live concentration | 5.155M cells/mL |
| Manual viability | 96.3% |
| Manual time | 716 s |
| LiveCount total concentration | 7.145M cells/mL |
| LiveCount live concentration | 6.890M cells/mL |
| LiveCount viability | 96.4% |
| LiveCount time | 318 s |
| LabelStudio time | 980 s |

## Updated Participant-Level Results

Participant-level tables now include `n = 7` participants and `21` long-form task rows.

| Comparison | Manual median | LiveCount median | Median LiveCount - manual | Wilcoxon p |
|---|---:|---:|---:|---:|
| Time | 837 s | 282 s | -590 s | 0.0078125 |
| Viability | 97.8% | 96.7% | -0.20 pp | 0.6875 |
| Total concentration | 5.870M cells/mL | 6.865M cells/mL | +0.705M cells/mL | 0.6875 |

Interpretation: LiveCount remains substantially faster than manual counting in the pilot. Viability remains close by paired comparison; concentration agreement remains exploratory and influenced by participant-level variability.

## Key Plots

![[participant_time_statistics.png]]

![[experience_livecount_benefit.png]]

![[participant_count_agreement.png]]

![[participant_speed_vs_viability.png]]

![[all_tasks_hypotheses.png]]

## Important Repo Files

- `/ML/data/participant_pdf_extracted_review.csv` — reviewed extraction table; p7 rows added.
- `/ML/data/participant_task_results_long.csv` — regenerated 21-row long table.
- `/ML/data/participant_task_results_wide.csv` — regenerated seven-participant wide table.
- `/ML/data/participant_statistics_summary.csv` — paired statistical tests.
- `/ML/docs/project_summary_and_hypotheses.md` — updated project summary and hypotheses.
- `/ML/scripts/organize_participant_tasks.py` — now falls back to local `sample_sheet_clean.csv` if external workbook is unavailable.
- `/ML/scripts/generate_stats_plots.py` — participant count in hypothesis note now generated dynamically.
- `/ML/scripts/analyze_experience_livecount_benefit.py` — participant count generated dynamically.
- `/ML/scripts/analyze_all_tasks_hypotheses.py` — distinguishes participant-level `n = 7` from Task 2 COCO export `n = 6`.

## Regeneration Commands

```bash
python3 ML/scripts/organize_participant_tasks.py
python3 ML/scripts/generate_stats_plots.py
python3 ML/scripts/analyze_experience_livecount_benefit.py
python3 ML/scripts/analyze_task3_labelstudio.py
python3 ML/scripts/analyze_task2_coco_and_task3_model.py
python3 ML/scripts/analyze_all_tasks_hypotheses.py
```

## Notes / Caveats

- Task 2 COCO correction exports still include six participants; no p7 COCO archive was provided in this session.
- Task 3 LabelStudio now uses the server export from `192.168.142.193:8085`, with 12 anonymized annotators for each supplied image.
- Matplotlib emitted font-cache warnings under sandboxed execution, but plots were generated successfully.
- Repo worktree also contains unrelated untracked `LH/` files that were intentionally left untouched.

## Related Notes

- [[SDL6 - HOM/OKR_SDL6|OKR — SDL6 Human Organ Mimicry]]
- [[CFI_HOM_SDL_Equipment_Justification]]
- [[GitHub/VibeCount]]
- [[GitHub/reproducibility]]
- [[Daily/2026-06-04]]


## Label Studio Server Export — 2026-06-06

Downloaded current Label Studio annotations from `http://192.168.142.193:8085` using the vault/repo session workflow. The relevant project is Label Studio project `19`, `Cell Counting`.

### Exported Projects

| Project | Title | Tasks | Completion records | Use |
|---:|---|---:|---:|---|
| 19 | Cell Counting | 2 | 24 | Main Task 3 human annotation export |
| 14 | cytometer imported 2026-05-25 | 550 | 285 | Raw live/dead/debris cell export saved for traceability |

Raw repo export folder: `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility/ML/data/task3_labelstudio_source/labelstudio_192_168_142_193_8085_2026-06-06/`

Vault manifest copy: [[_attachments/labelstudio_export_manifest_2026-06-06.json|Label Studio export manifest]]

### Updated Task 3 Dataset

- `task3_labelstudio_annotations.csv`: 24 rows, 12 annotators x 2 images.
- `task3_labelstudio_boxes.csv`: 3575 boxes.
- `task3_labelstudio_box_agreement.csv`: 24 leave-one-annotator-out agreement rows.
- `task3_labelstudio_summary.csv`: P0 and P16 summary medians/CVs.
- `task3_model_vs_human_counts.csv`: model-vs-human median comparison recalculated from 12-annotator summary.

### Updated Task 3 Results

| Metric | P0 | P16 | P16 - P0 | Wilcoxon p |
|---|---:|---:|---:|---:|
| Median total count | 53.5 | 245.5 | +191.0 | 0.000244 |
| Median dead count | 2.0 | 33.5 | +32.5 | 0.000244 |
| Median viability | 96.33% | 86.30% | -10.14 pp | 0.000244 |

### Updated Task 3 Plots

![[task3_labelstudio_counts_12_annotators.png]]

![[task3_labelstudio_viability_12_annotators.png]]

![[task3_labelstudio_consistency_12_annotators.png]]

![[task3_labelstudio_box_agreement_12_annotators.png]]

![[task3_model_vs_human_median_12_annotators.png]]

### Code Changes

- `/ML/scripts/analyze_task3_labelstudio.py` now prefers the 2026-06-06 Label Studio server export when present.
- Parser now handles both old exports where `completed_by` is a user object and new exports where `completed_by` is an integer user ID.
- Image metadata now maps both old hashed image filenames and server-export image names.
- Task 3 hypothesis text now generates annotator count dynamically.

### Caveats

- Task 2 COCO correction exports still include six participants.
- The 12 Label Studio annotators are anonymized as A1-A12; the export does not map them to PDF participant IDs.
- The Label Studio credentials used for export were defaults found in `cell_counting_images/docker-compose.yml`; no token or password was written to the vault.


## Participant PDF Import and Task Order Update — 2026-06-06

Imported the remaining participant result PDFs `ml-p7.pdf` through `ml-p12.pdf` into the ML study and regenerated the participant-level analysis. This supersedes the earlier p7-only participant update above; the old section is retained as historical session context.

### Updated Participant Dataset

| Artifact | Current value |
|---|---:|
| Reviewed PDF extraction rows | 36 |
| Participant-level wide rows | 12 |
| Long-form task rows | 36 |
| Task 2 COCO participants | 12 |

Important repo files:

- `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility/ML/data/participant_pdf_extracted_review.csv`
- `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility/ML/data/participant_task_results_long.csv`
- `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility/ML/data/participant_task_results_wide.csv`
- `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility/ML/data/participant_task_order.csv`
- `/Users/iyakavets/Library/CloudStorage/OneDrive-UniversityofToronto/AC/SDL6/SCripts/reproducibility/ML/docs/project_summary_and_hypotheses.md`

Vault copies:

- [[_attachments/participant_task_order_2026-06-06.csv|participant_task_order_2026-06-06.csv]]
- [[_attachments/ml-p12.pdf|ml-p12 source PDF]]
- ![[ml-p12_preview.png|350]]

### Confirmed / Current Task Order

| Participant | Sequence | Status |
|---|---|---|
| p7 | Task 2 → Task 1 → Task 3 | visible form marks |
| p8 | Task 2 → Task 1 → Task 3 | visible form marks |
| p9 | Task 3 → Task 1 → Task 2 | user confirmed Task 3 first |
| p10 | Task 1 → Task 2 → Task 3 | still needs confirmation if Task 3 timing differed |
| p11 | Task 3 → Task 2 → Task 1 | user confirmed Task 3 first; LiveCount before manual from form mark |
| p12 | Task 3 → Task 1 → Task 2 | user confirmed Task 3 first |

### p12 Values Needing Confirmation

p12 task order is confirmed, but the numeric fields remain flagged because the PDF contains crossed-out and overwritten entries.

| p12 field | Extracted value |
|---|---:|
| Manual total concentration | 3,133,333 cells/mL |
| Manual live concentration | 2,800,000 cells/mL |
| Manual viability | 89.0% |
| Manual time | 820 s (13:40) |
| LiveCount total concentration | 3,135,000 cells/mL |
| LiveCount live concentration | 2,955,000 cells/mL |
| LiveCount viability | 94.3% |
| LiveCount time | 324 s (5:24) |
| Task 3 time | 931 s (15:31) |

### Regenerated Participant Results

| Metric | Updated value |
|---|---:|
| Manual median time | 783.5 s |
| LiveCount median time | 284.5 s |
| Median LiveCount - manual time | -440.0 s |
| Time Wilcoxon p | 0.000244 |
| Manual median viability | 95.37% |
| LiveCount median viability | 95.90% |
| Median paired viability difference | -0.30 pp |
| Median paired total concentration difference | +0.053M cells/mL |

### Updated Plots

![[participant_time_statistics_12_participants.png]]

![[participant_count_agreement_12_participants.png]]

![[experience_livecount_benefit_12_participants.png]]

![[all_tasks_hypotheses_12_participants.png]]

### Regeneration Commands

```bash
python3 ML/scripts/organize_participant_tasks.py
python3 ML/scripts/generate_stats_plots.py
MPLCONFIGDIR=/private/tmp/mplconfig python3 ML/scripts/analyze_experience_livecount_benefit.py
MPLCONFIGDIR=/private/tmp/mplconfig python3 ML/scripts/analyze_all_tasks_hypotheses.py
```

### Caveats / Follow-Up

- Confirm p12 numeric values from the messy PDF before final manuscript tables.
- Confirm p10 task order if needed; current metadata keeps `1>2>3` from visible form layout.
- p1-p6 task order remains blank in `participant_task_order.csv` until explicitly confirmed.
