---
title: ML Cell Counting Reproducibility Study
date: 2026-06-04
project: SDL6-HOM
type: index
tags:
  - SDL6
  - HOM
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
- Task 3 LabelStudio export still includes six anonymized annotators for the supplied images.
- Matplotlib emitted font-cache warnings under sandboxed execution, but plots were generated successfully.
- Repo worktree also contains unrelated untracked `LH/` files that were intentionally left untouched.

## Related Notes

- [[SDL6 - HOM/OKR_SDL6|OKR — SDL6 Human Organ Mimicry]]
- [[CFI_HOM_SDL_Equipment_Justification]]
- [[GitHub/VibeCount]]
- [[GitHub/reproducibility]]
- [[Daily/2026-06-04]]
