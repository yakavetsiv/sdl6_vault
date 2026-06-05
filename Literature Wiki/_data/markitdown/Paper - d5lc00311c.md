---
tags:
  - literature
  - type/paper
  - lit/nanomedicine
  - lit/biofabrication
type: literature-note
source_note: "Papers/Paper - d5lc00311c.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/d5lc00311c.pdf"
converter: "microsoft/markitdown"
---
Lab on a Chip
PAPER
Spheroid-based skin-on-a-chip platform for the
evaluation of the toxicity of small molecules and
Citethis:DOI:10.1039/d5lc00311c †
nanoparticles
Dianoosh Kalhori,‡aFaeze Rakhshani,‡bYingshan Ma, b Ilya Yakavets, b
Sina Kheiri, cOphelieZeyons,dSusanne N.Kolle,e Ted Deisenroth,f
Liangliang Qu,f Zhengkun Chen *band Eugenia Kumacheva *abg
Exposureofhumanskintochemicalagentsmayleadtoskinsensitization,irritation,andcorrosion.Time-
efficienttoxicityscreeningiscurrentlyachievedusinginvitroskin-on-a-chipmodels;however,theseeither
lacka multilayerstructurecharacteristicoftheskin, orrequirelong fabricationtime. Here, wereportthe
development and proof-of-concept application of the microfluidic spheroid-based skin-on-a-chip
platform utilizing gravity-driven flow and large arrays of multilayer skin spheroids (MSSs). The MSSs
containing human dermal fibroblasts inthe coreand keratinocytes intheshell replicatedthedermal and
epidermal layers of skin, respectively. Within 3 days, the toxicity of five distinct small molecules was
Received31stMarch2025, characterized by measuring their IC values, which enabled the differentiation of non-irritant chemical
50
Accepted17thJune2025 agents fromthe irritant onesandcorrelatedwith theirinvivo scoresforskinirritation. Toxicity screening
was extended to nanoparticles, including carbon dots, liposomes, and insecticide-loaded liposomes. This
DOI:10.1039/d5lc00311c
MSS-based skin-on-a-chip microfluidic platform for the safety evaluation of small molecules and
rsc.li/loc nanoparticleshasdiverseapplicationsintheskincare,pharmaceutical,andagriculturefields.
TributetoGeorgeWhitesides
In2002,IspentmysabbaticalwithGeorgeWhitesides.Thiswasaneye-openingandtransformativeexperiencethatinmanywayshaschangedthewayI
doresearch.FollowingmystayinGeorge'slab,Ihaveinitiatedexperimentalworkinthefieldofmicrofluidics.Iusedmyexpertiseinpolymerscienceto
developcontinuousmicrofluidicreactorsforthesynthesisofpolymerparticleswithunprecedentedcontroloftheircompositions,shapesandmorphologies
andwashonoredtocollaboratewithGeorgeWhitesides.In2009,IspentthreemonthsinWhitesides'lab.Followingthisvisit,Ifocusedonpolymer-based
softrobotics.TheatmosphereinWhitesides'labandGeorge'svisionofscienceweretrulyinspirational.Thereisalmostnoresearchareathathehasnot
delvedintoeitherexperimentally,orintellectually.FromNMRspectroscopytomicrofluidics,self-assembly,softrobotics,nanotechnology,andtheoriginof
life among many others, all his work utilized innovative, simple and effective scientific approaches. With his unorthodox way of thinking, Whitesides
challengedhisstudents,postdocsandvisitorstothinkoutsidethebox.Heemphasizedthatsuccessinacademicsciencegoesbeyondhardworkandeven
brillianceinthelabandsharedhisviewsonscientificwriting,thepowerofclearcommunication,researchethics,administration,andresearchsupport.
GeorgeWhitesides'accomplishmentsservedasthesourceofinspirationforseveralgenerationsofscientists.Iamhonoredtocontributeanarticletoa
RoyalSocietyofChemistrycross-journalcollectioninhonourofGeorgeWhitesidestocelebratehis85thbirthday.
EugeniaKumacheva
Introduction
aInstituteofBiomedicalEngineering,UniversityofToronto,164CollegeStreet,
Toronto,Ontario,M5S3G9,Canada.E-mail:eugenia.kumacheva@utoronto.ca
bDepartmentofChemistry,UniversityofToronto,80SaintGeorgeStreet,Toronto, Human skin is frequently exposed to chemical agents that
Ontario,M5S3H6,Canada.E-mail:zhengkun.chen@alumni.utoronto.ca originate from detergents, textiles, cosmetics, pharmaceuticals,
cDepartmentofMechanicalandIndustrialEngineering,UniversityofToronto,5
or environmental
pollutants.1–3
Exposure to these agents may
King'sCollegeRoad,Toronto,Ontario,M5S3G8,Canada
cause adverse skin response varying from sensitization to
dBASFSE,Carl-Bosch-Straße38,67063LudwigshafenamRhein,Germany
eBASFSEExperimentalToxicologyandEcology,Ludwigshafen,Germany irritation and
corrosion.4–6
In addition, skin exposure to
fBASFAdvancedFormulationResearchNorthAmerica,500WhitePlainsRoad, nanoparticles (NPs),2 as well as to the cargo encapsulated in
Tarrytown,NewYork,10591,USA andreleasedfromtheNPs,maycauseinflammatoryresponses,
gDepartmentofChemicalEngineeringandAppliedChemistry,Universityof cytotoxicity,andgenotoxicity.5,7Forexample,aboveathreshold
Toronto,200CollegeStreet,Toronto,Ontario,M5S3E5,Canada
concentration, carbon-based NPs (i.e. carbon dots, C-dots) can
†Electronicsupplementaryinformation(ESI)available.SeeDOI:https://doi.org/
leadtoirritationandallergicreactionsandcausemorphological
10.1039/d5lc00311c
‡Theseauthorscontributedequallytothiswork. changes and loss of viability of skin cells.5,7,8 Lipid NPs
Thisjournalis©TheRoyalSocietyofChemistry2025 LabChip
.MP
50:52:2
5202/03/7
no
otnoroT
fo
ytisrevinU
yb
dedaolnwoD
.5202 enuJ
62
no
dehsilbuP
View Article Online
View Journal

View Article Online
| Paper |     |     |     |     |     |     |     |     |     | LabonaChip |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
encapsulatinginsecticides9,10cancauseallergicreactionsofthe attempttocreateamorephysiologicallyrelevantspheroid-based
skin,duetotheruptureoftheoutermostlayeroftheepidermis model.36,37 Furthermore, large arrays of uniformly sized skin
(stratum corneum) and production of reactive oxidative spheroids grown in a biomimetic environment from human
species.11–13ThecargoloadedinlipidNPsmayalsoaccumulate dermalfibroblastswerepreparedinanMFdevice38andusedfor
in the epidermis and dermis, causing cutaneous toxicity and throughput screening of the effect of vitamins on collagen and
immuneresponse.11,14–16
|     |     |     |     |     |     |     | fibronectin | production. | Combining | MF spheroid-on-chip |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --------- | ------------------- |
Skin response to different substances is conventionally platformswithgravity-drivenfloweliminatedtheneedfortubing,
evaluatedusinganimaltests,e.g.,theDraizeskinirritationtest, interconnects,andsyringepumpsandreducedtheconsumption
whichinvolvesdirectapplicationofthetestsubstancetorabbit ofchemicalagentsforscreeningpurposes.39
skin.17
In addition to ethical concerns about the use of such Here, we report a gravity-driven MF platform tailored for
 .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP
methods,18,19 skin response evaluated on animal models may throughput toxicity screening of chemical agents ranging
not accurately reflect the reaction of human skin, due to the from small molecules to NPs. The MF platform contained a
differentskinanatomy.3,20,21
Thus, thedevelopmentof reliable large array of MSSs with a human dermal fibroblast (hDF)-
in vitro skin models has attracted significant interest and has ladencore(mimickingdermis)andakeratinocyte-ladenshell
led to the adoption of several Organisation for Economic Co- (mimicking epidermis), both embedded in a biomimetic
operation and Development (OECD) test guidelines on skin hydrogel. The toxicity of each tested chemical agent was
toxicity (e.g., OECD Test Guidelines 431, 439, 442D).22–24 evaluated by half-maximal inhibitory concentration (IC ).
50
Currently, the most extensively utilized in vitro skin model for Notably, the mechanism of the toxicity of chemical agents
toxicity tests is the reconstructed human epidermis (RhE) was outside the scope of this work which focused on toxicity
models that are formed by human keratinocytes proliferating screening applications of the skin spheroid-on-chip MF
and differentiating on a cell culture insert.25,26 These models platform. The predictive performance of the platform was
are approved for tests for skin sensitization, irritation, and evaluated by comparing the trends in the variation of IC
50
OECD.22–24 andinvivoscoreslistedintheOECDtestguidelines.22–24The
| corrosion | by  | the |     | Despite | their | broad-range |     |     |     |     |
| --------- | --- | --- | --- | ------- | ----- | ----------- | --- | --- | --- | --- |
applications, the RhE models adopted as the OECD test application of the platform for toxicity tests was extended to
guidelines have several limitations. First, they represent only C-dots, liposomes, and metaflumizone-loaded liposomes,
the epidermal layer of human skin anddo not incorporate the demonstrating its capability to screen NP toxicity. For all
dermalskinlayer.Secondly,theRhEmodeltakesapproximately tested substances, the platform offered time-, cost-, and
epidermis,27,28
14 days to achieve full maturation of the which labor-efficientevaluationoftheirsafety.
prolongsthepreparationofthemodelanddelaysthedecision-
making step on substance toxicity. Thus, there is a growing Results and discussion
demandforthedevelopmentofphysiologicallyrelevantmodels
that can be used for time-efficient throughput screening to GenerationofMSSarrays
evaluate the toxicity of different substances for the skin. Such A microwell MF device illustrated in Fig. 1 was used for the
models would also ensure the development of safer products generation of MSSs38 and toxicity screening. In this device,
forhumanskin. individual MSSs were cultured inside cylinder-shaped
Integrating microfluidic (MF) technologies with 3D microwellsthatwere254μminheightand200μmindiameter.
organotypic human skin models, termed skin-on-a-chip Fourparallelrows,eachwith50microwellsandamicrochannel
|     |     |     |     |     |     |     | μm  | × μm |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
platforms, is an advanced approach to replacing animal (54 high 133 wide) supplying cell culture media, a
models.29,30 For example, by combining the RhE model with solution of the chemical agent, or a NP dispersion, were
MFs, an epidermis-on-a-chip platform was developed for the connected to a common inlet and outlet. Later in the text, we
evaluationofskinirritationbychemicalagents.29Thedynamic
| cell culture            | environment | and          | the        | air–liquid   | interface | provided     |      |     |     |     |
| ----------------------- | ----------- | ------------ | ---------- | ------------ | --------- | ------------ | ---- | --- | --- | --- |
| by MFs                  | improved    | the barrier  | function   |              | of the    | model,       | in   |     |     |     |
| comparison              | with        | conventional | transwell  | culture.29   |           | In addition, |      |     |     |     |
| a full-thickness        |             | skinmodel    | containing | boththe      | epidermis |              | and  |     |     |     |
| dermis was              | developed   | by seeding   |            | keratinocyte | cells     | on the       | top  |     |     |     |
| of the fibroblast-laden |             | matrix       | in         | the MF       | device.31 | Yet,         | both |     |     |     |
modelsrequiredafabricationtimeofover14days.29,31
| Skin            | spheroids, | 3D aggregates |          | of skin         | cells recapitulating |           |      |     |     |     |
| --------------- | ---------- | ------------- | -------- | --------------- | -------------------- | --------- | ---- | --- | --- | --- |
| many properties |            | and functions | of       | skin,           | have emerged         |           | as a |     |     |     |
| promising       | in vitro   | model.        | Dermal32 | and epidermal33 |                      | spheroids |      |     |     |     |
culturedfor7daysmimickedthephysiologicalfunctionsofskin
| tissues by | secreting | dermal | extracellular | matrix | (ECM) | proteins |     |     |     |     |
| ---------- | --------- | ------ | ------------- | ------ | ----- | -------- | --- | --- | --- | --- |
andexpressingepidermaldifferentiationmarkers.32,34,35Recently,
multilayer skin spheroids (MSSs) incorporating dermal and Fig. 1 Microfluidic (MF) platform containing MSS arrays for toxicity
| epidermal | layers | of human | skin | have been | developed | in  | the screening. |                                              |     |     |
| --------- | ------ | -------- | ---- | --------- | --------- | --- | -------------- | -------------------------------------------- | --- | --- |
| LabChip   |        |          |      |           |           |     |                | Thisjournalis©TheRoyalSocietyofChemistry2025 |     |     |

View Article Online
| LabonaChip |     |     |     |     |     |     |     |     |     |     |     |     |     | Paper |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
−1
refer to this design as a “quadruplet”.38 Each MF device with perfused at a flow rate of 0.1 mL h for 24 h at 37 °C
dimensionsof75×50mmaccommodated12quadrupletswith through the MF device. The details of MSS formation are
a total number of 2400 MSSs, which allowed simultaneous providedinthematerialsandmethodssection.
screeningof12samplesusing200MSSsforeachtestedsample. ThetoxicityofchemicalagentsorNPswastestedonday2
μL
Gravity-driven flow was used to supply solutions of by filling the pipette tips with 400 of a solution of a
chemical agents or dispersions to the MSSs located in the chemicalagentoraNPdispersionandplacingtheMFdevice
microwells.39 Pipette tips were introduced into the inlet and on a rocker platform to subject the MSSs to gravity-driven
outlet of the quadruplets and filled with cell culture media, flow for a particular time interval. After that, a solution of a
or solutions of chemical agents, or dispersions of NPs. The chemical agent or a NP dispersion in the pipette tips was
MF device was placed on a rocker platform to create gravity- replaced with a cell culture medium that was perfused
 .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP
driven flow of the liquid in the quadruplet. A hydrostatic throughtheMFdevicefor60minforcellrecovery.Sinceskin
pressure difference was generated by creating a height irritation is initiated by cellular damage, cell viability was
differential in the liquid levels within the reservoirs, which selected as the primary characteristic for irritation
was controlled by adjusting the tilting angle and the period assessment, in accordance with the OECD Test Guideline
| oftherockerstage.39Torecapitulateamultilayerstructureof |     |     |     |     |     | 439.24 |      |           |     |          |     |           |      |          |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | ------ | ---- | --------- | --- | -------- | --- | --------- | ---- | -------- |
|                                                         |     |     |     |     |     |        | Cell | viability | was | assessed | by  | live/dead | cell | staining |
human skin, we generated MSSs with hDFs in the core and using calcein-AM (green; live cells) and propidium iodide
keratinocytes(HaCaTcells)intheshell,bothencapsulatedin (red; dead cells). To compare the impact of different agents,
concentration–response
a biomimetic hydrogel composed of aldehyde-functionalized we utilized the curve to calculate the
cellulose nanocrystals and gelatin (termed EKGel)40 (see values of IC . The trends of change in IC values were
|     |     |     |     |     |     |     |     | 50  |     |     |     | 50  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
details in the materials and methods section). The average analyzed and compared with the in vivo scores outlined in
guidelines.22–24
diameter of the MSSs was 182 ± 7 μm (Fig. S1, ESI†). Since the OECD In this approach, the toxicity was
HaCaT cells offer greater consistency and scalability than assessed using the IC values derived from concentration–
50
primary human keratinocytes and have demonstrated response curves. Compared to the single-concentration
comparable responses in inflammation modeling,41,42 we viability measurements used in conventional in vitro models,
selected them as a model for evaluating skin toxicity in the this method provided a more comprehensive evaluation of a
developedMFplatform. chemical agent'stoxicity. Notably,the classificationasanon-
Fig. 2 illustrates the workflow of the experiments. On day irritant did not imply a complete absence of the cytotoxic
0, hDFs were mixed with precursors of EKGel-1 at a cell effects in vitro, as chemical agents exhibiting mild in vitro
density of 4.9 × 105 cells per μL, and the cell suspension was toxicitywerestillconsideredtobenon-irritants.
| introduced into        | the | quadruplet | to form    | hDF-laden | droplets |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ---------- | ---------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| filling the microwells |     | of the     | MF device. | Following | EKGel-1  |     |     |     |     |     |     |     |     |     |
gelation within 2 h at 37 °C, the device was incubated at 37 CharacterizationofMSSsandoptimizationofscreening
| °C       |      |            |           |        |              | conditions |     |     |     |     |     |     |     |     |
| -------- | ---- | ---------- | --------- | ------ | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| for 24 h | with | continuous | perfusion | of the | cell culture |            |     |     |     |     |     |     |     |     |
medium at a flow rate of 0.1 mL L −1. On day 1, dermal The distribution of fibroblasts and keratinocytes in the MSSs
fibroblastspheroids(DFSs)wereformedwithadiameter26% was verified by on-chip immunofluorescence staining. Cell
smaller than the diameter of the microwells, that is, an nuclei were stained with Hoechst dye. Claudin-1, a
unoccupied space appeared around the MSSs in the transmembrane protein found in keratinocytes forming tight
microwells. A suspension of keratinocytes mixed with the junctions, was used to identify keratinocyte localization in the
EKGel-2 precursors was introduced into the supplying MSS shell. Fibronectin, a major protein in the dermal
|     |     |     |     |     | × 105 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
channel of the quadruplet at a cell density of 6.3 cells extracellular matrix, was stained to identify the location of
per μL. This suspension filled the free space in the fibroblasts in the MSS core. Fig. 3A displays the representative
microwells, thus engulfing the DFSs. After the gelation of confocal fluorescence microscopy images of the MSSs. Three
°C,
EKGel-2 in 1.5 h at 37 the cell culture medium was images (left-to-right) explicitly show a fibroblast core (green)
|     |     |     |     |     |     | surrounded |     | with | a layer | of  | keratinocytes |     | (red), | thereby |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ------- | --- | ------------- | --- | ------ | ------- |
confirmingtheformationofacore–shellstructureoftheMSSs.
|     |     |     |     |     |     | Such            | spheroids |         | were       | reported      | to        | express           | epidermal  |           |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | ------- | ---------- | ------------- | --------- | ----------------- | ---------- | --------- |
|     |     |     |     |     |     | differentiation |           | and     | barrier    | proteins,     | including |                   | involucrin | and       |
|     |     |     |     |     |     | keratins.36     |           |         |            |               |           | air–liquid        |            |           |
|     |     |     |     |     |     |                 |           | Despite | the        | absence       | of an     |                   | interface, | the       |
|     |     |     |     |     |     | MSSs            | expressed |         | the marker |               | for the   | tight junction    |            | of the    |
|     |     |     |     |     |     | epidermis       |           | (Fig.   | 3A) and    | functional    | barrier   | properties        |            | (Fig. S2, |
|     |     |     |     |     |     | ESI†).          | These     |         | features   | contributed   | to        | increased         | chemical   |           |
|     |     |     |     |     |     | resistance      |           | of the  | MSSs       | and supported |           | the applicability |            | of the    |
modelforthroughputtoxicityscreening.
|     |     |     |     |     |     |     | To determine |     | the | conditions |     | of MSS | exposure | to  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---------- | --- | ------ | -------- | --- |
Fig. 2 Timeline for the generation of the MSSs and screening of chemical agents or NPs, we first subjected the MSSs to 0.5
chemicalagentsorNPdispersions. wt% Triton X-100 solution and Hank's balanced salt
| Thisjournalis©TheRoyalSocietyofChemistry2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | LabChip |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |

View Article Online
| Paper |     |     |     |     |     |     |     |              |           |             |          |        |           | LabonaChip      |        |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | ----------- | -------- | ------ | --------- | --------------- | ------ |
|       |     |     |     |     |     |     |     | To determine |           | the optimal |          | day of | the onset | of cytotoxicity |        |
|       |     |     |     |     |     |     |     | tests, cell  | viability | in          | the MSSs | was    | assessed  | after           | 60 min |
2–4.
|     |     |     |     |     |     |     |     | exposure           | to HBSS  | on           | days | As a     | negative | control,  | HBSS      |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | -------- | ------------ | ---- | -------- | -------- | --------- | --------- |
|     |     |     |     |     |     |     |     | was expected       | to       | have minimal |      | impact   | on cell  | viability | in the    |
|     |     |     |     |     |     |     |     | MSSs. Fluorescence |          | images       | of   | the MSSs | in       | Fig. 3D   | show that |
|     |     |     |     |     |     |     |     | a major            | fraction | of cells     | in   | the MSSs |          | exposed   | to HBSS   |
solutionwerealiveonday2.Cellviabilitydecreasedbyday4,
|     |     |     |     |     |     |     |     | as indicated  | by  | the overlay | of   | green  | (live cells) | and    | red (dead  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ---- | ------ | ------------ | ------ | ---------- |
|     |     |     |     |     |     |     |     | cells) images |     | resulting   | in a | yellow | color        | in the | MSS shell. |
Overall,cellviabilityintheMSSswas87,79,and72%onday
 .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP
|     |     |     |     |     |     |     |     | 2, 3, and | 4,        | respectively        | (Fig.     | 3E).         | The        | decrease  | of MSS   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------------- | --------- | ------------ | ---------- | --------- | -------- |
|     |     |     |     |     |     |     |     | viability | over time | was                 | primarily | due          | to the     | formation | of a     |
|     |     |     |     |     |     |     |     | necrotic  | core      | by the fibroblasts, |           | as           | previously | observed  | in       |
|     |     |     |     |     |     |     |     | DFS with  | a similar | size.38             |           | Since the    | MSSs       | had       | a higher |
|     |     |     |     |     |     |     |     | viability | on day    | 2, this             | time      | was selected | as         | the onset | of the   |
|     |     |     |     |     |     |     |     | toxicity  | tests.    | Furthermore,        | screening |              | on day     | 2 reduced | the      |
durationoftoxicityscreeningexperiments.
| Fig. 3 Immunostaining |     |                | of MSSs | and      | optimization | of  | screening  |     |     |     |     |     |     |     |     |
| --------------------- | --- | -------------- | ------- | -------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| parameters.           | (A) | Left-to-right: |         | confocal | fluorescence |     | microscopy |     |     |     |     |     |     |     |     |
Evaluationofskinirritationwithsmallmolecules
imagesofMSSshowingthenuclei(blue),fibronectin(green),claudin-1
| (red), and   | a merged | image.     | (B) | Fluorescence | microscopy    |     | images of    |           |     |            |     |              |     |             |      |
| ------------ | -------- | ---------- | --- | ------------ | ------------- | --- | ------------ | --------- | --- | ---------- | --- | ------------ | --- | ----------- | ---- |
|              |          |            |     |              |               |     |              | To assess | the | utility of | the | MF platform, |     | we selected | five |
| MSSs stained | with     | calcein-AM |     | (green)      | and propidium |     | iodide (red) |           |     |            |     |              |     |             |      |
showing live and dead cells, respectively. (C) Viability of cells in the substanceswithknownskinirritationeffects.Isopropylalcohol
MSSsexposedto0.5wt%solutionofTritonX-100asapositivecontrol (IPA), 3-amino-1,2,4-triazole (AT), and polyethylene glycol 400
| for 15, 30, | 45, and | 60      | min on | day 2. (D) | Fluorescence |      | microscopy |                                               |          |     |     |                |     |               |     |
| ----------- | ------- | ------- | ------ | ---------- | ------------ | ---- | ---------- | --------------------------------------------- | -------- | --- | --- | -------------- | --- | ------------- | --- |
|             |         |         |        |            |              |      |            | (PEG) were                                    | selected | as  | the | representative |     | non-irritants | and |
| images of   | MSSs    | stained | with   | calcein-AM | (green,      | live | cells) and |                                               |          |     |     |                |     |               |     |
|             |         |         |        |            |              |      |            | 2-chloromethyl-4-methoxy-3,5-dimethylpyridine |          |     |     |                |     | hydrochloride |     |
propidiumiodide(red,deadcells).(E)CellviabilityinMSSsexposedon
days2–4for60mintoHBSS.Thedataarerepresentedasmean±SD. (CMDH) and 1-methyl-3-phenylpiperazine (MPP) were selected
A total of at least 180 MSSs were analyzed from three independently as the representative skin irritants. Cell viability was assessed
prepared MSS arrays. Statistical analysis was performed with a one- after 60 min exposure of MSSs to each agent at varying
wayanalysisofvariance(ANOVA)testwithaTukeypost-hoctest.**p
<0.01.Scalebarsare100μm. concentrations in HBSS, which was followed by 60 min
perfusionofthecellculturemediumforcellrecovery.Thevalue
|     |     |     |     |     |     |     |     | of IC of | the | selected | chemical | agents | was | determined | using |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | -------- | ------ | --- | ---------- | ----- |
50
thecorrespondingconcentration–responsecurves,withahigher
solution (HBSS), acting as the positive and negative controls, IC valuereflectingalowerskintoxicity.
50
concentration–response
respectively. Fig. 3B shows the representative fluorescence Fig. 4 shows the curves of the
microscopy images of the MSSs exposed to 0.5 wt% Triton selected substances. The values of IC for IPA, AT, and PEG
50
X-100 solution for 15, 30, and 60 min. Following 15 min (all non-irritants) were 6.8, 29, and 31 wt%, respectively. In
exposure, the majority of dead cells accumulated near the contrast, MPP and CMDH (skin irritants) exhibited IC
50
MSS surface, suggesting incomplete MSS permeation with values of only 0.78 and 0.27 wt%, respectively. These results
Triton X-100. With an increasing exposure time, the fraction were compared with the reported in vivo scores obtained
of dead cells significantly increased, and following a 60 min from animal tests and cell viability determined using a
exposure to Triton X-100 solution, the dead cells were commerciallyavailableskinmodel,EpiDerm™.43
| uniformly     | distributed  |               | throughout | the           | MSSs.        | To quantify        | cell        |     |     |     |     |     |     |     |     |
| ------------- | ------------ | ------------- | ---------- | ------------- | ------------ | ------------------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| viability     | in the       | MSSs,         | we         | measured      | the          | ratio              | of the      |     |     |     |     |     |     |     |     |
| fluorescence  | intensity    |               | of live    | cells         | to the       | total fluorescence |             |     |     |     |     |     |     |     |     |
| intensity     | of both      | live          | and dead   | cells         | (Fig.        | 3C). Exposure      | of          |     |     |     |     |     |     |     |     |
| the MSSs      | to 0.5       | wt%           | solution   | of            | Triton       | X-100              | for 15, 30, |     |     |     |     |     |     |     |     |
| and 60        | min          | resulted      | in 40,     | 25,           | and 14%      | cell               | viability.  |     |     |     |     |     |     |     |     |
| Consequently, |              | the viability | after      | 60            | min exposure |                    | of 0.5 wt%  |     |     |     |     |     |     |     |     |
| Triton        | X-100        | was           | selected   | as            | the minimum  |                    | viability   |     |     |     |     |     |     |     |     |
| threshold     | for          | the positive  | control.   |               | In all       | toxicity           | screening   |     |     |     |     |     |     |     |     |
| experiments   | conducted    |               | for        | low-molecular |              | weight             | chemical    |     |     |     |     |     |     |     |     |
| agents,       | the exposure |               | time       | was set       | to 60        | min                | to ensure   |     |     |     |     |     |     |     |     |
Fig.4 Concentration–responsecurvesforMSSsexposedtosolutions
| complete | MSS | permeation. |     | Such exposure |     | time | falls within |             |      |            |              |                |     |     |           |
| -------- | --- | ----------- | --- | ------------- | --- | ---- | ------------ | ----------- | ---- | ---------- | ------------ | -------------- | --- | --- | --------- |
|          |     |             |     |               |     |      |              | of selected | test | substances | at different | concentrations |     | in  | HBSS. The |
the range of the durations used in existing OECD-approved dataarerepresentedasmean±SD.Atotalofatleast150MSSswere
irritation models.24 measuredfromthreeindependentlypreparedarrays.
| LabChip |     |     |     |     |     |     |     |     | Thisjournalis©TheRoyalSocietyofChemistry2025 |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |

View Article Online
| LabonaChip |     |     |     |     |     |     |     |     |     |     |     |     | Paper |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Table1 Toxicityscoresforchemicalagents
Agenta Stateb Invivoscore43 InvitroEpiDermmodel(viability)43 IC c(wt%) Category
50
| PEG  |     | Liquid |     | 0   |     | 99.9 |     |     |     | 31   |     |     | Non-irritant |
| ---- | --- | ------ | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | ------------ |
| AT   |     | Solid  |     | 0   |     | 92.1 |     |     |     | 29   |     |     | Non-irritant |
| IPA  |     | Liquid |     | 0.3 |     | 90.1 |     |     |     | 6.8  |     |     | Non-irritant |
| MPP  |     | Solid  |     | 3.3 |     | 7.4  |     |     |     | 0.78 |     |     | Irritant     |
| CMDH |     | Solid  |     | 2.7 |     | 6.7  |     |     |     | 0.27 |     |     | Irritant     |
a Water-soluble chemical agents were selected for screening tests using MSS arrays and comparison of IC values with the corresponding
50
reportedin vivoscoresandinvitro cellviabilitydata.43 b All ofthechemicalagentsweretestedinHBSS.c ThevaluesofIC wereestimated
50
basedonthreeindependentlypreparedarrayscontainingatotalofatleast150MSSs.
 .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP
Table 1 shows that within the group of non-irritants, the Using the workflow developed for toxicity screening of
decreasing degree of toxicity from IPA to AT and PEG was solutions of small molecules, a dispersion of C-dots in HBSS
reflected by the decreasing in vivo scores obtained from with concentrations of 0.01, 0.1, 2.0, and 8.0 wt% was
animal tests and the increasing cell viability in the supplied to the MSS arrays and to the MF device not
commercial in vitro model EpiDerm™ skin irritation test.43 containing MSSs as a control. Fluorescence images of the
Although the scores for AT were given for its solid state, a MSSs were taken 2, 15, 30, 45, and 60 min after the
similar trend was observed in the MF toxicity screening tests beginning of perfusion to characterize C-dot uptake by the
ESI†).
in our work, with an increasing IC 50 value from IPA to AT MSSs (Fig. S3, To determine C-dot retention in the
and PEG. In the group of irritants, MPP and CMDH exposed MSSs, immediately after C-dot dispersion perfusion, the cell
to the in vitro EpiDerm™ skin irritation test showed 7.4 and culture medium was supplied to the MF device for 60 min,
6.7% cell viability, respectively.43 This trend agreed with a andthefluorescenceimagesoftheMSSswerere-taken.
higher value of IC for MPP than that for CMDH. Notably, The variation in the uptake and retention of C-dots in the
50
based on the reference data provided in the OECD test MSSs with perfusion time was characterized by determining
guideline,24 the in vivo score of MPP was higher than that of the PL intensity of the MSSs at a particular time point and
CMDH, while the opposite trend was observed for the normalizing it by the PL intensity of the empty microwells
corresponding IC values. Yet, this discrepancy did not alter filled with C-dot dispersion with the corresponding
50
the conclusion that based on the IC values, both chemical concentration of C-dots after 2 min perfusion, as shown in
50
agents could be classified as irritants. Thus, the results of Fig. 5D and E, respectively. For all examined concentrations
toxicity screening using an MF array of MSSs correlated with of C-dot dispersions, the averaged normalized PL intensity,
in vivo scores, and such correlation allowed us to establish I , leveled off after 2 min. This time corresponded to the
PL
the criterion for the MSS arrays used as a preliminary beginning of MSS exposure to C-dot dispersion. Perfusion of
| prediction | model. | As the | IC  | of non-irritants |     | tested was in |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | --- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
50
| the range | between  | 6 and  | 30%, | we inferred | that        | chemicals |     |     |     |     |     |     |     |
| --------- | -------- | ------ | ---- | ----------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| with an   | IC value | within | this | range or    | even higher | are more  |     |     |     |     |     |     |     |
50
likelytobeclassifiedasnon-irritants;however,weadmitthat
| additional | tests | are needed |     | to establish | a universal | IC  |     |     |     |     |     |     |     |
| ---------- | ----- | ---------- | --- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
50
threshold.
EvaluationofthetoxicityofC-dots
| Since C-dots   | have  | a broad       | range | of applications |     | in skincare  |     |     |     |     |     |     |     |
| -------------- | ----- | ------------- | ----- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| products,44,45 | e.g., | in protecting |       | skin from       | the | effect of UV |     |     |     |     |     |     |     |
irradiation,46
we used a MF array of MSSs to examine C-dot Fig. 5 Screening C-dot toxicity. (A) TEM image of C-dots. The scale
toxicity.ThedetailsofC-dotsynthesisaredescribedintheESI.† bar is 20 nm. (B) Histogram of C-dot size distribution, based on the
Fig. 5A and B show a representative transmission electron TEM image analysis. n = 50. (C) Excitation and emission spectra of
C-dotsacquiredonday0and7afterincubationinHBSSat37°C.(D)
| microscopy | (TEM) | image | of C-dots | and           | their size | distribution |              |               |            |        |               |                |             |
| ---------- | ----- | ----- | --------- | ------------- | ---------- | ------------ | ------------ | ------------- | ---------- | ------ | ------------- | -------------- | ----------- |
|            |       |       |           |               |            |              | Variation in | PL intensity, | I ,        | of the | MSSs, plotted | as a           | function of |
| determined | by    | image | analysis, | respectively. |            | The average  |              |               | PL         |        |               |                |             |
|            |       |       |           |               |            |              | perfusion    | time of the   | dispersion | with   | C-dot         | concentrations | of 8.0      |
diameterofC-dotswas5±1nm.SincetheinvestigationofMSS (red),2.0(blue),0.1(orange),and0.01(green)wt%.(E)VariationinI
PL
permeation with C-dots utilized their photoluminescence (PL), oftheMSSsasin(D),plottedasafunctionofperfusiontimeofthecell
we acquired the excitation and emission spectra of C-dots in culture medium. The line colors correspond to C-dot concentrations
asin(D).(F)Concentration–responsecurveofMSSsexposedtoC-dot
| HBSS solution. |     | The excitation |     | and emission | peaks | of C-dots |             |                |                 |     |          |        |           |
| -------------- | --- | -------------- | --- | ------------ | ----- | --------- | ----------- | -------------- | --------------- | --- | -------- | ------ | --------- |
|                |     |                |     |              |       |           | dispersions | with different | concentrations. |     | The data | points | are shown |
werecenteredat344and420nm,respectively(Fig.5C).ThePL
asmean±SD.Eachdatapointrepresentsmeasurementsfromatotal
properties of C-dots did not appreciably change 7 days after of at least 180 MSSs collected from three independently prepared
| synthesis,ensuringgoodstabilityofPLintheC-dots. |     |     |     |     |     |     | arrays. |     |     |     |     |     |         |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ------- |
| Thisjournalis©TheRoyalSocietyofChemistry2025    |     |     |     |     |     |     |         |     |     |     |     |     | LabChip |

View Article Online
| Paper       |         |        |              |                |         |          |          |     |     |     |     |     | LabonaChip |     |
| ----------- | ------- | ------ | ------------ | -------------- | ------- | -------- | -------- | --- | --- | --- | --- | --- | ---------- | --- |
| dispersions | with    | higher | C-dot        | concentrations |         | resulted | in       |     |     |     |     |     |            |     |
| higher I    | values, | that   | is, the MSSs | were           | exposed | to       | a larger |     |     |     |     |     |            |     |
PL
quantityofC-dots.Notably,for8.0wt%C-dotdispersion,the
| valueofI | reacheditsmaximumafter2minperfusion,after |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PL
| which         | it was     | reduced | and leveled        |              | off. This | effect       | was       |     |     |     |     |     |     |     |
| ------------- | ---------- | ------- | ------------------ | ------------ | --------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| presumably    | caused     | by      | the self-quenching |              | of        | fluorescence | of        |     |     |     |     |     |     |     |
| C-dots47      | when they  | were    | in close           | proximity.53 |           | The          | retention |     |     |     |     |     |     |     |
| graphs        | in Fig.    | 5E show | that after         | the          | perfusion | of           | the cell  |     |     |     |     |     |     |     |
| culture       | medium     | for 60  | min, the           | C-dots       | were      | largely      | washed    |     |     |     |     |     |     |     |
| away, thereby | confirming |         | the suitability    |              | of the    | selected     | time      |     |     |     |     |     |     |     |
 .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP
periodfortheMSSrecovery.
Following 60 min perfusion of C-dot dispersions with Fig. 6 Characterization of metaflumizone-free liposomes. (A) Cryo-
TEMliposomeimage.Thescalebaris200nm.(B)Sizedistributionof
different concentrations and 60 min of recovery, live/dead theliposomes,basedontheimageanalysis.n=50.(C)Excitationand
| assays were | performed |     | for the | cells | in the | MSSs. | Fig. 5F |                  |              |     |          |        |               | I       |
| ----------- | --------- | --- | ------- | ----- | ------ | ----- | ------- | ---------------- | ------------ | --- | -------- | ------ | ------------- | ------- |
|             |           |     |         |       |        |       |         | emission spectra | of liposomes |     | on day 0 | and 7. | (D) Variation | in PL , |
shows that for all examined C-dot dispersions, the cell plottedasafunctionofperfusiontimeofthedispersionwithliposome
viability was above 50%. The value of IC was estimated to concentrations of 8.0 (red), 4.0 (blue), 0.8 (orange), and 0.08 (green)
|     |     |     |     |     | 50  |     |     | wt%.(E)VariationinI |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
be 12.5 wt%, and thus, the dispersions of C-dots fell in the PL asin(D),plottedasafunctionofperfusiontime
|          |                   |     |      |     |      |       |       | of the cell    | culture medium. | The      | line colors | correspond | to      | liposome |
| -------- | ----------------- | --- | ---- | --- | ---- | ----- | ----- | -------------- | --------------- | -------- | ----------- | ---------- | ------- | -------- |
| category | of non-irritants. |     | Such | a   | high | value | of IC |                |                 |          |             |            |         |          |
|          |                   |     |      |     |      |       | 50    | concentrations | as in (D).      | The data | points      | are shown  | as mean | ± SD.    |
underlinedthebiocompatibilityofC-dots,whichalignedwith
Eachdatapointrepresentsmeasurementsfromatotalofatleast180
thereportedresults.48–50
MSSscollectedfromthreeindependentlypreparedarrays.
Evaluationofthetoxicityofliposomesloadedwiththe
|     |     |     |     |     |     |     |     | culture medium,whichwascarriedoutimmediatelyafter60- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
insecticide
|     |     |     |     |     |     |     |     | min perfusion | of liposome |     | dispersion. | The | maximum | value |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | ----------- | --- | ------- | ----- |
50–75%,
TodemonstratetheversatilityoftheMFplatform,wetestedits of I PL was reduced by with a greater retention
ability to assess the toxicity of not only NPs, but also active corresponding to higher liposome concentrations. Compared
ingredients encapsulated in the NPs. As a case study, we totheretentionofC-dots(Fig.5E),itcanbeinferredthatthe
assessed the toxicity ofliposomes loadedwithmetaflumizone, liposomes were trapped in the MSSs and required a longer
a hydrophobic insecticide, non-irritant for the rabbit skin.51 timefortheircompleteremovalfromtheMSSs.
The liposomes were composed of cholesterol and To assess the toxicity of metaflumizone-loaded liposomes,
phosphatidylcholine at a 1:10 mass ratio, as described we encapsulated this insecticide in the liposomes formed by
elsewhere.52 The metaflumizone-free and metaflumizone- cholesterolandphosphatidylcholineattheir1:10massratio.
loadedliposomeswerepreparedusinganMFmethod(seethe Fig. 7A shows the encapsulation efficiency of metaflumizone
details in Fig. S4, ESI†). We first focused on the in the liposomes. The details of the measurements are
providedinFig.S5,ESI.†Theencapsulationefficiencywas60
| metaflumizone-free |     | liposomes. |     | To assess | their | uptake | and |     |     |     |     |     |     |     |
| ------------------ | --- | ---------- | --- | --------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
retentionbytheMSSsusingfluorescencemicroscopy,10mol% ±10%,anditdidnotsignificantlychangewithanincreasing
of the cholesterol in the liposomes was replaced with metaflumizone concentration in the solution. This effect was
cholesterol labeled with fluorescent boron dipyrromethene. expected for the MF preparation of the liposomes occurring
| Fig. 6A | and B show | the | cryogenic | TEM | (cryo-TEM) |     | image of |     |     |     |     |     |     |     |
| ------- | ---------- | --- | --------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
theseliposomesandtheirsizedistributionobtainedfromTEM
| image analysis. |     | The average | liposome |     | size was | 92  | ± 8 nm. |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | -------- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Fig.6CshowsthatthePLexcitationandemissionpeaksofthe
| liposomes | were | centered | at 500 | and 509 | nm, | respectively. | The |     |     |     |     |     |     |     |
| --------- | ---- | -------- | ------ | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
dispersionofliposomesremainedcolloidallystableover7days,
withanegligiblechangeinNPdimensionsandPLspectra.
| The       | dispersion |          | of fluorescent |             | metaflumizone-free |           |         |                  |          |                         |     |     |            |     |
| --------- | ---------- | -------- | -------------- | ----------- | ------------------ | --------- | ------- | ---------------- | -------- | ----------------------- | --- | --- | ---------- | --- |
| liposomes | was        | perfused | for 60         | min through |                    | the MF    | device. |                  |          |                         |     |     |            |     |
|           |            |          |                |             |                    |           |         | Fig. 7 Screening | toxicity | of metaflumizone-loaded |     |     | liposomes. | (A) |
| Fig. 6D   | and E      | show     | the change     | in          | PL                 | intensity | of the  |                  |          |                         |     |     |            |     |
Encapsulationefficiencyofmetaflumizoneintheliposomes,plottedas
| microwellscarryingtheMSSs.ThevalueofI |     |     |     |     |     | plateauedafter |     |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
PL a function of the concentration of metaflumizone in the solution. (B)
2 min perfusion of the liposome dispersions with all Lightscatteringintensityofmetaflumizone-freeliposomes,fluorescent
examined liposome concentrations, indicating complete MSS liposomes, and metaflumizone-loaded liposomes. (C) Concentration–
exposuretotheliposomedispersion(Fig.6D).Theleveled-off response curve for MSSs subjected to metaflumizone-loaded
|          |       |         |         |          |             |     |      | liposomes | following 24-h | dispersion | perfusion | and | 60-min | recovery, |
| -------- | ----- | ------- | ------- | -------- | ----------- | --- | ---- | --------- | -------------- | ---------- | --------- | --- | ------ | --------- |
| value of | I was | greater | for the | liposome | dispersions |     | with |           |                |            |           |     |        |           |
PL plottedvs.theconcentrationofmetaflumizone in thedispersion.The
| higher | concentrations, |     | which | corresponded |     | to the | greater |             |              |      |       |           |       |            |
| ------ | --------------- | --- | ----- | ------------ | --- | ------ | ------- | ----------- | ------------ | ---- | ----- | --------- | ----- | ---------- |
|        |                 |     |       |              |     |        |         | data points | are shown as | mean | ± SD. | Each data | point | represents |
quantity of liposomes to be uptaken by the MSSs. Fig. 6E measurementsfromatotalofatleast180MSSs,collectedfromthree
shows the variation in I during a 60 min supply of the independentlypreparedarrays.
PL
| LabChip |     |     |     |     |     |     |     |     | Thisjournalis©TheRoyalSocietyofChemistry2025 |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |

View Article Online
| LabonaChip |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Paper |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
concurrently with metaflumizone encapsulation. Fig. 7B timecompromisesfullmodelmaturation,partiallymaturated
shows the variation in the light scattering intensity of the MSSs effectively distinguished non-irritant chemicals from
irritantchemicalslistedintheOECDtestguideline.24
| dispersion | of non-fluorescent |     |     | metaflumizone-free |     | liposomes, |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------ | --- | --- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fluorescent liposomes described above, and metaflumizone- To expand the application of the MF platform beyond
loaded liposomes. All liposomes had similar average toxicity screening of small organic molecules, we expanded
hydrodynamic diameters of approximately 140 nm and a its utility for NPs such as C-dots and liposomes. Notably, for
narrow size distribution. Therefore, the results obtained for the liposomes, we assessed the toxicity of not only the
the uptake and retention of fluorescent metaflumizone-free liposome carrier, but also the encapsulated metaflumizone
liposomes (Fig. 6D and E) by the MSSs could be used for the insecticide. The MSS-based MF platform offers a robust,
metaflumizone-loadedliposomes. scalable, and time-efficient tool for screening a diverse range
 .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP
The liposomes with a metaflumizone/lipid mass ratio (R) ofchemicalagentsfortheirsafetyevaluation.
of 0.035 were selected for screening the toxicity of Next-step studies would include tests of a broader range of
metaflumizone-loaded liposomes. Following 60 min chemical agents, including both hydrophilic and hydrophobic
perfusion of the dispersion of metaflumizone-loaded components, to extend and refine the applications of the
liposomes through the MF device, the viability of cells in the developed MSS-based skin toxicity prediction model. With
MSSs was close to 100% for all tested concentrations of appropriate modification of the platform, it would be possible
metaflumizone-loaded liposomes in dispersions (Fig. S6, to use the MSSs for screening toxicity of solid compounds.
ESI†).
Based on these results, we conclude that 60-min Ultimately,theMSSplatformwouldbeapplicabletotestvarious
screening time was insufficient for the release of the types of skin-related products, including solutions, solid
insecticide from the liposomes. Therefore, the dispersion of powdersandcreams.
| metaflumizone-loaded |     |     | liposomes | was | perfused | through | the |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MF device for 24 h, which was followed by 60-min perfusion Materials and methods
| of the cell | culture | medium | for | MSS | recovery. | The details | of  |     |     |     |     |     |     |     |     |
| ----------- | ------- | ------ | --- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Materials
| the uptake | of  | liposomes | by the | MSSs | during | 24 h perfusion |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --------- | ------ | ---- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TopFluor®
oftheliposomedispersionareprovidedinFig.S7,ESI.†After Type A gelatin, PEG, AT, IPA, MPP, CMDH and
|             |     |       |           |     |         |            |     | cholesterol | were | obtained | from |     | Sigma-Aldrich, |     | Canada. |
| ----------- | --- | ----- | --------- | --- | ------- | ---------- | --- | ----------- | ---- | -------- | ---- | --- | -------------- | --- | ------- |
| 24-h supply | of  | 0.08, | 0.8, 4.0, | and | 8.0 wt% | dispersion | of  |             |      |          |      |     |                |     |         |
metaflumizone-loaded liposomes, corresponding to 2.8 × Poly(dimethylsiloxane) (PDMS) (Sylgard 184) was purchased
−3, × −2, × −1, × −1 from Ellsworth adhesives, and fluorinated oil HFE-7500 and
| 10 2.8        | 10  | 1.4    | 10         | and  | 2.8     | 10              | wt% of |                      |     |      |                               |     |     |     |     |
| ------------- | --- | ------ | ---------- | ---- | ------- | --------------- | ------ | -------------------- | --- | ---- | ----------------------------- | --- | --- | --- | --- |
|               |     |        |            |      |         |                 |        | 008-fluorosurfactant |     | were | purchasedfrom3MCorporationand |     |     |     |     |
| metaflumizone |     | in the | dispersion | (see | details | of calculations |        |                      |     |      |                               |     |     |     |     |
ESI†), RAN Biotechnologies, respectively. Dulbecco's Modified Eagle
| in the       |       | the cell | viability   | was | 96, 92,        | 79, and | 54%, |        |         |       |        |       |     |                    |     |
| ------------ | ----- | -------- | ----------- | --- | -------------- | ------- | ---- | ------ | ------- | ----- | ------ | ----- | --- | ------------------ | --- |
|              |       |          |             |     |                |         |      | Medium | (DMEM), | fetal | bovine | serum |     | (FBS), penicillin- |     |
| respectively | (Fig. | 7C).     | The reduced |     | cell viability | after   | 24-h |        |         |       |        |       |     |                    |     |
trypsin–EDTA
perfusion of the metaflumizone-loaded liposome dispersion streptomycin (pen-strep), solution, and 1X HBSS
|                  |      |                     |           |           |        |                |         | were purchased |                     | from | Life Technologies |               |       | (Thermo     | Fisher |
| ---------------- | ---- | ------------------- | --------- | --------- | ------ | -------------- | ------- | -------------- | ------------------- | ---- | ----------------- | ------------- | ----- | ----------- | ------ |
| indicated        | that | the internalization |           |           | of the | metaflumizone- |         |                |                     |      |                   |               |       |             |        |
|                  |      |                     |           |           |        |                |         | Scientific).   | Phosphatidylcholine |      |                   | (phospholipon |       | 90G)        | was    |
| loaded liposomes |      | into                | the cells | of the    | MSSs   | and the        | release |                |                     |      |                   |               |       |             |        |
|                  |      |                     |           |           |        |                |         | provided       | by LIPOID,          | LLC  | (Newark,          | NJ,           | USA). | Cholesterol | was    |
| of metaflumizone |      | from                | the       | liposomes |        | dominated      | the     |                |                     |      |                   |               |       |             |        |
suppliedbyBioShopCanadaInc.(Burlington,ON,Canada)and
| screening | of the | toxicity | of metaflumizone. |     |     | As a control, | we  |     |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ----------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
metaflumizone(Siesta®)wassuppliedbyBASFCorporation.An
| also perfused |     | 8 wt% | dispersion |     | of metaflumizone-free |     |     |         |            |     |           |              |     |           |     |
| ------------- | --- | ----- | ---------- | --- | --------------------- | --- | --- | ------- | ---------- | --- | --------- | ------------ | --- | --------- | --- |
|               |     |       |            |     |                       |     |     | aqueous | suspension | of  | cellulose | nanocrystals |     | at 10 wt% | was |
liposomesfor24h,followedby60-minMSSrecoverywiththe
|              |           |      |       |              |          |          |           | purchased     | from | the University |      | of Maine | Process | Development |         |
| ------------ | --------- | ---- | ----- | ------------ | -------- | -------- | --------- | ------------- | ---- | -------------- | ---- | -------- | ------- | ----------- | ------- |
| cell culture | medium.   | In   | these | experiments, |          | the cell | viability |               |      |                |      |          |         |             |         |
|              |           |      |       |              |          |          |           | Center (USA). | All  | chemicals      | were | utilized | as      | received    | without |
| was 85%,     | revealing | that | the   | liposome     | carriers |          | did not   |               |      |                |      |          |         |             |         |
furtherpurification.
significantlyaffectcellviability(Fig.S8,ESI†).
Cellculture
Conclusion
|     |     |     |     |     |     |     |     | Primary | human | dermal | fibroblasts | (hDFs) | (PCS-201-010) |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------ | ----------- | ------ | ------------- | --- | --- |
ATCC®
We developed an MSS-based MF platform and showed its HaCaT (no. 300493) were purchased from and Cell
utilityasanin vitroskinmodel tailoredfor toxicityscreening Lines Service GmbH, respectively. Both cell types were
of various low-molecular weight chemical agents and NPs. cultured in T-175 tissue culture flasks containing 18 mL of
The MSSs grown in the MF platform mimicked the structure DMEM culture medium, which was supplemented with 10%
of human skin, with a fibroblast core and a keratinocyte (v/v) FBS and 1% (v/v) pen-strep. The hDFs were detached
shell, representing the dermis and epidermis layers, from T-175 tissue culture flasks using 10 min incubation at
respectively. By analyzing the IC values, we established a 37 °C in 5 mL of trypsin–EDTA solution, while HaCaT cells
50
MSS-based skin toxicity model which, for the substances were detached through 15 min incubation in 6 mL of
trypsin–EDTA.
testedinthisproof-of-conceptstudy,effectivelydistinguished The cell suspension was centrifuged at 180 g
non-irritant chemical agents from the irritant ones, with for 3 min. The resulting cell pellet was then resuspended in
|     |     |     |     |     |     |     |     | μL  |     |     |     | μL  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
screening results aligning with the established OECD test 1000 of the medium, and 200 of the cell suspension
guidelines for skin irritation. Although shortened culture was transferred into a new flask. In this work, hDFs at
| Thisjournalis©TheRoyalSocietyofChemistry2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | LabChip |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |

View Article Online
|     | Paper |     |     |     |     |     |     |     |     |     |     |     |     | LabonaChip |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
passage 7–16 and HaCaT at passage 30–50 were used for antibody, Cat # PIPA532350, Invitrogen™). The device was
spheroidformation. thenincubatedwithprimaryantibodiesat4°Covernight.On
|     |     |     |     |     |     |     |     |     | the next           | day, | the     | MSSs | were washed  |                    | again | with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ---- | ------- | ---- | ------------ | ------------------ | ----- | ---- |
|     |     |     |     |     |     |     |     |     | immunofluorescence |      | washing |      | solution for | 1 h. Subsequently, |       |      |
Fabricationofthemicrofluidicdevice
|     |              |         |      |            |       |      |              |     | Hoechst | 33342 and | secondary |     | antibodies | (goat | anti-rabbit |     |
| --- | ------------ | ------- | ---- | ---------- | ----- | ---- | ------------ | --- | ------- | --------- | --------- | --- | ---------- | ----- | ----------- | --- |
|     | Microfluidic | devices | were | fabricated | using | soft | lithography, |     |         |           |           |     |            |       |             |     |
IgGAlexaFluor546andgoatanti-mouseIgGAlexaFluor488)
|     | as described | elsewhere.38  |        | In brief,    | the         | PDMS elastomer |         | and    |            |                 |           |           |               |     |           |     |
| --- | ------------ | ------------- | ------ | ------------ | ----------- | -------------- | ------- | ------ | ---------- | --------------- | --------- | --------- | ------------- | --- | --------- | --- |
|     |              |               |        |              |             |                |         |        | in primary | blocking        | solution  |           | were perfused | for | 60 min    | for |
|     | curing       | agent were    | mixed  | in a         | 10:1 weight | ratio          | and     | poured |            |                 |           |           |               |     |           |     |
|     |              |               |        |              |             |                |         |        | claudin-1  | and fibronectin |           | staining, | respectively. |     | Confocal  |     |
|     | onto a       | silicon wafer | master | manufactured |             | by             | FlowJEM | Ltd.   |            |                 |           |           |               |     |           |     |
|     |              |               |        |              |             |                |         |        | microscopy | was             | performed | using     | a Leica       | SP8 | STELLARIS |     |
|     | The PDMS     | was cured     | at     | 75 °C        | for 2 h,    | followed       | by a    | plasma |            |                 |           |           |               |     |           |     |
confocalmicroscope(LeicaMicrosystems,Wetzlar,Germany).
|  .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP | treatment | to bond | with | a glass | slide. | The bonded |     | devices |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------------------------------------- | --------- | ------- | ---- | ------- | ------ | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
wereplacedinanovenat115°Covernight.
Skintoxicityevaluation
FormationofMSSs
|     |     |     |     |     |     |     |     |     | On day | 2, the | MSSs | were | subjected | to the | solution | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ---- | ---- | --------- | ------ | -------- | --- |
On day 0, the device was filled with hDFs in the EKGel-1 chemical agents or dispersion of NPs in HBSS using pipette
precursor (composed of 0.5 wt% a-CNCs and 1.5 wt% tips(epT.I.P.S.®–20–300μL)asreservoirsconnectedtoinlets
gelatin) suspension at a concentration of 4.9 × 105 cells per and outlets of the MF device. The device was placed on a
|     | μL. |     |     |     |     |     |     |     |     |     |     |     | °C  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Following the formation of hDF-laden droplets, the rocker inside an incubator (37 and 5% CO ) and set to a
2
excess cell suspension in the channels was replaced with tilting angle of 25° and a tilting period of 6 h, operating in
fluorinated oil containing 0.5 wt% 008-fluorosurfactant. The the interval mode with step changes at a transition speed of
device was incubated for 2 h at 37 °C to facilitate EKGel-1 9° per s. The average flow rate was estimated to be 0.06 mL
gelation. Subsequently, the cell culture medium was h −1. After aspirating the solution of the chemical agents or
perfused through the supplying channel at a flow rate of 0.1 NPdispersion,thecellculturemediumwasintroducedtothe
mL h −1 for 24 h. On day 1, the hDFs aggregated to form reservoirsoftheMFdevicefor60minatanaverageflowrate
|     |     |     |     |     |     | ×   | 105 |     |     | −1. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DFSs in the microwells and HaCaT cells (8 cells per of 0.06 mL h Cell viability of the cells in the MSSs was
μL) in the EKGel-2 precursor suspension (comprising 1.5 assessed using live/dead assay. A solution containing 2 μM
wt% a-CNCs and 3.0 wt% gelatin) were perfused through calcein-AM (green, live cells) and 6 μM propidium iodide
the supplying channel to engulf the DFSs in the microwells. (red, dead cells) was perfused for 60 min at an average flow
After engulfing the DFS core with the suspension of HaCaT rate of 0.06 mL h −1. The stained MSSs were imaged using
cells and EKGel-2 precursors, the excess suspension was fluorescence microscopy (Nikon Ti Eclipse) with excitation
replaced with fluorinated oil containing 1 wt% 008- wavelengths of 488 nm (FITC) and 570 nm (TRITC) and
fluorosurfactant, and the device was incubated at 37 °C for emission wavelengths of 515 nm and 602 nm for live and
2 h. The cell culture medium was continuously perfused at dead cells, respectively. Fluorescence intensities were
a flow rate of 0.1 mL h −1 for 24 h. On day 2, MSSs were measured using ImageJ. The absolute cell viability was
|     | formed | in the microwells. |     |            |     |                           |     |                           | calculatedas:             |     |     |     |       |     |     |     |
| --- | ------ | ------------------ | --- | ---------- | --- | ------------------------- | --- | ------------------------- | ------------------------- | --- | --- | --- | ----- | --- | --- | --- |
|     |        |                    |     | Viability¼ |     |                           |     | IntensityoftheFITCchannel |                           |     |     |     | ×100% |     |     |     |
|     |        |                    |     |            |     | IntensityoftheFITCchannel |     |                           | þ IntensityofTRITCchannel |     |     |     |       |     |     |     |
ImmunofluorescencestainingofMSSs Cell viability was normalized to the viability of the cells in
Toperformimmunofluorescencestaining,first,1XHBSSwas the MSSs exposed to HBSS (negative control) as 100% and to
0.5wt%TritonX-100(positivecontrol)as0%.
|     | introduced   | for 20       | min     | to remove | the      | cell culture | medium, |     |          |              |      |         |           |          |     |        |
| --- | ------------ | ------------ | ------- | --------- | -------- | ------------ | ------- | --- | -------- | ------------ | ---- | ------- | --------- | -------- | --- | ------ |
|     | followed     | by perfusion | of      | a 5%      | formalin | solution     | in HBSS | for |          |              |      |         |           |          |     |        |
|     |              |              |         |           |          |              |         |     | Data     | availability |      |         |           |          |     |        |
|     | 30 min       | to fix the   | MSSs.   | The       | solution | was washed   | away    | by  |          |              |      |         |           |          |     |        |
|     | perfusing    | 0.1 M        | glycine | in 1X     | HBSS     | for 30 min.  | Next,   | to  |          |              |      |         |           |          |     |        |
|     |              |              |         |           |          |              |         |     | The data | supporting   | this | article | have been | included |     | in the |
|     | permeabilize | the          | MSSs,   | 0.5%      | Triton-X | in 1X        | HBSS    | was |          |              |      |         |           |          |     |        |
maintextandaspartoftheESI.†
|     | perfused | for 40 min, | and | an  | immunofluorescence |     | washing |     |     |     |     |     |     |     |     |     |
| --- | -------- | ----------- | --- | --- | ------------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
solution containing 0.05% NaN , 0.1% bovine serum Author contributions
3
|     | albumin, | 0.2% Triton-X-100, |     | and | 0.05% | Tween-20 | in  | HBSS |     |     |     |     |     |     |     |     |
| --- | -------- | ------------------ | --- | --- | ----- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
was supplied for 60 min to wash the MSSs. A primary Z. C. and E. K. conceptualized and designed the study. D. K.
blocking solution (10% goat serum in immunofluorescence and F. R. conducted the experiments and performed data
washing solution) was supplied for 90 min, followed by 60 analysis, with equal contribution. D. K. and F. R. drafted the
min perfusion of primary antibody solution (mouse anti- manuscriptwithcriticalrevisionsprovidedbyZ.C.andE.K.,
human fibronectin monoclonal antibody, Cat # MA5-11981, Y. M. contributed to the materials preparation and data
Invitrogen™; Rabbit anti-human claudin 1 polyclonal analysis. I. Y., S. K., S. N. K., T. D., L. Q., and O. Z.
|     | LabChip |     |     |     |     |     |     |     |     | Thisjournalis©TheRoyalSocietyofChemistry2025 |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |

View Article Online
| LabonaChip |     |     |     |     |     |     |     |     |     | Paper |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
contributed to the discussions and interpretation of the 18 D.Grimm,Science,2019,365,1231–1231.
results. 19 K. Schimek, H.-H. Hsu, M. Boehme, J. J. Kornet, U. Marx, R.
Lauster,R.PörtnerandG.Lindner,Bioengineering,2018,5,43.
| Conflicts | of  | interest |     |     |     |              |                 |             |                  |       |
| --------- | --- | -------- | --- | --- | --- | ------------ | --------------- | ----------- | ---------------- | ----- |
|           |     |          |     |     |     | 20 S. Costa, | V. Vilas-Boas,  | F. Lebre,   | J. M. Granjeiro, | C. M. |
|           |     |          |     |     |     | Catarino,    | L. M. Teixeira, | P. Loskill, | E. Alfaro-Moreno | and   |
Z.C.,T.D.andE.K.areco-inventorsonapatentapplication
A.R.Ribeiro,TrendsBiotechnol.,2023,41,1282–1298.
for the development of the method for the formation of 21 T. Moniz, S. A. Costa Lima and S. Reis, Br. J. Pharmacol.,
| MSSs. |     |     |     |     |     | 2020,177,4314–4329. |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
22 TestNo.442E:InVitroSkinSensitisation,OECD,2024.
Acknowledgements
|     |     |     |     |     |     | 23 Test | No. 431: In | vitro skin corrosion: | reconstructed | human |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | --------------------- | ------------- | ----- |
 .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP
epidermis(RHE)testmethod,OECD,2019.
| E. K.acknowledgessupport |             |          | fortheresearch | describedin | this     |         |                   |                  |               |       |
| ------------------------ | ----------- | -------- | -------------- | ----------- | -------- | ------- | ----------------- | ---------------- | ------------- | ----- |
|                          |             |          |                |             |          | 24 Test | No. 439: In Vitro | Skin Irritation: | Reconstructed | Human |
| study from               | the Natural | Sciences | and            | Engineering | Research |         |                   |                  |               |       |
EpidermisTestMethod,OECD,2021.
| Council | of Canada | (NSERC) | Alliance | Grants | and BASF |     |     |     |     |     |
| ------- | --------- | ------- | -------- | ------ | -------- | --- | --- | --- | --- | --- |
25 X.Zhao,Q.Lang,L.Yildirimer,Z.Y.Lin,W.Cui,N.Annabi,
| Corporation. | The authors | thank | the Centre | for | Research and |     |     |     |     |     |
| ------------ | ----------- | ----- | ---------- | --- | ------------ | --- | --- | --- | --- | --- |
Applications in Fluidic Technologies at the University of K. W. Ng, M. R. Dokmeci, A. M. Ghaemmaghami and A.
Khademhosseini,Adv.HealthcareMater.,2016,5,108–118.
Torontofortheirassistanceinconfocalmicroscopy.
|     |     |     |     |     |     | 26 Y. Poumay, | F. Dupont, | S. Marcoux, | M. Leclercq-Smekens, | M.  |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | ----------- | -------------------- | --- |
References Hérin and A. Coquette, Arch. Dermatol. Res., 2004, 296,
203–211.
1 S. E. Anderson and B. J. Meade, Environ. Health Insights, 27 Q.Li,C.Wang,X.Li,J.Zhang,Z.Zhang,K.Yang,J.Ouyang,S.
2014,8,EHI-S15258. Zha,L.ShaandJ.Ge,J.TissueEng.,2023,14,20417314231168530.
2 R.Fitoussi,M.-O.Faure,G.BeauchefandS.Achard,Environ. 28 Q.Quan,D. Weng,X.Li, Q.An,Y. Yang,B.Yu,Y.MaandJ.
Pollut.,2022,306,119316. Wang,Front.Bioeng.Biotechnol.,2022,10,939629.
3 M. Wufuer, G. Lee, W. Hur, B. Jeon, B. J. Kim, T. H. Choi 29 J.Zhang,Z.Chen,Y.Zhang,X.Wang,J.Ouyang,J.Zhu,Y.Yan,
X.Sun,F.WangandX.Li,LabChip,2021,21,3804–3818.
andS.Lee,Sci.Rep.,2016,6,37471.
4 M.Bilal,S.MehmoodandH.M.N.Iqbal,Cosmetics,2020,7, 30 L. H. Chong, T. Ching, H. J. Farm, G. Grenci, K. H. Chiam
| 13. |     |     |     |     |     | andY.C.Toh,LabChip,2022,22,1890–1904. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
5 M. Crosera, M. Bovenzi, G. Maina, G. Adami, C. Zanette, C. 31 G. Sriram, M. Alberti, Y. Dancik, B. Wu, R. Wu, Z. Feng, S.
Florio and F. Filon Larese, Int. Arch. Occup. Environ. Health, Ramasamy, P. L. Bigliardi, M. Bigliardi-Qi and Z. Wang,
| 2009,82,1043–1055. |     |     |     |     |     | Mater.Today,2018,21,326–340. |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
6 P. Puri, S. K. Nandar, S. Kathuria and V. Ramesh, Indian J. 32 S. Eom, W. Shim and I. Choi, J. Hazard. Mater., 2024, 465,
| Dermatol.Venereol.Leprol.,2017,83,415. |     |     |     |     |     | 133359. |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
7 T. Zaiter, R. Cornu, W. El Basset, H. Martin, M. Diab and A. 33 T. Srisongkram, N. F. Syahid, T. Piyasawetkul, P.
Béduneau,J.Nanopart.Res.,2022,24,149. Thirawatthanasak, P. Khamtang, N. Sawasnopparat, D.
8 A. Truskewycz, H. Yin, N. Halberg, D. T. H. Lai, A. S. Ball, Tookkane, N. Weerapreeyakul and P. Puthongking, Chem.
V. K. Truong, A. M. Rybicka and I. Cole, Small, 2022, 18, Res.Toxicol.,2023,36,1980–1989.
2106342. 34 Y. Tan, A. Suarez, M. Garza, A. A. Khan, J. Elisseeff and D.
Coon,Biomater.Sci.,2020,8,1951–1960.
| 9 M. J. | G. Fernandes, | R. B. | Pereira, A. | R. O. Rodrigues, | T. F. |     |     |     |     |     |
| ------- | ------------- | ----- | ----------- | ---------------- | ----- | --- | --- | --- | --- | --- |
Vieira, A. G. Fortes, D. M. Pereira, S. F. Sousa, M. S. T. 35 P. Ebner-Peking, L. Krisch,M. Wolf, S.Hochmann, A. Hoog,
GonçalvesandE.M.S.Castanheira,Nanomaterials,2022,12, B. Vári, K. Muigg, R. Poupardin, C. Scharler and S.
| 3583. |     |     |     |     |     | Schmidhuber,Theranostics,2021,11,8430. |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
10 X.Chen,L.Qiu,Q.LiuandY.He,Insects,2022,13,625. 36 Z.Chen,D.Kalhori,F.Rakhshani,O.ElBaraka,L.Qu,S.N.
11 S.Hashempour,S.Ghanbarzadeh,H.I.Maibach,M.Ghorbani Kolle, V. Andre, T. Deisenroth and E. Kumacheva, Sci. Adv.,
| andH.Hamishehkar,Ther.Delivery,2019,10,383–396. |     |     |     |     |     | 2025,11,1251. |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
12 T. K. Shaw, P. Paul and B. Chatterjee, Futur. J. Pharm. Sci., 37 T. Tang, P. Zhang, Q. Zhang, X. Man and Y. Xu,
| 2022,8,46. |     |     |     |     |     | Biofabrication,2024,16,045013. |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
13 L. Xu, X. Wang, Y. Liu, G. Yang, R. J. Falconer and C.-X. 38 Z. Chen, S. Kheiri, A. Gevorkian, E. W. K. Young, V. Andre, T.
DeisenrothandE.Kumacheva,LabChip,2021,21,3952–3962.
Zhao,Adv.NanoBiomedRes.,2022,2,2100109.
14 D. K. Patel, R. Kesharwani and V. Kumar, Int. J. Pharm. 39 S.Kheiri,Z.Chen,I.Yakavets,F.Rakhshani,E.W.K.Young
Invest.,2019,9,4. andE.Kumacheva,Biotechnol.J.,2023,18,2200621.
15 S. Doktorovova, A. B. Kovačević, M. L. Garcia and E. B. 40 E. Prince, Z. Chen, N. Khuu and E. Kumacheva,
Souto,Eur.J.Pharm.Biopharm.,2016,108,235–252. Biomacromolecules,2021,22,2352–2362.
16 Y. Li, L. Lofchy, G. Wang, H. Gaikwad, M. Fujita and D. 41 M. D. Seo, T. J. Kang, C. H. Lee, A. Y. Lee and M. Noh,
| Simberg,ACSNano,2022,16,6349–6358. |     |     |     |     |     | Biomol.Ther.,2012,20,171. |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- |
17 M. Lee, J.-H. Hwang and K.-M. Lim, Toxicol. Res., 2017, 33, 42 I.Colombo, E.Sangiovanni, R. Maggio, C. Mattozzi, S.Zava,
191–203. Y. Corbett, M. Fumagalli, C. Carlino, P. A. Corsetto, D.
| Thisjournalis©TheRoyalSocietyofChemistry2025 |     |     |     |     |     |     |     |     |     | LabChip |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |

View Article Online
| Paper |     |     |     |     |     |     | LabonaChip |
| ----- | --- | --- | --- | --- | --- | --- | ---------- |
Scaccabarozzi and S. Calvieri, Mediators Inflammation, 49 H. Kuznietsova, A. Géloën, N. Dziubenko, A. Zaderko, S.
2017,2017,7435621. Alekseev, V. Lysenko and V. Skryshevsky, Discover Nano,
43 J. Han, G.-Y. Lee, G. Bae, M.-J. Kang and K.-M. Lim, Toxics, 2023,18,111.
2021,9,314. 50 M.-H. Chan, B.-G. Chen, L. T. Ngo, W.-T. Huang, C.-H.
44 L. T. N. Ngoc, J.-Y. Moon and Y.-C. Lee, Nanomaterials, Li, R.-S. Liu and M. Hsiao, Pharmaceutics, 2021, 13,
| 2023,13,2654. |     |     |     | 1874. |     |     |     |
| ------------- | --- | --- | --- | ----- | --- | --- | --- |
45 G. Hu, B.Lei, X.Jiao, S.Wu, X. Zhang, J. Zhuang, X. Liu, C. 51 K. Hempel, F. G. Hess, C. Bögi, E. Fabian, J.
HuandY.Liu,Opt.Express,2019,27,7629–7641.
|                |     |                |                    | Hellwig and | I. Fegert, | Vet. Parasitol., | 2007, 150, |
| -------------- | --- | -------------- | ------------------ | ----------- | ---------- | ---------------- | ---------- |
| 46 H. Ehtesabi | and | R. Nasri, Adv. | Nat. Sci.:Nanosci. | 190–195.    |            |                  |            |
Nanotechnol.,2021,12,025006. 52 I. Yakavets, M. Ayachit, S. Kheiri, Z. Chen, F. Rakhshani, S.
 .MP 50:52:2 5202/03/7 no otnoroT fo ytisrevinU yb dedaolnwoD .5202 enuJ 62 no dehsilbuP
47 A. Sharma, T. Gadly, S. Neogy, S. K. Ghosh and M. McWhirter, E. W. K. Young, G. C. Walker and E.
Kumbhakar,J.Phys.Chem.Lett.,2017,8,1044–1052. Kumacheva, ACS Appl. Mater. Interfaces, 2024, 16,
9690–9701.
| 48 S. Demirci, | A. B. McNally, | R. S. Ayyala, | L. B. Lawson | and N. |     |     |     |
| -------------- | -------------- | ------------- | ------------ | ------ | --- | --- | --- |
Sahiner,J.DrugDeliverySci.Technol.,2020,59,101889. 53 Y.Ma,Adv.Mater.,2024,DOI:10.1002/adfm.202413525.
| LabChip |     |     |     | Thisjournalis©TheRoyalSocietyofChemistry2025 |     |     |     |
| ------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
