---
type: literature-note
status: reading-notes-extracted
source_type: pdf
source_path: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Uriah-Israel-2025-Feb-16-CellSAM--A-Foundation-Model-for-Cell-Segmentation.pdf"
source_file: "Uriah-Israel-2025-Feb-16-CellSAM--A-Foundation-Model-for-Cell-Segmentation.pdf"
year: "2025"
author_hint: "Uriah Israel"
topics:
  - "Foundation Models"
  - "Computer Vision for Biology"
  - "Digital Twins and Modeling"
tags:
  - "literature/seed"
  - "topic/foundation-models"
  - "topic/computer-vision-for-biology"
  - "topic/digital-twins-and-modeling"
---

# Feb 16 CellSAM: A Foundation Model for Cell Segmentation

## Handle
Likely about extracting biological state from images through segmentation, counting, representation learning, or model-assisted analysis.

## Why It Matters
- Connects to: [[Concept - Foundation Models]], [[Concept - Computer Vision for Biology]], [[Concept - Digital Twins and Modeling]]
- Use this note as a graph node first, then enrich it after reading the abstract and figures.

## Karpathy-Style Compression
- **One-line mental model:** Likely about extracting biological state from images through segmentation, counting, representation learning, or model-assisted analysis.
- **Core object:** experimental system, model, dataset, or workflow named in the title.
- **Useful when asking:** "What does this paper contribute to automated biological discovery?"

## Semantic Links
- [[Paper - Alexandra-Dunnum-VandeLoo-Sep-8,-2025-SAMCell--Generalized-label-free-biological-c]]
- [[Paper - 2020 iPSC Advances WadkinIntro Math Modelling]]
- [[Paper - 933a2911-7176-451f-8c84-304ee18e03ba ML Image Analysis]]
- [[Paper - Automatic Cell Counting With YOLOv5 A Fluorescence]]
- [[Paper - Digital twin enhanced three organ m]]
- [[Paper - hardman-et-al-2024-an-in-vitro-agent-based-modelling-approach-to-optimization-of-c]]

## Source
- [Open PDF](file:///Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Uriah-Israel-2025-Feb-16-CellSAM--A-Foundation-Model-for-Cell-Segmentation.pdf)
- Local path: `/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Uriah-Israel-2025-Feb-16-CellSAM--A-Foundation-Model-for-Cell-Segmentation.pdf`

## Reading Notes
- Abstract: Cells are a fundamental unit of biological organization, and identifying them in imaging data – cell segmentation – is a critical task for various cellular imaging experiments. While deep learning methods have led to substantial progress on this problem, most models are specialist models that work well for specific domains but cannot be applied across domains or scale well with large amounts of data. In this work, we present CellSAM, a universal model for cell segmentation that generalizes across diverse cellular imaging data.
- Key figure: from them, and make that knowledge accessible to life scientists via inference. In this work, we developed CellSAM, a foundation model for cell segmentation (Fig. 1). CellSAM extends the SAM methodology to perform automated cellular instance segmentation. To achieve this, we first assembled a comprehensive dataset for cell segmentation spanning five broad data archetypes: tissue, cell culture, yeast, H&E, and bacteria. Critically, we removed data leaks be
- Method: Uses image analysis or segmentation methods; confirm model architecture and evaluation details manually.
- Dataset/system: CellSAM: A Foundation Model for Cell Segmentation Uriah Israel1,3†, Markus Marks2,3†, Rohit Dilip3‡, Qilin Li2‡, Changhua Yu1, Emily Laubscher4, Ahamed Iqbal1, Elora Pradhan1, Ada Ates1, Martin Abt1, Caitlin Brown1, Edward Pao1, Shenyi Li1, Alexander Pearson-Goulart1, Pietro Perona2,3, Georgia Gkioxari3, Ross Barnowski1, Yisong Yue3, David Van Valen1,5* 1*Division of Biology and Biological Engineering, Caltech.
- Failure mode or limitation: Cell segmentation is also a key challenge for these experiments, as cells must be segmented and tracked to create temporally consistent records of cell behavior that can be queried at scale.
- Reusable idea for SDL6 / automation: Adapt the measurement or image-analysis pipeline as a reusable assay readout component for automated experiments.

## Knowledge Graph Edges
- `Paper - Feb 16 CellSAM A Foundation Model for Cell Segmentation` --mentions--> `Concept - Foundation Models`
- `Paper - Feb 16 CellSAM A Foundation Model for Cell Segmentation` --mentions--> `Concept - Computer Vision for Biology`
- `Paper - Feb 16 CellSAM A Foundation Model for Cell Segmentation` --mentions--> `Concept - Digital Twins and Modeling`
