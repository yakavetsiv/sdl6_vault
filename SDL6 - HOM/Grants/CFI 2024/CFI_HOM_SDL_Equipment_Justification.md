---
title: CFI Grant — HOM SDL Equipment Justification
date: 2026-06-04
project: SDL6-HOM
type: output
tags:
  - sdl6
  - sdl6/nanomedicine
  - sdl6/organ-on-chip
  - sdl6/cfi
  - type/output
  - project/sdl6-hom
  - organoids
  - grant-writing
  - acceleration-consortium
---

# CFI Grant — HOM SDL Equipment Justification
**Project:** SDL6 - Human Organoid Module (HOM), Acceleration Consortium, University of Toronto  
**Grant:** CFI 2024 Pre-proposal  
**File:** `/Users/iyakavets/Documents/docs_claude/HOM_SDL_equipment_justification.md`  
**Session date:** 2026-06-04  

---

## Development Notes

### Scope
¾ to 1 page equipment description/justification for Human Organoid *ex vivo* SDL Suite + 1-2 paragraphs on human organoid models in preclinical drug/nanomedicine assessment.

### Equipment List (final)
| Instrument | Cost (CAD) | Role |
|---|---|---|
| Liquid Handling System (≥20 deck, cooling/shaking/tilting) | $300K | Sample prep, nanomedicine dispensing |
| Automated Cell Culture Incubator (37°C, 5% CO₂, 90% RH) | $100K | Culture maintenance |
| Automated 4°C Storage System | $100K | Cold-chain reagent/formulation access |
| Collaborative Robotic Arm (computer vision) | $100K | Physical integration layer |
| Imaging Plate Reader (WF + confocal + live-cell) | $400K | High-content data acquisition, AI loop |
| Flow Cytometry System (well-plate compatible) | $300K | Single-cell nanomedicine validation |
| **Total** | **$1.3M** | |

> [!INFO] Uniqueness Claim
> No existing Canadian platform couples nanomedicine formulation design with autonomous human tissue screening. This infrastructure establishes that capability at the Acceleration Consortium.

### Key Writing Decisions
- Narrative structured as workflow: sample prep → culture → reagent supply → integration → analytics
- Each instrument justified as essential to closed loop; absence of robotic arm argument included
- Nanomedicine focus woven throughout (not bolted on)
- OKR metrics integrated: 10h → <2h labour/week, >30 days walk-away
- CFI uniqueness claim: no Canadian platform couples nanomedicine formulation design with autonomous human tissue screening
- Section 2 retitled and refocused on nanomedicine; added: flow/advection for vascular barrier, immune co-culture advantage vs. rodents, patient genetics, parametric decoupling in organ-on-chip, concurrent toxicity+efficacy on same well plate

### Style Rules Applied
- No em-dashes (treated as AI artifact)
- /deslop applied multiple times
- /research-grants CFI register check passed
- Word counts: equipment section ~393 words (¾ page), organoid section ~185 words

---

## Final Text

### Equipment Description and Justification: Human Organoid *Ex Vivo* Self-Driving Laboratory Suite

The Human Organoid *ex vivo* Self-Driving Laboratory (SDL) Suite is an automated platform for high-throughput nanomedicine screening, drug delivery characterization, and toxicity testing using patient-derived human organoid and organ-on-chip models. The $1.3M CAD request covers six instruments forming a closed-loop system that minimizes manual material transfer, reduces hands-on labour to under two hours per sample per week, and sustains unattended operation exceeding 30 days. No existing Canadian platform couples nanomedicine formulation design directly with autonomous biological screening in human tissue models; this infrastructure establishes that capability at the Acceleration Consortium.

A liquid handling system ($300K CAD) with at least 20 deck positions and cooling, shaking/heating, and tilting modules dispenses culture media, nanomedicine formulations, and reagents across multi-well plates at high throughput. The cooling module preserves temperature-sensitive materials including Matrigel and nanoparticle suspensions; the tilting module enables accurate aspiration from three-dimensional organoid cultures. Prepared plates transfer directly to an automated cell culture incubator ($100K CAD) maintaining cultures at 37°C, 5% CO₂, and 90% relative humidity, eliminating manual handling between preparation and incubation and the contamination and dosing variability it introduces.

The automated 4°C storage system ($100K CAD) provides cold-chain access to nanomedicine formulations, biologics, and labile reagents throughout each run, preventing freeze-thaw cycling that compromises nanoparticle integrity. A collaborative robotic arm ($100K CAD) with computer vision transfers plates and consumables between all stations using SLAS-standard gripper dimensions, converting six instruments into a single autonomous workflow.

An imaging plate reader ($400K CAD) combining wide-field fluorescence, spinning-disk confocal microscopy, and live-cell imaging is integrated directly into the SDL workflow for automated high-content data collection. Confocal sectioning is required for organoid and organ-on-chip structures where cellular architecture extends through the z-axis, and is indispensable for resolving sub-cellular localization of nanomedicine carriers within intact tissue. Continuous automated acquisition across every plate generates the structured dataset required to close the AI feedback loop for nanoformulation optimization. A well-plate-compatible flow cytometry system ($300K CAD) adds single-cell quantification of nanomedicine uptake, endosomal escape, and intracellular distribution alongside viability and marker profiling within the same run, adding to the multimodal dataset available for AI-driven formulation decisions.

---

### Human Organoid Models for Nanomedicine Efficacy and Toxicity Assessment

> [!NOTE] Animal Model Limitation
> Rodents differ from humans in innate immune receptor repertoire and complement pathway activation — both govern nanoparticle clearance and toxicity — risks that animal studies routinely fail to detect.

Human organoids and organ-on-chip devices derived from patient biopsies or induced pluripotent stem cells carry patient-specific genetic material, reflecting inter-individual differences in receptor expression, enzyme activity, and immune function that cell lines erase and rodent models do not reproduce. Organ-on-chip systems support co-culture of immune cells with parenchymal tissue, allowing direct assessment of nanomedicine-induced inflammatory activation and complement response in a human immune context. Rodents differ from humans in innate immune receptor repertoire and complement pathway activation, both of which govern nanoparticle clearance and toxicity, risks that animal studies routinely fail to detect. Physiological flow and advection recreate the hemodynamic forces driving nanoparticle transport across vascular endothelium, a process static cultures cannot replicate and one that largely determines in vivo delivery efficiency.

Parameters such as shear rate, matrix stiffness, cell composition, and perfusion rate can be varied independently to identify what limits nanomedicine performance in vivo. The SDL platform assesses toxicity and efficacy concurrently in the same well plate, using multiplexed imaging and flow cytometry to capture both endpoints from a single run, cutting the number of assays per candidate and producing paired human-tissue data to strengthen the preclinical case for Canadian nanomedicine programs moving toward clinical evaluation.

---

## Related Notes
- [[OKR_SDL6]] — OKR metrics cited in equipment section
- [[SDL_HOM_research_objectives]] — V1/V2 rationale
- [[SDL_access_facility_overview]] — facility context

## Related Literature
- [[Map - Biofabrication and Cell Systems]]
- [[Paper - Collins,-Evan-2025-10-01-Self-driving-labs-for-biotechnology]]
- [[Paper - Organ On A Chip OOC Image Dataset for Machine Learning and Tissue Model Evaluation (2)]]
- [[Paper - Wenckstern,-Johann-2025-01-10-AI-powered-virtual-tissues-from-spatial-proteomics-f]]
- [[Paper - 2025.02.14.638383v1.full]] — lipid nanoparticle delivery
- [[Paper - s41587-024-02490-y]] — nanoparticle LNP
- [[Paper - s11671-021-03553-8]] — nanomedicine
