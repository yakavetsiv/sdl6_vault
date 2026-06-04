---
type: literature-note
status: reading-notes-extracted
source_type: pdf
source_path: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/2603.15553v1.pdf"
source_file: "2603.15553v1.pdf"
year: ""
author_hint: ""
topics:
  - "Research Papers"
tags:
  - "literature/seed"
  - "topic/research-papers"
---

# 2603.15553v1

## Handle
Seed literature note generated from filename metadata; full abstract-level summary still needs extraction.

## Why It Matters
- Connects to: [[Concept - Research Papers]]
- Use this note as a graph node first, then enrich it after reading the abstract and figures.

## Karpathy-Style Compression
- **One-line mental model:** Seed literature note generated from filename metadata; full abstract-level summary still needs extraction.
- **Core object:** experimental system, model, dataset, or workflow named in the title.
- **Useful when asking:** "What does this paper contribute to automated biological discovery?"

## Semantic Links
- [[Paper - 1-s2.0-S0272884222036471-main]]
- [[Paper - 1-s2.0-S0272884224059509-main]]
- [[Paper - 1-s2.0-S1385894725029535-main]]
- [[Paper - 1-s2.0-S259025712200030X-main]]
- [[Paper - 10.48550 arxiv.2501.06039]]
- [[Paper - 1010 001 dec2025 iy]]

## Source
- [Open PDF](file:///Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/2603.15553v1.pdf)
- Local path: `/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/2603.15553v1.pdf`

## Reading Notes
- Abstract: The landscape of self-supervised learning (SSL) is currently dominated by generative approaches (e.g., MAE) that reconstruct raw low-level data, and predictive approaches (e.g., I-JEPA) that predict high-level abstract embeddings. While generative methods provide strong grounding, they are computationally inefficient for high-redundancy modalities like imagery, and their training objective does not prioritize learning high-level, conceptual features. Conversely, predictive methods often suffer from training instability due to their reliance on the non-stationary targets of final-layer self-distillation.
- Key figure: f channels. ∗Correspondence: scott.lowe@vectorinstitute.ai 1 Bootleg: Self-distillation of hidden layers for SSL Scott C. Lowe, et al. (2026) Figure 1: Multi-layer self-distillation with Bootleg. The teacher-encoder (blue), student-encoder (green), and predictor (orange) are ViTs, made of repeated transformer blocks. A schematic of a single transformer block is overlaid (bottom right). The teacher-encoder is an EMA of the student-encoder, and pro
- Method: ViT-S/16 MAE CrossMAE data2vec 2.0 I-JEPA Bootleg (ours) Data IN-1k IN-1k IN-1k IN-1k IN-1k Ep. The student-encoder starts by embedding all unmasked patches into tokens.
- Dataset/system: We introduce Bootleg, a method that bridges this divide by tasking the model with predicting latent representations from multiple hidden layers of a teacher network.
- Failure mode or limitation: However, both have their own disadvantages.
- Reusable idea for SDL6 / automation: Adapt the measurement or image-analysis pipeline as a reusable assay readout component for automated experiments.

## Knowledge Graph Edges
- `Paper - 2603.15553v1` --mentions--> `Concept - Research Papers`
