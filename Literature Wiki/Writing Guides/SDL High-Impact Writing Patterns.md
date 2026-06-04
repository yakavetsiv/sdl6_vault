# Writing Patterns From Highly Cited Self-Driving Lab Papers

Source set: downloaded and converted SDL literature in `literature/pdfs/self_driving_labs`, especially Burger 2020, Szymanski 2023, Boiko 2023, Abolhasani 2023, Coley 2019, Stein 2019, Roch 2020, and MacLeod 2020. Citation ranking is recorded in `literature/pdfs/self_driving_labs/most_cited_self_driving_labs.md`.

## Executive Pattern

High-impact SDL papers do not present automation as the novelty by itself. They present a bottleneck in scientific discovery, show why existing workflows cannot overcome it, then demonstrate a closed-loop system that changes what can be attempted experimentally.

The recurring narrative is:

1. A large scientific problem requires searching a space too complex for conventional experimentation.
2. Automation alone is insufficient because the bottleneck is decision-making, integration, or adaptation.
3. The work introduces an autonomous loop that connects planning, execution, measurement, and learning.
4. The system is demonstrated on a real scientific task with concrete scale: days of operation, number of experiments, dimensionality, targets, success rate, or improvement factor.
5. The conclusion generalizes from the case study to a broader class of laboratories or discovery problems.

For the LH_BO paper, the analogous story should be:

1. SDLs depend on liquid transfers, but liquid-handler calibration remains manual, liquid-specific, and fragile.
2. Vendor liquid classes and ISO checks validate performance but do not generate new parameter sets for non-standard biological liquids.
3. The work introduces a modular closed-loop calibration system that learns liquid-specific pipetting protocols under a one-plate measurement budget.
4. It demonstrates cross-platform operation, multi-objective optimization, human/robot benchmarking, and interpretable parameter regimes across viscosity.
5. The broader claim is that reliable liquid handling is an enabling infrastructure layer for biological SDLs.

## Abstract Style

The top SDL papers use abstracts with a strict four-move structure:

| Move | Function | Common style |
|---|---|---|
| Problem | Establish field-level need | “To close the gap between...” / “Accelerating discovery requires...” |
| System | Name the platform or framework | “We introduce...” / “Here we show...” |
| Demonstration | Quantify scale and outcome | “Over X days...” / “performing Y experiments...” / “identified Z-fold improvement...” |
| Generalization | State why it matters beyond the example | “This motivates...” / “This modular approach could...” |

Useful abstract template for LH_BO:

> Self-driving laboratories require reliable liquid transfer, but calibration of automated liquid handlers remains a slow, liquid-specific bottleneck for biological fluids whose viscosity, wetting, and time sensitivity differ from aqueous standards. Here we introduce a modular closed-loop calibration framework that couples robotic execution, volume measurement, Bayesian optimization, and interpretable surrogate analysis to learn liquid-specific pipetting parameters within a fixed one-plate measurement budget. Across five liquids spanning approximately three orders of magnitude in viscosity, the system identifies accurate transfer protocols and reveals distinct operating regimes governed by overaspiration, aspiration dynamics, or dispense dynamics. Cross-platform validation and human/robot benchmarking show that calibrated low-cost automation can exceed default commercial and manual performance. These results position liquid-class learning as a reusable infrastructure layer for biological self-driving laboratories.

## Introduction Pattern

Highly cited SDL introductions tend to start broad but become concrete quickly. They avoid long literature catalogs before the problem is defined.

Typical paragraph sequence:

1. Global or field bottleneck: discovery is slow because experimental spaces are high-dimensional and expensive.
2. Why current approaches fail: computation, screening, manual trial-and-error, or automation alone cannot close the loop.
3. Prior SDL progress: examples establish momentum but leave a specific unresolved gap.
4. Gap statement: one missing capability limits deployment.
5. Contribution statement: the current work closes that gap with quantified scope.

For LH_BO, the current introduction is close, but it should sharpen the field-level frame before moving into calibration details. The opening should make the reader understand that liquid handling is not a peripheral method detail; it is a hidden reliability layer for SDLs.

Recommended opening logic:

> Self-driving laboratories convert scientific discovery into an iterative loop between experiment planning, robotic execution, measurement, and model update. In biological SDLs, this loop is only as reliable as the liquid transfers that instantiate each planned experiment.

Then move immediately to the unresolved bottleneck:

> Automated liquid handlers are widely deployed, but their default liquid classes are calibrated for standard aqueous conditions and do not adapt to viscous, polymeric, or cell-associated fluids. Thus, the autonomy of the workflow is interrupted by manual, per-liquid calibration.

## Claim Style

The most cited SDL papers make claims at three levels:

1. **System claim:** what was built.
2. **Performance claim:** what it did quantitatively.
3. **Conceptual claim:** what principle the result establishes.

For LH_BO:

| Claim type | Strong phrasing |
|---|---|
| System | “We introduce a modular closed-loop calibration framework for liquid-handler parameter learning.” |
| Performance | “The framework reaches <2% APD across five liquids within a 96-measurement budget.” |
| Conceptual | “Liquid handling should be treated as a learnable, liquid-specific control problem rather than a static vendor liquid class.” |

Avoid making the conceptual claim too late. It should appear in the abstract, final introduction paragraph, and discussion.

## Quantification Pattern

Influential SDL papers quantify scale early:

- Burger: 8 days, 688 experiments, 10-variable space, 6-fold improvement.
- Szymanski: 17 days, 58 targets, 41 compounds, literature-trained recipe generation, active-learning loop.
- MacLeod: autonomous thin-film optimization with composition and processing variables.
- Roch: five applications across different automated equipment.

For LH_BO, the strongest quantitative hooks are:

- 32 trials x 3 replicates = 96 measurements per liquid condition.
- Five liquids spanning approximately 1-1490 mPa*s.
- <2% APD for all liquids under calibrated conditions.
- 10-fold parameter spread in aspiration speed and 6-48 uL overaspiration range.
- Human glycerol median APD 21.3% vs Hamilton 8.6%; N9 calibrated water APD 0.39%.
- Cross-platform execution on syringe-pump and air-displacement systems.

These should appear before detailed mechanism sections. Numbers make the work legible and citable.

## Figure Pattern

High-impact SDL figures usually follow this order:

1. **System overview:** closed-loop architecture and physical platform.
2. **Task and search space:** what the system is optimizing.
3. **Autonomous run results:** convergence, success, or improvement over time.
4. **Mechanistic interpretation:** what the model learned or why it worked.
5. **Generalization:** multiple tasks, platforms, materials, or conditions.

For LH_BO:

| Figure | Purpose |
|---|---|
| Fig. 1 | Closed-loop calibration framework plus N9/Hamilton platforms. |
| Fig. 2 | Liquid-specific parameter regimes and SHAP interpretation. |
| Fig. 3 | Optimization performance versus quasi-random search. |
| Fig. 4 | Human/commercial/default/calibrated benchmarking. |
| Fig. 5 | Cross-platform or multi-volume validation. |

Every figure should answer one claim. Avoid panels that only document workflow details unless they support a claim about portability, autonomy, or reliability.

## Discussion Pattern

The strongest SDL discussions do not repeat results. They translate the demonstration into design rules:

- What part of the discovery loop was previously missing?
- Which component made the loop autonomous?
- What remains hard to automate?
- What must be standardized for the field to scale?

LH_BO discussion should emphasize:

1. Calibration is an autonomous-experimentation problem, not a maintenance task.
2. Liquid-specific protocols are necessary because viscosity and wetting change the dominant control parameters.
3. One-plate calibration budgets make deployment realistic.
4. Cross-platform abstraction matters because SDLs are heterogeneous.
5. Future biological SDLs need liquid-handling metadata, calibration provenance, and transfer-quality monitoring.

## Style Rules Observed

Use:

- Active, concrete verbs: introduce, demonstrate, integrate, identify, reveal, close the loop.
- Measured claims before interpretation.
- Named systems or frameworks to make the contribution memorable.
- “Here we...” sparingly but decisively for the central contribution.
- Field-level nouns: bottleneck, platform, loop, workflow, search space, autonomy, integration, deployment.

Avoid:

- Long method catalogues before the reader knows the problem.
- “Novel” without specifying what capability is newly enabled.
- Treating robotics, BO, or software as independent contributions if the real contribution is the integrated loop.
- Overstating generality without a cross-platform, multi-liquid, or multi-task demonstration.
- Hiding negative or noisy results; high-impact SDL papers often use failure modes to make the system more credible.

## Recommended Rewrite Strategy For LH_BO

1. Put the SDL reliability bottleneck in the first two sentences.
2. Move ISO/vendor liquid classes into the “why current solutions fail” paragraph.
3. Make prior work a gap map, not a list: calibration, hardware adaptation, closed-loop optimization, orchestration.
4. End the introduction with three contribution bullets in prose:
   - one-plate multi-objective liquid-class learning,
   - cross-platform deployment,
   - interpretable liquid-specific parameter regimes.
5. In Results, lead with the strongest result summary before subsections.
6. In Discussion, claim “calibration as infrastructure for biological SDLs,” not merely better pipetting.

## Sentence Patterns To Emulate

Problem setup:

> Self-driving laboratories promise autonomous scientific iteration, but their reliability depends on low-level experimental operations that are rarely optimized as part of the loop.

Gap:

> Existing liquid classes validate whether a transfer is acceptable; they do not learn how a new biological liquid should be transferred.

Contribution:

> Here we treat liquid-handler calibration as a closed-loop experimental optimization problem.

Scale:

> Within a fixed 96-measurement budget per liquid, the framework learns protocols for liquids spanning three orders of magnitude in viscosity.

Mechanism:

> Surrogate interpretation reveals that different liquids are controlled by different physical levers: volume offset for water-like solvents, aspiration dwell for glycerol, and coupled aspiration/dispense dynamics for polymer solutions.

Impact:

> These results recast liquid handling from a static vendor setting into a learnable infrastructure layer for biological self-driving laboratories.

## Editorial Checklist

Before submission, each major section should answer:

- What field-level bottleneck does this section address?
- What quantitative evidence supports the claim?
- What does the reader learn that generalizes beyond this instrument?
- Is the result framed as part of a closed loop?
- Are limitations described as design constraints rather than apologies?

