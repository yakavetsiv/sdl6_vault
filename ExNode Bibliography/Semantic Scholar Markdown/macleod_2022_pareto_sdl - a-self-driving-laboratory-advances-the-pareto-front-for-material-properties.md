---
tags:
  - literature
  - type/paper
  - lit/sdl
  - lit/nanomedicine
title: "A self-driving laboratory advances the Pareto front for material properties"
doi: 10.1038/s41467-022-28580-6
source_url: https://www.nature.com/articles/s41467-022-28580-6.pdf
source_file: macleod_2022_pareto_sdl - a-self-driving-laboratory-advances-the-pareto-front-for-material-properties.pdf
type: semantic-scholar-oa-fulltext
---

# A self-driving laboratory advances the Pareto front for material properties

## Metadata

- DOI: 10.1038/s41467-022-28580-6
- Source URL: https://www.nature.com/articles/s41467-022-28580-6.pdf
- Downloaded file: [[Semantic Scholar PDFs/macleod_2022_pareto_sdl - a-self-driving-laboratory-advances-the-pareto-front-for-material-properties|macleod_2022_pareto_sdl - a-self-driving-laboratory-advances-the-pareto-front-for-material-properties.pdf]]
- Extracted characters: 65614

## Extracted Text

ARTICLE

https://doi.org/10.1038/s41467-022-28580-6

OPEN

A self-driving laboratory advances the Pareto front
for material properties
1,2,5, Fraser G. L. Parlane

Benjamin P. MacLeod
Michael S. Elliott
Nina Taherimakhsousi1, David J. Dvorak2, Hsi N. Chiu1, Christopher E. B. Waizenegger1, Karry Ocean1,
1,2,3,4✉
Mehrdad Mokhtari1 & Curtis P. Berlinguette

1,2,5, Connor C. Rupnow1,2,3, Kevan E. Dettelbach

1, Oleksii Proskurin1, Michael B. Rooney1,

1, Thomas D. Morrissey

1,2, Ted H. Haley

1,

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

Useful materials must satisfy multiple objectives, where the optimization of one objective is
often at the expense of another. The Pareto front reports the optimal trade-offs between
these conﬂicting objectives. Here we use a self-driving laboratory, Ada, to deﬁne the Pareto
front of conductivities and processing temperatures for palladium ﬁlms formed by combus-
tion synthesis. Ada discovers new synthesis conditions that yield metallic ﬁlms at lower
processing temperatures (below 200 °C) relative to the prior art for this technique (250 °C).
This temperature difference makes possible the coating of different commodity plastic
materials (e.g., Naﬁon, polyethersulfone). These combustion synthesis conditions enable
us to to spray coat uniform palladium ﬁlms with moderate conductivity (1.1 × 105 S m−1) at
191 °C. Spray coating at 226 °C yields ﬁlms with conductivities (2.0 × 106 S m−1) comparable
to those of sputtered ﬁlms (2.0 to 5.8 × 106 S m−1). This work shows how a self-driving
trade-offs between conﬂicting
laboratoy can discover materials that provide optimal
objectives.

1 Department of Chemistry, The University of British Columbia, 2036 Main Mall, Vancouver, BC V6T 1Z1, Canada. 2 Stewart Blusson Quantum Matter
Institute, The University of British Columbia, 2355 East Mall, Vancouver, BC V6T 1Z4, Canada. 3 Department of Chemical and Biological Engineering, The
University of British Columbia, 2360 East Mall, Vancouver, BC V6T 1Z3, Canada. 4 Canadian Institute for Advanced Research (CIFAR), MaRS Centre, 661
University Avenue Suite 505, Toronto, ON M5G 1M1, Canada. 5These authors contributed equally: Benjamin P. MacLeod, Fraser G. L. Parlane.
✉

email: cberling@chem.ubc.ca

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications

1


ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

Self-driving laboratories combine automation and artiﬁcial

intelligence to accelerate the discovery and optimization of
materials1–3. The increasing ﬂexibility of laboratory auto-
mation is enabling self-driving laboratories to manipulate and
measure a broader set of experimental variables4. Consequently, a
growing number of self-driving laboratories are being developed
across a range of ﬁelds5–28. While many self-driving laboratories
are able to test multiple experimental variables, most optimize for
only a single objective (e.g., process parameter, material
property)7–16. This situation is not consistent with most practical
applications, where multiple objectives need to be simultaneously
optimized29–35. Consider, for example, how a solar cell must be
optimized for voltage, current, and ﬁll factor to yield a high power
conversion efﬁciency36,37; how an electrolyzer must form pro-
ducts at low voltages and high reaction rates and selectivities38;
and, how structural alloys are optimized for both strength and
toughness31,35. These and other applications motivate the emer-
ging
for multiobjective
use
optimization18–28.

laboratories

self-driving

of

The optimization of materials for multiple objectives can be
challenging because improving one objective often compromises
the light-absorbing
another (e.g., decreasing the bandgap of
material in a photovoltaic cell increases the photocurrent but
decreases the voltage39). As a result, there is often no single
champion material, but rather a set of materials exhibiting trade-
offs between objectives (Fig. 1). The set of materials with the best
possible trade-offs lie at the Pareto front. Materials on the Pareto
front cannot be improved for one objective without compro-
mising one or more other objectives. Most self-driving labora-
tories used for multiobjective optimization, however, identify only
a single optimal material based on preferences speciﬁed in
advance of the experiment18–25.

Here, we use a self-driving laboratory to map out an entire
Pareto front27,28. We apply this approach to thin ﬁlm materials for
the ﬁrst time by mapping out a trade-off between ﬁlm con-
ductivity and processing temperature. In doing so, our self-driving
laboratory identiﬁes previously untested conditions that decrease
the temperature required for the combustion synthesis of palla-
dium ﬁlms from 250 to 190 °C40. This ﬁnding increases the scope
of polymeric substrates that palladium can be deposited on by
combustion synthesis to include Naﬁon41, polyethersulfone42, and

Pareto front of
best possible
materials

Ada
closes this
gap

objective B

Pareto front
of best
known materials

suboptimal
materials

objective A

Fig. 1 A Pareto front. No single optimal material exists when searching for
materials that satisfy two or more conﬂicting objectives (e.g., ﬁlm
conductivity and processing temperature). Rather, there is a set of
materials that offer the best possible tradeoffs between the objectives
(indicated by the blue curve). The state-of-the-art materials that offer the
best known compromises between the two objectives form the
experimentally observed Pareto front (black points).

heat-stabilized polyethylene napththalate42. Our
self-driving
laboratory also identiﬁes conditions suitable for spray coating
homogeneous ﬁlms on larger substrates with conductivities
approaching those of ﬁlms made by vacuum deposition methods.
The approach presented here is highly relevant to the materials
sciences because it identiﬁes optimal materials for every preferred
tradeoff between objectives.

Results
Autonomously discovering a Pareto front. We upgraded the
hardware and software of our existing self-driving laboratory,
Ada8, (Fig. 2) to study the combustion synthesis of conducting
palladium ﬁlms. This upgraded self-driving laboratory was
designed to map out a Pareto front that shows the tradeoff
between the temperature at which the ﬁlms are processed and the
ﬁlm conductivity. We selected combustion synthesis as an opti-
mization problem because it is a solution-based method for
making functional metal coatings. This method, however, has not
yet been scaled and has not been proven for making high-quality,
conductive metal ﬁlms40,43,44. Combustion synthesis can form
coatings at lower temperatures, enabling the potential use of
inexpensive polymeric substrates45,46, but ﬁlm conductivity
typically decreases with processing temperature43. This situation
presents a trade-off: to what extent can the conductivity be
maximized while the processing temperature is minimized? The
answer to this question would enable the researcher to determine,
for example, what types of substrates could be layered with a
metal coating of certain conductivity. We therefore leveraged Ada
to effectively study the numerous compositional47,48 and pro-
cessing variables43,49 that inﬂuence processing temperatures and
the corresponding conductivities.

For this study we conﬁgured Ada to manipulate four variables:
fuel identity, fuel-to-oxidizer ratio, precursor solution concentra-
tion, and annealing temperature (Fig. 3a). We conﬁned the study
to mixtures of two fuels, glycine and acetylacetone, that we
independently identiﬁed to yield conductive ﬁlms at temperatures
below 300 °C. The fuel-to-oxidizer ratio was varied because it
controls product oxidation in bulk combustion syntheses50,51.
The precursor concentration inﬂuences the morphology of the
drop-casted ﬁlms. Finally, we varied the processing temperature
which may inﬂuence the conductivity through solvent removal,
precursor decomposition, ﬁlm densiﬁcation, impurity removal,
grain growth, oxidation, or cracking52–54.

Flexible automation4 enabled us to upgrade Ada (Fig. 2a) by
coupling a larger, 6-axis robot to the existing smaller, 4-axis
robot. The smaller robot (Fig. 2b) deposited and characterized the
thin ﬁlms8, while the larger robot transported the samples to a
commercial X-ray ﬂuorescence (XRF) microscope for elemental
analysis. These two robots jointly executed a 7-step experimental
workﬂow (Fig. 2c, see “Methods” section). First, a combustion
synthesis precursor solution was formulated from stock solutions
and then drop-cast onto a glass microscope slide. The resulting
precursor droplet was imaged and then annealed in a forced-
convection oven to form a ﬁlm. The ﬁlm was subsequently
characterized by XRF microscopy, imaging, and 4-point probe
conductance mapping. The conductivity of each ﬁlm was
determined by combining the conductance with a ﬁlm thickness
estimated by XRF (see “Autonomous workﬂow step 7” in
“Methods” section, Supplementary Fig. 2). Finally, the conduc-
tivity and processing temperature for each ﬁlm were passed to a
multiobjective Bayesian optimization algorithm55 to plan the next
experiment based on all the available data (see “Autonomous
workﬂow step 8” in “Methods” section). The algorithm we used is
called q-expected hypervolume improvement (qEHVI)55.

2

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications


NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

ARTICLE

Fig. 2 The Ada self-driving laboratory and autonomous experimental workﬂow. a Schematic of the Ada self-driving laboratory. Ada consists of two
robots (N9 and UR5e) with overlapping work envelopes. These robots work together to synthesize and characterize thin ﬁlm samples. The N9 robot is a
4-axis arm equipped to mix, drop cast, and anneal precursors to create thin-ﬁlm samples. The N9 also performs imaging and 4-point probe conductance
measurements on the ﬁlms it creates. The UR5 robot is a larger 6-axis arm equipped to transport samples to additional modules, including an XRF
microscope. b Steps in the automated experimental workﬂow. Each iteration of the experiment produces a single, drop-cast, thin-ﬁlm sample; images of the
sample before and after annealing; an XRF map of the quantity of palladium in the ﬁlm; and a map of the ﬁlm conductance measured by the 4-point-probe
at different locations on the sample. After the sample is characterized, the ﬁlm conductivity is calculated and the qEHVI algorithm is used to autonomously
plan the next experiment. All scale bars are 5 mm.

All of the steps in the autonomous workﬂow were performed
without human intervention at a typical rate of two samples an
hour. Ada could run unattended for 40–60 experiments until the
necessary consumables (e.g., pipettes tips, mixing vials, glass
substrates,
section) were
see
exhausted. We used Ada to execute a total of 253 combustion
synthesis experiments that explored a wide range of pertinent
composition and processing variables.

and precursors;

“Methods”

The qEHVI algorithm is one of a number of a posteriori
multiobjective optimization algorithms designed to identify the
Pareto front55–58. These multiobjective optimization methods are
known as a posteriori methods because preferred solutions are
selected after the optimization. We chose to use an a posteriori
method for this exploratory study, because we sought to identify a
range of Pareto-optimal outcomes rather than a single optimal
point. We selected the qEHVI algorithm because previously
reported benchmarks show that the qEHVI algorithm often
in fewer experiments than other
resolves the Pareto front
algorithms.55

The qEHVI algorithm directed our self-driving laboratory to
quantify the trade-off between ﬁlm conductivity and annealing
temperature (Fig. 3). We manually selected eight synthesis
the design space to provide
conditions spanning most of
initialization data for the qEHVI algorithm (Supplementary
Table 1). After executing these initial experiments, Ada executed
more than 50 iterative qEHVI-guided experiments to map the
Pareto front of annealing temperature and conductivity. We
performed this autonomous optimization campaign in quad-
ruplicate. Each replicate generated a Pareto front showing a clear
trade-off between temperature and conductivity (Fig. 3b).

The synthesis conditions tested during the optimization are
shown in Fig. 3a; the conditions that created materials on the
Pareto front are highlighted. The data revealed that the optimal
precursors typically were those of concentrations near 6 mg mL−1,
fuel-to-oxidizer
ratios below 1, and fuel blends consisting
primarily of acetylacetone. Notably, our experiments did not
reveal a single optimal synthesis condition. The conditions
required to obtain the maximum conductivity depended in part

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications

3


ARTICLE

a

acac

l

e
u
f

x
,
d
n
e
b

l

gly
12.5

)
L
m
/
g
m

(

,
.
c
n
o
c

l

a
t
o
t

C

5.5
280

)

,
.
p
m
e
t

l

a
e
n
n
a

C
°
(
T

180

0

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

input space (parameters)

fuel-to-oxidizer
ratio

oxidizer

fuel blend

Pd(NO3)2

+

acac

+

1

−

gly

Pd

total concentration

combustion fuels
O

O O

H2N

OH

acetylacetone
(acac)

glycine
(gly)

b

120

)
1
-

m
S

(

y
t
i
v
i
t
c
u
d
n
o
c

80

40

0

output space (objectives)

Pareto front of
optimal materials

campaign 2

campaign 1

campaign 3

campaign 4

suboptimal
materials

fuel:oxidizer
ratio, φ

2.5

gly

acac

5.5

fuel
blend, x

total conc.,
C (mg/mL)

12.5

175

200

225

250

275

annealing temperature (°C)

Fig. 3 Trade-off between annealing temperature and conductivity for the combustion synthesized palladium ﬁlms. a Maps of the combustion synthesis
conditions required to obtain experimental outcomes on the Pareto front. Sampled points not on the Pareto front are shown in gray. The combustion
synthesis reaction, with parameters manipulated during the optimization highlighted, is shown. In this reaction x controls the fuel blend and φ is the fuel-to-
oxidizer ratio, as calculated using Jain’s method (see Supplementary Methods). The fuel-to-oxidizer ratio used is scaled by k = 36/5(8 - 5x) to account for
the differing reducing valences of the acetylacetone and glycine fuels. b The empirical Pareto fronts from each of the four campaigns (solid lines) reveal the
observed trade-off between temperature and conductivity. The experimental points which deﬁne the fronts are shown with open markers. Sampled points
not on the Pareto front are shown in gray.

on the annealing temperature. Speciﬁcally, conductive ﬁlms
created below 200 °C required precursors with predominantly
acetylacetone fuel. At higher temperatures, however, glycine-rich
fuel blends also yielded samples on the Pareto front. The data
shows how the fuel-to-oxidizer ratio could vary widely for fuels
rich in acetylacetone yet still yield ﬁlms on the Pareto front. The
Pareto-optimal samples resulting from glycine-rich fuel blends,
however, did not exhibit a wide range of fuel to oxidizer values.
These observations highlight the richness of the data generated by
the self-driving laboratory.

Quantiﬁcation of algorithm performance. We used computer
simulations to quantify the beneﬁt of the qEHVI algorithm
relative to random search (an open-loop sampling technique that
does not use feedback from the experiment to determine which
experiment to do next). These simulations were performed by
running both the random and qEHVI sampling techniques on a
response surface ﬁt to the experimental data (see “Methods”
section). Scenarios with and without experimental noise were
simulated by adding synthetic noise to the response surface as
appropriate (see “Models of the experimental response surface
and noise” in “Methods” section).The hypervolume (i.e., the area
under the Pareto front) was used to measure the progress of
optimization (Fig. 4a). We used acceleration factor (Fig. 4b) and
enhancement factor (Fig. 4c) to compare our closed-loop sam-
pling using qEHVI to open-loop sampling using random search;
see “Methods” section59. In a noise-free scenario, qEHVI required
less than 100 samples to outperform 10,000 random samples
(Fig. 4a). The performance of the qEHVI algorithm degraded in
the presence of simulated experimental noise (see “Methods”
section), but still exceeded the performance of random search.
This performance decrease due to noise emphasizes the impor-
tance of minimizing experimental noise when developing a self-
driving experiment. Benchmarks comparing other closed-loop

and open-loop sampling techniques yielded similar results (see
Supplementary Fig. 11). These ﬁndings highlight how self-driving
laboratories can effectively search large materials design spaces
without requiring extremely high throughput.

Translation of discovery to a scalable manufacturing process.
The practical application of combustion synthesis would require
the deposition of uniform ﬁlms over large areas that are inac-
cessible to drop casting. On this basis, we set out to combine
palladium combustion synthesis with ultrasonic spray coating60.
We sprayed precursors directly onto a preheated glass substrate60
(Fig. 5a, see “Methods” section). The precursors decomposed in
less than ﬁve minutes to yield reﬂective, conductive palladium
ﬁlms (Fig. 5b). An XRF map of the ﬁlms (Fig. 5c) showed
improved homogeneity relative to the drop-cast ﬁlms (Fig. 2b).
We performed additional spray coating experiments to verify
that
the trends observed in the autonomous optimization
translate to spray coating (i.e., that conductive palladium ﬁlms
can be obtained below 200 °C and that the ﬁlm conductivity
increases with temperature). Speciﬁcally, we spray coated
palladium ﬁlms using three recipes from the autonomously
identiﬁed Pareto front, with temperatures of 191, 200, and 226 °C
(Fig. 6 and Supplementary Table 2). Triplicate samples were spray
three recipes yielded ﬁlms
coated using each recipe. All
approximately 50–60 nm thick, as measured by XRF microscopy
(see “Methods” section). All the ﬁlms were relatively uniform,
with spatial variations in the ﬁlm thickness less than 5% of the
mean within an 8 mm × 20 mm region at the center of each
sample (see “Methods” section and Supplementary Table 3).
Spatial variations in the conductivity within the same region were
measured using the robot and were less than 18% of the mean for
all samples (see “Methods” section and Supplementary Table 3).
The ﬁlm conductivity of
recipe
the
(T = 191 °C) was 1.1 × 105 S m−1, which is approximately 1%

temperature

lowest

4

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications


NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

ARTICLE

Fig. 4 Quantiﬁcation of the beneﬁt provided by the qEHVI algorithm in simulated optimization campaigns. a The hypervolumes achieved by the
simulated qEHVI and random searches. The median (solid line) and interquartile range (shaded bands) of the results are shown for simulations with and
without simulated experimental noise. b The acceleration factors for the qEHVI algorithm relative to random search. The geometric mean is also shown
(dashed line). c The enhancement factor for the qEHVI algorithm relative to random search.

a

b

c

XRF Pd
signal
(cps)

40

0

ultrasonic
spray-coating
nozzle

substrates

hotplate
fixture

photo of
spray-coated
microscope slide

XRF homogeneity
map

Fig. 5 Low-temperature spray combustion synthesis of homogeneous palladium ﬁlms over large areas. a Spray coating apparatus. An ultrasonic nozzle
attached to an overhead XYZ stage (not visible) is used to spray palladium combustion synthesis precursors onto glass substrates placed on a hot plate
with an aluminum ﬁxture. The precursors decompose to yield palladium ﬁlms. Scale bar is 3 cm. b Photograph of a typical resulting ﬁlm on a 3″ × 1″ glass
substrate. Sharp edges were produced by masking the substrate using Kapton tape. c XRF map of the sample pictured in b. To aid visualization, the
photograph in panel a has been ﬂipped horizontally. Scale bars in b, c are 1 cm.

of the bulk conductivity of palladium61. The ﬁlm conductivity can
increase by more than an order of magnitude when the spray
coating temperature is increased by 35 °C. The highest tempera-
ture recipe tested (T = 226 °C) yielded palladium ﬁlms with a
conductivity of 2.0 × 106 S m−1, which is comparable to the
conductivities of sputtered palladium ﬁlms reported in the
literature (2.0–5.8 × 106 S m−1; Fig. 6)62–64. These ﬁndings create
new opportunities to deposit palladium ﬁlms without vacuum
onto large-area substrates,
including an expanded range of
temperature-sensitive polymers (e.g., Naﬁon41, polyethersulfone42,
and heat-stabilized polyethylene naphthalate42). One application
of this deposition process could be the fabrication of
large,
supported palladium membranes for more cost-effective electro-
catalytic palladium membrane reactors65.

be applied. Our approach eliminates the need for the researcher
to specify preferences between competing objectives in advance of
the experiment, and also produces a richer, more valuable data
set. In this case, the temperature–conductivity Pareto front is
more useful than optimizing conductance for a ﬁxed temperature
limit because processing temperature limits vary depending on
self-driving laboratory also identiﬁed
the application. Our
synthesis conditions that translated to a scalable spray-coating
method for depositing high-quality, high-conductivity palladium
ﬁlms at temperatures above 190 °C. This work shows how self-
driving laboratories can potentially accelerate the translation of
materials to industry, where satisfying multiple objectives is
essential.

Discussion
Here, we mapped out a Pareto front between ﬁlm processing
temperature and conductivity using a self-driving laboratory
guided by the qEHVI multi-objective optimization algorithm.
This tradeoff is just one example of the conﬂicting objectives
routinely faced by materials scientists to which our method could

Methods
Materials. MeCN (CAS 75-05-8; high-performance liquid chromatography
(HPLC) grade, ≥99.9% purity), glycine (CAS 56-40-6, ACS reagent grade, >98.5%
purity) and acetylacetone (CAS 123-54-6; ≥99% purity) were purchased from
Sigma-Aldrich. Urea (CAS 57-13-6, ultra-pure; heavy metal content 0.01 ppm) was
•H2O; Pd
purchased from Schwarz/Mann. Palladium(II) nitrate hydrate (Pd(NO3)2
~40% m/m; 99.9% Pd purity, CAS 10102-05-3) was purchased from Strem Che-
micals, Inc. All chemicals were used as received without further puriﬁcation.

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications

5


ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

Autonomous workﬂow step 1: mix precursors. The 4-axis robot formulated each
precursor by pipetting varying volumes of the stock solutions described above into
a clean 2 mL HPLC vial. Gravimetric feedback from an analytical balance (ZSA120,
Scientech) was used to minimize and record pipetting errors. The precursor was
mixed by repeated aspiration and dispensing.

Autonomous workﬂow step 2: drop cast precursor. The 4-axis robot used a
vacuum-based substrate handling tool to place a clean glass slide onto a tray. This
robot then created a thin ﬁlm sample by using a pipette to drop cast 98 µL of the
precursor into a predeﬁned well on the slide. The solution was ejected from the
pipette at a rate of 5 µL s−1 from a height of approximately 1.5 mm above the top
surface of the substrate.

Autonomous workﬂow step 3: image precursor droplet. The 4-axis robot
acquired visible-light photographs of each sample before annealing. This robot
positioned samples 90 mm below a camera (FLIR Blackﬂy S USB3; BFS-U3-
120S4C-CS) using a Sony 12.00 MP CMOS sensor (IMX226) and an Edmund
Optics 25 mm C Series Fixed Focal Length Imaging Lens (#59–871). The C-mount
lens was connected to the CS-mount camera using a Thorlabs CS- to C-Mount
Extension Adapter, 1.00″-32 Threaded, 5 mm Length (CML05). The sample was
illuminated from the direction of the camera using a MIC-209 3-W ring light. For
imaging, the lens was opened to f/1.4, and black ﬂocking paper (Thorlabs BFP1)
was placed 10 cm behind the sample.

Autonomous workﬂow step 4: annealing. After drop casting, the 4-axis robot
used the substrate handling tool to transport the precursor-coated slide into a
purpose-built miniature convection oven for annealing at a variable temperature
between 180 and 280 °C. The most important features of the oven are a low-
thermal mass construction (lightweight aluminum frame with glass-ﬁber insula-
tion) and internal and external fans. These features enable rapid heating and
cooling of the sample (Supplementary Fig. 12). A pneumatically actuated lid
enables robotic access to the sample. The oven employs a ceramic heating element
(P/N 3559K23, McMaster Carr) controlled by a PID temperature controller (P/N
CN7523, Omega Engineering). A type-K thermocouple located in the oven air
space provides temperature feedback to the controller. In the experiments per-
formed here, the sample was inserted into the oven which was then ramped at
40 °C per minute to the temperature set point, which was then held for 450 s. Upon
completion of the hold, the oven lid was opened and a cooling fan turned on to
blow ambient temperature air through the oven and over the sample. The sample
was removed from the oven after the temperature dropped below 60 °C. The oven
was further cooled to below 40 °C prior to loading of the next sample.

Autonomous workﬂow step 5: XRF imaging and data analysis. The self-driving
laboratory acquired hyperspectral X-ray ﬂuorescence (XRF) images of each sample
using a Bruker M4 TORNADO X-ray ﬂuorescence microscope equipped with a
customized sample ﬁxture. Samples were transported to the XRF microscope by the
UR5e 6-axis robotic arm equipped with a vacuum-based substrate handling tool
similar to the one used by the 4-axis N9 robot. A dedicated exchange tray accessible
to both robots enabled samples to be passed from one robot to the other.

The XRF microscope has a rhodium X-ray source operated at 50 kV/600 µA/
30 W and polycapillary X-ray optics yielding a 25 µm spot size on the sample. The
instrument employs twin 30 mm2 silicon drift detectors and achieves an energy
resolution of 10 eV. Hyperspectral images were taken over a 20 mm × 20 mm area
at a resolution of 125 × 125 pixels. The XRF spectra obtained (reported in counts)
were scaled by the integration time (50 ms) and the energy resolution (10 eV) to
yield units of counts s−1 eV−1.

To quantify the relative amount of palladium in the ﬁlm, the palladium Lyman-
alpha X-ray ﬂuorescence line (2.837 keV) was integrated from 2.6 to 3.2 keV. The
resulting counts were converted to ﬁlm thickness estimates by applying a
calibration factor obtained using reference samples (see below). Ninety-seven
points of interest are deﬁned within the XRF hypermap of the sample, as deﬁned in
Supplementary Fig. 3. For each point of interest, the average XRF counts
per second were calculated over a 3 mm × 3 mm area.

Autonomous workﬂow step 6: image annealed ﬁlm. The self-driving laboratory
acquired visible light photographs (as described in step 3) of each sample after
annealing.

Autonomous workﬂow step 7: ﬁlm conductivity measurement. After hyper-
spectral XRF imaging, the sample was returned by the UR5e robot to the N9 robot for
ﬁlm conductance measurements. Four-point probe conductance measurements were
performed with a Keithley Series K2636B System Source Meter instrument connected
to a Signatone four-point probe head (part number SP4-40045TBN; 0.040-inch tip
spacing, 45 g pressure, and tungsten carbide tips with 0.010-inch radii) by a Signatone
triax to BNC feedthrough panel (part number TXBA-M160-M). The source current
was stepped from 0 to 1 mA in 0.2 mA steps. After each current step, the source meter
was stabilized for 0.1 s and the voltage across the inner probes was then averaged for
three cycles of the 60 Hz power line (i.e., for 0.05 s) and recorded. Conductance

Fig. 6 Comparison between the conductivity of the spray-coated
palladium ﬁlms and sputtered ﬁlms. The conductivity values for sputtered
ﬁlms62–64 and bulk palladium61 are from previous literature. The spray
coating recipes are taken directly from the Pareto front and are given in
Supplementary Table 2. For the spray combustion data (see also
Supplementary Table 3), each point shows the conductivity of one of the
three replicate samples for each recipe. The bars show the average
conductivity across all three replicates for each recipe.

Manual preparation of stock solutions. The self-driving laboratory is provided
with starting materials in the form of stock solutions which are prepared manually
and then placed in capped 2 mL HPLC vials in a tray where they can be accessed by
the self-driving laboratory. All solutions were prepared at a concentration of
12 mg mL−1. The Pd(NO3)2
while all other solutions were prepared using deionized H2O.

•H2O solution was prepared using MeCN as a solvent

Preparation of glass substrates and other consumables. In addition to stock
solutions, the self-driving laboratory uses consumable glass substrates (75 mm ×
25 mm × 1 mm microscope slides; VWR catalog no. 16004-430), 2 mL HPLC vials
(Canadian Life Science), and 200 µL pipettes (Biotix, M-0200-BC). These are placed
in appropriate racks and trays for access by the robotics.

The HPLC vials and pipettes were used as received, whereas the microscope
slides were cleaned by sequential sonication in detergent, deionized water, acetone,
and isopropanol for 10 min each8. Wells of 18 mm diameter were then created on
the microscope slides using a sprayed enamel coating (DEM-KOTE enamel ﬁnish)
and circular masks placed at the center of each slide (Supplementary Fig. 1). The
wells serve to conﬁne the precursor solution before it dries.

Self-driving laboratory. The self-driving laboratory consists of a precision 4-axis
laboratory robot (N9, North Robotics) coupled with a 6-axis collaborative robot
(UR5e, Universal Robotics). The 4-axis robot is equipped to perform entire thin
ﬁlm deposition and characterization workﬂows and is described in our previous
work8. The 6-axis robot enables samples to be transferred to a variety of additional
modules, including the XRF microscope used here. Both robots are equipped with
vacuum-based tools for substrate handling. All robots and instruments were
controlled by a PC with software written in Python.

Overview of autonomous robotic workﬂow. The majority of operations in the
autonomous robotic workﬂow are performed by the 4-axis laboratory robot.
Samples are transported between the 4-axis robot and the XRF microscope by the
6-axis robot.

The 4-axis robot prepared each sample by combining stock solutions to form a

precursor mixture, drop casting this precursor onto a glass slide, and then
annealing the sample in a forced convection oven (Supplementary Fig. 1). The
samples were characterized by white light photography before and after annealing,
X-ray ﬂuorescence microscopy, and 4-point-probe conductance measurements.
The resulting data was then automatically analyzed using a custom data pipeline
implemented in Python. Finally, the result of the experiment was fed to a Bayesian
optimizer which used an expected hypervolume improvement acquisition function
to select the next experiment to be performed. Each of these steps is described in
further detail below.

6

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications


NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

ARTICLE

measurements were made on the same 97 points of interest as analyzed in the XRF
data, as deﬁned in Supplementary Fig. 3.

The ﬁlm conductivity was calculated using a custom data analysis pipeline
implemented in Python using the open-source Luigi framework66. This pipeline
combined conductance data and XRF data to estimate the ﬁlm conductivity at each
of the 97 points of interest on the sample.

For each set of current–voltage measurements at each position on each sample,
the RANSAC robust linear ﬁtting algorithm67 was used to extract the conductance
(dI/dV). The voltage compliance limit of the K2636B was set to 10 V and voltage
measurements greater than 10 V were therefore considered to have saturated the
Source Meter instrument and automatically discarded by the data analysis pipeline.
The conductivity of the thin ﬁlms was then calculated by combining the 4-

point-probe conductance data with the ﬁlm thicknesses estimated by XRF:

σ ¼ ln2
π

´ dI
dV

(cid:2)1;

´ t

ð1Þ

where dI/dV is the conductance from the 4-point-probe measurement, t is
estimated ﬁlm thickness from the XRF measurements, and σ is conductivity.
Due to the poor morphology of the drop-cast ﬁlms, a robust conductivity
estimation scheme was employed. First, conductance data was excluded for any
measurement positions with zero conductance. Next, outliers were excluded from
the remaining conductance data using a kernel density exclusion method (see
below). Outliers were also excluded from the XRF ﬁlm thickness estimates using
the same exclusion method. Conductivities were calculated for each position on the
sample for which neither conductance nor XRF data was excluded. The mean of
these conductivities was returned to the optimizer (see below). In cases where all
points were discarded, a mean conductivity of 0 was reported.

The outlier kernel density exclusion method was performed by calculating
Gaussian kernel density estimates for the conductance and XRF data, normalizing
the density between 0 and 1, and rejecting data points with a kernel density below
0.3. Bandwidths of 5 × 10−3 μΩ−1 m−1 and 5 × 103 cps were used for the
conductance and XRF data, respectively.

Autonomous workﬂow step 8: algorithmic experiment planning. The experi-
ment parameters for each optimization experiment performed on the autonomous
laboratory were determined by the qEHVI55 multiobjective Bayesian optimization
algorithm. In brief, this algorithm proposes experiments expected to increase the
area underneath the Pareto front by the largest amount. More formally, the
algorithm proposes a batch of q experiments (q = 1 here, but q could be increased
to exploit parallelized experimentation), which are collectively expected to increase
the hypervolume between the Pareto front and a reference point by the largest
amount. The hypervolume is a generalization of volume to an arbitrary number of
dimensions; this generalization supports optimization with more than two objec-
tives. The reference point must be speciﬁed prior to the optimization and speciﬁes a
minimum value of interest for each objective.

The algorithm involves two major conceptual steps: modeling the objectives
from data and proposing the next experiment. In the conﬁguration used here, each
objective is assumed to be independent and is modeled with an independent
gaussian process (see Supplementary Figs. 5 and 6). Based on the models for each
objective, the expectation value of the hypervolume improvement associated with
any candidate experiment can be computed; the candidate experiment with the
largest expected hypervolume improvement is selected. We ran the qEHVI
algorithm using the implementation available in the open-source BoTorch
Bayesian optimization library68,69. We used a temperature reference point at the
upper limit of the experiment (280 °C) so that any outcome with a processing
temperature below this upper limit would be targeted. We used a dynamic
conductivity reference point set to 5% of the running observed maximum
conductivity. This dynamic reference point ensured that the optimization would
identify Pareto-optimal outcomes over a wide range of conductivity values and did
not require prior knowledge of the scale of conductivity values expected. We used
heteroskedastic Gaussian processes to model both the conductivity and the
temperature68. We assigned each conductivity point an uncertainty equal to 20% of
its value, which is comparable to the repeatability of the experiment
(Supplementary Fig. 13). Zero uncertainty was assigned to the temperature values,
which were manipulated rather than responding variables and were trivial
to model.

Calibration of XRF signal against reference samples. To enable palladium ﬁlm
thickness to be estimated from the XRF signal, a calibration procedure was per-
formed on sputtered palladium reference samples having four different nominal
thicknesses (10, 50, 100, and 250 nm). These samples were characterized by pro-
ﬁlometry and XRF. A linear relationship between the ﬁlm thickness and the XRF
counts was observed (see Supplementary Fig. 2). This relationship was used to
estimate the thickness of each sample from the XRF data.

The reference samples were sputtered onto clean glass microscope slides (see
cleaning procedure above) using a Univex 250 sputter deposition system with a DC
magnetron source at 100 W and an argon working pressure of 5 × 10−6 bar. The
deposition chamber base pressure is 5 × 10−9 bar. Films were deposited after 1 min
of pre-sputtering. The substrate holder rotated at 10 rpm. Nominal ﬁlm thickness
was monitored using a quartz crystal microbalance mounted in the sputter

chamber. A 2-inch diameter palladium sputter target was used (99.99%, ACI
Alloys). Step edges for proﬁlometry were obtained by placing strips of Kapton™
tape onto the substrates prior to sputtering and removing these after sputtering.
The substrates were rinsed with acetone and IPA to remove any Kapton™ tape
residue prior to performing proﬁlometry.

Proﬁlometry was performed on the reference samples using a Bruker DektakXT
stylus proﬁlometer. XRF was performed on the reference samples using the same
settings used for the drop-casted samples during the optimization campaigns (see
above).

Deposition and characterization of spray-coated samples. The spray coater was
built from an ultrasonic nozzle (Microspray, USA) mounted to a custom motorized
XYZ gantry system (Zaber Technologies Inc., Canada) above a hot plate (PC-420D,
Corning, USA). Precursor ink was fed to the nozzle by a syringe pump (cavro
centris pump PN: 30098790-B, Tecan Trading AG, Switzerland). The ultrasonic
spray nozzle was operated at 3 W and 120 kHz. For each recipe, a total of 700 µL of
precursor was sprayed onto a glass substrate (75 mm × 25 mm × 1 mm microscope
slides; VWR catalog no. 16004-430) placed on a custom aluminum ﬁxture
mounted to the hotplate. Approximate substrate temperatures were measured
using a thermocouple attached to a glass substrate with thermal cement. This
instrumented substrate was placed at a position on the hotplate ﬁxture symmetrical
to the position where the substrates to be coated were placed. The hotplate power
was adjusted until the steady-state temperature of the instrumented substrate was
within 4 °C of the desired temperature before spray coating each of the recipes
reported here. To achieve consistent thermal contact between the substrates and
the hotplate ﬁxture, both the instrumented substrate and substrate to be coated
were afﬁxed to the hotplate with thermal paste (TG-7, Thermaltake Technology
Co., Taiwan). The spray coater nozzle speed was 5.1 mm s−1, the nozzle-to-
substrate distance was 15 mm, the spray ﬂow rate was 2 µL s−1, and the carrier gas
ﬂow rate was 7 L min−1. When spraying, the nozzle moved in a serpentine pattern
consisting of twelve 50 mm lines with 25 mm spacing (see an illustration of the
pattern in Supplementary Fig. 14). The coating on each sample was produced by
repeating this spray pattern three times with no delay between passes. After spray
coating, the samples were left to anneal on the hot plate for 5 min.

The spray-coated palladium ﬁlms were characterized at 26 locations on a 2 × 13

grid within an 8 × 20 mm region of interest at the center of the ﬁlm (see
Supplementary Fig. 14). The amount of palladium at each location was measured
using the XRF microscope and converted to a ﬁlm thickness estimate by applying
the same calibration method used for the drop-cast ﬁlms. The ﬁlm conductance at
each location was measured using the 4-point probe system on the robot described
above. The ﬁlm conductivity was calculated at each of the 26 measurement
locations by combining the 4-point probe conductance and XRF ﬁlm thickness
values for that location using Eq. (1). The mean and standard deviations of the 26
resulting thickness and conductivity values are reported for each ﬁlm in
Supplementary Table 3.

Computer simulations of optimization algorithm performance. Computer
simulations were used to study the performance of the qEHVI algorithm for
optimizing the combustion synthesis experiments. A model of the experimental
response surface was built from the experimental data. Experimental optimizations
were then simulated by sampling the model using grid search, random search,
Sobol sampling, and the qEHVI and qParEGO algorithms. Optimization perfor-
mance was quantiﬁed with and without simulated experimental noise. The per-
formance of qEHVI relative to random sampling was quantiﬁed using the
acceleration factor (AF) and enhancement factor (EF) metrics59. These simulation
procedures are described in more detail below.

Models of the experimental response surface and noise. Gaussian process
regression was used to create a model of the experimental response surface using
the combined data from all four optimization campaigns. This model predicts the
experimental outputs (i.e., annealing temperature and conductivity) from the
experimental inputs (i.e., fuel-to-oxidizer ratio, fuel blend, total concentration, and
annealing temperature). Our model is composed of two separate Gaussian pro-
cesses, as implemented by the scikit-learn Python package67. Each Gaussian pro-
cess is regressed on a single experimental output (i.e., either temperature or
conductivity) and all four of the experimental inputs. The kernels used for the
conductivity (kcond) and temperature (ktemp) models are:

ð
kcond x; x

0

Þ ¼ klin x; x

ð

0

ð
Þ ´ kSE x; x

0

Þ þ knoise x; x

ð

0

Þ;

ð
ktemp x; x

0

Þ ¼ klin x; x

ð

0

Þ(cid:3) ´ kSE x; x
ð

0

Þ(cid:3);

ð
knoise x; x

0

Þ ¼ noise if x ¼ x

0

else 0;

ð2Þ

ð3Þ

ð4Þ

where klin is a constant kernel, kSE is a squared exponential kernel, and knoise is a
white noise kernel, and * indicates that the lengthscale of the kernel is ﬁxed to 1.
The four types of input data and two types of output data were each normalized

prior to training the model. To simplify the optimization to be strictly a
maximization problem, the temperature values (which must be minimized) were
multiplied by negative one. The leave-one-out cross-validation residuals (LOOCV;

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications

7


ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

Supplementary Figs. 4, 9, and 10 and Supplementary Table 4) are comparable to
the measured experimental uncertainties (Supplementary Table 1). We also plotted
the LOOCV residuals as a function of each input (Supplementary Fig. 6), each
modeled output (Supplementary Fig. 7), and sampling order (Supplementary
Fig. 8) and observed that the distribution of the residuals was largely random.

For the simulations with no noise, the model posterior means were used directly

to represent the experiment. For simulations with experimental noise, noisy
conductivity values were simulated by randomly sampling a modiﬁed
Maxwell–Boltzmann distribution. First, the Maxwell–Boltzmann distribution was
ﬂipped across the y-axis by negating the x term. Second, the mean of this
Maxwell–Boltzmann distribution was set to the noiseless model posterior mean.
Finally, the variance of the Maxwell–Boltzmann distribution was set to be equal to
the noise level (or variance) of the white noise kernel. We chose to employ
Maxwell–Boltzmann noise to model the experimental noise because of the
tendency of drop-casted samples to exhibit a wide range of downwards deviations
in the apparent conductivity due to the poor sample morphology.

The Maxwell–Boltzmann probability density function is

PB xð Þ ¼

r

(cid:4)

ﬃﬃﬃ
π

2

(cid:3)
x2exp (cid:2)x2
2a2
a3

;

ð5Þ

where a is the distribution parameter. Since we set the variance of
Maxwell–Boltzmann distribution (σ2
(σ2

B) equal to the white noise kernel noise level

noise)

σ2

noise

¼ σ2
B

¼ a2ð3π (cid:2) 8Þ
π

:

ð6Þ

We computed the distribution parameter for the Maxwell–Boltzmann-

distributed simulated experimental noise as:

ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
πσ
:
noise
3π (cid:2) 8
If subtracting the Maxwell–Boltzmann noise from the posterior mean resulted

a ¼

ð7Þ

r

in a value less than zero, the noisy model value was set to zero.

Sampling strategies. To compare the performance of closed-loop and open-loop
approaches, several sampling strategies (grid search, random search, Sobol sam-
pling, and the qEHVI and qParEGO algorithms) were used to sample both the
noise-free and noisy experimental models. Random sampling was performed by
generating samples from a uniform distribution across the entire normalized input
space. Sobol sampling was performed with a scrambling technique such that each
Sobol sequence is unique to yield a statistically meaningful distribution of
optimizations70. qEHVI and qParEGO are initiated with ten scrambled Sobol
points. The qEHVI algorithm was conﬁgured as it was for the physical experiments
detailed above. The qParEGO algorithm was conﬁgured using the default settings,
except for the reference point which was conﬁgured in the same way done for
qEHVI. The complete benchmarking results are shown in Supplementary Fig. 11.

Simulated optimization campaigns. The performance of each sampling strategy
(grid, random, Sobol, qParEGO, and qEHVI) was determined both with and
without experimental noise. Each simulated optimization campaign was performed
for 1000 replicates and 100 experimental iterations, except for random which was
performed for 100,000 iterations for use in the acceleration calculations (shown in
Fig. 4b). If an optimization algorithm produced an error during optimization, then
that replicate was removed and repeated.

Pareto front and hypervolume. The Pareto front is deﬁned by the set of samples
for which no other sample simultaneously improves all the objectives. When
assessing the performance of a simulation, the hypervolume was computed using
the least desirable value of each objective function (the nadir objective vector) as
the reference point (i.e., zero conductivity and 280 °C temperature). This reference
point was held constant for evaluating all of the simulated optimization campaigns.
We assessed the performance of the noisy optimizations such that the only dif-
ference between the noisy and noise-free optimizations was the information pro-
vided to the optimization algorithm. To perform this assessment, we followed the
procedure described by Bakshy and coworkers58 wherein the hypervolume for
optimizations using the noisy experimental model were calculated from the
equivalent point from the noiseless model. Since each objective of the model is
normalized to the range [0, 1], the hypervolume of the model is in the range [0, 1].
For each simulated optimization campaign, the normalized hypervolume was
calculated at each iteration. When calculating acceleration and enhancement fac-
tors, each of the 1000 simulated qEHVI campaigns was compared to each of the
1000 simulated random campaigns, resulting in 1,000,000 comparisons.

Calculation of acceleration and enhancement factor. The acceleration factor
quantiﬁes how much faster one sampling technique is than another (Eq. 5). For
example, if sampling technique B requires 40 samples to reach the performance
attained by technique A after 20 samples, the acceleration factor of A relative to B

at 20 samples is 2.

(cid:3)

(cid:4)

AFA:B na

;

¼ nb
na
(cid:4)

(cid:3)

(cid:4)

(cid:3)
≥ PA na

;

(cid:4)

(cid:3)

ð8Þ

s:t: PB nb

; min nb
is the acceleration of technique A with respect to B at na samples,
where AFA:B na
ðnÞ is the performance of technique i at n samples. Note that it is possible for
and Pi
sampling technique A to outperform B such that there exists no value of nb where
≥ PA. In these cases, more samples with technique B are required to make the
PB
comparison, otherwise AFA:B is not calculable. If AFA:B is not calculable, then a
lower bound acceleration factor is calculated by assuming that the slow sampling
technique would beat the fast sampling technique if it observed one more sample.
The acceleration factor in Fig. 4b was reported until these lower bound estimates
compose more than 25% of all of the acceleration comparisons.

The enhancement factor of one sampling technique with respect to another for
a given number of samples is deﬁned as the ratio of their performance values for
the same number of observations (Eq. 6). For example, if sampling technique A
reaches a performance value of 7 after 20 samples, and technique B reaches a
performance value of 2 after 20 samples, the enhancement of technique A is 3.5 at
20 samples.

ðnÞ
ðnÞ
ðnÞ is the acceleration factor of sampling technique A with respect to B

EFA:B nð Þ ¼ PA
PB

where EFA:B
after n samples. When PA nð Þ ¼ 0 and PB nð Þ ¼ 0, then EFA:B nð Þ ¼ 1. When
PA nð Þ > 0 and PB nð Þ > 0, then EFA:B nð Þ is not calculable. To compare the AF and EF
from the repeated simulations, the median, geometric mean and interquartile range
were calculated.

ð9Þ

;

Data availability
The raw and processed data generated by the self-driving laboratory in this study is
available at https://github.com/berlinguette/ada. All other data related to this paper is
available from the corresponding author upon request.

Code availability
All code used in this study was based on open-source Python packages listed in the
supplementary information.

Received: 1 June 2021; Accepted: 26 January 2022;

References
1. Tabor, D. P. et al. Accelerating the discovery of materials for clean energy in

the era of smart automation. Nat. Rev. Mater. 3, 5–20 (2018).
Stein, H. S. & Gregoire, J. M. Progress and prospects for accelerating materials
science with automated and autonomous workﬂows. Chem. Sci. 10, 9640–9649
(2019).

2.

3. Häse, F., Roch, L. M. & Aspuru-Guzik, A. Next-generation experimentation

with self-driving laboratories. Trends Chem. 1, 282–291 (2019).

4. MacLeod, B. P., Parlane, F. G. L., Brown, A. K., Hein, J. E. & Berlinguette, C. P.
Flexible automation accelerates materials discovery. Nat. Mater. https://
doi.org/10.1038/s41563-021-01156-3 (2021).

5. Ament, S. et al. Autonomous materials synthesis via hierarchical active

learning of nonequilibrium phase diagrams. Science Advances 7, eabg4930
(2021).
Bash, D. et al. Multi‐ﬁdelity high‐throughput optimization of electrical
conductivity in P3HT‐CNT composites. Adv. Funct. Mater. 2102606 (2021).

6.

7. Nikolaev, P. et al. Autonomy in materials research: a case study in carbon

nanotube growth. npj Comput. Mater. 2, 16031 (2016).

8. MacLeod, B. P. et al. Self-driving laboratory for accelerated discovery of thin-

ﬁlm materials. Sci. Adv. 6, eaaz8867 (2020).
Langner, S. et al. Beyond ternary OPV: high-throughput experimentation and
self-driving laboratories optimize multicomponent systems. Adv. Mater. 32,
e1907801 (2020).

9.

10. Li, J. et al. Autonomous discovery of optically active chiral inorganic

perovskite nanocrystals through an intelligent cloud lab. Nat. Commun. 11,
2046 (2020).

11. Gongora, A. E. et al. A Bayesian experimental autonomous researcher for

mechanical design. Sci. Adv. 6, eaaz1708 (2020).

12. Burger, B. et al. A mobile robotic chemist. Nature 583, 237–241 (2020).
13. Wang, L., Karadaghi, L. R., Brutchey, R. L. & Malmstadt, N. Self-optimizing
parallel milliﬂuidic reactor for scaling nanoparticle synthesis. Chem. Commun.
56, 3745–3748 (2020).

8

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications


NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

ARTICLE

14. Shimizu, R., Kobayashi, S., Watanabe, Y., Ando, Y. & Hitosugi, T.

45. Perelaer, J. et al. Printed electronics: the challenges involved in printing

Autonomous materials synthesis by machine learning and robotics. APL
Mater. 8, 111110 (2020).

15. Dave, A. et al. Autonomous discovery of battery electrolytes with robotic

experimentation and machine learning. Cell Rep. Phys. Sci. 1, 100264 (2020).
16. Deneault, J. R. et al. Toward autonomous additive manufacturing: Bayesian
optimization on a 3D printer. MRS Bull. https://doi.org/10.1557/s43577-021-
00051-1 (2021).

17. Hall, B. L. et al. Autonomous optimisation of a nanoparticle catalysed
reduction reaction in continuous ﬂow. Chem. Commun. https://doi.org/
10.1039/d1cc00859e (2021).

18. Krishnadasan, S., Brown, R. J. C., deMello, A. J. & deMello, J. C. Intelligent routes
to the controlled synthesis of nanoparticles. Lab Chip 7, 1434–1441 (2007).
19. Moore, J. S. & Jensen, K. F. Automated multitrajectory method for reaction
optimization in a microﬂuidic system using online IR analysis. Org. Process
Res. Dev. 16, 1409–1415 (2012).

20. Walker, B. E., Bannock, J. H., Nightingale, A. M. & deMello, J. C. Tuning reaction
products by constrained optimisation. React. Chem. Eng. 2, 785–798 (2017).
21. Salley, D. et al. A nanomaterials discovery robot for the Darwinian evolution
of shape programmable gold nanoparticles. Nat. Commun. 11, 2771 (2020).
22. Epps, R. W. et al. Artiﬁcial chemist: an autonomous quantum dot synthesis

bot. Adv. Mater. 32, e2001626 (2020).

23. Christensen, M. et al. Data-science driven autonomous process optimization.

Commun. Chem. 4, 1–12 (2021).

24. Mekki-Berrada, F. et al. Two-step machine learning enables optimized

nanoparticle synthesis. npj Comput. Mater. 7, 1–10 (2021).

25. Abdel-Latif, K. et al. Self‐driven multistep quantum dot synthesis enabled by

autonomous robotic experimentation in ﬂow. Adv. Intell. Syst. 3, 2000245 (2021).

26. Grizou, J., Points, L. J., Sharma, A. & Cronin, L. A curious formulation robot

enables the discovery of a novel protocell behavior. Sci. Adv. 6, eaay4237 (2020).

27. Schweidtmann, A. M. et al. Machine learning meets continuous ﬂow

chemistry: automated optimization towards the Pareto front of multiple
objectives. Chem. Eng. J. 352, 277–282 (2018).

28. Cao, L. et al. Optimization of formulations using robotic experiments driven

devices, interconnects, and contacts based on inorganic materials. J. Mater.
Chem. 20, 8446–8453 (2010).

46. Li, D., Lai, W.-Y., Zhang, Y.-Z. & Huang, W. Printable transparent conductive

ﬁlms for ﬂexible electronics. Adv. Mater. 30, 1704738 (2018).

47. Cochran, E. A. et al. Role of combustion chemistry in low-temperature
deposition of metal oxide thin ﬁlms from solution. Chem. Mater. 29,
9480–9488 (2017).

48. Wang, B. et al. Marked cofuel tuning of combustion synthesis pathways for
metal oxide semiconductor ﬁlms. Adv. Electron. Mater. 5, 1900540 (2019).
49. Plassmeyer, P. N., Mitchson, G., Woods, K. N., Johnson, D. C. & Page, C. J.
Impact of relative humidity during spin-deposition of metal oxide thin ﬁlms
from aqueous solution precursors. Chem. Mater. 29, 2921–2926 (2017).
50. Kumar, A., Wolf, E. E. & Mukasyan, A. S. Solution combustion synthesis of
metal nanopowders: copper and copper/nickel alloys. AIChE J. 57, 3473–3479
(2011).

51. Manukyan, K. V. et al. Solution combustion synthesis of nano-crystalline

metallic materials: mechanistic studies. J. Phys. Chem. C 117, 24417–24427
(2013).

52. Mitzi, D. Solution Processing of Inorganic Materials (Wiley, 2008).
53. Cochran, E. A., Woods, K. N., Johnson, D. W., Page, C. J. & Boettcher, S. W.
Unique chemistries of metal-nitrate precursors to form metal-oxide thin ﬁlms
from solution: materials for electronic and energy applications. J. Mater.
Chem. A 7, 24124–24149 (2019).

54. Pujar, P., Gandla, S., Gupta, D., Kim, S. & Kim, M. Trends in low‐temperature
combustion derived thin ﬁlms for solution‐processed electronics. Adv.
Electron. Mater. 6, 2000464 (2020).

55. Daulton, S., Balandat, M. & Bakshy, E. Differentiable Expected Hypervolume
Improvement for Parallel Multi-Objective Bayesian Optimization. Advances in
Neural Information Processing Systems 33 (eds. Larochelle, H. et al.)
9851–9864 (Curran Associates, Inc., 2020).

56. Knowles, J. ParEGO: a hybrid algorithm with on-line landscape

approximation for expensive multiobjective optimization problems. IEEE
Trans. Evol. Comput. 10, 50–66 (2006).

by machine learning DoE. Cell Rep. Phys. Sci. 2, 100295 (2021).

57. Paria, B., Kandasamy, K. & Póczos, B. A Flexible Framework for Multi-

29. Maaliou, O. & McCoy, B. J. Optimization of thermal energy storage in packed

columns. Sol. Energy 34, 35–41 (1985).

30. Ahmadi, M. H., Ahmadi, M. A., Bayat, R., Ashouri, M. & Feidt, M. Thermo-
economic optimization of Stirling heat pump by using non-dominated sorting
genetic algorithm. Energy Convers. Manag. 91, 315–322 (2015).

31. Li, Z., Pradeep, K. G., Deng, Y., Raabe, D. & Tasan, C. C. Metastable high-
entropy dual-phase alloys overcome the strength-ductility trade-off. Nature
534, 227–230 (2016).

32. Zhang, L. et al. Correlated metals as transparent conductors. Nat. Mater. 15,

204–210 (2016).

33. Park, H. B., Kamcev, J., Robeson, L. M., Elimelech, M. & Freeman, B. D.

Maximizing the right stuff: The trade-off between membrane permeability and
selectivity. Science 356, eaab0530 (2017).

34. Oviedo, F. et al. Bridging the gap between photovoltaics R&D and

manufacturing with data-driven optimization. Preprint at https://arxiv.org/
2004.13599v1 (2020).

35. Liu, L. et al. Making ultrastrong steel tough by grain-boundary delamination.

Science 368, 1347–1352 (2020).

36. Ramirez, I., Causa’, M., Zhong, Y., Banerji, N. & Riede, M. Key tradeoffs
limiting the performance of organic photovoltaics. Adv. Energy Mater. 8,
1703551 (2018).

37. Kirkey, A., Luber, E. J., Cao, B., Olsen, B. C. & Buriak, J. M. Optimization of
the bulk heterojunction of all-small-molecule organic photovoltaics using
design of experiment and machine learning approaches. ACS Appl. Mater.
Interfaces 12, 54596–54607 (2020).

38. Ren, S. et al. Molecular electrocatalysts can mediate fast, selective CO2

reduction in a ﬂow cell. Science 365, 367–369 (2019).

39. Baumeler, T. et al. Minimizing the trade-off between photocurrent and
photovoltage in triple-cation mixed-halide perovskite solar cells. J. Phys.
Chem. Lett. 11, 10188–10195 (2020).

40. Voskanyan, A. A., Li, C.-Y. V. & Chan, K.-Y. Catalytic palladium ﬁlm

deposited by scalable low-temperature aqueous combustion. ACS Appl. Mater.
Interfaces 9, 33298–33307 (2017).

41. Mauritz, K. A. & Moore, R. B. State of understanding of naﬁon. Chem. Rev.

104, 4535–4585 (2004).

42. MacDonald, W. A. et al. Latest advances in substrates for ﬂexible electronics. J.

Soc. Inf. Disp. 15, 1075 (2007).

43. Kim, M.-G., Kanatzidis, M. G., Facchetti, A. & Marks, T. J. Low-temperature
fabrication of high-performance metal oxide thin-ﬁlm electronics via
combustion processing. Nat. Mater. 10, 382–388 (2011).

44. Hennek, J. W., Kim, M.-G., Kanatzidis, M. G., Facchetti, A. & Marks, T. J.

Exploratory combustion synthesis: amorphous indium yttrium oxide for thin-
ﬁlm transistors. J. Am. Chem. Soc. 134, 9593–9596 (2012).

Objective Bayesian Optimization using Random Scalarizations. In Proceedings
of The 35th Uncertainty in Artiﬁcial Intelligence Conference (eds. Adams, R.
P. & Gogate, V.) 115 766–776 (PMLR, 2020).

58. Daulton, S., Balandat, M. & Bakshy, E. Parallel Bayesian Optimization of
Multiple Noisy Objectives with Expected Hypervolume Improvement.
Advances in Neural Information Processing Systems 34 (eds. Ranzato, M. et al.)
(Curran Associates, Inc., 2021).

59. Rohr, B. et al. Benchmarking the acceleration of materials discovery by

sequential learning. Chem. Sci. 11, 2696–2706 (2020).

60. Yu, X. et al. Spray-combustion synthesis: efﬁcient solution route to high-
performance oxide transistors. Proc. Natl Acad. Sci. USA 112, 3217–3222
(2015).

61. Matula, R. A. Electrical resistivity of copper, gold, palladium, and silver. J.

Phys. Chem. Ref. Data 8, 1147–1298 (1979).

62. Shi, Y. S. Electrical resistivity of RF sputtered Pd ﬁlms. Phys. Lett. A 319,

555–559 (2003).

63. Hloch, H. & Wissmann, P. The electrical resistivity of thin pd ﬁlms grown on

Si(111). Phys. Status Solidi A 145, 521–526 (1994).

64. Anton, R., Häupl, K., Rudolf, P. & Wißmann, P. Electrical and structural

properties of thin palladium ﬁlms. Z. f.ür. Naturforsch. A 41, 665–670 (1986).
65. Delima, R. S., Sherbo, R. S., Dvorak, D. J., Kurimoto, A. & Berlinguette, C. P.
Supported palladium membrane reactor architecture for electrocatalytic
hydrogenation. J. Mater. Chem. A 7, 26586–26595 (2019).
66. Bernhardsson, E. & Freider, E. L. https://github.com/spotify/luigi.
67. Pedregosa, F. et al. Scikit-learn: machine learning in Python. J. Mach. Learn.

Res. 12, 2825–2830 (2011).

68. Balandat, M. et al. BoTorch: a framework for efﬁcient Monte-Carlo Bayesian
optimization. Advances in Neural Information Processing Systems 33 (eds.
Larochelle, H. et al.) 21524–21538 (Curran Associates, Inc., 2020).

69. Bakshy, E. et al. Advances in Neural Information Processing Systems vol. 31

70. Owen, A. B. Scrambling Sobol’ and Niederreiter–Xing Points. J. Complex. 14,

(The MIT Press, 2018).

466–489 (1998).

Acknowledgements
The authors are grateful to Natural Resources Canada’s Energy Innovation Program
(EIP2-MAT-001) for ﬁnancial support. The authors are grateful to the Canadian Natural
Science and Engineering Research Council (RGPIN-2018-06748), Canadian Foundation
for Innovation (229288), Canadian Institute for Advanced Research (BSE-BERL-162173),
and Canada Research Chairs for ﬁnancial support. B.P.M., F.G.L.P., T.D.M. and C.P.B.
acknowledge support from the SBQMI’s Quantum Electronic Science and Technology

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications

9


ARTICLE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-022-28580-6

Initiative, the Canada First Research Excellence Fund, and the Quantum Materials and
Future Technologies Program. We would like to acknowledge the many open-source
software communities without whose efforts this project would not have been possible.
Please see the supplementary information for further details.

Author contributions
C.P.B. conceived and supervised the project. B.P.M., K.E.D. and F.G.L.P. designed and
performed the autonomous optimization experiments. M.B.R., K.O., C.W., K.E.D., O.P.,
M.S.E., B.P.M. and F.G.L.P. developed the robotic hardware. M.S.E., O.P. and K.E.D.
developed and conﬁgured the robotic control software. F.G.L.P. and T.H.H. developed
the data analysis software with input from N.T., K.E.D. and B.P.M., F.G.L.P., M.M. and
B.P.M. performed and analyzed the simulations. M.S.E. and B.P.M. conﬁgured the EVHI
optimization algorithm and interfaced it with the self-driving laboratory. K.O., H.N.C.
and C.C.R. developed the spray coater hardware and software. C.C.R. performed the
spray coating experiments. N.T. performed additional data analysis. D.J.D. performed
additional experiments. All authors participated in the writing of the manuscript.

Competing interests
The authors declare no competing interests.

Additional information
Supplementary information The online version contains supplementary material
available at https://doi.org/10.1038/s41467-022-28580-6.

Correspondence and requests for materials should be addressed to Curtis P.
Berlinguette.

Peer review information Nature Communications thanks the anonymous reviewers for
their contribution to the peer review of this work.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons license, and indicate if changes were made. The images or other third party
material in this article are included in the article’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons license and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from
the copyright holder. To view a copy of this license, visit http://creativecommons.org/
licenses/by/4.0/.

© The Author(s) 2022

10

NATURE COMMUNICATIONS | 

(2022) 13:995 | https://doi.org/10.1038/s41467-022-28580-6 | www.nature.com/naturecommunications
