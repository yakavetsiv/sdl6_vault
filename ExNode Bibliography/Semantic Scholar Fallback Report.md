---
tags:
  - literature
  - type/paper
  - lit/sdl
title: Semantic Scholar Fallback Report
type: external-resolution-report
---

# Semantic Scholar Fallback Report

This report records external lookup results for ExNode citation keys that were not matched in Zotero. Zotero had no matching item for these keys, and the active `includes/references.bib` file also lacks complete entries for them.

## API Status

The Semantic Scholar Graph API returned HTTP 429 rate-limit responses during direct scripted lookup. I therefore used web-indexed Semantic Scholar and publisher pages to identify likely matches.

## Resolution Summary

| Missing key | Status | Best match | DOI / link | Confidence |
|---|---|---|---|---|
| `zhou_chemos_2017` | Resolved as ChemOS, but year/key should be corrected | Roch et al., "ChemOS: An orchestration software to democratize autonomous discovery" | DOI: `10.1371/journal.pone.0229862`; Semantic Scholar PDF indexed | High |
| `gao_autonomous_2023` | Resolved as A-Lab, but key should be replaced | Szymanski et al., "An autonomous laboratory for the accelerated synthesis of inorganic materials" | DOI: `10.1038/s41586-023-06734-w`; Semantic Scholar page available | High |
| `granda_labos_2018` | Not resolved as written | Possible nearby paper: Steiner et al., "Organic synthesis in a modular robotic system driven by a chemical programming language" | DOI: `10.1126/science.aav2211` | Low; verify intended citation |
| `stokes_autonomous_2024` | Not resolved as written | Search results did not identify an AutoSyn 2024 Stokes paper. Nearby AutoSyn article: "Fully Automated Chemical Synthesis: Toward the Universal Synthesizer" | DOI: `10.1021/acs.oprd.0c00143` | Low; verify intended citation |

## Recommended Bibliography Fixes

1. Replace `zhou_chemos_2017` with a valid key such as `roch_chemos_2020`, or cite the existing ChemOS 2.0 key `sim_chemos_2024` if the intended claim is about the newer architecture.
2. Replace `gao_autonomous_2023` with the existing `szymanski_autonomous_2023` key for A-Lab.
3. Verify whether `granda_labos_2018` is intended to cite a LabOS paper or the Cronin/Granda modular robotic synthesis paper.
4. Verify whether `stokes_autonomous_2024` is intended to cite AutoSyn, automated chemical synthesis, or a different Stokes paper.

## Sources Used

- Semantic Scholar indexed ChemOS PDF: `https://pdfs.semanticscholar.org/45bb/a8fbbdb848f695e0f8d96ad8aec48a254cd6.pdf`
- Semantic Scholar page for A-Lab discovered via search: `https://www.semanticscholar.org/paper/76e657339380b426ab26902b0d47e208e1ee91e4`
- PLOS One ChemOS article: `https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229862`
- Nature A-Lab article: `https://www.nature.com/articles/s41586-023-06734-w`
- ACS AutoSyn article: `https://doi.org/10.1021/acs.oprd.0c00143`

