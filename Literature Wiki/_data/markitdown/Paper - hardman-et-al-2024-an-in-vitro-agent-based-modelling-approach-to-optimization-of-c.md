---
tags:
  - literature
  - type/paper
  - lit/ai-methods
type: literature-note
source_note: "Papers/Paper - hardman-et-al-2024-an-in-vitro-agent-based-modelling-approach-to-optimization-of-c.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/hardman-et-al-2024-an-in-vitro-agent-based-modelling-approach-to-optimization-of-culture-medium-for-generating-muscle.pdf"
converter: "microsoft/markitdown"
---
|     |     |     | An in    | vitro |     | agent-based  |     |     | modelling |            |     |     |
| --- | --- | --- | -------- | ----- | --- | ------------ | --- | --- | --------- | ---------- | --- | --- |
|     |     |     | approach |       | to  | optimization |     |     |           | of culture |     |     |
royalsocietypublishing.org/journal/rsif medium for generating muscle cells
|     |     |     | David Hardman1, |     | Katharina |     | Hennig2, | Edgar | R.  | Gomes2, | William | Roman3 and |
| --- | --- | --- | --------------- | --- | --------- | --- | -------- | ----- | --- | ------- | ------- | ---------- |
Research
Bernabeu1,4
Miguel O.
1Centre
|     |     |     | for | MedicalInformatics,UsherInstitute, |     |     |     | TheUniversityofEdinburgh, |     | Edinburgh | EH164UX,UK |     |
| --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | ------------------------- | --- | --------- | ---------- | --- |
2InstitutodeMedicinaMolecular,FaculdadedeMedicina,UniversidadedeLisboa,AvenidaProfessorEgasMoniz,
| Cite this article: | Hardman D,  | Hennig K,   |                 |              |                    |     |        |             |          |           |     |     |
| ------------------ | ----------- | ----------- | --------------- | ------------ | ------------------ | --- | ------ | ----------- | -------- | --------- | --- | --- |
|                    |             |             | 1649-028Lisboa, | Portugal     |                    |     |        |             |          |           |     |     |
| Gomes ER, Roman    | W, Bernabeu | MO. 2024 An |                 |              |                    |     |        |             |          |           |     |     |
|                    |             |             | 3Australian     | Regenerative | MedicineInstitute, |     | Monash | University, | Clayton, | Australia |     |     |
invitro agent-based modelling approach to 4TheBayesCentre, UniversityofEdinburgh, Edinburgh EH8 9BT,UK
optimizationofculturemediumforgenerating
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD
DH, 0000-0001-9903-4443
musclecells.J.R.Soc.Interface21:20230603.
https://doi.org/10.1098/rsif.2023.0603
|     |     |     | Methodologies     |              | for culturing |           | muscle | tissue    | are        | currently  | lacking     | in terms of |
| --- | --- | --- | ----------------- | ------------ | ------------- | --------- | ------ | --------- | ---------- | ---------- | ----------- | ----------- |
|     |     |     | quality           | and quantity |               | of mature | cells  | produced. |            | We analyse | images      | from in     |
|     |     |     | vitro experiments |              | to            | quantify  | the    | effects   | of culture | media      | composition | on          |
|     |     |     | mouse-derived     |              | myoblast      | behaviour |        | and       | myotube    | quality.   | Metrics     | of early    |
Received: 17 October 2023 indicators of cell quality were defined. Images of muscle cell differentiation
Accepted: 11 December 2023 reveal that altering culture media significantly affects quality indicators and
myoblastmigratorybehaviours.Tostudytheeffectsofearly-stagecellbehav-
|     |     |     | iours on | mature | cell        | quality, | metrics  | drawn       | from | experimental |      | images or  |
| --- | --- | --- | -------- | ------ | ----------- | -------- | -------- | ----------- | ---- | ------------ | ---- | ---------- |
|     |     |     | inferred | by     | approximate |          | Bayesian | computation |      | (ABC)        | were | applied as |
inputstoanagent-basedmodel(ABM)ofskeletalmusclecelldifferentiation
Subject Category:
|     |     |     | with quality |     | indicator | metrics | as  | outputs. | Computational |     | modelling | was |
| --- | --- | --- | ------------ | --- | --------- | ------- | --- | -------- | ------------- | --- | --------- | --- |
Sciences–Mathematics
Life interface used to inform further in vitro experiments to predict the optimum media
|     |     |     | composition | for | culturing | muscle |     | cells. | Our results | suggest | that | myonuclei |
| --- | --- | --- | ----------- | --- | --------- | ------ | --- | ------ | ----------- | ------- | ---- | --------- |
Subject Areas: production in myotubes is inversely related to early-stage nuclei fusion
|                 |                    |     | index | and that | myonuclei |     | density | and | spatial | distribution | are | correlated |
| --------------- | ------------------ | --- | ----- | -------- | --------- | --- | ------- | --- | ------- | ------------ | --- | ---------- |
| biomathematics, | synthetic biology, |     |       |          |           |     |         |     |         |              |     |            |
withresidencetimeoffusingmyoblasts,theageatwhichmyotube–myotube
| computational | biology |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fusionendsandtherepulsionforcebetweenmyonuclei.Culturemediawith
5%serumwasfoundtoproducetheoptimumcellqualityandtomakemuscle
Keywords:
cellsculturedinaneurondifferentiationmediumviable.
| muscle, agent-based | model, tissue         |         |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --------------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| engineering,        | nuclei, computational | biology |     |     |     |     |     |     |     |     |     |     |
1. Introduction
Author for correspondence: Amajorchallengeintheengineeringoffunctionalskeletalmuscletissueisthe
David Hardman inability to reproduce the complex in vivo microenvironment of muscle tissue
|     |     |     | in vitro | [1]. To | form | contractile | myotubes, |     | distinct | cell | sources | are required. |
| --- | --- | --- | -------- | ------- | ---- | ----------- | --------- | --- | -------- | ---- | ------- | ------------- |
e-mail: david.hardman@ed.ac.uk
Currently,themostrelevantinvitromyogenesismodelemploysprimarymyo-
blasts[2]andatailoredculturemediumtosuccessfullydifferentiatemyoblasts
into multi-nucleatedmyotubes.
|     |     |     | Successful  |     | in vitro | myogenesis |       | is dependent |     | upon    | cell culture | medium     |
| --- | --- | --- | ----------- | --- | -------- | ---------- | ----- | ------------ | --- | ------- | ------------ | ---------- |
|     |     |     | composition | and | requires | it         | to be | fine-tuned   | to  | produce | healthy      | and mature |
myotubes.Sinceinvivomyogenesisreliesonseveralcelltypes,itisalsoimpor-
|     |     |     | tant to ensure |     | that the     | designed | medium |     | is compatible |     | with these | other cell |
| --- | --- | --- | -------------- | --- | ------------ | -------- | ------ | --- | ------------- | --- | ---------- | ---------- |
|     |     |     | typesformuscle |     | co-cultures. |          |        |     |               |     |            |            |
Considerationofthemediaconditionsthatfacilitateoptimalmusclecellfor-
|     |     |     | mation is | necessary | to               | maximize | the | quality, | yield   | and             | reproducibility | while     |
| --- | --- | --- | --------- | --------- | ---------------- | -------- | --- | -------- | ------- | --------------- | --------------- | --------- |
|     |     |     | reducing  | costs     | and experimental |          |     | time.    | Relying | on experimental |                 | trial and |
errortogeneratemoresophisticatedcell-basedinvitrosystemsisimpracticable
|                          |          |              | and new     | strategies | are        | necessary | forculture |           | medium | optimization |              | [3]. In vitro |
| ------------------------ | -------- | ------------ | ----------- | ---------- | ---------- | --------- | ---------- | --------- | ------ | ------------ | ------------ | ------------- |
| Electronic supplementary | material | is available |             |            |            |           |            |           |        |              |              |               |
|                          |          |              | experiments | are        | invaluable |           | tools for  | exploring |        | cell culture | environments | [4],          |
online at https://doi.org/10.6084/m9.figshare.
c.6984361.
©2024TheAuthors.PublishedbytheRoyalSocietyunderthetermsoftheCreativeCommonsAttribution
|     |     |     | License http://creativecommons.org/licenses/by/4.0/, |     |     |     |     | which | permits | unrestricted | use, provided | the original |
| --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | ----- | ------- | ------------ | ------------- | ------------ |
authorandsourcearecredited.

but they remain expensive, time consuming and provide Table 1. Listof metrics
2
| sparse data | points | for | analysis. | Numerical |     | models | of cell |     |     |     |     |     |     |     |
| ----------- | ------ | --- | --------- | --------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
and tissue behaviours [5] present fast, low-cost methods for royalsocietypublishing.org/journal/rsif
|            |          |             |     |             |     |          |       | indicator |     | metric |     |     |     |     |
| ---------- | -------- | ----------- | --- | ----------- | --- | -------- | ----- | --------- | --- | ------ | --- | --- | --- | --- |
| simulating | in vitro | experiments |     | but require |     | thorough | cali- |           |     |        |     |     |     |     |
bration against experimental results to establish confidence early-stage myoblastspeed (S )
mb
| in predictions. |     | Given the | lengthy | duration | of  | time | required |            |     |                     |     |         |               |     |
| --------------- | --- | --------- | ------- | -------- | --- | ---- | -------- | ---------- | --- | ------------------- | --- | ------- | ------------- | --- |
|                 |     |           |         |          |     |      |          | behaviours |     | myoblastvariationin |     | angular | velocity (ω ) |     |
mb
| to produce | mature  | myotubes    |     | in vitro,        | the ability | to         | predict |     |     |                 |     |               |     |     |
| ---------- | ------- | ----------- | --- | ---------------- | ----------- | ---------- | ------- | --- | --- | --------------- | --- | ------------- | --- | --- |
|            |         |             |     |                  |             |            |         |     |     | myoblastrate    | of  | proliferation | (P) |     |
| outcomes   | of cell | experiments |     | from early-stage |             | indicators | of      |     |     |                 |     |               |     |     |
|            |         |             |     |                  |             |            |         |     |     | myoblastangular |     | velocity      |     |     |
cellbehaviourwouldsaveexperimentaltimeandcosts.Find-
ing a single early-stage behaviour which is predictive of myoblastdirection of motion
| mature cell | quality     | would  | allow | direct | inference | of     | cell out- |     |     |                       |     |        |     |     |
| ----------- | ----------- | ------ | ----- | ------ | --------- | ------ | --------- | --- | --- | --------------------- | --- | ------ | --- | --- |
|             |             |        |       |        |           |        |           |     |     | myoblastpersistenceof |     | motion |     |     |
| comes.      | Agent-based | models |       | (ABM)  | apply     | simple | sets of   |     |     |                       |     |        |     |     |
myoblastvelocity
| behavioural | rules | to autonomous |     | agents | (such | as  | cells or |              |     |            |              |              |      |     |
| ----------- | ----- | ------------- | --- | ------ | ----- | --- | -------- | ------------ | --- | ---------- | ------------ | ------------ | ---- | --- |
|             |       |               |     |        |       |     |          | cell quality |     | difference | in myonuclei | density(days | 0–5) |     |
cell nuclei) and simulate their interactions with each other J.
and their environment in order to model higher level emer- indicators (dM) R.
| ging behaviours. |     | ABM | have | been used | to complement |     | cell |     |     |           |             |              |            | Soc. |
| ---------------- | --- | --- | ---- | --------- | ------------- | --- | ---- | --- | --- | --------- | ----------- | ------------ | ---------- | ---- |
|                  |     |     |      |           |               |     |      |     |     | myonuclei | coefficient | of variation | in spatial |      |
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  and tissue engineering as a method to gain insight into the Interface
|            |              |     |          |           |           |              |          |     |     | distribution(D |          | )                 |     |     |
| ---------- | ------------ | --- | -------- | --------- | --------- | ------------ | -------- | --- | --- | -------------- | -------- | ----------------- | --- | --- |
| underlying | mechanisms   |     | [6], but | to our    | knowledge |              | have not |     |     |                |          | var               |     |     |
|            |              |     |          |           |           |              |          |     |     | mean           | distance | between myonuclei | (D) |     |
| directly   | been applied |     | to the   | challenge | of        | optimization | of       |     |     |                |          |                   |     |     |
cell culture environments. Studies using ABM generally myotubewidth 21:
| derive agent | rules | from | the | literature | [7]. Here, | we  | present |     |     |            |          |           |            |          |
| ------------ | ----- | ---- | --- | ---------- | ---------- | --- | ------- | --- | --- | ---------- | -------- | --------- | ---------- | -------- |
|              |       |      |     |            |            |     |         |     |     | proportion | myotubes | withactin | striations | 20230603 |
aworkflowforacombinedinvitro–insilicoapproachtodeter-
| mining      | muscle      | cell quality | in        | which          | experimental |                 | data are  |             |      |              |        |           |                  |     |
| ----------- | ----------- | ------------ | --------- | -------------- | ------------ | --------------- | --------- | ----------- | ---- | ------------ | ------ | --------- | ---------------- | --- |
| used to     | define      | metrics      | of muscle | cell           | quality      | and             | of early- |             |      |              |        |           |                  |     |
| stage cell  | behaviours. |              | Metrics   | of early-stage |              | cell behaviours |           |             |      |              |        |           |                  |     |
|             |             |              |           |                |              |                 |           | composition | from | which        | we can | predict   | media conditions |     |
| are applied | as          | inputs       | to a      | nuclei-based   | ABM          | with            | two       |             |      |              |        |           |                  |     |
|             |             |              |           |                |              |                 |           | favourable  | for  | cell growth. | These  | functions | are used to      |     |
| phases,     | the first   | modelling    |           | myoblast       | motion       | and             | fusion,   |             |      |              |        |           |                  |     |
informthemediacompositionofafurtherinvitroexperiment
| and the    | second    | the nuclei |                   | force balance | within      |     | myotube |          |         |            |     |             |                |     |
| ---------- | --------- | ---------- | ----------------- | ------------- | ----------- | --- | ------- | -------- | ------- | ---------- | --- | ----------- | -------------- | --- |
|            |           |            |                   |               |             |     |         | in order | to more | accurately | map | the optimum | conditions for |     |
| cells with | metricsof | cell       | qualityindicators |               | asanoutput. |     |         |          |         |            |     |             |                |     |
culturingmusclecells.
| We selected |         | serum    | concentration | as        | the first      | media           | vari-    |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | ------------- | --------- | -------------- | --------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| able since  | primary | myoblast |               | fusion    | into           | multi-nucleated |          |     |     |     |     |     |     |     |
| myotubes    | occurs  | upon     | serum         | reduction | [8]            | but the         | cellular |     |     |     |     |     |     |     |
| effects of  | varying | serum    | at these      | low       | concentrations |                 | remain   |     |     |     |     |     |     |     |
2. Results
| ill-defined. | We  | chose the | proportion | of  | a neuronal |     | differen- |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
tiation media as our second component. Co-culturing 2.1. Changes in differentiation medium composition
| muscle cells | with | neurons | increases | muscle |     | cell maturation |     |        |      |                 |     |             |            |     |
| ------------ | ---- | ------- | --------- | ------ | --- | --------------- | --- | ------ | ---- | --------------- | --- | ----------- | ---------- | --- |
|              |      |         |           |        |     |                 |     | affect | both | early behaviour |     | and quality | indicators |     |
throughneuronal-derivedfactors[9]andprovidesthepossi-
bilitytostudyneuromuscularjunction(NMJ)formation,and Generatingbottom-upcell-basedsystemsreliesonthetimely
so it is of interest to study the extent to which high-quality developmentofcells.Cellularbehavioursearlyintheculture
myotube production is achievable in media tailored to will therefore govern the culture’s qualityat later stages. As
neuron differentiation. such, we used live and fixed imaging to identify a list of
Healthy muscle cells are long multi-nucleated cells with potential indicators divided into early-stage behaviours and
evenly distributed nuclei throughout the periphery of the quality indicators (table 1). To be of use in a predictive
fibre. Since uneven or centralized distribution of nuclei is model,indicatorsmustshowsignificantvariationinrelation
often linked to a disease state or improper maturation to oneor moreofthecell culturevariablesbeing optimized.
[10,11], nuclear position and distribution is a good marker Potential indicators of mature cell quality were extracted
of muscle cell maturity and health while the proportion of from fixed,stained images (figure1a).
myoblasts fusing to become myonuclei informs us of the Increasingtheserumconcentration(figure1b)from0%to
−2)
efficiency of cell differentiation. We therefore chose nuclei 2% led to a significant (464 more myonucleimm increase
positions of both unfused myoblasts and fused myotubes inthedifferenceindensityofmyonucleidMforcellscultured
(myonuclei) as the agents in our ABM. Nuclei are also inmusclecelldifferentiationmedia.Afurtherincreaseto10%
suitedtotheroleofagenthereastheirmotioncanbetracked serumconcentrationresultedinareductionindM(559fewer
over time from images, enabling quantification of their myonucleimm −2) to a level slightly lower than with no
behaviour. This enables us to calibrate a model linking serum. Increasing the concentration of serum resulted in a
nuclear behaviourwith cell health. gradual increase in the mean distance between myonuclei
Key metrics of cell behaviours are measured from in vitro (D)(figure1c)but,therewasnosignificantchangeincoeffi-
imagingand,forbehaviourswhichwewereunabletomeasure cientofvariationinmyonucleidistribution(D )(figure1d).
var
directly, inferred using an approximate Bayesian computation A significant drop in dM (567 less myonucleimm −2) was
(ABC–SMC)
sequential Monte Carlo method. A sensitivity observedbetweenexperimentsculturedinmusclecelldifferen-
analysisisperformedtodeterminetheeffectsofbothmeasured tiation media and in muscle and neuronal cell differentiation
and inferred cell behaviours on cell quality indicators. Early- mediamixedina1:1ratio(figure1e).dMremainedatasimi-
stage behaviour metrics found to correlate with cell quality larly low level in experiments with 100% neuronal medium,
indicators are fitted to functions of differentiation media demonstrating the existence of an optimal base medium for

(a) 3
royalsocietypublishing.org/journal/rsif
J.
R.
Soc.
|     | (b) |     |     |     | (c) |     |     |     | (d) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
300
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  *** ** Interface
|     |     | 1200 | **  |     |     |     |     | *   | )µ/σ( noitairav fo tneiciffeoc |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- |
1.5
|     | ebutoym ni ecnereffid |     |     |     |     | 250 |     |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1000
|     |     | 2–mmielcun |     |     | )mµ( ecnatsid | 200 |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
21:
|     |     | 800 |     |     |     |     |     |     | 1.0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
150 20230603
600
100
|     |     | 400 |     |     |     |     |     |     | 0.5 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
50
200
|     |     |     |     |     |     | 0   |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     |     | 0 2     | 10  |     |     | 0 2     | 10  |     | 0 2     | 10  |
| --- | --- | --- | ------- | --- | --- | --- | ------- | --- | --- | ------- | --- |
|     |     |     | % serum |     |     |     | % serum |     |     | % serum |     |
|     | (e) |     |         |     | (f) |     |         |     | (g) |         |     |
350
|     |     |      |     |     |     |     | *   |     |                                    | *   |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
|     |     | 1200 | *** |     |     |     |     |     | )µ/σ( noitairav fo tneiciffeoc 1.5 | *   |     |
|     |     |      | *** |     |     | 300 |     |     |                                    |     |     |
ebutoym ni ecnereffid
|     |     | 1000       |     |     |               | 250 |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
|     |     | 2–mmielcun |     |     | )mµ( ecnatsid |     |     |     |     |     |     |
|     |     | 800        |     |     |               | 200 |     |     | 1.0 |     |     |
|     |     | 600        |     |     |               | 150 |     |     |     |     |     |
|     |     | 400        |     |     |               | 100 |     |     | 0.5 |     |     |
50
200
|     |     |     |     |     |     | 0   |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     |     | 1:0 1:1 | 0:1 |     | 1:0 | 1:1 | 0:1 |     | 1:0 1:1 | 0:1 |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | ------- | --- |
ratio of standard:neuronal media ratio of standard:neuronal media ratio of standard:neuronal media
Figure 1. Myotube quality indicators at day 5 of differentiation. (a) A fixed image stained for cell nuclei (magenta) and actin cytoskeleton (cyan), yellow lines
indicate measured distances between myonuclei. Plots (b-d) show differences in quality indicators with varying serum concentrations. (b) Difference in myonuclei
mm2betweendays0and5ofdifferentiation,(c)meandistancebetweenmyonucleiand(d)uniformityofdistancebetweenmyonucleiexpressedas‘coefficient
per
of variationin spatial distribution’. Plots (e–g)show differences in quality indicators in varying ratios of neuronal medium. (e)Difference in myonuclei per mm2,
(f) mean distance between myonuclei and (g) coefficient of variation. In (b) and (e), values are reported as mean ± s.d.
myotube formation. Increasing the proportion of neuronal (figure2a).Significantand nonlineardifferencesinmetricsof
mediumledtoanincreaseinD(figure1f).Experimentswith myoblast speed of motion S mb , myoblast variation inangular
100%neuronalmediumanda1:1mixtureofmuscleandneur- velocity (ω ) and myoblast proliferation rate (P) were
mb
| onal cell | differentiation |     | media exhibited | a   | lower | D , and | observed. |     |     |     |     |
| --------- | --------------- | --- | --------------- | --- | ----- | ------- | --------- | --- | --- | --- | --- |
var
thereforemoreuniformdistribution,thanmusclecelldifferen- For serum concentrations between 0 and 2%, myoblast
tiationmediumalone(figure1g). cells moved with similar S (figure 2b). Increasing serum
mb
Meanthicknessofmyotubecells(electronicsupplementary concentration from 2 to 10% resulted in a significant
material,figureS1)andproportionofsampledmyotubeswith reduction in S . There was also evidence of a modest dip
mb
full or partial actin striations (electronic supplementary in ω as serum concentration is increased from 0 to 10%
mb
material, figure S2) were also studied as potential quality (figure2c).Pincreasedsignificantlyataserumconcentration
indicators,butdidnotdisplaysignificantdifferencesbetween from 2%(figure2d).
trials with different media compositions and so were Concerning distinct muscle-neuron media mixtures, we
discountedasappropriatequalityindicatorsforourworkflow. observed a decrease in S when muscle cell differentiation
mb
To create metrics of early-stage cell behaviours, myoblast medium was replaced with neuronal differentiation
ω
cells were segmented and tracked from live images taken medium or mixed to 1:1 ratios (figure 2e). However,
mb
during days 0–1 afterthe applicationofdifferentiation media (figure 2f) and P (figure 2g) were onlyaltered when muscle

|     |     |     | (a) |     |     |     |     |     |     |     |     |     |     | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
royalsocietypublishing.org/journal/rsif
J.
|     | (b) |     |     | (c) |     |     | (d) |     |     |     |     |     |     | R.  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
×10–3
|     | 1.5 |     |     |                              |     |     |     |     |     |     |     |     |     | Soc. |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     | *** | )1–nim °( noitairav ralulgna |     |     |     |     |     | *   |     |     |     |      |
|     |     |     | *** | 20                           |     |     |     | 1.0 | *   |     |     |     |     |      |
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  1–nim 1–llec snoisivid Interface
)1–nim mµ( deeps
0.8
15
*
0.6
|     | 1.0 |     |     |     |     |     |     |     |     |     |     |     |     | 21: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
|     |     |     |     |     |     |     |     | 0.4 |     |     |     |     |     | 20230603 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
5
0.2
|     | 0.5 |     |         | 0   |         |      |     | 0   |         |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ------- | ---- | --- | --- | ------- | --- | --- | --- | --- | --- |
|     |     |     | 0 2 10  |     | 0       | 2 10 |     |     | 0 2     | 10  |     |     |     |     |
|     |     |     | % serum |     | % serum |      |     |     | % serum |     |     |     |     |     |
|     | (e) |     |         | (f) |         |      | (g) |     |         |     |     |     |     |     |
×10–3
1.5
|     |     |     | *   | )1–nim °( noitairav ralulgna |     | *** |     |     |     | *   |     |     |     |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | *   | 20                           |     | *** |     | 1.2 |     |     |     |     |     |     |
1–nim 1–llec snoisivid
)1–nim mµ( deeps
1.0
15
0.8
1.0
|     |     |     |     | 10  |     |     |     | 0.6 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.4
5
0.2
|     | 0.5 |     |         | 0   |     |         |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 1:0 | 1:1 0:1 |     | 1:0 | 1:1 0:1 |     | 1:0 | 1:1 | 0:1 |     |     |     |     |
ratio of standard:neuronal media ratio of standard:neuronal media ratio of standard:neuronal media
Figure 2. Metrics of myoblast behaviour from live images of cells. (a) Illustration of tracking a single myoblast (red) in a brightfield image. Yellow dots show
positioninpreviousframes.Plots(b–d)showdifferencesinearly-stagebehaviourmetricswithvaryingserumconcentrations.Myoblast (b)speed,(c)variationin
angularvelocityand(d)rateofproliferation.Plots(e–g)showdifferencesinbehaviourmetricsinvaryingratiosofneuronalmediumand2%serumconcentration.
Myoblast (e) speed, (f) variation in angular velocity and (g) rate of proliferation. In (b–f) values are reported as mean ± s.d.
celldifferentiationmediumwasfullyreplacedwithneuronal complex interactions between early-stage behaviours and
differentiation medium. produce metrics of quality indicators as an output. The
Meandirectionandpersistenceofmyoblastmotionwere ABM is described in detail in the electronic supplementary
alsoextractedfromtrackingcellsinliveimages.Onaverage, material, Methods.
cells in all images analysed displayed no global directional Calibration of the residence time mechanism and force-
preference and so mean direction was discounted as an balance acting on fused nuclei requires the input of further
early-stagebehavioural indicator. metrics of cell behaviours which were not directly measur-
|                   |             |     |                |            |     | able from          | our imaging | data     | (see        | table | 4 in  | Methods). | The |     |
| ----------------- | ----------- | --- | -------------- | ---------- | --- | ------------------ | ----------- | -------- | ----------- | ----- | ----- | --------- | --- | --- |
|                   |             |     |                |            |     | use of approximate |             | Bayesian | computation |       | (ABC) | allows    | us  |     |
| 2.2. A calibrated | agent-based |     | model predicts | indicators |     |                    |             |          |             |       |       |           |     |     |
toinferdistributionsofthesemetricsbystrategicallyrunning
of cell quality from in vitro early-stage cell ABM simulations and comparing their outputs with
|     |     |     |     |     |     | measured | quality | indicator | metrics. | Two | extra | in vitro | trials |     |
| --- | --- | --- | --- | --- | --- | -------- | ------- | --------- | -------- | --- | ----- | -------- | ------ | --- |
behaviours measurements were conducted to provide conditions with further combi-
Whileourresultsshowthatbothearlybehaviourandquality nations of serum and neuronal differentiation medium. One
indicators vary with differentiation media composition, we trialwith5%serumandmuscleandneuronaldifferentiation
foundnodirectrelationshipbetweenanysingleearlybehav- medium mixed in a ratio of 1:4 and the other with 10%
iourand the qualityof mature myotubes. To study whether serumand exclusively neuronaldifferentiationmedium.
mature cell quality can be determined from the interaction ABMsimulationsreproducedmeanmyonucleidensitiesto
between early-stage behaviours, we designed an ABM of within 1 s.d. of those observed experimentally for most con-
myoblast fusion and myonuclei migration to simulate the ditions (figure 3a). The exceptions of 2% serum with 1:1

(a) 5
measured
|     |     |     | 1500 | simulated |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
ytisned ielcunoym royalsocietypublishing.org/journal/rsif
)2–mmielcun(
1000
500
0
|     |     |     |     | 0   | 0 0   | 1   | 1       | 1   | 1   |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | --- | --- |
|     |     |     | 1:  |     | 1: 1: | 1:  | 0:      | 3:  | 0:  |     |     |
|     |     |     | %,  | %,  | %,    | %,  | %,  %,  |     | %,  |     |     |
|     |     |     | 0   | 2   | 0     | 2   | 2 5     | 0   |     |     |     |
|     |     |     |     |     | 1     |     |         | 1   |     |     |     |
(b)
1.0
noitairav fo tneiciffeoc J.
0.8 R.
Soc.
0.6
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  Interface
0.4
0.2 21:
20230603
0
|     |     |     |     | 0   | 0 0   | 1   | 1       | 1   | 1   |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | --- | --- |
|     |     |     | 1:  |     | 1: 1: | 1:  | 0:      | 3:  | 0:  |     |     |
|     |     |     | %,  | %,  | %,    | %,  | %,  %,  |     | %,  |     |     |
|     |     |     | 0   | 2   | 1 0   | 2   | 2 5     | 1 0 |     |     |     |
Figure3.Comparisonofmeasuredandsimulatedqualityindicatorsatday5ofdifferentiation.Myonucleiqualitymetricsmeasuredfromimagingdatafrominvitro
trials against outputs from the calibrated agent-based model for varying serum concentrations and ratios of muscle to neuronal medium. (a) Myonuclei density.
(b) Coefficient of variation in spatial distribution, a metric of nuclei spatial uniformity. Values are reported as mean ± s.d.
muscle to neuronal cell differentiation media and 2% serum effectsizeofeachmetric.Thenucleirepulsionforceconstant
)wasestimatedtohaveasignificanteffect(t=−2.97,p<
| with100%neuronalcelldifferentiationmedium,whichexhibit |     |     |     |     |     | (k  |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nuc
day5myonucleidensitiessignificantlysmallerthantheinitial 0.05)ondifferenceinmyonucleimm −2(figure4a),withsmal-
Myotube–
number of myoblasts. The ABM assumes that myoblasts do ler k nuc relating to higher densities of myonuclei.
not die during the experimental timeframe and all have the myotube fusion time threshold (t ) and the residence
MTfuse
potential to fuse throughout the differentiation stage and so time threshold (t rmax ) were estimated to have some, though
the total number of nuclei at day 0 is the minimum number notsignificant (t=1.93,p=0.11andt=1.98,p=0.10,respect-
ofmyonucleiobtainablefromsimulation. ively), effecton dM while S and P were estimated to have
mb
To assess whether the ABM simulations successfully the least effect (t=0.29, p=0.78 and t=0.42, p=0.69,
| reproduce changes | inqualityindicatorsovertime, |     |     |     | the mean | respectively). |     |     |     |     |     |
| ----------------- | ---------------------------- | --- | --- | --- | -------- | -------------- | --- | --- | --- | --- | --- |
myonucleidensitiesinaninvitro2%serumandnoneuronal k nuc and t MTfuse were positively associated with (t=3.11,
medium trial were measured on each day of differentiation p=0.01 and t=2.93, p=0.03, respectively) D (figure 4b).
and compared with simulations. Simulated myonuclei den- t was weakly negatively related to (t=−2.30, p=0.07)
rmax
ω
sity (electronic supplementary material, figure S3) was D, while mc and S mb have a limited negative relation (t=
found to bewithin 1s.d.with measuredforeachday. −1.22, p=0.28 and t=−1.21, p=0.28) and P was estimated
m
Median values of D var were reproduced by the ABM to to have the least effect (t=0.13, p=0.90). Owing to the
within1s.d.foralltrials(figure3bandelectronicsupplemen- large variability in D , all the cell behaviour metrics were
var
tary material, table S1). The ABM results showed a smaller estimated to have limited to no effect (figure 4c). The linear
D var than measurements from imaging data (figure 3b and regression analysis shows that all of the cell behaviours
electronicsupplementarymaterial,tableS1).ABMsimulations which were estimated to be significantly associated with
also reproduced measurements of D from imaging data to cell outcomes and qualityindicatorsare inferredrather than
within1s.d.(electronicsupplementarymaterial,tableS1). measured parameters. A comparison of correlation between
Theseresultsimplythattheinvitro/ABMworkflowout- cell behaviour parameters (figure 4d) shows a significant
lined here is sufficiently calibrated to reproduce average (p=0.03) negative correlation between S mb and t MTfuse .
values of qualityindicatorsin trials inwhich fusion occurs. There is also some, non-significant (p=0.06), negative
|                     |             |     |          |                 |         | correlation | betweent          | rmax  | and t MTfuse | .               |       |
| ------------------- | ----------- | --- | -------- | --------------- | ------- | ----------- | ----------------- | ----- | ------------ | --------------- | ----- |
| 2.3. Cell behaviour | parameters  |     | inferred | via approximate |         |             |                   |       |              |                 |       |
|                     |             |     |          |                 |         | 2.4.        | Fitting functions |       | of inferred  | cell behaviours | from  |
| Bayesian            | computation | are | strongly | related         | to cell |             |                   |       |              |                 |       |
|                     |             |     |          |                 |         |             | discrete in       | vitro | experimental | data informs    | media |
| quality indicators  |             |     |          |                 |         |             |                   |       |              |                 |       |
A setof linear regression analyses of measuredand inferred composition of future experiments
cell behaviour metrics against cell quality indicators from in Having determined the significant effects of early-stage cell
vitro experiments was performed to determine the relative behavioursinferredviatheABC–SMCmethodoncellquality

|     |     | (a) |     |     | myonucleimm–2 |     |     |     | (b) | mean distance between myonuclei |     |     |     |     |     | 6   |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
royalsocietypublishing.org/journal/rsif
|     |     | t      |     |                        |     |     |      |     | t      |         |                        |     |       |     |     |     |
| --- | --- | ------ | --- | ---------------------- | --- | --- | ---- | --- | ------ | ------- | ---------------------- | --- | ----- | --- | --- | --- |
|     |     | MTfuse |     |                        |     |     |      |     | MTfuse |         |                        |     |       |     |     |     |
|     |     | k      |     |                        |     |     |      |     | k      |         |                        |     |       |     |     |     |
|     |     | nuc    |     |                        |     |     |      |     | nuc    |         |                        |     |       |     |     |     |
|     |     | t      |     |                        |     |     |      |     | t      |         |                        |     |       |     |     |     |
|     |     | rmax   |     |                        |     |     |      |     | rmax   |         |                        |     |       |     |     |     |
|     |     | P      |     |                        |     |     |      |     | P      |         |                        |     |       |     |     |     |
|     |     |        | m   |                        |     |     |      |     |        | m       |                        |     |       |     |     |     |
|     |     | ω      |     |                        |     |     |      |     | ω      |         |                        |     |       |     |     |     |
|     |     |        | mc  |                        |     |     |      |     | mc     |         |                        |     |       |     |     |     |
|     |     | S      |     |                        |     |     |      |     | S      |         |                        |     |       |     |     |     |
|     |     |        | mc  |                        |     |     |      |     | mc     |         |                        |     |       |     |     |     |
|     |     | –1000  |     | –500                   | 0   | 500 | 1000 |     |        | –30 –20 | –10                    | 0   | 10 20 | 30  |     |     |
|     |     |        |     | normalized coefficient |     |     |      |     |        |         | normalized coefficient |     |       |     |     |     |
J.
R.
|     |     | (c) |     | coefficient of variation |     |     |     |     | (d) |     |     |     |     |     |     |      |
| --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |                          |     |     |     |     |     |     |     |     |     |     | 1.0 | Soc. |
S
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  mc 1 Interface
t
MTfuse
|     |     |     |     |     |     |     |     |     | ω   |             |     |     |     |     | 0.5 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|     |     | k   |     |     |     |     |     |     |     | mc –0.02485 | 1   |     |     |     |     |     |
nuc
21:
|     |     | t    |     |     |     |     |     |     |     | P 0.1108 | 0.4599 1 |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- |
|     |     | rmax |     |     |     |     |     |     |     | m        |          |     |     |     | 0   |     |
20230603
|     |     | P   |     |     |     |     |     |     | t    |             |                | 1       |     |     |      |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | -------------- | ------- | --- | --- | ---- | --- |
|     |     |     | m   |     |     |     |     |     | rmax | 0.4238      | 0.5299 0.0325  |         |     |     |      |     |
|     |     | ω   |     |     |     |     |     |     |      |             |                |         |     |     | –0.5 |     |
|     |     |     | mc  |     |     |     |     |     | k    |             |                |         |     |     |      |     |
|     |     |     |     |     |     |     |     |     |      | nuc –0.1074 | –0.5261 0.1414 | –0.4664 | 1   |     |      |     |
S
mc
–1.0
|     |     |     |     |     |     |     |     |     | t MTfuse | –0.7994 | –0.2425 –0.2228 | –0.7432 | 0.4477 1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------------- | ------- | -------- | --- | --- | --- |
NaN
|     |     |     | –0.4 | –0.2 | 0   |     | 0.2 | 0.4 |     |     |      |      |            |     |     |     |
| --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---------- | --- | --- | --- |
|     |     |     |      |      |     |     |     |     |     | S   | ω P  | t    | k t        |     |     |     |
|     |     |     |      |      |     |     |     |     |     | mc  | mc m | rmax | nuc MTfuse |     |     |     |
normalized coefficient
Figure4.Linearregressionanalysisofmeasuredandinferredcellbehaviourparametersagainstcelloutcomesfrominvitroexperiments.Normalizedcoefficientsof
−2,
cell behaviour parameters with 95% confidence intervals against (a) myonuclei mm (b) mean distance between myonuclei in myotubes and (c) coefficient of
| variation | of  | myonuclei | spatial | distribution, | a measure | of spatial | uniformity. |     |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | ------- | ------------- | --------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     | (a) |     | t    |     |     | (b) |     | k   |     | ×10 | (c) |     | MTfuse |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |     | rmax |     |     |     |     | nuc |     |     | 10  |     |        |     | 6.0 |     |
|     | 10  |     |      |     | 140 |     | 10  |     |     |     | 8   |     |        |     |     |     |
|     |     |     |      |     | 120 |     |     |     |     |     |     |     |        |     | 5.5 |     |
|     | 8   |     |      |     |     |     | 8   |     |     |     | 8   |     |        |     |     |     |
|     |     |     |      |     |     |     |     |     |     |     | 7   |     |        |     | 5.5 |     |
100
|     | mures % |     |     |     |     | mures % | 6   |     |     |     | mures % 6 |     |     |     |          |     |
| --- | ------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --------- | --- | --- | --- | -------- | --- |
|     | 6       |     |     |     | 80  | setunim |     |     |     |     |           |     |     |     | 4.5 syad |     |
6
|     |     |     |     |     | 60  |     |     |     |     |     |     |     |     |     | 4.0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 4   |     |     |     |     |     | 4   |     |     |     | 4   |     |     |     |     |     |
|     |     |     |     |     | 40  |     |     |     |     |     | 5   |     |     |     | 3.5 |     |
|     | 2   |     |     |     |     |     | 2   |     |     |     | 2   |     |     |     |     |     |
|     |     |     |     |     | 20  |     |     |     |     |     |     |     |     |     | 3.0 |     |
|     |     |     |     |     |     |     |     |     |     |     | 4   |     |     |     | 2.5 |     |
0
|     | 0   | 20  | 40  | 60 80 | 100 |     | 0   | 50  |     | 100 | 0   | 20  | 40 60 | 80 100 |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- |
% neuron differentiation medium % neuron differentiation medium % neuron differentiation medium
Figure5.Fittedsurfacefunctionsforinferredcellbehavioursfrominvitroimagingdata.Second-orderfitofbehaviouralparameters.(a)Residencetimethreshold,
(b) nuclei repulsion force coefficient and (c) maximum age at which myotubes can fuse. Black dots denote media compositions of in vitro trials.
indicators, we describe how these key behaviours change as the concentration of neuronal differentiation medium is
with respect to the composition of the differentiation media increased. t was projected to be between 3 and 4.5
MTfuse
in order to suggest optimal media compositions for future days of cell differentiation for most media conditions
in vitro experiments. The effects of media composition on (figure 5c). This agrees with observations of actin striations,
cell behaviours are nonlinear and so a second-degree poly- an indicator of cell maturity, occurring in cells after day
nomial surface model was applied to fit metrics of cell 3. t MTfuse was shown to be earlier in cells cultured in an
behavioursfromeachofthepreviousinvitrotrials(figure5). increased proportion of neuronal differentiation medium
Increasingserumconcentrationwasshowntocorrespond andcontinueforlongerincellsculturedinhigherserumcon-
withanincreaseint (figure5a)suggestingthat,athigher centrations.Sincesimulationswereendedatday5,cellsina
rmax
serumconcentrations,myoblastsrequirealongertimeincon- medium with no neuronal differentiation medium and 10%
tact with myotubes before fusion can occur. k nuc (figure 5b) (or greater) serum concentration may still allow fusion at
showed a general increase with increased serum concen- day 5 and beyond. The surface plots indicate a local
trations, with a slight decline at high concentrations of maxima for t and a local minima for t at a media
|     |     |     |     |     |     |     |     |     |     |     | rmax |     |     | MTfuse |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ------ | --- | --- |
serum (greater than approx. 7%). For media with lower composition of 5% serum and 0% N2B27 differentiation
serum concentrations (less than approx. 4%), k increases media and so this composition was chosen for a further
nuc

|     | (a) | dM  |     |      |     | (b) | D   |     |     | (c) |     | D   | var |      | 7   |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
|     |     |     |     |      |     | 10  |     |     | 80  |     | 10  |     |     | 0.65 |     |
|     | 10  |     |     | 1000 |     |     |     |     |     |     |     |     |     |      |     |
royalsocietypublishing.org/journal/rsif
|     | 8       |     |     | 800 |            | 8       |     |     |     |         | 8   |     |     | 0.60 |     |
| --- | ------- | --- | --- | --- | ---------- | ------- | --- | --- | --- | ------- | --- | --- | --- | ---- | --- |
|     |         |     |     |     | 2–mmielcun |         |     |     | 70  |         |     |     |     |      |     |
|     | mures % |     |     |     |            | mures % |     |     |     | mures % |     |     |     |      |     |
|     | 6       |     |     | 600 |            | 6       |     |     |     |         | 6   |     |     |      |     |
µ/σ
|     |     |     |     |     |     |     |     |     | 60  | mµ  |     |     |     | 0.55 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
|     | 4   |     |     | 400 |     | 4   |     |     |     |     | 4   |     |     |      |     |
|     |     |     |     |     |     |     |     |     | 50  |     |     |     |     | 0.50 |     |
|     | 2   |     |     | 200 |     | 2   |     |     |     |     | 2   |     |     |      |     |
|     |     |     |     | 0   |     |     |     |     | 40  |     |     |     |     | 0.45 |     |
|     | 0   | 50  |     | 100 |     | 0   | 50  | 100 |     |     | 0   | 50  | 100 |      |     |
% neuron differentiation medium % neuron differentiation medium % neuron differentiation medium
−2,
Figure 6. Fitted surface functions forcell quality indicator metrics in vitro imaging data. Second-order fit of metrics of (a) myonuclei mm (b) mean distance
between myonuclei in myotubes and (c) coefficient of variation of myonuclei spatial distribution. Black dots denote media compositions of in vitro trials. Red
| diamond | denotes | extra in | vitro trial informed |     | from analysis | of inferred | cell behaviours. |     |     |     |     |     |     |     |     |
| ------- | ------- | -------- | -------------------- | --- | ------------- | ----------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
J.
R.
Soc.
|     | (a) |     |     |     |     | (b) |     |     |     | (c) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  Interface
|     |     | 1000 |           |     |     | 1000 |     |     |     |                       | 1.0 |     |     |     |     |
| --- | --- | ---- | --------- | --- | --- | ---- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
|     |     |      | myonuclei |     |     |      |     |     |     | 1 yad ta xedni noisuf |     |     |     |     |     |
s.d. myonuclei
|     | 2–mmielcun |     | myoblasts      |     |     | 2–mmielcun |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | -------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |            |     | s.d. myoblasts |     |     |            |     |     |     |     |     |     |     |     | 21: |
0.8
|     |     | 500 |     |     |     | 500 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
20230603
0.6
|     |     | 0   | 2000 4000  |     | 6000 |     | 0 2000 | 4000       | 6000 |     | 0                            |     | 500 | 1000 |     |
| --- | --- | --- | ---------- | --- | ---- | --- | ------ | ---------- | ---- | --- | ---------------------------- | --- | --- | ---- | --- |
|     |     |     | time (min) |     |      |     |        | time (min) |      |     | difference in myotube nuclei |     |     |      |     |
Figure 7. Relation between increase in myonuclei density and fusion index. Examples of agent-based model (ABM) generated changes in myonuclei (red) and
myoblast (blue)nucleidensityovertimeforconditions(a)0%seruminneuronalmediumand(b)2%seruminneuronalmedium(dashedlinesrepresentstandard
(R2=0.96).
deviation over five runs). (c) ABM generated differences in number of myonuclei between days 0 and 5 against fusion index
exploratoryinvitrotrial(k isalsopredictedtoberelatively be influenced by both larger k and little to no increase in
|     |     |     | nuc |     |     |     |     |     |     |     |     | nuc |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
highatthiscomposition,thoughthenearestlocalmaximais dM due to lack of fusion. In media with less than 50%
at7% serum). neuron differentiation media, increasing serum concen-
|     |     |     |     |     |     |     |     | trations | from | 0 to | 5% is | predicted | to decrease | D   | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---- | ----- | --------- | ----------- | --- | --- |
var
|     |     |     |     |     |     |     |     | myotubes | indicating |     | increased | uniformity |     | in distribution. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | ---------- | --- | ---------------- | --- |
2.5. Serum concentrations of 5% predicted to be At high concentrations of N2B27 this was reversed, and
|     |         |          |      |     |        |                 |     | higher | serum | concentrations |     | predict | less uniformly | distribu- |     |
| --- | ------- | -------- | ---- | --- | ------ | --------------- | --- | ------ | ----- | -------------- | --- | ------- | -------------- | --------- | --- |
|     | optimal | in media | with | low | neuron | differentiation |     |        |       |                |     |         |                |           |     |
tedmyonuclei.
media concentrations Our results indicate that a high concentration of neuron
Fitting second-order surface functions to quality indicator differentiation medium has a detrimental effect on muscle
cellfusion,thoughthiscanbereversedthroughtheaddition
| metrics | from | in vitro | trials, including |     | the additional |     | trial at |     |     |     |     |     |     |     |     |
| ------- | ---- | -------- | ----------------- | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
5% serum and no N2B27 medium as suggested by analysis of higher concentrations of serum to the differentiation
|     |     |     |     |     |     |     |     | media. | For media | in  | 100% muscle |     | differentiation | media, | we  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ----------- | --- | --------------- | ------ | --- |
ofinferredcellbehaviours,allowsvisualizationoftheeffects
|     |     |     |     |     |     |     |     | predict | the | optimum | serum | concentration | to  | be 5%. | This |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ----- | ------------- | --- | ------ | ---- |
ofvaryingmediacompositionandthepredictionofanopti-
mal media composition for culturing primary muscle cells aligns with the maximum predicted dM, and lower concen-
|     |     |     |     |     |     |     |     | trations | result | in  | less uniformly |     | distributed | nuclei, | while |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --- | -------------- | --- | ----------- | ------- | ----- |
(figure6).Increasingtheconcentrationofserumispredicted
to increase the dM, indicating increased fusion (figure 6). higherconcentrationshavenosignificanteffectonuniformity
5–6% of distribution. This optimum media composition fits with
| Above |               | serum, | dM then | begins          | to diminish. | Increasing |     |             |     |           |     |          |             |            |     |
| ----- | ------------- | ------ | ------- | --------------- | ------------ | ---------- | --- | ----------- | --- | --------- | --- | -------- | ----------- | ---------- | --- |
|       |               |        |         |                 |              |            |     | predictions |     | made from | the | inferred | early-stage | behaviours |     |
| the   | concentration | of     | neuron  | differentiation |              | medium     | was |             |     |           |     |          |             |            |     |
shown to inhibit fusion (dM tends to zero), especially in t rmax and t MTfuse .
| media | with | low serum | concentrations. |     | In  | media with | no  |     |     |     |     |     |     |     |     |
| ----- | ---- | --------- | --------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
serum,nofusionispredictedaboveanN2B27concentration
|     |     |     |     |     |     |     |     | 2.6. Difference |     | in  | total myonuclei |     | production | is  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --------------- | --- | ---------- | --- | --- |
of24%thoughtheadditionofserumconcentrationsover2%
|        |              |     |              |      |          |      |      | inversely |     | related | to early-stage |     | nuclei | fusion | index |
| ------ | ------------ | --- | ------------ | ---- | -------- | ---- | ---- | --------- | --- | ------- | -------------- | --- | ------ | ------ | ----- |
| fusion | is predicted | to  | be initiated | even | in media | with | 100% |           |     |         |                |     |        |        |       |
neuron differentiation media. An increase in serum concen- One advantage of ABM methods compared with using
tration is predicted to result in a gradual increase in D regressionmodelsaloneistheinsighttheygiveintotheposs-
when N2B27 differentiation media concentrations are below iblemechanismswhichaffecttheoutcomesofamodel.From
50%(figure6).ThistrendisinvertedinN2B27concentrations ABM simulations throughout the parameter space, it was
above50%,withthelargestDpredictedtobeinmediawith noted that conditions generating small (300–400nuclei
noserumand100%N2B27differentiationmedia.Thesefind- mm −2)totalincreasesindM(figure7a)exhibitanegativeexpo-
ings fit the trends observed in k (figure 6) and so D in nential curve in the increase in myonuclei density over time
nuc
media with low serum and high N2B27 concentrations will and a steep initial decline in myoblast numbers, while larger

| Table 2. Time | takentocomplete |     | keyworkflowtasks. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8
royalsocietypublishing.org/journal/rsif
in parallel/additional
| task |     |     |     |     |     | breakdown | of timings |     |     | total | time |     | to in vitro | trials |     |
| ---- | --- | --- | --- | --- | --- | --------- | ---------- | --- | --- | ----- | ---- | --- | ----------- | ------ | --- |
acquisition ofliveimages 2h/video for seventrials. 14h in parallel
analysis ofliveimages 5min/video for sixpositions and 30min 7h in parallel
|     |     |     |     |     |     | processing | datafor | seventrials |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
cell division count 10min/video for sixpositions in seventrials 7h in parallel
ABM–ABC computationof inferredbehaviours 20min/simulationfor up to300simulations 43.75h additional
|     |     |     |     |     |     | run in | parallel on 16cores | for seventrials |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | ------------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
ABM parameter sweep. 20min/simulationfor 121 simulations run in 2.5h additional
J.
|     |     |     |     |     |     | parallel | on 16cores |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
R.
| total time |     |     |     |     |     | —   |     |     |     | 74.3h |     |     | —   |     | Soc. |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ---- |
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  total extratime — 46.3h — Interface
total increases in myonuclei (figure 7b) are associated with a maturecellsaswellasensuringexperimentalreproducibility. 21:
sigmoidalincreaseinmyonucleiovertimewithnucleiinitially Applying quantitative mathematical and computational
20230603
increasing or remaining stable before decreasing. To account modelling approaches alongside in vitro experiments
forthesedistinctivetrends,wefirstcomparedtherateofmyo- increases efficiency and reduces costs when designing cell
nucleiproductionbetweendays0and1withday5difference culturing procedures, aiding the transition from bench to
inmyonucleiforallmedia-typeexperimentsbutfoundnosig- bedside forregenerativemedicine [13].
nificantcorrelation. Wedevelopednovelmetricsforindicatingthequalityand
Further analysis indicates that these differences in total quantity of mature muscle cells cultured from murine myo-
number of myonuclei (and therefore the number of fusion blasts and measured metrics of migratory and proliferative
events) relate to the ratio of myonuclei to total nuclei, myoblastbehaviour.Wefoundthatvaryingtheconcentrations
described by the nuclei fusion index [12], during the initial of media components produces significant changes in indi-
stages of differentiation. There is a strong negative linear cators of mature muscle cell quality and key early-stage cell
relation (R2=0.96) between dM and the nuclei fusion index behaviours. We created and calibrated an agent-based model
atday1 (figure7c). (ABM) to estimate indicators of cell quality using metrics of
|     |     |     |     |     |     |     |     | early-stage | behaviour | as  | inputs. | Using | outputs | of the | ABM |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------- | ----- | ------- | ------ | --- |
2.7. Computational modelling for all conditions can be and in vitro measurements, we inferred further early-stage
metricsofcellfusionandnucleimovementwithinmyotubes.
| completed              |     | in less     | than    | half the         | time     | required | for a |                |            |              |            |              |          |                |          |
| ---------------------- | --- | ----------- | ------- | ---------------- | -------- | -------- | ----- | -------------- | ---------- | ------------ | ---------- | ------------ | -------- | -------------- | -------- |
|                        |     |             |         |                  |          |          |       | These inferred | metrics    | were         | determined |              | to have  | significant    |          |
|                        |     |             |         |                  |          |          |       | effects on     | indicators | of muscle    | cell       | quality      | and      | were applied   |          |
| single                 | in  | vitro trial |         |                  |          |          |       |                |            |              |            |              |          |                |          |
|                        |     |             |         |                  |          |          |       | to define      | the media  | composition  |            | of a further |          | in vitro       | trial in |
| To evaluate            | the | time saved  | using   | our              | workflow | compared |       |                |            |              |            |              |          |                |          |
|                        |     |             |         |                  |          |          |       | order to       | predict    | optimum      | muscle     | cell         | growth.  | Serum          | is       |
| with non-computational |     |             | methods | of optimization, |          | we       | break |                |            |              |            |              |          |                |          |
|                        |     |             |         |                  |          |          |       | added to       | media      | to stabilize | conditions |              | for cell | proliferation, |          |
downthetypicaltimetakentoperformeachstepofthework-
|     |     |     |     |     |     |     |     | though | differentiation | in  | some | muscle | cell lines | has | been |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | --- | ---- | ------ | ---------- | --- | ---- |
flow.Thesetimingsaresummarizedintable2.Computational
showntobetriggeredbythedeprivationofserum.Serumrep-
modellingintheworkflowisdesignedforparallelcomputing
resentsanunknownintermsofcomposition,whichmayalter
andsothetimetakentocompletetaskswillvarysignificantly
|           |      |                   |     |           |     |            |     | motor neuron | differentiation |     | efficiency |     | and | trigger | loss of |
| --------- | ---- | ----------------- | --- | --------- | --- | ---------- | --- | ------------ | --------------- | --- | ---------- | --- | --- | ------- | ------- |
| depending | upon | the computational |     | resources |     | available. | We  |              |                 |     |            |     |     |         |         |
stemness.Ouranalysisindicatesthat,whilemusclecelldiffer-
assumethattheinvitrotrialsrequiredforalternativeoptimiz-
entiationisviableinmediawithoutserum,applyingmoderate
| ation methods | are | at least | as extensive |     | as those | proposed | in  |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ------------ | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
levelsofserumbooststheamountoffusionaswellasincreas-
ourworkflow.SeeMethodsforfurtherdetails.
ingboththespreadandtheuniformityofmyonuclei.Previous
| A parameter  |     | sweep     | of 121    | discrete  | media      | compositions |        |             |        |           |                 |           |         |                 |      |
| ------------ | --- | --------- | --------- | --------- | ---------- | ------------ | ------ | ----------- | ------ | --------- | --------------- | --------- | ------- | --------------- | ---- |
|              |     |           |           |           |            |              |        | work by     | Lawson | & Purslow | [8]             | shows     | C2C12   | cells differen- |      |
| was achieved | in  | under     | 3h using  | a 16-core | processor  |              | to run |             |        |           |                 |           |         |                 |      |
|              |     |           |           |           |            |              |        | tiated best | in low | serum     | media,          | and other | studies | [14]            | show |
| simulations  | in  | parallel. | In total, | the       | live image | acquisition  |        |             |        |           |                 |           |         |                 |      |
|              |     |           |           |           |            |              |        | using media | with   | low serum | is advantageous |           |         | in preparation  |      |
andanalysisandcomputationaleffortrequiredtoimplement
forco-culturingmusclecellswithiPS-derivedmotorneurons.
thisworkflowwaslessthan3.5days,ofwhichupto28hwas
|     |     |     |     |     |     |     |     | Our work | indicates | that | the relationship |     | between |     | serum |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | ---------------- | --- | ------- | --- | ----- |
runinparallelwithinvitrocellmaturation.Forcomparison,a
|     |     |     |     |     |     |     |     | concentration | and | cell fusion | is  | nonlinear. | The | addition | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ---------- | --- | -------- | --- |
singleinvitrotrialrequires9daystoreachday5ofmyotube
moderateconcentrationsofserum(uptoaround5%)hassig-
| differentiation |     | (4 days | in growth | medium |     | and 5 | days in |     |     |     |     |     |     |     |     |
| --------------- | --- | ------- | --------- | ------ | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
nificantbenefitstocellgrowthwithoutimpactingcellquality,
| differentiation | medium). |     |     |     |     |     |     |              |          |                 |              |           |             |                 |         |
| --------------- | -------- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --------------- | ------------ | --------- | ----------- | --------------- | ------- |
|                 |          |     |     |     |     |     |     | with these   | benefits | diminishing     |              | at higher |             | concentrations. |         |
|                 |          |     |     |     |     |     |     | Co-culturing | muscle   | cells           | with neurons |           | has been    | shown           | to      |
|                 |          |     |     |     |     |     |     | increase     | muscle   | cell maturation | [9]          | and       | the ability | to              | culture |
3. Discussion
muscleandneuronalcellsinparallelwouldbeasteptowards
Optimizationofcellculturingprotocolsintissueengineering recreatinganinvivoenvironmentformusclecells.Toachieve
isessential formaintainingthequantityand functionalityof this, a culture medium which effectively sustains and

differentiates bothmuscleandneuronalcellsisrequired.Our high levels of neuron differentiation media indicate that not
results show that increasing the concentration of a neuron allmyoblastsareviable,orthatsignificantnumbersofmyo-
differentiation medium inhibits fusion of myoblasts, though blasts die before they can fuse. We hypothesize that the
thiseffectcouldbepartiallyreversedthroughtheadditionof assumption of universal myoblast differentiation or the lack
higher serum concentrations. Though cell fusion was of acell death mechanism (or both) within the ABM lead to
decreasedwithhigherconcentrationsofneurondifferentiation an over-prediction of myotube formation by the ABM in
medium,therewasnosignificantdecreaseincellquality.Uni- experiments in which myonuclei densities are significantly
formdistributionofmyonucleiisknowntobeassociatedwith smallerthantheinitialnumberofmyoblasts.Nucleistainings
cells inhealthy muscletissue [15], with aggregation of nuclei whichdifferentiatebetweenmyoblastsandmyonucleiwould
linked to muscular disfunction [10,16,17]. In this study, the allow a clearer observation of myoblast fates and allow for
meandistancebetweenmyonucleiandcoefficientofvariation theinclusionofmodelparameterstodeterminemyoblastvia-
of myonuclei were applied as metrics of the uniformity of bility of differentiation and death. Additional early markers
myonucleidistributionwithinacell.Thedifferenceinmyonu- of cell quality include myotube width and the presence of
cleidensitypermm2overthefirst5daysofdifferentiationwas actin striations in myotubes [20]. We found no significant
used as a second indicator of cell outcomes. Trials showing differencesinwidthandahighproportionofactinstriations
greaterincreasesinmyonucleidensityattheendofthediffer- presentinalltrialsandsodidnotincludetheminourinves-
entiationphaseexhibitedalowerfusionindexduringtheearly tigation, though they may be relevant for optimizing other
stages of differentiation. This appears counterintuitive, but cell culture protocols or cell lines. Current practices in cell
since our simulations indicate that myoblast availability is a culturing tend to apply a trial-and-error approach to
limiting factor in cell fusion rate, we hypothesize that media experimental design, though there is acall to move to more
compositions with a lower fusion index prioritize myoblast systematic methods of optimization [5]. Our workflow of
proliferation over fusion during the early stages of differen- informing in vitro experiments by quantifying images and
tiation. The supply of myoblasts will therefore not be analysinginsilicoexperimentscanbeextendedasaniterative
exhausted as quicklyas more fusion-efficient regimes, leading processtofurtheroptimizecellcultureconditions.Italsopro-
to a greater total amount of fusion. The negative relation videsaninsightintothemechanismsunderlyingthechanges
between fusion index and total amount of fusion has wider in cell quality which is absent in methods relying purelyon
implicationsfortherelianceoffusionindexaloneasamarker regressionanalysis.Theworkflowdescribedhereisdesigned
ofexperimentalsuccess.Asfusionindexmeasurestheratioof to be applicable to other cell types, providing they exhibit
myonucleitomononucleatedmyoblastsatagiventime,itcon- earlybehavioursandqualityindicatorswhichcanbequanti-
flates the rate of cell–cell fusion with the proliferation rate of fied and that mature cell quality is not correlated with a
myoblasts.Whilefusionindexissimpletocalculateandgives single behavioural indicator. In this study, we optimize just
anintuitionofinitialexperimentalefficiency,itisimportantto twocellcultureconditions,butoncebehaviouralandquality
consider that a high fusion index may be due to a high indicators have been acquired, adding further variables for
fusion rate of neighbouring cells or a low rate of background optimization is trivial. The number of trials required for
cell division, or some more complex balance between the optimization using a design of experiment (DoE) method
two. Since availability of myoblasts appears to be a limiting increase exponentially with increasing numbers of factors
factor in the total amount of fusion, and thus the final observed and so the application of aworkflow for reducing
volumeofcells,itmayseemintuitivetoculturecellstoconflu- the number of in vitro trials will become increasingly more
ence during the growth phase so there is greater availability. cost-effective. Factors for optimization include further
Previous studies [18], however, show that seeding myoblasts media compositions, materials for substrate structure and
at a high density induces quiescence in cells and suppresses topological constraints such as patternings for aligning
differentiation and sowould notprovide an effective strategy. cells. The design and calibration of the ABM from scratch is
Committed myoblasts need to switch from a proliferation the most time consuming element of our workflow and
state (growth phase) to a fusion state (differentiation phase). requiresspecialistskillswhichmaynotbeimmediatelyavail-
In in vitro culture, this switch can be triggered by lowering able to labs. We have designed the ABM to be both user-
media serum content, which causes myoblasts to initiate cell friendly and customizable for general application, using
cyclearrestanddifferentiateintomyotubes,butthisbehaviour open-sourcesoftwarepackageswherepossible.NetLogosoft-
may be strongly altered if medium composition and serum wareforABMdesignprovidesauser-friendlygraphicaluser
concentrationarenotoptimal. interface (GUI). To obtain inferred cell behaviours, NetLogo
Our numerical modelling assumes that metrics of cell is linked to PyABC via the PyNetLogo extension, example
motion do not change over time. It may be expected that code available on Github, (https://github.com/dhardma2/
cellmigrationspeedandangularvelocitychangeasmyotube MyoChip). PyABC features provision for extensive parallel
density increases with time, though we found no significant computing for this task and so a calculation of the time
changesinmetricsofbehaviour(resultsnotshown)through- required for calibration will depend upon the number
out the first day of differentiation. Temporal changes over a processorsavailable.Byswitchingoffthecellfusionmechan-
longer timescale were not studied but assumed to have a ism,ourABMcanbeappliedasagenericmodelofmotilecell
minor impact on model outputs due to the short timespan behaviourwhichcouldbeusedasabaseforbuildingsimilar
(1–3 days) in which the bulk of fusion occurs. Our model predictive models of further cell types. While the fusion
also assumes that all myoblasts may differentiate into myo- dynamics of the ABM could have potential in studying the
tubes. This may not always be the case, for instance C2C12 formationoffurthertypesofsyncytia,amoreobviousappli-
cells which are deficient in the production of the proteins cationistheoptimizationoffurtherskeletalmusclecelllines
Myf-5andMyo-Dhavebeenshowntofailtoformmyotubes including human-induced pluripotent stem cells and the
inculture[19].Thelowmyonucleidensitiesobservedherefor studyof muscular degenerativediseases.
royalsocietypublishing.org/journal/rsif
J.
R.
Soc.
Interface
21:
20230603
9
5202
rebmetpeS
31
no
/gro.gnihsilbupyteicoslayor//:sptth
morf
dedaolnwoD

| Table 3. Listof | terms and abbreviations. |     |     |     |     |     |     |     |     |     |     |
| --------------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
royalsocietypublishing.org/journal/rsif
| name |     |     | description |     |     |     |     |     |     | symbol |     |
| ---- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ------ | --- |
agent-based model computational model simulating actionsand interactions of autonomous agents. Here, ABM
|     |     |     | agents arecell | nuclei |     |     |     |     |     |     |     |
| --- | --- | --- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
approximateBayesian computation– method forestimating posterior distributions of model parameters without a likelihood ABC–SMC
| sequential | Monte Carlo | method | function            |                      |           |           |     |     |     |     |     |
| ---------- | ----------- | ------ | ------------------- | -------------------- | --------- | --------- | --- | --- | --- | --- | --- |
| myoblast   |             |        | single nuclei       | muscle precursorcell |           |           |     |     |     |     |     |
| myotube    |             |        | multi-nucleatedcell | produced             | fromfused | myoblasts |     |     |     |     |     |
| myonuclei  |             |        | nuclei of amyotube  | cell                 |           |           |     |     |     |     |     |
quality indicators measurable early indicators ofeventual muscle cell qualityand quantity. Here, we use Q
J.
coefficient of variance of myonuclei distance and change in myonuclei density R.
Soc.
early-stage behaviours metrics of myoblastbehaviour which varysignificantly withculture mediacomposition, B
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  Interface
|     |     |     | applied as | inputstothe | ABM. Here,weuse | myoblastspeed, |     | angular | velocityand |     |     |
| --- | --- | --- | ---------- | ----------- | --------------- | -------------- | --- | ------- | ----------- | --- | --- |
proliferationrate
mediafunction generalterm for function determining quality indicators fora givenmediaparameter M(x) 21:
proportion ofneuronal differentiation the fraction ofdifferentiationmedium comprising neuron specificN2B27 medium α 20230603
medium
serum concentration percentage of serum byvolume in cell culturemedia β
myonuclei distance mean distance between myonuclei in givensample cell D
=(cid:1)
myonuclei coefficient of variationin spatial quality indicatorof uniformity in myonuclei distribution(Ds D) D
var
distribution
−2
difference in myonuclei density quality indicatorof cell fusion events, measuredas difference in myonuclei mm dM
|     |     |     | between | days0and | 5ofdifferentiation |     |     |     |     |     |     |
| --- | --- | --- | ------- | -------- | ------------------ | --- | --- | --- | --- | --- | --- |
myoblastspeed mean product ofdistance travelled bya myoblastcell between frames and frame rate S
mb
−1)
(μm min
myoblastvariationin angularvelocity standard deviation of angular deviationof myoblastmotion betweenframes multiplied ω
mb
−1)
|     |     |     | byframerate(degrees |     | min |     |     |     |     |     |     |
| --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
−1
| myoblastrateof | proliferation |     | cell divisions | percell | min |     |     |     |     | P   |     |
| -------------- | ------------- | --- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
area of influence area surrounding nuclei in which the residencetime counter is activatedif another nuclei AoI
is detected
residence time threshold the maximum time thattwonuclei mayspend within each other’s AoIbefore fusion is t
rmax
initiated
| combined | residence time parameter |     | AoI/t |     |     |     |     |     |     | γ   |     |
| -------- | ------------------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
rmax
myotube–myotube fusion time threshold the maximum agethatafused nuclei caninitiate fusion with another myonuclei t
MTfuse
coefficientofnuclei lateralforce coefficient governing thedistance-dependent lateral force enacting on myonuclei k
lat
coefficientofnuclei repulsion force coefficient ofmyonuclei repulsion force, simulating the actin-driven lengthwise repulsion k
nuc
of nuclei
In summary, we identified new quality indicators for andmuscleprogenitorcelllines,includinghumaniPS,provid-
muscle cells, which can be implemented in future statistical ing an efficient and cost-effective method for improving and
approaches to optimization. We showed that changes in the quantifyingtissueengineeringprocedures.
| composition   | of muscle      | cell differentiation | media affect      | both       |     |     |     |     |     |     |     |
| ------------- | -------------- | -------------------- | ----------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| early-stage   | cell migratory | behaviours,          | cell fusion index | and        |     |     |     |     |     |     |     |
| cell quality. | We designed    | an ABM               | to study the      | effects of |     |     |     |     |     |     |     |
4. Methods
measuredandinferredearly-stagecellbehavioursoncellqual-
ity.Ourresultsindicatethatmoderateconcentrationsofserum 4.1. In vitro primary myotube culture
canboostboththequantityandqualityofmusclecellsandcan
Invitromyotubeswereculturedfromprimarymicemyoblastsas
preventtheinhibitoryeffectofneurondifferentiationmedium
|     |     |     |     |     | described | previously |     | [21]. Shortly, | hind limb | muscles | were |
| --- | --- | --- | --- | --- | --------- | ---------- | --- | -------------- | --------- | ------- | ---- |
onmyoblastfusion.Extendingourworkflowtoaniterativeset
|                                                         |     |     |     |     | isolated | from         | 5- to 7-day-old | mice    | pups, minced | and     | digested |
| ------------------------------------------------------- | --- | --- | --- | --- | -------- | ------------ | --------------- | ------- | ------------ | ------- | -------- |
| ofinvitro–insilicoexperimentsherewouldallowoptimization |     |     |     |     |          |              |                 |         | −1           |         |          |
|                                                         |     |     |     |     | for      | 1.5h at 37°C | using           | 0.5mgml | collagenase  | (Sigma) | and      |
of a wide range of further muscle cell culturing parameters 3.5mgml −1 dispase (Roche) in phosphate-buffered saline

|     | (a) |     |        | residence time model |        |     |        |      | (b) | myonuclei forces |     |     |     |     | 11                                      |
| --- | --- | --- | ------ | -------------------- | ------ | --- | ------ | ---- | --- | ---------------- | --- | --- | --- | --- | --------------------------------------- |
|     |     |     |        |                      | t  < t |     | t  > t |      |     |                  |     |     |     |     |                                         |
|     |     |     | t  = 0 |                      | r rmax |     | r      | rmax |     |                  |     |     |     |     |                                         |
|     |     |     | r      |                      |        |     |        |      |     |                  | f   |     |     |     | royalsocietypublishing.org/journal/rsif |
nuc
major axis
f
nuc
|     |     | t = 0 |     |     |     |     |     |     |     |     |     | f nuc |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
r
|     |     | outside area |     | residence time |     |     | fusion |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | -------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
f
|     |     | of influence                         |     | count begins |     |     |     |     |            | lat |     |     |     |     |     |
| --- | --- | ------------------------------------ | --- | ------------ | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
|     |     | centre of nucleus                    |     |              |     |     |     |     | myotube    |     |     |     |     |     |     |
|     |     | area of influence (myoblast nucleus) |     |              |     |     |     |     | myonucleus |     |     |     |     |     |     |
area of influence (myonuclei)
|     |     |     |     |     |     |     |     |     | nuclei repulsion force (f |     |     | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
nuc
|     |     | direction of motion |     |     |     |     |     |     | nuclei lateral force (f |     | )   |     |     |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
lat
|     | (c) | (i) |     |     | (ii) |     |     | (iii) |     |     | (iv) |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | ----- | --- | --- | ---- | --- | --- | --- | --- |
J.
R.
Soc.
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  Interface
21:
Figure8. Overviewofagent-basedmodel. (a)Residencetime model of myoblast–myotube fusion. t isthreshold residence time. (b)Representationof forces
|     |     |     |     |     |     |     |     |     |     | rmax |     |     |     |     | 20230603 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | -------- |
acting on a single nucleus. A lateral force (f ) movesthe nucleus towards the majoraxis of nuclei in a myotube in a direction normal to the major axis. Total
lat
nucleirepulsionforceisthesumoftheindividualrepulsionforces(f )actingonthenucleus.(c)Myotube–myotubefusioninagent-basedmodelat (i)0minand
nuc
(ii) 15min (red dots represent nuclei and green lines represent myotubes) and in live images at (iii) 0min and (iv) 15min.
(PBS).Subsequently,filteredcellsuspensionwasplatedinIMDM takenevery5min foraminimumof12h.Imageswerestitched
(Invitrogen) for 4 h in the incubator (37°C, 5% CO ). To purify using Zen Blue software and stacked into 30min videos for
2
cells from fibroblasts and other contaminating cell types, furtherquantitativeanalysis.
| only non-adherent |     | myoblasts |     | were | collected | and centrifuged. |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------- | --- | ---- | --------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Cellswereresuspendedingrowthmedium(IMDMþ20%FBSþ
|                                                 |     |     |     |     |     |     |     |     | 4.3. Immunostaining |     | and | static imaging |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | -------------- | --- | --- | --- |
| 1%ChickEmbryoExtractþ1%penicillin=streptomycin) |     |     |     |     |     |     | and |     |                     |     |     |                |     |     |     |
plated onto 1:100 matrigel (RD) coated ibidi dishes. After 4 CellswerewashedoncewithPBSandfixedin4%PFAfor10min
|     |     |     |     |     |     |     |     |     | at room | temperature. | Cells | were permeabilized | (PBS | + 0.5% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ----- | ------------------ | ---- | ------ | --- |
days,mediumwaschangedtotriggerdifferentiation.Depending
on the experimental condition, standard muscle differentiation Triton) for 5min and blocked in blocking buffer (10% in goat
medium (IMDMþ1%penicillin=streptomycin) and neuronal serum in PBS + 5% BSA) for 1 hour at room temperature. Pri-
Anti-α-Actinin
medium (N2B27 medium: 50% DMEM-F12, 50%Neurobasalþ mary antibodies (1:200; (Sarcomeric) mouse
1XN2þ1XB27þ50mM b-Mercaptoethanol + 1% penicillin/ monoclonal antibody, Sigma Aldrich and A7732) were diluted
inblockingbuffercontaining0.1%saponineandcellswereincu-
| streptomycin) |     | were mixed | 1:0, | 1:1 | or 0:1, containing |     | 0, 2, | 5   |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | ---- | --- | ------------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
batedat4°Covernight.Disheswerewashedtwicefor5minin
or10%horseserum.After1dayofdifferentiation,athicklayer
of 1:1 matrigel was added on top of forming myotubes and PBS under agitation. Secondary antibodies (1:400; Goat anti-
100ngml −1agrinwasaddedtotheculturemedium.Cellswere Mouse IgG Alexa Fluor 555, Thermo Fisher Scientific, A21424;
culturedupto7daysat37(cid:2)C=5%CO . Goatanti-RabbitIgG AlexaFluor647,Thermo Fisher Scientific,
2
|     |     |     |     |     |     |     |     |     | A21245) in | blocking | buffer | were incubated | in the | presence of |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------ | -------------- | ------ | ----------- | --- |
TheRodentFacilityoftheInstitutodeMedicinaMolecularJoão
|              |     |           |      |           |           |         |     |     | DAPI (100μgml |     | −1) for 1h. | Dishes were | washed | twice, 200μl |     |
| ------------ | --- | --------- | ---- | --------- | --------- | ------- | --- | --- | ------------- | --- | ----------- | ----------- | ------ | ------------ | --- |
| Lobo Antunes |     | maintains | high | standards | of animal | welfare | and |     |               |     |             |             |        |              |     |
promotesaresponsibleuseofanimals,hencesupportingstate-of- Fluoromount-G(Invitrogen)wasaddedontopofcells.Samples
the-art animal-based research. The Rodent Facility has a license werestoredat4°C.Disheswereimagedwithaninvertedfluor-
ofestablishmentforbreedingandanimaluse,issuedbythePortu- escent microscope (Zeiss Cell observer) using a 40× phase air
authority—Direcção-Geral objective (EC Plan-NeoFluar NA 0.75). z-stacks of 1μm were
| guese competent |     |     |     |     | de  | Alimentação |     | e   |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Veterinária(DGAV)—since2013.ThisfacilitycomplieswithPortu-
|     |     |     |     |     |     |     |     |     | taken as | 3×3 | tiles with | 10% overlap | and 1×1 | binning. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ----------- | ------- | -------- | --- |
guese law Decreto-Lei 113/2013, transposed from the European Subsequently,imageswerestitchedinZenBlue.
Directive2010/63/EU,andfollowstheEuropeanCommissionrec-
| ommendations |               | (2007/526/EC) |            | on housing  | and        | care of | animals |     |                              |        |               |                               |                    |     |     |
| ------------ | ------------- | ------------- | ---------- | ----------- | ---------- | ------- | ------- | --- | ---------------------------- | ------ | ------------- | ----------------------------- | ------------------ | --- | --- |
|              |               |               |            |             |            |         |         |     | 4.4. Agent-based             |        | model         |                               |                    |     |     |
| and the      | FELASA        | (Federation   |            | of European | Laboratory |         | Animal  |     |                              |        |               |                               |                    |     |     |
|              |               |               |            |             |            |         |         |     | NetLogosoftware[22].NetLogo. |        |               | (http://ccl.northwestern.edu/ |                    |     |     |
| Science      | Associations) |               | guidelines | concerning  | laboratory |         | animal  |     |                              |        |               |                               |                    |     |     |
|              |               |               |            |             |            |         |         |     | netlogo/.                    | Center | for Connected | Learning                      | and Computer-Based |     |     |
welfare.(EthicsapprovalnumberAEC201403EG).
|     |     |     |     |     |     |     |     |     | Modeling, | Northwestern | University.Evanston, |     | IL.)wasused | to  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | -------------------- | --- | ----------- | --- | --- |
createanuclei-centredagent-basedmodel(ABM).Codeisavail-
|           |         |     |     |     |     |     |     |     | able on Github |             | (https://github.com/dhardma2/MyoChip). |           |            |           | A   |
| --------- | ------- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | -------------------------------------- | --------- | ---------- | --------- | --- |
| 4.2. Live | imaging |     |     |     |     |     |     |     |                |             |                                        |           |            |           |     |
|           |         |     |     |     |     |     |     |     | pseudocode     | description | outlining                              | the rules | of the ABM | is illus- |     |
Live imaging was performed using an inverted microscope trated in electronic supplementary material, figure S5. Terms
(Zeiss Cell Observer SD or Zeiss Cell observer) in widefield andabbreviationsusedareshownintable3.
mode, using a 20× phase air objective (Plan-Apochromat Ph2 The ABM is seeded with initial densities of myoblast nuclei
NA0.80orECPlan-NeofluarPh2NA0.50,respectively).Cells and myonuclei. Random sampling from normal distributions of
were imaged 2h after adding the respective differentiation measured and inferred myoblast behaviour metrics is used to
medium; 3×3 tiles with 10% overlap with 2×2 binning were apply the required inputs to model myoblast motion. Myoblast–

|     |     |     |     | (a) choice of in vitro trials |     |     |     |     |     | 12  |
| --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
royalsocietypublishing.org/journal/rsif
β
α
image processing and quantification
(b)
behaviour metrics from cell tracking nuclei distribution from stained images
J.
R.
Soc.
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  Interface
21:
|     |     |     | S , ω , P |     |     |     | dM, D, D |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | -------- | --- | --- | --- |
|     |     |     | mb mb     |     |     |     |          | var |     |     |
20230603
calibrating the ABM
(c)
|     | agent-based model of nuclei |     |     |                                |            | inferred parameters from ABC-SMC |     |     |     |     |
| --- | --------------------------- | --- | --- | ------------------------------ | ---------- | -------------------------------- | --- | --- | --- | --- |
|     |                             |     |     | (d) linear regression analysis |            |                                  |     |     |     |     |
|     |                             |     |     |                                | y = β  + β | x +                              |     |     |     |     |
|     |                             |     |     |                                | i 0        | 1 i                              |     |     |     |     |
|     |                             |     | (e) | surface fitting and validation |            |                                  |     |     |     |     |
|     |                             |     |     |                                | β          | α                                |     |     |     |     |
Figure 9. Overview of invitro–insilico workflow. (a) Conduct initial in vitro trials with discrete concentrations of serum and neuronal differentiation medium.
|     |     | ,ω  |     |     |     |     |     | =σ/Dfromfixed,stainedimages.(c)Representative |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- |
(b)ObtainmeasureddistributionsofS andPfromtrackingcellsinliveimages.MeasuredM,DandD
|     |     | mb mb |     |     |     |     | var |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
images of ABM(left-hand side, reddots representnuclei and green lines representmyotubes) and visualization ofposterior distributions from pyABC(right-hand
side).ParametersofinferredcellbehavioursderivedusinganABC–SMCmethod.MultipleABMruns,informedbymeasuredmyoblastbehaviours,arecomparedwith
measuredcellqualityindicators(Q).(d)Applylinearregressionanalysistoestimatetheeffectsizeofmeasuredandinferredearly-stagebehaviouralmetrics(B)on
Q. (e) Fit second-order surfaces to values of B found to be predictive of Q to determine concentrations of serum and neuronal differentiation medium likely to
| produce high | Q then conduct further | in vitro | trial(s) with | suggested media | compositions. |     |     |     |     |     |
| ------------ | ---------------------- | -------- | ------------- | --------------- | ------------- | --- | --- | --- | --- | --- |
myotubeandmyotube–myotubefusionismodelledviaaresidence
|     |     |     |     |     |     | 4.5. Model | workflow |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | --- | --- |
timemodel.Oncefused,aforcebalanceisappliedtomyonucleito
Anoverviewoftheworkflowincreatingapredictivemodelofcell
simulatelateralandlongitudinalmotionwithinthecell.TheABM qualityispresentedinfigure9andadetaileddescriptionofeach
providesmetricsofthedensitiesofmyoblastnucleiandmyonuclei processisgiveintheelectronicsupplementarymaterial,Methods.
|            |                   |        |                 |           |     | In vitro | experiments | with different | concentrations | of media |
| ---------- | ----------------- | ------ | --------------- | --------- | --- | -------- | ----------- | -------------- | -------------- | -------- |
| as well as | distances between | nuclei | within discrete | myotubes. |     |          |             |                |                |          |
variablesprovidedatawithwhichtoinitializeandcalibratethe
| Figure 8 | presents an overview | of  | the ABM methodology. |     | A   |     |     |     |     |     |
| -------- | -------------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
ABM(figure9a).Liveimagesofmyoblastsareanalysedtopro-
| detailed | description of the | initialization, | modelling | of myoblast |     |              |                |      |            |                |
| -------- | ------------------ | --------------- | --------- | ----------- | --- | ------------ | -------------- | ---- | ---------- | -------------- |
|          |                    |                 |           |             |     | vide metrics | of early-stage | cell | behaviours | (B) and fixed, |
motion,cellfusion,myonucleimotionandoutputsoftheABMis stained images of myoblasts and myotubes provide cell quality
foundintheelectronicsupplementarymaterial,Methods. indicators (Q) (figure 9b). Metrics of B and indicators of Q

Table 4. ABM input parameters. minima of each metric of B, which in turn relate to increases or
13
|     |     |     |     |     |     |     |     | decreases |              | in Q. Taken | together |      | the plots | can be used | to predict |                                         |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ----------- | -------- | ---- | --------- | ----------- | ---------- | --------------------------------------- |
|     |     |     |     |     |     |     |     | media     | compositions |             | which    | will | provide   | the optimum | values     | royalsocietypublishing.org/journal/rsif |
observedor
|     |     |     |     |     |     |     |     | of  | indicators | of  | Q. Once | one | or more | predicted | optimal |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --- | ------- | --------- | ------- | --- |
inferred
|     |     |     |     |     |     |     |     | media | compositions |     | are | obtained, | further | in vitro | trials can be |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | --- | --------- | ------- | -------- | ------------- | --- |
model parameter from data conducted which can either be assumed to be an optimum
|               |            |      |     |     |     |          |     | value             | or used | to further |     | update | the surface | fitting | models in an |     |
| ------------- | ---------- | ---- | --- | --- | --- | -------- | --- | ----------------- | ------- | ---------- | --- | ------ | ----------- | ------- | ------------ | --- |
| myoblastcount | att        |      |     |     |     | observed |     |                   |         |            |     |        |             |         |              |     |
|               | 0          |      |     |     |     |          |     | iterativefashion. |         |            |     |        |             |         |              |     |
| myotube       | proportion | at t |     |     |     | observed |     |                   |         |            |     |        |             |         |              |     |
0
myoblastspeed ofmotion (S ) observed 4.6. Evaluation of workflow timescale
mb
(ω
myoblastangular velocity ) observed Analysisofstatic,stainedimagestook2hforeachtrial(5minto
mb
download,5mintopre-processimagesand5mintoanalyseper
| myoblastrateof | proliferation(P) |     |     |     |     | observed |     |     |     |     |     |     |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
influence/residencetime unique position for at least six positions with 30min to collate
| nuclei area | of  |     |     | threshold |     | inferred |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
information).Sinceanalysisofstaticimagesisrequiredforatypi-
| (γ=AoI/t |      |     |     |     |     |     |     |                                                          |     |     |     |     |     |     |     | J.  |
| -------- | ---- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|          | )    |     |     |     |     |     |     | calinvitroanalysis,thesetimingshavenotbeenincludedhereas |     |     |     |     |     |     |     |     |
|          | rmax |     |     |     |     |     |     |                                                          |     |     |     |     |     |     |     | R.  |
coefficientoflateralforce anadditionaltaskforourproposedworkflow.
|     |     | (k  | )   |     |     | inferred |     |     |                                                  |     |     |     |     |     |     | Soc. |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---- |
|     |     | lat |     |     |     |          |     |     | Liveimagesforeachtrialwereacquiredovera2hwindow. |     |     |     |     |     |     |      |
coefficientofnuclei
 5202 rebmetpeS 31 no /gro.gnihsilbupyteicoslayor//:sptth morf dedaolnwoD  repulsion force (k ) inferred Interface
|     |     |     |     | nuc |     |     |     | Automatedanalysisofmyoblastmotionbehaviourforeachtrial |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
myotube–myotube
fusion time threshold (t ) inferred took1h(5minofcomputationperuniquepositionforatleastsix
MTfuse
positionsand30mintocollateinformation).Manualcountingof
|     |     |     |     |     |     |     |     | myoblast |             | proliferation | also         | took | 1h (10min  | per position). | Live    | 21: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------------- | ------------ | ---- | ---------- | -------------- | ------- | --- |
|     |     |     |     |     |     |     |     | image    | acquisition |               | and analysis |      | can be run | concurrently   | with in |     |
20230603
vitrotrials.
whichvarywithchangesincellculturevariablesareretained.If AtypicalABMrunwithouttheGUItakesbetween10and20
nodirectrelationshipbetweenanysinglemetricBandindicator mintosimulate5daysofcelldifferentiationandmaturation.The
Q can be found then an ABM is employed to model the inter- ABC–SMCmethodrequiresupto300ABMtrialstoprovidedistri-
actionsbetweenbehavioursandascertaintheeffectsizeofeach butionsof inferred cell behaviours.PyABCfeatures provision for
metricofBonindicatorsQ.
|     |     |     |     |     |     |     |     | extensive | parallel |     | computing | for | thistask | and so any | calculation |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --------- | --- | -------- | ---------- | ----------- | --- |
Nuclei positions are the agents manipulated in the model. oftimerequiredwilldependuponthenumberofprocessorsavail-
The main mechanisms of the ABM, chosen for their simplicity, able.WeranpyABCona16-coreprocessor,takingamaximumof
are a residence-time cell fusion model and a force-balance 6h15mintocompletepertrial(100hofprocessingtimeintotal).
modelactinguponfusednuclei. Gaininginferredbehaviourdistributionsfortheseventrialsused
Certainparametersrequiredtodrivethesemechanismscould
herecanthereforebeachievedwithina2-dayperiod.
not be measured and so, where identified, are inferred using an Once calibrated, the ABM can then be used to predict cell
ABC–SMC
method [23]. Observed metrics of B (table 4) from in quality and quantity for discrete media compositions (10–20
vitrotrialswereappliedasinputstotheABMandmultiplesimu- min per simulation) or sweep through the entire parameter
lationswithdifferentvaluesoftheparameterstobeinferredwere spaceofmediacompositions.
run(figure9c).ThevaluesofindicatorsQproducedasoutputsof
theABMarecomparedwithmeasuredvaluesfromexperimental
|              |            |     |          |       |      |             |     | 4.7. | Statistical | analysis |     |     |     |     |     |     |
| ------------ | ---------- | --- | -------- | ----- | ---- | ----------- | --- | ---- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
| images using | a distance |     | function | based | upon | differences | in  |      |             |          |     |     |     |     |     |     |
number of fusion events, distance between myonuclei and uni- TheWilcoxonsigned-ranktestwasappliedtoassessmeandistance
formity of myonuclei distribution (see electronic supplementary between myonuclei, and two-sample t-tests were applied for all
material,Methodsfordetails).ABC–SMCchoosessamplesofpar- other datasets unless otherwise stated. Statistical analysis and
linearregressionanalysiswasconductedinMatlab.
ametervaluesfromapriordistributionandselectsthesamplesin
whichthedistancefunctionoutputislessthanagiventhreshold
(e)tobuildadistributionoflikelyvaluesofeachparameter.The Ethics. The Rodent Facility of the Instituto de Medicina Molecular
|     |     |     |     |     |     |     |     | Joo | Lobo | Antunes | maintains | high | standards | of animal | welfare |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --------- | ---- | --------- | --------- | ------- | --- |
sizeofeisthensystematicallydecreased.Probabilitydistributions
|     |     |     |     |     |     |     |     | and | promotes | a   | responsible | use | of animals, | hence | supporting |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | --- | ----------- | ----- | ---------- | --- |
thatconvergetowardsaspecificvalueasedecreasesindicatepar-
|     |     |     |     |     |     |     |     | state-of-the-art |     | animal-based |     | research. | The | Rodent | Facility has | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | --------- | --- | ------ | ------------ | --- |
ameters which are sensitive to the indicators Q and qualify for license of establishment for breeding and animal use, issued by
ABC–
further investigation. The likelihood-free methodology of the Portuguese competent authority—Direo-Geral de Alimentao e
SMCallowsparameterstobeinferredwithuniformlydistributed Veterinria (DGAV)—since 2013. This facility complies with Portu-
priors. The initial range of uniform prior distributions used for guese law Decreto-Lei 113/2013, transposed from the European
eachinferredparameterareasfollows:t from1to100,t Directive 2010/63/EU, and follows the European Commission
|                    |     |          |                                  | rmax |     |     | MTfuse |                 |     |     |               |     |            |          |            |     |
| ------------------ | --- | -------- | -------------------------------- | ---- | --- | --- | ------ | --------------- | --- | --- | ------------- | --- | ---------- | -------- | ---------- | --- |
|                    |     |          |                                  |      |     |     |        | recommendations |     |     | (2007/526/EC) |     | on housing | and care | of animals |     |
| from0.5to4.5days,k |     | lat andk | nuc from0to1.Furtherdetailsofthe |      |     |     |        |                 |     |     |               |     |            |          |            |     |
ABC–SMCaredescribedintheelectronicsupplementarymaterial, and the FELASA (Federation of European Laboratory Animal
|         |             |            |     |             |     |           | eare | Science | Associations) |     | guidelines |     | concerning | laboratory | animal |     |
| ------- | ----------- | ---------- | --- | ----------- | --- | --------- | ---- | ------- | ------------- | --- | ---------- | --- | ---------- | ---------- | ------ | --- |
| Methods | and summary | statistics |     | and minimum |     | values of |      |         |               |     |            |     |            |            |        |     |
welfare.
foundinelectronicsupplementarymaterial,tableS2.
Dataaccessibility.Imagingdatausedinthisstudyisavailableandcanbe
| Once | the values | and distributions |     | of measured |     | and inferred |     |     |     |     |     |     |     |     |     |     |
| ---- | ---------- | ----------------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accessedfromthedatasharerepository:https://datashare.ed.ac.uk/
| cell behaviour | parameters |     | B have | been | obtained, | we  | apply |     |     |     |     |     |     |     |     |     |
| -------------- | ---------- | --- | ------ | ---- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
handle/10283/4404[25].Metricsextractedfromimagedataarepro-
| linear regression | analysis | to      | assess  | the effect | size | of each      | metric |       |        |        |      |         |                   |               |     |     |
| ----------------- | -------- | ------- | ------- | ---------- | ---- | ------------ | ------ | ----- | ------ | ------ | ---- | ------- | ----------------- | ------------- | --- | --- |
|                   |          |         |         |            |      |              |        | vided | either | in the | main | text or | in the electronic | supplementary |     |     |
| B on indicators   | Q        | (figure | 9d). If | a metric   | of B | is estimated | to     |       |        |        |      |         |                   |               |     |     |
material[26].TheImageJmacrosforpre-processingimages,Matlab
haveasignificanteffectononeormoreindicatorsofQthenthe
codeforimageanalysis,theNetlogocodefortheABMandPython
valuesofthemetric,takenfrominvitrotrials,arefittedtoasurface
|     |     |     |     |     |     |     |     | code | for linking |     | the ABM | with | pyABC | are available | from the |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ------- | ---- | ----- | ------------- | -------- | --- |
with axis comprising values of media composition variables Zenodorepository:https://zenodo.org/records/10300311[27].
(figure 9e). A second-degree polynomial surface model was Declaration of AI use. We have not used AI-assisted technologies in
applied as suggested for efficient response surface methodology creatingthisarticle.
approximation by Box & Wilson [24]. Surface plots estimate the Authors’ contributions. D.H.: conceptualization, investigation, method-
cell media compositions which will result in local maxima and ology, software, writing—original draft; K.H.: conceptualization,

investigation,methodology,resources,writing—reviewandediting; Conflictofinterestdeclaration.Wedeclarewehavenocompetinginterests.
E.R.G.: methodology, supervision, writing—review and editing; Funding.ThisprojecthasreceivedfundingfromtheEuropeanUnion’s
W.R.:methodology,resources,writing—reviewandediting;M.O.B.:
Horizon 2020 research and innovation programme under grant
methodology, project administration, resources, writing—review agreement no. 801423. This research was funded in whole, or in
andediting. part, by the Engineering and Physical Sciences Research Council
Allauthorsgavefinalapprovalforpublicationandagreedtobe (EPSRC)(grantnos.EP/R029598/1andEP/T008806/1).
heldaccountablefortheworkperformedtherein.
References
1. Mueller C,Trujillo-Miranda M, MaierM, HeathDE, 10. Roman W, Gomes ER.2018Nuclear positioningin 19. YoshikoY,HiraoK,SakabeK,SeikiK,TakezawaJ,
O’Connor AJ,Salehi S.2021Effects ofexternal skeletal muscle.Semin. Cell Dev. Biol.82,51–56. MaedaN.1996Autonomouscontrolofexpressionof
stimulators onengineered skeletal muscle tissue (doi:10.1016/j.semcdb.2017.11.005) genesforinsulin-likegrowthfactorsduringthe
maturation. Adv.Mater.Interfaces8, 2001167. 11. Cadot B,GacheV,Gomes ER.2015Moving and proliferationanddifferentiationofC2C12mouse
(doi:10.1002/admi.202001167) positioning thenucleus in skeletal muscle –one myoblastsinserum-freeculture.LifeSci.59,
2. HindiL, McMillan J, AfrozeD, HindiS, Kumar A. stepat atime.Nucleus 6, 373–381.(doi:10.1080/ 1961–1968.(doi:10.1016/S0024-3205(96)00547-4)
2017Isolation, culturing,and differentiation of 19491034.2015.1090073) 20. DwyerJ,IskratschT,EhlerE.2012Actininstriated
primary myoblastsfrom skeletal muscle ofadult 12. SunY,GeY,DrnevichJ,ZhaoY,BandM,ChenJ. muscle:recent insightsinto assemblyand
mice. Bio-Protocol 7,e2248. (doi:10.21769/ 2010Mammaliantargetofrapamycinregulates maintenance.Biophys.Rev.4,17–25.(doi:10.1007/
bioprotoc.2248) miRNA-1andfollistatininskeletalmyogenesis.J.Cell s12551-011-0062-7)
3. Goers L,Freemont P, PolizziKM. 2014Co-culture Biol.189,1157–1169.(doi:10.1083/jcb.200912093) 21. PimentelMR,FalconeS,CadotB,GomesER.2017In
systems andtechnologies: taking synthetic biology 13. WatersSL,SchumacherLJ,ElHajAJ.2021 vitrodifferentiationofmaturemyofibersforlive
tothenextlevel.J.R.Soc.Interface11,20140065. Regenerativemedicinemeetsmathematical imaging.J.Vis.Exp.2017,55141.(doi:10.3791/55141)
(doi:10.1098/rsif.2014.0065) modelling:developingsymbioticrelationships. 22. WilenskyU.1999NetLogo.Evanston,IL:Centerfor
4. VisMAM,ItoK,HofmannS.2020Impactofculture npjRegenerat.Med.6,24.(doi:10.1038/s41536-021- ConnectedLearningandComputer-BasedModeling,
medium oncellularinteractionsin invitroco- 00134-2) NorthwesternUniversity. Seehttp://ccl.
culturesystems.Front.Bioeng. Biotechnol.8, 911. 14. BrewerGJ, Torricelli JR,EvegeEK, PricePJ. 1993 northwestern.edu/netlogo/.
(doi:10.3389/fbioe.2020.00911) OptimizedsurvivalofhippocampalneuronsinB27- 23. Schälte Y, Hasenauer J.2020Efficient exact
5. MöllerJ, Pörtner R.2017Model-based design of supplemented neurobasal,anewserum-free inferencefor dynamical systems with noisy
processstrategiesforcellculturebioprocesses:state medium combination.J. Neurosci. Res. 35, measurementsusing sequential approximate
ofthe artand newperspectives.In Newinsights 567–576.(doi:10.1002/jnr.490350513) Bayesian computation. Bioinformatics 36,
into cell culture technology. InTech. Seehttp://dx. 15. Bruusgaard JC, LiestølK, Ekmark M, KollstadK, I551–I559.(doi:10.1093/BIOINFORMATICS/BTAA397)
doi.org/10.5772/67600. GundersenK.2003Numberandspatialdistribution 24. BoxGEP, Wilson KB.1951On the experimental
6. YuJS,BagheriN.2021Modular microenvironment ofnuclei in themuscle fibresofnormal mice attainmentofoptimumconditions.J.R.Stat.Soc.:
componentsreproducevasculardynamicsdenovoin studiedinvivo. J.Physiol.551,467–478.(doi:10. Ser.B(Methodological) 13, 1–38. (doi:10.1111/j.
amulti-scale agent-based model.Cell Syst. 12, 1113/jphysiol.2003.045328) 2517-6161.1951.tb00067.x)
795–809.e9.(doi:10.1016/j.cels.2021.05.007) 16. Metzger T, GacheV, Xu M, CadotB,FolkerES, 25. HardmanD,HennigK,GomesER,RomanW,Bernabeu
7. Thorne BC, BaileyAM, Peirce SM. 2007Combining Richardson BE,Gomes ER,Baylies MK.2012MAP MO.2024Aninvitroagent-basedmodellingapproach
experimentswith multi-cell agent-based and kinesin-dependent nuclear positioningis tooptimizationofculturemediumforgenerating
modelingtostudybiological tissue patterning. requiredfor skeletal muscle function. Nature 484, musclecells.Datasharerepository.(https://datashare.
Brief.Bioinform. 8, 245–257.(doi:10.1093/BIB/ 120–124.(doi:10.1038/nature10914) ed.ac.uk/handle/10283/4404)
BBM024) 17. Gimpel Petal. 2017Nesprin-1α-dependent 26. Hardman D, HennigK,Gomes ER,Roman W,
8. Lawson MA, PurslowPP. 2000Differentiation microtubulenucleation from thenuclearenvelope BernabeuMO.2024Aninvitro agent-based
ofmyoblastsin serum-freemedia:effects viaAkap450isnecessaryfornuclearpositioningin modelling approach tooptimization ofculture
ofmodified mediaarecell line-specific. Cells musclecells.Curr.Biol.27,2999–3009.e9.(doi:10. mediumfor generatingmuscle cells. Figshare.
Tissues Organs167,130–137.(doi:10.1159/ 1016/j.cub.2017.08.031) (doi:10.6084/m9.figshare.c.6984361)
000016776) 18. ChowdhurySR,MuneyukiY,TakezawaY,Kino-okaM, 27. HardmanD,HennigK,GomesER,RomanW,
9. BakooshliMA et al.2019A3D culturemodel of SaitoA,SawaY,TayaM.2010Growthand BernabeuMO.2024Aninvitroagent-based
innervated human skeletal muscle enablesstudies differentiationpotentialsinconfluentstateofculture modellingapproachtooptimizationof
ofthe adult neuromuscular junction. eLife 8, ofhumanskeletalmusclemyoblasts.J.Biosci.Bioeng. culturemediumforgeneratingmusclecells.Zenodo.
e44530.(doi:10.7554/eLife.44530) 109,310–313.(doi:10.1016/j.jbiosc.2009.09.042) (https://zenodo.org/records/10300311)
royalsocietypublishing.org/journal/rsif
J.
R.
Soc.
Interface
21:
20230603
14
5202
rebmetpeS
31
no
/gro.gnihsilbupyteicoslayor//:sptth
morf
dedaolnwoD
