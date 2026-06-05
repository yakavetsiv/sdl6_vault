---
type: literature-note
source_note: "Papers/Paper - Digilocs a leap forward in predicti.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Aravindakshan-2025-Digilocs-a-leap-forward-in-predicti.pdf"
converter: "microsoft/markitdown"
---
RESEARCH ARTICLE

DigiLoCS: A leap forward in predictive organ-
on-chip simulations

Manoja Rajalakshmi AravindakshanID
Stephan Schaller3, Christian MaassID

1, Chittaranjan Mandal1, Alex Pothen2,
3,4*

1 Department of Computer Science and Engineering, Indian Institute of Technology Kharagpur, Kharagpur,
West Bengal, India, 2 Department of Computer Science, Purdue University, West Lafayette, Indiana, United
States, 3 ESQlabs Gmbh, Saterland, Germany, 4 MPSlabs, ESQlabs Gmbh, Saterland, Germany

a1111111111
a1111111111
a1111111111
a1111111111
a1111111111

* christian.maass@esqlabs.com

Abstract

OPEN ACCESS

Citation: Aravindakshan MR, Mandal C, Pothen A,
Schaller S, Maass C (2025) DigiLoCS: A leap
forward in predictive organ-on-chip simulations.
PLoS ONE 20(1): e0314083. https://doi.org/
10.1371/journal.pone.0314083

Editor: Alberto Rainer, Università Campus Bio-
Medico di Roma, ITALY

Received: June 14, 2024

Accepted: November 5, 2024

Published: January 9, 2025

Copyright: © 2025 Aravindakshan et al. This is an
open access article distributed under the terms of
the Creative Commons Attribution License, which
permits unrestricted use, distribution, and
reproduction in any medium, provided the original
author and source are credited.

Data Availability Statement: All relevant data are
within the paper and its Supporting information
files.

Funding: MRA acknowledge funding from the
Science and Engineering Research Board, India
(https://serb.gov.in/) via the OVDF Scheme under
Award No. SB/S9/Z-03/2017-XI (2022). The
funders had no role in study design, analysis,
decision to publish, or preparation of the
manuscript.

Competing interests: The authors have declared
that no competing interests exist.

Digital twins, driven by data and mathematical modelling, have emerged as powerful tools
for simulating complex biological systems. In this work, we focus on modelling the clearance
on a liver-on-chip as a digital twin that closely mimics the clearance functionality of the
human liver. Our approach involves the creation of a compartmental physiological model of
the liver using ordinary differential equations (ODEs) to estimate pharmacokinetic (PK)
parameters related to on-chip liver clearance. The objectives of this study were twofold: first,
to predict human clearance values, and second, to propose a framework for bridging the
gap between in vitro findings and their clinical relevance. The methodology integrated quan-
titative Organ-on-Chip (OoC) and cell-based assay analyses of drug depletion kinetics and
is further enhanced by incorporating an OoC-digital twin model to simulate drug depletion
kinetics in humans. The in vitro liver clearance for 32 drugs was predicted using a digital-
twin model of the liver-on-chip and in vitro to in vivo extrapolation (IVIVE) was assessed
using time series PK data. Three ODEs in the model define the drug concentrations in
media, interstitium and intracellular compartments based on biological, hardware, and phys-
icochemical information. A key issue in determining liver clearance appears to be the insuffi-
cient drug concentration within the intracellular compartment. The digital twin establishes a
connection between the hardware chip structure and an advanced mapping of the underly-
ing biology, specifically focusing on the intracellular compartment. Our modelling offers the
following benefits: i) better prediction of intrinsic liver clearance of drugs compared to the
conventional model and ii)explainability of behaviour based on physiological parameters.
Finally, we illustrate the clinical significance of this approach by applying the findings to
humans, utilising propranolol as a proof-of-concept example. This study stands out as the
biggest cross-organ-on-chip platform investigation to date, systematically analysing and
predicting human clearance values using data obtained from various in vitro liver-on-chip
systems. Accurate prediction of in vivo clearance from in vitro data is important as inade-
quate understanding of the clearance of a compound can lead to unexpected and undesir-
able outcomes in clinical trials, ranging from underdosing to toxicity. Physiologically based
pharmacokinetic (PBPK) model estimation of liver clearance is explored. The aim is to
develop digital twins capable of determining better predictions of clinical outcomes, ulti-
mately reducing the time, cost, and patient burden associated with drug development.

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

1 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Various hepatic in vitro systems are compared and their effectiveness for predicting human
clearance is investigated. The developed tool, DigiLoCs, focuses explicitly on accurately
describing complex biological processes within liver-chip systems. ODE-constrained optimi-
sation is applied to estimate the clearance of compounds. DigiLoCs enable differentiation
between active biological processes (metabolism) and passive processes (permeability and
partitioning) by incorporating detailed information on compound-specific characteristics and
hardware-specific data. These findings signify a significant stride towards more accurate
and efficient drug development methodologies.

1 Introduction

The drug testing dilemma presents a significant challenge in pharmaceutical development,
marked by high costs and a distressing attrition rate in accurately predicting human responses
[1, 2]. A pivotal element in preclinical drug development is the accurate estimation of the first-
in-human dose and different dosing regimens to keep drug levels within a therapeutic range.
This demands precise assessments of hepatic clearance of the drug and human pharmacoki-
netics [3, 4]. Typically, the gold standard in drug development is the use of simpler in vitro sys-
tems to study drug metabolism, including liver microsomes [5] and suspension or plated
hepatocytes [6]. The drug depletion data (time-concentration profile) are then analysed to
determine the in vitro drug clearance rate. A simple mathematical model has been employed
in earlier work, and it considers the in vitro system as a single compartment, the one-compart-
ment PK model [7]. Well-mixing and instantaneous drug distribution is assumed and all bio-
logical processes, e.g., permeability and partitioning from cell culture media into intracellular
milieu are lumped into drug clearance. This approach also cannot differentiate between com-
pounds actually being metabolised and compounds bound to media proteins or hardware.
The so determined in vitro clearance value is then extrapolated to humans (in vitro—in vivo
extrapolation) and integrated into human physiologically-based pharmacokinetic (PBPK)
models [4, 8] to predict human pharmacokinetics (absorption, distribution, metabolism and
excretion (ADME)), before actually testing a new compound in humans. Although this
approach is well-established in drug development and easy to use, it also systematically under-
predicts human PK [9] by 5–10 fold across studies and compounds.

Microphysiological systems (MPS) and organ-on-chips, as well as 3D organoids, hold great

promise to address more complex in vitro ADME, toxicology and pharmacology questions
offering miniature, biomimetic systems that replicate key aspects of human organ physiology
[10–12]. These technologies create an environment where human cells can grow and interact
in an organ-specific context, providing insights into human biology and disease that were pre-
viously unattainable in conventional in vitro models or animal studies. OoC and MPS-based
systems are not only used in today’s drug development for PK but also for assessing drug effi-
cacy and toxicity [10, 13–15]. While the emulated in vitro biology of MPS and OoCs is getting
ever more complex and produces more human-relevant data, these systems still fall short in
considerably improving the prediction power of in-human situations, like PK [13, 16]. How-
ever, MPS and OoC data are also still analysed using the conventional mathematical model
(one-compartment) that does not account for advanced biology. It remains unclear whether
the OoC and MPS biology is still not human-relevant enough (and thus not producing
human-relevant data) or the conventional mathematical analysis is the cause for the underpre-
diction. Potentially, a digital twin framework that enables the mapping of complex on-chip

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

2 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

biology to advanced mathematical models could provide a useful approach to enable OoC and
MPS translation to humans and increase the prediction power, but it is currently lacking.

The current study aims to develop a digital twin approach integrating MPS and OoC data
within advanced computational models of biology to improve the prediction of clinical clear-
ances. DigiLoCs, our developed digital liver-on-chip simulator, facilitates the accurate descrip-
tion of on-chip complex biology to disentangle biological processes, namely clearance,
permeability, and partitioning. The tool comprises and utilises information on complex bio-
logical processes (clearance, permeability, partitioning), hardware-specific information from
the studied in vitro system, and compound-specific information. By accounting for more
multi-dimensional information, the tool enables differentiation between active biological pro-
cesses, such as metabolism, and passive ones, such as permeability and partitioning of a com-
pound from cell culture media into the cellular environment. This tool offers a significant
advancement over conventional approaches, which fail to explicitly consider passive biological
processes and conflate them into a singular clearance mechanism. By providing a more
detailed understanding of biological processes, our tool has the potential to reveal better
insights into liver-chip biology. Drug depletion kinetics of 32 compounds were taken from lit-
erature covering commercially available liver-on-chips (CnBio [13, 17], Javelin), and 3D
spheroids [18, 19], including fast and slow-cleared compounds. According to these studies,
DigiLoCs outperform the conventional prediction approach considerably. The impact of a
more accurate description of clinical clearance values on predicting human PK was investi-
gated in a proof-of-concept study using propranolol. The kinetics of propranolol was predicted
in humans using the conventional approach, DigiLoCs, and literature approach. The results
obtained from DigiLoCs for propranolol in the proof-of-concept study were much closer to
the actual observed human values than those of other approaches.

To the best knowledge of the authors, this is the first and biggest study so far, comparing
head-to-head the performance of different hepatic in vitro systems to predict human clearance
and demonstrating the impact OoC and MPS systems can have in the drug development pro-
cess, enhanced through the modelling and prediction features of DigiLoCs.

2 Methods

In this section, the following are described: i) data used in the study for predicting human
clearance, ii) DigiLocs, digital twin for liver-on-chip, iii) mathematical model, parameter esti-
mation and sensitivity analysis for DigiLocs, and iv) translation to humans and prediction of
human pharmacokinetics.

2.1 Data

In this work, published data on pharmacokinetics (metabolism) or toxicology studies of 32
drugs are used (See Table 1) to predict human pharmacokinetics.

2.2 Mathematical model

A typical single-compartment model is described as follows. Let C(t) be the drug concentration
in the chip at time t, V the volume of the chip, and CLc the clearance parameter. Then we have

dC
dt

¼ (cid:0)

CLc
V

� C;

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

3 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Table 1. Overview of literature reports providing on-chip pharmacokinetic information on compound clearance.

Study

Drugs Used in this study

Docci et al. 2022 [13]

Tsamandouras et al. 2017 [17]

Rajan et al. 2023 [20]

Kanebratt et al. 2021 [18]

Bonn et al. 2016 [19]

Total

9

6

12

4

8

38

9

3

8

4

8

32

https://doi.org/10.1371/journal.pone.0314083.t001

In vitro system
CnBio Liver-Chip

CnBio Liver-Chip

Javelin Liver-Chip

3D Spheroid (Hurel)

3D Spheroid (Hurel)

cell number [a.u.] Media volume [ml]

Flow

On-chip compartments

3E5

3E5

2.15E5

6E3

3E4

1.60

1.60

1.30

0.05

0.10

Recirculation

Recirculation

Recirculation

No

No

1

1

2

1

1

with initial value C(t = 0) = C0. The solution to this ODE is

CðtÞ ¼ C0 � e(cid:0) CLc

V

�t:

Taking the logarithm on both sides,

log CðtÞ ¼ (cid:0)

CLc
V

� t þ log C0;

ð1Þ

ð2Þ

which is equivalent to regression on log-transformed kinetic data.

A digital twin of liver-on-chip with three compartments that incorporate much more infor-
mation on parameters related to both on-chip characteristics and drug-specific properties was
developed. The three-compartment model considering media, interstitium and intracellular
compartment is described as follows: Let Cm(t), Ci(t), Cc(t) and Vm, Vi, Vc be the concentration
of the drug at time t, and volume of the media, interstitium, and intracellular compartment
respectively. CLc is the clearance parameter. Then we have

dCm
dt

¼ (cid:0)

k1
Vm

� Cm þ

k2
Vm

� Ci;

dCi
dt

¼

k1
Vi

� Cm (cid:0)

�

�

k2 þ k3
Vi

� Ci þ

k4
Vi

� Cc;

dCc
dt

¼

k3
Vc

� Ci (cid:0)

�

k4 þ CLc
Vc

�

� Cc:

The parameters here are defined as follows,

k1 ¼ Funbound � Pendothelial � SAmed int liver;

k2 ¼

k1
Kint med

;

k3 ¼ Kwater int � PAint cell and
k4 ¼ Kwater cell � PAcell int:

ð3Þ

ð4Þ

ð5Þ

ð6Þ

where Kint_med is the partition coefficient for the transfer of drug between the media and inter-
stitium, Pendothelial is the permeability coefficient of the drug between the endothelial layer,
SAmed_int_liver is the surface area of the interstitium, Kwater_cell is the partition coefficient for
water exchange or movement within the interstitium, Kwater_cell is the partition coefficient for
water exchange or movement within the intracellular compartment, PAcell_int is the product of
the surface area and permeability coefficient of the cellular membrane in the intracellular

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

4 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Table 2. Names and description of all relevant variables and parameters in the three-compartment digital twin.

Parameter

Description

Kint_med
Kwater_int
Kwater_cell
Pendothelial

Partition coefficient for the transfer of drug between the medium and interstitium

Partition coefficient for water exchange or movement within the interstitium

partition coefficient for water exchange or movement within the intracellular compartment

The rate of passive diffusion across the endothelial layer, which is the product of surface area and the permeability
coefficient of the drug

Permeability coefficient of the cellular membrane in the interstitium compartment

Permeability coefficient of the cellular membrane in the intracellular compartment

PAint_cell
PAcell_int
Funbound
SAmed_int_liver Surface area of the interstitium
CLc
Variables

Intrinsic on-chip clearance

Fraction unbound (medium, reference value)

Unit

Status

dimensionless calculated

dimensionless calculated

dimensionless calculated

cm/min

estimated

mL/min

mL/min

calculated

calculated

dimensionless calculated
cm2
mL/min

calculated

estimated

Cm
Ci
Cc

Concentration of the drug in the media compartment

Concentration of the drug in the interstitium compartment

Concentration of the drug in the intracellular compartment

https://doi.org/10.1371/journal.pone.0314083.t002

μmol/mL
μmol/mL
μmol/mL

simulated

simulated

simulated

compartment, PAint_cell is the product of the surface area and permeability coefficient of the
cellular membrane in the interstitium compartment and Funbound is the fraction unbound
(media, reference value). All the relevant variables and parameters with descriptions are given
in Table 2.

We can write this system of linear ODEs in matrix form,

C0 ¼ A � C; where

(cid:0)

k1
Vm

k2
Vm

2

A ¼

6
6
6
6
6
6
6
6
6
4

k1
Vi

0

�

�

(cid:0)

k2 þ k3
Vi

0

k4
Vi

k3
Vc

�

�

(cid:0)

k4 þ CLc
Vi

The general solution for the system of ODEs at time t is:

CðtÞ ¼ eA�t ¼ eX�Lt�X(cid:0) 1 � C0 ¼ X � eLt � X(cid:0) 1 � C0;

3

7
7
7
7
7
7
7
7
7
5

:

ð7Þ

ð8Þ

where X is the matrix of eigenvectors of A, Λ is the diagonal matrix with λ1, λ2, λ3 (eigenvalues
of A) as diagonal entries, and C0 is the initial value of variables at time 0.

The objective function for optimisation is as follows:

minimise
CLc

Xn

i¼1

ðyiobs

(cid:0) yia

Þ2

8
><

>:

¼ eA�ti � C0

yia
computed using eigenvalues

and eigenvectors;

where yiobs
is the number of observed data points.

is the observed data point and yia

is the computed value at time i respectively and n

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

5 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

2.3 DigiLoCs: Digital twins for cell-based liver assays

DigiLoCs is a software tool, developed within this work that describes the on-chip complex
biology more accurately in the context of use to predict clinical clearance values. The software
comprises (Fig 1):

• modelling of complex biological processes (clearance, permeability, partitioning),

• hardware-specific information from the studied in vitro system and

• compound-specific information.

The tool differentiates between active biological processes, such as metabolism, and passive
ones, like permeability and partitioning of a compound from cell culture media into the cellu-
lar milieu. This contrasts with conventional approaches, where passive biological processes are
not considered especially and lumped together into a single process, i.e., clearance.

Liver-on-chip technology provides a more physiologically relevant environment compared
to traditional cell cultures or animal models, enhancing the simulation of drug responses using
mathematical models. Hence, a more accurate mathematical description is needed. The three
primary compartments of the liver chip considered in the model are media, interstitium, and
intracellular space, which serve as dynamic environments where drugs are distributed, meta-
bolised, and interact with hepatic cells. This compartmentalisation is based on concepts
applied in human whole-body PBPK modelling.

The software tool is developed in the open-source programming language R [21] and seam-

lessly communicates with PK-Sim (https://www.open-systems-pharmacology.org/) via in-
house developed functions. For more information, see esqlabsR package (https://github.com/
esqLABS/esqlabsR). All analysis and plotting were also done in R. The proposed workflow
does not interfere with existing wet lab Standard Operating Procedures (SOPs) for performing
biological experiments and does not add an extra considerable burden to the user. DigiLoCs
uses existing biological data, and its performance may be improved by measuring cell-associ-
ated compound concentrations in addition to the compound media depletion time course,

Fig 1. Digital Twin (DT) approach. Contrasting conventional approach, the DT approach uses biological, hardware, and physicochemical information
to map the biological processes on liver-chip more accurately to in silico, thereby maximising the information leveraged. This results in the
disentanglement of active (metabolism) and passive (permeability, partitioning) processes. Created with biorender.com.

https://doi.org/10.1371/journal.pone.0314083.g001

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

6 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

which would add a minor extra step in the lab SOP. This, however, is negligible given the
improvement in performance power and the confidence in the prediction.

2.3.1 Implementation of hardware specifications. DigiLoCs map the chip architecture

to a compartmental model to describe the time-dependent distribution of a compound on-
chip. The compartment models use time-dependent ordinary differential equations (ODEs)
and assume well-mixing within compartments. These are generally accepted to describe the
distribution of exogenous and endogenous compounds and molecules.

A physical chamber separated by a membrane or connected by flow to another chamber is
represented by a compartment in the software. Serial compartments are connected via media
flow rates (typically in ml/min) between the compartments describing mass transport via gra-
dients and diffusion and normalised by the volume of the originating compartment.

2.3.2 Implementation of biological specifications. The biology (more precisely, the cell
type exerting the biological function under investigation; here: metabolism) is mapped by two
additional compartments representing the interstitial and intracellular space of the investi-
gated biology (Fig 1). Transport rates from the cell culture media into the interstitial and intra-
cellular milieu are described by two core processes:

• passive diffusion (driven by concentration gradients between compartments)

• thermodynamic equilibrium (distribution of compound between two phases)

These processes are then described by two main parameters in the computational model:
permeability (how fast is a compound taken up?) and partitioning (how much of the compound
is taken up by cells?). Lastly, the metabolism rate is reallocated to the intracellular compartment
and corrected by the unbound fraction of the compound in the intracellular compartment. Sim-
ilarly, in pharmacokinetics, the distribution of compounds is often described using a compart-
mental framework, which involves dividing a system into distinct compartments and modelling
the processes that govern the movement of compounds between them.

2.3.3 Implementation of compound-specific information. The following physicochemi-
cal properties of the investigated compounds are used in the software: i) lipophilicity (logP), ii)
molecular weight (MW) and iii)fraction unbound (fu); to calculate up to six dependent down-
stream parameters (listed below). These parameters describe the partitioning from the main
media compartment into the interstitial space and between the water fraction and both inter-
stitial and intracellular space. Additionally, permeability across the endothelial barrier and
between interstitial and intracellular spaces are calculated.

Partitioning: i) Kint_med ii) Kwater_cell iii) Kwater_cell

Permeability: i) Pendothelial ii) PAcell_int iii) PAint_cell

Here int refers to interstitial space, med refers to media, water refers to water exchange frac-
tion, and cell refers to intracellular space. These parameters are calculated based on well-estab-
lished and documented equations implemented in PK-Sim software [3], which is a
comprehensive software tool for whole-body PBPK modelling. It enables rapid access to all rel-
evant anatomical and physiological parameters for humans and common laboratory animals
contained in the integrated database for model building and parameterisation. The same parti-
tion coefficient calculation methods as implemented in PK-Sim are also readily available and
can be investigated:

• PK-Sim standard

• Poulin and Theil

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

7 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

• Rodgers and Rowland

• Schmitt

• Berezhkovskiy

Further, only the unbound fraction of a compound can be taken up by cells and be metabo-
lised by cells. The unbound fraction in the cell culture media is typically informed by biological
experiments. However, the intracellular unbound fraction is not often available or measured.
Thus, two established QSAR models (quantitative structure-activity relationship) are imple-
mented in the software to predict the unbound intracellular fraction of the investigated com-
pound as a function of its physicochemical properties [22, 23].

2.4 Parameter estimation

Parameter estimation aims to find unknown parameters in a computational model and is esti-
mated using experimental data collected from well-defined and standard conditions. By mini-
mising the distance of theoretical function values and experimentally known data, the set of
parameters in the model can be estimated. The parameters which are not directly measurable
can be estimated using least squares or any other fitting methods to analyse the model quanti-
tatively. Nominal parameter values are obtained from PK-Sim software.

Parameter estimation in DigiLoCs is a two-step process. Firstly, a customised cost function
is implemented. This cost function calculates the weighted difference (ssq) between the model
simulation (pred) from a specific compartment and the corresponding observed data (obs) for
each time point according to the equation

ssq ¼

obs (cid:0) pred
pred

:

ð9Þ

Common parameter estimation methods include maximum likelihood estimation and
Nelder Mead optimisation. Nelder Mead, a non-linear optimisation method, is used to find
the minima of the objective function in this work. Additionally, the partition coefficient
between the intracellular (IC) and the main media compartment is estimated using the area
under the simulated time-concentration profile of the IC and interstitial (IST) compartment
and corrected for by the QSAR-predicted cellular unbound fraction (fucell) and the unbound
fraction in the media (measured, fumedia):

Kpuu;pred ¼

AUCðIST þ ICÞ
AUCðmediaÞ

�

fucell
fumedia

:

ð10Þ

Kpuu,obs is calculated from literature [24], where media and intracellular concentrations in
hepatocytes were determined. Initially investigated for suspension hepatocytes in a 2D setting,
the authors provide a scaling factor (*4.9) to apply to human hepatocytes. Further, the ionisa-
tion state of the investigated compound (-1, 0, 1) results in a different partitioning. Otherwise,
a range of possible partition coefficients are investigated. This is an additional anchor point for
estimating the cost function value and links the simulated intracellular and main media com-
partment concentrations. Eventually, both differences are squared and summed up, resulting
in the final sum of residuals. Based on this, a compound-specific scaling factor (SF) is

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

8 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

calculated and used to scale the predicted human clearance:

SFðdrugÞ ¼

Kpuu;obs
Kpuu;pred

:

ð11Þ

Specifically for the liver use cases, on-chip liver clearance and surface area between the
main media compartment and the cell layer are estimated. It is possible to estimate other
parameters, such as pre-calculated permeability or partition coefficient values.

2.4.1 Implementation of software. Methodologically, DigiLoCs is implemented in the
open-source programming environment R with its own package. A library of two common
chip architectures and two cell types with six different chip-specific settings have already been
implemented.

1. One chamber, no media flow

2. Two chamber, recirculating flow

3. Organ-on-chip (hepatocytes)

a. CnBio

b. Hurel 1

c. Hurel 2

d. Dynamic42

e. Javelin

The most straightforward system is a single, perfused microfluidic chamber containing one

kind of cultured cell (e.g., hepatocytes) that exhibits functions of one tissue type linked to
channels for fluid transport. In more complex designs, two or more microchannels are con-
nected by porous membranes, lined on opposite sides by different cell types, to recreate inter-
faces between different tissues. The CnBio and Javelin chip settings are shown in Fig 2. For
detailed information on the processes and modelling, readers are directed to Bhatia et al. [25].
These building blocks can be interchangeably used and connected, similar to the building
blocks in PK-Sim. While the package provides a step-by-step guide to generate and run a sim-
ulation, the code communicates seamlessly with a generic PK-Sim model to determine parti-
tioning and permeability values as described above, which are used in the simulation.

2.5 Sensitivity analysis

Both local and global sensitivity analyses are used to quantify the impact of input parameters
on the output variables. This involves varying certain input parameters and observing changes
in the output variable intracellular concentration. The local sensitivity is estimated by chang-
ing one input parameter at a time while other parameters are held constant. The study pro-
vides insights into the sensitivity of various parameters and how they affect the output of the
model.

The input parameters Kint_med, Pendothelial, SAmed_int_liver, Kwater_int, Kwater_cell, PAcell_int,
PAint_cell, fu and CLc are varied to evaluate the sensitivity of the output variable intracellular
concentration (Cc). First, the local sensitivity is estimated by changing one input parameter by
10% at a time while the other parameters are held constant, and the changes in output variable
Cc are compared. Eq 12 shows the local sensitivity index for Cc with respect to the varying

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

9 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Fig 2. Chip 1 is for CnBio [13] and 3D spheroids [28] and chip 2 is for Javelin [20] architectures. Qmix is the mixing flow rate in mL/min. Created
with biorender.com.

https://doi.org/10.1371/journal.pone.0314083.g002

model parameter (Pi), which is approximated by a small perturbation ΔPi,

dCc
dPi

¼ lim
DPi!þ0

CcðPi þ DPi; Pn6¼iÞ (cid:0) CcðPiÞ
DPi

;

ð12Þ

where Cc(P) is the model prediction of the intracellular concentration for parameter set P. The
local sensitivity index is normalised to eliminate the effect of units,

Si ¼

dCc
dPi

Pi
CcðPÞ

:

ð13Þ

Global sensitivity analysis evaluates the effect of potential interactions of the input parame-

ters in an output variable. The Sobol sensitivity analysis of the SALib package in Python is
used to perform the global sensitivity analysis. Input parameters are sampled using the Saltelli
sampler. The lower and upper bound of the parameters are set as 0.1-fold and 10-fold of the
baseline parameter values, respectively. The first-order and total-order indices are estimated
using the Sobol sensitivity analysis.

2.6 Translation to humans

Drug-related parameters extracted from OoC or any other in vitro studies can be scaled to pre-
dict clinical parameters using in vitro-in vivo translation (IVIVT) [13, 17]. The typical value of
unbound intrinsic clearance CLint(u) determined for each drug from the pharmacokinetic anal-
ysis of the in vitro depletion data is scaled up to a human liver equivalent unbound intrinsic
clearance CLint(u),(H) using

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

CLintðuÞ;H ¼

CLintðuÞ;H � HC � LW
fuinc

;

ð14Þ

10 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

where HC is the human hepatocellularity of 120 million cells / g of liver, LW is the average
human liver weight of 25.7g / kg of body weight [17] and fuinc is the unbound fraction of drug
in the incubation medium. The hepatic clearance (referring to whole blood concentrations) is
then predicted (CLH,pred) using the Well-Stirred (WS) model:

CLHðpred; WSÞ ¼

QH � fub � CLintðuÞ;H
QH þ fub � CLintðuÞ;H

;

ð15Þ

where QH is the average hepatic blood flow of 20.7 mL/min/kg of body weight and fub is the
fraction of the drug unbound in blood. The fraction unbound in the blood was calculated for
each compound from the known fraction unbound in the media (fup) and blood-to-plasma
ratio (Rbp) according to the equation fup = fup/Rbp or directly used, if available from the liter-
ature. The predicted hepatic clearance (CLH,pred) values were then compared to observed
hepatic clearance (CLH,obs) values (referring to whole blood concentrations). Following, the
ratio of predicted (either via conventional or digital twin approach) and observed clinical
clearance values for all investigated compounds was calculated. Using these ratios, a density
distribution function was computed (function geom_density from ggplot [26]) for visual pur-
poses only.

2.7 Prediction of human pharmacokinetics

Initially, a PBPK model is developed using qualified installations of the software PK-Sim that
ensures the software has been installed correctly and thoroughly validated according to estab-
lished procedures. A whole-body PBPK model includes an explicit representation of the
organs most relevant to the uptake, distribution, excretion, and metabolism of the drug. These
typically include the heart, lungs, brain, stomach, spleen, pancreas, intestine, liver, kidney,
gonads, thymus, adipose tissue, muscles, bones, and skin. More information can be found in
S1 File.

The tissues are interconnected by arterial and venous blood compartments, and each is
characterised by an associated blood flow rate, volume, tissue partition coefficient, and perme-
ability. If applicable, R (Distribution 4.0) and RStudio (Version 1.2.5) are used in the analysis
for preprocessing and post-processing of data and model outputs [27]. The analytical approach
is based on the principles set out in the EMA, FDA, and/or OECD guidelines for reporting on
PBK M&S [11]. The developed PBPK model is used to describe the human kinetics of propran-
olol. Key kinetic parameters are informed by either clinical data, literature values or on-chip
predictions. The translational workflow that integrates organ-on-chip results to predict
human pharmacokinetics is shown in Fig 3.

3 Results

We report the following results in this section. First, results from a simulation model based on
a digital twin for selected compounds; second, sensitivity analyses; third, prediction of human
clearance values; and finally, translation to human PK using propranolol as a proof-of-concept
study. The liver clearance and surface area of the chip are estimated after fitting the drug
kinetic data. The Poulin and Theil method of partition coefficient calculation was used due to
its superior fit to observed drug kinetics, which outperformed alternative methods.

3.1 Simulating on-chip compound depletion

The digital twins for the investigated in vitro liver systems were successfully implemented in R
and used to simulate the on-chip kinetics. After parameter estimation, the resulting model

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

11 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Fig 3. Translational workflow plan that integrates results from organ-on-chip with computer modelling to predict the kinetics of drugs in
humans. The digital twins of the humanised organ-on-chip systems, together with chip-specific information and physicochemical information,
are developed in R. Created with biorender.com.

https://doi.org/10.1371/journal.pone.0314083.g003

simulations describing the observed compound depletion data were visually inspected. The
final parameter values can be found in Tables A and B in S1 File. Additionally, the squared
sum of residuals was evaluated and deemed acceptable as it was less than < 0.01, which was
the case for all simulations (data not shown). An example of on-chip kinetics is presented in
Fig 4.

As can be seen, the digital twin approach (violet line) captures the on-chip kinetics (blue
dots) very well. Simultaneously, the intracellular (IC) kinetics are plotted (red lines), clearly
highlighting the difference in compound uptake and, thus, clearance rates. The remaining fig-
ures are presented in S1 File (See Figs A-D).

3.2 Sensitivity analysis

The sensitivity analysis, both local and global, was conducted to quantify the sensitivity of
model output intracellular concentration with input parameters. The analyses were performed
for various parameters, and the results indicated that the output is more sensitive to parame-
ters such as the permeability coefficient of the endothelial layer, surface area of the liver sinu-
soids, and clearance. These parameters were estimated or calculated from clinical data/
experimental results. Clearance (CLc) is identified as the most sensitive parameter with respect
to intracellular concentration. The results imply that accurate values of these sensitive parame-
ters are crucial for the model’s accuracy.

The normalized local sensitivity indices (Fig 5a) and the first-order and total-order global
sensitivity indices (Fig 5b) for intracellular concentration across the input parameter set are

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

12 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Fig 4. Digital twin-based model simulation of on-chip kinetics after fitting parameters for selected compounds. Observed data are shown in blue
dots, where the data for diclofenac, midazolam, and oxazepam are from Docci et al. [13], while propranolol is from Tsamandouras et al. [17]. The red,
violet and green curve plots the drug concentration in the intracellular, medium and interstitium compartments, respectively: IC = intracellular,
Ist = interstitium.

https://doi.org/10.1371/journal.pone.0314083.g004

shown. The results from both local and global sensitivity analyses show that the output is more
sensitive to parameters Pendothelial, SApls_int_liver, fu and CLc. SApls_int_liver and CLc were esti-
mated and nominal values were used for all other parameters. SA results imply that we need
correct values of the constants Pendothelial, fu as they are more sensitive.

3.3 Predicting human clearance

The on-chip estimated clearance values were translated to total human clearance according to
Eq 15. More detailed information is available in S1 File (see Tables A and B). Likewise, from
the investigated studies (Table 1), in vitro unbound clearance values were available and scaled
to human equivalents.

The conventional approach is a single-compartment model explained in Section 2.2 using a

single ODE. The ratio of clinical observed human clearance values and either predicted
human clearances using conventional mathematical modelling or the digital twin approach
were estimated and converted into a density function for easier graphical visualisation as
described in Section 2.6. As can be seen in Fig 6, the digital twin approach (DigiLoCs) outper-
forms the conventional approach considerably. The centre of the distribution is around 1,
indicating a non-biased prediction of clinical clearance values, while the width of the distribu-
tion is very small. Quantitatively, the ratio for the digital twin approach overall compounds is
1.04 ± 0.31, with a coefficient of variation of 30%. In contrast, the conventional approach (red
curve) majorly under-predicts the clearance values while maintaining a broad distribution and
thereby adding to uncertainty in the prediction (0.56 ± 0.44, CV = 79.3%). The correlation plot
between the observed and herein predicted clinical clearance values highlights the improved
prediction performance of the DigiLoCs approach on an individual drug level. As can be seen
in Fig 7 (example graph for CnBio Liver-on-Chip data), most of the compounds fall within the
1.5-fold line (Average fold error, AFE = 0.965). Similar correlation plots are presented in the
S1 File (See Figs E-G) for the other in vitro systems.

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

13 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Fig 5. Local and global sensitivity of the parameters with respect to output intracellular concentration. (a) Blue bars indicate that the output and
the input changes in the same direction, and the red bar indicates that the output decreases when the input increases. (b) The blue and orange bars
represent first-order and total-order indices, respectively.

https://doi.org/10.1371/journal.pone.0314083.g005

3.4 Translation to human PK

The impact of accurately predicting human clearance values based on in vitro cell-based assays
on predicting human PK was assessed using propranolol as a proof-of-concept case study.
First, a human PBPK model describing the human kinetics of propranolol was implemented
in PK-Sim and qualified with clinical observations. Next, the predicted human clearance value
using either the conventional modelling approach or based on the same on-chip kinetic data
was implemented in the human PBPK model simulating the kinetics after a single oral dose.
Further, a population of n = 1000 patients was simulated to account for inter-patient variabil-
ity. As shown in Fig 5, the implemented human PBPK model describes observed clinical data
well (using clinical clearance values). When substituting only the clearance value with the con-
ventional or the digital twin-based values, the impact on simulating human PK becomes
apparent, while the conventional approach would overpredict (i.e., the on-chip clearance is
underpredicted) the human PK (3-fold Cmax, up to 6-fold overprediction of AUC). Moreover,

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

14 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Fig 6. Impact of DigiLoCs on predicting clinical clearance values compared to the conventional approach. In total, a set of 32 compounds across
three different in vitro liver systems have been investigated. The x-axis presents the ratio of predicted/observed clinical clearance values using either the
DigiLoCs or the conventional approach, and the y-axis shows the frequency of the ratio observed.

https://doi.org/10.1371/journal.pone.0314083.g006

this approach would actually simulate non-negligible concentrations of propranolol left over
after 24 h. For repeated daily dosing, this would result in accumulation of propranolol in this
hypothetical setting, which would have immediate implications for potential toxicity or effi-
cacy considerations. On the other hand, the digital-twin based approach still slightly overpre-
dicts the AUC and Cmax, however only by 1.5-fold and captures the terminal phase correctly.

4 Discussion

The aim of this work is to improve the current prediction of human clearance values and to
present a framework for translating in vitro findings to relevant clinical situations. The pre-
sented integrated translational approach combined quantitative OoC and cell-based assay
compound depletion kinetics with an OoC-digital twin to simulate drug kinetics in humans.

Initial investigations revealed the potential to describe clinical clearance values more appro-

priately than is currently possible with the conventional approach. This simpler approach
lumps biological processes together into a single process—clearance—and uses only minimal
information available, e.g., only the cell number and media volume. While biological systems
have evolved rapidly in the last decade, especially in the field of organ-on-chip and

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

15 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Fig 7. Correlation between observed and predicted in vivo intrinsic clearance (CLint) using the three-compartment liver chip for 12 drugs (Docci
et al. 2022; Tsamandouras et al. 2017). The solid line shows the line of unity, while the dotted line is 1.5-fold, and the dashed line has a 3-fold deviation.

https://doi.org/10.1371/journal.pone.0314083.g007

microphysiological systems, the applied mathematical models to analyse the quantitative com-
plex biological data have been the same for decades (the early concept of clearance was intro-
duced by Mo¨llers in 1928, while Well-stirred model was introduced in 1971).

In contrast, the digital twin approach for the organ-on-chip and 3D spheroids comprises
three building blocks described here: biological, hardware, and physicochemical information.
The distinction between active and passive processes is achieved by an explicit description of
uptake, distribution, and metabolism involved in the biological processes. Further, the digital
twin links the architecture of the hardware chip with an advanced mapping of the underlying
biology (intracellular compartment). The on-chip kinetics for 32 compounds (six compounds
were removed from the initial set due to missing information) was well described, highlighting
the drug-specific effects on cellular uptake and hence metabolism. Note that this analysis used
the same biological information as used in the conventional approach and that no additional

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

16 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Fig 8. Simulated kinetics of propranolol after a single oral dose (80 mg). Pink dots are clinical observations
(digitised from Borgstro¨m et al. [29]), while the blue solid line represents the mean of the patient population using the
clinical observed clearance value. When using the clearance value (red line) based on conventional approaches, the
area under the curve is 6-fold overpredicted. In contrast, using the digital twin-based clearance, the AUC is only
1.5-fold overpredicted, also simulating the right kinetics at 24 h (black curve). Shaded areas represent ± 1 SD.

https://doi.org/10.1371/journal.pone.0314083.g008

biological experiments were needed or performed to improve the outcome of the digital twin
approach.

The predictive power of organ-on-chip and 3D spheroids over conventional approaches
was revealed when the depletion data was analysed with the digital twins (Fig 6). Not only was
the systematic underprediction issue resolved, but the uncertainty in prediction was also
reduced by a factor of 3 (comparing CVs).

Lastly, we aimed to demonstrate the clinical impact of this approach by translating the
results to humans using propranolol as a proof-of-concept example. Here, the head-to-head
comparison clearly demonstrated the superior power of both quantitative biological data from
OoCs and digital twins over conventional approaches in predicting human PK more appropri-
ately (Fig 8). Although only one compound was used to demonstrate clinical impact, the work-
flow and process are easily applicable to other compounds. To the best of our knowledge, this
study is the biggest comprehensive report to systematically assess the predictive power of
organ-on-chip in the context of use of liver clearance.

The mathematical algorithm to determine liver clearance depends on the time-concentra-

tion profiles and, if available, on intracellular or cell-associated compound concentrations.
The algorithm minimises a cost function by identifying a clearance value such that model pre-
diction and data observation match. The cost function takes both the PK profile from cell cul-
ture media and the cell-associated levels into account, which is not the case for the
conventional approach. Further, binding of the compound to plastic/hardware of the chips, to
proteins contained in the cell culture media, or any other intracellular lipids can be accounted
for to accurately determine liver clearance. DigiLocs, further, also does not depend on a scaling
factor, which overcomes the systematic underprediction of conventional approaches (5–10
fold on average across multiple studies).

So far, limited information is available from the literature or in-house measurements on the

observed partitioning of compounds into the intracellular or cell-associated milieu of hepato-
cytes. If that data becomes available, it may be incorporated compared to the adjustments

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

17 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

made in the software to match the clinical clearance values. If the predicted and observed Kpuu
values match, the digital twin approach truly improves the prediction. If there is a discrepancy
between these values, the fitting process can be re-run including the observed Kpuu value. This
would inform the maximum capacity of the system to metabolise the compound. If this final
rate is still lower than the observed clinical clearance value, two options are possible to under-
stand and improve the prediction:

1. Calculate a correction factor, which is compound-specific and chip-specific and not generic

like in the conventional approaches.

2. Investigate other model-specific parameters to optimise, e.g., permeability or partitioning.

Although initially developed for hepatic clearance, the mathematical model can be

employed for toxicity or efficacy-related questions depending on the context of use. In such a
setting, time-concentration profiles will be simulated and linked to other measured biomark-
ers (e.g., ATP (adenosine triphosphate), TEER (barrier integrity)) to determine IC50 or EC50
values, and parameters to assess toxicity and efficacy, respectively. Likewise, the same integra-
tion of complex biological processes, hardware-, and drug-specific information can be used to
model other cell and chip types, e.g., a blood-brain-barrier-chip, which is used to determine
the permeability of compounds across the barrier.

Eventually, we envision DigiLoCs to support the pharmaceutical decision-making process

by reducing animal testing and ultimately streamlining the drug development process.

5 Conclusion

The development of digital twins for organ-on-chips, reported here, incorporating systems of
differential equations-based models and leveraging published data, holds great potential to
enhance our understanding of drug behaviour and clinical outcomes. The in vitro liver clear-
ance for 32 drugs was predicted using DigiLoCs and a proof-of-concept (translation to human
pharmacokinetics) study on propranolol was done. DigiLoCs are envisioned to serve as a deci-
sion-support tool for pharmaceutical research, aiding in estimating first-in-human doses, eval-
uating human pharmacokinetics, and importantly, diminishing reliance on animal
experimentation, thereby fostering more efficient, expedited, and sustainable drug develop-
ment processes. Our approach is generalisable across various physiological contexts and not
limited to liver metabolism but may be extended to other organs as well, such as gut metabo-
lism and barrier models such as the brain or placenta.

Supporting information

S1 File. SUPPLEMENTARY INFORMATION FOR DigiLoCS: A leap forward in predictive
organ-on-chip simulations.
(PDF)

Author Contributions

Conceptualization: Christian Maass.

Data curation: Manoja Rajalakshmi Aravindakshan, Christian Maass.

Formal analysis: Christian Maass.

Investigation: Christian Maass.

Methodology: Manoja Rajalakshmi Aravindakshan, Chittaranjan Mandal, Christian Maass.

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

18 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

Software: Manoja Rajalakshmi Aravindakshan, Christian Maass.

Supervision: Chittaranjan Mandal, Alex Pothen, Christian Maass.

Visualization: Manoja Rajalakshmi Aravindakshan, Christian Maass.

Writing – original draft: Manoja Rajalakshmi Aravindakshan, Christian Maass.

Writing – review & editing: Manoja Rajalakshmi Aravindakshan, Chittaranjan Mandal, Alex

Pothen, Stephan Schaller, Christian Maass.

References
1.

Franzen N, van Harten WH, Retèl VP, Loskill P, van den Eijnden-van Raaij J, IJzerman M. Impact of
organ-on-a-chip technology on pharmaceutical R&D costs. Drug Discovery Today. 2019; 24(9):1720–
1724. https://doi.org/10.1016/j.drudis.2019.06.003 PMID: 31185290

2. Denayer T, Sto¨ hr T, Roy MV. Animal models in translational medicine: validation and prediction. Euro-

pean Journal of Molecular & Clinical Medicine. 2014; 2(1):5. https://doi.org/10.1016/j.nhtm.2014.08.001

3.

4.

Thelen K, Coboeken K, Willmann S, Burghaus R, Dressman JB, Lippert J. Evolution of a detailed physi-
ological model to simulate the gastrointestinal transit and absorption process in humans, part 1: oral
solutions. Journal of Pharmaceutical Sciences. 2011; 100(12):5324–5345. https://doi.org/10.1002/jps.
22726 PMID: 21993815

Jones H, Chen Y, Gibson C, Heimbach T, Parrott N, Peters S, et al. Physiologically based pharmacoki-
netic modelling in drug discovery and development: a pharmaceutical industry perspective. Clinical
Pharmacology & Therapeutics. 2015; 97(3):247–262. https://doi.org/10.1002/cpt.37 PMID: 25670209

5. Obach RS. Prediction of human clearance of twenty-nine drugs from hepatic microsomal intrinsic clear-
ance data: an examination of in vitro half-life approach and nonspecific binding to microsomes. Drug
Metabolism and Disposition. 1999; 27(11):1350–1359. PMID: 10534321

6. Brown HS, Griffin M, Houston JB. Evaluation of cryopreserved human hepatocytes as an alternative in
vitro system to microsomes for the prediction of metabolic clearance. Drug Metabolism and Disposition.
2006; 35(2):293–301. https://doi.org/10.1124/dmd.106.011569 PMID: 17132764

7. Reddy MB, Mccarley KD, Bunge AL. Physiologically relevant one-compartment pharmacokinetic mod-
els for skin. 2. comparison of models when combined with a systemic pharmacokinetic model. Journal
of Pharmaceutical Sciences. 1998; 87(4):482–490. https://doi.org/10.1021/js9702877 PMID: 9548902

8. Murata Y, Neuhoff S, Rostami-Hodjegan A, Takita H, Al-Majdoub ZM, Ogungbenro K. In vitro to in vivo
extrapolation linked to physiologically based pharmacokinetic models for assessing the brain drug dis-
position. The AAPS Journal. 2022; 24(1).

9. Hallifax D, Foster JA, Houston JB. Prediction of human metabolic clearance from in vitro systems: Ret-
rospective analysis and prospective view. Pharmaceutical Research. 2010; 27(10):2150–2161. https://
doi.org/10.1007/s11095-010-0218-3 PMID: 20661765

10. Shroff T, Aina K, Maass C, Cipriano M, Lambrecht J, Tacke F, et al. Studying metabolism with multi-

organ chips: new tools for disease modelling, pharmacokinetics and pharmacodynamics. Open Biology.
2022; 12(3). https://doi.org/10.1098/rsob.210333 PMID: 35232251

11. European Medicines Agency. Guideline on the investigation of drug interactions; 2012. https://www.

ema.europa.eu/en/documents/scientific-guideline/guideline-investigation-drug-interactions-revision-1_
en.pdf.

12. Maass C, Stokes CL, Griffith LG, Cirit M. Multi-functional scaling methodology for translational pharma-
cokinetic and pharmacodynamic applications using integrated microphysiological systems (MPS). Inte-
grative Biology. 2017; 9(4):290–302. https://doi.org/10.1039/c6ib00243a PMID: 28267162

13. Docci L, Milani N, Ramp T, Romeo AA, Godoy P, Franyuti DO, et al. Exploration and application of a
liver-on-a-chip device in combination with modelling and simulation for quantitative drug metabolism
studies. Lab on a Chip. 2022; 22(6):1187–1205. https://doi.org/10.1039/D1LC01161H PMID: 35107462

14.

Fowler S, Chen WLK, Duignan DB, Gupta A, Hariparsad N, Kenny JR, et al. Microphysiological systems
for ADME-related applications: current status and recommendations for system development and char-
acterization. Lab on a Chip. 2020; 20(3):446–467. https://doi.org/10.1039/C9LC00857H PMID:
31932816

15. Maass C, Sorensen NB, Himmelfarb J, Kelly EJ, Stokes CL, Cirit M. Translational assessment of drug-

induced proximal tubule injury using a kidney microphysiological system. CPT: Pharmacometrics &
Systems Pharmacology. 2019; 8(5):316–325. https://doi.org/10.1002/psp4.12400 PMID: 30869201

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

19 / 20

PLOS ONEDigiLoCs: Enhancing predictive liver clearance models

16. Herland A, Maoz BM, Das D, Somayaji MR, Prantil-Baun R, Novak R, et al. Quantitative prediction of
human pharmacokinetic responses to drugs via fluidically coupled vascularized organ chips. Nature
Biomedical Engineering. 2020; 4(4):421–436. https://doi.org/10.1038/s41551-019-0498-9 PMID:
31988459

17.

Tsamandouras N, Kostrzewski T, Stokes CL, Griffith LG, Hughes DJ, Cirit M. Quantitative assessment
of population variability in hepatic drug metabolism using a perfused three-dimensional human liver
microphysiological system. Journal of Pharmacology and Experimental Therapeutics. 2016; 360(1):95–
105. https://doi.org/10.1124/jpet.116.237495 PMID: 27760784

18. Kanebratt KP, Janefeldt A, Vile´n L, Vildhede A, Samuelsson K, Milton L, et al. Primary human hepato-

cyte spheroid model as a 3D in vitro platform for metabolism studies. Journal of Pharmaceutical Sci-
ences. 2021; 110(1):422–431. https://doi.org/10.1016/j.xphs.2020.10.043 PMID: 33122050

19. Bonn B, Svanberg P, Janefeldt A, Hultman I, Grime K. Determination of human hepatocyte intrinsic

clearance for slowly metabolized compounds: comparison of a primary hepatocyte/stromal cell co-cul-
ture with plated primary hepatocytes and HepaRG. Drug Metabolism and Disposition. 2016; 44(4):527–
533. https://doi.org/10.1124/dmd.115.067769 PMID: 26851239

20. Rajan SAP, Sherfey J, Ohri S, Nichols L, Smith JT, Parekh P, et al. A novel milli-fluidic liver tissue chip

with continuous recirculation for predictive pharmacokinetics applications. The AAPS Journal. 2023; 25
(6). https://doi.org/10.1208/s12248-023-00870-x PMID: 37891356

21. R Core Team. R: A language and environment for statistical computing; 2021. Available from: https://

www.R-project.org/.

22. Poulin P, Haddad S. Hepatocyte composition-based model as a mechanistic tool for predicting the cell
suspension: aqueous phase partition coefficient of drugs in in vitro metabolic studies. Journal of Phar-
maceutical Sciences. 2013; 102(8):2806–2818. https://doi.org/10.1002/jps.23602 PMID: 23670739

23. Austin RP, Barton P, Mohmed S, Riley RJ. The binding of drugs to hepatocytes and its relationship to

physiochemical properties. Drug Metabolism and Disposition. 2004; 33(3):419–425. https://doi.org/10.
1124/dmd.104.002436 PMID: 15616151

24. Mateus A, Matsson P, Artursson P. Rapid measurement of intracellular unbound drug concentrations.
Molecular Pharmaceutics. 2013; 10(6):2467–2478. https://doi.org/10.1021/mp4000822 PMID:
23631740

25. Bhatia SN, Ingber DE. Microfluidic organs-on-chips. Nat Biotechnol. 2014; 32(8):760–772. https://doi.

org/10.1038/nbt.2989 PMID: 25093883

26. Wickham H. Ggplot2. 2nd ed. Use R!. Cham, Switzerland: Springer International Publishing; 2016.

27. Kuepfer L, Niederalt C, Wendl T, Schlender J, Willmann S, Lippert J, et al. Applied concepts in PBPK

modelling: how to build a PBPK/PD model. CPT: Pharmacometrics & Systems Pharmacology. 2016; 5
(10):516–531. https://doi.org/10.1002/psp4.12134 PMID: 27653238

28. Rodrigues AV, Alexandre-Pires G, Vale´rio-Bolas A, Santos-Mateus D, Rafael-Fernandes M, Pereira

MA, et al. 3D-hepatocyte culture applied to parasitology: immune activation of canine hepatic spheroids
exposed to leishmania infantum. Biomedicines. 2020; 8(12):628. https://doi.org/10.3390/
biomedicines8120628 PMID: 33352885

29. Borgstro¨ m L, Johansson CG, Larsson H, Lenander R. Pharmacokinetics of propranolol. Journal of

Pharmacokinetics and Biopharmaceutics. 1981; 9(4):419–429. https://doi.org/10.1007/BF01060886
PMID: 7310641

PLOS ONE | https://doi.org/10.1371/journal.pone.0314083 January 9, 2025

20 / 20

PLOS ONE
