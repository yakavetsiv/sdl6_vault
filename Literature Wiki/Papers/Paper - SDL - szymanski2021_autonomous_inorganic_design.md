---
tags:
  - literature
  - type/paper
  - lit/sdl
  - lit/nanomedicine
  - lit/ai-methods
type: literature-note
status: converted
source_type: pdf
source_file: "szymanski2021_autonomous_design_synthesis_inorganic_materials.pdf"
source_path: "/Users/iyakavets/Documents/Github/LH_BO_Preprint/literature/pdfs/self_driving_labs/szymanski2021_autonomous_design_synthesis_inorganic_materials.pdf"
pdf: "_attachments/Self-Driving Labs/szymanski2021_autonomous_design_synthesis_inorganic_materials.pdf"
title: "Toward autonomous design and synthesis of novel inorganic materials"
year: "2021"
doi: "10.1039/d1mh00495f"
citation_count_openalex: 148
topics:
  - Self-Driving Labs
  - Lab Automation
  - Autonomous Experimentation
tags:
  - literature/self-driving-labs
  - source/pdf
  - converted/markitdown
---

# Toward autonomous design and synthesis of novel inorganic materials

**Key:** `szymanski2021_autonomous_inorganic_design`  
**Year:** 2021  
**DOI:** 10.1039/d1mh00495f  
**OpenAlex citations:** 148  
**PDF:** [[_attachments/Self-Driving Labs/szymanski2021_autonomous_design_synthesis_inorganic_materials.pdf]]

## Why It Matters

This paper is part of the high-citation self-driving laboratory set imported from the LH_BO preprint literature review. Use it to support background claims about closed-loop experimentation, autonomous laboratory infrastructure, AI-guided experiment planning, or automated materials/chemical discovery.

## Connections

- [[Concept - Self-Driving Labs]]
- [[Concept - Lab Automation]]
- [[Concept - Optimization and Bayesian Search]]
- [[Map - Self-Driving Lab Stack]]

## Converted Text

Materials
Horizons

REVIEW

Toward autonomous design and synthesis
of novel inorganic materials

Nathan J. Szymanski,
Haegyeom Kim *b and Gerbrand Ceder

ab Yan Zeng,b Haoyan Huo,

*ab

ab Christopher J. Bartel,

*ab

intelligence (AI) provides an exciting opportunity to
Autonomous experimentation driven by artificial
revolutionize inorganic materials discovery and development. Herein, we review recent progress in the

design of self-driving laboratories, including robotics to automate materials synthesis and characterization,

in conjunction with AI to interpret experimental outcomes and propose new experimental procedures. We

focus on eﬀorts to automate inorganic synthesis through solution-based routes, solid-state reactions, and

thin film deposition. In each case, connections are made to relevant work in organic chemistry, where

automation is more common. Characterization techniques are primarily discussed in the context of phase

identification, as this task is critical to understand what products have formed during synthesis. The

application of deep learning to analyze multivariate characterization data and perform phase identification is
examined. To achieve ‘‘closed-loop’’ materials synthesis and design, we further provide a detailed overview

of optimization algorithms that use active learning to rationally guide experimental iterations. Finally, we

highlight several key opportunities and challenges for the future development of self-driving inorganic

Received 23rd March 2021,
Accepted 19th May 2021

DOI: 10.1039/d1mh00495f

rsc.li/materials-horizons

materials synthesis platforms.

1. Introduction

Historically, great innovations in technologies have been driven
by the discovery of novel materials. Current materials develop-
ment largely relies on three key steps: (i) identification of a new
composition and structure of interest, (ii) targeted and scalable
synthesis of that compound, and (iii) post-processing of the
product to carefully optimize its properties.1 To accelerate this
procedure, it is necessary to not only improve the eﬃcacy of
each step, but also to integrate all three into a closed loop so
that they can occur in rapid succession and benefit from
optimal feedback between them. While the initial identification
step has been assisted by large-scale ab initio simulations,2,3 the
latter two generally remain diﬃcult and time-consuming owing
to the iterative trial-and-error experimental approach required
for both synthesis and property optimization. A breakthrough
to overcome these challenges may be found in autonomous
experimentation enabled by self-driving laboratories, which
aim to aid the human researcher with robotic platforms guided
by artificial intelligence (AI).

The automation of experiments has long been a topic of interest,
with early examples of widespread utilization demonstrated in

a Department of Materials Science & Engineering, UC Berkeley, Berkeley, CA 94720,
USA. E-mail: cbartel@berkeley.edu, gceder@berkeley.edu
b Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley,
CA 94720, USA. E-mail: haegyumkim@lbl.gov

industry.4 There, high-throughput (HT)
the pharmaceutical
chemistry platforms have been developed to accelerate drug
discovery using combinatorial sampling of possible molecules
and synthesis conditions, which can be performed in an auto-
mated and highly parallelized manner to save considerable time
and costs.5–7 More recently, the advent of AI has created a
symbiosis between hardware and software, with active learning
techniques guiding the exploration of design spaces and leading
to increased efficiencies relative to combinatorial techniques.8–10
This has opened the door to more sophisticated applications
ranging from systematic inspection of retrosynthetic routes in
small molecule manufacturing11 to performance optimization in
organic photovoltaics.12 Furthermore, by automating the role of
the experimenter as opposed to individual instruments, modern
systems are flexible and can rapidly incorporate improvements in
the underlying technology.13

In contrast to organic chemistry, the development of auto-
nomous experimentation for inorganic materials remains in its
early stages. Given the challenges associated with handling
solid powders, the limited availability of methods that can
reliably characterize bulk samples, and the lack of a rigorous
theoretical
framework describing the factors influencing
synthesizability, the majority of existing work has demon-
strated only partial automation of the experimental process.
Within the thin film community, for example, HT automation
of synthesis and characterization is routinely carried out to
probe the eﬀects of composition and processing conditions on

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Cite this: DOI: 10.1039/d1mh00495fPublished on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineView JournalReview

Materials Horizons

the properties of resulting samples.14–16 Similar methods have
also been used to study bulk powders but are generally more
limited with respect to the scope of compounds that can be
dealt with.17–19 Existing workflows are restricted to materials
with readily available synthesis recipes, which precludes the
discovery of novel systems with new and interesting properties.
More recently, AI has been incorporated into the automation
pipeline to achieve closed-loop optimization of synthetic routes
for nanoparticles formed in continuous flow reactors20 and
nanotubes grown via chemical vapor deposition (CVD).21,22
While these platforms can be used to maximize the yield and
purity of a target phase, they rely on a reasonable initial guess
for the choice of precursors and synthesis conditions so that a
measurable amount of the product is consistently obtained and
used to guide the optimization. In novel compound synthesis
and discovery, however, there is typically insufficient infor-
mation available regarding successful reaction pathways, and
consequently, the majority of synthesis trials fail to produce any
the target phase. Therefore, although current
amount of
capabilities are indeed promising, considerable progress is
necessary before a universally applicable platform enabling
autonomous, end-to-end synthesis of inorganic materials can
be realized.

Herein, we review the progress made toward ‘‘closing the
loop’’ of experimental design, execution, and learning via
the development of self-driving laboratories with a focus on
applications in inorganic materials science. Accordingly, we
consider three major aspects that must be automated to reach
this goal. First, experimental procedures should be carried out
by modular, robotic platforms with the capability of synthesiz-
ing and characterizing the materials of interest. Second, the
data obtained from characterization should be interpreted by
the machine and converted into simple, physically meaningful
quantities providing insight into the experimental outcome.
Last but not least, this information should then be passed to an
intelligent decision-making algorithm that actively learns from
previously tabulated data and/or scientific principles to suggest
new experimental parameters for subsequent tests. Successful
design and integration of all three aspects is essential to
complete the closed-loop workflow illustrated in Fig. 1.

With the goal of reaching complete autonomy in the synthesis of
inorganic materials, we oﬀer perspectives regarding challenges and
future directions. To this end, we outline promising techniques to
automate solid-state synthesis, characterize the resulting samples by
using deep learning algorithms to interpret X-ray diﬀraction (XRD)
spectra, and make informed decisions regarding subsequent synth-
eses. The automation of synthesis and characterization would
ensure a high experimental throughput, freeing up time for the
researcher to analyze resulting datasets and plan new experiments.
An increase in the availability of synthesis data may also assist in the
development of AI that learns from experimental outcomes – not
only to discern whether a given synthesis attempt succeeded or
failed, but more importantly to hypothesize why it may have
succeeded or failed. Such predictions generally require insight from
human researchers with a detailed understanding of plausible
reaction mechanisms. Automating this process is a daunting task;
however, we propose that a useful set of rules for understanding
synthesis can be extracted from work being conducted in several
related areas including theories on synthesizability,23 in situ char-
acterization of reaction pathways,24 and an increasing availability of
synthesis data.25 If developments in these areas are successful in
enabling a self-driving synthesis laboratory, it would have wide-
reaching impacts across the materials science community,
providing the opportunity to efficiently generate new com-
pounds at an unprecedented rate while reducing the amount
of time and labor spent by the researcher.

2. Synthesis & characterization

Synthesizing samples is the first major step in the automated
optimization of materials properties and processes. We note
that our initial discussion presented here is restricted to the
hardware requirements necessary to carry out a synthesis
procedure with a given set of parameters including the choice
of precursors and conditions – algorithms designed to suggest
these parameters will be reviewed in Section 4. After the samples
have been prepared, appropriate characterization techniques
should be employed to reveal the properties of interest and provide
information regarding the experimental outcome. The execution of

Fig. 1 Schematic showing the general workflow of fully autonomous experimentation for the discovery and development of novel inorganic materials.

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

synthesis and characterization can be accomplished using robotic
systems coupled with real-time and online monitoring to ensure
high precision and the handling of any operational issues. The
ease of automation, however, varies depending on the synthesis
method and the form of the products. We therefore divide our
discussion into three major categories: batch or continuous
solution-based synthesis, thin film deposition, and solid-state
synthesis of bulk powders. Moreover, while the focus of this review
is placed on inorganic materials, we will often highlight related
platforms in organic chemistry, where automation is more com-
mon, to learn from their success and understand how similar
methods can be extended to inorganic compounds.

2.1 Solution-based synthesis

The batch solution-based approach, whereby reagents are
sequentially combined in appropriate solvents and subjected
to a series of carefully chosen experimental conditions, is often
the method chosen by organic chemists when synthesizing
small molecules.26 The automation of this method to enable
HT screening has been widely adopted. As detailed in previous
reviews,4,7,27 industrial drug discovery systems can routinely
conduct thousands of experiments each day. For more complex
molecules, however, subtle multi-step reaction sequences are
required. To automate the step-by-step addition of reagents, a
modular robotic system known as the ‘‘Chemputer’’ was devel-
oped by Steiner et al.11 The backbone of their setup, shown in
Fig. 2, contains a series of syringe pumps and six-way selection
valves used to transfer reagents between diﬀerent components
of the platform. Four modules are implemented to handle each
aspect required for synthesis and characterization, including
the main reactor, liquid–liquid separator, filtration apparatus,
and rotary evaporator. At the end of the line, chromatography is
employed to identify and quantify the resulting products. To
verify the effectiveness of their platform, the authors employed
the system to automatically synthesize three common drugs
over the course of several days. For all procedures, the desired
product was successfully obtained with a yield comparable to
that generated by human chemists using a standard synthetic
procedure.

To increase flexibility, Burger et al. produced a mobile robot
capable of replicating the actions performed by the traditional
chemist – e.g., dispensing reagents, handling vials, and executing
operations on lab hardware.13 Because this platform focuses on
automating the role of the researcher while allowing all other
aspects of the lab to be interchangeable, it can in principle be
applied to diverse sets of experiments by simply swapping out
labware and re-programming the robot accordingly. This was
demonstrated in the study of aqueous photocatalysts for hydrogen
evolution, for which the robotic chemist successfully conducted
688 experiments over the course of eight days. The authors estimate
that a comparable number of experiments would have taken a
human researcher several months to complete, thus highlighting
the benefits of automation.

Flow chemistry represents an alternative synthesis approach
that is more widely implemented for large-scale manufacturing of
organic compounds.28 Continuous flow reactors pump reagents

Fig. 2 (A) A schematic and (B) photograph of the Chemputer, an auto-
mated platform enabling the synthesis of pharmaceutical compounds. The
setup is comprised of four modules including the reactor, filter, separator,
and rotary evaporation, all of which are connected through a series
of syringe pumps and six-wave valves. Reproduced with permission.11
Copyright 2019, AAAS.

through a series of interconnected vessels, with reaction stoichio-
metries set by the reagent flow rates and conditions controlled
using in-line modules. Rapid flow rates and excellent mixing
ensure eﬃcient production of target compounds. Moreover,
because the systems can be pressurized, higher temperatures
can be accessed to enable faster reaction rates. As they eliminate
the need to manually transfer samples between diﬀerent
stations required in batch chemistry, flow reactors are readily
automated.29,30 For example, Be´dard et al. built a reconfigurable
system to autonomously optimize a variety of chemical trans-
formations in a flow reactor.31 An alternating series of tubing
and reaction bays shown in Fig. 3 allow reagents to be added
sequentially so that multi-step syntheses can be performed. To
improve the versatility of the flow reactor, a ‘‘plug-and-play’’
approach is employed whereby six diﬀerent modules can be
interchanged to provide unique capabilities such as heating,
cooling, and catalysis. Similarly, many diﬀerent characterization
techniques including high-performance liquid chromatography
(HPLC), mass spectrometry (MS), and optical spectroscopy can
be implemented to analyze the reaction outcome. Applying
the platform to three synthetic procedures involving common
pharmaceuticals, the authors investigated optimal reaction
conditions across hundreds of experiments spanning a cumulative
timespan of less than two days.

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

Fig. 3 A schematic showing the alternating series of reaction bays implemented sequentially throughout a continuous flow reactor designed to
optimize organic reactions. A ‘‘plug-and-play’’ approach is used to swap out the modules listed to replicate varied reaction conditions such as heating,
cooling, or photocatalysis. Reproduced with permission.31 Copyright 2018, AAAS.

The promising results for automated solution-based syntheses of
organic molecules have led to several eﬀorts to demonstrate the
automation of inorganic materials syntheses using similar methods.
For example, to rapidly produce lithium and sodium metal oxides
with varied compositions, a batch solution-based approach was
partially automated using the robotic system depicted in Fig. 4.18,19
This platform uses an electronic pipetting tool to transfer stock
solutions of precursors into microplates, which are heated to
mediate reactions between the starting materials. Depending on
the choice of precursors and temperature, both co-precipitation and
sol–gel routes can be tested at rates of hundreds of samples per day,
with the characterization of each conducted by XRD. Comparable
techniques have also been applied to automate the synthesis of
metal halide perovskites from solution using inverse crystallization
at high temperatures.32 In existing workflows based on batch
synthesis, however, manual
intervention is generally required
to transfer, dispose of, and replace sample containers between
experimental iterations. To automate these processes and fully close
the loop, future work may consider integrating a programmable
robotic arm as demonstrated by the mobile robotic chemist.13

In contrast to batch synthesis, flow chemistry is one of the
in making

few methods that has been proven successful

inorganic synthesis fully autonomous. This was first shown
by Krishnadasan et al. in the optimization of reactions produ-
cing CdSe nanoparticles.20 Flow rates of CdO and Se precursors
dissolved in organic solvents were controlled by electronic
syringe pumps, combined using a Y-shaped reactor, and passed
through a heated reaction vessel. Throughout this process, in-
line spectrometry with a charge-coupled device (CCD) was
employed to monitor product formation. In separate work, Li
et al. used comparable techniques to automate the discovery of
optically active perovskites. In their platform, precursor solutions
were prepared by a rotation sampler and injected into a pipeline
of temperature-controlled microfluidic reactors while in situ
monitoring was conducted by optical spectroscopy.33 For char-
acterization of the synthesized materials, a robotic arm trans-
ferred samples from the flow reactor to a separate station where
circular dichroism was measured using spectrometry. Each
autonomous workflow was shown to be capable of performing
hundreds of experiments at an accelerated rate relative to that
obtained by a human researcher.

Despite these successes, the generality of solution-based
synthesis for inorganic materials remains limited given the
constraints that are imposed on the choice of precursors and

Fig. 4 (a) A photograph of the robotic platform that partially automates the HT combinatorial synthesis of powder Na–Fe–Mn–O samples through a
sol–gel approach. (b) The precursors shown directly after solution mixing. (c) The products after being dried and crushed, shown directly before firing at
high temperature. Reproduced with permission.19 Copyright 2020, American Chemical Society.

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

reaction conditions. Both batch and flow syntheses require that
the starting materials are soluble in an appropriate solvent,
which precludes the use of compounds with low solubilities in
available liquids. This limitation has little eﬀect on the scope of
suitable organic compounds, most of which have reasonable
solubilities in organic solvents, but it is highly restrictive for
inorganic materials because many cannot be dissolved in
common solvents such as water or ethanol. Furthermore, to
avoid evaporation of the liquid solvent, operating temperatures
must be kept relatively low during synthesis. Even with the use
of pressurization in flow reactors, 200 1C is an upper bound for
most systems, suggesting that neither batch nor flow chemistry
can be used for inorganic materials that are synthesizable only at
high temperatures. Therefore, although solution-based methods
are useful where applicable, they do not provide suﬃcient coverage
of the entire chemical space to be used exclusively for automated
inorganic synthesis.

2.2 Thin film synthesis

Partial automation of synthesis and characterization has become
increasingly common throughout the thin film community,
where combinatorial methods are employed to study a range
of systems such as high-entropy alloys34 and mixed metal
chalcogenides.35,36 These platforms typically rely on physical
or chemical vapor depositions techniques to synthesize samples
spanning a continuous range of compositions, either by sequentially
depositing overlapping wedge-shaped layers from individual
sources or by simultaneously depositing multiple elements
(e.g., by co-sputtering) to achieve a compositional gradient.14
The resulting thin film allows the eﬀect of composition to be
studied without requiring the synthesis of many individual
samples. XRD, optical spectroscopy, and resistivity measure-
ments are often used to characterize a grid of points across the
sample and build a combinatorial library of material properties
for the system. By producing a large amount of data for a single
targeted sample, automation can be constrained to one experi-
mental cycle of synthesis and characterization, whereas the subse-
quent processes of analysis and planning of future experiments
remain to the researcher’s labor and intuition (i.e., the loop is not
closed). For a detailed account of existing combinatorial techniques
and their applications, we refer the reader to past review articles
on the subject.14,37 Here, we focus on several examples that
demonstrate progress made toward closing the loop of synthesis,
characterization, and decision-making for thin film materials.

In one of the first well-known examples of completely auto-
nomous experimentation for inorganic materials science, Nikolaev
et al. designed a platform to find the synthesis conditions that
optimized the growth rate of carbon nanotubes.21 This process was
automated using wafers containing thousands of micron-sized
silicon pillars that were coated in a thin layer of catalyst material.
Each individual pillar served as a microreactor in a CVD process
with ethylene as a source of carbon. By heating pillars one at a time
using a highly focused laser and iteratively moving the wafer
with a two-axis motion stage, the synthesis of individual
samples was precisely controlled. Moreover, the same laser
acted as an excitation source for Raman spectroscopy, allowing

Fig. 5 A schematic of the Autonomous Research System (ARES) built to
study the formation of carbon nanotubes throughout varied synthesis
conditions. A 532 nm laser was employed to heat individual samples of
precursors on the wafer while simultaneously providing an excitation
source for Raman spectroscopy. Reproduced with permission.21 Copyright
2016, Nature Publishing Group.

continuous in situ monitoring of growth rates. As illustrated in
Fig. 5, the system was shown to eﬃciently carry out experiments
at a rate of 100 samples per day, a significant improvement over
conventional methods.38 We note, however, that the success of
this platform relies on the use of wafers containing many
carefully constructed pillars of precursor material, which must
be formed in advance and are not necessarily suitable for
applications outside of microelectronics.

To autonomously synthesize, process, and characterize
organic thin films, MacLeod et al. introduced a self-driving
laboratory named Ada.12 As illustrated in Fig. 6, Ada utilizes a
robotic arm to transfer vials of fluid between stations on the
platform, each of which provides a unique capability including
sample storage, solution mixing, spin coating, annealing, and
characterization. A combination of four-point probe resistivity
measurements and ultraviolet-visible-near-infrared (UV-vis-NIR)
spectroscopy were used to study the hole mobility of each
sample. Focusing on Spiro-OMeTAD, an organic hole transport
material used in photovoltaics, Ada was shown to successfully
carry out 35 experiments in less than 30 hours with guidance
provided by a Bayesian optimization algorithm (discussed in
Section 4.1.3) to maximize hole mobility in the samples. Though
their platform was constrained to organic films, the methods
used can likely be extended to inorganic compounds where
solution-based precursors are available for spin coating.

Shimizu et al. extended autonomous synthesis to inorganic
thin films using magnetron sputtering deposition.39 With this
method, TiO2-based films with a varying concentration of Nb
dopants were grown. The partial pressure of oxygen was chosen
to be the single experimental variable, which set the reducing
conditions during synthesis and thereby influenced the amount
of dopant atoms implanted into the films. After each sample
was grown, a robotic arm was utilized to transfer it to a separate
station for characterization of its electric properties. Aiming
to optimize the resistivity with respect to Nb concentration,

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

Fig. 6 An illustration of the Ada platform used to optimize the optoelectronic properties of organic thin films. Handling and transferring of samples are
performed by the robotic arm (A) using a combination of tools shown in (B) and (B), whereas storage, synthesis, and characterization of samples are
conducted throughout the individual modules pictured in (D). Reproduced with permission.12 Copyright 2020, AAAS.

the films were synthesized and characterized in a closed loop
at a rate of twelve samples per day, whereas an equivalent
procedure carried out manually is suggested to produce only two
new samples per day. Although the observed rate of experiments is
not as rapid as the workflows involving CNTs or Spiro-OMeTAD,
magnetron sputtering deposition is more readily applicable to a
wider range of materials and applications.

laser

lateral-gradient

synthesis conditions,

More recently, Ament et al. demonstrated that closed-loop
experimentation can be used to synthesize metastable materials
that would otherwise be diﬃcult to access by trial-and-error.40 In
their approach, an amorphous layer with a composition of Bi2O3
was deposited onto a silicon substrate via reactive sputtering. To
explore the formation of metastable polymorphs of Bi2O3 under
diﬀerent
spike
annealing41 (lg-LSA) was used to rapidly heat and crystallize
samples at varied temperatures and dwell times. Within each
experimental iteration, optical spectroscopy was applied to mea-
sure the reflectivity from a batch of samples. Large changes in
reflectivity with respect to the synthesis conditions of the samples
were assumed to signify phase transitions (i.e., formation of new
Bi2O3 polymorphs). Hence, phase boundaries were determined
by choosing subsequent experiments that were expected to
maximize the gradient of the reflectance. A complete mapping
of these boundaries was achieved from 617 samples that were
autonomously synthesized, after which XRD was performed a
posteriori to verify the corresponding phase identities. A key
advantage of this approach was the use of lg-LSA, which allowed
microscopic regions of the sample to be heated independently of
one another. Therefore, a large number of temperatures and
dwell times could be tested from a single sample.

Because there are many available deposition techniques, the
automation of thin film synthesis may prove useful to make a

wide range of inorganic materials. In addition to solution-based
methods (e.g., spin coating12), which require precursors to be
soluble in an appropriate solvent, deposition from a gaseous
phase expands possible precursors to materials that can be
vaporized through heating, sputtering, or irradiation (e.g., for
CVD21). Techniques such as lg-LSA can also be used to produce
reactions or phase transformations in a sample after it has been
deposited, which further increases the number of accessible
phases40 However, the versatility of these methods is limited by
the applications for which thin films are suitable, which include
photovoltaics, protective coatings, and electronic circuitry. To
generalize autonomous experimentation for the synthesis of
compounds used for technologies such as batteries, catalysts, or
functional materials, a solid-state approach must be considered to
form bulk powders rather than thin films.

2.3 Solid-state synthesis

Solid-state synthesis, carried out by mixing powder precursors and
firing at high temperatures, is a widely used and scalable approach
to produce inorganic materials. Automating this process for HT or
closed-loop experimentation, however, remains challenging due to
the increased diﬃculty associated with handling solid powders as
opposed to liquids or thin films. Working at high temperatures for
long periods of time also poses potential problems caused by the
melting of samples and the degradation of containers. Recent
eﬀorts have made steps to automate a few key aspects of solid-
state synthesis for several classes of materials including
PbTe-based thermoelectrics,42 yttrium-doped zirconia,43 and
Zr–Ti–C–B ceramics.44 These existing methods increase the rate
at which solid-state syntheses are carried out by decomposing
the entire procedure into modular components, each of which
is either automated via robotic systems or designed to be

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

conducted in a highly parallelized manner, thereby reducing the
time spent by the human researcher per synthesized sample.

Automated weighing and dispensing of powder precursors
have been demonstrated with several commercial systems.45,46
These instruments use gravity to pass samples through a
hollow glass or plastic tip and into a container, which is placed
on a balance and continuously weighed to control the rate of
dispensing and produce the targeted precursor amount. When
too much powder is dispensed, small amounts of the sample
can be removed using a glass plunger, allowing the automated
system to reach a precision on the order of micrograms. Once
the precursors have been dispensed, mixing is typically carried
out using a ball mill, which can be designed to accommodate
many samples at once such that parallelization is possible.44 If
mechanochemical synthesis is desired, high-energy ball milling
or highly reactive starting materials can be used to encourage
the reaction.17 If, instead, the goal of ball milling is to obtain a
well-mixed sample while avoiding any reactions, then relatively
inert precursors can be used with low-energy milling.42 The
parallelization of compacting and densification can be achieved
by stacking samples on top of one another, separated by an inert
material, and loading them altogether into a press. Firing of
samples is readily parallelized, limited only by the size of the
reaction vessel. However, unless separate furnaces are employed,
all materials must be synthesized under the same conditions,
which prohibits an eﬃcient exploration of all synthesis para-
meters simultaneously. Ensuing characterization (e.g., by XRD) is
usually conducted serially, though their operation periods are
often short in comparison to the time required for synthesis and
are therefore unlikely to represent the time-limiting step.

Using HT methods, solid-state syntheses can be performed at
a rate of more than 200 reactions per day.17 We stress, however,
that all of the existing methods simply automate individual
components of the synthesis process while still requiring a
substantial amount of manual intervention between each step.
As a result, human eﬀorts constitute a large fraction of the total
time allocated for the synthesis and characterization and solid
powders, and closed-loop automation has not yet been estab-
lished. This shortcoming is illustrated by the Sankey plot in
Fig. 7, which shows that of the total 328 minutes necessary to
complete a full experimental iteration per sample, 105 minutes
are consumed by human eﬀorts. Much of this time is spent
performing preparative tasks such as sample loading, cleaning,
and extraction. These processes are generally diﬃcult to auto-
mate for solid powders given that their physical properties can
vary substantially between diﬀerent samples, and powders can
sometimes adhere to container walls. After synthesis, further
manual intervention is required to transfer samples and prepare
them for characterization. For example, powders must be well
ground and flattened before they can be characterized by XRD.
While these processes have been partially automated with
commercial systems,47 more specialized characterization techniques
remain heavily reliant on human eﬀorts (e.g., preparing Ohmic
contacts for electrical measurements). Future work is therefore
needed to address these limitations and progress toward full
autonomy. The development of automated sample preparation

Fig. 7 Sankey plot illustrating the time required to complete each com-
ponent of synthesis and characterization (per sample) throughout the
study of thermoelectric materials by Ortiz et al. Any eﬀort that must be
carried out manually by the human researcher is denoted ‘‘human time,’’
whereas all processes automated by the instrumentation is denoted
‘‘machine time.’’ As the workflow here is only partially automated to enable
HT, but not fully autonomous, a substantial portion of the total time
required is shown to be allocated to human eﬀorts. Reproduced with
permission.42 Copyright 2019, Royal Society of Chemistry Publishing.

and transfer for solid-state synthesis will be discussed further in
Section 5.

3. Interpretation

In some cases, the process of interpreting data from a cycle of
synthesis and characterization is straightforward; for example,
when measurements yield simple numerical quantities such as
electrical resistivity or optical absorbance.12,48 More generally,
however, reliably interpreting characterization data is highly
non-trivial, requiring detailed analysis by an expert. Such tasks may
involve spectral data obtained from spectroscopic techniques,49
images captured via microscopy,50 or application-based measures of
performance.51 As part of the eﬀort to realize self-driving labora-
tories in materials science, recent work has demonstrated the
potential for machine learning models to analyze and interpret a
variety of characterization data,52–54 thereby automating the inter-
pretation component of closed-loop experimentation. The difficulty
of this task depends on the number of variables associated with the
data being analyzed – i.e., higher dimensionality and an increased
amount of information tends to present greater challenges in
the automation of interpretation. Accordingly, we break down
our discussion into methods used for the analysis of univariate
quantities, multivariate data in one dimension (e.g., spectra),
and multivariate data in higher dimensions (e.g., images and
tomograms).

3.1 Univariate

3.1.1 Surrogate properties. When the property of interest
can be represented by a single scalar quantity obtained directly
from an automated characterization procedure, interpretation
is trivial. When univariate properties are diﬃcult to measure in

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

an automated way, one may instead choose a ‘‘surrogate’’
property that is more easily measured and has some known
relation to the property of interest. For example, MacLeod et al.
designed Ada to optimize the hole mobility in organic thin films.12
Considering that automating direct and reliable measurements of
the hole mobility is diﬃcult because it requires the construction
of multilayer photovoltaic devices, the authors instead used the
‘‘psuedomobility,’’ which is equal to the quotient of sheet
conductance over absorbance of the thin film and can be
measured with four-point probe measurements and optical
spectroscopy respectively. The actual hole mobility of each
sample was shown to be directly related to its psuedomobility,
and therefore the former can be optimized indirectly using
automated characterization techniques.

Another example demonstrating the utility of surrogate properties
is given by the determination of phase boundaries from combi-
natorial thin film libraries.37,55 A direct approach to detect
phase transitions would involve performing XRD measurements
and interpreting the resulting spectra to identify the constituent
phases. Although characterization by XRD can be carried out in
an automated way, the subsequent process of phase identifi-
cation (interpretation) is challenging given that it requires
multivariate analysis (as will be discussed in Section 3.2). To
avoid these diﬃculties, it is common to replace XRD by simpler
characterization techniques yielding univariate quantities that
vary when phase transitions occur. Common choices for these

properties include electrical resistivity, optical reflectivity, and
mechanical hardness,55 each of which are strongly dependent on
the phase present. Accordingly, large changes in these properties
are used to indicate that a phase transition has occurred.

3.1.2 Reduction to univariate. In some cases, measurements
generate data that are initially multivariate but that can be reduced
into univariate quantities through dimensionality reduction. For
example, optical spectra are commonly simplified by focusing on a
single wavelength or by integrating across a range of wavelengths.56
Similarly, stress–strain and hysteresis curves can be reduced to
univariate quantities such as the Young’s modulus or saturation
magnetization.57,58 These methods are commonly implemented in
combinatorial thin film studies but have also been extended to work
with bulk materials in partially automated workflows. During the
optimization of shape-memory alloys, for example, heat flow curves
obtained from differential scanning calorimetry were simplified to a
single value that represented thermal hysteresis of the samples.51
For battery materials, HT characterization can be carried out by
reducing voltage versus capacity curves into univariate quantities
such as capacity and energy density.59

To assist in phase identification, multivariate spectra (e.g.,
XRD or Raman) can be simplified by focusing on a subset of
peaks associated with a target phase. For example, Nikolaev et al.
estimated the growth rates of CNTs by measuring the maximum
intensities of two known Raman peaks shown in Fig. 8 as a
function of time.21 Similarly, Moosavi et al. monitored the phase

Fig. 8 (a) To automate the characterization of carbon nanotubes, the intensity of the G and D bands, from the Raman spectra shown in (c), are
continuously measured throughout each experiment. (b) By diﬀerentiating the Raman intensity with respect to time, the growth rate of each sample is
obtained. Reproduced with permission.21 Copyright 2016, Nature Publishing Group.

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

purity and crystallinity of metal–organic frameworks by measuring
the full-widths at half maximum (FWHM) of their XRD peaks.60 By
considering specific and well-defined features in the spectra, these
approaches avoid the difficulties associated with automating
phase identification from multivariate data. However, these tech-
niques are applicable only if the desired product forms throughout
most of the experimental trials, which may not be the case when
attempting to synthesize novel compounds. Moreover, it dis-
regards the formation of byproducts or impurities, which can
provide useful insights into why a synthesis attempt failed.

3.2 Multivariate in 1-D

A complete treatment of phase identification requires the analysis
of multivariate spectra. For crystalline inorganic materials, this
entails the application of XRD and comparing the sample’s
spectrum with reference data from sources such as the Inter-
national Centre for Diﬀraction Data (ICDD).61 However, this
comparison is complicated by variations that occur between
measured and reference patterns due to defects, strain, oﬀ-
stoichiometry, texture, and poor crystallinity. As a result, inter-
preting XRD spectra is generally an arduous process that must
be carried out by an expert. Even with state-of-the-art tools,

reliably automating phase identification for complex, multi-phase
spectra remains a longstanding challenge. The most popular
techniques used to complete this task are summarized in Fig. 9
and discussed below.

Historically, the analysis of diﬀraction data has been conducted
by decomposing spectra into discrete lists of peak positions (d) and
intensities (I) which are compared with reference data.62 Peak
search-match algorithms rely on a Figure of Merit (FoM) to
quantify the degree of similarity between pairs of d–I lists. A widely
used metric is the de Wolff FoM, which is inversely related
to the average discrepancy between observed and calculated
d-spacings.63 By calculating the FoM for all suspected reference
phases, the compound with the highest value may be chosen for
a given XRD pattern. However, the reliability of this method
hinges on the ability to extract diffraction peaks from the
measured spectrum, which becomes difficult in the presence
of peak overlap,
low peak intensity, or strong background
signal.64,65 These problems are exacerbated when a spectrum
contains many peaks (e.g., in low-symmetry structures or multi-
phase mixtures), and therefore the peak search-match approach
generally produces limited accuracy. In a study conducted by Le
Meins et al.,66 XRD spectra measured from ten distinct compounds

Fig. 9 Possible techniques for automating the interpretation of XRD spectra. Peak search-match algorithms rely on the identification of peaks and
comparison with reference data using a figure of merit (FoM). Full-profile methods compare entire spectra measured experimentally with reference
spectra, typically simulated, using a correlation metric. Deep learning employs neural networks trained on reference spectra to classify measured spectra
into constituent phases.

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

were provided to the broader research community with the task of
performing phase identification using peak search-match algo-
rithms. Based on results collected from 25 participants, only
80% of phases were correctly identified on average, even with
manual guidance by an expert, thus suggesting the need for
improved methods if automation is to be attained.

An alternative to the discrete peak search-match approach is
full-profile matching, where entire spectra are compared with
those of reference phases using a measure of correlation such
as cosine similarity, Pearson or Spearman coeﬃcients, or
dynamic time warping.67–69 By removing the need to explicitly
deconvolute individual peaks, analyzing the full profile provides
a more robust treatment of complex and low-symmetry XRD
patterns. Furthermore, this method can be combined with non-
negative matrix factorization to identify the combination of
compounds that best matches a measured spectrum, enabling
classification of multi-phase mixtures.70 However, the reliability
of full-profile matching remains limited when experimental
artifacts cause large changes in peak positions, widths, and
intensities. In a study by Iwasaki et al., an accuracy of 70% was
achieved with dynamic time warping for the classification of
multi-phase mixtures comprised of alloys spanning the Fe–Co–Ni
chemical space.71 Misclassifications were largely attributed to
variations in XRD patterns induced by off-stoichiometry of the
samples. To improve upon existing methods based on full-profile
matching, it is necessary to design an approach that can account
for the possibility of experimental artifacts.

Deep learning has more recently been used to automate the
interpretation of XRD spectra. In the initial study by Park et al.,
a convolutional neural network (CNN) was trained to categorize
the crystal symmetry of simulated patterns from 150 000 phases
in the ICSD.72 With 20% of spectra reserved for testing,
accuracies of 81% and 95% were achieved for the classification
of space groups and Bravais lattices respectively. Nevertheless,
characterization of experimentally measured spectra is compli-
cated by their diﬀerences from simulated patterns arising from
various artifacts. In later work by Vecsei et al., a neural network
was trained on simulated XRD patterns to classify symmetry as
described previously.73 The model was then applied to experi-
mentally measured spectra extracted from the RRUFF database,
producing a lower accuracy of 54% for space group classification.
To resolve these shortcomings, simulated spectra in the training
set can be augmented to include perturbations associated with
experimental artifacts. For example, Oviedo et al. demonstrated
that by stochastically varying peak positions and intensities in
simulated spectra using for training, the resulting CNN correctly
classified the space group for 80% of spectra measured from
metal halide thin films.54

In addition to symmetry classification, similar techniques
based on deep learning and data augmentation have also been
used to perform phase identification from experimentally
obtained XRD patterns.74 For example, Maﬀettone et al. trained
an ensemble CNN using simulated spectra augmented with
changes to peak widths, intensities, and background signals.75
Their model was tested on patterns measured from samples in
the Ni–Co–Al space, with 76% correctly identified. To handle

multi-phase mixtures, Lee et al. trained a CNN using multi-
phase spectra simulated from linear combinations of single-
phase patterns for 170 compounds in the Sr–Li–Al–O space.
Their model achieved a high accuracy of 98% when classifying
experimentally measured spectra obtained from mixtures of
high-purity powders including SrAl2O4, SrO, Li2O, and Al2O3.76
However, because the training procedure requires many linear
combinations of phases with varied weight fractions to be
sampled (1 785 405 in total), it restricts the inclusion of experi-
mental artifacts owing to combinatorial explosion. Therefore, the
model may fail when applied to characterize arbitrary samples
obtained from a synthesis trial, which often contain substantial
perturbations in their XRD spectra. With this limitation in mind,
a more reliable approach is needed to characterize complex
spectra produced by multi-phase mixtures, as will be discussed
further in Section 5.

In addition to XRD spectra, deep learning has also been
extended to automate the characterization of materials using
Raman and Fourier transform infrared (FTIR) spectroscopy. In
contrast to XRD, however, simulating Raman and FTIR spectra is
more diﬃcult because it involves the calculation of vibrational
frequencies through ab initio methods. Accordingly, Liu et al.
instead used experimentally measured spectra from the RRUFF
database to train a CNN.52 Data sparsity was overcome by
augmenting the available spectra with stochastic changes in
Raman shifts for each vibrational spectrum. The model correctly
identified 88% of the chemical species tested, exceeding the
accuracies of techniques that use similarity-based metrics.77
These results show that a reliable classification of vibrational
spectra can be automated in situations where suitable experi-
mental data is available; however, this is generally not the case as
clean and consistently measured vibrational spectra are diﬃcult
to find for most chemical spaces. Moreover, additional eﬀort is
necessary to determine whether deep learning can be used for
spectra measured from multi-phase mixtures, where peak overlap
is likely to be problematic.

3.3 Multivariate in higher dimensions

Imaging techniques have recently found use in partially automated
workflows to accomplish tasks related to quality assurance or
verification that the target materials were indeed synthesized.
For example, images obtained from scanning electron microscopy
(SEM) have been used to guide the optimization of fiber quality in
polymeric samples by allowing the user to rank the images
obtained after each experimental iteration.78 SEM has also been
used to check the quality of graphene79 and carbon nanotubes21
after automated growth procedures were carried out. Similarly,
optical microscopy was employed to ensure a low defect density in
organic thin films synthesized by Ada.12 In all cases, however,
manual analysis of the images was required. If this process could
instead be automated, the loop between experimentation and
interpretation could be closed.

Deep learning is well-suited to handle high-dimensional
multivariate data including images and tomograms. Its application
to inorganic materials was first demonstrated by Al-Khedher in a
study on CNTs, where a neural network was used to classify the

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

degree of alignment and curvature of nanotubes imaged by SEM.80
Training was performed on two datasets, each labeled with values
describing their alignment and curvature: one based on idealized
‘‘rope’’ images representing nanotubes in various orientations,
and another containing experimentally obtained images depicting
actual CNTs. By combining these images into a single dataset that
was used to train the neural network, a classification accuracy
comparable to that of a human researcher was achieved. A similar
analysis of SEM images was designed by Modarres et al. to
categorize the shape and morphology of nanomaterials using a
CNN.50 In their work, a training set was constructed by manually
labeling thousands of experimentally measured SEM images based
on ten categories including fibers, powders, and nanowires. The
resulting model correctly classified 90% of test images that were
obtained from experiment.

At higher spatial resolution, deep learning has also been
used to automate the analysis of images obtained with scanning
transmission electron microscopy (STEM). Several recent eﬀorts
have shown that CNNs are capable of mapping out atomic
positions and identifying defective regions (e.g., vacancies or
dislocations) in atomic-scale images.81–83 This can be achieved
by training the model on large sets of experimental data with
the locations and sometimes chemical identities of atoms or
defects manually labeled. Resulting accuracies can match or
even exceed that of a human researcher, likely because the task
being performed requires large amounts of data to be analyzed –
i.e., a human mapping out hundreds of atoms in an image is
likely to make occasional mistakes, whereas AI has the advan-
tage of steady consistency.

In three dimensions, the analysis of mixtures imaged by
atomic probe tomography (APT) has been automated with deep
learning to identify interfacial regions between distinct phases.84
Madireddy et al. employed a transfer learning technique where a
CNN was trained on a large number of completely unrelated
images with labeled edges such that it could then be applied to
detect interfaces in APT images. Interestingly, even though the
training set appeared very diﬀerent from the test set, accurate
phase segmentation was obtained by the model when applied to
an alloy containing precipitates suspended in a matrix; though,
occasional irregularities occurred when compositions smoothly
varied and therefore the interfaces between phases were ‘‘blurred.’’
The largest obstacle faced throughout many of the existing
deep learning methodologies is the limited availability of
training data. The measurement and organization of novel data
using methods such as electron microscopy and APT are often
time-consuming and expensive. Furthermore, supervised training
relies on manual labelling of features in images, which can be
tedious and prone to errors – mistakes have been mitigated in past
work by relying on more than one researcher to label a single set of
images.82 To avoid these difficulties, training data may be simu-
lated rather than measured. However, as opposed to XRD spectra,
simulating realistic images is challenging and sometimes not
possible. Therefore, to generalize the application of deep learning
for image analysis in materials science, a rapid and more reliable
method of tabulating data is needed. We note that an auto-
mated platform may be suitable for this purpose, given that

large amounts of data can be generated quickly without much
human intervention. If sufficient training data cannot be obtained,
then unsupervised learning may be employed to reveal similarities
and differences throughout large sets of images, a particularly
useful approach if data is obtained in HT.

4. Decision making

Upon conducting a set of experiments and interpreting the
resulting data, the next step in the closed-loop automation
process is to use this information to make decisions regarding
the subsequent experiments to be performed. These decisions
are usually made with the goal of optimizing some quantity;85
for example, maximizing the yield of a product by modifying its
synthetic procedure86 or tuning the properties of a material with
respect to its structure, composition, or processing conditions.12,51
Alternatively, decisions can be made to formulate experimental
tests that reveal information regarding a specific process.87 In
synthesis, for example, this may entail exploring various combina-
tions of reactants and conditions followed by observation of their
products to construct a network of possible reaction pathways in a
system of interest. Regardless of the underlying motivations, the
desired outcome of decision making remains the same: reaching a
pre-defined optimum while minimizing time and costs. To this
end, a variety of active learning techniques exist to iteratively learn
from and query data in the design space.9,88,89 Before reviewing
available active learning algorithms, it is first important to
understand why active learning is necessary by considering
the alternative methods listed in Fig. 10 and highlighting their
shortcomings.

A simple and widely used optimization strategy is to perform
a brute-force search of the design space, thus avoiding decision
making altogether. Such is the concept underlying HT work-
flows, where a grid of data points is generated from combinatorial
sampling of experimental parameters.90,91 From this dataset,
analysis may then be conducted ex post facto to identify relation-
ships among variables and estimate any optima in the objective of
interest. As the reliability of these conclusions depends on how
well the design space has been sampled, a large number of
experiments are typically necessary to obtain satisfactory results.
Consequently, successful applications of HT platforms have been
limited to problems for which (a) the appropriate experiments are
inexpensive, quick, and easily parallelized, or (b) the design space
of interest is relatively narrow. A suﬃciently dense sampling of
compositions on thin films spanning ternary spaces, for example,
can typically be achieved using several hundred samples.92,93 In
contrast, generating a grid of equal density for quaternary systems
requires several thousand samples. Additionally, process variables
may add extra dimensions to the design space. As the number of
necessary experiments scales exponentially with the dimension of
techniques quickly become
the design space, combinatorial
intractable when many variables are introduced. These problems
are sometimes simplified by partitioning the design space and
focusing on a much smaller subset of interest;94,95 however, this
solution is not generalizable because the most interesting region

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

Fig. 10 A schematic illustrating three possible optimization techniques. Combinatorial approaches sample many possible combinations of design
variables (ni), sometimes chosen uniformly across the design space. Passive learning employs existing data points (blue dots) to form a model of the
objective and make predictions regarding the location of its optimum (shaded region). Active learning builds upon this approach by suggesting new
points at which to evaluate the objective (purple dots), from which the information is used to update the initial predictions and once again suggest new
points to be queried (red dots), forming an iterative loop which is traversed until convergence to the true optimum is reached.

of the design space is generally unknown. Therefore, to eﬃciently
explore the entire design space, active learning is required.

Contrary to HT experimentation, existing data can be used
to learn trends and predict optima in the objective function
without performing any new experiments. As the learner simply
observes the environment without interacting with it to query
new information, this technique is sometimes called passive
learning to distinguish it from its active counterpart.96 Enabled
by the development of machine learning models and a growing
amount of available data,2,3,97 passive learning has found
widespread use throughout materials science. For a detailed
overview of common machine learning algorithms and their
application in materials science, we refer the reader to several
recent reviews on the topic.98–100 Here, we narrow our discus-
sion to focus on two key limitations of passive learning as
applied to optimization. First, the accuracy of the model is
heavily reliant on both the volume and diversity of training
data. In many situations, the design space of interest is sparsely
populated. For example, applying machine learning to inorganic
synthesis remains difficult because there are often few procedures
reported to make a given compound, and that information must
be extracted from the literature as relevant synthesis databases are
limited.25,101,102 Moreover, even in cases where more data is
available, it tends to be biased toward specific regions of the
design space. This bias commonly originates from a tendency for
researchers to only publish positive results while leaving negative
results unreported,103 or because many studies pursue minor
modifications of an already successful material/procedure. Such
data bias will limit the diversity of the training set and negatively
affect the performance or applicability of the corresponding
model. In addition to the limitations imposed by the sparsity of
training data, passive learning models are inherently inept at
predicting outliers, instead relying on the recognition of general
trends in the data. While this capability is sufficient for many
studies, it becomes problematic for optimization problems where
the global extrema are of interest. To overcome these limitations,
it is necessary to acquire new data so that the model can
continuously learn and improve its accuracy, thus ensuring
correct identification of optima.

As will be discussed below, active learning techniques are
gaining traction throughout materials science, with multiple
applications recently demonstrated in automated experimental
workflows.104–107 We emphasize that the decision-making process
used in active learning follows a natural approach, similar to that of
a human expert – performing an appropriate set of tests, using the
results to build knowledge of the system, and implementing that
knowledge to intuitively select new tests – typically in a serialized
nature as to avoid unnecessary experiments. Considering this para-
digm, we review two major categories of active learning as applied to
decision making in optimization: black-box and informed.

4.1 Black-box optimization

In situations where little is known about the system at hand,
the corresponding objective function can be treated as a ‘‘black
box,’’ i.e., an opaque function that must be queried at individual
points through experimentation or simulation. Performing black-
box optimization, a topic that has been studied extensively and
applied throughout many areas of science and technology,
requires the consideration of two key constraints.108 First, as no
analytical form of the objective function is available, optimization
must be carried out without the use of exact derivatives. Second,
the objective landscape may generally be non-convex, requiring
global instead of local optimization. These properties exclude the
application of explicit gradient-based and pure local search
methods respectively. Moreover, extending black-box optimiza-
tion specifically to experimentation presents an additional
challenge: evaluation of the objective is usually expensive and
time-consuming, stressing the importance of reaching conver-
gence in a minimal number of steps.8 The high cost of data
acquisition further excludes algorithms that approximate deriva-
tives via finite diﬀerences owing to their ineﬃciency with respect
to the number of evaluations required. Instead, a variety of
eﬃcient and derivative-free techniques have been developed to
perform global optimization on black-box functions.109,110 To
shed light on which of these approaches are most suitable for
accelerating inorganic materials discovery, we review those that
have been successfully implemented in experimental workflows
and outline the major advantages and limitations of each.

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

4.1.1 Genetic algorithms. Many of the earliest methods
used to replace brute-force optimization were based on genetic
algorithms (GAs).90 In this approach, an initial batch (or
generation) of experiments is conducted to evaluate the objective
function(s). From the results, a new batch of experiments is
suggested based on three processes: (i) selection dictates which
samples are chosen to contribute to the next generation of experi-
ments, (ii) crossover determines how the properties of selected
samples are merged to suggest new experiments, and (iii) mutation
applies random variations to the properties of suggested experi-
ments. Each process is controlled by a set of hyperparameters (e.g.,
the rate at which mutation is applied) defined by the user. From the
corresponding modifications, new generations of experiments are
iteratively produced until convergence of the objective function(s) is
reached. Because GAs impose a bias toward promising regions of
the design space by selectively sampling experiments where the
objective function is expected to be optimal, they generally provide
increased eﬃciency relative to combinatorial techniques. GAs
are also well-suited to handle a large number of variables, both
qualitative and quantitative, and can perform well in multi-
modal design spaces assuming that a suﬃciently high mutation
rate is used to escape local optima.111,112

For experimentation in materials science and chemistry,
GAs have found widespread application in the discovery of novel
catalysts.113 In such problems, where the aim is to maximize the
yield of a desired product phase with respect to the choice of
catalytic materials, traditional HT methods commonly become
intractable because realistic systems have highly complex design
spaces – industrial catalysts often contain as many as ten elements
and can be further complicated by the choice of a support
material.114,115 Addressing this challenge, work in the early 2000s
pioneered the implementation of GAs on batched heterogeneous
catalysis experiments. Wolf et al. demonstrated a proof of concept
by optimizing the composition of mixed metal oxide catalysts
containing eight unique components for the oxidative dehydro-
genation of propane.116 The GA achieved significantly increased
propene yield within only four generations, corresponding to a
total of 224 experiments. This number represents an improvement
for which
over the previously used combinatorial methods,

thousands of experiments were required in comparable systems.117
However, the authors emphasize that the GA performs well only after
its underlying hyperparameters were tuned through a series of tests
conducted using a ‘‘pseudo-dataset’’ generated by heuristic relation-
ships that approximate the effect of catalyst composition on the
reaction yield. Alternatively, to improve upon the accuracy of
heuristic relationships, machine learning models (e.g., neural
networks) have been used to construct pseudo-datasets that
assist in choosing the best-performing hyperparameters for a
GA.114,118,119 This method is applicable when a sufficient
amount of experimental data is available to train the model
on, and therefore may not be used in novel chemical spaces.

Outside of catalysis, GAs have also been applied to handle
synthesis procedures where the concentrations of precursors
and conditions are varied to optimize the yield and form of a
target phase. Moosavi et al. designed a robotic platform guided
by a GA to carry out experiments with the aim of maximizing
crystallinity and phase purity in metal–organic frameworks.60
Based on microwave-assisted synthesis, the search space con-
sisted of nine parameters involving reactant ratios, solvent
compositions, microwave power, environmental temperature,
and reaction time. Exploration of these variables was conducted
through three generations consisting of thirty experiments each.
Between each generation, a random forest model was trained on
data obtained from all previous experiments. The model was
used to predict the results of suggested experiments and excluded
any that were expected to yield unfavorable results (i.e., poor
crystallinity or phase purity). The authors propose that this
method improves the efficiency of the GA, which itself only
considers results from the previous generation. Indeed, Fig. 11
shows that a large fraction of the population has converged to a
narrow region of the design space by the third generation, with
the corresponding samples having high crystallinity and phase
purity. A similar approach was used by Nikolaev et al. to optimize
the growth rate of carbon nanotubes with respect to the system’s
temperature, pressure, and partial pressures of ethylene, hydro-
gen, and water vapor.21 Ten generations containing 84 samples
each were produced under the guidance of a GA. A random forest
model was trained between each generation and used to bias

Fig. 11 Results obtained during the optimization of synthesis conditions for metal–organic frameworks, guided by a genetic algorithm. (a) A dimension
reduction of trials conducted in the 9-dimensional parameter space onto a 2-dimensional plane, showing the convergence of experiments to an optimal
subspace. (b) Evolution of sample crystallinity throughout three generations. Reproduced with permission.60 Copyright 2019, Nature Publishing Group.

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

suggested experiments toward high expected growth rates. By the
final batch of experiments, the samples were grown at a rate
nearly 100(cid:2) more rapid than in the initial experiments.

Although GAs are capable of reaching convergence within
relatively few generations, each population must contain a large
number of individual experiments to achieve genetic diversity and
ensure reliable performance. Depending on the dimensionality of
the design space and the complexity of the associated objective
function, suitable population sizes may range from tens to
hundreds of samples.120 As a result, GAs excel when applied to
problems for which parallelization of many experiments can be
attained while keeping the associated time and costs reasonably
low. In more general situations, however, experiments tend to be
resource-intensive and large-scale parallelization can be diﬃcult
or impractical. Such cases therefore necessitate optimization
algorithms that reach convergence in a minimal number of total
experiments conducted either serially or in small batches.

4.1.2 Stable noisy optimization by branch and fit. The SNOBFIT
(Stable Noisy Optimization by Branch and FIT) algorithm121
combines aspects from local and global search strategies to
eﬃciently optimize an objective function. From a given dataset,
SNOBFIT employs a branching algorithm to partition the design
space into unique sub-regions, each containing a single known
datapoint. Within each region, a local model of the objective
function is constructed via least-squares quadratic fitting of the
contained datapoint and its nearest neighbors. These models
represent the objective function locally but do not necessarily
describe it globally – i.e., each quadratic fitting is performed
independently using a subset of known datapoints. The resulting
models are then used to predict and suggest sampling of new
datapoints in regions where the objective function is expected to
be optimal. At the same time, sampling is also suggested in
sparsely populated regions to ensure the global optimum is not
missed.

For automated experimentation, perhaps the most successful
application of SNOBFIT is in the optimization of chemical reactions
in continuous flow reactors.122,123 This was first demonstrated by
Krishnadasan et al., who maximized the fluorescence of CdSe
nanoparticles with respect to precursor flow rates in a microfluidic
reactor.20 SNOBFIT was used to minimize a ‘‘dissatisfaction coeﬃ-
cient’’ (DC) related to the diﬀerence between observed and desired
emission intensities produced by the samples. As shown in Fig. 12,
a minimum in the DC was found after performing 71 experiments,
with the final samples showing a near four-fold increase in emission
intensity relative to those initially measured. In a similar eﬀort, Li
et al. explored temperature-composition space to optimize circular
dichroism (CD) in inorganic perovskite nanocrystals.33 Experiments
suggested by SNOBFIT quickly identified a local optimum in less
than 50 trials, but then continued to converge toward an improved
solution exhibiting a CD intensity twice that of the initial optimum.
These results highlight the ability of SNOBFIT to escape local
optima by sampling sparsely populated regions of the design space
as opposed to relying on greedy optimization that only exploits well-
sampled regions.

Increasing the number of variables under consideration,
Be´dard et al. designed a reconfigurable flow reactor capable

Fig. 12 A visualization showing optimization of the dissatisfaction coeﬃcient
(DC) with respect to CdO and Se flow rates in the synthesis of CdSe
nanoparticles. Black points represent experimental results, which are pro-
jected onto the bottom plane and colored such that blue/red dots correspond
to samples with DC values greater/lesser than the median value of 0.26. The
spectrum obtained from the best sample found (with a DC value of 0.19) is
displayed by the inset, showing a high emission intensity at 530 nm.
Reproduced with permission.20 Copyright 2007, Royal Society of Chemistry
Publishing.

of probing multistep organic reaction sequences and maximizing
the corresponding yield through optimization with SNOBFIT.31 To
demonstrate this capability, six diﬀerent series of experiments
were carried out for a variety of processes including amination,
olefination, cross-coupling, and substitution. In all cases, high
product yield was obtained in less than 50 experiments by varying
temperature, flow rates, and catalyst compositions. However, the
authors note that reasonably tight bounds were placed on the
design variables using information obtained in previous work,
thereby reducing the problem’s complexity. A comparable perfor-
mance of SNOBFIT was illustrated in the work of Cherkasov et al.,
where the algorithm successfully identified an optimum in 61
trials to minimize a composite objective function incorporating
product yield and substrate flow rate with respect to three synth-
esis parameters.124

Although SNOBFIT often improves eﬃciency relative to
combinatorial methods and GAs, it displays several shortcomings
that limit its applicability to certain optimization problems. First,
its performance deteriorates when applied to problems with
high-dimensional parameter spaces; studies have shown that
SNOBFIT begins to underperform compared with many other
global optimization techniques in cases where there are ten or
more independent variables to consider.125 Second, SNOBFIT is
not capable of directly handling multi-objective optimization
procedures.126 An alternative route to deal with such problems
is to instead optimize a composite objective function defined to
capture changes in multiple quantities, however, this method
gives no information regarding the trade-oﬀ between properties

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

as would be revealed by the Pareto front. Last, SNOBFIT operates
by establishing a set of individual models (e.g., quadratic func-
tions) fit to approximate local regions of the objective function
without providing a global model for the entire system. This
approach therefore limits interpretability and makes it diﬃcult to
draw conclusions regarding general relationships between the
variables and objectives.

4.1.3 Bayesian optimization. One of the most popular
techniques for optimizing costly black-box objective functions
is Bayesian optimization,127–129 which is designed to minimize
the total number of experiments required to reach convergence.
To accomplish this, optimization is carried out on a known and
differentiable surrogate model rather than on the objective
function itself.108,109 As shown in Fig. 13, the surrogate model
approximates the objective function using all available data
points (e.g., from previously conducted experiments). This
approximation is given by a probabilistic distribution of functions
known as the prior, which is actively updated as new datapoints
are sampled to form a posterior distribution that more closely
resembles the true objective function. Calculating the prior and
posterior are essentially regression problems that can be solved
using a number of techniques, making Bayesian optimization
versatile with respect to the types of data it can handle. Two
models that are most commonly used for regression are Gaussian
processes (GPs) and random forests (RFs), which typically work
well with continuous and discrete search spaces respectively.8,127

Fig. 13 A schematic of the Bayesian optimization procedure. An approxi-
mation to the actual objective (solid black line) is given by the surrogate
model (dashed black line), which is constructed to fit all known observations.
Using the expected values and uncertainties (blue) given by this model, an
acquisition function (green) is built. The maximum of the acquisition function
is then identified to suggest new points at which to evaluate the objective,
leading to increased refinement of the surrogate model. Here, a somewhat
exploitative approach is used to select new evaluations near the predicted
optimum. Reproduced with permission.133

To analyze the surrogate model and choose the datapoints
sampled during optimization, an acquisition function is used.
The main task of the acquisition function is to query the objective
function in a way that balances exploration and exploitation.
Exploration aims to sample regions of the design space where
uncertainty in the surrogate model is high, therefore aiming to
improve the accuracy of the model and capture the global opti-
mum. Exploitation uses predictions of the surrogate model to
sample regions where the objective function is expected to be
optimal. A purely explorative search requires an excessive number
of evaluations to reach convergence whereas a purely exploitative
search is prone to missing the global optimum, necessitating a
trade-oﬀ between these two extremes. Some commonly used
acquisition functions include expected improvement (EI), entropy
search (ES), and upper confidence bound (UCB) as described in
detail by past work.130 It is important to keep in mind that no
single approach is universally suited for all optimization problems
(in accordance with the ‘‘no free lunch’’ theorem131). Rather, the
acquisition function should be chosen to best suit the properties
of the objective function at hand. For example, EI and UCB
usually converge more rapidly than ES but are less explorative
and therefore less suitable for objective functions with many
local optima.130,132

One of the first applications of Bayesian optimization to
automated experimentation for materials design is described
by Xue et al.51 The goal of their work was to minimize thermal
hysteresis eﬀects in NiTi-based shape memory alloys by varying
their composition. Although the corresponding samples could
be represented using three simple variables (x, y, and z in
Ni50(cid:3)x(cid:3)y(cid:3)zTi50CuxFeyPdz), the authors instead chose to map
each composition into a higher-dimensional feature space
containing information regarding the valence electron concen-
tration, atomic radii, and electronegativity to capture electronic
contributions to thermal hysteresis. To investigate the resulting six
parameters, several surrogate models and acquisition functions
were tested on a dataset of 22 randomly chosen experiments. A
support vector regression model was found to outperform GPs as a
surrogate model, and the most suitable acquisition function was
identified as the knowledge gradient – a slight variant of EI that
performs well when dealing with noisy objective functions.134
Accordingly, this combination was used to perform a series of
58 new experiments that converged after ten iterations. Thermal
hysteresis was decreased by as much as 42% relative to the
initial samples. Furthermore, the surrogate model was found to
accurately describe the objective landscape surrounding the
optimum as reflected by a close agreement between predicted
and experimentally measured values in the final few iterations.
A number of reports have extended Bayesian optimization to
a greater variety of material systems and properties. This
includes a study by Li et al., where the synthesis procedure
used to generate short polymer fibers was optimized to control the
corresponding fiber size and shape with respect to precursor flow
rates and reactor dimensions.78 Using GPs and EI as the surrogate
model and acquisition function, a five-dimensional parameter
space was explored in three diﬀerent series of trials, each toward
a unique target fiber shape specified by the researchers. With only

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

20 experiments conducted per series, the results were shown to be
highly dependent on the target to be optimized for. The authors
tested whether changing the initial sampling of experimental
parameters would improve the rate of convergence; however, they
found that the results remained largely unchanged. We note that
the mixed performance of Bayesian optimization in this situation
can possibly be attributed to the low number of experiments
conducted to search the broad, five-dimensional space of interest.
More recent work employed Bayesian optimization to build
upon previous eﬀorts involving autonomous carbon nanotube
synthesis.22 As discussed earlier in Section 4.1.1, this problem
was originally approached using a GA, which identified optimal
nanotube growth conditions over the course of 840 experiments.21
In contrast, Chang et al. revealed that optimization with GPs
produced a similar set of optimal conditions in less than
200 experiments, therefore confirming the improved eﬃciency
achieved using Bayesian techniques as opposed to GAs. However,
the work also demonstrated that the performance of Bayesian
optimization varies with respect to its underlying methods and
hyperparameters. For example, when the three diﬀerent kernel
functions listed in Fig. 14(a) were used to define covariance, a key
similarity measure employed in fitting the GPs, the optimized
growth rates diﬀered by as much as 15%. Even larger discrepan-
cies were found to coincide with the choice of acquisition
function, highlighting the importance of balancing exploration
and exploitation. As shown in Fig. 14(b), both UCB and EI
perform well, whereas a purely exploitative approach known
as the maximum probability improvement (MPI) converges to a
sub-optimal solution.

In place of an acquisition function, experiments can also be
suggested using reinforcement learning (RL), a class of algorithms
designed to interact with and learn from the environment. The
objective in RL is to build a policy function that suggests actions
(e.g., experiments) from a given set of states (e.g., design variables)
to produce an outcome that maximizes a pre-defined reward

function. By iteratively suggesting actions and observing their
outcomes, the policy function is improved to give better results
(i.e., higher reward) as more data is collected – this is similar to
refinement of the surrogate model during Bayesian optimization.
RL has recently been applied to the optimization of chemical
syntheses conducted in flow reactors.135 For example, Zhou et al.
designed a policy function based on a recurrent neural network
(RNN) that suggested changes in the temperature and precursor
flow rates to maximize the reaction yield in four different mole-
cular syntheses.86 As illustrated in Fig. 15, the RNN was iteratively
refined using all past experimental outcomes to optimize a reward
function related to the yield. To avoid being overly exploitative, the
authors employed a randomized exploration policy whereby
new experimental parameters were drawn from a probabilistic
distribution rather than from a deterministic model. Using this
policy, maximal yield was achieved across all four reactions in less
than 50 experimental iterations. For comparison, SNOBFIT did not
reach convergence within 50 iterations, supporting the improved
efficiency of RL when experiments are conducted serially. How-
ever, we note that RL tends to fail when the reward function is
sparse (i.e., when favorable outcomes are rare) and therefore may
not be suitable for some high-dimensional design spaces. For such
problems, a parallelized approach is preferred to more rapidly
sample the space and identify optimal regions.

To improve upon existing methods and formalize a comprehen-
sive tool for Bayesian optimization in the context of chemistry, the
Probabilistic Harvard Optimizer Exploring Non-Intuitive Complex
Surfaces (Phoenics) algorithm was developed.8 The surrogate model
and acquisition function in Phoenics are designed to evaluate costly
and non-convex objective functions through iterative batches of
experiments conducted in parallel. Because of its eﬃcient rate of
training, a Bayesian neural network (BNN) is chosen to approximate
the objective function. While providing comparable performance
to GPs, the time required to train a BNN scales linearly with the
number of observations whereas GPs scale cubic.136 Hence, using

Fig. 14 Results showing the evolution of growth rates measured during the synthesis of carbon nanotubes, with optimization carried out using a
Bayesian approach. Gaussian processes are implemented as the surrogate model and three diﬀerent kernel functions, listed in (a), are used to define
covariance. In (b), the Matern52 kernel is employed with three diﬀerent acquisition functions: upper confidence bound (UCB), expected improvement
(EI), and maximum probability of improvement (MPI). Reproduced with permission.22 Copyright 2020, AAAS.

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

This method was tested on a set of multi-modal objective functions
(e.g., the Ackley and Schwefel functions), with convergence achieved
more rapidly than optimizations based on GPs and RFs in all cases.
The Phoenics algorithm has been implemented in the
ChemOS software package9 to carry out Bayesian optimization
with fully autonomous experimental platforms in two studies.
MacLeod et al. engineered a self-driving laboratory to maximize
the hole mobility in organic thin films by tuning their annealing
time and dopant concentration.12 Given the low-dimensional
search space involving only two parameters, convergence was
obtained in less than 30 experiments, yielding a near ten-fold
improvement in the mobility relative to initial samples. Applying
the Phoenics algorithm to a more complex problem, Burger et al.
designed a mobile robotic chemist that performed the necessary
experiments to optimize the eﬃciency of aqueous photocatalysts
for hydrogen evolution.13 Based on a set of educated hypotheses,
ten chemical species were identified as promising components in
the catalysts. Bayesian optimization with Phoenics was used
to explore the space of concentrations for each component.
Despite the high dimensionality of this problem, the algorithm
successfully reached convergence in about 600 evaluations
conducted in batches of 16 experiments over the course of eight
days. As illustrated in Fig. 16, the resulting catalyst mixtures
displayed hydrogen evolution rates exceeding the baseline values
by a five-fold margin.

4.1.4 Summary. The examples reviewed in this paper sup-
port the eﬃcacy of black-box optimization as applied in a variety
of experimental workflows, with the Bayesian approach providing
a particularly eﬃcient route toward identifying global optima
while minimizing the number of trials required. However, the

Fig. 15 (Top) An outline of the RL workflow used to optimize the yield of
chemical reactions with respect to their experimental conditions. (Bottom)
An illustration showing how a recurrent neural network (RNN) is iteratively
refined suggest experiments that maximize the yield. Reproduced with
permission.86 Copyright 2017, ACS Publications.

the BNN as a surrogate model ensures the training step is not rate-
limiting in the optimization process, which becomes particularly
important when the number of evaluations is large (e.g., in high-
dimensional design spaces). A customized acquisition function is
defined to balance exploration and exploitation through a control
parameter set by the user. Batched experiments are chosen
by randomly sampling the control parameter such that some
experiments are highly explorative, while others favor exploitation.

Fig. 16 Results obtained during the automated optimization of hydrogen evolution mediated by a photocatalyst with varied composition.
(a) Experimental measurements taken throughout a series of trial guided by Bayesian optimization. (b) A radar plot showing how the sampling of
parameters changed over the course of optimization, with the shaded region boundaries representing the volume of each component dispensed after
distinct numbers of experiments. Reproduced with permission.13 Copyright 2020, Nature Publishing Group.

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

performance of these techniques is limited by their inherently
agnostic treatment of the objective, i.e., they make no assump-
tions regarding the underlying properties of the system at hand.
As a result, black-box optimization methods tend to become
intractable when (a) the design space is high-dimensional and
requires many evaluations to reach convergence, or (b) the
majority of evaluations yield trivial results, which occurs if the
objective function is constant-valued throughout large regions
of the design space. Moreover, while black-box optimization
methods are capable of illustrating trends in the data, further
analysis must be carried out to relate these trends to physical
phenomena.

4.2 Informed optimization

In contrast to black-box optimization techniques that learn and
make decisions based solely on relationships between design
variables and observed values of the objective function, informed
optimization gains further insights by incorporating prior knowl-
edge of the system into the optimization pipeline. In doing so, it
may be possible to increase the eﬃciency with which the design
space is explored, improve confidence in the identification of
the global optimum, and provide results that are directly inter-
pretable. As discussed by von Rueden et al.,137 devising an
informed optimization algorithm requires the consideration of
three questions: (1) what is the source of prior knowledge,
(2) how is the corresponding information represented, and
(3) where is the information integrated into the workflow? For
experimentation in the physical sciences, possible solutions to
these questions are summarized in Table 1.

Physics-based relations such as Arrhenius equations or
chemical descriptors (e.g., molecular properties such as dipole
moments) are common sources of information that can be
integrated with optimization algorithms to improve their
eﬃciency.138,139 Such information is often represented using
algebraic expressions that map experimental variables onto an
objective function – e.g., correlating temperature with reaction
rates – which leads to an improved representation of the objective
function and therefore fewer experiments to identify global
optima. Data obtained from past calculations or experiments
can also be used to bias exploration of the design space toward
subspaces where the objective is expected to be optimal.140 This
bias can be imposed by creating an ensemble of acquisition
functions from all data sources, with each weighted by its reliability,
and considering the product of all acquisition functions to suggest
new experiments. Hereafter, we refer to such methods as data
fusion. Alternatively, when suitable physics-based relations or

data sources are unavailable, expert knowledge and intuition
can be used to develop hypothetico-deductive models that use
knowledge graphs or decision trees to iteratively form hypotheses
and suggest experiments designed to confirm or disprove these
hypotheses.141,142 As these models sometimes contain many
possible steps, ML techniques such as Monte Carlo tree search
or RL have been used to aid exploration.143 The hypothetico-
deductive modeling approach is particularly promising because it
provides a high degree of interpretability; however,
it also
requires detailed planning regarding possible experimental out-
comes and their implications for the system. To highlight the
strengths and weaknesses of data fusion and hypothetico-deductive
modeling, several key examples of their applications in materials
science and chemistry are discussed below.

4.2.1 Data fusion. In the context of optimization, data fusion
refers to the mapping of information from multiple sources onto
an ensemble model where all knowledge is represented using a
single composite function.144 This method is commonly used to
obtain an optimal balance between theory and experiment – the
former is cheap to evaluate but prone to inaccuracy, whereas the
latter is accurate but expensive to carry out. For example, we
consider the relationship between the thermodynamic stability of
materials, calculated via density functional theory (DFT), and
their synthesizability observed in experiment under a given set of
conditions. While these two properties tend to be correlated for
many materials, they do not always agree with one another as
kinetic barriers can prevent a system from reaching its equili-
brium state (discussed in Section 5.3).145 Bridging the gap, Sun
et al. employed data fusion to combine DFT-calculated Gibbs free
energies of mixing with observed instabilities in halide perovs-
kites to guide experiments toward maximizing the stability of
samples with respect to their composition.140 A layout of the
process is shown in Fig. 17(a). After initially performing DFT
calculations to predict the free energy of mixing across a grid of
compositions in the (Cs-MA-FA)PbI3 space, a ‘‘physics-informed’’
Bayesian optimization technique was used to model stability and
suggest experimental trials. Data fusion was accomplished by
modifying the EI acquisition function to incorporate a probabilistic
distribution constructed from a fit of the free energy data. This
modification biased the suggested experiments toward compo-
sitions where the DFT-calculated free energy of mixing was
highly negative and therefore stability was predicted to be
strong. Following the data fusion approach, 112 samples
were tested over the course of four experimental iterations. As
illustrated in Fig. 17(b), guidance by DFT enabled rapid con-
vergence to a narrow subspace displaying high stability within

Table 1 Taxonomy of the informed optimization approach. Listed are several common examples of knowledge sources, forms of representation, and
routes for integration into the optimization pipeline. Adapted from von Rueden et al.137

What: source

Physics-based relations
First principles calculations
Past experimental results
Expert intuition

How: representation

Algebraic equations
Diﬀerential equations
Probabilistic relationships
Logic-based rules
Knowledge graphs

Where: integration

Parameter constraints
Guided exploration
Modified outcomes

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

Fig. 17 (a) Closed-loop process mediating the optimization of stability in halide perovskites, ((Cs-MA-FA)PbI3), for which free energy data obtained from
DFT calculations is integrated into the traditional experimental procedure. (b) The expected improvement (EI) acquisition function is fit to experimental
measurements of stability, then modified to account for predictions of DGmix from DFT. (c) After an initial uniform sampling of compositions, experiments
(black dots) are guided by the Bayesian optimization algorithm, showing convergence to narrow regions of the composition space with robust stability.
Reproduced with permission.140

the first batch of experiments, followed by minor variations in
composition throughout
the remainder of experiments to
further optimize the objective. These results demonstrate that
DFT calculations provide valuable prior insight that can be used
to inform optimization and ensure a more efficient exploration
of the design space.

Data fusion can also be used to improve the representation
of design variables. Shields et al. recently developed an informed
Bayesian optimization algorithm designed to optimize chemical
reactions by maximizing the yield of a target phase with respect
to the choice of precursors and synthesis conditions.138 Given a
set of promising reaction pathways, molecular precursors were
represented by chemical descriptors (e.g., dipole moments, molar
volumes, and electrophilicity) that were calculated in advance
using DFT. The relationships between these descriptors and the
objective function (the target yield) were modeled using Gaussian
processes. For each experimental iteration, a batch of reactions
were chosen according to Thompson sampling of the EI acquisi-
tion function. The authors first applied their algorithm to
optimize the direct arylation of imidazoles, for which the design
space included 12 ligands, four bases, three temperatures, and
three concentrations – totaling 1728 distinct reactions to be
explored. As a benchmark, all of these reactions were carried
out beforehand with HT experimentation, and the data was used
to set up a game where 50 expert chemists were asked to optimize
the reaction by iteratively selecting promising precursors and
conditions until they believed they had found the true optimum
(maximum target yield), or until a limit of 50 experiments was
reached. Although human experts typically identified better-
performing reaction pathways in early trials, the Bayesian

optimization algorithm surpassed the average human perfor-
mance within three batches of five experiments and obtained
99% target yield by the final batch. The algorithm was also
applied to several research problems with increased design
space complexity. For example, the Mitsunobu reaction146 was
optimized with respect to 180 000 possible reactions derived
from 12 phosphines and five solvents with varied concentrations.
In only four batches of 10 experiments, the optimizer identified
three sets of reactions conditions that gave improved yield over
the standard reaction, hence confirming the excellent perfor-
mance of the algorithm. We note that the marked success of this
approach relies on (i) a suitable choice of candidate reactions
(precursors and conditions) based on expert knowledge, and
(ii) DFT-calculated descriptors of the design variables, which
captures electronic and steric relationships between molecular
precursors and provides an improved representation over one-
hot encoding, where precursors are represented by dummy
variables (e.g., [1, 0, 0,. . .] and [0, 1, 0,. . .]) with no relation to
one another.

In the place of DFT calculations as an information source,
one may alternatively employ physical relationships based on
theoretical frameworks or empirical observations. For example,
Ren et al. utilized a data fusion approach to embed physics
domain knowledge into a Bayesian optimization procedure
designed to maximize the eﬃciency of GaAs-based solar cells
to their growth temperature.139 Given that
with respect
only temperature was considered as a free variable, a simple
black-box search method would likely suﬃce. However, the
authors emphasized that such an approach does not reveal why
that temperature maximizes solar cell eﬃciency. Instead, they

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

developed a hierarchical Bayesian model to reveal relationships
between the growth temperature and material descriptors
including dopant concentrations, carrier lifetimes, and recom-
bination velocities – each of which were related to the final
performance of the solar cell. To accomplish this, temperature
was mapped into a latent space represented by parameters that
were used to calculate the material descriptors via Arrhenius
equations, from which the efficiency of the corresponding solar
cell was predicted using a neural network trained on simulated
I–V curves. The model was used to guide a series of 25 experi-
ments, with the final batch of samples showing an efficiency
6.5% higher than the baseline value obtained from a grid
sampling of growth temperatures. For comparison, the authors
performed similar tests without the influence of the Arrhenius
equations, i.e., growth temperatures were mapped directly onto
the descriptors in a black-box manner. This approach led
to slower convergence and greater disagreement between
predicted and experimentally observed properties, therefore
supporting the advantages provided by data fusion.

4.2.2 Hypothetico-deductive models. For research problems
where the application of data fusion is restricted (e.g., when
relevant calculations cannot be performed prior to the experi-
ment), hypothetico-deductive models may instead be used to
actively learn from experimental results, interpret their implica-
tions for the system, and propose hypotheses to be tested by
subsequent experiments. King et al. pioneered the automation of
this approach in their design and application of a robotic scientist
named Adam.141 With the goal of identifying the genes encoding a
group of enzymes in yeast, Adam was engineered to systematically
probe a metabolic network describing all known biochemical
processes that occur in the organism. These networks consist of
nodes representing metabolites (i.e., intermediates and products)
that are connected through edges representing reactions catalyzed
by a known enzyme(s). If the genes encoding a specific enzyme are
removed from the organism through mutation, any reaction
catalyzed by that enzyme will be slowed.147 Based on this concept,
the authors constructed a decision tree with the following
structure: high-level nodes pose fundamental questions (what
genes encode an enzyme?), mid-level nodes form hypotheses
related to these questions (a list of suspected genes), and
low-level nodes suggest experiments to test the hypotheses
(measurements of reaction rates in mutated organisms). By
traversing this structure and iteratively proving or disproving a
series of hypotheses, Adam analyzes low-level experimental data
to propose solutions to high-level questions. The automated
platform was demonstrated to identify the genes encoding
13 diﬀerent enzymes in yeast, with all predictions confirmed
by manual experimentation. However, because the success of
Adam was enabled by the availability of detailed metabolic
networks extracted from bioinformatic databases,148,149 extension
to novel systems would require a re-design of the hypothetico-
deductive model to reflect the suspected genotype.

To extend hypothetico-deductive modeling to organic synthesis,
a reaction network may be used to illustrate possible pathways (i.e.,
intermediate reactions) originating from a set of precursors when
synthesizing targeted products. The hypothesized reactions can be

verified by carrying out the suggested syntheses and measuring the
yields of any expected intermediates and final products that
form using characterization techniques such as NMR. Given the
exceptionally large number of possible transformations deriving
from or giving rise to any arbitrary organic molecule, conceiving
detailed reaction networks is generally intractable for a human
researcher. Instead, a variety of techniques have been developed
for computer-aided synthesis planning (CASP),150,151 whereby
information taken from reaction databases along with chemistry-
based rules and heuristics are employed. In the context of optimi-
zation, CASP methods are often used to maximize the yield of a
desired product through retrosynthetic analysis, i.e., by starting
from the target molecule and working ‘‘backwards’’ through the
network to identify suitable precursors. To this end, Monte Carlo
tree search algorithms have been applied to traverse unique
branches in the reaction network and provide a ranking of
promising retrosynthetic routes and precursors.150 Techniques
based on RL have also been used to explore possible reaction
routes through a policy function that is trained to make optimal
decisions at each step in retrosynthetic planning, showing
improved eﬃciency relative to Monte Carlo tree search.143,152
Despite these successes, automated retrosynthesis has not yet
been fully integrated into a closed-loop workflow enabled
by iterative experiment-theory feedback, likely owing to the
large number of experiments that would be required and the
diﬃculties associated with automated and generalized identifi-
cation of molecules resulting from synthesis.

Simplifying the problem described above, Dragone et al.
created a robotic system designed to actively explore a reaction
network by searching for the most reactive pathways.153 Reactivity
was quantified using a ‘‘reaction selection index’’ (RSI), defined as
the mean squared error between the infrared spectrum of the
product and that of the reactants. As a proof of concept, the
authors worked with amide synthesis based on the reaction net-
work shown in Fig. 18. One core molecule was subjected to a
three-step reaction, where each step may involve four diﬀerent
reagents, resulting in 64 possible pathways (4 (cid:2) 4 (cid:2) 4). Possible
intermediates and products were predicted using chemistry-
based knowledge of likely transformations. To explore the net-
work, four reactions were carried out between the core molecule
and each reagent in the first generation. The reaction with the
highest RSI was then selected and its product was combined
with each reagent in the second generation to perform four new
reactions. By repeating this process across the second and third
generations, the most reactive pathway was identified (high-
lighted in Fig. 18) with a final product yield of 27%. This
task was accomplished in only 12 experiments, significantly
reducing the workload relative to a brute-force approach where
64 experiments would be necessary to explore all possible
pathways. Hence, the advantages of informed optimization are
realized not only by constructing an appropriate reaction net-
work to reach the desired product, but also by exploring the
network more eﬃciently with reactivity as a guiding metric.

4.2.3 Summary. A summary of the active learning techniques
discussed in this review is presented in Table 2. Relative
to black-box optimization techniques, both data fusion and

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

Fig. 18 (a) An illustration of the reaction network considered in the optimization of reactivity for a single core molecule undergoing reactions with four
possible reagents. Subsequent transformations are enumerated throughout three generations, with final products listed in the group of nodes labeled
with a, b, c, or d. (b) A schematic illustrating the reaction selection index (RSI) approach; as opposed to probing all possible pathways, only those with the
highest measured reactivity are investigated, therefore significantly reducing the experimental workload. Reproduced with permission.153 Copyright 2017,
Nature Publishing Group.

hypothetico-deductive modeling have been demonstrated to
accelerate convergence to global optima through integration
of physics-based or data-driven knowledge. To choose between
these techniques for future automated platforms in materials
science, consideration may be given to the types of properties/
processes being studied as well as the ability to extract relevant
data from databases or calculations. Based on the examples
reviewed here, we suggest that data fusion is well-suited to
optimize materials properties, such as stability or optoelectro-
nic performance, so long as they can be calculated (e.g., using
DFT) or deduced from empirical relations with design variables
(e.g., using Arrhenius equations). In contrast, although hypothetico-
deductive modeling has so far been limited to applications in
organic chemistry and biology, we propose that this approach
may be used to optimize complex materials processes. The synthesis
of novel inorganic compounds is a prime candidate for hypothetico-
deductive modeling because the underlying reactions may be

decomposed into sequences of reagents, intermediates, and
products – each of which can be verified through experimentation.
However, as will be discussed below, several key developments in
theory, characterization, and data availability are required before
informed optimization can be broadly extended to inorganic
materials synthesis.

5. Perspectives

The design of novel inorganic materials for any application
hinges upon the ability to synthesize targeted compounds. The
need for an expert to carefully plan and execute synthesis trials,
interpret their results, and design subsequent experiments
makes synthesis a time- and labor-intensive process. This limits
the amount of information-gathering experiments that can be
performed, instead requiring that the product be obtained in a

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

Table 2 Active learning techniques commonly used to guide autonomous experimentation. Summaries of their key strengths and weaknesses are listed.
Common applications demonstrated in previous work are also described

Methods

Strengths

Weaknesses

Use cases

Black-box optimization
Genetic algorithms

SNOBFIT

Bayesian
optimization

Informed optimization
Data fusion

Hypothetico-deductive
modeling

No model of the objective is given
Ill-suited to handle many (410) variables Optimization of flow reactions122–124

Catalyst discovery113–119

Can handle many variables and objectives Each batch requires many experiments
Few batches of experiments needed
Typically requires
Few experiments
Well-suited to handle noisy data
Attempts to minimize number of
experiments
A surrogate model for the objective
is given

Does not apply to multiple objectives
Optimization of the acquisition
function can be costly
Performance sensitive to the choice
of model

Optimization of material syntheses
and properties12,22,51,78

Readily integrated with black-box
techniques
Directly interpretable
Applicable to complex design spaces

Requires supplementary information
source (prior knowledge)
Requires substantial manual design
by the researcher

Chemical reaction optimization138
Phase stability investigation140
Genotype discovery141
Reaction network exploration153

black-box fashion (i.e., by trial-and-error). An autonomous
synthesis system could reduce the time for successfully making
new compounds and use prior results in a more systematic
manner. With this objective in mind, we outline the necessary
advancements in hardware,
interpretation techniques, and
decision-making algorithms needed to realize automated and
closed-loop synthesis of novel inorganic materials.

5.1 Synthesis

As discussed in Section 2.1, the full automation of solution-based
syntheses can be achieved by using electronic and programmable
syringe pumps to transfer samples between modules that per-
form unit operations such as mixing, heating, and filtration.11,13
Although most existing applications deal with organic molecules,
recent work has shown that similar techniques can be used to
automate the synthesis of inorganic materials through sol–gel or
precipitation methods,18–20 which are useful to produce nano-
particles (commonly metal oxides) so long as there exist appro-
priate precursors with high solubilities in available solvents such
as water. To expand the scope of compounds that can be made by
solution-based techniques, we suggest integrating hydrothermal
synthesis into future workflows. This approach permits a wider
range of starting materials since high temperature and pressure
lead to increased solubilities. Furthermore, it can be used to
access compounds that are only metastable under ambient
conditions.154 The automation of hydrothermal synthesis may
soon be implemented at the experimental stage of materials
development as robotic loading and unloading of the autoclave
reaction vessel has recently been demonstrated in a commercial
system.155

For thin film synthesis, there are many reported workflows
that can generate combinatorial
libraries of samples with
varied compositions in an automated and HT manner.14,91
However, these platforms are distinguished from closed-loop
experimentation by a lack of automation for data interpretation,
decision making, and replacement of samples between experi-
mental iterations. These shortcomings prevent an eﬃcient probing
of experimental variables beyond composition, including synthesis
conditions such as temperature or pressure. Fortunately, the

examples reviewed in Section 2.2 demonstrate that automated
thin film deposition can be integrated with robotics and
optimization algorithms to develop closed-loop platforms. So
far, autonomous thin film synthesis has been achieved with
CVD,21,22 spin coating,12 magnetron sputtering,39 and reactive
sputtering with lg-LSA.40 These methods alone can be used to
produce many types of materials, and increased adoption of
other techniques such as molecular beam epitaxy and pulsed
laser deposition support a promising future for the closed-loop
automation of thin film synthesis.

In contrast to syntheses based on solutions or thin films, the
automation of solid-state synthesis remains limited. As described in
Section 2.3, several unit operations such as mixing, densification,
and firing have been automated or parallelized; however, integrating
these components without manual intervention between operations
is challenging. To overcome these diﬃculties, we consider the
advantages of solution-based and thin film syntheses with respect
to ease of automation. On one hand, transferring of samples
dissolved in a solution can be accomplished with electronic syringe
pumps, whereas the handling of solid powders is more diﬃcult. To
solve this problem, a semi-solution-based approach may be taken
whereby solid powders are handled as a slurry to allow transfer
using syringe pumps. On the other hand, thin films avoid the
diﬃculties associated with sample transfer by performing all
experiments (including synthesis and characterization) on a
single substrate that is more easily handled by robotic systems.
Extending this concept to solid-state synthesis, automated plat-
forms may rely on a multipurpose container that has robust
mechanical, chemical, and heat resistance such that it can be
used throughout the entire synthesis procedure without any
degradation or contamination of the samples. This approach
would therefore remove the need to extract and transfer the
materials between unit operations.

5.2 Interpretation

After performing a synthesis trial, phase identification is needed to
decide whether a planned reaction was successful, or to under-
stand why it may have failed. Because of the wide availability of
reference patterns for crystalline inorganic materials, XRD is often

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

the tool of choice for this purpose.61,97 Although automated
loading of samples and analysis with XRD can be carried out with
commercially available systems, interpreting the resulting spectra
is a more diﬃcult task. Of the methods discussed in Section 3.2,
we suggest that those based on machine learning are most
promising given three unique advantages. First, they provide a
complete end-to-end treatment of raw spectra without requiring
sensitive pre-processing steps such as peak extraction or baseline
correction.74 Second, machine learning models can account for
possible non-idealities (e.g., from experimental artifacts) by
performing data augmentation across spectra in the training
set.54 Last, ensemble models can be employed to generate
probabilistic distributions associated with likely phases, there-
fore providing an estimation of uncertainty associated with the
final classification.75

Of the machine learning models previously developed, CNNs
are particularly adept at handling XRD spectra because they use
convolution to decompose complex patterns into feature maps
representing distinct properties such as peak positions or inten-
sities, which can then be related to corresponding phases through
a neural network. Indeed, Oviedo et al. have reported improved
performance of CNNs relative to several alternative machine
learning algorithms and full-profile techniques when applied to
experimentally measured single-phase patterns obtained from a
combinatorial library of thin film samples.54 We note that a key
component of their algorithm was the incorporation of peak shifts
in the training spectra, which reflect the epitaxial strain that is
common in thin film samples – this augmentation is therefore
denoted as ‘‘physics-informed’’. A similar approach was employed
in the work of Maffettone et al., where changes in peak intensities
were related to possible texture (preferred crystallographic orienta-
tion) in the samples.75 Future work may expand upon these
concepts to further improve the model’s accuracy and generality
by incorporating data augmentation designed to account for all
artifacts that commonly arise during sample preparation and
synthesis. If proven successful by rigorous testing on experi-
mentally measured patterns, CNNs will prove vital to facilitate
phase identification in closed-loop experimental platforms
enabling autonomous inorganic synthesis.

5.3 Decision making

Once the compounds produced by a reaction are known, a decision
must be made regarding the next batch of experiments. Automated
decision making for targeted syntheses requires either many experi-
ments or advanced knowledge of the underlying objective function.
For solid-state synthesis, the use of high temperatures and long
heating times typically precludes a large number of experiments
performed in parallel. Furthermore, unlike reactions between
organic molecules, which can often be decomposed into a series
of unit operations involving functional group additions/removals,156
solid-state reaction mechanisms are less well understood. Due to
the bulk nature of materials, reaction sequences based on nuclea-
tion and growth are not easily predicted, and therefore the objective
function that governs inorganic synthesis is unknown. When a
measurable amount of the desired product is consistently
formed throughout a set of experiments, the objective function

can be simplified by performing black-box optimization to
maximize the target yield.31,116,124 However, when dealing with
more complex syntheses involving novel compounds, an
informed optimization approach is better suited to overcome
the low success rates of many trial reactions. As described in
Section 4.2.2, the complexity of objective functions governing
organic syntheses can often be reduced by designing reaction
networks, which map input parameters (such as precursors)
onto possible experiments outcomes (intermediates and final
products).150,153 With hypothetico-deductive modeling, promising
pathways in the network can be hypothesized and verified by
performing stepwise reactions and measuring the yields of
expected products. While current applications of reaction networks
remain mostly limited to small molecules, similar concepts may be
extended to inorganic materials synthesis if an improved under-
standing of solid-state reactions is realized.

To build a reliable reaction network, it is necessary to predict
which phases are likely to form from a set of specified pre-
cursors and synthesis conditions. This task is challenging for
solid-state reactions because many factors can prevent a system
from reaching thermodynamic equilibrium, and therefore inor-
ganic materials synthesis is often treated as a black box that
must be probed with trial-and-error experiments. The combi-
nation of in situ characterization and computational modeling
of thermodynamics is however making progress in rationalizing
synthesis pathways. For example, Bianchini et al. monitored the
synthesis of sodium metal oxides to highlight the importance of
intermediate phase selection and its eﬀects on the reaction
products.23 The authors argued for two types of reaction path-
way controls. When the driving force is large, as in the initial
reaction between precursors, the pathway is dictated by the
compositionally unconstrained reaction energy – i.e., the first
phase that forms during high-temperature synthesis is the one
which locally maximizes the free energy reduction at the pre-
cursor interfaces, regardless of the overall composition of the
mixture. This phase then evolves to the equilibrium ground state for
the overall composition of the mixture through transformations that
are either kinetically or thermodynamically controlled. When the
remaining driving force is low, metastable intermediates were
observed when facile transformation mechanisms from previous
phases along the pathway allowed them to lower the free energy
of the system faster than through the formation of the equili-
brium phases.

Metastable intermediates that accompany reactions with low
thermodynamic driving forces are often templated by structural
similarities with preceding phases. For example, in the synthesis of
KBiS2 from K2S and Bi2S3, McClain et al. showed that K3BiS3
initially formed as an intermediate because it shares a similar
motif to the structures of the starting materials.157 The authors
propose that the distorted octahedral KS6 and BiS6 coordination
environments in K3BiS3 serve as transition states between the
distorted octahedral (tetrahedral) complexes of Bi2S3 (K2S) and the
ideal octahedral environments in KBiS2. In addition to structure,
the selectivity of intermediate phase formation can also be
controlled by environmental conditions such as temperature
and partial pressures of gaseous species. This was demonstrated

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

by Todd et al. for the synthesis of YMnO3 from a combination of
Mn2O3, YCl3, and Li2CO3 as precursors.158 They found that a
high oxygen fugacity favors the formation of LiMnO2 and YOCl
as intermediates over Y2O3 and Mn2O3. Moreover, because the
former pair of compounds are layered, their high diﬀusion rates
enable rapid formation of the target (YMnO3), further clarifying
the role of kinetics in dictating reaction pathways between solid
precursors. Alternatively, when compounds arise from molten
phases rather than from solids, the first intermediate to form
is usually the phase with the lowest barrier to nucleation.
For example, Shoemaker et al. found that a single metastable
phase, K5Sb2S8, initially nucleated from a melt formed by Sn
and K2S5.159 This novel compound was transient in the reaction
sequence,
later decomposing to a mixture of K2Sn2S5 and
K4Sn2S8, which is the thermodynamic ground state.

The utility of the concepts described above are highlighted
in the work of Miura et al., where the influence of precursors on
resulting reaction pathways taken throughout the synthesis of
YBa2Cu3O6+x (YBCO) was studied.160 In agreement with the
work of Bianchini et al.,23 it was observed that initial reactions
occurred at interfaces with the largest thermodynamic driving
forces. The first intermediates were shown to drive the reaction
along a pathway that led to rapid synthesis through a low-
temperature liquid phase, which would have been inaccessible
if other intermediates had formed. These findings suggest that
precursors can be carefully selected to control reaction pathways
and enable the formation of targeted products. However, as
opposed to organic molecules, where reactions can be rationa-
lized by considering molecular-level interactions (i.e., breaking
and forming individual bonds), predicting kinetic contributions
to solid-state reactions is challenging because they involve con-
certed displacements and interactions among many species over
extended distances, making first-principles approaches diﬃcult.
To simplify the analysis of solid-state reactions, McDermott
et al. developed an algorithm that predicts all possible path-
ways between a set of precursors and final product(s), with each
pathway decomposed into a sequence of pairwise reactions.161
The thermodynamic driving forces associated with each path-
way are used to calculate a cost function, from which suspected
reaction sequences are ranked from most to least favorable.
As an example, the authors demonstrated that their algorithm
was able to predict the reaction pathway taken during the
synthesis of YMnO3. However, to extend this approach to more
general syntheses of arbitrary compounds, it is necessary to
incorporate factors beyond thermodynamic driving forces. As
described in the previous three paragraphs, metastable inter-
mediates that form more rapidly than the equilibrium ground
state often dominate when their driving forces for formation
are comparable. Hence, although diﬃcult to calculate directly,
future algorithms may benefit from an estimation of transfor-
mation rates based on structural descriptions, since structures
can serve as templates for nucleated phases. An initial approach
was recently published by deriving a structural descriptor from
classical nucleation theory to help indicate which reactions are
plausible.162 Further advances in the prediction of reaction
pathways should also address the potential for melting and

preferential nucleation from molten phases that form during
high-temperature syntheses.

It is clear that more work is needed to improve our under-
standing of the underlying objective function that governs solid-
state synthesis, and an increased adoption of in situ characterization
would be helpful for this purpose. The information gained from
in situ measurements is vital to validate any predictions made by
the aforementioned theories and could be used to modify or
extend their rules accordingly.24 Additionally, any knowledge
regarding intermediates that form during a synthesis trial
provide direct insight into why a synthesis attempt succeeded or
failed.158,159,163,164 Therefore, the identification of intermediate
phases is particularly useful in the optimization of inorganic
materials synthesis because it allows us to understand why the
target phase was or was not formed. This knowledge can also be
reincorporated into the experimental procedure to actively
guide materials synthesis. For example, Rakita et al. used
in situ synchrotron X-ray absorption spectroscopy to monitor
the oxidation of copper samples placed in a controlled reaction
environment.163 By continuously observing changes in the
average Cu oxidation state with respect to the partial pressure
of the oxidant, more or less gas flow was fed into the reaction
vessel to target an average oxidation state of Cu1+. Although this
state is diﬃcult to obtain manually as it requires a precise
balance of Cu0 and Cu2+ species, the autonomous workflow
successfully formed samples with an average oxidation state
near Cu1+ through active control of the reaction environment.
Unfortunately, the availability of in situ characterization
techniques with high resolution and a fast scan rate remains
limited, especially within the context of automated platforms.
While methods such as thermogravimetric analysis or diﬀerential
scanning calorimetry can sometimes be used to indicate when a
reaction or phase change has occurred, they do not provide a
means of identifying which intermediate phases formed. For this
purpose, spectroscopic or diﬀraction-based techniques are necessary.
However, obtaining reliable in situ data typically requires that high-
intensity radiation or neutrons be used, which can be obtained only
with high-energy sources (e.g., a synchrotron or nuclear reactor).
Therefore, in the absence of improved in-lab diﬀractometers, we
suggest that an automated synthesis platform can potentially
replicate the information gained from in situ characterization by
carrying out reactions across a range of temperatures, quenching
after predetermined annealing times, and performing ex situ
measurements on the resulting samples. This approach would
provide discrete snapshots of the reaction pathway, and the
throughput of automated platforms may enable suﬃcient mea-
surements to mimic traditional in situ methods.

In the place of information obtained using new experiments,
previously reported data can be tabulated and analyzed to reveal
statistical trends, develop models, and validate predictions. In
recent years, large-scale databases and application programming
interfaces (APIs) that provide experimental and/or calculated
materials data sets have become increasingly popular. For example,
the ICSD contains hundreds of thousands of experimentally deter-
mined crystalline structures,97 and the Materials Project con-
tains a variety of DFT-calculated properties across a comparable

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

number of materials.2 For information regarding experimental
synthesis routes, however, there exists only a limited amount of
well-structured data with suﬃciently high quality to be coupled
with autonomous systems. To overcome this shortcoming,
NLP eﬀorts have been developed and applied to collect and
curate synthesis data in relevant literature, such as synthesis
conditions and resulting phases.25,101,102,165 Though, because of
inherent biases in published results, more work is needed to
address the lack of negative examples (i.e., failed synthesis
attempts), which limits the ability to learn which factors con-
tribute to an experiment’s success.103,166 Interestingly,
the
potential of coupling NLP with autonomous synthesis platforms
has been demonstrated by the work of Mehr et al., where a fully
integrated system was built to carry out the synthesis of organic
compounds with experimental parameters parsed directly from
the literature.167 With the increasing development of text-mined
inorganic synthesis databases,165,168 we suggest that similar
methods may be applied to power autonomous inorganic synthesis
platforms.

5.4 Summary

With the growing development and adoption of self-driving
laboratories in materials science, time can be freed up for the
researcher to work on high-level tasks involving conceptual
formulation and interpretation, while leaving low-level, manual
eﬀorts to be carried out by the robotic system.169,170 These high-
level tasks may include choosing the candidates to be synthe-
sized based on prior knowledge such as structure–property
relationships, designing the experiment such that all para-
meters and bounds are chosen to ensure maximal efficiency,
and analyzing the corresponding results to ascertain broader
scientific implications (e.g., a clarification of factors influen-
cing synthesis) which inform further experimentation. Indeed,
the sparsity of existing theories for solid-state reactivity emphasizes
the ample work left for the human to develop these concepts and
enable self-driving laboratories to meet their full potential in
inorganic materials science. The lack of these established theories
should not however precede the development of autonomous
systems as expanding available datasets and automating time-
consuming tasks will drive the development of more predictive
theories for the directed synthesis of novel inorganic materials.

Conflicts of interest

There are no conflicts to declare.

Acknowledgements

Primary funding for this work was obtained from the U.S.
Department of Energy, Oﬃce of Science, Basic Energy Sciences,
Materials Sciences and Engineering Division under Contract
No. DE-AC02-05-CH11231 within the D2S2 program KCD2S2
and the GENESIS EFRC program DE-SC0019212. The review of
methods used for analyzing XRD data was supported by the
Joint Center for Energy Storage Research (JCESR), an Energy

Innovation Hub funded by the U.S. Department of Energy,
Oﬃce of Science, Basic Energy Sciences under Contract No.
DE-AC02-05-CH11231. We also acknowledge support from the
National Science Foundation Graduate Research Fellowship
under Grant No. 1752814.

References

1 D. P. Tabor, et al., Accelerating the discovery of materials
for clean energy in the era of smart automation, Nat. Rev.
Mater., 2018, 3, 5–20.

2 A. Jain, et al., The materials project: A materials genome
approach to accelerating materials innovation, APL Mater.,
2013, 1, 011002.

3 J. E. Saal, S. Kirklin, M. Aykol, B. Meredig and C. Wolverton,
Materials design and discovery with high-throughput density
functional theory: The open quantum materials database
(OQMD), JOM, 2013, 65, 1501–1509.

4 M. Shevlin, Practical high-throughput experimentation for

chemists, ACS Med. Chem. Lett., 2017, 8, 601–607.

5 C. A. Nicolaou, I. A. Watson, H. Hu and J. Wang, The
proximal Lilly collection: Mapping, exploring and exploiting
feasible chemical space, J. Chem. Inf. Model., 2016, 56,
1253–1266.

6 A. Weber, E. v. Roedern and H. U. Stilz, SynCar: An approach
to automated synthesis, J. Comb. Chem., 2005, 7, 178–184.
7 P. Szyman´ski, M. Markowicz and E. Mikiciuk-Olasik,
Adaptation of high-throughput screening in drug discovery –
toxicological screening tests, Int. J. Mol. Sci., 2012, 13,
427–452.

8 F. Ha¨se, L. M. Roch, C. Kreisbeck and A. Aspuru-Guzik,
Phoenics: A Bayesian optimizer for chemistry, ACS Cent.
Sci., 2018, 4, 1134–1145.

9 L. M. Roch, et al., ChemOS: Orchestrating autonomous

experimentation, Sci. Robotics, 2018, 3, eaat5559.

10 N. S. Eyke, B. A. Koscher and K. F. Jensen, Toward machine
experimentation,

high-throughput

learning-enhanced
Trends Chem., 2021, 3, 120–132.

11 S. Steiner, et al., Organic synthesis in a modular robotic
system driven by a chemical programming language,
Science, 2019, 363, eaav2211.

12 B. P. MacLeod, et al., Self-driving laboratory for accelerated
discovery of thin-film materials, Sci. Adv., 2020, 6, eaaz8867.
13 B. Burger, et al., A mobile robotic chemist, Nature, 2020,

583, 237–241.

14 A. Ludwig, Discovery of new materials using combinatorial
synthesis and high-throughput characterization of thin-
film materials libraries combined with computational
methods, npj Comput. Mater., 2019, 5, 70.

15 F. Ren, et al., Accelerated discovery of metallic glasses through
iteration of machine learning and high-throughput experi-
ments, Sci. Adv., 2019, 4, eaaq1566.

16 S. Sun, et al., Accelerated development of perovskite-inspired
materials via high-throughput synthesis and machine-
learning diagnosis, Joule, 2019, 3, 1437–1451.

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

17 B. Li, et al., Hydrogen storage materials discovery via high
throughput ball milling and gas sorption, ACS Comb. Sci.,
2012, 14, 352–358, DOI: 10.1021/co2001789.

18 G. H. Carey and J. R. Dahn, Combinatorial synthesis of
mixed transition metal oxides for lithium-ion batteries,
ACS Comb. Sci., 2011, 13, 186–189.

19 T. Adhikari, et al., Development of high-throughput
methods for sodium-ion battery cathodes, ACS Comb.
Sci., 2020, 22, 311–318, DOI: 10.1021/acscombsci.9b00181.
20 S. Krishnadasan, R. J. C. Brown, A. J. deMello and J. C.
deMello, Intelligent routes to the controlled synthesis of
nanoparticles, Lab Chip, 2007, 7, 1434–1441.

21 P. Nikolaev, et al., Autonomy in materials research: a case
study in carbon nanotube growth, npj Comput. Mater.,
2016, 2, 16031.

22 J. Chang, et al., Eﬃcient closed-loop maximization of
carbon nanotube growth rate using Bayesian optimization,
Sci. Rep., 2020, 10, 9040.

23 M. Bianchini, et al., The interplay between thermo-
dynamics and kinetics in the solid-state synthesis of
layered oxides, Nat. Mater., 2020, 19, 1088–1095.

24 H. Kohlmann, Looking into the black box of solid-state

synthesis, Eur. J. Inorg. Chem., 2019, 4174–4180.

25 H. Huo, et al., Semi-supervised machine-learning classifica-
tion of materials synthesis procedures, npj Comput. Mater.,
2019, 5, 62.

Proc. Natl. Acad. Sci. U. S. A., 2017, 114, 3040–3043, DOI:
10.1073/pnas.1619940114.

36 S. Guerin, B. Hayden, D. W. Hewak and C. Vian, Synthesis
and screening of phase change chalcogenide thin film
materials for data storage, ACS Comb. Sci., 2017, 19, 478–491.
37 T. Gebhardt, D. Music, T. Takahashi and J. M. Schneider,
Combinatorial thin film materials science: from alloy
discovery and optimization to alloy design, Thin Solid
Films, 2012, 520, 5491–5499.

38 P. Nikolaev, D. Hooper, N. Perea-Lo´pez, M. Terrones and
B. Maruyama, Discovery of wall-selective carbon nanotube
growth conditions via automated experimentation, ACS Nano,
2014, 8, 10214–10222.

39 R. Shimizu, S. Kobayashi, Y. Watanabe, Y. Ando and
T. Hitosugi, Autonomous materials synthesis by machine
learning and robotics, APL Mater., 2020, 8, 111110.

40 S. Ament et al., Autonomous synthesis of metastable

materials. arXiv:2101.07385v1, 2021.

41 R. T. Bell, et al., Lateral temperature-gradient method for
high-throughput characterization of material processing
by millisecond laser annealing, ACS Comb. Sci., 2016, 18,
548–558.

42 B. R. Ortiz, J. M. Adamczyk, K. Gordiz, T. Braden and
E. S. Toberer, Towards the high-throughput synthesis of
bulk materials: thermoelectric PbTe–PbSe–SnTe–SnSe alloys,
Mol. Syst. Des. Eng., 2019, 4, 407–420.

26 J. R. Mohrig, D. Alberg, G. Hofmeister, P. F. Schatz and C. N.
Hammond. Laboratory Techniques in Organic Chemistry,
W.H. Freeman and Company, 2014.

27 G. Schneider, Automating drug discovery, Nat. Rev. Drug

43 T. A. Stegk, R.

Janssen and G. A. Schneider, High-
throughput synthesis and characterization of bulk cera-
mics from dry powders, J. Comb. Chem., 2008, 10, 274–279,
DOI: 10.1021/cc700145q.

Discovery, 2018, 17, 97–113.

28 B. Gutmann, D. Cantillo and C. O. Kappe, Continuous-flow
technology—A tool for the safe manufacturing of active
pharmaceutical ingredients, Angew. Chem., Int. Ed., 2015,
54, 6688–6728.

29 A. Adamo, et al., On-demand continuous-flow production
of pharmaceuticals in a compact, reconfigurable system,
Science, 2016, 352, 61–67.

44 S. Shuang, et al., High-throughput automatic batching
equipment for solid state ceramic powders, Rev. Sci. Instrum.,
2019, 90, 083904.

45 XPR Automatic Balance from Mettler Toledo, https://www.mt.
com/my/en/home/products/Laboratory_Weighing_Solutions/
Analytical/Excellence/XPR_Automatic_Balance.

46 Flex SWILE from Chemspeed Technologies, https://www.

chemspeed.com/flex-swile-nmr/.

30 C. W. Coley, et al., A robotic platform for flow synthesis of
organic compounds informed by AI planning, Science,
2019, 365, eaax1566, DOI: 10.1126/science.aax1566.

47 D8 Endeavor from Bruker, https://www.bruker.com/pt/
products-and-solutions/diﬀractometers-and-scattering-systems/
x-ray-diﬀractometers/d8-endeavor.html.

31 A.-C. Be´dard, et al., Reconfigurable system for automated
optimization of diverse chemical reactions, Science, 2018,
361, 1220–1225.

32 Z. Li, et al., Robot-accelerated perovskite investigation and
discovery, Chem. Mater., 2020, 32, 5650–5663, DOI: 10.1021/
acs.chemmater.0c01153.

33 J. Li, et al., Autonomous discovery of optically active chiral
inorganic perovskite nanocrystals through an intelligent
cloud lab, Nat. Commun., 2020, 11, 2046.

34 Y. J. Li, A. Savan, A. Kostka, H. S. Stein and A. Ludwig,
Accelerated atomic-scale exploration of phase evolution in
compositionally complex materials, Mater. Horiz., 2018, 5,
86–92, DOI: 10.1039/C7MH00486A.

35 Q. Yan, et al., Solar fuels photoanode materials discovery
by integrating high-throughput theory and experiment,

48 S. Langner, et al., Beyond ternary OPV: High-throughput
experimentation and self-driving laboratories optimize
multicomponent systems, Adv. Mater., 2020, 32, 1907801.
49 R. Gautum, S. Venga, F. Ariese and S. Umpathy, Review of
multidimensional data processing approaches for Raman
and infrared spectroscopy, EPJ Techn. Instrum., 2015, 2, 8.
50 M. H. Modarres, et al., Neural network for nanoscience
scanning electron microscope image recognition, Sci. Rep.,
2017, 7, 13282.

51 D. Xue, et al., Accelerated search for materials with
targeted properties by adaptive design, Nat. Commun.,
2016, 7, 11241.

52 J. Liu, et al., Deep convolutional neural networks for
Raman spectrum recognition: A unified solution, Analyst,
2017, 142, 4067–4074.

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

53 H. S. Stein, S. Jiao and A. Ludwig, Expediting combinatorial
data set analysis by combining human and algorithmic
analysis, ACS Comb. Sci., 2017, 19, 1–8.

54 F. Oviedo, et al., Fast and interpretable classification of
small X-ray diﬀraction datasets using data augmentation
and deep neural networks, npj Comput. Mater., 2019,
5, 60.

55 S. Thienhaus, D. Naujoks, J. Pfetzing-Micklich, D. Ko¨nig
and A. Ludwig, Rapid identification of areas of interest
in thin film materials libraries by combining electrical,
optical, X-ray diﬀraction, and mechanical high-throughput
measurements: A case study for the system Ni–Al, ACS
Comb. Sci., 2014, 16, 686–694.

56 L. Yu, R. S. Kokenyesi, D. A. Keszler and A. Zunger, Inverse
design of high absorption thin-film photovoltaic materials,
Adv. Energy Mater., 2013, 3, 43–48.

57 R. Zarnetta, S. Kneip, C. Somsen and A. Ludwig, High-
throughput characterization of mechanical properties of
Ti–Ni–Cu shape memory thin films at elevated temperature,
Mater. Sci. Eng. A, 2011, 528, 6552–6557.

58 S. Salomon, et al., Combinatorial synthesis andhigh-
throughput characterization ofthe thin film materials systemCo–
Mn–Ge: Composition, structure,and magnetic properties,
Phys. Status Solidi A, 2015, 212, 1969–1974.

59 Y. Lyu, Y. Liu, T. Cheng and B. Guo, High-throughput
characterization methods for lithium batteries, J Materio-
mics, 2017, 3, 221–229.

60 S. M. Moosavi, et al., Capturing chemical intuition in
synthesis of metal-organic frameworks, Nat. Commun.,
2019, 10, 539.

61 S. Gates-Rector and T. N. Blanton, The powder diﬀraction
file: A quality materials characterization database, Powder
Diﬀr., 2019, 34, 352–360.

62 A. Altomare, et al., Advances in powder diﬀraction pattern
indexing: N-TREOR09, J. Appl. Crystallogr., 2009, 42, 768–775.
63 P. M. d. Wolﬀ, A simplified criterion for the reliability of a
powder pattern indexing, J. Appl. Crystallogr., 1968, 1,
108–113.

64 A. Esmaeili, T. Kamiyama and R. Oishi-Tomiyasu, New
functions and graphical user interface attached to powder
indexing software CONOGRAPH, J. Appl. Crystallogr., 2017,
50, 651–659.

65 R. Oishi-Tomiyasu, Reversed de Wolﬀ figure of merit and its
application to powder indexing solutions, J. Appl. Crystallogr.,
2013, 46, 1277–1282.

66 J.-M. L. Meins, L. M. D. Cranswick and A. L. Bail, Results
and conclusions of the internet based ‘‘Search/match
round robin 2002’’, Powder Diﬀr., 2003, 18, 106–113.
67 C. J. Gilmore, G. Barr and J. Paisley, High-throughput
powder diﬀraction. A new approach to qualitative and
quantitative powder diﬀraction pattern analysis using full
pattern profiles, J. Appl. Crystallogr., 2004, 37, 231–242.
68 E. Herna´ndez-Rivera, S. P. Coleman and M. A. Tschopp,
Using similarity metrics to quantify diﬀerences in high-
throughput data sets: Application to X-ray diﬀraction
patterns, ACS Comb. Sci., 2017, 19, 25–36.

69 L. A. Baumes, M. Moliner and A. Corma, Design of a full-
profile-matching solution for high-throughput analysis
of multiphase samples through powder X-ray diﬀraction,
Chem. – Eur. J., 2009, 15, 4258–4260.

70 V. Stanev, et al., Unsupervised phase mapping of X-ray
diﬀraction data by nonnegative matrix factorization
integrated with custom clustering, npj Comput. Mater.,
2018, 4, 43.

71 Y. Iwasaki, A. G. Kusne and I. Takeuchi, Comparison of
dissimilarity measures for cluster analysis of X-ray diﬀraction
data from combinatorial libraries, npj Comput. Mater., 2017,
4, 4.

72 W. B. Park, et al., Classification of crystal structure using a
convolutional neural network, IUCrJ, 2017, 4, 486–494.
73 P. M. Vecsei, K. Choo, J. Chang and T. Neupert, Neural
network based classification of crystal symmetries from
X-ray diﬀraction patterns, Phys. Rev. B, 2019, 99, 245120.
74 H. Wang, et al., Rapid identification of X-ray diﬀraction
patterns based on very limited data by interpretable con-
volutional neural networks, J. Chem. Inf. Model., 2020, 60,
2004–2011.

75 P. M. Maﬀettone, L. Banko, P. Cui, Y. Lysogorskiy, M. A.
Little, D. Olds, A. Ludwig and A. I. Cooper, Crystallography
companion agent for high-throughput materials discovery,
Nat. Comput. Sci., 2021, 1, 290–297.

76 J.-W. Lee, W. B. Park, J. H. Lee, S. P. Singh and K.-S. Sohn,
A deep-learning technique for phase identification in multi-
phase inorganic compounds using synthetic XRD powder
patterns, Nat. Commun., 2020, 11, 86.

77 S. S. Khan and M. G. Madden, New similarity metrics for
Raman spectroscopy, Chemom. Intell. Lab. Syst., 2012, 114,
99–108.

78 C. Li, et al., Rapid Bayesian optimisation for synthesis of
short polymer fiber materials, Sci. Rep., 2017, 7, 5683.
79 H. Wahab, et al., Machine-learning-assisted fabrication:
Bayesian optimization of laser-induced graphene patterning
using in situ Raman analysis, Carbon, 2020, 167, 609–619.
80 M. A. Al-Kheder, C. Pezeshki, J. L. McHale and F. J. Knorr,
Quality classification via Raman identification and SEM
analysis of carbon nanotube bundles using artificial neural
networks, Nanotechnology, 2007, 18, 335703.

81 M. Ziatdinov, et al., Deep learning of atomically resolved
scanning transmission electron microscopy images: Chemical
identification and tracking local transformations, ACS Nano,
2017, 11, 12742–12752.

82 W. Li, K. G. Field and D. Morgan, Automated defect analysis in
electron microscopic images, npj Comput. Mater., 2018, 4, 36.
83 A. Maksov, et al., Deep learning analysis of defect and
phase evolution during electron beam-induced trans-
formations in WS2, npj Comput. Mater., 2018, 5, 12.

84 S. Madireddy, et al., Phase segmentation in atom-probe
tomography using deep learning-based edge detection, Sci.
Rep., 2019, 9, 20140.

85 J. H. Montoya, et al., Autonomous intelligent agents for
accelerated materials discovery, Chem. Sci., 2020, 11,
8517–8532.

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

86 Z. Zhou, X. Li and R. N. Zare, Optimizing chemical reactions
with deep reinforcement learning, ACS Cent. Sci., 2017, 3,
1337–1344.

104 M. M. Flores-Leonar, et al., Materials acceleration platforms:
On the way to autonomous experimentation, Curr. Opin.
Green Sustainable Chem., 2020, 25, 100370.

87 L. Porwol, et al., An autonomous chemical robot discovers
the rules of inorganic coordination chemistry without prior
knowledge, Angew. Chem., Int. Ed., 2020, 59, 11256–11261.
88 D. A. Cohn, Z. Ghahramani and M. I. Jordan, Active learning
with statistical methods, J. Artif. Intell., 1996, 4, 129–145.
89 E. J. Braham, R. D. Davidson, M. Al-Hashimi, R. Arro´yave
and S. Banerjee, Navigating the design space of inorganic
materials synthesis using statistical methods and machine
learning, Dalton Trans., 2020, 49, 11480.

90 W. F. Maier, K. Sto¨we and S. Sieg, Combinatorial and high-
throughput materials science, Angew. Chem., Int. Ed., 2007,
46, 6016–6067.

91 H. Koinuma and I. Takeuchi, Combinatorial solid-state
chemistry of inorganic materials, Nat. Mater., 2004, 3,
429–438.

92 M.-X. Li, et al., High-temperature bulk metallic glasses
developed by combinatorial methods, Nature, 2019, 569,
99–103.

93 S. A. Kube, et al., Combinatorial study of thermal stability
in ternary nanocrystalline alloys, Acta Mater., 2020, 188,
40–48.

94 R. Zarnetta, et al., Identification of quaternary shape memory
alloys with near-zero thermal hysteresis and unprecedented
functional stability, Adv. Funct. Mater., 2010, 20, 1917–1923.

95 A. Marshal, et al., Combinatorial evaluation of phase
formation and magnetic properties of FeMnCoCrAl high
entropy alloy thin flm library, Sci. Rep., 2019, 9, 7864.
96 S. Thrun, Handbook of Brain Science and Neural Networks,

1995, pp. 381–384.

97 A. Belsky, M. Hellenbrandt, V. L. Karen and P. Luksch, New
developments in the inorganic crystal structure database
(ICSD): Accessibility in support of materials research and
design, Acta Crystallogr., Sect. B: Struct. Sci., 2002, 58,
364–369.

98 J. Schmidt, M. R. G. Marques, S. Botti and M. A. L.
Marques, Recent advances and applications of machine
learning in solid-state materials science, npj Comput.
Mater., 2019, 5, 83.

99 D. Morgan and R. Jacobs, Opportunities and challenges for
machine learning in materials science, Annu. Rev. Mater.
Res., 2020, 50, 71–103.

100 L. Himanen, A. Geurts, A. S. Foster and P. Rinke,
Data-driven materials science: Status, challenges, and
perspectives, Adv. Sci., 2019, 6, 1900808.

101 E. Kim, K. Huang, S. Jegelka and E. Olivetti, Virtual screening
of inorganic materials synthesis parameters with deep
learning, npj Comput. Mater., 2017, 3, 53.

102 E. Kim, et al., Materials synthesis insights from scientific
literature via text extraction and machine learning, Chem.
Mater., 2017, 29, 9436–9444.

105 T. Lookman, P. V. Balachandran, D. Xue and R. Yuan,
Active learning in materials science with emphasis on
adaptive sampling using uncertainties for targeted design,
npj Comput. Mater., 2019, 5, 21.

106 A. G. Kusne, et al., On-the-fly closed-loop materials dis-
covery via Bayesian active learning, Nat. Commun., 2020,
11, 5966.

107 J. Li, et al., AI applications through the whole life cycle of

material discovery, Matter, 2020, 3, 393–432.

108 C. Audet and W. Hare, Derivative-free and Blackbox Optimization,

Springer, Cham, 2017.

109 A. Costa and G. Nannicini, RBFOpt: An open-source library
for black-box optimization with costly function evaluations,
Math. Program. Comput., 2018, 10, 597–629.

110 D. R. Jones, M. Schonlau and W. J. Welch, Eﬃcient global
optimization of expensive black-box functions, J. Glob.
Optim., 1998, 13, 455–492.

111 K. S. Tang, K. F. Man, S. Kwong and Q. He, Genetic
algorithms and their applications, IEEE Signal Proc. Mag.,
1996, 13, 22–37.

112 D. E. Goldberg, Genetic Algorithms in Search, Optimization

and Machine Learning, Addison Wesley, 1989.

113 M. Holena, in High-Throughput Screening in Chemical Catalysis:
Technologies, Strategies and Applications, ed. A. Hagemeyer,
P. Strasser and A. F. Volpe Jr., Wiley-VCH, 2006, pp. 153–174.
114 U. Rodemerck, M. Baerns, M. Holena and D. Wolf, Appli-
cation of a genetic algorithm and a neural network for the
discovery and optimization of new solid catalytic materials,
Appl. Surf. Sci., 2004, 223, 168–174.

115 Z. Ma and F. Zaera, Encyclopedia of Inorganic Chemistry,

John Wiley, 2006.

116 D. Wolf, O. V. Buyevskaya and M. Baerns, An evolutionary
approach in the combinatorial selection and optimization
of catalytic materials, Appl. Catal., 2000, 200, 63–77.
117 K. W. Kuntz, M. L. Snapper and A. H. Hoveyda, Combinatorial
catalyst discovery, Curr. Opin. Chem. Biol., 1999, 3, 313–319.
118 A. Corma, et al., Optimisation of olefin epoxidation catalysts
with the application of high-throughput and genetic algo-
rithms assisted by artificial neural networks (softcomputing
techniques), J. Catal., 2005, 229, 513–524.

119 K. McCullough, T. Williams, K. Mingle, P. Jamshidi and
J. Lauterbach, High-throughput experimentation meets
artificial intelligence: A new pathway to catalyst discovery,
Phys. Chem. Chem. Phys., 2020, 22, 11174–11196.

120 J. T. Alander, On optimal population size of genetic
algorithms, in Proceedings of CompEuro 1992 Computer
Systems and Software Engineering, 1992, vol. 1, pp. 65–70.
121 W. Huyer and A. Neumaier, SNOBFIT—Stable noisy
optimization by branch and fit, ACM Trans. Math. Softw.,
2008, 35, 1–25.

103 P. Raccuglia, et al., Machine-learning-assisted materials
discovery using failed experiments, Nature, 2016, 533,
73–76.

122 C. Mateos, M. J. Nieves-Remacha and J. A. Rinco´n, Auto-
mated platforms for self-optimization in flow, React. Chem.
Eng., 2019, 4, 1536.

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineMaterials Horizons

Review

123 A. D. Clayton, et al., Algorithms for the self-optimisation of
chemical reactions, React. Chem. Eng., 2019, 4, 1545.
124 N. Cherkasov, Y. Bai, A. J. Expo´sito and E. V. Rebrov,
OpenFlowChem – A platform for quick, robust and flexible
automation and self-optimisation of flow chemistry, React.
Chem. Eng., 2018, 3, 769.

125 L. M. Rios and N. V. Sahinidis, Derivative-free optimization:
a review of algorithms and comparison of software imple-
mentations, J. Glob. Optim., 2013, 56, 1247–1293.

126 A. M. Gopakumar, P. V. Balachandran, D. Xue, J. E. Gubernatis
and T. Lookman, Multi-objective optimization for materials
discovery via adaptive design, Sci. Rep., 2018, 8, 3738.

127 B. Shahriari, K. Swersky, Z. Wang, R. P. Adams and
N. d. Freitas, Taking the human out of the loop: A review
of Bayesian optimization, Proc. IEEE, 2015, 104, 148–175.
128 P. I. Frazier and J. Wang, in Information Science for Materials
Discovery and Design, ed. T. Lookman, F. Alexander and
K. Rajan, 2015, Springer, pp. 45–76.

129 K. Higgins, S. M. Valleti, M. Ziatdinov, S. V. Kalinin and
M. Ahmadi, Chemical robotics enabled exploration of stability
in multicomponent lead halide perovskites via machine learn-
ing, ACS Energy Lett., 2020, 5, 3426–3436.

130 J. M. Herna´ndez-Lobato, M. W. Hoﬀman and Z. Ghahramani,
Predictive entropy search for eﬃcient global optimization of
black-box functions, NIPS, 2014, 918–926.

131 D. H. Wolpert and W. G. Macready, No free lunch theorems
for optimization, IEEE Trans. Evolut. Comput., 1997, 1, 67–82.
132 Z. Wang and S. Jegelka, Max-value entropy search for

eﬃcient Bayesian optimization, arXiv:1703.01968v3, 2018.

133 E. Brochu, V. M. Cora and N. D. Freitas, A tutorial
on Bayesian optimization of expensive cost functions, with
application to active user modeling and hierarchical reinfor-
cement learning, arXiv:1012.2599v1, 2010.

134 J. Wu and P. Frazier, The parallel knowledge gradient method
for batch bayesian optimization, arXiv:1606.04414v4, 2018.
135 R. W. Epps, A. A. Volk, K. G. Reyes and M. Abolhasani,
Accelerated AI development for autonomous materials
synthesis in flow, Chem. Sci., 2021, 12, 6025.

136 J. Snoek, et al., Scalable Bayesian optimization using deep
neural networks, in International Conference on Machine
Learning, 2015, pp. 2171–2180.

137 L. von Rueden et al., Informed machine learning – A
taxonomy and survey of integrating knowledge into learn-
ing systems, arXiv preprint arXiv:1903.12394, 2019.
138 B. J. Shields, et al., Bayesian reaction optimization as a tool

for chemical synthesis, Nature, 2021, 590, 89–96.

139 Z. Ren, et al., Embedding physics domain knowledge into a
Bayesian network enables layer-by-layer process innova-
tion for photovoltaics, npj Comput. Mater., 2020, 6, 1–9.
140 S. Sun, et al., A data fusion approach to optimize compositional
stability of halide perovskites, Matter, 2021, 4, 1305–1322.
141 R. D. King, et al., The automation of science, Science, 2009,

324, 85–89.

143 X. Wang, et al., Towards eﬃcient discovery of green
synthetic pathways with Monte Carlo tree search and
reinforcement learning, Chem. Sci., 2020, 11, 10959.
144 L. A. Klein. Sensor and data fusion: a tool for information
assessment and decision making, SPIE Press, 2004, vol. 138.
145 W. Sun, et al., The thermodynamic scale of inorganic
crystalline metastability, Sci. Adv., 2016, 2, e1600225.
146 O. Mitsunobu and M. Yamada, Preparation of esters of
carboxylic and phosphoric acid via quaternary phosphonium
salts, Bull. Chem. Soc. Jpn., 1967, 40, 2380–2382.

147 K. E. Whelan and R. D. King, Using a logical model to
predict the growth of yeast, BMC Bioinf., 2008, 9, 97.
148 M. Kanehisa and S. Goto, KEGG: Kyoto encyclopedia of
genes and genomes, Nucleic Acids Res., 2000, 28, 27–30.
149 I. M. Keseler, et al., EcoCyc: A comprehensive database
resource for Escherichia coli, Nucleic Acids Res., 2005, 33,
D334–D337.

150 M. H. Segler, M. Preuss and M. P. Waller, Planning
chemical syntheses with deep neural networks and symbolic
AI, Nature, 2018, 555, 604–610.

151 C. W. Coley, W. H. Green and K. F. Jensen, Machine
learning in computer-aided synthesis planning, Acc. Chem.
Res., 2018, 51, 1281–1289.

152 J. S. Schreck, C. W. Coley and K. J. M. Bishop, Learning
retrosynthetic planning through simulated experience,
ACS Cent. Sci., 2019, 5, 970–981.

153 V. Dragone, V. Sans, A. B. Henson, J. M. Granda and
L. Cronin, An autonomous organic reaction search engine
for chemical reactivity, Nat. Commun., 2017, 8, 15733.
154 S. Feng and R. Xu, New materials in hydrothermal synthesis,

Acc. Chem. Res., 2001, 34, 239–247.

155 Flex Autoplant from Chemspeed Technologies. https://

www.chemspeed.com/flex-autoplant/.

156 A. F. d. Almeida, R. Moreira and T. Rodrigues, Synthetic
organic chemistry driven by artificial intelligence, Nat. Rev.
Chem., 2019, 3, 589–604.

157 R. McClain, et al., Mechanistic insight of KBiQ2 (Q 1

4 S, Se)
using panoramic synthesis towards synthesis-by-design,
Chem. Sci., 2021, 12, 1378.

158 P. K. Todd, A. M. M. Smith and J. R. Neilson, Yttrium
manganese oxide phase stability and selectivity using
lithium carbonate assisted metathesis reactions, Inorg.
Chem., 2019, 58, 15166–15174.

159 D. P. Shoemaker, et al., In situ studies of a platform for
metastable inorganic crystal growth and materials discovery,
Proc. Natl. Acad. Sci. U. S. A., 2014, 111, 10922–10927.
160 A. Miura, et al., Observing and Modeling the Sequential
Pairwise Reactions that Drive Solid-State Ceramic Synth-
esis, Adv. Mater., 2021, 33, 2100312.

161 M. J. McDermott, S. S. Dwarakanth and K. A. Persson, A
graph-based network for predicting chemical reaction
pathways in solid-state materials synthesis, 2021, DOI:
10.21203/rs.3.rs-38000/v1.

142 R. D. King, et al., Functional genomic hypothesis genera-
tion and experimentation by a robot scientist, Nature,
2004, 427, 247–252.

162 M. Aykol, J. H. Montoya and J. S. Hummelshøj, Rational
solid-state synthesis routes for inorganic materials. ChemRxiv,
2021.

This journal is © The Royal Society of Chemistry 2021Mater. Horiz.Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article OnlineReview

Materials Horizons

163 Y. Rakita, et al., Active reaction control of Cu redox state
based on real-time feedback from in situ synchrotron
measurements, J. Am. Chem. Soc., 2020, 142, 18758–18762.
164 M. R. Cosby, et al., Salt eﬀects on Li-ion exchange kinetics
of Na2Mg2P3O9N: Systematic in situ synchrotron diﬀraction
studies, J. Phys. Chem. C, 2020, 124, 6522–6527.

165 O. Kononova, et al., Text-mined dataset of inorganic materials

synthesis recipes, Sci. Data, 2019, 6, 203.

166 O. Kononova, et al., Opportunities and challenges of text
mining in aterials research, iScience, 2021, 24, 102155.

167 S. H. M. Mehr, M. Craven, A. I. Leonov, G. Keenan and L. Cronin,
A universal system for digitization and automatic execution of
the chemical synthesis literature, Science, 2020, 370, 101–108.

168 E. Kim, et al., Machine-learned and codified synthesis
parameters of oxide materials, Sci. Data, 2017, 4, 170127.
169 C. W. Coley, N. S. Eyke and K. F. Jensen, Autonomous
discovery in the chemical sciences part II: Outlook, Angew.
Chem., Int. Ed., 2020, 59, 2–25.

170 P. Langley, The computational support of scientific discovery,

Int. J. Hum. Comput. Stud., 2000, 53, 393–410.

Mater. Horiz.This journal is © The Royal Society of Chemistry 2021Published on 19 May 2021. Downloaded by Lawrence Berkeley National Laboratory on 5/26/2021 6:00:51 PM. View Article Online
