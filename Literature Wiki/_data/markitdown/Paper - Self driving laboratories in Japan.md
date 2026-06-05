---
tags:
  - literature
  - type/paper
  - lit/sdl
  - lit/nanomedicine
  - lit/ai-methods
  - lit/digital-discovery
type: literature-note
source_note: "Papers/Paper - Self driving laboratories in Japan.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Naruki-Yoshikawa-2025-06-11-Self-driving-laboratories-in-Japan.pdf"
converter: "microsoft/markitdown"
---
Showcasing Japan’s advancements in self-driving laboratory
development. Left: Maholo LabDroid from RIKEN Center for
Biosystems Dynamics Research, Hyogo, Japan. Right: Robotic
powder grinding system from The University of Osaka, Osaka, Japan.

Self-driving laboratories in Japan

This perspective highlights Japan’s initiatives in self-driving laboratory
(SDL) development, showcasing diverse applications across materials
science, biology, chemistry, and software. In addition, it covers national
funding programs, research communities and ecosystems, and industries
supporting progress in this ﬁ eld. Additionally, the perspective emphasizes
the critical roles of education, standardization, and benchmarking in
fostering the continued growth of SDL research.

Image reproduced by permission of Yumiko Miyahara from Digital
Discovery, 2025, 4, 1384–1403.

The artwork by Yumiko Miyahara includes an image by Kanda et al.,
licensed under CC BY 4.0.

As featured in:

See Naruki Yoshikawa et al.,
Digital Discovery, 2025, 4, 1384.

rsc.li/digitaldiscovery

Registered charity number: 207890

Digital
Discovery

PERSPECTIVE

Cite this: Digital Discovery, 2025, 4,
1384

Received 9th December 2024
Accepted 14th May 2025

DOI: 10.1039/d4dd00387j

rsc.li/digitaldiscovery

1

Introduction

Self-driving laboratories in Japan

Naruki Yoshikawa,
Taro Hitosugi,
Keisuke Nagato,
Kanta Ono,
Kunihiko Shizume,
Ryo Tamura,

*a Yuki Asano,
gh Genki N. Kanda,

bf Masanobu Naito,

bc Don N. Futaba,
aij Shoichi Matsuda,
o Tohru Natsume,

d Kanako Harada,

ef

kl Yuuya Nagata, mn
pq Kazunori Nishio,

h

r Haruka Ozaki,

ijst Woosuck Shin,

d Junichiro Shiomi,

bcu

c Koichi Takahashi,

i Seiji Takeda,v Ichiro Takeuchi,

uw

xy Koji Tsuda

uxy and Yoshitaka Ushiku

zaa

Self-driving laboratories (SDLs) are transforming the scientiﬁc discovery process worldwide by integrating
automated experimentation with data-driven decision-making. Japan, known for its automation industry,
is actively contributing to this ﬁeld. This perspective introduces Japan's eﬀorts in SDL development,
including diverse applications across materials science, biology, chemistry, and software. In addition, it

covers national funding programs, research communities, and Japanese industries supporting progress
in this ﬁeld. It also highlights the importance of education, standardization, and benchmarking for the
future growth of SDL research.

Self-driving laboratories (SDLs)1 are transforming the process of
scientic discovery. It involves the automation of experiments
for large-scale data generation and data-driven decision-making
for eﬃcient exploration of the candidate space. As global
interest in SDLs continues to grow, Japanese researchers are
actively contributing to the eld. This perspective oﬀers an
overview of research eﬀorts related to SDLs in Japan.

Japan has been renowned for its advanced automation
technology, holding a 46% share of the global industrial robot
market as of 2023.2 This background has fostered an aﬃnity for
laboratory automation research, where robots oen play

a central role. In 1988, Matsuda et al. demonstrated the opti-
mization of reaction conditions using an automated system.3
This system can be considered as one of the earliest SDLs in
Japan, as it incorporates a laboratory robot with decision-
making by the simplex method. A fully automated laboratory
system for testing blood samples built by a Japanese hospital in
the 1980s is reported by Sasaki et al.4 Their approach gained
global attention as a promising method to reduce laboratory
testing costs.5

The development of SDLs could oﬀer valuable solutions to
address Japan's social challenges, particularly its declining
birth rate and shrinking workforce. This demographic shi has
created a need for innovative solutions to maintain productivity

aMedical Research Laboratory, Institute of Integrated Research, Institute of Science
Tokyo, Tokyo, Japan. E-mail: yoshikawa.naruki@tmd.ac.jp

nJST, ERATO Maeda Articial
Discovery Project, Hokkaido, Japan

Intelligence in Chemical Reaction Design and

bDepartment of Mechanical Engineering, The University of Tokyo, Tokyo, Japan

cInstitute of Engineering Innovation, The University of Tokyo, Tokyo, Japan

oResearch Center for Macromolecules and Biomaterials, National Institute for
Materials Science (NIMS), Ibaraki, Japan

dNational Institute of Advanced Industrial Science and Technology (AIST), Ibaraki,
Japan

pNational Institute of Advanced Industrial Science and Technology (AIST), Tokyo,
Japan

eGraduate School of Medicine, The University of Tokyo, Tokyo, Japan

qRobotic Biology Institute Inc., Tokyo, Japan

fGraduate School of Engineering, The University of Tokyo, Japan

rDepartment of Applied Physics, The University of Osaka, Osaka, Japan

gDepartment of Chemistry, School of Science, The University of Tokyo, Tokyo, Japan

hSchool of Materials and Chemical Technology, Institute of Science Tokyo, Tokyo,
Japan

sInstitute of Medicine, University of Tsukuba, Ibaraki, Japan
tCenter for Articial Intelligence Research, University of Tsukuba, Ibaraki, Japan
uRIKEN Center for Advanced Intelligence Project, Tokyo, Japan

iRIKEN Center for Biosystems Dynamics Research, Hyogo, Japan

jLaboratory Automation Suppliers' Association, Hyogo, Japan

kCenter for Green Research on Energy and Environmental Materials, National
Institute for Materials Science (NIMS), Ibaraki, Japan

lCenter for Advanced Battery Collaboration, Center for Green Research on Energy
and Environmental Materials, National Institute for Materials Science (NIMS),
Ibaraki, Japan

mInstitute for Chemical Reaction Design and Discovery (WPI-ICReDD), Hokkaido
University, Hokkaido, Japan

vIBM Research, Tokyo, Japan

wGraduate School of Engineering, Nagoya University, Aichi, Japan

xCenter for Basic Research on Materials, National Institute for Materials Science,
Ibaraki, Japan

yGraduate School of Frontier Sciences, The University of Tokyo, Chiba, Japan

zNexaScience, Inc., Tokyo, Japan

aaOMRON SINIC X Corp., Tokyo, Japan

1384 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineView Journal | View IssuePerspective

Digital Discovery

radiative cooling materials. Applications of robot arms for
mechanochemical synthesis and autonomous X-ray diﬀraction
analysis are covered in Section 2.7. Finally, Section 2.8 intro-
duces Process informatics.

2.1 Autonomous experiments for thin-lm materials
Thin-lm research is important for a wide range of elds,
including semiconductor devices, sensors, catalysts, optics, and
various coatings. Shimizu, Hitosugi, and colleagues reported
a closed-loop system for inorganic thin-lm materials in 2020.7
The system combines Bayesian optimization, automated
synthesis,
evaluation
and automated physical property
(Fig. 2(a)). The system consists of a robot arm positioned at the
center of a hexagonal chamber, which is connected to six
thin-lm
satellite chambers with an automated sputter
synthesis equipment and an automated electrical resistance
evaluation system (Fig. 2(b)). The robot arm handles all sample
transfers between the satellite chambers. Autonomous experi-
ments aimed at minimizing the electrical resistance of Nb-
doped TiO2 thin lms achieved a throughput 10 times higher
than manual methods.7 Furthermore, the system discovered
a novel electrolyte material for all-solid-state Li batteries.
Specically, by mixing Li3PO4
and Li1.5Al0.5Ge1.5(PO4)3
(Fig. 2(c)), an amorphous thin lm (Li1.8Al0.03Ge0.05PO3.3) shows
higher Li-ion conductivity than either of the original materials
[Li3PO4 and Li1.5Al0.5Ge1.5(PO4)3] (Fig. 2(d)).8

To reduce the number of experiments in the Bayesian opti-
mization process,
the kernel and
the hyperparameters of
acquisition functions were tuned.9,10 Leveraging the knowledge
and expertise of materials researchers is essential for tuning.

with fewer people. SDLs can reduce the burden of labor-
intensive experimental work in laboratories, enabling research
to continue with fewer staﬀ members. Additionally, SDLs
improve researchers' work-life balance, an increasingly impor-
tant consideration in Japan's work culture. Moreover, Japan's
demographic shi threatens the transmission of technical
expertise to future generations. SDLs can help preserve the
specialized knowledge of experienced professionals by auto-
mating tasks and replicating their skills. While these advan-
tages are particularly relevant to Japan, other countries facing
similar demographic trends may also benet from SDLs in the
near future.

The remainder of this paper is structured as follows. To
introduce the current state of automation in Japan, we provide
a review of Japanese SDLs across three application areas—
materials science, biology, and organic chemistry in Section 2 to
4. Section 5 explores the soware aspects of SDLs by intro-
ducing research eﬀorts on AI for scientic discovery. Section 6
highlights national funding programs to promote advance-
ments in automation-focused studies. Section 7 addresses the
activities to form research communities and ecosystems. An
overview of the Japanese industries supporting SDL develop-
ment is provided in Section 8. Finally, Section 9 discusses the
future directions of SDLs, and Section 10 concludes the paper.
The geographical locations of SDLs introduced in this article are
shown in Fig. 1. This perspective is based on a workshop held at
the Institute of Science Tokyo in October 2024.

2 Materials science

The materials industry is a key sector of Japan's economy, and
active research in materials science is being conducted there. As
part of the government's strategy to strengthen materials
innovation, data-driven research methods are actively promoted
through projects like the DxMT.6 This section reviews eﬀorts in
Japan to advance SDLs in materials science. Section 2.1 outlines
an automated system for synthesizing and evaluating thin-lm
materials. Section 2.2 provides an overview of the MaiML
format, a standardized data format for measurement analysis
instruments. Section 2.3 details a robotic experiment setup for
discovering electrochemical materials. Section 2.4 and 2.5
highlight autonomous polymer synthesis achieved by two
research groups. Section 2.6 explores the development of

Fig. 1 Geographical locations of SDLs introduced in this article.

Fig. 2 (a) Photograph and (b) schematic of autonomous experimental
system for exploration of inorganic thin-ﬁlm materials. Copyright 2020
Shimizu et al.7 and reprinted with permission under CC BY 4.0. (c)
Autonomous experimental cycle for exploration of ionic conductors.
(d) Ionic transport properties of fabricated amorphous ionic conduc-
tors thin ﬁlms. Reprinted with permission from Kobayashi et al.8
Copyright 2023 American Chemical Society.

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1385

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

For example, materials researchers can anticipate the process
window of synthesis parameters and the scale of changes in
physical properties, which is the key to tuning the values of
hyperparameters.

Since this system can connect multiple measurement and
analysis instruments, it can acquire various physical properties
from multiple aspects to generate big data. For this purpose,
a standardized measurement and analysis data format
(Measurement Analysis Instrument Markup Language: MaiML)
was applied to the system.11 The format is described in the next
section. For interested readers, a review on autonomous
experimental systems in materials science is available from
Ishizuki et al.12

2.2 Standardization of data format with MaiML

Representing data in a standardized, structured format is
crucial
for facilitating automated analysis by computers.
Various data formats have been developed to store diﬀerent
types of
information. For example, Chemical Description
Language (cDL) has been introduced to describe experimental
procedures in organic chemistry.13 Currently, measurement
instruments from diﬀerent manufacturers oen provide data in
diﬀerent formats. This lack of a standard format requires users
to convert the formats manually or to prepare data conversion
soware. Therefore, there is a strong need for a standard
format. In response, the Japan Analytical Instruments Manu-
facturers Association (JAIMA), in collaboration with its member
companies and the Ministry of Economy, Trade, and Industry
(METI), established a data format called the Measurement
Analysis Instrument Markup Language (MaiML). In May 2024,
MaiML was registered as a Japanese Industrial Standard (JIS K
0200).

The MaiML format was developed as a standardized data
format with independent availability to achieve an instrument-
follows the ndable,
agnostic data structure. The format
accessible, interoperable, and reusable (FAIR) data principles.14
An XML format describes the processes of measurement, pre-
processing, and postprocessing steps. Detailed descriptions of
sample fabrication processes and measurement conditions
ensure the reproducibility of experiments. Additionally, logs for
each measurement operation provide traceability. The format
also includes tamper-prevention features and data encryption
capabilities. These features allow MaiML to encompass essen-
tial information for the reproducibility of sample fabrication to
measurement and analysis,
thus contributing to database
construction (Fig. 3). Guidelines for MaiML are available on
https://www.maiml.org/.

2.3 High throughput robotic experiments for rechargeable
batteries
Data-driven automated robotic experiments are an eﬀective
method to accelerate the development of new-materials even in
the eld of rechargeable batteries.15 Specically, optimizing the
composition of electrolytes and identifying eﬀective additive
combinations involves evaluating an enormous number of
potential candidate materials.16 Historically, this process has

Fig. 3 Schematic of the utilization of the standardized data format of
Measurement, Analysis, Instrument Markup Language (MaiML).

relied heavily on trial-and-error approaches, leading to signi-
cant bottlenecks in the development of new electrolyte
materials.

To overcome these challenges, Matsuda et al. developed the
robotic experimental setup for searching electrochemical
materials discovery using high-throughput combinatorial
techniques by use of miniaturized microplate type electro-
chemical cells.17 The system consisted of a liquid handling
dispenser and a 96-channel electrochemical analyzer equipped
with a robotic microplate handling arm, with a search
throughput of over 1000 samples per day. By integrating with
Bayesian optimization techniques, they discovered the specic
composition of electrolyte that enhances the cycle life of
lithium-oxygen batteries,18 demonstrating its eﬀectiveness in
signicantly accelerating the identication of optimal electro-
lyte compositions (Fig. 4). A key feature of their system is its

Fig. 4 Schematic illustration of the data-driven high-throughput
automated robotic experiments for searching multi-components
electrolyte for rechargeable batteries. Figure adapted with permission
from Matsuda et al.18 Copyright 2022, Elsevier.

1386 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

autonomous exploration capability, which is achieved with the
use of NIMO, an automation soware for establishing a closed-
loop workow between articial
intelligence and robotic
experimentation.19 The details of NIMO are described in Section
5.2. Recently, the group extended their interest for practical
design of battery cells, and reported the development of fully
automated sequential robotic experimental setup for the cell
fabrication of stacked-type battery cells with fabrication
throughput over 80 cells per day, which is 10 times higher than
conventional human-based experiments.20

2.4 Advances in autonomous synthesis for polymers

Autonomous synthesis in polymer science has progressed
signicantly since the early 2000s, with high-throughput (HTP)
techniques driving advances in polymerization. Early develop-
ments focused on automating polymer synthesis processes,
particularly for combinatorial studies, to enhance speed and
reproducibility.21 A major milestone was the application of
automation to precision-controlled polymerization, such as
Reversible Addition–Fragmentation Chain Transfer (RAFT) and
Atom Transfer Radical Polymerization (ATRP). These tech-
niques allow precise control over polymer architecture, molec-
ular weight, and functionality, enabling the creation of complex
and customized polymers.22,23 HTP methodologies have facili-
tated the rapid creation of polymer libraries and optimization of
synthesis parameters, though dataset sizes remain a limitation.
Recent innovations in platforms like Chemspeed have repli-
cated most manual processes, integrating Python-based tools
like Chemspyd24 for real-time adaptive control and process
optimization.

Despite these advancements, challenges persist in charac-
terizing critical physical properties, such as mechanical and
thermal performance. For example, tensile testing for adhesive
materials requires specialized setups and skilled sample prep-
aration. Addressing this, Naito and Sato developed a high-
throughput testing system for adhesives, which uses miniatur-
ized specimens to provide more realistic performance metrics
while reducing material usage.25 Moreover, integrating machine
learning techniques, such as Bayesian optimization, with ow
synthesis has enabled autonomous experiments for optimizing
radical polymerization.26,27 In summary, while autonomous
synthesis has revolutionized polymer research, the integration
of automation and intelligent algorithms promises further
advancements, addressing current challenges and unlocking
new possibilities for material innovation.

2.5 Flexible lab-automation using robot arms for polymer
materials development

Polymer materials are widely used in academia and industry.
Most polymer materials used for actual products are in the form
of composites to reinforce multi-functionality, for instance by
being mixed with dielectric llers. However, automation in the
development processes of polymer composite materials is still
limited because of the challenges in handling materials in the
form of powders and granules and molding processes required
for property characterization and application.

A Japanese team has been developing an automated system
for polymer materials development. One of the sub-processes is
the press process (Fig. 5(A)).28 A robot arm was adopted to
construct a system that handles the tools for the operations,
such as press plates and forks, and to increase the exibility of
the system for future adaptability rather than built-in automa-
tion of a dedicated system. The control soware operates both
the robots and the press machines. An experimental closed loop
was formed to obtain eﬀective press parameters and evaluates
the thickness of the polymer lm by image processing and press
parameters. Another automated sub-process is the property
measurement systems (Fig. 5(B)), such as the one for a dielectric
property utilizing the force-sensing capability of a robot arm for
stabilization of polymer placement.29 The automated system
successfully measured the dielectric properties with the same
accuracy as trained humans.

The exibility of the system was enhanced by the use of
a gripper interface that enables the grasping of multiple tools
and thus the completion of complex pressing processes with
a single robot arm. The same type of robot arms was used in
both the press and measurement sub-processes. The use of
a single type of robot arm reduces the development and main-
tenance costs for an automated workow than the development
of multiple dedicated automation machines for each process.

2.6 Automated lm development system generating massive
data for radiative cooling

Amid growing concerns over urban heat islands, sky radiator
technology, which selectively emits thermal radiation in the

Fig. 5 (A) Press process automation system for polymer materials
development, adapted from Asano et al.28 (B) Dielectric property
measurement system. Reprinted with permission from Asano et al.29
Copyright 2024, IEEE. (C) Automation system for heat transfer mate-
rials development.

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1387

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

atmospheric window region (8–13 mm) to directly radiate heat
into outer space, has received signicant attention. Shiomi et al.
have been developing thermal radiative metamaterials by
combining electromagnetic eld analysis and machine learning
to optimize metamaterials,
achieving high-performance
thermal emitters.30,31 While metamaterials are advantageous
in the wavelength selectivity of radiation, the diﬃculty in
fabrication poses
to widespread
application.

signicant barrier

a

As a scalable and cost-eﬀective approach to developing
radiative coolers, they are working on organic–inorganic hybrid
coatings consisting of a polymer matrix and inorganic llers.
The thermal radiation properties in the atmospheric window
region and the solar reection properties in the visible range for
heat shielding depend on the optical absorption of the polymers
and inorganic llers themselves, along with the resonances and
scattering phenomena occurring at their interfaces. Conse-
quently, the parameter space becomes extremely large because
it incorporates not only material parameters, such as the type
and mixing ratio of polymers and inorganic llers, but also
process parameters, such as casting and drying conditions. For
example, a coating involving ve materials and three process
parameters, such as mixing time, casting speed, and drying
temperature, yields an 8-dimensional search space. Exploring
just 10 choices per parameter results in 108 combinations,
leading to a combinatorial explosion. To address this challenge
they are developing an automated
with high throughput,
coating system capable of producing 1000 coatings per day
under various conditions and automatically acquiring infrared
and visible reection spectra (Fig. 5(C)). Additionally, they have
developed a spectral prediction model, useful for controlling
radiative properties, using a dataset of over 10 000 data.

2.7 Robotic mechanochemical synthesis and autonomous
XRD analysis

Mechanochemical synthesis, which induces chemical reactions
through mechanical force, oﬀers an energy-eﬃcient, solvent-
free method for producing materials such as metal–organic
frameworks (MOFs) and energy-related compounds. However,
traditional methods like manual grinding or ball milling oen
struggle with reproducibility and control. To overcome these
challenges, Nakajima et al. developed a force-controlled robotic
mechanochemical synthesis system,32 combined with an
autonomous X-ray diﬀraction (XRD) analysis workow33 (Fig. 6).
This system not only provides precise control over grinding
force and speed but also enables automated, high-throughput
structural analysis through autonomous XRD.

system demonstrated superior

In their experiments with perovskite materials, the robotic
synthesis
reproducibility
compared to manual and ball milling methods, especially for
force-sensitive reactions. By adjusting the grinding force and
speed, they could signicantly inuence the reaction pathways,
allowing for precise control of reaction outcomes. For instance,
increased grinding force produced higher yields of Cs4PbBr6,
while variations in speed shied the reaction toward other
phases like CsPbBr3.

Fig. 6 Automated system for powder material experiments.
(A)
Robotic powder grinding system using a Soft Jig, where the jig's
softness ensures safe grinding without the need for force sensing. (B)
Autonomous powder X-ray diﬀraction system for preparing XRD
samples and performing automated Rietveld analysis. (C) Enhanced
robotic powder grinding using visual and audio feedback, with grinding
sounds providing particle size information for more eﬃcient grinding.
(D) Robotic mechanochemical synthesis controlling reaction path-
ways through force conditions applied by a pestle.

Once the synthesis was complete, the fully autonomous XRD
system seamlessly handled sample preparation, measurement,
and data analysis. This integration allowed for high-throughput
analysis and minimized human error, particularly in the
reproducibility of low-angle diﬀraction patterns, which are
crucial for characterizing materials like lead halide perovskites.
This combined robotic synthesis and autonomous XRD
approach oﬀers a powerful tool for both advancing the under-
standing of
reaction mechanisms and accelerating the
discovery of novel materials. Future work will explore the
application of this system to a wider range of materials.

2.8 Process informatics – robotic objective process
exploration system (ROPES)
In order for new materials to be incorporated into nal prod-
ucts, process development and production technology devel-
opment are necessary, and AI robot-driven development is also
eﬀective (Fig. 7(a)). Process Informatics is located downstream
of Materials Informatics. Experimental-based Bayesian optimi-
zation was demonstrated in the powder-lm-dying process of
a catalyst layer in polymer electrolyte fuel cells (PEFCs).34

The catalyst layer of a solid polymer electrolyte fuel cell is
composed of carbon as an electronic conductor, uoropolymer
as a proton conductor, pores in the gas diﬀusion space, and
platinum nanoparticles as a reaction catalyst. The arrangement
of the three-dimensional microstructure changes signicantly
depending on how it is applied and dried, and optimization is
required. The autonomous experiment system shown in
Fig. 7(b) discovered new drying-process parameters among 85
candidates with 40 trials minimizing the defect ratio (Fig. 7(c)).
Not only the high-throughput exploration but also ve process

1388 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

Fig. 7 ROPES of powder-ﬁlm-formation-process, (a) schematic of an
autonomous system, (b) experimental setup with two robot hands,36
(c) results of exploration of drying process parameters minimizing
defect ratio,34 (d) a scalable autonomous system, (e) high-throughput
prototyped fuel cell catalyst layer samples. A video about ROPES is
available online.35

routes were found. Furthermore, we also prototyped an elevator-
sized autonomous system as shown in Fig. 7(d), which can
automatically demonstrate factory processes, i.e., die-coating
and zone-heating, and evaluate defect ratio, but also micron-
sized surface roughness and electronic impedance. The small-
sized samples are prototyped with various process parameters
(Fig. 7(e)). A video demonstration of this system is available
online.35

Process informatics is a methodology for process exploration
using small amounts of prototyped material samples, which
will lead to the accelerated social implementation of incorpo-
ration into nal products.

3 Biology

Automation in biological experiments has been pursued across
various elds and processes. For example, PCR experiments—
widely recognized due to COVID-19 testing—had already begun
transitioning from manual water bath operations to automated
thermal cyclers by the late 1980s.37 Numerous specialized
instruments like automated pipetting systems have been
developed, signicantly improving the eﬃciency of xed oper-
ations. However, more versatile robotic systems are needed,
especially for automation in basic research. In Japan, the
versatile humanoid robot Maholo LabDroid, developed by
Yaskawa Electric Corporation and the Robotic Biology Institute
Inc., is widely used from fundamental to clinical research
(Fig. 8).

Fig. 8 The LabDroid Maholo including peripheral equipment.
Reprinted from Kanda et al.38 under CC BY 4.0.

3.1 Maholo LabDroid

Maholo LabDroid has been employed in molecular and cellular
biology, drug screening, culturing and immunostaining of
induced pluripotent stem cells (iPS cells), and in closed-loop
cell culture using AI and robotics.39–43 By combining this robot
with optimization AI, Kanda et al., have successfully conducted
autonomous experiments targeting cell cultures for regenera-
tive medicine.38 Specically, they used a batch Bayesian opti-
mization algorithm with LabDroid Maholo to autonomously
explore combinations of seven parameters—such as reagent
concentrations, processing times, and cell handling intensi-
ties—involved in diﬀerentiating iPS cells into retinal cells,
achieving eﬃcient
induction without human intervention.
Beyond basic research, Maholo LabDroid is also utilized in
clinical studies. A research team at Kobe City Eye Hospital
created a sterile environment by integrating the robot with
a clean booth and successfully transplanted cells cultured by
the robot into patients during clinical research on retinal cells.44
As of October 2024, Maholo LabDroid is not sold outside Japan.

3.2 Robotic crowd biology

A Japan-led team has proposed the concept of Robotic crowd
biology in 2017, which involves aggregating hundreds of robots
into a robotic experimentation center for cloud-based experi-
ments.45 Researchers submit their desired experimental proto-
cols to the center via a network, where AI and robots eﬃciently
execute the experiments and return the results. This approach
oﬀers various benets, such as improving the reproducibility
and traceability of scientic experiments,
fundamentally
resolving research misconduct, increasing the utilization rates
of expensive advanced equipment, and eﬃciently conducting
high-biosafety-level
envisions
making biological research widely accessible to all humanity.

experiments. Ultimately,

it

In the Robotic Crowd Biology concept, managing numerous
robots and devices makes it impractical for humans to instruct
each one individually. To address this, the development of AI

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1389

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

and soware for directing robots is actively underway. A
research team at the University of Tsukuba has developed
algorithms to achieve parallel scheduling necessary for eﬃ-
ciently operating multiple robots.46,47 While some scheduling
algorithms exist in the eld of factory automation (FA), the
authors' formulation considers time constraints specic to life
science experiments—such as reaction times and the degrada-
tion of living cells and reagents—that are set among processes.
To automate the monitoring of multiple devices that would
otherwise require human oversight, the same team developed
image recognition soware, ne-tuned for identifying labware
used in life science experiments, to monitor the status of lab-
ware placed inside automated dispensing robots.48 Additionally,
a research team at RIKEN has demonstrated that it is possible to
automatically convert experimental procedures written in
natural
language into robot-operating code using large
language models.49 Furthermore, the development of AI-based
systems to manage robots and experimental equipment from
higher levels is currently being extensively pursued. Supporting
these eﬀorts, a prototyping lab has been established at RIKEN
BDR in Kobe, and a demonstration facility is planned at the
Institute of Science Tokyo. In recent years, researchers outside
Japan have also begun exploring ways to take advantage of
a cloud-based experimental platform, spurring discussions and
initiatives worldwide toward its realization.50

4 Organic chemistry

In organic chemistry research, experimental procedures still
largely depend on researchers' expertise and manual opera-
tions. However, there is a continuous demand for more eﬃcient
alternatives to these traditional methods, resulting in the
development of various innovative approaches. Recently, auto-
mated synthesis robots have drawn signicant attention for
their potential to automate and even autonomously conduct
organic chemistry research. Utilizing these robots can achieve
high reproducibility and experimental precision, oﬀering
substantial improvements in eﬃciency compared to conven-
tional manual processes. This technological advancement
simplies labor-intensive synthetic experiments and consider-
ably reduces the workload of researchers.

In the eld of organic synthesis, two primary types of robots
are commonly employed: articulated robots and Cartesian
coordinate robots. Here, articulated robots are highly exible,
with multiple joints that enable complex, multi-directional
movements. This makes them ideal for intricate tasks, such
as transferring reaction vessels, adjusting equipment, and
performing precise reagent additions in conned spaces. In
contrast, Cartesian coordinate robots operate along xed linear
axes, making them well-suited for high-precision, repeatable
tasks like liquid handling, reagent dispensing, and automated
sample preparation with minimal positioning errors. Many
processes in organic synthesis can oen be segmented into
simple operations that are well-suited for execution by Carte-
sian coordinate robots. For example, the polymerization of
poly(quinoxaline-2,3-diyl)s via living polymerization of diiso-
cyanobenzene derivatives has been successfully automated

using a Cartesian coordinate robot.51,52 In this process, the
resulting polymer thin lms were reported to exhibit unique
selective reection behavior. It was found that even slight
inaccuracies in the monomer composition and variations in the
degree of polymerization had a signicant impact on the
selective reection wavelength. Therefore, precise control of
these parameters was critically important. In particular, it was
necessary to dispense volumes with an accuracy of less than
10 mL. However, in the early 2010s, among the commercially
available automated systems investigated in the study, no
articulated robot was known to achieve this level of dispensing
precision with organic solvents. Consequently, a Cartesian
robot (Chemspeed SWING) was employed for this purpose.

Additionally, direct

integration of Cartesian coordinate
instruments is under active
robots with various analytical
investigation. For instance, integration with a UV-visible-NIR
spectrophotometer has enabled the development of a solu-
bility prediction model for porphyrins,53 while integration with
chromatography systems has facilitated the automatic evalua-
tion of asymmetric catalysts, advancing the development of
a high-performance catalyst.54 More recently, combining robots,
chromatography systems, and the PHYSBO package introduced
in Section 5.2 has been explored for autonomous optimization
of chemical reaction conditions.55

Beyond commercial laboratory automation systems, low-cost
hardware is crucial for reducing the entry barrier to SDLs.56
Kuwahara et al. developed a 3D-printed robot named FLUID to
democratize automation in materials synthesis.57 They showed
its utility by demonstrating the coprecipitation of cobalt and
nickel to form binary materials. All design les and control
soware are released under an open-source license, allowing
users to modify and adapt the system to their own research
environments.

5 AI for science

Since SDLs involve the automation of data-driven decision-
making,1 SDL research requires developing intelligent soware
as well as automation hardware. In this section, we review the
soware side of SDLs in Japan, focusing on the eld of AI for
science. The foundation models for material discovery devel-
oped in IBM Research-Tokyo are described in Section 5.1. Black
box optimization soware packages developed by Japanese
teams are introduced in Section 5.2. Research by OMRON SINIC
X is covered in Section 5.3 and several applications of large
language models for scientic research are outlined in
Section 5.4.

5.1 Foundation models for material discovery

The integration of AI models into self-driving laboratories
enhances their capabilities, enabling the preselection of
promising materials before chemical synthesis and guiding
experiments to achieve desirable properties. Property prediction
and structural generation are particularly promising AI appli-
cations. However, traditional AI models developed by individual
research groups within specic material domains are oen

1390 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

limited in size and small training datasets (order of 10 to 100
samples), resulting in insuﬃcient modeling accuracy.

To address these limitations, recent advancements inspired
by large language models (LLMs) have been adopted in mate-
rials informatics. These approaches involve pre-training large
models in a self-supervised manner using massive datasets.
Such pre-trained models eﬀectively capture general material
representations and can be ne-tuned with small domain-
specic datasets for various downstream applications. Exam-
ples of foundation models include MolCLR,58 a GNN-based
architecture pre-trained with 10 million molecular samples,
and ChemBERTa,59 which uses the RoBERTa architecture pre-
trained with 77 million SMILES samples. Although these
models perform well in regression and classication tasks, their
single-modal nature leaves room for improvement. Recent
studies explore multi-modal representations of materials to
enhance modeling capabilities. Shirasuna et al.60 introduced
models that fuse SMILES and molecular graphs using a Mixture-
of-Experts approach, achieving superior performance over
single-modal models. As noted in Takeda et al.,61 multi-modal
modeling is an emerging eld with vast opportunities,
including eﬃcient
fusion methods and strategic modality
selection. Other modalities, such as SELFIES, 3D atom posi-
tions, electron density, optical spectra, and text descriptions,
are also under consideration. These foundation models can
signicantly enhance SDL capabilities by utilizing their
predictive and generative functions, enabling the design of
more promising candidate materials. For instance, ref. 62
demonstrates how a SMILES-based foundation model was
integrated into a human-in-the-loop workow connected to an
SDL. Similarly, as demonstrated by RoboRXN,63 synthetic
pathways predicted by a foundation model can be executed in
automated robotic laboratories. Some of these models are
openly accessible on GitHub64 and Hugging Face, encouraging
open development within the materials informatics commu-
nity. Specically, Foundation Model for Materials (FM4M) has
achieved widespread adoption through active community-
building eﬀorts through the AI Alliance,65 bridging academia
and industry toward shared innovation goals.

5.2 Black box optimization methods and NIMO

Black box optimization techniques are useful as an AI to suggest
experimental conditions to be tested, which can be the brain of
self-driving labs (Fig. 9). Bayesian optimization is probably the
best-known technique for achieving desired material proper-
ties. The Python packages COMBO (COMmon Bayesian opti-
mization)66 and PHYSBO (optimization tool for PHYSics based
on Bayesian optimization)67 can quickly perform the Bayesian
optimization calculations. On the other hand, there are various
needs in materials research, but also the improvement of
material properties, and other techniques are required. For
example, to construct phase diagrams with a small number of
experiments,
the Python package PDC (Phase Diagram
Construction) has been developed by adopting the uncertainty
sampling strategy.68 To visually explore phase diagrams using
PDC, a web application called AIPHAD (Articial Intelligence

Fig. 9 Black box optimization methods depending on the aim of
exploration. Reprinted from ref. 71–73 under CC BY 4.0.

techniques for PHAse diagram) is freely available.69,70 In addi-
tion, algorithms such as BLOX (BoundLess Objective-free
eXploration)71 for overlooking the material property spaces
and SLEPA (Self-Learning Entropic Population Annealing)72 for
obtaining the material property distributions with the small
number of experiments have been developed as open source
soware. Furthermore, the black box optimization technique
using quantum annealer and Ising machines called FMQA
(Factorization Machine with Quantum Annealing) has been
developed to explore vast material space.73 Although these
methods have been mainly developed in materials science, we
believe that they can be used not only in materials science but
also in any self-driving labs for biology, organic chemistry, etc.
To achieve a self-driving lab by combining the robotic
experimental devices introduced in Section 2.3 and three black-
box optimization techniques (PHYSBO, PDC, and BLOX),
a generic soware NIMO (NIMS Orchestration System) has been
developed.19,74 In NIMO, a robotic experiment and a black-box
optimization method are treated as modules, and the system
is designed to enable various autonomous automated material
explorations by selecting these modules. As a demonstration
experiment, autonomous automated experiments on electro-
lytes for lithium metal electrodes were carried out using the
robotic experimental setup for searching electrochemical
materials discovery (see Section 2.3) controlled by NIMO. As
a result, a total of 384 electrolytes were successfully developed

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1391

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

as autonomous automated experiments without human inter-
vention using NIMO. Globally, various types of orchestration
soware (OS) have been developed.75–77 NIMO has an advantage
over other OSs due to its focus on AI algorithms, particularly its
use of diverse black-box optimization methods, beyond
Bayesian optimization. These methods are designed to be easily
integrated into other OSs, allowing us to enhance the capabil-
ities of self-driving laboratories by combining NIMO with other
systems. Additionally, we are developing new AI algorithms to
address a range of exploration needs. By incorporating these
into NIMO, we aim to establish it as an evolving open-source
soware (OSS). Furthermore, the three algorithms already
implemented in NIMO are widely used in materials science,78
chemistry,79 and drug discovery,80 leveraging both experimental
and simulation data. Thus, we believe that NIMO can facilitate
interactions between these diﬀerent domains in Japan.

5.3 From foundation model to AI scientist

As discussed in Section 5.1, foundation models are being
developed across various elds, with comprehensive applica-
tions being considered for SDLs. These applications extend
beyond providing scientic knowledge in respective elds;
related to Section 5.2, LLMs can also encompass optimization
tasks,81 and as will be discussed in Section 5.4, they include
a series of research activities such as hypothesis generation,
experimental design and implementation, paper writing, and
reective review as AI scientist.82

OMRON SINIC X Corporation, a research subsidiary of
OMRON that focuses on healthcare and factory automation, is
advancing various projects utilizing foundation models in AI
and robotics to realize real-world AI scientists. Following the
philosophy of OMRON's founder, “To the machine, the work of
the machine, to man the thrill of further creation”, the company
has been researching how to understand and support human
creation through AI and robots. A particular focus has been
understanding human research and experimental work, con-
ducting research and development through open innovation
with universities and public research institutions while
receiving competitive research funding.

The company's research into understanding research data
encompasses several key streams. The rst focuses on law
discovery, which involves tackling the symbolic regression
problem to discover scientic laws between variables from
measured data.83 This machine learning challenge takes tabular
data containing variable values as input and outputs mathe-
matical formulas showing relationships between variables.84
The second stream involves map-based visualization, primarily
targeting materials science, where representation learning
techniques are applied to various data types including material
structures, measurement data, and property-describing text.85
The goal is to create visualizations where materials with similar
properties are mapped close to each other. The third stream
concentrates on novel material design86 and property predic-
tion,87 including research on generating new crystal structures
and developing Transformer architectures to predict properties
of crystal structures with unknown characteristics.

Regarding the reproduction of experimental work, much of
the robotics research has focused on powder manipulation.
Powders present more challenging handling requirements than
liquids in terms of weighing, grinding, and mixing, making
them an engaging research topic in robotics. For instance,
research on powder-weighing robots has achieved sub-
milligram precision in liing and dropping powder using
spoons
In powder
grinding research, eﬃcient powder processing has been ach-
ieved by utilizing multiple modalities of information, including
visual and vibration data.89

through simulation-based learning.88

In parallel, research is being conducted on AI robots that can
execute various tasks while understanding environmental data
and linguistic instructions.90 Future plans involve connecting the
above-mentioned AI for research understanding with experi-
mental automation robots, advancing this research to realize AI
robot scientists capable of conducting real-world experiments.

5.4 Large language models for automated scientic research

LLMs have been adopted by multiple SDLs91,92 because of their
powerful ability in natural language processing. A number of
applications on LLM for automated scientic research have
been released from Japan. Sakana AI, a Japan-based startup,
proposed the AI Scientist,82,93 which aims for fully automatic
scientic discovery by harnessing the power of LLMs.
Hatakeyama-Sato et al. explored the ability of GPT-4 in various
chemical tasks and elucidated their current limitations.94 They
also applied GPT-4 for parameter selection of a polymer prop-
erty prediction95 and a semiautomated system for synthesizing
polyamic acid particles.96 Jiang et al. developed ProtoCode,97
information from natural
a tool that can extract protocol
language text and convert it to intermediate representation
formats. They demonstrated its ability by generating thermal
cycler operation les from polymerase chain reaction (PCR)
protocols written in natural language. Machi et al. developed
a framework for reviewing the results of automated conversions
of structured organic synthesis procedures extracted from the
literature.98 In this framework, organic synthesis procedures in
the literature are transformed into a structured chemical
description language (cDL)13 using both a proposed rule-based
method and a generative large language model-based method.91
The results from both methods are presented simultaneously to
users, facilitating eﬃcient transformation and renement.

As the potential of LLMs has become widely recognized, the
race for their development has intensied. Both commercial
models, such as GPT-4,99 and open-weight models like LLaMA100
and DeepSeek,101 are now widely available. To support the
development of LLMs in Japan, the Ministry of Economy, Trade
and Industry (METI) and the New Energy and Industrial Tech-
nology Development Organization (NEDO) started the Genera-
tive AI Accelerator Challenge (GENIAC)102 in February 2024. The
government-funded project subsidizes the computational costs
of LLM training for the selected players. The rst
term
(February–August 2024) supported 10 projects including Sakana
AI's, and the second term (October 2024–April 2025) selected 20
projects including 3 projects about LLMs for medicine.

1392 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

6 AI-robot-driven science

Japan Science and Technology Agency (JST), one of the major
national
funding agencies for science, supports multiple
projects related to SDL research. Two JST-Mirai projects,
Accelerating Life Sciences by Robotic Biology,103 Materials
Exploration space Extension Platform (MEEP),104 and two JST
Moonshot projects, Co-evolution of Human and AI-Robots to
Expand Science Frontiers105 and AI & Robots that Harmonize
with Humans to Create Knowledge and Cross Its Borders106
collaboratively founded the AI-Robot-Driven Science Initiative107
in 2023 to promote the new scientic methodology realized by
In 2024, “Research innovation through
AI and robotics.
autonomous-driven research systems” has been designated as
one of the strategic objectives authorized by the Ministry of
Education, Culture, Sports, Science and Technology (MEXT),108
and a new funding program “R&D Process Innovation by AI and
Robotics”109 has been started. In this section, we introduce
government-supported projects on AI-robot-driven
these
science.

labor-intensive nature of

6.1 Accelerating life sciences by robotic biology
This project, part of JST-Mirai Program in the “Common Plat-
form Technology, Facilities, and Equipment” area, addresses
critical issues in life sciences—such as low reproducibility,
ineﬃcient use of costly equipment, research misconduct, and
laboratory work—through
the
advanced laboratory automation. While laboratory automation
tools are increasingly available, most are limited to specic
tasks, still relying on human operators to manage samples,
reagents, and data interpretation. Consequently, human error
and labor remain constraints on the eﬀectiveness of automa-
tion. This project aims to overcome these limitations by devel-
oping a comprehensive suite of technologies. These include
a standardized experimental protocol description language and
IoT-based systems architectures designed for the coordinated
operation of diverse robotic and automated equipment. The
project's application areas broadly span the biological sciences,
including proteomics, genome editing, and stem cell culture.
This interdisciplinary eﬀort involves leading institutions like
RIKEN, AIST, University of Tsukuba, and major industry part-
ners including YASKAWA Electric and TECAN Japan. The
project began with a feasibility study (2018–2020) and moved to
full-scale development in 2021, with completion anticipated in
March 2025. Funded at approximately 1.1 billion yen (∼7.3
million USD), this initiative strives to redene experimental
workows, minimizing human involvement and enhancing
reproducibility and operational eﬃciency across the life
sciences. Many of the project's outcomes are presented in
Section 3.1 (Maholo LabDroid) and 3.2 (Robotic crowd biology).

6.2 Materials exploration space extension platform

MEEP was launched in the JST-Mirai project in 2021.110–112
Researchers' experiment and intuition are important in mate-
rials research and development (R&D), and the researchers'
inspiration should be more eﬀectively utilized by AI and robot

systems. MEEP's proof of concept is 1000 times throughput of
exploration of ion-conductive materials for solid-state batteries.
The materials exploration space is overwhelmingly expanded in
R&D sites with the following three methods;

(1) High-throughput autonomous exploration systems;
(cid:1) “make”: Autonomous prototyping system with vacuum

coating7–9

(cid:1) “measure”: “Materials doc” including autonomous crystal

analysis system113

(cid:1) “save”: materials property prediction system114
(2) Data-driven/hypothesis driven hybrid system (Fig. 10);
OODA loop with “make”–“measure”–“save”–“understand”

induces inspiration85

(3) Knowledge sharing;
The knowledge obtained from the data is shared among R&D
and measuring instrument

institutes, R&D companies,
manufacturers.

6.3 Co-evolution of human and AI-robots to expand science
frontiers
In the current movement toward scientic automation through
AI and robotics, the focus is largely on conducting reproducible,
high-throughput experiments to accelerate scientic discov-
eries. However, such automation proves eﬀective primarily
when hypotheses can be tested at low cost and within a short
time frame, and when experiments involve repetitive actions on
rigid objects. As experimental models become increasingly
complex, hypothesis testing generally requires greater invest-
ment of both time and resources. For instance, in life sciences,
experiments with high-delity model organisms—far more
complex than cell-based tests—pose signicant challenges for
automation. These organisms are typically small, exible, and
variable, limiting the ability of current robotics to perform
precise
experimental procedures based solely on pre-
programmed instructions.

Fig. 10 Schematic of MEEP policy based on OODA loop. Observe
phase: materials doc, orient phase: materials big data, decide phase:
human, act phase: autonomous prototyping.

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1393

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

In scenarios that demand experimentation in extreme envi-
ronments where each task cannot be pre-specied, autonomous
robots capable of self-directed learning and action become
essential. Such autonomy allows robots to leverage their unique
ability to recongure physical capabilities, presenting a novel,
robotics-specic approach to scientic exploration. This project
under JST Moonshot Goal 3 aims to realize autonomous AI
robotic scientists by 2050. Through transdisciplinary research,
it integrates mathematical foundations, scientic AI, robotic AI,
and robotic hardware.

6.4 AI & robots that harmonize with humans to create
knowledge and cross its borders

This project aims to develop AI robots that can harmonize with
humans to create knowledge and transcend its boundaries by
2050. The initiative represents a signicant advancement in the
integration of articial intelligence with scientic research and
innovation processes.

The project has established clear milestones, with the rst
target set for 2025: developing AI robots capable of under-
standing, reproducing, and explaining research conducted by
human scientists, while also generating novel hypotheses. By
2030, the project envisions these AI robots collaborating with
researchers across various elds to drive innovation, resulting
in the publication of peer-reviewed papers. The ultimate goal
for 2050 is to create an environment where researchers and AI
systems can work together to produce Nobel prize-level research
achievements.

The research framework encompasses three interconnected
components. The experiment automation AI robot system is
designed to conceptualize experiments based on research
hypotheses, estimate specic procedures in cyberspace, and
execute them in physical space. This includes developing
automated synthesis capabilities and understanding experi-
mental papers. The Claim and analysis AI focuses on compre-
hending multimodal scientic data and providing language-
based evidence, utilizing a foundation model that can under-
stand relationships between research papers and generate
comprehensive analyses. The Description and dialogue AI
system aims to summarize experimental results and update
hypotheses through interactive discussions with researchers,
incorporating researcher feedback to improve performance
without requiring large datasets.

To achieve these objectives, the project employs various
advanced technologies including large language models,
multimodal AI systems, and automated synthesis devices. The
project particularly emphasizes the importance of combining
deductive thinking for continuous performance improvement
with inductive thinking and abduction for paradigm disrup-
tion, ultimately aiming to create a new approach to scientic
discovery that leverages both human expertise and articial
intelligence capabilities.

6.5 Research process innovation with AI and robot

As a public funding program related to self-driving laboratories
in Japan, the “R&D Process Innovation by AI and Robotics:

Technical Foundations and Practical Applications” eld was
launched by the JST in 2024. This funding primarily targets
young researchers and conducts three phases of three-and-a-half-
year research projects, with about 30 research proposals expected
to be selected in total. The purpose of this program is to revo-
lutionize the R&D process through the use of AI and robotics. By
introducing AI and robotics, the program aims not only to free
researchers and engineers from simple tasks but also to enable
them to tackle complex challenges beyond conventional cogni-
tive and physical capabilities. It is anticipated that by advancing
R&D through collaboration between researchers, engineers, and
AI and robotics, unprecedented scientic discoveries and tech-
nological innovations will be realized, transforming the nature of
R&D. This program seeks proposals from researchers in AI,
robotics, and applied elds such as life science and materials
science, with the goal of creating foundational technologies that
contribute to innovating the R&D process using AI and robotics.
By fostering close collaboration among researchers in these
elds, the program promotes the construction of methodologies
and their practical applications for R&D powered by AI and
robotics. By linking foundational technology development with
practical applications in scientic and technological research,
the program aims to build a general-purpose framework for
autonomously driven R&D, creating new scientic discoveries
and technological innovations.

7 Ecosystem

Collaboration among researchers or industry partners is indis-
pensable for developing SDLs that require experts from various
elds. This section reviews the eﬀorts to promote collaboration
for SDLs. We introduce Japanese communities for lab auto-
mation users and developers in Section 7.1. An initiative in
a national research institute for sharing modules is described in
Section 7.2.

7.1 Community—LASA, LADEC and Digital Laboratory
Consortium

In Japan, the Laboratory Automation Suppliers' Association
(LASA) was established in May 2019 to accelerate the develop-
ment of complex laboratory automation systems by fostering
a regional community of developers.115 Recognizing that
modern laboratory automation demands expertise across
hardware, soware, operational management, and application
domains, LASA provides a platform where various experts with
diﬀerent backgrounds collaborate closely from the planning
stage. Through regular events like the monthly workshop and
the annual Laboratory Automation Developers Conference
(LADEC), LASA oﬀers opportunities for members to stay upda-
ted on the latest developments, share insights, and engage in
face-to-face collaborations. These events feature talks, discus-
sions, and activities that cover a broad spectrum of topics, from
hardware customization to soware and AI development, as
well as operational best practices. Several outcomes inuenced
by collaborations and discussions within that community have
been published to date.43,44,46,47,49,116–120

1394 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

As of October 2024, LASA has grown to over 3200 members
from academia, industry, government agencies, and media,
facilitating cross-disciplinary interactions among researchers,
engineers, management, and students. By bridging the gap
between diverse elds of expertise, LASA plays a critical role in
advancing laboratory automation development in Japan and
serves as a model for regional developer communities.

As an organization dedicated to materials science, the Digital
Laboratory Consortium121 was established in September 2023,
bringing together more than 40 companies to exchange infor-
mation and develop technologies for automatic and autono-
mous experiments.

7.2 AUTOkobo at AIST

At the National Institute of Advanced Industrial Science and
Technology (AIST) Japan, eﬀorts are underway to increase
research eﬃciency and streamline experimental processes by
improving access to laboratory automation. This initiative,
called “AUTOkobo,” was developed as part of the in-house
“Multi-Modal AI” (MMAI) project,122 which aims to improve
digital transformation (DX) literacy among researchers. The
MMAI project enables even beginners to develop advanced AI
technologies through education and shared programming
resources. Recognizing the need for more eﬃcient data acqui-
sition, the AUTOkobo was launched in 2023 and has since
expanded to all seven research departments at AIST.

The AUTOkobo focuses on automating traditionally batch-
based experimental processes, particularly in areas such as,
polymers, inorganic materials, thin lms, and ceramics. Central

to its approach is the modularization of laboratory processes
(Fig. 11, below). Automation modules, such as robots and liquid
or powder dispensing devices, are provided free of charge,
allowing researchers to integrate them into their workows to
perform complex tasks. In Self-Driving Lab (SDL) systems,
robotics and peripherals manage the ow of materials between
instruments, while the AUTOkobo team supports system inte-
gration to reduce the burden on the researchers. In addition, the
AUTOkobo is developing a workspace that serves as both
a showroom and a workshop for automation technologies,
allowing researchers to engage in hands-on examination of the
available modules and instruments. This modular approach
addresses key challenges in laboratory automation, including
low costs, system exibility, and integration of new systems into
conventional experimental setups. By providing exible auto-
mation modules, researchers can automate experiments without
nancial risk, and once completed, modules can be reused by
others. In this way, the AUTOkobo approach not only saves time
and resources but also promotes the widespread adoption of
automation across diverse research domains, including poly-
mers, inorganic materials, thin lms, and ceramics.

8 Industry support for SDL
development

Japan has active manufacturing industries, and universities and
research institutes oen collaborate closely with companies to
develop SDLs. This section outlines the contributions of Japa-
nese industries to SDL development and highlights partner-
ships between academia and industry. Section 8.1 introduces
robotic arms developed in Japan, Section 8.2 highlights custom-
made automation systems created through collaborations, and
Section 8.3 showcases soware development eﬀorts.

8.1 Robotic arms

Robotic arms play a central role in some SDLs for their dexterity
in object handling. Japan has competitive robot manufacturers,
including FANUC and YASKAWA, which are two of the “Big 4”,
the four largest industrial robot manufacturers in the world. They
provide diﬀerent kinds of robot arms for SDLs. For example,
Maholo LabDroid (Section 3.1) was developed by YASKAWA and
the Robotic Biology Institute. A collaborative robot COBOTTA by
DENSO WAVE is adopted in the autonomous X-ray diﬀraction
analysis system33 (Section 2.7) and a robotic pipetting system for
plant pots.123 Industrial robotic arms from DENSO WAVE are
integrated into a multiarm robotic platform for scientic explo-
ration.124 An industrial robot MELFA from MITSUBISHI ELEC-
TRIC has been incorporated into an automatic gamma-ray
activation analysis system at Japan Atomic Energy Agency.125 A
dual-arm robot NEXTAGE from Kawada Robotics has been
utilized in the cell culture system in a pharmaceutical company
Eisai126 and powder dispensing system by ExaWizards.127

Fig. 11 Conceptual image of AUTOkobo infrastructure accelerating
SDL development
in AIST. Automation modules, such as liquid
dispensing or powder dispensing, are developed and shared allowing
each SDL to integrate them into their systems to perform complex
tasks.

8.2 Custom-made lab automation system
SDLs in Japan are oen developed through close collaboration
between academia and industry. For example, Shimadzu

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1395

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

Corporation and Kobe University jointly developed an autono-
mous laboratory system for biotechnology research and
demonstrated the optimization of medium conditions for
bacteria to improve glutamic acid production.128 KiQ Robotics
developed Lab Auto, an integrated system that automates RNA
evolution experiments at The University of Tokyo.129 Here, we
present three case studies from SDLs developed by the authors
to highlight the real-world challenges and their solutions.

The rst case study is the Lab Full Automation system from
ForDx.130 The collaboration between ForDX and Furukawa
Electric Advanced Engineering Co., Ltd brought expertise in
developing automation technology that integrates dispensing
and measurement devices. However, they lacked the capability
to create a self-driving laboratory by incorporating AI algo-
rithms. To address this, NIMO (Section 5.2) was employed to
establish a closed-loop system between experiments and AI,
enabling the development and commercialization of self-
driving laboratory devices. In Japan, the development of hard-
ware and soware for machine learning has traditionally been
conducted independently. We recognize that fostering close
integration between these two elements is a key challenge for
the widespread adoption of self-driving laboratories in Japan.

Another case study is from HORIBA, Ltd that is collaborating
with ROPES (Section 2.8). The FC(fuel cell)-ROPES, shown in
Fig. 7(d) and (e), was developed by a nationally-funded project
by the New Energy and Industrial Technology Development
Organization (NEDO) with the initial users from R&D sites at
Japanese fuel cell stack OEMs,
including Toyota, Honda,
Panasonic, and Toshiba. These companies required a higher-
throughput system for exploring process parameters that
could be applied in real factories. While they were interested in
automation, traditional R&D methods based on manual labor
were estimated to be more cost-eﬀective compared to automa-
tion systems developed independently by individual companies.
To overcome this barrier and promote system adoption, it was
necessary to reduce the unit price and increase the operating
eﬃciency. To achieve this, the FC-ROPES was designed with
three design-philosophies: (i) scalability, including a wide range
of process parameters and customizable evaluation units (e.g.,
customer-selectable objective functions) (ii) desktop size for
quick delivery and fast returns and adaptability to project
changes, and (iii) the ability to function as a pilot line for real
factories. As demand for fuel cells grows and prices decrease,
the system can be expanded horizontally to other applications
using powder-lm-formation processes, such as batteries or
ceramic lms. Furthermore, when the number of users of the
production process R&D increases, commoditization is likely to
spread among academic researchers as well.

Finally, Nishio, Hitosugi et al. have recently constructed
a digital laboratory, called dLab, which interconnects instru-
ments using robots to collect experimental data (including
synthesis processes, measured physical properties, and
measurement conditions) for solid materials research in thin-
lm form.131 Several modular experimental instruments are
interconnected (Fig.
automated material
synthesis, measurement, and analysis. Data from the instru-
ments are output in the MaiML format and stored in a cloud-

allowing

12),

Fig. 12 Schematic of
materials.131

the digital

laboratory (dLab)

for thin ﬁlm

based database. JEOL Ltd has developed an automated scan-
ning electron microscope for thin lm samples that can be
connected to the dLab system (Fig. 12). Rigaku Corp. has
developed a thin-lm X-ray diﬀractometer that works with
a robot for experiments, both of which are commercially avail-
able. Additionally, Shimadzu Corp. and HORIBA, Ltd provide
optical properties measurement systems. All these instruments
follow established standards for physical connections and
communication protocols, which are publicly available.132 The
dLab system autonomously synthesized high-quality LiCoO2
(001) thin lms, optimizing the X-ray diﬀraction peak-intensity
ratio using Bayesian methods. The diﬀraction pattern les in
MaiML format on the cloud were automatically analyzed, and
Bayesian optimization autonomously proposed the next thin-
lm deposition condition to obtain better-quality thin lms. It
showcases advanced autonomous material synthesis driven by
data and robotics for materials science.

In addition, companies oen collaborate to develop labora-
tory automation systems. A robotic system for mouse tail vein
injection developed by Preferred Networks and Chugai Pharma-
ceutical133 is a notable example, which is now commercialized as
AUTiv.134 TORCH, Inc. provides laboratory automation solutions
to companies, such as automated pouring and closing of sample
containers with collaborative robots at Lion Corporation.135

8.3 Soware development

In Japan,

To realize SDLs, it is important to develop programs to control
each device. These programs are implemented in Python, Lab-
there are
VIEW, and various other languages.
companies that can help with the development of the control
programs of devices. For example, CJS Inc. has created a Lab-
VIEW program to control a syringe pump, contributing to
developing an automated autonomous odor blending system.136
Furukawa Electric Advanced Engineering has developed
a program for automated dispensing equipment, which has
been implemented in the robotic experimental setup for
searching electrochemical materials discovery (see Section 2.3).

9 For the future of SDLs

We have reviewed the current state of SDLs in Japan. While
signicant
their adoption

research has been conducted,

1396 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

remains limited due to various challenges. Further democrati-
zation is necessary for wider adaptation of SDL technologies.56
This section identies the key barriers and explores potential
strategies to alleviate them, facilitating broader implementa-
tion of SDLs.

Adopting SDLs may face several challenges, one of which is
a reluctance to change. Many researchers oen prefer to rely on
traditional methods and hesitate to adopt next-generation
to familiarity with traditional
strategies, perhaps due
methods, technological barriers,
lack of trust in the new
methodologies, etc. This issue can be mitigated through the
education of young researchers, particularly during the early
stages of their training. Educational eﬀorts in Japan aimed at
nurturing future automation developers are introduced in
Section 9.1. Another challenge lies in the high cost of hardware
and soware development. Many current SDLs are monolithic,
meaning they are entirely custom-built with non-replaceable
components. Standardization plays an important
role in
reducing costs and enhancing exibility (modularity and
expandability).
enable modular
systems, allowing users to customize setups, select aﬀordable
hardware, and optimize their systems based on their require-
ments. Standardization also allows soware reuse. This topic is
further explored in Section 9.2. Finally, benchmarks are vital in
helping users select appropriate methods and guiding devel-
opers in taking their rst steps into SDL development. Several
benchmarks for SDL research are proposed in Section 9.3 to
support this objective.

Standardized interfaces

research to those using a micropipette for the rst time, but all
were new to programming robots for experiments. Through
collaborative learning and tackling assignments, they gained
various stimulating experiences. Plans are underway to transfer
the course to other universities.

The Department of Chemistry at The University of Tokyo
oﬀers Information Chemistry as a regular lecture course,
teaching the basics of materials informatics and SDL to third-
year undergraduates and above.138 The lecture also includes
hands-on experience with machine learning and teaching robots
to perform specic motions. This is a unique lecture in Japan as
there are still only a few institutions that can teach robotics in
chemistry.139 At the Institute of Tokyo Science (Science Tokyo),
materials informatics can be studied systematically in an orga-
nization called TAC-MI; basic education on SDL has also been
initiated.140 These educational eﬀorts can provide young students
and potential future researchers with a foundational under-
standing of new technologies as well as oﬀer a hands-on expe-
rience that helps reduce the mental barriers to their adoption.141
In addition to lectures at universities, textbooks written in
local languages help disseminate knowledge about SDLs to
a broader audience. A book entitled ‘Intersection of Materials,
Machine Learning, and Robotics’142 has been published to
support the development of the community. LASA (see Section
7.1) is also planning to create a textbook on laboratory auto-
mation. These resources will be valuable to the eld by
providing researchers with foundational knowledge and
making SDL development more accessible.

9.1 Education

9.2 Standardization

To enhance the development of SDLs in the future, education
programs that familiarize students with the concept of SDLs are
necessary. Several lecture courses have already been provided in
Japanese universities for this purpose.

At Keio University, a practical training course on AI-robotic
science has been oﬀered to undergraduates. As part of the
JST-Mirai Program described in Section 6.1, from 2021 to 2024,
a 5–6 days intensive course titled “Automation of Scientic
Experiments” was conducted using actual robots.137 The course
was designed to allow students to experience how AI connected
to experimental robots can discover new knowledge through
automated experiments. Specically, students learned to
program experimental protocols for liquid-handling experi-
ments, which are fundamental techniques for PCR tests and
chemical experiments—using Python to fully control the OT-2
liquid-handling robot (Opentrons Labworks Inc.). They also
built an automated experimental planning AI that interprets
results, plans subsequent experiments, and instructs the robot,
creating an AI-robot system that autonomously performs
scientic experiments. By rst manually performing the exper-
imental processes and then implementing them into the robot
and AI, students gained a deeper understanding of how the
collaboration between humans, automation, and AI can
enhance problem-solving capabilities, foster creativity, and
improve learning outcomes in addition to their respective roles.
Participants ranged from students engaged in life science

SDLs typically connect devices such as robot arms and
measurement
instruments. As automation system require-
ments change, hardware and soware may need replacement.
Standardization is crucial for creating exible systems that
allow hardware to be replaced while keeping soware changes
minimal. Key areas of standardization include hardware
dimensions, physical connection interfaces, and communica-
tion protocols. Modularity achieved through standardization
can lower development costs and encourage broader adoption
of SDL technologies.

I/O buses. Similarly,

Several initiatives have been undertaken by various groups to
address this need for standardization. For instance, the IVI
Foundation provides open industry standard soware archi-
tectures, including the Virtual Instrument Soware Architecture
(VISA),143 which aims to improve the interchangeability of test
and measurement instruments that communicate through
the SiLA Consortium144
a variety of
develops open standards to support the integration of labora-
tory automation systems. Recently, the Laboratory and Analyt-
ical Device Standard (LADS)145 has been introduced as
a manufacturer-independent, open standard for analytical and
laboratory equipment.
is built upon Open Platform
Communications Unied Architecture (OPC UA) and aims to
improve the plug and play interoperability of analytical devices.
These eﬀorts involve manufacturers and impact the direction of
hardware development.

It

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1397

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

Japan Analytical Instruments Manufacturers Association
laboratory and
(JAIMA) advances the standardization of
analytical
instruments in Japan. JAIMA contributed to the
development of LADS OPC UA and the standardization of the
MaiML format (Section 2.2) as Japanese Industrial Standards
(JIS K 0200).

including academia and industry,

Although standards play a crucial role in enhancing inter-
operability, the real challenge lies in ensuring their widespread
adoption and compliance. Close collaboration between stake-
holders,
to
developing practical and eﬀective standards. Additionally, the
existence of multiple competing standards may undermine the
intended benets of standardization. To facilitate global
adoption,
to
promoting the broad implementation of these standards.

collaboration is also critical

international

is essential

9.3 Benchmark for SDLs

Benchmarks have been helpful for various research areas by
facilitating the comparison of diﬀerent methods, and the need
for standard benchmarks for SDLs was highlighted during the
authors' meeting. Here we propose potential benchmarking
tasks to evaluate the practical utility of lab automation systems
to enhance the international discussion on establishing SDL
benchmarks.

9.3.1 Powder dispensing.

In comparison with liquid
dispensers, powder dispensing is still tricky because of the
complex mechanics of small particles. The use of robotic arms
has been investigated recently88,146 to overcome the limitations
of commercial devices such as Chemspeed or Quantos (Mettler
Toledo). Due to the widespread nature of the task and the
diversity of approaches available, powder dispensing is suitable
for a benchmarking task. Benchmark criteria can include speed,
accuracy, and hardware cost, allowing researchers to develop
robotic systems optimized for specic performance aspects.

9.3.2 Viscous liquid handling. Working with viscous liquid
is required in various experiments. For instance, this may be the
case when using compounds with melting points near room
temperature, such as di-tert-butyl dicarbonate or tri-tert-butyl-
phosphine, as reagents, or when using highly viscous polymers
or oligomers as reaction substrates. Furthermore, in industrial
production, reducing the amount of solvent oen enhances
productivity, which frequently necessitates the consideration of
concentrated solutions. However,
high-viscosity, highly
currently available liquid handlers sometimes have diﬃculties
in treating viscous liquids, and optimization of the liquid
handling parameters is necessary for desirable performance.147
Benchmarks on viscous liquid handling would help developers
choose an appropriate device for their use case. Polyethylene
glycol (PEG) can be used as a viscosity standard because of the
diversity in viscosity.

9.3.3 Robot performance in realistic tasks. Precise object
handling is oen required to complete regular tasks in SDLs,
such as microplate placing.148 Although the manufacturers
usually provide the repeatability of their robotic arm, this
metric does not always reect their precision in practical
applications since various factors, such as payload, can aﬀect

the performance of the robot. Harazono, et al.116 developed
a platform to evaluate the microplate handling accuracy of
robot arms. Practical benchmarks like this are useful for
assessing the real-world performance of robotic systems.

10 Conclusions

This perspective has highlighted the advancements in SDL
research in Japan, spanning material sciences, biology, and
organic chemistry. Furthermore, we have explored the roles of
community collaboration, funding initiatives, and the industry
that supports the growth of SDLs.

Compared to SDLs developed in other countries, a distinc-
tive characteristic of Japan's SDL development might be the
strong collaboration between academia and industry. As dis-
cussed in Section 8, universities and national research insti-
tutes in Japan frequently partner with industrial collaborators,
including small companies, to develop custom automation
hardware tailored to specic research needs. In addition to
Japan's strong automation industry, active measurement and
analysis equipment manufacturers, holding an 8% of the global
market share as of 2021 and ranking third aer the United
States and Germany,149 are supporting the development of
Japanese SDLs. The integral nature of SDLs also aligns with the
strengths of Japanese manufacturers, as Japan tends to have
a comparative advantage in products with a more integral
architecture.150 However, it has been pointed out that Japanese
robotics research is lagging, reecting the relatively weak
performance in the eld of AI.151 Advancements in AI may also
be crucial for the further development of SDLs in Japan.

In addition to research institutes, companies also show
strong interest in SDLs. Japan has a large concentration of
materials, automation, and scientic equipment industries.
These companies are making eﬀorts to introduce SDLs to
enhance the creativity of researchers. Although the number of
SDLs is still small, their use is steadily spreading. By building
synergy among diverse players, SDLs in Japan will continue to
develop and drive innovation in the eld.

Data availability

As this is a Perspective article, no primary research results, data,
soware or code have been included.

Author contributions

Conceptualization (organizers)—D. N. F., T. H., K. Nis., W. S., S.
T., K. Tsu., N. Y.; writing (original dra)—Section 1: N. Y.;
Section 2.1, 2.2: T. H., K. Nis.; Section 2.3: S. M.; Section
2.4: M. N.; Section 2.5, 2.6: Y. A., J. S., K. S.; Section 2.7: K. O.;
Section 2.8: K. Nag.; Section 3: G. N. K., T. N., H. O., K. Tak.;
Section 4: Y. N.; Section 5.1: S. T.; Section 5.2: R. T.; Section 5.3:
Y. U.; Section 5.4: N. Y.; Section 6.1: K. Tak.; Section 6.2: K. Nag.;
Section 6.3: K. H.; Section 6.4: Y. U.; Section 6.5: I. T.; Section
7.1: T. H., G. N. K.; Section 7.2: D. N. F., W. S.; Section 8: T. H., K.
Nag., K. Nis., R. T., N. Y.; Section 9.1: T. H., G. N. K., H. O.;

1398 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

Section 9.2, 9.3, 10: N. Y.; Writing (review & editing)—D. N. F., N.
Y.; project administration—N. Y.

University of Osaka) for providing Fig. 6. We appreciate Toru
Ishikuma (JAIMA) for reviewing the content of Section 9.2.

Conﬂicts of interest

References

Tohru Natsume is an executive at Robotic Biology Institute Inc.,
which may benet nancially from the increased scientic use
of Maholo LabDroid.

Acknowledgements

Stress

and Multilayered

Y. A., K. S., and J. S. acknowledge the support of JSPS KAKENHI
(23K03771), JST CREST (JPMJCR21O2), and Daikin Industries,
Ltd. K. H. acknowledges the support of JST Moonshot R&D
JPMJMS2033. T. H. and K. Nishio acknowledge the support of
the JST-Mirai Program JPMJMI21G2, JST CREST (JPMJCR22O4),
JSPS KAKENHI (24K01599), NEDO Project (P20003), and MEXT
Program: Data Creation and Utilization-Type Material Research
and Development Project Grant Number JPMXP1122712807.
G. N. K. acknowledges the support of Grant-in-Aid for Scientic
Research (C) (JP23K11820). G. N. K. and N. Y. are supported by
Medical Research Center Initiative for High Depth Omics,
Nanken-Kyoten,
Diseases
(JPMXP1323015483), Science Tokyo. Y. N. acknowledges the
support of JST-ERATO (JPMJER1903), JSPS KAKENHI Grant
Numbers JP21H01924 and JP23H03810, and the Institute for
Chemical Reaction Design and Discovery (ICReDD), which was
established by the World Premier International Research
Initiative (WPI), MEXT, Japan. K. Nagato acknowledges the
support of JST-Mirai Program JPMJMI21G2, JST-Mirai Program
JPMJMI19G3, and NEDO Project 23200629-0. M. N. acknowl-
edges the support of JST CREST (JPMJCR19J3), MEXT Program:
Data Creation and Utilization-Type Material Research and
Development Project Grant Number JPMXP1122714694, and
COI-NEXT (JPMJPF2102). H. O. and K. Takahashi acknowledge
the
and
JPMJMI20G7). H. O. also acknowledges the support of Grant-in-
Aid for Early-Career Scientists (JP22K17992) and Grant-in-Aid
for Transformative Research Areas (A) (JP23H04149). K. O.
acknowledges the support of JST-Mirai Program JPMJMI19G1,
MEXT Program: Data Creation and Utilization-Type Material
Research and Development Project (Digital Transformation
(Grant Number
for Magnetic Materials)
Initiative Center
JPMXP1122715503),
Program: Developing
a Research Data Ecosystem for the Promotion of Data-Driven
Science. I. T. acknowledges the support of MEXT KAKENHI
(20H00601), JST CREST (JPMJCR21D3), JST Moonshot R&D
(JPMJMS2033-05), and RIKEN Center for Advanced Intelligence
Project. R. T. acknowledges the support of
JST-PRESTO
(JPMJPR24T8). Y. U. and K. O. acknowledge the support of JST
Moonshot R&D JPMJMS2236. K. Takahashi and Y. U. are sup-
ported by Advanced General Intelligence for Science Program
(AGIS), the RIKEN TRIP initiative. We thank Yasuhiro Naito of
Keio University for assistance with the writing of Section 9.1. We
are grateful to Yumiko Miyahara for preparing the graphical
abstract and Fig. 1. We also thank Yusaku Nakajima (The

JST-Mirai Program (JPMJMI18G4

and MEXT

support

of

1 G. Tom, S. P. Schmid, S. G. Baird, Y. Cao, K. Darvish,
H. Hao, S. Lo, S. Pablo-Garc´ıa, E. M. Rajaonson,
M. Skreta, N. Yoshikawa, S. Corapi, G. D. Akkoc,
F. Strieth-Kalthoﬀ, M. Seifrid and A. Aspuru-Guzik, Chem.
Rev., 2024, 124, 9633–9732.

2 World Robotics 2023 Report: Asia ahead of Europe and the
https://ifr.org/ifr-press-releases/news/world-

Americas,
robotics-2023-report-asia-ahead-of-europe-and-the-
americas, accessed May 2025.

3 R. Matsuda, M. Ishibashi and Y. Takeda, Chem. Pharm.

Bull., 1988, 36, 3512–3518.

4 M. Sasaki, T. Kageoka, K. Ogura, H. Kataoka, T. Ueta and

S. Sugihara, Clin. Chim. Acta, 1998, 278, 217–227.

5 J. Boyd, Science, 2002, 295, 517–518.
6 About DxMT, https://dxmt.mext.go.jp/en/about, (accessed

April 2025).

7 R. Shimizu, S. Kobayashi, Y. Watanabe, Y. Ando and

T. Hitosugi, APL Mater., 2020, 8, 111110.

8 S. Kobayashi, R. Shimizu, Y. Ando and T. Hitosugi, ACS

Mater. Lett., 2023, 5, 2711–2717.

9 R. Nakayama, R. Shimizu, T. Haga, T. Kimura, Y. Ando,
S. Kobayashi, N. Yasuo, M. Sekijima and T. Hitosugi, Sci.
Technol. Adv. Mater.:Methods, 2022, 2, 119–128.

10 H. Xu, R. Nakayama, T. Kimura, R. Shimizu, Y. Ando,
S. Kobayashi, N. Yasuo, M. Sekijima and T. Hitosugi, Sci.
Technol. Adv. Mater.:Methods, 2023, 3, 2210251.

11 K. Nishio et al., Talk at the Accelerate Conference, 2024

(https://www.accelerate24.ca/program-3).

12 N. Ishizuki, R. Shimizu and T. Hitosugi, Sci. Technol. Adv.

Mater.:Methods, 2023, 3, 2197519.

13 S. H. M. Mehr, M. Craven, A. I. Leonov, G. Keenan and

L. Cronin, Science, 2020, 370, 101–108.

14 S. Ichimura, T. Sigehuzi, T. Yasunaga and S. Inoue, Oyo

Buturi, 2023, 92, 142–146.

15 M. Aykol, P. Herring and A. Anapolsky, Nat. Rev. Mater.,

2020, 5, 725–727.

16 K. Xu, Chem. Rev., 2014, 114, 11503–11618.
17 S. Matsuda, K. Nishioka and S. Nakanishi, Sci. Rep., 2019, 9,

6211.

18 S. Matsuda, G. Lambard and K. Sodeyama, Cell Rep. Phys.

Sci., 2022, 3, 100832.

19 R. Tamura, K. Tsuda and S. Matsuda, Sci. Technol. Adv.

Mater.:Methods, 2023, 3, 2232297.

20 S. Matsuda, S. Kimura and M. Takahashi, Batteries

Supercaps, 2024, 7, e202400509.

21 S. Schmatloch, M. A. R. Meier and U. S. Schubert, Macromol.

Rapid Commun., 2003, 24, 33–46.

22 S. Oliver, L. Zhao, A. J. Gormley, R. Chapman and C. Boyer,

Macromolecules, 2019, 52, 3–23.

23 G. K. K. Clothier, T. R. Guimar˜aes, S. W. Thompson,
S. C. Howard, B. W. Muir, G. Moad and P. B. Zetterlund,
Angew. Chem., Int. Ed., 2024, 63, e202320154.

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1399

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

24 M. Seifrid, F. Strieth-Kalthoﬀ, M. Haddadnia, T. C. Wu,
E. Alca, L. Bodo, S. Arellano-Rubach, N. Yoshikawa,
M. Skreta, R. Keunen and A. Aspuru-Guzik, Digital
Discovery, 2024, 3, 1319–1326.

25 C. Kang, J. J. M. Machado, Y. Sekiguchi, M. Ji, C. Sato and

M. Naito, J. Adhes., 2023, 99, 2080–2096.

26 S. Takasuka, S. Ito, S. Oikawa, Y. Harashima, T. Takayama,
A. Nag, A. Wakiuchi, T. Ando, T. Sugawara, M. Hatanaka,
T. Miyao, T. Matsubara, Y.-Y. Ohnishi, H. Ajiro and
M. Fujii, Sci. Technol. Adv. Mater.:Methods, 2024, 4, 2425178.
27 C. Kang, M. Ji, Y. Sekiguchi, M. Naito and C. Sato, J. Adhes.,

2023, 101, 18–40.

K. Matsukuma, T. Natsume, G. N. Kanda, M. Takahashi
and K. Takahashi, SLAS Technol., 2021, 26, 209–217.

44 M. Terada, Y. Kogawa, Y. Shibata, M. Kitagawa, S. Kato,
T. Iida, T. Yorimitsu, A. Kato, K. Matsukuma, T. Maeda,
M. Takahashi and G. N. Kanda, SLAS Technol., 2023, 28,
449–459.

45 N. Yachie, R. B. Consortium and T. Natsume, Nat.

Biotechnol., 2017, 35, 310–312.

46 T. D. Itoh, T. Horinouchi, H. Uchida, K. Takahashi and

H. Ozaki, SLAS Technol., 2021, 26, 650–659.

47 Y. Arai, K. Takahashi, T. Horinouchi, K. Takahashi and

H. Ozaki, SLAS Technol., 2023, 28, 264–277.

28 Y. Asano, K. Okada, S. Nakagawa, N. Yoshie and J. Shiomi,

48 K. Tachibana and H. Ozaki, OT2Eye (1.0.1), 2024, DOI:

Robot. Auton. Syst., 2025, 185, 104868.

10.5281/zenodo.13923719.

29 Y. Asano, K. Okada and J. Shiomi, IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), 2024,
DOI: 10.1109/IROS58592.2024.10802186.

49 T. Inagaki, A. Kato, K. Takahashi, H. Ozaki and G. N. Kanda,
arXiv, 2023, preprint, arXiv:2304.10267, DOI: 10.48550/
arXiv.2304.10267.

30 A. Sakurai, K. Yada, T. Simomura, S. Ju, M. Kashiwagi,
H. Okada, T. Nagao, K. Tsuda and J. Shiomi, ACS Cent.
Sci., 2019, 5, 319–326.

31 J. Guo and J. Shiomi, Next Energy, 2024, 2, 100078.
32 Y. Nakajima, K. Kawasaki, Y. Takeichi, M. Hamaya,
Y. Ushiku and K. Ono, Digital Discovery, 2024, 3, 2130–2136.
33 Y. Yotsumoto, Y. Nakajima, R. Takamoto, Y. Takeichi and

K. Ono, Digital Discovery, 2024, 3, 2523–2532.

34 K. Nagai, T. Osa, G.

Inoue, T. Tsujiguchi, T. Araki,
Y. Kuroda, M. Tomizawa and K. Nagato, Sci. Rep., 2022,
12, 1615.

35 Experience the ”feeling of powder”!! ROPES, https://
www.youtube.com/watch?v=QySre6yKSSM, (accessed April
2025).

36 Autonomous Experiment with AI&Robot, https://youtu.be/

_JM4BZHsSKQ, (accessed April 2025).

37 H. Zhu, H. Zhang, Y. Xu, S. Laˇsˇs´akov´a, M. Korabeˇcn´a and

P. Neuˇzil, BioTechniques, 2020, 69, 317–325.

38 G. N. Kanda, T. Tsuzuki, M. Terada, N. Sakai, N. Motozawa,
T. Masuda, M. Nishida, C. T. Watanabe, T. Higashi,
S. A. Horiguchi, T. Kudo, M. Kamei, G. A. Sunagawa,
K. Matsukuma, T. Sakurada, Y. Ozawa, M. Takahashi,
K. Takahashi and T. Natsume, eLife, 2022, 11, e77007.
39 W. A. Kamel, E. Sugihara, H. Nobusue, S. Yamaguchi-Iwai,
N. Onishi, K. Maki, Y. Fukuchi, K. Matsuo, A. Muto, H. Saya
and T. Shimizu, Mol. Cancer Ther., 2017, 16, 182–192.
40 M. Sasamata, D. Shimojo, H. Fuse, Y. Nishi, H. Sakurai,
T. Nakahata, Y. Yamagishi and H. Sasaki-Iwaoka, SLAS
Technol., 2021, 26, 441–453.

41 A. W. Liu, A. Villar-Briones, N. M. Luscombe and C. Plessy,
10.12688/

2022,

DOI:

11,

F1000Research,
f1000research.109251.1.

42 S. Kaneko, T. Mitsuyama, K. Shiraishi, N. Ikawa, K. Shozu,
A. Dozen, H. Machino, K. Asada, M. Komatsu, A. Kukita,
K. Sone, H. Yoshida, N. Motoi, S. Hayami, Y. Yoneoka,
T. Kato, T. Kohno, T. Natsume, G. v. Keudell, V. Saloura,
H. Yamaue and R. Hamamoto, Cancers, 2021, 13, 2126.
43 K. Ochiai, N. Motozawa, M. Terada, T. Horinouchi,
T. Masuda, T. Kudo, M. Kamei, A. Tsujikawa,

50 C. Armer, F. Letronne and E. DeBenedictis, PLoS Biol., 2023,

21, e3001919.

51 Y. Nagata, Y.-Z. Ke and M. Suginome, Chem. Lett., 2015, 44,

53–55.

52 Y. Nagata, K. Takagi and M. Suginome, J. Am. Chem. Soc.,

2014, 136, 9858–9861.

53 R. Shirasawa, I. Takemura, S. Hattori and Y. Nagata,

Commun. Chem., 2022, 5, 158.

54 N. Tsuji, P. Sidorov, C. Zhu, Y. Nagata, T. Gimadiev,
A. Varnek and B. List, Angew. Chem., Int. Ed., 2023, 62,
e202218659.

55 S. Akiyama, H. Akitsu, R. Tamura, W. Matsuoka, S. Maeda,
K. Tsuda and Y. Nagata, ChemRxiv, 2024, preprint, DOI:
10.26434/chemrxiv-2024-bnj6p-v2.

56 S. Lo, S. G. Baird, J. Schrier, B. Blaiszik, N. Carson, I. Foster,
A. Aguilar-Granda, S. V. Kalinin, B. Maruyama, M. Politi,
H. Tran, T. D. Sparks and A. Aspuru-Guzik, Digital
Discovery, 2024, 3, 842–868.

57 M. Kuwahara, Y. Hasukawa, F. Garcia-Escobar, S. Maeda,
L. Takahashi and K. Takahashi, ACS Appl. Eng. Mater.,
2025, 3, 978–987.

58 Y. Wang, J. Wang, Z. Cao and A. Barati Farimani, Nat. Mach.

Intell., 2022, 4, 279–287.

59 S. Chithrananda, G. Grand and B. Ramsundar, arXiv, 2020,
10.48550/

arXiv:2010.09885,

DOI:

preprint,
arXiv.2010.09885.

60 V. Y. Shirasuna, E. Soares, E. V. Brazil, K. F. A. Gutierrez,
R. Cerqueira, S. Takeda and A. Kishimoto, ICML 2024 AI
for Science Workshop, 2024, https://openreview.net/
forum?id=PkDHmg2JLI.

61 S. Takeda, A. Kishimoto, L. Hamada, D. Nakano and
J. R. Smith, Proc. AAAI Conf. Artif. Intell., 2024, 37, 15376–
15383.

62 Example 6 – Human-in-the-loop design of more soluble
(smi-TED),

molecules with IBM's embedding model
https://mehradans92.github.io/dZiner/
solubility_inference_IBM_representation_learning.html,
(accessed April 2025).

1400 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

63 RoboRXN:

automating

chemical

synthesis, https://

85 Y. Suzuki, T. Taniai, K. Saito, Y. Ushiku and K. Ono, Mach.

research.ibm.com/blog/roborxn-automating-chemical-
synthesis, (accessed April 2025).

Learn.: Sci. Technol., 2022, 3, 045034.

86 N. Chiba, Y. Suzuki, T. Taniai, R. Igarashi, Y. Ushiku,

64 Foundation Model for Materials – FM4M, https://github.com/

K. Saito and K. Ono, Commun. Mater., 2023, 4, 106.

IBM/materials, accessed April 2025.

65 Materials and Chemistry Working Group j AI Alliance,

https://thealliance.ai/working-groups/materials-and-
chemistry, (accessed April 2025).

66 T. Ueno, T. D. Rhone, Z. Hou, T. Mizoguchi and K. Tsuda,

Materials Discovery, 2016, 4, 18–21.

67 Y. Motoyama, R. Tamura, K. Yoshimi, K. Terayama, T. Ueno
and K. Tsuda, Comput. Phys. Commun., 2022, 278, 108405.
68 K. Terayama, R. Tamura, Y. Nose, H. Hiramatsu,
H. Hosono, Y. Okuno and K. Tsuda, Phys. Rev. Mater.,
2019, 3, 033802.

69 R. Tamura, H. Morito, G. Deﬀrennes, M. Naito, Y. Nose,
T. Abe and K. Terayama, Commun. Mater., 2024, 5, 139.
70 AIPHAD Investigate Phase Diagrams using AI, https://

aiphad.org/, (accessed April 2025).

71 K. Terayama, M. Sumita, R. Tamura, D. T. Payne,
M. K. Chahal, S. Ishihara and K. Tsuda, Chem. Sci., 2020,
11, 5959–5968.

72 J. Li, J. Zhang, R. Tamura and K. Tsuda, Digital Discovery,

2022, 1, 295–302.

87 T. Taniai, R. Igarashi, Y. Suzuki, N. Chiba, K. Saito,
Y. Ushiku and K. Ono, The Twelh International
Conference on Learning Representations, 2024, https://
openreview.net/forum?id=fxQiecl9HB.

88 Y. Kadokawa, M. Hamaya and K. Tanaka,

IEEE/RSJ
International Conference on Intelligent Robots and Systems
(IROS), 2023, DOI: 10.1109/IROS55552.2023.10342463.

89 Y. Nakajima, M. Hamaya, Y.

Suzuki, T. Hawai,
F. v. Drigalski, K. Tanaka, Y. Ushiku and K. Ono, IEEE/RSJ
International Conference on Intelligent Robots and Systems
(IROS), 2022, DOI: 10.1109/IROS47612.2022.9981081.

90 K.

Shirai, C. C. Beltran-Hernandez, M. Hamaya,
A. Hashimoto, S. Tanaka, K. Kawaharazuka, K. Tanaka,
Y. Ushiku and S. Mori, IEEE International Conference on
Robotics and Automation (ICRA), 2024, DOI: 10.1109/
ICRA57147.2024.10611112.

91 N. Yoshikawa, M. Skreta, K. Darvish, S. Arellano-Rubach,
Z. Ji, L. Bjørn Kristensen, A. Z. Li, Y. Zhao, H. Xu,
A. Kuramshin, A. Aspuru-Guzik, F. Shkurti and A. Garg,
Auton. Robots, 2023, 47, 1057–1086.

73 K. Kitai, J. Guo, S. Ju, S. Tanaka, K. Tsuda, J. Shiomi and

92 D. A. Boiko, R. MacKnight, B. Kline and G. Gomes, Nature,

R. Tamura, Phys. Rev. Res., 2020, 2, 013319.

2023, 624, 570–578.

74 nimo, https://github.com/NIMS-DA/nimo, (accessed April

2025).

75 L. M. Roch, F. H¨ase, C. Kreisbeck, T. Tamayo-Mendoza,
L. P. E. Yunker, J. E. Hein and A. Aspuru-Guzik, PLoS One,
2020, 15, e0229862.

76 J. Li, Y. Tu, R. Liu, Y. Lu and X. Zhu, Advanced Science, 2020,

7, 1901957.

77 M. Sim, M. G. Vakili, F. Strieth-Kalthoﬀ, H. Hao,
R. J. Hickman, S. Miret, S. Pablo-Garc´ıa and A. Aspuru-
Guzik, Matter, 2024, 7, 2959–2977.

78 R. Katsube, K. Terayama, R. Tamura and Y. Nose, ACS

Mater. Lett., 2020, 2, 571–575.

79 K. Terayama, Y. Osaki, T. Fujita, R. Tamura, M. Naito,
K. Tsuda, T. Matsui and M. Sumita, J. Chem. Theory
Comput., 2023, 19, 6770–6781.

80 Y. Murakami, S. Ishida, Y. Demizu and K. Terayama, Digital

Discovery, 2023, 2, 1347–1353.

81 T. Liu, N. Astorga, N. Seedat and M. van der Schaar, The
Conference
Learning
on
https://openreview.net/forum?

International
2024,

Twelh
Representations,
id=OOxotBmGol.

82 C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune and D. Ha,
arXiv, 2024, preprint, arXiv:2408.06292, DOI: 10.48550/
arXiv.2408.06292.

83 Y. Matsubara, N. Chiba, R. Igarashi and Y. Ushiku, J. Data-
centric Mach. Learn. Res., 2024, 1(3), 1–38, https://
openreview.net/forum?id=qrUdrXsiXX.

84 F. Lalande, Y. Matsubara, N. Chiba, T. Taniai, R. Igarashi
and Y. Ushiku, NeurIPS 2023 AI for Science Workshop,
2023, https://openreview.net/forum?id=AIfqWNHKjo.

93 Y. Yamada, R. T. Lange, C. Lu, S. Hu, C. Lu, J. Foerster,
preprint,

J.
arXiv:2504.08066, DOI: 10.48550/arXiv.2504.08066.

and D. Ha,

Clune

arXiv,

2025,

94 K. Hatakeyama-Sato, N. Yamane, Y. Igarashi, Y. Nabae and
T. Hayakawa, Sci. Technol. Adv. Mater.:Methods, 2023, 3,
2260300.

95 K. Hatakeyama-Sato, S. Watanabe, N. Yamane, Y. Igarashi

and K. Oyaizu, Digital Discovery, 2023, 2, 1548–1557.

96 K. Hatakeyama-Sato, H. Ishikawa, S. Takaishi, Y. Igarashi,
Y. Nabae and T. Hayakawa, Polym. J., 2024, 56, 977–986.

97 S.

D.

Jiang,

Bersenev,
Evans-Yamamoto,
S. K. Palaniappan and A. Yachie-Kinoshita, SLAS Technol.,
2024, 29, 100134.

D.

98 K. Machi, S. Akiyama, Y. Nagata and M. Yoshioka, Digital

Discovery, 2025, 4, 172–180.

99 J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya,
F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman,
S. Anadkat et al., arXiv, 2023, preprint, arXiv:2303.08774,
DOI: 10.48550/arXiv.2303.08774.
100 H. Touvron, T. Lavril, G.

Izacard, X. Martinet,
M.-A. Lachaux, T. Lacroix, B. Rozi`ere, N. Goyal,
E. Hambro, F. Azhar et al., arXiv, 2023, preprint,
arXiv:2302.13971, DOI: 10.48550/arXiv.2302.13971.

101 D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu,

S. Ma, P. Wang, X. Bi et al., arXiv, 2025, preprint.

102 GENIAC,

mono_info_service/geniac/index.html,
2025).

https://www.meti.go.jp/english/policy/
April

(accessed

103 Accelerating Life Sciences by Robotic Biology, https://
www.jst.go.jp/mirai/en/program/core/JPMJMI20G7.html,
(accessed April 2025).

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1401

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlineDigital Discovery

Perspective

104 Materials Exploration Platform; Expanding Search Space by
technology, https://www.jst.go.jp/mirai/
high-throughput
en/program/core/JPMJMI21G2.html, (accessed April 2025).
105 Goal 3: HARADA Kanako Project j Moonshot R&D, https://

www.jst.go.jp/moonshot/en/program/goal3/
33_harada.html, (accessed April 2025).

106 Goal 3: USHIKU Yoshitaka Project j Moonshot R&D, https://

www.jst.go.jp/moonshot/en/program/goal3/
36_ushiku.html, (accessed April 2025).

107 AI Robot-Driven Science

Initiative, https://ai-robot-

science.com/en/, (accessed April 2025).

108 Research innovation through autonomous-driven research
https://www.mext.go.jp/b_menu/houdou/2023/

systems,
mext_00006.html, (accessed April 2025).

109 R&D Process Innovation by AI and Robotics: Technical
Foundations
https://
Practical
www.jst.go.jp/kisoken/presto/en/research_area/area2024-
1.html, (accessed April 2025).

Applications,

and

110 Common Platform Technology, Facilities, and Equipment”
mission area j JST-Mirai Program, https://www.jst.go.jp/
mirai/en/program/core/index.html, (accessed April 2025).

111 MEEP introduction video, short version (3 min. English
subtitle), https://youtu.be/Wg7E_rqMB5A, (accessed April
2025).

112 MEEP introduction video, full version (10 min. English
subtitle), https://youtu.be/_P6DomhaF8k, (accessed April
2025).

113 Y. Suzuki, H. Hino, T. Hawai, K. Saito, M. Kotsugi and

K. Ono, Sci. Rep., 2020, 10, 21790.

114 T. Fukushima, H. Akai, T. Chikyow and H. Kino, Phys. Rev.

Mater., 2022, 6, 023802.

127 ExaWizards

co-developed “exaBase

robotics powder
dispensing for NEXTAGE” with Kawada Robotics that
automates powder dispensing for manufacturing with
a humanoid dual-arm robot, https://exawizards.com/
archives/21909/, in Japanese, (accessed April 2025).

128 K. Fushimi, Y. Nakai, A. Nishi, R. Suzuki, M. Ikegami,
R. Nimura, T. Tomono, R. Hidese, H. Yasueda, Y. Tagawa
and T. Hasunuma, Sci. Rep., 2025, 15, 6648.

129 Development of “Lab Auto” that automates dispensation
and
https://prtimes.jp/main/html/rd/p/
000000004.000073464.html, in Japanese, (accessed April
2025).

agitation,

130 Autonomous lab automation system LFA series, https://
in

www.fordx.co.jp/product/labautomation.html,
Japanese, (Accessed April 2025).

131 K. Nishio, A. Aiba, K. Takihara, Y. Suzuki, R. Nakayama,
S. Kobayashi, A. Abe, H. Baba, S. Katagiri, K. Omoto,
K. Ito, R. Shimizu and T. Hitosugi, Digital Discovery, 2025,
DOI: 10.1039/D4DD00326H.

132 Standardization,

https://digital-laboratory.jp/en/

standardization.html, (Accessed April 2025).

133 T. Ko, K. Nishiwaki, K. Terada, Y. Tanaka, S. Mitsumata,
R. Katagiri, J. Taketo, N. Horiba, H. Igata and K. Mizuno,
IEEE International Conference on Robotics and Automation
(ICRA), 2022, DOI: 10.1109/ICRA46639.2022.9811804.
134 Automatic mouse tail vein injection system AUTiv, https://
www.summitpharma.co.jp/japanese/service/products/
autiv/, in Japanese (accessed April 2025).

135 Using collaborative robots for pouring and closing sample
https://www.lion.co.jp/en/rd/new-activity/

containers,
digital/case02.php, (accessed April 2025).

115 A. Kato, T. Horinouchi, H. Ozaki and G. N. Kanda, SLAS

136 Y. Fukui, K. Minami, K. Shiba, G. Yoshikawa, K. Tsuda and

Technol., 2024, 29, 100211.

116 Y. Harazono, H. Shimono, K. Hata, T. Mitsuyama and

T. Horinouchi, SLAS Technol., 2024, 29, 100200.

117 S. Taguchi, Y. Suda, K. Irie and H. Ozaki, SLAS Technol.,

2023, 28, 55–62.

118 Y. T. Fukai and K. Kawaguchi, Bioinformatics, 2022, 39,

btac799.

119 M. Jinno and R. Nonoyama, Robomech J., 2025, 12, 14.
120 M.

Jinno, R. Nonoyama, Y. Sakurai, R. Yoshikawa,

T. Kinoshita and J. Yasuda, ROBOMECH J., 2024, 11, 13.

121 Digital

Laboratory

Consortium,

https://digital-

laboratory.jp/en/index.html, (accessed April 2025).

122 Developing Technology to Predict Various Functions from
Complex Material Data Using Multimodal-AI, https://
www.aist.go.jp/aist_j/press_release/pr2022/pr20220630_2/
pr20220630_2.html, in Japanese, (accessed April 2025).
123 J. Zhang, W. Wan, N. Tanaka, M. Fujita, K. Takahashi and
K. Harada, IEEE Trans. Autom. Sci. Eng., 2024, 21, 5503–
5522.

124 M. M. Marinho, J. J. Quiroz-Omaña and K. Harada, IEEE

Robot. Autom. Mag., 2024, 31, 10–20.

125 T. Osawa, J. Radioanal. Nucl. Chem., 2015, 303, 1141–1146.
126 The use of robots in research, https://www.eisai.co.jp/
in

innovation/research/digital/robots/index.html,
Japanese, (accessed April 2025).

137 Automation

R. Tamura, Digital Discovery, 2024, 3, 969–976.
Experiments,

Scientic
syllabus.sfc.keio.ac.jp/courses/2024_46846?locale=en,
(accessed April 2025).

Of

https://

138 Information Chemistry, https://www.chem.s.u-tokyo.ac.jp/
April

(accessed

chem_research/information_en.html,
2025).
139 Information

Chemistry

https://
catalog.he.u-tokyo.ac.jp/detail?code=0530085&year=2025,
(accessed April 2025).

Catalog),

(Lecture

140 Academy for Convergence of Materials and Informatics
(accessed

(TAC-MI), https://www.tac-mi.titech.ac.jp/en/,
April 2025).

141 TAC-MI Curriculum, https://www.tac-mi.titech.ac.jp/en/

curriculum/, (accessed April 2025).

142 Intersection of Materials, Machine Learning, and Robotics, in
Japanese, ed. T. Hitosugi, Tokyo Kagaku Dozin, Tokyo,
2024, ISBN: 978-4807913480.

143 D. Cheij,

IEEE Autotestcon Proceedings.

IEEE Systems
Readiness Technology Conference, 2001, DOI: 10.1109/
AUTEST.2001.948916.
Rapid
(accessed April 2025).

https://sila-standard.com/,

Integration,

144 SiLA

1402 | Digital Discovery, 2025, 4, 1384–1403

© 2025 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article OnlinePerspective

Digital Discovery

145 OPC 30500-1 Laboratory and Analytical Device Standard,
(accessed

https://opcfoundation.org/documents/30500-1/,
April 2025).

146 Y. Jiang, H. Fakhruldeen, G. Pizzuto, L. Longley, A. He,
T. Dai, R. Clowes, N. Rankin and A. I. Cooper, Digital
Discovery, 2023, 2, 1733–1744.

147 P. Quijano Velasco, K. Y. A. Low, C. J. Leong, W. T. Ng,
S. Qiu, S. Jhunjhunwala, B. Li, A. Qian, K. Hippalgaonkar
and J. J. W. Cheng, Digital Discovery, 2024, 3, 1011–1020.

148 S. Pai, K. Takahashi, S. Masuda, N. Fukaya, K. Yamane and
International Conference on
A. Ummadisingu,
Intelligent Robots and Systems (IROS), 2024, DOI: 10.1109/
IROS58592.2024.10801608.

IEEE/RSJ

149 Issues in the Development of Advanced Research Tools and
Equipment, https://www.jst.go.jp/crds/pdf/2024/RR/CRDS-
FY2024-RR-03.pdf, in Japanese (accessed April 2025).

150 T. Fujimoto, Evol. Inst. Econ. Rev., 2007, 4, 55–112.
151 R. Nuwer, Nature, 2023, 615, S92–S94.

© 2025 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2025, 4, 1384–1403 | 1403

Open Access Article. Published on 27 May 2025. Downloaded on 10/30/2025 12:46:49 PM.  This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.View Article Online
