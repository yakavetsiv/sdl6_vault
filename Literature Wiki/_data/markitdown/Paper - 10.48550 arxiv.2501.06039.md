---
source_note: "Papers/Paper - 10.48550 arxiv.2501.06039.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/10.48550_arxiv.2501.06039.pdf"
converter: "microsoft/markitdown"
---
AI-powered virtual tissues from spatial proteomics for
clinical diagnostics and biomedical discovery
Johann Wenckstern 1,6,, Eeshaan Jain 1,6,, Kiril Vasilev2, Matteo Pariset2,
Andreas Wicki 3,4, Gabriele Gut 3,4, Charlotte Bunne 1,4,7
1SchoolofComputerandCommunicationSciences,EPFL,Lausanne,Switzerland,
2DepartmentofComputerScience,ETH,Zurich,Switzerland,
3DepartmentofMedicalOncologyandHematology,UniversityHospitalZurich,Zurich,Switzerland,
4UniversityofZurich,FacultyofMedicine,Zurich,Switzerland,
5SwissInstituteforExperimentalCancerResearch,SchoolofLifeSciences,EPFL,Lausanne,Switzerland.
6Theseauthorscontributedequally.
7Correspondenceto: charlotte.bunne@epfl.ch.
Abstract derstanding the spatial organization, composition and
function of the tumor microenvironment (TME) has
Spatialproteomicstechnologieshavetrans-
formed our understanding of complex tissue thus emerged as an important element for advancing
architecturesbyenablingsimultaneousanalysis cancer treatment.
of multiple molecular markers and their spa- Capturing complex tissue structure requires ad-
tial organization. The high dimensionality of vanced molecular imaging techniques that go beyond
thesedata,varyingmarkercombinationsacross traditional methods8.
experiments and heterogeneous study designs
The emergence of multiplexed imaging
poseuniquechallengesforcomputationalanaly-
technologies—including co-detection by indexing
sis. Here,wepresentVirtualTissues(VirTues),
(CODEX)9, imaging mass cytometry (IMC)10 and
afoundationmodelframeworkforbiologicaltis-
suesthatoperatesacrossthemolecular,cellular
multiplex immunohistochemistry (IHC)11—has revolu-
and tissue scale. VirTues introduces innova- tionizedourabilitytostudytheTMEbyenablinginsitu
tionsintransformerarchitecturedesign,includ- detection of multiple markers on a single slide12. IMC,
ing a novel tokenization scheme that captures in particular, can measure up to 150 target proteins at
bothspatialandmarkerdimensions,andatten- cellular and sub-cellular scales, serving as a crucial tool
tionmechanismsthatscaletohigh-dimensional
for precision oncology13 (Fig. 1a).
multiplex data while maintaining interpretabil-
Advancement in computational tools of multiplexed
ity. Trained on diverse cancer and non-cancer
tissue imaging data from patient tumors may provide
tissue datasets, VirTues demonstrates strong
generalizationcapabilitieswithouttask-specific three critical functions in clinical oncology: clinical di-
fine-tuning, enabling cross-study analysis and agnostics, e.g., the identification and characterization
novelmarkerintegration. Asageneralistmodel, of tumors, biological discovery, e.g., understanding
VirTuesoutperformsexistingapproachesacross disease mechanisms and therapy responses, and clini-
clinicaldiagnostics,biologicaldiscoveryandpa- cal decision support through retrieval of comparable
tient case retrieval tasks, while providing in- patient cases for molecular tumor boards14 (Fig. 1a).
sights into tissue function and disease mecha-
The complexity of multiplexed data, characterized by
nisms.
immensescaleandhighlynon-linear,context-dependent
relationships between molecular markers, necessitates
Introduction AI methods for meaningful pattern interpretation and
prediction15.
Tissues, particularly in cancer, display pronounced het- To achieve this, we present Virtual Tissues, an arti-
erogeneity across patients, disease stages and even ficial intelligence (AI)-driven foundation model frame-
within individual tumors—evident in diverse cell pheno- work for representing biological tissues from spatial
types, states and spatial organization1. Accounting for proteomics data. Trained on diverse datasets covering
this heterogeneity is critical: tumor development and breast13,17, lung18 and melanoma19 tissues and eval-
responsetotherapydependnotjustoncancercells,but uated via zero-shot inference on diabetic pancreatic
on their complex interactions with their surrounding en- tissue20, VirTues achieves strong performance across
vironment. Differentcellphenotypesmayactaspromot- variousclinicalandbiologicaltaskswithouttask-specific
ers or suppressors of tumor development and progres- training. Importantly, it can generate virtual tissue rep-
sion, depending on the biological context2,3, with their resentations of new cancer types or diseases without
spatial co-occurrence patterns predicting immunother- fine-tuning, while maintaining robustness to dataset-
apy response4,5, disease relapse6 and survival7. Un- specific artifacts.
1
5202
naJ
01
]MQ.oib-q[
1v93060.1052:viXra

| a.  | diagnostics via     |     | Virtual Tissues |     |     | d. e.g., multiplex images |     |     |     |     |     |
| --- | ------------------- | --- | --------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
|     | spatial proteomics  |     |                 |     |     | Histone H3                |     |     |     |     |     |
FOXP3
|         | (e.g. IMC, CODEX, 4i) |     |     | prediction tasks |     | CD10 |     |     |      |     |     |
| ------- | --------------------- | --- | --- | ---------------- | --- | ---- | --- | --- | ---- | --- | --- |
| patient |                       |     |     |                  |     |      |     |     | crop |     |     |
clinical diagnostics
|     | tissue |     |     | therapy selection  |     |     |     |            |     |     |     |
| --- | ------ | --- | --- | ------------------ | --- | --- | --- | ---------- | --- | --- | --- |
|     |        |     |     | outcome prediction |     |     |     | processing |     |     |     |
Virtual Tissues
|                    | m ul ti p e | x   Representation |     | b io l o g ic a l  d i s       | c o v e ry  |                 |         |          |       |        |              |
| ------------------ | ----------- | ------------------ | --- | ------------------------------ | ----------- | --------------- | ------- | -------- | ----- | ------ | ------------ |
|                    | im a g e    | s                  |     |    u n d e rs t a n d i        | n g  o f    |                 |         | É        |       |        | É            |
|                    |             |                    |     | biological tissues             |             | y               |         |          | É     |        |              |
|                    |             |                    |     | across the cell,   niche and   |             |                 |         |          |       |        | noitazinekot |
|                    |             |                    |     | tissue level                   |             |                 |         | markers  | patch |        |              |
|                    |             |                    |     |                                |             | x               |         |          |       | image  |              |
|                    |             | Virtual Tissues    |     | information                    |             | space           | ~40     |          |       | tokens |              |
|                    |             | Database           |     | retrieval                      |             |                 |         |          |       |        |              |
| reference patients |             |                    |     |                                |             |                 |         | marker   |       |        |              |
|                    |             |                    |     |                                |             | level ralucelom | marker  | tokens   |       |        |              |
epitopes
|     |                 |     |     |     |                         | É   |                | protein   |        |         |     |
| --- | --------------- | --- | --- | --- | ----------------------- | --- | -------------- | --------- | ------ | ------- | --- |
| b.  | Distribution    |     |     |     |                         |     | language model |           | fusion | srekram |     |
|     | over markers    |     |     |     | c lin i c a l           |     |                |           |        |         |     |
|     | across datasets |     |     |     | decis io n   s u p port |     |                |           |        |         |     |
|     |                 |     |     |     |                         |     |                | É         |        | space   |     |
level ralullec
|     |     |     |     |     |     |     | VirTues  |     | VirTues  |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- |
|     |     |     |     |     |     |     | Encoder  |     | Decoder  |     |     |
cell summary tokens
|     |     |     | 41 markers |     |     |     |     |     |                     |     | erutcetihcra seussiT lautriV |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | ------------------- | --- | ---------------------------- |
|     |     |     | 38 markers |     |     |     |     |     | Sparse Transformer  |     |                              |
blocks of VirTues Encoder
|     |     |     | 35 markers |     |     | level ehcin |             |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | ----------- | ----------- | --- | --- | --- | --- |
|     |     |     | 35 markers |     |     |             | aggregation |     |     |     |     |
marker
|     |     |     |     |     |     | niche summary tokens |     |     | attention |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --------- | --- | --- |
level eussit
aggregation
spatial
attention
tissue summary token
|     |     |     |     |     | e.  |     |     | Virtual Tissues |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
Scaling laws w.r.t. compute and performance
CA-MAE
primary lung cancer tissue (Cords et al., 2023) (Kraus et al., 2024)
| primary and metastatic melanoma cancer tissue (Hoch et al., 2022) |     |     |     |     | Compute cost |     |     | Cancer type |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | ----------- | --- | --- | --- |
Cell type
primary breast cancer tissue (Danenberg et al., 2022) No. of parameters full attention
primary breast cancer tissue (Jackson et al., 2020)
c.
|     | 2062     |     | 3470    | 8.5 million  |                           |     |     |                           |     |     |     |
| --- | -------- | --- | ------- | ------------ | ------------------------- | --- | --- | ------------------------- | --- | --- | --- |
|     | patients |     | samples | cells        | Number of marker channels |     |     | Number of marker channels |     |     |     |
Figure1: OverviewoftheVirtualTissuesplatform. a,FlowchartdepictingVirTuescapabilities. VirTuesmapshighlymultiplexed
imagesoftissuesamplestovirtualtissuerepresentationsusefulforclinicalandbiologicalpredictiontasksatcell,nicheandsample
level. Adatabaseofvirtualtissuerepresentationspermitsretrievalofsimilartissuesamplesforclinicaldecisionsupport. b,VirTuesis
trainedonfourIMCdatasetsoftumorsandtheirmicro-environmentsoriginatingfromlung,breastandmelanomacancer,containing
96distinctproteinandmRNAmarkersintotal. c,Sizesofdatasetsintermsofpatients,biopsysamplesandcells. d,Multiplexed
imagesareprocessedcrop-wiseinto3Dgridsofimagetokens,representingpatchesofeachmarkerateachposition. Markertokens,
derivedfromaproteinlanguagemodel,arefusedwiththerespectiveimagetokensusingalinearprojectionandaddition. VirTues
isanovelvisiontransformerarchitecturetrainedwithamaskedautoencodingobjective. Inputtokensareconcatenatedwithcell
summarytokens,whichareinitializedwithlearnableweights. Duringinference,VirTues’encoderprocessesthissetoftokens. The
encodedcellsummariesaresubsequentlyaggregatedtonicheandtissuesummarytokens. Fortraining,arandomsubsetoftokens
isindependentlyselectedandmaskedforeachchannel. VirTues’decoderpredictschannel-wisereconstructionsreceivingasinput
theencoded,non-maskedtokensfromthetargetchannelalongwithallcellsummarytokens. Encodedcellsummarytokensare
aggregated to niche and niche to tissue summary tokens. VirTues encoder uses sparse attention mechanisms restricting direct
tokeninteractionstoeitherpositions(markerattention)orchannels(spatialattention). e,Comparisonofcomputationalcostand
predictionperformancebetweenchannel-agnosticmaskedauto-encoder(CA-MAE16)andVirTuesasafunctionofthenumberof
utilizedmarkers.
Recent foundation models in digital pathol- Second, every experiment may record a set of
different
ogy21,22,23 and cellular microscopy16,24,25,26 (such as markers,requiringarchitecturesthatscaleanddealwith
CellPainting data27), have established vision transform- flexible inputs of potentially never-measured markers
ers (ViT)28 as the predominant architecture for ana- and their distribution within cells and tissues (Fig. 1b).
lyzing spatial biomedical data. However, neither these Lastly, multiplex tissue imaging remains costly, result-
transformer-based approaches nor CNN-based meth- ing in fewer, often smaller datasets. The relative data
ods7 adequately address the unique challenges inher- scarcity necessitates models that can robustly general-
ent in multiplex imaging data: First, multiplex images izeacrossdiversestudycontextsandincorporatefuture
are high-dimensional—instead of the three-dimensional patient cohorts while maintaining reliable performance
| RGBformatofH&Eslices,theseimagesoftencomprise |      |             |     |                  |            | (Fig. | 1c). |     |     |     |     |
| --------------------------------------------- | ---- | ----------- | --- | ---------------- | ---------- | ----- | ---- | --- | --- | --- | --- |
| more                                          | than | 40 channels | of  | intensity values | indicating |       |      |     |     |     |     |
the presence of different protein or RNA molecules. Followingthevisionofconstructingmulti-scalefoun-
|     |     |     |     |     |     | dation | models | for biology29, | VirTues | provides | new in- |
| --- | --- | --- | --- | --- | --- | ------ | ------ | -------------- | ------- | -------- | ------- |
2

novations in AI architecture development: Its success and proteomics: by combining protein language model
stems from its transformer architecture that respects embeddings with spatially-patched channel information
biological hierarchy across multiple scales, providing and learnable cell summary tokens, we enable flexible
representations and insights into tissue function. At processing of variable marker combinations while incor-
the molecular level, it is powered by protein language porating biological meaning and subcellular spatial dis-
models (PLM) trained on the entire protein data bank tributionof markers (Fig.1d, detailsin Methods). This
(PDB), enabling it to capture complex relationships be- multi-scaledesign29,34enablestheintegrationofhetero-
tween protein markers, distinguish the semantic mean- geneous datasets containing different marker combina-
ings of different markers, and generalize to previously tions (Fig. 1b), as demonstrated across lung cancer18
unseen markers. Through hierarchical internal repre- (41 markers), melanoma19 (38 markers) and breast
sentations spanning cellular, niche, and tissue levels30, cancer tissues17,13 (35 markers each). These datasets
combined with its novel attention mechanism (Fig. 1d), show substantial variation in cohort sizes (2,062 to-
VirTuesachievesbiologicalinterpretabilitybyidentifying tal patients), cell counts (8.5 million total cells) and
the specific tissue regions and biomarkers driving each samples (3,470 total images) across different cancer
prediction. This interpretability is crucial for clinical ap- types(Fig.1c). WealsonotethatVirTues’designdoes
plications and provides deeper insights into underlying not provide a network architecture for biological vision
biological mechanisms. foundation models simply due to its ability to scale:
VirTues is a generalist model: Contrary to existing While modality-agnostic architectures used in previous
tools, VirTues is the model able to tackle a wide methods do not profit from providing richer biological
first
range of prediction and retrieval tasks across cell, niche features, VirTues’ performance scales with increasing
and tissue levels, while consistently outperforming all number of markers, as demonstrated on a task on the
baselines and demonstrating emergent capabilities for cellularlevel(i.e., celltypeclassification)andthetissue
embedding unseen markers, patients and diseases. level (i.e., cancer type) (Fig. 1e).
TheVirtualTissuesframeworkisbasedonamasked
|     |     |     |     |     |     |     | autoencoder | (MAE) | architecture35. |     |     | The VirTues | En- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --------------- | --- | --- | ----------- | --- |
Results
|         |        |             |     |     |           |     | coder and     | Decoder        | are        | trained   | in an unsupervised |        | fash-     |
| ------- | ------ | ----------- | --- | --- | --------- | --- | ------------- | -------------- | ---------- | --------- | ------------------ | ------ | --------- |
|         |        |             |     |     |           |     | ion through   | reconstructing |            | partially |                    | masked | marker-   |
| A novel | vision | transformer |     | to  | construct | AI- |               |                |            |           |                    |        |           |
|         |        |             |     |     |           |     | space tensors | (Fig.          | 2, details | in        | Methods).          |        | Multiplex |
powered Virtual Tissues imaging data provide information at a subcellular reso-
|     |     |     |     |     |     |     | lution and | thus | provide | the foundation |     | for tissue | under- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------- | -------------- | --- | ---------- | ------ |
Apivotalcharacteristicoffoundationmodelsistheirabil-
|     |     |     |     |     |     |     | standing | on the | cell, niche | and | tissue | level. | To allow |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | --- | ------ | ------ | -------- |
itytoleveragelargerandmorediversetrainingdatasets
|     |     |     |     |     |     |     | for downstream |     | predictions | across | all | biological | tissue |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ------ | --- | ---------- | ------ |
inordertoachievesuperiorperformanceacrossmultiple
scales,VirTuesgeneratescell,nicheandtissuesummary
| downstream                        | tasks.        | Importantly, |       | the        | current | state          | of             |       |                 |     |                 |               |        |
| --------------------------------- | ------------- | ------------ | ----- | ---------- | ------- | -------------- | -------------- | ----- | --------------- | --- | --------------- | ------------- | ------ |
|                                   |               |              |       |            |         |                | tokens that    | serve | as hierarchical |     | and multi-scale |               | tissue |
| vision transformers16,24,25,26,31 |               |              |       | developed  |         | for biological |                |       |                 |     |                 |               |        |
|                                   |               |              |       |            |         |                | representation |       | used across     | a   | variety         | of downstream |        |
| imaging                           | face several  | limitations  |       | when       | applied | to mul-        |                |       |                 |     |                 |               |        |
|                                   |               |              |       |            |         |                | tasks (Figs.   | 3 and | 4, details      | in  | Methods).       |               |        |
| tiplexed                          | biomedical    | data         | (Fig. | 1e).       | First,  | the current    |                |       |                 |     |                 |               |        |
| architectures’                    | computational |              |       | complexity | scales  | quadrat-       |                |       |                 |     |                 |               |        |
ically with both spatial dimensions and number of Virtual Tissues understand tissue architec-
channels, makingthemimpracticalforhigh-dimensional tures and relations between markers
| spatial data. | Second, | their | token-based |     | representations |     |     |     |     |     |     |     |     |
| ------------- | ------- | ----- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
typicallytreatallchannelsequally,failingtocapturethe To evaluate VirTues’ understanding of tissue architec-
distinct ones and filter out the potentially redundant ture, we challenge its ability to reconstruct tissues
biological information of different markers. Third, they masked in three different ways of increasing difficulty:
lackexplicitmechanismsforintegratingdifferingmarker (1) independent masking, where independently for each
combinations across experiments or for incorporating marker patches are masked at random spatial locations
prior knowledge about protein interactions. (Figs. 2a,b), (2) marker masking, where all patches of
We specifically design VirTues to overcome the a single marker are masked (Figs. 2c,d) and (3) niche
identified challenges and introduce a purpose-built ViT masking, where patches across all markers are masked
model for multiplexed imaging. By disentangling trans- at randomly selected spatial locations (Figs. 2e,f).
former’sattentionmechanism32,33 intomarkerandspa- In the independent masking experiments, VirTues
tial attention components, VirTues not only enables successfully reconstructs masked regions across mark-
training on images with hundreds of channels, but also ers, e.g., CAV1, FOXP3, H3 in Fig. 2b in lung cancer
learns to distinguish between the spatial distribution tissue18 and KRT14, panCK, Twist in breast cancer
and composition of cells that determine the molecular samples17, preserving both spatial distribution and in-
profile of a tissue as well as the relation and inter- tensity patterns (Suppl. Figs. 1, 2, 3, 4 for results
action between protein and RNA markers. Another on further channels of all datasets18,19,17,13). This
critical innovation in VirTues is the introduction of a demonstrates the model’s ability to leverage contextual
new tokenization scheme for spatial transcriptomics information across both spatial and marker dimensions.
3

| a.VirTues captures tissue organization | b.  |     |
| -------------------------------------- | --- | --- |
primary lung cancer tissue
H3
FOXP3
| CAV1 |  tnednepedni |     |
| ---- | ------------ | --- |
gniksam
independent
| masking         | VirTues |                              |
| --------------- | ------- | ---------------------------- |
| across markers  |         | primary breast cancer tissue |
| and space       | H3      |                              |
FOXP3
| CAV1 |  tnednepedni |     |
| ---- | ------------ | --- |
gniksam
c.
| VirTues reconstructs fully masked  | d.  |     |
| ---------------------------------- | --- | --- |
markers by learning biological
| relationships across markers |     | primary lung cancer tissue |
| ---------------------------- | --- | -------------------------- |
PDGFRB
CD248
CD68
 rekram gniksam
primary breast cancer tissue
| masking of   | VirTues |     |
| ------------ | ------- | --- |
entire marker
across entire space
CD248 PDGFRB
| CD68 |     | gniksam |
| ---- | --- | ------- |
 rekram
| e. VirTues recovers fully masked         | f.  |                            |
| ---------------------------------------- | --- | -------------------------- |
| niches by understanding tissue structure |     | primary lung cancer tissue |
MMP9
H3
CAV1
gniksam
 ehcin
| masking of   | VirTues | primary breast cancer tissue |
| ------------ | ------- | ---------------------------- |
entire niche
| across all markers  | MMP9 |     |
| ------------------- | ---- | --- |
H3
CAV1
gniksam
 ehcin
g.
primary lung cancer tissue primary breast cancer tissue primary breast cancer tissue primary and metastatic melanoma cancer tissue
| indep. | marker niche |     |
| ------ | ------------ | --- |
Figure2: VirtualTissuesunderstandtissuearchitectureandmarkerrelationships. a,Illustrationofindependentmasking. Tokensof
eachchannelaremaskedindependentlywithachannel-wiserandommaskingratiorangingfrom60%to100%. b,Examplesof
reconstructionresultsusingindependentmasking. c,Illustrationofmarkermasking. Onemarkerischosenandalltokensofits
channelaremaskedwhileallotherchannelsremainunmasked. d,Examplesofreconstructionresultsusingmarkermasking. Each
rowdepictstheinpaintingofdifferentchannelsforthesametissuesample. e,Illustrationofnichemasking. Asubsetofpositionsis
chosenandalltokensacrossmarkersaremaskedatthesepositions. f,Examplesofreconstructionresultsusingnichemasking. Each
rowdepictsthenichereconstructionsofdifferentchannelsofthesametissuesample. g,Overviewofmarker-wisereconstruction
errorsfordifferentdatasetsandmaskingstrategies. Contrarytothetrainingobjective,thereconstructionerrorisonlycomputedfor
maskedtokens.
For marker reconstruction (Fig. 2c,d), we com- channels of all datasets18,19,17,13), indicating its ability
pletely mask individual markers across the entire space. to learn biological relationships between different mark-
VirTues accurately recovers the expression patterns of ers. Since with marker masking the VirTues Decoder
maskedmarkers(e.g., CD68, CD248, PDGFRBinlung receives only the encoded cell summary tokens as in-
cancer18 and CD68, CK19, Sox9 in breast cancer tis- put, its ability to decode a channel absent from the
sue17, Suppl. Figs. 5, 6, 7, 8 for results on further encoder’s input further demonstrates that the cell sum-
4

mary tokens generated by VirTues effectively capture a is pre-trained on ImageNet, where each channel is em-
meaningful and robust representation of the molecular bedded separately and reduced to 16 dimensions with
tissue architecture. PCA. While CA-MAE16 is able to conduct predictions
In niche-level experiments (Figs. 2e,f), we mask across different tasks on all scales (cell, niche and
entire tissue regions across all markers. The model tissue level), ResNet7’s architecture is restricted to
successfully reconstructs complex tissue architectures, niche and tissue level tasks, since it aggregates spatial
recovering marker patterns (e.g., CAV1, H3, MMP9 in information directly into niche-level embeddings.
lungcancer18 andc-Myc,CD31,Twistinbreastcancer Importantly—and a critical property of founda-
tissue17,Suppl. Figs.9,10,11,12forresultsonfurther tion models—the performance on such downstream
channels of all datasets18,19,17,13) while maintaining bi- tasks increases when trained on a large collection of
ological plausibility. Quantitative evaluation in terms of datasets, here demonstrated for an exemplary down-
the average mean squared error (MSE) across different stream task on the Danenberg et al.13 patient co-
markers, cancer types and masking strategies (Fig. 2g) hort when comparing the VirTues platform with a
shows robust reconstruction capability with significant VirTues Encoder/Decoder pair trained on the Danen-
improvements over the reconstructions based on pre- berg et al.13 dataset only (Fig. 3d).
dicting the mean channel intensity of all visible patches
Identifying the cell types in a tissue sample offers
(Suppl. Fig. 13).
critical insights into its functional dynamics and cellular
makeup. Moreover, it helps in dissecting the complex
interactions between different cell types within a TME,
Performing biological discovery and clini-
which can help guiding systemic therapies geared to-
cal diagnostics tasks across the scales of
wardsthetumorenvironment(suchasimmunotherapy),
biology
treatments targeting the tumor cells themselves, and
ultimately refine a broad range of systemic anti-cancer
VirTuesenablescomprehensiveanalysisoftissuesacross
treatment regimens. For instance, we can gauge the
biological scales through a unified framework (Figs. 3a-
strength of immune response through the high pres-
c). At the cellular level, cell summary tokens support
ence of tumor-infiltrating lymphocytes38, or adjust
tasks such as cell type classification. Niche summary
treatments to target tumor- or resistance-promoting
tokens facilitate tissue structure analysis, while tissue
stroma39.
summary tokens enable clinical diagnostics like the pre-
diction of cancer type and grade. This unified multi- At the cellular level (Fig. 3e), VirTues outperforms
scale approach is particularly powerful as it allows pre- baseline methods in cell type multi-class classification
dictions and queries across the inherent hierarchical for both breast cancer (distinguishing stromal, ER+,
organization of biological tissues, where molecular and NK, ER-, B cell, myeloid and T cell populations) and
cellular patterns inform higher-level tissue structures lung cancer tissues (tumor, immune, fibroblast, T cell
that ultimately contribute to clinical outcomes. and vessel cells). The cell type classification tasks are
For biological discovery tasks at the cellular level, affected by significant class imbalance (see Fig. 28 for
we employ logistic regression on the encoded cell sum- the test set distribution). For instance, NK and B
mary tokens (Fig. 3a), a common practice referred to cells are severely underrepresented in the breast cancer
as linear probing, which measures discriminative perfor- dataset, while vessel and T cells are underrepresented
mance and the representation quality of a foundation in the lung cancer dataset. Despite this, the model
model encoder36. For niche and tissue level tasks, we demonstrates particular strength compared to base-
learn niche and tissue summary tokens (Fig. 1d) using lines in identifying rare cell populations, maintaining
attention-based multiple instance learning (ABMIL)37 robust performance across varying cell type frequencies.
on the cell summary tokens which enables addressing Additional classification results for fine-grained, highly-
biological discovery and clinical diagnostic tasks on in- imbalancedcelltypesonCordsetal.18 showconsistent
dividual niches and tissue of patients (for details see trends (see Suppl. Figs. 16 and 29 for results and
Methods, Fig. 3b,c). support distribution).
VirTues consistently outperforms other pretrained Forbreastcancertissue,VirTuesachievesF1-scores
encoders and vision transformers16,24 trained unsuper- of 0.55 for stromal cells and 0.49 for ER- cells, sur-
vised on multiplex images (Fig. 3), across all cell, niche passing CA-MAE16 by 4.94% and 18.27% respectively.
and tissue level tasks performed on breast13 and lung The performance advantage is even more pronounced
cancertissue18 (seeSuppl. Fig.14foradditionalresults for rare cell types such as NK and B cell, which cover
onJacksonetal.17). Specifically,webenchmarkagainst only 1.17% and 3.27% of the test set. We first notice
CA-MAE1616 and ResNet77 as they represent the cur- that VirTues is able to achieve an F1-score of 0.51
rent state-of-the-art architectures for cellular imaging for NK, while CA-MAE16 fails to identify any NK cell.
data, respectively (for additional baselines, see Suppl. In case of B cells, VirTues achieves an F1-score of
Fig. 15). CA-MAE16 follows the vision transformer ar- 0.41,surpassingCA-MAE16 by66.26%. Inlungcancer
chitecture, however, it features a common encoder and analysis, VirTues maintains its superior performance,
separate decoders for each multiplex channel. ResNet7 achievingF1-scores of0.91 for tumorcells and0.75for
5

| a.  | cellular level |     | b.  | niche level | c.  | tissue level | d.  |
| --- | -------------- | --- | --- | ----------- | --- | ------------ | --- |
trained on
Biological discovery and clinical diagnostics   cell summary tokens Danenberg et al., 2022
| across biological scales |     |     |     |     |     |     | trained on all 0 |
| ------------------------ | --- | --- | --- | --- | --- | --- | ---------------- |
multiplex images
f r o m   p ri m a ry   b re a s t   V ir t u a l  T is s u e   b i o lo g i c a l  a tt e n t i o n - b a s e d   b i o lo g i c a l  a tt e n t i o n - b a s e d   c l i n ic a l
a n d  l u n g  c a n c e r  ti s s ue R e p r e s e n ta t io n d i sc o v e r y in s d t e a e n p c   e m  l u e l a t i r p n l e in   g   d i sc o v e r y d e e p   m u l t i p l e     d i a g n o s tics
|     |     |     |     |     | in s t a n c | e  l e a r n in g |     |
| --- | --- | --- | --- | --- | ------------ | ----------------- | --- |
e.g., cell type
| 0Virtual Tissues |     |               |     |               |     | e.g., prediction of   |     |
| ---------------- | --- | ------------- | --- | ------------- | --- | --------------------- | --- |
|                  |     | and category  |     | e.g., tissue  |     | cancer grade, type,   |     |
C A - M A E   cell   su m m ary  classification, etc.  s tr u c t u re   relapse, etc.
| (K ra u s  e t a l., 2024) | t o ke n | s linear  | n ic he       |                  | ti ss u       | e       |     |
| -------------------------- | -------- | --------- | ------------- | ---------------- | ------------- | ------- | --- |
| ResNet                     |          | probing   | su m m a r y  | id e n t if ic a | tion,  su m m | a r y   |     |
| (Sorin et al., 2023)       |          |           | token         | etc.             | token         |         |     |
e. primary breast cancer tissue (Danenberg et al., 2022) f. primary breast cancer tissue g. primary breast cancer tissue (Danenberg et al., 2022)
primary lung cancer tissue (Cords et al., 2023) primary lung cancer tissue (Cords et al., 2023)
h. Cell type  Spatial attention  i. Spatial attention  Cell type  Marker attention
annotation of VirTues Encoder of VirTues Encoder annotation of VirTues Encoder
Tumor cells V ir T u e s
Impor ta n c e   S core
Fibroblasts
Immune cells
T cells
Vessel cells
Other
cancer type
| Adeno-    |     |            | attention | Squamous       |     |     |     |
| --------- | --- | ---------- | --------- | -------------- | --- | --- | --- |
| carcinoma |     |            |           | cell carcinoma |     |     |     |
|           |     | Tumor cell | low high  |                |     |     |     |
Figure3: Multi-scalebenchmarkanalysisandinterpretabilityoftheVirtualTissuesEncoder. a-c,Methodsandtaskstoevaluate
VirTues’representationsacrossbiologicalscales. a,Cellularlevelevaluation. Weclassifycelltypesandcategoriesfromindividualcell
summarytokensusinglogisticregression. b,Nichelevelevaluation. Wedetectmulticellulartissuestructuresfromcellsummary
tokens of the niche using attention-based multiple instance learning (ABMIL). c, Tissue level evaluation. We predict clinical
patientfeaturesfromcellsummarytokensoftheentiretissueusingABMIL.d,ComparisonofF1-scoresforcelltypeclassification
betweenVirTuestrainedanallfourcancerdatasetsandVirTuestrainedonlyonDanenbergetal.13. e-g,Comparisonofprediction
performanceofVirTues,CA-MAE16 andResNet7 acrossscales. ResNet7 yieldsonlyrepresentationvectorscorrespondingtoentire
nichesandisthereforenotevaluatedforcell-leveltasks. Forniche-leveltasks,ResNet7’srepresentationsareevaluatedusinglogistic
regressionandfortissue-leveltasksusingABMIL.e,RecallandF1-scoresforcelltypeclassificationonDanenbergetal.13 and
Cordsetal.18. f,Accuraciesandmacro-averagedF1-scoresfortissuestructuredetectiononDanenbergetal.13. g,Accuraciesand
macro-averagedF1-scoresfortissue(orpatient)levelfeaturepredictiononDanenbergetal.13 andCordsetal.18. h,Visualization
ofspatialattentionmaps. Tocomputetheattentionscores,weintegratedanadditionalclasstokenintoVirTues’architecturewhich
canattendtoallcellsummarytokensandwefine-tunedthisextendedmodelonthecancertypeprediction. Thedepictedattention
scorescorrespondtotheattentionscoresofthisclasstoken. i,Visualizationofmarkerattentionfordifferenttissueregions. We
selectedthreetissuenicheswithdistinctcelltypecompositionsandvisualizedthefivemarkersthataremostattendedtobyother
markersafteraveragingattentionscoresacrosstheseregions.
immune cells, representing improvements of 4.05% and immune cell organization similar to tertiary lymphoid
48.83% over CA-MAE16 respectively. For the challeng- structures; and PDPN+ regions represent areas of ac-
ing and underrepresented vessel cell identification task, tive stroma. The structures present within the niches
VirTues achieves an F1-score of 0.36, outperforming oftheTMEoftenrecuracrosstumors13 andidentifying
the baseline by a significant margin of 324.38%. such structures gives insights into the functional state
|              |       |                    |              | of the | TME providing | prognostic | value. |
| ------------ | ----- | ------------------ | ------------ | ------ | ------------- | ---------- | ------ |
| At the niche | level | (Fig. 3f), VirTues | demonstrates |        |               |            |        |
robust performance in identifying multicellular tissue For suppressed expansion regions, binary classifica-
structures as defined by the respective authors of the tion based on VirTues learned representation achieves
studies including suppressive expansion, tertiary lym- an accuracy of 0.85, surpassing CA-MAE16 by 4.11%
phoid structures (TLS)-like regions, PDPN+ regions. (P < 0.006), and ResNet7 by 3.45% (P < 0.005).
These regions reflect distinct cellular compositions and TheVirTues-basedmodelmaintainsstrongperformance
functionalstates: suppressiveexpansionregionscontain across other tissue structures, with accuracies of 0.81
regulatory T cells and PD-1-expressing cells indicating for TLS-like regions and 0.78 for PDPN+ regions, con-
immune suppression; TLS-like regions show complex sistently outperforming CA-MAE16 by 15.01% (P <
6

0.006)and11.49%(P<0.005),andResNet7by7.28% Spatial and marker attention provides ex-
(P < 0.005) and 4.24% (P < 0.005) for TLS-like and plainability of algorithmic decisions
PDPN+ respectively.
VirTues provides interpretable insights into its decision-
making process through spatial and marker attention
Akin to a pathologist, AI models should evaluate mechanisms (Fig. 3h,i). Importantly, the newly intro-
tissue characteristics comprehensively for robust clini- duced attention scheme allows to disentangle the influ-
cal classifications and predictions. The model’s tissue ence of spatial regions and markers that are critical for
level predictions (Fig. 3g) show particularly strong per- analgorithmicdecision—anabilitynootherarchitecture
formance in critical clinical tasks such as ER status possesses.
determination, tumor grade classification and PAM50
Here highlighted for adenocarcinoma (Fig. 3h) and
subtyping in breast cancer, as well as the prediction
squamous cell carcinoma samples (Fig. 3i), spatial at-
of cancer type, cancer relapse and grade classification
tention maps reveal the influence of distinct cellular
in lung cancer. ER status indicates estrogen recep-
neighborhoods and the tumor architecture on the pre-
tor presence, affecting treatment response. Tumor
dictions of clinical properties. When classifying a pa-
grade reflects cancer cell differentiation and growth
tient’scancertype,forexample,thespatialattentionof
rate. PAM50 subtyping classifies breast cancers into
VirTues’ Encoder is high on tumor cell regions through-
intrinsicsubtypes(LuminalA/B,HER2-enriched,Basal-
out the tissue.
like, Normal-like), guiding treatment strategies. In lung
Marker attention analysis, on the other hand, pro-
cancer, accurate cancer type classification (e.g., ade-
vides insights into the relative importance of different
nocarcinoma vs. squamous cell carcinoma) and grade
RNAs and proteins in algorithmic decisions. This anal-
assessment are crucial for treatment planning and prog-
ysis can be conducted across the entire tissue or in
nosis.
spatial regions of interest, e.g., for tissue niches that
are rich in tumor cells, a fibroblast neighborhood or the
tumor immune microenvironment (TIME) (Fig. 3i). To
For breast cancer, VirTues representations achieve
quantify the importance of a marker for the generated
accuracies of 0.89 for ER Status and 0.68 for cancer
representation, we showcase the importance scores per-
grade prediction, representing improvements of 7.26%
ceived by VirTues, which signifies the relative marker
(P < 0.005) and 32.16% (P < 0.005) over CA-MAE16,
attention scores learned by VirTues for the region of
and 1.88% (P < 0.199) and 8.86% (P < 0.02) over
interest (see Methods for details).
ResNet7 respectively. Similarly, in lung cancer analy-
Whenanalyzing animmune-cell infiltratedtumorre-
sis, the model demonstrates superior performance in
gionofsquamouscellcarcinoma,forexample,themodel
cancer type prediction (0.87 accuracy, 11.72% over
assigns high importance to tumor cell markers panCK
CA-MAE16 (P < 0.006) and 4.36% over ResNet7 (P
and MMP11 and immune cell markers CD45RA and
< 0.005)) and cancer grade prediction (0.63 accuracy,
CD10. panCKisapositivemarkerforcarcinomasofep-
16.21% over CA-MAE16 (P < 0.006), and 5.37% over
ResNet7 (P<0.005)). Importantly, sometasksexhibit
ithelialorigin44. Matrixmetalloproteinase-11(MMP11)
is secreted by stromal cells in the tumor microenvi-
a high class imbalance, e.g., ER Status and PAM50
ronment, and its overexpression correlates with tumor
(see Suppl. Fig. 30 for details).
aggressiveness by inhibiting apoptosis and promoting
the migration and invasion of cancer45. CD45RA is
A common strategy to deal with the high- expressed on naive T and B cells46, while CD10 is pri-
dimensionality of multiplex images is to project image marily found on early B lymphocytes and certain T cell
channels that contain measurements of different mark- subsets47, making both proteins reliable markers for
ersontoalower-dimensionalmanifold40,subsetmarkers identifying specific immune cell populations within the
or features41 or to summarize all markers into a single tumor and its microenvironment.
value per pixel42,43. However, such approaches risk los- Regions of the tissue mostly populated by fibrob-
ing crucial marker-specific patterns and biological rela- lasts with interspersed immune cells show high atten-
tionshipsthatareessentialforunderstandingtissueorga- tion weights for both stromal and immune markers.
nization and function. VirTues’ marker attention mech- Vimentin (VIM) and smooth muscle actin (SMA) are
anismtakesafundamentallydifferentapproachbymain- canonical markers for fibroblasts and myofibroblasts48,
taining the full biological dimensionality while learning while Collagen I is associated with extracellular ma-
toattendtorelevantmarkercombinationsinacontext- trix production and stromal cell activation49. CD248
dependent manner. This allows the model to capture (endosialin)expressionincanceriscomplexandcontext-
complex marker interactions and their spatial distri- dependent —while it is found on fibroblasts and peri-
butions, preserving biological interpretability while effi- cytesinhealthytissue,itsexpressionpatternandcellular
cientlyhandlingthehigh-dimensionalnatureofmultiplex localization can vary significantly between different car-
data. See Suppl. Fig. 15 for comparison against trans- cinomas50. Fittingly, its role in this region may reflect
former architectures operating on compressed images. stromal components of the TIME.
7

Vessel cells
a. d. Incoming Patients Results of the Virtual Tissues Database Tumor cells Immune cells
|     |     |     |     |     | Fibroblasts | T cells Other |     |
| --- | --- | --- | --- | --- | ----------- | ------------- | --- |
Virtual Tissues
Representation
clinician
 noitisopmoc epyt lleC
| patient query | niche  summary  clinical  |     |     |     |     |     |     |
| ------------- | ------------------------- | --- | --- | --- | --- | --- | --- |
tokens decision
support
Virtual Tissues
Database
clinical  records
|     |     | Squamous Cell Carcinoma  |                          | Squamous Cell Carcinoma  |     | Squamous Cell Carcinoma  |     |
| --- | --- | ------------------------ | ------------------------ | ------------------------ | --- | ------------------------ | --- |
|     |     | Grade 2                  | Squamous Cell Carcinoma  | Grade 3                  |     | Grade 3                  |     |
|     |     | No LN. Metastases        | Grade 3                  | No LN. Metastases        |     | No LN. Metastases        |     |
retrieved archival patients  No Relapse LN. Metastases  Relapse No Relapse Relapse
with similar tissue phenotype
| Virtual Tissues | CA-MAE               |     |     |     |     |     |                        |
| --------------- | -------------------- | --- | --- | --- | --- | --- | ---------------------- |
| b.              | (Kraus et al., 2024) | e.  |     |     |     |     |                        |
| Random          | ResNet               |     |     |     |     |     |  noitisopmoc epyt lleC |
(Sorin et al., 2023)
| Cell type    | Molecular tissue  |                    |                    |                    |     |                    |     |
| ------------ | ----------------- | ------------------ | ------------------ | ------------------ | --- | ------------------ | --- |
| composition  | composition       |                    |                    |                    |     |                    |     |
|              |                   | Adenocarcinoma     | Adenocarcinoma     | Adenocarcinoma     |     | Adenocarcinoma     |     |
|              |                   | Grade 3            | Grade 3            | Grade 2            |     | Grade 3            |     |
|              |                   | No LN. Metastases  | No LN. Metastases  | No LN. Metastases  |     | No LN. Metastases  |     |
|              |                   | No Relapse         | No Relapse         | Relapse            |     | No Relapse         |     |
f.
| c. Clinical diagnostics  |     |                    |                 |                    |     |                 |  noitisopmoc epyt lleC |
| ------------------------ | --- | ------------------ | --------------- | ------------------ | --- | --------------- | ---------------------- |
|                          |     | Adenocarcinoma     | Adenocarcinoma  | Adenocarcinoma     |     | Adenocarcinoma  |                        |
|                          |     | Grade 2            | Grade 2         | Grade 2            |     | Grade 2         |                        |
|                          |     | No LN. Metastases  | LN. Metastases  | No LN. Metastases  |     | LN. Metastases  |                        |
|                          |     | Relapse            | Relapse         | Relapse            |     | No Relapse      |                        |
Figure4: ClinicaldecisionsupportthroughVirtualTissuesDatabase. a,VirTuesenablesdata-drivenclinicaldecisionsupportby
retrievingsimilarpatientcasesfromadatabaseoftissuerepresentationsbasedonVirTuesnichesummarytokensandanoptimal
transport-basedretrievalsystem. b-c,ComparisonofretrievalstatisticsevaluatedonCordsetal.18 usingthenicherepresentations
ofVirTues,CA-MAE16 andResNet7. Thereddottedlinesindicatethescoresachievedbyuniformlyrandomretrievalforreference.
b,Barplotsdepictaveragesimilarityscoresbetweenquerytissueandclosestmatchesintermsofcelltypecomposition(left)and
molecularcomposition(right). CelltypecompositionsimilarityisquantifiedbytheL1distancebetweenthequery’sandmatch’s
celltypeproportionvector. MolecularcompositionismeasuredbytheslicedWassersteindistancebetweenthepixel-sizedmarker
intensityvectors. c,Meanprecisionofthetop-3results(@3)fortheretrievaloffourclinicallabels: cancertype,grade,presenceof
lymphnodemetastasisandrelapse. P-valuesabovethebarsarecomputedbasedonaMcNemartestforeachclinicallabeland
indicatethenumberofhitsachievedbyVirTuescomparedtoarandomretrieval. d-f ExemplaryretrievalresultsfortissuesinCords
etal.18. Eachrowshowsthequerytissuefollowedbythethreeclosestmatches. Tissuesaredepictedusingtheircolor-codedcell
typemasks. Colorbarsnexttothetissuesindicatetheirproportionalcelltypecompositions.
Lastly, densely packed immune cells in the TIME a database of previous patients (Fig. 4a). This system
exhibit strong attention to lymphocyte-specific markers. could enable clinicians to make informed decisions by
CD45RA and HLA-DR are key markers for immune cell comparing tissue phenotypes, applied therapies, and
identification and activation status, while CD20 specifi- clinical outcomes across cases. Given a VirTues repre-
cally marks B lymphocytes. While histone H3 appears sentation of a patient’s tissue through niche summary
in the attention profile, as a structural component of tokensthatcapturetissuecomposition,architectureand
chromatin it is present in all nucleated cells, making interactions between different cellular neighborhoods,
it more likely a general nuclear marker in this context theVirtualTissueplatformallowsqueryingtheVirTues
rather than a specific indicator of cellular state. Database for archival cases with similar molecular pro-
VirTueslearnsbiologicallymeaningfulmarkerimpor- files. To achieve this, VirTues measures the structural
tance across various spatial regions without requiring similarity between virtual tissue embeddings using an
knowledge of the underlying cell type composition dur- optimal transport-based approach. Concretely, we com-
ing training. This explainability enables the validation putethepairwiseWassersteindistance51,52 betweenthe
of known biological relationships as well as the poten- respective niche summary tokens of the query tissue
tial discovery of novel biomarkers and thus ultimately and samples in the VirTues Database. Top-k matches,
potential targets for drug development. along with the clinical records of their corresponding
|     |     |     | patients | are retrieved | for clinical decision | support. |     |
| --- | --- | --- | -------- | ------------- | --------------------- | -------- | --- |
Retrieval via the Virtual Tissues database Quantitative evaluation demonstrates superior per-
for clinical decision support formance in matching both cell type composition and
|     |     |     | molecular | tissue structure | compared | to existing | meth- |
| --- | --- | --- | --------- | ---------------- | -------- | ----------- | ----- |
VirTues facilitates clinical decision support through a ods (i.e., ResNet7, CA-MAE16) and random retrievals.
novel retrieval system that identifies similar cases from Concretely, we measure the L1 distance between nor-
8

malizedhistogramsofthecelltypedistributionsineach Virtual Tissues represent patient samples
patient sample. In our example of primary lung cancer of previously unseen cancer type or disease
tissue18, VirTues significantly outperforms other meth-
ods7,16,24 (Fig. 4b, left). To quantify the similarity in The rapid advancement of precision oncology and the
molecular tissue structure between query and retrieval emergence of new molecular disease subtypes require
samples,weintroduceanoptimaltransport-basedevalu- computational methods that can immediately analyze
ationmetricbasedoncomputingtheslicedWasserstein novel cancer types without the time-consuming process
distance of the raw pixel values of the corresponding of collecting large training datasets and retraining mod-
multiplex images53 (see Methods for details). Again, els. Thisisparticularlycriticalinclinicalsettings,where
VirTuesretrievesarchivalpatientsampleswhosemolec- prompt analysis of rare cancers or newly characterized
ular tissue composition is highly similar to the query disease subtypes can directly impact treatment deci-
(Fig. 4b, right). So while the retrieval is based on sions. While most approaches require model updates
VirTues niche summary tokens, the similarity also holds or fine-tuning which risks overfitting and compromising
with regards to other representations of the tissues, the universality of learned representations, we demon-
such as cell type annotations or raw images. strate that VirTues achieves true zero-shot general-
ization to unseen cancer types and diseases (Fig. 5).
When tested on new datasets including melanoma19
Further, we evaluate the similarity of the retrieved
and pancreatic tissue samples19, the model maintains
archival patients not only in terms of cell type and
robust performance without any refinement, preserving
molecular tissue composition but also their associated
tissue representation capabilities that are apparently
clinical records. Concretely, we perform a McNemar
universal across tissue types and downstream tasks.
test for each clinical label to compare the number of
Trained on primary breast13,17 and lung cancer tis-
hits among the top three results achieved by VirTues
sue18, VirTues directly maps primary and metastatic
with the number of hits for random retrieval. The
melanomacancersamplesintotheVirtualTissuespace
model achieves significant improvements in critical clin-
(Fig.5a). ToevaluatetheVirTuesEncoder,weanalyze
ical diagnostic tasks (Fig. 4c), including cancer type
its reconstruction abilities in the zero-shot setting for
classification (P = 6.5e-116), grade determination (P
different - previously described - masking strategies.
= 1.1e-25), lymph node metastasis prediction (P =
The evaluation is conducted over the subset of markers
1.0e-06) and relapse prediction (P = 5.6e-07).
in Hoch et al.19 shared with the train datasets13,17,18.
Examples of different marker reconstructions are visible
in Fig. 5b. Reconstruction results on further markers
Three case studies demonstrate VirTues’ ability to
can be found in Suppl. Figs. 18, 19, and 20. Quantify-
retrieve relevant matches across different cancer pre-
ing the average MSE over all markers shows that the
sentations: (1) A grade 2 squamous cell carcinoma
reconstruction performance for independent and niche
case retrieving similar cases with varying lymph node
masking is relatively stable across the trained (many-
metastasis and relapse outcomes (Fig. 4d), (2) a grade
shot) or zero-shot setting. When masking an entire
3 adenocarcinoma case matching samples with similar
markerandthusanyinformationoninter-markercorrela-
tissuearchitectureandlymphnode(LN)metastasissta-
tion,theperformancesignificantlydrops(Fig.5c,Suppl.
tus but different clinical trajectories (Fig. 4e) and (3) a
Fig. 25). In independent and niche masking, spatial
grade 2 adenocarcinoma case with lymph node metas-
attention can leverage local spatial context and marker
tasis and relapse, showing previous adenocarcinoma
attention dynamically picks up correlations between
cases with comparable grades and tissue architectures
markerstoreconstructmissingregions. However, when
(Fig. 4f). Each retrieved case includes a visualization
an entire marker is masked, reconstruction relies solely
of the cell type distribution (tumor, immune, vessel,
on learned relations between markers from the training
fibroblast, T cells) and clinical annotations, enabling
data. Unsurprisingly, in zero-shot settings, these may
direct comparison of tissue architecture and outcomes.
not fully generalize to novel cancer types where marker
Further case studies are exhibited in Suppl. Fig. 17.
relationships could differ from the training distribution.
Moststrikingly,quantitativeevaluationshowsstrong
The systematic evaluation of VirTues’ retrieval ca- performanceinthebiologicaldiscoveryandclinicaldiag-
pabilities demonstrates not only its ability to identify nostic tasks even in the zero-shot setting, i.e., cell type
molecular similar tissue architectures but also the clini- classification (Fig. 5d) and clinical feature prediction
cal relevance of these similarities, as evidenced by the (Fig. 5e); for melanoma samples performance levels
concordanceofretrievedcases’clinicalfeaturesandout- approach those achieved on trained datasets. At the
comes. Thus, by integrating molecular profiles, tissue cellular level, we compare the performance of VirTues
architecture and clinical outcomes in a unified retrieval (zero-shot) with VirTues (many-shot) on cell type clas-
framework, VirTues provides the foundation for a data- sification (distinguishing lymphocytes, macrophages,
driven comparison of tissue phenotypes across patient stromal, T cell and tumor cells). VirTues (zero-shot)
cohorts. achieves F1-scores of 0.94 for tumor cells and 0.81 for
9

a. primary lung cancer tissue b. primary and metastatic melanoma cancer tissue Virtual Tissues (zero-shot) Virtual Tissues (trained)
primary breast cancer tissue
|     |     | primary breast cancer tissue |     |  tnednepedni |     |     |     |
| --- | --- | ---------------------------- | --- | ------------ | --- | --- | --- |
GNINIART
gniksam
|     |     | Virtual Tissues | e.g., distribution   |     |     |     |     |
| --- | --- | --------------- | -------------------- | --- | --- | --- | --- |
of cell tokens
primary and metastatic
|                      | new datasets | melanoma cancer tissue |           |                 |     |     |     |
| -------------------- | ------------ | ---------------------- | --------- | --------------- | --- | --- | --- |
|                      |              | diabetic pancreas      |           |  rekram gniksam |     |     |     |
|  TOHS-OREZ ECNEREFNI |              |                        | Virtual   |                 |     |     |     |
Tissues
|     |     | Virtual Tissues | Space |     |     |     |     |
| --- | --- | --------------- | ----- | --- | --- | --- | --- |
*
|     |     |     | prediction  information   | gniksam |     |     |     |
| --- | --- | --- | ------------------------- | ------- | --- | --- | --- |
|     |     |     | tasks retrieval           |  ehcin  |     |     |     |
new  MLANA
marker
Virtual Tissues (zero-shot on dataset)
|     | zero-shot | Virtual Tissues (trained on dataset)                              |     |     | ResNet (Sorin et al., 2023)                   |     |     |
| --- | --------- | ----------------------------------------------------------------- | --- | --- | --------------------------------------------- | --- | --- |
| c.  | trained   | d.                                                                |     |     | e.                                            |     |     |
|     |           | primary and metastatic melanoma cancer tissue (Hoch et al., 2022) |     |     | primary and metastatic melanoma cancer tissue |     |     |
level ralucelom
|     |     | level ralullec                          |                  |                                               | level eussit                            |                |                             |
| --- | --- | --------------------------------------- | ---------------- | --------------------------------------------- | --------------------------------------- | -------------- | --------------------------- |
| f.  |     | g.                                      |                  |                                               | h.                                      |                |                             |
|     |     | diabetic pancreas (Damond et al., 2019) |                  |                                               | diabetic pancreas (Damond et al., 2019) |                |                             |
|     |     |                                         |                  | primary and metastatic melanoma cancer tissue |                                         |                | Virtual Tissues (zero-shot) |
| i.  |     |                                         |                  | j.                                            |                                         | k.             | Virtual Tissues (trained)   |
|     |     |                                         | supported marker | independent masking                           |                                         | marker masking |                             |
k-nearest neighbors
| Protein language model  |     |     | of MLANA |     |     |     |     |
| ----------------------- | --- | --- | -------- | --- | --- | --- | --- |
marker embeddings
trained on
primary lung cancer tissue
primary breast cancer tissue
primary breast cancer tissue
| zero-shot on            |     |     |     |     | supported markers |     | isolated markers |
| ----------------------- | --- | --- | --- | --- | ----------------- | --- | ---------------- |
| primary and metastatic  |     |     |     |     | l.                |     |                  |
melanoma cancer tissue
indep. zero-shot
marker trained
niche average
isolated marker
2 PAMU
k-nearest neighbors
of CCL8
UMAP 1
Figure 5: Zero-shot generalization to new cancer types and markers. a, VirTues’ architecture enables the generation of virtual
tissue representations for multiplexed images from new datasets in a zero-shot manner. These datasets may contain markers
thatwereeitherobservedorunobservedduringpretraining. Toassessthezero-shotcapabilitiesofVirTues,wetrainedtwomodel
instances: oneusingCordsetal.18,Danenbergetal.13 andJacksonetal.17 toevaluatezero-shotperformanceonHochetal.19
andanotherusingCordsetal.18,Danenbergetal.13,Jacksonetal.17 andHochetal.19 toevaluatezero-shotperformanceon
Damondetal.20. b,Examplesofzero-shotreconstructionsformarkersofHochetal.19 whicharemeasuredinthepretraining
datasets. Eachrowshowsresultsforadifferentmaskingstrategy. Forcomparison,reconstructionsofthesamesamplesgenerated
byamodelpretrainedonHochetal.19 arealsoshown. c,f,Comparisonofthereconstructionerrorsbetweenthezero-shotandthe
non-zero-shotsettingforHochetal.19 (top)andDamondetal.20 (bottom). Inbothsettings,theaverageistakenoverchannels
presentinthepretrainingdatasets. d,e,g,hZero-shotperformanceofVirTuesforcelltypeclassificationandtissuelevelprediction
tasksonHochetal.19 andDamondetal.20 comparedtothenon-zero-shotsetting. Inbothcases,onlymarkerswhicharemeasured
inthepretrainingdatasetsareusedtocomputetherepresentations. Forthecelltypeclassificationtaskbarplotsshowclass-wise
recallandF1-scores,whileforthetissue(orpatient)levelclassificationtasks,barplotspresentaccuraciesandmacro-averaged
F1-scores. ResultsofResNet7 areincluded,displayedingray. i,UMAPvisualizationofproteinlanguagemodelembeddings. Each
dotrepresentstheembeddingofaproteinmarkercoloredbythedatasetinwhichitismeasured. Notethatthecoloringdoesnot
differentiatemarkerspresentinmultipledatasets. TheproteinembeddingsoftwomarkersexclusivetoHochetal.19,MLANAand
CLL8-mRNA,alongwiththeirnearestneighbors,whichwereseenduringpretrainingonCordsetal.18,Danenbergetal.13 and
Jacksonetal.17,arehighlighted. j,kExamplesofzero-shotreconstructionsformarkersMLANAandCCL8-mRNAmeasuredin
Hochetal.19,whichwerenotobservedduringpretraining. Forcomparison,reconstructionsofthesamesamplesgeneratedbya
modelpretrainedonHochetal.19 arealsoshown. l,SquaredreconstructionerrorformarkersexclusivetoHochetal.19 inthe
zero-shotandnon-zero-shotsetting. Markersaregroupedbasedonthedensityoftheirsurroundingneighborhoodwithintheprotein
embeddingspace,constrainedtoincludeonlymarkerspresentduringthepretraining. Dashedlinesrepresenttheaveragezero-shot
MSEsacrosschannelsforindependentmasking: 0.40forsupportedmarkersand0.64forisolatedmarkers.
10

T cells, as compared to VirTues (many-shot) achieving tissue suggests that VirTues’ learned tissue represen-
F1-scores of 0.94 and 0.84 respectively. Moreover, we tations capture fundamental biological patterns that
noticethatinmacrophages,VirTues(zero-shot)outper- generalize across diseases and organs.
forms VirTues (many-shot) achieving F1-scores of 0.51
and0.48respectively. Atthetissuelevel,VirTuesshows
Multi-scale design enables extrapolation to
strongerperformancethanResNet7ingeneral. VirTues
(zero-shot) demonstrates superior performance, for ex- new markers
ample, in Relapse prediction (0.88 accuracy, improving
The ability to analyze new protein or RNA markers
performancebyover79.49%ascomparedtoResNet7),
without model retraining is crucial for two key reasons:
and Mutation prediction (0.76 accuracy, with relative
First, therapidevolutionofproteinbiomarkerdiscovery
performance improvement of 32.59% over ResNet7).
in oncology continually identifies new molecular targets
Benchmarking here is reduced to ResNet7 in the tissue
that could serve as diagnostic markers or therapeutic
level as CA-MAE16 is not designed to operate in the
targets. While traditional approaches would require
zero-shot setting. As mentioned before, ResNet7 is
complete retraining with new datasets that contain
restricted to niche- and tissue-level tasks.
additional markers, this creates an unacceptable delay
Besides representing a completely new cancer type,
in clinical translation. Second, different research stud-
we test VirTues’ capacity to create virtual tissues of
ies and clinical applications focus on distinct aspects
a new disease, specifically, diabetic pancreas tissue20.
of tumor biology, necessitating flexible combinations
This dataset comprises multiplexed IMC data from 843
and possibly measurement of new markers. A frame-
images from 12 human donors, including eight with
workthatrequiresretrainingforeachnewmarkerwould
type-1 diabetes (T1D), capturing the progression of
severely limit interoperability between studies.
T1D through comprehensive profiling of pancreatic tis-
Akeyinnovationofthemulti-scaledesignofVirTues
sue sections with 32 markers (Fig. 24). While the
is therefore its ability to incorporate new markers with-
overall reconstruction performance of masked regions
out retraining, enabling both rapid translation of novel
is lower (Fig. 5f) compared to zero-shot performance
biomarkers and integration of data across diverse scien-
on a different cancer tissue type (Fig. 5c), the overall
tific studies. A critical building block to achieve this is
findings hold for T1D tissues. Reconstruction results
theintegratedproteinlanguagemodelthatoperateson
on further markers can be found in Suppl. Figs. 21, 22,
the molecular level of the VirTues architecture which
and 23. MAE losses for individual markers are shown
allowszero-shotembeddingofnewmarkers. Concretely,
in Suppl. Fig. 25.
VirTuesleverageslearnedrelationshipsbetweenproteins
Further, acrosstasksonthecellularandtissuelevel, captured in the embeddings of the PLM trained on mil-
thezero-shotperformanceofVirTuesisonparwiththe lions of protein structures54 to predict the behavior of
many-shot setting (Fig. 5g,h). At the cellular level, we new markers based on their molecular similarities and
compare the performance of VirTues (zero-shot) with biological contexts34. A UMAP of the PLM embed-
VirTues (many-shot) on cell type classification (distin- ding of the different markers from the used datasets is
guishing exocrine, immune, and islet cell populations). displayed in Fig. 5i (see Suppl. Fig. 26 for UMAPs of
We note that the populations are highly imbalanced, individual datasets). As expected, proteins with similar
with exocrine cells occupying 84.10% of all cells, while structures (and functions) cluster together such as var-
immune and islet cells occupy 3.17% and 12.73% re- ious cytokeratins or transcription factors in the bottom
spectively. VirTues (zero-shot) achieves an F1-score right and top of the UMAP, respectively.
of 0.84 for exocrine cells and 0.15 for islet cells, as We demonstrate VirTues’ capability to perform
compared to VirTues (many-shot), which gets 0.84 zero-shot embedding of new unseen markers, that are
and 0.18 respectively. Importantly, the overall perfor- presentinHochetal.19 butabsentfromVirTues’train-
mance in predicting the immune and islet class is low ing datasets, in two different scenarios of increasing
even in the many-shot setting, likely due to the overall difficulty: First, we embed new proteins that are well
limited amount of training data for these tasks. At the supported by markers of highly similar PLM embed-
tissue level, VirTues (zero-shot) achieves an accuracy dings across training datasets. One such marker is
of 0.84 surpasses ResNet7, with an accuracy of 0.83, Melan-A (MLANA), also known as melanoma antigen
by 0.80% in AAB status classification, while VirTues recognized by T cells 1 (MART-1), which contains
(trained)achievesanaccuracyof0.89, andhasalarger a fragment that is bound by MHC class I complexes
improvement of 7.50%. For the stage classification presented to T cells of the immune system (Fig. 5j,k).
task, VirTues (zero-shot) achieves an accuracy of 0.75 MLANA is well surrounded by markers such as PDN,
outperforms ResNet7, with an accuracy of 0.70, by cell surface receptor on T cells and B cells, or CD20 or
6.72%, with VirTues (trained) achieving an accuracy CD38, cell surface molecules of immune cells. Second,
of 0.77 and demonstrating an improvement of 9.25%. increasing the difficulty, we test VirTues on integrating
Furthermore, the ability to reconstruct masked tis- isolated markers that have only a few similar markers
sueregionsandmarkermeasurementsandtacklepredic- across the training datasets, e.g., CCL8-mRNA, the
tion tasks across different physical scales of pancreatic mRNA of a chemokine secreted by tumor-associated
11

macrophages55. Besides markers such as CCL21 ize across cancer types, diseases and organs without
present in Cords et al.18 and CXCL12, present in requiring retraining or fine-tuning. This capability is
Danenberg et al.13, VirTues has not seen any further particularly valuable for rare cancers and newly charac-
marker with related PLM embedding. terized disease subtypes, where collecting large training
Analyzing VirTues ability to reconstruct new mark- datasets is impractical. The model’s robust zero-shot
ers highlights the importance of VirTues’ multi-scale performance in both melanoma and pancreatic tissue
design: Despite not encountering MLANA (or other analysissuggeststhatitcapturesfundamentalbiological
well-supportedmarkerssuchasPD-L1,p-Rn,SLC2A12 patterns that transcend specific contexts. This univer-
and SOX10, see Fig. 5l), the model reaches the re- sality is enabled by our novel transformer architecture
construction performance of a version of VirTues that that explicitly separates spatial and marker attention
includestheHochetal.19 datasetintrainingintheinde- mechanisms, allowing the model to learn generalizable
pendent marking setting. The marker attention is able relationships between molecular markers while main-
toprocessthecombinedmarkerandspatialtokenonthe taining sensitivity to tissue-specific spatial patterns.
fly, given access to some unmasked patches of the new The integration of protein language models at the
marker(Fig.5j). Inthesettingwheretheentiremarker molecular scale represents another key advancement,
is masked, VirTues can reconstruct the overall expres- enabling VirTues to incorporate new markers without
sion of the marker, however, not its intensity (Fig. 5k). retraining. This capability is essential for keeping pace
The result on CCL8-mRNA demonstrates that with rapid biomarker discovery and accommodating di-
VirTues’ performance varies based on the information verse research priorities that require different marker
supportavailablefornewmarkers(Fig.5j,k). Whilethe combinations. By leveraging learned protein relation-
overall trends in VirTues’ reconstruction ability follow ships,VirTuescanpredictthebehaviorofnovelmarkers
theresultsinFig.5j,konsupportedmarkers,thequality based on their molecular similarities to known mark-
is lower the less supported a marker is: Fig. 5l shows ers, as demonstrated with MLANA in melanoma tissue.
all markers in Hoch et al.19 that are not present in any The model’s ability to handle varying marker combi-
of the training dataset sorted by the average distance nations also facilitates cross-study comparisons and
| to its 5   | nearest | neighbors | in      | the PLM        | embedding | space | meta-analyses. |             |     |         |           |      |         |
| ---------- | ------- | --------- | ------- | -------------- | --------- | ----- | -------------- | ----------- | --- | ------- | --------- | ---- | ------- |
| (Fig. 5i). | The     | average   | squared | reconstruction |           | error |                |             |     |         |           |      |         |
|            |         |           |         |                |           |       | VirTues’       | multi-scale |     | design, | operating | from | molecu- |
thereby increases from 0.40 in supported markers to lartotissuelevels, providesacomprehensiveframework
| 0.67 in | isolated | markers. | Results | on  | further | markers |                   |     |         |     |            |          |      |
| ------- | -------- | -------- | ------- | --- | ------- | ------- | ----------------- | --- | ------- | --- | ---------- | -------- | ---- |
|         |          |          |         |     |         |         | for understanding |     | complex |     | biological | systems. | This |
highlighted in Fig. 5l can be found in Suppl. Fig. 27. hierarchical approach enables the model to capture
| This | systematic | analysis |     | of VirTues’ | ability | to  | in-           |     |              |          |     |        |              |
| ---- | ---------- | -------- | --- | ----------- | ------- | --- | ------------- | --- | ------------ | -------- | --- | ------ | ------------ |
|      |            |          |     |             |         |     | how molecular |     | and cellular | patterns |     | inform | higher-level |
corporate new markers reveals both the power and tissue structures that ultimately determine clinical out-
| limitations | of  | protein | language | model-guided |     | marker |        |             |     |        |             |     |             |
| ----------- | --- | ------- | -------- | ------------ | --- | ------ | ------ | ----------- | --- | ------ | ----------- | --- | ----------- |
|             |     |         |          |              |     |        | comes. | The model’s |     | strong | performance |     | across cell |
extrapolation: While the model successfully generalizes type classification, tissue structure identification and
| to new | markers | that are | molecularly | similar |     | to those | in  |     |     |     |     |     |     |
| ------ | ------- | -------- | ----------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
clinicalfeaturepredictiondemonstratesthevalueofthis
the training data, its performance decreases for more integrated analysis. Furthermore, the attention-based
| isolated | markers. | This | behavior | aligns | with | biological |                  |     |            |     |         |            |          |
| -------- | -------- | ---- | -------- | ------ | ---- | ---------- | ---------------- | --- | ---------- | --- | ------- | ---------- | -------- |
|          |          |      |          |        |      |            | interpretability |     | mechanisms |     | provide | biological | insights |
intuition—markers with similar molecular properties are by revealing critical spatial regions and marker relation-
| more likely   | to            | exhibit | related       | spatial      | distributions |          | in              |             |               |                    |     |              |               |
| ------------- | ------------- | ------- | ------------- | ------------ | ------------- | -------- | --------------- | ----------- | ------------- | ------------------ | --- | ------------ | ------------- |
|               |               |         |               |              |               |          | ships that      | influence   | predictions.  |                    |     |              |               |
| tissues—and   | suggests      |         | that future   | improvements |               | in pro-  |                 |             |               |                    |     |              |               |
|               |               |         |               |              |               |          | The             | potential   | clinical      | utility            | of  | VirTues      | is demon-     |
| tein language |               | models  | could         | further      | enhance       | VirTues’ |                 |             |               |                    |     |              |               |
|               |               |         |               |              |               |          | strated through |             | its retrieval | system             |     | for clinical | decision      |
| marker        | extrapolation |         | capabilities. |              |               |          |                 |             |               |                    |     |              |               |
|               |               |         |               |              |               |          | support.        | By enabling |               | the identification |     | of           | similar cases |
basedonmolecularandcellularpatternsacrossdifferent
| Discussion |     |     |     |     |     |     | studydesigns,thesystemcouldassistinevidence-based |     |     |                  |     |     |             |
| ---------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | ---------------- | --- | --- | ----------- |
|            |     |     |     |     |     |     | clinical assessment.                              |     |     | The improvements |     |     | in matching |
The development of the Virtual Tissues platform repre- tissue composition and predicting clinical outcomes
|         |                 |     |     |               |     |            | suggest | that VirTues |     | captures | biologically |     | meaningful |
| ------- | --------------- | --- | --- | ------------- | --- | ---------- | ------- | ------------ | --- | -------- | ------------ | --- | ---------- |
| sents a | new development |     | in  | computational |     | pathology, |         |              |     |          |              |     |            |
introducing a foundation model framework that ad- similarities between cases, though prospective clinical
|         |                |     |              |           |     |         | validation | would | be needed | to  | confirm | its utility | in clini- |
| ------- | -------------- | --- | ------------ | --------- | --- | ------- | ---------- | ----- | --------- | --- | ------- | ----------- | --------- |
| dresses | key challenges |     | in analyzing | multiplex |     | imaging |            |       |           |     |         |             |           |
datawhileenablingnewcapabilitiesforbiologicaldiscov- cal decision-making or in selecting patients for clinical
|         |          |               |     |             |             |     | trials based | on  | tissue | architecture. |     |     |     |
| ------- | -------- | ------------- | --- | ----------- | ----------- | --- | ------------ | --- | ------ | ------------- | --- | --- | --- |
| ery and | clinical | applications. |     | Our results | demonstrate |     |              |     |        |               |     |     |     |
thatVirTuesachievesthreecriticalobjectives: universal Despite these advances, several important limita-
tissue representation across cancer types, diseases and tions of our study should be acknowledged. While
organs, flexible incorporation of new molecular markers VirTues shows promising zero-shot performance, its
and interpretable multi-scale analysis from molecular to effectiveness varies depending on the biological simi-
tissue levels. larity between new markers and those in the training
A fundamental innovation of VirTues is its ability set. Performance degradation is particularly noticeable
to generate virtual tissue representations that general- for markers lacking close biological relationships to the
12

training data, as demonstrated by the CCL8 mRNA els for biology that can seamlessly integrate diverse
results. This suggests that the model’s generalization data types and generalize across biological contexts.
capabilities, while robust, are not unlimited. As multiplex imaging technologies continue to evolve,
Although our study incorporates data from five di- frameworks like VirTues will become increasingly im-
|                    |           |               |           |          |             |             | portant       | for translating | molecular | insights into | clinical |
| ------------------ | --------- | ------------- | --------- | -------- | ----------- | ----------- | ------------- | --------------- | --------- | ------------- | -------- |
| verse cohorts      | spanning  |               | different | cancer   | types       | and         | di-           |                 |           |               |          |
| abetes,            | further   | validation    | on larger | and      | more        | diverse     | applications. |                 |           |               |          |
| datasets           | is needed | to fully      | assess    | VirTues’ |             | scalability |               |                 |           |               |          |
| and generalization |           | capabilities. |           | While    | our current | re-         |               |                 |           |               |          |
References
| sults demonstrate |     | strong      | performance |        | across         | these ini- |                                                  |     |     |     |      |
| ----------------- | --- | ----------- | ----------- | ------ | -------------- | ---------- | ------------------------------------------------ | --- | --- | --- | ---- |
| tial datasets,    | the | exponential |             | growth | in multiplexed |            |                                                  |     |     |     |      |
|                   |     |             |             |        |                |            | [1] NataliedeSouza,ShanZhao,andBerndBodenmiller. |     |     |     | Mul- |
imaging data and the emergence of new experimental tiplexproteinimagingintumourbiology. NatureReviews
protocolsmayrevealadditionalchallengesorlimitations Cancer,24(3):171–191,2024.
| in the model’s | architecture. |     | This | is particularly |     | relevant |             |         |            |             |              |
| -------------- | ------------- | --- | ---- | --------------- | --- | -------- | ----------- | ------- | ---------- | ----------- | ------------ |
|                |               |     |      |                 |     |          | [2] Douglas | Hanahan | and Robert | A Weinberg. | Hallmarks of |
for assessing the model’s performance across differ- Cell,144(5):646–674,2011.
|                  |     |          |        |             |     |         | cancer: | thenextgeneration. |     |     |     |
| ---------------- | --- | -------- | ------ | ----------- | --- | ------- | ------- | ------------------ | --- | --- | --- |
| ent experimental |     | batches, | tissue | preparation |     | methods |         |                    |     |     |     |
and imaging platforms not represented in our current [3] Douglas Hanahan. Hallmarks of cancer: new dimensions.
CancerDiscovery,12(1):31–46,2022.
| datasets.  | Our current | implementation |     |                      | focuses | primarily |                                                    |     |     |     |     |
| ---------- | ----------- | -------------- | --- | -------------------- | ------- | --------- | -------------------------------------------------- | --- | --- | --- | --- |
| on protein | and         | RNA markers.   |     | The generalizability |         |           | to                                                 |     |     |     |     |
|            |             |                |     |                      |         |           | [4] XiaoQianWang,EstherDanenberg,Chiun-ShengHuang, |     |     |     |     |
other molecular data types such as metabolomics or Daniel Egle, Maurizio Callari, Begoña Bermejo, Matteo
disease contexts remains to be fully evaluated. Ad- Dugo, Claudio Zamagni, Marc Thill, Anton Anton, et al.
ditionally, the model’s performance on rare cell types Spatial predictors of immunotherapy response in triple-
Nature,621(7980):868–876,2023.
negativebreastcancer.
| or unusual | tissue | architectures |     | may be | limited | by their |     |     |     |     |     |
| ---------- | ------ | ------------- | --- | ------ | ------- | -------- | --- | --- | --- | --- | --- |
underrepresentation in training data. [5] Darci Phillips, Magdalena Matusiak, Belén Rivero Gutier-
|       |                     |     |     |                  |     |        | rez, | Salil S | Bhate, Graham | L Barlow, Sizun | Jiang, Janos |
| ----- | ------------------- | --- | --- | ---------------- | --- | ------ | ---- | ------- | ------------- | --------------- | ------------ |
| While | our attention-based |     |     | interpretability |     | mecha- |      |         |               |                 |              |
Demeter,KimberlySSmythe,RobertHPierce,StevenP
nisms provide valuable insights, they may not capture Fling, et al. Immune cell topography predicts response
all biologically relevant features. The model’s decisions toPD-1blockadeincutaneousTcelllymphoma. Nature
Communications,12(1):6726,2021.
| could be          | influenced | by subtle | patterns  |               | that are | not eas- |                                                        |     |     |     |     |
| ----------------- | ---------- | --------- | --------- | ------------- | -------- | -------- | ------------------------------------------------------ | --- | --- | --- | --- |
| ily interpretable |            | through   | attention | visualization |          | alone.   |                                                        |     |     |     |     |
|                   |            |           |           |               |          |          | [6] AndreaJRadtke,EkaterinaPostovalova,ArinaVarlamova, |     |     |     |     |
Furthermore,theclinicalrelevanceofidentifiedpatterns AlexanderBagaev,MariaSorokina,OlgaKudryashova,Mark
requires validation through prospective studies. Meerson,MargaritaPolyakova,IliaGalkin,ViktorSvekolkin,
|         |          |         |           |     |          |        | et al. | Multi-omic | profiling of | follicular lymphoma | reveals |
| ------- | -------- | ------- | --------- | --- | -------- | ------ | ------ | ---------- | ------------ | ------------------- | ------- |
| Looking | forward, | several | important |     | research | direc- |        |            |              |                     |         |
changesintissuearchitectureandenhancedstromalremod-
tions emerge. The framework could be expanded to eling in high-risk patients. Cancer Cell, 42(3):444–463,
| handleadditionalimagingmodalitiesandmoleculardata |        |            |                |              |     |          | 2024.    |        |                    |               |        |
| ------------------------------------------------- | ------ | ---------- | -------------- | ------------ | --- | -------- | -------- | ------ | ------------------ | ------------- | ------ |
| types. Methods                                    |        | to improve | generalization |              | for | markers, |          |        |                    |               |        |
|                                                   |        |            |                |              |     |          | [7] Mark | Sorin, | Morteza Rezanejad, | Elham Karimi, | Benoit |
| which are                                         | rarely | measured,  | could          | be developed |     | through  |          |        |                    |               |        |
Fiset,LysanneDesharnais,LucasJMPerus,SimonMilette,
integration of additional protein structure and function MirandaWYu,SarahMMaritan,SamuelDoré,etal.Single-
information. Theincorporationoftemporalinformation cellspatiallandscapesofthelungtumourimmunemicroen-
|     |     |     |     |     |     |     | vironment. |     | Nature,614(7948):548–554,2023. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------------------ | --- | --- |
couldenhanceunderstandingofdiseaseprogressionand
| treatment | responses, | while | the | clinical | decision | support |                                                      |     |     |     |     |
| --------- | ---------- | ----- | --- | -------- | -------- | ------- | ---------------------------------------------------- | --- | --- | --- | --- |
|           |            |       |     |          |          |         | [8] Jia-RenLin,Yu-AnChen,DanielCampton,JeremyCooper, |     |     |     |     |
system could be enriched with additional metadata and ShannonCoy,ClarenceYapp,JuliannBTefft,ErinMcCarty,
outcome data to provide more comprehensive guidance. KeithLLigon,ScottJRodig,etal. High-pleximmunoflu-
|             |         |                |     |               |        |       | orescence                                         |     | imaging and traditional | histology | of the same |
| ----------- | ------- | -------------- | --- | ------------- | ------ | ----- | ------------------------------------------------- | --- | ----------------------- | --------- | ----------- |
| VirTues’    | ability | to reconstruct |     | fully         | masked | mark- |                                                   |     |                         |           |             |
|             |         |                |     |               |        |       | tissuesectionfordiscoveringimage-basedbiomarkers. |     |                         |           | Na-         |
| ers through | learned | biological     |     | relationships |        | opens | in-                                               |     |                         |           |             |
tureCancer,4(7):1036–1052,2023.
| triguing | possibilities | for | integration | with | generative |     | AI  |     |     |     |     |
| -------- | ------------- | --- | ----------- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
approaches. While current virtual multiplexing meth- [9] SarahBlack,DarciPhillips,JohnWHickey,JuliaKennedy-
|                        |               |     |          |        |                |      | Darling,                                  | Vishal | G Venkataraaman, | Nikolay Samusik, | Yury  |
| ---------------------- | ------------- | --- | -------- | ------ | -------------- | ---- | ----------------------------------------- | ------ | ---------------- | ---------------- | ----- |
| ods focus              | on generating |     | specific | marker | patterns       | from |                                           |        |                  |                  |       |
|                        |               |     |          |        |                |      | Goltsev,ChristianMSchürch,andGarryPNolan. |        |                  |                  | Codex |
| H&E images56,57,58,59, |               |     | VirTues’ | marker | reconstruction |      |                                           |        |                  |                  |       |
multiplexedtissueimagingwithdna-conjugatedantibodies.
capabilities could be leveraged to generate and validate NatureProtocols,16(8):3802–3835,2021.
| synthetic | multiplex     | data. | The   | model’s        | understanding |         |                                                        |     |     |     |     |
| --------- | ------------- | ----- | ----- | -------------- | ------------- | ------- | ------------------------------------------------------ | --- | --- | --- | --- |
|           |               |       |       |                |               |         | [10] CharlotteGiesen,HaoAOWang,DenisSchapiro,NevenaZi- |     |     |     |     |
| of marker | relationships |       | could | help constrain |               | genera- |                                                        |     |     |     |     |
vanovic,AndreaJacobs,BodoHattendorf,PeterJSchüffler,
| tive processes |     | to biologically | plausible |     | configurations, |     |     |     |     |     |     |
| -------------- | --- | --------------- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
DanielGrolimund,JoachimMBuhmann,SimoneBrandt,
potentially improving the fidelity of virtual staining ap- et al. Highly multiplexed imaging of tumor tissues with
proaches. This synergy between reconstruction and subcellularresolutionbymasscytometry. NatureMethods,
11(4):417–422,2014.
| generation | could   | enable        | more | robust       | and biologically |         |                                                          |     |     |     |     |
| ---------- | ------- | ------------- | ---- | ------------ | ---------------- | ------- | -------------------------------------------------------- | --- | --- | --- | --- |
| accurate   | virtual | multiplexing, |      | particularly | for              | markers |                                                          |     |     |     |     |
|            |         |               |      |              |                  |         | [11] SabrinaMLewis,Marie-LiesseAsselin-Labat,QuanNguyen, |     |     |     |     |
that are challenging to measure experimentally. Jean Berthelet, Xiao Tan, Verena C Wimmer, Delphine
|         |            |     |               |      |        |     | Merino,KellyLRogers,andShalinHNaik. |     |     |     | Spatialomics |
| ------- | ---------- | --- | ------------- | ---- | ------ | --- | ----------------------------------- | --- | --- | --- | ------------ |
| VirTues | represents |     | a significant | step | toward | the |                                     |     |     |     | Nature       |
andmultiplexedimagingtoexplorecancerbiology.
broader goal of creating universal computational mod- methods,18(9):997–1012,2021.
13

[12] ThierryM.Nordmann,AndreasMund,andMatthiasMann. [24] KianKenyon-Dean,ZitongJerryWang,JohnUrbanik,Kon-
AnewunderstandingoftissuebiologyfromMS-basedpro- stantin Donhauser, Jason Hartford, Saber Saberian, Nil
teomics at single-cell resolution. Nature Methods, 21: Sahin,IhabBendidi,SafiyeCelik,MartaFay,etal. ViTally
2220–2222,2024. Consistent: ScalingBiologicalRepresentationLearningfor
|     |     |     |     |     |     |     | CellMicroscopy. |     | arXivpreprintarXiv:2411.02572,2024. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------------------------- | --- | --- | --- | --- |
[13] EstherDanenberg,HelenBardwell,VitoRTZanotelli,Elena
|             |            |     |       |       |          |        | [25] Ankit Gupta, | Zoe | Wefers, | Konstantin |     | Kahnert, | Jan N |
| ----------- | ---------- | --- | ----- | ----- | -------- | ------ | ----------------- | --- | ------- | ---------- | --- | -------- | ----- |
| Provenzano, | Suet-Feung |     | Chin, | Oscar | M Rueda, | Andrew |                   |     |         |            |     |          |       |
Hansen,WilliamDLeineweber,AnthonyCesnik,DanLu,
| Green, | Emad Rakha, | Samuel |     | Aparicio, | Ian | O Ellis, et | al.              |     |          |             |          |           |     |
| ------ | ----------- | ------ | --- | --------- | --- | ----------- | ---------------- | --- | -------- | ----------- | -------- | --------- | --- |
|        |             |        |     |           |     |             | Ulrika Axelsson, |     | Frederic | Ballllosera | Navarro, | Theofanis |     |
Breasttumormicroenvironmentstructuresareassociated
|     |     |     |     |     | NatureGenet- |     | Karaletsos, | et al. | SubCell: | Vision | foundation | models | for |
| --- | --- | --- | --- | --- | ------------ | --- | ----------- | ------ | -------- | ------ | ---------- | ------ | --- |
withgenomicfeaturesandclinicaloutcome.
ics,54(5):660–669,2022. microscopycapturesingle-cellbiology. bioRxiv,2024.
[14] ApostoliaMTsimberidou,MichaelKahle,HenryHiepVo, [26] YujiaBao,SrinivasanSivanandan,andTheofanisKaralet-
Mehmet A Baysal, Amber Johnson, and Funda Meric- sos. Channel Vision Transformers: An Image Is Worth C
InInternationalConferenceonLearning
| Bernstam. | Moleculartumourboards—currentandfuture |     |     |     |     |     | x16x16Words. |     |     |     |     |     |     |
| --------- | -------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Representations(ICLR),2023.
| considerationsforprecisiononcology. |     |     |     | NatureReviewsClini- |     |     |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
calOncology,20(12):843–863,2023.
|     |     |     |     |     |     |     | [27] Mark-Anthony | Bray, | Shantanu |     | Singh, Han | Han, | Chad- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----- | -------- | --- | ---------- | ---- | ----- |
wickTDavis,BlakeBorgeson,CathyHartland,MariaKost-
| [15] Alessandra | Rigamonti, |     | Marika | Viatore, | Rebecca | Polidori, |          |        |                  |     |             |     |         |
| --------------- | ---------- | --- | ------ | -------- | ------- | --------- | -------- | ------ | ---------------- | --- | ----------- | --- | ------- |
|                 |            |     |        |          |         |           | Alimova, | Sigrun | M Gustafsdottir, |     | Christopher | C   | Gibson, |
DaoudRahal,MarcoErreni,MariaRitaFumagalli,Damiano
|         |        |            |      |            |     |              | andAnneECarpenter. |                   | CellPainting,ahigh-contentimage- |     |                 |             |     |
| ------- | ------ | ---------- | ---- | ---------- | --- | ------------ | ------------------ | ----------------- | -------------------------------- | --- | --------------- | ----------- | --- |
| Zanini, | Andrea | Doni, Anna | Rita | Putignano, |     | Paola Bossi, |                    |                   |                                  |     |                 |             |     |
|         |        |            |      |            |     |              | based assay        | for morphological |                                  |     | profiling using | multiplexed |     |
etal.IntegratingAI-PoweredDigitalPathologyandImaging
fluorescentdyes.NatureProtocols,11(9):1757–1774,2016.
MassCytometryIdentifiesKeyClassifiersofTumorCells,
Stroma,andImmuneCellsinNon–SmallCellLungCancer.
|     |     |     |     |     |     |     | [28] AlexeyDosovitskiy,LucasBeyer,AlexanderKolesnikov,Dirk |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
CancerResearch,84(7):1165–1177,2024.
Weissenborn,XiaohuaZhai,ThomasUnterthiner,Mostafa
[16] OrenKraus,KianKenyon-Dean,SaberSaberian,Maryam Dehghani,MatthiasMinderer,GeorgHeigold,SylvainGelly,
Fallah,PeterMcLean,JessLeung,VasudevSharma,Ayla Jakob Uszkoreit, and Neil Houlsby. An Image is Worth
Khan, Jia Balakrishnan, Safiye Celik, et al. Masked Au- 16x16Words: TransformersforImageRecognitionatScale.
|     |     |     |     |     |     |     | In International | Conference |     | on  | Learning | Representations |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------- | --- | --- | -------- | --------------- | --- |
toencodersforMicroscopyareScalableLearnersofCellular
(ICLR),2021.
| Biology. | InIEEEConferenceonComputerVisionandPat- |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ternRecognition(CVPR),pages11757–11768,2024.
|     |     |     |     |     |     |     | [29] CharlotteBunne,YusufRoohani,YanayRosen,AnkitGupta, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
XikunZhang,MarcelRoed,TheoAlexandrov,Mohammed
| [17] Hartland | W Jackson, | Jana | R   | Fischer, | Vito | RT Zanotelli, |     |     |     |     |     |     |     |
| ------------- | ---------- | ---- | --- | -------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
AlQuraishi,PatriciaBrennan,DanielB.Burkhardt,Andrea
HRazaAli,RobertMechera,SavasDSoysal,HolgerMoch,
|     |     |     |     |     |     |     | Califano, | Jonah | Cool, | Abby F. | Dernburg, | Kirsty | Ewing, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ----- | ------- | --------- | ------ | ------ |
SimoneMuenst,ZsuzsannaVarga,WalterPWeber,etal.
EmilyB.Fox,MatthiasHaury,AmyE.Herr,EricHorvitz,
Thesingle-cellpathologylandscapeofbreastcancer.Nature,
PatrickD.Hsu,VirenJain,GregoryR.Johnson,Thomas
578(7796):615–620,2020.
|           |               |            |     |        |            |       | Kalil, David  | R.            | Kelley, | Shana | O. Kelley,   | Anna       | Kreshuk, |
| --------- | ------------- | ---------- | --- | ------ | ---------- | ----- | ------------- | ------------- | ------- | ----- | ------------ | ---------- | -------- |
|           |               |            |     |        |            |       | TimMitchison, | StephaniOtte, |         |       | JayShendure, | NicholasJ. |          |
| [18] Lena | Cords, Sandra | Tietscher, |     | Tobias | Anzeneder, | Claus |               |               |         |       |              |            |          |
Sofroniew,FabianTheis,ChristinaV.Theodoris,Srigokul
| Langwieder,  | Martin                                      | Rees, | Natalie | de  | Souza,         | and Bernd |              |         |         |           |            |             |        |
| ------------ | ------------------------------------------- | ----- | ------- | --- | -------------- | --------- | ------------ | ------- | ------- | --------- | ---------- | ----------- | ------ |
|              |                                             |       |         |     |                |           | Upadhyayula, | Marc    | Valer,  | Bo        | Wang, Eric | Xing,       | Serena |
| Bodenmiller. | Cancer-associatedfibroblastclassificationin |       |         |     |                |           |              |         |         |           |            |             |        |
|              |                                             |       |         |     | NatureCommuni- |           | Yeung-Levy,  | Marinka | Zitnik, | Theofanis |            | Karaletsos, | Aviv   |
single-cellandspatialproteomicsdata.
cations,14(1):4294,2023. Regev, Emma Lundberg, Jure Leskovec, and Stephen R.
|     |     |     |     |     |     |     | Quake. How | to  | Build | the Virtual | Cell with | Artificial | In- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ----------- | --------- | ---------- | --- |
[19] Tobias Hoch, Daniel Schulz, Nils Eling, Julia Martínez telligence: Priorities and Opportunities. arXiv Preprint
Gómez,MitchellPLevesque,andBerndBodenmiller. Mul- arXiv:2409.11654,2024.
tiplexedimagingmasscytometryofthechemokinemilieus
|     |     |     |     |     |     |     | [30] JohnWHickey,EranAgmon,NinaHorowitz,Tze-KaiTan, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
inmelanomacharacterizesfeaturesoftheresponsetoim-
MatthewLamore,JohnBSunwoo,MarkusWCovert,and
| munotherapy. | ScienceImmunology,7(70):eabk1692,2022. |     |     |     |     |     |                |             |     |             |         |     |          |
| ------------ | -------------------------------------- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ----------- | ------- | --- | -------- |
|              |                                        |     |     |     |     |     | Garry P Nolan. | Integrating |     | multiplexed | imaging |     | and mul- |
tiscalemodelingidentifiestumorphenotypeconversionas
[20] NicolasDamond,StefanieEngler,VitoRTZanotelli,Denis
|           |       |               |     |                    |     |       | a critical | component | of  | therapeutic | T cell | efficacy. | Cell |
| --------- | ----- | ------------- | --- | ------------------ | --- | ----- | ---------- | --------- | --- | ----------- | ------ | --------- | ---- |
| Schapiro, | Clive | H Wasserfall, |     | Irina Kusmartseva, |     | Harry | S          |           |     |             |        |           |      |
Systems,15(4):322–338,2024.
Nick,FabrizioThorel,PedroLHerrera,MarkAAtkinson,
| et al.                | A Map of | Human | Type                          | 1 Diabetes | Progression |     | by                                                  |     |     |     |     |     |     |
| --------------------- | -------- | ----- | ----------------------------- | ---------- | ----------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                       |          |       |                               |            |             |     | [31] MichaelDoron,ThéoMoutakanni,ZitongSChen,Nikita |     |     |     |     |     |     |
| ImagingMassCytometry. |          |       | CellMetabolism,29(3):755–768, |            |             |     |                                                     |     |     |     |     |     |     |
Moshkov,MathildeCaron,HugoTouvron,PiotrBojanowski,
2019.
|              |         |      |       |      |       |         | WolfgangMPernice,andJuanCCaicedo. |     |                      |     |        | Unbiasedsingle- |     |
| ------------ | ------- | ---- | ----- | ---- | ----- | ------- | --------------------------------- | --- | -------------------- | --- | ------ | --------------- | --- |
|              |         |      |       |      |       |         | cell morphology                   |     | with self-supervised |     | vision | transformers.   |     |
| [21] Richard | J Chen, | Tong | Ding, | Ming | Y Lu, | Drew FK | bioRxiv,2023.                     |     |                      |     |        |                 |     |
Williamson,GuillaumeJaume,AndrewHSong,BowenChen,
| AndrewZhang,DanielShao,MuhammadShaban,etal. |     |     |     |     |     | To- |                                                       |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                             |     |     |     |     |     |     | [32] AshishVaswani,NoamShazeer,NikiParmar,JakobUszko- |     |     |     |     |     |     |
wardsageneral-purposefoundationmodelforcomputational
reit,LlionJones,AidanNGomez,ŁukaszKaiser,andIllia
| pathology. | NatureMedicine,30(3):850–862,2024. |     |     |     |     |     |             |                        |     |     |                  |     |     |
| ---------- | ---------------------------------- | --- | --- | --- | --- | --- | ----------- | ---------------------- | --- | --- | ---------------- | --- | --- |
|            |                                    |     |     |     |     |     | Polosukhin. | AttentionisAllyouNeed. |     |     | InAdvancesinNeu- |     |     |
ralInformationProcessingSystems(NeurIPS),volume30,
[22] HanwenXu,NaotoUsuyama,JaspreetBagga,ShengZhang,
2017.
RajeshRao,TristanNaumann,CliffWong,ZelalemGero,
Javier González, Yu Gu, et al. A whole-slide foundation [33] Gedas Bertasius, Heng Wang, and Lorenzo Torresani. Is
modelfordigitalpathologyfromreal-worlddata. Nature, Space-TimeAttentionAllYouNeedforVideoUnderstand-
pages1–8,2024. ing? In International Conference on Machine Learning
(ICML),volume139,pages813–824.PMLR,2021.
| [23] Xiyue | Wang, Junhan | Zhao, | Eliana | Marostica, |     | Wei Yuan, |     |     |     |     |     |     |     |
| ---------- | ------------ | ----- | ------ | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
JietianJin,JiayuZhang,RuijiangLi,HongpingTang,Kan- [34] YanayRosen,YusufRoohani,AyushAgarwal,LeonSamo-
ran Wang, Yu Li, et al. A pathology foundation model torčan,TabulaSapiensConsortium,StephenRQuake,and
Nature,634
forcancerdiagnosisandprognosisprediction. JureLeskovec. UniversalCellEmbeddings: AFoundation
bioRxiv,pages2023–11,2023.
| (8035):970–978,2024. |     |     |     |     |     |     | ModelforCellBiology. |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
14

[35] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr [49] Joke Tommelein, Laurine Verset, Tom Boterberg, Pieter
Dollár,andRossGirshick. MaskedAutoencodersAreScal- Demetter, Marc Bracke, and Olivier De Wever. Cancer-
ableVisionLearners. InIEEEConferenceonComputerVi- associatedfibroblastsconnectmetastasis-promotingcom-
sionandPatternRecognition(CVPR),pages16000–16009, municationincolorectalcancer. FrontiersinOncology,5:
| 2022. |     |     |     |     |     |     | 63,2015. |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
[36] RandallBalestriero,MarkIbrahim,VladSobal,AriMorcos, [50] KatherineRybinski,HongxiaZImtiyaz,BarrieMittica,Brian
ShashankShekhar,TomGoldstein,FlorianBordes,Adrien Drozdowski,JamesFulmer,KeijiFuruuchi,ShawnFernando,
Bardes,GregoireMialon,YuandongTian,AviSchwarzschild, MarianneHenry,QiminChao,BradKline,etal. Targeting
Andrew Gordon Wilson, Jonas Geiping, Quentin Garrido, endosialin/CD248throughantibody-mediatedinternaliza-
Pierre Fernandez, Amir Bar, Hamed Pirsiavash, Yann Le- tion results in impaired pericyte maturation and dysfunc-
Cun,andMicahGoldblum. ACookbookofSelf-Supervised tionaltumormicrovasculature. Oncotarget,6(28):25429,
arXivpreprintarXiv:2304.12210,2023.
| Learning.                                    |              |             |                 |     |         |          | 2015.                   |                    |                             |                    |     |     |
| -------------------------------------------- | ------------ | ----------- | --------------- | --- | ------- | -------- | ----------------------- | ------------------ | --------------------------- | ------------------ | --- | --- |
| [37] Maximilian                              |              | Ilse, Jakub | Tomczak,        |     | and Max | Welling. |                         |                    |                             |                    |     |     |
|                                              |              |             |                 |     |         |          | [51] MarcoCuturi.       | SinkhornDistances: |                             | LightspeedComputa- |     |     |
| Attention-basedDeepMultipleInstanceLearning. |              |             |                 |     |         | InInter- |                         |                    |                             |                    |     |     |
|                                              |              |             |                 |     |         |          | tionofOptimalTransport. |                    | AdvancesinNeuralInformation |                    |     |     |
| national                                     | Conferenceon |             | MachineLearning |     | (ICML), | pages    |                         |                    |                             |                    |     |     |
ProcessingSystems(NeurIPS),26,2013.
2127–2136.PMLR,2018.
|           |            |          |           |     |           |            | [52] GabrielPeyré,MarcoCuturi,etal. |                                         |     | ComputationalOptimal |     |     |
| --------- | ---------- | -------- | --------- | --- | --------- | ---------- | ----------------------------------- | --------------------------------------- | --- | -------------------- | --- | --- |
| [38] Wolf | H Fridman, | Laurence | Zitvogel, |     | Catherine | Sautès-    |                                     |                                         |     |                      |     |     |
|           |            |          |           |     |           |            | Transport.                          | FoundationsandTrends®inMachineLearning, |     |                      |     |     |
| Fridman,  | and        | Guido    | Kroemer.  | The | immune    | contexture |                                     |                                         |     |                      |     |     |
11(5-6):355–607,2019.
| incancerprognosisandtreatment. |     |     |     | NatureReviewsClinical |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Oncology,14(12):717–734,2017.
|     |     |     |     |     |     |     | [53] NicolasBonneel,JulienRabin,GabrielPeyré,andHanspeter |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- |
[39] KennethCValkenburg,AmberEDeGroot,andKennethJ Pfister. SlicedandRadonWassersteinBarycentersofMea-
|     |     |     |     |     |     |     | Journal | of Mathematical |     | Imaging | and Vision, |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ------- | ----------- | --- |
Pienta. Targeting the tumour stroma to improve cancer sures. 51:
NatureReviewsClinicalOncology,15(6):366–381,
| therapy. |     |     |     |     |     |     | 22–45,2015. |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
2018.
|                                        |     |     |     |     |                   |     | [54] ZemingLin,HalilAkin,RoshanRao,BrianHie,Zhongkai |            |           |        |          |     |
| -------------------------------------- | --- | --- | --- | --- | ----------------- | --- | ---------------------------------------------------- | ---------- | --------- | ------ | -------- | --- |
| [40] TakashiSembaandTakatsuguIshimoto. |     |     |     |     | Spatialanalysisby |     |                                                      |            |           |        |          |     |
|                                        |     |     |     |     |                   |     | Zhu, Wenting                                         | Lu, Nikita | Smetanin, | Robert | Verkuil, | Ori |
currentmultiplexedimagingtechnologiesforthemolecular
|                                  |     |     |     |                         |     |     | Kabeli, Yaniv | Shmueli, | Allan dos | Santos | Costa, | Maryam |
| -------------------------------- | --- | --- | --- | ----------------------- | --- | --- | ------------- | -------- | --------- | ------ | ------ | ------ |
| characterisationofcancertissues. |     |     |     | BritishJournalofCancer, |     |     |               |          |           |        |        |        |
Fazel-Zarandi,TomSercu,SalvatoreCandido,andAlexan-
pages1–11,2024.
|                |        |       |            |     |        |         | der Rives.        | Evolutionary-scale |            | prediction | of atomic-level |     |
| -------------- | ------ | ----- | ---------- | --- | ------ | ------- | ----------------- | ------------------ | ---------- | ---------- | --------------- | --- |
|                |        |       |            |     |        |         | protein structure | with               | a language | model.     | Science,        | 379 |
| [41] Guillaume | Jaume, | Lukas | Oldenburg, |     | Anurag | Vaidya, |                   |                    |            |            |                 |     |
(6637):1123–1130,2023.
| Richard | J Chen, | Drew | FK Williamson,  |     | Thomas           | Peeters, |                   |          |        |       |              |       |
| ------- | ------- | ---- | --------------- | --- | ---------------- | -------- | ----------------- | -------- | ------ | ----- | ------------ | ----- |
| Andrew  | H Song, | and  | Faisal Mahmood. |     | Transcriptomics- |          |                   |          |        |       |              |       |
|         |         |      |                 |     |                  |          | [55] Xiang Zhang, | Lu Chen, | Wei-qi | Dang, | Mian-fu Cao, | Jing- |
guidedsliderepresentationlearningincomputationalpathol-
fangXiao,Sheng-qingLv,Wen-jieJiang,Xiao-hongYao,
ogy. InIEEEConferenceonComputerVisionandPattern
|     |     |     |     |     |     |     | Hui-minLu,Jing-yaMiao,etal. |     |     | CCL8secretedbytumor- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | -------------------- | --- | --- |
Recognition(CVPR),pages9632–9644,2024.
|              |     |           |              |     |            |      | associated      | macrophages | promotes   | invasion   | and        | stemness |
| ------------ | --- | --------- | ------------ | --- | ---------- | ---- | --------------- | ----------- | ---------- | ---------- | ---------- | -------- |
|              |     |           |              |     |            |      | of glioblastoma | cells       | via ERK1/2 | signaling. | Laboratory |          |
| [42] Candace | C   | Liu, Noah | F Greenwald, |     | Alex Kong, | Erin | F               |             |            |            |            |          |
Investigation,100(4):619–629,2020.
| McCaffrey, | Ke  | Xuan | Leow, Dunja | Mrdjen, | Bryan | J Can- |     |     |     |     |     |     |
| ---------- | --- | ---- | ----------- | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
non,JosefLorenzRumberger,SricharanReddyVarra,and
|                |         |                                      |                   |     |             |        | [56] PushpakPati,SofiaKarkampouna,FrancescoBonollo,Eva |     |     |     |     |     |
| -------------- | ------- | ------------------------------------ | ----------------- | --- | ----------- | ------ | ------------------------------------------------------ | --- | --- | --- | --- | --- |
| MichaelAngelo. |         | Robustphenotypingofhighlymultiplexed |                   |     |             |        |                                                        |     |     |     |     |     |
|                |         |                                      |                   |     |             | Nature | Compérat,MartinaRadić,MartinSpahn,AdrianoMartinelli,   |     |     |     |     |     |
| tissue         | imaging | data                                 | using pixel-level |     | clustering. |        |                                                        |     |     |     |     |     |
Communications,14(1):4618,2023. MartinWartenberg,MariannaKruithof-deJulio,andMari-
|     |     |     |     |     |     |     | annaRapsomaniki. |     | Acceleratinghistopathologyworkflows |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------------------------------- | --- | --- | --- |
[43] Gabriele Gut, Markus D Herrmann, and Lucas Pelkmans. withgenerativeAI-basedvirtuallymultiplexedtumourprofil-
Multiplexed protein maps link subcellular organization to ing. NatureMachineIntelligence,6(9):1077–1093,2024.
| cellularstates. |     | Science,361(6401):eaar7042,2018. |     |     |     |     |                                                      |     |     |     |     |     |
| --------------- | --- | -------------------------------- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|                 |     |                                  |     |     |     |     | [57] EricWu,MatthewBieniosek,ZhenqinWu,NityaThakkar, |     |     |     |     |     |
[44] Si-HongLu,Wen-SyTsai,Ying-HsuChang,Teh-YingChou, Gregory W Charville, Ahmad Makky, Christian Schürch,
See-TongPang,Po-HungLin,Chun-MingTsai,andYing- Jeroen R Huyghe, Ulrike Peters, Christopher I Li, et al.
ChihChang.Identifyingcanceroriginusingcirculatingtumor ROSIE: AI generation of multiplex immunofluorescence
cells. CancerBiology&Therapy,17(4):430–438,2016. stainingfromhistopathologyimages. bioRxiv,2024.
[45] Bing Ma, Rui Ran, Hai-Yang Liao, and Hai-Hong Zhang. [58] MarijaPizurica,YuanningZheng,FranciscoCarrillo-Perez,
Theparadoxicalroleofmatrixmetalloproteinase-11incan- Humaira Noor, Wei Yao, Christian Wohlfart, Antoaneta
Biomedicine&Pharmacotherapy,141:111899,2021.
| cer. |     |     |     |     |     |     | Vladimirova,KathleenMarchal,andOlivierGevaert. |     |     |     |     | Digi- |
| ---- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | ----- |
talprofilingofgeneexpressionfromhistologyimageswith
[46] YuanTian,MarianaBabor,JeromeLane,VeroniqueSchul-
|      |       |          |                  |     |       |            | linearizedattention. |     | NatureCommunications,15(1):9886, |     |     |     |
| ---- | ----- | -------- | ---------------- | --- | ----- | ---------- | -------------------- | --- | -------------------------------- | --- | --- | --- |
| ten, | Veena | S Patil, | Grégory Seumois, |     | Sandy | L Rosales, |                      |     |                                  |     |     |     |
2024.
| ZhengFu,GaellePicarda,JulieBurel,etal. |     |     |     |     | Uniquepheno- |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
typesandclonalexpansionsofhumanCD4effectormemory
Tcellsre-expressingCD45RA. NatureCommunications,8 [59] Sonali Andani, Boqi Chen, Joanna Ficek-Pascual, Simon
(1):1473,2017. Heinke,RubenCasanova,BernardHild,BettinaSobottka,
|     |     |     |     |     |     |     | BerndBodenmiller, |     | TumorProfilerConsortium, |     |     | ViktorH |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------------------ | --- | --- | ------- |
[47] TahaniLouhichi,HaneneSaad,MyriamBenDhiab,Sonia Koelzer,etal. HistoPlexer: Histopathology-basedProtein
medRxiv,2024.
Ziadi,andMounirTrimeche. StromalCD10expressionin MultiplexGenerationusingDeepLearning.
| breast | cancer | correlates | with | tumor | invasion | and cancer |     |     |     |     |     |     |
| ------ | ------ | ---------- | ---- | ----- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
stemcellphenotype. BMCCancer,18:1–9,2018. [60] JianlinSu,MurtadhaAhmed,YuLu,ShengfengPan,Wen
|     |     |     |     |     |     |     | Bo,andYunfengLiu.Roformer: |     |     | Enhancedtransformerwith |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ----------------------- | --- | --- |
Neurocomputing,568:127063,
[48] RaghuKalluriandMichaelZeisberg. Fibroblastsincancer. rotarypositionembedding.
NatureReviewsCancer,6(5):392–401,2006.
2024.
15

|     |     |     |     |     |     | typically |     | RGB, with | a fixed | semantic |     | meaning. | More- |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ------- | -------- | --- | -------- | ----- | --- |
[61] RuibinXiong,YunchangYang,DiHe,KaiZheng,Shuxin
Zheng, Chen Xing, Huishuai Zhang, Yanyan Lan, Liwei over, in contrast to RGB channels, which combine to
Wang,andTieyanLiu. Onlayernormalizationinthetrans- produce colors, multiplex channels convey distinct bio-
formerarchitecture.InInternationalConferenceonMachine
|     |     |     |     |     |     | logical | meanings |     | and exhibit | complex |     | interrelationships. |     |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ----------- | ------- | --- | ------------------- | --- | --- |
Learning(ICML),pages10524–10533.PMLR,2020.
|     |     |     |     |     |     | To  | address | the | unique | challenges | posed | by  | multiplex |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------ | ---------- | ----- | --- | --------- | --- |
[62] Benjamin Lefaudeux, Francisco Massa, Diana Liskovich, imaging data, we propose VirTues, an encoder-decoder
Wenhan Xiong, Vittorio Caggiano, Sean Naren, Min model based on the ViT architecture. VirTues is de-
| Xu,                    | Jieru Hu, Marta | Tintore, | Susan      | Zhang,           | Patrick La-    |        |      |               |     |            |     |                    |     |      |
| ---------------------- | --------------- | -------- | ---------- | ---------------- | -------------- | ------ | ---- | ------------- | --- | ---------- | --- | ------------------ | --- | ---- |
|                        |                 |          |            |                  |                | signed | for  | the efficient |     | processing | of  | highly-multiplexed |     |      |
| batut,                 | Daniel Haziza,  | Luca     | Wehrstedt, |                  | Jeremy Reizen- |        |      |               |     |            |     |                    |     |      |
|                        |                 |          |            |                  |                | image  | data | accommodating |     | varying    |     | numbers            | and | com- |
| stein,andGrigorySizov. |                 |          | xFormers:  | Amodularandhack- |                |        |      |               |     |            |     |                    |     |      |
able Transformer modelling library. https://github.com/ binations of measured markers. Furthermore, VirTues
facebookresearch/xformers,2022. incorporates the attribution of distinct biological mean-
[63] PascalVincent,HugoLarochelle,YoshuaBengio,andPierre- ing to each measured marker. VirTues operates on
AntoineManzagol. ExtractingandComposingRobustFea- tokenizedimagecropsofsized =128×128,cap-
|                                 |     |     |     |                    |     |        |        |         |             |     | c ×d c |            |     |      |
| ------------------------------- | --- | --- | --- | ------------------ | --- | ------ | ------ | ------- | ----------- | --- | ------ | ---------- | --- | ---- |
| tureswithDenoisingAutoencoders. |     |     |     | InIEEEConferenceon |     |        |        |         |             |     |        |            |     |      |
|                                 |     |     |     |                    |     | turing | tissue | niches. | Restricting |     | VirT   | ues’ input | to  | such |
ComputerVisionandPatternRecognition(CVPR),pages
|     |     |     |     |     |     | crops | increases | the | number | and | diversity | of  | pretraining |     |
| --- | --- | --- | --- | --- | --- | ----- | --------- | --- | ------ | --- | --------- | --- | ----------- | --- |
1096–1103,2008.
|                       |                                    |       |                           |     |     | samples       |     | while decreasing |             | the dimensionality |                  |     | per sample. |     |
| --------------------- | ---------------------------------- | ----- | ------------------------- | --- | --- | ------------- | --- | ---------------- | ----------- | ------------------ | ---------------- | --- | ----------- | --- |
| [64] DiederikPKingma. |                                    | Adam: | AMethodforStochasticOpti- |     |     |               |     |                  |             |                    |                  |     |             |     |
| mization.             | arXivpreprintarXiv:1412.6980,2014. |       |                           |     |     |               |     |                  |             |                    |                  |     |             |     |
|                       |                                    |       |                           |     |     | Tokenization. |     |                  | To preserve |                    | the biologically |     | distinct    |     |
[65] LukasHeumos,AnnaCSchaar,ChristopherLance,Anasta-
|     |     |     |     |     |     | meaning |     | of each | channel | and | allow | for a flexible |     | num- |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ------- | --- | ----- | -------------- | --- | ---- |
siaLitinetskaya,FelixDrost,LukeZappia,MalteDLücken,
DanielCStrobl,JuanHenao,FabiolaCurion,etal. Best ber of channels per image, we employ a multi-channel
practicesforsingle-cellanalysisacrossmodalities. Nature tokenization procedure16,26. Each channel is spatially
ReviewsGenetics,24(8):550–572,2023.
|             |              |         |            |     |                 | divided       | into  | patches  | of   | size d            | ×d  | =8×8,  | since      | this |
| ----------- | ------------ | ------- | ---------- | --- | --------------- | ------------- | ----- | -------- | ---- | ----------------- | --- | ------ | ---------- | ---- |
|             |              |         |            |     |                 |               |       |          |      | p                 | p   |        |            |      |
|             |              |         |            |     |                 | approximately |       | captures |      | one cell          | per | patch. | Flattening |      |
| [66] Maciej | Sypetkowski, | Morteza | Rezanejad, |     | Saber Saberian, |               |       |          |      |                   |     |        |            |      |
|             |              |         |            |     |                 | each          | patch | results  | in a | three-dimensional |     |        | grid of    | im-  |
OrenKraus,JohnUrbanik,JamesTaylor,BenMabey,Ma-
sonVictors,JasonYosinski,AlborzRezazadehSereshkeh, age tokens x ∈ RM×H×W×d 2, where M is the number
p
etal. RxRx1: ADatasetforEvaluatingExperimentalBatch of measured markers and the grid
|            |          |     |                 |     |             |        |       |        |     | H   | = W        | = d /d |             |     |
| ---------- | -------- | --- | --------------- | --- | ----------- | ------ | ----- | ------ | --- | --- | ---------- | ------ | ----------- | --- |
| Correction | Methods. | In  | IEEE Conference |     | on Computer |        |       |        |     |     |            | c      | p           |     |
|            |          |     |                 |     |             | height | resp. | width. | For | all | M markers, |        | we retrieve |     |
VisionandPatternRecognition(CVPR),pages4285–4294,
|     |     |     |     |     |     | from | a precomputed |     | lookup |     | table | the corresponding |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | ------ | --- | ----- | ----------------- | --- | --- |
2023.
|     |     |     |     |     |     | protein | embeddings |     | π   | ∈ RM×dPLM | given | by  | the PLM |     |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | --- | --------- | ----- | --- | ------- | --- |
[67] KaimingHe,XiangyuZhang,ShaoqingRen,andJianSun. (ESM-254 with 640). We refer to these em-
| Deepresiduallearningforimagerecognition.InIEEEConfer- |     |     |     |     |     |     |     |     | d = |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PLM
enceonComputerVisionandPatternRecognition(CVPR), beddings as marker tokens. For each channel m and
eachgridposition(i,j),weprojecttheimagetokenx
pages770–778,2016.
mij
|     |     |     |     |     |     | and | the | corresponding |     | marker | token | π to | the same |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ----- | ---- | -------- | --- |
[68] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, m
|               |           |     |                               |     |     | dimension |     |     | using | learnable | linear | projections, |     | to  |
| ------------- | --------- | --- | ----------------------------- | --- | --- | --------- | --- | --- | ----- | --------- | ------ | ------------ | --- | --- |
| andLiFei-Fei. | ImageNet: |     | Alarge-scalehierarchicalimage |     |     |           |     | d   |       |           |        |              |     |     |
model
database. In IEEE Conference on Computer Vision and get x′ ∈ Rdmodel and π′ ∈ Rdmodel respectively. The
|     |     |     |     |     |     |     | mij |     |     | m   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PatternRecognition(CVPR),pages248–255,2009. image and marker tokens are fused through summa-
|                                                   |     |                              |     |     |     | tion,  | resulting    | in  | the image | tokens                    | x         | ∈RM×H×W×dmodel |     | ,   |
| ------------------------------------------------- | --- | ---------------------------- | --- | --- | --- | ------ | ------------ | --- | --------- | ------------------------- | --------- | -------------- | --- | --- |
| [69] NiteshVChawla,KevinWBowyer,LawrenceOHall,and |     |                              |     |     |     |        |              |     |           |                           | (cid:101) |                |     |     |
|                                                   |     |                              |     |     |     | wherex |              |     | .         | Thefusionofthemarkertoken |           |                |     |     |
| WPhilipKegelmeyer.                                |     | SMOTE:SyntheticMinorityOver- |     |     |     |        | (cid:101)mij | =x′ | +π′       |                           |           |                |     |     |
|                                                   |     |                              |     |     |     |        |              | mij | m         |                           |           |                |     |     |
sampling Technique. Journal of Artificial Intelligence Re- with the image tokens serves two main purposes: (1)
search,16:321–357,2002. enabling VirTues to differentiate the channel origins
|     |     |     |     |     |     | of        | input | tokens,    | and (2)   | introducing |       | an inductive |          | bias |
| --- | --- | --- | --- | --- | --- | --------- | ----- | ---------- | --------- | ----------- | ----- | ------------ | -------- | ---- |
|     |     |     |     |     |     | regarding |       | the marker | function, |             | which | cannot       | be added |      |
Methods
|             |                 |               |                         |                  |               | through |           | other marker   |            | tokenization |                | schemes    | (such       | as    |
| ----------- | --------------- | ------------- | ----------------------- | ---------------- | ------------- | ------- | --------- | -------------- | ---------- | ------------ | -------------- | ---------- | ----------- | ----- |
|             |                 |               |                         |                  |               | one-hot |           | or learnable   | marker     |              | embeddings).   |            | We          | note  |
| VirTues     | architecture    |               |                         |                  |               |         |           |                |            |              |                |            |             |       |
|             |                 |               |                         |                  |               | that    | this      | is the first   | of         | many         | building       | blocks     | enabling    |       |
|             |                 |               |                         |                  |               | VirTues |           | to generalize  | across     |              | unseen         | markers.   | Further,    |       |
| Multiplexed | imaging         | data          | poses modality-specific |                  | chal-         |         |           |                |            |              |                |            |             |       |
|             |                 |               |                         |                  |               | to      | allow     | VirTues        | to capture | an           | aggregated     |            | representa- |       |
| lenges to   | the development |               | of scalable             | machine          | learning      |         |           |                |            |              |                |            |             |       |
|             |                 |               |                         |                  |               | tion    | for       | each patch,    | we         | introduce    | an             | additional |             | layer |
| algorithms. | The             | images        | represent               | high-dimensional |               |         |           |                |            |              |                |            |             |       |
|             |                 |               |                         |                  |               | of      | learnable | cell           | summary    | tokens       | c ∈RH×W×dmodel |            |             | , one |
| samples,    | characterized   | by            | a large                 | number           | of measured   |         |           |                |            |              |                |            |             |       |
|             |                 |               |                         |                  |               | for     | each      | spatial        | position.  | Each         | cell           | summary    | token       |       |
| channels    | and high        | spatial       | resolutions.            | On               | the contrary, |         |           |                |            |              |                |            |             |       |
|             |                 |               |                         |                  |               | c       | ∈Rdmodel  | is initialized |            | using        | the same       | weights.   |             |       |
| the number  | of samples      | per           | dataset                 | in terms         | of entire     | ij      |           |                |            |              |                |            |             |       |
| images      | and patients    | is relatively | small.                  | Further,         | the to-       |         |           |                |            |              |                |            |             |       |
talnumberaswellasthecombinationofchannelsvaries Masking. During training, a portion of the image
between datasets as studies use different marker pan- tokens {x } is masked by replacing them with a spe-
(cid:101)mij
els. These characteristics of the data modality hinder cial masking token □∈Rdmodel initialized with learnable
the simple off-the-shelf application of established vision weights. Masking is applied channel-wise by sampling a
architectures. Both CNNs and standard Vision Trans- masking ratio r between 60% and 100% and uni-
masking
formers require a constant number of input channels, formlyselectingthecorresponding⌈r HW⌉tokens
masking
16

to mask within the channel. We denote the resulting eachchannelm∗,wegrouptheencodedandthemasked
3DbinarymaskbyM ∈{0,1}M×H×W,wherethevalue tokens of that channel with a copy of the encoded cell
1 marks masking. Masked tokens remain linked to summary tokens:
their specific markers, which is indicated by adding the
marker tokens to the masked tokens. (cid:8) x (cid:101)m en ∗ c ij | M m∗ij =0 (cid:9) ∪{x (cid:101)m∗ij | M m∗ij =1}∪ (cid:8) c i e j nc(cid:9) .
These groups of tokens are passed individually to the
VirTues Encoder. The set of all non-masked image decoder one by one. Hence, in the decoder tokens of
tokens {x (cid:101)mij | M mij =0} and the set of cell summary differentchannelsdonotinteractwitheachother. This
tokens {c ij } is passed as an input to the VirTues En- design is intended to force the decoder to extract the
coder. This encoder is constructed by modifying the majorityoftheinformationtoreconstructeachchannel
vision transformer’s architecture28, to adapt it to work from the cell summary tokens rather than relying on
with varying input channels efficiently, and capture otherchannelsandthusincentivizetheencodertostore
marker correlations and spatial patterns separately. In a meaningful representation in these. This regrouping
contrast to standard Vision Transformers, which use further limits the individual token set sizes to 2HW,
full multi-head self-attention where all tokens attend thus allowing us to use full multi-head self-attention
pairwisetoeachother(Fig.1e), weusetwospecialized instead of marker and channel attention. Processing
sparse multi-head self-attention mechanisms, marker all tokens by the decoder’s transformer followed by the
attentionandchannelattention,(Fig.1d)akintospace linear projection yields the final grid of reconstructed
and time attention employed in video transformers33. image tokens xrec ∈RM×H×W×d
p
2.
In marker attention, only tokens which are placed at FollowingHeetal.35,wesetuptheencoder-decoder
the same spatial grid position attend to each other, framework in an asymmetric fashion, where the size of
thereby capturing inter-marker dependencies and cor- encoder is deeper than the decoder, allowing the major
relations. We denote the set of input tokens to the workloadofthemodeltorelyontheencoderratherthan
ℓ-th transformer block as (cid:8) tℓ (cid:9), where the token tℓ thedecoder. Weconstructashallowdecoderconsisting
mij mij
is associated to the m-th channel and position (i,j). In of 4 transformer blocks with full attention (in contrast
this notation, we treat the layer of cell summary tokens to16transformerblocksintheencoderwithalternating
simply as a further channel. Then, a marker attention marker and channel attention). Similar to the encoder,
transformer block computes we use 2D rotatory position embeddings60 to encode
spatial positions and pre-layer normalization61 in the
∀i∗,j∗ : (cid:110) t m ℓ+ ij 1 | j i= = i j ∗ ∗ (cid:111) =MHSA( (cid:8) t m ℓ ij | j i= = i j ∗ ∗ (cid:9) ). decoder.
whereMHSAdenotesatransformerblockwithstandard
Aggregation into niche and tissue level representa-
multi-head self-attention. In contrast, in channel atten-
tions. During inference, VirTues Encoder represents
tion, only tokens present in the same channel attend
each image crop as a grid of cell summary tokens
to each other, hence capturing spatial patterns across
tissue. Following the notation for marker attention, a
cenc ∈ RH×W×dmodel . To process an entire tissue, the
multiplexedimageisdividedintonon-overlappingcrops,
channel attention transformer block computes as
each representing a niche, which are then embedded
∀m∗ : (cid:110) tℓ+1 | m =m∗ (cid:111) =MHSA( (cid:8) tℓ | m =m∗(cid:9) ). individually. Niche or tissue level representations are
mij mij obtained by aggregating all encoded cell summary to-
kens from the crop or the full image, respectively. For
The VirTues Encoder architecture consists of a se-
unsupervised tasks, such as the retrieval experiments
quence of 16 transformer blocks, which alternate be-
in Figure 4, a simple average z = 1 (cid:80) cenc is used
tween blocks that use marker and channel attention. HW i,j ij
for aggregation, generating task-agnostic embeddings.
Each of the transformer blocks uses 8 attention heads.
In supervised settings, a dynamically weighted average
Spatial positions are encoded using 2D rotatory posi-
is employed, achieved by training an attention-based
tion embeddings60. Further, we use pre-layer normal-
multiple instance learning classifier37 on the given task
ization61.
(while the parameters of VirTues’ are kept frozen),
The VirTues Encoder outputs a set of encoded im-
generating task-specific embeddings. This attention
age tokens (cid:8) xenc | M =0 (cid:9) and a set of encoded
(cid:101)mij mij weighted average computes as
cell summary tokens (cid:8) cenc(cid:9).
ij
(cid:88)
z = a cenc
ij ij
VirTues Decoder. The VirTues Decoder is used dur- i,j
ingtrainingandinferencetoreconstructtheoriginalim- expwT(tanh(Vcenc)⊙σ(Ucenc))
age. It is comprised of a Vision Transformer28 followed a ij = (cid:80) expwT(tanh(V ij cenc)⊙σ(U ij cenc)) ,
by a single linear projection. To reconstruct the origi- i′j′ i′j′ i′j′
nal image, the encoded tokens (cid:8) x
(cid:101)m
en
i
c
j
| M
mij
=0 (cid:9), the whereU,V ∈Rdhidden×dmodel andw ∈Rdhidden arelearnable
encoded cell summary tokens (cid:8) cenc(cid:9) and the masked weights, σ is the sigmoid activation function and ⊙
ij
tokens{x | M =1}areregroupedasfollows: For indicates element-wise multiplication. In a multi-head
(cid:101)mij mij
17

setting,thiscomputationisrepeatedforeachheadwith channels randomly, and exclude them from the training
| a different     | weight | vector            | wh  | ∈Rdhidden | and      | the resulting | sample. |     |     |     |     |     |     |     |
| --------------- | ------ | ----------------- | --- | --------- | -------- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| representations |        | are concatenated. |     | Per       | default, | we use        |         |     |     |     |     |     |     |     |
4 heads.
|     |     |     |     |     |     |     | Optimization. |     | We   | train VirTues |     | for 3000 | epochs  |      |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | ------------- | --- | -------- | ------- | ---- |
|     |     |     |     |     |     |     | using AdamW64 |     | with | an effective  |     | batch    | size of | 128, |
To efficiently implement achievedbyaccumulatinggradientsover8mini-batches.
| Implementation |     | details. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
marker and channel attention, we reduce these mecha- Each epoch involves iterating over one random crop
nisms to full attention by merging either the spatial or fromeachtrainingimage. Aweightdecay,appliedtoall
channelaxisofthebatchedtokentensorwiththebatch weights except biases and Layer Normalization terms,
axis, allowing subsets of tokens that attend to each followsacosineschedulefrom0.04to0.4. Thelearning
other to be treated as independent sequences. Dur- rate is initialized with a linear warmup over 10 epochs,
ing inference without masking, this reduction leverages followedbyacosineschedulefrom2×10−4 to2×10−6.
built-in, hardware-optimized implementations of stan- Training employs automatic mixed precision. Gradients
dard self-attention. However, during training, channel- are clipped to a maximum norm of 1.0.
| wise independent |           | masking | with        | varying   | ratios   | and chan-  |          |           |         |             |          |     |            |     |
| ---------------- | --------- | ------- | ----------- | --------- | -------- | ---------- | -------- | --------- | ------- | ----------- | -------- | --- | ---------- | --- |
| nel dropout      | lead      | to      | token       | sequences | in       | the marker |          |           |         |             |          |     |            |     |
|                  |           |         |             |           |          |            | Datasets | for       | VirTues | development |          |     |            |     |
| and channel      | attention |         | blocks      | having    | variable | lengths.   |          |           |         |             |          |     |            |     |
| This variability |           | poses   | a technical | challenge |          | because    | ef-      |           |         |             |          |     |            |     |
|                  |           |         |             |           |          |            | Dataset  | curation. | For     | training    | VirTues, |     | we curated |     |
ficient built-in PyTorch attention mechanisms require four publicly available image mass cytometry datasets,
| uniform | sequence | lengths | within | a batch. | To  | avoid the |              |     |             |              |     |     |       |     |
| ------- | -------- | ------- | ------ | -------- | --- | --------- | ------------ | --- | ----------- | ------------ | --- | --- | ----- | --- |
|         |          |         |        |          |     |           | each mapping |     | the spatial | organization |     | of  | tumor | mi- |
computational overhead of adding padding tokens, we croenvironments across various cancer types and tissue
employ a dynamic re-packaging strategy in conjunction sites. The Cords et al.18 dataset contains samples of
with xFormers’62 support for block-diagonal masked non-smallcell lungcancer, Jackson etal.17 andDanen-
self-attention. Non-masked tokens within a batch are berg et al.13 focus on breast cancer tissues, and Hoch
repacked into a single sequence, preserving coherent et al.19 examines primary and metastatic melanoma
subsequencesoftokensthatbelongtothesamesample tissues. Images smaller than 256 256 pixels were
×
and channel or spatial position. A block-diagonal mask excluded, resulting in a total of 3,473 distinct images.
is generated dynamically to indicate the subsequences, Each dataset was split into an 80%-20% train-test par-
specifying which tokens can attend to each other. The tition, grouped by patient identities. For each dataset,
repacked sequence and associated mask are processed we compiled a list of markers corresponding to the im-
using xFormers’ masked self-attention implementation. age channels. We identified the amino acid sequence
|         |             |     |     |     |     |     | for each    | marker    | and      | computed | its  | ESM-254 | embed-    |     |
| ------- | ----------- | --- | --- | --- | --- | --- | ----------- | --------- | -------- | -------- | ---- | ------- | --------- | --- |
|         |             |     |     |     |     |     | ding. For   | mRNA      | markers, | we       | used | the     | sequences | of  |
| VirTues | pretraining |     |     |     |     |     |             |           |          |          |      |         |           |     |
|         |             |     |     |     |     |     | the encoded | proteins. |          |          |      |         |           |     |
VirTuesistrainedend-to-endtorecon-
Lossfunction. To evaluate the generalization ability of VirTues to
struct image crops in a masked auto-encoding frame- a new disease and tissue type, we prepared in a similar
| work35,63. | Our | reconstruction |     | loss is | the mean | squared |        |               |     |               |     |       |        |       |
| ---------- | --- | -------------- | --- | ------- | -------- | ------- | ------ | ------------- | --- | ------------- | --- | ----- | ------ | ----- |
|            |     |                |     |         |          |         | manner | an additional |     | fifth dataset |     | based | on the | study |
error between the reconstructed pixels’ intensity values of Damond et al.20, which examines pancreatic tissue
| and the | original | pixels’ | intensity | values, | i.e., |     |             |      |           |            |           |             |              |     |
| ------- | -------- | ------- | --------- | ------- | ----- | --- | ----------- | ---- | --------- | ---------- | --------- | ----------- | ------------ | --- |
|         |          |         |           |         |       |     | sections    | from | both type | 1 diabetic |           | and healthy | donors.      |     |
|         |          |         |           |         |       |     | An overview |      | of all    | used IMC   | datasets, |             | their sample |     |
=∥xrec−x∥2.
L
MAE 2 sizes in terms of patients, images and cells, as well as
|           |                |         |          |      |            |         | available | and | used annotations |     | can | be found | in  | Suppl. |
| --------- | -------------- | ------- | -------- | ---- | ---------- | ------- | --------- | --- | ---------------- | --- | --- | -------- | --- | ------ |
| Note that | this           | loss is | computed | over | all pixels | of both |           |     |                  |     |     |          |     |        |
| masked    | and non-masked |         | tokens.  |      |            |         | Table 1.  |     |                  |     |     |          |     |        |
Data augmentation. Before training, we first ran- Dataset preprocessing. For each image, intensity
domly sample from each tissue image 4N subimages of values are clipped channel-wise at the 99th percentile,
|           |     |        |       |          |        |        | followed | by a | shifted logarithm |     | transformation |     |     | with a |
| --------- | --- | ------ | ----- | -------- | ------ | ------ | -------- | ---- | ----------------- | --- | -------------- | --- | --- | ------ |
| dimension | 256 | × 256, | where | N is the | number | of 128 |          |      |                   |     |                |     |     |        |
128 crops within the tissue image. During training, size factor of 1, as commonly applied to scRNA-seq
×
|     |     |     |     |     |     |     | count data65. |     | Additionally, | a   | Gaussian | blur | filter | with |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | --- | -------- | ---- | ------ | ---- |
eachsize128×128issubsampleduniformlyatrandom
from a randomly chosen subimage. Such a hierarchical a kernel size of 3 and unit variance is used to smooth
|            |                |           |                   |              |           |           | each image.        |     | Finally, | each image |     | is self-standardized |     |     |
| ---------- | -------------- | --------- | ----------------- | ------------ | --------- | --------- | ------------------ | --- | -------- | ---------- | --- | -------------------- | --- | --- |
| two-step   | subsampling    |           | method            | approximates |           | randomly  |                    |     |          |            |     |                      |     |     |
| sampling   | crops          | uniformly | at                | random       | from      | the whole | channel-wise66,16. |     |          |            |     |                      |     |     |
| image,     | while avoiding |           | an I/O-bottleneck |              | while     | training. |                    |     |          |            |     |                      |     |     |
| We further | apply          | random    | rotations         |              | and flips | to each   |                    |     |          |            |     |                      |     |     |
Evaluation
| selected | crop. | Moreover, | to  | ensure VirTues |     | learns rep- |     |     |     |     |     |     |     |     |
| -------- | ----- | --------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
resentations robust to varying combinations of markers, VirTues model instances. In total we have 5
and enhance its ability to generalize to unseen datasets datasets, 4 of which are cancer IMC datasets18,13,17,19,
andmarkers,wealsorandomlydropupto25%ofinput while Damond et al.20 is a pancreatic tissue IMC
18

dataset. Unless stated otherwise, the default VirTues Masked reconstructions. We evaluate VirTues’ un-
model is trained on all 4 cancer IMC datasets and is derstanding of molecular tissue structure and biological
used in most experiments. To showcase the benefit of relationships between markers by assessing the recon-
trainingonmultipledatasets,wetrainasecondinstance struction ability of VirTues for three different masking
of VirTues on Danenberg et al.13 only (Fig. 3d). A strategies: independent masking, marker masking and
third instance of VirTues is trained on Cords et al.18, nichemasking. Forindependentmasking(Fig.2a,band
Danenbergetal.13 andJacksonetal.17,forbenchmark- Suppl. Figs. 1-4), we sample a masking ratio indepen-
ing performance of zero-shot VirTues on Hoch et al.19 dently for each channel in the input image, uniformly
(Fig 5d,e). Finally, as a reference baseline for the zero- between 60% and 100% and mask the corresponding
shot experiments on Damond et al.20 (Fig 5f,g), we number of patches. This strategy allows the model
train VirTues on all 5 IMC datasets. to leverage both spatial patterns and marker relation-
ships to reconstruct the masked regions, aligning with
the masking used during training. For marker masking
Comparisons and baselines. We compare VirTues (Fig. 2c,d and Suppl. Figs. 5-8), we select a single
primarily with two baselines: (1) ResNet7 and (2)
marker from the input image and mask all correspond-
CA-MAE16. We utilize a pretrained ResNet7 based
ing patches. This approach enables us to evaluate
on the approach described by Sorin et al.7. Specifi-
VirTues’ understanding of marker correlations is iso-
cally, each channel is individually embedded using the
lation of its spatial understanding. In reverse, niche
ResNet5067architecture,pretrainedonImageNet-1K68,
masking (Fig. 2e,f and Suppl. Figs. 9-12) is designed
where each channel is duplicated thrice to match the
to analyze VirTues’ understanding of spatial structures.
input dimension. The resulting ResNet50 embeddings
For each image, we sample a single masking ratio uni-
are then projected channel-wise to their 16 principal
formly between 60% and 100% and use this ratio to
components and concatenated to generate the crop
selectthecorrespondingnumberofgridpositions,where
representation. Wespecificallychoosethetop16prinic-
we mask all patches across all channels. We emphasize
ipal components, so that the final crop representation
that in all three masking strategies, channel dropout
retains approximately the same dimension as VirTues’.
is not applied during the evaluation phase. To quan-
Since ResNet is a convolutional neural network that
tify the reconstruction ability, we compute the average
generatesnichelevelrepresentationsdirectlyandisthus
mean squared reconstruction error on the test images,
unable to embed patches at the cellular level. Hence,
per dataset, marker and masking strategy (Fig. 2g and
we compare against ResNet7 only for niche-level and
Suppl. Fig. 13). In contrast to the training loss, we
tissue-level tasks. Furthermore, since it utilizes a pre-
compute the reconstruction error for the masked to-
trained network and is channel-agnostic, we also com-
kens’pixelsonlytoensurecomparabilityacrossmasking
pare against it for zero-shot tasks. Secondly, we use
strategies, despite varying relative masking ratios.
a channel-agnostic masked autoencoder proposed by
Kraus et al.16. This model adopts a multi-channel tok-
enization strategy and an encoder-decoder framework Cell level tasks. Previous work on IMC image-based
similar to VirTues, but with key differences: each chan- learning7 fails to decode cell types at a cellular scale.
nel is assigned a separate decoder, marker identities In contrast, VirTues demonstrates the ability to: (1)
are not encoded in the tokenization, and full attention identify the most common cell type within each patch
is utilized. These design choices restrict the model’s through linear probing with cell-level supervision and
capability to scale to a large number of channels, im- (2) highlight key cellular regions, such as tumor ar-
posesefficiencyissuesandhindersthemodel’sabilityto eas, contributing to cancer via spatial attention maps,
zero-shot to unseen markers or datasets. We pretrain achieved through tissue-level fine-tuning (see Fig. 3h,i).
CA-MAE16 withthereconstructionobjectiveandproce- We benchmark the performance of VirTues against
dure described in Kraus et al.16, setting the patch size CA-MAE16 in identifying the most common cell type
to 8 to capture information at the cellular scale. Fur- withinapatch,andinturntheirabilitytocapturebiolog-
ther, we train CA-MAE16 for each dataset separately icallymeaningfulsignals. Thisevaluationspansmultiple
addressing scaling issues and mitigating the computa- datasets—Cords et al.18, Danenberg et al.13, Hoch
tionalbottleneckscausedbytheunequalrepresentation etal.19 andDamondetal.20 —and,forCordsetal.18,
ofchannelsindatasets,whichwouldotherwiseleadtoa is performed at two levels of class granularity. These
disproportionateincreaseinmodelparameterswithouta datasets include pixel-wise cell instance segmentation
correspondingincreaseindata. FromFig.1e,wenotice masks and tabular single-cell annotations with pheno-
that the number of parameters in VirTues is already typelabels. Fromthismetadata,wegeneratepixel-wise
25× less than CA-MAE16 for 40 markers. CA-MAE16 cell type masks, assigning empty pixels (those without
can be used to generate both cell-level and niche-level a cell) to a separate class. Patch labels are determined
representations. For cell-level representations, we aver- by the mode of all pixel labels within each patch.
age the embedded tokens along the channel dimension. For the prediction task, we perform linear prob-
For self-supervised niche-level representations, we take ing using a logistic regression model with an L-BFGS
the average of all embedded tokens of the crop. solver and L2 regularization with coefficient λ = 1.0.
19

This ensures the evaluation focuses on the quality of Suppressed expansion, TLS-like and PDPN+ active
the learned representations rather than the complexity stroma — within a niche as binary classification tasks,
or configuration of the classifier. Since the datasets since a niche can contain multiple such regions. We
contain millions of cells, we subsample the patches by use gated attention-based multiple instance learning
randomlysampling5cropsfromeachimageinthetrain models37 (Gated ABMIL) to predict the presence of
and test cohort, and further subsampling 100 patches the structures, where the input is the set of cell-level
randomlyatuniformfromthem. Wekeepthesepatches representations (cell summary tokens) belonging within
consistentacrossVirTuesandCA-MAE16. Wedropall the niche. The ABMIL classifiers aggregate the in-
those patches which have no assigned label or have an put representations using gated-attention computed
unknown or ambiguous label. For Danenberg et al.13, over four heads, each with a hidden dimension of 256.
we regroup the highly nuanced phenotypes provided by Finally, the niche representations are projected to a
the authors into seven high-level categories, filtering single value, followed by a sigmoid activation to com-
out antigen-presenting cells. Similar, we regroup phe- pute the probability of the structure’s presence. Each
notypes provided by Hoch et al.19 into five high-level batch consists of 32 crops, and we use the Adam64
categories. The mappings to regroup the phenotypes optimizerwithlearningrateof10−4. Weuseearlystop-
canbefoundinSuppl. Tables3and4. Weavoidresam- ping, with patience of 5 epochs over the training loss.
pling strategies as applying them solely to the training For ResNet7, we employ logistic regression instead of
set did not yield noticeable performance improvements, ABMIL, as ResNet7 directly provides aggregated niche-
except for Damond et al.20, where we use SMOTE69 level representations. The logistic regression uses the
to augment the training data for the minority class, same configuration as cell-level classification tasks.
and randomly undersample exocrine cells. Each task To train and evaluate the classifiers, we generate
is treated as multi-class classification, and we report training and testing sets of labeled embedded niches as
the recall and F1-score per class. The patches are also follows: Each training and testing image is divided in
inherently imbalanced, and we show the cell counts in non-overlapping crops of size 128×128, and excess
the test set in Fig. 28. The labels for each task are as pixels at the borders of the images are disregarded.
follows: Each crop, representing a single niche, is embedded in-
dividually using VirTues and the baseline methods. We
• Primary lung cancer tissue18 (cell type, coarse): use the structure annotations available in the published
5 classes, namely tumor, fibroblast, immune, T
metadata of Danenberg et al.13 to determine the pres-
cell and vessel.
ence of the target structure in the niche. We report
the overall accuracy and macro average F1-score (to
• Primary lung cancer tissue18 (cell type, fine-
emphasize class imbalance) for each task. We report
grained): 21 classes, namely B cell, blood, CD4,
the average metrics over 5 seeded runs, and calculate
CD8, collagen CAF, HEV, hypoxic tumor, IDO
CAF, lymphatic, myeloid, neutrophil, normal tu- the P values using Mann-Whitney U test.
mor, PDPN CAF, SMA CAF, dCAF, hypoxic
CAF, hypoxic tpCAF, iCAF, mCAF, tpCAF and Tissue level classification. To evaluate the ability of
vCAF. VirTues’ representations to capture clinically meaning-
ful information about the tissue and the patient, we
• Primary breast cancer tissue13 (cell type): 7 define and benchmark various tissue-level classification
classes, namely NK, B cell, T cell, myeloid, ER+,
tasks. We derive these tasks from the clinical patient-
ER- and stromal.
level annotations available in the metadata of all five
published datasets, where each image is treated as an
• Primary and metastatic melanoma cancer tis-
independent sample. For each task, we exclude images
sue19 (cell type): 5 classes, namely lymphocytes,
withoutlabelsandomitclasseswithambiguousormiss-
macrophages, stroma, T cells, tumor.
ing descriptions. We describe the labels for each task
• Diabeticpancreas20 (celltype): 3classes,namely below:
immune, islet and exocrine.
• Primary lung cancer tissue18: (1) Cancer type:
We restrict the classes to Adenocarcinoma and
Niche level classification. Danenberg et al.13 iden- Squamous cell carcinoma, as these account for
tifies recurrent multicellular structures within breast
95% of the samples, (2) Relapse: 2 classes (Re-
tumor microenvironments and we evaluate the VirTues’
lapse, No relapse), and (3) Grade: 3 classes
ability to predict the presence of these structures us-
(cancer grade 1, 2, and 3).
ing niche-level representations. Imbalance is evident in
niche level tasks within the test set: 40.44% of niches • Primary breast cancer tissue13: (1) ER Status: 2
contain suppressed expansion regions, 17.62% contain classes (ER positive, ER negative), (2) PAM50:
TLS-like regions, and 30.38% contain PDPN+ regions. 5 classes (Normal-like, Basal, HER2, Luminal A,
Each niche level task is treated as binary classification. Luminal B), and (3) Grade: 3 classes (cancer
We treat the classification of the following structures: grade 1, 2, 3).
20

• Primary breast cancer tissue17: (1) Tumor Clin- closest retrieved match, then compare their average
ical Type: 4 classes (HR-HER2+, HR+HER2-, values to those from randomized retrieval – (1) The
HR+HER2+, Triple Negative (TN)), (2) Tumor first metric evaluates similarity based on cell type com-
Type: 2 classes (invasive ductal, not invasive duc- position by calculating the proportion of each coarse
tal), and (3) Grade: 3 classes (cancer grade 1, 2, cell type with the image using published metadata and
3). computing the L1-distance between the resulting pro-
portion vectors, and (2) the second metric assesses
• Primary and metastatic melanoma cancer tis-
molecular tissue composition by treating each image as
sue19: (1) Relapse: 2 classes (Relapse, No re-
a set of pixel vectors and calculating the sliced Wasser-
lapse), (2) Mutation: 3 classes (BRAF, NRAS,
stein distance53 between these sets. Given the pixels
wildtype),and(3)Cancerstage: 2classes(stage
x,y ∈ RP×C for two tissue images, where P is the
III, stage IV).
number of pixels in an image, the sliced Wasserstein
• Diabetic pancreas20: (1) Stage: 3 classes (on- distance is defined as
set, long-duration, non-diabetic), and (2) AAB
(cid:18)(cid:90) (cid:19)1
Status: 2 classes (negative, positive). SW (x,y)= W (proj (x),proj (y))2dθ 2 ,
2 2 θ θ
SC−1
For all tasks, we train Gated ABMIL classifiers as
prediction models, similar to the models for niche-level where proj θ denotes the projection of each row on the
tasks. In contrast to the niche-level classification, the
unit vector θ. We use the sliced Wasserstein distance
as an computationally efficient approximation of the
full set of all embedded representations — cell-level for
Wasserstein distance since the number of pixels per
VirTuesandCA-MAE16,andniche-levelforResNet7—
belonging to an image constitutes an individual sam- image P is very large.
We also performa McNemartest toanalyzeclinical
ple and an input to the ABMIL classifiers. We report
label matches. For each clinical label, we compare the
the overall accuracy and macro average F1-score (to
number of correct matches retrieved by the top three
emphasize class imbalance) for each task.
results of our Wasserstein-based retrieval method with
those from three random retrievals, reporting the re-
Information retrieval. We construct the Virtual Tis-
sulting p-values. If n are the correct matches from
suedatabaseforCordsetal.18 byextractingthecentral 1
Wasserstein-based retrieval while being incorrect from
4×4 grid of crops with each crop sized 128×128, for
random retrievals, and n be the incorrect matches
eachimage,excludingthosesmallerthanthisgrid. This 2
from Wasserstein-based retrieval while being correct
choice of grid size maximizes the tissue area captured
from random retrievals, we calculate the test-statistic,
per image while minimizing the number of excluded
which follows a chi-square distribution (with 1 DOF) as
images. Additionally, it often eliminates empty or irrele-
χ2 =(n −n )2/(n +n ),andthep-valueiscomputed
vantcornersasasideeffect. Similartotissueleveltasks, 0 1 2 1 2
as Pr(χ2 ≥ χ2), and p < 0.05 suggests a significant
we keep those images associated with Adenocarcinoma 0
difference between the retrieval methods in terms of
or Squamous cell carcinoma. The remaining crops are
clinical label matches.
embedded using VirTues or one of the baselines and
the resulting niche-level representations are stored in
the database. For VirTues and CA-MAE16, we use Zero-shot inference. We demonstrate the zero-shot
capabilityofVirTuesacrosstwoscenarios(withincreas-
self-supervised niche-level representations, computed
ing level of difficulty): (1) a new cancer type and (2)
as the average of cell-level embeddings.
a new organ and disease. In both cases, we compare
The database is used to retrieve tissues similar
zero-shotperformancewiththeperformanceofVirTues
to a given reference image, measured using the 2-
(trained), which includes the corresponding dataset in
Wasserstein distance between sets of niche-level rep-
pretraining. For zero-shot inference on a new cancer
resentations. Given the niche-level representations
type, we embed the images using markers overlapping
a,b ∈ RN×dmodel for two tissues, the Wasserstein dis-
with pretraining and use the model trained on Cords
tance computes as
etal.18,Danenbergetal.13,andJacksonetal.17. Per-
 1 formance is benchmarked on two tasks: (a) IMC image
N 2
W 2 (a,b)=m π∈ in Γ (cid:88) π ij ∥a i −b j ∥2 2  , r t e ra c i o n n in st g r , u h c i t g io h n lig ( h F t i i g n . g 5 r b e , c c o ), ns fo tr r u c c h t a io n n ne q l u s a p li r t e y s . en W t e in co p m re - -
i,j=1
pare the performance of zero-shot VirTues and trained
whereΓ= (cid:8) π ∈RN×N | π⃗1=⃗1/N and πT⃗1 =⃗1/N (cid:9). VirTues by evaluating reconstruction error in terms of
For a given reference image, we identify the closest MSE. We further benchmark VirTues (zero-shot and
matches based on this distance metric. trained) on (b) downstream cellular- and tissue-level
To evaluate the efficacy of the retrieval mechanism, tasks (Fig. 5d,e), where we also benchmark against
we compare it quantitatively across different embed- ResNet7 on tissue-level tasks.
ding methods. Specifically, we compute two alternative Additionally, we evaluate the zero-shot ability of
distance metrics between the reference image and its VirTues to reconstruct channels previously unseen dur-
21

ing pretraining. In Fig 5j and Fig 5k, we demonstrate We consider the post-softmax attention weights for all
the reconstructed images for unseen markers. We dis- channels except the cell summary token, say α
h,m′,m,i,j
tinguishbetweensupportedunseenmarkers,whichhave when marker m′ attends to marker m for head h and
closeneighboringmarkersintheESM2embeddingspace spatial position (i,j), and aggregate them across all
present in the training datasets, and isolated unseen heads and spatial positions. The final scores, termed
markers, that have no close neighboring markers in the as importance scores I , can be written as
m
training datasets. Further, in Fig 5l, we plot the recon-
(cid:88)
struction error for supported and isolated markers for ρ = α
m,m′,h h,m′,m,i,j
thethreetypesofmaskingschemes: independentmask- i,j
ing,markermasking,andnichemasking. Inallcases,we
I =
(cid:88) ρ m,m′,h −min m′ ρ m,m′,h
.
comparethereconstructionerrorswithVirTuescontain- m max ρ −min ρ
m′ m,m′,h m′ m,m′,h
m′,h
ingHochetal.19 inpretraining. Forzero-shotinference
on a new organ and disease, we use diabetic pancreas Visualization of spatial attention typically relies on
tissuedatafromDamondetal.20. WepretrainVirTues a [CLS] token. Since the pretrained VirTues inherently
on IMC images from all four cancer datasets for zero- doesnothavea[CLS]token,weaugmentVirTueswith
shot inference and benchmark performance. Similar to learnable channel summary tokens (one for each chan-
Hoch et al.19, we evaluate (a) image reconstruction nel, including the cell summary token channel), which
error (Fig. 5f) and (b) performance on downstream are spatially placed at the center of the input image.
cellular- and tissue-level tasks (Fig. 5g,h). We finetune the augmented model on the cancer type
prediction task on Cords et al.18, using the encoded
channel summary tokens of the cell summary layer to
Scaling analysis. To analyze the impact of the num-
predict the cancer type. To visualize attention maps,
ber of measured markers on both computational costs
we compute the attention scores directed from the
and prediction performance, we select nested subsets
channel summary token to the cell summary tokens in
of 10, 20 and 40 markers from the original panel of 41,
thepenultimatespatialattentionlayeranddisplaythese
from the primary lung cancer tissue dataset, based on
as a heatmap over the spatial positions.
their presumed informativeness regarding general tissue
morphology and cell type differentiation. This selec-
tion is guided by prior knowledge and domain expertise. Computing hardware and software.
However,weacknowledgethatthisprocessisinherently
subjective, as a quantitative framework to objectively We used Python (v3.12.7), PyTorch (v2.5.1, CUDA
rank markers by informativeness does not exists. For 12.1), xformers62 (v0.0.28) and scikit-learn (v1.5.2)
a full list of markers per experiment, see Suppl. Table for all experiments and analyses in the study. All exper-
2. We train instances of VirTues and CA-MAE16 on iments were conducted on a single NVIDIA A100 80
these chosen subsets on the Cords et al.18 dataset, GB GPU.
andreporttheinferencecomputationalcost,numberof
parameters, and downstream performance upon scaling
Data availability
the number of channels (Fig 1e). We measure the
computational cost c =m×t, where m is the memory
We will release all processed datasets upon publication
utilized during forward pass of a batch of 16 images,
of this work.
and t is the inference time for the batch. We allow
10 warmup runs to remove GPU startup effects, and
report the average of 100 iterations. We further report
Code availability
thedownstreamaccuracy,usingABMILforcancertype
classification, and linear probing for cell type (coarse)
All code was implemented in Python using PyTorch as
classification, on Cords et al.18.
the primary deep learning package. The source code
We further evaluated the effects of single-dataset
and Supplementary Information for VirTues is available
versus multi-dataset pretraining by training a model
at http://github.com/bunnelab/virtues.
exclusively on primary breast cancer tissues13, and as-
sessing its cell type classification performance using
class-specific F1-scores (Fig 3d). Acknowledgments
We thank Bernd Bodenmiller, Eric Lubeck, Zoe Pi-
Model inspection and visualization
ran, Benedikt von Querfurth, Lucas Pelkmans and Aviv
WeinvestigateVirTues’interpretabilityinlearningmean- Regev for discussions and for providing feedback on
ingful signals by evaluating the attention scores from our manuscript. We acknowledge support from Lena
the marker and channel attention layers in the encoder. Cords and Daniel Schulz with accessing and analyzing
We begin by examining the attention weights learned thedatasets. WeareverygratefulforAndreasKrause’s
by the first marker attention layer for an input image. support and hosting J.W., K.V. and C.B. during the
22

initialphaseofthisstudy. Iconscreatedusingresources E.J. and K.V. performed the experiments; J.W., E.J.,
from Flaticon.com. A.W., G.G. and C.B. wrote the manuscript; A.W. and
|                      |                             |                  |              | C.B. funded | the study.      | All authors approved | the final |
| -------------------- | --------------------------- | ---------------- | ------------ | ----------- | --------------- | -------------------- | --------- |
|                      |                             |                  |              | version of  | the manuscript. |                      |           |
| Author               | contributions.              |                  |              |             |                 |                      |           |
| G.G. and C.B.        | conceived                   | the study; J.W., | M.P., G.G.   |             |                 |                      |           |
|                      |                             |                  |              | Declaration | of              | interests            |           |
| and C.B.             | devised the encoder-decoder |                  | architecture |             |                 |                      |           |
| and its pretraining; | J.W.,                       | K.V. and E.J.    | curated the  |             |                 |                      |           |
datasets; J.W., E.J., K.V., G.G. and C.B. developed The authors declare no competing financial interests.
the evaluation framework and downstream tasks; J.W., No patent applications have been filed on this work.
23
