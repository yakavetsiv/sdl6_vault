---
type: literature-note
source_note: "Papers/Paper - sciadv.adt1851.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/sciadv.adt1851.pdf"
converter: "microsoft/markitdown"
---
S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

C A N C E R
Machine learning- assisted exploration of
multidrug- drug administration regimens for
organoid arrays
Ilya Yakavets1†, Sina Kheiri2†, Jennifer Cruickshank3, Riley J. Hickman4,5, Faeze Rakhshani1,
Matteo Aldeghi4,5,6,7, Ella M. Rajaonson4,6, Edmond W.K. Young2,8, Alán Aspuru- Guzik4,5,6,9,10,11*,
David W. Cescon3*, Eugenia Kumacheva1,8,9*

Combination therapies enhance the therapeutic effect of cancer treatment; however, identifying effective inter-
dependent doses, durations, and sequences of multidrug administration regimens is a time-  and labor- intensive
task.  Here,  we  integrated  machine  learning,  automation,  and  large  microfluidic  arrays  of  cancer  spheroids  or
patient- derived organoids formed in a tissue- mimetic hydrogel to achieve notable acceleration of the discovery
of effective multidrug administration regimens. For the clinically approved drug combination, we found a sequen-
tial administration regimen leading to a substantial reduction in the total drug dose, in comparison with concur-
rent drug supply, both at comparable drug efficacy. For the drugs that are currently under clinical development,
we found a synergistic effect of concurrently administered drugs and showed that the synergy diminishes for the
sequential drug supply. The developed strategy holds promise for the discovery of effective combination thera-
pies for advanced cancer treatment, including personalized chemotherapies.

copyright © 2025 the
Authors, some rights
reserved; exclusive
licensee American
Association for the
Advancement of
Science. no claim to
original U.S.
Government Works.
distributed under a
creative commons
Attribution
noncommercial
license 4.0 (cc BY- nc).

INTRODUCTION
The  heterogeneous  and  dynamic  nature  of  cancer  complicates  the
development of effective therapies for the treatment of human ma-
lignancies. This is true of breast cancer, one of the most common
cancers diagnosed globally, which exhibits both intra and interpa-
tient  heterogeneity  (1–3).  Over  the  past  several  decades,  systemic
drug–based therapy has significantly improved the survival of pa-
tients diagnosed with breast cancer. Yet, because of the heterogene-
ity of the disease and the trend in tumor evolution, the development
of drug resistance remains a challenge.

To address this challenge, multidrug chemotherapy has become
the  cornerstone  of  curative  adjuvant  therapy,  as  it  is  based  on  the
principle that an appropriately selected drug combination can en-
hance the therapeutic effect by attacking different biochemical tar-
gets  and  overcoming  drug  resistance  in  heterogeneous  tumor  cell
populations. Combination therapies offer a higher therapeutic effica-
cy for metastatic breast cancer than single- agent therapy (4–6). Typi-
cally, multidrug chemotherapy is delivered by intravenous infusions

1department of chemistry, University of toronto, 80 Saint George Street, toronto, On
M5S 3h6, canada. 2department of Mechanical & industrial engineering, University of
toronto, 5 King’s college Road, toronto, On M5S 3G8, canada. 3Princess Margaret
cancer centre, University health network, 610 University Avenue, toronto, On M5G
2c1, canada. 4chemical Physics theory Group, department of chemistry, University
of toronto, 80 Saint George street, toronto, On M5S 3h6, canada. 5department of
computer Science, University of toronto, 40 Saint George street, toronto, On M5S
2e4, canada. 6vector institute for Artificial intelligence, 661 University Avenue,
toronto, On M5G 1M1, canada. 7Bayer Research and innovation center, 238 Main
Street, cambridge, MA 02142, USA. 8institute of Biomedical engineering, University
of  toronto,  164  college  street,  toronto,  On  M5S  3G9,  canada.  9department  of
chemical engineering and Applied chemistry, University of toronto, 200 college
Street, toronto,  On  M5S  3e5,  canada.  10department  of  Materials  Science  &  engi-
neering, University of toronto, 184  college Street, toronto, On M5S 3e4,  canada.
11canadian  institute  for  Advanced  Research,  661  University  Avenue, toronto,  On
M5G 1M1, canada.
*corresponding author. email: eugenia. kumacheva@ utoronto. ca (e.K.); dave. cescon@
uhn. ca (d.W.c.); aspuru@ utoronto. ca (A.A.- G.)
†these authors contributed equally to this work.

based on the most successful empirically determined schedule test-
ed in clinical trials (7). Effective concurrent multiagent chemother-
apy  is  expected  to  meet  the  following  criteria:  (i)  an  independent
effect of each agent with no cross- resistance, (ii) a synergistic effect
of different agents, and (iii) nonoverlapping safety profiles of the
agents (8). Addressing these criteria should enhance therapeutic ef-
ficiency by targeting cancer cells more selectively and reducing tox-
icity in normal tissues. Unfortunately, currently used combination
therapies do not meet all three criteria, and drugs are generally ad-
ministered at suboptimal doses due to dose- limiting toxicities (9).

The sequential administration of individual drugs may circum-
vent  some  of  these  limitations  (10),  taking  advantage  of  dynamic
changes that occur in tumor or host tissues in response to each agent
and leading to a maintained or superior response rate and, poten-
tially, to a lower toxicity risk and improvement of the patient’s qual-
ity of life (6, 11–13). Sequential regimens of combination therapies
may be especially appropriate in frail or elderly patients that are un-
able  to  tolerate  the  toxicity  of  multiagent  chemotherapy  or  in  pa-
tients  with  slowly  growing  tumors.  Because  identifying  effective
concurrent or sequential drug administration regimens—e.g., a par-
ticular drug sequence, dose, and time—is a challenging time- , cost- ,
and labor- intensive task, it is highly desirable to explore this multi-
dimensional parameter space by using nonconventional strategies.
Furthermore, it necessitates the development of reliable preclinical
models that capture the complexity of the tumor environment and
permit  each  parameter  to  be  modeled  with  adequate  throughput.
These challenges in the optimization of combination chemothera-
pies stimulate the development of innovative strategies aimed at ex-
ploring multidimensional parameter spaces.

Multicellular  cancer  spheroids  and  organoids  have  emerged  as
promising in vitro cancer models that recapitulate many features of
malignant tumors (14, 15). The limitations of these models include
a limited capacity to capture tumor microenvironments (16), a broad
distribution of spheroid and organoid dimensions, high reagent con-
sumption,  and  a  lack  of  physiological  flow  (17–19).  Combining

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

1 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

microfluidics (MFs) and organ- on- a- chip models yields uniformly
sized tumor spheroids and organoids, thus reducing variability and
enhancing the reproducibility of experiments (20, 21), Moreover,
MF platforms recapitulate interstitial flow, thereby providing more
physiologically relevant tumor models (22). For example, a MF plat-
form integrated with lung cancer spheroids was used to examine the
effect of drugs on epithelial- mesenchymal transition in cancer pro-
gression (23). In another study, an automated MF platform was used
to evaluate the efficacy of 20 independent chemotherapy protocols
on 200 samples of patient- derived pancreatic organoids (24). A no-
table variability in drug responses between different patients high-
lighted the importance of personalized approaches to cancer treatment.
Yet,  currently  used  MF  tumor- on- a- chip  platforms  have  a  limited
capacity in the exploration of large parameter space in the screening
of multidrug combinations.

Integration of MF tumor- on- a- chip models with machine learn-
ing (ML) in closed- loop platforms offers predictive capabilities that
can enable time-  and labor- efficient prioritization of effective multi-
drug combinations (25). Similar to evolutionary algorithms (26, 27),
Bayesian optimization (BO) frameworks enable rapid identification
and  optimization  of  the  multidimensional  parameter  space  with
continuous  (e.g.,  drug  dose),  discrete  (e.g.,  administration  time),
and categorical (e.g., drug sequence) input features (28–32). What
distinguishes  BO  from  other  approaches  is  the  strong  emphasis
on sampling efficiency, that is, optimizing a desired property with
the lowest number of experiments possible. In particular, based on
the  tumor  cells′  response  to  treatment,  the  Gryffin  algorithm  can
adaptively learn to propose drug sequences, doses, and times with
greater therapeutic effects while constraining the drug dose or the
total treatment time (33, 34). The time- efficient prioritization of the
most promising therapy is generally achieved by maintaining a bal-
ance  between  the  exploitation  (capitalizing  on  knowledge  already
gained) and the exploration (discovery of new features) of the mul-
tidimensional parameter space (32). The advantages of such a strat-
egy  lend  themselves  to  the  problem  of  evaluating  and  optimizing
multidrug therapeutic strategies for cancer. A rational approach is
the delivery of combination treatments with the largest therapeutic
index while minimizing drug doses (that is, concentrations and du-
rations of exposure).

Here, we report the integration of the BO strategy, automation,
and a tumor- on- a- chip MF platform for the identification of effec-
tive combination therapies with concurrent or sequential drug ad-
ministration for breast cancer treatment. We developed a closed- loop
workflow, an iterative process where the output from the last step of
the preceding iteration was used to automatically generate the in-
puts for the first step of the subsequent iteration. To identify effec-
tive regimens for the administration of drug combinations, we used
the Gryffin algorithm, which supports optimization over a multidi-
mensional parameter space with continuous, discrete, and categorical
variables (28, 29). The Gryffin also supported batched BO, suggesting
more than one set of combination therapies per iteration, thus en-
abling  parallel  testing  of  multiple  treatment  conditions  within  a
single  MF  platform.  Furthermore,  the  algorithm  handled  a  priori
known constraints on the parameter space (e.g., the total drug dos-
age) (35), suggesting only favorable treatment conditions.

The  main  objective  of  our  work  was  to  develop  a  strategy  that
avoids extensive systematic experiments that are time- , labor- , and
cost- intensive.  To  develop  the  platform,  we  first  used  ML- driven
closed- loop experiments to determine the most effective three- drug

combination,  that  is,  5- fluorouracil  (5- FU),  doxorubicin  (DOX),
and cyclophosphamide (CPA), which were supplied concurrently to
breast cancer spheroids. Subsequently, by leveraging automatic con-
trol of fluid flow in the MF platform, these drugs were administered
sequentially. For the comparable drug efficacy, a substantial reduction
in the total administered drug dose was achieved in the sequential
administration regimen. Next, using patient- derived breast cancer
organoids,  we  tested  simultaneous  and  sequential  administration
modes for the combinations of olaparib (OLA) and IBET- 762 drugs
that are currently under clinical development. For this drug combi-
nation, we found a synergistic effect of concurrently administered
drugs,  highlighting  the  importance  of  concurrent  rather  than  se-
quential drug administration.

RESULTS
A closed- loop MF platform integrated with ML
Figure 1A illustrates a closed- loop ML- driven MF platform for the
exploration and identification of effective drug administration regi-
mens for combination therapies. An array of breast cancer spheroids
or patient- derived organoids (PDOs) was formed from the MCF- 7
cell line or isolated breast cancer cells, respectively, in the microwells
of the MF device and, subsequently, subjected to treatment with drug
combinations at varying doses, sequences, and time intervals (Fig. 1A,
step 1). The efficacy of spheroid or PDO treatment with drugs was
evaluated by examining cell viability via LIVE/DEAD assays (Fig. 1A,
step 2) and validated using confocal laser scanning microscopy and
flow  cytometry. The  results  of  the  analysis  of  LIVE/DEAD  assays,
that is, the combination index (CI) and cell viability were provided
as  optimization  targets  to  Gryffin  for  BO- based  experiment  plan-
ning.  The  CI  was  used  to  identify  synergistic  drug  doses,  with  a
clinically relevant threshold for synergy defined as CI ≤ −0.1 (based
on the Bliss model) (36). Prioritizing the CI as a primary objective
over cell viability prevented the selection of maximum drug doses,
which could mislead the algorithm by identifying clinically irrele-
vant combinations since multiple combinations could result in simi-
larly low cell viability values. On the basis of the results accumulated
from the previous- step iteration, Gryffin aided in the next- step se-
lection of drug doses in multidrug combination, the sequence in which
individual  drugs  are  supplied,  and  the  duration  of  their  supply
(Fig. 1A, steps 3 and 4). After identifying the most effective regimen
aligned with a target CI and cell viability, one additional iteration
was performed. By leveraging model- based optimization within the
defined constraints, this closed- loop workflow enabled the identifi-
cation  of  promising  drug  supply  regimens  from  a  broad  range  of
drug administration conditions.

The spheroids and PDOs were formed in cylindrical microwells
of the MF device, which were organized in four parallel rows con-
nected to a common inlet for supplying cell culture medium or drug
solution and a common outlet (Fig. 1B). The design and dimensions
of the MF device are shown in fig. S1. In the rest of the paper, we
refer to this design as a “quadruplet.” The height and diameter of
the microwells were 330 and 300 μm, respectively, and the supply-
ing channels were 200- μm wide and 80- μm tall. A size chip of 75 mm
by  50  mm  accommodated  12  quadruplets,  with  each  quadruplet
containing  100  microwells  (Fig.  1C),  thus  enabling  the  growth  and
analysis  of  1200  spheroids  or  PDOs  in  response  to  12  drug  supply
regimens. The spheroids and PDOs were formed from droplets of a
dense  cell  suspension  [for  spheroids  (1.5  ×  105  cells/μl)  and  for

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

2 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

Fig. 1. Closed- loop MF tumor- on- a- chip platform integrated with ML. (A) Schematics of the closed- loop workflow for drug screening. (B) design of the quadruplet
unit with 25 microwells in each row. Scale bar, 1 mm. (C) MF device containing 12 quadruplets. Scale bar, 1 cm. (D) Schematics of the automated fluidic system for sequen-
tial administration of multidrug combinations. PdO, patient- derived organoid.

PDOs (1.2 × 105 cells/μl)] in the solution containing precursors for
a biomimetic hydrogel (referred to as EKGel) (fig. S2 and Materials
and Methods) (37–39).

A  fully  automated  fluidic  system  was  developed  to  supply  and
remove drug solutions from the rows of the MF device (Fig. 1D).
The  solutions  were  supplied  at  specific  concentrations  in  the  se-
quence recommended by Gryffin. Drug solutions (drug A, B, or C)
were  collected  from  the  corresponding  reservoirs  (fig.  S3A)  and
supplied  to  the  inlet  and  outlet  of  the  quadruplet  using  a  syringe
pump (fig. S3B). After subjecting spheroids or PDOs to a particular
drug solution for the desired time, the solution was withdrawn from the
MF device (fig. S3C) and transferred to a waste container (fig. S3D),

and  another  drug  was  supplied  following  the  algorithm- proposed
drug sequence.

Identification of effective combination therapy for spheroids
To develop a closed- loop platform, we used spheroids formed from
breast adenocarcinoma MCF- 7 cells and selected the combination
of three drugs used for breast cancer chemotherapy (40, 41), that is,
5- FU, DOX (known as Adriamycin), and CPA (known as Cytoxan).
Before screening the effect of this multidrug combination, we evalu-
ated the efficacy of each individual drug (fig. S4). Cell viability was
accessed  by  staining  spheroids  with  calcein- AM  (live  cells;  green
color) and propidium iodide (PI) (dead cells; red color) (fig. S5).

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

3 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

Solutions of DOX, CPA, and 5- FU were supplied to MCF- 7 spher-
oids for 48 hours. The Gryffin recommended drug concentrations
for  iterative  experiments  and  prioritized  the  most  effective  multi-
drug combination.

Figure 2A shows a bright- field image of the fragment of the array
of  300- μm- diameter  microwells  compartmentalizing  MCF- 7  cell–
laden droplets. The cells cultured in the MF device for 24 hours were
viable, as shown for spheroids stained with calcein- AM (live cells)
and PI (dead cells) (Fig. 2B). Spheroid formation after 24 hours was
verified by cell immunofluorescence (IF) staining with E- cadherin an-
tibodies and phalloidin. Figure 2C shows the expression of E- cadherin
[fluorescein  isothiocyanate  (FITC);  green],  a  key  component  of  the
adherens junctions between the cells, the distribution of the actin
cytoskeleton  [phalloidin;  red],  and  cell  nuclei  [4′,6- diamidino- 2-
phenylindole (DAPI); blue] in the spheroids. After 48 hours, the cells
were actively proliferating, as shown by their positive staining with
the Ki- 67 antibody (Fig. 2D).

On the basis of spheroid response to individual drugs, we deter-
mined  the  parameter  space  to  be  explored  for  drug  combinations
(table S1). The calculated values of median effective concentration
(EC50) indicated a higher potency of cell cycle nonspecific DOX, in
comparison with 5- FU and CPA, the drugs targeting the cell cycle.
The fitted dose- response curves were used to compute the theoreti-
cal cell viability, CVtheor, for drug combinations by multiplying the cell
viabilities corresponding to individual drugs at concentrations pro-
posed by the Gryffin algorithm (CVtheor = CVDOX × CV5- FU × CVCPA).
The efficacy of drug combination in the iterative process was as-
sessed by the metric for drug synergy, that is, the values of the CI
and experimental cell viability, CVexp. The targets or “objectives” in
this process were CI ≤ −0.1 and CVexp ≤ 70%. The concentrations of
the concurrently administrated drugs (expressed as log [Cdrug]) were
used as the parameters to be optimized by Gryffin. The algorithm’s
proposals were constrained to ensure CVtheor > 0.3. The optimiza-
tion of the CI and CVexp values was achieved by (i) prioritizing the
combinations  with  high  uncertainty  to  increase  the  predictive  ac-
curacy  in  the  exploration  mode  and  (ii)  proposing  more  effective
synergistic drug combinations in the exploitation mode. The Gryffin

allowed explicit control of the balance between these two strategies
(28). The workflow started with an equal balance of exploration and
exploitation, which was adjusted manually by human intervention.
A detailed description of human- algorithm collaboration is provid-
ed in the standardized protocol (fig. S6). The protocol involves hu-
man intervention at key points of the experiments, where the user
approves shifts in the optimization strategy, provides additional con-
straints, or terminates the campaign based on the algorithm’s progress.
The  details  of  drug  dose  optimization  are  provided  in  Supple-
mentary Text. Briefly, the optimization was performed in four gen-
erations of iterative experiments (denoted as G0 to G4 series) (fig. S7A).
In each generation, we examined seven distinct drug combinations
proposed by Gryffin, tested for at least three biological replicates. In
total,  we  identified  five  synergistic  drug  combinations  leading  to
−0.19 ≤ CI ≤ −0.11 and 64 ≤ CVexp ≤ 86%. The most effective three-
drug combination meeting the targets and resulting in CI = −0.12
and CVexp = 65% was identified in the G3 series (labeled as the G3- 7
series) (fig. S7, B and C).

Next, we focused on the spheroid response to DOX, CPA, and
5- FU  administered  in  a  sequence.  The  most  effective  synergistic
drug combination found in the G3- 7 series was selected to explore
the time- sequencing regimens for three- drug administration. Each
drug was supplied individually at the concentration optimized for
the  simultaneous  drug  supply  in  the  G3- 7  series,  that  is,  1.25  μM
DOX, 105 μM 5- FU, and 94.4 μM CPA. The drugs were supplied for
different time intervals, with a total drug administration time of
48  hours.  Gryffin  was  initialized  with  three  input  parameters:  the
drug administration sequence and the administration times of two
individual drugs, t1 and t2 (the supply time for the third drug, t3, was
calculated  as  t3  =  48  –  (t1  +  t2).  Figure  3A  illustrates  six  possible
drug administration sequences (S). The time interval for the indi-
vidual drug supply was used as a discrete variable with an increment
of 4 hours. The details of the selection of time intervals are provided
in Supplementary Text. To improve the CVexp value of 65% achieved
for the simultaneous three- drug administration (marked as a horizon-
tal cyan line in Fig. 3B), the goal was to attain a CVexp = 50%, marked
by the horizontal red line in Fig. 3B. An automated liquid- handling

Fig. 2. Growth of MCF- 7 spheroids in the MF platform. (A) Fragment of the array of 300- μm- diameter McF- 7 cell–laden droplets. (B) Fluorescence images of spheroids
stained with calcein- AM (green, live cells) and Pi (red, dead cells), taken 24 hours after cell loading in the MF device. (C) immunofluorescence staining of spheroids after
24- hour cell culture using 4′,6- diamidino- 2- phenylindole (dAPi) (blue, nuclei), Alexa Fluor 488 e- cadherin rabbit monoclonal antibody (green, cell- cell junctions) and Al-
exa Fluor 568 phalloidin (red, cytoskeleton). (D) Spheroid staining with Ki- 67 rabbit monoclonal antibody (green, proliferative cells), Alexa Fluor 568 phalloidin (red, cyto-
skeleton), and dAPi (blue, nuclei). the bottom rows in (c) and (d) show merged confocal fluorescence microscopy images.

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

4 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

Fig. 3. Sequential drug administration to MCF- 7 spheroids. (A) illustration of sequential drug administration. (B) variation of cell viability, cvexp, achieved in different
experimental series [generations (GSs)]. the horizontal red line indicates the optimization target for cvexp. the lowest cvexp achieved for G3- 2 simultaneous drug admin-
istration is marked with a horizontal cyan line. the most effective sequential schedule is marked with a purple diamond. the data are shown as means ± Sd based on three
to five independent experiments. (C) examined sequential drug schedules, organized from left- to- right in the order of ascending cvexp. the color coding indicates the first
administered drug, represented by red, blue, and green for dOX, cPA, and 5- FU, respectively. the data are shown as means ± Sd based on three to five independent ex-
periments. (D) validation of the best- performing drug combination administered concurrently and sequentially. two- sample t test with holm correction. the data are
shown as means ± Sd based on more than five independent experiments.

setup was used to supply three drugs in the time sequence and time
intervals proposed by Gryffin (fig. S3).

Figure 3B shows the variation in the average CVexp value, plotted
for  four  experimental  generations  (GS0  to  GS3),  each  comprising
eight sequential drug administration experiments. In the first series
(GS0),  three  drugs  were  supplied  in  random  regimens  that  were
proposed  by  the  Gryffin  algorithm  in  the  absence  of  preliminary
data on the sequential drug administration. The lowest CVexp = 80%
was achieved in experiment GS0- 4, with an 8- hour supply of CPA,
28- hour administration of 5- FU, and 12- hour supply of DOX. On
the basis of these results, for the GS1 generation, Gryffin proposed
eight new regimens, that resulted in CVexp = 65% for the most effi-
cient schedule. Next, the search was narrowed by “human interven-
tion,”  that  is,  all  further  schedules  were  selected  solely  in  the
exploitation mode. In the generation GS2, the three- drug adminis-
tration resulted in 65% ≤ CVexp ≤ 68%. In generation GS3, for the
more precise identification of the best- performing drug administra-
tion schedule, we reduced the time interval of individual drug ad-
ministration from 4 to 2 hours, leading to the best- performing regimen

with  CVexp  =  65%.  The  selection  of  the  2- hour  time  step  in  drug
delivery was supported by the results of our prior work on drug de-
livery to MF arrays of cancer spheroids with similar cell density
(fig. S8), where this time interval was the shortest one that enabled
spheroid  penetration  with  small- molecule  drugs  (38).  Because  the
learning curve in the GS3 experimental series did not change in com-
parison with the results of GS2, the ML- driven identification of the
most effective sequential multidrug administration was terminated.

Figure 3C shows the summary of the values of CVexp achieved for
the sequential drug administration in the closed- loop optimization
process. A total of 11 distinct administration schedules recommend-
ed by Gryffin exhibited a similar efficiency (P > 0.05; two- sample t
test)  as  the  simultaneous  drug  administration  (marked  with  the
cyan  horizontal  line  in  Fig.  3C).  A  trend  emerged,  in  which  8  of
these 11 drug supply regimens started from the administration of
DOX as the first drug (Fig. 3C and fig. S9A). Among these 11 sched-
ules, the most promising sequence corresponded to the generation
GS2- 7 (marked with a purple diamond), that is, an 8- hour adminis-
tration of the 1.25 μM solution of DOX, followed by the 32- hour

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

5 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

supply of the 105 μM solution of 5- FU and, subsequently, by 8- hour
administration  of  94  μM  CPA  solution  (fig.  S9A).  The  target  of
CVexp = 50% was not reached for the sequential drug administra-
tion, and for the most effective schedule, the administration of three
drugs  resulted  in  CVexp  =  65%,  similar  to  the  lowest  CVexp  value
achieved for the simultaneous drug supply (Fig. 3D). Yet, sequential
drug supply enabled a significant reduction in the overall drug ex-
posure without compromising the value of CVexp. More specifically,
the total dosage of three drugs in the sequential regimen was 75%
lower than in their simultaneous administration (fig. S9B). This re-
sult  revealed  that  sequential  drug  administration  was  effective  at
reducing drug dosage at comparable performance.

The efficacy of the GS2- 7 drug administration schedule was vali-
dated in several ways. We compared the CVexp values for the spher-
oids subjected to individual drugs, simultaneous drug administration,
and sequential drug supply, as well as the CVexp values for the re-
spective control groups (Fig. 4, A and B). More specifically, to assess
the effect of individual drugs, the spheroids were subjected to each
drug  for  the  time  interval  similar  to  that  in  the  GS2- 7  schedule,
while the solutions of two other drugs were replaced with the nutri-
tion medium. After that, the spheroids were stained with Ki- 67 an-
tibody, imaged using confocal laser scanning microscopy (Fig. 4C),
and examined by flow cytometry (Fig. 4D). The details of the flow cy-
tometry analysis and gating strategy are described in Supplementary

Fig. 4. Validation of sequential drug administration to MCF- 7 spheroids. comparison of cvexp in the best- performing (A) simultaneous and (B) sequential multidrug
administration and individual drug administration [1.25 μM dOX (8 and 48 hours), 105 μM 5- FU (32 and 48 hours), and 94 μM cPA (8 and 48 hours)]. two- sample t test
comparison to the control group with holm correction. Bars, average of at least, three biological replicates. error bars, Sd. (C) left to right: confocal fluorescence micros-
copy images of spheroids stained with Ki- 67 rabbit monoclonal antibody (green, proliferative cells) and with Alexa Fluor 568 phalloidin (red, cytoskeleton); with no treat-
ment (control) and with individual treatment with dOX for 48 and 8 hours, 5- FU for 32 and 48 hours, and cPA for 8 and 48 hours; with concurrent (G3- 7) and sequential
(GS2- 7) administration of three- drug combination. Scale bars, 50 μm. (D) Flow cytometry profiles for McF- 7 cells stained with Ki- 67 antibody (proliferative cells), obtained
by spheroid dissociation after drug treatment [as in (A) and (B)]. the lines and the numbers show the fraction of proliferative cells.

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

6 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

Text and fig. S10. Based on the results of spheroid staining for ne-
crotic (PI) and metabolically active (calcein- AM) cells, cell viabili-
ties  or  CVexp  values  were  similar  after  concurrent  and  sequential
three- drug treatments; however, IF staining of proliferative cells us-
ing the Ki- 67 marker revealed a lower number of proliferative cells
in the spheroids after simultaneous drug administration. These re-
sults suggest that simultaneous drug administration reduced prolif-
erative and metabolic activity without inducing necrosis, as follows
from the results of PI staining. A similar trend was observed when
only DOX was supplied to the spheroids for 48 hours. We also per-
formed confocal microscopy imaging of the spheroids subjected to
the GS2- 1 schedule (the administration of 5- FU before DOX). No-
tably, after 32- hour treatment with DOX, the spheroids exhibited a
comparable  reduction  in  the  fraction  of  proliferative  cells,  as  ob-
served in the GS2- 1 schedule (fig. S11). Thus, we conclude that the
advantage of sequential drug administration was in reducing the total
drug exposure and, potentially, the associated drug toxicity while
maximizing the desired anticancer effect.

Identification of effective multidrug therapy for PDOs
The closed- loop workflow developed for MCF- 7 spheroids was ex-
tended to the concurrent and sequential drug administration for the
PDO model. Breast cancer PDOs were formed using a suspension of

patient- derived cells (patient line: ER−/PR−/HER2−; table S2), as de-
scribed elsewhere (37). Figure 5 (A to C) show the bright- field and
LIVE/DEAD fluorescence images of PDOs after 96- hour culture in
EKGel in the MF device, with cell viability of 89 ± 7%. Figure 5D
shows that the cell nuclei were positively stained for Ki- 67, indi-
cating active cell proliferation. The formation of PDOs after 96- hour
cell culture in the MF device was confirmed by immunostaining
with E- cadherin (cell- cell junction) and F- actin (cell cytoskeleton)
(Fig. 5E). The PDOs grown in the MF platform exhibited similar
patterns of proliferative cell distribution as mature PDO cultures
grown off- chip in EKGel for 28 days (Fig. 5F). Thus, the use of the
MF platform significantly accelerated PDO growth.

We selected OLA {a poly[adenosine diphosphate (ADP) ribose
polymerase] (PARP) inhibitor} and an epigenetic drug IBET- 762 (a
bromodomain and extraterminal motif inhibitor), a combination of
drugs that was found to be synergistic in the treatment of homolo-
gous recombination- proficient tumors (42). Our goal was to explore
the impact of sequential drug administration versus concurrent drug
supply. Moreover, because these classes of drugs have overlapping
toxicities (myelosuppression), insights into the optimal sequencing
could inform clinical development (43, 44). Before the experiments,
we  verified  PDO  response  to  the  combination  of  these  drugs  in  a
384- well plate (fig. S12).

Fig. 5. Growth of PDOs in the MF platform. (A to C) Bright- field (A) and fluorescence images of PdOs stained with calcein- AM (green, live cells) (B) and Pi (red,
dead cells) (c) 96- hour postseeding. Scale bars, 300 μm. (D) immunofluorescence staining of PdOs after 96- hour cell culture with Ki- 67 rabbit monoclonal anti-
body (green, proliferative cells), Alexa Fluor 568 phalloidin (red, cytoskeleton), and dAPi (blue, nuclei). (E ) immunofluorescence staining of PdOs with dAPi (blue,
nuclei), Alexa Fluor 488 e- cadherin rabbit monoclonal antibody (green, cell- cell junctions), and Alexa Fluor 568 phalloidin (red, cytoskeleton) after 96- hour cell culture.
(F) immunofluorescence staining of PdOs grown 4 days on- chip and 28 days off- chip with Ki- 67 rabbit monoclonal antibody (green, proliferative cells) and Alexa
Fluor 568 phalloidin (red, cytoskeleton).

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

7 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

Using an MF array of PDOs, we determined the value of EC50 for
each  drug  after  a  96- hour  continuous  supply  of  drug  solution  to
PDOs (table S4). The EC50 values for OLA and IBET- 762 were 132 and
380 μM, respectively. From the drug- response curves (fig. S13), we
determined the drug concentration range to be 10 to 1000 μM and
0.01 to 300 μM for OLA and IBET- 762, respectively. The fitted dose-
response curves were used to compute CVtheor for drug combina-
tions  by  multiplying  cell  viabilities  corresponding  to  individual
drugs at the concentrations proposed by Gryffin, that is, CVtheor =
CVOLA × CVIBET- 762. The details of dose optimization are provided
in Supplementary Text.

The targets in the Gryffin algorithm for the PDO treatment with
a concurrent two- drug combination were set to be CI ≤ −0.15 and
CVexp ≤ 50%. Various drug combinations were examined in five se-
ries of experiments (fig. S14A). A synergistic drug combination pro-
viding the targeted CVexp values with CI = −0.21 and CVexp = 42%
was  identified  in  the  G3- 2  sample,  in  which  OLA  and  IBET- 762
were administered at 116 and 0.993 μM concentrations, respectively
(fig. S14, B and C). Overall, the experimental results showed that
concurrent administration of OLA and IBET- 762 synergistically re-
duced the viability and proliferation of cells in PDOs and resulted in
the accumulation of double- strand breaks (DBSs) in DNA.

To explore sequential drug administration for PDOs, we used the
G3- 2  drug  combination  identified  in  the  concurrent  drug  supply.
Two administration protocols included sequence A, involving PDO
treatment with OLA, followed by the supply of IBET- 762, and se-
quence  B  commencing  with  IBET- 762  and  followed  by  the  OLA
supply (Fig. 6A). The automated liquid- handling platform was used
to administer OLA and IBET- 762 solutions in the designated time-
sequence  schedules.  The  total  treatment  duration  for  PDOs  was
96 hours, with an individual drug supply interval of 4 hours used as
a discrete variable (fig. S15).

Figure 6B shows the variation in the average CVexp value across
three sequential generations of experiments (denoted as GSs), each
examining nine sequence protocols. In the initial series (denoted as
GS0)  with  sequences  randomly  proposed  by  Gryffin,  none  of  the
drug combinations met the objective of CVexp = 50% (shown with
the horizontal red line in Fig. 6B), that is, the lowest acheived CVexp
was 87%. Next, in the subsequent GS- 1 and GS- 2 generations, the
temporal  resolution  was  doubled  by  reducing  the  time  interval  of
individual drug administration from 4 to 2 hours. Nonetheless, no
substantial  improvement  in  achieving  lower  values  of  CVexp  was
reached. As shown in Fig. 6C, the lowest CVexp of 87% was achieved
for the series GS2- 2 (marked with a purple diamond symbol) compared

Fig. 6. Sequential drug administration to PDOs. (A) illustration of sequential drug administration. (B) variation of cell viability, cvexp, in different experimental series
(GSs). the horizontal red line indicates the optimization target. the most effective drug combination identified in the GS- 2 generation is marked with a purple diamond.
the data are shown as means ± Sd based on three to five independent experiments. (C) drug schedules, sorted from left to right in the order of ascending cvexp. the
color (red or blue) represents the first administered drug (OlA or iBet- 762, respectively). the data are shown as means ± Sd based on three to five independent experi-
ments. (D) comparison of cvexp values for the best- performing simultaneous drug combination G3- 2 with sequentially administered multidrug combination GS2- 2. two-
sample t test with holm correction. the data are shown as means ± Sd based on more than four independent experiments.

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

8 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

to CVexp = 42% attained for the simultaneous drug administration
(Fig. 6D). We note that CVexp exceeding 100% at low drug dosages
(shown in Fig. 6C) may result from (i) the enhanced PDO permea-
bility with dyes used for LIVE/DEAD assay (45) and (ii) the activated
cell survival mechanisms, including up- regulated anti- apoptotic path-
ways and increased DNA repair mechanisms or proliferative effects at
low drug doses (46, 47).

Figure 7A shows a significant reduction in cell viability in PDOs
treated  with  drug  combination  G3- 2  compared  to  treatment  with

individual drugs. Comparison of CVexp for the best- performing se-
quentially administered drug combination with the results of PDO
treatment with individual drugs is displayed in Fig. 7B. The efficien-
cy of the identified sequence was also confirmed using flow cytom-
etry and IF imaging experiments (Fig. 7, C and D). Flow cytometry
experiments  were  conducted  on  Ki- 67  antibody–stained  cells  ob-
tained from the PDOs dissociated after drug treatment (Fig. 7D). In
nontreated PDOs, 61% of the cells were proliferative. The treatment
of PDOs with IBET- 762 or OLA led to a reduction in the fraction of

Fig. 7. Validation of sequential drug administration to PDOs. comparison of cvexp for best- performing (A) concurrent and (B) sequential administered multidrug
combination with the results of PdO treatment with individual drugs [116 μM OlA (96 and 30 hours) and 0.993 μM iBet- 762 (96 and 66 hours)]. two- sample t test with
holm correction). the data are shown as means ± Sd based on three to five independent experiments. (C) left to right: confocal fluorescence microscopy images of PdOs
stained with h2AX rabbit monoclonal antibody (green, dBSs in dnA) and Alexa Fluor 568 phalloidin (red, cytoskeleton); with no treatment (control) and individual treat-
ment with OlA for 96 and 30 hours and iBet- 762 for 96 and 66 hours; and with concurrent (G3- 2) and sequential (GS2- 2) administration of two drugs. Scale bars, 50 μm.
(D) Flow cytometry profiles for cells stained with Ki- 67 antibody (proliferative cells), obtained by dissociating PdOs postdrug treatment [as in (A) and (B)]. the line desig-
nates the fraction of proliferative cells.

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

9 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

proliferative cells to 31%. Coadministration of  both drugs further
suppressed  cancer  cell  proliferation,  with  only  20%  of  cells  being
positively stained with Ki- 67 antibody. Furthermore, the occurrence
of DNA double- strand breaks (DSBs) in the PDO- treated G3- 2 drug
combination is shown in confocal fluorescence microscopy images
(Fig. 7C). Upon negative staining of these PDOs with the H2A his-
tone family member X (H2AX) antibody, nearly all cells in the un-
treated PDOs (control) showed no evidence of DSBs. Individually,
treatment with IBET- 762 did not cause DSB, while OLA increased
the  number  of  cells  exhibiting  DSBs.  Simultaneous  IBET- 762  and
OLA administration led to a significant increase in the fraction of
H2AX- positive cells in PDOs. Collectively, these results show that
the reduction in cell viability was predominantly caused by OLA when
drugs were administered sequentially.

DISCUSSION
The  developed  integrated  platform  enabled  several- day  growth  of
uniformly sized 300- μm- diameter breast tumor spheroids and PDOs.
A  single  tumor- on- a- chip  MF  device  accommodated  1200  cancer
spheroids or PDOs, which were used for the screening of 12 distinct
drug combinations and/or administration regimens. Screening close-
 to- physiological flow conditions enabled the exploration of a large
parameter space in spheroid and PDO treatment with drugs. Auto-
mation facilitated the screening process for both simultaneous and
sequential administration of multiple drugs.

The integration of the tumor- on- a- chip platform with automa-
tion and closed- loop BO was used to make a decision about the ef-
ficacy  of  a  particular  therapeutic  strategy.  The  Gryffin  algorithm
enabled a hierarchical multiobjective optimization of drug synergy
(combination index) as a primary objective and efficiency (cell via-
bility) as a secondary target across continuous (drug concentration),
discrete (time), and categorical (sequence) parameters. For each se-
ries of experiments, up to 10 experimental conditions were explored,
along  with  at  least  two  control  experiments.  On  the  basis  of  the
spheroid or PDO response to a particular multidrug combination,
the ML algorithm adaptively learned to propose a synergistic drug
combination and its administration regimens with higher and high-
er efficacy.

What distinguishes BO and similar model- based approaches is
their focus on sample efficiency in small data regimes, learning from
a minimal number of past experiments to guide the next set. Sto-
chastic  and  metaheuristic  experiment  planning  algorithms,  e.g.,
random walk or simulated annealing, provide simple and computa-
tionally efficient algorithms for global optimization. Yet, they offer
limited sample efficiency (that is, the fewest possible experiments),
as it is often assumed that property evaluation is fast and inexpen-
sive. Among metaheuristic approaches, there are evolutionary algo-
rithms,  which  are  suitable  for  evaluating  parallel  and  large- scale
samples, but they make similar assumptions. BO achieves a higher
sample efficiency, although it comes with increased computational
cost due to the need for training a ML model with strong regulariza-
tion to prevent overfitting. Despite this consideration, the computa-
tional  expense  of  BO  is  negligible  compared  to  the  timescales  of
experimental science, and it only becomes a concern when dealing
with large sample sizes (e.g., >103 to 104 experiments). In the cur-
rent work, we selected the Gryffin BO algorithm to identify effective
regimens in combination cancer therapy. Gryffin is competitive with

state- of- the- art  categorical  optimization  algorithms  in  its  simplest
form (28). It offers key features essential for our study, including the
ability to handle flexible known constraints and support for multi-
objective optimization. The capability to handle flexible constraints
allows it to manage arbitrary constraints through an intuitive inter-
face (35), which is critical for navigating interdependent experimen-
tal parameters and conditions in our work.

With regard to our work, for three drugs administered concur-
rently at seven possible concentrations (table S1), one would need
343 samples to explore all possible combinations. When considering
sequential administration, there are six possible administration se-
quences for three drugs (Fig. 3). In addition, for 10 possible admin-
istration times for each drug, 600 possible administration regimens
should be considered. This number reduces to 276 when constraints
are imposed, i.e., that (i) three drugs are administered over a period
of 48 hours and that (ii) each drug is administered for a minimum
of 4 hours. The boundaries of the parametric space for the maximal
treatment window were defined on the basis of established in vitro
research protocols for organoid propagation and the three- drug
combination of DOX, 5- FU, and CPA (48). For concurrent adminis-
tration, a theoretical cell viability constraint of 0.3 was chosen em-
pirically to guide the algorithm in search for moderate and low drug
concentrations.  To  avoid  confusion  of  the  model  and  reduce  the
number  of  experiments  required  to  identify  synergistic  combina-
tions, this constraint was not set as an explicit objective and could be
adjusted to higher values if the algorithm is unable to find a syner-
gistic  combination.  In  our  ML- driven  exploration  work,  Gryffin
identified  synergistic  administration  regimens  in  only  35  experi-
ments for the concurrent and 32 experiments for the sequential ad-
ministration schedules, thus exploring only 10 and 12% of all possible
regimens, respectively. Progress in each experimental iteration was
assessed using cell viability measurements (sequential drug admin-
istration) and both cell viability and combination index (concurrent
drug administration). The best result from each iteration served as
the key performance indicator. A multiobjective optimization was
conducted using Chimera scalarizing function (49), which was inte-
grated into the Gryffin algorithm, with progress monitored by the
number  of  objectives  that  were  “satisfied,”  meaning  that  the  ob-
tained results met the Chimera tolerance for that objective. One ad-
ditional iteration was performed for possible local optimization of
the  region  around the identified satisfactory parameters, ensuring
the optimality of the selected values. For sequential administration,
we discretized time into 4- hour intervals to accelerate the explora-
tion of the complex parametric space of treatment times and sequenc-
es, which are categorical variables. After the initial fast exploration, we
increased the temporal resolution to 2- hour intervals to validate the
identified  optimal  regimes.  Given  the  complex  nature  of  the  phe-
nomena being explored and the high adaptability of the algorithm
without prior data, the human guidance helped prevent model con-
fusion  and  resource  overuse,  thereby  underscoring  the  practical
relevance and potential clinical applicability of this approach. The
implementation of the Gryffin algorithm enabled the identification
of effective regimens in 10 weeks for spheroids and in 15 weeks for
PDOs. This time frame was primarily constrained by the duration of
cell culture. Further acceleration of this process can be achieved via
transfer learning, which would enable the application of the knowl-
edge gained for specific drug combinations and regimens to inform
future experiments.

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

10 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

In  the  present  work,  the  tumor- on- a- chip  platform  was  devel-
oped using cancer spheroids formed by the well- established MCF- 7
breast cancer cell line and a three- drug combination, that is, DOX,
CPA, and 5- FU. To develop the close- looped workflow, we aimed to
achieve 10% synergy and 70% cell viability [this degree of anticancer
effect is consistent with levels that correlate with potential antitumor
activity (50, 51)]. These targets were used to evaluate the synergistic
effect of the three- drug combination while balancing the minimal
toxicity of individual drugs and the combined anticancer activity of
a synergistic combination. With a limited number of experiments,
the ML- driven closed- loop workflow successfully identified the syn-
ergistic drug combination within a large parametric space. We fur-
ther validated the results obtained in the MF platform by wide- field
microscopy, IF staining, and flow cytometry. In particular, for flow
cytometry experiments spheroids were dissociated into single cells
inside  the  microwells  by  purging  TrypLE  through  the  MF  device
and subsequently staining with Ki- 67 antibody. The results showed
that 83% of cells in the control group were proliferative, which de-
creased to 53% after DOX and media treatment. Spheroid treatment
with CPA or 5- FU reduced proliferative cells to 65 and 61%, respec-
tively, and the combination of three drugs reduced it to 37%, con-
firming  the  synergistic  effect  of  the  GS2- 7  schedule  (Fig.  4).  The
results showed a strong correlation between the calculated cell via-
bility and the number of proliferating cells within both the spher-
oids.  Specifically,  cell  viability  decreased  from  100  to  65%  (using
fluorescence microscopy LIVE/DEAD assay), and proliferating cells
were reduced from 83 to 37% (assessed using flow cytometry) for
the sequential three- drug combination in MCF- 7 spheroids. These
findings confirm the effectiveness of the optimized administration
regimens for the three- drug combination in MCF- 7 spheroids. The
relationship between the identified drug concentrations aligned
with approved clinical dosages reported for in vitro studies (48).
While in clinical settings, all three drugs are administered together
(52), we found that their comparable efficacy can be attained with a
sequential drug supply at the reduced administration time for each
drug, thus reducing the total drug exposure by 75%, in comparison
with simultaneous drug administration. While we did not assess the
effect of drug administration scheduling for normal cells, e.g., car-
diomyocytes, the regimens that maintain efficacy while reducing
drug exposure may reduce both acute and long- term toxicities. With
regards to the tests using normal cells, according to the limited lit-
erature data, in clinical settings, FAC multidrug therapy is associat-
ed  with  cardiotoxicity  (53).  For  2D  culture,  the  FAC  combination
(50 μM 5- FU, 1 μM DOX, and 50 μM CPA) induced significant cy-
totoxicity (72.69 ± 4.62%) in rat cardiomyocyte- derived H9c2 cells
after 48- hour administration (48). The same treatment resulted in
18% reduction in proliferation in 3D cardiac microtissues composed
of iPSC- derived cardiomyocytes and cardiac fibroblasts (54). Nota-
bly, in our study, the optimal concentrations—DOX (1.25 μM), CPA
(94 μM), and 5- FU (105 μM)—were comparable to those used in the
2D study, while the DOX concentration was significantly lower than
that used in the 3D model. We recognize that toxicity tests on nor-
mal cells are an important next step and expect that our approach
can  be  extended  to  normal  tissues,  with  validation  using  in  vivo
models. For example, DOX- related cardiotoxicity is correlated with
cumulative  exposure.  Our  findings  for  the  sequential  drug  supply
are particularly important for DOX, the most toxic component of
the drug combination. The reduction in the drug dosage has the po-
tential to limit acute and chronic side effects in cancer chemotherapy

(55, 56) and is especially important for young and elderly patients
(57, 58).

Following the validation of the performance of the tumor- on- a-
chip platform, we demonstrated its versatility and practical relevance
for the development of therapeutic strategies by using PDOs and an
investigational two- drug combination (42). We explored the effect of
individual, simultaneous, and sequential administration of IBET- 762
(targeting BET proteins to modify chromatin and thereby altering
gene transcription through epigenetic mechanisms) (59) and OLA
(an approved PARP inhibitor, targeting specific DNA repair path-
ways) (60). Olaparib, the Food and Drug Administration–approved
PARP inhibitor showed a synergistic effect when coadministered with
IBET- 762 in established breast cancer cell lines and xenograft animal
models (42); however, the characterization of sequential drug adminis-
tration has not been explored. We have previously reported successful
time- effective  EKGel- based  generation  of  PDOs  derived  directly
from patient tumors (PDOs) and from existing patient- derived xeno-
graft (PDX) organoids (PDXOs), which are organoids derived from
PDXs  models,  and  their  pharmacologic  characterization,  including
concordance between in vitro response and in vivo response in orig-
inating tumors. Here, we confirmed the synergistic effect for the simul-
taneous administration of OLA and IBET- 762 in breast cancer PDOs
and showed that the synergy reduces when these drugs are admin-
istered in a sequence, regardless of the order and duration of their
supply. The examined drug concentrations were relevant to the estab-
lished in vitro IC50s for these agents, where the doses are relevant to
achievable in vivo pharmacokinetics.

Comparative analysis of the effect of OLA and IBET- 762 in the
sequential administration schedule showed that the reduction in
cell viability was predominantly caused by OLA. This result indi-
cates that concurrent, rather than sequential drug administration, is
important, which points to a more complex basis for the empirical
synergy observed with combined treatment. Our results demon-
strated a correlation between the calculated cell viability, the num-
ber of proliferating cells, and the imaging of double- strand DNA
breaks within PDOs. More specifically, cell viability decreased from
100 to 87%, as determined by the LIVE/DEAD assay, while the pro-
portion of proliferating cells declined from 85 to 78% based on the
flow  cytometry  results.  These  findings  indicate  no  significant  in-
crease in double- strand DNA breaks following treatment with the
sequential OLA/IBET- 762 combination. Although the pharmaco-
logic effect of drug combinations can be predicted theoretically based
on the mechanism of individual drug action, these are complex and
are likely influenced by cellular factors that may vary between different
cancers  (61). The  developed  tumor- on- a- chip  strategy  enables  em-
pirical evaluation and optimization of treatment schedules, recogniz-
ing that optimal schedules may differ for different drug combinations
and tumor types. In addition, recognizing the heterogenous responses
that are observed in similar combinations in patients (44), our re-
sults suggest the need to characterize combinations and sequences
of candidate regimens more comprehensively in a diverse represen-
tative collection of models, which could be achieved using this plat-
form. While different tumors and their PDO models will have varying
sensitivities to different drugs (and drug combinations), our work is
based on the hypothesis that the order and timing of treatment in a
synergistic combination will be more broadly applicable across dif-
ferent sensitive models.

The  integration  of  the  tumor- on- a- chip  platform,  automation,
and ML facilitated and significantly accelerated the identification of

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

11 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

effective multidrug formulations and their administration regimens,
that is, the simultaneous and sequential supply of individual drugs.
The  platform  enables  spheroid  and  PDO  growth  under  close- to-
physiological flow conditions, provides precise control over spher-
oid and PDO dimensions, and incorporates EKGel, an extracellular
matrix (ECM)–mimetic hydrogel. The platform can support pro-
longed cell culture and dynamic modeling of drug concentrations,
as well as drug administration regimens, thus mimicking clinical
pharmacokinetics for preclinical research. These advancements high-
light the translational potential of the integrated platform for optimiz-
ing drug administration regimens and, potentially, for the develo pment
of personalized medicine using PDOs generated from individual
patient tumors. Note that the evaluation of PDXO response is par-
ticularly valuable, as it takes advantage of available in vivo response
data for standard agents and informs complex in vivo combination
experiments, while in vivo optimization is not feasible. While our
work has focused on breast cancer, we expect that the developed
strategy would accommodate the search for the treatment of other
solid tumors types, where organoid generation is possible and mul-
tidrug regimens are relevant. The optimization and validation of 3D
tumor models of diverse tumor types will be an important extension
of this work.

We note that the developed strategy can also identify potential
nanomedicine candidates, whose flow- assisted PDO penetration is
underestimated  in  static  3D  models  (62),  thus  paving  the  way  for
subsequent preclinical studies in vivo. The platform can facilitate the
iterative design of nanomedicines tailored to specific PDO models
or ECM characteristics, including its porosity, charge, and stiffness
(63). In addition, the developed platform significantly enhances the
ability to explore a range of drug administration strategies in rele-
vant tumor models, a key factor in optimizing the design of in vivo
animal studies and clinical trials. Given the practical limitations in
these settings, which markedly constrain the exploration of dosages
and timing, this capability marks a key step away from the reliance
on empirical, fixed- dose simultaneous combinations.

Further developments will include the incorporation of stromal
components, such as immune cells and cancer- associated fibroblasts
(64, 65), thus enhancing the predictive value of the integrated plat-
form (66, 67). While in the present work we aimed to minimize drug
exposure to identify regimens with the greatest therapeutic poten-
tial, in vitro models of normal tissues that are responsible for dose-
limiting toxicities, such as hematopoietic cells or normal epithelial
cells, could be used to assess the identified regimens by estimating
therapeutic index. Further automation of cell loading in the MF de-
vice and imaging process will increase the throughput and facilitate
drug screening across multiple PDO models. Furthermore, the ex-
tension of information learned from certain drug combinations and
specific regimens to future novel experiments would be achieved by
enabling transfer learning in the Gryffin algorithm. The combina-
tion of large language models with Bayesian optimizers is a potential
strategy to realize this task (68).

MATERIALS AND METHODS
Materials
Type A gelatin was purchased from Sigma- Aldrich (Canada). SU- 8
photoresist  was  supplied  by  MicroChem  Corporation.  Poly(dime-
thyl siloxane) (PDMS) (Sylgard 184) was purchased from Ellsworth
Adhesives. Fluorinated oil HFE- 7500 3M Novec was purchased from

3M Corporation. 008- FluoroSurfactant was supplied by RAN Bio-
technologies.  Dulbecco’s  modified  Eagle’s  medium  (DMEM),  fetal
bovine  serum  (FBS),  penicillin/streptomycin,  trypsin- EDTA  solu-
tion, and Hank’s balanced salt solution (HBSS; 1×) were purchased
from Life Technologies (Thermo Fisher Scientific). Doxorubicin hy-
drochloride [>98% purity, high- performance liquid chromatography
(HPLC)] and 5- FU (>98% purity, HPLC) were obtained from Bioshop
(Canada). CPA monohydrate was purchased from MilliporeSigma.
I- BET762 (GSK525762A) and OLA (AZD2281) were supplied by
Cell Signaling Technology. All chemicals were used as received with-
out purification. An aqueous 10 weight % (wt %) suspension of cel-
lulose  nanocrystals  was  purchased  from  the  University  of  Maine
Process  Development  Center  (USA).  The  cellulose  nanocrystals
were surface- functionalized with aldehyde groups as described  else-
where  (69).  All  fluidic  connectors  and  paraformaldehyde  tubing
(1/16″ outer diameter, 1/8″ inner diameter) were supplied by IDEX
Health & Science.

Fabrication of MFs devices
The fabrication of the MF devices was previously described in (62).
The design of MF devices with an array of 300- μm- diameter microw-
ells is provided in Fig. 1C and fig. S1. MF devices were fabricated by
soft lithography (70) using silicon masters supplied by FlowJEM Ltd.
Glass slides (75 mm by 50 mm) were coated with PDMS using spin
coating at 800g for 15 s. The assembled MF device was maintained at
115°C overnight.

Preparation of the hydrogel
The hydrogel (EKGel) for spheroid and PDO growth was prepared
as described elsewhere (69). The stock suspension of a- CNCs and a
solution of gelatin were sterilized using ultraviolet illumination for
20 min and maintained in a water bath at 37°C for at least 30 min
before mixing. In all experiments, cell- laden droplets containing hy-
drogel precursors were incubated for 2 to 3 hours in an incubator at
37°C with a 5% CO2 supply to form cell- laden microgels.

Culture of MCF- 7 cells
Human breast adenocarcinoma MCF- 7 cells were purchased from
American Type Culture Collection (ATCC) (catalog no: ATCC
HTB- 22). MCF- 7 cells (5 × 105 cells) were seeded in 75- cm2 flasks
and grown to 90% confluence for 1 week in a DMEM (Thermo Fisher
Scientific)  cell  culture  media  supplemented  with  10%  (v/v)  FBS
(Thermo Fisher Scientific) and 1% (v/v) penicillin/streptomycin,
Thermo Fisher Scientific). The cells were maintained in a humidi-
fied incubator at 37°C with 5% CO2. To passage cells or prepare them
for MF experiments, they were detached from the flasks by incubating
with 3 ml of trypsin- EDTA (Thermo Fisher Scientific) solution for 6
min at 37°C. Then, following the addition of 7 ml of DMEM cell cul-
ture media, the cell suspension was centrifuged at 300g for 5 min.

Culture of patient- derived breast tumor cells and
cancer PDOs
Patient  tumor  tissue  was  collected  with  informed  patient  consent
and used according to UHN Research Ethics Board approved proto-
cols (06- 196, 14- 8358- C, and 175518). Breast organoid model used
in the study (PDO line 1) was established in EKGel from the PDX
model, as described elsewhere (37). The details of the PDO model
are provided in table S2. The components of PDO media are listed in
table S4. Medium changes were performed every 3 to 4 days, and

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

12 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

cells were passaged every 2 weeks. For passaging, the cell culture
medium was replaced with 1 ml of TrypLE Express (Gibco) per well,
and the samples were dissociated by manual shearing using a P1000.
The PDOs were incubated in TrypLE at 37°C and mixed every 10 min
until complete PDO dissociation. After centrifugation at 300g for
5 min, the supernatant was removed, and the cells were suspended
in the suspension of EKGel precursors (15,000 cells per well were
plated in 300 μl/EKGel per well) and plated in a 24- well plate. Fol-
lowing 2 hours of gelation, the EKGel- encapsulated cells were over-
laid with breast organoid media prepared as described elsewhere
(19). Fresh medium was prepared every week and stored at 4°C.

Generation of MF arrays
Following procedures previously described in (62), the detailed pro-
tocol of the generation of cell- laden droplets serving as precursors
for the generation of uniformly sized spheroids and PDOs is de-
scribed in fig. S2. Briefly, the MF device was sterilized by exposing it
to ultraviolet light for 10 min. Then, cell- laden droplets were formed
in the microwells of the MF device from the suspension of MCF- 7
cells (cell density of 1.5 × 105 cells/μl) or patient- derived cells (cell
density of 1.1 × 105 cells/μl) mixed with EKGel precursors. Follow-
ing 3- hour incubation of the MF device at 37°C, the cell- laden drop-
lets were gelled, and the fluorinated oil in the supplying channel of the
MF device was replaced with the cell culture media. The MF device
was placed on the rocker (OrganoFlow, MIMETAS, the Netherlands)
in the humidified incubator at 37°C supplied with 5% CO2 for cul-
ture of spheroids or PDOs.
Drug screening
DOX (DOX042, BioShop, Canada), 5- FU (FLU597, BioShop, Canada),
CPA monohydrateand (239785, Sigma- Aldrich, USA) were used for
MCF- 7 spheroid treatment. For PDOs, I- BET762 (GSK525762A, Cell
Signaling Technology) and OLA (AZD2281, Cell Signaling Tech-
nology) were used. For screening of individual drugs and drug com-
binations, a solution with a particular drug concentration in the cell
culture medium was perfused through the MF device containing
spheroids or PDOs. For sequential drug screening, an automatic flu-
idic system was developed using an automatic dispenser pump (Cavro
Centris Pump, TECAN, USA) with a 12- valve (TECAN, USA) sys-
tem (fig. S3). For each specific experiment, this software- controlled
platform automatically perfused, collected, and discarded drug solu-
tions, following the selected sequential drug treatment plan.

Cell viability in the spheroids and PDOs was determined by stain-
ing them for 1 hour at 37°C with calcein- AM (green, live cells) and
PI (red, dead cells) with the corresponding concentration in the cell
culture media of 2 and 6 μM. The stained cells were imaged using a
fluorescence  microscope  (Nikon  Ti  Eclipse)  with  excitation  wave-
lengths  of  480/30  and  540/25  nm  and  emission  wavelengths  of
535/45 and 605/55 nm for live and dead cells, respectively. Fluores-
cence images were processed and analyzed using ImageJ software
[National Institutes of Health (NIH)] and custom Python software
(https://github.com/yakavetsiv/Live- dead) (71). Cell viability in spher-
oids and PDOs after subjecting them to drugs for 48 hours (spher-
oids) and 96 hours (PDOs) was determined by measuring the mean
pixel fluorescence intensity for the green (live) and red (dead) chan-
nels after the detailed protocol of image processing is described in
fig. S4. To reduce potential device- to- device variation, the CVexp was
calculated as the ratio of cell viabilities determined before and after
drug administration and subsequently normalized to CVexp of the con-
trol group. The data analysis of dose- response curves was performed

by the drc (72) and PharmacoGx (73) packages for RStudio (PBC,
MA, USA).
Immunofluorescence staining
Immunofluorescence  staining  of  spheroids  and  PDOs  was  per-
formed by perfusing 1× HBSS through an MF device for 10 min to
replace the cell culture media. Following spheroid or PDO fixation
of by perfusing 5% formalin for 45 min, the formalin solution was
removed by purging for 45 min a 0.1 M solution of glycine. Then,
glycine solution was replaced with a 0.5 vol % solution of Triton X-
100 in 1× HBSS to permeabilize the spheroids or PDOs and incu-
bated for 30 min. An IF solution (0.05 wt % NaN3, 0.1 wt % bovine
serum albumin, 0.2 vol % of Triton X- 100, and 0.05 vol % Tween 20
in HBSS) was then perfused through the MF device for 30 min to
remove excess of Triton X- 100. A primary blocking solution (10 wt
% goat serum in IF solution) was purged through the MF device for
60 min and subsequently replaced with the antibody solution. The
device was incubated overnight at 4°C. For F- actin and E- cadherin
or Ki- 67 staining, the antibody solution consisted of Alexa Fluor 568
phalloidin (1:400 dilution; Cell Signaling Technology) and Alexa
Fluor 488 E- cadherin rabbit monoclonal antibody (1:800 dilution;
Cell Signaling Technology) or Ki- 67 rabbit monoclonal antibody
conjugated to FITC (1:50 dilution, Thermo Fisher Scientific) in IF
wash. For H2AX, the primary antibody solution consisted of phosphor-
histone H2A.X (Ser139) rabbit monoclonal antibody (1:200 dilution;
Cell Signaling Technology), while the secondary antibody solution
consisted of goat anti- rabbit immunoglobulin G antibody conjugated
to Alexa Fluor 488 (1:200 dilution; Thermo Fisher Scientific) in IF
wash solution. To remove excess of antibodies, the spheroid or PDO
arrays were washed with IF wash solution for 90 min. For nuclei
staining, DAPI solution (0.5 ng ml−1) was perfused through the MF
device for 1 hour. Following immunostaining, the MF devices were
imaged using a Leica SP8 STELLARIS confocal microscope (Leica
microsystem, Wetzlar, Germany) using an ×10, numerical aperture
0.4 dry objective. The images were processed using LAS X software
(Leica) and analyzed by ImageJ software (NIH).
Flow cytometry
Following procedures previously described in (62), flow cytometry
experiments were performed on the dissociated spheroids or PDOs
after 48-  and 96- hour drug treatment, respectively. The spheroids and
PDOs were dissociated into individual cells by purging TrypLE ex-
press (Gibco) through the MF device for 45 s at a volumetric flow rate
of 1 ml/min, followed by 20- min incubation at room temperature.
The dissociated cells were transferred to the centrifuge tubes, centri-
fuged at 300g for 5 min, and, subsequently, fixed using 70% ethanol
cooled to −20°C. Following incubation at −20°C overnight, the sam-
ples were washed with 2% FBS solution in HBSS. The dissociated cells
were incubated with Ki- 67 rabbit monoclonal antibody conjugated to
FITC (1:50 dilution; Thermo Fisher Scientific) in the blocking solu-
tion (0.1 wt % FBS and 0.01 vol% Triton X- 100 in HBSS buffer) for
1 hour at room temperature. Flow cytometry analysis was performed
on a Cytoflex S2 instrument (Beckman Coulter) at the University
Health Network Research Flow Cytometry Facility. The gating strate-
gy is described in fig. S10. The fluorescence of the Ki- 67–conjugated
antibody was detected in the fluorescence channel (FITC) with a
525/40- nm filter under the excitation at 488 nm. The data analysis was
carried out using FlowJo software version 10.5 (FlowJo LLC).
Statistical analysis
All data in the present work are reported with average ± SD from
at least three independent experiments. The statistical analysis was

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

13 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

performed using a two- sample t test with Holm correction for mul-
tiple comparisons. The data analysis was carried out using RStudio
(PBC, MA, USA) with a significant level established at P ≤ 0.05.

Supplementary Materials
This PDF file includes:
Supplementary text
Figs. S1 to S15
tables S1 to S4
References

REFERENCES AND NOTES
  1.  G. turashvili, e. Brogi, tumor heterogeneity in breast cancer. Front. Med. 4, 227 (2017).
  2.  n. harbeck, F. Penault- llorca, J. cortes, M. Gnant, n. houssami, P. Poortmans, K. Ruddy,

J. tsang, F. cardoso, Breast cancer. Nat. Rev. Dis. Primers 5, 66 (2019).

  3.  F. lüönd, S. tiede, G. christofori, Breast cancer as an example of tumour heterogeneity
and tumour cell plasticity during malignant progression. Br. J. Cancer 125, 164–175
(2021).

  4.  M. l. telli, R. W. carlson, First- line chemotherapy for metastatic breast cancer. Clin. Breast

Cancer 9, S66–S72 (2009).

  16.  J. J. G. Marin, e. herraez, e. lozano, R. i. R. Macias, O. Briz, Models for understanding

resistance to chemotherapy in liver cancer. Cancers 11, 1677 (2019).

  17.  K. Moshksayan, n. Kashaninejad, M. e. Warkiani, J. G. lock, h. Moghadas, B. Firoozabadi,

M. S. Saidi, n.- t. nguyen, Spheroids- on- a- chip: Recent advances and design
considerations in microfluidic platforms for spheroid formation and culture. Sens.
Actuators B 263, 151–176 (2018).

  18.  G. vlachogiannis, S. hedayat, A. vatsiou, Y. Jamin, J. Fernández- Mateos, K. Khan, A. lampis,

K. eason, i. huntingford, R. Burke, M. Rata, d.- M. Koh, n. tunariu, d. collins,
S. hulkki- Wilson, c. Ragulan, i. Spiteri, S. Y. Moorcraft, i. chau, S. Rao, d. Watkins,
n. Fotiadis, M. Bali, M. darvish- damavandi, h. lote, Z. eltahir, e. c. Smyth, R. Begum,
P. A. clarke, J. c. hahne, M. dowsett, J. de Bono, P. Workman, A. Sadanandam, M. Fassan,
O. J. Sansom, S. eccles, n. Starling, c. Braconi, A. Sottoriva, S. P. Robinson, d. cunningham,
n. valeri, Patient- derived organoids model treatment response of metastatic
gastrointestinal cancers. Science 359, 920–926 (2018).

  19.  n. Sachs, J. de ligt, O. Kopper, e. Gogola, G. Bounova, F. Weeber, A. v. Balgobind, K. Wind,
A. Gracanin, h. Begthel, J. Korving, R. van Boxtel, A. A. duarte, d. lelieveld, A. van hoeck,
R. F. ernst, F. Blokzijl, i. J. nijman, M. hoogstraat, M. van de ven, d. A. egan, v. Zinzalla,
J. Moll, S. F. Boj, e. e. voest, l. Wessels, P. J. van diest, S. Rottenberg, R. G. J. vries,
e. cuppen, h. clevers, A living biobank of breast cancer organoids captures disease
heterogeneity. Cell 172, 373–386.e10 (2018).

  20.  Z. chen, S. Kheiri, e. W. K. Young, e. Kumacheva, trends in droplet microfluidics: From
droplet generation to biomedical applications. Langmuir 38, 6233–6248 (2022).

  21.  Y. Wang, M. liu, Y. Zhang, h. liu, l. han, Recent methods of droplet microfluidics and their

  5.  G. n. hortobagyi, A. U. Buzdar, current status of adjuvant systemic therapy for primary

applications in spheroids and organoids. Lab Chip 23, 1080–1096 (2023).

breast cancer: Progress and controversy. CA Cancer J. Clin. 45, 199–226 (1995).
  6.  M. J. lee, A. S. Ye, A. K. Gardino, A. M. heijink, P. K. Sorger, G. MacBeath, M. B. Yaffe,

Sequential application of anticancer drugs enhances cell death by rewiring apoptotic
signaling networks. Cell 149, 780–794 (2012).

  7.  l. Zitvogel, l. Apetoh, F. Ghiringhelli, G. Kroemer, immunological aspects of cancer

chemotherapy. Nat. Rev. Immunol. 8, 59–73 (2008).

  8.  d. Miles, G. von Minckwitz, A. d. Seidman, combination versus sequential single- agent

therapy in metastatic breast cancer. Oncologist 7, 13–19 (2002).

  9.  P. Savage, J. Stebbing, M. Bower, t. crook, Why does cytotoxic chemotherapy cure only

some cancers? Nat. Rev. Clin. Oncol. 6, 43–52 (2009).

  10.  R. Gray, R. Bradley, J. Braybrooke, Z. liu, R. Peto, l. davies, d. dodwell, P. McGale, h. Pan,
c. taylor, W. Barlow, J. Bliss, P. Bruzzi, d. cameron, G. Fountzilas, S. loibl, J. Mackey,
M. Martin, l. d. Mastro, v. Möbus, v. nekljudova, S. d. Placido, S. Swain, M. Untch,
K. i. Pritchard, J. Bergh, l. norton, c. Boddington, J. Burrett, M. clarke, c. davies, F. duane,
v. evans, l. Gettins, J. Godwin, R. hills, S. James, h. liu, e. MacKinnon, G. Mannu,
t. Mchugh, P. Morris, S. Read, Y. Wang, Z. Wang, P. Fasching, n. harbeck, P. Piedbois,
M. Gnant, G. Steger, A. d. leo, S. dolci, P. Francis, d. larsimont, J. M. nogaret,
c. Philippson, M. Piccart, S. linn, P. Peer, v. tjan- heijnen, S. vliek, J. Mackey, d. Slamon,
J. Bartlett, v. h. Bramwell, B. chen, S. chia, K. Gelmon, P. Goss, M. levine, W. Parulekar,
J. Pater, e. Rakovitch, l. Shepherd, d. tu, t. Whelan, d. Berry, G. Broadwater, c. cirrincione,
h. Muss, R. Weiss, Y. Shan, Y. F. Shao, X. Wang, B. Xu, d.- B. Zhao, h. Bartelink, n. Bijker,
J. Bogaerts, F. cardoso, t. cufer, J.- P. Julien, P. Poortmans, e. Rutgers, c. van de velde,
e. carrasco, M. A. Segui, J. U. Blohmer, S. costa, B. Gerber, c. Jackisch, G. von Minckwitz,
M. Giuliano, M. d. laurentiis, c. Bamia, G.- A. Koliou, d. Mavroudis, R. A’hern, P. ellis,
l. Kilburn, J. Morden, J. Yarnold, M. Sadoon, A. h. tulusan, S. Anderson, G. Bass,
J. costantino, J. dignam, B. Fisher, c. Geyer, e. P. Mamounas, S. Paik, c. Redmond,
d. l. Wickerham, M. venturini, c. Bighin, S. Pastorino, P. Pronzato, M. R. Sertoli, t. Foukakis,
K. Albain, R. Arriagada, e. B. nordström, F. Boccardo, e. Brain, l. carey, A. coates,
R. coleman, c. correa, J. cuzick, n. davidson, M. dowsett, M. ewertz, J. Forbes, R. Gelber,
A. Goldhirsch, P. Goodwin, d. hayes, c. hill, J. ingle, R. Jagsi, W. Janni, h. Mukai, Y. Ohashi,
l. Pierce, v. Raina, P. Ravdin, d. Rea, M. Regan, J. Robertson, J. Sparano, A. tutt, G. viale,
n. Wilcken, n. Wolmark, W. Wood, M. Zambetti, increasing the dose intensity of
chemotherapy by more frequent administration or sequential scheduling: A patient- level
meta- analysis of 37,298 women with early breast cancer in 26 randomised trials. Lancet
393, 1440–1452 (2019).

  11.  A. c. Palmer, P. K. Sorger, combination cancer therapy can confer benefit via patient- to-

patient variability without drug additivity or synergy. Cell 171, 1678–1691.e13 (2017).

  12.  M. A. Shah, G. K. Schwartz, the relevance of drug sequence in combination

chemotherapy. Drug Resist. Updat. 3, 335–356 (2000).

  13.  F. cardoso, P. l. Bedard, e. P. Winer, O. Pagani, e. Senkus- Konefka, l. J. Fallowfield,

S. Kyriakides, A. costa, t. cufer, K. S. Albain, eSO- MBc task Force, international guidelines
for management of metastatic breast cancer: combination vs sequential single- agent
chemotherapy. J. Natl. Cancer Inst. 101, 1174–1181 (2009).

  14.  d. huh, G. A. hamilton, d. e. ingber, From 3d cell culture to organs- on- chips. Trends Cell

Biol. 21, 745–754 (2011).

  22.  Y. Wu, Y. Zhou, X. Qin, Y. liu, From cell spheroids to vascularized cancer organoids:

Microfluidic tumor- on- a- chip models for preclinical drug evaluations. Biomicrofluidics 15,
061503 (2021).

  23.  A. R. Aref, R. Y.- J. huang, W. Yu, K.- n. chua, W. Sun, t.- Y. tu, J. Bai, W.- J. Sim,

i. K. Zervantonakis, J. P. thiery, R. d. Kamm, Screening therapeutic eMt blocking agents in
a three- dimensional microenvironment. Integr. Biol. 5, 381–389 (2013).
 24.  B. Schuster, M. Junkin, S. S. Kashaf, i. Romero- calvo, K. Kirby, J. Matthews,

c. R. Weber, A. Rzhetsky, K. P. White, S. tay, Automated microfluidic platform for
dynamic and combinatorial drug screening of tumor organoids. Nat. Commun. 11,
5271 (2020).

  25.  G. Schneider, Automating drug discovery. Nat. Rev. Drug Discov. 17, 97–113 (2018).
  26.  P. K. Wong, F. Yu, A. Shahangian, G. cheng, R. Sun, c.- M. ho, closed- loop control of cellular

functions using combinatory drugs guided by a stochastic search algorithm. Proc. Natl.
Acad. Sci. U.S.A. 105, 5105–5110 (2008).

  27.  A. Weiss, X. ding, J. R. van Beijnum, i. Wong, t. J. Wong, R. h. Berndsen, O. dormond,

M. dallinga, l. Shen, R. O. Schlingemann, R. Pili, c.- M. ho, P. J. dyson, h. van den Bergh,
A. W. Griffioen, P. nowak- Sliwinska, Rapid optimization of drug combinations for the
optimal angiostatic treatment of cancer. Angiogenesis 18, 233–244 (2015).

  28.  F. häse, M. Aldeghi, R. J. hickman, l. M. Roch, A. Aspuru- Guzik, Gryffin: An algorithm for

Bayesian optimization of categorical variables informed by expert knowledge. Appl. Phys.
Rev. 8, 031406 (2021).

  29.  F. häse, l. M. Roch, c. Kreisbeck, A. Aspuru- Guzik, Phoenics: A bayesian optimizer for

chemistry. ACS Cent. Sci. 4, 1134–1145 (2018).

  30.  J. d. Feala, J. cortes, P. M. duxbury, c. Piermarocchi, A. d. Mcculloch, G. Paternostro,

Systems approaches and algorithms for discovery of combinatorial therapies. WIREs Syst.
Biol. Med. 2, 181–193 (2010).

  31.  J. Mockus, Bayesian Approach to Global Optimization: Theory and Applications (Springer,

1989), vol. 37; https://link.springer.com/book/10.1007/978- 94- 009- 0909- 0.

  32.  M. Park, M. nassar, h. vikalo, Bayesian active learning for drug combinations. IEEE Trans.

Biomed. Eng. 60, 3248–3255 (2013).

  33.  J. Yu, X. li, M. Zheng, current status of active learning for drug discovery. Artif. Intell. Life

Sci. 1, 100023 (2021).

  34.  d. Reker, G. Schneider, Active- learning strategies in computer- assisted drug discovery.

Drug Discov. Today 20, 458–465 (2015).

  35.  R. J. hickman, M. Aldeghi, F. häse, A. Aspuru- Guzik, Bayesian optimization with known

experimental and design constraints for chemistry applications. Digit. Discov. 1, 732–744
(2022).

  36.  c. i. Bliss, the toxicity of poisons applied jointly. Ann. Appl. Biol. 26, 585–615 (1939).
  37.  e. Prince, S. Kheiri, Y. Wang, F. Xu, J. cruickshank, v. topolskaia, h. tao, e. W. K. Young,

A. P. McGuigan, d. W. cescon, e. Kumacheva, Microfluidic arrays of breast tumor spheroids
for drug screening and personalized cancer therapies. Adv. Healthc. Mater. 11, e2101085
(2022).

  38.  S. Kheiri, e. Kumacheva, e. W. K. Young, computational modelling and big data analysis of
flow and drug transport in microfluidic systems: A spheroid- on- a- chip study. Front.
Bioeng. Biotechnol. 9, 781566 (2021).

  15.  G. Mehta, A. Y. hsiao, M. ingram, G. d. luker, S. takayama, Opportunities and challenges

  39.  Z. chen, S. Kheiri, A. Gevorkian, e. W. K. Young, v. Andre, t. deisenroth, e. Kumacheva,

for use of tumor spheroids as models to test drug delivery and efficacy. J. Control. Release
164, 192–204 (2012).

Microfluidic arrays of dermal spheroids: A screening platform for active ingredients of
skincare products. Lab Chip 21, 3952–3962 (2021).

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

14 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

  40.  G. n. hortobagyi, G. R. Blumenschein, W. Spanos, e. d. Montague, A. U. Buzdar, h.- Y. Yap,
F. Schell, Multimodal treatment of locoregionally advanced breast cancer. Cancer 51,
763–768 (1983).

  41.  J. Anampa, d. Makower, J. A. Sparano, Progress in adjuvant chemotherapy for breast

  62.

i. Yakavets, M. Ayachit, S. Kheiri, Z. chen, F. Rakhshani, S. McWhirter, e. W. K. Young,
G. c. Walker, e. Kumacheva, A microfluidic platform for evaluating the internalization of
liposome drug carriers in tumor spheroids. ACS Appl. Mater. Interfaces 16, 9690–9701
(2024).

cancer: An overview. BMC Med. 13, 195 (2015).

  42.  l. Yang, Y. Zhang, W. Shan, Z. hu, J. Yuan, J. Pi, Y. Wang, l. Fan, Z. tang, c. li, X. hu,

J. l. tanyi, Y. Fan, Q. huang, K. Montone, c. v. dang, l. Zhang, Repression of Bet activity
sensitizes homologous recombination–proficient cancers to PARP inhibition. Sci. Transl.
Med. 9, eaal1645 (2017).

  43.  P. G. Aftimos, M. Oliveira, K. Punie, v. Boni, e. P. hamilton, A. Gucalp, P. d. Shah,

M. J. de Miguel, P. Sharma, l. Bauman, e. campeau, S. Attwell, M. Snyder, K. norek,
e. Johnson, M. h. Silverman, S. lakhotia, S. M. domchek, J. K. litton, M. e. Robson, A
phase 1b/2 study of the Bet inhibitor Zen- 3694 in combination with talazoparib for
treatment of patients with tnBc without gBRcA1/2 mutations. J. Clin. Oncol. 40,
1023–1023 (2022).

  44.  Zenith epigenetics, “A Phase 2b Study of Zen003694 in combination With talazoparib in
Patients With triple- negative Breast cancer” (clinical trial registration nct03901469,
clinicaltrials.gov, 2024); https://clinicaltrials.gov/study/nct03901469.

  45.  K. A. Rejniak, v. estrella, t. chen, A. S. cohen, M. c. lloyd, d. l. Morse, the role of tumor
tissue architecture in treatment penetration and efficacy: An integrative study. Front.
Oncol. 3, 111 (2013).

  46.  K. Braun, c. M. Stürzel, J. Biskupek, U. Kaiser, F. Kirchhoff, M. lindén, comparison of

different cytotoxicity assays for in vitro evaluation of mesoporous silica nanoparticles.
Toxicol. In Vitro 52, 214–221 (2018).

  47.  t. Sobanski, M. Rose, A. Suraweera, K. O’Byrne, d. J. Richard, e. Bolderson, cell metabolism

and dnA repair pathways: implications for cancer therapy. Front. Cell Dev. Biol. 9, 633305
(2021).

  48.  M. Pereira- Oliveira, A. Reis- Mendes, F. carvalho, F. Remião, M. de l. Bastos, v. M. costa,
doxorubicin is key for the cardiotoxicity of FAc (5- fluorouracil + adriamycin +
cyclophosphamide) combination in differentiated h9c2 cells. Biomolecules 9, 21 (2019).
  49.  F. häse, l. M. Roch, A. Aspuru- Guzik, chimera: enabling hierarchy based multi- objective

optimization for self- driving laboratories. Chem. Sci. 9, 7642–7655 (2018).

  50.  v. Mehta, S. vilikkathala Sudhakaran, v. nellore, S. Madduri, S. n. Rath, 3d stem- like

spheroids- on- a- chip for personalized combinatorial drug testing in oral cancer.
J. Nanobiotechnol. 22, 344 (2024).

  51.  R. Fevre, G. Mary, n. vertti- Quintero, A. durand, R. F.- X. tomasi, e. del nery, c. n. Baroud,

combinatorial drug screening on 3d ewing sarcoma spheroids using droplet- based
microfluidics. iScience 26, 106651 (2023).

  52.  G. catimel, F. chauvin, J. P. Guastalla, P. Rebattu, P. Biron, M. clável, FAc (fluorouracil,
doxorubicin, cyclophosphamide) as second line chemotherapy in patients with
metastatic breast cancer progressing under Fec (fluorouracil, epirubicin,
cyclophosphamide) chemotherapy. Ann. Oncol. 5, 95–97 (1994).

  53.  J. R. Mackey, M. Martin, t. Pienkowski, J. Rolski, J.- P. Guastalla, A. Sami, J. Glaspy, e. Juhos,
A. Wardley, t. Fornander, J. hainsworth, R. coleman, M. R. Modiano, J. vinholes, t. Pinter,
A. Rodríguez- lescure, B. colwell, P. Whitlock, l. Provencher, K. laing, d. Walde, c. Price,
J. c. hugh, B. h. childs, K. Bassi, M.- A. lindsay, v. Wilson, M. Rupin, v. houé, c. vogel, tRiO/
BciRG 001 investigators, Adjuvant docetaxel, doxorubicin, and cyclophosphamide in
node- positive breast cancer: 10- Year follow- up of the phase 3 randomised BciRG 001
trial. Lancet Oncol. 14, 72–80 (2013).

  54.  J. lee, S. Mehrotra, e. Zare- eelanjegh, R. O. Rodrigues, A. Akbarinejad, d. Ge, l. Amato,
K. Kiaee, Y. Fang, A. Rosenkranz, W. Keung, B. B. Mandal, R. A. li, t. Zhang, h. lee,
M. R. dokmeci, Y. S. Zhang, A. Khademhosseini, S. R. Shin, A heart- breast cancer- on- a- chip
platform for disease modeling and monitoring of cardiotoxicity induced by cancer
chemotherapy. Small 17, e2004258 (2021).

  55.  h. Wildiers, Mastering chemotherapy dose reduction in elderly cancer patients. Eur. J.

Cancer 43, 2235–2241 (2007).

  56.  G. Makin, Principles of chemotherapy. Paediatr. Child Health 24, 161–165 (2014).
  57.  W. M. c. van den Boogaard, d. S. J. Komninos, W. P. vermeij, chemotherapy side- effects:

not all dnA damage is equal. Cancers 14, 627 (2022).

  58.  J.- J. Monsuez, J.- c. charniot, n. vignat, J.- Y. Artigou, cardiac side- effects of cancer

chemotherapy. Int. J. Cardiol. 144, 3–15 (2010).

  59.  J. Shi, c. R. vakoc, the mechanisms behind the therapeutic activity of Bet bromodomain

inhibition. Mol. Cell 54, 728–736 (2014).

  60.  c. J. lord, A. n. J. tutt, A. Ashworth, Synthetic lethality and cancer therapy: lessons

learned from the development of PARP inhibitors. Annu. Rev. Med. 66, 455–470 (2015).

  61.  R. S. narayan, P. Molenaar, J. teng, F. M. G. cornelissen, i. Roelofs, R. Menezes, R. dik,
t. lagerweij, Y. Broersma, n. Petersen, J. A. Marin Soto, e. Brands, P. van Kuiken,
M. c. lecca, K. J. lenos, S. G. J. G. in’t veld, W. van Wieringen, F. F. lang, e. Sulman,
R. verhaak, B. G. Baumert, l. J. A. Stalpers, l. vermeulen, c. Watts, d. Bailey, B. J. Slotman,
R. versteeg, d. noske, P. Sminia, B. A. tannous, t. Wurdinger, J. Koster, B. A. Westerman,
A cancer drug atlas enables synergistic targeting of independent drug vulnerabilities.
Nat. Commun. 11, 2935 (2020).

  63.  S. Mitragotri, d. G. Anderson, X. chen, e. K. chow, d. ho, A. v. Kabanov, J. M. Karp,
K. Kataoka, c. A. Mirkin, S. h. Petrosko, J. Shi, M. M. Stevens, S. Sun, S. teoh,
S. S. venkatraman, Y. Xia, S. Wang, Z. Gu, c. Xu, Accelerating the translation of
nanomaterials in biomedicine. ACS Nano 9, 6644–6654 (2015).

  64.  J. t. neal, X. li, J. Zhu, v. Giangarra, c. l. Grzeskowiak, J. Ju, i. h. liu, S.- h. chiou,

A. A. Salahudeen, A. R. Smith, B. c. deutsch, l. liao, A. J. Zemek, F. Zhao, K. Karlsson,
l. M. Schultz, t. J. Metzner, l. d. nadauld, Y.- Y. tseng, S. Alkhairy, c. Oh, P. Keskula,
d. Mendoza- villanueva, F. M. d. l. vega, P. l. Kunz, J. c. liao, J. t. leppert, J. B. Sunwoo,
c. Sabatti, J. S. Boehm, W. c. hahn, G. X. Y. Zheng, M. M. davis, c. J. Kuo, Organoid
modeling of the tumor immune microenvironment. Cell 175, 1972–1988.e16 (2018).

  65.  e. Garreta, R. d. Kamm, S. M. chuva de Sousa lopes, M. A. lancaster, R. Weiss, X. trepat,
i. hyun, n. Montserrat, Rethinking organoid technology through bioengineering. Nat.
Mater. 20, 145–155 (2021).

  66.  c. Belli, d. trapani, G. viale, P. d’Amico, B. A. duso, P. della vigna, F. Orsi, G. curigliano,
targeting the microenvironment in solid tumors. Cancer Treat. Rev. 65, 22–32 (2018).
  67.  W. li, Z. Zhou, X. Zhou, B. l. Khoo, R. Gunawan, Y. R. chin, l. Zhang, c. Yi, X. Guan, M. Yang,
3d biomimetic models to reconstitute tumor microenvironment in vitro: Spheroids,
organoids, and tumor- on- a- chip. Adv. Healthc. Mater. 12, e2202609 (2023).

  68.  A. Kristiadi, F. Strieth- Kalthoff, M. Skreta, P. Poupart, A. Aspuru- Guzik, G. Pleiss, A sober
look at llMs for material discovery: Are they actually good for Bayesian optimization
over molecules? arXiv:2402.05015 [cs.lG] (2024); https://doi.org/10.48550/
arXiv.2402.05015.

  69.  e. Prince, J. cruickshank, W. Ba- Alawi, K. hodgson, J. haight, c. tobin, A. Wakeman,
A. Avoulov, v. topolskaia, M. J. elliott, A. P. McGuigan, h. K. Berman, B. haibe- Kains,
d. W. cescon, e. Kumacheva, Biomimetic hydrogel supports initiation and growth of
patient- derived breast tumor organoids. Nat. Commun. 13, 1466 (2022).

  70.  R. S. Kane, A. d. Stroock, n. li Jeon, d. e. ingber, G. M. Whitesides, “chapter 18–Soft

lithography and microfluidics,” in Optical Biosensors, F. S. ligler, c. A. Rowe taitt, eds.
(elsevier Science, 2002), pp. 571–595; www.sciencedirect.com/science/article/pii/
B9780444509741500185.
i. Yakavets, yakavetsiv/live- dead: Release v.1.01, version 1.01 (Zenodo, 2025); https://doi.
org/10.5281/zenodo.14903369.

  71.

  72.  c. Ritz, F. Baty, J. c. Streibig, d. Gerhard, dose- response analysis using R. PLOS ONE 10,

e0146021 (2015).

  73.  P. Smirnov, Z. Safikhani, n. el- hachem, d. Wang, A. She, c. Olsen, M. Freeman, h. Selby,

d. M. A. Gendoo, P. Grossmann, A. h. Beck, h. J. W. l. Aerts, M. lupien, A. Goldenberg,
B. haibe- Kains, PharmacoGx: An R package for analysis of large pharmacogenomic
datasets. Bioinformatics 32, 1244–1246 (2016).
i. Yakavets, yakavetsiv/ml- mf_chemo: Release 1.0, version 1.0 (Zenodo, 2025); https://doi.
org/10.5281/zenodo.14890340.

  74.

  75.  S. Kheiri, Z. chen, i. Yakavets, F. Rakhshani, e. W. K. Young, e. Kumacheva, integrating
spheroid- on- a- chip with tubeless rocker platform: A high- throughput biological
screening platform. Biotechnol. J. 18, e2200621 (2023).

  76.  J. l. Sebaugh, Guidelines for accurate ec50/ic50 estimation. Pharm. Stat. 10, 128–134

(2011).

  77.  B. Yadav, K. Wennerberg, t. Aittokallio, J. tang, Searching for drug synergy in complex
dose–response landscapes using an interaction potency model. Comput. Struct.
Biotechnol. J. 13, 504–513 (2015).

  78.  A. ianevski, A. K. Giri, t. Aittokallio, SynergyFinder 2.0: visual analytics of multi- drug

combination synergies. Nucleic Acids Res. 48, W488–W493 (2020).

Acknowledgments: We are grateful to FlowJeM inc. for the fabrication of silicon masters for
the preparation of MF devices. We thank A. G. Frøseth for the generous support. Funding: We
are grateful for the support of the new Frontiers in Research Fund (canada) and canada
Foundation for innovation/Ontario Research Fund (Grant 36442) to the centre for Research
and Application Fluidic technologies (cRAFt). i.Y. and S.K. acknowledge support from nSeRc
canada cReAte training Program in Organ- on- a- chip engineering and entrepreneurship
(tOeP). S.K. acknowledges Ontario Graduate Scholarship (OGS). i.Y. is grateful for the financial
support of the Precision Medicine initiative (PRiMe) at the University of toronto and the
University health network (Uhn) (internal fellowship number PRMUhn2022- 006). e.M.R.
acknowledges support from the vector institute for Artificial intelligence. e.Y. acknowledges
support from nSeRc discovery Program (RGPin- 2019- 05885). this work was also supported by
the Office of the Assistant Secretary of defense of health Affairs, through the Breast cancer
Research Program under award no. W81XWh- 22- BcRP- BtA12- 2 (to d.W.c.). Opinions,
interpretations, conclusions, and recommendations are those of the author and are not
necessarily endorsed by the department of defense. this research was undertaken thanks in
part to funding provided to the University of toronto’s Acceleration consortium from the
canada First Research excellence Fund (grant cFReF- 2022- 00042). Author contributions: i.Y.,

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

15 of 16

Downloaded from https://www.science.org on July 31, 2025S c i e n c e   A d v An c eS   |   R eSeA R c h   AR t i c l e

S.K., d.W.c., and e.K. wrote the original draft of the manuscript. d.W.c., A.A.- G., e.W.K.Y., M.A.,
e.M.R., i.Y., S.K., and e.K. participated in the review and editing of the manuscript. e.K., d.W.c.,
A.A.- G., e.W.K.Y., M.A., i.Y., and S.K. conceptualized the search goals and aims of the work. e.K.,
A.A.- G., d.W.c., M.A., R.J.h., J.c., i.Y., and S.K. developed the methodology. M.A., e.M.R., R.J.h.,
and i.Y. programmed and integrated the software. d.W.c., S.K., J.c., and i.Y. validated the
results. d.W.c., i.Y., S.K., F.R., and J.c. conducted the research and performed the experiments.
i.Y., R.J.h., S.K., e.M.R. and d.W.c. curated data. i.Y., S.K., and R.J.h. conducted a formal analysis.
A.A.- G., d.W.c., J.c., and e.W.K.Y. provided resources. e.K., i.Y., and S.K. visualized the results.
d.W.c., e.K., and i.Y. administrated the project. e.K., d.W.c., A.A.- G., and e.W.K.Y. supervised the
research and acquired funding for the project. All authors provided active and valuable
feedback on the manuscript. establishment of the organoid models in BMe has been done in
collaboration with the Princess Margaret living Biobank (https://pmlivingbiobank.
uhnresearch.ca/) Competing interests: d.W.c. reports consultancy and advisory relationships
with AstraZeneca, daiichi Sankyo, GenomeRx, Gilead, GlaxoSmithKline, inivata/neoGenomics,
lilly, Merck, novartis, Pfizer, Roche, and SAGA and research funding to their institution from
AstraZeneca, GenomeRx, Guardant health, Grail, Gilead, GlaxoSmithKline, inivata/
neoGenomics, Knight, Merck, Pfizer, ProteinQure, and Roche. d.W.c. is an inventor on a patent
for methods of treating cancers characterized by a high expression level of spindle and

kinetochore associated complex subunit 3 (ska3) gene related to this work filed by Uhn (no.
US62/675,228, filed 22 May 2019, published 28 november 2019). the other authors declare
that they have no competing interests. Data and materials availability: All data needed to
evaluate the conclusions in the paper are present in the paper and/or the Supplementary
Materials and available on dryad (https://doi.org/10.5061/dryad.0vt4b8h8x) (74). the Gryffin
optimization code and the collected data are available on the Github repository (https://
github.com/yakavetsiv/ml- mf_chemo) and Zenodo (https://doi.org/10.5281/
zenodo.14890339) for the studies of three- drug and two- drug combinations (75). the in vitro
models can be provided pending scientific review and will be reviewed under Uhn policies
(www.uhncommercialization.ca/for- researchers/acdemic- partners). Access requires
submission of a formal request, institutional approval, and execution of a noncommercial
material transfer agreement including appropriate attribution and ethical compliance.
Requests for these should be submitted to mtas@ uhn. ca and d.W.c. (dave. cescon@ uhn. ca).

Submitted 16 September 2024
Accepted 27 June 2025
Published 30 July 2025
10.1126/sciadv.adt1851

Yakavets et al., Sci. Adv. 11, eadt1851 (2025)     30 July 2025

16 of 16

Downloaded from https://www.science.org on July 31, 2025
