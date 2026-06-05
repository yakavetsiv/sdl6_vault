---
type: literature-note
source_note: "Papers/Paper - Wu,-Tianyi-2025-02-08-Self-driving-lab-for-the-photochemical-synthesis-of-plasmoni.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Wu,-Tianyi-2025-02-08-Self-driving-lab-for-the-photochemical-synthesis-of-plasmonic-nanoparticles-with-targeted-structural-and-optical-properties.pdf"
converter: "microsoft/markitdown"
---
Article

https://doi.org/10.1038/s41467-025-56788-9

Self-driving lab for the photochemical
synthesis of plasmonic nanoparticles with
targeted structural and optical properties

Received: 23 December 2023

Accepted: 31 January 2025

Check for updates

;
,
:
)
(

0
9
8
7
6
5
4
3
2
1

;
,
:
)
(

0
9
8
7
6
5
4
3
2
1

Tianyi Wu 1, Sina Kheiri
Zhi-Bo Yang5, Xin Ge6, Wei Zhang 6, Milad Abolhasani
Alan Aspuru-Guzik 1,3,4,8,9,10,11 & Eugenia Kumacheva 1,10,11,12

2, Riley J. Hickman1,3,4, Huachen Tao1, Tony C. Wu1,3,

7, Kun Liu 5,

Many applications of plasmonic nanoparticles require precise control of their
optical properties that are governed by nanoparticle dimensions, shape,
morphology and composition. Finding reaction conditions for the synthesis of
nanoparticles with targeted characteristics is a time-consuming and resource-
intensive trial-and-error process, however closed-loop nanoparticle synthesis
enables the accelerated exploration of large chemical spaces without human
intervention. Here, we introduce the Autonomous Fluidic Identiﬁcation and
Optimization Nanochemistry (AFION) self-driving lab that integrates a micro-
ﬂuidic reactor, in-ﬂow spectroscopic nanoparticle characterization, and
machine learning for the exploration and optimization of the multi-
dimensional chemical space for the photochemical synthesis of plasmonic
nanoparticles. By targeting spectroscopic nanoparticle properties, the AFION
lab identiﬁes reaction conditions for the synthesis of different types of nano-
particles with designated shapes, morphologies, and compositions. Data
analysis provides insight into the role of reaction conditions for the synthesis
of the targeted nanoparticle type. This work shows that the AFION lab is an
effective exploration platform for on-demand synthesis of plasmonic
nanoparticles.

Applications of inorganic nanoparticles (NPs) in chemical and biolo-
gical sensing1,2, photovoltaics3,4, imaging5, and drug delivery6 are lar-
gely governed by their optical properties. The identiﬁcation of the
multidimensional chemical space for the synthesis of NPs with pre-
cisely controlled characteristics is a challenge, since the rate of reagent

addition and mixing, reagent concentration, and reaction time and
temperature are interdependent and synergistic. A small disturbance
in these conditions can signiﬁcantly change NP properties. Further-
more, with every additional reaction condition, the size of the chemical
the identiﬁcation of key
space exponentially increases7. Thus,

1Department of Chemistry, University of Toronto, Toronto, ON M5S 3H6, Canada. 2Department of Mechanical and Industrial Engineering, University of Toronto,
Toronto, ON M5S 3G8, Canada. 3Department of Computer Science, University of Toronto, Toronto, ON M5S 3H6, Canada. 4Vector Institute for Artiﬁcial
Intelligence, Toronto, ON M5S 1M1, Canada. 5State Key Laboratory of Supramolecular Structure and Materials, College of Chemistry, Jilin University,
Changchun 130012, P. R. China. 6School of Materials Science & Engineering, Electron Microscopy Center, Jilin University Changchun 130012, P. R. China.
7Department of Chemical and Biomolecular Engineering, North Carolina State University, Raleigh, NC 27606, USA. 8Department of Materials Science &
Engineering, University of Toronto, Toronto, ON M5S 3E4, Canada. 9Canadian Institute for Advanced Research (CIFAR), Toronto, ON M5S 1M1, Canada.
10Department of Chemical Engineering and Applied Chemistry, University of Toronto, Toronto, ON M5S 3E5, Canada. 11Acceleration Consortium, University of
Toronto, Toronto, ON M5S 3H6, Canada. 12Institute of Biomaterials and Biomedical Engineering, University of Toronto, Toronto, ON M5S 3G9, Canada.

e-mail: eugenia.kumacheva@utoronto.ca

Nature Communications |

 (2025) 16:1473

1

Article

https://doi.org/10.1038/s41467-025-56788-9

parameters controlling NP properties through experience-based
manual trial-and-error experiments is a time-, labor-, and resource-
intensive task.

reagent

The use of self-driving labs (SDLs) that operate in a “closed-loop”
manner with minimal human intervention emerged as a promising
strategy for addressing this challenge. These labs operate via iterative
NP syntheses by integrating automation, e.g., robotics or microﬂuidics
(MFs), NP characterization, and machine learning (ML)8,9. Automation
enables control over
injection, mixing, heating, and
separation10,11. In particular, MFs offers ﬂow-controlled reagent supply,
enhanced mass and heat
transfer, and real-time online NP
characterization12–14 which provides rapid data acquisition13,15. Despite
the advantages of automation, the decision on the next-step syntheses
for identiﬁcation of the most effective NP reaction conditions remains
in the hands of the operator. Here, ML algorithms play a pivotal role in
inferring relationships between reaction conditions and correspond-
ing NP properties, thereby recommending experimental conditions
for subsequent optimization steps without examining the entire che-
mical space16. Application of ML algorithms in SDLs include the stable
noisy optimization by branch and ﬁt algorithm (SNOBFIT)17, covariance
matrix adaptation evolution strategy (CMA-ES)18, genetic algorithm19,
and Bayesian optimization (BO)20–25.

Starting from the introduction of an SDL for the synthesis of CdSe
NPs26, automated ML-assisted synthesis was extended to other NP
types18–20,22–33. For the synthesis of plasmonic NPs, SDLs operated by
targeting characteristic absorption spectra. For instance, a high-
throughput SDL for the synthesis of silver (Ag) triangular nanopr-
isms targeted their full absorption spectra and used BO with deep
neural network to minimize the loss function22. This approach did not
utilize the knowledge of speciﬁc spectroscopic NP properties such as
plasmon resonance peak wavelength or full width at half maximum
(FWHM) and was sensitive to the presence of impurities and noise. An
alternative approach utilized well-established knowledge about
essential spectroscopic characteristics of NPs, which were used as
objectives in their ML-guided synthesis. For instance, in the SDL per-
forming seeded synthesis of gold (Au) nanospheres, rods, and octa-
hedrons, an evolutionary genetic algorithm was used to optimize a
ﬁtness function for the selected areas under the plasmon peak28.
Recently, an ensemble neural network was utilized for the synthesis of
lead halide perovskite NPs by optimizing a pre-assigned weight func-
tion to ﬂuorescence emission intensity and FWHM31. While the second
approach is more efﬁcient, it poses a challenge in selecting appropriate
weights to multiple objectives34. The use of a hierarchical algorithm
would obviate the need to assign appropriate individual weights to
each objective and would focus on their hierarchical importance. More
speciﬁcally, the secondary objective would not be fulﬁlled if it causes a
degradation in the objective that is higher in the hierarchy. This
strategy was used in our earlier proof of concept work which utilized a
Gryfﬁn algorithm35 for the SDL-based synthesis of Au nanospheres by
targeting in an order of importance the wavelength of their plasmon
resonance, FWHM, and absorbance intensity23.

Seeded SDL-based synthesis of plasmonic NPs has been
achieved by either introducing pre-synthesized NP seeds into the
SDLs as one of the reagents22,25,30, or by synthesizing NP seeds in the
SDLs with a complicated design and subsequently using them in the
next-step reaction19,28, however seedless photochemical synthesis in
SDLs has not been reported. Although in comparison with conven-
tional synthesis of plasmonic NPs, their photochemical synthesis
offers mild reaction conditions, temporal reaction control, and
adaptability with MF synthesis36–38, it remains underused due to the
inherent sensitivity of the reaction output to irradiation intensity and
exposure time39. This challenge is compounded in seedless NP
synthesis, where the concurrent nucleation and growth processes
demand precise control over reaction conditions. These complica-
tions make seedless photochemical syntheses of a variety of

plasmonic NPs with precise control of their optical properties and in
high yield a synthetic challenge.

Here, we report a ML-assisted seedless photochemical synthesis
of plasmonic NPs by utilizing an autonomous ﬂuidic identiﬁcation
and optimization nanochemistry (AFION) SDL. We selected NP
spectroscopic properties as the output for ML-guided multi-objec-
tive experimental planning. The rationale in this selection was driven
by the variation of the wavelength of surface plasmon resonance
(SPR) bands with NP size and shape40, a narrower full width at half-
maximum of the SPR peak for more uniform NP size distribution41,
and a stronger intensity of SPR with higher yield of NP synthesis42. By
targeting the distinct spectroscopic NP characteristics and subse-
quently adjusting chemically intuitive hierarchical objectives the
AFION lab synthesized on-demand eight types of NPs, including Au
nanorods with two tailored shapes, spherical alloy AuAg NPs with
two selected compositions, spherical Au/Ag NPs with a core-shell
morphology, spherical Ag and Cu NPs, and Au tetrapods. For each NP
type, the AFION lab traversed a multidimensional parameter chemi-
cal space and identiﬁed the optimal conditions within 30 or fewer
experiments conducted in 30 h or less. Complementary to spectro-
scopic NP characteristics, their properties were validated by trans-
mission electron microscopy (TEM) imaging and energy-dispersive
X-ray (EDS) elemental analysis.

The developed AFION platform is an SDL designed for the pho-
tochemical synthesis of inorganic nanomaterials.
It enables on-
demand synthesis of different types of plasmonic NPs within the
same platform, thus, eliminating the need for the hardware and soft-
ware redesign for each NP type. Furthermore, through multi-objective
optimization it provides key insights into the role of the combination
of multiple reaction parameters on a speciﬁc NP characteristic, which
stimulates further comprehensive studies of reaction mechanisms.

Results
Closed-loop synthesis in the AFION lab
Figure 1a shows the workﬂow of the ML-assisted synthesis of plas-
monic NPs in the AFION lab. For a particular type of NPs, their spec-
troscopic properties were selected using existing literature data and
used as objectives (targets) in a closed-loop iterative photochemical
synthesis. The closed-loop operation embodied the execution of a ML-
selected experiment, the collection of experimental data, the updates
of a ML model, and the determination of the subsequent set of
experimental conditions for next iteration. More speciﬁcally, following
the synthesis conducted under seven-parameter reaction conditions
(step 1), the spectroscopic NP properties were acquired online (step 2)
and reported to a ML algorithm Gryfﬁn35 with a scalarizing function,
Chimera43 for hierarchy-based multi-objective optimization (step 3).
Gryfﬁn was trained on the reaction conditions/spectroscopic property
pairs to propose a new set of reaction conditions for the next-iteration
synthesis (step 4). The details of optimization are provided in “Meth-
ods” section. The fully autonomous closed-loop process operated
without human intervention, reaching convergence when the NP
spectroscopic properties met the designated targets and were not
enhanced in subsequent syntheses. The desired NP characteristics
were validated using TEM, EDS mapping, and EDS line scans,
respectively.

The experimental setup is illustrated in Fig. 1b. Individual reagent
solutions were supplied to the MF reactor to form a slug of the mixed
reagent solution, which oscillated back and forth in the tube reactor,
while being exposed to ultraviolet (UV) irradiation. The varying seven
reaction conditions included the concentration of four reagents,
reaction time, UV light intensity, and slug oscillation speed (controlling
reagent mixing)44. Upon reaction completion, the NP-containing slug
moved to a ﬂow cell for the spectroscopic NP characterization and
subsequently, was discharged to the waste container or sample col-
lection reservoir. The spectroscopic data were analyzed and reported

Nature Communications |

 (2025) 16:1473

2

Article

a

Selection of NPs to be synthesized

b

Selection of spectroscopic targets for the NPs

Close-loop synthesis

Step 1: Photochemical
synthesis

Step 2: Online spectroscopic
characterization

4

6

8

5

9

7

3

2

1

hv

n
o

i
t
c
n

i
t
x
E

Wavelength (nm)

Steps 3 & 4
output

Step 4: New experimental
proposal

Step 3: Algorithm

surrogate model update

Steps 1 & 2

input

Next experiment

Validation of the NP shape, morphology and
composition

https://doi.org/10.1038/s41467-025-56788-9

)
.

u

.

b
r
a
(

n
o

i
t
c
n

i
t
x
E

)
.

u

.

b
r
a
(

n
o

i
t
c
n

i
t
x
E

)
.
u

.

b
r
a
(

n
o

i
t
c
n

i
t
x
E

)
.

u
.
b
r
a
(

n
o
i
t
c
n
i
t
x
E

Au nanorod

c

1

0.8

0.6

0.4

0.2

0

400

500

600

700

800

900

1000

Wavelength (nm)

Alloy AuAg
nanosphere

1

0.8

0.6

0.4

0.2

0

400

500

600

700

800

900

1000

Wavelength (nm)

Core-shell Au/Ag
nanosphere

400

500

600

700

800

900

1000

Wavelength (nm)

Au tetrapod

1

0.8

0.6

0.4

0.2

0

1

0.8

0.6

0.4

0.2

0

400

500

600

700

800

900

1000

Wavelength (nm)

Fig. 1 | Closed-loop photochemical NP synthesis in the AFION lab. a Workﬂow of
the synthesis of plasmonic NPs in the AFION lab. Created in BioRender. Kheiri, S.
(2025) https://BioRender.com/w89i187. b Schematic of the AFION lab. The lab
includes (1) reservoirs with reagent solutions, (2) a pump dispenser to generate a
slug of reagent solution, (3) an oscillator pump, (4) a UV light source with adjustable
height, (5) ﬂow cell for optical NP characterization, (6) tungsten halogen UV light
source, (7) an in-line, ﬁber-optics, charge-coupled spectrometer, (8) a reservoir for
the collection of waste, and (9) a reservoir for NP collection for further

characterization. Created in BioRender. Kheiri, S. (2025) https://BioRender.com/
n80b990. c Illustrated literature-based characteristic extinction spectra of selected
plasmonic NPs: AuNRs with the solid and dashed lines corresponding to their high-
and low-aspect ratios, respectively; alloy AuAg NSs with the solid and dashed lines
representing high and low mole fraction of Au, respectively; core-shell Au/Ag NS;
and Au tetrapod. The shaded regions show the SPR peaks targeted in the closed-
loop synthesis.

to Gryfﬁn to obtain a new experimental proposal (steps 3 and 4). The
details of closed-loop NP synthesis are provided in the “Methods”.

The AFION lab was developed by matching spectroscopic NP
properties with NP shapes, dimensions, and compositions: Au nanor-
ods (AuNRs) with two different aspect ratios, alloy AuAg nanospheres
(AuAg NSs) with two different compositions, core-shell Au/Ag NSs, and
Au tetrapods NPs. Figure 1c illustrates the literature-based extinction
spectra of these NP types45–49. The shaded areas correspond to the SPR
bands that were targeted in the NP synthesis. The explored chemical
spaces are detailed in Supplementary Tables 1–5 for AuNRs, alloy NSs,
core-shell NSs, and Au tetrapods NPs.

regions corresponded to the reported LSPR and transverse SPR of
AuNRs51,52. The LSPR peak in the 650–1000 nm spectral range depends
on the AuNR aspect ratio (as it red-shifts with increasing AuNR aspect
ratio), while the peak in the 490–560 nm region corresponds to both
the SPR of spherical Au NPs (by-products) and the transverse SPR of
AuNRs, however the latter peak is only weakly sensitive to the variation
in the AuNR aspect ratio52. Thus, the value of AUC1000(cid:1)650 represents
the AuNR population, while the value of AUC560(cid:1)490 is largely governed
by the by-product. To synthesize a large population of AuNRs
(irrespective of their aspect ratio), a boundary limit of R ≥ 3.0 was set
as a target.

Synthesis of AuNRs
The AFION lab synthesized AuNRs with “high” and “low” aspect ratios
with the corresponding values of 4.1 and 3.0 and longitudinal SPR
(LSPR) of 880 and 750 nm, respectively45,46. The aspect ratio was
deﬁned as the ratio of the length to the diameter of AuNRs50. The
following four spectroscopic targets of AuNRs were identiﬁed in order
of decreasing importance:

Objective 1. The ratio (R) is deﬁned as the area under the peak in
the 650–1000 nm spectral region over the area under the peak in the
490–560 nm range, that is:

Objective 2. The spectral position of the LSPR peak (λ

LSPR) was
Target = 880 nm for the AuNRs with “high” aspect ratio of
Target = 750 nm for the AuNRs with “low” aspect ratio of 3.046.
j) was set to be

aimed to be λ
4.145, and λ
The deviation between λ
no more than 10 nm.

LSPR and λ

Target (jλ

(cid:1) λ

Target

LSPR

Objective 3. The FWHM of the LSPR band was minimized to syn-
thesize AuNRs with a uniform size distribution. A relative tolerance of
40% was used for Chimera, allowing speciﬁc deviation of the objective
value with respect to the full range of observed value:

FWHMtolerance = FWHMmin + 40% × ðFWHMmax

(cid:1)FWHMmin

Þ

ð2Þ

R =

AUC1000(cid:1)650
AUC560(cid:1)490

ð1Þ

where FWHMmin and FWHMmax represent the minimum and maximum
FWHM values, respectively, satisfying higher importance objec-
tives 1 and 2.

where AUC denotes the “area under the curve”, and the subscripts
refer to the designated spectral ranges. The selection of spectral

Objective 4. Since the extinction intensity at 400 nm (I400) linearly
correlates with the total NP concentration in the solution (including

Nature Communications |

 (2025) 16:1473

3

Article

https://doi.org/10.1038/s41467-025-56788-9

a

R

c

)

m
n
(

M
H
W
F

e

)
.
u
.
b
r
a
(
n
o
i
t
c
n
i
t
x
E

0.25

0.20

0.15

0.10

0.05

0.00

Second objective

First objective

b

)

m
n
(

|
0
8
8

λ

–

R
P
S
L

λ
|

Second objective

First objective

g

R

h

)

m
n
(

|
0
5
7

λ

–

R
P
S
L

λ
|

Experiment

Experiment

Experiment

Experiment

Third objective

Experiment

Fourth objective

Experiment

d

R

I

f

Third objective

Experiment

j

R

I

l

Fourth objective

Experiment

i

)

m
n
(

M
H
W
F

k

)
.
u
.
b
r
a
(
n
o
i
t
c
n
i
t
x
E

0.12

0.09

0.06

0.03

0.00

400

600

800

1000

Wavelength (nm)

400

800
600
Wavelength (nm)

1000

Fig. 2 | Properties of “high” and “low” aspect ratio AuNRs synthesized using ML-
recommended iterative synthesis. a Variation R value for high aspect ratio AuNRs,
plotted as a function of the number of experiments. The shaded red area corre-
sponds to targeted R ≥ 3.0 (objective 1). b Changes in |λ
The shaded yellow area corresponds to | λ
c Variation in optimized FWHM of the LSPR of the high aspect ratio AuNRs. The
shaded area gives FWHM values lower than 40% threshold (objective 3). d Variation
in IR in high aspect ratio AuNR synthesis. The increase in the color intensity in the
gradient shaded area corresponds increasing IR values (objective 4). e Extinction
spectrum of high aspect ratio AuNRs in experiment #23. f Representative TEM

– λ
880 | ≤ 10 nm (objective 2).

880| of the AuNRs.

– λ

LSPR

LSPR

by-products)42, the highest ratio (IR) of the LSPR peak intensity (ILSPR)
to that at 400 nm was targeted toward the synthesis of AuNRs
(objective 1) with high yield, while maintaining their desired aspect
ratio (objective 2) and narrow size distribution (objective 3). We use
the equation

IR =

ILSPR
I400

ð3Þ

where ILSPR is the intensity of the LSPR peak at the designated wave-
length corresponding to the aspect ratio of the AuNRs, and I400 is the
extinction intensity at 400 nm.

880

LSPR

(cid:1)λ

Figure 2a–d shows the variation in four designated characteristics
of high aspect ratio AuNRs during iterative syntheses, that is, R ≥ 3.0,
j ≤ 10 nm, minimized FWHM of the LSPR peak, and max-
jλ
imized IR, respectively. Figure 2a–c shows that objective 1 was met in
j was
experiment #1, however the tolerated deviation jλ
j
(cid:1)λ
exceeded. Iterative syntheses led to a steady approach of jλ
880
to objective 2 and the reduction in FWHM (objective 3), with both
objectives being met in experiment #23. Although experiment #15 led

(cid:1)λ

LSPR

LSPR

880

image of high aspect ratio AuNRs as in (e). g–j Variation in spectroscopic properties
of low aspect ratio AuNRs as in (a–d), plotted vs. the number of conducted
syntheses. The shaded areas correspond to the targeted characteristics, that is, (g),
R ≥ 3.0 (objective 1); h |λ
values (objective 3); j maximized IR values (objective 4). k Extinction spectrum of
low aspect ratio AuNRs synthesized in experiment #23. l Representative TEM image
of low aspect ratio AuNRs as in (k). The scale bars (f) and (l) are 50 nm. In the graphs
a–d and g–j, each data point shows an optimized spectroscopic characteristic for
each experiment. Source data are provided as a Source Data ﬁle.

750 | ≤ 10 nm (objective 2); i minimized FWHM

– λ

LSPR

to the highest IR value (Fig. 2d), the FWHM value in this experiment
failed to satisfy the tolerance for objective 3. Thus, all objectives were
met in experiment #23, with R = 10.9, λ
LSPR = 880 nm, FWHM = 185
nm, and IR = 3.17 (compromised), with no further improvement
achieved in AuNR properties in subsequent experiments. Supple-
mentary Table 6 details reaction conditions of experiment #23.
Figure 2e, f shows the corresponding spectrum and the representa-
tive TEM image of the high aspect ratio AuNRs (Supplementary
Fig. 1a shows larger AuNR populations). Analysis of TEM images
revealed that the content of spherical NPs was <7%, and the AuNRs
had an average aspect ratio of 3.9 ± 0.4 (Supplementary Fig. 1b–d),
similar to the AuNRs synthesized by seeded conventional synthesis
and close to the target value of 4.145.
The AuNRs with low aspect ratio were synthesized by targeting
(cid:1)
(cid:1)
(cid:1) ≤ 10 nm, minimized FWHM, and the maximum IR
(cid:1)
R ≥ 3.0, λ
value (Fig. 2g–j). In experiment #23, all objectives were met, with
R = 5.47, λ
LSPR = 757 nm, FWHM = 186 nm, and IR = 1.98. No improve-
ment occurred in further experiments. The corresponding spectrum
and TEM images of the AuNRs are shown in Fig. 2k, l, respectively.
Supplementary Table 6 provides reaction conditions for experiment

(cid:1)λ

LSPR

750

Nature Communications |

 (2025) 16:1473

4

Article

https://doi.org/10.1038/s41467-025-56788-9

a

)

m
n
(

|
5
6
4

λ

–

R
P
S

λ
|

j

)

m
n
(

|
5
8
4

λ

–

R
P
S

λ
|

First objective

b

Second objective

c

Third objective

)

m
n
(

M
H
W
F

)
.
u

.
b
r
a
(
R
P
S

I

Experiment

Experiment

Experiment

e

HAADF

f

gA

g

Au

h

yalrevO

First objective

k

)

m
n
(

M
H
W
F

Second objective

l

)
.

u

Third objective

.

b
r
a
(
R
P
S

I

Experiment

Experiment

Experiment

n

FDAAH

o

gA

p

uA

q

yalrevO

d

)
.
u
.
b
r
a
(

n
o
i
t
c
n
i
t
x
E

i

)
s
t
n
u
o
c
(

y
t
i
s
n
e
t
n
I

m

)
.
u
.

b
r
a
(

n
o

i
t
c
n

i
t
x
E

0.40

0.30

0.20

0.10

0.00

120

100

80

60

40

20

0

400

600

800

1000

Wavelength (nm)

Au
Ag

5

10

15

20

25

Position (nm)

0.30

0.20

0.10

0.00

400

600

800

1000

Wavelength (nm)

Au

Ag

0

5

10

15

20

Position (nm)

r

)
s
t
n
u
o
c
(

y
t
i
s
n
e
n

t

I

120

100

80

60

40

20

0

SPR

SPR

– λ

– λ

465|, plotted as a function of the number
Au. The shaded red area corresponds
465 | ≤ 5 nm (objective 1). b Variation in FWHM of the SPR of alloy NSs. The

Fig. 3 | Properties of alloy AuAg NSs synthesized using ML-recommended
iterative synthesis. a Variation in |λ
of experiments for alloy AuAg NSs with low χ
to |λ
shaded green area shows FWHM values lower than 20% threshold (objective 2).
c Variation in ISPR of alloy NSs. Increasing color intensity of the shaded yellow area
corresponds to maximized values of ISPR (objective 3). d Extinction spectrum of
alloy AuAg NSs with low χ
Au synthesized in experiment #27. Inset shows repre-
sentative TEM image of the corresponding NSs. e HAADF-STEM image of the alloy
NSs as in (d). f Elemental Ag STEM − EDS map of the NSs as in (e). g Elemental Au
STEM − EDS map of the NSs as in (e). h Overlay image of (f) and (g). i EDS line
proﬁles of alloy AuAg NSs with low χ
j–l Variation in spectroscopic properties as in (a–c) of alloy AuAg NSs with high χ

Au along the yellow dashed line (inset).

Au,

SPR

– λ

Au. The corre-

485 | ≤ 5 nm (objective 1, in red),

plotted vs. the number of syntheses of alloy AuAg NSs with high χ
sponding shaded areas show the targeted j |λ
k minimized FWHM values (objective 2, in green), l highest ISPR (objective 3, in
yellow). m Extinction spectrum of alloy AuAg NSs with high χ
Au, synthesized in
: n HAADF-
experiment #29. Inset shows representative alloy NPs with high χ
STEM image of the alloy AuAg NSs with high χ
STEM − EDS map of the NSs as in (n). p Elemental Au STEM − EDS map of the NSs as
in (n). q Overlay image of (o) and (p). r EDS line proﬁles of alloy AuAg NSs with high
χ
Au along the yellow dashed line (inset). Au and Ag are indicated as blue and red
lines, respectively. All scale bars are 10 nm. In the graphs a–c and j–l each data point
shows an optimized spectroscopic characteristic for each experiment. Source data
are provided as a Source Data ﬁle.

Au as in (m). o Elemental Ag

Au

#23. The AuNRs had an aspect ratio of 2.9 ± 0.4, with <5% spherical
impurities (Supplementary Fig. 1e–h), close to the AuNRs with aspect
ratio of 3.0 produced by seeded photochemical synthesis46. The
optimized formulations for AuNR syntheses contained ten-fold lower
CTAB concentration than that reported for the seeded photochemical
AuNR synthesis with similar size distribution and shape purity46.

Synthesis of alloy AuAg NSs
Photochemical synthesis of alloy AuAg NSs with “low” and “high” mole
fractions of Au (χ
Au) of 0.54 and 0.80, respectively, was conducted by
targeting the corresponding SPR positions, based on the literature
data for alloy NSs synthesized by conventional seedless synthesis47.
Three targeted characteristics for the synthesis of AuAg alloy NSs were
as follows:

Objective 1. The λ

Target was set to be 465 and 485 for alloy NSs with
SPR and

Au of 0.54 and 0.80, respectively. The deviation between λ
χ
λ
Target

jÞ was set to be no more than 5 nm.
Objective 2. The FWHM of the SPR band was minimized with 20%

(cid:1) λ

Target

ðjλ

SPR

relative tolerance without degrading objective 1:

FWHMtolerance = FWHMmin + 20% × ðFWHMmax

(cid:1)FWHMmin

Þ

ð4Þ

where FWHMmin and FWHMmax represent the minimum and maximum
experimental FWHM values, respectively.

Objective 3. The highest intensity of the SPR peak (ISPR) was tar-

geted to achieve high yield of alloy NSs53.

Figure 3a–c depicts the variation in three targeted characteristics
Au vs. the number of experiments, namely

of alloy AuAg NSs with low χ

Nature Communications |

 (2025) 16:1473

5

Article

https://doi.org/10.1038/s41467-025-56788-9

SPR

– λ

|λ
465|, minimized FWHM of the SPR peak, and the maximized ISPR,
respectively. All objectives were met in experiment #27, without fur-
ther improvement in the NS properties in the following syntheses. The
reaction conditions for experiment #27 are listed in Supplementary
Table 7. The corresponding extinction spectrum is shown in Fig. 3d
(λ
SPR = 467 nm, FWHM = 138 nm, and ISPR = 0.34), and the TEM images
of these NSs are displayed in Fig. 3d, inset and Supplementary Fig. 2a.
The average NS diameter was 13 ± 2.7 nm (Supplementary Fig. 2b).
Figure 3e–j shows high-angle annular dark-ﬁeld (HAADF)-STEM image,
the corresponding Ag and Au STEM-EDS maps, and the overlay of Au
and Ag maps of alloy NSs, respectively. The Au and Ag atoms were
homogeneously distributed in the alloy NSs. The determined χ
Au of
0.53 was close to the targeted value of 0.5447. The EDS line scans fur-
ther validated the uniform distribution of Au and Ag elements within
the NSs (Fig. 3i).

Au

SPR

Next, we synthesized alloy AuAg NSs with high χ
– λ

: Figure 3j–l
shows the variation in |λ
485|, FWHM of the SPR peak, and ISPR
values, respectively, in the iterative NS synthesis. The optimized
reaction conditions (experiment #29) are shown in Supplementary
Table 7. The corresponding NSs exhibited λ
SPR = 487 nm, FWHM = 123
nm, and ISPR = 0.20 (Fig. 3m) and had an average diameter of
16 ± 3.1 nm (Fig. 3m, inset and Supplementary Fig. 2c, d). Figure 3n–q
shows the HAADF-STEM image, the corresponding Ag and Au STEM-
EDS maps, and the overlay of Au and Ag maps for the NSs with high χ
Au,
respectively. The value of χ
Au = 0.8
reported for conventionally synthesized alloy NSs47. Figure 3r indicates
a uniform distribution of Au and Ag elements within the NSs.

Au was 0.76, close to the target of χ

Synthesis of core–shell Au/Ag NSs
For the synthesis of core–shell Au/Ag NSs, based on the reported
data48, the following targets were selected.

Objective 1. The area ratio (R) is deﬁned as:

R =

AUC440(cid:1)400 + AUC520(cid:1)480
AUC480(cid:1)440

ð5Þ

where AUC440(cid:1)400 represents the AUC in the range of 400–440 nm
(representing the SPR of the Ag shell), AUC520(cid:1)480 represents the AUC
in the range of 480–520 nm (representing the SPR of the Au core), and
the denominator is the AUC in the range of 440–480 nm. To ensure the
synthesis of core-shell Au/Ag NSs, a boundary limit of R ≥ 2.0 was set as
a target.

Objective 2. To synthesize core–shell Au/Ag NSs, the targeted
SPRs were 510 nm (Au core) and 415 nm (Ag shell), corresponding to
Au/Ag NSs with a 10 nm-diameter core and 3.4 nm-thick shell48. A root
mean squared error (RMSE) ﬁtness function was established to mini-
mize the deviation between the experimentally measured SPRs of the
Ag shell and Au core and their respective target values. The RMSE is
deﬁned as:

s

ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
(cid:1) 510Þ2
ðλ

(cid:1) 415Þ2 + ðλ

SPR, C

SPR, S

2

RMSE =

ð6Þ

SPR, S is an experimentally measured SPR peak of the Ag shell,
SPR, C is an experimentally measured SPR peak of the Au core. The

where λ
and λ
threshold was set to be less than 10 nm.

Objective 3. Minimized FWHM was targeted to achieve narrow
size distribution of the NSs. The challenge of overlapping SPR bands of
the Au core and Ag shell, was addressed by spectra deconvolution54 to
separate the peaks into their individual additive components. The sum
of FWHMs for both SPR bands, denoted as ΣFWHM, was selected with
20% threshold, expressed as:

ΣFWHMtolerance = ΣFWHMmin + 20% × ΣFWHMmax

(cid:4)

(cid:1) ΣFWHMmin

(cid:5)

ð7Þ

Where ΣFWHM is the sum of the FWHMs for the two SPR bands,
FWHMSPR, C and FWHMSPR, S, corresponding to the FWHM of the Au
core SPR bands and that of the Ag shell, respectively, and calculated as:

ΣFWHM = FWHMSPR, C + FWHMSPR, S

ð8Þ

Objective 4. To achieve high yield of core-shell NSs, the sum of the

SPR intensity, denoted as ΣInten, was maximized, as

ΣInten = ISPR, C + ISPR, S

ð9Þ

where ISPR, C represents the SPR intensity corresponding to the Au
cores, and ISPR, S represents the SPR intensity corresponding to the Ag
shells.

Figure 4a–d shows the variation in NS characteristics during
iterative synthesis toward the targets, that is, R ≥ 2.0, RMSE ≤ 10 nm,
minimized ΣFWHM, and the maximized ΣInten, respectively. All
objectives were met in experiment #25, with R = 2.31, RMSE = 5.1 nm at
SPR, S = 413 nm, and λ
SPR, C = 517 nm, ΣFWHM = 185 nm, and ΣInten =
λ
0.05. Supplementary Table 8 lists reaction conditions of experiment
#25. Figure 4e shows the corresponding NS extinction spectrum, while
Fig. 4e, inset and Supplementary Fig. 3 display the TEM images of the
core-shell NSs, with average diameter of 12 ± 1.9 nm, 11 nm-diameter
core and 2 nm-thick shell, close to the targeted dimensions48. The EDS
line scan conﬁrmed the Au core and Ag shell morphology (Fig. 4b).

Exploration of photochemical synthesis of Au tetrapods
NPs with a spiky morphology have speciﬁc spectroscopic properties
and have advantages in surface-enhanced Raman scattering spectro-
scopy, strong catalytic ability, increased photothermal absorption, and
a broad tunable wavelength range for biosensing applications55.
Nanopods, i.e., spiky NPs with a well-deﬁned number and size of
branches, present signiﬁcant synthesis challenges due to the precise
control required for symmetry breaking55. Synthesis of nanopods has
been achieved by conventional wet-chemical synthesis but not pho-
tochemical synthesis49,56. More speciﬁcally, tetrahedron-type nano-
pods, have been produced utilizing Au NSs as seeds57, or employing
various biological buffers58,59, Alternative geometries such as cross-
type planar Au tetrapods, have been synthesized using either Ag
nanoplates as seeds56, or diethylamine as a selective facet-hindering
capping agent in dimethylformamide solvent without the use of
seeds49.

Here we explored the seedless photochemical synthesis of Au
tetrapods in the AFION lab. To this end, we used the spectra reported
for the conventional wet-chemical synthesis as the target49. We tar-
geted high-intensity SPR band and a low-intensity shoulder in the
spectra, which were reported for the cross-type planar tetrapods with
an average diagonal arm length of 93 nm49. Note that while Au tetra-
pods and AuNRs show similar spectral features, the tetrapod synthesis
was explored in a different chemical space. A high reducing agent
concentration was used, due to the kinetically controlled tetrapod
synthesis process, favoring Au deposition rate against the Au diffusion
rate60. Secondly, a lower Ag precursor concentration was used, com-
pared to the AuNR synthesis. Four targeted spectroscopic optical
characteristics were as follows:

Objective 1: The area ratio (R) was set as R ≥ 1.0, expressed as

R =

AUC600(cid:1)1000
AUC500(cid:1)600

ð10Þ

where AUC600(cid:1)1000 represents the AUC in the 600–1000 nm spectral
range (signifying high-intensity SPR band) and AUC500(cid:1)600 represents
the area under the 500–600 nm shoulder (the low-intensity band).

Objective 2: The spectral position of the SPR peak (λ

SPR) was tar-
Target = 75 nm for the tetrapod with targeted diagonal

geted to be λ

Nature Communications |

 (2025) 16:1473

6

Article

https://doi.org/10.1038/s41467-025-56788-9

a

First objective

b

Second objective

c

Third objective

d

Fourth objective

R

E
S
M
R

)

m
n
(

M
H
W
F
Σ

n
e
t
n
I
Σ

Experiment

Experiment

Experiment

Experiment

e

0.04

)
.
u
.
b
r
a
(
n
o
i
t
c
n
i
t
x
E

0.03

0.02

0.01

0

400

600

800

1000

Wavelength (nm)

Fig. 4 | Properties of core-shell Au/Ag NSs synthesized using ML-recommended
iterative synthesis. a Variation in R, plotted as a function of the number of per-
formed experiments. The shaded area shows R ≥ 2.0 (objective 1). b Variation in
RMSE of the core–shell Au/Ag NSs in the iterative synthesis, with the shaded area
corresponding to RMSE ≤ 10 nm (objective 2). c Changes in ΣFWHM for the
core–shell Au/Ag NSs, plotted vs. the number of syntheses. The shaded area shows
ΣFWHM values lower than the 20% threshold (objective 3). d Variation in ΣInten of
the core–shell NSs, plotted vs. the number of experiments. The increase in color

length, based on ref. 49. The deviation between λ
(jλ

j) was set to be no more than 10 nm.

(cid:1) λ

SPR

Target

SPR and λ

Target

Objective 3: The FWHM of the SPR band was minimized to reach
tetrapod narrow size distribution with 40% threshold, as described in
Eq. (2).

Objective 4: To achieve a high yield in tetrapod synthesis, we
targeted the highest intensity ratio (IR) of the SPR intensity (ISPR) to
that at 400 nm (I400), while satisfying objectives 1–3. The follow-
ing equation was used

IR =

ISPR
I400

ð11Þ

SPR

(cid:1) λ

Figure 5a–d shows the variation in the targeted NP characteristics
750 | ≤
during iterative tetrapod synthesis, that is, R ≥ 1.0, |λ
10 nm, minimized FWHM, and maximized IR, respectively. All objec-
tives were met in experiment #28, with no further improvement in
subsequent syntheses. Supplementary Table 9 lists the reaction con-
ditions for experiment #28. Figure 5e shows the corresponding tetra-
pod spectrum, with R = 1.66, λ
SPR = 750 nm, FWHM = 169 nm, and
IR = 0.70. The TEM images (Fig. 5f and Supplementary Fig. 4a) show
tetrapods with four sharp tips with an average diagonal length of 89 ±
10 nm (Supplementary Fig. 4b), close to targeted diagonal length
of 93 nm49.

To compare the efﬁciencies of ML-assisted NP synthesis and
random search experiments, we conducted random search for the
slowest AFION lab’s campaign, that is, the synthesis of Au tetrapods,
the most challenging NP system requiring 28 experiments for multi-
objective optimization. Random search experiments were performed
within the same reaction parameter space as the ML-assisted synthesis
(Supplementary Table 10). The details and results of 30 random search
experiments are provided in Supplementary Fig. 5. Compared to ML-

Au

Ag

f

120

100

)
s
t
n
u
o
c
(

y
t
i
s
n
e
t
n
I

80

60

40

20

0

0

2

4

6
8
Position (nm)

10

12

14

16

intensity of the shaded area reﬂects maximized values of ΣInten (objective 4). In
a–d, each data point shows an optimized spectroscopic characteristic for each
experiment. e Extinction spectrum and the corresponding TEM image (inset) of
core–shell Au/Ag NSs synthesized in experiment #25. f EDS line proﬁles of the
cross-section of the NS as in (e) (shown along the yellow line in inset). The proﬁles
of Au and Ag are shown as blue and red lines, respectively. The scale bars shown in
e and f are 10 nm. Source data are provided as a Source Data ﬁle.

(cid:1)λ

assisted synthesis where all objectives were met at experiment #28,
j ≤ 10 nm) corresponding to the targeted tetra-
objective 2 (jλ
pod dimensions was never met within 30 random search experiments,
thus, underscoring the efﬁciency of the AFION lab in achieving multi-
objective optimization for the synthesis of plasmonic NPs.

SPR

750

tetrapod synthesis. To evaluate potential

Reproducibility and precision in the AFION lab
To evaluate the reproducibility of the AFION lab, we conducted
randomly selected experiments for the reaction parameter space
used for
cross-
contaminations between the experiments, three randomly selected
reaction conditions were repeated ﬁve times, each, with other ran-
domly selected experiments spread between the repetitions. The
exemplary scheme of the workﬂow is shown in Supplementary Fig. 6.
The observed small relative standard deviations for the repetitive
experiments did not exceed 0.6% for the SPR wavelength, 8.7% for
the FWHM, and 6.4% for the SPR peak intensity (Supplementary Fig. 7
and Supplementary Table 11), which conﬁrmed the independence of
each data point.

Furthermore, for all NPs synthesized in our work, we conducted
two repetitive consecutive experiments for the optimized reaction
conditions. The relative standard deviations for NP characteristics are
provided Supplementary Fig. 8 and Supplementary Table 12. In addi-
tion, to assess consistent AFION performance over time and reagent
stability, we acquired the spectra of AuNRs over 48-h synthesis with 6-h
intervals (Supplementary Fig. 9 and Supplementary Table 13). These
results collectively demonstrated the experimental precision of the
AFION lab.

Expanding universality of the AFION lab
By using different precursors and surfactants, we explored the cap-
ability of seedless photochemical synthesis of other types of

Nature Communications |

 (2025) 16:1473

7

Article

https://doi.org/10.1038/s41467-025-56788-9

a

First objective

b

Second objective

c

Third objective

d

Fourth objective

)

m
n
(

M
H
W
F

f

R

I

Experiment

Experiment

R

)

m
n
(

|
0
5
7

λ

–

R
P
S

λ
|

Experiment

Experiment

e

)
.

u

.

b
r
a
(

n
o

i
t
c
n

i
t
x
E

0.10

0.08

0.06

0.04

0.02

0.00

400

600

800

1000

Wavelength (nm)

Fig. 5 | Properties of Au tetrapods synthesized using ML-assisted iterative
synthesis. a Variation in R, plotted as a function of the number of experiments. The
shaded area corresponds to R ≥ 1.0 (objective 1). b Changes in |λ
tetrapods, with the shaded area corresponding to |λ
iterative synthesis (objective 2). c Variation in FWHM of the SPR of the tetrapods
during the course of synthesis. The shaded area gives FWHM values lower than 40%

750| for
750 | ≤ 10 nm, during

– λ

– λ

SPR

SPR

threshold (objective 3). d Variation in IR of the tetrapods, plotted vs. the number of
experiments. The increase in the color intensity in the shaded area corresponds to
increasing IR values (objective 4). In a–d, each data point shows an optimized
spectroscopic characteristic for each experiment. e Extinction spectrum of the
tetrapods synthesized in experiment #28. f Corresponding TEM image of the tet-
rapods. The scale bar is 50 nm. Source data are provided as a Source Data ﬁle.

plasmonic NPs, that is, Ag and Cu NSs, in the ML-searched six-dimen-
sional chemical space. The reaction parameters and targeted spec-
troscopic characteristics of these NPs are provided in Supplementary
Table 14, and the progression of iterative synthesis toward the targets
is shown in Supplementary Fig. 10. The optimized reaction conditions
(Supplementary Table 15) for the synthesis of Ag NSs were identiﬁed in
experiment #29. The NPs had average diameter of 28 ± 4 nm, which
was larger than 3.3 ± 0.4 nm diameter of Ag NSs synthesized in seed-
less batch (cuvette-based) photochemical synthesis61. The reaction
conditions for the synthesis of Cu NSs with 11.8 ± 2.0 nm in diameter
(Supplementary Table 15) were optimized in experiment #19. These
NPs were larger and had reduced dispersity in size, in comparison with
Cu NSs of 7.9 ± 3.5 nm in diameter synthesized by seedless batch
photochemical synthesis62. The Cu NSs were synthesized under
nitrogen atmosphere, highlighting the capability of the AFION plat-
form to perform oxygen-sensitive NP synthesis and expand its versa-
tility to chemically challenging scenarios.

Data analysis
To obtain insight into the relationship between reaction conditions
and the types of synthesized NPs, we utilized knowledge-governed and
data-driven approaches. In the former strategy, we selected three
parameters of the photochemical NP synthesis, which conventionally
reﬂect the energy harnessed by the photoreducing agent to generate
ketal radicals and reduce precursors, namely, the average UV light
intensity, reaction time, and the concentration of photoreducing agent
2-hydroxy-4′-(2-hydroxyethoxy)-2-methylpropiophenone, denoted as
[I-2959]. Figure 6a shows that AuNRs formed under longer reaction
time (5–20 min), low [I-2959] (<2 mM), and low UV light intensity
(11–25 mW cm−2), while Au tetrapods were synthesized within shorter
(5–12 min) reaction time, high [I-2959] (>8 mM), and high UV light
intensity (34–60 mW cm−2). Longer (>20 min) reaction times with
relatively low [I-2959] (<2 mM), and UV light intensity (<15 mW cm−2)
favored core–shell NS synthesis, while shorter reaction times
(2–5 mM), and high UV intensity
(<15 min), moderate [I-2959]
(20–50 mW cm−2) were preferred for the synthesis of alloy NSs.

The data-driven approach employed the mutual information sta-
tistics method63. In contrast to the knowledge-drive approach, it
highlighted the signiﬁcance of the concentration of silver nitrate,
denoted as [AgNO3], for the synthesized NP types. As shown in Fig. 6b,
AuNRs and Au tetrapods were produced at relatively low [AgNO3]
(<0.02 mM and <0.0001 mM,
respectively), whereas alloy and
core–shell NSs formed over a broad [AgNO3] range. The data-driven
analysis provided insight into reaction conditions governing the
synthesis of distinct NPs, surpassing conventional knowledge about
these reactions.

Discussion
By integrating ﬂuidic synthesis, real-time spectroscopic NP char-
acterization, and established hierarchy-based multi-objective ML-
governed optimization, we developed a ﬂuidic SDL for on-demand
seedless photochemical synthesis of a diverse range of plasmonic
NPs. The use of the AFION lab addresses the challenges inherent to
the photochemical NP synthesis such as the sensitivity of the
reaction product to irradiation intensity and exposure time, as well
as the complexities associated with seedless NP synthesis, which
involves concurrent nucleation and growth processes. As a result,
this work broadens the spectrum of synthetic techniques available
for SDLs. By targeting the intrinsic spectroscopic characteristics
reported for particular NP types, we have synthesized eight dif-
ferent types of NPs, including AuNRs with two tailored shapes,
alloy AuAg NSs with two selected compositions, Au/Ag NSs with a
core-shell morphology, Ag and Cu NSs, and Au tetrapods. The
ofﬂine analysis conﬁrmed that these NPs were synthesized with
pre-selected shapes, morphologies, and compositions, which
highlighted the effectiveness of the AFION lab in the synthesis of
plasmonic NPs on demand. The shape purity, dimensions, and size
distribution of the NPs synthesized were comparable with those of
NPs produced by the optimized time-consuming conventional
syntheses. In addition, using ML guidance, we proposed reaction
conditions for Au tetrapods, whose seedless photochemical ﬂuidic
synthesis has not been reported.

Nature Communications |

 (2025) 16:1473

8

Article

a

https://doi.org/10.1038/s41467-025-56788-9

)
2
-

m
c
W
m

(

y
t
i
s
n
e
t
n

i

V
U

b

)
2
-

m
c
W
m

(

y
t
i
s
n
e
t
n

i

V
U

AuNRs

AuAg alloy NSs

Au/Ag core-shell NSs

Au tetrapods

Fig. 6 | Data analysis of the photochemical synthesis of NPs. a 3D knowledge-
driven correlation graph representing the relationship of the UV light intensity, the
concentration of the photoreducing agent [I-2959], and the reaction time. b 3D
data-driven correlation graph, representing the relationship between the

concentrations of the precursor ([AgNO3]), the photoreducing agent [I-2959], and
the UV light intensity. In a, b, the NPs are shown as follows: AuNRs (purple inverted
triangles), alloy NSs (green circles), core-shell NSs (red squares), and Au tetrapods
(blue crosses). Source data are provided as a Source Data ﬁle.

We evaluated performance metrics of the AFION lab as follows64:
(i) Degree of autonomy: Close-looped NP synthesis in the AFION
platform required no human intervention during the goal-
seeking process beyond the preparation of reagent solutions.
Importantly, a ﬂuidic droplet-based reactor for NP synthesis was
integrated with an online spectroscopic characterization
module;

(ii) Operational lifetime: The AFION platform demonstrated an
unassisted lifetime of 2 days (primarily limited by precursor
degradation), which included approximately 80–100 reactions.
Beyond this limitation, the platform could run continuously
without stopping;

(iv)

(iii) Throughput: The AFION platform achieved an average
throughput of 2–3 samples per hour, which was governed by the
intrinsic reaction time for a particular NP type. In fact, the
oscillatory ﬂuidic synthesis could decrease reaction duration.
For example, in the case of AuNRs, the reaction time was
reduced from 30 min65 (batch photochemical synthesis of these
NPs) to within 20 min in the AFION lab with uniform size
dispersity;
Experimental precision and reproducibility: The consistency of
the repetitive randomly selected experiments that were spread
within other experiments between the repetitions was con-
ﬁrmed for the tetrapod synthesis. The low values of the relative
standard deviations underscored the effectiveness of the
washing protocol and data independence. Similarly, low rela-
tive standard deviations for the characteristics of all NPs syn-
thesized in consecutive repetitive experiments conﬁrmed the
precision of the AFION platform. Reagent stability tests con-
ducted for AuNR synthesis for 48-h also yielded low relative
standard deviations, further validating the platform’s robust
performance.

(v) Material usage: The AFION platform utilized small amounts
in total, across 265

for each reagent

(0.005–0.06 g)
experiments.

(vi) Optimization efﬁciency: To compare the efﬁciency of the ML-
assisted NP synthesis against the random search approach, we
conducted random search for the slowest AFION lab’s cam-
paign, that is, the synthesis of Au tetrapods, the most

challenging NP system requiring 28 experiments for multi-
objective optimization. After 30 experiments, random search
failed to meet all objectives for tetrapod characteristics, thus,
underscoring the efﬁciency of AFION lab in achieving multi-
objective synthesis of plasmonic NPs. Previous works35,43 also
demonstrated Gryfﬁn’s efﬁciency by outperforming other
strategies such as SMAC, PyEvolve, Hyperopt, and GPyOpt by
minimizing the explored search space.

The AFION lab enabled efﬁcient exploration and optimization of
the multidimensional chemical space for NP synthesis. Across various
NP types, the identiﬁcation of reaction conditions in a chemical space
containing 7 interdependent reaction parameters was achieved less
than 30 experiments that were conducted in less than 30 h and used
less than 0.06 g of each reagent. The success of AFION’s utilizing a
limited number of experiments underscores the efﬁcient management
of data size within the constraints of time and resources.

We also note that the AFION-identiﬁed recipe for the preparation
of AuNRs, the concentration of CTAB was ten-fold lower than that used
in the reported photochemical AuNR synthesis46, with non-
compromised size distribution and shape purity. Such a reduction in
CTAB amount can enhance post-synthesis puriﬁcation and reduce NP
toxicity66.

The advantages of the AFION lab over batch-type SDLs in the
synthesis of inorganic nanomaterials stem from enhanced mass
transport, rapid reagent mixing, and reaction efﬁciency (both chemical
consumption and reaction rate), while ensuring consistent, repro-
ducible results through online NP characterization. The AFION lab
excels in reaction versatility, facilitating photochemical NP synthesis
and reactions requiring inert atmosphere. It offers cost-effectiveness
and safety of the synthesis by reducing reagent consumption. Finally,
its modular design facilitates easy adaptation and customization for
different reaction types without the need in redesigning the entire
experimental setup, which broadens the range of reactions available to
researchers. In addition, based on the exploration of the chemical
space in the AFION lab, the data-driven analysis surpassed the results
of conventional knowledge-based analysis in identifying critically
important reaction conditions and trends for the photochemical
synthesis of different NP types.

Nature Communications |

 (2025) 16:1473

9

Article

https://doi.org/10.1038/s41467-025-56788-9

Despite research acceleration and advancements are provided by
the AFION lab within its accessible experimental space, we acknowl-
edge the role of prior knowledge on the (i) correlation between
spectroscopic properties of plasmonic NPs and their shapes, (ii) NPs
precursor chemistry, and (iii) constraints imposed on reaction condi-
tions. While the incorporation of such knowledge facilitates the iden-
tiﬁcation of the relevant optical characteristics and selection of the
experimentally explored space, along with enhancing model
performance67,68, balancing prior knowledge and discovery of new NP
synthesis or properties is an important area of research that warrants
further exploration.

We admit that although the integration of UV–Vis–NIR spectro-
scopy provided real-time output results for the NP synthesis, the ability
to broaden the range of plasmonic NPs synthesized in the AFION lab is
currently constrained by the limitations in the wavelength range of the
spectrometer and light source used. For example, SPR bands of Pt69 or
Pd70 NPs are beyond the current detection range of 400–1000 nm.
These limitations can be mitigated by upgrading the AFION platform
to enhance its universality. Furthermore, the potential spectral overlap
of SPR bands of the selected NPs may lead to the challenge in their
target-speciﬁc synthesis. For example, differentiating between the
spectra of Au nanocubes and octahedra, based solely on their spec-
troscopic characteristics, would be challenging71,72. Another limitation
is that two SPR modes corresponding to the Au core and Ag shell are
observed distinctly for core–shell Au/Ag NSs with thin shells, however
as the Ag shell thickness increases, the SPR mode of Au core signal
would progressively blue-shift, until eventually disappearing73. This
effect would make the selection of spectroscopic targets for the
synthesis of Au/Ag core-shell NSs challenging, as a single SPR can be
attributed to Ag NPs74 or alloy NPs47. To address this challenge, the
integration of additional characterization techniques such as X-ray
diffraction would beneﬁt in characterizing the core–shell NP mor-
phology with alloy or NPs with single metal component75, while surface
enhanced Raman spectroscopy would be effective in distinguishing
between nanocubes, octahedra, and rhombic dodecahedra76. Other
complementary tools, including dynamic light scattering or induc-
tively coupled plasma mass spectrometry, can enhance NP size dis-
tribution and enable quantitative measurements of NPs concentration,
respectively77.
Finally,

in the present work, the AFION platform integrated
existing knowledge on the spectroscopic NP properties with the
algorithm objective deﬁnition and parameter space selection for the
synthesis of NPs with speciﬁc characteristics. This integration facil-
itates leveraging of the chemical domain expertize, particularly, in
areas where knowledge is still evolving. Further utilization of the
exploration mode of the AFION lab would pave the way for the
synthesis of plasmonic NPs that are yet to be reported, aligning with
theoretical predictions of their spectroscopic characteristics.

Building upon the knowledge gained from the present work, the
AFION lab can be further extended to perform multistep NP synthesis
by incorporating in-line centrifugation, heating, or cooling. Moreover,
exploring the photochemical synthesis of non-plasmonic NPs would
be feasible in the AFION lab. These developments would lead to
advancements for on-demand synthesis of NPs with enhanced preci-
sion and tailored functionalities.

In conclusion, we developed an SDL integrating seedless ﬂuidic
photochemical synthesis, real-time spectroscopic NP characterization,
and hierarchy-based multi-objective ML optimization algorithms to
explore a large chemical space for the on-demand seedless photo-
chemical synthesis of plasmonic NPs with different shapes, composi-
tions, and morphologies, and precisely controlled optical properties.
This work addresses the challenges of seedless photochemical synth-
esis, that is, concurrent nucleation and growth processes, as well as the
sensitivity of the NP properties to irradiation intensity and time. The
identiﬁcation of reaction conditions for the synthesis of each type of

NPs was accomplished in less than 30 experiments within less than
30 h. Validation by TEM imaging and EDS elemental mapping and line
scans showed that the UV-Vis-NIR spectroscopy is an efﬁcient guiding
tool in NP synthesis. Data analysis provided insight into the impact of
reaction conditions for the synthesis of the targeted NP type and the
impact of a speciﬁc reaction parameter on NP quality.

The results of this study provide the basis for future work in NP
synthesis. By further reﬁning synthetic techniques, transversing
unexplored chemical spaces, and employing advanced characteriza-
tion, the AFION lab can contribute to the development of ML-assisted
nanomaterial synthesis, self-assembly, and fabrication.

Methods
Chemicals
Gold (III) chloride solution (HAuCl4, 99.99%, 30 wt. % in dilute HCl),
silver nitrate (AgNO3, ≥ 99%), 2-hydroxy-4′-(2-hydroxyethoxy)-2-
methylpropiophenone (I-2959, 98%), hexadecyltrimethylammonium
bromide (CTAB, BioXtra, ≥ 99%, lot number 0000373694), copper(II)
chloride (CuCl2, 99%), hexadecyltrimethylammonium chloride (CTAC,
≥ 98%, lot number BCCH9939), and cetylpyridinium chloride (CPC,
meets USP testing speciﬁcations) were purchased from Sigma Aldrich
Canada and used as received. All solutions were prepared using deio-
nized water (Milli-Q water, 18 MΩ cm). The I-2959 reagent solution was
purged with nitrogen for 15 min before introducing it in the AFION Lab.
For CuNSs synthesis, all reagents (CuCl2, CTAC, I-2959, and deionized
water) were purged with nitrogen for at least 15 min due to reaction
sensitivity to oxygen.

The AFION platform setup
The syringe pumps for the AFION lab (PSD/8 precision syringe pump,
PSD/6 precision syringe pump) were purchased from Hamilton Com-
pany. For online spectroscopic analysis, an online ﬁber-optic, charge-
coupled device spectrometer (CCS200) and a spectrometer tungsten
halogen light source (SLS201L) were purchased from Thorlabs, Inc. To
facilitate ﬂuid transport, perﬂuroalkoxy tubing, accompanied by
appropriate tube ﬁttings were purchased from McMaster-Carr. The
details of tubing and liquid slug dimensions and ﬂow rates was pre-
sented in Table 1. The nitrogen gas inside the tubing and the vials of the
platform was pressurized at 137 kPa. The UV source providing wave-
length range of 345–385 nm (RX Fireﬂy Series) was purchased from
Phoseon Technology. The height adjustment and light control of the
UV source was implemented and controlled by Arduino Uno micro-
controller, which was acquired from Canada Robotix.

Nanoparticle synthesis
The photochemical synthesis of AuNRs, alloy AuAg NSs, core-shell Au/
Ag NSs, and Au tetrapods was achieved by reducing HAuCl4 and AgNO3
using photoreducing agent I-2959, with CTAB used as a surfactant. The
photochemical synthesis of CuNSs was achieved by reducing CuCl2
using photoreducing agent I-2959 and utilizing CTAC as a surfactant.
Synthesis of AgNSs was conducted by using I-2959 as a reducing agent,
with CPC acting as a surfactant. If replenishing the reagent solutions
was needed, to validate the initial starting point in both the ML-assisted
synthesis and random search experiments, a reference experiment was
conducted under identical reaction conditions within the same para-
meter space. The concentration for each reagent, photoirradiation
time, and reaction time were recommended by ML to obtain NPs with
different sizes, shapes, and compositions. The AuNR and Au tetrapod
solutions were centrifuged at 8000×g for 10 min at 27 °C; other NP
solutions were centrifuged at 15,000×g for 10 min at 27 °C, to remove
unreacted reagents.

Closed-loop NP synthesis
Reagent solutions with particular concentrations were prepared in
advance and introduced individually into 20-mL vials. Another 125-mL

Nature Communications |

 (2025) 16:1473

10

Article

https://doi.org/10.1038/s41467-025-56788-9

Table 1 | Dimensions of tubing and ﬂow rates of reagent solutions

Tubing dimensions

Dimensions of the cylindrical slug of
reagent solution

Volumetric ﬂow rate
(µL s-1)

Function

1/32-in. inner diameter, 1/16-in.
outer diameter

Diameter: 0.08 cm
Length: 19.89 cm

1/8-in. inner diameter, 1/4-in. outer
diameter

Diameter: 0.32 cm
Length: 1.26 cm

10

Solution transfer from the syringe dispenser to the
photochemical reactor

5–7, proposed by ML

Oscillation in the photochemical tube reactor

vial containing deionized water (MilliQ quality) served as a replenish-
ing source for the preparation of the reagent mixture. Deionized water
was also used to wash the tubing after each reaction. The dispenser
pump supplied sequentially reagent solutions into the tube to form a
100-μL volume cylindrical slug serving as a microreactor for NP
synthesis. The slug was moved in the oscillatory manner back and forth
in the tube by using a syringe pump equipped with a 2.5 mL gas-tight
syringe ﬁlled with pressurized nitrogen gas at 137 kPa, thereby ensur-
ing enhanced mixing of the solution44. The slug was subjected to UV
irradiation with intensity modulated by the distance between the UV
source and the ﬂow reactor, which changed from 9 to 75 mW cm−2. The
dispensed volumes of reagents (controlling the reagent concentration
in the liquid slug), the reaction time, the irradiation intensity, and the
oscillation speed of the liquid slug were all recommended by the ML-
algorithm. Upon completing the reaction, the liquid slug was trans-
ferred to a ﬂow cell for online spectroscopic characterization of the
NPs using a tungsten halogen light source and an in-line, ﬁber-optic,
charge-coupled device spectrometer. The extinction spectra of the
NPs were acquired in the 400–1000 nm wavelength range. Subse-
quently, the liquid slug was discharged to either the reservoir col-
lecting waste, or to the container for further off-line characterization
using TEM or EDS analysis. The TEM imaging was conducted to
determine the shapes and dimensions of the NPs synthesized under
optimized conditions. Statistical analyses on the TEM images were
performed with Python for at least, several hundreds of NPs.

Each set of reaction conditions proposed by the ML algorithm
for the NP synthesis was evaluated twice. The ML algorithm used as
inputs the mean values of the wavelength of the SPR band, its FWHM,
the SPR peak intensities, and the peak area under the curve (spec-
trum) in the designated spectral region. The AFION lab performance,
that is, the hardware control, analysis, and optimization were con-
trolled via in-house developed software written in Python. The user-
deﬁned parameters were customizable in an experimental conﬁg-
uration ﬁle, detailing the accessible parameter space of each reaction
condition, sampling strategies of parameter λ for the exploration-
exploitation trade-off, numerical seed of random number to gen-
erate for the suggestion of the ﬁrst experimental parameters,
objective hierarchy of the spectroscopic properties, and tolerance
levels of each objective.

Algorithm optimization process
We utilized the established BO algorithm, Gryfﬁn35, which employs a
kernel regression surrogate model inferred using a Bayesian neural
network for the modeling of the relationship between the reaction
conditions and the spectroscopic properties of the resulting NPs.
Initially, Gryfﬁn navigated a large reaction parameter space from a
position of no prior knowledge, with the ﬁrst set of reaction conditions
selected randomly. Upon collection of the spectroscopic NP char-
acteristics, the surrogate model commenced training on all available
experimental observations. Subsequently, Gryfﬁn proposed new
experimental proposals based on its acquisition function. The acqui-
sition function balanced exploitative and explorative sampling of
reaction conditions using a user-speciﬁed hyperparameter, which
could be adjusted between 1 and −1 to balance exploitative and
explorative proposals. Exploitative proposals aimed to provide local
reﬁnements to reaction conditions that have already produced

promising spectroscopic NP properties. Explorative proposals
prioritized unexplored regions in reaction parameter space, in which
the surrogate model’s predictions were highly uncertain. The sca-
larizing function, Chimera43, was used to conduct hierarchy-based
multi-objective optimization by transforming the spectroscopic NP
properties into a scalar value. Each objective was organized in a
hierarchy representing the ranking of the importance of each
objective importance to the research goal. Chimera also accepted
tolerances for each objective, that is, the threshold values beyond
which we were satisﬁed with the objective’s value. The optimizer was
then allowed to proceed to move on to optimize the subsequent
objective in the hierarchy.

Mutual information
The mutual information statistical method quantiﬁed the dependence
between the reaction conditions and the resulting NP type. Higher
mutual information values indicate a stronger relationship, providing
insight into the importance of each reaction parameter in the synthesis
of a particular NP type, that is, AuNRs, AuAg alloy NSs, Au/Ag
core–shell NSs, and tetrapods. The dataset comprised 214 data points,
representing 81% of the total 265 experiments conducted, with the
remaining data points beyond the scope of our research targets.

Validation of NP characteristics
The selected properties of NPs were validated by TEM imaging, EDS
element mapping and EDS line scans. TEM images of NPs were
acquired using a Hitachi HT7700 microscope at 100 kV. The EDS ele-
ment mapping and line scans were obtained from a JEM-ARM300F with
the JEOL Spherical Aberration Corrector at 200 kV. The samples for
both imaging instruments were prepared by drop-casting the solution
of NPs onto carbon-coated 300 mesh copper grids and dried in air at
room temperature.

Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.

Data availability
The data that support the ﬁndings of this study are available from the
corresponding author upon request. TEM images are available from
Github and Zenodo78. Source data are provided with this paper.

Code availability
The codes used in this study are available from the corresponding
author upon request. The source code for the AFION platform control,
NP size measurement, and related data analysis are available from
Github and Zenodo78. The source code for the algorithm Gryfﬁn is
available from Github.

References
1. West, J. L. & Halas, N. J. Engineered nanomaterials for biophotonics
applications: improving sensing, imaging, and therapeutics. Annu.
Rev. Biomed. Eng. 5, 285–292 (2003).

2. Nie, Z., Petukhova, A. & Kumacheva, E. Properties and emerging
applications of self-assembled structures made from inorganic
nanoparticles. Nat. Nanotechnol. 5, 15–25 (2010).

Nature Communications |

 (2025) 16:1473

11

Article

https://doi.org/10.1038/s41467-025-56788-9

3.

Burschka, J. et al. Sequential deposition as a route to high-
performance perovskite-sensitized solar cells. Nature 499,
316–319 (2013).

5.

4. Gao, P., Bin Mohd Yusoff, A. R. & Nazeeruddin, M. K. Dimensionality
engineering of hybrid halide perovskite light absorbers. Nat. Com-
mun. 9, 1–14 (2018).
Popovtzer, R. et al. Targeted gold nanoparticles enable molecular
CT imaging of cancer. Nano Lett. 8, 4593–4596 (2008).
Liong, M. et al. Multifunctional inorganic nanoparticles for imaging,
targeting, and drug delivery. ACS Nano 2, 889–896 (2008).
7. Hastie, T., Friedman, J. & Tibshirani, R. The Elements of Statistical

6.

Learning. (Springer New York, New York, NY, 2001).

8. Abolhasani, M. & Kumacheva, E. The rise of self-driving labs in
chemical and materials sciences. Nat. Synth. 2, 483–492
(2023).
Tao, H. et al. Nanoparticle synthesis assisted by machine learning.
Nat. Rev. Mater. 6, 701–716 (2021).

9.

10. Lohse, S. E., Eller, J. R., Sivapalan, S. T., Plews, M. R. & Murphy, C. J. A

simple milliﬂuidic benchtop reactor system for the high-
throughput synthesis and functionalization of gold nanoparticles
with different sizes and shapes. ACS Nano 7, 4135–4150 (2013).

11. Song, Y., Hormes, J. & Kumar, C. S. S. R. Microﬂuidic synthesis of

nanomaterials. Small 4, 698–711 (2008).

27. Torres, J. A. G. et al. A multi-objective active learning platform and

web app for reaction optimization. J. Am. Chem. Soc. 144,
19999–20007 (2022).

28. Salley, D. et al. A nanomaterials discovery robot for the Darwinian
evolution of shape programmable gold nanoparticles. Nat. Com-
mun. 11, 2771 (2020).

29. Volk, A. A. et al. AlphaFlow: autonomous discovery and optimiza-
tion of multi-step chemistry using a self-driven ﬂuidic lab guided by
reinforcement learning. Nat. Commun. 14, 1–16 (2023).

30. Zhao, H. et al. A robotic platform for the synthesis of colloidal

nanocrystals. Nat. Synth. 2, 505–514 (2023).

31. Abdel-Latif, K. et al. Self‐driven multistep quantum dot synthesis
enabled by autonomous robotic experimentation in ﬂow. Adv.
Intell. Syst. 3, 2000245 (2021).

32. Li, J., Tu, Y., Liu, R., Lu, Y. & Zhu, X. Toward “on-demand” materials
synthesis and scientiﬁc discovery through intelligent robots. Adv.
Sci. 7, 1901957 (2020).

33. Bezinge, L., Maceiczyk, R. M., Lignos, I., Kovalenko, M. V. & deMello,
A. J. Pick a color MARIA: adaptive sampling enables the rapid
identiﬁcation of complex perovskite nanocrystal compositions with
deﬁned emission characteristics. ACS Appl Mater. Interfaces 10,
18869–18878 (2018).

34. Clayton, A. D. et al. Algorithms for the self-optimisation of chemical

12. Sai Krishna, K. et al. Milliﬂuidics for time-resolved mapping of the

reactions. React. Chem. Eng. 4, 1545–1554 (2019).

growth of gold nanostructures. J. Am. Chem. Soc. 135,
5450–5456 (2013).

13. Długosz, O. & Banach, M. Inorganic nanoparticle synthesis in ﬂow
reactors-applications and future directions. React. Chem. Eng. 5,
1619–1641 (2020).

14. Li, W. et al. Multi-step microﬂuidic polymerization reactions con-

ducted in droplets: The internal trigger approach. J. Am. Chem. Soc.
130, 9935–9941 (2008).

35. Häse, F., Aldeghi, M., Hickman, R. J., Roch, L. M. & Aspuru-Guzik, A.
Gryfﬁn: an algorithm for Bayesian optimization of categorical vari-
ables informed by expert knowledge. Appl. Phys. Rev. 8,
031406 (2021).

36. Marin, M. L., McGilvray, K. L. & Scaiano, J. C. Photochemical stra-

tegies for the synthesis of gold nanoparticles from Au(III) and Au(I)
using photoinduced free radical generation. J. Am. Chem. Soc. 130,
16572–16584 (2008).

15. Park Il, J., Saffari, A., Kumar, S., Günther, A. & Kumacheva, E.

37. Yang, S. et al. Continuous synthesis of gold nanoparticles and

Microﬂuidic synthesis of polymer and inorganic particulate mate-
rials. Annu Rev. Mater. Res. 40, 415–443 (2010).

16. Taylor, C. J. et al. A brief introduction to chemical reaction optimi-

zation. Chem. Rev. 123, 3089–3126 (2023).

17. Li, J. et al. Autonomous discovery of optically active chiral inorganic
perovskite nanocrystals through an intelligent cloud lab. Nat.
Commun. 11, 1–10 (2020).

18. Epps, R. W. et al. Artiﬁcial chemist: an autonomous quantum dot

19.

synthesis bot. Adv. Mater. 32, 2001626 (2020).
Jiang, Y. et al. An artiﬁcial intelligence enabled chemical synthesis
robot for exploration and optimization of nanomaterials. Sci. Adv. 8,
1–12 (2022).

20. Low, A. K. et al. Evolution-guided Bayesian optimization for con-
strained multi-objective optimization in self-driving labs. NPJ
Comput. Mater. 10, 104 (2024).

21. Shields, B. J. et al. Bayesian reaction optimization as a tool for

chemical synthesis. Nature 590, 89–96 (2021).

22. Mekki-Berrada, F. et al. Two-step machine learning enables opti-
mized nanoparticle synthesis. NPJ Comput. Mater. 7, 1–10 (2021).

23. Tao, H. et al. Self-driving platform for metal nanoparticle synthesis:
combining microﬂuidics and machine learning. Adv. Funct. Mater.
31, 1–9 (2021).

24. Jose, N. A. et al. Pushing nanomaterials up to the kilogram scale—an
accelerated approach for synthesizing antimicrobial ZnO with high
shear reactors, machine learning and high-throughput analysis.
Chem. Eng. J. 426, 131345 (2021).

25. Vaddi, K., Chiang, H. T. & Pozzo, L. D. Autonomous retrosynthesis of
gold nanoparticles via spectral shape matching. Digit. Discov. 1,
502–510 (2022).

26. Krishnadasan, S., Brown, R. J. C., deMello, A. J. & deMello, J. C.

nanoplates with controlled size and shape under UV irradiation.
Colloids Surf. A Physicochem. Eng. Asp. 296, 37–44 (2007).
38. Ross, A., Muñoz, M., Rotstein, B. H., Suuronen, E. J. & Alarcon, E. I. A
low cost and open access system for rapid synthesis of large
volumes of gold and silver nanoparticles. Sci. Rep. 11, 5420 (2021).
39. Cambié, D., Bottecchia, C., Straathof, N. J. W., Hessel, V. & Noël, T.
Applications of continuous-ﬂow photochemistry in organic synth-
esis, material science, and water treatment. Chem. Rev. 116,
10276–10341 (2016).

40. Link, S. & El-Sayed, M. A. Spectral Properties and Relaxation

Dynamics of Surface Plasmon Electronic Oscillations in Gold and
Silver Nanodots and Nanorods. J. Phys. Chem. B 103,
8410–8426 (1999).

41. Eustis, S. & El-Sayed, M. A. Determination of the aspect ratio sta-

tistical distribution of gold nanorods in solution from a theoretical ﬁt
of the observed inhomogeneously broadened longitudinal plas-
mon resonance absorption spectrum. J. Appl. Phys. 100,
044324 (2006).

42. Hendel, T. et al. In situ determination of colloidal gold concentra-
tions with UV-Vis spectroscopy: limitations and perspectives. Anal.
Chem. 86, 11115–11124 (2014).

43. Häse, F., Roch, L. M. & Aspuru-Guzik, A. Chimera: enabling hier-
archy based multi-objective optimization for self-driving labora-
tories. Chem. Sci. 9, 7642–7655 (2018).

44. Abolhasani, M. & Jensen, K. F. Oscillatory multiphase ﬂow strategy

for chemistry and biology. Lab Chip 16, 2775–2784 (2016).
45. Liu, K. et al. Seedless synthesis of monodispersed gold nanorods

with remarkably high yield: synergistic effect of template mod-
iﬁcation and growth kinetics regulation. Chem. Eur. J. 23,
3291–3299 (2017).

Intelligent routes to the controlled synthesis of nanoparticles. Lab
Chip 7, 1434–1441 (2007).

46. Toussi, S. M., Zanella, M., Abdelrasoul, G. N., Athanassiou, A. &
Pignatelli, F. Twofold role of hexadecyltrimethylammonium

Nature Communications |

 (2025) 16:1473

12

Article

https://doi.org/10.1038/s41467-025-56788-9

bromide in photochemical synthesis of gold nanorods. J. Photo-
chem. Photobiol. A 311, 76–84 (2015).

47. Link, S., Wang, Z. L. & El-Sayed, M. A. Alloy formation of gold-
silver nanoparticles and the dependence of the plasmon
absorption on their composition. J. Phys. Chem. B 103,
3529–3533 (1999).

48. Perez-Lloret, M. et al. One-step photochemical green synthesis of
water-dispersible Ag, Au, and Au@Ag core–shell nanoparticles.
Chem. Eur. J. 25, 14638–14643 (2019).

49. Zhu, J., Chen, X. H., Li, J. J. & Zhao, J. W. The synthesis of Ag-coated
tetrapod gold nanostars and the improvement of surface-enhanced
Raman scattering. Spectrochim. Acta A Mol. Biomol. Spectrosc. 211,
154–165 (2019).

50. Park, K. et al. Growth mechanism of gold nanorods. Chem. Mater.

25, 555–563 (2013).

51. Shi, W., Casas, J., Venkataramasubramani, M. & Tang, L. Synthesis

and characterization of gold nanoparticles with plasmon absor-
bance wavelength tunable from visible to near infrared region. ISRN
Nanomater. 2012, 1–9 (2012).

52. Payne, E. K., Shuford, K. L., Park, S., Schatz, G. C. & Mirkin, C. A.

Multipole plasmon resonances in gold nanorods. J. Phys. Chem. B
110, 2150–2154 (2006).

67. Gennatas, E. D. et al. Expert-augmented machine learning. Proc.

Natl Acad. Sci. USA 117, 4571–4577 (2020).

68. George, J. & Hautier, G. Chemist versus machine: traditional

knowledge versus machine learning techniques. Trends Chem. 3,
86–95 (2021).

69. Stepanov, A. L., Golubev, A. N., Nikitin, S. I. & Osin, Y. N. A review on
the fabrication and properties of platinum nanoparticles. Rev. Adv.
Mater. Sci. 38, 160–175 (2014).

70. De Marchi, S., Núñez-Sánchez, S., Bodelón, G., Pérez-Juste, J. &

Pastoriza-Santos, I. Pd nanoparticles as a plasmonic material:
synthesis, optical properties and applications. Nanoscale 12,
23424–23443 (2020).

71. Kim, D. Y., Im, S. H., Park, O. O. & Lim, Y. T. Evolution of gold

nanoparticles through Catalan, Archimedean, and Platonic solids.
CrystEngComm 12, 116–121 (2010).

72. Li, C. et al. High-yield synthesis of single-crystalline gold nano-
octahedra. Angew. Chem. Int. Ed. 46, 3264–3268 (2007).

73. Zhang, C., Chen, B. Q., Li, Z. Y., Xia, Y. & Chen, Y. G. Surface plasmon
resonance in bimetallic core-shell nanoparticles. J. Phys. Chem. C
119, 16836–16845 (2015).

74. Liang, H. et al. Controlled synthesis of uniform silver nanospheres.

J. Phys. Chem. C 114, 7427–7431 (2010).

53. Blaber, M. G., Arnold, M. D. & Ford, M. J. A review of the optical

75. Csapó, E. et al. Synthesis and characterization of Ag/Au alloy and

properties of alloys and intermetallics for plasmonics. J. Phys.
Condens. Matter 22, 143201 (2010).

core(Ag)-shell(Au) nanoparticles. Colloids Surf. A Physicochem.
Eng. Asp. 415, 281–287 (2012).

54. Jansson, P. A. Deconvolution of Images and Spectra, 2nd Edition.

(Academic Press, 2014).

55. Siegel, A. L. & Baker, G. A. Bespoke nanostars: synthetic strategies,
tactics, and uses of tailored branched gold nanoparticles. Nanos-
cale Adv. 3, 3980–4004 (2021).

56. Chen, S., Wang, Z. L., Ballato, J., Foulger, S. H. & Carroll, D. L.

Monopod, bipod, tripod, and tetrapod gold nanocrystals. J. Am.
Chem. Soc. 125, 16186–16187 (2003).

57. Chang, Y. X. et al. Gold nanotetrapods with unique topological
structure and ultranarrow plasmonic band as multifunctional
therapeutic agents. J. Phys. Chem. Lett. 10, 4505–4510 (2019).
58. Xie, J., Lee, J. Y. & Wang, D. I. C. Seedless, surfactantless, high-yield
synthesis of branched gold nanocrystals in HEPES buffer solution.
Chem. Mater. 19, 2823–2830 (2007).

59. Liu, H. et al. Ligand-directed formation of gold tetrapod nanos-

tructures. J. Phys. Chem. C 117, 17143–17150 (2013).

60. Chang, Y. X. et al. Synergistic reducing effect for synthesis of well-
deﬁned Au nanooctopods with ultra-narrow plasmon band width
and high photothermal conversion efﬁciency. Front. Chem. 6,
1–8 (2018).

61. Stamplecoskie, K. G. & Scaiano, J. C. Light emitting diode irradiation
can control the morphology and optical properties of silver nano-
particles. J. Am. Chem. Soc. 132, 1825–1827 (2010).

62. Pacioni, N. L., Pardoe, A., McGilvray, K. L., Chrétien, M. N. & Scaiano,
J. C. Synthesis of copper nanoparticles mediated by photo-
generated free radicals: catalytic role of chloride anions. Photo-
chem. Photobiol. Sci. 9, 766–774 (2010).

63. Kraskov, A., Stögbauer, H. & Grassberger, P. Estimating mutual
information. Phys. Rev. E Stat. Phys. Plasmas Fluids Relat. Inter-
discip. Top. 69, 16 (2004).

64. Volk, A. A. & Abolhasani, M. Performance metrics to unleash the

power of self-driving labs in chemistry and materials science. Nat.
Commun. 15, 1–7 (2024).

65. Ahmed, M. & Narain, R. Rapid synthesis of gold nanorods using a
one-step photochemical strategy. Langmuir 26, 18392–18399
(2010).

66. Connor, E. E., Mwamuka, J., Gole, A., Murphy, C. J. & Wyatt, M. D.
Gold nanoparticles are taken up by human cells but do not cause
acute cytotoxicity. Small 1, 325–327 (2005).

76. Wu, H. L. et al. A comparative study of gold nanocubes, octahedra,
and rhombic dodecahedra as highly sensitive SERS substrates.
Inorg. Chem. 50, 8106–8111 (2011).

77. Shang, J. I. & Gao, X. Nanoparticle counting: towards accurate
determination of the molar concentration. Chem. Soc. Rev. 43,
7267–7278 (2014).

78. Wu, T., Tao, H. & Wu, Tony. C. Self-driving lab for the photochemical
synthesis of plasmonic nanoparticles with targeted structural and
optical properties. Zenodo https://doi.org/10.5281/zenodo.
14676292 (2025).

Acknowledgements
The authors are grateful to Natural Sciences and Engineering Research
Council of Canada (NSERC Canada) through the Discovery grant pro-
gram. A.A.-G. acknowledges support from the Canada 150 Research
Chairs program and the support of Anders. G. Frøseth. M.A. gratefully
acknowledges ﬁnancial support from the National Science Foundation
(Awards #1940959 and #2420490). R.J.H. gratefully acknowledges
NSERC Canada for the provision of the Postgraduate Scholarships-
Doctoral Program (PGSD3-534584-2019), as well as support from the
Vector Institute. S.K. acknowledges the Ontario Graduate Scholarship.
T.W. acknowledges the Queen Elizabeth II Graduate Scholarships in
Science and Technology. This research was undertaken thanks in part to
funding provided to the University of Toronto’s Acceleration Consortium
from the Canada First Research Excellence Fund.

Author contributions
E.K. and T.W. conceived the concept of the project. T.W. and S.K. built
the platform. T.W. and H.T. programmed the control of the AFION
platform with assistance of T.C.W. R.J.H. and A.A.-G. contributed with
the development of the algorithms. T.W. synthesized and character-
ized the nanoparticles using TEM images and EDS line scans. Z.B.Y,
X.G., W.Z., and K.L. performed EDS element mapping. E.K. and A.A.G.
acquired funding and directed the project. T.W. and E.K. wrote the
paper with the assistance of M.A. All authors provided feedback on
the paper.

Competing interests
The authors declare no competing interests.

Nature Communications |

 (2025) 16:1473

13

Article

https://doi.org/10.1038/s41467-025-56788-9

Additional information
Supplementary information The online version contains
supplementary material available at
https://doi.org/10.1038/s41467-025-56788-9.

Correspondence and requests for materials should be addressed to
Eugenia Kumacheva.

Peer review information Nature Communications thanks Olga Długosz
and the other, anonymous, reviewer(s) for their contribution to the peer
review of this work. A peer review ﬁle is available.

Reprints and permissions information is available at
http://www.nature.com/reprints

Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the
Creative Commons licence, and indicate if you modiﬁed the licensed
material. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other third
party material in this article are included in the article’s Creative
Commons licence, unless indicated otherwise in a credit line to the
material. If material is not included in the article’s Creative Commons
licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.

Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional afﬁliations.

© The Author(s) 2025

Nature Communications |

 (2025) 16:1473

14
