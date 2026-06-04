---
type: literature-note
status: reading-notes-extracted
source_type: pdf
source_path: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/2111.06377v3.pdf"
source_file: "2111.06377v3.pdf"
year: ""
author_hint: ""
topics:
  - "Research Papers"
tags:
  - "literature/seed"
  - "topic/research-papers"
---

# 2111.06377v3

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
- [Open PDF](file:///Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/2111.06377v3.pdf)
- Local path: `/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/2111.06377v3.pdf`

## Reading Notes
- Abstract: This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision. Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels. First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that reconstructs the original image from the latent representation and mask tokens.
- Key figure: ked autoencoders, a form of more general denoising autoencoders [58], is natural and applicable in computer vision as well. Indeed, closely related research Figure 1. Our MAE architecture. During pre-training, a large random subset of image patches (e.g., 75%) is masked out. The encoder is applied to the small subset of visible patches. Mask tokens are introduced after the encoder, and the full set of encoded patches and mask tokens is processed by a small de
- Method: supervised MoCo v3 BEiT MAE pre-train data IN1K w/ labels IN1K IN1K+DALLE IN1K ViT-B 47.4 47.3 47.1 48.1 ViT-L 49.9 49.1 53.3 53.6 Table 4. COCO object detection and segmentation using a ViT Mask R-CNN baseline.
- Dataset/system: Coupling these two designs enables us to train large models efﬁciently and effectively: we accelerate training (by 3× or more) and improve accuracy.
- Failure mode or limitation: However, despite significant interest in this idea following the success of BERT, progress of autoencoding methods in vision lags behind NLP.
- Reusable idea for SDL6 / automation: Adapt the measurement or image-analysis pipeline as a reusable assay readout component for automated experiments.

## Knowledge Graph Edges
- `Paper - 2111.06377v3` --mentions--> `Concept - Research Papers`
