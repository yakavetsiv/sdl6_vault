---
title: CFI Equipment Notes — Brandon Version
date: 2026-06-04
project: SDL6-HOM
type: source
tags:
  - CFI
  - SDL6
  - HOM
  - equipment
  - Brandon
  - draft
---

# CFI Equipment Notes — Brandon Version
**Source:** `OneDrive/.../SDL6 - HOM/Data (secure)/Grants/CFI 2024/CFI _ Brandon.docx`  
**Type:** Equipment justification draft with cost breakdown  

---

## Equipment Categories & Costs

### High-Fidelity Model Validation
| Item | Cost |
|---|---|
| High-content automated imaging system (UV-VIS + fluorescence + luminescence + confocal 3D) | $1,000K |
| High-throughput proteomics/metabolites screening system | $400K |
| High-resolution 3D printer | $200K |

### Drug Compound Screening
| Item | Cost |
|---|---|
| High-precision liquid dispensing (e.g., Echo 650, pico-nanoliter resolution) | $700K |
| Collaborative robots | $80K |

### ML-Based Analysis
| Item | Cost |
|---|---|
| High-throughput automated cell sorter and flow cytometer (e.g., Union BioSorter) | $300K |

---

## Key Justification Points from Document

**Imaging system:**
- Multimodal data critical for AI/ML integration (10x more data collected)
- High-throughput enables large compound libraries (1536-well plates, 4-16x throughput increase)
- Temperature/CO₂/humidity control required for culture model maintenance

**Proteomics/metabolomics:**
- Cytokine and inflammation marker quantification
- Real-time biomolecular monitoring for organ-specific toxicity/efficacy
- Longitudinal drug trials, patient stratification

**3D printer:**
- Custom well plates with micro/nanoscale features
- Organ-on-chip device fabrication without thermal bonding
- Microgrooves, ridges, hanging structures for cell guidance

---

> [!NOTE] Instrument Selection Pivot
> Brandon version uses Echo liquid handler, Union BioSorter, and a proteomics system. The final CFI list pivoted to a standard organoid-compatible liquid handler, confocal imaging plate reader, and well-plate flow cytometer — simpler stack, same capability coverage.

## Notes vs. Final Equipment List
Brandon version uses different instrument selection (Echo liquid handler, Union BioSorter, proteomics system). Final CFI HOM equipment list pivoted to:
- Versa/standard liquid handler with organoid-compatible modules
- Imaging plate reader (confocal) instead of separate imaging system
- Standard well-plate flow cytometer instead of cell sorter
