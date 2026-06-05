---
tags:
  - literature
  - type/paper
  - lit/sdl
  - lit/ai-methods
  - lit/digital-discovery
type: literature-note
status: converted
source_type: pdf
source_file: "rooney2022_sdl_adhesive_materials.pdf"
source_path: "/Users/iyakavets/Documents/Github/LH_BO_Preprint/literature/pdfs/self_driving_labs/rooney2022_sdl_adhesive_materials.pdf"
pdf: "_attachments/Self-Driving Labs/rooney2022_sdl_adhesive_materials.pdf"
title: "A self-driving laboratory designed to accelerate the discovery of adhesive materials"
year: "2022"
doi: "10.1039/d2dd00029f"
citation_count_openalex: 48
topics:
  - Self-Driving Labs
  - Lab Automation
  - Autonomous Experimentation
---

# A self-driving laboratory designed to accelerate the discovery of adhesive materials

**Key:** `rooney2022_sdl_adhesive_materials`  
**Year:** 2022  
**DOI:** 10.1039/d2dd00029f  
**OpenAlex citations:** 48  
**PDF:** [[_attachments/Self-Driving Labs/rooney2022_sdl_adhesive_materials.pdf]]

## Why It Matters

This paper is part of the high-citation self-driving laboratory set imported from the LH_BO preprint literature review. Use it to support background claims about closed-loop experimentation, autonomous laboratory infrastructure, AI-guided experiment planning, or automated materials/chemical discovery.

## Connections

- [[Concept - Self-Driving Labs]]
- [[Concept - Lab Automation]]
- [[Concept - Optimization and Bayesian Search]]
- [[Map - Self-Driving Lab Stack]]

## Converted Text

Volume 1
Number 4
August 2022
Pages 347-542

 Digital
  Discovery

rsc.li/digitaldiscovery

ISSN 2635-098X

PAPER
Curtis P. Berlinguette et al.
A self-driving laboratory designed to accelerate
the discovery of adhesive materials

Digital
Discovery

PAPER

Cite this: Digital Discovery, 2022, 1, 382

A self-driving laboratory designed to accelerate the
discovery of adhesive materials†

Michael B. Rooney,
Zachary J. Thompson,e Kolby L. White,e Justin Tungjunyatham,e
Brian J. Stankiewicz

e and Curtis P. Berlinguette

‡a Benjamin P. MacLeod,

‡ab Ryan Oldford,

*abcd

a

We report a self-driving laboratory for adhesive material optimization. This autonomous laboratory

combines a robot for preparing and testing adhesive bonds with a Bayesian optimizer to rapidly improve

adhesive formulations. This system uses a single robot to perform a complex sequence of eight tasks

including surface preparation,

test specimen assembly, and bond strength evaluation. To enable

automated strength testing, we developed an automated pull test method that correlates linearly with
a single-lap-joint shear test method. This work demonstrates how ﬂexible automation accelerates
complex, multi-step experimental workﬂows for which commercial automation solutions are not available.

Received 4th April 2022
Accepted 28th May 2022

DOI: 10.1039/d2dd00029f

rsc.li/digitaldiscovery

Introduction

Adhesives are an easy to use, inexpensive way to bond materials
together.1 A wide range of ingredients are used to customize
adhesives for diﬀerent applications.1–4 Optimized adhesive
formulations may contain six or more components (Fig. 1). It is
extremely diﬃcult to predict the properties of the resulting
disordered composites a priori.5 This challenge is compounded
by the fact that bond strength depends not only on the chemical
makeup of the adhesive, but also on the properties of the
adhesive/adherend interfaces.1 These challenges make the
discovery of new adhesives highly empirical.

New adhesives are developed by iteratively preparing and
testing experimental formulations. The overall adhesive devel-
opment process is time-consuming because the number of
possible formulations is large and multiple test specimens
must be made and broken to characterize each formulation.
One of the most common adhesive characterization methods is
the single-lap-joint shear test (“lap shear” – e.g. ASTM D1002 6),
where the test specimen consists of two rectangular coupons of
material bonded together in an overlapping geometry (Fig. 1).

aDepartment of Chemistry, The University of British Columbia, 2036 Main Mall,
Vancouver, British Columbia, Canada, V6T 1Z1. E-mail: cberling@chem.ubc.ca

bStewart Blusson Quantum Matter Institute, The University of British Columbia, 2355
East Mall, Vancouver, British Columbia, Canada, V6T 1Z4

cDepartment of Chemical & Biological Engineering, The University of British Columbia,
2360 East Mall, Vancouver, British Columbia, Canada, V6T 1Z3

dCanadian Institute for Advanced Research (CIFAR), MaRS Innovation Centre, 661
University Ave. Suite 505, Toronto, Ontario, Canada, M5G 1M1

e3M Company, 3M Center, Maplewood, Minnesota 55144, USA
† Electronic
https://doi.org/10.1039/d2dd00029f
‡ These authors contributed equally to this work.

supplementary

information

(ESI)

available.

See

The shear stress required to separate these coupons is
a measure of the adhesive bond strength.6 The preparation of
reliable and reproducible lap shear specimens requires
a researcher to manually clean and abrade the coupons, deposit
adhesive on them, close the joints, and xture them in place for
curing. The researcher must then wait hours to days for the
specimens to cure before testing them. This testing is typically
done by manually loading specimens into a universal tester one
at a time. Although autosampling universal testers exist,7 they
do not eliminate the time-consuming manual preparation of
test specimens. This specimen preparation bottleneck limits
the rate at which new formulations can be tested. The cognitive
challenge of optimizing a multi-component formulation also
slows the development of new adhesives. Here we describe
a self-driving robotic laboratory which addresses both the rate
of adhesive specimen testing and the challenge of choosing
which formulations to test.

Our self-driving laboratory uses a robot to automatically
create and test adhesive specimens. This robot employs a dolly
pull-oﬀ test,8–10 which we show correlates with manual lap shear
tests. The robot operator is only responsible for the initial
stocking of consumables and dispensing the adhesive. Once set
up, the laboratory can run without direct supervision and test
up to 50 independent samples before restocking. Our robot
signicantly reduces the existing manual labor requirement of
specimen creation and oﬀers precise control over the time
between forming and testing the bond.

We combined this robot with a Bayesian optimizer to enable
the autonomous optimization of an adhesive formulation
(Fig. 2). Bayesian optimizers iteratively search for
input
parameters that maximize an outcome and have previously
been used to guide manual optimization of adhesive formula-
tions.11 Autonomous workows that combine optimizers with

382 | Digital Discovery, 2022, 1, 382–389

© 2022 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 07 June 2022. Downloaded on 6/1/2026 2:13:27 AM.  This article is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported Licence.View Article OnlineView Journal | View IssuePaper

Digital Discovery

Fig. 1 Adhesives are complex, multi-component materials which must satisfy multiple objectives. Two-part formulations may include six or
more components. An adhesive must satisfy several objectives depending on the application. The fully cured material must exhibit suitable
physical properties while the uncured material must have appropriate handling characteristics. Other important objectives include cost and
toxicity. A single-lap-joint shear test specimen is shown in the middle; it is composed of two ﬂat substrates bonded by an adhesive of known area.

Fig. 2 A workﬂow for optimizing the strength of an adhesive formulation. This workﬂow involves preparing adhesive formulations, cleaning
substrates using abrasives and solvents, and then using these formulations and substrates to create test specimens. The test specimens are then
cured, and their strength is measured. The data is analyzed, and the results are used to design improved formulations for the next round of
experiments. Typically, all the steps of this lengthy procedure are performed manually. Here we automated six of the seven steps using ﬂexible
automation and machine learning.

robotic experiments to optimize formulations are nascent12,13
and have not yet been reported for adhesives research. To
demonstrate the capabilities of our self-driving laboratory, we
used it to maximize the bond strength of a two-part epoxy by
optimizing the resin to hardener ratio.

system was controlled through a custom graphical user inter-
face (UI) built in Python (Fig. S3†). The steps in the robotic
workow (preparation, adherend cleaning, specimen assembly
and curing, bond strength measurement, see Fig. 3 and Video
S1†) are described in more detail below.

Experimental

The preparation of overlap shear test specimens is diﬃcult to
automate. We therefore devised an alternate bond strength
testing method more amenable to automation (Fig. 3). Speci-
cally, we adapted a standard pull-oﬀ testing method (normally
used to measure coating adhesion14) to enable the automated
testing of adhesive strength. This pull-oﬀ method involves
adhering an aluminum dolly to a substrate, pulling oﬀ the dolly
using a force normal to the substrate with a commercially
available testing head, and recording the maximum force
required to break the bond (Fig. 3a and j). We built on our
previous self-driving laboratories,15,16 by constructing the
system described here using a 4-axis robotic arm (N9, North
Robotics) (Fig. 4 and S1†). We leveraged rapid prototyping to
develop the custom hardware components necessary for the
exible automated workow executed by this robot. The robotic

To prepare the robotic platform for operation, it was rst
manually stocked with dollies and test plates. The soware was
then congured to run the desired test. The workow presented
here used commercially available aluminum dollies with 10 mm
or 20 mm diameter bond areas (Defelsko Corporation). Up to 50
dollies could be placed within reach of the robot on two dolly
trays (25 dollies each). Test plates were waterjet cut from 1
4 inch-
thick 6061 aluminum sheets. Two alignment holes in each test
plate facilitated accurate xturing on the robotic platform.
restocking
Other
included: a foam brush, isopropanol bath, abrasive pad, and
abrasive tool.

requiring periodic

consumable

items

The rst step in the workow was the automated cleaning of
both the dollies and the test plates (Fig. 3c–f). The bottom face
of each dolly was abraded by rapidly rotating the dolly (using the
robot arm's gripper rotation) while in contact with an abrasive
pad. The dolly was dipped in an isopropyl alcohol (IPA) bath to
clean away the dust generated by the abrasion step and dried in

© 2022 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2022, 1, 382–389 | 383

Open Access Article. Published on 07 June 2022. Downloaded on 6/1/2026 2:13:27 AM.  This article is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported Licence.View Article OnlineDigital Discovery

Paper

Fig. 3 Multi-step robotic workﬂow for adhesive specimen preparation and testing. (a) The adhesive test specimen employed in the workﬂow is
a pull-oﬀ type consisting of an aluminum dolly adhered to an aluminum plate. (b) A 4-axis robotic arm including a rotating gripper was employed
for this study. The major steps in the workﬂow executed by the robot are (c) and (d) abrasive cleaning of the dolly and test plate, (e) and (f) solvent
cleaning of the dolly and test plate, (g) and (h) assembly of the test specimen by dipping the dolly into a weigh boat containing adhesive and then
placing the dolly on the test plate, (i) curing of the adhesive under ambient conditions, and (j) strength testing by measuring the force required to
break the bond between the dolly and the test plate.

a stream of compressed N2 gas. Digital photographs of the
dolly's bottom face were taken at the camera station (BFS-U3-
120S4C-CS, Teledyne FLIR LLC) before and aer cleaning, and
saved with all workow data. The test plates were abraded by
a medium coarse rotating abrasive disk tool which was held by
the robot's rotating gripper and pressed downward onto the test
plate. The distance between the gripper and test plate was
manually adjusted until test plates were visibly cleaned of
contaminants, and a consistent surface nish was observed.
The robot arm did not have force feedback, however the
downward force applied by the abrasive tool to the test plate was
estimated to be 20 N. Accumulated dust and abrasion particu-
lates were brushed clean with a disposable foam brush wetted
with IPA. The foam brush was automatically cleaned by soni-
cation in an IPA bath (PC3, L & R Manufacturing), then dried
with a stream of N2 compressed gas. Aer cleaning both the
dollies and the test plates, the robot assembled each specimen
by picking up a dolly, dipping it in adhesive, and then placing it
onto the test plate. Up to 25 specimens in a 5 (cid:1) 5 pattern could
be placed on each test plate. The adhesives to be tested are
stored in trays adjacent to the test plates on the robotic plat-
form. Each tray contained up to 5 adhesive formulations to test.
Each formulation was stored in a disposable weigh boat and
contained enough adhesive for up to 5 specimens. To set bond
thickness, glass spacer beads (Envirospheres, E-SPHERES SL
Grade SLG, mean particle size 0.130 mm) were manually mixed
into the adhesive at 0.5% of the total adhesive mass. When the
robot is ready to begin assembling specimens, the robot

prompts the operator to manually dispense the adhesives to be
tested into the weigh boats. For the two-part epoxies studied
here (3M™ Scotch-Weld™ Epoxy Adhesive DP190 Gray and
3M™ Scotch-Weld™ Epoxy Adhesive DP420 Black), we experi-
mentally determined that approximately 0.33 g of adhesive is
needed per specimen. The robot arm dipped the dolly into the
adhesive, performed pre-set movements to minimize dripping,
and placed the dolly on the test plate. The robot placed each
dolly on the test plate at a xed height set to ensure the dolly
rmly contacted the plate before being released by the gripper.
The robotic system oﬀers precise control over the time between
bond formation and strength measurement. The bond strength
measurements were performed one specimen at a time aer
a predetermined curing period.

The robot measured the adhesive bond strengths using
a commercial pull-oﬀ adhesion tester (PosiTest ATA20, DeFel-
sko, Fig. 4b). This tester consists of a hydraulic actuator and
a quick-release collar congured to pull a dolly away from a test
plate with up to 7.55 kN of force. This tool was originally
designed for manual use, so we modied it in order to automate
its functions, and to enable it to be picked up by the robot
(Fig. 4b and S2†). A 3D-printed chassis along with pneumatic
pistons were added to the testing tool to actuate the internal
collar. A longer metal handle was added to the tester tool to
provide a cylindrical feature for the robot to grip. These modi-
cations enabled fully automated docking, testing, and ejection
of dollies. Aer locking on to a dolly, the test head increased the
(cid:3)1 until the bond failed.
force at a rate of approximately 300 N s

384 | Digital Discovery, 2022, 1, 382–389

© 2022 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 07 June 2022. Downloaded on 6/1/2026 2:13:27 AM.  This article is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported Licence.View Article OnlinePaper

Digital Discovery

Fig. 4 Robotic platform used to automatically create and test adhesive specimens. (a) The robot, stations, and tools used to execute the
automated workﬂow (see also Fig. S1†). This system can create up to 50 test specimens from up to 10 unique formulations before the
consumables (adhesives, dollies and test plates) need to be replenished. (b) Detailed view of the hydraulic strength testing tool used by the robot
to measure bond strength. A variety of custom components added to the strength testing tool to enable automated operation are shown (see
also Fig. S2†). (c) The sequence of operations performed by the system. After data is obtained by the robot, a Bayesian optimization algorithm is
used to design the next batch of formulations to test.

The normal force required to break the bond between the dolly
and plate was recorded for each specimen. Aer performing the
pull-oﬀ test, the robot captured an image of the adhesive failure
surface on the dolly's bottom face. The robot then ejected the
dolly into a discard bin, and reset the test head. This pull test
took approximately 2 minutes, and was repeated for each dolly
on the test plate.

Results and discussion

To assess the validity of our automated pull tests we compared
them to manual lap shear tests for two commercial epoxies
(3M™ Scotch-Weld™ Epoxy Adhesive DP190 Gray and 3M™
Scotch-Weld™ Epoxy Adhesive DP420 Black) at varying cure
times (Fig. 5 and Tables S1–S3†). The resulting data showed
a linear correlation between the automated pull test and
manual lap shear methods for each epoxy.

3M™ Scotch-Weld™ Epoxy Adhesive DP190 Gray is a exible
epoxy. Flexible epoxies provide an elastic bond that enables
some movement between the adherends without failure. We
compared pull-oﬀ tests for this epoxy to manual lap shear tests
performed in our laboratory. These lap shear tests used 4 (cid:1) 1 (cid:1)
0.0625 inch aluminum coupons that were prepared by

sandblasting followed by wiping with isopropanol before
assembly with a 0.5 inch overlap using 0.003 inch diameter
glass beads to control the bond thickness. The correlation slope
between the tensile stress of the pull-oﬀ test and the shear stress
of the lap shear tests was 2.29 over the range of cure conditions
tested. 3M™ Scotch-Weld™ Epoxy Adhesive DP420 Black is
a toughened epoxy. Toughened epoxies provide a more rigid but
impact and fatigue-resistant bond. We compared pull-oﬀ tests
for this epoxy to manual lap shear data from the material
technical data sheet.17 The correlation slope was 0.72 (Fig. 5).

Correlations for both epoxy adhesives exhibited high degrees
of linearity (R2 ¼ 0.99 for 3M™ Scotch-Weld™ Epoxy Adhesive
DP190 Gray; R2 ¼ 0.99 for 3M™ Scotch-Weld™ Epoxy Adhesive
DP420 Black). We attribute the diﬀerences in correlation slope
to the very diﬀerent mechanical properties of the two adhesives
(exible vs. toughened) and the diﬀerent lap shear procedures
employed (our manual preparation and testing of lap shear
samples vs. datasheet reported values). These results show that
the pull-oﬀ test is suitable for comparing the relative strengths
of a given type of adhesive and can track rate-of-strength build
as a function of cure time.

To demonstrate the capabilities of our self-driving labora-
tory, we used it to maximize the bond strength of an adhesive

© 2022 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2022, 1, 382–389 | 385

Open Access Article. Published on 07 June 2022. Downloaded on 6/1/2026 2:13:27 AM.  This article is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported Licence.View Article OnlineDigital Discovery

Paper

Fig. 5 Correlation between automated (pull-oﬀ) and manual (lap shear) adhesive strength tests. Bond strength data was obtained using triplicate
pull-oﬀ tests executed by our robotic system, triplicate manual lap shear tests for 3M™ Scotch-Weld™ Epoxy Adhesive DP190 Gray, and
referenced lap shear data for 3M™ Scotch-Weld™ Epoxy Adhesive DP420.17 Both adhesives were tested over a range of curing conditions (2–6
hours for 3M™ Scotch-Weld™ Epoxy Adhesive DP420, 1–5 days for 3M™ Scotch-Weld™ Epoxy Adhesive DP190 Gray) to assess the adhesive
strength correlation over a wider range of values. Horizontal and vertical error bars indicate standard deviations of the recorded stresses across
replicate samples.

formulation. We performed this optimization by coupling our
automated workow to a Bayesian optimizer.15,16 Bayesian
optimizers combine a surrogate model with an acquisition
function. The surrogate model predicts the response of an
experiment
to the manipulated variables. The acquisition
function determines which experiment(s) should be performed
next to optimize the outcome of the experiment. The Bayesian
optimization performed here manipulated the ratio of resin to
hardener in a two-part epoxy system to maximize the strength as
measured using the robotic pull-oﬀ test. We expressed this
manipulated variable as a resin fraction R ¼ massresin/(massresin
+ masshardner) to obtain a variable ranging from 0 to 1. The resin
and hardener used in the formulation were taken from
a commercially available two-part epoxy (3M™ Scotch-Weld™
Epoxy Adhesive DP420 Black).

We leveraged the ability of the robotic system to test multiple
formulations in parallel by employing the AX Bayesian optimi-
zation package which supports batchwise acquisition of data
from the experiment using the q-noisy expected improvement
(qNEI) acquisition function.18,19 Once a batch of formulations was
requested by this optimizer, formulations with the requested
resin fraction were prepared by manually weighing individual
components into a weigh boat on a digital weigh scale. The
formulations were then mixed by hand with a stir stick before
being loaded onto the robotic platform. This step was followed by
completely automated specimen preparation, curing for 3 h, and
testing. The resulting data is used to update the optimizer's
surrogate model and a new batch of formulations is requested,
beginning the next round of the optimization.

Each round of the optimization involved testing a batch of
ve formulations in triplicate (Fig. 6 and Tables S4–S7†). The
resin fractions for the ve formulations tested in the rst round
were selected using a scrambled sobol sequence. The resulting
data was used to initialize the Gaussian process surrogate
model used by the optimizer. The sobol sequence and surrogate
function used the default settings implemented in the AX
Bayesian optimization package.18 The resin fractions for
subsequent rounds were selected by the optimizer using the
qNEI acquisition function. Dolly images acquired aer the pull-
oﬀ tests showed wet-looking residual material consistent with
incompletely cured adhesive for resin ratios below 0.2 or above
0.7. The images of dollies with resin ratios between 0.2 and 0.7
showed dry-looking residual material consistent with cured
adhesive. The region containing the optimal resin fraction to
maximize strength was very clearly dened aer four rounds of
In the particular experimental optimization
optimization.
campaign shown here,
the formulation with the highest
strength was identied in round 1 by random chance. Simu-
lated optimization campaigns using the same optimizer
conguration as the real-world experiments showed that when
the optimum formulation is not identied in round 1, the
optimizer will converge on the optimal formulation in subse-
quent rounds (see Fig. S4†). These results demonstrate that our
self-driving laboratory can nd an optimal resin fraction for
maximizing the tensile strength of a 2-part epoxy. This self-
driving lab could be adapted to the optimization of more
complex formulations.

386 | Digital Discovery, 2022, 1, 382–389

© 2022 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 07 June 2022. Downloaded on 6/1/2026 2:13:27 AM.  This article is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported Licence.View Article OnlinePaper

Digital Discovery

testing, and by using a Bayesian optimizer to choose which
formulations to test next. The automated workow used a single
robot to perform a complex sequence of eight tasks, including
a pull-oﬀ strength test. This test correlates with standard lap
shear tests and is suitable for optimizing adhesive bond
strength. This self-driving laboratory for adhesives could be
improved in several ways.

For example, increased ambient lab temperatures in opti-
mization round 4 increased the curing rate, resulting in
increased strength at the same epoxy fraction (compare Fig. 4c
with Fig. 4d). A temperature-controlled curing environment
would mitigate this problem. We note that the samples in this
study were cured for less time than specied in the technical
datasheet.

Consistent surface preparation is critical to obtaining
repeatable bond strength data. While we manually changed
the abrasion tools and pads employed in our setup at regular
intervals to maintain consistent surface preparation, a more
advanced system might automatically use fresh abrasion
media on a schedule. Alternatively, fresh adhesive media
could be adaptively requested by the system in response to
feedback
assurance
measurements.

from automated surface

quality

In this study, we manually developed a dip and place routine
that minimized unwanted dripping of adhesives. To facilitate
working with new adhesives having diﬀerent uid characteris-
tics, automatic optimization of the dip and place routine using
feedback (e.g., from a weigh scale or machine vision) would be
benecial.

Our robotic system automatically photographs the bottom
surface of every dolly aer testing. These images could be
automatically processed with machine vision to help classify the
bond failure mode or categorize morphological defects.20 This
information could be used to alert the researcher if an outlier
occurred.

While we presented a single-parameter, single-objective
optimization here, this optimization could be extended to
incorporate multiple manipulated variables or multiple opti-
mization objectives. Such extensions would be synergistic with
hardware upgrades.12,16 For example, incorporating an oven into
the robot would enable the optimization of thermal curing
protocols. Expert knowledge (such as the range of resin ratios
likely to yield high strength) or bond strength estimates based
on simulations21 could also be incorporated to increase the
eﬃciency of the Bayesian optimization.22,23

This work shows how exible automation can enable mate-
rials scientists to automate complex, multi-step experimental
workows for which commercial automation solutions are not
available.24 Self-driving laboratories will empower human
experts to rapidly develop high performance adhesives and
other complex formulated materials.

Fig. 6 Optimization of an adhesive formulation by a self-driving
laboratory. In each round of the optimization, ﬁve adhesive formula-
tions were cured for 3 h and then tested in triplicate. The mean and
standard deviation of the pull-oﬀ force for each formulation are
In round 1 (a), the ﬁve formulations were selected using
shown.
a scrambled sobol sequence. In the following rounds (b)–(d), the
formulations were selected by a Bayesian optimizer conﬁgured to
maximize the pull-oﬀ force of the adhesive by manipulating the ratio
of base to accelerant of a commercial two-part epoxy adhesive (3M™
Scotch-Weld™ Epoxy Adhesive DP420 Black).

Conclusions

Data availability

We demonstrated a self-driving laboratory that can optimize an
epoxy formulation to maximize the bond strength. This system
reduces human eﬀort by automating specimen preparation and

The experimental data are provided in the ESI.† The code used
for the simulations shown in Fig. S4† is available at https://
github.com/berlinguette/ada.

© 2022 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2022, 1, 382–389 | 387

Open Access Article. Published on 07 June 2022. Downloaded on 6/1/2026 2:13:27 AM.  This article is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported Licence.View Article OnlineDigital Discovery

Author contributions

Michael B. Rooney: conceptualization, methodology, visualiza-
tion, writing – original dra preparation. Benjamin P. MacLeod:
conceptualization, methodology, writing – original dra prep-
aration. Ryan Oldford: soware, methodology, visualization,
writing – review & editing. Zachary J. Thompson: methodology,
writing – review & editing. Kolby L. White: methodology, writing
– review & editing. Justin Tungjunyatham: methodology, writing
– review & editing. Brian Stankiewicz: conceptualization,
methodology, funding acquisition, writing – review & editing.
Curtis P. Berlinguette: conceptualization, methodology, fund-
ing acquisition, writing – review & editing.

Funding

We thank 3M Company, 3M Innovative Properties Company,
and the Natural Sciences and Engineering Research Council of
Canada (CRDPJ 543581-19) for their nancial support. C. P. B. is
grateful to the Canadian Foundation for Innovation (229288),
the Canadian Institute for Advanced Research (BSE-BERL-
162173), and the Canada Research Chairs Program for nan-
cial support. B. P. M. and C. P. B. acknowledge support from the
SBQMI's Quantum Electronic Science and Technology Initia-
tive, the Canada First Research Excellence Fund, and the
Quantum Materials and Future Technologies Program.

Conﬂicts of interest
The authors declare no conict of interest.

Acknowledgements

We gratefully acknowledge Karry Ocean, Alex Proskurin, and
Caroline Krzyszkowski for engineering and research support,
and Fraser Parlane for his assistance creating gures. We thank
CMC Microsystems for the provision of products and services
that facilitated this research, including SolidWorks 2019 SP5.0.
For soware that facilitated robot control and data processing,
we acknowledge the contributors to the Python programming
Soware
language
https://
www.python.org).

Foundation,

(Python

References

1 S. Ebnesajjad and A. H. Landrock, Chapter 1 – Introduction
and Adhesion Theories, in Adhesives Technology Handbook,
ed. S. Ebnesajjad and A. H. Landrock, William Andrew
Publishing, Boston, 3rd edn, 2015, pp. 1–18.

2 L. T. Tseng, R. H. Jhang, J. Q. Ho and C. H. Chen, Molecular
Approach to Enhance Thermal Conductivity in Electrically
Conductive Adhesives, ACS Appl. Electron. Mater., 2019,
1(9), 1890–1898.

3 G. H. Shim, B. Kweon, M. S. Lee, J. H. Kim, T. S. Jun, T. Kim,
et al., Highly improved mechanical and thermal properties
of alkali silicate and graphene nanoplatelet composite
adhesives, Int. J. Adhes. Adhes., 2021, 110, 102942.

Paper

4 J. S. Kang, A. J. Myles and K. D. Harris, Thermally-Degradable
Thermoset Adhesive Based on a Cellulose Nanocrystals/
Epoxy Nanocomposite, ACS Appl. Polym. Mater., 2020, 2(11),
4626–4631.

5 H. Quan and R. Alderliesten, On the eﬀect of plastic model
on simulation of adhesive bonded joints with FM94, Int. J.
Adhes. Adhes., 2021, 110, 102916.

6 American Society for Testing and Materials, Standard Test
Method for Apparent Shear Strength of Single-Lap Joint
Adhesively Bonded Metal Specimens by Tension Loading
(Metal-to-Metal), ASTM, 2019, Report No.: D1002-10,
available from: https://www.astm.org/d1002-10r19.html.
7 Illinois Tool Works Inc., Instron Automated Testing Systems,
from: https://www.instron.com/en-us/products/

available
testing-systems/automated-testing-systems.

8 B. J. Chisholm, D. C. Webster, J. C. Bennett, M. Berry,
D. Christianson, J. Kim, et al., Combinatorial materials
research applied to the development of new surface
coatings VII: an automated system for adhesion testing,
Rev. Sci. Instrum., 2007, 78(7), 072213.

9 L. L. Zhai, G. P. Ling and Y. W. Wang, Eﬀect of nano-Al2O3 on
adhesion strength of epoxy adhesive and steel, Int. J. Adhes.
Adhes., 2008, 28(1), 23–28.

10 American Society for Testing and Materials, Standard Test
Method for Pull-Oﬀ Strength of Coatings Using Portable
Adhesion Testers, 2017, Report No.: D4541-17, available
from: https://www.astm.org/d4541-17.html.

11 S. Pruksawan, G. Lambard, S. Samitsu, K. Sodeyama and
M. Naito, Prediction and optimization of epoxy adhesive
strength from a small dataset through active learning, Sci.
Technol. Adv. Mater., 2019, 20(1), 1010–1021.

12 L. Cao, D. Russo, K. Felton, D. Salley, A. Sharma, G. Keenan,
et al., Optimization of Formulations Using Robotic
Experiments Driven by Machine Learning DoE, Cell Rep.
Phys. Sci., 2021, 2(1), 100295.

13 T. Erps, M. Foshey, M. K. Lukovi´c, W. Shou, H. H. Goetzke
and H. Dietsch, et al., Accelerated Discovery of 3D Printing
Materials Using Data-Driven Multi-Objective Optimization,
arXiv [cond-mat.mtrl-sci], 2021, available from: http://
arxiv.org/abs/2106.15697.

14 Defelsko Corporation, Dolly Preparation for Pull-Oﬀ
Adhesion
https://
www.defelsko.com/resources/dolly-preparation-for-pull-oﬀ-
adhesion-testing.

available

Testing,

from:

15 B. P. MacLeod, F. G. L. Parlane, T. D. Morrissey, F. H¨ase,
L. M. Roch, K. E. Dettelbach, et al., Self-driving laboratory
for accelerated discovery of thin-lm materials, Sci. Adv.,
2020, 6(20), eaaz8867.

16 B. P. MacLeod, F. G. L. Parlane, C. C. Rupnow,
K. E. Dettelbach, M. S. Elliott, T. D. Morrissey, et al., A self-
driving laboratory advances the Pareto front for material
properties, Nat. Commun., 2022, 13(1), 1–10.

17 3M, Scotch Weld Epoxy Adhesive DP420 Black DP420 NS
Black DP420 Oﬀ-White DP420 LH Technical Data, available
from:
https://multimedia.3m.com/mws/media/1235389O/
dp420-technical-data-sheet.pdf.

388 | Digital Discovery, 2022, 1, 382–389

© 2022 The Author(s). Published by the Royal Society of Chemistry

Open Access Article. Published on 07 June 2022. Downloaded on 6/1/2026 2:13:27 AM.  This article is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported Licence.View Article OnlinePaper

Digital Discovery

18 E. Bakshy, L. Dworkin, B. Karrer, K. Kashin, B. Letham and
A. Murthy, et al., AE: a domain-agnostic platform for
adaptive experimentation, in Workshop on Systems for ML
and Open Source Soware at NeurIPS 2018, 2018, available
from:
http://learningsys.org/nips18/assets/papers/
87CameraReadySubmissionAE%20-%20NeurIPS%
202018.pdf.

21 O. B¨uy¨uk¨ozt¨urk, M. J. Buehler, D. Lau and C. Tuakta,
dynamics:
Structural
fundamentals and a case study of epoxy-silica interface,
Int. J. Solids Struct., 2011, 48(14), 2131–2140.

using molecular

solution

22 S. Sun, A. Tiihonen, F. Oviedo, Z. Liu, J. Thapa, Y. Zhao, et al.,
A data fusion approach to optimize compositional stability
of halide perovskites, Matter, 2021, 4(4), 1092–1094.

19 B. Letham, B. Karrer, G. Ottoni and E. Bakshy, Constrained
Bayesian Optimization with Noisy Experiments, arXiv
[stat.ML],
http://arxiv.org/abs/
1706.07094.

available

from:

2017,

23 A. E. Gongora, K. L. Snapp, E. Whiting, P. Riley, K. G. Reyes,
E. F. Morgan, et al., Using simulation to accelerate
autonomous
using
mechanics, iScience, 2021, 24(4), 102262.

experimentation:

study

case

a

20 N. Taherimakhsousi, B. P. MacLeod, F. G. L. Parlane,
T. D. Morrissey, E. P. Booker, K. E. Dettelbach, et al.,
Quantifying defects in thin lms using machine vision, npj
Comput. Mater., 2020, 6(1), 1–6.

24 B. P. MacLeod, F. G. L. Parlane, A. K. Brown, J. E. Hein and
C. P. Berlinguette,
automation accelerates
Flexible
materials discovery, Nat. Mater., 2021, DOI: 10.1038/
s41563-021-01156-3.

© 2022 The Author(s). Published by the Royal Society of Chemistry

Digital Discovery, 2022, 1, 382–389 | 389

Open Access Article. Published on 07 June 2022. Downloaded on 6/1/2026 2:13:27 AM.  This article is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported Licence.View Article Online
