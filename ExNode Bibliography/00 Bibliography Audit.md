---
title: Bibliography Audit
type: audit
source_bibliography: includes/references.bib
source_manuscript: includes/include-body-revised.tex
---

# Bibliography Audit

## Scope

This audit checks the citations currently used in the ExNode body against `includes/references.bib`, the active bibliography file referenced by `preprint.tex` and `preprint_revised.tex`.

## Cited Keys Found In `includes/references.bib`

- `martin_perspectives_2023`
- `tom_self-driving_2024`
- `ishizuki_autonomous_2023`
- `tobias_autonomous_2025`
- `baird_what_2022`
- `strieth-kalthoff_delocalized_2024`
- `gottstein_foundational_2026`
- `wolf_towards_2024`
- `maroulis_users_2025`
- `hase_next-generation_2019`
- `wierenga_pylabrobot_2023`
- `canty_science_2025`
- `maffettone_what_2023`
- `sarkar_vibe_2025`
- `bromig_sila_2022`
- `narayanan_orchestrating_2024`
- `gamma_design_1994`
- `liu_scheduling_1973`
- `rodriguez_rest_2016`
- `hou_model_2025`

## Missing Cited Keys

The revised body cites these keys, but they are not present in the active `includes/references.bib` file:

- `granda_labos_2018`
- `zhou_chemos_2017`
- `stokes_autonomous_2024`
- `gao_autonomous_2023`

### Suggested Fix

Do not leave these as-is. Either add the missing BibTeX entries or replace them with available keys already in the bibliography.

Candidate replacements currently present:

- `zhou_chemos_2017` could likely be replaced or supplemented with `sim_chemos_2024` for ChemOS 2.0.
- `gao_autonomous_2023` appears to refer to A-Lab; the available key is `szymanski_autonomous_2023`.
- `gao_unilabos_2025` is present and may be useful for positioning ExNode relative to UniLabOS, but it is not the same as A-Lab.

## Duplicate Keys

Several keys appear more than once in `includes/references.bib`. This can create BibTeX ambiguity or silently select one entry depending on tool behavior.

Observed duplicate examples:

- `baird_what_2022`
- `canty_science_2025`
- `hase_next-generation_2019`
- `maffettone_what_2023`
- `tom_self-driving_2024`

### Suggested Fix

Keep the complete journal article entries and remove or rename the abbreviated `@misc` duplicates. For example, keep the full `@article{baird_what_2022,...}` entry and remove the earlier abbreviated `@misc{baird_what_2022,...}` entry.

## Current Bibliography Fit

The current bibliography is strong for:

- SDL motivation and reviews.
- Workflow and orchestration framing.
- Device standardization and robotics integration.
- Software architecture concepts supporting state and scheduling.

The current bibliography is weaker for:

- Direct comparisons to vendor-GUI-preserving automation layers.
- Safety-specific SDL literature.
- Concrete lab automation schedulers beyond Prefect and SiLA 2.
- PF3400 robot arm and InHECO incubator vendor/device-specific references.

## Recommended Next Bibliography Work

1. Fix missing keys before compiling.
2. Deduplicate repeated BibTeX keys.
3. Add 2-3 references specifically about safety in SDLs or laboratory robotics.
4. Add references for PF3400 and InHECO if those devices remain central examples.
5. Replace broad claims about "zero-code" with citations about AI-assisted programming and careful human validation.

