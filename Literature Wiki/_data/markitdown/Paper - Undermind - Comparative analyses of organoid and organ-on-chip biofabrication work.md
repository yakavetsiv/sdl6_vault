---
source_note: "Papers/Paper - Undermind - Comparative analyses of organoid and organ-on-chip biofabrication work.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Undermind - Comparative analyses of organoid and organ-on-chip biofabrication workflows exposing automation gaps for self-driving systems.pdf"
converter: "microsoft/markitdown"
---
Undermind

REPORT CREATED ON
11/22/2025

Research Report on

Comparative analyses of organoid and organ-on-chip biofabrication
workflows exposing automation gaps for self-driving systems

Full search query: I want to find scholarly work that characterizes current organoid, organ-on-chip, and robotic biofabrication (including bioprinting)
tools and workflows, comparing manual and automated approaches, and explicitly describing limitations, automation gaps, and unmet needs in
throughput, reproducibility, spatial control, and multi-organoid assembly, in order to identify scientific and technical whitespace for AI-enabled,
closed-loop, imaging-guided, self-driving biofabrication systems

Summary

The literature reveals several mature but still fragmented automation platforms for organoids, organs(cid:17)on(cid:17)chips, and bioprinting
that clearly improve throughput and reproducibility over manual workflows [1,2,3,4,5,9,10,11,12,23,44,45], yet essentially no truly
end(cid:17)to(cid:17)end, AI(cid:17)enabled, imaging(cid:17)guided, closed(cid:17)loop “self(cid:17)driving” biofabrication system—especially for multi(cid:17)organoid assembly—has
been demonstrated, defining a large, well(cid:17)articulated whitespace [6,7,8,14,15,18,19,24,41].

Overall Picture: What This Corpus Says About “Self(cid:17)Driving” Biofabrication

• There are now several robust, production(cid:17)grade automated organoid platforms (e.g., ORCA [1], midbrain AMO pipeline [2,3],
microcavity arrays [12], automated microfluidic culture [10]) and high(cid:17)throughput biofabrication tools (tumor organoid droplet
printing [4], kidney organoid bioprinting [11], MAGIC granular bioprinting [23], pillar/perfusion plates [44,45], vascularized OoC
bioprinting [5]).

• These systems:

• Replace key manual operations (seeding, aggregation, ECM dispensing, feeding, chip loading).

• Quantitatively reduce batch(cid:17)to(cid:17)batch and organoid(cid:17)to(cid:17)organoid variation, and increase usable throughput [1,2,3,4,10,11,12].

• Begin to demonstrate spatially precise, programmable multi(cid:17)cell or multi(cid:17)organoid patterning, including assembloids

[4,5,6,11,23].

• At the same time:

• Decision(cid:17)level automation—where real(cid:17)time sensing drives culture or fabrication actions—is only just emerging, mainly in

narrow control problems (closed(cid:17)loop micromanipulation [6,7], mechanically triggered media changes [8]).

• Most AI/ML uses are for offline analysis and phenotyping (variability decomposition [1], HTS phenotyping [2,3], interfer-

ometric mass tracking [9]), not real(cid:17)time closed(cid:17)loop control.

• Multi(cid:17)organoid/multi(cid:17)organ assembly and long(cid:17)term control under a unified AI policy remain unaddressed.

• Reviews across organoids, OoCs, and bioprinting converge on the same unmet needs: standardized, modular hardware;

integrated, high(cid:17)throughput sensing (especially imaging); robust process(cid:17)analytical technologies; and intelligent control to close
the loop [13,14,15,18,19,24,25,26,28,29,30,31,32,34,35,36,37,40,41,42,43,46,48,49,50,51,52].

In short, the field has many of the component technologies your goal requires, but they are isolated and open(cid:17)loop; integrating them
into a self(cid:17)driving, imaging(cid:17)guided biofabrication stack is essentially untouched territory.

Current Automated Organoid Platforms: Gains Over Manual Practice and Remaining Gaps

Highly Automated Plate(cid:17)Based Organoid Workflows

• ORCA + OrgBook (cerebral organoids) [1]:

• Scope:

• Robotic liquid handling, plate handling, incubation, and imaging coordinated via a cloud(cid:17)based experiment manager.

• Longitudinal culture and multimodal phenotyping across many donor lines.

• Manual vs automated:

• Shows that manual pooled culture in spinner flasks amplifies variability and prevents repeated assays on individual

organoids [1].

• Single(cid:17)organoid 96(cid:17)well automated culture enables precise tracking and protocol optimization.

• Quantitative benefits:

• ML(cid:17)based variance decomposition across morphology, gene expression, and cell(cid:17)type composition reveals reduced

batch effects and a better separation of donor/clone contributions [1].

• Enables detection of early, reproducible disease phenotypes (e.g., TSC+/-).

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 1/41

Undermind

• Gaps:

REPORT CREATED ON
11/22/2025

• Protocols are still pre(cid:17)defined; imaging and analytics are used offline, not to adjust culture in real time.

• No spatial assembly or organoid(cid:17)on(cid:17)chip integration.

• Automated midbrain organoids (AMOs) in 96(cid:17)well HTS format [2,3]:

• Scope:

• Fully automated generation, maintenance, whole(cid:17)mount staining, clearing, and high(cid:17)content 3D imaging in standard

96(cid:17)well plates.

• Manual vs automated:

• Directly targets heterogeneity of manual midbrain organoid protocols.

• Demonstrates that full automation yields organoids with highly homogeneous size, morphology, global gene expres-

sion, cellular composition, and synchronized neural activity [3].

• Quantitative gains:

• Substantially reduced intra(cid:17) and inter(cid:17)batch variation, documented by RNA(cid:17)seq and high(cid:17)content imaging [2,3].

• Gaps:

• Decision(cid:17)level automation absent; all operations follow static scripts.

• Single organoid per well; no multi(cid:17)organoid assembly or dynamic protocol adaptation.

• High(cid:17)throughput aggregation in microcavity arrays [12]:

• Scope:

• Automated stem(cid:17)cell aggregation into organoids via microcavity arrays and liquid handling.

• Benefits vs manual wells:

• Tight control of initial cell numbers and aggregate sizes; improved homogeneity and throughput [12,41].

• Gaps:

• Focused on early aggregation only; later differentiation, quality control, and selection remain largely manual and

open(cid:17)loop.

Automated Microfluidic Organoid Culture

• 24(cid:17)plex automated microfluidic platform for cerebral organoids [10]:

• Scope:

• Programmable media flow and reagent delivery into 24 isolated organoid microchambers; compatible with longitu-

dinal live imaging and IoT(cid:17)style control.

• Manual vs automated:

• Continuous microfluidic feeding (automated) vs intermittent manual feeding.

• RNA(cid:17)seq shows significantly reduced glycolytic and ER stress gene expression in automated cultures [10].

• Gaps:

• Flow schedules are pre(cid:17)programmed; no adaptation based on imaging or sensor readouts.

• One organoid per chamber, no multi(cid:17)organoid assembly or coupling between chambers.

Robotic Control for Organoid Handling and Culture

• Robotic micromanipulation for fragment selection and seeding [7]:

• Scope:

• Robot selects tissue fragments of defined size and transfers them into a custom in(cid:17)situ organoid chip with microwells

using model(cid:17)predictive fluid(cid:17)control.

• Manual vs automated:

• Replaces subjective manual fragment handling.

• Produces significantly more homogeneous colorectal cancer organoids [7].

• Gaps:

• Limited to initial seeding; does not close the loop over long(cid:17)term culture or phenotypes.

• Closed(cid:17)loop micromanipulation for patterned organoids and assembloids [6]:

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 2/41

Undermind

• Scope:

REPORT CREATED ON
11/22/2025

• Micromanipulation platform with multi(cid:17)dimensional cell sensing, real(cid:17)time feedback, and adaptive fluid dynamics to

tightly control spatial distribution of multiple cell types.

•

Impact:

• Enables programmable organoid manufacturing and multi(cid:17)cell(cid:17)type assembloid construction with improved consisten-

cy [6].

• Gaps:

• Closed loop limited to seeding; does not yet govern days(cid:17)long differentiation, perfusion, or functional readouts.

• Mechanical(cid:17)feedback(cid:17)based personalized culture [8]:

• Scope:

• Ultra(cid:17)thin membrane sensors per organoid group + robotic culture system; uses real(cid:17)time mechanical signals to adapt

media(cid:17)change timing.

• Manual vs automated:

• Manual: discrete, visually guided, subjective decisions on media changes.

• Automated: sensor(cid:17)driven, personalized timing; improved 7(cid:17)day colorectal cancer organoid culture performance [8].

• Gaps:

• Only one control variable (media(cid:17)change timing); culture composition, spatial arrangement, and other stimuli remain

static.

• Sensing is mechanical; imaging and molecular data are not yet integrated into the feedback loop.

Overall, existing organoid platforms demonstrate that:

• Workflow(cid:17)level automation markedly improves reproducibility and throughput vs manual practice [1,2,3,10,11,12].

• Robotic micromanipulation and sensing can tackle previously intractable tasks (fragile fragment handling, finely patterned

assembloids, personalized feeding) [6,7,8].

• But none of these systems combine rich imaging, multi(cid:17)modal sensing, and AI(cid:17)driven control across the full organoid life cycle.

Automated Organs(cid:17)on(cid:17)Chips and Bioprinting: Manufacturing, Spatial Control, and Throughput

Bioprinting as a Replacement for Manual Organoid Generation

• Extrusion(cid:17)based kidney organoid bioprinting [11]:

• Replaces manual dome casting with controlled extrusion of PSC(cid:17)derived cells.

• Gains:

• Tight control over organoid size, initial cell number, and conformation; increased nephron yield per input cell; and

compatibility with 6(cid:17) and 96(cid:17)well formats [11].

• Demonstrates uniform kidney tissue sheets and drug toxicity assays.

• Gaps:

• QC imaging and analysis offline; no in situ, closed(cid:17)loop adjustment of printing parameters.

• Tumor organoid droplet templating and printing [4]:

• Scope:

• Matrigel droplet templating + rapid droplet printing to generate highly uniform tumor organoid precursors.

• Quantitative metrics:

• ~100–1,000 organoid precursors produced in <10 minutes; ~1 organoid/s sequential patterning; ~95% placement

success [4].

• Manual vs automated:

• Dramatically reduced organoid(cid:17)to(cid:17)organoid variability and labor vs manual unpatterned suspensions.

• Gaps:

• Partial automation only: e.g., plate transfer between modules remains manual.

• No interactive feedback based on imaging or functional readouts.

• Granular “MAGIC” matrix bioprinting for self(cid:17)organization [23]:

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 3/41

Undermind

• Scope:

REPORT CREATED ON
11/22/2025

• Tunable granular bioink with independent control over relaxation timescale and deformation magnitude; fully scripted

printing workflow.

• Benefits:

• Enables complex but uniform organoid morphogenesis; printed vs manually seeded organoids show more repro-

ducible self(cid:17)organization under optimized mechanical regimes [23].

• Gaps:

•

Imaging used to define good parameter regimes, but printing is not actively adjusted based on online readouts.

High(cid:17)Throughput Arrayed Printing and Plate(cid:17)Compatible Platforms

• Pillar/perfusion plate system with microarray 3D bioprinting [44,45]:

• Scope:

• High(cid:17)precision stem cell printing and encapsulation on pillar plates, coupled to deep(cid:17)well and perfusion plates.

• Features:

• Compatible with standard 384(cid:17)well HTS equipment.

• Demonstrated liver and intestine organoid differentiation with in situ functional assays [44,45].

• Gaps:

• Control remains open(cid:17)loop; no adaptive culture or printing based on live readouts.

• Spatial assembly limited to the static pillar array; no dynamic rearrangement or cross(cid:17)plate logistics.

Bioprinting and Robotics for Organs(cid:17)on(cid:17)Chips

• High(cid:17)scale 3D bioprinting + robotic handling for vascularized OoCs [5]:

• Scope:

• Drop(cid:17)on(cid:17)demand 3D bioprinting into a sealable, transparent microfluidic chip; robotic placement, loading, and assem-

bly; perfusion system integration.

• Gains:

• Three distinct tissue models printed on a chip in ~1 minute; many chips processed sequentially without manual

intervention [5].

• Stable vascular networks and liver carcinoma function (albumin) over 14 days.

• Gaps:

• No real(cid:17)time correction of printing or perfusion based on sensor data.

• Multi(cid:17)organ coupling and standardized interfaces are acknowledged but not fully solved.

• Bioprinting(cid:17)enabled OoC manufacturing (broader picture):

• Reviews and systematic analyses [27,28,29,31,33,38,39,46] consistently report that:

• 3D printing/bioprinting can move OoC fabrication from manual, multi(cid:17)step soft lithography toward automated, poten-

tially assembly(cid:17)free workflows with higher spatial control and reproducibility.

• Current limitations include:

• Printing resolution vs microfluidic length scales.

• Bioink constraints (viscosity, cytotoxicity).

• Lack of sensor(cid:17)integrated, high(cid:17)throughput manufacturing lines.

• Yi et al. [31] and Miri et al. [28] explicitly frame one(cid:17)step printing of chip and tissues as a way to avoid manual chip assembly

and loading—core pain points for closed(cid:17)loop deployment.

Reproducibility and Standardization in Bioprinting

• Round(cid:17)robin study on extrusion bioprinting reproducibility [16]:

• Multi(cid:17)site evaluation across 12 labs with shared materials and SOPs for cell(cid:17)free polymer inks.

• Findings:

• Substantial inter(cid:17)lab and operator(cid:17)dependent variability in printed geometries despite nominally standardized protocols

[16].

• Automated image analysis is feasible and yields similar feature ranges, but still requires manual artifact handling.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 4/41

Undermind

•

Identified gaps:

REPORT CREATED ON
11/22/2025

• Need for more automated hardware (piston(cid:17)driven extrusion, automated coordinate and z(cid:17)height calibration, temper-

ature(cid:17)controlled printheads) and formal process(cid:17)analytical technologies [16].

•

Implication:

• Even “automated” printers are not reproducible enough for self(cid:17)driving systems without additional sensing, standard-

ization, and closed(cid:17)loop control.

AI, Imaging, and Closed(cid:17)Loop Control: Current Uses vs Whitespace

How AI and Imaging Are Used Today

• Offline phenotyping and variability analysis:

• ORCA [1]: ML models decompose sources of variability (donor, clone, batch) across large datasets.

• AMOs [2,3]: AI framed as necessary to mine rich, multiplexed 3D imaging data for subtle phenotypes.

• HSLCI + ML [9]: ML(cid:17)based segmentation and classification increase trackable organoids ~15(cid:17)fold, enabling single(cid:17)organoid

drug(cid:17)response profiling.

•

Imaging(cid:17)based QC in bioprinting:

• Kidney organoids [11]: Fluorescent bead imaging used to quantify printed cell density and layer height.

• MAGIC matrix [23]: High(cid:17)throughput automated imaging pipelines used to compare bioprinted vs manually seeded

organoids and to map mechanical parameter space.

• Conceptual AI frameworks:

• Reviews on AI for bioprinting/biofabrication [14,18,19,24,52] detail:

• Use cases: parameter prediction, process optimization, real(cid:17)time monitoring, defect detection, predictive mainte-

nance, and robotic manipulation.

• Potential to use computer vision to guide printing and to perform automated quality control.

However, almost all of these applications are:

• Offline or near(cid:17)offline: AI processes images after the fact, informing future experiments but not dynamically modifying the current

one.

• Narrowly scoped: focused on a single device or operation (e.g., print quality, organoid classification), not integrated across the

entire workflow.

Genuine Closed(cid:17)Loop Examples

• Real(cid:17)time fluidic control during micromanipulation [6]:

• Sensing: “multidimensional cell sense” technology monitors cell distribution and fluid dynamics.

• Control: Adaptive fluid control compensates seeding(cid:17)induced nonlinear perturbations to maintain designed spatial distri-

butions.

• Outcome: Robust, reproducible patterning of complex organoids and multi(cid:17)cell(cid:17)type assembloids.

• Limitation: Loop closed only during the seeding step; no multi(cid:17)day adaptation.

• CFD(cid:17)informed robust model predictive control for fragment transfer [7]:

• Uses computational models to design control policies for robotic fragment transfer into chips.

• Feedback: Primarily on fluid dynamics and positioning, not biological state per se.

• Limitation: Still a single(cid:17)operation control problem; not a full experimental feedback loop.

• Mechanical feedback for personalized media change [8]:

• Sensing: Ultra(cid:17)thin membrane sensors provide continuous mechanical readouts from organoid groups.

• Control: Media(cid:17)change timing adapted based on sensed mechanical changes, enabling personalized culture.

• Limitation: Control acting on a single dimension of the protocol; no integration with imaging, molecular readouts, or spatial

manipulation.

Crucially, there is:

• No example in this corpus where:

• High(cid:17)content imaging (e.g., confocal, light(cid:17)sheet, HSLCI) feeds directly into an AI controller that then adjusts printing,

perfusion, media composition, or manipulation on the fly.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 5/41

Undermind

REPORT CREATED ON
11/22/2025

• Multiple devices (e.g., printer + microfluidics + microscope + robot) are orchestrated by a unified, state(cid:17)aware control policy

over days to weeks.

That absence defines a central whitespace for AI(cid:17)enabled, imaging(cid:17)guided, self(cid:17)driving biofabrication.

Cross(cid:17)Cutting Limitations and Automation Gaps Relevant to Your Goal

Across both primary studies and reviews, the same classes of limitations recur, and they map well onto your target axes (throughput,
reproducibility, spatial control, multi(cid:17)organoid assembly, and closed(cid:17)loop control):

1. Throughput and Workflow Integration

• Gains:

• 96(cid:17)well plate automation and HTS(cid:17)compatible workflows for organoids [1,2,3,11,12].

• 24(cid:17)plex microfluidic platforms [10], microarray bioprinting on pillar plates with 384(cid:17)well compatibility [44,45].

• High(cid:17)speed droplet printing and bioprinting for organoid seeding [4,9,11,23].

• Remaining gaps:

• Many operations still manual or semi(cid:17)manual:
• Plate/chip transfer between modules [4].

• Chip loading and bubble management [34,35,36,37,48,50].

• Sample preparation and some analytical steps (e.g., scRNA(cid:17)seq, immunostaining) [2,41].

• End(cid:17)to(cid:17)end integration—from cell thaw through fabrication, culture, and multi(cid:17)modal readout—remains rare and lab(cid:17)specific

[13,41].

Opportunity: A self(cid:17)driving system that spans the entire workflow, with a scheduler/orchestrator coordinating cell expansion,
printing/assembly, microfluidic loading, perfusion, imaging, and endpoint assays.

2. Reproducibility and Standardization

• Evidence of improvement:

• Reduced inter(cid:17) and intra(cid:17)batch variability with automated 96(cid:17)well organoid systems [1,2,3,11,12].

• Homogeneity gains from microcavity arrays, microwell chips, and microfluidic flow [10,12,41,48].

• Round(cid:17)robin evidence that standardized protocols alone are insufficient; hardware and operator effects still large [16].

• Persistent issues:

• ECM variability (especially Matrigel) complicates automation and standardization [2,4,41,47].

• Protocol diversity across labs and organoid types; few universally accepted SOPs [13,25,41].

• Lack of standardized chip formats and connectors for organ(cid:17)on(cid:17)chip [17,32,34,35,36,37].

Opportunity: Combine standardized physical formats (e.g., organoid(cid:17)on(cid:17)chip cartridges, FCB(cid:17)style interfaces [17]) with automated,
AI(cid:17)based QC pipelines (on(cid:17)the(cid:17)fly imaging + analysis) to enforce reproducibility and enable cross(cid:17)site self(cid:17)driving protocols.

3. Spatial Control and Multi(cid:17)Organoid Assembly

• What is possible today:

• Precise control of organoid size and initial geometry via bioprinting, microcavities, and microwells [4,11,12,23,41,48].

• Bioprinted tissue sheets and multi(cid:17)material constructs [5,11,23,31,33].

• Robotic micromanipulation achieving programmable assembloids with controlled spatial cell distributions [6] and highly

uniform fragment(cid:17)derived organoids [7].

• Multi(cid:17)tissue chips with interconnected compartments (e.g., three(cid:17)tissue OoC, vascularized chips) [5,31,46].

• Gaps:

• Few systems support dynamic rearrangement or re(cid:17)patterning over time (e.g., repositioning organoids based on observed

phenotype).

• Multi(cid:17)organ networks (e.g., liver–gut–kidney) often rely on fixed chip geometries and manual coupling [34,36,46].

• Robust 3D positional metrology (tracking actual vs intended positions over long culture times) is largely missing [41,48].

Opportunity: Imaging(cid:17)guided robotic micro(cid:17)assembly systems that can:

• Recognize, pick, and place organoids/spheroids with sub(cid:17)100 µm precision.

• Reconfigure multi(cid:17)organoid layouts over time as guided by observed functional states (e.g., to drive fusion or vascularization).

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 6/41

Undermind

REPORT CREATED ON
11/22/2025

4. Sensing and Readouts for Closed(cid:17)Loop Control

• Current state:

• Routine: brightfield/fluorescence imaging, sometimes high(cid:17)content 3D imaging [2,3,9,23,44,45].

• Advanced: label(cid:17)free interferometry for mass tracking [9], multi(cid:17)modal microfluidic sensing (TEER, electrochemical sensors)

[34,35,36,37,50], and integrated mechanical sensors [8].

• Limitations:

• Many functional assays remain endpoint, destructive, or low(cid:17)throughput (e.g., scRNA(cid:17)seq, immunostaining) [2,41,47].

•

Inline functional sensing (e.g., electrophysiology, contractility, secretion profiles) is not yet routine or standardized
[32,41,50].

• Real(cid:17)time analysis pipelines robust enough for control (latency, reliability, artifact robustness) are rarely described [9,16,41].

Opportunity: Design sensor suites and analysis pipelines explicitly for control—not just for characterization—e.g.:
• Pre(cid:17)defined, robust feature sets derived from imaging (size, shape, lumen count, functional markers, motion).

• Real(cid:17)time anomaly detection and state estimation to feed into control policies (RL, MPC).

5. Decision(cid:17)Level Automation and AI(cid:17)Driven Control

• Existing decision(cid:17)level examples are narrow (fluid dynamics control [6,7], media(cid:17)change timing [8]).

• Concept papers and reviews explicitly call for intelligent monitoring and control, especially via AI/ML [14,15,18,19,24,41,52],

but implementations are mostly missing.

Opportunity: The core “self(cid:17)driving” whitespace:

•

Implement controllers (possibly model(cid:17)based or RL) that:

• Observe multi(cid:17)modal state (imaging + sensors + historical trajectories).

• Choose actions (printing parameters, media recipes, flow rates, mechanical stimuli, spatial manipulations).

• Learn from outcomes across many experiments (as ORCA already does in a batch(cid:17)optimization sense [1]) but now in an

online, adaptive fashion.

Synthesis: Where the Scientific and Technical Whitespace Lies

Given your stated goal, the key conclusions from this corpus are:

1. The building blocks for self(cid:17)driving biofabrication already exist but are siloed:

• High(cid:17)throughput automated organoid culture (ORCA, AMOs, microcavities) [1,2,3,10,12].

• Automated and programmable biofabrication/bioprinting with good spatial and throughput characteristics [4,5,9,11,23,44,45].

• Microfluidic organ(cid:17)on(cid:17)chip platforms enabling fine control of microenvironment and multi(cid:17)organ coupling, with emerging modular

standards (FCB) [5,10,17,31,32,34,35,36,37,46,50].

• Early closed(cid:17)loop robotic control systems (micromanipulation, personalized feeding) that prove feasibility of decision(cid:17)level

automation in specific tasks [6,7,8].

1. The main whitespace is in integration and control, not in inventing entirely new hardware modalities:

• No publication combines:

• Rich, high(cid:17)throughput imaging and sensing,

• With AI(cid:17)driven, real(cid:17)time control policies,

• Coordinating multiple devices (printers, robots, microfluidic controllers, microscopes),

• Over multi(cid:17)day organoid/OoC experiments.

1. Particularly underexplored areas that align directly with your ambition:

•

Imaging(cid:17)guided robotic micro(cid:17)assembly of multi(cid:17)organoid systems:

• Using real(cid:17)time CV to localize and classify organoids, then assemble them into complex chips or scaffolds based on desired

phenotypes (e.g., selecting only “correct” organoids measured by morphology/marker expression).

• Closed(cid:17)loop control of differentiation and maturation trajectories:

• Adjusting media composition, flow, and mechanical stimuli based on continuously measured constructs (morphology,

functional readouts) rather than fixed schedules.

• Multi(cid:17)layer, multi(cid:17)device orchestration:

• Building on open hardware like FCB [17] and plate(cid:17)compatible systems [3,10,44], but adding an experiment(cid:17)orchestration

layer akin to OrgBook [1] that can run AI(cid:17)driven protocols across heterogeneous devices.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 7/41

Undermind

REPORT CREATED ON
11/22/2025

1. There is strong conceptual support for your vision in high(cid:17)level reviews, but almost no concrete systems yet:

• Nature Reviews and high(cid:17)impact reviews repeatedly call for automation, intelligent monitoring, and AI(cid:17)enabled control

[15,19,30,31,32,34,35,36,37,41,48,49,50,51,52].

• Yet the only implemented closed(cid:17)loop examples are limited to one or two control variables in single devices [6,7,8].

This combination—mature automated components, clear quantitative benefits over manual methods, explicit recognition of automa-
tion and AI needs, but very little integrated, closed(cid:17)loop realization—defines a rich and tractable space for developing AI(cid:17)enabled,
imaging(cid:17)guided, self(cid:17)driving biofabrication systems targeting throughput, reproducibility, spatial control, and multi(cid:17)organoid assembly.

Categories

Comparative Analysis of Key Experimental Automation Platforms

Overview

Below, I focus on the most directly relevant experimental platforms that actually implement automated or semi(cid:17)automated
organoid/OoC/biofabrication workflows and report quantitative or at least concrete qualitative comparisons vs manual practice:
[1,2,3,4,5,6,7,8,9,10,11,12,23,5,6,7,8,9,10,44,45]. These are compared along dimensions an expert would care about for “self(cid:17)driving
biofabrication”: scope of automation, level of decision(cid:17)making, sensing/imaging, metrics for throughput/reproducibility/spatial control,
and explicit limitations/gaps.

Comparison of Experimental Platforms Relevant to Self-Driving Biofabrication

(Organoids, organ(cid:17)on(cid:17)chip, and biofabrication/bioprinting systems with substantial automation)

Ref

[1]

System / modali-
ty

Scope of au-
tomation (task /
workflow / deci-
sion)

Manual vs auto-
mated compari-
son (what actual-
ly improved)

ORCA + OrgBook:
robotic, cloud(cid:17)-
managed cerebral
organoid culture

• Task(cid:17) and work-
flow(cid:17)level automa-
tion: robotic liq-
uid handling, plate
handling, incu-
bation, imaging;
cloud LIMS (Org-
Book) for protocol
management and
metadata tracking.

• Contrasts
automated
single(cid:17)organoid
96(cid:17)well culture vs
manual
pooled/bioreactor
culture; shows
pooled/manual
methods inflate
variability and
prevent
longitudinal
tracking of
individual
organoids.

[3]

Fully automat-
ed HTS midbrain
organoid workflow

• End(cid:17)to(cid:17)end
task/workflow au-
tomation for mid-
brain organoids:
aggregation, dif-
ferentiation, media
changes, whole(cid:17)-
mount staining,

• Directly target-
ed at replacing
manual midbrain
organoid work-
flows that pro-
duce heteroge-
neous aggregates.
• Demonstrates
that fully automat-
ed handling yields
highly homoge-
neous organoid
morphology, size,
gene expression,
and cellular com-

Throughput / re-
producibility /
spatial control –
key quantitative
or concrete find-
ings

• Large(cid:17)scale
patient(cid:17)derived
brain organoids
across many lines.
• Automated
protocol
optimization yields
a directed
forebrain protocol
compatible with
96(cid:17)well format with
reduced variability
in morphology,
gene expression,
and cell(cid:17)type
composition while
preserving
complexity [1]. •
Decomposition of
variance into
donor/clone/batch
components via
ML—first
systematic
quantification of
these sources at
scale in an
automated
system.

• HTS(cid:17)compatible
96(cid:17)well format with
one organoid per
well. • RNA(cid:17)seq
and high(cid:17)content
3D imaging show
significantly re-
duced intra(cid:17) and in-
ter(cid:17)batch variability

Sensing / imag-
ing and data han-
dling

Explicit limita-
tions and au-
tomation gaps
(relative to self(cid:17)-
driving vision)

• Longitudinal
multimodal phe-
notyping: auto-
mated imaging
plus transcrip-
tomics and oth-
er assays. • ML
used to quantify
variability sources
and discover ear-
ly phenotypes in
TSC+/- organoids.

• No online feed-
back from imaging
to actuation—pro-
tocols are opti-
mized offline and
then executed as
static programs. •
No spatial place-
ment/assembly of
multiple organoids;
focus is on single
organoid per well.
• ECM depen-
dence, inline func-
tional sensing, and
cross(cid:17)device inter-
operability not fully
addressed.

• Whole(cid:17)mount
clearing adapt-
ed for automa-
tion; high(cid:17)content
3D fluorescence

• No decision(cid:17)lev-
el automation:
screening proto-
cols are pre(cid:17)de-
fined; imaging is
not used to ad-
just culture condi-
tions in real time.
• No explicit spa-
tial assembly of
multiple organoids;
focus on homo-
geneous, isolat-
ed organoids. •
ECM dependence

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 8/41

Undermind

REPORT CREATED ON
11/22/2025

(AMOs) in 96(cid:17)well
plates

clearing, high(cid:17)con-
tent imaging [3].

Automated Mid-
brain Organoids
(AMOs) + AI(cid:17)based
phenotyping con-
cept paper

• Builds on [3]; em-
phasizes integra-
tion of automated
culture/assay with
AI(cid:17)based analysis.

Automated Ma-
trigel droplet
templating and
organoid printing
platform (tumor
organoids)

• Task(cid:17)level au-
tomation: droplet
templating and
dispensing cel-
l(cid:17)laden Matrigel
into plates; partial
workflow automa-
tion for organoid
initiation.

Extrusion(cid:17)based
cellular bioprinting
for kidney
organoids
(replacing manual
formation)

• Task(cid:17)level au-
tomation: con-
trolled extrusion of
PSC(cid:17)derived cells
to form organoids
or tissue sheets.

position compared
to typical manual
protocols.

• Reiterates
manual limita-
tions (ECM vari-
ability, labori-
ous staining/sec-
tioning, het-
erogeneity) and
shows automa-
tion in [3] re-
duces variabili-
ty across batches
and donors.

• Explicitly com-
pares manual un-
patterned suspen-
sions vs au-
tomated templat-
ed droplets; shows
manual methods
produce broad
size/shape distrib-
utions, while au-
tomated printing
yields monodis-
perse organoid
precursors [4]. •
Reduced labor and
higher scalability
vs manual dome
casting.

vs manual meth-
ods [2,3].

imaging with sin-
gle(cid:17)cell resolution.

• Optimizes clear-
ing and 3D imag-
ing for fully au-
tomated pipelines;
explicitly positions
AI/ML as needed
to mine rich, mul-
tiplexed datasets
instead of simple
size/viability met-
rics.

• Mainly end-
point imaging and
molecular assays;
no inline imag-
ing(cid:17)based feedback
during printing.

• Demonstrates
low inter(cid:17)/intra(cid:17)batch
variation in mor-
phology, size, and
cell subpopula-
tions in AMOs, en-
abling HTS [2].

• Production
rate: ~100–1,000
organoid precur-
sors in <10 min;
sequential pat-
terning at ~1
organoid/s [4]. •
~95% placement
success; failures
linked to Matrigel
temperature con-
trol. • Organoids
show reduced
size heterogene-
ity while maintain-
ing patient(cid:17)specif-
ic heterogeneity
(RNA(cid:17)seq, histol-
ogy, drug re-
sponse).

• Spinning(cid:17)disk
confocal imag-
ing of fluorescent
beads for quali-
ty control; custom
Python analysis for
bead counting and
morphology.

• Direct compar-
ison vs manu-
al organoid gen-
eration: bioprint-
ing provides more
reproducible cell
numbers, organoid
sizes, and confor-
mations; increases
nephron yield per
input cell and al-
lows production of
uniform kidney tis-
sue sheets [11].

• Supports 6(cid:17)
and 96(cid:17)well for-
mats; high-
(cid:17)throughput gener-
ation with fixed cell
number per con-
struct. • Bead-
(cid:17)based imaging
quantifies printed
cell density and
layer height; shows
high reproducibility
of deposited vol-
umes [11].

[2]

[4]

[11]

[12]

Microcavity(cid:17)array
driven
high(cid:17)throughput
automated
organoid culture
(PSC aggregation)

• Task(cid:17)/work-
flow(cid:17)level automa-
tion: microcavity
arrays + auto-
mated liquid han-
dling for parallel
stem(cid:17)cell aggrega-
tion into organoids
[12].

• Replaces man-
ual aggregation
in low(cid:17)adhesion
plates; provides
controlled initial
cell numbers and
uniform aggrega-
tion conditions.

[10]

24(cid:17)plex automated
microfluidic plat-

• Workflow(cid:17)level
automation of per-
fusion and reagent
delivery: program-
mable flow control,
multiple reservoirs,
user(cid:17)defined flow
profiles; compati-

• Contrasts con-
tinuous automated
microfluidic feed-
ing vs manual bulk
feeding; shows re-
duced transcrip-
tional signatures of
glycolytic and ER

• Standard mi-
croscopy compat-
ible; microarrays
designed for in-
tegration with au-
tomated platforms
and parallel imag-
ing [12,41].

• Integrated sta-
tionary imaging
platform for longi-
tudinal live imaging
of each organoid;

• High(cid:17)through-
put formation of
large numbers of
aggregates with
tightly controlled
size distributions
in microcavities;
improved homo-
geneity vs manual
wells (as summa-
rized in [41]).

• 24 indepen-
dently addressable
organoid cham-
bers with continu-
ous flow; improved
parallelization and
long(cid:17)term mainte-
nance. • RNA(cid:17)seq:
downregulation of
glycolytic and ER
stress genes in

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 9/41

and long(cid:17)term mul-
ti(cid:17)modal sensing
integration not fully
addressed.

• AI/ML
used conceptual-
ly/offline; no real(cid:17)-
time feedback to
control culture or
screening. • Many
deep assays (e.g.,
scRNA(cid:17)seq) remain
low(cid:17)throughput and
weakly automat-
able; integration
into closed(cid:17)loop
systems is not yet
realized.

• Plate trans-
fer between mod-
ules still manual
(no robotic arm),
breaking full work-
flow automation. •
Limited organoid
yield per patient
sample (~300–500
per surgery; few-
er from biop-
sies) constrains
large combinator-
ial screens. • No
decision(cid:17)level au-
tomation or mul-
ti(cid:17)organoid spatial
assembly beyond
regular arrays; chip
integration and
closed(cid:17)loop moni-
toring not imple-
mented.

• No workflow(cid:17)lev-
el automation (cell
expansion, media
changes, imag-
ing, and analy-
sis largely sep-
arate). • No re-
al(cid:17)time feedback
from imaging to
printing parame-
ters; QC is offline. •
Multi(cid:17)organoid as-
sembly limited to
sheets/arrays; no
dynamic assembly
of heterogeneous
organoids.

• Mostly governs
early aggregation
and size; down-
stream differen-
tiation, analysis,
and selection still
not fully automat-
ed. • No closed(cid:17)loop
adaptation of ag-
gregation para-
meters based on
real(cid:17)time imaging.

• No active feed-
back from imag-
ing or sen-
sors to adjust
flow; profiles are
pre(cid:17)programmed. •
No high(cid:17)preci-
sion spatial place-
ment or multi-
(cid:17)organoid assem-
bly; one organoid

Undermind

REPORT CREATED ON
11/22/2025

[5]

[6]

[7]

[8]

form for cerebral
organoids

ble with automated
imaging.

stress in microflu-
idic cultures [10].

IoT(cid:17)style control
compatible.

automated mi-
crofluidic cultures
relative to conven-
tional manual cul-
tures [10].

High(cid:17)scale 3D bio-
printing platform +
robotic handling for
vascularized or-
gans(cid:17)on(cid:17)a(cid:17)chip

• Addresses man-
ual OoC fabrica-
tion and assem-
bly (chip load-
ing, sealing, tubing
hookup) as bottle-
necks; offers au-
tomated chip han-
dling and rapid tis-
sue patterning.

• Task(cid:17) and
workflow(cid:17)level
automation:
drop(cid:17)on(cid:17)demand
bioprinting of
tissues directly
into sealable
microfluidic chips,
robotic
placement/load-
ing/assembly of
chips, and
connection to
perfusion systems
[5].

Closed(cid:17)loop robot-
ic micromanipula-
tion platform for
patterned, com-
plex organoid bio-
fabrication (as-
sembloids)

• Task(cid:17) and de-
cision(cid:17)level au-
tomation: robot-
ic micromanipula-
tion with multidi-
mensional sens-
ing; closed(cid:17)loop
control of fluid dy-
namics to com-
pensate for non-
linear perturba-
tions during seed-
ing [6].

• Explicitly targets
lack of standard-
ization and control
of cell distribution
in ECM compared
to largely manu-
al embedding; en-
ables program-
mable organoid
manufacturing and
construction of as-
sembloids com-
posed of multiple
cell types [6].

Robotic micro-
manipulation sys-
tem + in(cid:17)si-
tu organoid chip
(IOC) for homo-
geneous colorectal
cancer organoid
culture

• Task(cid:17)level au-
tomation plus
model(cid:17)based con-
trol: robotic sys-
tem selects tissue
fragments by size
and transfers them
into microwell IOC
using robust mod-
el predictive con-
trol (RMPC) guid-
ed by CFD models
[7].

• Directly com-
pares robotic
transfer vs con-
ventional manu-
al fragment han-
dling: robotic sys-
tem achieves
more homoge-
neous organoid
morphologies in
colorectal cancer
organoid cultures
[7].

• Imaging through
transparent chips
for morphology
and function; per-
fusion readouts
(e.g., albumin) as
functional metrics.

• “Multidimension-
al cell sense tech-
nology” for real(cid:17)time
feedback on cell
distribution; sen-
sors feed into
adaptive control of
seeding flows [6].

• IOC design fa-
cilitates imaging;
system validated
via simulation +
experiments, like-
ly with standard
microscopy read-
outs.

• Can print
three distinct tis-
sue models on
a chip within ~1
min and process
many chips se-
quentially without
manual interven-
tion [5]. • Demon-
strates stable vas-
cular networks and
liver carcinoma
tissue with albumin
secretion over 14
days under perfu-
sion.

• Demonstrates
constrained
spatial distribution
of multiple cell
types to drive
consistent
self(cid:17)assembly;
improved
reproducibility of
patterned
organoid
structures vs
uncontrolled
manual cell
seeding
(qualitative/quanti-
tative data in the
paper).

• Microwell IOC
provides uni-
form microenvi-
ronment; robot-
ic selection al-
lows tighter initial
size distributions
and improved ho-
mogeneity (quan-
tified in morpho-
logical metrics).

Robotic system for
long(cid:17)term person-
alized automat-
ed cultivation of
colorectal cancer
organoids (CR-

• Task(cid:17) and deci-
sion(cid:17)level automa-
tion: distributed ul-
tra(cid:17)thin membrane
sensors for re-
al(cid:17)time mechanical
monitoring (RISM)
+ long(cid:17)term au-
tomated culture
platform (LTAC)
that adjusts me-
dia change tim-
ing based on

• Contrasts con-
ventional manu-
al media change
based on subjec-
tive optical evalua-
tion vs automated,
sensor(cid:17)driven tim-
ing; manual ap-
proaches cannot
adapt to patien-

• Demonstrates
7(cid:17)day CRCO cul-
ture with contin-
uous mechanical
monitoring of in-
dividual organoid
groups and adap-
tive media change
timing; reports im-
proved growth/vi-
ability relative to

• Mechanical sen-
sors embed-
ded per organoid
group; real(cid:17)time
in situ monitoring
feeds into control

per chamber. • Mi-
crofluidic loading
and bubble man-
agement still chal-
lenging; chip for-
mat not standard-
ized across sys-
tems.

• Feedback is lim-
ited to offline eval-
uation; no re-
al(cid:17)time closed(cid:17)loop
correction during
printing or perfu-
sion. • Chip sealing
and perfusion in-
tegration are auto-
mated but sensory
integration (pres-
sure, flow, imag-
ing) is not yet used
for adaptive con-
trol. • Multi(cid:17)organ
chip(cid:17)to(cid:17)chip inte-
gration and stan-
dardized inter-
faces still open is-
sues.

• Closed(cid:17)loop
is limited to
the seeding/man-
ufacturing phase;
not extended to
long(cid:17)term cul-
ture, perfusion,
or differentiation.
• No integra-
tion with large(cid:17)s-
cale screening or
multi(cid:17)device work-
flows. • Specifics
of sensing modal-
ities and gener-
alizability to other
bioinks/chips re-
main to be stan-
dardized.

• Selection is
still semi(cid:17)super-
vised/initiated by
operator; deci-
sion(cid:17)level automa-
tion is confined
to executing pre(cid:17)-
computed control
trajectories. • Fo-
cus is on initial
culture setup; not a
full end(cid:17)to(cid:17)end, self-
(cid:17)optimizing culture
workflow. • No in-
tegrated functional
readouts or adap-
tive medium/for-
mulation control.

• Feedback fo-
cuses solely on
media(cid:17)change tim-
ing; other culture
decisions (com-
position, tempera-
ture, flow) remain
static. • Sens-
ing is mechanical,
not imaging(cid:17)based;
integration with
imaging/omics is
not described. •
Limited to sin-
gle organoid type
and relatively short

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 10/41

Undermind

REPORT CREATED ON
11/22/2025

COs) with me-
chanical sensors

sensed mechani-
cal changes [8].

t(cid:17)specific variations
[8].

fixed schedules
(details in paper).

strategy for media
changes [8].

culture duration (7
days).

Bioprinting +
high(cid:17)speed live cell
interferometry
(HSLCI) for
single(cid:17)organoid(cid:17)res-
olution drug
screening

• Task(cid:17)level au-
tomation: auto-
mated bioprint-
ing for organoid
seeding; automat-
ed interferometric
imaging; ML(cid:17)based
offline segmenta-
tion and track fil-
tering.

• Bioprinting re-
places manual
seeding, reducing
time and opera-
tor(cid:17)dependent vari-
ability [9]. • ML(cid:17)en-
hanced analysis
increases num-
ber of trackable
organoids ~15(cid:17)fold
compared to ini-
tial naive tracking
(~1% usable) [9].

• Thousands of
individual tumor
organoids imaged
in parallel; HSL-
CI yields dry
mass trajectories
and distinguishes
transient vs per-
sistent drug re-
sponses [9].

• Label(cid:17)free
quantitative phase
imaging (HSLCI)
with high temporal
resolution; ML for
segmentation/clas-
sification of
organoid tracks.

[9]

[23]

“MAGIC matrix”
granular bioink
+ automated
bioprinting for
organoid self(cid:17)orga-
nization

• Task(cid:17)level au-
tomation: parame-
terized, scripted
bioprinting work-
flow (automated
aspiration, posi-
tioning, extrusion)
using programma-
ble stages [23].

• Directly
compares
bioprinted vs
manually seeded
organoids;
demonstrates that
stress(cid:17)relaxing
granular matrix
with controlled
printing improves
complex yet
uniform
self(cid:17)organization
[23].

[44,45]

Pillar + perfu-
sion plate plat-
form with microar-
ray 3D bioprinting
for organoids

• Task(cid:17)/work-
flow(cid:17)level automa-
tion: microar-
ray 3D bioprint-
ing of cells/spher-
oids onto pil-
lar plates; cou-
pling with deep-
(cid:17)well and perfu-
sion plates for sta-
tic/dynamic culture
[44,45].

• Targets
low throughput
and reproducibili-
ty of conventional
organoid differen-
tiation and fluidic
systems; demon-
strates high(cid:17)preci-
sion, high(cid:17)through-
put stem cell print-
ing and encap-
sulation on pillar
plates vs manual
loading [44,45].

• High(cid:17)throughput
imaging using GE
IN Cell Analyzer
2200; custom Fiji
macros for seg-
mentation and vol-
ume quantification;
bootstrapped sta-
tistics [23].

• Designed
for compatibili-
ty with stan-
dard HTS scan-
ners/plate read-
ers; allows in situ
functional read-
outs while under
perfusion.

• Tunable
viscoelastic matrix
with
independently
adjustable
relaxation time
and loss tangent;
identifies
parameter
regimes that
optimize
morphogenesis. •
Automated
printing yields
high(cid:17)fidelity
patterns;
throughput: arrays
of printed
organoids
constrained to
user(cid:17)defined
bounding boxes;
exact numbers
depend on print
layout but are
high(cid:17)density.

• Pillar/perfusion
plates compatible
with 384(cid:17)well for-
mat and HTS
equipment [44,45].
• Demonstrat-
ed differentia-
tion of print-
ed cells/spheroids
into liver and in-
testine organoids
with in situ func-
tional assays.

• Imaging is
single(cid:17)plane;
multi(cid:17)plane
imaging would
reduce temporal
resolution and
increase data
volume. • ~6 h
delay between
drug dosing and
imaging misses
very rapid events
[9]. • No real(cid:17)time
control based on
imaging; ML is
used offline, and
culture conditions
are not adjusted
adaptively. • Data
volume (~250
GB/plate/day)
makes analysis a
bottleneck; no
integrated control
layer.

• Feedback from
imaging is offline;
printing parame-
ters are not ad-
justed in real time.
• Perfusion inte-
gration and multi-
(cid:17)organoid function-
al assembly be-
yond patterning
are not fully ex-
plored. • Work-
flow still requires
manual cell slur-
ry preparation and
system setup.

• While print-
ing and per-
fusion geome-
try are standard-
ized, there is no
decision(cid:17)level au-
tomation (media
change, differen-
tiation cues, etc.,
are scheduled, not
feedback(cid:17)driven). •
Spatial assembly
is regular (pillar
array); no dynamic
re(cid:17)arrangement of
multiple organoids.
• Chip(cid:17)level sensors
beyond bulk read-
outs are not inte-
grated.

Key takeaways across these platforms:

• Workflow(cid:17)level automation of organoid culture is now clearly feasible at 96(cid:17)well scale ([1,2,3]) and in microfluidic chips ([10]),

with quantifiable improvements in reproducibility and stress reduction compared to manual protocols.

• Task(cid:17)level biofabrication automation (bioprinting, droplet templating, microarray printing) provides strong gains in size/shape

control and throughput ([4,9,11,12,23,44,45]).

•

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 11/41

Undermind

REPORT CREATED ON
11/22/2025

Robotic micromanipulation and sensing begin to address spatial precision and decision(cid:17)level control ([6,7,8]), with [6,8] being
the clearest steps toward genuine closed(cid:17)loop behavior (though still limited in scope).

However, no platform yet integrates:

• High(cid:17)throughput automated fabrication,

• Rich real(cid:17)time imaging/sensing,

• And algorithmic decision(cid:17)making that adaptively controls culture and assembly over days/weeks.

This gap defines prime whitespace for “self(cid:17)driving” biofabrication systems.

Comparative Synthesis of Review and Concept Papers on Automation Gaps and AI/Closed-Loop
Needs

Here, I compare the main reviews and concept papers that explicitly analyze au-
tomation, scalability, and AI/closed(cid:17)loop issues across organoids, OoC, and bioprinting:
[13,14,15,18,19,20,21,22,24,25,26,28,29,30,31,32,33,34,35,36,37,40,41,42,43,46,47,48,49,50,51,52,17,31,30,41,48,49,50].

How Reviews Frame the Automation and Self-Driving Biofabrication Whitespace

Focus domain

Manual vs automat-
ed workflow analysis

Ref

[13]

[15]

Automation of
organoid cultures (re-
view)

Integrating engi-
neering, automation,
and intelligence for
organoids

[14,42,40,43]

Bioprinting of
organoids with AI
/ 3D bioprinting for
organoids (multiple
reviews)

[18,19,24,52]

AI for bioprinting/bio-
fabrication (reviews)

[41]

Surveys current auto-
mated organoid plat-
forms (incl. cere-
bral/retinal); explicitly
motivated by limita-
tions of manual scal-
ing and variability [13].

Explicitly argues that
high(cid:17)throughput, ho-
mogeneous, stan-
dardized organoid
production, automat-
ed manipulation, and
intelligent monitor-
ing/control are miss-
ing from current prac-
tice [15].

Contrast manual
organoid culture (vari-
able, labor(cid:17)intensive)
with bioprinting’s po-
tential for stan-
dardized, automat-
ed cell placement
[14,40,42,43].

Not focused on man-
ual vs automated bi-
ology per se; assume
bioprinting as “auto-
mated” baseline.

Systematic analysis
of organoid limitations
and engineering in-
terventions; discuss-
es manual vs micro-
engineered workflows

Throughput / repro-
ducibility / spatial
control gaps high-
lighted

Notes need for
large(cid:17)scale, repro-
ducible organoid gen-
eration; manual pipet-
ting and ECM handling
are bottlenecks; em-
phasizes compatibili-
ty with liquid handlers
and HTS.

Summarizes batch(cid:17)to(cid:17)-
batch variability, low
throughput, lack of
standardization, and
limitations of hydro-
gel domes and manu-
al handling; advocates
organoids(cid:17)on(cid:17)chip as
“ideal platform” [15].

Emphasize that bio-
printing can control
size, shape, and com-
position; highlight un-
resolved issues: print-
ing resolution vs vi-
ability, bioink con-
straints, limited vas-
cularization, and limit-
ed high(cid:17)throughput ca-
pability [14,40,42,43].

Note lack of standard-
ized, high(cid:17)throughput,
sensor(cid:17)rich printers;
challenge of in-
tegrating multimodal
process data; need for
better process(cid:17)analyti-
cal technologies.

Identifies core gaps:
high batch variability,
low throughput, limit-
ed analytical access,
hydrogel domes in-
compatible with elec-
trodes, small analyte
volumes, labor(cid:17)inten-
sive single(cid:17)timepoint
assays; calls for con-
trolled positioning and
shape constraints to

AI / closed(cid:17)loop /
self(cid:17)driving relevance

Distinctive contri-
bution for our topic

Suggests increased
use of automation but
only touches briefly on
data(cid:17)driven control; no
deep AI framework.

Good field(cid:17)level map
of existing organoid
automation platforms
and protocols; use-
ful context for where
ORCA [1], AMOs
[3], microcavity arrays
[12], etc., fit.

Clearly frames AI and
on(cid:17)chip instrumenta-
tion as necessary for
intelligent monitoring,
evaluation, and con-
trol; conceptual blue-
print for self(cid:17)driving
organoid platforms.

The clearest articula-
tion of end(cid:17)to(cid:17)end “en-
gineering + AI” strat-
egy for organoids; di-
rectly aligned with
self(cid:17)driving biofabrica-
tion vision, though
mostly conceptual.

[14,42] explicitly pro-
pose AI for real(cid:17)-
time monitoring and
feedback during print-
ing; [40,43] empha-
size need for optimiz-
ing bioprinter hard-
ware and process
control but are less
specific on AI.

These position bio-
printing as a key
automation step and
articulate specific
technical bottlenecks
that AI(cid:17)enabled feed-
back could address
(e.g., defect detection,
process optimization,
in situ QC).

Detail use cases for
AI: predicting optimal
parameters, real(cid:17)time
monitoring, error cor-
rection, and adaptive
control in 3D bioprint-
ing [18,19,24,52].

Alludes to automa-
tion and “intelli-
gent” measurement
but does not for-
malize AI/closed(cid:17)loop;
nonetheless points to
the need for automat-
ed routine function-
al measurements and

Provide generic but
useful conceptual
frameworks for how
ML/CV/robotics can
close the loop in
biofabrication, which
can be mapped onto
organoid/OoC con-
texts.

Central high(cid:17)level ref-
erence for articulat-
ing organoid engi-
neering gaps direct-
ly relevant to self(cid:17)-
driving systems—es-
pecially around posi-

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 12/41

Undermind

[37,36,35,34,48,50]

REPORT CREATED ON
11/22/2025

standardized plat-
forms.

tioning, inline sensing,
and throughput.

Discuss opportunities
for integrating biosen-
sors and real(cid:17)time
monitoring, but ful-
ly closed(cid:17)loop demon-
strations are rare.
Some works men-
tion “IoT(cid:17)style” or
semi(cid:17)automated con-
trol [10,37].

These reviews clearly
articulate system(cid:17)lev-
el bottlenecks for
OoC and organoid-
s(cid:17)on(cid:17)chip, especially
around hardware in-
tegration, paralleliza-
tion, and standard-
ized interfaces—key
design constraints for
self(cid:17)driving platforms.

Engineering
organoids (Nature
Rev. Materials)

Organoids(cid:17)on(cid:17)chip /
microengineered
organoids /
microfluidic +
bioelectronic
interfaces

(microwells, microflu-
idics, bioprinting).

Compare tradition-
al static cultures
vs microfluidic/OoC
systems; highlight
how microfluidics
and automation im-
prove control and
reduce variability
[34,35,36,37,48,50].

enable inline sens-
ing and high(cid:17)through-
put functional read-
outs [41].

Recurrent themes:
complexity of chip
operation (tubing,
pumps), lack of
standardization,
bubble
formation/loading
challenges, limited
scalability, and
difficulty integrating
multimodal sensors
[34,35,36,37,48,50].
[36] discusses
multi(cid:17)organoids(cid:17)on(cid:17)chip
advances and
remaining
reproducibility issues.

[28,29,31,27,30,33,38,39,46,32]

3D printing/bioprinting
for OoCs and micro-
physiological systems
(multiple reviews and
a systematic review)

[25,26,30,47,49]

High(cid:17)throughput
organoids, organoid
engineering, and
translational
challenges

[17]

[16]

Fluidic circuit board
(FCB) for modular
OoC flow control

Round(cid:17)robin study on
extrusion bioprinting
reproducibility

Explicitly contrast tra-
ditional microfabri-
cation (photolithog-
raphy/soft lithogra-
phy: multi(cid:17)step, manu-
al, low(cid:17)throughput) with
3D printing/bioprint-
ing as more auto-
matic and potentially
one(cid:17)step digital work-
flows [28,29,31,46].

Acknowledge poten-
tial to integrate sen-
sors and to auto-
mate chip+tissue fab-
rication; some fu-
ture(cid:17)perspective sec-
tions mention AI and
advanced CAD for
modular design, but
specifics are limited.

Identify fabrication as
a main bottleneck for
reproducible OoC
production; highlight
trade(cid:17)offs in resolution
vs throughput vs cost;
emphasize lack of
standardized design
rules and modularity;
note that most current
OoC bioprinting
studies are still
proof(cid:17)of(cid:17)concept
[27,28,29,30,31,32,33,38,39].

Provide a manu-
facturing(cid:17)oriented view
of where automa-
tion already exists
(e.g., one(cid:17)step bio-
printed OoCs [31])
and where it is missing
(standardized, high-
(cid:17)throughput, sensor(cid:17)in-
tegrated mass pro-
duction).

Repeatedly con-
trast labor(cid:17)inten-
sive, variable man-
ual organoid work-
flows with emerging
automated or micro-
engineered solutions
(liquid handlers, mi-
crofluidics, bioreac-
tors) [25,26,30,47,49].

Analyzes current OoC
culture platforms as
“closed ecosystems”
that limit interoper-
ability; proposes an
open standard FCB
for modular integration
[17].

Compares outcomes
across 12 labs us-
ing standard inks/de-
vices/SOPs; reveals
large inter(cid:17)lab variabil-
ity despite formal pro-
tocols [16].

Emphasize needs
for: scalable
organoid produc-
tion, better con-
trol of size/composi-
tion/maturity, integra-
tion with HTS for-
mats (384/1536(cid:17)well),
Matrigel(cid:17)free or stan-
dardized ECMs, and
better functional read-
outs [25,26,47,49].

Identifies that plat-
form heterogene-
ity and propri-
etary hardware/soft-
ware ecosystems im-
pede scalable au-
tomation and cross(cid:17)-
platform workflows
[17].

Identifies remaining
manual steps (image
analysis, z(cid:17)height cal-
ibration), lack of ful-
ly automated equip-
ment (piston(cid:17)driven
extrusion, automat-
ed coordinate cali-
bration, temperature(cid:17)-
controlled printheads),
and the strong influ-
ence of individual op-
erators [16].

Mention AI/ML large-
ly in context of im-
age analysis and data
processing; [26] and
[47] more explicitly
call for integrated an-
alytics + automation
to enable personal-
ized medicine work-
flows.

These reviews are
valuable for connect-
ing technical automa-
tion gaps to transla-
tional use cases (drug
discovery, personal-
ized therapy), which
helps prioritize which
automation problems
matter most.

Focuses on hardware
modularity rather than
AI per se, but mod-
ular interfaces are a
prerequisite for any
self(cid:17)driving system that
orchestrates multiple
devices.

Key reference for
the “infrastructure lay-
er” of self(cid:17)driving
OoC systems—stan-
dardized interfaces
and modular compo-
nents for flow control
and sensing.

Highlights need
for process(cid:17)analytical
technologies and au-
tomation to achieve
reproducibility, sug-
gesting a role for AI
and standardized QC
pipelines.

Provides rare, quan-
titative, multi(cid:17)site ev-
idence that even
“automated” print-
ing steps are
not yet reproducible
enough—and pin-
points which substeps
most need automation
and closed(cid:17)loop QC.

High(cid:17)level synthesis:

• The reviews collectively agree that:

• Manual workflows are a major source of variability, low throughput, and limited standardization in organoids, OoCs, and

biofabrication.

• Existing automation is fragmented: task(cid:17)level tools (liquid handlers, printers, pumps) and some workflow(cid:17)level systems exist,

but end(cid:17)to(cid:17)end, interoperable pipelines are rare.

• Decision(cid:17)level automation (true closed(cid:17)loop control) is essentially absent, with [6,8] being early exceptions at very narrow

scopes.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 13/41

Undermind

REPORT CREATED ON
11/22/2025

• Across domains, they converge on key unmet needs highly aligned with self(cid:17)driving biofabrication:

•

Integrated sensing (imaging + mechanical + electrical + biochemical) at single(cid:17)organoid and multi(cid:17)tissue scales.

• Robust, automated image/signal analysis that runs in real time and can drive control decisions.

• Standardized hardware interfaces (e.g., FCB [17], standardized plate/chip formats) to coordinate printers, robots, mi-

crofluidics, and imaging.

• Formal process(cid:17)analytical technologies and SOPs to quantify and control reproducibility across sites [16,41].

These convergent findings from both experimental platforms and reviews define a coherent landscape of what has been automated
and what remains as technical whitespace for AI(cid:17)enabled, imaging(cid:17)guided, closed(cid:17)loop biofabrication systems.

Timeline

Historical Trajectory: From Conceptual Framing to Early Self(cid:17)Driving Biofabrication

1. Early Foundations (pre(cid:17)2017 to ~2018): Organoids, OoCs, Bioprinting as Separate Streams

• Early organoid and organ(cid:17)on(cid:17)chip work (not all captured here) largely focused on:
• Demonstrating biological relevance (disease models, drug response).

• Crafting microfluidic devices via soft lithography (highly manual, low standardization) [32].

• Establishing basic 3D bioprinting modalities and bioink concepts.

Within this period, a key milestone for our topic is the recognition that fabrication methods themselves are the bottleneck for scaling
OoCs and that 3D printing could relieve manual PDMS workflows:

• Yi et al. (2017) explicitly framed 3D printing as a way to move from cumbersome “two(cid:17)step” fabrication (manual placement

of tissues into prefabricated chips) to “one(cid:17)step” printing of both tissue and chip, specifically to reduce manual interventions,
contamination risk, and reproducibility issues [31]. This is one of the earliest systematic articulations of:

•

“Assembly(cid:17)free,” automated OoC fabrication as a goal.

• The idea that printing could transform OoCs from craft to manufacturable devices.

By ~2018, organoids, OoCs, and bioprinting were still largely separate streams, with automation framed as desired but not yet
embodied in integrated systems.

2. 2019–2020: Convergence and Problem Framing Around Automation and Reproducibility

Around 2019–2020, several influential reviews and early platforms crystallized the central pain points (variability, throughput, manual
handling) and began mapping explicit engineering solutions.
Key conceptual milestones:

• Organoids(cid:17)on(cid:17)chip as an engineering agenda:

• Park & Huh (Science 2019) positioned “organoids(cid:17)on(cid:17)a(cid:17)chip” as a deliberate fusion: using OoC technology to tackle

organoids’ variability, low throughput, and poor access for analysis [37]. They:

•

Identified production, control, and analysis of organoids as engineering problems.

• Explicitly highlighted needs for flow control, mechanical cues, and integrated sensing for organoids.

• Positioned organoids(cid:17)on(cid:17)chip as a platform for future automation and more deterministic control.

• Engineering organoids and automation gaps:

• Hofer & Lutolf (2021, but synthesizing ~2010s work) systematically described organoids’ key limitations—batch(cid:17)to(cid:17)batch

variability, low throughput, labour(cid:17)intensive assays—and explicitly called out:

• Need for controlled positioning/shape of organoids for inline sensing and parallel readouts.

• Need for automation of functional measurements and high(cid:17)throughput analytics.

• Bioprinting of organoids as “still in its infancy” but promising for spatial control and standardization [41].

• This review effectively defined the “engineering problem statement” that later self(cid:17)driving concepts build on.

• Bioprinting for OoC and automation:

• Miri et al. (2019) and Yi et al. (2017) together framed bioprinting as a way to:

• Replace multi(cid:17)step, manual chip fabrication with digital, single(cid:17)step printing.

•

Integrate tissues, channels, and possibly sensors in one automated process.

• Move towards automated, scalable OoC manufacturing with higher throughput and reproducibility [28,31].

• Early systematic analyses of manufacturing/standardization:

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 14/41

Undermind

REPORT CREATED ON
11/22/2025

• Puryear et al. (2020) highlighted fabrication methods as the primary bottleneck for reproducible, multifunctional OoC

devices, and explicitly called for:

• Automation and standardization of device fabrication.

• Modular CAD(cid:17)driven designs for easier assembly and interconnection [32].

• This begins the “manufacturing/standardization” thread that later leads to round(cid:17)robin and interoperability efforts.

First wave of concrete automated organoid workflows (2020):

• High(cid:17)throughput automated organoid culture:

• Brandenberg et al. (Nature Biomed. Eng. 2020) introduced high(cid:17)throughput automated organoid culture via stem(cid:17)cell

aggregation in microcavity arrays [12] (details not in the excerpt but heavily cited as a benchmark for scalable, automated
aggregation).

• Lawlor et al. (Nat. Materials 2020) replaced manual kidney organoid production with extrusion bioprinting, showing:

• Much higher throughput.

• Tight control of organoid size, starting cell number, and conformation.

• Proof(cid:17)of(cid:17)concept toxicity assays in multi(cid:17)well formats [11].

• These studies represent a transition from conceptual “bioprinting can help” to concrete, task(cid:17)level automation improving

reproducibility and throughput.

• Automated droplet/printing(cid:17)based tumor organoid platforms:

• Jiang et al. (Cell Reports Medicine 2020) built a Matrigel(cid:17)droplet templating and printing platform to generate highly uniform

tumor organoids, explicitly quantifying:

• Production rates (100–1,000 precursors <10 min).

• Spatial placement success (~95%).

• Reduced organoid(cid:17)to(cid:17)organoid variability vs manual suspensions [4].

• They also articulated technical limitations (temperature control, no robotic plate transfer, limited organoid yields per

patient), foreshadowing later discussions of full workflow automation and multi(cid:17)organoid assembly gaps.

• Fully automated midbrain organoid HTS workflow:

• Renner et al. (eLife 2020) presented a fully automated midbrain organoid pipeline (generation, maintenance, optical

analysis) in 96(cid:17)well plates [3], directly:

• Comparing automated vs manual workflows in terms of morphology, gene expression, and cellular composition.

• Demonstrating reduced intra(cid:17) and inter(cid:17)batch variability in an end(cid:17)to(cid:17)end HTS setting.

• This is one of the earliest examples of true workflow(cid:17)level automation for organoids.

Taken together, 2019–2020 marks a clear shift:

• From descriptive biology to explicit engineering problem framing (variability, throughput).

• From conceptual to implemented task(cid:17) and workflow(cid:17)level automation (microcavity arrays, droplet printing, automated HTS

organoids).

• From “bioprinting for constructs” to “bioprinting for organoid production and OoC fabrication.”

3. 2020–2022: Scaling, Platformization, and Quantitative Variability Analysis

The next phase builds on these early systems and emphasizes scaling, quantitative characterization of variability, and platform
thinking.

• ORCA and quantitative decomposition of organoid variability:

• Shah et al. (2020; ORCA) described an automated organoid culture and assay platform plus a cloud experiment manager

(Orgbook) [1]. They:

• Controlled robotic systems for longitudinal, high(cid:17)throughput culture of many cerebral organoids.

• Used machine learning to quantify sources of variability (donor, clone, batch) across multimodal readouts.

• Argued that manual pooled cultures (e.g., spinner flasks) amplify variability and prevent repeated measurements on

the same organoid.

• This is a major milestone where:

• Automation is used not only to increase throughput but also to rigorously dissect and reduce variability.

• Data/experiment(cid:17)management infrastructure (cloud, logging) is treated as first(cid:17)class, anticipating self(cid:17)driving lab

architectures.

• Extension of automated midbrain platforms and explicit AI framing:

•

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 15/41

Undermind

REPORT CREATED ON
11/22/2025

Renner et al. (2021, Movement Disorders) extended their midbrain organoid platform, introducing “automated midbrain
organoids (AMOs)” and explicitly:

• Highlighted automation barriers (Matrigel variability, ECM handling, incompatibility of many assays with HTS).

• Developed whole(cid:17)mount clearing and staining compatible with fully automated handling and 3D imaging.

• Framed AI/ML as essential to mine rich multiplexed data from automated workflows [2].

• This is a turning point where AI is framed as an intrinsic component of automated organoid pipelines, even if not yet used

for real(cid:17)time control.

• Automated microfluidic organoid culture:

• Seiler et al. (Sci. Reports 2022) implemented a 24(cid:17)plex automated microfluidic platform for cerebral organoids with

programmable flow, comparing automated versus manual feeding [10].

• RNA(cid:17)seq showed reduced glycolytic and ER stress in automated cultures.

• The platform was explicitly designed for parallelization and remote (IoT(cid:17)style) control.

• This work underscores that even relatively simple “decision(cid:17)static” automation (fixed flow schedules) can materially improve

organoid physiology.

• Platformization and interoperability in OoC:

• Vivas et al. (2021) introduced the Fluidic Circuit Board (FCB) within the “Translational Organ(cid:17)on(cid:17)Chip Platform,” an open,

well(cid:17)plate(cid:17)form(cid:17)factor interface for integrating diverse chips and components [17].

• This marks a move from “closed ecosystem” OoC platforms toward interoperable, modular workflows—an important

precursor for end(cid:17)to(cid:17)end automated or self(cid:17)driving systems.

• Manufacturing/standardization and reproducibility:

• Grijalva Garces et al. (2023) conducted a round(cid:17)robin study on extrusion bioprinting reproducibility, showing:

• Significant inter(cid:17)lab and operator effects despite standardized materials and SOPs.

• That automated image analysis is feasible but still contains manual steps.

• Explicitly calling for further equipment automation (piston(cid:17)driven extrusion, automated z(cid:17)height calibration, tempera-

ture(cid:17)controlled printheads) [16].

• This moves the field toward formal metrology and standardization frameworks, rather than only device(cid:17)specific optimiza-

tions.

The main trend over 2020–2022 is a shift from “look what automation can do” to:
“How do we quantify and reduce variability across scales and sites?”

•

•

•

“How do we build modular platforms that interoperate and scale?”

“How do we incorporate richer readouts and AI into automated workflows?”

4. 2021–2023: Conceptual Calls for AI/Intelligence and Integration Across Technologies

Around the same time, several high(cid:17)level reviews explicitly connected automation with AI and intelligence, while integrating organoids,
OoCs, and bioprinting conceptually.

• AI + organoids + OoCs:

• Ma et al. (Advanced Biology 2021) explicitly proposed integrating engineering, automation, and AI as the “missing link”

for organoid translation [15]. They:

• Outlined milestones: high(cid:17)throughput standardized production, automated manipulation, intelligent monitoring and

control.

• Positioned organoids(cid:17)on(cid:17)a(cid:17)chip as an ideal platform for these goals.

• This is one of the clearest early articulations of a roadmap toward intelligent, closed(cid:17)loop organoid systems.

• Bioprinting + AI:

• Lee (2023) and Chen et al. (2024) reviewed AI in 3D bioprinting, arguing that AI could:

• Optimize printing parameters.

• Provide real(cid:17)time monitoring and feedback for quality control.

• Enable imaging(cid:17)guided, closed(cid:17)loop printing [14,18].

• Robazzi et al. (2025) further generalized this to “AI(cid:17)enhanced 3D bioprinting” with real(cid:17)time defect detection, predictive

maintenance, and robotic CV(cid:17)guided placement [24].

• Although largely conceptual, these reviews establish:

• Core action space (printing speed, pressure, temperature).

• Sensing channels (imaging, force, process data).

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 16/41

Undermind

REPORT CREATED ON
11/22/2025

• A vocabulary of self(cid:17)monitoring and self(cid:17)correction that is directly relevant for self(cid:17)driving biofabrication.

• Bioprinting + OoC integration:

• Multiple reviews (Thakare et al. 2021; Rahmani Dabbagh et al. 2022; Carvalho et al. 2021; Rothbauer et al. 2022; Wu et
al. 2025; Kim et al. 2024) catalog bioprinting methods applied to OoCs [27(cid:17)29,33,38,39,46]. They converge on several
themes:

• Bioprinting can enable automated, digital(cid:17)to(cid:17)device fabrication of OoCs with precise microarchitecture and integrated

microchannels.

• Soft(cid:17)lithography remains labor(cid:17)intensive and hard to automate at scale [32,46].

• Major unresolved issues: limited printing resolution vs microfluidic needs, bioink constraints, integration of sensors,

and lack of high(cid:17)throughput manufacturing demonstrations [27(cid:17)29,33,46].

• These reviews crystallize the sense that we have the component technologies, but not yet the integrated, scalable,

sensor(cid:17)rich manufacturing lines needed for self(cid:17)driving systems.

• Microfluidics + organoids and automation implications:

• Duzagac et al. (2021), Liu et al. (2023), Papamichail et al. (2025), and Ferguson et al. (2025) review microfluidic organoid

platforms, repeatedly emphasizing:

• Better control of microenvironment (flow, gradients) and improved functional maturation [34(cid:17)36,50].

• Multiplexed perfusion and some examples of automated fluid handling (e.g., multiplexer(cid:17)controlled arrays, robotic

transfers between chips) [34].

• Persistent standardization/scale(cid:17)up challenges and dependence on external pumps/tubing [34(cid:17)36,50].

• These works reinforce that microfluidics is a natural substrate for automation and closed(cid:17)loop control, but practical

integration and standardization are still immature.

• Organoid engineering and mechanobiology:

• Hofer & Lutolf (2021) [41], Silva et al. (2019) [49], and later “microengineered organoids” reviews [48] summarize engi-

neering strategies (microwells, microtopography, microfluidic flow) to control organoid size, shape, and microenvironment,
but also:

• Acknowledge remaining bottlenecks in high(cid:17)throughput production, maturation, and functional assessment.

• Highlight the need for scalable, automated evaluation pipelines (imaging, electrophysiology, sensors).

During this phase, the field’s narrative shifts from “automation and bioprinting are helpful tools” to:

•

•

“We need intelligent, integrated, and sensor(cid:17)rich platforms.”

“AI and ML should be embedded in design, monitoring, and optimization.”
Yet most implementations remain either:

• Workflow automation without adaptive control, or

• AI used for offline analysis rather than real(cid:17)time feedback.

5. 2021–2024: Integrating Bioprinting, Imaging, and High(cid:17)Throughput Analytics

Concurrently, a set of more specialized platforms begin to integrate automated bioprinting with rich imaging and analytics, moving
closer to the self(cid:17)driving paradigm.

• Bioprinting + quantitative, label(cid:17)free imaging:

• Tebon et al. (2021) developed a workflow combining automated bioprinting of tumor organoids with time(cid:17)resolved

high(cid:17)speed live cell interferometry and ML(cid:17)based segmentation/classification, enabling:

• Parallel single(cid:17)organoid mass tracking for thousands of organoids.

• Detection of heterogeneous drug responses at single(cid:17)organoid resolution [9].

• They explicitly highlighted:

• The benefit of automated seeding for throughput and reproducibility versus manual methods.

• Data bottlenecks (<250 GB/plate/day) and the lack of closed(cid:17)loop intervention—analysis remains offline.

• High(cid:17)throughput microarray bioprinting and pillar/perfusion plates:

• Kang et al. (pillar/perfusion plates, 2023/2024) built a “microarray 3D bioprinting” system for organoids on pillar plates

coupled to perfusion plates, enabling:

• High(cid:17)precision, high(cid:17)throughput stem cell printing and encapsulation.

• Static and dynamic culture compatible with 384(cid:17)well HTS equipment [44,45].

• This work expands the “platformization” trend by providing a format that is:

• Bioprinter(cid:17)friendly.

• HTS(cid:17)system compatible.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 17/41

Undermind

REPORT CREATED ON
11/22/2025

• Ready for integration with automated imaging and liquid handling.

• Granular bioprinting for uniform organoid self(cid:17)organization:

• Graham et al. (2024, MAGIC matrix) developed a tunable granular biomaterial and an automated bioprinting workflow:

• Parameterized, scripted control of printhead/printbed stages and aspiration/dispensing.

• Direct comparison of manually seeded vs bioprinted organoids, with automated imaging and segmentation for

quantitative analysis [23].

• The key conceptual leap here is recognizing that:

• Tailored materials + automated, parameterized printing can create self(cid:17)organization(cid:17)friendly environments that im-

prove uniformity and morphogenesis.

• Automation is not just about placement, but about creating reproducible physical “state spaces” for self(cid:17)organization.

• Vascularized organs(cid:17)on(cid:17)chip via high(cid:17)scale bioprinting:

• Fritschen et al. (2024) presented an automated platform combining drop(cid:17)on(cid:17)demand bioprinting with robotic handling of

microfluidic chips to fabricate vascularized OoCs [5].

• They articulated chip design criteria for automation and perfusion.

• Demonstrated multi(cid:17)tissue printing on a chip in <1 minute, and the ability to process many chips consecutively without

manual intervention.

• This foreshadows self(cid:17)driving platforms for multi(cid:17)organ assembly, but still operates under pre(cid:17)programmed, open(cid:17)loop

protocols without real(cid:17)time adaptive control.

Overall, these works demonstrate:

•

Increasingly sophisticated integration of:
• Automated deposition (bioprinting).

• Standardized formats (pillar plates, perfusion chips).

• High(cid:17)content imaging and advanced analytics (including ML).

• But the “decision(cid:17)level automation” and truly closed(cid:17)loop control remain largely conceptual or limited to narrow control problems.

6. 2024–2025: Emergence of True Closed(cid:17)Loop and Robotic Micromanipulation

The most recent works in the corpus show the first concrete moves into genuine closed(cid:17)loop, feedback(cid:17)driven biofabrication and
organoid culture—bridging toward “self(cid:17)driving.”

• Closed(cid:17)loop micromanipulation for organoid patterning and assembloids:

• Tong et al. (Science Advances 2025) introduced a micromanipulation platform that:

• Uses multi(cid:17)dimensional cell sensing and real(cid:17)time feedback to adapt fluid dynamics and robustly control the spatial

distribution of multiple cell types.

• Enables programmable organoid manufacturing and construction of multi(cid:17)cell(cid:17)type assembloids [6].

• This is a clear milestone:

•

Integrating sensing, control theory, and actuation in a closed loop to achieve spatially precise, reproducible patterning
and multi(cid:17)organoid assembly.

• Directly addressing spatial control and assembloid construction—two of the key gaps you identified.

• Robotic fragment selection and in(cid:17)chip culture:

• Wang et al. (IEEE T(cid:17)ASE 2025) built a robotic micromanipulation system that:

• Automatically selects tissue fragments of specified sizes and transfers them into a custom in(cid:17)situ organoid chip with

microwell arrays.

• Uses CFD(cid:17)informed robust model predictive control (RMPC) to control transfer dynamics.

• Demonstrates significantly improved morphological homogeneity in colorectal cancer organoids [7].

• This platform pushes automation from:

• Pure liquid handling to delicate manipulation of soft, fragile biological fragments.

• Static to model(cid:17)based, feedback(cid:17)enabled control (though feedback is primarily on fluidics, not biological state).

• Long(cid:17)term personalized automated organoid culture with mechanical feedback:

• Zhu et al. (RA(cid:17)Letters 2025) present a robotic system that:

Integrates ultra(cid:17)thin membrane mechanical sensors for real(cid:17)time, in situ monitoring of organoid group mechanics
(RISM platform).

•

•

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 18/41

Undermind

REPORT CREATED ON
11/22/2025

Implements an adaptive media(cid:17)change timing policy based on sensed mechanical changes, on a long(cid:17)term automated
culture platform [8].

• This is arguably one of the first examples of:

• Decision(cid:17)level automation in organoid culture (culture schedule adapts to sensed state).

• A closed(cid:17)loop system where non(cid:17)imaging sensors directly drive operational decisions (media change timing).

• Robotic(cid:17)assisted bottom(cid:17)up assembly as a recognized subfield:

• Almeida et al. (2025) review robotic(cid:17)assisted bottom(cid:17)up tissue assembly, including:

• Robotic handling of spheroids/organoids.

• Key considerations for robotic assembly of complex tissues.

• Advantages and limitations of various robot(cid:17)assisted systems [21].

• This review consolidates “robotic micro(cid:17)assembly” as a distinct and promising direction for complex, multi(cid:17)component tissue

fabrication.

• Mature framing of AI(cid:17)for(cid:17)biofabrication:

• Zhou et al. (2024) provide a broad synthesis of AI applications in biofabrication across:

• Data extraction, structural design optimization, intelligent cell sorting, process optimization, real(cid:17)time monitoring and

evaluation [19].

• Liu et al. (2023) and Silva Robazzi et al. (2025) further emphasize computer vision, dynamic monitoring, and on(cid:17)the(cid:17)fly

defect correction in printing workflows [24,52].

• These works indicate a community consensus that:

• AI will underpin future automation at multiple levels (design, monitoring, control).

• Self(cid:17)driving biofabrication is plausible and increasingly technically grounded, though still rarely implemented end(cid:17)-

to(cid:17)end.

In parallel, additional reviews on organoids(cid:17)on(cid:17)chip, microfluidic/bioelectronic interfaces, and organoid(cid:17)bioprinting (e.g., Papamichail
et al. 2025; Li et al. 2025; Cabral et al. 2024; Ma et al. 2025) consolidate the field’s understanding of:

• Remaining challenges in standardization, long(cid:17)term culture, maturation, and multi(cid:17)organ integration [36,40,42,43].

• The centrality of automation, bioprinting, and intelligent control to overcome these barriers.

Key Trends and Patterns Across the Timeline

Trend 1: From Manual Craft to Platformized Automation

• Early work: device(cid:17) and protocol(cid:17)centric, manual, with low throughput and high variability.

• Mid(cid:17)phase (2019–2022): emergence of:

• Automated unit operations (bioprinting, microcavity aggregation, microfluidic perfusion) [11(cid:17)12,10].

• End(cid:17)to(cid:17)end automated pipelines for specific organoid types (midbrain, cerebral) [1,3].

• Recent work (2023–2025): platformized systems:

• Standard formats (pillar plates, FCB, modular chips) [17,44].

• Robotic handling and chip assembly [5,21].

•

Increasing use of cloud/IoT orchestration [1,10,17].

Implication: The field is moving from bespoke automation toward modular, interoperable platforms that could be orchestrated by
higher(cid:17)level “self(cid:17)driving” experiment managers.

Trend 2: Increasingly Rich Sensing and Analytics, from Size to High(cid:17)Dimensional Phenotypes

• Early metrics: organoid size, viability, morphology.

• 2020–2022: integration of:

• RNA(cid:17)seq and single(cid:17)cell RNA(cid:17)seq to quantify variability and maturation [1,3,11].

• Whole(cid:17)mount high(cid:17)content 3D imaging with automated analysis [2,3].

• 2021–2024: advanced, often label(cid:17)free imaging:

• Quantitative phase interferometry (HSLCI) with ML(cid:17)based segmentation [9].

• High(cid:17)throughput time(cid:17)lapse brightfield/fluorescence with custom pipelines [23,44].

• 2025: non(cid:17)imaging sensors for real(cid:17)time mechanical monitoring [8] and integrated microfluidic/bioelectronic sensing [50].

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 19/41

Undermind

REPORT CREATED ON
11/22/2025

Implication: The state space for control is becoming richer and more quantitative, making AI(cid:17)based closed(cid:17)loop control increasingly
feasible.

Trend 3: From Open(cid:17)Loop Automation to Closed(cid:17)Loop, Decision(cid:17)Level Control

• 2019–2022: Automation largely open(cid:17)loop:

• Pre(cid:17)programmed protocols (fixed feeding schedules, fixed printing patterns).

• AI/ML used mainly for offline analysis (phenotyping, variability decomposition) [1(cid:17)3,9].

• 2023–2025: First closed(cid:17)loop systems:

• Real(cid:17)time feedback to compensate fluidic perturbations and maintain spatial cell distributions during micromanipulation

[6].

• CFD(cid:17)informed RMPC to control fragment transfer [7].

• Mechanical feedback to adapt media change timing [8].

• Reviews in the same period argue for:

• AI(cid:17)driven real(cid:17)time monitoring, error correction, and parameter optimization [14,18,19,24,52].

Implication: The field is just beginning to move into true control(cid:17)theoretic territory, with localized examples of state(cid:17)dependent decision
making. Fully self(cid:17)driving, multi(cid:17)device, multi(cid:17)day workflows remain an open frontier.

Trend 4: Multi(cid:17)Organoid Assembly and Spatially Precise Biofabrication

• Early organoids: self(cid:17)assembled with minimal spatial control.

• Engineering efforts: microwells, micropatterned scaffolds, and microtopography for size and shape control [41,48,49].

• Bioprinting platforms: improved spatial control over cell placement and organoid deposition [4,11,23,40,42,43].

• Recent closed(cid:17)loop micromanipulation: programmable assembly of multi(cid:17)cell(cid:17)type organoids and assembloids with real(cid:17)time

feedback [6].

• Bioprinted multi(cid:17)tissue OoCs and vascularized chips [5,46].

Implication: There is a clear progression from uncontrolled self(cid:17)organization to deterministic spatial assembly, culminating in
robot(cid:17)assisted, feedback(cid:17)controlled assembloid construction—a key requirement for advanced self(cid:17)driving biofabrication.

Trend 5: Standardization, Interoperability, and Community(cid:17)Level Reproducibility

• Recognition that manual fabrication and operator effects limit reproducibility [31,32,41].

• Development of:

• Open hardware standards (TOP/FCB) [17].

• Standardized bioprinting assays and cross(cid:17)lab reproducibility studies [16].

• Plate(cid:17)compatible organoid and OoC formats (pillar plates, 96(cid:17)well organoids, FCB form factor) [3,4,17,44].

• Growing emphasis on SOPs, process(cid:17)analytical technologies, and structured data logging [1,16,19].

Implication: The infrastructure necessary for reproducible, multi(cid:17)site, AI(cid:17)driven experimentation is slowly emerging, but harmonization
across organoid, OoC, and bioprinting platforms is still incomplete.

Key Collaborator Clusters and Their Contributions

Several recurring groups anchor the field’s progression and suggest where future innovation is likely:

• Lutolf/Hofer and collaborators:

• High(cid:17)throughput organoid culture (microcavity arrays) [12].

• Conceptual framework “Engineering organoids” that articulates key automation and standardization needs [41].

• Their work consistently pushes toward controlled self(cid:17)organization and microengineering solutions.

• Bruder/Renner group:

• Pioneers of fully automated HTS(cid:17)compatible midbrain organoid workflows [3].

• Extension to disease(cid:17)focused automated pipelines with explicit AI(cid:17)analysis framing [2].

• Likely to remain central for large(cid:17)scale, automated neural organoid platforms with rich phenotyping.

• Ma/Shaohua and co(cid:17)authors:

• Automated tumor organoid droplet printing platform [4].

• High(cid:17)level roadmap integrating engineering, automation, and intelligence for organoids [15].

• Their work exemplifies the integration of concrete automated hardware with conceptual thinking about intelligent organoid

systems.

• Gao and collaborators (Tong, Wang, Zhu):

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 20/41

Undermind

REPORT CREATED ON
11/22/2025

• Robotic micromanipulation for homogeneous organoid culture and assembloid construction with closed(cid:17)loop control [6,7].

• Personalized, sensor(cid:17)driven automated organoid culture [8].

• This cluster is at the forefront of robotic, control(cid:17)theoretic approaches for organoid handling—highly relevant to self(cid:17)driving

lab concepts.

• van der Meer and colleagues:

•

Interoperable organ(cid:17)on(cid:17)chip flow(cid:17)control hardware (TOP/FCB) [17].

• Recent reviews on organoids(cid:17)on(cid:17)chip and current limitations/challenges [36].

• This group drives standardization and modularity in OoC platforms, a prerequisite for large(cid:17)scale automated integration.

• Bioprinting/OoC integration community (Khademhosseini/Qin/Tasoglu/Cho, etc.):

• Systematic reviews of bioprinting for OoCs and 3D(cid:17)printed microdevices [27(cid:17)29,31,38,39,46].

• Highlighting hybrid “one(cid:17)step” approaches and the need for sensor integration and high(cid:17)throughput manufacturing.

• These groups shape how bioprinting will be deployed as a manufacturable route for OoCs.

• AI(cid:17)for(cid:17)biofabrication reviewers (Zhou, Lee, Chen, Robazzi, Liu, Cabral, Ma 2025):

• Codifying the space of AI applications in biofabrication and 3D bioprinting [14,18,19,24,40,42,52].

• Proposing AI(cid:17)enabled monitoring, defect prediction, and control strategies.

These clusters suggest that the most likely near(cid:17)term advances in self(cid:17)driving biofabrication will come from:

• Cross(cid:17)pollination between robotic/control groups (Gao), organoid automation groups (Bruder, Shah, Ma), and bioprinting/OoC

integration groups (Khademhosseini/Qin/Tasoglu/Cho, Blaeser).

• Stronger integration of AI/ML teams with hardware(cid:17)rich labs already operating automated platforms.

Overall Perspective on the State and Future Trajectory

Putting the timeline together:

• The field has progressed through:

1. Conceptual recognition of organoids, OoCs, and bioprinting as separate but complementary technologies.

1. Explicit engineering problem framing around variability, throughput, and manual handling.

1. First(cid:17)generation automated organoid and OoC platforms with improved reproducibility and throughput.

1. Platformization and standardization efforts to increase interoperability and reproducibility.

1. Conceptual embedding of AI and intelligence into biofabrication workflows.

1. Initial realizations of closed(cid:17)loop, feedback(cid:17)driven robotic systems for organoid handling and culture.

• However, fully self(cid:17)driving biofabrication systems that:

•

Integrate organoid, OoC, and bioprinting workflows.

• Use rich, real(cid:17)time imaging and sensor data.

• Employ AI to adapt protocols over multi(cid:17)day experiments.

• Coordinate multiple devices (printers, robots, microfluidics, microscopes) in a single feedback loop.

are not yet realized in the literature surveyed.

This historical trajectory strongly suggests that the key scientific and technical whitespace now lies in:

• End(cid:17)to(cid:17)end orchestration:

• Connecting existing automated modules (organoid HTS, bioprinting, OoCs, imaging, microfluidics) into unified, soft-

ware(cid:17)orchestrated pipelines with common data models.

• Real(cid:17)time AI(cid:17)driven control:

• Moving from static, rule(cid:17)based automation to reinforcement learning or model(cid:17)based control agents that operate on real(cid:17)time

imaging and sensor streams.

• Multi(cid:17)organoid/multi(cid:17)organ assembly and coupling:

• Extending closed(cid:17)loop micromanipulation to multi(cid:17)organ networks on(cid:17)chip, with adaptive perfusion and stimulation.

• Standardized, open interfaces:

• Building on efforts like TOP/FCB [17] and round(cid:17)robin studies [16] to define interoperable hardware/software standards

suited to self(cid:17)driving biofabrication.

The existing body of work provides a rich set of technical building blocks and conceptual frameworks; the next phase will likely be
defined by how effectively these components are integrated into truly self(cid:17)driving, imaging(cid:17)guided, AI(cid:17)controlled biofabrication systems.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 21/41

Undermind

REPORT CREATED ON
11/22/2025

Foundational Work

Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the reference
rate, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be
familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but
provide important context.

Ref.

[6]

[141]

[4]

[11]

[41]

[142]

[143]

[144]

[109]

[37]

[145]

[146]

[12]

[120]

[133]

[147]

[148]

[149]

[108]

[98]

Reference
Rate

Title

Cited By These Relevant Papers

0.45

0.30

0.19

0.17

0.16

0.14

0.13

0.12

0.11

0.11

0.11

0.10

0.10

0.10

0.10

0.10

0.09

0.09

0.09

0.08

Robotic micromanipulation for patterned and complex organoid biofab-
rication

Imaging-guided deep tissue in vivo sound printing.

[8]

[6]

An Automated Organoid Platform with Inter-organoid Homogeneity and
Inter-patient Heterogeneity

[6, 7, 8, 15, 22, 23, 25]

Cellular extrusion bioprinting improves kidney organoid reproducibility
and conformation.

[6, 7, 8, 14, 22, 23, 40]

Engineering organoids

Organogenesis in a dish: Modeling development and disease using
organoid technologies

Progress and potential in organoid research

Multisensor-integrated organs-on-chips platform for automated and
continual in situ monitoring of organoid behaviors

[6, 7, 10, 14, 15, 36]

[3, 4, 7, 12, 14, 15, 37]

[2, 6, 10, 36, 37, 41]

[4, 10, 15, 28, 37]

One-step fabrication of an organ-on-a-chip with spatial heterogeneity
using a 3D bioprinting technology.

[14, 27, 28, 31, 33]

Organoids-on-a-chip

[4, 15, 36, 40, 41]

Hydrogel-in-hydrogel live bioprinting for guidance and control of
organoids and organotypic cultures

[21, 23]

Flow-enhanced vascularization and maturation of kidney organoids in
vitro

[22, 34, 36, 37, 41]

High-throughput automated organoid culture via stem-cell aggregation
in microcavity arrays

[6, 7, 15, 23, 41]

Bioprinting 3D microfibrous scaffolds for engineering endothelialized
myocardium and heart-on-a-chip.

[22, 27, 28, 33]

Single Lgr5 stem cells build crypt–villus structures in vitro without a
mesenchymal niche

[3, 4, 7, 12, 15]

Organoids

[21, 22]

3D bioprinting of high cell-density heterogeneous tissue models through
spheroid fusion within self-healing hydrogels

[7, 21, 22, 23, 41]

Creation of bladder assembloids mimicking tissue regeneration and
cancer

[6, 15, 22]

Tissue geometry drives deterministic organoid patterning

[6, 23]

Vascularized Liver Organoids Generated Using Induced Hepatic Tissue
and Dynamic Liver(cid:16)Specific Microenvironment as a Drug Testing Platform

[4, 34, 37, 41]

Adjacent Work

Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas
for useful new research directions.

Ref.

Adjacency
score

Title

References These Foundational Papers

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 22/41

Undermind

REPORT CREATED ON
11/22/2025

[73]

1.92

Bridging the organoid translational gap: integrating standardization and
micropatterning for drug screening in clinical and pharmaceutical med-
icine

[4, 11, 12, 37, 41, 124, 133]

[84]

[166]

[167]

[168]

[169]

[170]

[171]

[60]

[119]

[63]

[172]

[173]

[174]

[175]

[176]

[177]

[178]

[179]

[180]

1.82

1.56

1.54

1.30

1.23

1.16

1.13

1.12

1.09

1.05

1.00

0.99

0.99

0.98

0.98

0.98

0.98

0.98

0.98

Strategies to overcome the limitations of current organoid technology -
engineered organoids

[3, 4, 12, 37, 41]

Osteochondral organoid biofabrication: construction strategies, appli-
cations and perspectives

[4, 5, 11]

Advances in 3D Bioprinting and Microfluidics for Organ-on-a-Chip Plat-
forms

[5, 27]

Soft Micromanipulation Robot for Real-Time Adaptive Multimodal Op-
eration.

Artificial Human Blood Vessels for Tissue Engineering

Bioprinting for drug screening: A path toward reducing animal testing or
redefining preclinical research?

[5, 12]

[5, 14]

[5, 11]

Advanced Biomanufacturing Technologies for Micro-physiological Sys-
tems

[4, 12, 31]

Recent advances and challenges in organoid-on-a-chip technology

[12, 37, 41]

Development and Applications of Organoids in Gynecological Diseases [34, 37, 133, 149, 151]

3D organ-on-a-chip: The convergence of microphysiological systems
and organoids

[3, 11, 120, 143]

Materiobiology in the omics era

Liver-on-a-chip: Considerations, advances, and beyond.

[6]

[27, 28]

Improving tumor microenvironment assessment in chip systems through
next-generation technology integration

Microfluidic informatics - A research paradigm for the future of microflu-
idics.

Synergies Between Robotics, AI, and Bioengineering—A Narrative Re-
view Concerning the Future of Transplants

Cell-instructive microfibers enable programmable alignment of bioprint-
ed hMSC

Exploring the 3D Bioprinting Landscape in the Delivery of Active Phar-
maceutical Compounds for Therapeutic and Regenerative Medicine
Applications.

A pump-free dual unidirectional circulation microfluidic device for tumor
spheroid microenvironment modulation and motility analysis

Functional substrate-enhanced bioprinting technology for next-genera-
tion organ-on-a-chip: from fabrication to functionalization.

[5]

[5]

[5]

[5]

[5]

[5]

[5]

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 23/41

Undermind

REPORT CREATED ON
11/22/2025

References

[1] Optimization and scaling of patient-derived brain organoids uncovers deep phenotypes of disease

K. Shah, ..., and G. S. Escola. bioRxiv, 2020. 8 citations.
100% Topic Match
Demonstrates an automated, scalable organoid culture and assay (ORCA) system.
Implements robotic handling + cloud experiment manager (Orgbook), high-throughput 96(cid:17)well culture, and ML analyses to quantify donor/clone/batch variability and
optimize protocols.
Relevant: explicitly compares automated vs manual/pooled culture effects on variability, reports reduced variability, high reproducibility, and enables longitudinal
multimodal phenotyping—useful for closed-loop/self-driving biofabrication needs.

[2] Combining Automated Organoid Workflows with Artificial Intelligence(cid:16)Based Analyses: Opportunities to Build a New Generation of Interdisciplinary
High(cid:16)Throughput Screens for Parkinson's Disease and Beyond

Henrik Renner, ..., and J. Bruder. Movement Disorders, 2021. 27 citations.
100% Topic Match
Demonstrates an end-to-end, HTS-compatible automated workflow for human midbrain organoids.
Implements 96(cid:17)well “automated midbrain organoids (AMOs)”, integrates automated generation, maintenance, whole(cid:17)mount clearing/staining, and high(cid:17)content 3D
imaging; reports low inter/intra(cid:17)batch morphological and cellular variation.
Notes explicit automation gaps (ECM viscosity/temperature issues for liquid handlers, incompatibility of deep assays with scale), imaging limits without clearing,
and positions AI/ML for mining rich multiplexed datasets but calls for richer, scalable phenotyping for closed(cid:17)loop control.

[3] A fully automated high-throughput workflow for 3D-based chemical screening in human midbrain organoids

Henrik Renner, ..., and J. Bruder. eLife, 2020. 155 citations.
100% Topic Match
Demonstrates a fully automated, high(cid:17)throughput workflow for midbrain organoid generation and analysis.
Implements end-to-end automation (96(cid:17)well format): organoid formation, maintenance, automated imaging, high-content analysis, and RNA(cid:17)seq-based QC to improve
reproducibility.
Relevant: explicitly compares automated vs manual variability (reports improved intra/inter(cid:17)batch reproducibility), focuses on throughput and standardized 96(cid:17)well
operations, but does not address spatial placement/multi(cid:17)organoid assembly or closed(cid:17)loop AI control.

[4] An Automated Organoid Platform with Inter-organoid Homogeneity and Inter-patient Heterogeneity

Shengwei Jiang, ..., and Shaohua Ma. Cell Reports Medicine, 2020. 122 citations.
100% Topic Match
Demonstrates an automated, high-throughput organoid production and printing platform.
Templates cell-laden Matrigel droplets and prints ~100–1,000 organoid precursors in <10 min (H1 organoid/sec), yielding monodisperse size/shape and preserved
inter-patient heterogeneity (RNA-seq, histology, drug-response).
Explicitly compares manual vs automated limits, reports ~95% placement success (failures from Matrigel temperature), lists gaps: manual plate transfer, limited
yield per clinical sample, serum-induced artifacts, and no real-time sensing, AI control, organ(cid:17)on(cid:17)chip integration, or multi(cid:17)organoid assembly workflows.

[5] High(cid:16)Scale 3D(cid:16)Bioprinting Platform for the Automated Production of Vascularized Organs(cid:16)on(cid:16)a(cid:16)Chip

Anna Fritschen, ..., and A. Blaeser. Advanced Healthcare Materials, 2024. 19 citations.
100% Topic Match
Demonstrates an integrated, automated drop(cid:17)on(cid:17)demand bioprinting + robotic handling platform for vascularized organs(cid:17)on(cid:17)a(cid:17)chip.
Implements a post(cid:17)printing sealable microfluidic chip compatible with multiple 3D printers, robotic placement/loading, and perfusion; prints three tissue regions per
chip in ~1 min and runs consecutive chips without manual intervention.
Reports a multicellular vascularized liver carcinoma model with stable microvasculature and functional readouts (albumin, HepG2 growth) over 14 days; discusses
automation gaps, chip design criteria, scalability, and need for sensors/robotic frameworks relevant to closed(cid:17)loop, high(cid:17)throughput biofabrication.

[6] Robotic micromanipulation for patterned and complex organoid biofabrication

Mingsi Tong, ..., and Huijun Gao. Science Advances, 2025. 2 citations.
100% Topic Match
Demonstrates a closed-loop robotic micromanipulation platform for patterned organoid biofabrication.
Implements multidimensional cell-sensing and adaptive fluid-dynamics control to constrain cell distributions and compensate seeding-induced nonlinear perturba-
tions in real time.
Relevant: explicitly compares automated, feedback-driven placement vs manual variability (claims improved consistency), demonstrates multi-cell-type assembloid
assembly and programmable manufacturing — key for spatial control and multi-organoid assembly; check paper for quantitative throughput, reproducibility metrics,
integration with imaging pipelines, and extent of workflow-level automation.

[7] A Robotic Micromanipulation System for Homogeneous Organoid Culture

Xiaofei Wang, ..., and Huijun Gao. IEEE Transactions on Automation Science and Engineering, 2025. 4 citations.
100% Topic Match
Demonstrates a robotic micromanipulation system to produce more homogeneous organoid cultures.
Uses fragment selection + automated transfer into a microwell in-situ organoid chip (IOC), with CFD-based transfer modeling and a robust model-predictive controller;
validated in simulation and colorectal cancer organoid experiments.
Relevant because it compares an automated handling step to manual frag ment transfer, quantifies improved morphological homogeneity and reproducibility,
 and addresses spatial placement into microwells—but does not claim full workflow integration, closed-loop imaging control, or multi-organoid assembly beyond
 single-fragment placement

[8] A Robotic System for Long-Term Personalized Automated Cultivation of Colorectal Cancer Organoids

Yibo Zhu, ..., and Songlin Zhuang. IEEE Robotics and Automation Letters, 2025. 0 citations.
100% Topic Match
Demonstrates an automated robotic system for personalized, adaptive organoid culture.
Integrates real-time in-situ mechanical sensing (ultra-thin membrane RISM) with a long-term automated culture (LTAC) that adaptively times media changes for
colorectal cancer organoids.
Relevant because it moves beyond static protocols toward decision-level automation/closed-loop control (mechanical-sensor ’ actuation); check for details on
throughput, reproducibility metrics, imaging integration, multi-organoid assembly, and whether adaptation uses ML or simple heuristic rules.

[9] Drug screening at single-organoid resolution via bioprinting and interferometry

Peyton J. Tebon, ..., and A. Soragni. Nature Communications, 2021. 95 citations.
100% Topic Match
Demonstrates an automated pipeline combining bioprinting with label-free, time-resolved interferometric imaging.
Implements automated organoid seeding by bioprinting, HSLCI quantitative-phase imaging, and ML-based segmentation/tracking to measure dry biomass of
thousands of individual tumor organoids.
Relevant because it compares automated seeding vs manual variability, quantifies throughput/reproducibility gains, notes limits (single z-plane imaging, 6(cid:17)hour
imaging delay, huge data volumes, offline analysis) and does not implement closed(cid:17)loop or real(cid:17)time control.

[10] Modular automated microfluidic cell culture platform reduces glycolytic stress in cerebral cortex organoids

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 24/41

Undermind

REPORT CREATED ON
11/22/2025

Spencer T. Seiler, ..., and M. Teodorescu. Scientific Reports, 2022. 31 citations.
100% Topic Match
Demonstrates a multiplex automated microfluidic platform for long-term organoid culture.
Builds a 24-plex PDMS chip with programmable perfusion (user-defined flow rates, multiple reagent reservoirs) and integrates stationary longitudinal imaging.
Shows automated perfusion reduces glycolytic/ER stress versus conventional/manual culture (RNA(cid:17)seq); does not address spatial placement, robotic assembly,
closed(cid:17)loop AI control, or bioprinting.

[11] Cellular extrusion bioprinting improves kidney organoid reproducibility and conformation.

K. Lawlor, ..., and M. Little. Nature materials, 2020. 322 citations.
100% Topic Match
Demonstrates automated extrusion bioprinting replacing manual kidney organoid generation.
Uses syringe-based cellular extrusion to print 6(cid:17) and 96(cid:17)well organoids with controlled cell number, size, conformation; includes imaging, image-analysis and
scRNA-seq validation.
Relevant: directly compares manual vs automated workflows, reports gains in throughput, reproducibility and spatial conformation control, and shows task-level
automation but not full closed-loop/AI decision-level control.

[12] High-throughput automated organoid culture via stem-cell aggregation in microcavity arrays

N. Brandenberg, ..., and M. Lutolf. Nature Biomedical Engineering, 2020. 309 citations.
100% Topic Match
No summary or abstract available

[13] Automation of Organoid Cultures: Current Protocols and Applications

Alexandra Louey, ..., and Maciej S Daniszewski. SLAS Discovery, 2021. 21 citations.
100% Topic Match
Reviews automated organoid culture workflows and applications.
Surveys current automation tools (liquid handlers, plate-stackers, imaging) and examples in cerebral/retinal organoid pipelines.
Notes gaps: need for scalable, reproducible large(cid:17)scale generation; discusses automation benefits but limited detailed comparison of manual vs fully closed(cid:17)loop AI
control.

[14] Engineering In vitro Models: Bioprinting of Organoids with Artificial Intelligence

Hyungseok Lee. Cyborg and Bionic Systems, 2023. 61 citations.
100% Topic Match
Proposes combining bioprinting and AI to standardize and automate organoid fabrication.
Reviews bioprinting modalities, highlights extrusion use, lists bottlenecks (resolution, bioink shear, vascularization), and suggests AI for real-time monitoring/feed-
back.
Paper is a conceptual/review piece (few integrated studies); it does not provide empirical closed-loop systems or quantitative comparisons of manual vs automated
workflows.

[15] Integrating Engineering, Automation, and Intelligence to Catalyze the Biomedical Translation of Organoids

Shaohua Ma, ..., and Edgar A. Galan. Advanced Biology, 2021. 10 citations.
99% Topic Match
Proposes integrating engineering, automation, and AI to accelerate organoid translation.
Argues organoids-on-chip plus on(cid:17)chip instrumentation and AI enable high(cid:17)throughput, standardized production, automated manipulation, and intelligent monitor-
ing/control.
Conceptual/review perspective (2021); outlines vision and unmet needs (throughput, reproducibility, automation gaps) but lacks quantitative comparisons or
implemented closed(cid:17)loop systems.

[16] On the reproducibility of extrusion-based bioprinting: round robin study on standardization in the field

David Grijalva Garces, ..., and J. Hubbuch. Biofabrication, 2023. 18 citations.
99% Topic Match
Demonstrates a multi-site round-robin evaluation of reproducibility in extrusion-based bioprinting.
Standardized consumables, SOPs and a prototype imaging device distributed to 12 labs; prints (cell(cid:17)free polymer inks) analyzed via automated image analysis by
three groups to quantify geometric variability.
Finds substantial inter(cid:17)lab and operator-dependent variability despite SOPs; highlights missing equipment automation (piston-driven extrusion, automated z(cid:17)calibra-
tion, temp(cid:17)controlled printheads), manual IA steps, and lack of cell-inclusive analytics — directly relevant to automation gaps, throughput/reproducibility limits, and
needs for process control in closed(cid:17)loop biofabrication.

[17] Fluidic circuit board with modular sensor and valves enables stand-alone, tubeless microfluidic flow control in organs-on-chips

Aisen Vivas, ..., and A. D. van der Meer. Lab on a Chip, 2021. 15 citations.
99% Topic Match
Demonstrates a modular fluidic circuit board (FCB) enabling stand(cid:17)alone, tubeless flow control for organs(cid:17)on(cid:17)chips.
Builds an open(cid:17)format microfluidic plate that integrates commercial/in(cid:17)house sensors, valves, and chips to deliver constant and pulsatile recirculation.
Relevant for automation/throughput gaps: focuses on hardware interoperability and closed systems avoidance, but does not present closed(cid:17)loop AI/image(cid:17)guided
control or characterization of reproducibility, spatial placement, or multi(cid:17)organoid assembly.

[18] Recent advances and applications of artificial intelligence in 3D bioprinting.
Hongyi Chen, ..., and Jie Huang. Biophysics reviews, 2024. 25 citations.
99% Topic Match
Reviews AI applications across stages of 3D bioprinting.
Summarizes uses in image reconstruction, bioink selection, and printing-process optimization with ML and classical AI.
Broad review: discusses potential for AI-enabled improvements but lacks detailed workflow comparisons (manual vs automated), quantitative gaps in throughput/re-
producibility/spatial control, or concrete closed(cid:17)loop system implementations.

[19] AI for biofabrication

Chang Zhou, ..., and Wei Sun. Biofabrication, 2024. 5 citations.
99% Topic Match
Reviews AI applications across biofabrication processes.
Surveys uses of AI for data analysis, design/optimization, cell sorting, biomaterial/process tuning, and real-time monitoring.
High-level review focused on AI opportunities; lacks detailed comparisons of manual vs automated workflows, quantitative gaps in throughput/reproducibility, or
concrete closed-loop implementations.

[20] 3D bioprinting and label-free imaging: Bridging innovations for organoid research

Linbin Zha, ..., and Byullee Park. International Journal of Bioprinting, 2024. 1 citations.
98% Topic Match
Reviews integration of 3D bioprinting with label-free imaging for organoid research.
Summarizes how bioprinting provides spatial control/scalability and label-free imaging enables non(cid:17)invasive longitudinal monitoring.
Mostly a review: discusses advantages for reproducibility and monitoring but likely lacks quantitative comparisons of manual vs automated workflows, explicit
throughput metrics, or closed(cid:17)loop/AI control demonstrations.

[21] The Future of Automated Tissue Engineering: Robotic(cid:16)Assisted Strategies for Complex 3D Tissue Bottom(cid:16)Up Assembly

Ana Margarida Almeida, ..., and J. Mano. Advanced Materials Technologies, 2025. 1 citations.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 25/41

Undermind

REPORT CREATED ON
11/22/2025

98% Topic Match
Reviews robot-assisted, bottom-up 3D tissue assembly strategies.
Surveys robotic handling methods, compares advantages/limitations, and discusses key considerations for complex tissue assembly.
Review-level (2025); focuses on robotic assembly rather than organoids/OoC specifically—useful for spatial-control and automation-gap insights but may lack
quantitative throughput/reproducibility metrics or explicit closed-loop/AI integration examples.

[22] Integrating 3D Bioprinting and Organoids to Better Recapitulate the Complexity of Cellular Microenvironments for Tissue Engineering

Yan Hu, ..., and Haijun Cui. Advanced Healthcare Materials, 2024. 18 citations.
98% Topic Match
Reviews integration of 3D bioprinting with organoids to improve microenvironment complexity.
Summarizes bioprinting methods/materials, advantages (high cell density, precise deposition, automation/high-throughput) and recent studies.
Notes current limitations and future prospects are discussed, but likely a high-level review — may lack quantitative comparisons of manual vs automated workflows
or concrete automation gaps for closed-loop control.

[23] Stress relaxing granular bioprinting materials enable complex and uniform organoid self-organization

Austin J. Graham, ..., and Zev J. Gartner. bioRxiv, 2024. 1 citations.
97% Topic Match
Demonstrates a tunable, stress(cid:17)relaxing granular bioink (MAGIC) enabling high(cid:17)fidelity bioprinting and optimized organoid self(cid:17)organization.
Builds a two(cid:17)temperature material (4 °C yield(cid:17)stress for printing; 37 °C crosslinking for adjustable viscoelasticity), implements scripted/parameterized automated
bioprinting (motor stages, calibrated plate geometry, aspirate/extrude routines), and compares printed vs manually seeded organoids with automated imaging and
quantitative analysis.
Relevant points for automation/whitespace: includes an automated bioprinting workflow and high(cid:17)throughput imaging but focuses on bioink material properties
and morphogenesis; discusses automation at task/workflow level (print calibration, scripted aspiration/extrusion) but does not appear to implement closed(cid:17)loop
imaging(cid:17)guided control or decision(cid:17)level automation for adaptive protocols.

[24] The Synergy of Artificial Intelligence and 3D Bioprinting: Unlocking New Frontiers in Precision and Tissue Fabrication.

João Vítor Silva Robazzi, ..., and I. Ozbolat. Advanced functional materials, 2025. 0 citations.
97% Topic Match
Reviews AI-enabled enhancements to 3D bioprinting (precision, QC, scalability).
Synthesizes literature on ML/CV/robotics for real-time monitoring, parameter optimization, error correction, and predictive maintenance.
Review-level treatment: discusses opportunities and challenges but lacks experimental comparisons of manual vs automated workflows, quantitative gaps in
throughput/reproducibility, or closed-loop implementation details.

[25] High-throughput solutions in tumor organoids: from culture to drug screening

Jianing Zuo, ..., and Shanshan Liang. Stem Cells, 2024. 8 citations.
96% Topic Match
Reviews high-throughput solutions across tumor-organoid workflows.
Surveys technologies for sampling, single-cell prep, automated culture, and drug screening to enable scalable, automated pipelines.
Useful for workflow-level overview of automation gaps, but likely a technology-review—check for explicit manual vs automated comparisons, quantitative through-
put/reproducibility metrics, and discussion of closed-loop or imaging-guided control.

[26] Integrative Approaches for Advancing Organoid Engineering: From Mechanobiology to Personalized Therapeutics

Zarif Bin Akhtar and Anik Das Gupta. Journal of Applied Artificial Intelligence, 2024. 15 citations.
96% Topic Match
Surveys integrative organoid/OoC engineering and automation opportunities.
Reviews mechanobiology, acoustofluidics, biosensor-equipped chips, bioreactors, and cited automation examples (digital microfluidics, microfluidic selection).
Notes many automation/closed(cid:17)loop gaps (batch variability, maturation, vascularization, sensor integration) but gives no quantitative throughput/reproducibility/spa-
tial(cid:17)control metrics or direct manual vs automated workflow comparisons.

[27] Bioprinting of Organ-on-Chip Systems: A Literature Review from a Manufacturing Perspective

Ketan Thakare, ..., and Hongmin Qin. Journal of Manufacturing and Materials Processing, 2021. 22 citations.
96% Topic Match
Reviews bioprinting for automated, assembly-free organ-on-chip manufacturing.
Surveys 22 studies, compares extrusion/inkjet/SLA parameters, bioink trade-offs, resolution/throughput and scalability limits.
Relevant: manufacturing-focused; highlights gaps (multimaterial, sensors, high-throughput, integration); most studies are proof-of-concept, not closed-loop or
AI-guided.

[28] Bioprinters for organs-on-chips

A. Miri, ..., and A. Khademhosseini. Biofabrication, 2019. 71 citations.
94% Topic Match
Reviews bioprinting methods for organ-on-chip fabrication (nozzle- vs optical-based).
Summarizes resolution, fidelity, time, cost; discusses integrating microfluidics, sensors, and one-step digital-to-construct workflows.
Relevant as a technology-level survey noting automation potential and challenges (assembly, shear stress, scaffold needs), but lacks quantitative metrics or explicit
comparisons of manual vs automated workflows and no closed(cid:17)loop/AI control data.

[29] 3D bioprinted organ(cid:16)on(cid:16)chips

Sajjad Rahmani Dabbagh, ..., and S. Tasoglu. Aggregate, 2022. 69 citations.
93% Topic Match
Reviews 3D bioprinting applied to organ(cid:17)on(cid:17)chip platforms.
Surveys bioprinting methods, bioinks, organ examples, and OOC features (perfusion, sensors), and discusses challenges/future directions.
Relevant for technology landscape and method limitations but lacks quantitative metrics, workflow-level manual vs automated comparisons, and any
closed(cid:17)loop/AI/imaging(cid:17)guided control analysis.

[30] Tackling Current Biomedical Challenges With Frontier Biofabrication and Organ-On-A-Chip Technologies
Nehar Celikkin, ..., and M. Costantini. Frontiers in Bioengineering and Biotechnology, 2021. 15 citations.
92% Topic Match
Reviews biofabrication and organ-on-chip technologies and their biomedical applications.
Summarizes capabilities, limitations, and a comparative multi-feature chart (including operator dependency, precision, throughput).
Notes automation potential (claims automated generation with high precision/repeatability), lists shared limitations and translational gaps, and briefly speculates on
AI/big-data integration but offers no empirical automation or closed-loop implementation details.

[31] 3D Printing of Organs-On-Chips

H. Yi, ..., and D. Cho. Bioengineering, 2017. 161 citations.
92% Topic Match
Reviews 3D bioprinting integration into organ-on-chip fabrication.
Surveys two-step vs one-step printing, modalities, bioinks, and functional printed OoC examples.
Notes manual steps in two-step workflows hinder automation/reproducibility; argues one-step printing aids scale but lacks quantitative throughput, closed-loop, or
AI-control analysis.

[32] Advanced Fabrication Techniques of Microengineered Physiological Systems
Joseph R Puryear Iii, ..., and YongTae Kim. Micromachines, 2020. 28 citations.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 26/41

Undermind

REPORT CREATED ON
11/22/2025

88% Topic Match
Reviews fabrication methods for organs-on-chips, highlighting bottlenecks for reproducible, multiscale device production.
Compares photolithography, laser, soft lithography, 3D printing, and injection molding; identifies soft lithography dominance and limitations, and 3D printing/molding
promise.
Flags unmet needs directly relevant to automation/closed-loop systems: standardized/automated fabrication workflows, modular CAD-enabled assemblies,
embedded sensors/stimuli, and PDMS/material alternatives.

[33] Recent Advances in Additive Manufacturing and 3D Bioprinting for Organs-On-A-Chip and Microphysiological Systems

M. Rothbauer, ..., and P. Ertl. Frontiers in Bioengineering and Biotechnology, 2022. 30 citations.
87% Topic Match
Reviews integration of 3D bioprinting/additive manufacturing with organ(cid:17)on(cid:17)a(cid:17)chip systems.
Summarizes modalities (extrusion, inkjet, SLA, two(cid:17)photon), compares applications, and discusses synergies and limits.
Notes automation/translation is nascent: highlights bioink constraints, biocompatibility, cost/throughput limits, and that printing(cid:17)to(cid:17)microfluidic workflows remain
immature (relevant but not an experimental automation/closed(cid:17)loop study).

[34] Microfluidic Organoids-on-a-Chip: Quantum Leap in Cancer Research

Fahriye Duzagac, ..., and F. Rizzolio. Cancers, 2021. 61 citations.
86% Topic Match
Surveys microfluidic organoid/organ(cid:17)on(cid:17)chip platforms for cancer research.
Reviews examples of fluidic control, multiplexed arrays, robotic liquid transfers, and imaging-enabled dynamic assays.
Notes automation benefits (reduced variability) but emphasizes gaps in standardization, connectivity (pumps/tubing), scale(cid:17)up, and need for advanced engineer-
ing/bioprinting for multi(cid:17)organ workflows — relevant for closed(cid:17)loop, imaging(cid:17)guided automation.

[35] Advances in Microfluidic Technologies in Organoid Research

Haitao Liu, ..., and Jianhua Qin. Advanced Healthcare Materials, 2023. 32 citations.
85% Topic Match
Reviews integration of microfluidics with organoid systems.
Surveys microarrays, microreactors, and microfluidic chips for high(cid:17)throughput manipulation, scaffold fabrication, and functional culture.
Mostly a technology-review: discusses limitations, standardization needs and future opportunities but does not provide quantitative comparisons of manual vs
automated workflows or explicit closed(cid:17)loop/AI control implementations.

[36] Organoids-on-a-chip: microfluidic technology enables culture of organoids with enhanced tissue function and potential for disease modeling

Lito Papamichail, ..., and A. D. van der Meer. Frontiers in Bioengineering and Biotechnology, 2025. 21 citations.
80% Topic Match
Reviews organoids-on-chip developments and limitations for reproducible organoid culture.
Surveys microfluidic strategies to control microenvironment, multi-organoid integration, and functional maturation improvements.
Relevant as a recent (2025) synthesis: discusses challenges (standardization, loading, perfusion, multiplexing) but is a review—limited primary automation/robotics
data or explicit manual vs automated workflow comparisons.

[37] Organoids-on-a-chip

S. Park, ..., and D. Huh. Science, 2019. 596 citations.
77% Topic Match
Reviews organ-on-chip integration with organoid technology.
Surveys engineering approaches to control, produce, and analyze organoids using microfluidic OoC platforms.
High-level review: discusses opportunities, challenges, standardization, interfacing, and potential to address throughput, reproducibility, spatial control—but lacks
quantitative comparisons of manual vs automated workflows or specific automation implementations/closed-loop AI systems.

[38] Developing 3D bioprinting for organs-on-chips.

Zhuhao Wu, ..., and Yuanjin Zhao. Lab on a chip, 2025. 6 citations.
74% Topic Match
Reviews integration of 3D bioprinting with organs-on-chip to increase structural complexity.
Surveys bioprinting methods applied to OoC fabrication, examples of on-chip printing workflows, and technical/biological challenges.
Likely a technology-focused review (2025); may discuss fabrication bottlenecks, but unclear if it compares manual vs automated workflows or quantifies throughput,
reproducibility, spatial-control gaps or closed-loop/AI needs — check full text for specifics.

[39] Application of biomaterial-based three-dimensional bioprinting for organ-on-a-chip fabrication
Joeng Ju Kim, ..., and Dong(cid:16)Woo Cho. International Journal of Bioprinting, 2024. 10 citations.
70% Topic Match
Reviews the use of 3D bioprinting for fabricating organ-on-a-chip devices.
Summarizes biomaterial selection, cell choices, and bioprinting methods to create tissue-specific microfluidic environments.
Mostly a technology-review: discusses precision and versatility of bioprinting but provides limited quantitative comparison of manual vs automated workflows,
throughput, reproducibility, or closed-loop/AI control gaps.

[40] A review of 3D bioprinting for organoids

Zeqing Li, ..., and Maobin Xie. Medical Review, 2025. 3 citations.
68% Topic Match
Reviews recent 3D bioprinting advances for organoid creation (focus on volumetric bioprinting).
Summarizes printing modalities, VBP emphasis, and bioink formulations addressing spatial control and construct complexity.
Notes high-level discussion of reproducibility, scalability, and throughput limitations; likely lacks detailed workflow comparisons, automation gaps, or closed-loop/AI
control specifics.

[41] Engineering organoids

Moritz Hofer and M. Lutolf. Nature Reviews. Materials, 2021. 789 citations.
62% Topic Match
Argues that engineering approaches can mitigate organoid variability and enable more controlled, scalable workflows.
Surveys cell/genetic engineering, microwells/microfluidics, niche/matrix design, OoC integration and nascent bioprinting for control and reproducibility.
Explicitly notes automation gaps (laborious assays, small analyte volumes, impractical hydrogel formats, limited inline sensing), calls for controlled positioning,
standardization, and multimodal/automated readouts — directly relevant to closed(cid:17)loop, imaging(cid:17)guided biofabrication needs.

[42] Three-Dimensional Bioprinting of Organoids: Past, Present, and Prospective

Mariana Cabral, ..., and Donghui Zhu. Tissue Engineering Part A, 2024. 21 citations.
62% Topic Match
Reviews 3D bioprinting approaches for organoid fabrication and applications.
Surveys bioprinting modalities, bioinks, and use-cases; compares bioprinting vs traditional organoid methods qualitatively.
Relevant as a technology-review: discusses benefits and challenges (throughput, scalability, bioink constraints) but likely lacks quantitative workflow comparisons,
automation gaps, or closed(cid:17)loop/AI control details.

[43] Advancing organoid development with 3D bioprinting

Wenping Ma, ..., and Chengtie Wu. Organoid Research, 2025. 9 citations.
58% Topic Match

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 27/41

Undermind

REPORT CREATED ON
11/22/2025

Reviews the role of 3D bioprinting in advancing organoid development.
Summarizes literature on how bioprinting controls cell distribution, ECM conditions, scalability, and high-throughput cultivation.
Likely a technology-focused review (2025) highlighting bioink/device optimization and scalability, but appears review-level without detailed workflow comparisons,
quantitative automation gaps, or closed(cid:17)loop/AI control discussion.

[44] A Pillar and Perfusion Plate Platform for Robust Human Organoid Culture and Analysis

Soo-yeon Kang, ..., and Moo-Yeal Lee. bioRxiv, 2023. 20 citations.
48% Topic Match
Demonstrates a high-precision pillar/perfusion plate platform for scalable organoid culture.
Uses microarray 3D bioprinting to deposit stem cells/spheroids into hydrogel pillars coupled to deep-well and perfusion plates for static/dynamic differentiation into
liver and intestine organoids.
Relevant because it addresses throughput, compatibility with 384(cid:17)well HTS equipment, and dynamic perfusion, but provides limited discussion of automation gaps,
closed-loop imaging control, multi-organoid assembly precision, or reproducibility metrics across batches.

[45] Pillar/Perfusion Plates for Miniature Human Tissue Culture and Predictive Compound Screening

Sooyeon Kang. Journal Not Provided, Unknown year. 0 citations.
39% Topic Match
Demonstrates a pillar/perfusion plate system enabling static and dynamic miniature human tissue/organoid culture.
Fabricates injection-molded pillar, deep-well, and perfusion plates; tests hydrogel cell loading, flow effects on spheroid necrosis, and microarray 3D bioprinting for
high-precision, high-throughput stem cell printing.
Relevant to automation/throughput and spatial placement (compatible with 384(cid:17)well formats and bioprinting), but paper appears focused on hardware/platform design
and printing demonstration rather than end-to-end workflow automation, closed-loop control, or explicit comparisons of manual vs automated processes.

[46] 3D Printing Techniques and Their Applications to Organ-on-a-Chip Platforms: A Systematic Review

V. Carvalho, ..., and Rui A. Lima. Sensors (Basel, Switzerland), 2021. 84 citations.
34% Topic Match
Provides a systematic review of 3D printing/bioprinting applied to organ-on-chip platforms.
Synthesizes literature (PRISMA-guided search of PubMed/Scopus/ScienceDirect) comparing 3D printing approaches to conventional microfabrication, with
examples of printed spheroid placement, projection lithography, multi-tissue OoC, vascularized constructs, and composite bioinks.
Discusses potential for higher throughput, accuracy, single-step chip+tissue fabrication and trends (hybrid printers), but lacks quantitative workflow comparisons,
explicit manual vs automated analyses, and limited discussion of closed(cid:17)loop/AI control or automation gaps.

[47] Advancing Drug Discovery for Neurological Disorders Using iPSC-Derived Neural Organoids

G. Costamagna, ..., and S. Corti. International Journal of Molecular Sciences, 2021. 61 citations.
28% Topic Match
Reviews organoid use for neurological drug discovery and highlights automation/scalability barriers.
Summarizes biological variability, incompatibility with higher-density screening, Matrigel lot effects, and suggests CRISPR, scRNA-seq, automated liquid handling,
microfluidics, HCI, and ML as solutions.
Relevant as a high-level, application-focused review: discusses automation gaps and proposed tools but lacks experimental comparisons of manual vs automated
workflows or closed-loop/control demonstrations.

[48] Microengineered organoids: reconstituting organ-level functions in vitro

S. Park, ..., and Jangho Kim. Organoid, 2023. 1 citations.
22% Topic Match
Summarizes microengineering strategies to improve organoid reproducibility and function.
Reviews microwells, microfluidic chips, and biomimetic microtopography, citing examples of improved morphology, reduced apoptosis, and multi-organoid co(cid:17)culture.
Notes automation-relevant points and gaps: microwells compatible with automated imaging but have morphology/size limits; microfluidics enable throughput and
integration but depend on pumps/tubing and tuning; practical handling, device variability, loading, and scalability remain unresolved.

[49] Design Principles for Pluripotent Stem Cell-Derived Organoid Engineering

Teresa P. Silva, ..., and Tiago G Fernandes. Stem Cells International, 2019. 31 citations.
17% Topic Match
Reviews bioengineering strategies for PSC-derived organoid assembly, patterning, and morphogenesis.
Summarizes methods (DPAC, ECM encapsulation, inkjet/microextrusion/laser bioprinting) and discusses control of initial state and spatiotemporal cell positioning.
Notes key gaps: scaling/high-throughput production, maturity/function readouts, and measurement limitations; paper does not provide workflow-level automation,
closed-loop control, or AI-integration details.

[50] Recent Advances in Microfluidics and Bioelectronics for Three-Dimensional Organoid Interfaces

Caroline Ferguson, ..., and Xueju Wang. ArXiv, 2025. 0 citations.
14% Topic Match
Reviews advances in 3D microfluidic and bioelectronic interfaces for organoid culture.
Summarizes microfabrication methods, device examples (microwells, perfused chips, droplet printers), and computational fluid modeling to address diffusion,
longevity, and reproducibility.
Relevant: discusses automated elements (an automated biopsy’96(cid:17)well schematic, droplet printer) and integrated sensing needs, but is a review (no new closed(cid:17)loop
implementations) and only briefly addresses automation gaps and AI/real(cid:17)time control.

[51] Establishment of organoid models based on a nested array chip for fast and reproducible drug testing in colorectal cancer therapy

Yan-cheng Cui, ..., and Xiaoni Ai. Bio-Design and Manufacturing, 2022. 12 citations.
11% Topic Match
No summary or abstract available

[52] 3D Bioprinting tissue analogs: Current development and translational implications

Suihong Liu, ..., and Murugan Ramalingam. Journal of Tissue Engineering, 2023. 23 citations.
9% Topic Match
Reviews current 3D bioprinting techniques and translational challenges.
Surveys extrusion, droplet, laser, stereolithography/volumetric and hybrid methods, plus bioreactors and vascularization hurdles.
High-level strategic review: mentions AI/ML, computer-vision, and imaging-guided/in(cid:17)situ bioprinting but lacks quantitative comparisons of manual vs automated
workflows, throughput, reproducibility, spatial-accuracy metrics, or multi-organoid assembly protocols.

[53] Spatially defined microenvironment for engineering organoids.

Yilan Zhang, ..., and Yiwei Li. Biophysics reviews, 2024. 2 citations.
9% Topic Match
Abstract: In the intricately defined spatial microenvironment, a single fertilized egg remarkably develops into a conserved and well-organized multicellular organism.
This observation leads us to hypothesize that stem cells or other seed cell types have the potential to construct fully structured and functional tissues or organs,
provided the spatial cues are appropriately configured. Current organoid technology, however, largely depends on spontaneous growth and self-organization, lacking
systematic guided intervention. As a result, the structures replicated in vitro often emerge in a disordered and sparse manner during growth phases. Although existing
organoids have made significant contributions in many aspects, such as advancing our...

[54] Microfluidic Techniques for Next(cid:16)Generation Organoid Systems

Jing Gong, ..., and Hai-Huang Xu. Advanced Materials Interfaces, 2022. 8 citations.
9% Topic Match

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 28/41

Undermind

REPORT CREATED ON
11/22/2025

Abstract: Organoids are 3D multicellular structures derived from pluripotent stem cells (PSCs) or adult stem cells (ASCs), which have attracted increasing
interest in the fields of drug screening, cell therapy, and regenerative medicine. Despite considerable success in culturing organoids with native microanatomy,
challenges to achieving a physiologically relevant microenvironment remain. Complex dynamic feedback between cells and the extracellular matrix and uncontrollable
mechano(cid:16)physiological cues hamper the further study of organoid systems. Innovative engineering approaches are needed to produce, control, and analyze
organoids and their microenvironment. Organoids(cid:16)on(cid:16)a(cid:16)chip, inspired by organs(cid:16)on(cid:16)a(cid:16)chip, presents a major technological breakthrough in providing physiologically
relevant environmental parameters. Organoids cultured...

[55] Development of a miniaturized 3D organoid culture platform for ultra-high-throughput screening

Yuhong Du, ..., and H. Fu. Journal of Molecular Cell Biology, 2020. 89 citations.
8% Topic Match
Abstract: Abstract The recent advent of robust methods to grow human tissues as 3D organoids allows us to recapitulate the 3D architecture of tumors in an in
vitro setting and offers a new orthogonal approach for drug discovery. However, organoid culturing with extracellular matrix to support 3D architecture has been
challenging for high-throughput screening (HTS)-based drug discovery due to technical difficulties. Using genetically engineered human colon organoids as a model
system, here we report our effort to miniaturize such 3D organoid culture with extracellular matrix support in high-density plates to enable HTS. We first established
organoid culturing in a 384-well plate...

[56] 3D Bioprinting for Engineering Organoids and Organ(cid:16)on(cid:16)a(cid:16)Chip: Developments and Applications

Yuqing Ren, ..., and Xinwei Han. Medicinal Research Reviews, 2025. 2 citations.
7% Topic Match
Abstract: Three(cid:16)dimensional (3D) bioprinting is a promising technology for the fabrication of complex tissue structures with bionic biological functions and stable
mechanical properties. Compared to traditional two(cid:16)dimensional models and animal models, 3D bioprinted biomimetic tissue models offer enhanced mimicry of
biological systems, enable high(cid:16)throughput screening, reduce experimental costs, and have multiple applications in disease modeling, drug discovery, and precision
medicine. Despite recent advancements in the commercialization of 3D bioprinting, the technology continues to encounter bioethical and legal issues, as well as a
lack of innovation in novel biomaterials. This review provides an overview of the fundamental techniques of 3D bioprinting and...

[57] Iteration of Tumor Organoids in Drug Development: Simplification and Integration

Rui Zhao, ..., and Shang Xie. Pharmaceuticals, 2025. 0 citations.
7% Topic Match
Abstract: The inherent complexity and heterogeneity of tumors pose substantial challenges for the development of effective oncology therapeutics. Organoids,
three-dimensional (3D) in vitro models, have become essential tools for predicting therapeutic responses and advancing precision oncology, with established
correlations to clinical outcomes in patient-derived models. These systems have transformed preclinical drug screening by bridging the gap between conventional
two-dimensional (2D) cultures and in vivo models, preserving tumor histopathology, cellular heterogeneity, and patient-specific molecular profiles. Despite their
potential, limitations in tumor organoid biology, including inter-batch variability and microenvironmental simplification, can undermine their reliability and scalability
in large-scale drug screening. To overcome these...

[58] From organoids to organoids-on-a-chip: Current applications and challenges in biomedical research

Kailun Liu, ..., and Baoyang Hu. Chinese Medical Journal, 2025. 5 citations.
6% Topic Match
Abstract: Abstract The high failure rates in clinical drug development based on animal models highlight the urgent need for more representative human models
in biomedical research. In response to this demand, organoids and organ chips were integrated for greater physiological relevance and dynamic, controlled
experimental conditions. This innovative platform—the organoids-on-a-chip technology—shows great promise in disease modeling, drug discovery, and personalized
medicine, attracting interest from researchers, clinicians, regulatory authorities, and industry stakeholders. This review traces the evolution from organoids to
organoids-on-a-chip, driven by the necessity for advanced biological models. We summarize the applications of organoids-on-a-chip in simulating physiological and
pathological phenotypes and...

[59] Organoid-on-a-chip: Current challenges, trends, and future scope toward medicine.

Zhangjie Li, ..., and Xiaolin Wang. Biomicrofluidics, 2023. 12 citations.
6% Topic Match
Abstract: In vitro organoid models, typically defined as 3D multicellular aggregates, have been extensively used as a promising tool in drug screening, disease
progression research, and precision medicine. Combined with advanced microfluidics technique, organoid-on-a-chip can flexibly replicate in vivo organs within the
biomimetic physiological microenvironment by accurately regulating different parameters, such as fluid conditions and concentration gradients of biochemical factors.
Since engineered organ reconstruction has opened a new paradigm in biomedicine, innovative approaches are increasingly required in micro-nano fabrication,
tissue construction, and development of pharmaceutical products. In this Perspective review, the advantages and characteristics of organoid-on-a-chip are first
introduced. Challenges in...

[60] Recent advances and challenges in organoid-on-a-chip technology

Intan Rosalina Suhito and Tae-Hyung Kim. Organoid, 2022. 8 citations.
6% Topic Match
Abstract: Conventional 2-dimensional cell culture poorly mimics human-relevant models, which is considered a major challenge in biological research. Organoids are
a recent breakthrough in 3-dimensional (3D) in vitro tissue engineering that better reflect the physiological, morphological, and functional properties of in vivo organs
(e.g., brain, heart, kidney, lung, and liver). Consequently, organoids are extensively used in various impactful biomedical applications including organ development,
disease modeling, and clinical drug testing. However, organoid technology still has several limitations, including low reproducibility, vascularization, limited nutrient
uptake and distribution (affecting the level of organoid maturation), lack of standardization, and intra-clonal variability. Efforts have been made...

[61] Advances in human organoids-on-chips in biomedical research

Yaqing Wang and J. Qin. Life Medicine, 2023. 31 citations.
5% Topic Match
Abstract: Abstract Organoids-on-chips is opening up new frontier of research in biomedical field by combining organoids and organs-on-chips technology. The
integrative technology offers great opportunities to maximize the potentials of organoids with higher fidelity, thus building advanced organ model systems in a
physiologically relevant manner. In this review, we highlight the key features of organoids-on-chips and how this integrative technology could be used to build
organoids in higher fidelity under controlled cellular microenvironment. We then introduce the recent progress of organoids-on-chips and their applications in
biomedical research. We also discuss the opportunities and challenges of the nascent field of organoids-on-chips that...

[62] Organoid bioprinting strategy and application in biomedicine: A review

Chen He, ..., and Jinhong Guo. International Journal of Bioprinting, 2023. 3 citations.
5% Topic Match
Abstract: Organoids are three-dimensional cell structures cultured in vitro. They are self-organizing and can mimic real organs in structure and function. Bioprinting
technology breaks through some limitations of organoid manufacturing, making it more widely used in drug screening, regenerative medicine, and other fields. In this
review, we first introduce bioinks and bioprinting methods for stem cell and organoid bioprinting, then summarize several vascularization strategies for bioprinting
organoids, and present applications in biomedicine. In the future, the development of microfluidic technology and four-dimensional bioprinting technology may be
conducive to forming better bioprinted organoids.

[63] 3D organ-on-a-chip: The convergence of microphysiological systems and organoids

L. Baptista, ..., and C. Perrault. Frontiers in Cell and Developmental Biology, 2022. 63 citations.
5% Topic Match
Abstract: Medicine today faces the combined challenge of an increasing number of untreatable diseases and fewer drugs reaching the clinic. While pharmaceutical
companies have increased the number of drugs in early development and entering phase I of clinical trials, fewer actually successfully pass phase III and launch
into the market. In fact, only 1 out of every 9 drugs entering phase I will launch. In vitro preclinical tests are used to predict earlier and better the potential of new
drugs and thus avoid expensive clinical trial phases. The most recent developments favor 3D cell culture and human stem cell biology. These...

[64] Recent advances in organ-on-a-chip technologies and future challenges: a review

H. Avci, ..., and Ali Akpek. TURKISH JOURNAL OF CHEMISTRY, 2018. 23 citations.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 29/41

Undermind

REPORT CREATED ON
11/22/2025

4% Topic Match
Abstract: The significant development in the construction of microscale cell culture platforms and the interest in bioanalytical analysis have recently resulted in the
emergence of a new concept of `organ-on-a-chip' systems. Organ-on-a-chip is a new three-dimensional (3D) in vitro microfabricated unit that contains a multichannel
microfluidic cell culture. Even if many informative and useful data are obtained from animal models and in vitro assays, they are still limited for extrapolation to human
systems during drug design and development. Only about 1 out of 10,000 compounds is processed in clinical trials for final approval. As being the first example of
its kind,...

[65] Design and Fabrication of Organ-on-Chips: Promises and Challenges

Alireza Tajeddin and N. Mustafaoglu. Micromachines, 2021. 71 citations.
4% Topic Match
Abstract: The advent of the miniaturization approach has influenced the research trends in almost all disciplines. Bioengineering is one of the fields benefiting from
the new possibilities of microfabrication techniques, especially in cell and tissue culture, disease modeling, and drug discovery. The limitations of existing 2D cell
culture techniques, the high time and cost requirements, and the considerable failure rates have led to the idea of 3D cell culture environments capable of providing
physiologically relevant tissue functions in vitro. Organ-on-chips are microfluidic devices used in this context as a potential alternative to in vivo animal testing to
reduce the cost and...

[66] Advances of Cell Printing Technology in Organoid Engineering.

Yu-Han Ho, ..., and Ren Xu. Tissue engineering. Part B, Reviews, 2025. 1 citations.
4% Topic Match
Abstract: Organoid engineering is a rapidly expanding field that involves developing miniaturized, three-dimensional (3D) structures to mimic the architecture and
function of real organs. It provides a powerful platform to investigate organ development, disease modeling, and personalized medicine. Recent advances in cell
printing technology, also known as bioprinting, feature high-throughput potential, precise control, and enhanced reproducibility, enabling the deposition of living cells
to generate complex, 3D biological structures. Cell printing with bioinks composed of cells and supportive biomaterials has been utilized to generate in vitro tissues
and organs with intricate architectures and functionalities to investigate normal tissue morphogenesis and disease progression....

[67] Organoid technology for personalized pancreatic cancer therapy

Axel Bengtsson, ..., and D. Ansari. Cellular Oncology (Dordrecht), 2021. 21 citations.
3% Topic Match
Abstract: Pancreatic ductal adenocarcinoma has the lowest survival rate among all major cancers and is the third leading cause of cancer-related mortality. The
stagnant survival statistics and dismal response rates to current therapeutics highlight the need for more efficient preclinical models. Patient-derived organoids
(PDOs) offer new possibilities as powerful preclinical models able to account for interpatient variability. Organoid development can be divided into four different key
phases: establishment, propagation, drug screening and response prediction. Establishment entails tailored tissue extraction and growth protocols, propagation
requires consistent multiplication and passaging, while drug screening and response prediction will benefit from shorter and more precise...

[68] Research on the Methods for the Mass Production of Multi-Scale Organs-On-Chips

A. Díaz Lantada, ..., and J. García-Ruíz. Polymers, 2018. 24 citations.
3% Topic Match
Abstract: The success of labs- and organs-on-chips as transformative technologies in the biomedical arena relies on our capacity of solving some current challenges
related to their design, modeling, manufacturability, and usability. Among present needs for the industrial scalability and impact promotion of these bio-devices,
their sustainable mass production constitutes a breakthrough for reaching the desired level of repeatability in systematic testing procedures based on labs- and
organs-on-chips. The use of adequate biomaterials for cell-culture processes and the achievement of the multi-scale features required, for in vitro modeling the
physiological interactions among cells, tissues, and organoids, which prove to be demanding requirements...

[69] Immersion bioprinting of hyaluronan and collagen bioink-supported 3D patient-derived brain tumor organoids

Casey Clark, ..., and A. Skardal. Biomedical Materials, 2022. 30 citations.
3% Topic Match
Abstract: Organoids, and in particular patient-derived organoids, have emerged as crucial tools for cancer research. Our organoid platform, which has supported
patient-derived tumor organoids (PTOs) from a variety of tumor types, has been based on the use of hyaluronic acid (HA) and collagen, or gelatin, hydrogel bioinks.
One hurdle to high throughput PTO biofabrication is that as high-throughput multi-well plates, bioprinted volumes have increased risk of contacting the sides of wells.
When this happens, surface tension causes bioinks to fall flat, resulting in 2D cultures. To address this problem, we developed an organoid immersion bioprinting
method—inspired by the FRESH printing method—in...

[70] Advancements in Organ(cid:16)on(cid:16)a(cid:16)Chip Systems: Materials, Characterization, and Applications

Balu Mahendran Gunasekaran, ..., and Noel Nesakumar. ChemistrySelect, 2024. 3 citations.
3% Topic Match
Abstract: Recent advancements in 3D tissue engineering and organ(cid:16)on(cid:16)a(cid:16)chip systems have revolutionized biomedical research by providing sophisticated platforms
that mimic complex physiological environments. This review explores various techniques in 3D printing, including bioprinting materials, laser(cid:16)induced forward transfer,
ink(cid:16)jet systems, and microextrusion methods, highlighting their roles in fabricating intricate tissue constructs. Physical and biochemical characterization methods
for assessing these engineered tissues on microchips are discussed in detail, emphasizing their importance in accurately replicating physiological conditions. The
review further delves into the development of multiple organ and single organ(cid:16)on(cid:16)a(cid:16)chip systems. It covers two(cid:16)organ, three(cid:16)organ, and four(cid:16)organ platforms, as well as
individual systems such...

[71] Engineered Human Organoids for Biomedical Applications

Yujuan Zhu, ..., and Yuanjin Zhao. Advanced Functional Materials, 2023. 19 citations.
3% Topic Match
Abstract: Human organoid models potentially offer a physiologically relevant platform to replace traditional monolayer cultures and animal models. In particular,
the rapid development of engineered strategies including microfluidics, hydrogel, 3D printing and others, which have enormous advantages in comparison to
conventional methods, is expected to further advance organoid technology. Up to now, many studies have demonstrated the engineered organoid models with
complex cell composition, controlled structure, enhanced maturation, reduced heterogeneity, and so on. These engineered organoids are high promising for studies
in development, disease, tissue repair, precision medicine and drug screening. In this review, a comprehensive summary of the engineered organoid...

[72] Organ bioprinting: progress, challenges and outlook.

Yang Wu, ..., and Xue Yang. Journal of materials chemistry. B, 2023. 11 citations.
3% Topic Match
Abstract: Bioprinting, as a groundbreaking technology, enables the fabrication of biomimetic tissues and organs with highly complex structures, multiple cell types,
mechanical heterogeneity, and diverse functional gradients. With the growing demand for organ transplantation and the limited number of organ donors, bioprinting
holds great promise for addressing the organ shortage by manufacturing completely functional organs. While the bioprinting of complete organs remains a distant
goal, there has been considerable progress in the development of bioprinted transplantable tissues and organs for regenerative medicine. This review article
recapitulates the current achievements of organ 3D bioprinting, primarily encompassing five important organs in the human...

[73] Bridging the organoid translational gap: integrating standardization and micropatterning for drug screening in clinical and pharmaceutical
medicine

Haowei Yang, ..., and Shaohua Ma. Life Medicine, 2024. 6 citations.
3% Topic Match
Abstract: Abstract Synthetic organ models such as organoids and organ-on-a-chip have been receiving recognition from administrative agencies. Despite the
proven success of organoids in predicting drug efficacy on laboratory scales, their translational advances have not fully satisfied the expectations for both
clinical implementation and commercial applications. The transition from laboratory settings to clinical applications continues to encounter challenges. Employing
engineering methodologies to facilitate the bridging of this gap for organoids represents one of the key directions for future advancement. The main measures to
bridge the gap include environmental and phenotypic recapitulation, 3D patterning, matrix engineering, and multi-modality information acquisition and processing....

[74] The emergence of 3D bioprinting in organ-on-chip systems

Kirsten Fetah, ..., and A. Khademhosseini. Progress in Biomedical Engineering, 2019. 76 citations.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 30/41

Undermind

REPORT CREATED ON
11/22/2025

3% Topic Match
Abstract: Understanding complex cell–cell interactions and physiological microenvironments is critical for the development of new therapies for treating human
diseases. Current animal models fail to accurately predict success of therapeutic compounds and clinical treatments. Advances in biomaterials, engineering, and
additive manufacturing have led to the development of printed tissues, lab-on-chip devices, and, more recently, organ-on-chip systems. These technologies have
promising applications for the fabrication of more physiologically representative human tissues and can be used for high-throughput testing of human cells and
organoids. These organ-on-chip systems can be fabricated with integrated fluidics to allow for the precise control and manipulation of cellular...

[75] Out of Box Thinking to Tangible Science: A Benchmark History of 3D Bio-Printing in Regenerative Medicine and Tissues Engineering

Karthika Pushparaj, ..., and Sung-Wook Park. Life, 2023. 20 citations.
3% Topic Match
Abstract: Advancements and developments in the 3D bioprinting have been promising and have met the needs of organ transplantation. Current improvements in
tissue engineering constructs have enhanced their applications in regenerative medicines and other medical fields. The synergistic effects of 3D bioprinting have
brought technologies such as tissue engineering, microfluidics, integrated tissue organ printing, in vivo bioprinted tissue implants, artificial intelligence and machine
learning approaches together. These have greatly impacted interventions in medical fields, such as medical implants, multi-organ-on-chip models, prosthetics, drug
testing tissue constructs and much more. This technological leap has offered promising personalized solutions for patients with chronic diseases,...

[76] Bioengineering Approaches for the Advanced Organoid Research

S. A. Yi, ..., and Ki(cid:16)Bum Lee. Advanced Materials, 2021. 137 citations.
3% Topic Match
Abstract: Recent advances in 3D cell culture technology have enabled scientists to generate stem cell derived organoids that recapitulate the structural and
functional characteristics of native organs. Current organoid technologies have been striding toward identifying the essential factors for controlling the processes
involved in organoid development, including physical cues and biochemical signaling. There is a growing demand for engineering dynamic niches characterized by
conditions that resemble in vivo organogenesis to generate reproducible and reliable organoids for various applications. Innovative biomaterial(cid:16)based and advanced
engineering(cid:16)based approaches have been incorporated into conventional organoid culture methods to facilitate the development of organoid research. The recent...

[77] Organoids as Next-Generation Models for Tumor Heterogeneity, Personalized Therapy, and Cancer Research: Advancements, Applications, and
Future Directions

Ayush Madan, ..., and M. K. Satapathy. Organoids, 2025. 1 citations.
2% Topic Match
Abstract: Organoid technology has emerged as a revolutionary tool in cancer research, offering physiologically accurate, three-dimensional models that preserve the
histoarchitecture, genetic stability, and phenotypic complexity of primary tumors. These self-organizing structures, derived from adult stem cells, induced pluripotent
stem cells, or patient tumor biopsies, recapitulate critical aspects of tumor heterogeneity, clonal evolution, and microenvironmental interactions. Organoids serve as
powerful systems for modeling tumor progression, assessing drug sensitivity and resistance, and guiding precision oncology strategies. Recent innovations have
extended organoid capabilities beyond static culture systems. Integration with microfluidic organoid-on-chip platforms, high-throughput CRISPR-based functional
genomics, and AI-driven phenotypic analytics has enhanced mechanistic...

[78] Integrating Microfluidics and 3D Bioprinting for Advanced in vitro Tissue and Organ Models

Wei Fu, ..., and Zhenya Yuan. Sains Malaysiana, 2025. 0 citations.
2% Topic Match
Abstract: Advances in tissue engineering necessitate in vitro models that accurately replicate human organ complexity. The limitations of conventional 2D cultures
and animal models have driven development of biomimetic platforms integrating microfluidics and 3D bioprinting. Microfluidic technologies enable precise control
of fluid dynamics, nutrient delivery, and biochemical gradients at microscale, while 3D bioprinting facilitates layer-by-layer fabrication of complex tissue structures.
This review examines design principles of microfluidic platforms, highlighting organ-on-a-chip and tumor-on-a-chip applications demonstrating controlled perfusion
advantages. We analyze major bioprinting modalities, extrusion, inkjet, laser-assisted, and stereolithography, evaluating their suitability for specific tissue engineering
applications. The review describes integration strategies, including...

[79] Developments and Opportunities for 3D Bioprinted Organoids

Ya Ren, ..., and Jinwu Wang. International Journal of Bioprinting, 2021. 84 citations.
2% Topic Match
Abstract: Organoids developed from pluripotent stem cells or adult stem cells are three-dimensional cell cultures possessing certain key characteristics of their
organ counterparts, and they can mimic certain biological developmental processes of organs in vitro. Therefore, they have promising applications in drug
screening, disease modeling, and regenerative repair of tissues and organs. However, the construction of organoids currently faces numerous challenges, such as
breakthroughs in scale size, vascularization, better reproducibility, and precise architecture in time and space. Recently, the application of bioprinting has accelerated
the process of organoid construction. In this review, we present current bioprinting techniques and the application of...

[80] Organoids(cid:16)On(cid:16)a(cid:16)Chip for Personalized Precision Medicine

Yunqi Man, ..., and Zhenbao Liu. Advanced Healthcare Materials, 2024. 19 citations.
2% Topic Match
Abstract: The development of personalized precision medicine has become a pivotal focus in modern healthcare. Organoids(cid:16)on(cid:16)a(cid:16)Chip (OoCs), a groundbreaking
fusion of organoid culture and microfluidic chip technology, has emerged as a promising approach to advancing patient(cid:16)specific treatment strategies. In this review,
the diverse applications of OoCs are explored, particularly their pivotal role in personalized precision medicine, and their potential as a cutting(cid:16)edge technology is
highlighted. By utilizing patient(cid:16)derived organoids, OoCs offer a pathway to optimize treatments, create precise disease models, investigate disease mechanisms,
conduct drug screenings, and individualize therapeutic strategies. The emphasis is on the significance of this technological fusion in...

[81] Automated Bioprocess Feedback Operation in a High-Throughput Facility via the Integration of a Mobile Robotic Lab Assistant

L. Kaspersetz, ..., and M. Cruz-Bournazou. Unknown journal, 2022. 9 citations.
2% Topic Match
Abstract: The development of biotechnological processes is challenging due to the diversity of process parameters. For efficient upstream development, parallel
cultivation systems have proven to reduce costs and associated timelines successfully while offering excellent process control. However, the degree of automation
of such small-scale systems is comparatively low, and necessary sample analysis requires manual steps. Although the subsequent analysis can be performed in
a high-throughput manner, the integration of analytical devices remains challenging, especially when cultivation and analysis laboratories are spatially separated.
Mobile robots offer a potential solution, but their implementation in research laboratories is not widely adopted. Our approach demonstrates...

[82] Advances in 3D Bioprinting of TissuesOrgans for Regenerative Medicine and In Vitro Models: A Review

Sonam Samal, ..., and Jonnalagadda Vihari. Biomedicine, 2024. 0 citations.
2% Topic Match
Abstract: A promising area for the creation of cutting-edge treatments to deal with organtissue failure is regenerative medicine. In contrast to other methods,
3D bioprinting has drawn a lot of interest since it can create intricate structures with exact cell placement and composition. A thorough assessment of current
developments in 3D bioprinting technologies for tissueorgan engineering and in vitro models is the goal of this review. The study includes a thorough investigation
and evaluation of pertinent papers released between 2015 and 2023. The review discusses developments in cell sources, biomaterials, bioinks, bioprinting methods,
and post-printing maturation processes. The results show important...

[83] The Role of Microfluidics for Organ on Chip Simulations

A. Aziz, ..., and Bo Liu. Bioengineering, 2017. 59 citations.
2% Topic Match
Abstract: A multichannel three-dimensional chip of a microfluidic cell culture which enables the simulation of organs is called an “organ on a chip” (OC). With the
integration of many other technologies, OCs have been mimicking organs, substituting animal models, and diminishing the time and cost of experiments which is
better than the preceding conventional in vitro models, which make them imperative tools for finding functional properties, pathological states, and developmental
studies of organs. In this review, recent progress regarding microfluidic devices and their applications in cell cultures is discussed to explain the advantages and
limitations of these systems. Microfluidics is not...

[84] Strategies to overcome the limitations of current organoid technology - engineered organoids

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 31/41

Undermind

REPORT CREATED ON
11/22/2025

Xulong Fan, ..., and Gaofeng Liang. Journal of Tissue Engineering, 2025. 4 citations.
2% Topic Match
Abstract: Organoids, as 3D in vitro models derived from stem cells, have unparalleled advantages over traditional cell and animal models for studying organogenesis,
disease mechanisms, drug screening, and personalized diagnosis and treatment. Despite the tremendous progress made in organoid technology, the translational
application of organoids still presents enormous challenges due to the complex structure and function of human organs. In this review, the limitations of the
translational application of traditional organoid technologies are first described. Next, we explore ways to address many of the limitations of traditional organoid
cultures by engineering various dimensions of organoid systems. Finally, we discuss future directions...

[85] 3D bioprinting of collagen-based high-resolution internally perfusable scaffolds for engineering fully biologic tissue systems

Daniel J. Shiwarski, ..., and A. Feinberg. Science Advances, 2025. 13 citations.
2% Topic Match
Abstract: Organ-on-a-chip and microfluidic systems have improved the translational relevance of in vitro systems; however, current manufacturing approaches
impart limitations on materials selection, non-native mechanical properties, geometric complexity, and cell-driven remodeling into functional tissues. Here, we
three-dimensionally (3D) bioprint extracellular matrix (ECM) and cells into collagen-based high-resolution internally perfusable scaffolds (CHIPS) that integrate with
a vascular and perfusion organ-on-a-chip reactor (VAPOR) to form a complete tissue engineering platform. We improve the fidelity of freeform reversible embedding
of suspended hydrogels (FRESH) bioprinting to produce a range of CHIPS designs fabricated in a one-step process. CHIPS exhibit size-dependent permeability of
perfused molecules into...

[86] 3D Bioprinting for Personalized Medicine: Advances, Challenges, and Future Directions.
Xinshuai Gao, ..., and Tao Xu. ACS biomaterials science & engineering, 2025. 0 citations.
2% Topic Match
Abstract: Due to the shortage of donors and the immune rejection of patients, the shortage of tissues/organs is a major challenge in the medical field. Since
the development of regenerative medicine, the exploration from constructing disease models in vitro to the repair, regeneration, and replacement of organs in
vivo has never ceased. However, few technologies can replicate complex tissue structures and cell spatial heterogeneity. As a biological manufacturing method,
three-dimensional (3D) bioprinting has developed rapidly and can deposit biomaterials and cells in a 3D controlled space with unprecedented accuracy. Compared
with traditional tissue-engineering methods, 3D bioprinting can create highly complex 3D...

[87] Automated bioprocess feedback operation in a high throughput facility via the integration of a mobile robotic lab assistant

L. Kaspersetz, ..., and M. Cruz-Bournazou. bioRxiv, 2022. 3 citations.
1% Topic Match
Abstract: Biotechnological processes development is challenging due to the sheer variety of process parameters. For efficient upstream development parallel
cultivation systems have proven to reduce costs and associated timelines successfully, while offering excellent process control. However, the degree of automation
of such small scale systems is comparably low and necessary sample analysis requires manual steps. Although the subsequent analysis can be performed in
a high-throughput manner, the integration of analytic devices remains challenging. Especially, when cultivation and analysis laboratories are spatially separated.
Mobile robots offer a potential solution, but the implementation in research laboratories is not widely adopted. Our approach demonstrates...

[88] Bioprinted Organoids: An Innovative Engine in Biomedicine

Zhengwei Li, ..., and Changshun Ruan. Advanced Science, 2025. 2 citations.
1% Topic Match
Abstract: Bioprinted organoids integrate bioprinting technology with organoid research, enabling the simultaneous reconstruction of human tissue morphology and
physiological function in vitro. This approach offers distinct advantages in organoid fabrication, particularly in terms of structural precision, tissue mimicry, and
functional fidelity. By leveraging the complementary strengths of both technologies, bioprinted organoids allow for the fabrication of personalized, architecturally
engineered models that more accurately replicate organogenesis, physiological processes, and disease progression. Herein, this review outlines the key advantages
of bioprinted organoids, with a focus on their ability to precisely control morphology, dimensions, and spatial organization. Bioprinted organoids are further categorized
into three...

[89] Human organoids: model systems for human biology and medicine

Jihoon Kim, ..., and J. Knoblich. Nature Reviews. Molecular Cell Biology, 2020. 1533 citations.
1% Topic Match
Abstract: The historical reliance of biological research on the use of animal models has sometimes made it challenging to address questions that are specific to
the understanding of human biology and disease. But with the advent of human organoids — which are stem cell-derived 3D culture systems — it is now possible
to re-create the architecture and physiology of human organs in remarkable detail. Human organoids provide unique opportunities for the study of human disease
and complement animal models. Human organoids have been used to study infectious diseases, genetic disorders and cancers through the genetic engineering of
human stem cells, as...

[90] AngioPlate – Biofabrication of perfusable complex tissues in multi-well plates with 4D subtractive manufacturing

Shravanthi Rajasekar, ..., and Boyang Zhang. bioRxiv, 2021. 1 citations.
1% Topic Match
Abstract: Organ-on-a-chip systems that recapitulate tissue-level functions have been proposed to improve in vitro–in vivo correlation in drug development. Significant
progress has been made to control the cellular microenvironment with mechanical stimulation and fluid flow. However, it has been challenging to introduce complex
3D tissue structures due to the physical constraints of microfluidic channels or membranes in organ-on-a-chip systems. Although this problem could be addressed
with the integration of 3D bioprinting, it is not an easy task because the two technologies have fundamentally different fabrication processes. Inspired by 4D
bioprinting, we develop a 4D subtractive manufacturing technique where a flexible sacrificial...

[91] Vascularized organoid-on-a-chip for centimeter-scale organoid cultivation

Xiaofeng Gong, ..., and Bing Zhao. Bio-Design and Manufacturing, 2025. 1 citations.
1% Topic Match
Abstract: An organoid is a three-dimensional (3D) cell culture model that can reproduce the distinct structure and inherent functionality of certain organs.
Nevertheless, a major limitation of organoids is the absence of a complex vascular network, thus restricting the supply of oxygen and essential nutrients. Coupled
with their inherent size constraints and metabolite accumulation, it is challenging for organoids to replicate the natural intricacies of organs, thereby limiting their
applicability. To overcome the challenges associated with this technology, we developed a culture platform to cultivate tumors or organ-derived organoids up to the
centimeter scale. Initially, a customized organoid-on-a-chip including a microvascular...

[92] Transformative potential of three-dimensional bioprinting technology for advanced organoid research

Jungbin Yoon, ..., and Jinah Jang. Organoid, 2024. 1 citations.
1% Topic Match
Abstract: Organoid research has emerged as a transformative field in biomedicine, focusing on the in vitro development of 3-dimensional (3D) structures that mimic
human organs. Derived from various types of stem cells, organoids closely replicate human organ structures and functions, offering significant advantages over
2-dimensional cell cultures and animal models, particularly for drug development, tissue engineering, and precision medicine. Recent innovations, including the
integration of biofabrication technologies, have significantly increased the structural complexity and maturity of organoids, expanding their biomedical applications.
A critical factor in organoid culture is the utilization of the extracellular matrix (ECM), particularly decellularized ECM hydrogels. These hydrogels...

[93] Organoids/organs-on-chips towards biomimetic human artificial skin

Yuting Huang, ..., and Xiaodong Chen. Burns & Trauma, 2025. 0 citations.
1% Topic Match
Abstract: Abstract As the largest organ in the human body, the skin protects the body from pathogens and harmful substances through physical, chemical, and
immune barrier functions. However, accurately replicating the complex physiology of human skin in mouse models remains a significant challenge. Accurately
replicating the complex physiology of human skin in mouse models remains a significant challenge, making the development of bionic artificial skin particularly
important. In recent years, skin organoid and skin-on-a-chip technologies have greatly enhanced in vitro skin modeling, overcoming many limitations of traditional
approaches. In this review, we comprehensively summarize important advances in research on skin organoids...

[94] Organoid bioinks: construction and application

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 32/41

Undermind

REPORT CREATED ON
11/22/2025

Fuxiao Wang, ..., and Jiachan Su. Biofabrication, 2024. 25 citations.
1% Topic Match
Abstract: Organoids have emerged as crucial platforms in tissue engineering and regenerative medicine but confront challenges in faithfully mimicking native
tissue structures and functions. Bioprinting technologies offer a significant advancement, especially when combined with organoid bioinks-engineered formulations
designed to encapsulate both the architectural and functional elements of specific tissues. This review provides a rigorous, focused examination of the evolution and
impact of organoid bioprinting. It emphasizes the role of organoid bioinks that integrate key cellular components and microenvironmental cues to more accurately
replicate native tissue complexity. Furthermore, this review anticipates a transformative landscape invigorated by the integration of artificial intelligence with...

[95] How to Design Engineered Organs to Enhance Physiological Function

Qi Gu. The International Conference on Computational &amp; Experimental Engineering and Sciences, 2024. 0 citations.
1% Topic Match
Abstract: In the complex field of organ fabrication, which combines developmental biology, bioinspired engineering, and regenerative medicine, the main goal is
to closely mimic the detailed structure and function of natural organs. While advanced techniques like 3D bioprinting have made significant strides but often fall
short in accurately emulating the dynamic, self-organizing processes fundamental to organogenesis, particularly the nuanced patterns of cellular motility and spatial
organization [1]. This issue highlights a big challenge in tissue engineering: making synthetic organs that truly match their natural models. Our work aims to bring
together principles of developmental biology with the latest in organ making...

[96] Bioprinting Cell- and Spheroid-Laden Protein-Engineered Hydrogels as Tissue-on-Chip Platforms

D. F. Duarte Campos, ..., and S. Heilshorn. Frontiers in Bioengineering and Biotechnology, 2020. 50 citations.
1% Topic Match
Abstract: Human tissues, both in health and disease, are exquisitely organized into complex three-dimensional architectures that inform tissue function. In biomedical
research, specifically in drug discovery and personalized medicine, novel human-based three-dimensional (3D) models are needed to provide information with
higher predictive value compared to state-of-the-art two-dimensional (2D) preclinical models. However, current in vitro models remain inadequate to recapitulate the
complex and heterogenous architectures that underlie biology. Therefore, it would be beneficial to develop novel models that could capture both the 3D heterogeneity
of tissue (e.g., through 3D bioprinting) and integrate vascularization that is necessary for tissue viability (e.g., through culture...

[97] 3D bioprinting in tissue engineering: current state-of-the-art and challenges towards system standardization and clinical translation

Tarun Agarwal, ..., and T. K. Maiti. Biofabrication, 2025. 5 citations.
1% Topic Match
Abstract: Over the past decade, three-dimensional (3D) bioprinting has made significant progress, transforming into a key innovation in tissue engineering. Despite
the early strides, critical challenges remain in 3D bioprinting that must be addressed to accelerate clinical translation. In particular, there is still a long way to go before
functionally-mature, clinically-relevant tissue equivalents are developed. Current limitations range from the sub-optimal bioink properties and degree of biomimicry
of bioprintable architectures, to the lack of stem/progenitor cells for massive cell expansion, and fundamental knowledge regarding in vitro culturing conditions. In
addition to these problems, the absence of guidelines and well-regulated international standards...

[98] Vascularized Liver Organoids Generated Using Induced Hepatic Tissue and Dynamic Liver(cid:16)Specific Microenvironment as a Drug Testing Platform

Yoonhee Jin, ..., and Seung(cid:16)Woo Cho. Advanced Functional Materials, 2018. 138 citations.
1% Topic Match
Abstract: Induced hepatic (iHep) cells generated by direct reprogramming have been proposed as cell sources for drug screening and regenerative medicine.
However, the practical use of a 3D hepatic tissue culture comprised of iHep cells for drug screening and toxicology testing has not been demonstrated. In this study,
a 3D vascularized liver organoid composed of iHep cells and a decellularized liver extracellular matrix (LEM) cultured in a microfluidic system is demonstrated. iHep
cells are generated by transfection with polymer nanoparticles and plasmids expressing hepatic transcription factors. The iHep cells are cocultured with endothelial
cells in the 3D LEM hydrogel in a...

[99] Organoid(cid:16)based novel technology for antitumor drug screening

Yu Su, ..., and Yihai Shi. VIEW, 2025. 0 citations.
1% Topic Match
Abstract: Organoids are an emerging biomedical research model that can highly mimic the key physiological characteristics and biological functions of organs in vivo,
achieving significant breakthroughs in tumor immunotherapy drug screening. With continuous technological innovation, the integration of organoids with emerging
technologies such as gene editing, high(cid:16)throughput screening, artificial intelligence (AI), and 3D bioprinting has further expanded their applications in antitumor drug
screening, particularly through the development of novel fusion models, such as organoid(cid:16)AI and organoid(cid:16)3D bioprinting platforms, paving new ways for constructing
more complex and optimized model systems. Although organoid technology still faces limitations at this stage, these challenges are...

[100] Organ-on-a-Chip Models—New Possibilities in Experimental Science and Disease Modeling

BartBomiej WysoczaDski, ..., and A. Wójcik-GBadysz
1% Topic Match
Abstract: ‘Organ-on-a-chip’ technology is a promising and rapidly evolving model in biological research. This innovative microfluidic cell culture device was created
using a microchip with continuously perfused chambers, populated by living cells arranged to replicate physiological processes at the tissue and organ levels. By
consolidating multicellular structures, tissue–tissue interfaces, and physicochemical microenvironments, these microchips can replicate key organ functions. They
also enable the high-resolution, real-time imaging and analysis of the biochemical, genetic, and metabolic activities of living cells in the functional tissue and organ
contexts. This technology can accelerate research into tissue development, organ physiology and disease etiology, therapeutic approaches, and...

. Biomolecules, 2024. 10 citations.

[101] Exploring recent breakthroughs in robotic biomechanical and electrophysiological measurement tools
Huiyao Shi, ..., and Lianqing Liu. Biomedical Engineering Communications, Unknown year. 0 citations.
1% Topic Match
Abstract: Single-cell biomechanics and electrophysiology measuring tools have transformed biological research over the last few decades, which enabling a
comprehensive and nuanced understanding of cellular behavior and function. Despite their high-quality information content, these single-cell measuring techniques
suffer from laborious manual processing by highly skilled workers and extremely low throughput (tens of cells per day). Recently, numerous researchers have
automated the measurement of cell mechanical and electrical signals through robotic localization and control processes. While these efforts have demonstrated
promising progress, critical challenges persist, including human dependency, learning complexity, in-situ measurement, and multidimensional signal acquisition. To
identify key limitations and highlight...

[102] Engineering vascularised organoid-on-a-chip: strategies, advances and future perspectives

Zhangjie Li, ..., and Xiaolin Wang. Biomaterials Translational, 2024. 7 citations.
1% Topic Match
Abstract: ABSTRACT In recent years, advances in microfabrication technology and tissue engineering have propelled the development of a novel drug screening and
disease modelling platform known as organoid-on-a-chip. This platform integrates organoids and organ-on-a-chip technologies, emerging as a promising approach
for in vitro modelling of human organ physiology. Organoid-on-a-chip devices leverage microfluidic systems to simulate the physiological microenvironment of specific
organs, offering a more dynamic and flexible setting that can mimic a more comprehensive human biological context. However, the lack of functional vasculature
has remained a significant challenge in this technology. Vascularisation is crucial for the long-term culture and in vitro...

[103] 3D Bioprinting of Collagen-based Microfluidics for Engineering Fully-biologic Tissue Systems

Daniel J. Shiwarski, ..., and A. Feinberg. bioRxiv, 2024. 2 citations.
1% Topic Match
Abstract: Microfluidic and organ-on-a-chip devices have improved the physiologic and translational relevance of in vitro systems in applications ranging from disease
modeling to drug discovery and pharmacology. However, current manufacturing approaches have limitations in terms of materials used, non-native mechanical
properties, patterning of extracellular matrix (ECM) and cells in 3D, and remodeling by cells into more complex tissues. We present a method to 3D bioprint ECM
and cells into microfluidic collagen-based high-resolution internally perfusable scaffolds (CHIPS) that address these limitations, expand design complexity, and
simplify fabrication. Additionally, CHIPS enable size-dependent diffusion of molecules out of perfusable channels into the surrounding device...

[104] A programmable platform for probing cell migration and proliferation

Jillian Cwycyshyn, ..., and I. Rajapakse. APL Bioengineering, 2024. 1 citations.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 33/41

Undermind

REPORT CREATED ON
11/22/2025

1% Topic Match
Abstract: The advent of advanced robotic platforms and workflow automation tools has revolutionized the landscape of biological research, offering unprecedented
levels of precision, reproducibility, and versatility in experimental design. In this work, we present an automated and modular workflow for exploring cell behavior
in two-dimensional culture systems. By integrating the BioAssemblyBot® (BAB) robotic platform and the BioApps™ workflow automater with live-cell fluorescence
microscopy, our workflow facilitates execution and analysis of in vitro migration and proliferation assays. Robotic assistance and automation allow for the precise
and reproducible creation of highly customizable cell-free zones (CFZs), or wounds, in cell monolayers and “hands-free,” schedulable...

[105] Geometrically engineered organoid units and their assembly for pre-construction of organ structures

Ayaka Kadotani, ..., and Daisuke Yoshino. APL Bioengineering, 2024. 1 citations.
1% Topic Match
Abstract: Regenerative medicine is moving from the nascent to the transitional stage as researchers are actively engaged in creating mini-organs from pluripotent
stem cells to construct artificial models of physiological and pathological conditions. Currently, mini-organs can express higher-order functions, but their size is
limited to the order of a few millimeters. Therefore, one of the ultimate goals of regenerative medicine, “organ replication and transplantation with organoid,” remains
a major obstacle. 3D bioprinting technology is expected to be an innovative breakthrough in this field, but various issues have been raised, such as cell damage,
versatility of bioink, and printing time. In this...

[106] Bioprinting of Cells, Organoids and Organs-on-a-Chip Together with Hydrogels Improves Structural and Mechanical Cues

C. Mierke. Cells, 2024. 26 citations.
1% Topic Match
Abstract: The 3D bioprinting technique has made enormous progress in tissue engineering, regenerative medicine and research into diseases such as cancer. Apart
from individual cells, a collection of cells, such as organoids, can be printed in combination with various hydrogels. It can be hypothesized that 3D bioprinting will
even become a promising tool for mechanobiological analyses of cells, organoids and their matrix environments in highly defined and precisely structured 3D
environments, in which the mechanical properties of the cell environment can be individually adjusted. Mechanical obstacles or bead markers can be integrated
into bioprinted samples to analyze mechanical deformations and forces...

[107] Bioprinting of Complex Multicellular Organs with Advanced Functionality—Recent Progress and Challenges Ahead

L. Bertassoni. Advanced Materials, 2021. 54 citations.
0% Topic Match
Abstract: Bioprinting has emerged as one of the most promising strategies for fabrication of functional organs in the lab as an alternative to transplant organs.
While progress in the field has mostly been restricted to a few miniaturized tissues with minimal biological functionality until a few years ago, recent progress has
advanced the concept of building three(cid:16)dimensional multicellular organ complexity remarkably. This review discusses a series of milestones that have paved the way
for bioprinting of tissue constructs that have advanced levels of biological and architectural functionality. Critical materials, engineering and biological challenges
that are key to addressing the desirable function...

[108] Tissue geometry drives deterministic organoid patterning
N. Gjorevski, ..., and M. Lutolf. Science, 2022. 350 citations.
0% Topic Match
Abstract: Description Spatial and temporal organoid control Stem cell–derived organoids form through self-organization and serve as models for organ development,
function, and disease, with potential applications in drug development and personalized medicine. However, in the absence of external guidance, developmental
processes are stochastic, resulting in variable end products that differ significantly from the native organ. Gjorevski et al. developed approaches for specifying the
initial organoid geometry to build intestinal organoids of defined shape, size, and cell distributions, forming structures that are predictable, more similar to normal
organs, and reproducible (see the Perspective by Huycke and Gartner). These methods identify symmetry-breaking mechanisms...

[109] One-step fabrication of an organ-on-a-chip with spatial heterogeneity using a 3D bioprinting technology.

Hyungseok Lee and D. Cho. Lab on a chip, 2016. 282 citations.
0% Topic Match
Abstract: Although various types of organs-on-chips have been introduced recently as tools for drug discovery, the current studies are limited in terms of fabrication
methods. The fabrication methods currently available not only need a secondary cell-seeding process and result in severe protein absorption due to the material
used, but also have difficulties in providing various cell types and extracellular matrix (ECM) environments for spatial heterogeneity in the organs-on-chips. Therefore,
in this research, we introduce a novel 3D bioprinting method for organ-on-a-chip applications. With our novel 3D bioprinting method, it was possible to prepare an
organ-on-a-chip in a simple one-step fabrication process....

[110] 3D cell cultures toward quantitative high-throughput drug screening.

Yichun Wang and H. Jeon. Trends in pharmacological sciences, 2022. 81 citations.
0% Topic Match
No summary or abstract available

[111] A Microfluidic Cell Printer for Bio-Fabrication

Panzhe Xiao, ..., and Yifan Liu. 2025 IEEE 20th International Conference on Nano/Micro Engineered and Molecular Systems (NEMS), 2025. 0
citations.
0% Topic Match
Abstract: Biological systems such as organoids are three-dimensional structures formed through the self-organization of stem cells or organ-specific progenitor cells,
exhibiting functions similar to those of in vivo organs. Despite their significant applications in disease modeling, the cultivation of organoids faces challenges, such
as the inability to control the number and spatial arrangement of starting cells precisely. This study develops a microfluidic cell printer with single-cell resolution. By
introducing a voltage comparator and a DC power supply, the inversion of selection logic and the control of electrical signal output can be achieved without custom
hardware or software rewriting. This approach reduces...

[112] Human organs-on-chips for disease modelling, drug development and personalized medicine

D. Ingber. Nature Reviews. Genetics, 2022. 878 citations.
0% Topic Match
Abstract: The failure of animal models to predict therapeutic responses in humans is a major problem that also brings into question their use for basic research.
Organ-on-a-chip (organ chip) microfluidic devices lined with living cells cultured under fluid flow can recapitulate organ-level physiology and pathophysiology with
high fidelity. Here, I review how single and multiple human organ chip systems have been used to model complex diseases and rare genetic disorders, to study
host–microbiome interactions, to recapitulate whole-body inter-organ physiology and to reproduce human clinical responses to drugs, radiation, toxins and infectious
pathogens. I also address the challenges that must be overcome...

[113] Subtractive manufacturing with swelling induced stochastic folding of sacrificial materials for fabricating complex perfusable tissues in multi-well
plates.

Shravanthi Rajasekar, ..., and Boyang Zhang. Lab on a chip, 2022. 9 citations.
0% Topic Match
Abstract: Organ-on-a-chip systems that recapitulate tissue-level functions have been proposed to improve in vitro-in vivo correlation in drug development. Significant
progress has been made to control the cellular microenvironment with mechanical stimulation and fluid flow. However, it has been challenging to introduce complex
3D tissue structures due to the physical constraints of microfluidic channels or membranes in organ-on-a-chip systems. Inspired by 4D bioprinting, we develop a
subtractive manufacturing technique where a flexible sacrificial material can be patterned on a 2D surface, swell and shape change when exposed to aqueous
hydrogel, and subsequently degrade to produce perfusable networks in a natural hydrogel...

[114] Hybrid 3D Bioprinting of Sustainable Biomaterials for Advanced Multiscale Tissue Engineering.

Xuejiao Ma, ..., and Qian Wu. Small, 2025. 7 citations.
0% Topic Match

Abstract: 3D printing has greatly improved the precision of cell and biomaterial placement, enabling accurate reproduction of tissue models with sustainable potential.
Various techniques, including inkjet printing, extrusion-based printing, and vat photopolymerization, offer unique advantages but often fail to replicate the full

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 34/41

Undermind

REPORT CREATED ON
11/22/2025

complexity of native tissues because of material and scalability limitations. Hybrid 3D bioprinting, combining multiple techniques in a single process, has shown
great potential in creating complex tissue models with multifunctional capabilities, ranging from patient-specific implant fabrication to full-scale organ development.
It capitalizes on the strengths of multiple techniques, enabling the integration of sustainable, renewable biomaterials at varying resolutions,...

[115] Bioengineering methods for organoid systems

Jad Saleh, ..., and W. Xi. Biology of the Cell, 2021. 11 citations.
0% Topic Match
Abstract: Organoids have been widely used in fundamental, biomimetic, and therapeutic studies. These multicellular systems form via cell(cid:16)autonomous self(cid:16)orga-
nization where a cohort of stem cells undergoes in vivo(cid:16)like proliferation, differentiation, and morphogenesis. They also recapitulate a series of physiological cell
organization, complexity and functions that are untouchable by conventional bio(cid:16)model systems using immortal cell lines. However, the development of organoids
is often not easily controlled and their shape and size are yet fully physiological. Recent research has demonstrated that multiple bioengineering tools could be
harnessed to control important internal and external cues that dictate stem cell behavior and stem(cid:16)cell based organoid...

[116] Novel Strategies in Artificial Organ Development: What Is the Future of Medicine?

M. Klak, ..., and M. WszoBa. Micromachines, 2020. 25 citations.
0% Topic Match
Abstract: The technology of tissue engineering is a rapidly evolving interdisciplinary field of science that elevates cell-based research from 2D cultures through
organoids to whole bionic organs. 3D bioprinting and organ-on-a-chip approaches through generation of three-dimensional cultures at different scales, applied
separately or combined, are widely used in basic studies, drug screening and regenerative medicine. They enable analyses of tissue-like conditions that yield much
more reliable results than monolayer cell cultures. Annually, millions of animals worldwide are used for preclinical research. Therefore, the rapid assessment of drug
efficacy and toxicity in the early stages of preclinical testing can significantly reduce the...

[117] Biomaterial-Guided Organoid Engineering for Modeling Development and Diseases

Plansky Hoang and Zhen Ma. Bioengineering eJournal, 2020. 0 citations.
0% Topic Match
Abstract: Organoids are miniature models of organs to recapitulate spatiotemporal cellular organization and tissue functionality. The production of organoids has
revolutionized the field of developmental biology, providing the possibility to study and guide human development and diseases in a dish. More recently, novel
bio-material-based culture systems demonstrated the feasibility and versatility to engineer and produce the organoids in a consistent and reproducible manner.
By engineering proper tissue micro-environment, functional organoids have been able to exhibit spatial-distinct tissue patterning and morphogenesis. This review
will focus on enabling technologies in the field of organoid engineering, including chemical-defined hydrogels, micro-fabrication techniques and organoid-on-chip
platforms,...

[118] Organ-Specific Strategies in Bioprinting: Addressing Translational Challenges in the Heart, Liver, Kidney, and Pancreas

Mohamad Al Qassab, ..., and Hilda E. Ghadieh. Journal of Functional Biomaterials, 2025. 1 citations.
0% Topic Match
Abstract: Organ bioprinting is a rapidly evolving field designed to address the persistent shortage of donor organs by engineering patient-specific tissues
that replicate the function and structure of natural organs. Despite significant technological advancements, bioprinting still faces major obstacles, including
tissue rejection, inadequate vascularization, limited physiological functionality, and various ethical and translational challenges. In this review, we assess current
bioprinting modalities, particularly extrusion-based printing, inkjet printing, laser-assisted bioprinting (LAB), and stereolithography/digital light processing (SLA/DLP),
highlighting their individual strengths and limitations. We also explore different bioink formulations, focusing especially on hybrid bioinks as promising solutions to
traditional bioink constraints. Additionally, this article...

[119] Development and Applications of Organoids in Gynecological Diseases

Jian Yang, ..., and Wenyan Wang. Stem Cell Reviews and Reports, 2024. 1 citations.
0% Topic Match
Abstract: Organoids are rapidly self-organizing 3D in vitro cultures derived from pluripotent stem cells (PSCs) or adult stem cells (ASCs) that possess disease-like
characteristics with high success rates. Due to their ability to retain tissue structure, biological phenotypes, and genetic information, they have been utilized as
a novel in vitro model for disease research. In recent years, scientists have established self-organizing 3D organoids for human endometrium, fallopian tubes,
ovaries, and cervix by culturing stem cells with cytokines in 3D scaffolds. The integration of organoids with animal models, organ-on-a-chip systems, and 3D printing
technologies offers a novel preclinical model for exploring disease...

[120] Bioprinting 3D microfibrous scaffolds for engineering endothelialized myocardium and heart-on-a-chip.

Y. S. Zhang, ..., and A. Khademhosseini. Biomaterials, 2016. 778 citations.
0% Topic Match
No summary or abstract available

[121] Research progress of organoids-on-chips in biomedical application

Qian Wu, ..., and Ping Wang. Chinese Science Bulletin, 2019. 5 citations.
0% Topic Match
Abstract: Drug screening is traditionally based on the pharmacodynamic models from 2D cell culture or animal experiments. However, these models suffer from
poor drug efficacy prediction due to their difference from human in vivo cell microenvironments. In recent years, advances in biotechnology and tissue engineering
have enabled rapid growth of in vitro organoid culturing. These organoids cultured in matrigel can mimic human in vivo cell microenvironment and physiology more
accurately than traditional 2D cell culture and animal models. Among them, tumor organoids, especially patient-derived tumour organoids, can be applied as effective
cancer models for drug screening and personalized medicine. By integrating...

[122] AI(cid:16)organoid integrated systems for biomedical studies and applications

Sudhiksha Maramraju, ..., and Huaxiao Yang. Bioengineering & Translational Medicine, 2024. 29 citations.
0% Topic Match
Abstract: Abstract In this review, we explore the growing role of artificial intelligence (AI) in advancing the biomedical applications of human pluripotent stem cell
(hPSC)(cid:16)derived organoids. Stem cell(cid:16)derived organoids, these miniature organ replicas, have become essential tools for disease modeling, drug discovery, and
regenerative medicine. However, analyzing the vast and intricate datasets generated from these organoids can be inefficient and error(cid:16)prone. AI techniques offer a
promising solution to efficiently extract insights and make predictions from diverse data types generated from microscopy images, transcriptomics, metabolomics,
and proteomics. This review offers a brief overview of organoid characterization and fundamental concepts in AI while...

[123] Organ-on-a-Chip: Ubi sumus? Fundamentals and Design Aspects

Ana Sofia Morais, ..., and Carla Vitorino. Pharmaceutics, 2024. 8 citations.
0% Topic Match
Abstract: This review outlines the evolutionary journey from traditional two-dimensional (2D) cell culture to the revolutionary field of organ-on-a-chip technology.
Organ-on-a-chip technology integrates microfluidic systems to mimic the complex physiological environments of human organs, surpassing the limitations of
conventional 2D cultures. This evolution has opened new possibilities for understanding cell–cell interactions, cellular responses, drug screening, and disease
modeling. However, the design and manufacture of microchips significantly influence their functionality, reliability, and applicability to different biomedical applications.
Therefore, it is important to carefully consider design parameters, including the number of channels (single, double, or multi-channels), the channel shape, and the
biological context....

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 35/41

Undermind

REPORT CREATED ON
11/22/2025

[124] Cancer modeling meets human organoid technology

D. Tuveson and H. Clevers. Science, 2019. 713 citations.
0% Topic Match
Abstract: Organoids are microscopic self-organizing, three-dimensional structures that are grown from stem cells in vitro. They recapitulate many structural and
functional aspects of their in vivo counterpart organs. This versatile technology has led to the development of many novel human cancer models. It is now possible to
create indefinitely expanding organoids starting from tumor tissue of individuals suffering from a range of carcinomas. Alternatively, CRISPR-based gene modification
allows the engineering of organoid models of cancer through the introduction of any combination of cancer gene alterations to normal organoids. When combined
with immune cells and fibroblasts, tumor organoids become models for the...

[125] Advances and applications of organoid-on-a-chip in disease modeling.

Yujia Yang, ..., and Xuesong Qian. The Analyst, 2025. 0 citations.
0% Topic Match
Abstract: Recent studies have emphasized the ability of organoids, a class of self-organizing mini-organs derived from various cell sources and tissue biopsies,
to faithfully replicate the main anatomical features and physiological traits of internal organs. Because of the numerous avenues this technology has opened
for biomedical research, there is a growing need for creative engineering approaches to create, manufacture, manipulate, and study organoids and their
microenvironments. This review covers the most recent developments in disease modeling for both the organoid-on-a-chip and the more recent, more sophisticated
multiorgan-on-a-chip platforms. These technologies have the potential to significantly influence a few growing biomedical domains,...

[126] “A novel Organ-Chip system emulates three-dimensional architecture of the human epithelia and allows fine control of mechanical forces acting
on it.”

A. Varone, ..., and C. Hinojosa. bioRxiv, 2020. 0 citations.
0% Topic Match
Abstract: Successful translation of in vivo experimental data to human patients is an unmet need and a bottleneck in the development of effective therapeutics. micro
technology aims to address this need with significant advancements reported recently that enable modeling of organ level function. These microengineered chips
enable researcher to recreate critical elements such as in vivo relevant tissue-tissue interface, air-liquid interface, and mechanical forces, such as mechanical stretch
and fluidic shear stress, are crucial in emulating tissue level functions. Here, we present the development of a new, comprehensive 3D cell-culture system, where
we combined our proprietary Organ-Chip technology with recent advantages...

[127] Organoid research: Theory, technology, and therapeutics

Long Bai, ..., and Changsheng Liu. Organoid Research, 2025. 9 citations.
0% Topic Match
Abstract: Organoids are 3D cellular constructs formed through in vitro assembly and stem cell self-organization, recapitulating key features of human tissues with
physiological relevance far exceeding traditional 2D cultures and animal models. Their ability to mimic tissue-specific architecture, cellular diversity, and functional
dynamics has driven transformative advances in biomedical research, spanning disease modeling, drug discovery, and regenerative medicine. In recent years,
significant progress in organoid technology has been achieved, driven by innovations such as organoid bioprinting, highlighting the need for a dedicated academic
platform. In response, we established Organoid Research, a journal committed to advancing this rapidly evolving field through the...

[128] Modeling Human Nonalcoholic Fatty Liver Disease (NAFLD) with an Organoids-on-a-Chip System.

Yaqing Wang, ..., and J. Qin. ACS biomaterials science & engineering, 2020. 82 citations.
0% Topic Match
Abstract: Nonalcoholic fatty liver disease (NAFLD) is a common metabolic and progressive disease, which has emerged as a major cause of chronic liver disease
worldwide. It is characterized by the process ranging from simple steatosis to nonalcoholic steatohepatitis. However, a deep understanding of NAFLD progression
remains challenging due to the lack of proper in vitro human disease models. In this work, we proposed a new strategy to establish a human NAFLD model based on
a human-induced pluripotent stem cell (hiPSC)-derived liver organoids-on-a-chip system. This system allows us to characterize the pathological features of NAFLD
in liver organoids by exposure to free...

[129] Development and Application of Brain Region–Specific Organoids for Investigating Psychiatric Disorders

Zhijian Zhang, ..., and G. Ming. Biological Psychiatry, 2022. 23 citations.
0% Topic Match
No summary or abstract available

[130] Advancements in Organoid(cid:16)Based Drug Discovery: Revolutionizing Precision Medicine and Pharmacology

Dilpreet Singh, ..., and Akshay Kumar. Drug Development Research, 2025. 5 citations.
0% Topic Match
Abstract: Organoids, 3D cellular models derived from stem cells, have revolutionized drug testing by providing human(cid:16)relevant systems for modeling diseases and
testing drug efficacy. Unlike traditional 2D cell cultures or animal models, organoids closely resemble the complex architecture and function of human tissues,
offering more accurate predictions of drug responses. Researchers are increasingly utilizing these models in oncology, neurology, liver toxicity, and personalized
medicine. Recent advances in gene editing (e.g., CRISPR(cid:16)Cas9), multi(cid:16)omics technologies, and organoid(cid:16)on(cid:16)chip systems have further enhanced the capabilities of
organoids in drug discovery. CRISPR(cid:16)Cas9 allows for precise modeling of genetic disorders, while multi(cid:16)omics approaches integrate transcriptomics, proteomics,
and...

[131] Organoids: Principle, application and perspective

Kaizheng Liu, ..., and Changshun Ruan. The Innovation Life, 2024. 5 citations.
0% Topic Match
Abstract: Organoid technology, a notable advancement in biomedical engineering, has emerged over the past decade, offering significant scientific and therapeutic
potential. By accurately mimicking the structural and functional intricacies of human organs at a small scale, organoids have become a groundbreaking tool for
exploring basic biological principles, understanding disease mechanisms, and progressing regenerative medicine. Despite the large number of relevant reports, a
comprehensive summary of current organoid research updates is needed urgently for interdisciplinary researchers with an interest in constructing biomimetic tissue
models. This review presents a thorough look at the diverse fields of organoid research, covering the fundamental principles guiding...

[132] Analysis of organoid and immune cell co-cultures by machine learning-empowered image cytometry

Philipp Stüve, ..., and Uwe Ritter. Frontiers in Medicine, 2024. 6 citations.
0% Topic Match
Abstract:  Organoids are three-dimensional (3D) structures that can be derived from stem cells or adult tissue progenitor cells and exhibit an extraordinary ability
to autonomously organize and resemble the cellular composition and architectural integrity of specific tissue segments. This feature makes them a useful tool
for analyzing therapeutical relevant aspects, including organ development, wound healing, immune disorders and drug discovery. Most organoid models do not
contain cells that mimic the neighboring tissue’s microenvironment, which could potentially hinder deeper mechanistic studies. However, to use organoid models in
mechanistic studies, which would enable us to better understand pathophysiological processes, it is necessary...

[133] Single Lgr5 stem cells build crypt–villus structures in vitro without a mesenchymal niche

Toshiro Sato, ..., and H. Clevers. Nature, 2009. 6280 citations.
0% Topic Match
No summary or abstract available

[134] Vascularized human cortical organoids (vOrganoids) model cortical development in vivo

Yingchao Shi, ..., and Xiaoqun Wang. PLoS Biology, 2020. 278 citations.
0% Topic Match
Abstract: Modeling the processes of neuronal progenitor proliferation and differentiation to produce mature cortical neuron subtypes is essential for the study of
human brain development and the search for potential cell therapies. We demonstrated a novel paradigm for the generation of vascularized organoids (vOrganoids)
consisting of typical human cortical cell types and a vascular structure for over 200 days as a vascularized and functional brain organoid model. The observation of

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 36/41

Undermind

REPORT CREATED ON
11/22/2025

spontaneous excitatory postsynaptic currents (sEPSCs), spontaneous inhibitory postsynaptic currents (sIPSCs), and bidirectional electrical transmission indicated
the presence of chemical and electrical synapses in vOrganoids. More importantly, single-cell RNA-sequencing analysis illustrated that...

[135] Organ-on-chip models: new opportunities for biomedical research

A. Mosig. Future Science OA, 2016. 33 citations.
0% Topic Match
Abstract: Animal models are frequently used in biomedical research. However, recently a controversial debate about the transferability of data obtained in
mouse models to human conditions emerged. Although cell-based in vitro approaches can be an alternative, conventional cell culture methods hardly reflect
cellular cross-communication and neglect essential physiological parameters. Biochipembedded tissue culture allows an optimal supply with nutrients and oxygen,
an efficient removal of catabolic metabolites, and enables a physiological cell polarization and communication within tissues creating a complex physiological
microenvironment in vitro. The combination of animal as well as human organ-on-chip with reliable in vivo models will create new possibilities...

[136] Advances, challenges and future applications of liver organoids in experimental regenerative medicine

Da Gong, ..., and Xuesong Deng. Frontiers in Medicine, 2025. 2 citations.
0% Topic Match
Abstract: The liver is a vital organ responsible for numerous metabolic processes in the human body, including the metabolism of drugs and nutrients. After liver
damage, the organ can rapidly return to its original size if the causative factor is promptly eliminated. However, when the harmful stimulus persists, the liver’s
regenerative capacity becomes compromised. Substantial theoretical feasibility has been demonstrated at the levels of gene expression, molecular interactions,
and intercellular dynamics, complemented by numerous successful animal studies. However, a robust model and carrier that closely resemble human physiology
are still lacking for translating these theories into practice. The potential for liver...

[137] 3D Bioprinting- An Advanced Manufacturing Process for Healthcare Applications

Prosenjit Saha, ..., and Pooja Ghosh. Innovation of Chemistry &amp; Materials for Sustainability, 2025. 0 citations.
0% Topic Match
Abstract: 3D bioprinting is a cutting-edge technique used to create intricate mechanical and biological structures. It was developed to impart few advanced features
to the process of biomanufacturing mainly for healthcare applications. This state-of-the-art technique is a viable alternative for the manufacturing of complex 3D
biological scaffolds employing different bioinks/ biomaterial inks that improves the ability significantly to solve the shortcomings adhering to the traditional 2D
biomanufacturing processes. Despite enormous advances of 3D bioprinting technology, the clinical translations of this technique are still constrained by several
important issues such as restricted biocompatibility, fragile mechanical strength, and insufficient printability. Replicating native tissue...

[138] Artificial Intelligence for Organoids Multidimensional Assessment

Yulin Mo, ..., and Jiachan Su. SmartMat, 2025. 1 citations.
0% Topic Match
Abstract: Organoids are tissue analogues formed through in vitro three(cid:16)dimensional culture of stem cells, possessing specific spatial structures. Organoids have
become integral to various biomedical fields, including disease pathogenesis, model construction, regenerative and precision medicine, drug screening, tissue
and organ development, toxicology, and pathological analysis. However, the diversity of organoid types and variations in their production processes have led to
inconsistencies in their application for assessment and analysis. To date, no comprehensive standards or guidelines for evaluating organoids have been established.
Artificial intelligence (AI) technology is extensively employed in biomedical image analysis, data processing, and molecular structure prediction, demonstrating
benefits in...

[139] Brain organoid model systems of neurodegenerative diseases: recent progress and future prospects

Saniyah Shaikh, ..., and Ahmed Yaqinuddin. Frontiers in Neuroscience, 2025. 2 citations.
0% Topic Match
Abstract: Neurological diseases are a leading cause of disability, morbidity, and mortality, affecting 43% of the world’s population. The detailed study of neurological
diseases, testing of drugs, and repair of site-specific defects require physiologically relevant models that recapitulate key events and dynamic neurodevelopmental
processes in a highly organized fashion. As an evolving technology, self-organizing and self-assembling brain organoids offer the advantage of modeling different
stages of brain development in a 3D microenvironment. Herein, we review the utility, advantages, and limitations of the latest breakthroughs in brain organoid
endeavors in the context of modeling three of the most prevalent neurodegenerative diseases—Alzheimer’s, Parkinson’s,...

[140] Stem cells for organoids

Shutong Qian, ..., and Xiaoming Sun. Smart Medicine, 2022. 13 citations.
0% Topic Match
Abstract: Abstract Organoids are three(cid:16)dimensional (3D) cell culture systems that simulate the structures and functions of organs, involving applications in disease
modeling, drug screening, and cellular developmental biology. The material matrix in organoids can provide a 3D environment for stem cells to differentiate into
different cell types and continuously self(cid:16)renew, thereby realizing the in vitro culture of organs, which has received extensive attention in recent years. However,
some challenges still exist in organoids, including low maturity, high heterogeneity, and lack of spatiotemporal regulation. Therefore, in this review, we summarized
the culturing protocols and various applications of stem cell(cid:16)derived organoids and proposed...

[141] Imaging-guided deep tissue in vivo sound printing.

Elham Davoodi, ..., and Wei Gao. Science, 2025. 21 citations.
Not measured Topic Match
Abstract: Three-dimensional printing offers promise for patient-specific implants and therapies but is often limited by the need for invasive surgical procedures. To
address this, we developed an imaging-guided deep tissue in vivo sound printing (DISP) platform. By incorporating cross-linking agent-loaded low-temperature-sen-
sitive liposomes into bioinks, DISP enables precise, rapid, on-demand cross-linking of diverse functional biomaterials using focused ultrasound. Gas vesicle-based
ultrasound imaging provides real-time monitoring and allows for customized pattern creation in live animals. We validated DISP by successfully printing near diseased
areas in the mouse bladder and deep within rabbit leg muscles in vivo, demonstrating its potential for localized drug delivery...

[142] Organogenesis in a dish: Modeling development and disease using organoid technologies

Madeline A. Lancaster and J. Knoblich. Science, 2014. 2403 citations.
Not measured Topic Match
No summary or abstract available

[143] Progress and potential in organoid research

Giuliana Rossi, ..., and M. Lutolf. Nature Reviews Genetics, 2018. 897 citations.
Not measured Topic Match
No summary or abstract available

[144] Multisensor-integrated organs-on-chips platform for automated and continual in situ monitoring of organoid behaviors

Y. S. Zhang, ..., and A. Khademhosseini. Proceedings of the National Academy of Sciences, 2017. 679 citations.
Not measured Topic Match
No summary or abstract available

[145] Hydrogel-in-hydrogel live bioprinting for guidance and control of organoids and organotypic cultures

A. Urciuolo, ..., and N. Elvassore. Nature Communications, 2023. 82 citations.
Not measured Topic Match
Abstract: Three-dimensional hydrogel-based organ-like cultures can be applied to study development, regeneration, and disease in vitro. However, the control of
engineered hydrogel composition, mechanical properties and geometrical constraints tends to be restricted to the initial time of fabrication. Modulation of hydrogel
characteristics over time and according to culture evolution is often not possible. Here, we overcome these limitations by developing a hydrogel-in-hydrogel live
bioprinting approach that enables the dynamic fabrication of instructive hydrogel elements within pre-existing hydrogel-based organ-like cultures. This can be
achieved by crosslinking photosensitive hydrogels via two-photon absorption at any time during culture. We show that instructive hydrogels guide...

[146] Flow-enhanced vascularization and maturation of kidney organoids in vitro

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 37/41

Undermind

REPORT CREATED ON
11/22/2025

Kimberly A. Homan, ..., and Ryuji Morizane. Nature methods, 2018. 702 citations.
Not measured Topic Match
Abstract: Kidney organoids derived from human pluripotent stem cells have glomerular- and tubular-like compartments that are largely avascular and immature in
static culture. Here we report an in vitro method for culturing kidney organoids under flow on millifluidic chips, which expands their endogenous pool of endothelial
progenitor cells and generates vascular networks with perfusable lumens surrounded by mural cells. We found that vascularized kidney organoids cultured under flow
had more mature podocyte and tubular compartments with enhanced cellular polarity and adult gene expression compared with that in static controls. Glomerular
vascular development progressed through intermediate stages akin to those involved in...

[147] Organoids

Zixuan Zhao, ..., and Hanry Yu. Nature Reviews Methods Primers, 2022. 493 citations.
Not measured Topic Match
Abstract: Organoids are simple tissue-engineered cell-based in vitro models that recapitulate many aspects of the complex structure and function of the
corresponding in vivo tissue. They can be dissected and interrogated for fundamental mechanistic studies on development, regeneration and repair in human tissues,
and can also be used in diagnostics, disease modelling, drug discovery and personalized medicine. Organoids are derived from either pluripotent or tissue-resident
stem (embryonic or adult) or progenitor or differentiated cells from healthy or diseased tissues, such as tumours. To date, numerous organoid engineering strategies
that support organoid culture and growth, proliferation, differentiation and maturation have been reported....

[148] 3D bioprinting of high cell-density heterogeneous tissue models through spheroid fusion within self-healing hydrogels

Andrew C. Daly, ..., and J. Burdick. Nature Communications, 2020. 343 citations.
Not measured Topic Match
Abstract: Cellular models are needed to study human development and disease in vitro, and to screen drugs for toxicity and efficacy. Current approaches are
limited in the engineering of functional tissue models with requisite cell densities and heterogeneity to appropriately model cell and tissue behaviors. Here, we
develop a bioprinting approach to transfer spheroids into self-healing support hydrogels at high resolution, which enables their patterning and fusion into high-cell
density microtissues of prescribed spatial organization. As an example application, we bioprint induced pluripotent stem cell-derived cardiac microtissue models
with spatially controlled cardiomyocyte and fibroblast cell ratios to replicate the structural and...

[149] Creation of bladder assembloids mimicking tissue regeneration and cancer

Eunjee Kim, ..., and Kunyoo Shin. Nature, 2020. 197 citations.
Not measured Topic Match
No summary or abstract available

[150] Recapitulating macro-scale tissue self-organization through organoid bioprinting
Jonathan A. Brassard, ..., and M. Lutolf. Nature Materials, 2020. 355 citations.
Not measured Topic Match
No summary or abstract available

[151] Disease Modeling in Stem Cell-Derived 3D Organoid Systems.

Devanjali Dutta, ..., and H. Clevers. Trends in molecular medicine, 2017. 693 citations.
Not measured Topic Match
No summary or abstract available

[152] Evaluation of variability in human kidney organoids

B. Phipson, ..., and M. Little. Nature Methods, 2018. 215 citations.
Not measured Topic Match
No summary or abstract available

[153] Homeostatic mini-intestines through scaffold-guided organoid morphogenesis

M. Nikolaev, ..., and M. Lutolf. Nature, 2020. 561 citations.
Not measured Topic Match
No summary or abstract available

[154] Microfluidic device with brain extracellular matrix promotes structural and functional maturation of human brain organoids

Ann-Na Cho, ..., and Seung(cid:16)Woo Cho. Nature Communications, 2021. 261 citations.
Not measured Topic Match
Abstract: Brain organoids derived from human pluripotent stem cells provide a highly valuable in vitro model to recapitulate human brain development and
neurological diseases. However, the current systems for brain organoid culture require further improvement for the reliable production of high-quality organoids.
Here, we demonstrate two engineering elements to improve human brain organoid culture, (1) a human brain extracellular matrix to provide brain-specific cues and
(2) a microfluidic device with periodic flow to improve the survival and reduce the variability of organoids. A three-dimensional culture modified with brain extracellular
matrix significantly enhanced neurogenesis in developing brain organoids from human induced pluripotent...

[155] Integrating organoids and organ-on-a-chip devices

Yimu Zhao, ..., and M. Radiši(cid:7). Nature Reviews Bioengineering, 2024. 72 citations.
Not measured Topic Match
No summary or abstract available

[156] Merging organoid and organ-on-a-chip technology to generate complex multi-layer tissue models in a human retina-on-a-chip platform

K. Achberger, ..., and P. Loskill. eLife, 2019. 267 citations.
Not measured Topic Match
Abstract: The devastating effects and incurable nature of hereditary and sporadic retinal diseases such as Stargardt disease, age-related macular degeneration
or retinitis pigmentosa urgently require the development of new therapeutic strategies. Additionally, a high prevalence of retinal toxicities is becoming more and
more an issue of novel targeted therapeutic agents. Ophthalmologic drug development, to date, largely relies on animal models, which often do not provide results
that are translatable to human patients. Hence, the establishment of sophisticated human tissue-based in vitro models is of upmost importance. The discovery of
self-forming retinal organoids (ROs) derived from human embryonic stem cells (hESCs) or...

[157] High-Throughput Screening Enhances Kidney Organoid Differentiation from Human Pluripotent Stem Cells and Enables Automated Multidi-
mensional Phenotyping.

Stefan M. Czerniecki, ..., and Benjamin S. Freedman. Cell stem cell, 2018. 365 citations.
Not measured Topic Match
No summary or abstract available

[158] The upcoming 3D-printing revolution in microfluidics.

N. Bhattacharjee, ..., and A. Folch. Lab on a chip, 2016. 854 citations.
Not measured Topic Match
No summary or abstract available

[159] Robotics-Driven Manufacturing of Cartilaginous Microtissues for Skeletal Tissue Engineering Applications

Isaak Decoene, ..., and I. Papantoniou. Stem Cells Translational Medicine, 2024. 4 citations.
Not measured Topic Match

Abstract: Abstract Automated technologies are attractive for enhancing the robust manufacturing of tissue-engineered products for clinical translation. In this work,
we present an automation strategy using a robotics platform for media changes, and imaging of cartilaginous microtissues cultured in static microwell platforms.

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 38/41

Undermind

REPORT CREATED ON
11/22/2025

We use an automated image analysis pipeline to extract microtissue displacements and morphological features as noninvasive quality attributes. As a result, empty
microwells were identified with a 96% accuracy, and dice coefficient of 0.84 for segmentation. Design of experiment are used for the optimization of liquid handling
parameters to minimize empty microwells during long-term differentiation protocols. We found no...

[160] Individual brain organoids reproducibly form cell diversity of the human cerebral cortex

Silvia Velasco, ..., and P. Arlotta. Nature, 2019. 798 citations.
Not measured Topic Match
Abstract: Experimental models of the human brain are needed for basic understanding of its development and disease1. Human brain organoids hold unprecedented
promise for this purpose; however, they are plagued by high organoid-to-organoid variability2,3. This has raised doubts as to whether developmental processes of
the human brain can occur outside the context of embryogenesis with a degree of reproducibility that is comparable to the endogenous tissue. Here we show that
an organoid model of the dorsal forebrain can reliably generate a rich diversity of cell types appropriate for the human cerebral cortex. We performed single-cell
RNA-sequencing analysis of 166,242 cells isolated...

[161] Latest Trends in Biosensing for Microphysiological Organs-on-a-Chip and Body-on-a-Chip Systems

S. R. Kratz, ..., and M. Rothbauer. Biosensors, 2019. 76 citations.
Not measured Topic Match
Abstract: Organs-on-chips are considered next generation in vitro tools capable of recreating in vivo like, physiological-relevant microenvironments needed to cultivate
3D tissue-engineered constructs (e.g., hydrogel-based organoids and spheroids) as well as tissue barriers. These microphysiological systems are ideally suited to
(a) reduce animal testing by generating human organ models, (b) facilitate drug development and (c) perform personalized medicine by integrating patient-derived
cells and patient-derived induced pluripotent stem cells (iPSCs) into microfluidic devices. An important aspect of any diagnostic device and cell analysis platform,
however, is the integration and application of a variety of sensing strategies to provide reliable, high-content information on...

[162] Human Brain Organoids on a Chip Reveal the Physics of Folding

Eyal Karzbrun, ..., and O. Reiner. Nature physics, 2018. 335 citations.
Not measured Topic Match
Abstract: Human brain wrinkling has been implicated in neurodevelopmental disorders and yet its origins remain unknown. Polymer gel models suggest that wrinkling
emerges spontaneously due to compression forces arising during differential swelling, but these ideas have not been tested in a living system. Here, we report the
appearance of surface wrinkles during the in vitro development and self-organization of human brain organoids in a microfabricated compartment that supports in
situ imaging over a timescale of weeks. We observe the emergence of convolutions at a critical cell density and maximal nuclear strain, which are indicative of a
mechanical instability. We identify two...

[163] Analytics in Extrusion-Based Bioprinting: Standardized Methods Improving Quantification and Comparability of the Performance of Bioinks

Svenja Strauß, ..., and J. Hubbuch. Polymers, 2023. 9 citations.
Not measured Topic Match
Abstract: Three-dimensional bioprinting and especially extrusion-based printing as a most frequently employed method in this field is constantly evolving as a
discipline in regenerative medicine and tissue engineering. However, the lack of relevant standardized analytics does not yet allow an easy comparison and transfer
of knowledge between laboratories regarding newly developed bioinks and printing processes. This work revolves around the establishment of a standardized
method, which enables the comparability of printed structures by controlling for the extrusion rate based on the specific flow behavior of each bioink. Furthermore,
printing performance was evaluated by image-processing tools to verify the printing accuracy for...

[164] A bioprinted human-glioblastoma-on-a-chip for the identification of patient-specific responses to chemoradiotherapy

H. Yi, ..., and D. Cho. Nature Biomedical Engineering, 2019. 469 citations.
Not measured Topic Match
No summary or abstract available

[165] Keeping It Organized: Multicompartment Constructs to Mimic Tissue Heterogeneity

Alvaro Sanchez-Rubio, ..., and M. Salmerón-Sánchez. Advanced Healthcare Materials, 2023. 18 citations.
Not measured Topic Match
Abstract: Tissue engineering aims at replicating tissues and organs to develop applications in vivo and in vitro. In vivo, by engineering artificial constructs using
functional materials and cells to provide both physiological form and function. In vitro, by engineering three(cid:16)dimensional (3D) models to support drug discovery
and enable understanding of fundamental biology. 3D culture constructs mimic cell–cell and cell–matrix interactions and use biomaterials seeking to increase the
resemblance of engineered tissues with its in vivo homologues. Native tissues, however, include complex architectures, with compartmentalized regions of different
properties containing different types of cells that can be captured by multicompartment constructs. Recent...

[166] Osteochondral organoid biofabrication: construction strategies, applications and perspectives

Liwei Fu, ..., and Quanyi Guo. Biofabrication, 2025. 1 citations.
Not measured Topic Match
Abstract: Osteochondral tissue is a functional complex with crosstalk shown to occur between cartilage and subchondral bone, playing a pivotal role in joint
function and mobility. Osteochondral tissue repair has long been an enormous challenge in regenerative medicine and tissue engineering. With the development of
biofabrication and biomaterials innovations, organoid technology, which can mimic the biological architecture and characteristics of organs through the construction
of 3D tissue structures in vitro, provides novel insight into osteochondral (OC) tissue regeneration. This review explores the significance of OC organoid biofabrication
and the related biological structures and functions of the joint OC unit. Furthermore, we...

[167] Advances in 3D Bioprinting and Microfluidics for Organ-on-a-Chip Platforms

N. R. de Barros, ..., and A. C. M. Figueira. Polymers, 2025. 0 citations.
Not measured Topic Match
Abstract: The convergence of 3D bioprinting and microfluidics has revolutionized the development of organ-on-a-chip platforms, offering unprecedented opportunities
in biomedical research and tissue engineering. This comprehensive review delves into the latest advancements in these technologies, highlighting their significance
and transformative potential. The introduction provides an overview of 3D bioprinting, microfluidics, and organ-on-a-chip systems, emphasizing their critical roles in
replicating physiological conditions and enhancing the precision of biomedical studies. The review aims to move beyond fundamental concepts, focusing on recent
innovations and applications that have propelled these technologies to the forefront of research. In the realm of 3D bioprinting, the review explores...

[168] Soft Micromanipulation Robot for Real-Time Adaptive Multimodal Operation.
Zhuowei Li, ..., and Songlin Zhuang. Advanced science, 2025. 0 citations.
Not measured Topic Match
Abstract: Micromanipulation robots hold immense promise for biomedical applications, yet they remain fundamentally limited by three persistent challenges:
cross-scale target heterogeneity, spatially constrained workspaces, and integrated multimodal operation requirements. Here, a soft micromanipulation robot (SMR)
capable of omnidirectional, micrometer-precision manipulation via a hollow multi-notch agonist-antagonist mechanism is presented. Combining ± 180° bending
and 360° rotation for full-angle operation, this bio-inspired design achieves 14 µm positioning accuracy, enabling reliable handling of single-cell-sized objects. The
SMR adapts in situ to sensitive biosamples and limited workspaces, supporting diverse manipulation modes including aspiration, transfer, programmable assembly,
targeted microinjection, and localized cutting of biospecimens. To evaluate...

[169] Artificial Human Blood Vessels for Tissue Engineering

Yi Zhang, ..., and Yan Zu. ACS Materials Letters, 2025. 7 citations.
Not measured Topic Match
No summary or abstract available

[170] Bioprinting for drug screening: A path toward reducing animal testing or redefining preclinical research?

Harshavardhan Budharaju, ..., and Hae-Won Kim. Bioactive Materials, 2025. 1 citations.
Not measured Topic Match

No summary or abstract available

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 39/41

Undermind

REPORT CREATED ON
11/22/2025

[171] Advanced Biomanufacturing Technologies for Micro-physiological Systems

Min Kyeong Kim, ..., and Hyun(cid:16)Wook Kang. International Journal of Precision Engineering and Manufacturing, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[172] Materiobiology in the omics era

Peiran Song, ..., and Jiachan Su. Materials Today Bio, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[173] Liver-on-a-chip: Considerations, advances, and beyond.

Zhenxu Yang, ..., and Ken(cid:16)Tye Yong. Biomicrofluidics, 2022. 18 citations.
Not measured Topic Match
Abstract: The liver is the largest internal organ in the human body with largest mass of glandular tissue. Modeling the liver has been challenging due to its variety of
major functions, including processing nutrients and vitamins, detoxification, and regulating body metabolism. The intrinsic shortfalls of conventional two-dimensional
(2D) cell culture methods for studying pharmacokinetics in parenchymal cells (hepatocytes) have contributed to suboptimal outcomes in clinical trials and drug
development. This prompts the development of highly automated, biomimetic liver-on-a-chip (LOC) devices to simulate native liver structure and function, with the
aid of recent progress in microfluidics. LOC offers a cost-effective and accurate...

[174] Improving tumor microenvironment assessment in chip systems through next-generation technology integration

Daniela Gaebler, ..., and Christopher C W Hughes. Frontiers in Bioengineering and Biotechnology, 2024. 5 citations.
Not measured Topic Match
Abstract: The tumor microenvironment (TME) comprises a diverse array of cells, both cancerous and non-cancerous, including stromal cells and immune cells.
Complex interactions among these cells play a central role in driving cancer progression, impacting critical aspects such as tumor initiation, growth, invasion,
response to therapy, and the development of drug resistance. While targeting the TME has emerged as a promising therapeutic strategy, there is a critical need for
innovative approaches that accurately replicate its complex cellular and non-cellular interactions; the goal being to develop targeted, personalized therapies that
can effectively elicit anti-cancer responses in patients. Microfluidic systems present notable advantages...

[175] Microfluidic informatics - A research paradigm for the future of microfluidics.

Qing Lu, ..., and Xianting Ding. Analytica chimica acta, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[176] Synergies Between Robotics, AI, and Bioengineering—A Narrative Review Concerning the Future of Transplants

Domiziana Picone, ..., and Alberto Fucarino. Applied Biosciences, 2025. 0 citations.
Not measured Topic Match
Abstract: The critical shortage of donor organs remains the foremost challenge in transplantation medicine. Nevertheless, advancements in robotic-assisted surgery
(RAS), artificial intelligence (AI)-enhanced donor–recipient matching, and bioengineering—particularly 3D bioprinting—are revolutionizing the field. Today, RAS has
evolved from an innovative technique into a reliable clinical tool, with evidence indicating that it enhances surgical precision and results in better patient outcomes.
Meanwhile, AI and machine learning are advancing donor–recipient matching and allocation, producing models that offer superior predictive accuracy for graft
survival compared to traditional methods. Additionally, bioengineering strategies, especially 3D bioprinting and tissue engineering, are progressing from the creation
of acellular scaffolds...

[177] Cell-instructive microfibers enable programmable alignment of bioprinted hMSC

A. Neuhäusler, ..., and A. Blaeser. Bioactive Materials, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[178] Exploring the 3D Bioprinting Landscape in the Delivery of Active Pharmaceutical Compounds for Therapeutic and Regenerative Medicine
Applications.

Khonzisizwe Somandi and Y. Choonara. Journal of biomedical materials research. Part B, Applied biomaterials, 2025. 0 citations.
Not measured Topic Match
Abstract: Three-dimensional (3D) bioprinting is transforming the delivery of active pharmaceutical compounds and regenerative medicine by enabling patient-specific
solutions that enhance treatment efficacy and safety. This review explores recent advancements in 3D bioprinting for targeted therapy, focusing on its ability to
fabricate complex delivery systems of drugs, cells, and various biomolecules with controlled and sustained release profiles. By leveraging bioinks with tunable
properties, 3D bioprinting allows for localized drug administration, reducing systemic side effects while improving bioavailability. Additionally, in situ 3D bioprinting
facilitates the direct deposition of therapeutic agents at the site of injury or disease, enhancing precision medicine approaches and...

[179] A pump-free dual unidirectional circulation microfluidic device for tumor spheroid microenvironment modulation and motility analysis

Xiaoqing Chen, ..., and Ling Yu. Microchemical Journal, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[180] Functional substrate-enhanced bioprinting technology for next-generation organ-on-a-chip: from fabrication to functionalization.

G. Lee, ..., and Je(cid:16)Kyun Park. Trends in biotechnology, 2025. 1 citations.
Not measured Topic Match
No summary or abstract available

[181] A practical guide to hydrogel working curves for bioprinting

Rion J. Wendland, ..., and J. Killgore. Additive Manufacturing Letters, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[182] Advances in Infectious Disease Modeling: A perspective on 3D-Bioprinted Tissue Models to Study Host-Pathogen Interactions

Soja Saghar Somana, ..., and Sunil Kumarab. Journal of Veterinary and Animal Sciences, 2025. 1 citations.
Not measured Topic Match
Abstract: Three-dimensional (3D) bioprinting is a revolutionary biomedical technology that allows researchers to create custom 3D tissue models to study human
organ physiology and disease pathobiology. Bioprinting utilizes bioinks containing living cells, biomaterials, and essential growth factors to construct complex, 3D
tissue-like structures with remarkable precision. Their application in infectious disease research is particularly significant, as they replicate organs such as lungs,
liver, skin, and intestines, allowing scientists to analyze pathogen-host interactions at cellular and tissue levels closely. By employing 3D bioprinting, researchers
have successfully developed tissue models to study viral and bacterial infections, offering insights into pathogen evolution, immune responses,...

[183] Recent advances in blood-brain barrier-on-a-chip models.

J. Vetter, ..., and A. Blaeser. Acta biomaterialia, 2025. 5 citations.
Not measured Topic Match
No summary or abstract available

[184] Biotechnological advances in 3D modeling of cancer initiation. Examples from pancreatic cancer research and beyond

C. Handschin, ..., and J. Guillermet(cid:16)Guibert. Biofabrication, 2025. 2 citations.
Not measured Topic Match

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 40/41

Undermind

REPORT CREATED ON
11/22/2025

Abstract: In recent years, biofabrication technologies have garnered significant attention within the scientific community for their potential to create advanced in vitro
cancer models. While these technologies have been predominantly applied to model advanced stages of cancer, there exists a pressing need to develop pertinent,
reproducible, and sensitive 3D models that mimic cancer initiation lesions within their native tissue microenvironment. Such models hold profound relevance for
comprehending the intricacies of cancer initiation, to devise novel strategies for early intervention, and/or to conduct sophisticated toxicology assessments of putative
carcinogens. Here, we will explain the pivotal factors that must be faithfully recapitulated when...

[185] Hydrogel-Based Vascularized Organ Tissue Engineering: A Systematized Review on Abdominal Organs

Filippos F Karageorgos, ..., and Aleck H. Alexopoulos. Gels, 2024. 6 citations.
Not measured Topic Match
Abstract: Background: Biomedical engineering, especially tissue engineering, is trying to provide an alternative solution to generate functional organs/tissues for
use in various applications. These include beyond the final goal of transplantation, disease modeling and drug discovery as well. The aim of this study is to
comprehensively review the existing literature on hydrogel-based vascularized organ (i.e., liver, pancreas, kidneys, intestine, stomach and spleen) tissue engineering
of the abdominal organs. Methods: A comprehensive literature search was conducted on the Scopus database (latest search 1 September 2024). The research
studies including hydrogel-based vascularized organ tissue engineering in the organs examined here were eligible for...

[186] Biomaterials Mimicking Mechanobiology: A Specific Design for a Specific Biological Application

Leonardo Donati, ..., and S. Martino. International Journal of Molecular Sciences, 2024. 5 citations.
Not measured Topic Match
Abstract: Mechanosensing and mechanotransduction pathways between the Extracellular Matrix (ECM) and cells form the essential crosstalk that regulates cell
homeostasis, tissue development, morphology, maintenance, and function. Understanding these mechanisms involves creating an appropriate cell support that
elicits signals to guide cellular functions. In this context, polymers can serve as ideal molecules for producing biomaterials designed to mimic the characteristics of
the ECM, thereby triggering responsive mechanisms that closely resemble those induced by a natural physiological system. The generated specific stimuli depend
on the different natural or synthetic origins of the polymers, the chemical composition, the assembly structure, and the physical and...

[187] Trends and challenges in organoid modeling and expansion with pluripotent stem cells and somatic tissue

Jian-Yun Ge, ..., and Yun-Wen Zheng. PeerJ, 2024. 6 citations.
Not measured Topic Match
Abstract: The increasing demand for disease modeling, preclinical drug testing, and long waiting lists for alternative organ substitutes has posed significant challenges
to current limitations in organoid technology. Consequently, organoid technology has emerged as a cutting-edge tool capable of accurately recapitulating the
complexity of actual organs in physiology and functionality. To bridge the gaps between basic research and pharmaceutical as well as clinical applications, efforts
have been made to develop organoids from tissue-derived stem cells or pluripotent stem cells. These developments include optimizing starting cells, refining culture
systems, and introducing genetic modifications. With the rapid development of organoid technology, organoid composition...

[188] Human organoids as 3D in vitro platforms for drug discovery: opportunities and challenges.

Daisong Wang, ..., and H. Clevers. Nature reviews. Drug discovery, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

View this report online at:
https://app.undermind.ai/report/00976f43c62aea45c504ced62e138a7fbd12439d94741d1d797b090abf78473b

Page 41/41
