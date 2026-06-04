---
type: writing-guide
status: draft
tags:
  - writing-guide
  - digital-discovery
  - tutorial-review
  - rsc
  - self-driving-labs
source_papers:
  - "[[Paper - DD Tutorial - lo2024_frugal_twin]]"
  - "[[Paper - DD Tutorial - lo2023_selfies_library]]"
  - "[[Paper - DD Tutorial - niroomand2024_energy_landscapes_ml]]"
  - "[[Paper - DD Tutorial - gaidimas2026_computer_vision_materials_synthesis]]"
  - "[[Paper - DD Tutorial - maroulis2026_self_driving_liquid_handling_lab]]"
related_maps:
  - "[[Map - Digital Discovery Tutorial Papers]]"
  - "[[Map - Self-Driving Lab Stack]]"
---

# Digital Discovery Tutorial Paper Writing Guide

This guide distills writing patterns from the imported Digital Discovery tutorial set, especially the highly cited frugal twin Tutorial Review, the SELFIES library Tutorial Review, the energy-landscapes-for-ML Tutorial Review, the computer-vision-for-materials-synthesis Tutorial Review, and the tutorial-style self-driving liquid-handling guide.

## Core Principle

An impactful tutorial paper is not a long review with extra examples. It is an onboarding machine for a field: it identifies a capability that many readers need, explains why current routes are hard, gives a conceptual map, walks through a reusable workflow, demonstrates the workflow on a concrete case, and leaves the reader with enough code, data, hardware files, protocols, or decision rules to act.

For Digital Discovery, the strongest tutorial papers teach a capability at the intersection of chemistry, materials science, biotechnology, machine learning, automation, data workflows, or scientific hardware. The paper should make a reader more capable after reading it.

## Formal Digital Discovery Requirements

Digital Discovery labels these as `Tutorial Review` articles. RSC guidance says they should:

- Introduce and overview an important topic relevant to the journal readership.
- Explain the development of the subject, its current state, and likely future directions.
- May describe modern software tools, AI systems, hardware-control systems, or open hardware designs for synthesis or characterization.
- May target readers ranging from graduate students to faculty.
- Must not contain unpublished original research.
- Need accessible code and data when relevant, deposited in community or general repositories.
- Need persistent deposition for custom code on acceptance, such as Zenodo, Code Ocean, or equivalent archival repository.
- Need a Data Availability Statement, conflicts-of-interest statement, and normal RSC submission files.

Practical implication: a tutorial paper can include a case study, worked example, notebook, or demonstration, but the primary contribution must be educational synthesis and reusable guidance rather than new unpublished research results.

## What Makes The Paper Impactful

The imported papers share five impact moves:

1. They name a bottleneck that blocks broader adoption.
2. They define a concept or workflow that makes the field easier to enter.
3. They translate expert tacit knowledge into explicit steps, design rules, tables, and diagrams.
4. They demonstrate the workflow through a concrete case study.
5. They leave durable artifacts: code, notebooks, build guides, curated resources, repositories, or discussion spaces.

Examples from the source set:

- `lo2024_frugal_twin` succeeds by naming a memorable concept, the frugal twin, then using it to organize low-cost self-driving laboratory education, prototyping, modularity, and ethics.
- `lo2023_selfies_library` succeeds by explaining the evolution, grammar, API, design choices, and practical use of a software tool that many ML-for-molecules readers can use directly.
- `niroomand2024_energy_landscapes_ml` succeeds by translating a mature chemical-physics framework into machine-learning language, giving readers analogies and metrics for understanding black-box models.
- `gaidimas2026_computer_vision_materials_synthesis` succeeds by turning computer vision into an experimentalist-ready roadmap: imaging, annotation, training, validation, deployment, and limitations.
- `maroulis2026_self_driving_liquid_handling_lab` is formally a Paper, but tutorial-style: it combines active-learning concepts, low-cost liquid-handler implementation, notebooks, build guides, and practical adoption paths.

## Choose A Tutorial Topic

Use this scorecard before drafting.

| Criterion | Strong topic | Weak topic |
|---|---|---|
| Reader pain | Many chemists/materials/biotech researchers want the capability but lack a clear starting route. | Only specialists already know why it matters. |
| Timeliness | The field has enough examples to synthesize but no practical entry guide. | Either too mature and over-reviewed, or too new with little evidence. |
| Reusability | The paper can teach a workflow, decision tree, toolchain, or design principle. | The paper mainly summarizes papers chronologically. |
| Digital Discovery fit | Accelerates discovery through ML, AI, robotics, databases, high-throughput workflows, or open hardware. | Low-throughput computational or mechanistic analysis without data/automation relevance. |
| Artifacts | Can provide code, data, notebooks, build files, tables, or curated resources. | No reusable artifact can be shared. |
| Audience bridge | Helps one community adopt another community's tools. | Written only for people already fluent in both domains. |

A strong topic sentence looks like:

> Many [target readers] want to use [capability], but adoption is limited by [specific bottleneck]. This tutorial provides [roadmap/toolchain/design framework] for [concrete use case], with [reusable artifact].

## Define The Reader

Impactful tutorials are explicit about reader level. Pick one primary reader and write to them consistently.

| Reader | What they need |
|---|---|
| Graduate student | Vocabulary, minimal prerequisites, stepwise workflow, pitfalls, examples. |
| Experimentalist | Hardware/software stack, sample preparation, data collection, validation, troubleshooting. |
| Computational scientist | Domain constraints, data-generation realities, evaluation metrics, deployment limits. |
| Faculty or lab lead | Field map, adoption cost, infrastructure choices, reproducibility and training value. |
| Tool builder | API design, integration points, benchmarks, failure modes, extension paths. |

Do not write for everyone equally. Write for one primary reader, then include sidebars or tables for adjacent readers.

## Title Patterns

Good titles make the tutorial promise legible.

Use one of these patterns:

- `A user's guide to [first/practical workflow]`
- `[Technique] for [domain]: a tutorial for [audience]`
- `Review of [topic]: the [memorable concept] concept`
- `Recent advances in the [tool/library/framework]`
- `Insights into [new field] from [mature field]: a [framework] approach`

A strong title should contain at least two of: method, domain, audience, concept, tool, or use case.

## Abstract Formula

Use a five-move abstract. Each move should be one to three sentences.

| Move | Job | Example phrasing |
|---|---|---|
| Field opportunity | Establish why the capability matters now. | "High-throughput automation is expanding the scale of materials discovery." |
| Adoption bottleneck | Name what blocks readers. | "However, characterization remains sequential, costly, and difficult to integrate." |
| Tutorial promise | State what the paper teaches. | "Here we provide a structured tutorial for experimentalists to build..." |
| Concrete roadmap | List the workflow components. | "We cover image acquisition, annotation, model training, performance evaluation, and deployment." |
| Reusable outcome | Say what readers can do after reading. | "The tutorial equips readers to adapt the workflow to their own synthesis tasks." |

Template:

> [Field] is transforming [domain] by enabling [capability]. However, [specific bottleneck] limits adoption by [target readers]. Here we provide a tutorial introduction to [topic], organized around [framework/workflow]. We cover [component 1], [component 2], [component 3], and [component 4], and demonstrate the approach using [case study]. By making [tacit knowledge] explicit, this tutorial equips [audience] to [actionable outcome] and highlights [future direction].

## Introduction Architecture

The best introductions move from field-level need to specific reader pain quickly.

Recommended sequence:

1. **Field acceleration:** Why this capability matters for discovery.
2. **Adoption gap:** Why current papers, tools, or workflows are insufficient for newcomers.
3. **Audience statement:** Who this tutorial is for and what background is assumed.
4. **Scope boundary:** What the tutorial covers and intentionally does not cover.
5. **Roadmap:** How the paper is organized.
6. **Reusable contribution:** What resources or artifacts accompany the paper.

Avoid opening with a literature catalog. Define the problem first, then cite selectively.

Strong gap language:

- "Despite growing examples, practical guidance remains fragmented."
- "Newcomers often face a steep learning curve because hardware, software, and validation decisions are discussed separately."
- "The field lacks a shared vocabulary for comparing low-cost surrogates of high-cost autonomous systems."
- "Existing reviews describe applications, but do not provide an implementation path for experimentalists."

## Section Blueprint

A comprehensive tutorial paper can use this structure.

### 1. Conceptual Map

Define the key concept, vocabulary, and boundaries. The frugal twin paper does this well by naming the concept and distinguishing simple examples, low-cost surrogates, and high-cost systems.

Include:

- Definitions.
- What is in scope and out of scope.
- Relationship to adjacent terms.
- Diagram of the conceptual landscape.
- Table comparing categories.

### 2. Historical Development And Current State

Do not make this a chronological dump. Organize history around capabilities.

Possible capability axes:

- Manual to automated.
- Closed-loop to self-driving.
- Proprietary to open-source.
- Single-task to modular.
- Human-interpreted to AI-assisted.
- Demonstration-only to reusable infrastructure.

### 3. Practical Workflow

This is the tutorial core. Convert expert practice into steps.

For each step, include:

- Purpose.
- Inputs.
- Outputs.
- Key decisions.
- Minimal viable implementation.
- Common mistakes.
- Validation check.

Example workflow for an SDL tutorial:

1. Define target property and constraints.
2. Choose experiment space and measurement budget.
3. Select hardware and orchestration stack.
4. Seed initial data.
5. Train surrogate model.
6. Choose acquisition function.
7. Execute recommended experiment.
8. Validate measurement quality.
9. Update model and repeat.
10. Archive data, code, metadata, and provenance.

### 4. Worked Case Study

Every strong tutorial needs a concrete case study, but the case study should teach the method rather than compete as a new research result.

A good case study includes:

- Why this case is representative.
- Starting assumptions.
- Dataset or hardware setup.
- Step-by-step decisions.
- Results that illustrate the workflow.
- Failure modes and troubleshooting.
- What changes for other use cases.

### 5. Tools, Resources, And Implementation Details

Readers need a practical stack.

Include tables for:

- Software libraries and when to use each.
- Hardware components or instruments.
- Data formats and metadata requirements.
- Annotation tools or control software.
- Repositories and notebooks.
- Cost/complexity tradeoffs.

The computer-vision tutorial is a good model: it names the hardware and software stack, then describes acquisition, annotation, training, and evaluation.

### 6. Validation And Evaluation

Tutorial papers are more credible when they teach how to know whether the workflow worked.

Include:

- Metrics.
- Baselines.
- Negative controls.
- Calibration checks.
- Uncertainty or error analysis.
- Reproducibility expectations.
- Failure cases.

For AI/ML tutorials, evaluation must include model validation and domain validation. For hardware tutorials, evaluation must include physical performance and operational reliability.

### 7. Limitations And Failure Modes

Impactful tutorials are honest about where the approach fails. This increases trust.

Turn limitations into design guidance:

- When not to use the method.
- What assumptions must hold.
- What data quality is required.
- What hardware constraints matter.
- What scaling problems remain.
- What human expertise is still needed.

### 8. Future Directions

Future directions should be specific enough to guide research.

Good future directions:

- Standardized benchmark datasets.
- Shared metadata schemas.
- Better integration with orchestration systems.
- Lower-cost hardware modules.
- More robust evaluation under real lab noise.
- Community repositories and living resources.

Weak future directions:

- "More work is needed."
- "This field will continue to grow."
- "AI will transform chemistry."

## Figure Strategy

A tutorial paper should teach visually. Use figures to reduce cognitive load.

| Figure type | Purpose |
|---|---|
| Concept map | Define terms and relationships. |
| Workflow schematic | Show the end-to-end process. |
| Stack diagram | Connect hardware, software, data, and user decisions. |
| Decision tree | Help readers choose methods. |
| Case-study pipeline | Ground the tutorial in a concrete example. |
| Failure-mode panel | Teach troubleshooting. |
| Future-roadmap figure | Show where the field can go. |

Recommended first five figures:

1. Field bottleneck and tutorial scope.
2. End-to-end workflow.
3. Toolchain or architecture.
4. Worked case study with data/results.
5. Decision rules, pitfalls, and future extensions.

Each figure should answer one reader question. If a figure only decorates the paper, remove it.

## Table Strategy

Tutorial reviews should be table-rich because tables convert expertise into reusable reference material.

High-value tables:

- Glossary of terms.
- Comparison of methods/tools/hardware.
- Minimum viable setup vs advanced setup.
- Common pitfalls and fixes.
- Data requirements and metadata fields.
- Evaluation metrics and when to use them.
- Repository/resource list.
- Do/don't checklist.

A table should let the reader make a decision faster.

## Reproducibility Package

For Digital Discovery, the tutorial should be accompanied by reusable artifacts wherever possible.

Minimum package:

- Public repository.
- Persistent archive with DOI.
- README with environment setup.
- Example notebook or script.
- Example input data.
- Expected output files.
- License.
- Data Availability Statement.

For software tutorials:

- Version-pinned environment.
- Minimal working example.
- API examples.
- Benchmark or validation script.
- Explanation of design choices.

For hardware tutorials:

- Bill of materials.
- CAD/build files.
- Assembly instructions.
- Calibration procedure.
- Safety notes.
- Validation protocol.
- Failure modes.

For ML/AI tutorials:

- Training data or toy data.
- Preprocessing scripts.
- Model configuration.
- Evaluation metrics.
- Uncertainty/failure analysis.
- Guidance on domain shift.

## Writing Style

Use direct educational language. A tutorial paper should feel authoritative but not opaque.

Use:

- "This tutorial aims to equip..."
- "We first introduce..."
- "We then show how..."
- "For readers implementing this workflow..."
- "A minimal implementation requires..."
- "This choice matters because..."
- "In practice, failure often occurs when..."

Avoid:

- Excessive novelty claims.
- Long unstructured literature summaries.
- Acronyms before definitions.
- Tool lists without decision guidance.
- Equations without implementation intuition.
- Case studies with no reusable lesson.
- Claims of generality without scope boundaries.

## Citation Strategy

Citations should support learning, not just coverage.

Use citations for:

- Foundational concepts.
- Representative applications.
- Best existing tools.
- Benchmark datasets.
- Known limitations.
- Alternative approaches.

Do not cite every paper in the field. Tutorial readers need the shortest reliable path through the literature.

A useful citation paragraph follows this logic:

1. Foundational method.
2. Representative domain applications.
3. Current limitation or fragmented practice.
4. Why this tutorial is needed.

## Submission Positioning

A strong cover-letter argument should answer:

- Why Digital Discovery readers need this tutorial now.
- What specific capability the article teaches.
- Which communities it bridges.
- What reusable resources accompany the manuscript.
- Why it is not just another review.

Cover-letter skeleton:

> We submit this manuscript as a Tutorial Review for Digital Discovery because it provides an implementation-oriented introduction to [topic], a capability increasingly important for [chemistry/materials/biotechnology discovery]. While recent studies demonstrate [field progress], practical guidance for [target audience] remains fragmented across [software/hardware/domain literature]. Our tutorial synthesizes these developments into [framework/workflow], demonstrates the workflow through [case study], and provides [repository/notebooks/data/build files] to support adoption. We believe this article will be useful to Digital Discovery readers interested in [AI/robotics/data workflows/open hardware/high-throughput discovery].

## Quality Checklist

Before submission, confirm that the manuscript satisfies every item below.

### Fit And Scope

- The paper is anchored in accelerated discovery, AI/ML, robotics, databases, data workflows, or open scientific hardware.
- The topic is relevant to chemistry, materials science, biotechnology, or adjacent physical/biological sciences.
- The manuscript teaches a capability rather than only summarizing a literature area.
- The article contains no unpublished original research as its main claim.

### Reader Value

- The target reader is named or obvious.
- Required background is stated.
- Key terms are defined early.
- The paper gives a path from beginner understanding to implementation.
- The reader can reuse at least one workflow, decision tree, code resource, dataset, or design rule.

### Narrative

- The abstract has field opportunity, adoption bottleneck, tutorial promise, roadmap, and reusable outcome.
- The introduction reaches the specific gap quickly.
- The paper explains why existing reviews or examples are insufficient.
- The contribution is framed as educational infrastructure for the community.
- The conclusion returns to future directions and field-level adoption.

### Technical Substance

- The workflow is stepwise and actionable.
- The case study illustrates the workflow clearly.
- Evaluation metrics and validation procedures are explained.
- Limitations and failure modes are explicit.
- Tables and figures support decisions, not decoration.

### Reproducibility

- Code and data are accessible during review.
- Custom code is deposited in a persistent repository on acceptance.
- Repository has installation instructions and expected outputs.
- Data Availability Statement is present.
- Conflicts of interest are declared.
- Licenses are clear for code, data, and hardware files.

## One-Page Planning Template

Use this before writing.

| Field | Fill in |
|---|---|
| Working title |  |
| Target reader |  |
| Reader pain point |  |
| Capability taught |  |
| Digital Discovery fit |  |
| Main concept or framework |  |
| Case study |  |
| Reusable artifact |  |
| Key figures |  |
| Key tables |  |
| Known limitations |  |
| Future directions |  |
| Repository/archive plan |  |

## Fast Draft Outline

1. Abstract.
2. Introduction: field need, adoption gap, audience, roadmap.
3. Conceptual foundations: terms, history, current state.
4. Practical workflow: step-by-step implementation.
5. Tools and resources: software/hardware/data stack.
6. Case study: demonstrate the workflow.
7. Validation and troubleshooting: metrics, failure modes, checks.
8. Best practices: design rules and decision tables.
9. Future directions: standards, benchmarks, integration, community resources.
10. Data/code availability, conflicts, acknowledgements.

## Sentence Bank

Problem:

> Despite rapid growth in [field], practical adoption remains limited by [bottleneck].

Audience:

> This tutorial is intended for [audience] who are familiar with [baseline knowledge] but new to [capability].

Gap:

> Existing studies demonstrate what is possible, but implementation details remain distributed across domain-specific literatures.

Contribution:

> Here we provide a structured roadmap for [capability], from [first step] to [validated outcome].

Scope:

> We focus on [included scope] and do not attempt to cover [excluded scope].

Case study:

> To make the workflow concrete, we illustrate each step using [case study].

Limitations:

> This approach is most useful when [assumption]; it is less appropriate when [failure condition].

Impact:

> By making [tacit practice] explicit, this tutorial lowers the barrier to [community outcome].

## Skill Card

When writing or reviewing a Digital Discovery Tutorial Review, act as an implementation-oriented editor.

Ask:

1. What can the reader do after reading this paper that they could not do before?
2. What bottleneck does the tutorial remove?
3. What concept, workflow, or decision framework organizes the paper?
4. Where is the concrete worked example?
5. What artifacts make the tutorial reusable?
6. What limitations prevent misuse?
7. Why is Digital Discovery the right venue?

If any answer is vague, revise before polishing prose.
