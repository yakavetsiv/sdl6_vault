---
tags:
  - literature
  - type/paper
  - lit/sdl
  - lit/ai-methods
type: literature-note
status: converted
source_type: pdf
source_file: "macleod2020_thin_film_sdl.pdf"
source_path: "/Users/iyakavets/Documents/Github/LH_BO_Preprint/literature/pdfs/self_driving_labs/macleod2020_thin_film_sdl.pdf"
pdf: "_attachments/Self-Driving Labs/macleod2020_thin_film_sdl.pdf"
title: "Self-driving laboratory for accelerated discovery of thin-film materials"
year: "2020"
doi: "10.1126/sciadv.aaz8867"
citation_count_openalex: 43
topics:
  - Self-Driving Labs
  - Lab Automation
  - Autonomous Experimentation
---

# Self-driving laboratory for accelerated discovery of thin-film materials

**Key:** `macleod2020_thin_film_sdl`  
**Year:** 2020  
**DOI:** 10.1126/sciadv.aaz8867  
**OpenAlex citations:** 43  
**PDF:** [[_attachments/Self-Driving Labs/macleod2020_thin_film_sdl.pdf]]

## Why It Matters

This paper is part of the high-citation self-driving laboratory set imported from the LH_BO preprint literature review. Use it to support background claims about closed-loop experimentation, autonomous laboratory infrastructure, AI-guided experiment planning, or automated materials/chemical discovery.

## Connections

- [[Concept - Self-Driving Labs]]
- [[Concept - Lab Automation]]
- [[Concept - Optimization and Bayesian Search]]
- [[Map - Self-Driving Lab Stack]]

## Converted Text

Title: Self-driving laboratory for accelerated discovery of thin-film materials

One sentence summary:
optimize the doping and annealing of organic semiconductors.

 The first autonomous laboratory for the discovery of thin films is used to

 B. P. MacLeod
Authors:
1
1
​, L. P. E. Yunker
​, R. Moreira
Dettelbach
1
1
​, T. H. Haley
​, M. S. Elliott

H. Zhang

1,3†

​, F. G. L. Parlane

1,3

1,3†

​, T. D. Morrissey
1
1
​, J. R. Deeth
​, M. B. Rooney
3
1
 A. Aspuru-Guzik
D. J. Dvorak
​,
​,
1-3,8
​*
Berlinguette

4-7

4-7

​, F. Häse

​, L. M. Roch
​, K. E.
1
1
1
1
​, H. Situ
​, G. J. Ng
​, R.
​, V. Lai
1
4-10
​*, C. P.
​*, J. E. Hein

Affiliations:

1
​Department of Chemistry, The University of British Columbia, Vancouver, British Columbia, Canada
2
​Department of Chemical & Biological Engineering, The University of British Columbia, Vancouver,
British Columbia, Canada
3
​Stewart Blusson Quantum Matter Institute, The University of British Columbia, Vancouver, British
Columbia, Canada
4
​Department of Chemistry and Chemical Biology, Harvard University, Cambridge, Massachusetts, USA
5
​Department of Chemistry, University of Toronto, Toronto, Ontario, Canada
6
​Department of Computer Science, University of Toronto, Toronto, Ontario, Canada
7
​Vector Institute for Artificial Intelligence, MaRS Centre, Toronto, Ontario, Canada
8
​Canadian Institute for Advanced Research (CIFAR), MaRS Centre, Toronto, Ontario, Canada
9
​Kebotix, Inc., 501 Massachusetts Ave., Cambridge, Massachusetts, USA
10
​Zapata Computing, Inc., 100 Federal St, 20th Floor, Boston, Massachusetts, USA

†
​These authors contributed equally to this work

*Email:

cberling@chem.ubc.ca

,

alan@aspuru.com

,

jhein@chem.ubc.ca

Page

1 of 27
​

​

​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​

​
​
​
​
​

​

Abstract:

Discovering and optimizing commercially viable materials for clean energy

applications typically takes over a decade. Self-driving laboratories that iteratively design, execute, and

learn from material science experiments in a fully autonomous loop present an opportunity to accelerate

this research. We report here a modular robotic platform driven by a model-based optimization

algorithm capable of autonomously optimizing the optical and electronic properties of thin-film

materials by modifying the film composition and processing conditions. We demonstrate this platform

by using it to maximize the hole mobility of organic hole transport materials commonly used in

perovskite solar cells and consumer electronics. This demonstration highlights the possibilities of using

autonomous laboratories to discover organic and inorganic materials relevant to materials sciences and

clean energy technologies.

Main text:

Introduction

Optimizing the properties of thin films is time intensive because of the large number of compositional,

deposition, and processing parameters available

(

,
1
​

)
2
​

. These parameters are often correlated and can

have a profound effect on the structure and physical properties of the film and any adjacent layers

present in a device

(

)
3
​

. There exist few computational tools for predicting the properties of materials

with compositional and structural disorder, and thus the materials discovery process still relies heavily

on empirical data. High-throughput experimentation (HTE) is an established method for sampling a

large parameter space

(

,
4
​

)
5
​

, but it is nearly impossible to sample the full set of combinatorial

parameters available for thin films. Parallelized methodologies are also constrained by the experimental

techniques that can be used effectively in practice. The overwhelming size of the thin-film materials

Page

2 of 27
​

​

​
​
​
​
​
​
​
​
​
​
​
​

parameter space motivates the need for both data- and theory-guided algorithms for executing

experiments beyond what can be achieved with HTE alone

(

–
6
​

)
8
​

.

The experimental approach of iterating between automated experimentation and

machine-learning-based experiment planning has resulted in early successes in addressing

high-dimensional problems in experimental physics

(

, chemistry

(

)
9
​

)
10
​

, and life-sciences

(

. This

)
11
​

approach is only starting to be implemented in the materials sciences

(

, as demonstrated by the

)
1
​

optimization of carbon nanotube growth

(

, amorphous alloy compositions

(

)
12
​

, and inorganic

)
13
​

perovskite quantum dot nucleation

(

)
7
​

. We demonstrate here the optimization of thin films using our

platform named

, a flexible and modular self-driving laboratory capable of autonomously
“Ada”
​

synthesizing, processing, and characterizing organic thin films (Fig. 1; Fig. S1; Movie S1).

 trains
Ada
​

itself how to find target parameters without any prior knowledge, enabling iterative experimental

designs that maximize the information gain per sample (Fig. 2).

Page

3 of 27
​

​
​
​
​

​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​

Fig. 1. The

 self-driving laboratory.
Ada
​

 (

A)

The self-driving laboratory is based on a modular robotic platform which

interacts with objects using a rotatable pneumatic gripper on a polar robotic arm achieving 10 μm repeatability and ~1 m/s

maximum velocity. (

B)

Fluid handling is achieved using disposable pipette tips which can be press-fit onto and removed

from the arm’s pipette mount by the robot. Pipetting with a mean accuracy of 5 μL is achieved using a syringe pump

connected to the pipette mount. (

C)

Substrate handling is achieved using a vacuum substrate handler gripped by the robotic

arm. (

D)

 Configuration of the robotic platform for a specific experimental workflow is achieved by mounting an appropriate

collection of experimental modules on the robot; here the

platform is shown equipped for the synthesis and
Ada
​

characterization of thin film materials.

Page

4 of 27
​

​
​
​
​
​
​
​
​
​
​
​

​

Fig. 2.

 employs an autonomous optimization workflow.
Ada
​

 The autonomous workflow involves iterative

experimentation with the goal of discovering a thin-film composition with the highest possible “pseudomobility”. Each

iteration of the workflow involves: [1] mixing an HTM-dopant-additive ink, [2] spin coating the ink onto a substrate, [3]

thermally annealing for a variable amount of time, [4] imaging with a visible-light camera, [5] acquiring UV-Vis-NIR spectra

in reflection and transmission modes, [6] measuring the I-V curve of the film with a 4-point probe, [7] computing a

pseudomobility based on the IV and spectroscopic data, and [8] feeding this pseudomobility into the

ChemOS
​

)
14
(
​

orchestration software and the

Phoenics
​

 Bayesian optimization algorithm which then designs the next experiment.
)
15
(
​

Page

5 of 27
​

​
​
​

​
​
​

​
​
​

​

Results

As a first step in proving out the methodology, we designed

 to target organic hole and
Ada
​

electron transport layers that are ubiquitous in advanced solar cells

(

, as well as optoelectronics

)
16
​

applications such as organic lasers

(

 and light emitting diodes

(

)
17
​

)
18
​

. For this work, we configured

Ada

specifically to optimize the hole mobility of spiro-OMeTAD, an organic HTM common to perovskite

solar cells (PSCs)

(

)
19
​

. The hole mobility of spiro-OMeTAD is critical to PSC performance, but it is

highly sensitive to dopants, additives, spin-coating solvents, and post-deposition processing

(

–
19
​

)
26
​

.

How each of these factors affect the hole mobility of amorphous spiro-OMeTAD remains difficult to

model

(

,
3
​

)
27
​

, and thus optimizing the relevant properties of spiro-OMeTAD is still done empirically.

This optimization process often takes months to complete and slows the translation of new organic hole

and electron transport layers for solar cells and related devices.

 autonomously optimizes the hole mobility of spiro-OMeTAD by: (i) measuring and mixing
Ada
​

solutions of HTMs, dopants, and plasticizers; (ii) depositing solutions as thin films on rigid substrates;

(iii) annealing each film for a specified duration (iv) imaging each film to detect morphologies, defects,

and impurities; and (v) characterizing the optical and conductivity properties to produce surrogate hole

mobility data. This data is received by

ChemOS
​

(

,

)
14
​

which uses the
​

Phoenics
​

(

)
15
​

 global Bayesian

optimization algorithm to design new experiments by actively learning from previously acquired data.

 uses a sampling parameter to explicitly bias experimental design towards exploration or
Phoenics
​

exploitation in an alternating fashion, and has been shown to outperform random and systematic

searches

(

,
14
​

,
15
​

)
28
​

. The optimization experiments are performed by a multi-purpose robot (Fig. 1)

equipped with a rotatable pneumatic gripper and a pipette mount which enable the platform to

accomplish a wide variety of tasks by interacting with a number of different modules. The platform

Page

6 of 27
​

​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​

​

​
​
​
​

​

​
​
​
​
​
​
​
​
​

aspirates, dispenses, and mixes liquid precursors with the assistance of syringe pump and a weigh scale.

Precursor solutions are spin-cast as thin films on glass substrates, which can then be annealed up to 165

°C (Fig. S2) using a forced convection annealing system which enables control over the extent of

annealing by leveraging the ability of the robot to accurately and repeatably position the sample in a hot

air stream for a precisely controlled duration .

 then characterizes the films using purpose-built
Ada
​

systems for dark field photography, UV-Vis-NIR reflection and transmission spectroscopy, and 4-point

probe conductance. The robot also serves as a XYZ sample-positioning stage enabling all

characterizations to be performed at multiple positions on the sample, which we leverage to collect

spectroscopy and conductance data at 7 spatial positions on each sample. One sample is synthesized and

characterized approximately every 20 minutes, with consumables (pipettes, substrates, stock solutions)

requiring replenishment every 7 samples. The ability to produce high quality, well-organized datasets

(Figs. S3 and S4) while also enabling typically uncontrolled variables (e.g., time between process steps,

height of spin coating dispense nozzle) to become controlled or optimization parameters are very

powerful features of

. Moreover,
Ada
​

 is controlled using flexible, open-source Python software (see
Ada
​

Materials and Methods), which facilitates the rapid implementation of new experiments.

We selected HTM hole mobility as our target parameter for optimization, but this parameter

typically requires assembly of multilayer devices in order to get a valid measurement

(

,
27
​

,
29
​

)
30
​

.

Conventional methods are simply not compatible with the time scale needed for efficient autonomous

optimization

(

)
31
​

. We therefore developed a scheme where we could use 4-point-probe conductivity and

UV-Vis-NIR spectroscopy measurements to produce a diagnostic quantity, “pseudomobility”, that is

proportional to hole mobility (see Materials and Methods and Supplementary figure S5). Pseudomobility

is the quotient of the sheet conductance of a thin film and the absorptance of oxidized spiro-OMeTAD in

Page

7 of 27
​

​
​
​

​
​
​
​
​
​
​
​
​

the film. We estimated the absorptance of each thin film with an analytical model which incorporates

experimental reflection and transmission spectra, and which accounts for the effect of the glass substrate

on these spectra. The pseudomobility ratio, which provides a thickness-independent low latency

analytical surrogate for hole mobility, became our target optimization objective and enabled us to

accelerate the rate of meaningful data collection

The pseudomobilities of spiro-OMeTAD thin films were optimized by iteratively designing film

compositions with variable annealing times and dopant concentrations (tables S1, S2). Solutions

prepared from stock solutions of spiro-OMeTAD and a cobalt(III) dopant (along with a fixed amount of

the plasticizer 4-

-butylpyridine) were spin-coated onto substrates to yield thin films. Each film was
tert
​

annealed, imaged, and analyzed to determine a pseudomobility value that was relayed to

. Fig.
ChemOS
​

3A chronicles how the doping ratios and annealing times were varied during optimization for two

independent experimental campaigns. Each of the two 35-sample campaigns took under 30 h (including

time for restocking consumables) and each had one failed sample. This failure rate is typical for our

system. An important outcome is that both campaigns converged on the same global maximum for both

doping ratio (~0.4 eq.) and annealing time (~75 s) to deliver films with the same maximum

pseudomobilities. This reproducible endpoint is significant and demonstrates that

 can successfully
Ada
​

navigate a broad experimental space (see table S3 for additional reproducibility data).

Page

8 of 27
​

​
​
​

​

Fig. 3. Results of thin-film pseudomobility optimization carried out by the self-driving lab.

 (

A)

Experimental values for

cobalt doping ratio, annealing time, and maximum measured pseudomobility as a function of the number of experiments

performed for two independent optimization runs. (

B)

 The pseudomobility response surface and sampled points for the

second (blue, left) optimization run. The algorithm initially discovered a local maximum, and then discovered the global

maximum of the sampled parameter space.

Fig. 3b shows the locations and sequence of the experimentally sampled points in the parameter

space. The sampled points can be seen to initially cluster at a local maximum (~100% doping and

annealing time >200 s) prior to finding a higher performance region elsewhere in the parameter space.

While the eventual rejection of the local maximum confirms that the

 functionality of
explore-exploit
​

 can prevent the search from becoming stuck near local optima, we were curious why
Phoenics
​

Ada

identified a local maximum at high doping levels. Subsequent investigations of the dark field images of

these films revealed annealing-induced dewetting of the films containing intermediate amounts of

dopant (Fig. S6). At elevated doping levels, dewetting was suppressed, allowing a region of improved

thermal stability to be identified (see Supplementary Information). The favourable performance of high

dopant/high annealing time films was not intuitive

(

, and this observation was facilitated by our

)
32
​

Page

9 of 27
​

​
​
​
​
​

​
​
​
​
​
​

autonomous platform, which searched over a larger range of doping and annealing conditions than is

typically explored in studies of organic HTMs. We hypothesize that the highly doped films are stable at

high annealing temperatures because of the greater intrinsic thermal stability of the dopant (which does

not readily form a glass and melts at 189 °C, see Fig. S7) compared to amorphous spiro-OMeTAD

(which exhibits a glass transition at 124 °C, see

(

)
33
​

). On this basis, when sufficient Co(III) salt is added

to the HTM film, the increase in the stability of the doped HTM due to the intrinsic stability of the

dopant overcomes the decrease in thermal stability generally associated with the addition of dopants to

hole transport materials

(

,
32
​

,
34
​

)
35
​

. This result is non-trivial and represents an unexpected scientific

observation from an artificially intelligent experimental design.

Discussion

We report here the first use of a self-driving laboratory to optimize composition and processing

parameters for thin-film materials. This proof-of-principle study targeted the optimization of a type of

thin organic semiconducting film common to advanced solar cells, but the modularity of our robotic

platform and control software enables the rapid incorporation of new experiments, techniques, analytical

hardware, and algorithms. The

 platform can therefore be easily tailored for a range of inorganic and
Ada
​

organic materials and applications, and even be coupled to automated organic synthesis methodologies

developed for the pharmaceutical industry

(

,
36
​

)
37
​

. The next stage of development for this robotic

platform is to introduce sequential film deposition to extend autonomous optimization experiments to

multi-layered systems that comprise full devices. As the robotic workflow complexity increases, the

experimental throughput of our current, fully-serial scheme will decrease; to overcome this challenge,

we plan to develop stand-alone synthesis and characterization modules which can run in parallel. Our

ability to iteratively modify Ada will prove to be particularly useful in this regard. Indeed, we expect

platforms such as

 to facilitate the deployment of effective autonomous experimentation at a scale
Ada
​

Page

10 of 27
​

​
​
​
​
​
​
​
​
​
​
​
​
​
​
​

compatible with the rapidly evolving needs and constraints (e.g., budget, time, space) of a broad

cross-section of the materials science research community.

Materials and Methods

Materials

Acetonitrile (CAS 75-05-8, HPLC grade, ≥ 99.9%), toluene (CAS 108-88-3, ACS grade),

acetone (CAS 67-64-1, ACS grade), spiro-OMeTAD (CAS 207739-72-8, HPLC grade, 99%), FK 102

Co(III) TFSI salt (Sigma Aldrich product number 805203, 98%), and 4-tert-butylpyridine (CAS

3978-81-2, 96%) were purchased from Sigma Aldrich and were used without further purification.

Extran

®
​ 300 detergent (EX0996-1) and 2-propanol (ACS grade, ≥99.5%) were purchased from EMD

Millipore Corporation and were used without further purification. Microscope slide substrates (75 × 25

× 1 mm, VWR Cat. No. 16004-430) were purchased from VWR International.

Consumables for the robotic platform

During the optimization experiments, the robotic platform was periodically restocked with

consumables. These include 3” × 1” × 1 mm microscope slides (VWR VistaVision), 2mL HPLC vials

(Canadian Life Science) , 200μL pipettes (Biotix M-0200-BC) and various stock solutions. Cleaning of

the microscope slides and preparation of the stock solutions are further detailed below.

Manual preparation of stock solutions

All reagent solutions were prepared in an atmosphere dried over anhydrous calcium sulfate

®
​), resulting in ~0.005 mg/L of water remaining in the atmosphere. Toluene and acetonitrile
(DRIERITE

solvents were prepared by drying over anhydrous magnesium sulfate, filtering through a 0.2 μm PTFE

Page

11 of 27
​

​
​
​

filter, and stored over 3 Å molecular seives. A solution of 1:1 v/v solution of acetonitrile/toluene

(MeCN/MePh) was prepared by mixing equal volumes of dry acetonitrile and toluene. A stock solution

of spiro-OMeTAD was prepared by briefly (1-5 min) sonicating a mixture of spiro-OMeTAD (off-white

powder) with MeCN/MePh. The resulting solution had a transparent, pale yellow color. A stock solution

of FK 102 Co(III) TFSI salt was prepared by dissolving FK102 Co(III) TFSI salt (bright orange

crystalline powder) in MeCN/MePh and stored without exposure to UV-light. The resulting solution had

a transparent bright orange color. A stock solution of 4-tert-butylpyridine was prepared by dissolving

tert-butylpyridine (clear, colorless solution) in MeCN/MePh. All stock solutions were prepared at

concentrations of 50 mg solute per 1 mL solvent.

Manual cleaning of substrates

75 × 25 × 1 mm microscope slide substrates were cleaned through multi-step sonication. First,

the slides were sonicated for 10 min in a 5% v/v solution of Extran

®
​ in deionized water. The sides were

then sonicated sequentially in deionized water, acetone, and 2-propanol for 10 minutes each step. The

slides were stored in 2-propanol and dried with filtered air before use.

Robotic methods

The robot used is a Selective Compliance Assembly Robot Arm (SCARA)-type robot (N9, North

Robotics; www.northrobotics.com) which performs the robotic manipulations in our workflows. This

robot is driven by a controller (C9, North Robotics), which also provides auxiliary controls for

third-party instruments and components used by the robot. The controller and additional peripherals are

controlled by a computer running a Python script based on open-source libraries (see

https://gitlab.com/ada-chem

).

Page

12 of 27
​

​
​
​

Autonomous workflow step 1: Robotic preparation of spin-coating inks

The precursor solution for each sample was prepared by mixing varying amounts of:

spiro-OMeTAD stock solution; FK 102 Co(III) TFSI salt stock solution; and 4-tert-butylpyridine stock

solution in ambient conditions. In each precursor solution the FK 102 Co(III) TFSI:spiro-OMeTAD ratio

(n/n) was between 0 to 1, with the ratio determined by the ChemOS orchestration software. The ratio

(m/m) of tert-butylpyridine to the total amount of spiro-OMeTAD and FK102 Co(III) TFSI was fixed at

0.2. The resulting precursor solutions became dark purple in appearance upon the combination of the

spiro-OMeTAD and FK 102 Co(III) TFSI solutions. The precursor solutions were mixed through

aspiration and were used within a minute of preparation.

Autonomous workflow step 2: Robotic spin coating of thin-film samples

The thin-film samples were prepared via spin-coating with a custom-built spin-coater provided

by North Robotics. The microscope slides were spun at 1000 rpm and 0.100 mL of the precursor

solution was dispensed at a normal incidence at the center of the slide. Rotation continued for 60 s.

Autonomous workflow step 3: Robotic thermal processing of thin-film samples

The forced convection annealing furnace was constructed from a MHT Products Inc. model 750

heat gun facing upward into a vertically oriented 75 × 50 mm rectangular aluminum tube kept under

ambient conditions. A 40 × 5 mm sample port was cut 40 mm from the heat gun. Freshly spin coated

thin-film samples were moved by the N9 slide gripper into the furnace via the sample port, after which

the heat gun power was triggered for the amount of time requested by the orchestration software. The

temperature profile of the annealing procedure is shown in Supplementary Fig 2. The temperature of the

slide ramps from ambient temperature to 165 °C over the first 100 s and remains at that temperature for

Page

13 of 27
​

​

the rest of the annealing time. After the requested heating time has elapsed, the arm immediately

removed the sample from the furnace and held 25 mm above a 4500 rpm cooling fan for 3 min. This

cooling period allowed samples to return to ambient temperature, regardless of annealing time, before

further characterization.

Autonomous workflow step 4: Robotic dark field photography

Thin-film samples were imaged at a dark field photography station composed of a FLIR Blackfly

S Mono 12 MP USB Vision (Sony IMX226) camera mounted above an AmScope MIC-209 3 W ring

light. The sample was moved by the robotic arm to 90 mm below the camera and illuminated by the ring

light to provide contrast between smooth and rough regions of the film. Images were captured at three

different overlapping locations at a resolution of 4000 × 3000 px. Manual post-experiment analysis of

collected images was used to identify dust, defects, and dewetting in thin-film samples.

Autonomous workflow step 5: Robotic UV-Vis-NIR spectroscopy

Spectrometer design

UV-Vis-NIR transmission and reflection spectra were collected with a custom-built, fiber-optic

spectroscopy station. A BLACK-Comet UV-Vis Spectrometer (190 - 900 nm, < 1 nm resolving

resolution), a DWARF-Star Miniature NIR Spectrometer (900 - 1700 nm, 2.5 nm resolving resolution),

and two SL4 High Power Tungsten Halogen and Deuterium Lamps (190 - 2500 nm spectral range, 3000

K) were purchased from StellarNet, Inc. The visible portion of the lamps were operated on the third

color temperature setting. A 3-way split fiber optic reflection probe was positioned above and normal to

the surface of the sample, which was connected to the BLACK-Comet spectrometer, the DWARF-Star

spectrometer, and an SL4 lamp (reflection lamp). A collimating lens was positioned below and normal

to the surface of the sample, and was connected to the second SL4 lamp (transmission lamp) via a

Page

14 of 27
​

​

second fiber-optic cable. A mechanical shutter was placed between the collimating lens and the sample,

which was darkened with black flocked paper (Thorlabs part number BFP1). The BLACK-Comet

UV-Vis and DWARF-STAR Miniature NIR spectrometers were controlled by a Raspberry Pi 3 Model

B+ (2017) running Raspbian Stretch (Kernel 4.14) and Python 2.7.0. The SL4 lamps were controlled by

an Arduino Due (A000062), which was slaved to the Raspberry Pi.

To perform a transmission measurement the mechanical shutter was opened, the upper reflection

lamp internal shutter was closed, and the lower transmission lamp internal shutter was opened. To

perform a reflection measurement the mechanical shutter was closed, the lower transmission lamp

internal shutter was closed, and the upper reflection lamp internal shutter was opened.

Spectrometer calibration

A 75 × 25 × 1 mm glass slide coated with 50 nm aluminum was purchased from Deposition

Research Lab Inc. for use as a reflectance baseline. The true specular reflectance of the prepared

reference sample was measured with an Agilent Cary 7000 Universal Measurement Spectrometer

(UMS) using the Cary Universal Measurement Accessory (UMA) to hold the sample at 10° from

normal. The sensitivity of the BLACK-Comet and DWARF-Star spectrometers were set by increasing

the integration time (in ms) of the detectors until the signal was between 80% and 95% of saturation,

where saturation was 2

16

​ counts. For transmission measurements, the sensitivity was determined with no

sample present, and for reflection measurements, the sensitivity was determined with the calibrated

aluminum mirror. The bright and dark baselines for transmission were completed with no sample

present and with the transmission lamp on and off, respectively. The bright and dark baselines for

reflection were completed with the calibrated aluminum mirror present and with the reflection lamp on

Page

15 of 27
​

​
​

and off, respectively. The known true reflection of the aluminum mirror, obtained from the Cary 7000,

was used to define the bright reflection baseline.

Robotic spectroscopy measurement

For each film fabricated by the robotic platform, UV-Vis-NIR spectra were collected by the

robot, which holds samples in the optical path of the spectrometer using the vacuum substrate handler.

First the reflection and transmission spectra of a blank glass substrate were collected, followed by

analogous reflection and transmission spectra of the annealed thin film on an identical substrate. The

spectra of the uncoated and coated substrate were used to compute an approximation to the absorbance

of the thin film, as described in the UV-Vis-NIR data processing section. The spectra of each thin film

and the spectra of the blank substrate were measured at seven positions spaced ~1 mm apart near the

center of the substrate.

UV-Vis-NIR data processing

Reflection and transmission spectra were measured at normal incidence and were assumed to be

entirely specular and incoherent. This assumption is reasonable as long as surfaces and interfaces scatter

a minimal amount of light, and interference fringes in the spectra are minimal. At any

wavelength/energy, the raw reflection (R

) of the blank substrate can thus be
) and transmission (T
​0
​0

related to the reflectivity/transmissivity (R

) of the glass-air interface, and to the single-pass
/T
​g
​g

transmission of the glass substrate (X

) using the following equations:
​g

R0 =   g +   R X T
R

g
g
1 − R Xg

2

g

g

2

2

2

 T 0 =   X Tg

g
2
1 − R Xg

2

2

g

1 =   g +   g
R

T

Page

16 of 27
​

​
​
​
​
​

​

These equations can be solved for R

, and X
, T
​g
​g

.
​g

Since a thin film on a glass substrate is a multilayer system, additional assumptions are needed to

process the film/glass spectra analytically. In this work, the refractive indices of the film and substrate

were both expected to be ~1.5, and thus the reflection at the film-glass interface could be ignored

without significant distortion of the result. This simplification allowed for the raw reflection (R

) and
​1

) of the film/substrate to be incorporated into a similar set of equations as above while
transmission (T
​1

introducing only three new parameters:

R1 =

f +
R

2

g

2

2
R X X T
g
2

f
1 − R R X X
g f

g

f

2

f

 T 1 =

g

g

X X T T
f
f
2
1 − R R X X
g f

g

2

f

1 =

R

f +

T

f

In this second set of equations, R

 are the reflectivity and transmissivity of the film-air
 and T
​f
​f

interface, respectively, and X

 is the single-pass transmission of the thin film. Solving these equations
​f

for X

 gives the corrected transmission of the thin film. The corresponding absorption of the film is:
​f

Absf ilm =   − l

og(X )
f

This quantity can be calculated at each measured wavelength/energy to give the corrected

absorption spectrum of the film at each of the seven measured positions.

Autonomous workflow step 6: 4-point probe conductance instrumentation and characterization

4-point probe conductivity measurements were performed with a Keithley Series K2636B

System SourceMeter

®
​ Instrument with a Signatone Four Point Probe Head (part number

Page

17 of 27
​

​
​
​
​
​

​
​
​
​

​
​

SP4-40045TBN, 0.040” tip spacing, 45 gram pressure, tungsten carbide tips with 0.010” radii)

connected through a Signatone Triax to BNC feedthrough panel (part number TXBA-M160-M).

The current on the outer probes was stepped from 0 to 4 nA in 0.8 nA steps. The system was

stabilized at each step for 0.5 s, and the potential across the inner probes was integrated for 25 power

line cycles (at 60 Hz). The slope of the potential as a function of the current sourced afforded the

resistance. No correction factors were applied to the resistance measurement, as the size of the slide is

significantly larger than the spacing between the probes. The conductance of each film was measured at

seven positions spaced ~1 mm apart near the center of the substrate. These positions matched those used

in spectroscopy measurements.

Autonomous workflow step 7: pseudomobility calculation

Conventional theory describes the conductivity (σ) of p-type semiconductors as the product of

the elementary charge (e), the density of positive charge carriers (ρ

), and the mobility of these same
​h

charge carriers (μ). In numerous examples, ρ

 is treated as an independent variable programmed by
​h

doping fraction, while μ is an intrinsic material property found to vary with temperature, applied

voltage, disorder, and doping fraction (24, 25). μ thus encompasses most of the complexity of σ and is

often maximized in order to optimize the performance of electronic materials. In the specific case of a

hole transport material (HTM), the doping fraction must be managed carefully given that under-doping

reduces hole conductivity, while over-doping risks depletion of valence electrons at the HTM/absorber

interface that can lead to inefficient hole injection.

Page

18 of 27
​

​
​

​

In this work, the value of μ for each HTM film was extracted from sheet resistance 4-point probe

and UV-Vis measurements using the following methodology.

The hole mobility of the HTM is expressed as:

μh =   σ
ρ eh

where the hole conductivity of the HTM is assumed to approximate the total conductivity due to the

heavy p-doping of most measured conditions and the high intrinsic mobility of holes relative to that of

electrons known to exist in spiro-OMeTAD. σ is defined as:

σ = (R

S · t −1 =  ( dI

(

)

dV · C · π · t

)/ln

(2))−1

where R

 is the sheet resistance, t is the film thickness, dV/dI is the linear change in voltage (V) with
​S

respect to current (I) at low V and I extracted from the 4-point probe measurement, and C is a geometric

correction factor tied to the ratio between the probe tip distances and the rectangular dimensions of the

film. The redefinition of R

 here is valid for any 4-point probe measurement in which t is significantly
​S

less than the distance between adjacent probe tips. ρ

 is defined as:-
​h

+]
HT M[
ρh =   HT M · HT M[
]

ρ

where ρ

 is the total density of redox active HTM sites in the film and [HTM

​HTM

+
​]/[HTM] is the fraction

of active sites carrying a positive charge at any given time. This fraction is not necessarily equal to the

ratio of dopant to HTM in the film, since not all dopants oxidize HTM material quantitatively. ρ

 can

​HTM

be converted to a molar concentration by:

ρHT M =

1000

· N A · [

HT M ]

Page

19 of 27
​

​
​
​

​
​
​

​

where N

 is the Avogadro constant and 1000 N
​A

 is the unit of conversion between m
​A

-3
​ and M. The ratio

of [HTM

+
​] to [HTM] is the same as the ratio of ρ

 to ρ
​h

. This yields:

​HTM

ρh =

1000

· N A · HT M[

+]

which can be used in conjunction with Beer’s law to incorporate data from the UV-Vis spectrum of the

film in question. The resulting equation:

ρh =

1000

· N A ·

Abs

HT M + = 1
ε·t

000

· N A ·

Absf ilm

ε·t

includes the molar extinction coefficient of the film (ε), the film thickness (t), and the reflection- and

substrate-corrected absorbance (Abs

) of the film in the wavelength range of 500±5 nm, where all

​HTM+

absorption can be attributed to HTM

+
​. This final expression for ρ

 is only valid when the programmed
​h

dopant:HTM ratio is at or below 1:1 so that minimal HTM

2+

​ exists in the film. Finally, μ

 can be defined
​h

in terms of both experimental results:

μh =   σ
ρ eh

=  (

ln(2)·ε

1000·π·e·C·N A) ( dI

(
dV ) Abs

HT M +)−1

This expression is crucially independent of film thickness, allowing for accurate optimization

over the full compositional and processing variable space employed in this work. Dividing out the

constants in the final equation above yields a parameter termed pseudomobility:

p

seudomobility

=   ( dI

(
dV ) Abs

HT M +)−1

Pseudomobility is equivalent to the quotient of film conductivity and p-type carrier density and

provides a useful measure of relative mobility that can be utilized in optimization experiments. The

pseudomobility of each thin film was calculated independently at each of the seven characterized

Page

20 of 27
​

​
​
​
​
​
​

​
​
​
​
​

​

positions. The pseudomobility value passed to the optimization algorithm was the mean value of the

seven positional pseudomobilities.

Autonomous workflow step 8: determining the next experiment with Bayesian optimization

After each thin film experiment, the realized experimental parameters and resulting

pseudomobility value were sent to an instance of

ChemOS
​

(

)
14
​

 running on a remote server via a file

transfer interface (Dropbox).

 then provided the experimental data to the
ChemOS
​

Phoenics
​

(

)
15
​

 global

Bayesian optimization algorithm, initiating an update of the algorithm’s surrogate model of the

experimental response surface. To minimize the robot’s down-time between the completion of one

experiment and the initiation of the next experiment,

immediately provides parameters for the
ChemOS
​

next experiment which have been pre-computed by

In this way, the moderately
Phoenics.
​

computationally intensive updating of

’s surrogate model can occur in parallel with the robotic
Phoenic
​

execution of the next experiment, shortening the execution of a campaign with 30 experiments by

approximately 30 minutes.

 suggests new experiments by using an adjustable sampling
Phoenics
​

parameter to explicitly bias experimental design towards exploration or exploitation in an alternating

fashion and thus enables global optimization over the response surfaces explored by the robotic

platform. The initial sample is chosen at random as no model of the response surface is initially

available. The exchange of information between

and the robotic platform is managed by
ChemOS
​

Python software written in-house.

References and notes

1.  A. Aspuru-Guzik, K. Persson, A. Alexander-Katz, C. Amador, D. Solis-Ibarra, M. Antes, A.
Mosby, M. Aykol, E. Chan, S. Dwaraknath, J. Montoya, E. Rotenberg, J. Gregoire, J.
Hattrick-Simpers, D. M. Huang, J. Hein, G. Hutchison, O. Isayev, Y. Jung, J. Kiviaho, C.
Kreisbeck, L. Roch, S. Saikin, D. Tabor, J. Lambert, S. Odom, J. Pijpers, M. Ross, J. Schrier, R.
Segal, M. Sfeir, H. Tribukait, T. Vegge, “Materials Acceleration Platform: Accelerating Advanced

Page

21 of 27
​

​

​
​
​
​
​

​
​
​
​
​
​
​
​

​

Energy Materials Discovery by Integrating High-Throughput Methods and Artificial Intelligence”
(Mission Innovation Clean Energy Materials Innovation Challenge, 2018), (available at
http://nrs.harvard.edu/urn-3:HUL.InstRepos:35164974

).

2.

J.-P. Correa-Baena, K. Hippalgaonkar, J. van Duren, S. Jaffer, V. R. Chandrasekhar, V. Stevanovic,
C. Wadia, S. Guha, T. Buonassisi, Accelerating materials development via automation, machine
learning, and high-performance computing.

, 1410–1420 (2018).

2

.
Joule
​

3.  B. Cao, L. A. Adutwum, A. O. Oliynyk, E. J. Luber, B. C. Olsen, A. Mar, J. M. Buriak, How to
optimize materials and devices via design of experiments and machine learning: demonstration
using organic photovoltaics.

, 7434–7444 (2018).

12

.
ACS Nano
​

4.  X. D. Xiang, X. Sun, G. Briceño, Y. Lou, K. A. Wang, H. Chang, W. G. Wallace-Freedman, S. W.

Chen, P. G. Schultz, A combinatorial approach to materials discovery.
(1995).

.
Science
​

268

, 1738–1740

5.  H. S. Stein, D. Guevarra, P. F. Newhouse, E. Soedarmadji, J. M. Gregoire, Machine learning of
optical properties of materials - predicting spectra from images and images from spectra.
Chem.
Sci.
​

, 47–55 (2019).

10

6.  F. Häse, L. M. Roch, A. Aspuru-Guzik, Next-generation experimentation with self-driving

laboratories.

.
Trends in Chemistry
​

1

 (2019), pp. 282–291.

7.

J. Li, Y. Lu, Y. Xu, C. Liu, Y. Tu, S. Ye, H. Liu, Y. Xie, H. Qian, X. Zhu, AIR-Chem: authentic
intelligent robotics for chemistry.

, 9142–9148 (2018).

122

.
J. Phys. Chem. A
​

8.  Y. Bai, L. Wilbraham, B. J. Slater, M. A. Zwijnenburg, R. S. Sprick, A. I. Cooper, Accelerated
discovery of organic polymer photocatalysts for hydrogen evolution from water through the
J. Am. Chem. Soc.
integration of experiment and theory.
​

, 9063–9071 (2019).

141

9.  V. Gopalaswamy, R. Betti, J. P. Knauer, N. Luciani, D. Patel, K. M. Woo, A. Bose, I. V.

Igumenshchev, E. M. Campbell, K. S. Anderson, K. A. Bauer, M. J. Bonino, D. Cao, A. R.
Christopherson, G. W. Collins, T. J. B. Collins, J. R. Davies, J. A. Delettrez, D. H. Edgell, R.
Epstein, C. J. Forrest, D. H. Froula, V. Y. Glebov, V. N. Goncharov, D. R. Harding, S. X. Hu, D.
W. Jacobs-Perkins, R. T. Janezic, J. H. Kelly, O. M. Mannion, A. Maximov, F. J. Marshall, D. T.
Michel, S. Miller, S. F. B. Morse, J. Palastro, J. Peebles, P. B. Radha, S. P. Regan, S. Sampat, T. C.
Sangster, A. B. Sefkow, W. Seka, R. C. Shah, W. T. Shmyada, A. Shvydky, C. Stoeckl, A. A.
Solodov, W. Theobald, J. D. Zuegel, M. G. Johnson, R. D. Petrasso, C. K. Li, J. A. Frenje, Tripled
yield in direct-drive laser fusion through statistical modelling.

, 581–586 (2019).

565

.
Nature
​

10.  A. Milo, E. N. Bess, M. S. Sigman, Interrogating selectivity in catalysis using molecular vibrations.

.
Nature
​

507

, 210–214 (2014).

11.  R. D. King, K. E. Whelan, F. M. Jones, P. G. K. Reiser, C. H. Bryant, S. H. Muggleton, D. B. Kell,

S. G. Oliver, Functional genomic hypothesis generation and experimentation by a robot scientist.
.
Nature
​

, 247–252 (2004).

427

12.  P. Nikolaev, D. Hooper, N. Perea-López, M. Terrones, B. Maruyama, Discovery of wall-selective

carbon nanotube growth conditions via automated experimentation.

.
ACS Nano
​

8

, 10214–10222

Page

22 of 27
​

​
​
​
​
​
​
​
​
​
​
​

​
​
​
​
​
​
​
​
​

​
​
​
​
​
​
​
​
​
​
​
​
​

(2014).

13.  F. Ren, L. Ward, T. Williams, K. J. Laws, C. Wolverton, J. Hattrick-Simpers, A. Mehta,
Accelerated discovery of metallic glasses through iteration of machine learning and
high-throughput experiments.

, 1566 (2018).

4

.
Sci Adv
​

14.  L. M. Roch, F. Häse, C. Kreisbeck, T. Tamayo-Mendoza, L. P. E. Yunker, J. E. Hein, A.
3
.
Science Robotics
​

Aspuru-Guzik, ChemOS: Orchestrating autonomous experimentation.
eaat5559 (2018).

,

15.  F. Häse, L. M. Roch, C. Kreisbeck, A. Aspuru-Guzik, Phoenics: a bayesian optimizer for

chemistry.

.
ACS Cent Sci
​

4

, 1134–1145 (2018).

16.  L. Meng, Y. Zhang, X. Wan, C. Li, X. Zhang, Y. Wang, X. Ke, Z. Xiao, L. Ding, R. Xia, H.-L.

Yip, Y. Cao, Y. Chen, Organic and solution-processed tandem solar cells with 17.3% efficiency.
.
Science
​

, 1094–1098 (2018).

361

17.  A. S. D. Sandanayaka, T. Matsushima, F. Bencheikh, S. Terakawa, W. J. Potscavage Jr, C. Qin, T.
Fujihara, K. Goushi, J.-C. Ribierre, C. Adachi, Indication of current-injection lasing from an
12
organic semiconductor.

, 061010 (2019).

.
Appl. Phys. Express
​

18.  S. Jhulki, J. N. Moorthy, Small molecular hole-transporting materials (HTMs) in organic
,
6

light-emitting diodes (OLEDs): structural diversity and classification.
8280–8325 (2018).

J. Mater. Chem.
​

19.  X. Yang, H. Wang, B. Cai, Z. Yu, L. Sun, Progress in hole-transporting materials for perovskite

solar cells.

J. Mater. Chem. A Mater. Energy Sustain.
​

27

, 650–672 (2018).

20.  J. Burschka, F. Kessler, M. K. Nazeeruddin, M. Grätzel, Co(III) complexes as p-dopants in

solid-state dye-sensitized solar cells.

.
Chemistry of Materials
​

25

 (2013), pp. 2986–2990.

21.  S. Wang, M. Sina, P. Parikh, T. Uekert, B. Shahbazian, A. Devaraj, Y. S. Meng, Role of

4-tert-butylpyridine as a hole transport layer morphological controller in perovskite solar cells.
Nano Lett.
​

, 5594–5600 (2016).

16

22.  T. Bu, L. Wu, X. Liu, X. Yang, P. Zhou, X. Yu, T. Qin, J. Shi, S. Wang, S. Li, Z. Ku, Y. Peng, F.
Huang, Q. Meng, Y.-B. Cheng, J. Zhong, Synergic interface optimization with green solvent
engineering in mixed perovskite solar cells.

, 1700576 (2017).

7

Adv. Energy Mater.
​

23.  Y. Fang, X. Wang, Q. Wang, J. Huang, T. Wu, Impact of annealing on spiro-OMeTAD and

corresponding solid-state dye sensitized solar cells.

.
Phys. Status Solidi
​

211

, 2809–2816 (2014).

24.  C. Liu, K. Huang, W.-T. Park, M. Li, T. Yang, X. Liu, L. Liang, T. Minari, Y.-Y. Noh, A unified
understanding of charge transport in organic semiconductors: the importance of attenuated
4
delocalization for the carriers.

, 608–618 (2017).

Mater. Horiz.
​

25.  Y. Shen, K. Diest, M. H. Wong, B. R. Hsieh, D. H. Dunlap, G. G. Malliaras, Charge transport in
.
Phys. Rev. B Condens. Matter
​

doped organic semiconductors.

, 081204 (2003).

68

Page

23 of 27
​

​
​
​
​
​
​
​
​
​
​
​
​
​
​
​

​
​
​

​
​
​
​
​

​
​
​

​
​
​
​
​
​

​
​
​
​
​
​

26.  Z. H. Bakr, Q. Wali, A. Fakharuddin, L. Schmidt-Mende, T. M. Brown, R. Jose, Advances in hole

transport materials engineering for stable and efficient perovskite solar cells.
271–305 (2017).

.
Nano Energy
​

34

,

27.  P. Friederich, V. Meded, A. Poschlad, T. Neumann, V. Rodin, V. Stehr, F. Symalla, D. Danilov, G.
Lüdemann, R. F. Fink, I. Kondov, F. von Wrochem, W. Wenzel, Molecular origin of the charge
carrier mobility in small molecule organic semiconductors.
(2016).

Adv. Funct. Mater.
​

, 5757–5763

26

28.  F. Häse, L. M. Roch, A. Aspuru-Guzik, Chimera: enabling hierarchy based multi-objective

optimization for self-driving laboratories.

Chem. Sci.
​

9

, 7642–7655 (2018).

29.  J. C. Blakesley, F. A. Castro, W. Kylberg, G. F. A. Dibb, C. Arantes, R. Valaski, M. Cremona, J. S.

Kim, J.-S. Kim, Towards reliable charge-mobility benchmark measurements for organic
, 1263–1272 (2014).
semiconductors.

15

Org. Electron.
​

30.  B. Xu, H. Tian, L. Lin, D. Qian, H. Chen, J. Zhang, N. Vlachopoulos, G. Boschloo, Y. Luo, F.

Zhang, A. Hagfeldt, L. Sun, Integrated Design of Organic Hole Transport Materials for Efficient
Adv. Energy Mater.
Solid-State Dye-Sensitized Solar Cells.
​

, 1401185 (2015).

5

31.  R. E. Brandt, R. C. Kurchin, V. Steinmann, D. Kitchaev, C. Roat, S. Levcenco, G. Ceder, T. Unold,

T. Buonassisi, Rapid photovoltaic device characterization through bayesian parameter estimation.
.
Joule
​

, 843–856 (2017).

1

32.  T. H. Schloemer, J. A. Christians, J. M. Luther, A. Sellinger, Doping strategies for small molecule
organic hole-transport materials: impacts on perovskite solar cell performance and stability.
Chem.
Sci.
​

, 1904–1935 (2019).

10

33.  T. Malinauskas, D. Tomkute-Luksiene, R. Sens, M. Daskeviciene, R. Send, H. Wonneberger, V.
Jankauskas, I. Bruder, V. Getautis, Enhancing Thermal Stability and Lifetime of Solid-State
Dye-Sensitized Solar Cells via Molecular Engineering of the Hole-Transporting Material
Spiro-OMeTAD.

, 11107–11116 (2015).

7

.
ACS Appl. Mater. Interfaces
​

34.  J.-Y. Seo, H.-S. Kim, S. Akin, M. Stojanovic, E. Simon, M. Fleischer, A. Hagfeldt, S. M.

Zakeeruddin, M. Grätzel, Novel p-dopant toward highly efficient and stable perovskite solar cells.
Energy Environ. Sci.
​

, 2985–2992 (2018).

11

35.  Q. Wang, Influence of a cobalt additive in spiro-OMeTAD on charge recombination and carrier
Phys. Chem. Chem.

density in perovskite solar cells investigated using impedance spectroscopy.
Phys.
​

, 10114–10120 (2018).

20

36.  A.-C. Bédard, A. Adamo, K. C. Aroh, M. G. Russell, A. A. Bedermann, J. Torosian, B. Yue, K. F.
Jensen, T. F. Jamison, Reconfigurable system for automated optimization of diverse chemical
reactions.

, 1220–1225 (2018).

361

.
Science
​

37.  P. J. Kitson, G. Marie, J.-P. Francoia, S. S. Zalesskiy, R. C. Sigerson, J. S. Mathieson, L. Cronin,
Digitization of multistep organic synthesis in reactionware for on-demand pharmaceuticals.
.
Science
​

, 314–319 (2018).

359

Page

24 of 27
​

​
​
​
​

​
​
​

​
​
​

​
​
​

​
​
​
​
​

​
​
​
​
​

​
​
​

​
​
​
​
​
​
​
​

Acknowledgments:

The authors would like to acknowledge Maddie Eghtesad for her contributions to

the project hardware and experimentation and to Tara Zepel for her contributions in literature research.

We thank the UBC Chemistry machine shop for assistance with instrument fabrication. We would like

to acknowledge CMC Microsystems for the provision of products and services that facilitated this

research, including SolidWorks 2018 SP5.0. For robot control and data processing, we would like to

acknowledge the contributors to the Python programming language (Python Software Foundation,

https://www.python.org).

Funding:

 The authors thank Natural Resources Canada (EIP2-MAT-001) for their financial support. C.

P. B. is grateful to the Canadian Natural Sciences and Engineering Research Council (RGPIN

337345-13), Canadian Foundation for Innovation (229288), Canadian Institute for Advanced Research

(BSE-BERL-162173), and Canada Research Chairs for financial support. B. P. M, F. G. L. P., T. D. M.,

and C. P. B. acknowledge support from the SBQMI’s Quantum Electronic Science and Technology

Initiative, the Canada First Research Excellence Fund, and the Quantum Materials and Future

Technologies Program. J. E. H. is supported by the Canadian Natural Sciences and Engineering

Research Council (RGPIN 2016-04613) and Canada Foundation for Innovation (35833). V. L. and H. S.

were supported by an NSERC Strategic Partnership Grant (STPGP 493833-16). F. H. acknowledges

support from the Herchel Smith Graduate Fellowship and the Jacques-Emile Dubois Student

Dissertation Fellowship. L. M. R. and A. A.-G. were supported by the Tata Sons Limited Alliance

Agreement (A32391) and the Office of Naval Research (N00014-19-1-2134), and would also like to

thank Dr. Anders Frøseth for generous support.

Page

25 of 27
​

​
​

​

Author contributions:

A.A-G., J. E. H., and C. P. B. conceived of and supervised the project. B. P. M.,
​

M. R., H. S., G. J. N., R. H. Z., and F. G. L. P. developed the robotic hardware. F. G. L. P., T. D. M., J.

R. D., T. H. H. and B. P. M. developed the data analysis software. L. P. E. Y., B. P. M., F. G. L. P., G. J.

N., R. H. Z., V. L., M. S. E., K. E. D. and H. S. developed the robotic control software. F. H., L. M. R.,

and A. A.-G. developed the optimization algorithm and interfaced the algorithm with the robot. F. G. L.

P., T. D. M., B. P. M., K. E. D., F. H., and L. M. R. designed and performed the robotic optimization

experiments. T. D. M, M. S. E., and D. J. D performed additional experiments. All authors participated

in the writing of the manuscript.

Competing interests:

 The authors declare no competing interests.

Data and material availability:

 All data needed to evaluate the conclusions in the paper are present in

the paper and/or the Supplementary Materials. The raw data recorded by the robotic platform during the

two optimization runs is available at

https://github.com/berlinguette/ada/tree/master/Science_Advances_aaz8867

.  Additional data available

from authors upon request.

Supplementary Materials:

Materials and Methods

Fig. S1. Ada robotic platform for thin film fabrication and characterization.

Fig. S2. Temperature profile of the heating protocol employed by Ada’s annealing furnace.

Fig. S3. UV-Vis-NIR film absorptance spectra for both optimization runs.

Fig. S4. Current-voltage relationships for both optimization runs.

Fig. S5. Correlation between pseudomobility measured using Ada and hole mobility measured using

hole-only thin film devices.

Page

26 of 27
​

​

​
​
​
​

Fig. S6. Dark field images of highly annealed spiro-OMeTAD thin films with different ratios of dopant.

Fig. S7. Differential scanning calorimetry traces of FK102 Co(III) TFSI salt.

Table S1. Values of manipulated and responding variables for run 1.

Table S2. Values of manipulated and responding variables for run 2.

Table S3. Repeatability of a pseudomobility measurement made using Ada.

Movie S1. Robotic workflow

Page

27 of 27
​

​

Supplementary Materials for

Self-driving laboratory for accelerated discovery of thin-film materials

B. P. MacLeod, F. G. L. Parlane, T. D. Morrissey, F. Häse, L. M. Roch, K. E. Dettelbach, R. Moreira, L. P. E.
Yunker, M. B. Rooney, J. R. Deeth, V. Lai, G. J. Ng, H. Situ, R. H. Zhang, M. S. Elliott, T. H. Haley, D. J.
Dvorak, A. Aspuru-Guzik*, J. E. Hein*, C. P. Berlinguette*

Correspondence to: cberling@chem.ubc.ca

This PDF file includes:

Supplementary materials and methods
Supplementary figures S1 to S7
Supplementary tables S1 to S3
Supplementary movie S1

1

Supplementary materials and methods

Hole mobility measurement using hole-only devices device fabrication

Hole-only devices were fabricated and used to perform hole mobility measurements of spiro-OMeTAD

films using the steady-state space-charge limited current (SCLC) method

29,30

​ (see Fig. S5).

Indium tin oxide (ITO)-coated glass substrates

(Thin Film Devices, 1.1 mm OLED/OPV grade)

were cut

into 1.8cm × 3.5 cm pieces.  1.5 cm of the ITO coating was removed by etching with Zn powder and 2M HCl.

The etched substrates were then sonicated for 5 minutes in each of the following: detergent (Extran®  300),

distilled water, acetone, isopropanol.  The ultrasonically cleaned substrates were then blown dry with nitrogen

and subjected to a UV-ozone treatment for 30 minutes directly before use.

A PEDOT:PSS ink was formulated by filtering an aqueous dispersion of PEDOT:PSS (Heraeus

Clevios™ AI 4083) through a 40 µm PVDF filter and then combining 1 part by volume of this dispersion with 2

parts by volume of isopropanol. PEDOT:PSS films were then manually deposited on the ITO substrates by

dynamic spin-coating 100 µL of the PEDOT:PSS ink at 3000 RPM for 1 minute. A Kimwipe

®

 soaked in water

was then used to remove 1 cm of the PEDOT:PSS from each side of the device before baking the device for 1 h

at 150 °C.

Spin-coating inks with FK 102 Co(III) TFSI:spiro-OMeTAD molar ratios of 0, 14, 42, 56, 84 and 98%

were prepared by robotic pipetting using the

platform as described in the
Ada
​

section of
Materials and Methods
​

the manuscript. Spiro-OMeTAD films of varying doping levels were then manually deposited on the

glass/ITO/PEDOT:PSS devices by dynamic spin coating 50 µL of each ink at 3000 RPM for 1 minute. A

2

​

​

​
​

​

​
​

​
​
Kimwipe soaked in acetone was then used to remove 1 cm of the spiro-OMeTAD film from each side of the

device.

To complete the devices, 80 nm-thick gold contact layers were deposited by electron beam evaporation

through a Kapton

®

 shadow mask. The final device area was 3.5 mm

2
​.

Film thicknesses for the HTM layers on the hole-only devices were measured by stylus profilometry

(Bruker Dektak XT). Current-voltage curves were obtained for each device using a source-measure unit

(Keithley 2400); the applied voltage ranged from 0 to 1 volts and measurements occurred in air. Following Xu

et. al

30

​, , hole mobilities were extracted using the SCLC method by fitting the quadratic region of the current

density curve to the Mott-Gurney law

9
J = 8

μεε

V 2
0 d3

where

 μ

is the mobility of the HTM layer,

 ε

is the relative permittivity of the HTM (for which we assumed a

value of 3),

 εo

is the vacuum permittivity and

d

is the HTM thickness.

With the exception of the device with a dopant:HTM molar ratio of 84% which was removed from the

dataset as reliable thickness data was not obtained, the hole mobilities reported in figure S6C are the mean

values obtained from all the working devices obtained for each doping level, numbering between 3 - 7. The

error bars are the standard deviations across all the measured devices.

Robotic pseudomobility measurements for comparison to hole mobility measurements

The pseudomobility values reported in figure S6C are the average of quadruplicate measurements made

on HTM films with FK 102 Co(III) TFSI:spiro-OMeTAD molar ratios of 0, 14, 42, 56, 84 and 98%. These

3

​
​
​

​

films were prepared and characterized using the

platform as described in the
Ada
​

Materials and Methods

section of the manuscript. The pseudomobility error-bars shown in figure S6C are the standard deviation of the

quadruplicate measurement results.

Determination of the melting point of FK102 Co(III) TFSI by Differential Scanning Calorimetry

The melting of FK102 Co(III) TFSI salt (see Fig. S7) was measured by a Differential Scanning

Calorimeter (Netzsch DSC 214 Polyma) using heating and cooling rates of 10 K min

-1
​ and a N

 purge. The
​2

sample was heated and cooled five times between 0 °C and 250 °C, with the final two cycles showing a

stabilized melting point of 189 °C. The DSC traces from the final two heating cycles are shown in Fig. S7.

4

​
​
​
​

Supplementary figures

All figures containing numerical data were created in Python using the matplotlib library.

Fig. S1.

 robotic platform for thin film fabrication and characterization.
Ada
​

 This platform includes: (1) an annealing furnace with

(2) a slot-shaped sample port; (3) a weigh scale for feedback dispensing of solutions; (4) a rack for stock solution vials; (5) a rack for

storing clean pipet tips and (6) a container for disposal of used tips; (7) a rack for clean mixing vials; (8) a rack for clean glass slides;

(9) a 4-point probe for measuring film conductance; (10) a robotic arm for handling vials and slides with (11) an attachment for

gripping slides and (12) a station for storing this attachment when not in use; (13) a spin coater with (14) a removable lid; (15) a

camera for dark field imaging; (16) a spectrometer for transmission and reflection measurements.

5

​
​
Fig. S2. Temperature profile of the heating protocol employed by

annealing furnace.
Ada’s
​

 A thermocouple was contacted to a

glass microscope slide and the measured temperature was collected at a series of times after the heat gun was turned on. The data was

fit to an asymptotic regression model.

6

​
​

Fig. S3. UV-Vis-NIR film absorptance spectra for both optimization runs.

 (

A)

spectra for run 1. (

B)

 spectra for run 2. The film

absorption was calculated from the transmission and reflection spectra of both the glass substrate and the deposited film on the glass

substrate. Absorption values for films with varying dopant:HTM ratios are shown, as indicated by the side bar. The mean absorption

from 495 - 505 nm (indicated by the grey bar) was used to calculate pseudomobility.

7

​
​
​
​
​

Fig. S4. Current-voltage relationships for both optimization runs.

 (

A)

 I-V curves for run 1.  (

B)

 I-V curves for run 2. Potentials

were recorded with a 4-point probe delivering a current between 0 and 4 nA for films with varying dopant:HTM ratios as indicated by

the side bar. Conductance was calculated from the fitted slope of the current-voltage plots.

8

​
​
​
​
​

Fig. S5. Correlation between pseudomobility measured using

 and hole mobility measured using hole-only thin film
Ada
​

devices.

 (

A)

 Photograph of an array of hole-only devices used for measuring hole mobility (

B)

Schematic of the prepared hole-only

devices. (

C)

Comparison between manually-measured hole mobility data from the hole-only devices and the pseudomobility data

measured using the

platform. To facilitate visual comparison, the y-axes have been scaled such that the maxima of the two
Ada
​

data-sets are equal. Photo credit: David J. Dvorak, The University of British Columbia.

9

​
​
​
​
​
​
​
​
​

Fig. S6. Dark field images of highly annealed spiro-OMeTAD thin films with different ratios of dopant.

 Shown above are the

images of three representative samples from run 2. When no dopant was added, no dewetting was observed. Dewetting was much

more significant at an intermediate dopant:HTM ratio compared to a high dopant:HTM ratio. Scale bars are 1 cm.

10

​

Fig. S7. Differential scanning calorimetry traces of FK102 Co(III) TFSI salt.

The sharp, labelled endothermic peak in each trace

indicates the temperature of the crystalline-to-liquid phase transition. Traces of the fourth and fifth heating cycles are offset vertically

for clarity.

11

​

Table S1. Values of manipulated and responding variables for run 1.

Sample

Conductance

+
​ Absorptance
HTM

Pseudomobility

Dopant:HTM
(mol:mol)

Annealing time (s)

(nS)

at 500 nm

 (nS)

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

0.358

0.994

0

0.761

0.979

0.987

0.046

0.994

0

0.178

0.491

0.341

0.394

0.444

0.025

0.402

0.458

0.409

0.522

115

202

237

133

1

227

2

216

0

21

0

49

3

23

128

76

238

92

88

mean

st. dev.

mean

st. dev.

mean

st. dev.

7.6

20.0

0.079

0.050

47

124

0.324

0.020

157

19

41.8

17.9

0.314

0.038

50.7

0.0

0.0

35.9

3.3

0.0

0.0

0.3

4.2

42.2

0.0

39.2

60.8

0.1

9.6

0.0

0.9

2.0

0.001

0.000

0.067

0.004

0.258

0.006

0.026

0.000

0.329

0.033

0.086

0.003

0.183

0.004

0.005

0.002

0

73.8

20.5

0.135

0.002

52.2

17.4

0.153

0.003

66.5

25.9

0.163

0.006

3.9

120.7

0.0

0.4

1.1

0.0

0.022

0.003

0.164

0.003

0.055

0.002

16.6

28.6

0.102

0.049

10.7

24.4

0.098

0.048

0

0

139

136

161

129

458

332

548

341

410

184

734

0

98

60

0

0

3

59

4

30

0

23

11

156

114

165

25

13

0

168

129

12

​

19

20

21

22

0.395

0.389

0.387

0.975

69

73

81

88

74.5

36.2

0.152

0.009

109.8

10.1

0.160

0.003

47.4

54.0

0.142

0.038

68.0

0.8

0.357

0.196

485

685

281

218

237

52

319

59

  23*

  0.376*

  72*

  104.0*

  18.4*

  0.044*

 0.014*

  2,600*

  935*

24

25

26

27

28

29

30

31

32

33

34

0.345

0.308

0.529

0.372

0.685

0.315

0.235

0.337

0.31

0.45

0

73

82

55.9

54.8

0.153

0.008

58.1

39.3

0.139

0.006

355

421

172

0.0

0.0

0.073

0.010

0

70

75

63

94.9

42.9

0.163

0.003

580

10.4

27.6

0.129

0.064

51

102.4

2.5

0.141

0.004

727

167

4.5

11.8

0.090

0.030

72

81

58

93

60.8

42.0

0.138

0.021

97.7

11.1

0.141

0.008

126.6

0.0

1.5

0.0

0.180

0.003

0.002

0.000

0

34

427

692

703

347

281

0

261

134

13

90

262

74

10

0

*A brief spectrometer power failure resulted in calibration errors between the spectra of the glass slide and the spectra of the thin
film, invalidating the calculation of thin film absorptance. This outlier was removed in all following analyses.

13

Table S2. Values of manipulated and responding variables for run 2.

Sample

Conductance

+
​ Absorptance
HTM

Pseudomobility

Dopant:HTM
(mol:mol)

Annealing time (s)

(nS)

at 500 nm

 (nS)

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

0.988

0.359

0.702

0.032

0.904

0.927

0.973

0

0.967

0.98

1.009

0.543

1.026

0.516

0.535

0.491

0.504

0.023

0.567

202

115

151

4

175

233

206

237

212

1

147

0

159

1

43

0

58

127

67

mean

st. dev.

mean

st. dev.

mean

st. dev.

53.5

3.0

0.354

0.013

152

13

9.3

0.0

2.4

77.6

24.6

0.082

0.044

0.0

0.1

6.4

0.067

0.003

0.019

0.000

0.300

0.009

46.0

28.6

0.285

0.084

39.0

21.6

0.299

0.056

58

0

122

259

190

139

0.0

0.0

0.008

0.016

0

48.9

38.7

0.284

0.102

39.3

0.1

0.275

0.002

39.8

27.1

0.290

0.068

78.5

0.5

0.204

0.003

49.4

16.9

0.318

0.016

76.9

125.6

71.0

1.2

1.0

1.7

0.192

0.005

0.219

0.005

0.189

0.008

88.2

53.4

0.190

0.007

3.7

0.1

0.023

0.001

47.3

55.9

0.170

0.051

241

143

161

384

155

399

574

376

457

158

225

154

0

3

29

134

92

0

245

1

144

5

54

5

15

21

272

2

260

14

​

19

20

21

22

23

24

25

26

27

28

0.508

0.464

0.592

0.472

0.337

0.482

0.314

0.441

0.239

0.469

233

0.0

0.055

0.004

0

0.0

1.3

131.5

0.185

0.003

100.6

36.7

0.191

0.035

130.2

108.5

1.6

7.4

0.184

0.002

0.155

0.009

126.7

15.4

1.556

2.310

107.3

133.3

5.6

0.4

0.149

0.008

0.182

0.002

57.5

39.9

0.122

0.001

47.4

51.2

0.154

0.039

712

515

707

701

438

722

734

470

269

47

59

41

70

62

70

50

79

66

  29*

  0.292*

  57*

  0.0*

  0.0*

  0.001*

  0.000*

 0*

30

31

32

33

34

0.313

0.329

0.367

0.247

0.314

28

58

19

59

34

92.7

109.0

87.1

88.9

90.5

1.3

2.7

0.9

0.6

3.7

0.138

0.003

0.146

0.003

0.148

0.002

0.119

0.001

0.127

0.007

671

745

587

748

717

0

6

151

14

27

287

42

7

326

277

 0*

11

18

13

7

54

*An alignment error during spin coating resulted in no precursor solution deposited onto the glass slide. This outlier was removed in
all following analyses.

15

Table S3. Repeatability of a pseudomobility measurement made using
The Pseudomobility values
Ada.
​
shown below were measured on 10 replicate samples with nominal doping ratio 0.247 and annealing time 59
seconds. These samples were robotically prepared and characterized by the Ada platform in a single run over
the course of 3.75 hours

Replicate number

Pseudomobility (nS)

1

2

3

4

5

6

7

8

9

10

mean

standard deviation

662.5

667.7

640.4

655.8

643.8

651.1

659.7

663.9

657.5

658.2

656.1

8.687

standard deviation / mean

1.324%

Supplementary movies

Movie S1 - Robotic workflow. For high-resolution version, see:

https://youtu.be/0wVLjVdrYEE

This video shows the
 robotic platform performing workflow steps identical or similar to those used to
Ada
​
perform the experiments reported in the manuscript.

16

​

​
​
