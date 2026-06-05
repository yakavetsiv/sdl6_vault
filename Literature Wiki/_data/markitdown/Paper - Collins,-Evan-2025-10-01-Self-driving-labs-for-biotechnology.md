---
type: literature-note
source_note: "Papers/Paper - Collins,-Evan-2025-10-01-Self-driving-labs-for-biotechnology.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Collins,-Evan-2025-10-01-Self-driving-labs-for-biotechnology.pdf"
converter: "microsoft/markitdown"
---
Self-driving labs for biotechnology

https://doi.org/10.1038/s43588-025-00885-8

Evan Collins, Robert Langer & Daniel G. Anderson

 Check for updates

Self-driving laboratories that integrate robotic
production with artificial intelligence have
the potential to accelerate innovation in
biotechnology. Because self-driving labs can
be complex and not universally applicable, it
is useful to consider their suitable use cases
for successful integration into discovery
workflows. Here, we review strategies for
assessing the suitability of self-driving labs for
biochemical design problems.

Self-driving labs (SDLs) are closed-loop platforms that typically inte-
grate two key components — robotic hardware and artificial intelligence
(AI) — to collectively plan, make, test and evaluate samples through iter-
ative optimization toward a defined research objective. These systems
leverage automation to perform high-throughput experimentation
while using AI-driven decision-making to choose research directions
in real time with minimal human intervention1,2. When implemented
effectively, robotic automation can increase both the speed and scale
of sample production, surpassing the limits of conventional manual
methods. In parallel, AI-driven optimization can improve the discovery
efficiency of functional molecules and materials.

Recent research has demonstrated the potential of SDLs in the
fields of biology2, chemistry, and materials science1, including, for
example, protein engineering3 and organic synthesis4. However, SDLs
are currently not a one-size-fits-all solution for biochemical design
problems, particularly those aimed at developing functional thera-
peutics, which involves the engineering of biological macromolecules
(such as proteins, lipids, nucleic acids and carbohydrates) and small
molecules. Functional therapeutic design in biotechnology poses
distinct challenges for SDLs. Unlike physical or chemical systems
whose outputs can often be measured and modeled directly, bio-
chemicals assessed for therapeutic effect must operate within complex,
non-deterministic biological systems, where outcomes emerge from
multilayered interactions. This complexity makes it difficult not only
to automate experimental workflows but also to optimize functional
activity reliably. As robotic and AI technologies continue to advance,
clarifying suitable use cases for SDLs in biotechnology will be essential
for realizing their benefits. In this Comment, we examine ways to assess
the suitability of SDLs for a given biochemical design problem.

Selection strategies for directed evolution
For SDLs to be effective, the biochemical design problem must have
a means of iterative selection, for instance, a mechanism to refine
candidates progressively by generally favoring those with improved
functional activity over each experimental iteration. Stepping back,
it is important to consider selection in the broader context. Selection
itself is not a new concept in biological design — natural selection is the

nature computational science

fundamental driving force behind evolution, shaping all organisms
and their constituent biomolecules over millions of years for improved
fitness. In natural selection, each reproduction event for a species rep-
resents an iteration (that is, a generation). To mimic natural selection
when designing biochemicals with specific functionality, researchers
have developed directed evolution, relying on functional outputs from
biochemical assays rather than reproduction events from organisms
in order to optimize iteratively. For example, assays involving cell-
or phage-based selection methods have been deployed to drive the
directed evolution of proteins5.

Applications of directed evolution for biochemicals invariably
mimic natural selection through iterative optimization, but the level of
intelligence required to direct the evolution process varies. In this con-
text, intelligence refers to decision-making external to the biochemical
experiment itself, such as human or algorithmic evaluation of variant
performance. On the one hand, the directed evolution of proteins
via phage display involves an intelligence-free selection mechanism,
because the protocol intrinsically ensures that only proteins with the
desired function are retained (not washed away) for subsequent itera-
tions. On the other hand, many activity-based assays for biochemicals
do not have a passive experimental selection mechanism and so require
intelligent selection (that is, external guidance) to determine which
variants should advance to the next iteration.

Indeed, many biochemical design problems relevant to therapeu-
tic development — such as designing nucleic acid sequences with opti-
mal stability and activity, optimizing lipid nanoparticle formulations,
or engineering proteins with complex functional objectives — rely on
intelligent selection, requiring external judgment to guide experi-
mental directions. Traditionally, intelligent selection in biochemistry
has depended on manual human decision-making at each round, in a
process usually referred to as rational design. However, recent inno-
vations in artificial intelligence (AI)6 have now enabled researchers
to encode selection criteria algorithmically (for instance, through an
objective function) at the outset, enabling fully automated downstream
selection. These machine learning-driven approaches can replace and
even outperform human decision-making in biochemical design7. This
newfound ability to implement intelligent selection computationally
marks a major shift: when combined with robotic hardware to establish
a hypothesis-to-experimentation feedback loop (Fig. 1a), it enables
SDLs to take on many more biotechnology design challenges.

However, if the biochemical design problem in question cannot be
defined by an accurate objective function, SDLs become impractical.
This limitation can arise when the desired biological activity cannot be
comprehensively quantified, either because it is difficult to measure
outside a complex in vivo system or because the multilayered biologi-
cal factors driving it are not fully understood. For instance, traits such
as in vivo immunogenicity, toxicity or long-term pharmacodynamic
effects often lack a reliable in vitro assay — the format most compatible
with SDLs — making it challenging to assign meaningful fitness values
to candidate biomolecules. In the absence of a clear selection signal,
the iterative refinement process at the core of directed evolution can-
not proceed effectively. In many other biochemical design problems,

Commenta   Directed evolution via iterative optimization

b   Diverse, representative data spaces

c   Automatable, scalable experimental workflows

Automatable

Scalable

Experiment

Selection
logic

Selected
candidates

y
t
i
v
i
t
c
A

Large
pool of
candidates

Meaningful features

a b c
1 3 0.4
0 1 0.2
0 4 0.1
1 7 0.3

Fig. 1 | Suitability criteria to maximize the efficacy of self-driving labs for
biotechnology. a, The biochemical design challenge in question should
have an effective means of selection to enable directed evolution via iterative
optimization towards higher activity. b, The biochemical design data space
should have many possible candidates, making active learning a beneficial
strategy and maximizing the utility of autonomous high-throughput

experimentation. Meaningful data features should capture the relevant
biochemical properties of each candidate; these can include one-hot encodings,
physicochemical properties, geometric deep learning on graphs and
masked-language modeling for evolutionary semantics, among others. c, The
experimental workflow should be automatable and scalable.

particularly in therapeutic development, objective functions are meas-
urable but are shaped by multilayered biological factors (for example,
separate goals of efficacy, stability and toxicity). In such cases, SDLs can
accommodate these complexities through multi-objective optimiza-
tion techniques (such as Pareto front approximation or scalarization)1,8.
Overall, biotechnology design problems suitable for SDLs should have
clearly definable objective functions.

With AI now capable of automating selection, it is worth clarifying
the role of the robotic hardware — the other key component of SDLs —
to facilitate directed evolution. At one end of the spectrum, iterative
robotic experimentation could become unnecessary. As AI models
advance with larger training datasets, they could reach a point where
they can predict the optimal structure outright, bypassing the need for
iterative experimentation — termed zero-shot AI. On the other end of
the spectrum, some therapeutically relevant biochemical problems
may be too domain-specific (in other words, not generalizable) for
pretrained AI foundation models to be effectively applied. Compre-
hensive experimentation would always be necessary to characterize
the landscape before meaningful AI predictions could be made.

Where do solutions for real-world biotechnology problems fall
on this spectrum today? Recent research points to somewhere in the
middle, benefiting from an ‘active learning’ approach that combines
AI-driven predictions with iterative experimentation9,10. For exam-
ple, a protein-engineering method called EVOLVEpro10 demonstrates
the value of active learning for directed evolution. The study empha-
sizes the limitations of zero-shot protein language models trained on
natural sequences, which can fail to generalize to problems requiring
de novo design for improved functionality. The study10 highlights how
directed evolution via AI-driven iterative optimization can outperform
natural selection and performs best when fine-tuned on data that
explicitly measures the functional activity being engineered into the
biomolecules. Thus, the effectiveness of active learning over zero-shot
prediction methods clarifies the potential use cases for SDLs in bio-
technology. Whether or not SDLs could be effective tools for a given

biochemical design challenge, however, requires additional consid-
eration of the data properties and implementation feasibility, which
we detail below.

Diverse and representative design spaces
SDLs are useful when the design space in question is sufficiently diverse,
meaning that many possible candidates can be produced and tested. In
biochemistry, diversity may manifest as different molecule types (for
instance, different residues in proteins3), different relative amounts in
mixtures (for example, different ratios of lipids in nanoparticles11), and
different environmental conditions (such as catalysts and other reaction
conditions for organic synthesis7). Diversity is important in realizing the
full potential of SDLs. High-throughput production — a core hardware
capability of SDLs — is especially advantageous when the combinatorial
design space is too large to be produced manually. Moreover, AI-guided
optimization — a core software capability of SDLs — is more efficient and
accurate when trained on diverse, high-quality data6.

The ease of generating diversity varies according to the biochemi-
cal class and optimization goal in question. For example, mutagenesis
provides a simple method for generating massive gene libraries, which
can be translated into proteins according to the central dogma of
molecular biology5,12. However, other library-generation efforts — such
as producing intelligently selected mutations in proteins10 or synthetic
molecules like novel lipids11 or small molecules — can require substan-
tially more effort, which could bottleneck diversity and in turn limit the
practicality of SDLs. Although complex, labor-intensive experiments
may be harder to integrate into SDLs, they potentially stand to gain the
most in terms of time saved compared to manual methods.

Beyond diversity, ensuring that the data space accurately rep-
resents the biochemicals in question is equally critical. If the feature
representations are not meaningful, AI-guided optimization will
struggle to navigate the activity landscape effectively. Poor feature
representations can obscure underlying relationships, leading to
suboptimal predictions and inefficient search strategies. Meaningful

nature computational science

Commentfeatures should originate from the most relevant biochemical prop-
erties, whether structural, physicochemical or functional, to enable
informed optimization decisions. Although simple features capture
essential properties, learned embeddings from machine learning
models can add value by incorporating more nuanced structural and
functional information6. For example, a simple one-hot encoding (that
is, a binary vector) for proteins could be a padded linear sequence of
their constituent amino acids. However, more complex deep learning
methods can compactly encode additional important information,
such as masked-language model embeddings to encode evolutionary
semantics13. For other biochemical classes like lipids, geometric deep
learning with graphs and neural message-passing strategies have been
leveraged6,11. For messenger RNA, lattice representations inspired from
computational linguistics have been used14.

The completeness and relevance of these features can be evalu-
ated by assessing how well machine learning models trained on these
features predict the desired biological activity output. Strong pre-
dictive performance (for example, as measured by high R² between
predicted and experimentally measured activity values) suggests that
the features capture much of the variance underlying the biochemi-
cal activity. Conversely, poor model performance indicates that the
features are insufficient, and alternative data modalities or encoding
techniques should be explored. In practice, the choice of features
depends on the nature of the biochemical problem: one-hot encodings
may suffice for well structured, discrete systems like short peptides;
physicochemical descriptors can be advantageous when properties
such as hydrophobicity or charge are mechanistically important; and
learned embeddings from deep learning models can be most powerful
in data-rich scenarios where subtle structure–function relationships
can be captured. Without meaningful features, the optimization pro-
cess becomes misdirected, rendering SDLs impractical for the design
problem at hand.

Therefore, creating meaningful representations is essential for
any design challenge in bioengineering (Fig. 1b), because they are the
basis for optimization via intelligent selection. Prior to deployment
with SDLs, it is advisable to optimize featurization strategies for the
biochemical class in question. Thus, designing an efficient optimizer
is an optimization problem in itself7.

Automatable and scalable experimental workflows
For SDLs to function effectively, intelligent selection needs to be cou-
pled with experimental workflows that robotic hardware can execute.
This requires considering not only how human-driven experiments
can be automated, but also how new experimental strategies can be
unlocked through SDLs. Whether a conventional workflow is automat-
able depends on both the complexity of experimental tasks and on prac-
tical constraints (time, space and resource availability). Modern robotic
systems are capable of key experimental functionalities with speed
and scale that often surpass human capabilities, including liquid han-
dling, microfluidics, sample manipulation, reagent dispensing, plate
transfers, reactor integration, centrifugation, temperature-controlled
storage, cell incubation and optical readout1,2. Ongoing innovations
are further broadening their capabilities. For example, mobile robots
have the potential to extend automation beyond fixed workstations
by transporting materials between instruments, akin to a human bio-
chemist navigating the laboratory15. In parallel, advances in real-time
and in-line characterization technologies are making it increasingly
feasible to collect diverse functional data during experimentation,
enabling additional active feedback for AI-guided optimization1,8.

nature computational science

To gauge the suitability of an SDL for a given experimental work-
flow, it is important to assess the experimental tasks that can be
automated with the robotic hardware available. Not all experimental
workflows can easily be automated with stationary robots; factors such
as liquid handling complexity, reaction times, purification require-
ments and environmental sensitivity all affect suitability1. Moreover,
not all experimental workflows justify the cost and complexity of
fully closed-loop automation, especially when the system is intended
for a limited number of experiments, making it difficult to justify the
upfront investment1,2.

Whereas some workflows may not warrant any automation, oth-
ers may benefit from a hybrid approach. Partial automation protocols
with some human intervention (for example, robotic liquid handling
but manual sample purification) may be a more practical, efficient
and error-free method. This is particularly true for therapeutic design
in biotechnology, where the complexity of producing and handling
biological systems is often a barrier to full automation. Examples of
workflow methods that may be better suited to partial automation
include: complex purification protocols for proteins, nucleic acids and
lipids; primary cell culture and differentiation assays that depend on
morphological assessment and fine-tuned environmental control; and
assays using rare, expensive or unstable reagents where minimizing
material loss and ensuring sample integrity is best handled manually.
Along with considering the degree to which the design challenge
is automatable, it is also important to consider scalability. SDLs excel
in high-throughput experimentation, especially when workflows
are designed to scale efficiently by accommodating large numbers
of experiments in parallel. Fortunately, many biochemical assays
are easily amenable to parallelization. Standardized assay formats
involving microplates and parallel batch reactors facilitate scalability
and maximize the throughput capacity of SDLs, which rely on active
learning over many rounds of experiments. However, biochemical
workflows can include bespoke, sequential experiments that limit
scalability and, consequently, the practicality of SDLs. Scalability can
also be constrained by the cost of materials, a substantial barrier to
high-throughput experimentation. Ultimately, SDLs are most suitable
for experimental workflows that are automatable and scalable (Fig. 1c).

Future perspectives
SDLs hold immense potential to accelerate biotechnology discovery by
integrating AI-driven intelligent selection with robotic experimenta-
tion. However, the suitability of an SDL for a given problem in biotech-
nology depends on several key factors, including the presence of an
effective selection mechanism for directed evolution, the diversity and
representativeness of data features, and the automation and scalability
potential of the experimental workflow. When effective, SDLs optimize
experimental efficiency by overcoming the limitations of traditional
workflows — such as inefficient navigation of the activity landscape and
disconnected experimental stages — and yield experimental results
that would be difficult to obtain using manual methods.

In order for SDLs to evolve to be more effective in biotechnology
applications, common workflow steps that are currently resistant to
automation, such as those not currently compatible with basic liquid
handlers, should be made modular and programmable. Additionally,
large-scale structure–function data-collection efforts, like those that
catalyzed progress in deep learning for proteins13, should be extended
to the other biomolecule classes — lipids, nucleic acids and carbohy-
drates — to similarly enable the development of robust foundation
models. The continued progress of SDLs in biotechnology will depend

Commenton the systematic generation of both structural and functional biologi-
cal data, which will be critical for training, validating and fine-tuning
machine learning models capable of guiding molecular design across
diverse biochemical contexts.

Ongoing progress in AI trained on multi-source, multi-modal
molecular datasets will broaden the scope of intelligent selection,
enabling the directed evolution of biomolecules with improved thera-
peutic potential. Moreover, as robotic technology improves over time,
refining the role of human biochemists to maximize the efficiency and
accuracy of SDLs will be essential. By coupling state-of-the-art active
learning approaches with the appropriate robotic hardware, effective
SDLs will transform how biomolecules are designed and optimized,
unlocking possibilities in multiple important areas of biotechnology,
including drug development, vaccine technology, gene therapy, preci-
sion medicine, protein engineering and biomanufacturing.

Published online: xx xx xxxx

References
1.  Abolhasani, M. & Kumacheva, E. Nat. Synth. 2, 483–492 (2023).
2.  Martin, H. G. et al. Curr. Opin. Biotechnol. 79, 102881 (2023).
3.  Rapp, J. T., Bremer, B. J. & Romero, P. A. Nat. Chem. Eng. 1, 97–107 (2024).
4.  Coley, C. W. et al. Science 365, eaax1566 (2019).
5.  Packer, M. S. & Liu, D. R. Nat. Rev. Genet. 16, 379–394 (2015).
6.  Wang, H. et al. Nature 620, 47–60 (2023).
7.  Shields, B. J. et al. Nature 590, 89–96 (2021).
8.  Sagmeister, P. et al. Adv. Sci. 9, 2105547 (2022).
9.  Pandi, A. et al. Nat. Commun. 13, 3876 (2022).
10.  Jiang, K. et al. Science 387, eadr6006 (2025).
11.  Witten, J. et al. Nat. Biotechnol. https://doi.org/10.1038/s41587-024-02490-y

(2024).

12.  Zhao, H., Giver, L., Shao, Z., Affholter, J. A. & Arnold, F. H. Nat. Biotechnol. 16,

258–261 (1998).

13.  Lin, Z. et al. Science 379, 1123–1130 (2023).
14.  Zhang, H. et al. Nature 621, 396–403 (2023).
15.  Burger, B. et al. Nature 583, 237–241 (2020).

Acknowledgements
This work is supported by Sanofi, MIT’s Jameel Clinic and NIH grant R33AI161805-05.
The figure was created in part using images from Biorender.com and Iconify.design.

Competing interests
D.G.A. receives research funding from Sanofi and is a founder of Orna Therapeutics,
Soufflé Therapeutics and Combined Therapeutics. R.L. is a co-founder and former member
of the board of directors of Moderna. He also serves on the board and has equity in
Particles for Humanity. For a full list of entities with which R.L. is involved, compensated
or uncompensated, see https://www.dropbox.com/scl/fi/ty2b7x8vyebid8ybcbeox/
Rev-Langer-COI.pdf?rlkey=lko2srm1qjknm53ck9yns1dfj&e=1&dl=0. E.C. has no competing
interests to declare.

Additional information
Peer review information Nature Computational Science thanks Milad Abolhasani and the
other, anonymous, reviewer(s) for their contribution to the peer review of this work.

  1,2,4,5,6 &

  1,2,3, Robert Langer
  2,4,5,6

Evan Collins
Daniel G. Anderson
1Department of Biological Engineering, Massachusetts Institute
of Technology, Cambridge, MA, USA. 2David H. Koch Institute for
Integrative Cancer Research, Massachusetts Institute of Technology,
Cambridge, MA, USA. 3Jameel Clinic, Massachusetts Institute
of Technology, Cambridge, MA, USA. 4Department of Chemical
Engineering, Massachusetts Institute of Technology, Cambridge, MA,
USA. 5Harvard and MIT Division of Health Science and Technology,
Massachusetts Institute of Technology, Cambridge, MA, USA.
6Institute for Medical Engineering and Science, Massachusetts
Institute of Technology, Cambridge, MA, USA.

 e-mail: dgander@mit.edu

nature computational science

Comment
