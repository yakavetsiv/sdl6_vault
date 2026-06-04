---
type: literature-note
status: converted
source_type: pdf
source_file: "stein2019_automated_autonomous_workflows.pdf"
source_path: "/Users/iyakavets/Documents/Github/LH_BO_Preprint/literature/pdfs/self_driving_labs/stein2019_automated_autonomous_workflows.pdf"
pdf: "_attachments/Self-Driving Labs/stein2019_automated_autonomous_workflows.pdf"
title: "Progress and prospects for accelerating materials science with automated and autonomous workflows"
year: "2019"
doi: "10.1039/c9sc03766g"
citation_count_openalex: 237
topics:
  - Self-Driving Labs
  - Lab Automation
  - Autonomous Experimentation
tags:
  - literature/self-driving-labs
  - source/pdf
  - converted/markitdown
---

# Progress and prospects for accelerating materials science with automated and autonomous workflows

**Key:** `stein2019_automated_autonomous_workflows`  
**Year:** 2019  
**DOI:** 10.1039/c9sc03766g  
**OpenAlex citations:** 237  
**PDF:** [[_attachments/Self-Driving Labs/stein2019_automated_autonomous_workflows.pdf]]

## Why It Matters

This paper is part of the high-citation self-driving laboratory set imported from the LH_BO preprint literature review. Use it to support background claims about closed-loop experimentation, autonomous laboratory infrastructure, AI-guided experiment planning, or automated materials/chemical discovery.

## Connections

- [[Concept - Self-Driving Labs]]
- [[Concept - Lab Automation]]
- [[Concept - Optimization and Bayesian Search]]
- [[Map - Self-Driving Lab Stack]]

## Converted Text

Chemical
Science
| MINIREVIEW |     |     |     |     |     |     |     |     | View Article Online |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
View Journal | View Issue
|     |     |     | Progress | and prospects |     | for | accelerating |     | materials |     |
| --- | --- | --- | -------- | ------------- | --- | --- | ------------ | --- | --------- | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  science with automated and autonomous
 .MA 71:31:2 6202/1/6 no dedaolnwoD .9102 rebmetpeS 02 no dehsilbuP .elcitrA sseccA nepO
| Citethis:Chem.Sci.,2019,10,9640 |     |     | fl       |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|                                 |     |     | work ows |     |     |     |     |     |     |     |
Allpublicationchargesforthisarticle
havebeenpaidforbytheRoyalSociety
|             |     |     |                | a        |             |     | *ab |     |     |     |
| ----------- | --- | --- | -------------- | -------- | ----------- | --- | --- | --- | --- | --- |
| ofChemistry |     |     | Helge S. Stein | and John | M. Gregoire |     |     |     |     |     |
Accelerating materials research by integrating automation with artificial intelligence is increasingly
scientific
recognized as a grand challenge to discover and develop materials for emerging and future
technologies.Whilethesolidstatematerialssciencecommunityhasdemonstratedabroadrangeofhigh
throughput methods and effectively leveraged computational techniques to accelerate individual
research tasks, revolutionary acceleration of materials discovery has yet to be fully realized. This
perspective review presents a framework and ontology to outline a materials experiment lifecycle and
workflows,
visualize materials discovery providing a context for mapping the realized levels of
automation and the next generation of autonomous loops in terms of scientific and automation
complexity. Expanding autonomous loops to encompass larger portions of complex workflows will
require integration of a range of experimental techniques as well as automation of expert decisions,
Received26thJuly2019
includingsubtlereasoningaboutdataquality,responsestounexpecteddata,andmodeldesign.Recent
Accepted19thSeptember2019
demonstrations of workflows that integrate multiple techniques and include autonomous loops,
DOI:10.1039/c9sc03766g
combined with emerging advancements in artificial intelligence and high throughput experimentation,
rsc.li/chemical-science signaltheimminenceofarevolutioninmaterialsdiscovery.
Introduction both processes,12 for example in the identication of a hyster-
|     |     |     |     |     | esis-free | shape | memory alloy.13 | Continued | automation | of  |
| --- | --- | --- | --- | --- | --------- | ----- | --------------- | --------- | ---------- | --- |
Grand missions, such as combating climate change through materials experiments is motivated by potential benets
|               |     |           |                      |             | including | lowering | per-experiment |     | costs and eliminating |     |
| ------------- | --- | --------- | -------------------- | ----------- | --------- | -------- | -------------- | --- | --------------------- | --- |
| proliferation | of  | renewable | energy technologies, | necessitate |           |          |                |     |                       |     |
technological advancements for which discovery of functional humanerror,andtoenableactivelearning-drivenexperiments
materialsisoenaprerequisite.1,2Historically,transformative that identifyandexplore themost promisingregionsofmate-
materials discoveries have been the result of serendipity from rials parameter space.12,14 In solid state materials science,
experimenting in a related area and/or decades of systematic advancements in automation have largely been driven by the
|     |     |     |     |     | combinatorial | materials | science | community, | where | compre- |
| --- | --- | --- | --- | --- | ------------- | --------- | ------- | ---------- | ----- | ------- |
materialsdevelopment.1Earlyexamplesofautomatedsynthesis
and screening techniques were implemented3–11 to accelerate hensiveexplorationofahighdimensionalmaterialsparameter
spacerequiresasubstantialnumberofsynthesisandscreening
efforts
Articial experiments. While these have provided automation of
| aJoint Center | for | Photosynthesis, | California Institute | of Technology, |            |          |           |        |                      |     |
| ------------- | --- | --------------- | -------------------- | -------------- | ---------- | -------- | --------- | ------ | -------------------- | --- |
|               |     |                 |                      |                | individual | research | tasks for | a wide | variety of materials | and |
Pasadena,CA91125,USA.E-mail:gregoire@caltech.edu
|              |             |             |                               |                | functional | properties, | manual | execution | of several experiment |     |
| ------------ | ----------- | ----------- | ----------------------------- | -------------- | ---------- | ----------- | ------ | --------- | --------------------- | --- |
| bDivision of | Engineering | and Applied | Science, California Institute | of Technology, |            |             |        |           |                       |     |
Pasadena,CA91125,USA
Dr Stein conducts research at the Intersection of Laboratory Dr John Gregoire leads the High Throughput Experimentation
Automation, Data Science, and Materials Science to unravel group at Caltech where he is also the Thrust Coordinator for
composition–structure–processing–function relationships in Photoelectrocatalysis in the Joint Center for Articial Photosyn-
energy related materials. As an alumni in physics from Georg- thesis, a U.S. DOE Energy Innovation Hub. His research team
AugustUniversitaetGoettingenhegraduatedasadoctorofengi- explores, discovers and understands energy-related materials via
neering at Ruhr-Universitaet Bochum with summa cum laude in combinatorial and high throughput experimental methods and
2017.HeworkswithDrGregoireattheJointCenterforArticial theirintegrationwithmaterialstheoryandarticialintelligence.
PhotosynthesisatCaltechtodiscovernewandimprovedmaterials The group seeks to accelerate scientic discovery by automating
workows,
forrenewableenergystorageandproduction. critical components of materials discovery from
synthesisandscreeningtodatainterpretation.
9640 | Chem.Sci.,2019,10,9640–9649 Thisjournalis©TheRoyalSocietyofChemistry2019

Minireview ChemicalScience
steps,aswellasmanualdesignofexperimentsanddatainter- analyzed23 data from individual combinatorial materials
pretation, result in partially-automated workows. The science laboratories complement the suite of computational
emergingvisionofautonomousmaterialsdiscovery12,15requires materialsdatabases60,61aswellasarapidlygrowingnumberof
ahigherlevelofautomation.Establishmentofanautonomous materialsdatarepositoriesincludingtheCitrinationplatform,24
workow is referred to as “closing the loop” since complete the Materials Data Facility (MDF),25 and text mining of the
task-to-task integration is required to allow computer- literature.26 For the purposes of the present analysis of auto-
controlled iteration. Initial14,16 and ongoing progress towards mating12,16,27materialsscienceworkows,thesedatabasesserve
realizingsuchclosed-loopsystemscanbetrackedbythelevelof as successful examples of experiment automation and as
processautomationandintegrationinaworkow. resources that can beused toaccelerate experiment planning,
Sanchez-Lengeling and Aspuru-Guzik17 recently described for example by training machine learning models to identify
theadventofclosed-loopexperimentationasaparadigmshi promisingmaterials.Insuchplanning,itisimportanttonote
inmaterialsandmoleculardiscovery.TheillustrationofFig.1 complementary search goals of optimizing a given material
providesthehighleveltemplateofaclosed-loopworkow,and property and establishing relationships that represent funda-
in the present work we critically review the progress towards mentalmaterialsknowledge.Mappingcomposition–structure–
this vision in solid materials experiments. The integration of processing–function relationships28–30 is a tenet of combinato-
sequentialautomatedprocessesischallengingduetotheneed rial materials research,28–30 which contrasts with direct imple-
for mutually compatible parameters and planning, with mentation of active learning to optimize31 one or a few
requirements spanning from a commensurate sample format, propertieswithoutrequiringacquisitionofdatatoelucidatethe
to a protocol for decision-making based on results from the underpinnings of the materials optimization. Indeed the
prior experiment, and to the identication of measurement experiment workow and its operation must be designed to
failure. To facilitate the analysis of where process integration meetthespecicresearchgoals,althoughworkowautomation
has been successfully implemented as well as the remaining isimportantforacceleratingmanydifferentmodesofdiscovery.
challenges,wepresentaframeworkandontologyfortheauto- We discuss the lifecycle of materials science experiments
mationofthematerialsexperimentlifecycle. and the three primary stages of workow acceleration, (i) the
The exploration of vast materials spaces (i.e. composition, integrationofnewtechniquesintotraditionalresearchtasksto
structure,processing,morphology)viacombinatorialmaterials accelerate process throughput, (ii) the integration of research
science has yielded a wide variety of discoveries and advance- tasksintoacohesiveworkowtomitigatebottlenecks,and(iii)
ments in fundamental knowledge14,18–20 and has additionally integration of tasks with automated analysis and decisions to
producedexperimentdatabaseswithunprecedentedbreadthof close experiment loops and enable autonomous iteration
materialsandmeasuredproperties,asexempliedbytherecent thereof.Wendthatthesolidstatematerialssciencecommu-
publication of the High Throughput Experimental Materials nity has demonstrated tremendous progress in the rst stage,
database (HTEM)21 based on photovoltaics materials and the substantial progress in the second stage including high
Materials Experiments and Analysis Database (MEAD)22 based throughput workows, and seminal demonstrations in the
on solar fuels materials. These compilations of raw and thirdstagewithrelativelysimpleworkows,makingconcurrent
Fig.1 Highlevelcomparisonofparadigmsformaterials/molecularsciences.Left:currentparadigmexemplifiedwithredoxflowbatteries.Right:
closed-loopdiscoveryutilizinginversedesignandatightlyintegratedworkflowtoenablefasteridentification,scale-upandmanufacturing.
FigurereproducedfromScience,361,6400,360–365withpermissionfromTheAmericanAssociationfortheAdvancementofScience.
Thisjournalis©TheRoyalSocietyofChemistry2019 Chem.Sci.,2019,10,9640–9649 | 9641
.MA
71:31:2
6202/1/6
no
dedaolnwoD
.9102 rebmetpeS
02
no
dehsilbuP
.elcitrA
sseccA
nepO
.ecneciL
detropnU
0.3
noitubirttA
snommoC
evitaerC
a
rednu
desnecil
si
elcitra
sihT
View Article Online

View Article Online
|     | ChemicalScience |     |         |           |     |          |     |        |        |     |     |     |     |     |     | Minireview |
| --- | --------------- | --- | ------- | --------- | --- | -------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | ---------- |
|     | advancement     |     | of both | the level | of  | autonomy | and | extent | of the |     |     |     |     |     |     |            |
workowapriorityresearchdirection.
|     | The      | experimental |           |     | materials |     | science |     |     |     |     |     |     |     |     |     |
| --- | -------- | ------------ | --------- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | research |              | lifecycle |     |           |     |         |     |     |     |     |     |     |     |     |     |
Atahighlevel,theexperimentlifecycle†forfunctionalmate-
|                                                                                      | rials discovery |             | consists | of               | a set | of  | core | research    | tasks: |     |     |     |     |     |     |     |
| ------------------------------------------------------------------------------------ | --------------- | ----------- | -------- | ---------------- | ----- | --- | ---- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| .ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  | synthesis,      | processing, |          | characterization |       |     | and  | performance |        |     |     |     |     |     |     |     |
 .MA 71:31:2 6202/1/6 no dedaolnwoD .9102 rebmetpeS 02 no dehsilbuP .elcitrA sseccA nepO evaluation.Thissettranscendsthespecictechniquesusedto
|     | perform | each | task, | and their | generality |     | is evident |     | in their |     |     |     |     |     |     |     |
| --- | ------- | ---- | ----- | --------- | ---------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
workow
|     | consistent           | discussion              |            | in       | reviews,1,32 |              | laboratory |               |        |     |     |     |     |     |     |     |
| --- | -------------------- | ----------------------- | ---------- | -------- | ------------ | ------------ | ---------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     | descriptions,6,33,34 |                         | and        | database | designs      |              | for high   | throughput    |        |     |     |     |     |     |     |     |
|     | materials            | science.5,6,10,32,35–37 |            |          | Oen         | unmentioned, |            |               | though |     |     |     |     |     |     |     |
|     | virtually            | always                  | performed, |          | are the      | additional   |            | core research |        |     |     |     |     |     |     |     |
tasksofplanning,datamanagement,datainterpretation,and
|     | quality | control. | Individual |      | and        | sequences |       | of experiments |      |     |     |     |     |     |     |     |
| --- | ------- | -------- | ---------- | ---- | ---------- | --------- | ----- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     | require | these    | tasks,     | with | the extent | and       | style | varying        | with |     |     |     |     |     |     |     |
researchstrategy.Inatraditionalmaterialsexperiment,the4
|     | experiment | tasks |     | are performed |     | manually, |     | as are | the |     |     |     |     |     |     |     |
| --- | ---------- | ----- | --- | ------------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
complementary 4 tasks, for example planning via a stated Fig.2 (a)Overviewofcoreresearchtaskswitharrowsindicatingthe
hypothesis and data management via lab notebooks. The cyclic execution of a traditional materials science experimental
workflow.(b)Accelerationofeachtaskinaworkflowcanbeobtained
workow
|     | corresponding |     |     | can | be  | represented |     | as shown | in  |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
byincorporatingaccelerationtechnique(s),asrepresentedbythese6
|     | Fig. 2a | and | represents |     | the foundation |     | on  | which | more |     |     |     |     |     |     |     |
| --- | ------- | --- | ---------- | --- | -------------- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
typesofaccelerators.
advancedandacceleratedworkowsarebuilt.Asnotedabove,
|     | the rst | stage      | of workow |        | acceleration |                | involves     | implementa- |                                                     |     |     |     |     |     |     |     |
| --- | -------- | ---------- | ---------- | ------ | ------------ | -------------- | ------------ | ----------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | tion of  | techniques | we         | refer  | to as        | “accelerators” |              | into        | one or                                              |     |     |     |     |     |     |     |
|     |          | workow    |            |        |              |                |              |             | extensivemethodsdevelopmentinthepasttwodecades,with |     |     |     |     |     |     |     |
|     | more of  | the        |            | tasks. | Classifying  |                | all possible | accelera-   |                                                     |     |     |     |     |     |     |     |
notabledemonstrationsincludingelectrochemicaltesting,43–46
|     | tors is | more subjective |     | than | the | above | classication | of  | work- |     |     |     |     |     |     |     |
| --- | ------- | --------------- | --- | ---- | --- | ----- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
owtasks,andforthepresentworkwendthe6accelerators X-raydiffraction,47–49processing,9,50,51opticalspectroscopy,52,53
|     |          |      |           |           |     |            |     |                 | electric | properties,65,66 |     | shape | memory,13,54 |     | and | phase |
| --- | -------- | ---- | --------- | --------- | --- | ---------- | --- | --------------- | -------- | ---------------- | --- | ----- | ------------ | --- | --- | ----- |
|     | noted in | Fig. | 2b enable | effective |     | annotation |     | of experimental |          |                  |     |       |              |     |     |       |
workows from the literature. Some accelerator-task combi- dynamics.9 These advancements in experiment automation
haveundoubtedlyledtodiscoveriesthatwouldnothavebeen
|     | nations | are readily | achievable, |     | for | example | parallelization |     | of  |     |     |     |     |     |     |     |
| --- | ------- | ----------- | ----------- | --- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
processingbyannealingmultiplematerialsinafurnace.Other made in the same time frame using traditional techniques.
|     |     |     |     |     |     |     |     |     | Automation | and | parallelization-based |     |     | removal | of  | synthesis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------------- | --- | --- | ------- | --- | --------- |
combinationsmaynotbemeaningful,suchasactivelearning
|     |     |     |     |     |     |     |     |     | and characterization |     |     | bottlenecks | introduces |     | new challenges |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ----------- | ---------- | --- | -------------- | --- |
ofdatamanagement.Ofthemanycombinationsthatareboth
meaningfulandimpactful,somehavebeeneffectivelyrealized for further acceleration of materials discovery, which are
|     |                                              |     |                   |     |     |         |            |     | generally     | being | addressed | with | data and | data | science-related |     |
| --- | -------------------------------------------- | --- | ----------------- | --- | --- | ------- | ---------- | --- | ------------- | ----- | --------- | ---- | -------- | ---- | --------------- | --- |
|     | while others                                 |     | are opportunities |     | for | further | experiment |     | accel-        |       |           |      |          |      |                 |     |
|     | eration,assummarizedbelowforeachaccelerator. |     |                   |     |     |         |            |     | accelerators. |       |           |      |          |      |                 |     |
Datarepositories
Automationandparallelization
|     |     |     |     |     |     |     |     |     | As noted | above, | the emergence |     | of experiment |     | databases | from |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------------- | --- | ------------- | --- | --------- | ---- |
Automatedexecutionofaserialexperimenttypicallyinvolves
offeropportunities
incorporation of robotics into a traditional experiment. Par- highthroughputexperimentation fordata-
|     |              |           |     |          |             |     |     |        | based accelerations. |     | The      | established | uses    | of data  | repositories   |     |
| --- | ------------ | --------- | --- | -------- | ----------- | --- | --- | ------ | -------------------- | --- | -------- | ----------- | ------- | -------- | -------------- | --- |
|     | allelization | typically |     | involves | development |     | of  | custom | instru-              |     |          |             |         |          |                |     |
|     |              |           |     |          |             |     |     |        | for accelerating     |     | research | tasks       | include | the data | interpretation |     |
mentationtoperformmanyexperimentssimultaneously.Both
diffraction
approaches are commonly used in combinatorial materials for crystallography by matching X-ray patterns to
|     |         |       |             |     |           |            |     |         | those from | a   | database,55 | planning | synthesis |     | based | on phase |
| --- | ------- | ----- | ----------- | --- | --------- | ---------- | --- | ------- | ---------- | --- | ----------- | -------- | --------- | --- | ----- | -------- |
|     | science | where | accelerated |     | synthesis | techniques |     | include | co-        |     |             |          |           |     |       |          |
sputtering,6co-evaporation,10ink-jetprinting,38combinatorial diagrams,56 and planning catalyst performance evaluation
|     |                 |     |                 |     |     |              |     |                 | using computational |     | databases |           | of Pourbaix | stability.57,58 |      | Data-      |
| --- | --------------- | --- | --------------- | --- | --- | ------------ | --- | --------------- | ------------------- | --- | --------- | --------- | ----------- | --------------- | ---- | ---------- |
|     | ball-milling,39 |     | high-throughput |     |     | hydrothermal |     | synthesis,40,41 |                     |     |           |           |             |                 |      |            |
|     |                 |     |                 |     |     |              |     |                 | driven discoveries  |     | are       | typically | enabled     | by a            | data | repository |
andbulkceramichot-pressing.42Similarly,theaccelerationof
thecharacterizationofmaterialspropertiesandevaluationof producedviacarefuldatamanagement.Whileguidelinessuch
asFAIR59exist,thesegeneralguidelinesfocusondatadissem-
|     | performancefora |     | targetfunctionalityhavebeenthefocusof |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inationanddonotexpressthedatamanagementrequirements
|     |            |            |              |             |           |           |          |           | for establishing   |           | autonomous |              | loops, which  | require | fully | auto-   |
| --- | ---------- | ---------- | ------------ | ----------- | --------- | --------- | -------- | --------- | ------------------ | --------- | ---------- | ------------ | ------------- | ------- | ----- | ------- |
|     | †There are | different  | terms        | to describe | the       | sequence  | and      | interplay | of basic           |           |            |              |               |         |       |         |
|     |            |            |              |             |           |           |          |           | mated data         | ingestion |            | and seamless | communication |         |       | between |
|     | research   | tasks such | as materials |             | pipeline, | materials | highway, | or        | materials          |           |            |              |               |         |       |         |
|     | platform.  |            |              |             |           |           |          |           | experimentaltasks. |           |            |              |               |         |       |         |
9642 | Chem.Sci.,2019,10,9640–9649 Thisjournalis©TheRoyalSocietyofChemistry2019

View Article Online
|     | Minireview |     |     |     |     |     |     |     |     |     |     |     |     | ChemicalScience |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
Machinelearning reinterpreted given the most recent measurements, the data
interpretation,qualitycontrol,andplanningtasksarenotreadily
|     | Acceleration | by  | Machine | Learning | (ML) | models | encompasses |               |     |          |             |     |            |                 |     |
| --- | ------------ | --- | ------- | -------- | ---- | ------ | ----------- | ------------- | --- | -------- | ----------- | --- | ---------- | --------------- | --- |
|     |              |     |         |          |      |        |             | automatedwith |     | existing | algorithms, |     | motivating | the development |     |
abroadrangeofapplicationsofcomputersciencealgorithmsto
ofautomatedreasoningtoacceleratethesetaskswithAImethods
|     | perform | regression, | classication |     | or embedding |     | tasks. The |     |     |     |     |     |     |     |     |
| --- | ------- | ----------- | ------------- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
thatmimicand/orsupersedehumanexecutionofthesetasks(i.e.
|     | recent literature |        | abounds | with         | discussions | of        | the existing and |             |                  |     |                 |          |        |           |          |
| --- | ----------------- | ------ | ------- | ------------ | ----------- | --------- | ---------------- | ----------- | ---------------- | --- | --------------- | -------- | ------ | --------- | -------- |
|     |                   |        |         |              |             |           |                  | “superhuman | performance”69). |     |                 |          |        |           |          |
|     |                   |        |         |              |             |           |                  |             |                  |     |                 | Examples | of     | automated | incorpo- |
|     | potential         | impact | of ML   | in materials |             | research. | Given recent     |             |                  |     |                 |          |        |           |          |
|     |                   |        |         |              |             |           |                  | ration of   | physics          | and | chemistry-based |          | models | into such | tasks    |
reviewscoveringthistopic,62thepresentdiscussionfocusesonits
includetuningthemorphologyofathinlmbasedonastructure
roleinexperimentworkows.ML-basedaccelerationofresearch
zonediagram51andne-tuningthecompositiontoobtainadesired
| .ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  | tasks typically | involves | either | research | planning |     | or data inter- |             |     |                |     |       |        |       |           |
| ------------------------------------------------------------------------------------ | --------------- | -------- | ------ | -------- | -------- | --- | -------------- | ----------- | --- | -------------- | --- | ----- | ------ | ----- | --------- |
|                                                                                      |                 |          |        |          |          |     |                | doping type | in  | semiconducting |     | metal | oxides | based | on spinel |
 .MA 71:31:2 6202/1/6 no dedaolnwoD .9102 rebmetpeS 02 no dehsilbuP .elcitrA sseccA nepO pretationthroughevaluationofMLmodelstrainedonpriordata.
dopingrules.70TheopportunityforAIdevelopmentinthisareais
Representativeexamplesincludeselectionofcompositionspaces
|     |               |                                     |     |     |     |     |         | the topic | of a | recent | perspective,69 |     | and among | the | promising |
| --- | ------------- | ----------------------------------- | --- | --- | --- | --- | ------- | --------- | ---- | ------ | -------------- | --- | --------- | --- | --------- |
|     | for exploring | metallicglassesbasedonMLpredictions |     |     |     |     | ofglass |           |      |        |                |     |           |     |           |
forming ability70 and identication of ultraincompressible researchdirectionsistheestablishmentofgenerativemodelsthat
expandthepurviewofactivelearningtodesignmaterialsbasedon
materials.71MLmethodshavealsobeendevelopedtoaccelerate
|     |     |     |     |     |     |     |     | desired properties.71 |     | While | inverse | design | has | been successfully |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ----- | ------- | ------ | --- | ----------------- | --- |
datainterpretationinareasincludingphasemappingfromXRD
demonstratedfordiscoveryoffunctionalmaterials,70–73integration
identication
|     | patterns,18                                     | microscopy | data,51 | signal |     |     | in spectros- |                |     |          |         |     |             |           |       |
| --- | ----------------------------------------------- | ---------- | ------- | ------ | --- | --- | ------------ | -------------- | --- | -------- | ------- | --- | ----------- | --------- | ----- |
|     |                                                 |            |         |        |     |     |              | into automated |     | workows | remains |     | a challenge | for solid | state |
|     | copy data,73annotationofmicrostructureimages,74 |            |         |        |     |     | andvisuali-  |                |     |          |         |     |             |           |       |
zation of complex compositions.34,73 ML methods can also be materials research. The corresponding high level challenge for
|     |           |      |        |          |     |           |             | closed-loop | experimentation |           | of        | solid | state materials | is         | that the |
| --- | --------- | ---- | ------ | -------- | --- | --------- | ----------- | ----------- | --------------- | --------- | --------- | ----- | --------------- | ---------- | -------- |
|     | developed | into | active | learning | and | reasoning | techniques, |             |                 |           |           |       |                 |            |          |
|     |           |      |        |          |     |           |             | scope of    | a given         | automated | synthesis |       | tool is         | oen quite | limited  |
althoughduetotheirdifferentroleswithrespecttoexperiments,
|     |     |     |     |     |     |     |     | comparedtothe |     | scopeofmaterialsthat |     |     | maybe | predictedbyan |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------------- | --- | --- | ----- | ------------- | --- |
thosetechniquesarediscussedseparately,asdetailedbelow.
|     |     |     |     |     |     |     |     | activelearningor |     | inverse | design | algorithm.In |     | organicsynthesis, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------ | ------------ | --- | ----------------- | --- |
forexample,therehasbeenmoresuccessindevelopingworkows
Activelearning that encompass the entirety of the synthesis scope of interest,
enablingdeeperintegrationofautomatedreasoning.17
Activelearninginvolvesthechoiceofthenextexperimentbased
|     | on an acquisition |         | function   | that            | typically        | requires   | a prediction     |             |        |      |       |             |            |           |         |
| --- | ----------------- | ------- | ---------- | --------------- | ---------------- | ---------- | ---------------- | ----------- | ------ | ---- | ----- | ----------- | ---------- | --------- | ------- |
|     | fora gureofmerit |         | and        | the uncertainty |                  | thereof.75 | MLmodels         |             |        |      |       |             |            |           |         |
|     |                   |         |            |                 |                  |            |                  | Integration |        | of   | tasks | into        | a workflow |           |         |
|     | are used          | for the | prediction | and             | uncertainty      |            | estimation, with |             |        |      |       |             |            |           |         |
|     | a distinguishing  |         | feature    | of active       | learning         | being      | the need         | to          |        |      |       |             |            |           |         |
|     |                   |         |            |                 |                  |            |                  | The most    | common | type | of    | accelerated |            | discovery | workow |
|     | update the        | model   | in real    | time            | during execution |            | of the experi-   |             |        |      |       |             |            |           |         |
mentalworkow.Activelearningisakeycomponentofclosed- consists of an automation-accelerated synthesis and an
loop workows that can ultimately yield self-driving laborato- automation-acceleratedcharacterizationorperformanceevalua-
|     |                    |     |      |               |     |           | specically | tion,followedbyextensivemanualanalysis,interpretation,and |     |     |     |     |     |     |     |
| --- | ------------------ | --- | ---- | ------------- | --- | --------- | ----------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | ries.44 Algorithms |     | such | as Phoenics63 |     | have been |             |                                                           |     |     |     |     |     |     |     |
developed for chemistry experiments and integrated into planning of both additional characterization experiments and
workowmanagementsowaresuchasChemOS.64Thecarbon future iterations of the workow. Most commonly the highly
nanotube(CNT)autonomousresearchsystem(ARES)project,65 automated instruments require manual interfacing (e.g. align-
whichisdiscussedfurtherbelow,isanexampleofaclosed-loop ment, measurement parameter setup, supervision for quality
systemofaworkowwheretaskssuchasdatainterpretationare control),whereanincreasedhumaninvolvementcorrespondsto
readily automated. There have been additional implementa- alowerdegreeofintegration.Tosimplifythepresentdiscussion,
|     |     |     |     |     |     |     |     | we consider | two | classes | of  | task | integration | with | the dis- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --- | ---- | ----------- | ---- | -------- |
tionsofactivelearninginmaterialssciencetoaccelerateindi-
vidualtasks,forexamplebyacquiringonlythenecessaryX-ray tinguishing feature being whether expert involvement is
required,whichdesignatestheintegrationas“expertmediated”
|     | diffraction   | patterns | for | phase     | diagram  | characterization.66 |         |               |     |             |     |                |     |            |          |
| --- | ------------- | -------- | --- | --------- | -------- | ------------------- | ------- | ------------- | --- | ----------- | --- | -------------- | --- | ---------- | -------- |
|     |               |          |     |           |          |                     | elds   | and indicates | the | integration |     | is incomplete. |     | This level | of inte- |
|     | Sophisticated | examples |     | of active | learning | in                  | related |               |     |             |     |                |     |            |          |
including functional genomics,67 separations optimization,64 gration is prone to creating bottlenecks due to the scarcity of
|     |     |     |     |     |     |     |     | experts. | Technique | integration |     | by robotics | is  | not distinguished |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----------- | --- | ----------- | --- | ----------------- | --- |
andmultiobjectivemolecularoptimizationforsmallmolecule
|     |                   |     |       |      |                       |     |          | from integration |     | by trained |     | technicians | in  | the present | work |
| --- | ----------------- | --- | ----- | ---- | --------------------- | --- | -------- | ---------------- | --- | ---------- | --- | ----------- | --- | ----------- | ---- |
|     | drug discovery.68 |     | While | many | optimization-oriented |     | searches |                  |     |            |     |             |     |             |      |
workow
are amenable to acceleration via active learning, its utility for because the resulting impact on throughput requires
|     |           |           |     |        | sufficiently |     |              | morein-depthevaluationofthespecicworkow. |     |     |     |     |     |     |     |
| --- | --------- | --------- | --- | ------ | ------------ | --- | ------------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | materials | discovery | has | yet to | be           |     | explored and |                                            |     |     |     |     |     |     |     |
demonstrated, making the above examples a springboard for Tofurtherillustratehowacceleratedmaterialsexperiments
|     |           |             |     |        |          |               |         | have been | integrated, |     | we inspect | four | reported | projects | and |
| --- | --------- | ----------- | --- | ------ | -------- | ------------- | ------- | --------- | ----------- | --- | ---------- | ---- | -------- | -------- | --- |
|     | assessing | the ability | of  | active | learning | to accelerate | complex |           |             |     |            |      |          |          |     |
workows constructthecorrespondingworkowsinFig.3.Eachworkow
|     | experimental |     |     | and the | generation |     | of fundamental |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | ------- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
understandinginmaterialsscience. exhibits unique aspects that collectively frame the stateof the
|     |     |     |     |     |     |     |     | art in accelerated |         | materials     |     | discovery | and   | illustrate | the intri- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ------- | ------------- | --- | --------- | ----- | ---------- | ---------- |
|     |     |     |     |     |     |     |     |                    | workow |               |     |           |       |            | workow    |
|     |     |     |     |     |     |     |     | cacies of          |         | acceleration. |     | The       | scope | of each    |            |
Automatedreasoning
|     |     |     |     |     |     |     |     | schematicis | the | sequence | oftasks |     | describedinthe | respective |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------- | --- | -------------- | ---------- | --- |
For complex measurement workows where competing interpre- publications, and the largest demonstrated equivalent of
traditionalexperimentationisprovidedforeachworkow.
tationsofthedataneedtobeconsideredoramodelneedstobe
Thisjournalis©TheRoyalSocietyofChemistry2019 Chem.Sci.,2019,10,9640–9649 | 9643

ChemicalScience Minireview
Theprimaryexampleofclosed-loopdiscoveryinsolidstate Ramanspectroscopy,producingspectrogramsthatareanalyzed
materials science is the ARES project for carbon nanotube todeterminethenanotubegrowthrate.14,65Withthismaterials
synthesis. Nikolaev et al.14 demonstrated optimization of characterizationalsoprovidingthegureofmerit,theworkow
carbonnanotubegrowthwithaworkowthatmitigatesexpert- contains no further performance evaluation. The automated
mediated integration and features acceleration by automation data management and interpretation enables closed-loop
andactivelearning.Automatedcontrolofgrowthtemperature, operation for up to approximately 100 growth experiments
pressure,andatmosphericconditionsenablesauniquegrowth planned by active learning-based selection of growth condi-
condition in each experiment, with a series of experiments tions. Expert intervention in this closed loop occurs occasion-
performed by spatially addressing an array of seeds on ally (estimated to be 1–3%) to assess the quality of the active
asubstrate.Processingandcharacterizationareintertwinedas learningandadjusttheobjectiveasnecessary.Uponexhaustion
laser illumination provides both heating and excitation for
Fig.3 Workflowdiagramsofacceleratedmaterialsexperimentationspanningarangeoftechniques,strategiesandresearchgoals.Basedon(a)
Nikolaevetal.,14(b)Yanetal.,20(c)Kusneetal.,66and(d)Lietal.,29eachworkflowinvolvesacceleratedtaskswithvariouslevelsofautomationand
task-to-taskintegration.Theproductivityforasinglepassthroughtheworkflowisnoted,correspondingtothenumberofequivalenttraditional
experiments for (a)–(c) and duration of traditional experiments for (d). Feedback loops are each labelled with the approximate number of
iterationsperworkflowexecution(bold),andin(a)and(c)thepercentageofiterationsinvolvingexpertmediationisalsoapproximated(italics).
9644 | Chem.Sci.,2019,10,9640–9649 Thisjournalis©TheRoyalSocietyofChemistry2019
.MA
71:31:2
6202/1/6
no
dedaolnwoD
.9102 rebmetpeS
02
no
dehsilbuP
.elcitrA
sseccA
nepO
.ecneciL
detropnU
0.3
noitubirttA
snommoC
evitaerC
a
rednu
desnecil
si
elcitra
sihT
View Article Online

View Article Online
| Minireview |     |     |     |     |     |     |     |     |     | ChemicalScience |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
atomprobetomography(APT)characterizationaereachpro-
| of the | array | of CNT | growth | seeds, | manual | intervention |     | is  |     |     |     |
| ------ | ----- | ------ | ------ | ------ | ------ | ------------ | --- | --- | --- | --- | --- |
requiredtochangesamplesandrestarttheworkow. cessingstep.EachAPTcharacterizationinvolvesdestructionof
ThephotoanodediscoverypipelineinFig. 2brepresentsthe oneofthereactors,andthe numberofreactorsismadetobe
tiered screening by Yan et al.20 that includes both theory and severaltimeslargerthanthenumberofprocessingstepsdueto
experiment-based down-selection of candidate metal oxides. routine failure of the APT measurement. The critical advance-
Withrespecttotheexperiments,thecomputationalscreeningis ment enabled by a small autonomous loop is the real-time
anaccelerantandrepresentedassuchintheplanningtask.The monitoring of APT data acquisition with well-integrated
MaterialsProjectdatabase60servesastheprimaryrepository,with quality control. Data interpretation is performed by compar-
additional calculations specic to photoanode screening, and ison to external data and visualization is done through
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
while these calculations are critical to the success of the work, a machine learning model.30,76 The richness of the APT data
 .MA 71:31:2 6202/1/6 no dedaolnwoD .9102 rebmetpeS 02 no dehsilbuP .elcitrA sseccA nepO
|     |     |     |     |     |     |     | workow. | signicant |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --- | --- |
they are not fully integrated into the experimental coupled with annealing time reduction yields high
Synthesis, processing,characterization, andperformanceevalu- throughput knowledge generation even though the workow
ationareacceleratedusingautomation,withtenstothousandsof containsmostlyexpert-mediatedintegrationoftasks.Increased
materials being synthesized or measured automatically. While autonomy in the workow would only be warranted aer
thissequenceoftasksisinprincipleamenabletomoreautono- substantialadvancesinautomateddatainterpretation.
Foreachoftheseworkows,thenominaltimetoexecutethe
| mous operation, |     | setup | and | selection | on  | meaningful |     | experi- |     |     |     |
| --------------- | --- | ----- | --- | --------- | --- | ---------- | --- | ------- | --- | --- | --- |
mental conditions are chosen by an expert, resulting in expert entireworkowisontheorderof1day.Theequivalentnumber
workow. ofpassesthroughatraditionalworkow,orthenumberofdays
| mediated | linkages | in  | the |     | The heavy | use | of paralleli- |     |     |     |     |
| -------- | -------- | --- | --- | --- | --------- | --- | ------------- | --- | --- | --- | --- |
zationandautomationissupportedbyautomaticdatamanage- oftraditionalexperimentation toproduce the equivalent data,
ment and quality control, with data interpretation requiring providesthenominalaccelerationfactoroftheworkow,which
workow
expert mediation. A key attribute of this is the estab- isonlyequaltotheaccelerationfactorofknowledgediscoveryif
lishmentofautomatedtechniquesforalargebreadthofexperi- theselectionofexperimentsandqualityoftheresultingdatais
mentaltasks,fromsynthesistoperformanceevaluation,thatcan equivalent to those of traditional experiments. Assessment of
operateonlibrarieswithuptoca.2000uniquematerials.74The such data value is beyond the scope of the present discussion
research strategy involves collection of combinatorial materials but remains a critical consideration for quantifying workow
scientic
datasets that facilitate data interpretation and acceleration, particularly in settings where the research goals
discovery, as well as evaluation of every prediction from the involve understanding the underlying materials science as
computational screeningtoassess its efficacy.These aspectsof opposedtoperformanceoptimization.
theresearchlimitthevalueoffurthertask-to-taskintegrationand
| application | of     | active learning, |                    | with the | broader | message            |     | being |     |     |     |
| ----------- | ------ | ---------------- | ------------------ | -------- | ------- | ------------------ | --- | ----- | --- | --- | --- |
| that the    | impact | ofthe            | closed-loopconcept |          |         | varieswithresearch |     |       |     |     |     |
strategyandgoals.
TheworkowofFig.3cdescribesadifferentimplementation
| of combinatorial |             | materials   |                    | science | for studying |             | functional |        |     |     |     |
| ---------------- | ----------- | ----------- | ------------------ | ------- | ------------ | ----------- | ---------- | ------ | --- | --- | --- |
| materials        | where       | synthesis,  | processing         |         | and          | performance |            | evalu- |     |     |     |
| ation are        | accelerated |             | by parallelization |         | and          | automation  |            | with   |     |     |     |
| expert-mediated  |             | integration |                    | similar | to that      | of          | Fig. 3b.   | The    |     |     |     |
uniqueaspectofthisworkistheuseofanactivelearningloop
workow
| in the middle |     | of the |     | to accelerate |     | the | mapping | of  |     |     |     |
| ------------- | --- | ------ | --- | ------------- | --- | --- | ------- | --- | --- | --- | --- |
phaseboundariesinacompositionlibrary,demonstratingthe
sub-workow
| use of active   | learning |      | in a |          | to       | accelerate | a      | bottle- |     |     |     |
| --------------- | -------- | ---- | ---- | -------- | -------- | ---------- | ------ | ------- | --- | --- | --- |
| neck experiment |          | (and | save | valuable | beamline |            | time). | The     |     |     |     |
synchrotronX-raydiffraction(XRD)characterizationdescribed
on-the-y
| by Kusne      | et al.66  | includes |            |        | data        | interpretation |     | and    |     |     |     |
| ------------- | --------- | -------- | ---------- | ------ | ----------- | -------------- | --- | ------ | --- | --- | --- |
| automated     | selection |          | of the     | next   | composition |                | for | XRD    |     |     |     |
| measurements, |           | with     | occasional | expert |             | supervision    |     | of the |     |     |     |
clustering-basedidenticationofpure-phasepatterns.
Fig.4 Visualizationofthelandscapeofmaterialsexperimentwork-
The atomic-scale phase evolution workow by Li et al.29 flowintermsofthescientificcomplexityofautomatedtasksandthe
|     |     |     |     |     |     |     |     | workflow automation | complexity, which | is based on | the number, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ----------------- | ----------- | ----------- |
illustratedinFig.3dusesaspecializednanometersizedreactor
variety,speed,anddifficultyofexperimentalstepsintheworkflow.The
| to assess | phase | stability | with | ca. 1 | hour | of experiment |     | time |     |     |     |
| --------- | ----- | --------- | ---- | ----- | ---- | ------------- | --- | ---- | --- | --- | --- |
advancementsincombinatorialmaterialsscienceandhighthroughput
| yielding | the same | data | as over | 500 days | of  | annealing | in  | tradi- |     |     |     |
| -------- | -------- | ---- | ------- | -------- | --- | --------- | --- | ------ | --- | --- | --- |
experimentation(CMS/HTE)havebeenlargelyalongthislatter(hori-
tional bulk experiments. Using data repositories of phase zontal) axis, and initial demonstrations of autonomous loops have
diagrams and stability ranges of multicomponent complex madeprogressontheformer(vertical)axiswithautomationofmore
intellectuallychallengingresearchtasks.Thenominallocationofthe4
| metal alloys |     | to plan | synthesis, | an  | array | of 36 | reactors | is  |     |     |     |
| ------------ | --- | ------- | ---------- | --- | ----- | ----- | -------- | --- | --- | --- | --- |
workflowsfromFig.3arenotedbystars.Whileresearchwillpushthe
deposited,forexamplewithequiatomicmixturesoftheCantor
|     |     |     |     |     |     |     |     | frontier of automated | experiments | along both axes | (arrows with |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | ----------- | --------------- | ------------ |
alloyCr–Mn–Fe–Co–Ni.75Theloopinthisworkowisbasedon
italics),themostcomplexscientifictaskswillremaintheresponsibility
the step-wise annealing of the reactor array with subsequent ofhumanexpertsfortheforeseeablefuture.
Thisjournalis©TheRoyalSocietyofChemistry2019 Chem.Sci.,2019,10,9640–9649 | 9645

View Article Online
| ChemicalScience |     |     |     |     |     |     |     |     |     |     |     |     | Minireview |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
workows
Conclusions and outlook this existing work makes autonomous more readily
|     |     |     |     |     |     |     |     | extendable |     | into complex | automation | as compared | to the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | ---------- | ----------- | ------ |
extremesofcomplexscienticreasoning.
| The urgent |     | need for | better | materials | demands | faster | turn- |     |     |     |     |     |     |
| ---------- | --- | -------- | ------ | --------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
aroundcyclesfrombasicresearch,suchthatbetter,moreeffi- Anoutstandingquestionwithregardtothenextgeneration
ofexperimentalworkowsishowtobestcombathumanbiases
| cient, | more | eco | friendly, | and more | economically |     | viable |     |     |     |     |     |     |
| ------ | ---- | --- | --------- | -------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- |
materials can enter the market sooner than the traditionally that can severely limit innovation.77 Advanced autonomous
observed40years.1Acceleratedmaterialsexperimentworkows experimentationmayremovebiaseswithinagivensearchspace
havebeendemonstratedtoincreasethroughputbyuptoafew through computationally designed experiments. However, the
orders of magnitude compared to traditional methods. scope of the search space is limited by both instrument capa-
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
Surveyingthereportedworkowsrevealstwoprimaryareasfor bilities and active learning strategy, whose designs originate
 .MA 71:31:2 6202/1/6 no dedaolnwoD .9102 rebmetpeS 02 no dehsilbuP .elcitrA sseccA nepO
workow withhumanidenticationofthematerialsspaceofinterest.To
|     | sophistication, |     | the | integration | of  | sequential | tasks |     |     |     |     |     |     |
| --- | --------------- | --- | --- | ----------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
without requiring expert involvement and the expansion of theextentthathumanbiasesdisseminatefromthe“complex”
| feedbackloopstoincorporatealargerfractionoftheworkow |     |     |     |     |     |     |     | scientic |       |                 |         |           |            |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --------------- | ------- | --------- | ---------- |
|                                                       |     |     |     |     |     |     |     |           | tasks | of Fig. 4, bias | removal | within an | autonomous |
tasks. The ARES workow achieves both of these goals with workow must be complemented by sociological solutions for
a relatively small workow compared to the functional mate- removingbiasindecisionsbeyondtheexperimentworkow.
rials discovery research where the variety of characterization We are aware of several research groups that are building
andperformanceevaluationexperimentsincreasesthenumber autonomous experiments in the "next generation" regime of
ofworkowtasksaswellasthedemandsondatamanagement, synthesis78
|     |     |     |     |     |     |     |     | Fig. 4, | including | emerging | reports | from perovskite |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------- | ------- | --------------- | --- |
datainterpretation,andqualitycontrol. and molecular materials for of organic photovoltaics79 and
Tovisualizeprogresstodateandtheexpectedadvancesfrom organic hole transport materials.80 Continuation of these
efforts
ongoing research, Fig. 4 illustrates the continuum of materials concerted to increase automation and develop tailored
workows in terms of the scientic complexity and workow AI algorithms will enable the materials science community to
|            |     |             |     |               |          |         |     | realize | a paradigm | shi in | scientic | discovery | where expert |
| ---------- | --- | ----------- | --- | ------------- | -------- | ------- | --- | ------- | ---------- | ------- | --------- | --------- | ------------ |
| automation |     | complexity. | To  | elucidate our | intended | meaning |     | of      |            |         |           |           |              |
scientic complexity, representative tasks spanning minimal scientists can dedicate a substantially larger fraction of their
complexitytoverycomplexarelisted.Arguablythemostimpor- time to performing the critical tasks of identifying important
tant aspect of a successful science program is the ability to problemsandcommunicatingcriticalinsights.
| identify | interesting |     | problems | and ask | the important |     | questions |           |     |             |     |     |     |
| -------- | ----------- | --- | -------- | ------- | ------------- | --- | --------- | --------- | --- | ----------- | --- | --- | --- |
|          |             |     |          |         |               |     |           | Conflicts |     | of interest |     |     |     |
thatguideresearchactivities.Thesetasksarebeyondthepurview
ofpresentautonomousresearchandwillbefortheforeseeable
future. Advances in natural language processing for materials Therearenoconictstodeclare.
sciencemayautomateaspectsofscienticcommunication,but
critical analysis of the literature and communication of the Acknowledgements
insightsprovidedbyagivenexperimentwillcontinuetorelyon
humanintellectfortheforeseeablefuture. This material is based upon work supported by the Air Force
Determiningthemosteffectiveadvancementsinamaterials OfficeofScienticResearchunderawardnumberFA9550-18-1-
| experimentworkowrequirescriticalevaluationofbottlenecks |     |     |     |     |     |     |     |       | Office |            |        |                 |           |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ---------- | ------ | --------------- | --------- |
|                                                          |     |     |     |     |     |     |     | 0136, | the    | of Science | of the | U.S. Department | of Energy |
for progress against the research goals. Even when expert underAwardNo.DE-SC0004993,andanAcceleratedMaterials
mediation is required between tasks, workow throughput is DesignandDiscoverygrantfromtheToyotaResearchInstitute.
oenlimitedbythemanualstepsatthefrontandbackendsof
automatedexperiments.Theseperipheral activities,whichfall References
|       |     |              |     | “complicated” |       |     | scientic |     |     |     |     |     |     |
| ----- | --- | ------------ | --- | ------------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- |
| under | the | intermediate |     |               | level | of  |           |     |     |     |     |     |     |
complexityinFig.4,canbedifficult(orcurrentlyimpossible)to 1 K. Alberi, et al., The 2019 materials by design roadmap, J.
fullyautomateduetotheroutineuseofexpertknowledge,for Phys.D:Appl.Phys.,2019,52,013001.
example in judgement of data quality based on extensive 2 Report of the Clean Energy Materials Innovation Challenge
previous experience with related data. Advances in articial Expert Workshop January 2018, Mission Innovation, 2018,
http://mission-innovation.net/wp-content/uploads/2018/01/
| intelligence |     | (AI) for | materials | encompasses | a   | wide | variety | of  |     |     |     |     |     |
| ------------ | --- | -------- | --------- | ----------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- |
strategiesforaddressingthesechallenges,whichwillbecritical Mission-Innovation-IC6-Report-Materials-Acceleration-
forexpandingthescopeofautonomousloops.Thisapproachto Platform-Jan-2018.pdf.
pushingthefrontierofmaterialsworkowsisillustratedbythe
|     |     |     |     |     |     |     |     | 3 X.-D. | Xiang | and I. | Takeuchi, | Combinatorial | Materials |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------ | --------- | ------------- | --------- |
“Materials AI” arrow in Fig. 4 and will ideally accompany the Synthesis,CRCPress,2003.
|                       |     |     |     |                |             |     |     | 4 H. | Koinuma | and I. | Takeuchi, | Combinatorial | solid-state |
| --------------------- | --- | --- | --- | -------------- | ----------- | --- | --- | ---- | ------- | ------ | --------- | ------------- | ----------- |
| expansionofautonomous |     |     |     | loopstoinclude | morecomplex |     | and |      |         |        |           |               |             |
chemistryofinorganicmaterials,Nat.Mater.,2004,3,429–438.
| a larger | variety | of  | experimental | tasks. | This | complementary |     |     |     |     |     |     |     |
| -------- | ------- | --- | ------------ | ------ | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
approach to pushing the frontier of materials workows is 5 W.F.Maier,K.St¨oweandS.Sieg,CombinatorialandHigh-
|     |     | “Build |     | HTE” |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
illustrated by the on arrow due to the demon- ThroughputMaterialsScience,Angew.Chem.,Int.Ed.,2007,
strated successes in experiment automation from the high 46,6016–6067.
throughputexperimentationcommunity.Theabilitytoleverage 6 A. Ludwig, R. Zarnetta and S. Hamann, Development of
lms
|     |     |     |     |     |     |     |     | multifunctional |     | thin |     | using high-throughput |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---- | --- | --------------------- | --- |
9646 | Chem.Sci.,2019,10,9640–9649 Thisjournalis©TheRoyalSocietyofChemistry2019

Minireview ChemicalScience
experimentationmethods,J.Mater.Chem.A,2008,99,1144– 23 C. P. Gomes, et al., CRYSTAL: a multi-agent AI system for
1149. automated mapping of materials' crystal structures, MRS
7 C. J. Long, D. Bunker, X. Li, V. L. Karen and I. Takeuchi, Commun.,1–9,DOI:10.1557/mrc.2019.50,undened/ed.
Rapid identication of structural phases in combinatorial 24 J. O'Mara, B. Meredig and K. Michel, Materials data
thin-lm libraries using X-ray diffraction and non-negative infrastructure: a case study of the citrination platform to
matrix factorization, Rev. Sci. Instrum., 2009, 80, 103902– examine data import, storage, and access, JOM, 2016, 68,
103906. 2031–2034.
8 D.A.Keller,etal.,UtilizingPulsedLaserDepositionLateral 25 B.Blaiszik,etal.,TheMaterialsDataFacility:Dataservicesto
InhomogeneityasaToolinCombinatorialMaterialScience, advance materials science research, JOM, 2016, 68, 2045–
ACSComb.Sci.,2015,17,209–216. 2052.
9 Z. Li, A. Ludwig, A. Savan, H. Springer and D. Raabe, 26 L. Weston, et al., Named Entity Recognition and
Combinatorial metallurgical synthesis and processing of Normalization Applied to Large-Scale Information
high-entropyalloys,J.Mater.Res.,2018,33,3156–3169. Extraction from the Materials Science Literature, J. Chem.
10 J.N.Cawse,ExperimentalStrategiesforCombinatorialand Inf.Model.,2019,59(9),3692–3702.
High-Throughput Materials Development, Acc. Chem. Res., 27 F. H¨ase, L. M. Roch and A. Aspuru-Guzik, Next-Generation
2001,34,213–221. Experimentation with Self-Driving Laboratories, Trends in
11 E. M. Chan, Combinatorial approaches for developing Chemistry,2019,1,282–291.
upconverting nanomaterials: high-throughput screening, 28 S. K. Suram, et al., High Throughput Light Absorber
modeling, and applications, Chem. Soc. Rev., 2015, 44, Discovery, Part 2: Establishing Structure–Band Gap Energy
1653–1679. Relationships,ACSComb.Sci.,2016,18,682–688.
12 S. K. Saikin, C. Kreisbeck, D. Sheberla, J. S. Becker and 29 Y. J. Li, A. Savan, A. Kostka, H. S. Stein and A. Ludwig,
A. Aspuru-Guzik, Closed-loop discovery platform Accelerated atomic-scale exploration of phase evolution in
integration is needed for articial intelligence to make an compositionallycomplexmaterials,Mater.Horiz.,2018,5.
impact in drug discovery, Expert Opin. Drug Discovery, 30 H. Stein, et al., Functional mapping reveals mechanistic
2019,14,1–4. clustersforOERcatalysisacross(Cu–Mn–Ta–Co–Sn–Fe)Ox
13 J. Cui, et al., Combinatorial search of thermoelastic shape- composition and pH space, Mater. Horiz., 2019, 6, 1251–
memory alloys with extremely small hysteresis width, Nat. 1258.
Mater.,2006,5,286–290. 31 S. K. Suram, M. Z. Pesenson and J. M. Gregoire, High
14 P. Nikolaev, et al., Autonomy in materials research: a case Throughput Combinatorial Experimentation + Informatics
study in carbon nanotube growth, npj Comput. Mater., ¼ Combinatorial Science, in Information Science for
2016,2,16031. Materials Discovery and Design, ed. T. Lookman, F. J.
15 D.P.Tabor,etal.,Acceleratingthediscoveryofmaterialsfor AlexanderandK.Rajan,SpringerInternationalPublishing,
cleanenergyintheeraofsmartautomation,Nat.Rev.Mater., 2016,pp.271–300,DOI:10.1007/978-3-319-23871-5_14.
2018,3,5. 32 R. A. Potyrailo and V. M. Mirsky, Combinatorial and High-
16 T.Dimitrov,C.Kreisbeck,J.S.Becker,A.Aspuru-Guzikand Throughput Development of Sensing Materials: The First
S.K.Saikin,AutonomousMolecularDesign:ThenandNow, 10Years,Chem.Rev.,2008,108,770–813.
ACSAppl.Mater.Interfaces,2019,11(28),24825–24836. 33 J. M. Gregoire, C. Xiang, X. Liu, M. Marcin and J. Jin,
17 B. Sanchez-Lengeling and A. Aspuru-Guzik, Inverse Scanning droplet cell for high throughput electrochemical
molecular design using machine learning: Generative and photoelectrochemical measurements, Rev. Sci.
modelsformatterengineering,Science,2018,361,360–365. Instrum.,2013,84,24102–24107.
18 M. Umehara, et al., Analyzing machine learning models to 34 K.Sliozberg,etal.,High-ThroughputScreeningofThin-Film
accelerate generation of fundamental materials insights, Semiconductor Material Libraries I: System Development
npjComput.Mater.,2019,5,34. and Case Study for Ti–W–O, ChemSusChem, 2015, 8, 1270–
19 A. Ludwig, Discovery ofnew materials using combinatorial 1278.
synthesis and high-throughput characterization of thin- 35 S. Curtarolo, et al., The high-throughput highway to
lm materials libraries combined with computational computational materials design, Nat. Mater., 2013, 12,
methods,npjComput.Mater.,2019,5,70. 191–201.
20 Q.Yan,etal.,Solarfuelsphotoanodematerialsdiscoveryby 36 A.Zakutayev,etal.,HighThroughputExperimentalMaterials
integrating high-throughput theory and experiment, Proc. Database,2017,DOI:10.7799/1407128.
Natl.Acad.Sci.U.S.A.,2017,114,3040–3043. 37 W.F.Maier,EarlyYearsofHigh-ThroughputExperimentation
21 A. Zakutayev, et al., An open experimental database for and Combinatorial Approaches in Catalysis and Materials
exploringinorganicmaterials,Sci.Data,2018,5,1–12. Science,ACSComb.Sci.,2019,21,437–444.
22 E. Soedamadji, H. Stein, S. Suram, D. Guevarra and 38 X. Liu, et al., Inkjet Printing Assisted Synthesis of
J. Gregoire, Tracking materials science data lineage to Multicomponent Mesoporous Metal Oxides for Ultrafast
manage millions of materials experiments and analyses, CatalystExploration,NanoLett.,2012,12,5733–5739.
npjComput.Mater.,2019,79.
Thisjournalis©TheRoyalSocietyofChemistry2019 Chem.Sci.,2019,10,9640–9649 | 9647
.MA
71:31:2
6202/1/6
no
dedaolnwoD
.9102 rebmetpeS
02
no
dehsilbuP
.elcitrA
sseccA
nepO
.ecneciL
detropnU
0.3
noitubirttA
snommoC
evitaerC
a
rednu
desnecil
si
elcitra
sihT
View Article Online

View Article Online
| ChemicalScience |     |     |     |     |     |     |     |     |     | Minireview |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
Diffraction
39 B.Li,etal.,HydrogenStorageMaterialsDiscoveryviaHigh 55 International Centre for Data, ICDD, Powder
ThroughputBallMillingandGasSorption,ACSComb.Sci., Diffraction File. Powder Diffraction File, Newtown Square,
2012,14,352–358.
Pennsylvania,USA.
40 X.Weng,etal.,High-ThroughputContinuousHydrothermal 56 H.Baker,ASMhandbook,ASMinternational,1992,vol.3.
SynthesisofanEntireNanoceramicPhaseDiagram,J.Comb. 57 K.A.Persson,B.Waldwick,P.LazicandG.Ceder,Prediction
| Chem.,2009,11,829–834. |     |     |     |     |                  |     |             |        |            | rst- |
| ---------------------- | --- | --- | --- | --- | ---------------- | --- | ----------- | ------ | ---------- | ----- |
|                        |     |     |     |     | of solid-aqueous |     | equilibria: | Scheme | to combine |       |
41 R. Jin, G. Chen, J. Pei and C. Yan, Hydrothermal synthesis principlescalculationsofsolidswithexperimentalaqueous
PbS–PbTe core–
and thermoelectric transport property of states, Phys. Rev. B: Condens. Matter Mater. Phys., 2012, 85,
| shellheterostructures,NewJ.Chem.,2012,36,2574–2576. |     |     |     |     | 235438. |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
42 T. A. Stegk, R. Janssen and G. A. Schneider, High- 58 A. K. Singh, et al., Electrochemical Stability of Metastable
 .MA 71:31:2 6202/1/6 no dedaolnwoD .9102 rebmetpeS 02 no dehsilbuP .elcitrA sseccA nepO
Materials,Chem.Mater.,2017,29,10159–10167.
| Throughput |     | Synthesis | and Characterization | of  | Bulk |     |     |     |     |     |
| ---------- | --- | --------- | -------------------- | --- | ---- | --- | --- | --- | --- | --- |
Ceramics from Dry Powders, J. Comb. Chem., 2008, 10, 59 M. D. Wilkinson, et al., The FAIR Guiding Principles for
| 274–279. |     |     |     |     | scientic |      |            |                  |     |            |
| -------- | --- | --- | --- | --- | --------- | ---- | ---------- | ---------------- | --- | ---------- |
|          |     |     |     |     |           | data | management | and stewardship, |     | Sci. Data, |
43 J. Jin, J. M. Gregoire and C. Xiang, Scanning Drop Sensor, 2016,3,160018–160019.
2013,pp.1–12. 60 A. Jain, et al., Commentary: The materials project: A
44 A. I. Mardare, A. Ludwig, A. Savan and A. W. Hassel, materials genome approach to accelerating materials
Scanning droplet cell microscopy on a wide range innovation,APLMater.,2013,1,011002.
| hafnium–niobium |     |     | lm |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thin combinatorial library, 61 S.Curtarolo,etal.,AFLOWLIB.ORG:adistributedmaterials
Electrochim.Acta,2013,110,539–549.
|     |     |     |     |     | properties | repository | from | high-throughput |     | ab initio |
| --- | --- | --- | --- | --- | ---------- | ---------- | ---- | --------------- | --- | --------- |
45 J. P. Grote, A. R. Zeradjanin, S. Cherevko and calculations,Comput.Mater.Sci.,2012,58,227–235.
ow
K. J. J. Mayrhofer, Coupling of a scanning cell with 62 J.-P. Correa-Baena, et al., Accelerating Materials
online electrochemical mass spectrometry for screening of Development via Automation, Machine Learning, and
reactionselectivity,Rev.Sci.Instrum.,2014,85,104101. High-PerformanceComputing,Joule,2018,2,1410–1420.
46 A.K.Schuppert,A.A.Topalov,I.Katsounaros,S.O.Klemm 63 F. H¨ase, L. M. Roch, C. Kreisbeck and A. Aspuru-Guzik,
andK.J.J.Mayrhofer,AScanningFlowCellSystemforFully Phoenics: A Bayesian Optimizer for Chemistry, ACS Cent.
Sci.,2018,4,1134–1145.
| Automated | Screening |     | of Electrocatalyst | Materials, | J.  |     |     |     |     |     |
| --------- | --------- | --- | ------------------ | ---------- | --- | --- | --- | --- | --- | --- |
Electrochem.Soc.,2012,159,F670–F675. 64 L. M. Roch, et al., ChemOS: An Orchestration Soware to
47 I.Takeuchi,C.J.LongandO.O.Famodu,Datamanagement Democratize Autonomous Discovery, 2018, DOI: 10.26434/
andvisualizationofX-raydiffractionspectrafromthinlm
chemrxiv.5953606.v1.
ternary composition spreads, Rev. Sci. Instrum., 2005, 76, 65 P. Nikolaev, D. Hooper, N. Perea-L´opez, M. Terrones and
| 062223. |     |     |     |     | B. Maruyama, |     | Discovery | of Wall-Selective |     | Carbon |
| ------- | --- | --- | --- | --- | ------------ | --- | --------- | ----------------- | --- | ------ |
48 C. J. Long, D. Bunker, X. Li, V. L. Karen and I. Takeuchi, Nanotube Growth Conditions via Automated
Rapid identication of structural phases in combinatorial Experimentation,ACSNano,2014,8,10214–10222.
| thin-lm |     |     | diffraction |     |     |     | On-the-y |     |     |     |
| -------- | --- | --- | ----------- | --- | --- | --- | --------- | --- | --- | --- |
libraries using X-ray and non-negative 66 A. G. Kusne, et al., machine-learning for high-
matrix factorization, Rev. Sci. Instrum., 2009, 80, 103902– throughput experiments: search for rare-earth-free
| 103906. |     |     |     |     | permanentmagnets,Sci.Rep.,2014,4,6367. |     |     |     |     |     |
| ------- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
49 J. M. Gregoire, et al., High-throughput synchrotron X-ray 67 R.D.King,etal.,TheAutomationofScience,Science,2009,
| diffraction | for | combinatorial | phase | mapping, | J. 324,85–89. |     |     |     |     |     |
| ----------- | --- | ------------- | ----- | -------- | ------------- | --- | --- | --- | --- | --- |
SynchrotronRadiat.,2014,21,1262–1268.
|     |     |     |     |     | 68 R. G´omez-Bombarelli, |     | et  | al., Automatic | Chemical | Design |
| --- | --- | --- | --- | --- | ------------------------ | --- | --- | -------------- | -------- | ------ |
50 R. T. Bell, et al., Lateral Temperature-Gradient Method for Using a Data-Driven Continuous Representation of
Molecules,ACSCent.Sci.,2018,4,268–276.
| High-Throughput |     | Characterization | of Material | Processing |     |     |     |     |     |     |
| --------------- | --- | ---------------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
Articial
by Millisecond Laser Annealing, ACS Comb. Sci., 2016, 18, 69 C. P. Gomes, B. Selman and J. M. Gregoire,
548–558. intelligence for materials discovery, MRS Bull., 2019, 44,
538–544.
| 51 H. Stein, | et  | al., A structure | zone diagram | obtained | by  |     |     |     |     |     |
| ------------ | --- | ---------------- | ------------ | -------- | --- | --- | --- | --- | --- | --- |
simultaneous deposition on a novel step heater: A case 70 T. R. Paudel, A. Zakutayev, S. Lany, M. d'Avezac and
study for Cu O thin lms, Phys. Status Solidi A, 2015, 212, A. Zunger, Doping Rules and Doping Prototypes in A BO
|            | 2   |     |     |     |                                                  |     |     |     |     | 2 4 |
| ---------- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
| 2798–2804. |     |     |     |     | SpinelOxides,Adv.Funct.Mater.,2011,21,4493–4501. |     |     |     |     |     |
52 M.Schwarting,S.Siol,K.Talley,A.ZakutayevandC.Phillips, 71 J.D.Perkins,etal.,Inversedesignapproachtoholedoping
Automated algorithms for band gap analysis from optical in ternary oxides: Enhancing p-type conductivity in cobalt
absorptionspectra,MaterialsDiscovery,2017,10,43–52. oxide spinels, Phys. Rev. B: Condens. Matter Mater. Phys.,
53 S. Mitrovic, et al., High-throughput on-the-y scanning 2011,84,205207–205208.
ultraviolet-visible dual-sphere spectrometer, Rev. Sci. 72 A. Zakutayev, Design of nitride semiconductors for solar
Instrum.,2015,86,13904. energyconversion,J.Mater.Chem.A,2016,4,6742–6754.
Identication
54 R. Zarnetta, et al., of Quaternary Shape 73 L. Yu, R. S. Kokenyesi, D. A. Keszler and A. Zunger, Inverse
Memory Alloys with Near-Zero Thermal Hysteresis and Design of High Absorption Thin-Film Photovoltaic Materials.
Unprecedented Functional Stability, Adv. Funct. Mater., Advanced Energy Materials, 2013, available at: https://
2010,20,1917–1923.
9648 | Chem.Sci.,2019,10,9640–9649 Thisjournalis©TheRoyalSocietyofChemistry2019

Minireview ChemicalScience
onlinelibrary.wiley.com/doi/abs/10.1002/aenm.201200538, 77 X.Jia,etal.,Nature,2019,573,251–255.
accessed:18thJuly2019. 78 I. M. Pendleton, G. Cattabriga, Z. Li, M. A. Najeeb,
74 P. F. Newhouse, et al., Discovery and Characterization of S. A. Friedler, A. J. Norquist, E. M. Chan and J. Schrier,
a Pourbaix-Stable, 1.8 eV Direct Gap Bismuth Manganate MRSCommun.,2019,9,846–859.
Photoanode,Chem.Mater.,2017,29,10027–10036. 79 S. Langner, et al., Beyond Ternary OPV: High-Throughput
75 B. Cantor, I. T. H. Chang, P. Knight and A. J. B. Vincent, Experimentation and Self-Driving Laboratories Optimize
Microstructural development in equiatomic Multi-ComponentSystems,arXiv:1909.03511[physics],2019.
multicomponentalloys,J.Mater.Sci.Eng.A,2004,375–377, 80 B. P. MacLeod, et al., Self-driving laboratory for accelerated
213–218. discovery ofthin-lmmaterials,arXiv:1906.05398 [cond-mat,
76 J. B. Kruskal, Nonmetric multidimensional scaling: physics:physics],2019.
anumericalmethod,Psychometrika,1964,29,115–129.
Thisjournalis©TheRoyalSocietyofChemistry2019 Chem.Sci.,2019,10,9640–9649 | 9649
.MA
71:31:2
6202/1/6
no
dedaolnwoD
.9102 rebmetpeS
02
no
dehsilbuP
.elcitrA
sseccA
nepO
.ecneciL
detropnU
0.3
noitubirttA
snommoC
evitaerC
a
rednu
desnecil
si
elcitra
sihT
View Article Online
