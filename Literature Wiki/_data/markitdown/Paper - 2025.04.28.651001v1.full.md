---
type: literature-note
source_note: "Papers/Paper - 2025.04.28.651001v1.full.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/2025.04.28.651001v1.full.pdf"
converter: "microsoft/markitdown"
---
bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
Cellpose-SAM: superhuman generalization for cellular segmentation
MariusPachitariu†,MichaelRariden,CarsenStringer†
HHMIJaneliaResearchCampus,Ashburn,VA,USA
† correspondenceto(pachitarium,stringerc)@janelia.hhmi.org
Modern algorithms for biological segmentation can match inter-human agreement in annotation quality.
This however is not a performance bound: a hypothetical human-consensus segmentation could reduce
error rates in half. To obtain a model that generalizes better we adapted the pretrained transformer
backbone of a foundation model (SAM) to the Cellpose framework. The resulting Cellpose-SAM model
substantially outperforms inter-human agreement and approaches the human-consensus bound. We
increasegeneralizationperformancefurtherbymakingthemodelrobusttochannelshuffling,cellsize,shot
noise,downsampling,isotropicandanisotropicblur. ThenewmodelcanbereadilyadoptedintotheCellpose
ecosystem which includes finetuning, human-in-the-loop training, image restoration and 3D segmentation
approaches. ThesepropertiesestablishCellpose-SAMasafoundationmodelforbiologicalsegmentation.
Introduction backbones (U-Net, Transformer etc [10]) were also
varied. In this study, we show that replacing computer
Themostimportantaspectofbiologicalsoftwareisthat
vision segmentation frameworks with the Cellpose
it works well in the hands of biologists. This typically
framework gives a major boost in performance in
requires good performance on new data, acquired in
foundationmodelssuchasSAM.
new experiments, possibly in new tissues or using
Foundation models like SAM do have some unique
new stains or new microscopes. Such data is often
properties. Due to being pretrained on very large
outsideoftheinputdistributionthatmodelshavebeen
datasets, these models develop representations that
trained on. Algorithm developers can make an effort
have strong inductive biases. Such biases can be
to develop models that anticipate user needs, but it
highly beneficial for out-of-distribution generalization,
is difficult to predict what new datasets will require
especially when finetuning on limited data [13, 14].
segmentation. Instead, developers may specifically
In a “best case” scenario, foundation models may
focus on methods that can be proved to generalize
“understand” what tasks they are asked to do, and
well out-of-distribution. Pursuing this goal is not
use their general purpose computations to complete
straightforward,becausemanyoftheexistingdatasets
these tasks, not unlike how a human may approach a
and challenges contain homogeneous datasets, in
new task. Metaphors aside, such models still require
whichtestimagesareverysimilartotrainimages[1,2].
mechanismsandcomputationtotransformknowledge
Successful models on these datasets are those that
into segmentations, a task that Cellpose is uniquely
can best memorize training patterns and convert that
well-suitedtoachieve.
knowledgeintosegmentations.
Thus, we designed a new Cellpose-SAM model
Converting knowledge into segmentations is not
that combines the Cellpose framework with the
straightforward. Previous versions of Cellpose excel
pretrained SAM weights, and we make it available
at this [3–5]. As we show below, they even locally1 and online2. Below, we start by describing
outperform the latest foundation models such as
the model design. Then we explain why inter-
the Segment Anything Model (SAM), that has been
annotator agreement is not a true upper bound for
recentlyadaptedtobiologicalsegmentationbymultiple
model performance, and show that a hypothetical
groups [6–9]. Models may perform better based on
“average” or “consensus” annotation has about half
their architecture, loss function and post-processing
the error rate. We show that Cellpose-SAM
steps [10]. For example, the Cellpose loss function
approaches this hypothetical bound for the Cellpose
and post-processing has often proved advantageous,
test set, while previous models do not exceed inter-
outperforming models like Stardist and Mask R-CNN
annotator agreement. From there we describe all
when trained on biological data [3, 11, 12]. Other
the augmentations that were used for Cellpose-SAM;
frameworkssuchasprompt-basedsegmentationhave
while these do not necessarily improve performance,
recently been developed in computer vision and
they allow for much more flexibility in using Cellpose-
adapted to biology [6–9], but it is unclear if these
SAM across a range of datasets. Then we show
frameworks perform as well as Cellpose, due to
difficulty interpreting benchmarks in their respective 1https://github.com/MouseLand/cellpose
studiesandbecausethetrainingstrategiesandmodel 2https://huggingface.co/spaces/mouseland/cellpose
1

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
image encoder
(ViT-L)
x4
8x8 patches,
|     |     | x2  | style | x2  |     |     |     | 256x256 images,             |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
|     |     | x2  |       | x2  |     |     |     | global attention everywhere |     |     |     |     |     |
x2
x2
image encoder
(ViT-B/L/H)
16x16 patches,
|     | 1024x1024 images,  |     | +   |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
global attention @
|     |     | 4 layers  |     | mask decoder |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conv
i m a g e
|     |     | em b | e d d ings | p ro m     | p t  |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ---------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |      |            | d e c od   | e r  |     |     |     |     |     |     |     |     |
|     |     |      | mask       | points box | text |     |     |     |     |     |     |     |     |
valid masks
Training dataset for SAM (SA-1B)
|     |     |     |     |     |     | 300,000 images, 10.2 million manual ROIs |     |     |     |     |  22, 826 images, 3.34 million manual ROIs |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- |
Figure 1: Defining and training the Cellpose-SAM model. a, Schematic of the U-net backbone used in the original Cellpose model
with skip connections and global style vector. Shown on the right is the representation of the flow vectors that Cellpose predicts as an
intermediatetomaskreconstruction. b,SchematicoftheSegmentAnythingModelthatincludesanencoderbasedonaViTbackbonewitha
fewmodifications,aswellascomplexmaskandpromptdecodersrequiredforbothtrainingandinference. c,SchematicoftheCellpose-SAM
modelcombiningacustomizedencoderbackbonebasedonSAM,withtheflowfieldpredictionandgradienttrackingofCellpose. d,Training
stagesforCellpose-SAM.e,ExampleimagesusedtotraintheoriginalSAMmodel.f,Exampleimagesandflowfieldsfortheupdatedtraining
datasetforCellpose-SAM.
that Cellpose-SAM can be adapted more quickly (Figure 1a). These vector flows can be iterated in
to new datasets, which also holds in 3D. Finally parallel at every pixel by gradient tracking to produce
we show that Cellpose-SAM can be retrained as a a set of masks. Conversely, the flow fields can be
panoptic segmentation model for joint segmentation constructed from the masks as training data for the
andsemanticclassification. neural network. By contrast, SAM predicts masks in
|     |     |     |     |     |     |     | an image | sequentially |     | one-by-one, |     | based | on prompts |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ----------- | --- | ----- | ---------- |
Results given to the algorithm either in the form of point(s),
Modeldesign a box, or text and which get further processed by
|                |                 |                  |          |          |            |           | specializedmodules[6](Figure1b).   |       |              |               |                      | Todenselypredict |               |
| -------------- | --------------- | ---------------- | -------- | -------- | ---------- | --------- | ---------------------------------- | ----- | ------------ | ------------- | -------------------- | ---------------- | ------------- |
| Our goal       | in Cellpose-SAM |                  | was      | to take  | advantage  | of        |                                    |       |              |               |                      |                  |               |
|                |                 |                  |          |          |            |           | all the                            | cells | in an image, |               | biologically-adapted |                  | versions      |
| SAM as         | a foundation    | model            |          | that was | pretrained | on a      |                                    |       |              |               |                      |                  |               |
|                |                 |                  |          |          |            |           | of SAM                             | add   | another      |               | set of               | modules          | and neural    |
| large dataset. |                 | This pretraining |          | allows   | SAM        | to learn  |                                    |       |              |               |                      |                  |               |
|                |                 |                  |          |          |            |           | networks[7–9](notshowninFigure1b). |       |              |               |                      |                  | Thisstrategy  |
| the structure  |                 | of natural       | images   | and      | this       | knowledge |                                    |       |              |               |                      |                  |               |
|                |                 |                  |          |          |            |           | for generating                     |       | dense        | segmentations |                      |                  | is cumbersome |
| can be         | beneficial      | when             | training | the      | model      | on a new  |                                    |       |              |               |                      |                  |               |
andrequirescarefultuningofmanydifferentparts.
| task. However, |     | SAM | also has | design | choices | that |     |     |     |     |     |     |     |
| -------------- | --- | --- | -------- | ------ | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
make it poorly suited for dense image segmentation. We decided to instead eliminate entirely the
We wanted to replace those weak points with the decoder modules of SAM and use the image
advantages provided by the Cellpose framework. encoder exclusively, which contains a majority of the
Briefly in Cellpose, a U-net type neural network is parameters (305M out of 312M, Figure 1c). From the
used to predict a set of vector flows, which form an encoder output, we directly predicted the vector flow
intermediate representation of the segmentation [3] fields of Cellpose, without any intermediate modules
2

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
a
|     | Style vector correlation between train and test images |     |     |     |     |     |     |                   |     | b                    |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------------------- | --- | --- | --- |
|     |                                                        |     |     |     |     |     |     | Omnipose Omnipose |     | noitalerroc naem 0.8 |     |     |     |
Cellpose Nuclei Tissuenet Livecell YeaZ phase-contrast fluorescent DeepBacs egami tset rep
1
0
| segami niart |     |     |     |     |     |     |     |     |     | 0.4 |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
0.0
|     |             |     |     |     |     |     |     |     |     |         | e e i   | e t ll Z          | ) ) Bacs  |
| --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----------------- | --------- |
|     | 05          |     |     |     |     |     |     |     |     | Cellpos | u c l u | en e ce Y e a P h | C flu o r |
|     |             |     |     |     |     |     |     |     |     |         | N i s s | L iv s e   ( s e  |  ( e e p  |
|     | 25          |     |     |     |     |     |     |     |     |         | T       | n i p o n i p o   | D         |
|     | test images |     |     |     |     |     |     |     |     |         |         | O m O m           |           |
d
| cSimulated annotations |     |     |     |     |             |     |             | Performance on Cellpose test set |         |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | ----------- | --- | ----------- | -------------------------------- | ------- | --- | --- | --- | --- |
|                        |     |     |     |     | Annotator 1 |     | Annotator 2 |                                  | = FP+FN |     | e   |     |     |
Annotator 2 to 1  to human consensus to human consensus error rate average=  TP
|     |     |     |             |     |     |     |     |     | TP+FN |     | precision | TP+FN+FP |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | ----- | --- | --------- | -------- | --- |
|     |     |     | Annotator 1 |     |     |     |     |     | ***   |     |           |          |     |
|     |     |     |             |     |     |     |     |     |       | *** |           |          | *** |
false positives (FP) n = 67 images *** UoI 5.0 @ )PA( noisicerp egareva ***
|     |     |     | false negatives (FN) |     |     |     |     | 0.8 |     |     | 1.0 |     | *** |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
human consensus
|     |     |     |     |     |     |     |     | 0.7 |     |     | 0.8 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 rotatonnA ot evitaler etar rorre
0.6
0.6
gExample segmentations from Cellpose test set
|     |     |     |     |     |     |     | Cellpose-SAM | 0.5 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
0.4
0.4
|     |     |     |     |     |     |     |     | 0.3 |     |     | f   | per image         |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |
|     |     |     |     |     |     |     |     |     |     |     | 10  | segmentation time |     |
0.2
).ces( emitnur
|     | AP@0.5=0.89 |     |     | AP@0.5=0.89 |     | AP@0.5=0.93 | AP@0.5=0.99 |     |     |     |     |     |     |
| --- | ----------- | --- | --- | ----------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- |
0.1
1
0.0
|     |             |     |     |             |     |             |             |  2          | u s e cyto3 M e ll | M      |     |                           |      |
| --- | ----------- | --- | --- | ----------- | --- | ----------- | ----------- | ----------- | ------------------ | ------ | --- | ------------------------- | ---- |
|     |             |     |     |             |     |             |             | to r n      | s e ) CellS A C    | se-S A |     |                           |      |
|     |             |     |     |             |     |             |             | t a s e     | m a t A M          |        |     |                           |      |
|     |             |     |     |             |     |             |             | nn o o n ti | o s S o            |        | 0.1 |                           |      |
|     |             |     |     |             |     |             |             | A  c e s    | l p el lp          |        |     |                           |      |
|     |             |     |     |             |     |             |             | a n ( C     | e l C              |        |     | 200                       | 1000 |
|     |             |     |     |             |     |             |             | hu m        |                    |        |     | # of pixels per dimension |      |
|     | AP@0.5=0.92 |     |     | AP@0.5=0.86 |     | AP@0.5=0.96 | AP@0.5=0.97 |             |                    |        |     |                           |      |
Figure2: Performancerelativetoothermethodsandtohumans. a,Simulatedannotationstoillustratehuman-to-humanvariabilityand
thehumanconsensusasahypotheticalabsoluteboundonperformance.b,PerformanceontheupdatedCellposetestsetshownaserrorrates
(left)andaverageprecision(right). Per-imagesegmentationtimeonanA100GPU(bottom). c,ExamplesegmentationsofCellpose-SAM,
takenfromtheupdatedCellposetestset.
(Figure 1c). In addition, we made a few modifications DeepBacs, Neurips 2022, MoNuSeg, MoNuSAC,
to the encoder itself. The default 1024x1024 image CryoNuSeg, NuInsSeg, BCCD, CPM 15+17, TNBC,
inputs and 16x16 patch sizes of SAM were designed LynSec, IHC TMA, CoNIC, PanNuke [1–3, 17–36]
for high-resolution photographs [6, 15]. We reduced (Figure 1df, Figure S1). We continued to use
this to 256x256 and 8x8, which required us to adapt the Cellpose3 mixing probabilities for down-weighting
the position embeddings and patch embedding filters homogeneousdatasetswithmanyimages[5].
| via                                          | appropriate |             | subsampling. |         | These     | modifications |         |                 |                |            |           |                   |         |
| -------------------------------------------- | ----------- | ----------- | ------------ | ------- | --------- | ------------- | ------- | --------------- | -------------- | ---------- | --------- | ----------------- | ------- |
| improvedruntimeperformanceandensuredthatmore |             |             |              |         |           |               |         | Modelvalidation |                |            |           |                   |         |
| computation                                  |             | is          | dedicated    | to each | region    | of the        | image.  |                 |                |            |           |                   |         |
|                                              |             |             |              |         |           |               |         | Since we        | are especially | interested |           | in generalization |         |
| We                                           | also        | reverted    | the          | local   | attention | layers        | of the  |                 |                |            |           |                   |         |
|                                              |             |             |              |         |           |               |         | performance,    | we wanted      | to         | choose    | a test            | dataset |
| custom                                       | ViT         | transformer |              | from    | SAM back  | to the        | default |                 |                |            |           |                   |         |
|                                              |             |             |              |         |           |               |         | in which        | images are     | relatively | different | from              | those   |
globalattentionofViT-L,withalmostnoruntimepenalty
|     |     |     |     |     |     |     |     | in the training | set. To | determine |     | this, we | extracted |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | --------- | --- | -------- | --------- |
[16].
|     |     |     |     |     |     |     |     | feature vectors | that describe |     | the styles | of  | images [5, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | --- | ---------- | --- | ---------- |
Despite making these modifications, we were still 10, 37], and correlated them between pairs of images
able to initialize Cellpose-SAM with the SAM weights (Figure 2a). In most datasets, the style vectors were
pretrained on the SA-1B dataset [6] (Figure 1de). The highly-correlatedbetweenallpairsoftrain/testimages
model was then trained on an updated dataset of (Figure 2b), matching our subjective experience of
cells and nuclei containing 22,826 train images with theseimages. TheCellposedatasetalonecontaineda
a combined 3,341,254 training ROIs. This dataset highamountofvariabilitybetweentrain/testexemplars,
combinesmajorcurrentlyavailabledatasets: Cellpose, leading to low correlations between the styles of
CellposeNuclei,Omnipose,TissueNet,LiveCell,YeaZ, train/test images. We therefore chose to focus our
3

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
benchmarkingeffortsontheCellposetestset. computations;2)thepost-processingtimesaccountfor
Before we evaluate performance, we must set a substantial fraction of the runtime; 3) Cellpose-SAM
our expectations. In general computer vision doesnotneedtomaketwopassesforeveryimagelike
applications, improvements on the order of a few Cellpose 1/2/3, which need to first estimate the sizes
percent can be considered major steps [38–40], of cells using a size model. As we describe below,
and comparisons to human performance can help Cellpose-SAMrunsnativelyonimagesatawiderange
in setting targets for improvement [41]. Previous ofresolutions.
biological segmentation models, including Cellpose, We also evaluated the performance of Cellpose-
have described performance as matching inter- SAMonotherpublicdatasetsthatweusedfortraining.
annotatoragreement[4,7,42],whichisdefinedasthe All of these datasets are much more homogeneous
“performance” of one annotator when benchmarked than Cellpose, thus providing more images of the
against another (Figure 2c). While this can be a same type for training, and a much higher chance
usefulreference,itisnotatrueupperbound,because that images in the test set are similar to those in the
bothannotatorsmakemistakes. Carefulconsideration training set (Figure 2a, Figure S1). Thus, models
shows that if we model each annotator as making areevaluatedmainlyfortheirin-samplegeneralization,
errors randomly starting from the same underlying and even models trained from scratch (like previous
ground truth or “human consensus”, then the number versions of Cellpose) can perform well given enough
of errors for inter-annotator comparisons is less than trainingdata. Cellpose-SAMoutperformedormatched
twice as large as that between each annotator and othermodelsonalldatasets,buttheperformancegaps
the human consensus, and approaches the two-fold were typically smaller than those we reported above
limit when the errors are relatively small (Figure 2c, on the Cellpose test set Figure S2. We conclude
see Methods for exact calculations). Thus, setting thatCellpose-SAMespeciallyshinesonout-of-sample
the human consensus estimate for errors at half the generalization, which is likely also the crucial property
inter-annotatorrateresultsinaperformanceboundon neededbyusersapplyingittotheirowndata.
performance that automated models may be able to
reach. Invarianceandrobustness
To determine the inter-annotator variability we To further drive our goal of increasing generalization,
relabeled the Cellpose test set using a different we were able to make the model robust to common
annotator. RelativetotheoriginalAnnotator1,theerror imagemanipulationswithoutlossofperformance,thus
rate of Annotator2 was 0.257 (Figure 2d). Halving simplifyingtheuserexperience. Forexample,usersof
this error rate gives the human consensus estimate at Cellpose previously had to indicate which channel of
0.128. Previous models, like Cellpose3 and CellSAM an image represents the nucleus, and which channel
approach the inter-annotator error rates, at 0.292 represents a cytoplasmic or membrane marker. While
and 0.328 respectively (Figure 2d). Cellpose-SAM this is not in itself an onerous task, it can lead
however, achieves error rates of 0.163, substantially to some confusion, especially when benchmarking
below inter-annotator agreement, and approaching againstCellpose,withsomepublicchallengesexplicitly
the human consensus estimate. Note this was designed to break the order of image channels by
possibledespitethemodelsbeingtrainedondatafrom random channel permutations [22]. Thus, we trained
Annotator1 exclusively. Rather than being “fooled” Cellpose-SAMtobeentirelychannelorderinvariant,by
by the occasional errors of Annotator1, Cellpose- randomlypermutingchannelsattraintime(Figure3a).
SAM reverts to its inductive biases to selectively learn Notethisdoeseffectivelywithholdinformationfromthe
the generalizable structure in the data. We can model: specifically information about which channel
draw similar conclusions using the average precision represents which stain. Nonetheless, Cellpose-
@ 0.5 intersection-over-union (AP @ 0.5 IoU) score SAM had no performance loss from this modification
(Figure 2e). While this metric is more widely used (Figure3a). Similarly,usersofCellposepreviouslyhad
than the error rate, it does not scale linearly with to indicate the average cell diameters in an image, or
the number of errors, so we cannot easily estimate rely on a built-in size estimation method. This also
the human consensus bound. Finally, we measured led to confusion in benchmarks by other studies [22],
runtime performance (Figure 2f, Table S1). Despite and we therefore trained Cellpose-SAM at a range
having50xmoreparametersthanCellpose, Cellpose- of image diameters ranging from 7.5 pixels to 120
SAM is the fastest of the models considered here pixels. At test time, Cellpose-SAM runs natively on
whenbenchmarkedonaper-imagebasis. Thisisdue the provided images without resizing, and maintains
to a few factors: 1) modern GPUs have specialized its high-performance, with a small performance loss
tensor cores that can vastly accelerate transformer atsmallcelldiameters,whereinformationiseffectively
4

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
| ainvariance to channel order |     |              |              | binvariance to size |     |     |                  |     |
| ---------------------------- | --- | ------------ | ------------ | ------------------- | --- | --- | ---------------- | --- |
|                              |     | ground-truth | 1.00         |                     |     |     | 1.0 Cellpose-SAM |     |
|                              |     |              | UoI 5.0 @ PA |                     |     |     | UoI 5.0 @ PA     |     |
0.75
|     |     |     | 0.50 |     |     |     | 0.5 |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Cellpose-SAM
|     |     |     | 0.25 |     |     |     |     | Cellpose |
| --- | --- | --- | ---- | --- | --- | --- | --- | -------- |
cyto3
CellSAM
|     |     |     | 0.00 |                |     |     | 0.0      |       |
| --- | --- | --- | ---- | -------------- | --- | --- | -------- | ----- |
|     |     |     | RGB  | BRG GBR Random |     |     | 10 15 30 | 60 90 |
RGB BRG GBR cell diameter=10px 30px 90px cell diameter (pixels)
| crobustness to Poisson noise |        |      |              | drobustness to pixel size |            |      |                     |      |
| ---------------------------- | ------ | ---- | ------------ | ------------------------- | ---------- | ---- | ------------------- | ---- |
|                              |        |      | 1.0          | Cellpose-SAM              |            |      | 1.0 Cellpose-SAM    |      |
|                              |        |      |              | -- cyto3+denoising        |            |      | -- cyto3+upsampling |      |
|                              |        |      | UoI 5.0 @ PA |                           |            |      | UoI 5.0 @ PA        |      |
|                              |        |      | 0.5          |                           |            |      | 0.5                 |      |
|                              |        |      |              | cyto3                     |            |      | cyto3               |      |
|                              |        |      |              | CellSAM                   |            |      | CellSAM             |      |
|                              |        |      | 0.0          |                           |            |      | 0.0                 |      |
|                              |        |      |              | low medium high           |            |      | low medium          | high |
|                              |        |      |              | noise                     |            |      | pixel size          |      |
| low                          | medium | high |              |                           | low medium | high |                     |      |
Cellpose-SAM
| erobustness to blur |        |      |              | f                   | robustness to anisotropic blur |      |                          |      |
| ------------------- | ------ | ---- | ------------ | ------------------- | ------------------------------ | ---- | ------------------------ | ---- |
|                     |        |      | 1.0          | Cellpose-SAM        |                                |      | 1.0 -- cyto3+anisotropic |      |
|                     |        |      |              | -- cyto3+deblurring |                                |      | deconvolution            |      |
|                     |        |      | UoI 5.0 @ PA |                     |                                |      | UoI 5.0 @ PA             |      |
|                     |        |      | 0.5          |                     |                                |      | 0.5                      |      |
|                     |        |      |              | cyto3               |                                |      | cyto3                    |      |
|                     |        |      |              | CellSAM             |                                |      | CellSAM                  |      |
|                     |        |      | 0.0          |                     |                                |      | 0.0                      |      |
|                     |        |      |              | low medium high     |                                |      | low medium               | high |
| low                 | medium | high |              | blur                | low medium                     | high | anisotropic blur         |      |
.
Figure 3: Quality of life improvements for Cellpose-SAM. a, Cellpose-SAM is invariant to channel order, because it was trained with
channelshuffling. b,Cellpose-SAMismostlyinvarianttoimageresizingbecauseitwastrainedwithawiderangeofimageaugmentations.
NotethatpreviousCellposeversionsreliedonanintermediatesizepredictionmodel.c-f,Cellpose-SAMisrobusttocPoissonnoise,dblurring,
eimagedownsamplingandfanisotropicblur,becauseitwastrainedonsuchimages. NotethatthepreviousversionofCellposereliedon
intermediateimagerestorationmodelstoachievesimilarperformance.
| lostbydownsampling(Figure3b). |     |     |     |     | segmentationpipeline. |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
To further take advantage of the high capacity FinetuningCellpose-SAMin2Dand3Dandfor
| of Cellpose-SAM, | we  | trained | it on a | set of image |     |     |     |     |
| ---------------- | --- | ------- | ------- | ------------ | --- | --- | --- | --- |
othertasks
| degradations | that are | common | in microscopy, | and |     |     |     |     |
| ------------ | -------- | ------ | -------------- | --- | --- | --- | --- | --- |
which we previously used in the Cellpose3 study. NextwewantedtotesttheintegrationofCellpose-SAM
Specificallythesedegradationsaretheadditionofper- with other aspects of the Cellpose framework, such
pixel noise (“shot noise”), downsampling or increasing as the finetuning and human-in-the-loop capabilities.
pixel size and (an)isotropic blurring (Figure 3c-f). Comparedtoinference,trainingandfinetuninganeural
Previously we had found that an additional image network can require considerable more hardware
restoration step was required on such images for best resources. Forexample,othermethodslikemicroSAM
performance [5]; directly predicting the segmentation have quoted computational concerns as preventing
from the noisy image was inferior for the U-Net a human-in-the-loop approach for their SAM-based
based version of Cellpose. The additional restoration model [8]. We do not find similar concerns when
step was however not required for Cellpose-SAM. testing Cellpose-SAM, due to our customizations
Across all types of image alteration, the Cellpose- enabling the model to run on low resolution images.
SAM model performed as well as our best previous We find that it is always possible to train Cellpose-
imagerestorationmodels(Figure3c-f). Notethatthese SAM with a batch size of one, even on GPUs
restoration models are individually trained for each with relatively low VRAM (8-12 GB) Table S2. To
type of image degradation, while a single Cellpose- test finetuning performance, we analyze a series of
SAM model was used for all the benchmarks in this datasets that we did not use for training, specifically
entire study. Thus, Cellpose-SAM can run out-of-the- BlastoSPIM [43] and PlantSeg [44]. These datasets
box on images that have been acquired with varying contain 3D annotations, from which we can extract
levels of image degradation, at different pixel sizes or both 2D ground-truth, and 3D ground-truth. From
in arbitrary channel order, substantially simplifying the the PlantSeg categories, we used the “lateral root”
logistics typically associated with setting up an image and “ovules” datasets which contained higher-quality
5

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
| a BlastoSPIM (Nunley et al 2024) |                       |     |     |              |     |     | 3D segmentation w/ 2D model |     |                       |     |     |                  |     |     |
| -------------------------------- | --------------------- | --- | --- | ------------ | --- | --- | --------------------------- | --- | --------------------- | --- | --- | ---------------- | --- | --- |
| # of train ROIs = 0              | # of train ROIs = 333 |     |     | 0.8          |     |     |                             |     |                       |     |     | 1.0              |     |     |
|                                  |                       |     |     |              |     |     | # of train ROIs = 0         |     | # of train ROIs = 333 |     |     |                  |     |     |
|                                  |                       |     |     | UoI 5.0 @ PA |     |     |                             |     |                       |     |     | UoI 5.0 @ PA 0.8 |     |     |
0.6
0.6
0.4
|     |             |     |             |     | Cellpose-SAM   |     |     |             |     |             |     | 0.4 | Cellpose-SAM   |     |
| --- | ----------- | --- | ----------- | --- | -------------- | --- | --- | ----------- | --- | ----------- | --- | --- | -------------- | --- |
|     |             |     |             | 0.2 | Cellpose cyto3 |     |     |             |     |             |     | 0.2 | Cellpose cyto3 |     |
|     | AP@0.5=0.50 |     | AP@0.5=0.82 |     |                |     |     |             |     |             |     |     |                |     |
|     |             |     |             | 0.0 |                |     |     | AP@0.5=0.58 |     | AP@0.5=0.89 |     | 0.0 |                |     |
|     |             |     |             |     | 0 101 102      | 103 |     |             |     |             |     | 0   | 101 102        | 103 |
bPlantSeg: lateral root (Wolny et al 2020) # of training ROIs # of training ROIs
|                     |                       |     |             |     |           |         | # of train ROIs = 0 |             | # of train ROIs = 366 |             |     |     |         |         |
| ------------------- | --------------------- | --- | ----------- | --- | --------- | ------- | ------------------- | ----------- | --------------------- | ----------- | --- | --- | ------- | ------- |
| # of train ROIs = 0 | # of train ROIs = 366 |     |             | 0.8 |           |         |                     |             |                       |             |     | 0.8 |         |         |
|                     |                       |     |             | 0.6 |           |         |                     |             |                       |             |     | 0.6 |         |         |
|                     |                       |     |             | 0.4 |           |         |                     |             |                       |             |     | 0.4 |         |         |
|                     |                       |     |             | 0.2 |           |         |                     |             |                       |             |     | 0.2 |         |         |
|                     | AP@0.5=0.19           |     | AP@0.5=0.64 |     |           |         |                     |             |                       |             |     |     |         |         |
|                     |                       |     |             | 0.0 |           |         |                     | AP@0.5=0.35 |                       | AP@0.5=0.64 |     | 0.0 |         |         |
|                     |                       |     |             |     | 0 101 102 | 103 104 |                     |             |                       |             |     | 0   | 101 102 | 103 104 |
c PlantSeg: ovules (Wolny et al 2020)
| # of train ROIs = 0 | # of train ROIs = 406 |     |             |     |           |     |                     |             |                       |             |     |     |         |     |
| ------------------- | --------------------- | --- | ----------- | --- | --------- | --- | ------------------- | ----------- | --------------------- | ----------- | --- | --- | ------- | --- |
|                     |                       |     |             | 0.8 |           |     | # of train ROIs = 0 |             | # of train ROIs = 406 |             |     | 0.8 |         |     |
|                     |                       |     |             | 0.6 |           |     |                     |             |                       |             |     | 0.6 |         |     |
|                     |                       |     |             | 0.4 |           |     |                     |             |                       |             |     | 0.4 |         |     |
|                     |                       |     |             | 0.2 |           |     |                     |             |                       |             |     | 0.2 |         |     |
|                     | AP@0.5=0.65           |     | AP@0.5=0.88 |     |           |     |                     |             |                       |             |     |     |         |     |
|                     |                       |     |             | 0.0 |           |     |                     | AP@0.5=0.65 |                       | AP@0.5=0.69 |     | 0.0 |         |     |
|                     |                       |     |             |     | 0 102 103 | 104 |                     |             |                       |             |     | 0   | 102 103 | 104 |
Figure4: Finetuningperformance. a,Cellpose-SAMsegmentationsontheBlastoSPIMdataset[43]either(left)out-of-the-boxor(center)
after finetuning with a medium number of manually-annotated ROIs. (right) Performance as a function of the number of training ROIs for
Cellpose-SAMandCellpose3.b-c,Sameasaforthe“lateralroot”and“ovules”categoriesofthePlantSegdataset[44].d-f,3Dsegmentations
extendedfrom2DpredictionsusingeitherCellpose-SAMorCellpose3. The3DextensionwasmadeusingtheflowaveragingmethodonXY,
XZandYZslicesfrom[3].Samedatasetswereusedasina-c.
|     |     |     |     |     |     |     |     |     |     | Figure | 5:  | Finetuning | Cellpose- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---------- | --------- | --- |
MoNuSAC 2020 challenge: segmentation and classification SAM for panoptic segmentation.
acell classes:
|            |     |     |     |     | *** |     |     | *** |     | a,         | Representative |                | examples     | from      |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | -------------- | ------------ | --------- |
| epithelial |     |     |     | b   | **  |     | c   | *** |     |            |                |                |              |           |
| lymphocyte |     |     |     |     | *** |     |     | **  |     | the        | MoNuSac        |                | 2020         | challenge |
| macrophage |     |     |     |     | *** |     |     | *** |     |            |                |                |              |           |
| neutrophil |     |     |     | 0.8 |     |     | 1.0 |     |     | containing |                | four different | cell         | classes.  |
|            |     |     |     |     |     |     |     |     |     | b,         | Segmentation   | error          | rate         | averaged  |
|            |     |     |     |     |     |     |     |     |     | across     | classes        | for            | Cellpose-SAM |           |
|            |     |     |     |     |     |     | 0.8 |     |     | and        | four           | leading        | algorithms   | from      |
0.6
|     |     |     |     |     |     |     |     |     |     | the | challenge | (n=85 | test | images, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ---- | ------- |
UoI 5.0 @ etar rorre
|     |     |     |     |     |     |     | UoI 5.0 @ PA |     |     | Wilcoxon                | signed-rank |     | test). | c, Same |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ----------------------- | ----------- | --- | ------ | ------- |
|     |     |     |     |     |     |     | 0.6          |     |     | asbforaverageprecision. |             |     |        |         |
0.4
0.4
0.2
0.2
|     |     |     |     | 0.0             |     |        | 0.0             |     |        |     |     |     |     |     |
| --- | --- | --- | --- | --------------- | --- | ------ | --------------- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     | Cellpose P   L1 | PL2 | PL3 L2 | Cellpose P   L1 | PL2 | PL3 L2 |     |     |     |     |     |
|     |     |     |     | SAM             |     |        | SAM             |     |        |     |     |     |     |     |
segmentations. Across datasets, Cellpose-SAM available for training, good inductive biases are no
provided a better starting point for finetuning than longernecessary, andmodelswithlessgeneralization
the cyto3 model and finetuned equally fast or faster, capacitycanstillperformwell.
| both in | 2D (Figure  | 4a-c) | and       | in 3D    | (Figure | 4d-  |     |            |        |      |              |     |     |       |
| ------- | ----------- | ----- | --------- | -------- | ------- | ---- | --- | ---------- | ------ | ---- | ------------ | --- | --- | ----- |
|         |             |       |           |          |         |      |     | Generalist | models | like | Cellpose-SAM |     | are | often |
| f). The | performance | gap   | generally | narrowed |         | with |     |            |        |      |              |     |     |       |
more training data (Figure 4acdf) but in some cases good initializations for other image-based tasks. To
|           |               |     |               |     |     |       | demonstrate |     | this, | we chose |     | the MoNuSAC |     | 2020 |
| --------- | ------------- | --- | ------------- | --- | --- | ----- | ----------- | --- | ----- | -------- | --- | ----------- | --- | ---- |
| persisted | (Figure 4be). |     | The narrowing |     | gap | again |             |     |       |          |     |             |     |      |
illustrates the specific strengths of Cellpose-SAM: the challenge [24], where participants were asked to
model is especially good at generalizing with zero- segment cells in histopathology images and classify
|                 |       |      |        |         |      |     | them       | into | four classes:  |     | epithelial, |      | lymphocyte, |         |
| --------------- | ----- | ---- | ------ | ------- | ---- | --- | ---------- | ---- | -------------- | --- | ----------- | ---- | ----------- | ------- |
| shot or limited | data. | When | enough | labeled | data | is  |            |      |                |     |             |      |             |         |
|                 |       |      |        |         |      |     | macrophage |      | and neutrophil |     | (Figure     | 5a). | This        | task is |
6

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
often referred to as ”panoptic segmentation”. After thank the authors of [1–3, 17–36, 43, 44] for sharing
| training,   | a Cellpose-SAM-based |               |     | model |        | outperformed |       | theirdatasets. |     |     |     |     |     |     |     |
| ----------- | -------------------- | ------------- | --- | ----- | ------ | ------------ | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| the winners | of                   | the challenge |     | both  | before | and          | after |                |     |     |     |     |     |     |     |
the deadline, on nearly all types of cells, and Dataavailability
substantially increased the classification accuracy The‘cyto2’datasetispubliclyavailableathttps://ww
| overall | (Figure | 5b). | This | example |     | shows | what |                         |     |     |     |     |           |          |     |
| ------- | ------- | ---- | ---- | ------- | --- | ----- | ---- | ----------------------- | --- | --- | --- | --- | --------- | -------- | --- |
|         |         |      |      |         |     |       |      | w.cellpose.org/dataset, |     |     |     | and | the other | datasets |     |
generalist or “foundational” models can achieve when were generated and shared by other labs [1, 2, 17–
| simply | trained | on new | tasks | with | minimal | additional |     |     |     |     |     |     |     |     |     |
| ------ | ------- | ------ | ----- | ---- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
36,43,44].
effortrequired.
Codeavailability
Discussion
Cellpose-SAMwasusedtoperformallanalysesinthe
| Here we     | have                | shown       | that | Cellpose-SAM |      |           | can     |                                    |          |           |            |           |            |             |        |
| ----------- | ------------------- | ----------- | ---- | ------------ | ---- | --------- | ------- | ---------------------------------- | -------- | --------- | ---------- | --------- | ---------- | ----------- | ------ |
|             |                     |             |      |              |      |           |         | paper.                             | The code | and GUI   | are        | available |            | at https:// |        |
| generalize  | out-of-distribution |             |      | to a         | wide | range     | of test |                                    |          |           |            |           |            |             |        |
|             |                     |             |      |              |      |           |         | www.github.com/mouseland/cellpose. |          |           |            |           |            | An          | online |
| images,     | obtaining           | performance |      | that         | is   | close     | to the  |                                    |          |           |            |           |            |             |        |
|             |                     |             |      |              |      |           |         | version                            | of the   | algorithm | is running |           | on Hugging |             | Face   |
| theoretical | bound.              | This        | was  | achieved     | by   | combining | a       |                                    |          |           |            |           |            |             |        |
https://huggingface.co/spaces/mouseland/
pretrained foundation model (SAM), which has strong cellpose. Scripts for recreating the analyses in the
inductive biases due to the broad knowledge built-in figureswillbeavailableathttps://github.com/Mou
| to its weights |     | [6], with | the Cellpose |     | framework, |     | which |     |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ------------ | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
seLand/cellpose/tree/main/paper/cpsam.
| is especially | well-suited |         | for converting |     | knowledge           |     | into |     |     |     |     |     |     |     |     |
| ------------- | ----------- | ------- | -------------- | --- | ------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| segmentations |             | [3]. To | demonstrate    |     | out-of-distribution |     |      |     |     |     |     |     |     |     |     |
Methods
| generalization,   |             | we used | the          | Cellpose | test     | dataset | and    |               |       |                |            |              |          |           |       |
| ----------------- | ----------- | ------- | ------------ | -------- | -------- | ------- | ------ | ------------- | ----- | -------------- | ---------- | ------------ | -------- | --------- | ----- |
|                   |             |         |              |          |          |         |        | The Cellpose  |       | code library   | is         | implemented  |          | in Python |       |
| multiple          | annotators. | This    | dataset      |          | uniquely | has     | a high |               |       |                |            |              |          |           |       |
|                   |             |         |              |          |          |         |        | 3 [54],       | using | pytorch,       |            | numpy,       | scipy,   | opencv,   |       |
| dissimilarity     | between     |         | train        | and test | images,  |         | due to |               |       |                |            |              |          |           |       |
|                   |             |         |              |          |          |         |        | imagecodecs,  |       | tifffile,      | fastremap, |              | and tqdm | [55–62].  |       |
| being constructed |             | as      | a generalist |          | dataset. | As      | such,  |               |       |                |            |              |          |           |       |
|                   |             |         |              |          |          |         |        | The graphical |       | user interface |            | additionally |          | uses      | PyQt, |
performanceonthetestsetindicatesout-of-distribution
generalization. This property, we believe, is the main pyqtgraph, and superqt [63–65]. The figures were
madeusingmatplotlibandjupyter-notebook[66,67].
| indicator | of how | well a | segmentation |     | method | will | work |     |     |     |     |     |     |     |     |
| --------- | ------ | ------ | ------------ | --- | ------ | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
inthehandsofitsend-users.
Cellpose-SAMnetwork
| Looking | ahead, | Cellpose-SAM |     |     | can | be used | as  |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------ | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a basis for many different biological applications. Modelarchitecture
| We have | shown | here | that | the model |     | can be | easily |     |     |     |     |     |     |     |     |
| ------- | ----- | ---- | ---- | --------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
WeusedacustomizedversionoftheViT-Ltransformer
finetuned, and that it can be extended to 3D from the Segment Anything Model [6], which has
| segmentation. |     | Similarly, | 3D  | segmentations |     |     | can be |           |     |              |     |           |     |     |       |
| ------------- | --- | ---------- | --- | ------------- | --- | --- | ------ | --------- | --- | ------------ | --- | --------- | --- | --- | ----- |
|               |     |            |     |               |     |     |        | 24 blocks | and | an embedding |     | dimension |     | of  | 1024. |
extended to 4D (including time) using other methods Each block contains the standard attention and MLP
[45–47]. The model can also be used on images with layers, common to most transformers. We used an
| more than | three | channels, | such | as  | those | arising | from |            |         |         |     |               |     |     |     |
| --------- | ----- | --------- | ---- | --- | ----- | ------- | ---- | ---------- | ------- | ------- | --- | ------------- | --- | --- | --- |
|           |       |           |      |     |       |         |      | input size | 256x256 | instead |     | of 1024x1024, |     | and | we  |
in-situ sequencing experiments, from “cell painting” or reduced the image patch size from 16x16 to 8x8. To
other multi-stain or multi-antibody methods [48, 49], this we add simple input and output operations to
by replacing its three-channel inputs and retraining. convert from pixel space to patch space and back
The outputs can also be repurposed, for example for again. Since the SAM model already had strided
| classification, |     | as we | have | shown | here | [24]. | More |                     |     |     |       |       |      |       |     |
| --------------- | --- | ----- | ---- | ----- | ---- | ----- | ---- | ------------------- | --- | --- | ----- | ----- | ---- | ----- | --- |
|                 |     |       |      |       |      |       |      | input convolutions, |     | we  | adapt | these | from | 16x16 | to  |
generally, any task that used previous versions of our 8x8 patch size by downsampling. The position
Cellpose can now use Cellpose-SAM for a boost in embeddings from SAM were also downsampled by a
| performance |     | [50–53]. | We especially |     | expect | the | boost |           |          |            |     |     |           |     |        |
| ----------- | --- | -------- | ------------- | --- | ------ | --- | ----- | --------- | -------- | ---------- | --- | --- | --------- | --- | ------ |
|             |     |          |               |     |        |     |       | factor of | 2. Next, | we changed |     | the | attention | to  | global |
to be high for images that are obtained with non- on all layers, rather than only global in layers 6, 12,
| standard | and | novel approaches, |     |     | and for | which | large |         |         |              |     |      |       |          |     |
| -------- | --- | ----------------- | --- | --- | ------- | ----- | ----- | ------- | ------- | ------------ | --- | ---- | ----- | -------- | --- |
|          |     |                   |     |     |         |       |       | 18, and | 24 like | the original |     | SAM. | Then, | we added | a   |
annotated datasets are not available for finetuning. transposed convolution layer to revert the patchified
Biologists developing new imaging methods or novel embeddingsbackintopixelspacetopredictthreepixel
molecularapproachesmaythusespeciallybenefitfrom
mapscorrespondingtocellprobabilities,horizontaland
thegeneralizationperformanceofCellpose-SAM. verticalflows(3x256x256,[3]). Weusedtheweightsof
|     |     |     |     |     |     |     |     | SAM pretrained |     | on segmentations |     |     | from | photographs. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | --- | --- | ---- | ------------ | --- |
Acknowledgments
|     |     |     |     |     |     |     |     | Note that | only | images | not | containing |     | humans | are |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------ | --- | ---------- | --- | ------ | --- |
This research was funded by the Howard Hughes shown in Figure 1e. About half of the images in SA-
MedicalInstituteattheJaneliaResearchCampus. We 1Bdocontainblurredhumanswithblurredfaces.
7

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
Whole-datasettrainingandevaluation On 50% of the images in a batch we added
We trained Cellpose-SAM on the combined dataset four types of degradations: Poisson noise, Gaussian
|             |        |          |        |           |             |              |          | blurring,     | downsampling, |       | and anisotropic |         | blurring      | with    |
| ----------- | ------ | -------- | ------ | --------- | ----------- | ------------ | -------- | ------------- | ------------- | ----- | --------------- | ------- | ------------- | ------- |
| of 22,826   | images |          | with a | combined  |             | 3,341,254    | ROI      |               |               |       |                 |         |               |         |
|             |        |          |        |           |             |              |          | downsampling. |               | Out   | of 256 images   | per     | batch,        | exactly |
| annotations | (see   | below    | for    | details). |             | All training | was      |               |               |       |                 |         |               |         |
|             |        |          |        |           |             |              |          | 32 had        | each          | type  | of degradation, |         | and the       | rest of |
| performed   | with   | the      | AdamW  | optimizer |             | [68]         | using a  |               |               |       |                 |         |               |         |
|             |        |          |        |           |             |              |          | the images    | were          | clean | (except         | for the | augmentations |         |
| learning    | rate   | of 5e-5, | which  | we        | empirically |              | found to |               |               |       |                 |         |               |         |
lead to fast reductions in the training loss. We trained describedinthepreviousparagraph). Thedegradation
|        |       |          |      |           |        |          |        | parameters | for    | each      | of the four | conditions | were  | the    |
| ------ | ----- | -------- | ---- | --------- | ------ | -------- | ------ | ---------- | ------ | --------- | ----------- | ---------- | ----- | ------ |
| with a | batch | size of  | 256, | divided   | across | eight    | H200   |            |        |           |             |            |       |        |
|        |       |          |      |           |        |          |        | same as    | in the | Cellpose3 | paper       | [5].       | After | adding |
| GPUs.  | The   | learning | rate | increased |        | linearly | from 0 |            |        |           |             |            |       |        |
to its maximum value over the first 10 epochs, then the image degradation, we renormalized the images
|           |     |          |     |        |          |     |        | to again | set | 0 to the | first percentile |     | and 1 | to the |
| --------- | --- | -------- | --- | ------ | -------- | --- | ------ | -------- | --- | -------- | ---------------- | --- | ----- | ------ |
| decreased | by  | a factor | of  | 10 for | the last | 100 | epochs |          |     |          |                  |     |       |        |
andanotherfactorof10forthelast50epochs,similar 99th percentile of the image intensity. In this case,
|                            |     |     |     |                     |     |     |     | the brightness |     | and contrast | augmentations |     | described |     |
| -------------------------- | --- | --- | --- | ------------------- | --- | --- | --- | -------------- | --- | ------------ | ------------- | --- | --------- | --- |
| totheSAMtrainingrecipe[6]. |     |     |     | Epochsweredefinedas |     |     |     |                |     |              |               |     |           |     |
abovewereappliedafterthedegradations.
| random | samples | of  | 800 images |     | per GPU | drawn | with |     |     |     |     |     |     |     |
| ------ | ------- | --- | ---------- | --- | ------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
the mixing probabilities described below, for a total of During testing, the tile size was 256. There
|              |     |              |     |     |         |     |         | was no | diameter | estimation | and | resizing | performed |     |
| ------------ | --- | ------------ | --- | --- | ------- | --- | ------- | ------ | -------- | ---------- | --- | -------- | --------- | --- |
| 6,400 images |     | per “epoch”. |     | The | network | was | trained |        |          |            |     |          |           |     |
for 2,000 epochs, which took around 20 hours. The like in previous versions of Cellpose. We did not
|     |     |     |     |     |     |     |     | perform | test-time | augmentations, |     | and | the default | tile |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------------- | --- | --- | ----------- | ---- |
weightdecayparameterwassetto0.1,andadditional
|                |     |     |           |     |          |          |     | overlap | of 0.1 | was used. | The | default | cell probability |     |
| -------------- | --- | --- | --------- | --- | -------- | -------- | --- | ------- | ------ | --------- | --- | ------- | ---------------- | --- |
| regularization |     | was | performed | by  | randomly | dropping |     |         |        |           |     |         |                  |     |
layers of the image encoder with a 0.4 layer drop rate and flow error thresholds were used, 0.0 and 0.4
|     |     |     |     |     |     |     |     | respectively. |     | For memory | benchmarking, |     | we  | used |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ------------- | --- | --- | ---- |
aspreviouslyusedforSAM[6].
The loss function was the Cellpose segmentation ‘memory profiler’(‘mprof’command)forCPURAMand
|     |     |     |     |     |     |     |     | ‘torch.cuda.max |     | memory | allocated’ | for | GPU | RAM - |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ---------- | --- | --- | ----- |
loss[3]: themeansquarederrorbetweentheXYflows
whentheprocessusedmoreGPURAMthanavailable
| from the | ground-truth |     | segmentation |     | and | the predicted |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ------------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
XY flows, scaled by a factor of five, added to the on the GPU, the processing did slow down but was
|             |               |     |               |     |                  |              |      | successful(e.g. |     | the9,600x9,600imagesizetesting). |     |     |     |     |
| ----------- | ------------- | --- | ------------- | --- | ---------------- | ------------ | ---- | --------------- | --- | -------------------------------- | --- | --- | --- | --- |
| binary      | cross-entropy |     | between       |     | the ground-truth |              | cell |                 |     |                                  |     |     |     |     |
| probability | and           | the | the predicted |     | cell             | probability. | The  |                 |     |                                  |     |     |     |     |
Fine-tuningandevaluation
| XY flows | were | computedfrom |     | the | ground-truth |     | masks |     |     |     |     |     |     |     |
| -------- | ---- | ------------ | --- | --- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
as described in [5]. During training, all images were We varied the number of training images by powers
normalizedsuchthat0wassettothefirstpercentileof of 2 (from 1 to 512 and additionally the full dataset
theimageintensityand1wasthe99thpercentile. of training images). The training images were not
In each batch, images were randomly rotated, rescaled by the diameters of the labeled cells. The
learningrateincreasedlinearlyfrom0to1e-5overthe
| flipped, | and resized |     | with a | scale | factor | logarithmically |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ------ | ----- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
distributed between 0.25 and 4 relative to a mean first 10 epochs, then decreased by factors of 2 every
cell diameter of 30 pixels, and randomly cropped to 10 epochs over the last 50 epochs. The network was
an image size of 256x256. Images were randomly trainedfor100epochs. Eachepochhadatminimum8
converted to grayscale 10% of the time. For single- images. Thebatchsizewassetto1. Asinthewhole-
channel images, grayscale conversion was done by dataset training, the weight decay parameter was set
replicating the non-zero channel across all three to 0.1 and a 0.4 layer drop rate. We used the same
channels; for H&E images, grayscale conversion was augmentations as the previous Cellpose papers: the
done by taking the mean across all channels and images were randomly rotated, flipped, and resized
replicating that across all channels; while for images with a scale factor uniformly distributed between 0.75
with nuclei, we discarded the nucleus channel and and1.25,andthenrandomlycroppedtoanimagesize
| replicatedtheprimarychannel. |     |     |     | Weinvertedtheimage |     |     |     | of256x256. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
contrast 25% of the time (x → 1−x). After this During test time, the 2D masks were computed
operation, the third channel was randomly dropped as described above, without resizing the images
on 10% of the images, and then the channels of and without test-time augmentations. For 3D mask
each image were randomly permuted. Finally, the computation,weusedthe2Dto3Dmaskcreationstep
brightness level of each channel (the pixel mean) described in Cellpose [3]. In brief, the flows and cell
was randomly perturbed by a random normal jitter of probabilitieswerecomputedonall2DslicesinXY,ZY
standarddeviation0.2,andthecontrastlevel(standard and YZ, and then averaged to create flows in 3D, on
deviation)wasuniformlyrescaledbyarandomly-drawn whichthedynamicsstepswereperformed. Wesetthe
factor between -2 and 2. All 256 images in a batch numberofdynamicsiterationsto1,000andthe3Dflow
underwenttheseaugmentations. smoothingparameterto2. Cellmaskswithfewerthan
8

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
1,000pixelswerediscarded. usingtheaveragediameterfromthetrainingROIs. For
|     |     |     |     |     |     |     | all analyses, | the | flow | error threshold | (quality | control |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | --------------- | -------- | ------- |
Semanticsegmentationtrainingandevaluation step) was set to 0.4, the cell probability threshold was
setto0,andtest-timeaugmentationswereon,withthe
| We retrained |     | the Cellpose-SAM |     | model | to  | perform |     |     |     |     |     |     |
| ------------ | --- | ---------------- | --- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
semantic segmentation on the MoNuSAC dataset, tile overlap set to 0.5. In Figure 5, for all models we
|       |          |         |     |                |     |        | turned on | test-time | augmentations |     | during | evaluation, |
| ----- | -------- | ------- | --- | -------------- | --- | ------ | --------- | --------- | ------------- | --- | ------ | ----------- |
| which | has four | classes | of  | nuclei labeled |     | in H&E |           |           |               |     |        |             |
images [24]. We added five additional output maps to asin[3]and[73]. Whensegmentingbacterialimages,
Cellpose-SAM corresponding to background and the wesetthenumberofiterations‘niter’forthedynamics
post-processingto2,000forallimages,toimprovethe
fournucleiclasses,andinitializedtheweightsofthese
maps with the weights from the cell probability output convergenceforlongandthincells. Forthefine-tuning
|                 |     |         |         |            |       |     | experiments, | we  | retrained | the | cyto3 model | using the |
| --------------- | --- | ------- | ------- | ---------- | ----- | --- | ------------ | --- | --------- | --- | ----------- | --------- |
| map, multiplied |     | by -0.5 | for the | background | class | and |              |     |           |     |             |           |
0.5 for the four nuclei classes. The loss function for AdamW optimizer with a learning rate of 5e-3, weight
the class maps was the cross-entropy loss, weighted decayof1e-4,batchsizeof8,andfor300epochs,with
thesamelearningratescheduleandaugmentationsas
| by the inverse |     | of the per-pixel |     | class frequencies. |     | The |     |     |     |     |     |     |
| -------------- | --- | ---------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
training images were not rescaled by the diameters of intheCellpose2.0paper.
|             |        |     |          |                |     |          | CellSAM | [7]: | The CellSAM |     | model was | trained on |
| ----------- | ------ | --- | -------- | -------------- | --- | -------- | ------- | ---- | ----------- | --- | --------- | ---------- |
| the labeled | cells. | The | learning | rate increased |     | linearly |         |      |             |     |           |            |
from0to5e-5overthefirst10epochs,thendecreased manydatasets,includingtheCellposecellulardataset,
by factors of 2 every 10 epochs over the last 100 TissueNet, Omnipose, DeepBacs, and MoNuSeg, on
epochs. The network was trained for 500 epochs in whichwetestedtheperformanceofthemodel. Weran
total. The batch size was set to 16, weight decay to the ‘segment cellular image‘ function available from
|          |        |       |           |         |         |     | CellSAM. | CellSAM | takes | as input | 3 channel | images, |
| -------- | ------ | ----- | --------- | ------- | ------- | --- | -------- | ------- | ----- | -------- | --------- | ------- |
| 0.1, and | random | layer | drop rate | to 0.4. | We used | the |          |         |       |          |           |         |
sameaugmentationsasinthefine-tuningtraining. with the cytoplasmic channel in blue and the nuclear
During test time, we first computed the nucleus channel in green. For all the test sets considered,
segmentation masks using the flows and cell the cells were placed in the blue channel, and the
probabilitiesaspreviouslydescribed. Themapwiththe nuclearchannelwasoptionallyfilled. ForH&Eimages,
|     |     |     |     |     |     |     | the channels | were | averaged |     | and input | as a single |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | -------- | --- | --------- | ----------- |
largestvalueacrossallclasseswascomputedforeach
pixel, and the nucleus was assigned to the class with channel in the blue channel as described in the
themostpixelswithinthenucleus. Ifthisclasswasthe paper. We used the image resizing conventions for
background,thenthenucleusmaskwasremovedfrom each dataset that the authors provided in their shared
thepredictedmasks. Thepredictedmasksandclasses datasets, available in our benchmarking script. We
were also shared for the challenge winners PL1, PL2, normalizedalltestimagessuchthattheminimumwas
PL3 and L2 (the L1 link did not work). The winners set to 0 and the maximum set to 1. We enabled
usedahover-netarchitecturewitharesnet,U-nets,or the histogram normalization (normalize=True) for the
DeepBacsdatasetasthisimprovedperformance.
afeaturepyramidnetwork[69–72].
|     |     |     |     |     |     |     | SAMCell | [9]: | SAMCelltrainedtwoseparatemodels, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | -------------------------------- | --- | --- | --- |
Othermodels one on the Cellpose cellular dataset and one on the
Cellpose cyto3 [5]: This model was trained on LiveCelldataset,whichweappliedtotheCellposetest
the Cellpose cellular dataset, the nuclear dataset, set and the LiveCell test set respectively. We ran the
TissueNet, LiveCell, Omnipose, YeaZ,andDeepBacs, ‘SlidingWindowPipeline‘ ‘run‘ method available from
and thus we ran the model on the test set images SAMCell. SAMCell only takes single channel inputs
|            |          |            |     |          |     |         | (and was | trained | using | the grayscale |     | version of the |
| ---------- | -------- | ---------- | --- | -------- | --- | ------- | -------- | ------- | ----- | ------------- | --- | -------------- |
| from these | datasets | (excluding |     | the YeaZ | and | nuclear |          |         |       |               |     |                |
datasets as our test splits differed from other ‘cyto’dataset), soweinputtheCellposetestsetusing
algorithms). Two channels - cytoplasm and optionally theaverageofthetwochannels. TheCellposetestset
nuclei - were used as inputs for these models. The images were resized such that their longest side was
Cellpose segmentation models are trained such that 512, as described in their code. The LiveCell test set
imageswerenotresizedandwereinputdirectly.
allcellsandnucleiareapproximatelythesamesizein
pixels across all images, by resizing each image such MicroSAM [8]: MicroSAM was trained on a
that the average ROI diameter is 30.0. We trained variety of datasets, including TissueNet, LiveCell, and
an ROI size estimation model for the cyto3 model in DeepBacs, on which we tested the performance of
[5], which was used for Figure 1 and Figure S2. In the model. MicroSAM was trained only on grayscale
Figure 3, the images were either resized as described images (averaging multiple channels if available such
below or the model was run directly on the image as in TissueNet), input as the same value in all three
without the size model estimation. In Figure 4, as in channels. Thus, we input grayscale versions of all
theCellpose2.0paper,thetestimageswererescaled the test images. We used the ‘vit l lm‘ model and
9

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
computedtheautomaticinstancesegmentations(AIS). between each annotator and a hypothetical “mean” or
PathoSAM: PathoSAM was trained on H&E image consensusannotator.
datasets,includingMoNuSeg[74],andthuswetested
|     |     |     |     |     |     |     |     | This bound |     | may never |     | exactly | be achieved |     | due to |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | ------- | ----------- | --- | ------ |
its performance on the MoNuSeg test set. We ran the approximations above, and in practice we should
the ‘automatic segmentation wsi‘ function using the expect the best possible scores to be somewhere
‘vit l histopathology’model.
|     |     |     |     |     |     |     |     | between      | inter-annotator |              | performance |     |        | and half | of this |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | ------------ | ----------- | --- | ------ | -------- | ------- |
|     |     |     |     |     |     |     |     | value (where |                 | Cellpose-SAM |             | is  | Figure | 2c).     | An      |
Human-consensusbound
|          |            |     |       |         |        |          |     | additional                             | confound |     | is that | the | models | are        | trained |
| -------- | ---------- | --- | ----- | ------- | ------ | -------- | --- | -------------------------------------- | -------- | --- | ------- | --- | ------ | ---------- | ------- |
| Consider | annotators |     | 1 and | 2, each | making | mistakes |     |                                        |          |     |         |     |        |            |         |
|          |            |     |       |         |        |          |     | exclusivelyondatafromasingleannotator. |          |     |         |     |        | Theability |         |
relativetoanabsolutegroundtruth,oraveragehuman tomatchsegmentationsfromadifferentannotatorthus
| consensus. | Consider |     | their false | positive |     | FPi and | false |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----------- | -------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
isanindicationofitsgeneralization.
| negative       | FNi   | rates | relative | to this | consensus, |      | and    |     |     |     |     |     |     |     |     |
| -------------- | ----- | ----- | -------- | ------- | ---------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| their relative | rates | FPij  | and      | FNij    | between    | each | other, |     |     |     |     |     |     |     |     |
Segmentationbenchmarks
| where | i,j ∈ {1,2},i |     | ̸= j. | It can | be easily | seen | that |     |     |     |     |     |     |     |     |
| ----- | ------------- | --- | ----- | ------ | --------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
FPij = FNji. We assume that if the same absolute We tested Cellpose-SAM on the test set images from
ground truth ROI is present in both the annotations of the following datasets: Cellpose, TissueNet, LiveCell,
Annotator 1 and 2, then it will be matched also when Omnipose,DeepBacs,andMoNuSeg.
| comparing | annotators |        | against           | each | other. | This   | is not |         |                |        |          |             |     |          |         |
| --------- | ---------- | ------ | ----------------- | ---- | ------ | ------ | ------ | ------- | -------------- | ------ | -------- | ----------- | --- | -------- | ------- |
|           |            |        |                   |      |        |        |        | We make |                | a note | about    | comparisons |     |          | between |
| always    | true,      | but we | can approximately |      |        | assume | it is  |         |                |        |          |             |     |          |         |
|           |            |        |                   |      |        |        |        | models  | from different |        | research | groups.     |     | For this | study,  |
true for the relatively low IoU threshold we require to we chose to exclusively compare against models that
consideredtwoROIsmatched(0.5).
|     |     |     |     |      |       |     |     | were trained | by  | their | respective |     | teams, | and | to report |
| --- | --- | --- | --- | ---- | ----- | --- | --- | ------------ | --- | ----- | ---------- | --- | ------ | --- | --------- |
|     |     |     |     | ≤FPj | +FNi, |     |     |              |     |       |            |     |        |     |           |
Undertheseconditions, FPij because performance exclusively on those datasets where the
| the false | positives |     | of Annotator |     | j   | compared | to  |        |      |         |      |     |      |            |        |
| --------- | --------- | --- | ------------ | --- | --- | -------- | --- | ------ | ---- | ------- | ---- | --- | ---- | ---------- | ------ |
|           |           |     |              |     |     |          |     | models | were | trained | with | the | same | train/test | splits |
annotatorioriginatefromeithermistakesofAnnotator
|     |     |     |     |     |     |     |     | (Figure | 2, Figure | S2). | This | removes | the | possibility | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ---- | ---- | ------- | --- | ----------- | --- |
j where a new ROI is introduced compared to ground major errors when re-training a model designed by a
| truth (FPj) | or  | mistakes | of  | Annotator | i   | where | an ROI |           |        |              |     |       |         |      |         |
| ----------- | --- | -------- | --- | --------- | --- | ----- | ------ | --------- | ------ | ------------ | --- | ----- | ------- | ---- | ------- |
|             |     |          |     |           |     |       |        | different | group. | In contrast, |     | other | studies | like | [7] and |
from the ground truth was omitted (FNi) but it was [75] retrain the Cellpose model. To further facilitate
| not omitted | by  | Annotator | j   | so it | appears | as  | a false |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ----- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
comparisonsforfuturestudies,wewillpubliclyrelease
| positive | of Annotator |     | j. Furthermore, |     |     | there | are no |                                           |     |     |     |     |     |     |      |
| -------- | ------------ | --- | --------------- | --- | --- | ----- | ------ | ----------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
|          |              |     |                 |     |     |       |        | thecombineddatasetthatwasusedinthisstudy, |     |     |     |     |     |     | with |
other kinds of mistakes that can be counted in the train/test splits for every dataset upon publication of
FPij. IftheAnnotator1and2happentomakesomeof
|             |            |           |          |         |              |            |        | the study.    | We         | have   | previously  |          | reported  | separately |        |
| ----------- | ---------- | --------- | -------- | ------- | ------------ | ---------- | ------ | ------------- | ---------- | ------ | ----------- | -------- | --------- | ---------- | ------ |
| the same    | mistakes   |           | compared | to      | the absolute |            | ground |               |            |        |             |          |           |            |        |
|             |            |           |          |         |              |            |        | [10] on       | the issues | of     | training    | Cellpose |           | in [75].   | Note   |
| truth (same | false      | positives |          | or same | false        | negative), |        |               |            |        |             |          |           |            |        |
|             |            |           |          |         |              |            |        | that [7]      | reports    | better | performance |          | compared  |            | to the |
| then the    | inequality | becomes   |          | strict: | FPij         | <FPj       | +FNi.  |               |            |        |             |          |           |            |        |
|             |            |           |          |         |              |            |        | old Cellpose3 |            | model  | (“cyto3”),  |          | but these | are        | either |
Notehoweverthattheabsolutegroundtruthisdefined reported on datasets Cellpose3 has not been trained
| as a consensus |        | across       | a large | number    |           | of annotators, |         |                                        |              |       |        |              |     |          |          |
| -------------- | ------ | ------------ | ------- | --------- | --------- | -------------- | ------- | -------------------------------------- | ------------ | ----- | ------ | ------------ | --- | -------- | -------- |
|                |        |              |         |           |           |                |         | on,orretrainedbytheauthorsfromscratch. |              |       |        |              |     |          | Whenwe   |
| so on average  |        | the mistakes |         | will only | be        | identical      | at a    |                                        |              |       |        |              |     |          |          |
|                |        |              |         |           |           |                |         | directly                               | compare      | cyto3 | to     | CellSAM      | on  | datasets | both     |
| rate that      | is the | square       | of the  | single    | annotator |                | mistake |                                        |              |       |        |              |     |          |          |
|                |        |              |         |           |           |                |         | have been                              | trained      | on,   | cyto3  | performs     |     | better   | on every |
| rates (10%     | error  | rates        | becomes |           | 1%        | common         | error   |                                        |              |       |        |              |     |          |          |
|                |        |              |         |           |           |                |         | dataset.                               | As described |       | above, | Cellpose-SAM |     |          | performs |
rates between two annotators). If we ignore this betterstill,andbyasubstantialmarginfortheCellpose
smalloverlapinerrors,wegetanapproximateequality
testimages.
| FPij ≈FPj | +FNi,andsinceFN |     |     |     | =FPji,weget |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ij
Colorandsizeinvariance
| FPij | +FNij | =FPij | +FPji |     |     |     |     |         |       |            |     |          |     |     |          |
| ---- | ----- | ----- | ----- | --- | --- | --- | --- | ------- | ----- | ---------- | --- | -------- | --- | --- | -------- |
|      |       |       |       |     |     |     |     | To test | color | invariance | we  | permuted |     | the | channels |
≈FPj +FNi +FPi +FNj of images from the Cellpose test set to RGB, BRG
|     |     |       |      |        |     |      |     | and GBR,  | and         | also | performed | a   | random | permutation |     |
| --- | --- | ----- | ---- | ------ | --- | ---- | --- | --------- | ----------- | ---- | --------- | --- | ------ | ----------- | --- |
|     |     | =(FPj | +FNj | )+(FNi |     | +FPi | )   |           |             |      |           |     |        |             |     |
|     |     |       |      |        |     |      |     | per image | (‘Random‘), |      |           | and | then   | quantified  | the |
≈2(FPj +FNj ) segmentation quality for each image (Figure 3a). To
testsizeinvariance,weresizedimagesintheCellpose
where the last approximation arises from the test set such that the ROI diameters were set to 10,
symmetry of considering two random annotators from 15, 30, 60 and90(Figure3b). We ranCellpose-SAM,
the same distribution of annotators. Thus, the inter- Cellposecyto3,andCellSAMontheseimageswithout
| annotator | errors | are | approximately |     | twice | the | errors | imageresizing. |     |     |     |     |     |     |     |
| --------- | ------ | --- | ------------- | --- | ----- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
10

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
| Robustnesstoimagedegradation |            |              |          |      |             |        |     | as  |     |     |     |     |     |     |
| ---------------------------- | ---------- | ------------ | -------- | ---- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| We tested                    | robustness |              | to image |      | degradation | using  | the |     |     |     | TP  |     |     |     |
| images                       | from       | the Cellpose |          | test | set (Figure | 3c-f). | We  |     |     | AP= |     |     | .   |     |
TP+FP+FN
| added       | three | levels   | of degradation |             | for     | each of       | the four |          |             |     |             |                   |            |        |
| ----------- | ----- | -------- | -------------- | ----------- | ------- | ------------- | -------- | -------- | ----------- | --- | ----------- | ----------------- | ---------- | ------ |
| degradation |       | type.    | For Poisson    |             | noise   | we multiplied |          |          |             |     |             |                   |            |        |
|             |       |          |                |             |         |               |          | The      | error rates |     | and average |                   | precisions | were   |
| the image   | by    | scaling  | factors        | of          | 5, 2.5, | and           | 0.5 and  |          |             |     |             |                   |            |        |
|             |       |          |                |             |         |               |          | reported | per image,  |     | with the    | full distribution |            | across |
| used this   | as    | the mean | for            | the Poisson |         | distribution  | to       |          |             |     |             |                   |            |        |
imagesshownineachviolinplot.
| randomly | sample | from | for | each | pixel. | For | blurring, |         |          |     |              |              |     |     |
| -------- | ------ | ---- | --- | ---- | ------ | --- | --------- | ------- | -------- | --- | ------------ | ------------ | --- | --- |
|          |        |      |     |      |        |     |           | For the | semantic |     | segmentation | performance, |     | the |
the Gaussian standard deviations were 2, 4, and 8, error rate and average precision were computed per
andwegeneratedtheimageswithPoissonnoiseafter
imageandperclass,resultinginfourscoresperimage,
| multiplying   | by  | 120 | (small  | amount | of       | Poisson         | noise |             |       |         |         |               |       |          |
| ------------- | --- | --- | ------- | ------ | -------- | --------------- | ----- | ----------- | ----- | ------- | ------- | ------------- | ----- | -------- |
|               |     |     |         |        |          |                 |       | and then    | these | four    | scores  | were averaged |       | across   |
| degradation). |     | For | varying | pixel  | size     | and anisotropic |       |             |       |         |         |               |       |          |
|               |     |     |         |        |          |                 |       | classes.    | If an | image   | did not | contain       | any   | ground-  |
| downsampling, |     | the | images  | were   | rescaled | such            | that  |             |       |         |         |               |       |          |
|               |     |     |         |        |          |                 |       | truth masks | of a  | certain | class,  | then the      | error | rate and |
the diameter of the cells was 30 pixels for each image average precision for that class were not used in the
| before | downsampling. |     | The | pixel | size | downsampling |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | --- | ----- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
averageacrossclasses.
factorswere2,5,and10,andtheimageswereblurred
| with a       | Gaussian | with    | a standard |             | deviation | of           | half the | Datasets |     |     |     |     |     |     |
| ------------ | -------- | ------- | ---------- | ----------- | --------- | ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- |
| downsampling |          | factor. | The        | anisotropic |           | downsampling |          |          |     |     |     |     |     |     |
Mainretraining
| factors | were | 2, 6, and | 12  | along | one | dimension, | with |     |     |     |     |     |     |     |
| ------- | ---- | --------- | --- | ----- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
blurring with a Gaussian with a standard deviation We used 18 publicly available datasets for training
of half the downsampling factor along the same Cellpose-SAM.Thesamplingprobabilityofeachimage
dimension. After downsampling, the images were varieddependingontheimageset: PhCyeastimages
bilinearly interpolated to their original size to be input and fluorescent bacterial images were sampled at
|                  |     |       |       |             |     |      |        | a probability | of  | 1% each; | bright-field |     | yeast | images, |
| ---------------- | --- | ----- | ----- | ----------- | --- | ---- | ------ | ------------- | --- | -------- | ------------ | --- | ----- | ------- |
| to the networks. |     | After | these | operations, |     | each | of the |               |     |          |              |     |       |         |
degradedimageswasnormalizedsuchthat0wasthe phase bacterial images, and DeepBacs images at 2%
firstpercentileand1wasthe99thpercentile,asinthe each; livecell images at 5%; tissuenet images at 8%;
Cellpose3paper[5]. nuclei images at 20%; and cyto2 images at 59%. We
The noisy and blurry images were at their original upweighted images in the cyto2 and nuclei training
setsbecausetheycontainedthemostvariabilityacross
| size with   | varied    | sizes | of      | cells   | in pixels. | As    | in the  |         |     |     |     |     |     |     |
| ----------- | --------- | ----- | ------- | ------- | ---------- | ----- | ------- | ------- | --- | --- | --- | --- | --- | --- |
| Cellpose3   | paper,    |       | for the | ‘cyto3’ | network    |       | and the | images. |     |     |     |     |     |     |
| restoration | networks, |       | we      | first   | resized    | these | images  |         |     |     |     |     |     |     |
•
such that the cells were 30 pixels in diameter, as we Cellpose (updated) dataset: The cyto2 training
did not train size models on the degraded images. dataset contains 796 training images from various
|            |     |      |             |     |                  |     |     | sources | [5, 76–80]. |     | The | dataset | is available | at  |
| ---------- | --- | ---- | ----------- | --- | ---------------- | --- | --- | ------- | ----------- | --- | --- | ------- | ------------ | --- |
| The images |     | were | not resized |     | for Cellpose-SAM |     | or  |         |             |     |     |         |              |     |
https://www.cellpose.org/dataset.
CellSAM.
|     |     |     |     |     |     |     |     | The | original | test | dataset | contained | 13  | images |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------- | --------- | --- | ------ |
Quantificationofsegmentationquality of non-biological structures, that we remove from
|                 |      |             |                  |       |        |               |     | evaluation. | We        | instead | added      | 12         | new test | images    |
| --------------- | ---- | ----------- | ---------------- | ----- | ------ | ------------- | --- | ----------- | --------- | ------- | ---------- | ---------- | -------- | --------- |
| As described    |      | in Cellpose |                  | 1 and | 2,     | we quantified |     |             |           |         |            |            |          |           |
|                 |      |             |                  |       |        |               |     | that were   | segmented |         | by our     | annotator  |          | after the |
| the predictions |      | of          | the segmentation |       |        | algorithms    | by  |             |           |         |            |            |          |           |
|                 |      |             |                  |       |        |               |     | Cellpose    | dataset   | was     | originally | published, |          | resulting |
| matching        | each | predicted   |                  | mask  | to the | ground-truth  |     |             |           |         |            |            |          |           |
in67testimagesfortheupdatedCellposetestset.
maskthatismostsimilar,asdefinedbytheintersection
| over union    | metric |         | (IoU) | between | the       | predicted | and     |            |        |           |           |         |      |             |
| ------------- | ------ | ------- | ----- | ------- | --------- | --------- | ------- | ---------- | ------ | --------- | --------- | ------- | ---- | ----------- |
|               |        |         |       |         |           |           |         | • Cellpose | nuclei | dataset:  | This      | dataset |      | of nuclear  |
| ground-truth. |        | We used | an    | IoU     | threshold | of 0.5    | for all |            |        |           |           |         |      |             |
|               |        |         |       |         |           |           |         | images     | was    | described | in detail | in      | [3]. | It consists |
analyses in the paper. The error rate for each test of 1025 training images from various sources, with
imageisdefinedusingthetruepositives(matcheswith
|     |     |     |     |     |     |     |     | about | half of | the images | originating |     | from | the 2018 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ---------- | ----------- | --- | ---- | -------- |
IoUaboveathresholdof0.5),falsepositives(predicted
DataBowlcompetition[17,18,23,81].
| masks | without | matches), |     | and false | negatives |     | (missed |     |     |     |     |     |     |     |
| ----- | ------- | --------- | --- | --------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
ground-truthmasks):
|     |     |     |     |     |     |     |     | • TissueNet | [2]:     | The | TissueNet |             | dataset | consists  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | --------- | ----------- | ------- | --------- |
|     |     |     |     |     |     |     |     | of 2601     | training | and | 1249      | test images |         | collected |
FN+FP
errorrate= . using fluorescent microscopy on 6 tissue types with
|                                              |     |     |     | TP+FN |     |     |     | labeled       | cells | and nuclei | (https://datasets.dee |          |               |     |
| -------------------------------------------- | --- | --- | --- | ----- | --- | --- | --- | ------------- | ----- | ---------- | --------------------- | -------- | ------------- | --- |
|                                              |     |     |     |       |     |     |     | pcell.org/)   |       | – we       | used the              | cellular | segmentations |     |
| Theaverageprecisionisdefinedforeachtestimage |     |     |     |       |     |     |     | forallimages. |       |            |                       |          |               |     |
11

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
• LiveCell [1]: The LiveCell dataset consists of 3188 • MoNuSAC [24]: The MoNuSAC dataset consists of
training and 1516 test images of 8 different cell H&E images from 4 different organs with labeled
linescollectedusingphase-contrastmicroscopy(ht nuclei and nuclei classification, with 209 training
tps://sartorius-research.github.io/ imagesand85testimages,availableathttps://mo
LIVECell/). Overlapping mask regions were nusac-2020.grand-challenge.org/. The main
removed, as described in the Cellpose 2.0 paper model was only trained on the training images. The
[4]. Many images in this dataset are incompletely nuclei classification labels from the training images
annotated, which is reflected in the high error rates wereusedtotrainthesemanticsegmentationmodel
fromFigureS2. described in Figure 5, with the performance on test
imagesshowninthefigure.
| • Omnipose     | [19]: |           | The Omnipose |        | dataset |          | consists |             |       |     |           |     |         |          |
| -------------- | ----- | --------- | ------------ | ------ | ------- | -------- | -------- | ----------- | ----- | --- | --------- | --- | ------- | -------- |
| of fluorescent |       | bacterial |              | images | (143    | training | and      |             |       |     |           |     |         |          |
|                |       |           |              |        |         |          |          | • CryoNuSeg | [25]: | The | CryoNuSeg |     | dataset | consists |
75 test images), and phase-contrast microscopy ofH&Eimagesfrom10differenthumanorganswith
bacterialimages(249trainingand148testimages). (https://www.kaggle.com/datas
|     |     |     |     |     |     |     |     | labeled | nuclei |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --- | --- | --- | --- | --- |
ets/ipateam/segmentation-of-nuclei-in-c
•
YeaZ [20]: The YeaZ dataset consists of bright-field ryosectioned-he-images). Weusedallavailable
| and phase | contrast |     | images | of  | yeast | cells. | We used |     |     |     |     |     |     |     |
| --------- | -------- | --- | ------ | --- | ----- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
images(30)astrainingimages.
| 16 2D                                           | images | from | the | phase | contrast | dataset | for |          |       |     |          |         |     |             |
| ----------------------------------------------- | ------ | ---- | --- | ----- | -------- | ------- | --- | -------- | ----- | --- | -------- | ------- | --- | ----------- |
| training,and229imagesfromthebright-fielddataset |        |      |     |       |          |         |     | •        |       |     |          |         |     |             |
|                                                 |        |      |     |       |          |         |     | NuInsSeg | [26]: | The | NuInsSeg | dataset |     | consists of |
fortraining.
|     |     |     |     |     |     |     |     | H&E images | from         | 31  | different | human     |     | and mouse |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | --------- | --------- | --- | --------- |
|     |     |     |     |     |     |     |     | organs     | with labeled |     | nuclei,   | available | at  | https://  |
•
DeepBacs[21]: Weusedthefollowingsegmentation www.kaggle.com/datasets/ipateam/nuinss
| datasets     | from | DeepBacs: |             | S. aureus |         | bright-field | and     |        |          |           |     |        |       |             |
| ------------ | ---- | --------- | ----------- | --------- | ------- | ------------ | ------- | ------ | -------- | --------- | --- | ------ | ----- | ----------- |
|              |      |           |             |           |         |              |         | eg. We | used all | available |     | images | (665) | as training |
| fluorescence |      | with      | 56 training |           | patches | and          | 10 test |        |          |           |     |        |       |             |
images.
| images       | [82], | E.       | coli bright-field |        | with     | 19     | training |            |                               |       |        |              |     |              |
| ------------ | ----- | -------- | ----------------- | ------ | -------- | ------ | -------- | ---------- | ----------------------------- | ----- | ------ | ------------ | --- | ------------ |
| images       | and   | 15 test  | images            |        | [83],    | and B. | subtilis |            |                               |       |        |              |     |              |
|              |       |          |                   |        |          |        |          | • BCCD     | [27]: The                     | blood | cell   | segmentation |     | dataset      |
| fluorescence |       | with     | 80 training       |        | images   | and    | 10 test  |            |                               |       |        |              |     |              |
|              |       |          |                   |        |          |        |          | consists   | of blood                      | smear | images | taken        |     | with a light |
| images       | [84]; | in total | this              | is 155 | training | images | and      |            |                               |       |        |              |     |              |
|              |       |          |                   |        |          |        |          | microscope | (https://www.kaggle.com/datas |       |        |              |     |              |
35testimages.
ets/jeetblahiri/bccd-dataset-with-mask).
Thereare1,169trainingimagesinthedataset,allof
| • Neurips | 2022 | challenge |     | dataset |     | [22]: | The |     |     |     |     |     |     |     |
| --------- | ---- | --------- | --- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
whichwereusedfortraining.
| Neurips  | 2022          |       | challenge    |     | training        |         | dataset |                           |     |     |     |               |     |     |
| -------- | ------------- | ----- | ------------ | --- | --------------- | ------- | ------- | ------------------------- | --- | --- | --- | ------------- | --- | --- |
| consists | of            | 1,000 | images       |     | with            | labeled | cells   |                           |     |     |     |               |     |     |
|          |               |       |              |     |                 |         |         | • CPM15+17andTNBC[28,29]: |     |     |     | CPM15and17and |     |     |
| from     | bright-field, |       | fluorescent, |     | phase-constrast |         | and     |                           |     |     |     |               |     |     |
differential interference contrast imaging modalities TNBC consist of H&E images with labeled nuclei.
(https://neurips22-cellseg.grand-challen CPM 15 + 17 are from brain cancer patients, with
|                             |     |     |     |     |     |       |         | 15 and | 32 training | images |     | per dataset | respectively. |     |
| --------------------------- | --- | --- | --- | --- | --- | ----- | ------- | ------ | ----------- | ------ | --- | ----------- | ------------- | --- |
| ge.org/neurips22-cellseg/). |     |     |     |     |     | There | are ∼10 |        |             |        |     |             |               |     |
categoriesofimages,witheachcontainingbetween TNBC consists of 50 images from triple negative
|       |             |     |       |     |        |       |         | breast cancer |     | patients, | all | of which | were | used for |
| ----- | ----------- | --- | ----- | --- | ------ | ----- | ------- | ------------- | --- | --------- | --- | -------- | ---- | -------- |
| 5-200 | homogeneous |     | image |     | types. | Also, | a large |               |     |           |     |          |      |          |
https:
fraction of these images are annotated sparsely. training. The datasets are available at
//drive.google.com/drive/folders/1l55c
| We manually |     | selected | a   | subset | of  | 504 images | for |     |     |     |     |     |     |     |
| ----------- | --- | -------- | --- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
v3DuY-f7-JotDN7N5nbNnjbLWchK.
| training, | which     | contained |               | more  | dense   | annotations, |         |          |           |        |          |     |        |         |
| --------- | --------- | --------- | ------------- | ----- | ------- | ------------ | ------- | -------- | --------- | ------ | -------- | --- | ------ | ------- |
| and with  | the       | aim       | of equalizing |       | to some | degree       | the     |          |           |        |          |     |        |         |
|           |           |           |               |       |         |              |         | • LynSec | [30, 31]: | LynSec | consists |     | of 699 | IHC and |
| number    | of images |           | across        | image | types.  | We           | did not |          |           |        |          |     |        |         |
evaluateperformanceonthevalidationortestsetfor H&E images from lymphoma patients with labeled
nuclei (https://zenodo.org/records/80651
| this dataset, |     | since | the | test images |     | have the | same |     |     |     |     |     |     |     |
| ------------- | --- | ----- | --- | ----------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
74). Wechose616oftheseimagesrandomlytouse
biasesandhomogeneitiesasthetrainingset.
inourtrainingset.
| • MoNuSeg | [23]: | The | MoNuSeg |     | dataset | consists | of  |     |     |     |     |     |     |     |
| --------- | ----- | --- | ------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
37 training images and 14 test images with labeled • IHC TMA [32, 33]: The IHC TMA dataset consists
nuclei, available at https://monuseg.grand-cha of TMA sections from non-small cell lung cancer
| llenge.org/. |     |     |        |          |        |      |      |          |              |     |        | (https://doi.org/ |     |     |
| ------------ | --- | --- | ------ | -------- | ------ | ---- | ---- | -------- | ------------ | --- | ------ | ----------------- | --- | --- |
|              |     | 30  | of the | training | images | were | also | patients | with labeled |     | nuclei |                   |     |     |
includedinourCellposeNucleitrain/testdatasetsin 10.5281/zenodo.7647846). Thereare195and36
grayscale and inverted - we removed them for the images in the training and validation sets, we used
| visualizationinFigure2a. |     |     |     |     |     |     |     | allofthesefortraining. |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
12

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
• CoNIC [34]: The CoNIC dataset consists of and by a factor of 2.35 in Z (to create an isotropic
4,981 H&E images with labeled nuclei and nuclei volume). We used the 22 defined training volumes
classification (https://www.kaggle.com/dat forthetrainingsetandthe7definedtestsetvolumes
asets/aadimator/conic-challenge-datas for testing. As in the lateral root dataset, we took
et?select=data). We randomly chose 3,863 of 40 2D slices from each stack, resulting in 880 2D
theimagesfortraining, allofwhichhadatleastone trainingslicesand2802Dtestslices,andtested3D
labelednuclei(asubsetofimagesinthedatasethad segmentationonthe7fullvolumes.
| nolabels). | Weusedallnucleilabels. |     |     |     |     |     |                  |     |     |         |          |     |        |
| ---------- | ---------------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------- | -------- | --- | ------ |
|            |                        |     |     |     |     |     | • The BlastoSPIM |     |     | dataset | consists | of  | 231 3D |
• PanNuke [35, 36]: The PanNuke dataset consists volumes of early-stage mouse embryos from 55
of 7,898 H&E images from 19 tissues types from different embryos, and 80 3D volumes of late-stage
cancer patients with labeled nuclei and nuclei mouse embryos (‘Blast’) acquired on a confocal
classification (https://warwick.ac.uk/fac/ microscope, withavoxelsizeof0.208x0.208x2.0
cross_fac/tia/data/pannuke). We randomly um[43]. Wedefinedthetestsetasthevolumesfrom
chose 6,053 of the images for training, all of which 5randomearly-stageembryos(16volumesintotal),
had at least one labeled nuclei (a subset of images and10randomvolumesfromthelate-stageembryo
in the dataset had no labels). We used all nuclei dataset. Thetrainingsetcontainedvolumesfromthe
| labels. |     |     |     |     |     |     | other50early-stageembryosand70Blastvolumes. |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
WeupsampledthevolumesinZbyafactorof10to
For testing we only used the datasets with a well- create isotropicvolumes. Weused 3 2Dslices from
defined test set, as described above, and on which each training and test volume, 1 in XY, ZY and ZX.
other models had been trained, because those were These slices were sampled randomly, until a slice
the only datasets in which we could ensure train/test withatleastonemaskwasobtained,withapadding
splitswereconsistentacrossavailablemodels.
|     |     |     |     |     |     |     | of 30 pixels |                                      | on each | side | of the | dimension | being |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------------------------ | ------- | ---- | ------ | --------- | ----- |
|     |     |     |     |     |     |     | sampled.     | Thisresultedin8552Dtrainingslicesand |         |      |        |           |       |
Fine-tuningdatasets 782Dtestslices. Wetested3Dsegmentationonthe
We tested fine-tuning performance on three publicly 26full3Dtestvolumes.
availabledatasets:
References
•
| The lateral | root      | dataset     | consists |          | of 27   | volumes  |                 |        |         |         |         |          |         |
| ----------- | --------- | ----------- | -------- | -------- | ------- | -------- | --------------- | ------ | ------- | ------- | ------- | -------- | ------- |
|             |           |             |          |          |         |          | [1] Christoffer |        | Edlund, | Timothy | R       | Jackson, | Nabeel  |
| from three  | different | Arabidopsis |          | thaliana | lateral | root     |                 |        |         |         |         |          |         |
|             |           |             |          |          |         |          | Khalid,         | Nicola | Bevan,  |         | Timothy | Dale,    | Andreas |
| primordia   | timelapse | recordings, |          | acquired |         | every 30 |                 |        |         |         |         |          |         |
|             |           |             |          |          |         |          | Dengel,         | Sheraz |         | Ahmed,  | Johan   | Trygg,   | and     |
minuteswithavoxelsizeof0.1625×0.1625×0.250
|     |     |     |     |     |     |     | Rickard | Sjo¨gren. |     | Livecell—a |     | large-scale | dataset |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ---------- | --- | ----------- | ------- |
um(XxYxZ),withground-truth3Dsegmentations
|                               |     |     |     |     |            |     | for label-free |     | live | cell | segmentation. |     | Nature |
| ----------------------------- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | ---- | ---- | ------------- | --- | ------ |
| [44] (https://osf.io/2rszy/). |     |     |     |     | We reduced | the |                |     |      |      |               |     |        |
methods,18(9):1038–1045,2021.
| size of                                    | the volumes | by      | a factor | of 4   | in XY | and by a  |          |              |      |        |        |               |            |
| ------------------------------------------ | ----------- | ------- | -------- | ------ | ----- | --------- | -------- | ------------ | ---- | ------ | ------ | ------------- | ---------- |
|                                            |             |         |          |        |       |           | [2] Noah | F Greenwald, |      | Geneva |        | Miller, Erick | Moen,      |
| factorof2.6inZ(tocreateanisotropicvolume). |             |         |          |        |       | We        |          |              |      |        |        |               |            |
|                                            |             |         |          |        |       |           | Alex     | Kong,        | Adam | Kagel, | Thomas |               | Dougherty, |
| used all                                   | 17 of the   | volumes | from     | Movies | 1     | and 3 for |          |              |      |        |        |               |            |
ChristineCamachoFullaway,BriannaJMcIntosh,
| training, | and two | of the | ground-truth |     | volumes | from |     |     |     |     |     |     |     |
| --------- | ------- | ------ | ------------ | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Movie 2 for testing, which were in the original test Ke Xuan Leow, Morgan Sarah Schwartz, Cole
|                |     |     |         |         |     |          | Pavelchek, |     | Sunny | Cui, | Isabella | Camplisson, |     |
| -------------- | --- | --- | ------- | ------- | --- | -------- | ---------- | --- | ----- | ---- | -------- | ----------- | --- |
| set (timepoint | 10  | and | 20). We | divided | by  | movie id |            |     |       |      |          |             |     |
OmerBar-Tal,JaiveerSingh,MaraFong,Gautam
| to avoid | any relationship |     | between | the | train | and test |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | ------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
Chaudhry,ZionAbraham,JacksonMoseley,Shiri
| set. From       | each                                 | training                    | and     | test stack | we        | took 40 |             |             |         |           |             |              |             |
| --------------- | ------------------------------------ | --------------------------- | ------- | ---------- | --------- | ------- | ----------- | ----------- | ------- | --------- | ----------- | ------------ | ----------- |
|                 |                                      |                             |         |            |           |         | Warshawsky, |             | Erin    | Soon,     | Shirley     | Greenbaum,   |             |
| slices,         | 20 in XY                             | and 10                      | in each | ZY         | and ZX.   | These   |             |             |         |           |             |              |             |
|                 |                                      |                             |         |            |           |         | Tyler       | Risom,      | Travis  | Hollmann, |             | Sean         | C. Bendall, |
| slices were     | evenly                               | spaced                      | within  | the        | volume,   | with a  |             |             |         |           |             |              |             |
|                 |                                      |                             |         |            |           |         | Leeat       | Keren,      | William | Graf,     | Michael     | Angelo,      | and         |
| padding         | of 10 on                             | each                        | side    | of the     | dimension | being   |             |             |         |           |             |              |             |
|                 |                                      |                             |         |            |           |         | David       | Van         | Valen.  |           | Whole-cell  | segmentation |             |
| sampled.        | Thisresultedin6802Dtrainingslicesand |                             |         |            |           |         |             |             |         |           |             |              |             |
|                 |                                      |                             |         |            |           |         | of tissue   | images      |         | with      | human-level | performance  |             |
| 802Dtestslices. |                                      | Wetested3Dsegmentationusing |         |            |           |         |             |             |         |           |             |              |             |
|                 |                                      |                             |         |            |           |         | using       | large-scale |         | data      | annotation  |              | and deep    |
the3Dground-truthforthetwo3Dtestvolumes.
|             |         |          |     |       |         |      | learning. |     | Nature | biotechnology, |     | pages | 1–11, |
| ----------- | ------- | -------- | --- | ----- | ------- | ---- | --------- | --- | ------ | -------------- | --- | ----- | ----- |
| • The ovule | dataset | consists |     | of 31 | volumes | from | 2021.     |     |        |                |     |       |       |
Arabidopsis thaliana ovule recordings with a voxel [3] Carsen Stringer, Tim Wang, Michalis Michaelos,
sizeof0.075×0.075×0.235um,withground-truth and Marius Pachitariu. Cellpose: a generalist
3Dsegmentations[44](https://osf.io/w38uf/). algorithm for cellular segmentation. Nature
We reduced the size of the volumes by 1.33 in XY methods,18(1):100–106,2021.
13

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
[4] Marius Pachitariu and Carsen Stringer. Cellpose computer vision and pattern recognition, pages
| 2.0: | how | to train | your | own | model. |     | Nature | 16000–16009,2022. |     |     |     |     |     |     |     |
| ---- | --- | -------- | ---- | --- | ------ | --- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
methods,19(12):1634–1641,2022.
|     |     |     |     |     |     |     |     | [16] Alexey |     | Dosovitskiy, |     | Lucas | Beyer, | Alexander |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ----- | ------ | --------- | --- |
[5] Carsen Stringer and Marius Pachitariu. Kolesnikov, Dirk Weissenborn, Xiaohua Zhai,
Cellpose3: one-click image restoration for ThomasUnterthiner,MostafaDehghani,Matthias
improvedcellularsegmentation. NatureMethods, Minderer, Georg Heigold, Sylvain Gelly, et al.
| pages1–8,2025. |     |     |     |     |     |     |     | An  | image | is worth | 16x16 |     | words: | Transformers |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ----- | --- | ------ | ------------ | --- |
[6] AlexanderKirillov,EricMintun,NikhilaRavi,Hanzi for image recognition at scale. arXiv preprint
Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, arXiv:2010.11929,2020.
SpencerWhitehead,AlexanderCBerg,Wan-Yen [17] Juan C. Caicedo, Allen Goodman, Kyle W.
Lo,etal.Segmentanything.InProceedingsofthe Karhohs, Beth A. Cimini, Jeanelle Ackerman,
IEEE/CVF international conference on computer Marzieh Haghighi, CherKeng Heng, Tim Becker,
vision,pages4015–4026,2023. Minh Doan, Claire McQuin, Mohammad Rohban,
ShantanuSingh,andAnneE.Carpenter.Nucleus
| [7] Uriah | Israel, | Markus | Marks, |     | Rohit | Dilip, | Qilin |     |     |     |     |     |     |     |     |
| --------- | ------- | ------ | ------ | --- | ----- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Li, Morgan Sarah Schwartz, Elora Pradhan, segmentation across imaging experiments: the
|        |      |        |     |               |     |          |     | 2018 | Data | Science |     | Bowl. | Nature | Methods, |     |
| ------ | ---- | ------ | --- | ------------- | --- | -------- | --- | ---- | ---- | ------- | --- | ----- | ------ | -------- | --- |
| Edward | Pao, | Shenyi |     | Li, Alexander |     | Pearson- |     |      |      |         |     |       |        |          |     |
16(12):1247–1253,December2019.
| Goulart, | Pietro | Perona, |     | Georgia | Gkioxari, |     | Ross |     |     |     |     |     |     |     |     |
| -------- | ------ | ------- | --- | ------- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Barnowski, Yisong Yue, and David Van Valen. A [18] Luis Pedro Coelho, Aabid Shariff, and Robert F.
foundation model for cell segmentation. bioRxiv, Murphy. Nuclear segmentation in microscope
| pages2023–11,2023. |         |          |             |       |        |          |         | cell          | images: |           | A hand-segmented |     |            | dataset  | and  |
| ------------------ | ------- | -------- | ----------- | ----- | ------ | -------- | ------- | ------------- | ------- | --------- | ---------------- | --- | ---------- | -------- | ---- |
|                    |         |          |             |       |        |          |         | comparison    |         | of        | algorithms.      |     | In         | 2009     | IEEE |
| [8] Anwai          | Archit, | Sushmita |             | Nair, | Nabeel |          | Khalid, |               |         |           |                  |     |            |          |      |
|                    |         |          |             |       |        |          |         | International |         | Symposium |                  | on  | Biomedical | Imaging: |      |
| Paul               | Hilt,   | Vikas    | Rajashekar, |       | Marei  | Freitag, |         |               |         |           |                  |     |            |          |      |
FromNanotoMacro,pages518–521,June2009.
| Sagnik        | Gupta,     | Andreas                    |       | Dengel, | Sheraz | Ahmed,    |        |                 |       |           |         |          |           |             |     |
| ------------- | ---------- | -------------------------- | ----- | ------- | ------ | --------- | ------ | --------------- | ----- | --------- | ------- | -------- | --------- | ----------- | --- |
| and           | Constantin |                            | Pape. | Segment |        | anything  | for    | ISSN:1945-8452. |       |           |         |          |           |             |     |
|               |            |                            |       |         |        |           |        | [19] Kevin      | J     | Cutler,   | Carsen  |          | Stringer, | Teresa      | W   |
| microscopy.   |            | bioRxiv,pages2023–08,2023. |       |         |        |           |        |                 |       |           |         |          |           |             |     |
|               |            |                            |       |         |        |           |        | Lo,             | Luca  |           | Rappez, | Nicholas |           | Stroustrup, |     |
| [9] Alexandra |            | D VandeLoo,                |       | Nathan  | J      | Malta,    | Emilio |                 |       |           |         |          |           |             |     |
|               |            |                            |       |         |        |           |        | S               | Brook | Peterson, |         | Paul     | A         | Wiggins,    | and |
| Aponte,       | Caitlin    | van                        | Zyl,  | Danfei  | Xu,    | and Craig | R      |                 |       |           |         |          |           |             |     |
Forest. Samcell: Generalizedlabel-freebiological Joseph D Mougous. Omnipose: a high-
|     |     |     |     |     |     |     |     | precision |     | morphology-independent |     |     |     |     | solution |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------------------- | --- | --- | --- | --- | -------- |
cellsegmentationwithsegmentanything.bioRxiv,
|     |     |     |     |     |     |     |     | for | bacterial | cell | segmentation. |     | Nature | methods, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------------- | --- | ------ | -------- | --- |
pages2025–02,2025.
19(11):1438–1448,2022.
| [10] Carsen | Stringer |     | and | Marius |     | Pachitariu. |     |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | --- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Benchmarking cellular segmentation methods [20] Nicola Dietler, Matthias Minder, Vojislav
|                  |         |     |                            |          |     |          |     | Gligorovski, |       |         | Augoustina |       | Maria   | Economou,  |     |
| ---------------- | ------- | --- | -------------------------- | -------- | --- | -------- | --- | ------------ | ----- | ------- | ---------- | ----- | ------- | ---------- | --- |
| againstcellpose. |         |     | bioRxiv,pages2024–04,2024. |          |     |          |     |              |       |         |            |       |         |            |     |
|                  |         |     |                            |          |     |          |     | Denis        | Alain | Henri   | Lucien     | Joly, | Ahmad   | Sadeghi,   |     |
| [11] Uwe         | Schmidt | and | Martin                     | Weigert. |     | StarDist | -   |              |       |         |            |       |         |            |     |
|                  |         |     |                            |          |     |          |     | Chun         | Hei   | Michael |            | Chan, | Mateusz | Kozin´ski, |     |
ObjectDetectionwithStar-convexShapes,2019.
|              |           |         |           |     |                  |          |     | Martin        | Weigert, |        | Anne-Florence |         | Bitbol,   | et  | al. A  |
| ------------ | --------- | ------- | --------- | --- | ---------------- | -------- | --- | ------------- | -------- | ------ | ------------- | ------- | --------- | --- | ------ |
| [12] Kaiming | He,       | Georgia | Gkioxari, |     | Piotr            | Dolla´r, | and |               |          |        |               |         |           |     |        |
|              |           |         |           |     |                  |          |     | convolutional |          |        | neural        | network | segments  |     | yeast  |
| Ross         | Girshick. | Mask    | R-CNN.    |     | arXiv:1703.06870 |          |     |               |          |        |               |         |           |     |        |
|              |           |         |           |     |                  |          |     | microscopy    |          | images | with          | high    | accuracy. |     | Nature |
[cs],January2018. arXiv: 1703.06870. communications,11(1):5723,2020.
[13] Dan Hendrycks, Xiaoyuan Liu, Eric Wallace, [21] Christoph Spahn, Estibaliz Go´mez-de Mariscal,
| Adam  | Dziedzic,  |     | Rishabh      | Krishnan, |     | and     | Dawn |        |          |          |              |       |            |     |        |
| ----- | ---------- | --- | ------------ | --------- | --- | ------- | ---- | ------ | -------- | -------- | ------------ | ----- | ---------- | --- | ------ |
|       |            |     |              |           |     |         |      | Romain |          | F Laine, |              | Pedro | M Pereira, |     | Lucas  |
| Song. | Pretrained |     | transformers |           |     | improve | out- |        |          |          |              |       |            |     |        |
|       |            |     |              |           |     |         |      | von    | Chamier, |          | Mia Conduit, |       | Mariana    | G   | Pinho, |
of-distribution robustness. arXiv preprint Guillaume Jacquemet, Se´amus Holden, Mike
arXiv:2004.06100,2020.
|     |     |     |     |     |     |     |     | Heilemann, |     | and | Ricardo | Henriques. |     | Deepbacs |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | ------- | ---------- | --- | -------- | --- |
[14] Stanislav Fort, Jie Ren, and Balaji for multi-task bacterial image analysis using
Lakshminarayanan. Exploring the limits of open-source deep learning approaches.
out-of-distribution detection. Advances in neural CommunicationsBiology,5(1):688,2022.
| information |     | processing |     | systems, | 34:7068–7081, |     |     |          |        |        |      |             |            |          |       |
| ----------- | --- | ---------- | --- | -------- | ------------- | --- | --- | -------- | ------ | ------ | ---- | ----------- | ---------- | -------- | ----- |
|             |     |            |     |          |               |     |     | [22] Jun | Ma,    | Ronald | Xie, | Shamini     | Ayyadhury, |          | Cheng |
| 2021.       |     |            |     |          |               |     |     | Ge,      | Anubha | Gupta, |      | Ritu Gupta, |            | Song Gu, | Yao   |
[15] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Zhang, Gihun Lee, Joonkee Kim, et al. The
Li, Piotr Dolla´r, and Ross Girshick. Masked multimodalitycellsegmentationchallenge: toward
autoencoders are scalable vision learners. In universalsolutions. Naturemethods,pages1–11,
| Proceedings |     | of  | the IEEE/CVF |     | conference |     | on  | 2024. |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------------ | --- | ---------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
14

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
[23] Neeraj Kumar, Ruchika Verma, Deepak Anand, [27] DS Depto, S Rahman, MM Hosen, MS Akter,
Yanning Zhou, Omer Fahri Onder, Efstratios TR Reme, A Rahman, H Zunai, MRC Mahdy,
Tsougenis, Hao Chen, Pheng Ann Heng, Jiahui MS Rahman, and JB Lahiri. Blood cell
Li, Zhiqiang Hu, Yunzhi Wang, Navid Alemi segmentationdataset,2023.
Koohbanani, Mostafa Jahanifar, Neda Zamani [28] Quoc Dang Vu, Simon Graham, Tahsin Kurc,
| Tajeddin, | Ali Gooya, | Nasir | Rajpoot, |     | Xuhua | Ren, |      |        |      |     |              |     |         |     |
| --------- | ---------- | ----- | -------- | --- | ----- | ---- | ---- | ------ | ---- | --- | ------------ | --- | ------- | --- |
|           |            |       |          |     |       |      | Minh | Nguyen | Nhat |     | To, Muhammad |     | Shaban, |     |
Sihang Zhou, Qian Wang, Dinggang Shen, Talha Qaiser, Navid Alemi Koohbanani, Syed Ali
Cheng Kun Yang, Chi Hung Weng, Wei Hsiang Khurram, Jayashree Kalpathy-Cramer, Tianhao
| Yu, Chao | Yuan | Yeh, | Shuang | Yang, | Shuoyu | Xu, |       |     |     |         |     |              |     |     |
| -------- | ---- | ---- | ------ | ----- | ------ | --- | ----- | --- | --- | ------- | --- | ------------ | --- | --- |
|          |      |      |        |       |        |     | Zhao, | et  | al. | Methods | for | segmentation |     | and |
Pak Hei Yeung, Peng Sun, Amirreza Mahbod, classification of digital microscopy tissue images.
| Gerald Schaefer, |      | Isabella  | Ellinger,       |       | Rupert   | Ecker, |            |         |                   |              |              |                |           |     |
| ---------------- | ---- | --------- | --------------- | ----- | -------- | ------ | ---------- | ------- | ----------------- | ------------ | ------------ | -------------- | --------- | --- |
|                  |      |           |                 |       |          |        | Frontiers  |         | in bioengineering |              | and          | biotechnology, |           |     |
| Orjan Smedby,    |      | Chunliang |                 | Wang, | Benjamin |        | 7:53,2019. |         |                   |              |              |                |           |     |
| Chidester,       | That | Vinh      | Ton, Minh-Triet |       | Tran,    | Jian   |            |         |                   |              |              |                |           |     |
|                  |      |           |                 |       |          |        | [29] Peter | Naylor, | Marick            |              | Lae´, Fabien |                | Reyal,    | and |
| Ma, Minh         | N.   | Do, Simon | Graham,         |       | Quoc     | Dang   |            |         |                   |              |              |                |           |     |
|                  |      |           |                 |       |          |        | Thomas     |         | Walter.           | Segmentation |              |                | of nuclei | in  |
Vu, Jin Tae Kwak, Akshaykumar Gunda, Raviteja histopathology images by deep regression of the
| Chunduri, | Corey | Hu, | Xiaoyang | Zhou, |     | Dariush |          |     |      |      |              |     |            |     |
| --------- | ----- | --- | -------- | ----- | --- | ------- | -------- | --- | ---- | ---- | ------------ | --- | ---------- | --- |
|           |       |     |          |       |     |         | distance |     | map. | IEEE | transactions |     | on medical |     |
Lotfi, Reza Safdari, Antanas Kascenas, Alison imaging,38(2):448–459,2018.
| O’Neil, Dennis |        | Eschweiler, | Johannes    |          | Stegmaier,  |        |                |         |         |              |              |            |            |        |
| -------------- | ------ | ----------- | ----------- | -------- | ----------- | ------ | -------------- | ------- | ------- | ------------ | ------------ | ---------- | ---------- | ------ |
|                |        |             |             |          |             |        | [30] Peter     | Naylor, | Marick  |              | Lae´, Fabien |            | Reyal,     | and    |
| Yanping        | Cui,   | Baocai      | Yin, Kailin |          | Chen,       | Xinmei |                |         |         |              |              |            |            |        |
|                |        |             |             |          |             |        | Thomas         |         | Walter. | Segmentation |              |            | of nuclei  | in     |
| Tian, Philipp  |        | Gruening,   | Erhardt     |          | Barth,      | Elad   |                |         |         |              |              |            |            |        |
|                |        |             |             |          |             |        | histopathology |         | images  |              | by deep      | regression |            | of the |
| Arbel, Itay    | Remer, |             | Amir        | Ben-Dor, | Ekaterina   |        |                |         |         |              |              |            |            |        |
|                |        |             |             |          |             |        | distance       |         | map.    | IEEE         | transactions |            | on medical |        |
| Sirazitdinova, |        | Matthias    | Kohl,       | Stefan   | Braunewell, |        |                |         |         |              |              |            |            |        |
imaging,38(2):448–459,2018.
| Yuexiang     | Li, Xinpeng |          | Xie, Linlin    | Shen,  |      | Jun Ma,  |            |             |          |         |           |       |     |         |
| ------------ | ----------- | -------- | -------------- | ------ | ---- | -------- | ---------- | ----------- | -------- | ------- | --------- | ----- | --- | ------- |
|              |             |          |                |        |      |          | [31] Naji  | Hussein,    | Bu¨ttner |         | Reinhard, | Simon |     | Adrian, |
| Krishanu     | Das         | Baksi,   | Mohammad       |        | Azam | Khan,    |            |             |          |         |           |       |     |         |
|              |             |          |                |        |      |          | Eich       | Marie-Lisa, |          | Lohneis | Philipp,  |       | and | Bozek   |
| Jaegul Choo, |             | Adria´ n | Colomer,       | Valery |      | Naranjo, |            |             |          |         |           |       |     |         |
|              |             |          |                |        |      |          | Katarzyna. |             |          | Lynsec: | Lymphoma  |       |     | nuclear |
| Linmin       | Pei,        | Khan M.  | Iftekharuddin, |        |      | Kaushiki |            |             |          |         |           |       |     |         |
segmentationandclassification,June2023.
| Roy, Debotosh |        | Bhattacharjee, |              | Anibal |             | Pedraza, |             |       |     |        |      |       |      |      |
| ------------- | ------ | -------------- | ------------ | ------ | ----------- | -------- | ----------- | ----- | --- | ------ | ---- | ----- | ---- | ---- |
|               |        |                |              |        |             |          | [32] Ranran | Wang, |     | Yusong | Qiu, | Xinyu | Hao, | Shan |
| Maria Gloria  | Bueno, |                | Sabarinathan |        | Devanathan, |          |             |       |     |        |      |       |      |      |
Saravanan Radhakrishnan, Praveen Koduganty, Jin, Junxiu Gao, Heng Qi, Qi Xu, Yong Zhang,
|           |        |        |      |             |      |         | and | Hongming    | Xu. | Simultaneously |        |     | segmenting |        |
| --------- | ------ | ------ | ---- | ----------- | ---- | ------- | --- | ----------- | --- | -------------- | ------ | --- | ---------- | ------ |
| Zihan Wu, | Guanyu |        | Cai, | Xiaojie     | Liu, | Yuqin   |     |             |     |                |        |     |            |        |
|           |        |        |      |             |      |         | and | classifying |     | cell           | nuclei | by  | using      | multi- |
| Wang, and | Amit   | Sethi. | A    | Multi-organ |      | Nucleus |     |             |     |                |        |     |            |        |
Segmentation Challenge. IEEE Transactions on task learning in multiplex immunohistochemical
|     |     |     |     |     |     |     | tissue | microarray |     | sections. |     | Biomedical |     | Signal |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | --------- | --- | ---------- | --- | ------ |
MedicalImaging,pages1–1,2019.
[24] Ruchika Verma, Neeraj Kumar, Abhijeet Patil, ProcessingandControl,93:106143,2024.
|                |     |         |         |     |       |       | [33] Ranran | Wang, |     | Yusong | Qiu, | Yong | Zhang, | and |
| -------------- | --- | ------- | ------- | --- | ----- | ----- | ----------- | ----- | --- | ------ | ---- | ---- | ------ | --- |
| Nikhil Cherian |     | Kurian, | Swapnil |     | Rane, | Simon |             |       |     |        |      |      |        |     |
Graham, Quoc Dang Vu, Mieke Zwager, Hongming Xu. Image dataset from multiplex ihc
stainedtmasections,February2023.
| Shan E | Ahmed | Raza, | Nasir | Rajpoot, |     | et al. |     |     |     |     |     |     |     |     |
| ------ | ----- | ----- | ----- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Monusac2020: Amulti-organnucleisegmentation [34] Simon Graham, Quoc Dang Vu, Mostafa
and classification challenge. IEEE Transactions Jahanifar,MartinWeigert,UweSchmidt,Wenhua
onMedicalImaging,40(12):3413–3423,2021. Zhang, Jun Zhang, Sen Yang, Jinxi Xiang, Xiyue
[25] Amirreza Mahbod, Rahim Entezari, Isabella Wang, et al. Conic challenge: Pushing the
|           |          |        |      |        |     |         | frontiers |     | of nuclear |     | detection, | segmentation, |     |     |
| --------- | -------- | ------ | ---- | ------ | --- | ------- | --------- | --- | ---------- | --- | ---------- | ------------- | --- | --- |
| Ellinger, | and Olga | Saukh. | Deep | neural |     | network |           |     |            |     |            |               |     |     |
pruning for nuclei instance segmentation in classification and counting. Medical image
analysis,92:103047,2024.
| hematoxylin |     | and | eosin-stained |     | histological |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
images. In International Workshop on [35] Jevgenij Gamper, Navid Alemi Koohbanani,
Applications of Medical AI, pages 108–117. Ksenija Benet, Ali Khuram, and Nasir Rajpoot.
| Springer,2022. |     |     |     |     |     |     | Pannuke: |     | an  | open | pan-cancer |     | histology |     |
| -------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---- | ---------- | --- | --------- | --- |
[26] Amirreza Mahbod, Christine Polak, Katharina dataset for nuclei instance segmentation and
|           |        |     |       |           |     |         | classification. |     |     | In  | Digital | Pathology: |     | 15th |
| --------- | ------ | --- | ----- | --------- | --- | ------- | --------------- | --- | --- | --- | ------- | ---------- | --- | ---- |
| Feldmann, | Rumsha |     | Khan, | Katharina |     | Gelles, |                 |     |     |     |         |            |     |      |
Georg Dorffner, Ramona Woitek, Sepideh European Congress, ECDP 2019, Warwick,
|            |     |          |           |     |           |     | UK, | April | 10–13, | 2019, | Proceedings |     | 15, | pages |
| ---------- | --- | -------- | --------- | --- | --------- | --- | --- | ----- | ------ | ----- | ----------- | --- | --- | ----- |
| Hatamikia, | and | Isabella | Ellinger. |     | Nuinsseg: |     |     |       |        |       |             |     |     |       |
A fully annotated dataset for nuclei instance 11–19.Springer,2019.
segmentation in h&e-stained histological images. [36] Jevgenij Gamper, Navid Alemi Koohbanani,
arXivpreprintarXiv:2308.01760,2023. Simon Graham, Mostafa Jahanifar, Syed Ali
15

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
Khurram, Ayesha Azam, Katherine Hewitt, and [45] Dmitry Ershov, Minh-Son Phan, Joanna W
Nasir Rajpoot. Pannuke dataset extension, Pylva¨na¨inen, Ste´phane U Rigaud, Laure
insights and baselines. arXiv preprint Le Blanc, Arthur Charles-Orszag, James RW
arXiv:2003.10778,2020. Conway, Romain F Laine, Nathan H Roy, Daria
|           |          |       |                |     |        |               |     | Bonazzi,   | et al.       | Trackmate |            | 7: integrating | state-        |
| --------- | -------- | ----- | -------------- | --- | ------ | ------------- | --- | ---------- | ------------ | --------- | ---------- | -------------- | ------------- |
| [37] Leon | A Gatys, |       | Alexander      | S   | Ecker, | and Matthias  |     |            |              |           |            |                |               |
|           |          |       |                |     |        |               |     | of-the-art | segmentation |           | algorithms |                | into tracking |
| Bethge.   |          | Image | style transfer |     | using  | convolutional |     |            |              |           |            |                |               |
neural networks. In Proceedings of the IEEE pipelines. Naturemethods,19(7):829–832,2022.
conference on computer vision and pattern [46] Caroline Malin-Mayor, Peter Hirsch, Leo
recognition,pages2414–2423,2016. Guignard, Katie McDole, Yinan Wan, William C
|              |       |            |          |          |            |              |     | Lemon,         | Dagmar     | Kainmueller,    |     | Philipp      | J Keller,     |
| ------------ | ----- | ---------- | -------- | -------- | ---------- | ------------ | --- | -------------- | ---------- | --------------- | --- | ------------ | ------------- |
| [38] Kaiming |       | He, Xinlei | Chen,    | Saining  |            | Xie, Yanghao |     |                |            |                 |     |              |               |
|              |       |            |          |          |            |              |     | Stephan        | Preibisch, | and             | Jan | Funke.       | Automated     |
| Li,          | Piotr | Dolla´r,   | and      | Ross     | Girshick.  | Masked       |     |                |            |                 |     |              |               |
|              |       |            |          |          |            |              |     | reconstruction |            | of whole-embryo |     |              | cell lineages |
| autoencoders |       | are        | scalable |          | vision     | learners.    | In  |                |            |                 |     |              |               |
|              |       |            |          |          |            |              |     | by learning    |            | from sparse     |     | annotations. | Nature        |
| Proceedings  |       | of         | the      | IEEE/CVF | conference |              | on  |                |            |                 |     |              |               |
biotechnology,41(1):44–49,2023.
| computer |     | vision | and | pattern | recognition, |     | pages |     |     |     |     |     |     |
| -------- | --- | ------ | --- | ------- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
16000–16009,2022. [47] Jorda˜o Bragantini, Ilan Theodoro, Xiang
|             |      |                                      |       |         |       |     |      | Zhao,            | Teun    | APM   | Huijben,    | Eduardo    | Hirata-       |
| ----------- | ---- | ------------------------------------ | ----- | ------- | ----- | --- | ---- | ---------------- | ------- | ----- | ----------- | ---------- | ------------- |
| [39] Hangbo | Bao, | Li                                   | Dong, | Songhao | Piao, | and | Furu |                  |         |       |             |            |               |
|             |      |                                      |       |         |       |     |      | Miyasaki,        | Shruthi |       | VijayKumar, |            | Akilandeswari |
| Wei.Beit:   |      | Bertpre-trainingofimagetransformers. |       |         |       |     |      |                  |         |       |             |            |               |
|             |      |                                      |       |         |       |     |      | Balasubramanian, |         | Tiger |             | Lao, Richa | Agrawal,      |
arXivpreprintarXiv:2106.08254,2021.
|           |          |        |           |       |               |     |        | Sheng         | Xiao, | et al. Ultrack: |            | pushing | the limits of |
| --------- | -------- | ------ | --------- | ----- | ------------- | --- | ------ | ------------- | ----- | --------------- | ---------- | ------- | ------------- |
| [40] Hugo | Touvron, |        | Matthieu  | Cord, | Matthijs      |     | Douze, |               |       |                 |            |         |               |
|           |          |        |           |       |               |     |        | cell tracking |       | across          | biological | scales. | bioRxiv,      |
| Francisco |          | Massa, | Alexandre |       | Sablayrolles, |     | and    |               |       |                 |            |         |               |
2024.
| Herve´        | Je´gou. |            | Training     |         | data-efficient |            | image |                   |           |       |               |       |            |
| ------------- | ------- | ---------- | ------------ | ------- | -------------- | ---------- | ----- | ----------------- | --------- | ----- | ------------- | ----- | ---------- |
|               |         |            |              |         |                |            |       | [48] Mark-Anthony |           | Bray, | Shantanu      |       | Singh, Han |
| transformers  |         | &          | distillation | through |                | attention. | In    |                   |           |       |               |       |            |
|               |         |            |              |         |                |            |       | Han,              | Chadwick  | T     | Davis,        | Blake | Borgeson,  |
| International |         | conference |              | on      | machine        | learning,  |       |                   |           |       |               |       |            |
|               |         |            |              |         |                |            |       | Cathy             | Hartland, | Maria | Kost-Alimova, |       | Sigrun M   |
pages10347–10357.PMLR,2021.
|     |     |     |     |     |     |     |     | Gustafsdottir, |     | Christopher | C   | Gibson, | and Anne E |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | ------- | ---------- |
[41] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Carpenter. Cell painting, a high-content image-
Krause, Sanjeev Satheesh, Sean Ma, Zhiheng based assay for morphological profiling using
Huang, Andrej Karpathy, Aditya Khosla, Michael multiplexed fluorescent dyes. Nature protocols,
| Bernstein, |     | et al. | Imagenet |     | large | scale | visual |     |     |     |     |     |     |
| ---------- | --- | ------ | -------- | --- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- |
11(9):1757–1774,2016.
recognition challenge. International journal of [49] Kok Hao Chen, Alistair N Boettiger, Jeffrey R
computervision,115(3):211–252,2015.
|     |     |     |     |     |     |     |     | Moffitt, | Siyuan | Wang, | and | Xiaowei | Zhuang. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | --- | ------- | ------- |
[42] Noah F Greenwald, Geneva Miller, Erick Moen, Spatiallyresolved,highlymultiplexedrnaprofiling
Alex Kong, Adam Kagel, Thomas Dougherty, in single cells. Science, 348(6233):aaa6090,
| ChristineCamachoFullaway,BriannaJMcIntosh, |      |       |        |       |           |     |        | 2015.         |     |        |        |             |         |
| ------------------------------------------ | ---- | ----- | ------ | ----- | --------- | --- | ------ | ------------- | --- | ------ | ------ | ----------- | ------- |
| Ke                                         | Xuan | Leow, | Morgan | Sarah | Schwartz, |     | et al. |               |     |        |        |             |         |
|                                            |      |       |        |       |           |     |        | [50] Shanshan | He, | Ruchir | Bhatt, | Carl Brown, | Emily A |
Whole-cell segmentation of tissue images with Brown, Derek L Buhr, Kan Chantranuvatana,
| human-level |     | performance |     |     | using | large-scale |     |         |          |        |     |          |        |
| ----------- | --- | ----------- | --- | --- | ----- | ----------- | --- | ------- | -------- | ------ | --- | -------- | ------ |
|             |     |             |     |     |       |             |     | Patrick | Danaher, | Dwayne |     | Dunaway, | Ryan G |
data annotation and deep learning. Nature Garrison, Gary Geiss, et al. High-plex imaging
biotechnology,40(4):555–565,2022. of rna and proteins at subcellular resolution in
[43] Hayden Nunley, Binglun Shao, David Denberg, fixed tissue by spatial molecular imaging. Nature
Prateek Grover, Jaspreet Singh, Maria Avdeeva, biotechnology,40(12):1794–1806,2022.
Bradley Joyce, Rebecca Kim-Yip, Abraham [51] Zizhen Yao, Cindy TJ van Velthoven, Michael
Kohrman, Abhishek Biswas, et al. Nuclear Kunst,MengZhang,DelissaMcMillen,Changkyu
instance segmentation and tracking for Lee, Won Jung, Jeff Goldy, Aliya Abdelhak,
preimplantation mouse embryos. Development, Matthew Aitken, et al. A high-resolution
151(21):dev202817,2024.
transcriptomicandspatialatlasofcelltypesinthe
[44] Adrian Wolny, Lorenzo Cerrone, Athul Vijayan, whole mouse brain. Nature, 624(7991):317–332,
2023.
| Rachele |     | Tofanelli, | Amaya | Vilches | Barro, |     | Marion |     |     |     |     |     |     |
| ------- | --- | ---------- | ----- | ------- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
Louveaux, Christian Wenzl, So¨ren Strauss, [52] David R Stirling, Madison J Swain-Bowden,
DavidWilson-Sa´nchez,RenaLymbouridou,etal. AliceMLucas, AnneECarpenter, BethACimini,
Accurate and versatile 3d segmentation of plant andAllenGoodman. Cellprofiler4: improvements
tissues at cellular resolution. Elife, 9:e57613, inspeed,utilityandusability. BMCbioinformatics,
| 2020. |     |     |     |     |     |     |     | 22:1–11,2021. |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
16

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
[53] Giovanni Palla, Hannah Spitzer, Michal [67] Thomas Kluyver, Benjamin Ragan-Kelley,
Klein, David Fischer, Anna Christina Schaar, Fernando Pe´rez, Brian E Granger, Matthias
Louis Benedikt Kuemmerle, Sergei Rybakov, Bussonnier, Jonathan Frederic, Kyle Kelley,
Ignacio L Ibarra, Olle Holmberg, Isaac Virshup, Jessica B Hamrick, Jason Grout, Sylvain Corlay,
et al. Squidpy: a scalable framework for spatial et al. Jupyter notebooks-a publishing format for
omics analysis. Nature methods, 19(2):171–178, reproduciblecomputationalworkflows. InELPUB,
| 2022. |     |     |     |     |     |     |     | pages87–90,2016. |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
[54] Guido Van Rossum and Fred L. Drake. Python 3 [68] Ilya Loshchilov and Frank Hutter. Decoupled
Reference Manual. CreateSpace, Scotts Valley, weight decay regularization. arXiv preprint
| CA,2009. |     |     |     |     |     |     |     | arXiv:1711.05101,2017. |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
[55] Adam Paszke, Sam Gross, Francisco Massa, [69] Simon Graham, Quoc Dang Vu, Shan E Ahmed
Adam Lerer, James Bradbury, Gregory Chanan, Raza, Ayesha Azam, Yee Wah Tsang,
Trevor Killeen, Zeming Lin, Natalia Gimelshein, Jin Tae Kwak, and Nasir Rajpoot. Hover-net:
Luca Antiga, Alban Desmaison, Andreas Kopf, Simultaneous segmentation and classification of
Edward Yang, Zachary DeVito, Martin Raison, nuclei in multi-tissue histology images. Medical
Alykhan Tejani, Sasank Chilamkurthy, Benoit imageanalysis,58:101563,2019.
Steiner, Lu Fang, Junjie Bai, and Soumith [70] Kaiming He, Xiangyu Zhang, Shaoqing Ren,
| Chintala. |     | Pytorch: |     | An imperative |     | style, | high- |     |      |      |      |          |     |          |     |
| --------- | --- | -------- | --- | ------------- | --- | ------ | ----- | --- | ---- | ---- | ---- | -------- | --- | -------- | --- |
|           |     |          |     |               |     |        |       | and | Jian | Sun. | Deep | residual |     | learning | for |
performance deep learning library. In Advances image recognition. In Proceedings of the
in Neural Information Processing Systems 32, IEEE conference on computer vision and pattern
pages8024–8035.CurranAssociates,Inc.,2019.
recognition,pages770–778,2016.
| [56] Stefan | Van | Der | Walt, | S Chris | Colbert, | and | Gael |           |              |     |     |         |          |     |     |
| ----------- | --- | --- | ----- | ------- | -------- | --- | ---- | --------- | ------------ | --- | --- | ------- | -------- | --- | --- |
|             |     |     |       |         |          |     |      | [71] Olaf | Ronneberger, |     |     | Philipp | Fischer, |     | and |
Varoquaux. The numpy array: a structure for Thomas Brox. U-Net: Convolutional
| efficient |     | numerical | computation. |     |     | Computing | in  |          |     |                |     |       |     |               |     |
| --------- | --- | --------- | ------------ | --- | --- | --------- | --- | -------- | --- | -------------- | --- | ----- | --- | ------------- | --- |
|           |     |           |              |     |     |           |     | Networks |     | for Biomedical |     | Image |     | Segmentation. |     |
Science&Engineering,13(2):22,2011. arXiv:1505.04597 [cs], May 2015. arXiv:
1505.04597.
[57] EricJones,TravisOliphant,PearuPeterson,etal.
SciPy: Open source scientific tools for Python, [72] Tsung-YiLin,PiotrDolla´r,RossGirshick,Kaiming
2001.
|     |     |     |     |     |     |     |     | He, | Bharath | Hariharan, |     | and | Serge | Belongie. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | --- | ----- | --------- | --- |
[58] G. Bradski. The OpenCV Library. Dr. Dobb’s Featurepyramidnetworksforobjectdetection. In
ProceedingsoftheIEEEconferenceoncomputer
JournalofSoftwareTools,2000.
visionandpatternrecognition,pages2117–2125,
| [59] Christoph |     | Gohlke. |     | cgohlke/imagecodecs: |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2017.
v2024.1.1(v2024.1.1).,2024.
|                |     |         |     |                   |     |           |     | [73] Gihun | Lee, | SangMook |     | Kim, | Joonkee | Kim, | and |
| -------------- | --- | ------- | --- | ----------------- | --- | --------- | --- | ---------- | ---- | -------- | --- | ---- | ------- | ---- | --- |
| [60] Christoph |     | Gohlke. |     | cgohlke/tifffile: |     | v2022.5.4 |     |            |      |          |     |      |         |      |     |
(v2022.5.4),2022. Se-Young Yun. Mediar: Harmony of data-centric
|                          |     |     |            |     |                |     |     | and | model-centric |     | for | multi-modality |     | microscopy. |     |
| ------------------------ | --- | --- | ---------- | --- | -------------- | --- | --- | --- | ------------- | --- | --- | -------------- | --- | ----------- | --- |
| [61] WilliamSilversmith. |     |     | fastremap. |     | https://github |     |     |     |               |     |     |                |     |             |     |
arXivpreprintarXiv:2212.03465,2022.
.com/seung-lab/fastremap,2023.
[74] TitusGriebel,AnwaiArchit,andConstantinPape.
| [62] Casper |     | O. da    | Costa-Luis. |       | ‘tqdm‘:    | A   | fast, |         |     |          |     |                 |     |     |       |
| ----------- | --- | -------- | ----------- | ----- | ---------- | --- | ----- | ------- | --- | -------- | --- | --------------- | --- | --- | ----- |
|             |     |          |             |       |            |     |       | Segment |     | anything | for | histopathology. |     |     | arXiv |
| extensible  |     | progress |             | meter | for python | and | cli.  |         |     |          |     |                 |     |     |       |
preprintarXiv:2502.00408,2025.
| Journal | of  | Open | Source | Software, |     | 4(37):1277, |     |          |            |     |      |         |            |     |       |
| ------- | --- | ---- | ------ | --------- | --- | ----------- | --- | -------- | ---------- | --- | ---- | ------- | ---------- | --- | ----- |
|         |     |      |        |           |     |             |     | [75] Jun | Ma, Ronald |     | Xie, | Shamini | Ayyadhury, |     | Cheng |
2019.
|                       |     |              |                         |            |         |            |      | Ge,     | Anubha         | Gupta,    |            | Ritu         | Gupta, | Song       | Gu,      |
| --------------------- | --- | ------------ | ----------------------- | ---------- | ------- | ---------- | ---- | ------- | -------------- | --------- | ---------- | ------------ | ------ | ---------- | -------- |
| [63] MarkSummerfield. |     |              | RapidGUIProgrammingwith |            |         |            |      |         |                |           |            |              |        |            |          |
|                       |     |              |                         |            |         |            |      | Yao     | Zhang,         | Gihun     |            | Lee, Joonkee |        | Kim,       | et al.   |
| Python                | and | Qt:          | The                     | Definitive | Guide   | to         | PyQt |         |                |           |            |              |        |            |          |
|                       |     |              |                         |            |         |            |      | The     | multi-modality |           | cell       | segmentation |        | challenge: |          |
| Programming           |     | (paperback). |                         |            | Pearson | Education, |      |         |                |           |            |              |        |            |          |
|                       |     |              |                         |            |         |            |      | towards |                | universal | solutions. |              |        | arXiv      | preprint |
2007.
arXiv:2308.05864,2023.
| [64] Luke         | Campagnola. |     |     | Scientific | graphics | and | gui |              |     |           |      |        |            |            |     |
| ----------------- | ----------- | --- | --- | ---------- | -------- | --- | --- | ------------ | --- | --------- | ---- | ------ | ---------- | ---------- | --- |
|                   |             |     |     |            |          |     |     | [76] Weimiao |     | Yu, Hwee  | Kuan | Lee,   | Srivats    | Hariharan, |     |
| libraryforpython. |             |     |     |            |          |     |     | WenYu        | Bu, | andSohail |      | Ahmed. | Ccdb:6843, |            | mus |
https://github.com
[65] Talley Lambert. superqt. musculus,neuroblastoma. CellImageLibrary.
/pyapp-kit/superqt,2023.
|     |     |     |     |     |     |     |     | [77] Vebjorn |     | Ljosa, | Katherine |     | L. Sokolnicki, |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --------- | --- | -------------- | --- | --- |
[66] John D Hunter. Matplotlib: A 2d graphics Anne E. Carpenter. Annotated high-throughput
environment. Computing in science & microscopy image sets for validation. Nature
| engineering,9(3):90,2007. |     |     |     |     |     |     |     | Methods,9(7):637–637,July2012. |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
17

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
[78] Thouis R. Jones, Anne Carpenter, and Polina
Golland. Voronoi-Based Segmentation of Cells
on Image Manifolds. In Yanxi Liu, Tianzi Jiang,
and Changshui Zhang, editors, Computer Vision
forBiomedicalImageApplications,LectureNotes
in Computer Science, pages 535–543, Berlin,
Heidelberg,2005.Springer.
[79] OMERO. Imagedataresource.
[80] ShanEAhmedRaza,LindaCheung,Muhammad
Shaban, Simon Graham, David Epstein, Stella
Pelengaris, Michael Khan, and Nasir M. Rajpoot.
Micro-Net: A unified model for segmentation of
various objects in microscopy images. Medical
ImageAnalysis,52:160–173,February2019.
[81] Konstantin Lopuhin. kaggle-dsbowl-2018-
dataset-fixes,2018.
[82] Pedro Matos Pereira and Mariana Pinho.
Deepbacs – staphylococcus aureus widefield
segmentationdataset,October2021.
[83] ChristophSpahnandMikeHeilemann. Deepbacs
– escherichia coli bright field segmentation
dataset,October2021.
[84] Se´amus Holden and Mia Conduit. Deepbacs
– bacillus subtilis fluorescence segmentation
dataset,October2021.
18

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
| imagesize |          | GPURAM         | RAMused    |           |           |
| --------- | -------- | -------------- | ---------- | --------- | --------- |
|           | filesize |                |            | batchsize | runtime   |
| (pixels)  |          | used(reported) | (reported) |           |           |
| 150       | 270KB    | 2.45GB         | 2.18GB     | 1         | 0.37sec   |
| 300       | 1.08MB   | 2.45GB         | 2.18GB     | 4         | 0.41sec   |
| 600       | 4.32MB   | 3.39GB         | 2.23GB     | 9         | 0.87sec   |
| 1,200     | 17.2MB   | 8.90GB         | 3.57GB     | 32        | 3.24sec   |
| 2,400     | 69MB     | 8.90GB         | 3.84GB     | 32        | 12.48sec  |
| 4,800     | 276MB    | 8.90GB         | 4.80GB     | 32        | 46.71sec  |
| 9,600     | 1.11GB   | 12.28GB        | 18.40GB    | 32        | 368.88sec |
TableS1: GPUstatisticsforinference.RuntimesandmemoryprofilingformodelinferenceonaconsumerGPU(RTX4070S,$600,12GB
ofGPURAM)onWindowswithamaximumbatchsizeof32fordifferentimagessizes.
|      |      | GPURAM | GPURAM         | RAMused    |         |
| ---- | ---- | ------ | -------------- | ---------- | ------- |
| GPUs | MSRP |        |                |            | runtime |
|      |      | max    | used(reported) | (reported) |         |
$300
| RTX4060   |          | 8GB  | 8.53GB | 3.01GB | 363.58sec |
| --------- | -------- | ---- | ------ | ------ | --------- |
| T4(colab) | free     | 16GB | 8.53GB | 1.81GB | 185.17sec |
| RTX4070S  | $600     | 12GB | 8.53GB | 1.87GB | 55.08sec  |
| RTX5090   | $2,000   | 32GB | 8.53GB | 2.56GB | 33.71sec  |
| A100      | >$10,000 | 80GB | 8.53GB | 2.26GB | 27.30sec  |
TableS2: GPUstatisticsfortraining.Runtimesandmemoryprofilingformodeltrainingwithasmallnumber(8)ofuserprovidedannotated
imageswithabatchsizeof1,epochsizeof8,and100epochs.Typicalforthehuman-in-the-loopretrainingstage.
19

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
 & H O O S R V H  1 X F O H L  7 L V V X H Q H W  / L Y H F H O O  2 P Q L S R V H
 ' H H S E D F V  < H D ] \  1 H X U L S V  % & & '  F R Q L F
 F S P    F S P    F U \ R Q X V H J  L K F W P D  O \ Q V H F
 P R Q X V D F  P R Q X V H J  Q X L Q V V H J  S D Q Q X N H  W Q E F
S1: Exampletrainingimages. Imagesoriginatefromatotalof20distinctdatasets. FortheCellposedataset,theindividualimageisnot
representativeoftheheterogeneityofthedataset(seeFigure2a).
20

bioRxiv preprint doi: https://doi.org/10.1101/2025.04.28.651001; this version posted May 1, 2025. The copyright holder for this preprint (which
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY-NC 4.0 International license.
Tissuenet Livecell Omnipose (PhC) Omnipose (fluor) DeepBacs MoNuSeg
|     | n=1,249 |     | n=1,512 |     | n=148 |     | n=75 |     | n=35 | n=14 |
| --- | ------- | --- | ------- | --- | ----- | --- | ---- | --- | ---- | ---- |
|     | *       |     | ***     |     | ***   |     | n.s. |     | **   |      |
|     | ***     |     | ***     |     | n.s.  |     | ***  |     | ***  | n.s. |
|     | ***     |     | ***     |     | ***   |     | ***  |     | ***  | **   |
generalists 0.8
Cellpose-SAM 0.7
Cellpose UoI 5.0 @ etar rorre 0.6
cyto3
0.5
CellSAM
microSAM 0.4
specialists 0.3
SAMCell 0.2
PathoSAM
0.1
Omnipose
0.0
M se cyto 3 M M M to 3 M Cell M to 3 nipos e M M to 3 nipos e M M se cyto 3 M M M M M
S A ellS A icroSA S A se cy roSA M S A se cy ellSA S A se cy ellSA S A ellS A icroSA Cellpose-SA ellS A thoSA
| se - |     | se - | ic A | se - | m   | se - | m   | se - |     |     |
| ---- | --- | ---- | ---- | ---- | --- | ---- | --- | ---- | --- | --- |
Cellpo o C m Cellpo o m S Cellpo o O C Cellpo o O C Cellpo o C m C P a
| e l lp |      | e   | l lp | e l lp |     | e l lp |      | e l lp |     |     |
| ------ | ---- | --- | ---- | ------ | --- | ------ | ---- | ------ | --- | --- |
| C      |      | C   |      | C      |     | C      |      | C      |     |     |
|        | n.s. |     | ***  |        | *** |        | n.s. |        | *** |     |
|        | ***  |     | ***  |        | *   |        | ***  |        | *** | **  |
|        | ***  |     | ***  |        | *** |        | ***  |        | *** | *   |
1.0
UoI 5.0 @ )PA( noisicerp egareva
0.9
0.8
0.7
0.6
0.5
0.4
0.3
S2: Segmentationperformanceonotherdatasets. SimilartoFigure2de. Performanceisreportedwitheithererrorrates(top)orAP@
IoU=0.5(bottom). Algorithmsareincludedineachpanelif: 1)theyhavebeentrainedontherespectivedataset;2)theyusedthepublicly
availabletrain/testsplit. Wedidnotretrainanyofthealgorithmsfromothergroups. Specialistmodelswereonlytrainedonasingledataset.
Wilcoxonsigned-ranktestperformed-CellposeSAMperformsaswellas(n.s.) orsignificantlybetterthanallotheralgorithms, besidesthe
specialistOmniposemodelontheOmnipose(fluor)dataset.
21
