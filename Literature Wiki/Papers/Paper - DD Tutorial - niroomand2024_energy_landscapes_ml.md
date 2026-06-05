---
tags:
  - literature
  - type/paper
  - lit/nanomedicine
  - lit/ai-methods
  - lit/digital-discovery
type: literature-note
status: converted
source_type: pdf
source_file: "niroomand2024_energy_landscapes_ml.pdf"
pdf: "_attachments/Digital Discovery/niroomand2024_energy_landscapes_ml.pdf"
markitdown_source: "_data/markitdown/Paper - DD Tutorial - niroomand2024_energy_landscapes_ml.md"
title: "Insights into machine learning models from chemical physics: an energy landscapes approach (EL for ML)"
authors: "Maximilian P. Niroomand, Luke Dicks, Edward O. Pyzer-Knapp, David J. Wales"
year: "2024"
doi: "10.1039/D3DD00204G"
journal: "Digital Discovery"
article_type: "Tutorial Review"
citation_count_crossref: 6
topics:
  - Machine Learning
  - Chemical Physics
  - Model Interpretability
---

# Insights into machine learning models from chemical physics: an energy landscapes approach (EL for ML)

**Key:** `niroomand2024_energy_landscapes_ml`  
**Year:** 2024  
**DOI:** [10.1039/D3DD00204G](https://doi.org/10.1039/D3DD00204G)  
**Article type:** Tutorial Review  
**Crossref citations:** 6  
**PDF:** [[_attachments/Digital Discovery/niroomand2024_energy_landscapes_ml.pdf]]  
**Raw MarkItDown:** [[_data/markitdown/Paper - DD Tutorial - niroomand2024_energy_landscapes_ml.md]]

## Why It Matters

Connects chemical-physics energy-landscape methods to machine-learning loss landscapes, useful for interpretability and optimization framing.

## Connections

- [[Concept - Materials Discovery]]
- [[Concept - Optimization and Bayesian Search]]

## Converted Text

Showcasing research from the collaboration between
As featured in:
the groups of Professor Wales - Yusuf Hamied,
Department of Chemistry, University of Cambridge,
and Dr Pyzer-Knapp - IBM Research Europe.
Insights into machine learning models from chemical
physics: an energy landscapes approach (EL for ML)
This work showcases how principles from Chemical Physics,
namely the Energy Landscapes approach, can be applied
to machine learning models. We show how various physical
properties fi nd analogues in machine learning systems, and
how these properties can be employed to both increase
understanding of the machine learning ‘black-box’ and
enhance the performance of machine learning models.
See Edward O. Pyzer-Knapp,
David J. Wales et al.,
Digital Discovery, 2024, 3, 637.
rsc.li/digitaldiscovery
Registered charity number: 207890

Digital
Discovery
| TUTORIAL |     | REVIEW |     |     |     |     |     |     |     |     |     | View Article Online |     |     |
| -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- |
View Journal | View Issue
|     |     |     | Insights |     | into | machine |     | learning |     | models |     | from |     |     |
| --- | --- | --- | -------- | --- | ---- | ------- | --- | -------- | --- | ------ | --- | ---- | --- | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  chemical physics: an energy landscapes approach
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO Citethis:DigitalDiscovery,2024,3,
|     |     |     | (EL | for | ML) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
637
|     |     |     |            |       |               |     | a    |        | b      |     |                |     | *b  |     |
| --- | --- | --- | ---------- | ----- | ------------- | --- | ---- | ------ | ------ | --- | -------------- | --- | --- | --- |
|     |     |     | Maximilian |       | P. Niroomand, |     | Luke | Dicks, | Edward |     | O. Pyzer-Knapp |     |     |     |
|     |     |     | and        | David | J. Wales      | *a  |      |        |        |     |                |     |     |     |
Thestudyofenergylandscapesasaconceptualframework,andasourceofnovelcomputationaltools,isan
active area of research in chemistry and physics. The energy landscape provides insight into structure,
dynamics,andthermodynamicswhencombinedwithtoolsfromstatisticalmechanicsandunimolecular
ratetheory.Thisapproachcanalsobeappliedtoquestionsthatariseinmachinelearning.Here,theloss
landscape (LL) of a machine learning system is treated in the same way as the energy landscape for
Received9thOctober2023
Accepted26thJanuary2024 amolecularsystem.Inthiscontributionwesummariseanddiscussapplicationsofenergylandscapesfor
machine learning (EL4ML). We will outline how various physical properties find analogues in machine
DOI:10.1039/d3dd00204g learning systems, and show how these properties can be employed to both increase understanding of
themachinelearning‘black-box’andenhancetheperformanceofmachinelearningmodels.
rsc.li/digitaldiscovery
1 Introduction functionandidentifythelowest-lyingsolution.Ina(supervised)
|     |     |     |     |     |     |     | machine | learning | system, |     | this solution | is  | the set of weights/ |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------- | --- | ------------- | --- | ------------------- | --- |
hyperparametersdescribinganarbitraryfunctionthatbestts
| In the | physical | sciences, | energy | landscapes1 |     | provide |     |     |     |     |     |     |     |     |
| ------ | -------- | --------- | ------ | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
a computational framework to predict structure, thermody- someinputdatatoknownoutputs.
namics, and dynamics.2 Exploring the energy landscape In ML there is an additional consideration, requiring
means computing the potential energy E for a given atomic amodelgeneralisingwelltounseendata.Foragivenmachine
conguration, dened by the coordinates of the individual learning algorithm and some data, the loss landscape
ℝ3. describes the quality of each possible weight/hyperparameter
| atoms in | The | potential | energy | surface | (PES) | gives the |     |     |     |     |     |     |     |     |
| -------- | --- | --------- | ------ | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
energy for any combination of coordinates of the individual combination.Importantly,thesemodelsareonlyconditioned
atoms. The PES is a continuous, non-convex function, in on the training data, hence the LL cannot make a statement
whichlocalminimacorrespondtolocally-stablestatesofthe about generalisation to unseen testing data. Numerous loss
system, and potentially interesting congurations. The Mur- functions exist, from simple mean squared error losses to
rell–Laidler cross-entropy,contrastive,orapproximateAUClossfunctions.
|     | theorem | states | that the | lowest | barrier | between |     |     |     |     |     |     |     |     |
| --- | ------- | ------ | -------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
local minima involves a pathway mediated by index one Thus, the correlation between loss value and performance of
saddle points (transition states).3 These transition states are the minimum must be viewed with caution. The global
essentialtodescribingthedynamicsofaphysicalsystem.An minimumoftheLListhebestguessastowhichsetofweights
illustrative PES is shown in Fig. 1, where the zero-gradient maybeoptimalforthespecicproblem,butoptimalitycannot
|            |       |              |         |     |        |         | be guaranteed. |     | Train-test |     | generalisability |     | is not the focus | of  |
| ---------- | ----- | ------------ | ------- | --- | ------ | ------- | -------------- | --- | ---------- | --- | ---------------- | --- | ---------------- | --- |
| transition | state | separatestwo | minima. | The | global | minimum |                |     |            |     |                  |     |                  |     |
corresponds to the lowest potential energy achievable for this contribution, but the reader should keep this issue in
| agivensystem,whichcorrespondstotheequilibriumstateat |     |     |     |     |     |     | mind. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
lowtemperature. Tocharacterisethelosslandscape(LL)ofamachinelearning
In machine learning, the problem posed is analogous to system, only the training data is relevant. Hence, the global
optimisingatomisticarrangementsinmolecularsystems.Given minimumisthesetofweightsthatminimisetheloss(energy)
asetofvariables(weights,hyperparametersetc.),alossfunction foragivencost/lossfunctionandtrainingdata.Notethatthis
is minimised to provide the best possible solution to the setupimpliesthat,forastandardlossfunction,overttingthe
modeltotrainingdataisencouragedbytheformulationofthe
| problem. | As for | molecular | systems, | machine | learning | is  | an  |     |     |     |     |     |     |     |
| -------- | ------ | --------- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
optimisation problem, with the aim to minimise the cost problem. Thus, ideally, the model would perfectly predict the
|     |     |     |     |     |     |     | correct | output | for each | input, | irrespective |            | of performance | on   |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | -------- | ------ | ------------ | ---------- | -------------- | ---- |
|     |     |     |     |     |     |     | unseen  | data.  | In Table | 1,     | we have      | summarised | the            | most |
aUniversityofCambridge,DepartmentofChemistry,Cambridge,UK.E-mail:mpn26@
|     |     |     |     |     |     |     | important |     | features to | describe | an energy | landscape, | and | what |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- | -------- | --------- | ---------- | --- | ---- |
cam.ac.uk;dw34@cam.ac.uk
theymeanwhentranslatedtoaMLsetting.
bIBMResearchUK,Daresbury,UK.E-mail:EPyzerK3@uk.ibm.com
©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2024,3,637–648 | 637

DigitalDiscovery TutorialReview
Fig.1 Asimplifiedpotentialenergylandscape.Eachvalueoftheredlineisthepotentialenergyataspecificsetofatomcoordinates.Hence,the
redlineisanenergyfunctionfforsomemolecule.
Table1 ComparisonofenergylandscapesfeaturesinmolecularsystemsandtheiranalogueinMLsystems
Feature MolecularPES MLLL
Energy Potentialenergy Lossvalue
Temperature Physicaltemperature Fictitiousparameter
Coordinates Atomisticcoordinates Weights/hyperparameters
Localminimum Locally-stablemolecularisomer Locallyoptimalweights
Globalminimum Energeticallymostfavourablemolecularisomer Bestweightsforgivenlossfunction
2 Motivation: EL4ML systems20–22canbeanalysed.Forreasonsofcomputationalcost,
itiscommonpracticeinmachinelearningtostartfromagiven
Machine learning has become one of the most active elds in setofinitialweights,choseneitherrandomlyorbysomeiniti-
scienceduetoitsimpactacrossabroadrangeofapplications. alisation scheme,23 minimise the loss as far as possible with
These applications range from games, such as chess,4 Go,5 or a greedy algorithm, and accept this result for the trained
the collaborative Dota 26 to autonomous driving (covered weights. Perhaps unexpectedly, this procedure seems to work
extensivelyinref.7),proteinstructureprediction8mathematical well,andvariousexplanationsforthisfortuitoussituationhave
proofs,9 chat bots,10,11 image generation12,13 and many more. been suggested.24,25 The most prominent suggestion derives
Applications to the physical sciences, including force-eld from Goodfellow et al.26 They report what they call the Mono-
parametrisation are discussed in ref. 14. This list is far from tonic Linear Interpolation (MLI) property, the fact that there
exhaustive, andnovelmachinelearningmodelsaredeveloped usually exists a monotonically decreasing path between some
and open-sourced every day. The basic foundation of the initialsetofparametersq andsomeminimumq identiedby
i o
machine learning approach is that, given enough data and somemethodsuchasstochasticgradientdescent.Theinsight
computationalresources,thettingandpredictionproblemis thatthispropertyexists,despitenon-convexlossfunctionsand
solvableinprinciple.Infact,itcanbeshownthat,givenenough non-linear training sets raises questions, but might be
parameters, any dataset can be tted perfectly by a machine explainedby the factthat, givenenough data,manyproblems
learningmodel.15However,weseekadeeperunderstandingof simplyarenotthatdifficult.Theseresultsreceivedconsiderable
whyandwhenmachinelearningworks,andthefactthatthere attention in the eld, and the matter is likely to be more
existsafunctiontomapgiveninputtooutputdoesnotprovide complicated.Lucasetal.27areabletocreatecounterexamplesto
understanding or interpretation of which features from the theMLIpropertyandothershaveobserveddifferentresultsto
inputleadthemodeltoagivenoutputchoice. Goodfellow et al.26 when revisiting the work on more modern
Interpretability in ML has received increasing attention16–18 architectures and data sets.28 Further doubt that ‘Machine
with the realisation that in many elds, an understanding of learningmayjustbesimple’iscastinref.29showingthatthe
whyacertainpredictionisbeingmade,isasimportantasthe MLIdoesnotalwaysholdandmustbeconsideredwithcaution.
accuracy. Unfortunately, interpreting a high-dimensional and In general, simply considering a linear interpolation from an
complexfunctionisdifficult.19Recenteffortsininterpretability initialsetofweightstotheidentiedminimummaybeinsuf-
have been summarised in Zhang et al.16 Usually, these cient and all the aforementioned papers agree that further
approachesrevolvearoundunderstandingthegradientsofthe studyandconsiderationoftheML-LLisofcriticalimportance.
loss function with respect to the input, to understand how Otherworkhasshownthatconvergencetoaglobalminimum
changes in the input affect the output, as in Davies et al.9 for overparameterised networks under certain, somewhat
However, given the relatively high complexity of machine restrictive conditions, is provable.30 These interpretability
learningmodelssuchasneuralnetworks,thisanalysisisoen approaches share the commonality that large areas of the LL
insufficientanddoesnotprovideacompletepicture.19 and its complex geometric features remain unexplored. In
To better understand the foundations of machine learning practice is not always guaranteed that the global minimum is
capabilities, the loss landscapes of machine learning identied,andnoconsiderationisgiventotheshapeoftheLL
638 | DigitalDiscovery,2024,3,637–648 ©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry
.MA
65:61:3
6202/1/6
no
dedaolnwoD
.4202 yraurbeF
80
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

TutorialReview DigitalDiscovery
ortheexistenceofotherlocalminima.Whilesuchresultsmay change the landscape, but can signicantly modify the rate of
besufficientintermsofperformance,itisnothelpfulinterms exploration.
of interpretability. Understanding the LL has the potential to Theenergylandscapeapproachisfeasibleifthenumberof
provide some of the missing understanding.31 Specically, variablesinthettingspaceisnottoolarge(uptoperhaps104),
understanding the topography of a loss landscape can allow andthehopeistodevelopunderstandingthatistransferableto
novel insights into the convergence process or optimiser path the much larger problems oen employed in deep learning
takentowardstheglobalminimum. models. To analyse the LL using the energy landscape frame-
Another suitable task for global optimisation based LL work,globaloptimisationisperformedinitially,thesetoflow-
explorationistheefficientenumerationandanalysisofvarious valuedminimaarestored,andtheirconnectedtransitionstates
minima. Using generic tools, surveying large areas of the loss are located. In a rst step, the global minimum of the LL is
landscape is expensive and time consuming, while the explo- identied,whichiscommonlydoneusingbasin-hoppingglobal
rationtoolsoutlinedbelowsubstantiallysimplifytheproblem. optimisation.39,40 Starting from any initial values for the
Energy landscapes are reasonably well understood for parameters, this procedure progresses by local minimisation.
moleculesandcondensedmatter,andthehopeexiststhatsome Stepstonewminimaareacceptedorrejected,commonlyusing
oftheassociatedmethodologycouldhelptobetterunderstand a Metropolis-type60 condition, and steps are proposed by per-
machine learning. Importantly, since a loss function is ubiq- turbingtheparameterscorrespondingtothecurrentminimum
uitousinanymachinelearningsystem,considerationoftheLL inthechain.Localminimisationsareusuallyperformedusing
isapplicableinabroadrangeofelds.Whilemostworkhasso the LBFGS routine. For a Metropolis accept/reject scheme,
farconsideredneuralnetworks,20,31LLshavealsobeenanalysed anewminimumisalwaysacceptedifitsenergy(lossfunction)
inthecontextofclusteringmethods,suchasK-means32orfor is lower, and is also accepted if the energy is higher with
Gaussian processes33 in Bayesian machine learning.34 These probability
!
c
la
o
n
n
d
tr
s
i
c
b
a
u
p
t
e
io
s
n
v
s
iew
su
o
g
f
g
m
es
a
t
c
a
h
n
in
o
e
th
l
e
e
r
ar
u
n
s
in
ef
g
u
.
l
En
pr
ti
o
r
p
e
e
ly
rt
d
y
iff
o
e
f
re
th
n
e
tm
en
o
e
d
r
e
g
ls
y
Pfexp (cid:1)
DE ~
(1)
can now be compared with each other, not just for output
kBT
metrics such as accuracy, but for the solution landscapes. whereDE ~ isthedifferenceinenergybetweenthenewminimum
Understandinghowmanyminimaexistforagivenmodel,how
andtheoldminimuminthechain,k theBoltzmannconstant
B
theyareconnected,theirrelativevolumes inparameterspace, andTactitioustemperature.Iftheenergydifferencebetween
andhowquicklyanoptimiserconvergesforthem,mayprovide
theoldandnewminimaislargeandpositive,themoveisless
importantinsightsintomodelselection.21
likely to be accepted. Uphill steps are needed to escape from
traps in the landscape, and the value of the k T parameter is
B 3 LL exploration
chosentobalancelocalandglobalexploration.
Localminimadonotconstitutealandscape.Tounderstand
There are a variety of methods developed in chemical physics theorganisationofsolutionspace,transitionstates,denedas
for exploring potential energy landscapes. Some of these
saddle points with Hessian index one3 need to be located.
methods are commonly referred to as enhanced sampling,
Transition states mediate the pathways between minima with
including meta-dynamics,35 umbrella sampling,36 and replica- the lowestbarriers according tothe Murrell–Laidler theorem.3
exchange molecular dynamics;37 a recent review is given by
Here, double-ended searches are usually employed to connect
ref.38.Analternativeapproachsuitableforbothpotentialand
each selected pair of minima, using the doubly-nudged61,62
lossfunctionsurfacesistheenergylandscapeframework. elastic band63–66 method to identify likely candidates for accu-
Global optimisation algorithms aim to nd the lowest rate renement using hybrid-eigenvector following.67–69 These
minimum, amongst the (possibly) many local minima and methods require continuous rst and second derivatives, but
funnels. In global optimisation for physical systems popular
even for loss functions without these properties, such as K-
algorithms are basin-hopping39–41 and genetic algorithms.42 In
means, landscapes can still be explored using algorithmic
ML,itiscommontosimplyusevariousrandominitialisations
adaptations.32 These geometry optimisation tools have been
and local minimisation, which has limited use in physical renedforawiderangeofproblemsoverseveraldecades,and
systems.43 Examples of random, or pseudo-random, initialisa-
areimplementedintheGMIN,70OPTIM71andPATHSAMPLE72
tion and minimisation are seen in K-means,44–46 Gaussian
programs,73allavailableforuseundertheGNUGeneralPublic
processes,47andneuralnetworks.Allthesemethodsrelyupon
License.
minimisation algorithms to locate local minima of the cost
Global optimisation and subsequent transition state
functionsurfaces,andcommonchoicesarelimited-memory48,49
searchesprovidesthefoundationsforafullcharacterisationof
quasi-Newton Broyden,50 Fletcher,51 Goldfarb,52 Shanno53 (L-
theenergylandscape/LLofaparticularsystem.Thisapproachis
BFGS) routine and its variants with box-constraints54,55 for
clearlymuchmorecomputationallyexpensivethanonlyasingle
bounded problems such as tting Gaussian processes. Conju-
optimisation pass, but the objective here is to understand the
gate gradient approaches can leverage matrix multiplication
structureofthesolutionspace,nottoseekpredictionsforany
tricks to address larger datasets,56,57 and stochastic gradient
particularproblem.TheLLitselfisgenerallyunboundedfrom
descent scales well with dataset size due to only considering
above.Regularisationmethodsorotherconstraintsareusually
a portion of the data.58,59 The choice of minimiser should not
©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2024,3,637–648 | 639
.MA
65:61:3
6202/1/6
no
dedaolnwoD
.4202 yraurbeF
80
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

DigitalDiscovery TutorialReview
employed to reduce overtting problems,74,75 which tends to p~e a q(T)=pe a q(T)/(1−pe gm q in (T)).As discussedabove,theeffective
keepthettingparameterswithinasensiblerange. temperature T is simply a parameter to interrogate the land-
scapeinmachinelearningsystems.StudyingSðTÞorFðTÞover
4 Physical properties and analogues arangeofvaluesforTatthesystemtemperaturecorresponding
to the peaks in heat capacity curves reveals features of the
for ML
landscape comparable to the analysis of molecular and
condensed matter systems in,76 where various metrics are
Machine learning loss landscapes are analogous to energy
compared.AnexampleisgiveninFig.2.Here,thelandscapeon
landscapesandcanbeinterrogatedtoextracttheanaloguesof the le is an ideal single funnel, where locating the global
thermodynamic and kinetic properties, which constitute the
minimumisstraightforwardoverawiderangeoftemperatures.
key observables for molecular systems. When characterising
Incontrast,locatingthetrueglobalminimumforthelandscape
a landscape, we can loosely distinguish two sets of metrics: onthe right ismore difficult. However,if alternative low-lying
globalandlocal.Globalmetricscharacteriseoverallproperties
minimaprovidegoodsolutionsthenitwill bestraightforward
ofthelandscape,andlocalmetricsdistinguishdifferenttypesof
to locate a member of this set. Importantly, the alternative
solutions(i.e.minima).Theformermetricsallowforacharac- minima will probably have different properties, and perhaps
terisation of the whole solution space for archetypal datasets, provide slightly different predictions. Nevertheless, this struc-
and provide a better understanding of the nature of the opti-
ture may be more robust to initialisation noise and multiple
misationproblem.Thedistinctionisfuzzyandseveralmetrics
such minima could be combined in ensembles to improve
haveimportantfeaturesinbothclasses.Adiscussionofsomeof
overall accuracy. In machine learning applications,
F~ðTÞ
has
themost usefulpropertiesisgivenbelow, andsummarisedin importanteffectsontrainingreproducibilityandmaycorrelate
Table2. withbatchingeffects.Sincethesameminimumismorelikelyto
befoundrepeatedlyinunfrustratedlandscapes,trainingthese
4.1 Globallandscapemetrics systems is more reproducible and variation in output is less
4.1.1 Frustration index. The frustration index is a metric likely to come from initialisation noise. High-frustration
that was designed to report on the existence of low-lying surfaces may further be more prone to batch effects, or at
minima separated from the global minimum by high
leasthaveincreasedvariancewithbatcheffects.Likeabove,this
barriers.76Thismetricreectsthedifficultyofrelaxationtothe isduetothehighlikelihoodofindividualminimabeingovert
equilibrium occupation probabilities, which will likely corre-
tospecicaspectsoftheinputdata.
spondtothedifficultyofglobaloptimisationonthesurface.An 4.1.2 Heat capacity. The heat capacity of a system is
importantdifferencebetweenthefrustrationindex,FðTÞ,and denedastheamountofenergy(heat)thathastobeaddedto
theShannonentropy,77SðTÞ,isthatFðTÞaccountsfortransi- achieve a unit change in temperature. Wales78 describes
tion states and barriers, while the Shannon entropy considers a theoretical framework that enables features of the heat
only the equilibrium thermodynamic properties of local capacity to be connected to particular local minima in the
minima.TheShannonentropyisgivenby energy landscape. Normal mode analysis for each minimum
X allows a harmonic superposition approximation to the vibra-
SðTÞ¼(cid:1) pe a qðTÞlnpe a qðTÞ; (2) tional density of states. Given the partition function for some
a minimuma
Q
at some temperature, T, and equilibrium occupation proba- 2 N!(cid:2) (cid:3) (cid:2) (cid:3)
bility, pe a q, for minimum a. In contrast, the frustration metric Z ðTÞ¼ s s kBT k e(cid:1)Va =kBThn kBT k e(cid:1)Va =kBT; (4)
hastheform a o a hn a a hn a
(cid:2) (cid:3)
FðTÞ¼ X peqðTÞ L† a (cid:1)L gmin (3) where k = 3N − 6 is the number of vibrational degrees of
asgmin a L a (cid:1)L gmin freedom for N atoms, k B the Boltzmann constant, (cid:2)n a the
geometricmeannormalmodevibrationalfrequency,ameasure
where L a is the loss value of minimum a, and L† a is the loss ofbasingeometry,o a theorderofthemolecularpointgroup,T
value of the highest transition state of the lowest energy path thetemperatureandV thepotentialenergyofminimumg,the
g
between minimum a and the global minimum. The loss val- corresponding internal energy E and heat capacity C can be
V
ue of the global minimum is denoted L gmin . To compare derived. By dening the harmonic superposition partition
between systems, we can consider F~ðTÞ dened in terms of
Table2 InterpretationofphysicalcharacteristicsformolecularenergylandscapesandmachinelearningLLs
Feature MolecularPES MLLL
Basinvolume Entropiccontributiontooccupationprobability Connectiontorobustness
Heatcapacity Changeinoccupiedminimaasafunctionof Identicationofminimawithcomplementaryproperties
temperature
Frustration Propensityforbrokenergodicity Implicationsforoptimisationandtraining
640 | DigitalDiscovery,2024,3,637–648 ©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry
.MA
65:61:3
6202/1/6
no
dedaolnwoD
.4202 yraurbeF
80
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
a rednu
desnecil
si
elcitra
sihT
View Article Online

View Article Online
| TutorialReview |     |     |     |     |     |     |     |     |     |     |     | DigitalDiscovery |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO
Fig. 2 Examples for two distinct loss landscapes, visualised using disconnectivity graphs, with drastically different frustration indices. The
landscapeontheleftisanidealsinglefunnel,whilethelandscapeontherighthasmanylow-lyingminima(acceptablesolutions),whichare
equallyaccessible,potentiallymakingthislandscapemorerobust.
function, and using some elementary identities, a novel ‘specialise’ in different parts of the input data, so that better
formulationoftheheatcapacitycanbederived.78Peaksinthe predictionscanbeobtainedbyemployingalternativesolutions
heat capacity curve can be interpreted by looking at the fromtheLLfordifferentinput.Theheatcapacityprovidesaway
contributionofminimawithpositiveandnegativetemperature toidentifythese‘different’minimawithcontrastingproperties.
derivatives In applications such as ensemble learning, this capability is
|     |           |     |         |                   |     |         |     | highly relevant. | Combining | different |     | minima enhances |     |
| --- | --------- | --- | ------- | ----------------- | --- | ------- | --- | ---------------- | --------- | --------- | --- | --------------- | --- |
|     | gg XðTÞ.0 |     | (cid:4) | (cid:5) gg XðTÞ\0 |     | (cid:4) |     | (cid:5)          |           |           |     |                 |     |
signicantly
CV ¼kkB þ g ðTÞ V (cid:1)hVi þ g ðTÞ V (cid:1)hVi ensemble methods beyond randomly choosing
|     |     | g   | g   | min | g   | g   | min |                    |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
|     |     | g   |     |     | g   |     |     | asubsetofminima.80 |     |     |     |     |     |
hkkB þCþðTÞþC(cid:1)ðTÞ 4.1.3 Network properties. The representation of the
(5)
|               |     |          |         |            |             |     |       | continuous surface | by a weighted                        | graph, | or  | kinetic transition |     |
| ------------- | --- | -------- | ------- | ---------- | ----------- | --- | ----- | ------------------ | ------------------------------------ | ------ | --- | ------------------ | --- |
| This analysis |     | tells us | how the | occupation | probability |     | shis |                    |                                      |        |     |                    |     |
|               |     |          |         |            |             |     |       | network81–84allows | graphalgorithmstobeappliedtogenerate |        |     |                    |     |
between local minima as a function of the temperature physical insight. One useful class of algorithms address
| parameter. | Around | specic | peaks | in the | heat | capacity, | some |                      |     |              |     |                    |     |
| ---------- | ------ | ------- | ----- | ------ | ---- | --------- | ---- | -------------------- | --- | ------------ | --- | ------------------ | --- |
|            |        |         |       |        |      |           |      | community detection, | and | when applied | to  | kinetic transition |     |
minima contribute positively (increased occupation proba- networks generate a set of solutions that are dynamically
| bility),      | while | others contribute |               | negatively | (lowered | occupation |           |                        |        |                |     |              |     |
| ------------- | ----- | ----------------- | ------------- | ---------- | -------- | ---------- | --------- | ---------------------- | ------ | -------------- | --- | ------------ | --- |
|               |       |                   |               |            |          |            |           | distinct.85,86 Members | of the | same community |     | interconvert | on  |
| probability). | This  | effect            | is visualised | in         | Fig. 3,  | where      | the posi- |                        |        |                |     |              |     |
atimescalemuchshorterthanthoseindifferentcommunities.
tivelyandnegativelycontributingminimafortwopeaksinthe Understanding the partitioning of solutions based not on
heatcapacitycurvearevisualised.Notethatsubstantiallymore
Euclideandistance,butthetopography,givesamoreaccurate
minimacontributearoundthelargerpeakintheC V curve. picture of the time evolution of a physical system, and the
Inmolecularsystems,peaksintheheatcapacitycorrespond distinctnessofdifferentsolutions.Theabilitytomovebeyond
| to solid–solid |     | or solid–liquid |     | phase | transitions, | where | the |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | ----- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Euclideandistanceinevaluatingthedistinctnessofmodelsmay
different
system moves between qualitatively sets of local bepromisingfordevelopingensemblemodelsthatcaptureall
minima,associatedwithdifferentenergyandentropy.ForML
therelevantinformation.
| systems, | the | analogue | of the | heat capacity | reveals |     | how the |     |     |     |     |     |     |
| -------- | --- | -------- | ------ | ------------- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
Furthermore,thedegreeofeachminimum,i.e.thenumber
| occupation | of  | minima | changes | with the | temperature |     | param- |                       |          |        |     |                     |     |
| ---------- | --- | ------ | ------- | -------- | ----------- | --- | ------ | --------------------- | -------- | ------ | --- | ------------------- | --- |
|            |     |        |         |          |             |     |        | of direct connections | to other | minima | via | a single transition |     |
eter.ThetemperatureinanMLproblemisctitious(Fig.3),but
state,isausefulproperty.Nodeswithahighdegreeconstitute
serves as a parameter to scan the properties of the landscape hubs,associatedwithsmallworldproperties.Theseminimaare
| and report | on  | changes | that | highlight | qualitatively |     | different |     |     |     |     |     |     |
| ---------- | --- | ------- | ---- | --------- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
usuallyeasytolocateduringoptimisation,andtheyarekeyto
| solutions | (local | minima). | Minima | separated | by  | a high | energy |                |                   |     |        |                     |     |
| --------- | ------ | -------- | ------ | --------- | --- | ------ | ------ | -------------- | ----------------- | --- | ------ | ------------------- | --- |
|           |        |          |        |           |     |        |        | moving between | different regions |     | of the | space. For physical |     |
different,79
| barrier | may be | very |     | although | degenerate |     | solutions |                  |                  |           |     |             |       |
| ------- | ------ | ---- | --- | -------- | ---------- | --- | --------- | ---------------- | ---------------- | --------- | --- | ----------- | ----- |
|         |        |      |     |          |            |     |           | systems it tends | to be low-valued | solutions |     | that act as | hubs, |
canalsoexistduetosymmetriesofthelossfunction.80Infact,it
|     |     |     |     |     |     |     |     | which can explain | whether | they are | easy | to locate.87,88 | The |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | -------- | ---- | --------------- | --- |
different
has been shown in one example that minima may degree of a node can also highlight its importance to
©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2024,3,637–648 | 641

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |     |     |     | TutorialReview |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO
Fig.3 Heatcapacitycurveforamachinelearninglosslandscape.Thelosslandscapeisvisualisedusingdisconnectivitygraphs.Bothgraphs
showthesamelandscape,highlightedarethepositiveandnegativecontributionstotheheatcapacitycurveforthesmaller(left)andlarger(right)
peakinblueandredrespectively.
optimisation algorithms in physical systems and abstract cost calculated with the contributions of all known solutions,
functions. Furthermore, the distribution of node degrees, account for both intervening barriers in the loss function and
which is a global property of the system, can be used to the number of intermediate minima. Both properties have
understandtheorganisationofthelandscape.89 physical meaning for understanding the solution space, and
|     |     |     |     |     |     |     |     | contain  | important     | additional |       | information | not  | present | in    |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ---------- | ----- | ----------- | ---- | ------- | ----- |
|     |     |     |     |     |     |     |     | distance | calculations. | Small      | rates | indicate    | that | two     | given |
4.2 Locallandscapemetrics
|       |        |       |        |           |          |     |           | minima | are highly | distinct, | where | interconversion |     | requires |     |
| ----- | ------ | ----- | ------ | --------- | -------- | --- | --------- | ------ | ---------- | --------- | ----- | --------------- | --- | -------- | --- |
| 4.2.1 | Rates. | Rates | are an | essential | quantity | in  | computing |        |            |           |       |                 |     |          |     |
eithermany,orlarge,changesinmodelparameters.
| the time-evolution |     | of  | physical | systems. |     | The rate | constant |       |           |          |     |         |           |          |     |
| ------------------ | --- | --- | -------- | -------- | --- | -------- | -------- | ----- | --------- | -------- | --- | ------- | --------- | -------- | --- |
|                    |     |     |          |          |     |          |          | 4.2.2 | Monotonic | sequence |     | basins. | Monotonic | sequence |     |
betweentwominimathataredirectlyconnectedbyatransition
basins(MSBs)areminimanotdirectlyconnectedtoanylower-
| state is | computed | using | unimolecular |     | rate | theory.90,91 | From |                |     |          |     |           |     |               |     |
| -------- | -------- | ----- | ------------ | --- | ---- | ------------ | ---- | -------------- | --- | -------- | --- | --------- | --- | ------------- | --- |
|          |          |       |              |     |      |              |      | valued minima. |     | Reducing | a   | landscape | to  | its monotonic |     |
theseelementarystepsonecanbuildaglobalviewofdynamics
sequencebasinsallowsasignicantreductionincomplexity.In
| by combining |     | them. Rates | between |     | sets of | minima | are calcu- |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | ------- | --- | ------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
complexsystems,hundredsofminimamaybewellrepresented
| lated for | a complete | network |     | using | the graph | transformation |     |         |           |            |      |                |     |          |     |
| --------- | ---------- | ------- | --- | ----- | --------- | -------------- | --- | ------- | --------- | ---------- | ---- | -------------- | --- | -------- | --- |
|           |            |         |     |       |           |                |     | by only | a handful | of states. | This | representation |     | contains | all |
algorithm.92,93Rateshavebeenusedtoanalysetimeevolutionof
|                    |     |     |                   |     |     |          |          | optimal | solutions | within | their surrounding |     | regions | of  | space. |
| ------------------ | --- | --- | ----------------- | --- | --- | -------- | -------- | ------- | --------- | ------ | ----------------- | --- | ------- | --- | ------ |
| many solid-state94 |     | and | biomolecular95,96 |     |     | systems, | and rate |         |           |        |                   |     |         |     |        |
Furthermore,thenumberofMSBscanbeseenasaproxyforthe
| calculations | have | been | extended | to  | K-means | clustering.32 |     | A   |     |     |     |     |     |     |     |
| ------------ | ---- | ---- | -------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
numberoffunnels,whicharedistinctregionsofthelandscape
recentreviewofnumericalratecalculationsisgiveninref.97 different congurations
|       |          |       |      |             |     |           |          | associated | with |     | molecular |     |     | or weights/ |     |
| ----- | -------- | ----- | ---- | ----------- | --- | --------- | -------- | ---------- | ---- | --- | --------- | --- | --- | ----------- | --- |
| In ML | systems, | rates | have | no physical |     | analogue, | but they |            |      |     |           |     |     |             |     |
hyperparameters.
| nevertheless | provide | a   | useful | estimate | of  | the difficulty |     | in  |     |     |     |     |     |     |     |
| ------------ | ------- | --- | ------ | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
movingbetweendifferentregionsofsolutionspace.Therates,
642 | DigitalDiscovery,2024,3,637–648 ©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
| TutorialReview |     |     |     |     |     |     |     |     |     |     |     | DigitalDiscovery |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
4.2.3 Catchmentbasinvolume.Thebasinofattraction,1,98 In practice, ML models are largely scored for accuracy and
foranygivenminimum,isthesetofpointsforwhichsteepest- robustness,i.e.testaccuracy.Apractitionermaybeinterestedin
decentpathsconvergetothatstructure.Thisregionhasawell- howthelossvaluechangesontrainingdata,andperhapsalso
dened volume in conguration space. A Taylor expansion to in training loss. Yet, results are usually reported on test data-
|              |     |              |            |         |     |             | sets. A helpful |     | review of | machine | learning | evaluation |     | can be |
| ------------ | --- | ------------ | ---------- | ------- | --- | ----------- | --------------- | --- | --------- | ------- | -------- | ---------- | --- | ------ |
| second order | in  | the vicinity | of a local | minimum |     | enables the |                 |     |           |         |          |            |     |        |
corresponding partition function to be computed in terms of found in ref. 99. In general, the relevant metrics in machine
thelogproductofpositiveHessianeigenvalues(LPPHE)forthe learningmodelsarelargelyresults-focusedandonlytoalesser
Hessian matrix of second derivatives. The corresponding degreeincorporateanunderstandingofthesystem.Aslongas
conguration volume (or density of states) is related to the the test accuracy in terms of MSE, AUC, or top-k loss is suffi-
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
cient,thepractitionerrarelycaresaboutinterpretationinterms
harmonicvibrationalentropyinanatomicsystem,andthelog
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO
productofpositiveeigenvaluesisaconvenientmeasureofthe of the Hessian eigenvalues of the underlying loss landscape.
‘width’associated with a local minimum for a loss landscape. Such physical quantities have a clearmeaning in energy land-
Theoccupationprobabilityforagivenminimumasafunction scapes, and they are routinely analysed. We hope that by
ofthetemperatureparameterdependsonthebalancebetween translating some of these metrics into practical machine
theenergy(lossfunction),whichappearsasaBoltzmannfactor, learning understanding, more attention will be paid to these
andtheentropy, whichisdeterminedbythe (generallyanhar- metricsinthefuture.
| monic) density | of  | states | in the catchment |     | basin. | The rate | at  |     |     |     |     |     |     |     |
| -------------- | --- | ------ | ---------------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
dene
which this equilibrium value is achieved, if we the 5 Applications of EL4ML
analogueofchemicalkinetics,dependsonthebarriersbetween
minimaandtheglobalorganisationofthelandscape.
|     |     |     |     |     |     |     | Here we | will discuss | applications |     | where | knowledge |     | of the LL |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ------------ | --- | ----- | --------- | --- | --------- |
AccuratevaluesfortheanaloguepropertiesofLLminimaare
|     |     |     |     |     |     |     | has been | used | to understand | or  | improve | machine |     | learning. |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------------- | --- | ------- | ------- | --- | --------- |
notrequiredtodiagnosetheexistenceofqualitativelydifferent
|     |     |     |     |     |     |     | Fig. 4 provides |     | an overview | of  | the four | application |     | areas we |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- | -------- | ----------- | --- | -------- |
solutions,andhencetheharmonicvaluereportedbytheLPPHE
considerasmostpromisingforlosslandscapemethods.
issufficientfordiagnosticpurposes.Thecongurationvolume
forabasinofattractionmayalsohaveusefulinterpretationsin
| MLproblems.Oneofthemostimportantfeaturesofamachine |     |     |     |     |     |     | 5.1 Robustness |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
learningmodelisthatisshouldberobust.TheLPPHEprovides
|     |     |     |     |     |     |     | Incorporating |     | knowledge | of the | loss | landscape | has | become |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ------ | ---- | --------- | --- | ------ |
volume31
a harmonic measure of the basin which allows increasinglycommoninmachinelearning.Mostprominently,
minimatobeselectedbasedonsomeintuitionofhowrobust several new optimisation methods have been developed that
theymightbe,aswellastrainingaccuracy.Weemphasiseonce
|     |     |     |     |     |     |     | include | some degree | of  | information | about | the | gradient | of the |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ----------- | ----- | --- | -------- | ------ |
effective
again, that the value of the heat capacity is not LL.100–103 Including information about the LL in optimisation
importanthere,butpeaksinthisfunctionenableustoidentify
seemstoleadtoimprovedrobustnessofthesolution.Robust-
|     |     |     | classication |     |     | effi- |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
local minima with distinct properties in an ness in machine learning refers to the ability of a particular
cientmanner. modeltogeneralisewelltounseentestingdata.Amorerobust
modelwillperformbetterontestingdatathanamodelthatis
4.3 Furtherpossibilities overtonthetrainingdataanddoesnotgeneralisewell.Flatter
The machine learning community has only recently begun to minima, geometrically characterised by Hessian eigenvalues
(curvatures)withsmallermagnitudes,areexpectedtobemore
exploretheanaloguesofphysicallyobservablethermodynamic
|     |     |     |     |     |     |     | robust.104–106 | This | result | seems intuitive, |     | since | it means | that if |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ------ | ---------------- | --- | ----- | -------- | ------- |
andkineticpropertiesformachinelearninglosslandscapes.In
slightlydifferenttrainingdatadisplacetheminimumfromits
| particular, | little    | work has | been done  | to  | determine         | whether |                 |     |               |          |        |          |          |     |
| ----------- | --------- | -------- | ---------- | --- | ----------------- | ------- | --------------- | --- | ------------- | -------- | ------ | -------- | -------- | --- |
|             |           |          |            |     |                   |         | given position, |     | it will still | be close | to the | original | position | for |
| dynamical   | analogues | might    | be useful. | As  | for thermodynamic |         |                 |     |               |          |        |          |          |     |
a‘atter’landscape,whereastheresultingdisplacementmaybe
| quantities, | such | as the | heat capacity, | there | could | be useful |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------ | -------------- | ----- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
largerwhenthelocalcurvaturesaregreater.
| insight to | be gained | from | understanding |     | how such | quantities |     |     |     |     |     |     |     |     |
| ---------- | --------- | ---- | ------------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Mathematically,givenaminimumatpositionPwithenergy/
reportonthenatureofthemachinelearningsolutionspace.
lossE,asmalldisplacementofP+p,causedbyslightlydifferent
|     |     |     |     |     |     |     | training | data, | will have | an effect | on  | E depending |     | on the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | --------- | --- | ----------- | --- | ------ |
4.4 MLmodelmetrics
1
|     |     |     |     |     |     |     | curvatures | around | P, i.e. | DE ¼ | pTHðPÞp, | where | H(P) | is the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------- | ---- | -------- | ----- | ---- | ------ |
Above,wehavediscussedvariousmetricsthatarerelevantwhen
2
specically
considering the energy landscape of an atomistic system, and Hessian at P. Hence, if the Hessian, and more its
how these may be applied to ML systems. We now want to eigenvalues, are larger, the minimum is ‘narrower’ and the
brieydiscussmetricsthatareconsideredinmachinelearning, differenceinE,DE betweenpositionsPandP+pisgreater,the
implicitlycharacterisingMLLLs.Asdescribedabove,theLLis minimumislessrobust.Foretetal.101haveincludedknowledge
atbestasurrogateofquality:sinceitisonlybasedontraining abouttheshapeofthelossfunctionandmanagedtondmore
data, the ability to generalise to testing data is not easily robust minima. Overall, robustness is one of the most impor-
obtainable.Thesameimperfectcorrelationbetweenlossfunc- tant concepts in machine learning.107 A completely overt
tion and quality is seen in unsupervised clustering methods, model, one that has perfect training accuracy, but does not
suchasK-means,evenwithoutthepresenceoftestdata. generalise at all to testing data, is useless in practice. Thus,
©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2024,3,637–648 | 643

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |     |     |     | TutorialReview |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO
Fig.4 Four applications areas of energy landscapes methodsin machine learningwith specific examples.(a) Robustness: insights into the
relative curvature around minima can be generated from a landscapes perspective, providing a quantification of model robustness. (b)
Ensembles:qualitativelydifferentminimacanbeidentifiedfromthelosslandscapeandselectedforensemblemodels.(c)Interpretability:identify
weightsconservedacrossminimaandvisualisemodeltrainingdescentpath.(d)Parameterselection:landscapegeometryandnumberoffunnels
canbeusedasamethodforparameterselectioninalgorithmssuchasK-means.
consideringgeometricfeaturesofthelosslandscapemaybean votes, to complex weighting schemes for the contribution of
importantwayincombatingthisproblem. individual classiers. The same methods can be applied to
|     |     |     |     |     |     |     |     | unsupervised |     | learning, | where | clustering | solutions | can be |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ----- | ---------- | --------- | ------ |
5.2 Ensemblemethods combined to improve separation, without the separation into
|     |     |     |     |     |     |     |     | training | and | testing data.118 | The | value | of ensemble | learning |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------------- | --- | ----- | ----------- | -------- |
Knowledgeofthelosslandscapemayhelpimproveprediction ariseswhendifferentclassiersaregoodatclassifyingdifferent
| accuracyfora | givenmodel. |     | Ensemble |     | methods,combiningor |     |     |         |        |                     |     |           |       |               |
| ------------ | ----------- | --- | -------- | --- | ------------------- | --- | --- | ------- | ------ | ------------------- | --- | --------- | ----- | ------------- |
|              |             |     |          |     |                     |     |     | subsets | of the | data, or prioritise |     | different | parts | of the input. |
averagingmultiplepredictorsforasingletask,isawellestab-
|     |     |     |     |     |     |     |     | Recently, | the | idea of combining |     | multiple | minima | of the LL, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------------- | --- | -------- | ------ | ---------- |
lishedapproach.108–111Onereasonwhyensemblemethodshave
|             |                |     |               |      |           |        |           | obtained  | via  | energy landscapes |     | methodology,80 |     | has been      |
| ----------- | -------------- | --- | ------------- | ---- | --------- | ------ | --------- | --------- | ---- | ----------------- | --- | -------------- | --- | ------------- |
| become      | so important   |     | over previous |      | years     | is the | imperfect |           |      |                   |     |                |     |               |
|             |                |     |               |      |           |        |           | examined. | Each | minimum           | can | be viewed      | as  | an individual |
| correlation | of performance |     | and           | loss | resulting | from   | limited   |           |      |                   |     |                |     |               |
classier,whereallmodelshavethesamearchitecture,butvery
trainingdata.Thesinglebestminimumisoennotsufficient
|     |     |     |     |     |     |     |     | different |             |           |     | classiers, |             |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --------- | --- | ----------- | ----------- | ---- |
|     |     |     |     |     |     |     |     |           | parameters. | Combining |     |             | allobtained | from |
andhence,acombinationofsocalledweaklearnersisrequired
oneLL,providesthedistinctadvantagethattheclassiersare
tooutperforma‘better’minimum.Relatedchallengesarisein
knowntobequalitatively‘different’,whichisthekeyfeaturein
| batch selection |             | for Bayesian | optimisation, |        | where   | the     | key chal- |          |           |              |     |            |      |              |
| --------------- | ----------- | ------------ | ------------- | ------ | ------- | ------- | --------- | -------- | --------- | ------------ | --- | ---------- | ---- | ------------ |
|                 |             |              |               |        |         |         |           | ensemble | learning. | Specically, |     | for        | some | LL, standard |
| lenge is        | determining | a            | diverse       | set of | samples | for the | task      | of       |           |              |     |            |      |              |
|                 |             |              |               |        |         |         |           | measures | based     | on analogue  |     | properties | from | the physical |
maximisinganexpensive‘black-box’function.112–116Twoofthe
sciences,suchastheheatcapacity,canbeanalysedtoincrease
| critical | design choices | in  | ensemble | learning |     | are, which | classi- |     |     |     |     |     |     |     |
| -------- | -------------- | --- | -------- | -------- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
thelikelihoodthattheminimaarecomplementary.Landscape
ers
| to  | combine, | and | how | to combine |     | them. | Common |        |          |          |            |         |     |              |
| --- | -------- | --- | --- | ---------- | --- | ----- | ------ | ------ | -------- | -------- | ---------- | ------- | --- | ------------ |
|     |          |     |     |            |     |       |        | guided | ensemble | learning | is another | example | of  | how physics- |
approachesincludebaggingandboostingmethods,whichare
inspiredmachinelearningcanoutperformcommonmethods,
welldescribedinref.117.Thepossibleapproachestocombine
andhenceprovidesignicantadditionalperformance.
different
| predictions | of  |     | minima | range | from | simple | majority |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------ | ----- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
644 | DigitalDiscovery,2024,3,637–648 ©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
|     | TutorialReview |     |     |     |     |     |     |     |     |     |     |     |     | DigitalDiscovery |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
5.3 Interpretability candidate for improving our understanding of machine
|     |               |     |           |     |            |          |         |     | learning, | by transferring |     | knowledge | from | a   | relatively | mature |
| --- | ------------- | --- | --------- | --- | ---------- | -------- | ------- | --- | --------- | --------------- | --- | --------- | ---- | --- | ---------- | ------ |
|     | Understanding |     | the black | box | of machine | learning | systems |     | is        |                 |     |           |      |     |            |        |
eld,toanewerone.
eld
|     | one of   | the greatest | challenges   |       | to the  |           | today. | Various   |            |         |          |             |                  |     |          |          |
| --- | -------- | ------------ | ------------ | ----- | ------- | --------- | ------ | --------- | ---------- | ------- | -------- | ----------- | ---------------- | --- | -------- | -------- |
|     |          |              |              |       |         |           |        |           | Another    | area    | in which | the         | energy landscape |     | approach | may      |
|     | gradient | and          | perturbation | based | methods | exist,119 |        | yet their |            |         |          |             |                  |     |          |          |
|     |          |              |              |       |         |           |        |           | prove very | helpful |          | is Bayesian | inference        |     | using    | Gaussian |
usefulnessandaccuracyisdebated,andisnotgenerallyagreed
sufficient.120 processes(GPs).Aninherentchallengewithinthesemethodsis
|     | to be         |     | Hence,             | alternative |     | ways         | to improve | our |             |          |                  |     |     |      |           |        |
| --- | ------------- | --- | ------------------ | ----------- | --- | ------------ | ---------- | --- | ----------- | -------- | ---------------- | --- | --- | ---- | --------- | ------ |
|     |               |     |                    |             |     |              |            |     | identifying | suitable | hyperparameters. |     |     | Most | commonly, | a loss |
|     | understanding |     | of decision-making |             | by  | a particular | model      | are |             |          |                  |     |     |      |           |        |
function,usuallythelogmarginallikelihood,ismaximisedand
desirable.Studyingindividualfunnelsofthelandscape,asseen
|                                                                                      |                    |     |         |     |         |             |     |     | a single | point | estimate | is  | taken for | the | hyperparameters. |     |
| ------------------------------------------------------------------------------------ | ------------------ | --- | ------- | --- | ------- | ----------- | --- | --- | -------- | ----- | -------- | --- | --------- | --- | ---------------- | --- |
| .ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  | in disconnectivity |     | graphs, | may | provide | a promising |     | way | to       |       |          |     |           |     |                  |     |
However,single-pointestimatesmaybeinsufficientwhenthere
increaseinterpretability.Thisapproachiscommonlyexploited
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO aremultiplecompetingts.130Acommonmethodtoovercome
|     | in the molecular |     | sciences121,122 |     | where | a multifunnelled |     | land- |                 |     |           |       |           |     |       |            |
| --- | ---------------- | --- | --------------- | --- | ----- | ---------------- | --- | ----- | --------------- | --- | --------- | ----- | --------- | --- | ----- | ---------- |
|     |                  |     |                 |     |       |                  |     |       | the limitations |     | of single | point | estimates | is  | Monte | Carlo (MC) |
scapeisanalysedtounderstandwhichstructuraldifferencesof
distribution.131–133
amoleculeconstituteagroupofsolutionsinaspecicfunnel. sampling of the hyperparameter Previous
|     |             |              |             |          |         |            |                 |            | work has           | used | sequential  |      | MC sampling,130,134 |      | Bayesian      | MC       |
| --- | ----------- | ------------ | ----------- | -------- | ------- | ---------- | --------------- | ---------- | ------------------ | ---- | ----------- | ---- | ------------------- | ---- | ------------- | -------- |
|     | The machine | learning     |             | analogue | is that | for a      | multi-funnelled |            |                    |      |             |      |                     |      |               |          |
|     |             |              |             |          |         |            |                 |            | sampling,135       | and  | Hamiltonian |      | MC sampling.136     |      | Additionally, |          |
|     | landscape,  | one          | can compute | the      | sets of | parameters |                 | that char- |                    |      |             |      |                     |      |               |          |
|     |             |              |             |          |         |            |                 |            | slice sampling,137 |      | adaptive    |      | importance          |      | sampling,138  | and      |
|     | acterise    | a particular | funnel,     | as       | in ref. | 123. These | parameters,     |            |                    |      |             |      |                     |      |               |          |
|     |             |              |             |          |         |            |                 |            | entropy-based      |      | methods139  | have | been                | used | within        | Bayesian |
|     | conserved   | across       | multiple    | minima,  | are     | therefore  | likely          | to be      |                    |      |             |      |                     |      |               |          |
importantinthemodel,andmayguideinterpretability. optimisation,wherethereisinterestinmovingbeyondsingle-
|     |                                |     |     |     |     |     |     |     | point estimates |      | to fully-Bayesian |         | approaches.140,141 |               |     | The main |
| --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------------- | ---- | ----------------- | ------- | ------------------ | ------------- | --- | -------- |
|     |                                |     |     |     |     |     |     |     | drawback        | with | these             | methods | is the high        | computational |     | cost,    |
|     | 5.4 Selectingoverallparameters |     |     |     |     |     |     |     |                 |      |                   |         |                    |               |     |          |
andideallytheyshouldonlybeemployedwhenitwillprovide
ML algorithms can involve choosing a parameter that is not a substantial advantage over single point estimates. However,
itselfpartoftheoptimisationproblem.Aprominentexampleis this condition cannot be known a priori. Looking at the loss
denes
the choice of cluster number, K, in K-means. Each K landscape may provide an answer. There may bea direct rela-
a distinct cost function surface that must be optimised to tionship between the number of funnels in the landscape,
|     | generate | low-valued | clustering |     | solutions. | The | choice | of the |         |               |     |              |     |          |         |        |
| --- | -------- | ---------- | ---------- | --- | ---------- | --- | ------ | ------ | ------- | ------------- | --- | ------------ | --- | -------- | ------- | ------ |
|     |          |            |            |     |            |     |        |        | perhaps | characterised |     | by monotonic |     | sequence | basins, | or the |
appropriate cluster number is usually made using one, or frustration index, and the effect that MC sampling has on
a small set, of solutions at each K,124–127 reviewed in ref. 128. improving accuracy and generalisability over single point esti-
However, it is possible to make this decision using the topog- mates. Thus,knowledge ofthe landscape, obtained via appro-
raphyofthewholesolutionspace,ratherthanasmallnumber priate sampling, could lead to a substantial reduction in
|     | of solutions. | The | use of | landscapes, | composed |     | of many | solu- |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | ------ | ----------- | -------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
computecostbyidentifyingwhenafully-Bayesianapproachis
tions,increasesthereproducibility,asthereislessdependence required. Moreover, the additional information present in
on locating certain minima, amongst a vast number, when landscapes may extend existing variational inference
computingmetrics.Thepresenceofcertainlandscapestructure methods142,143 by allowing more accurate approximate distri-
isindicativeofanappropriatenumberofclusters,asobserved butionstobegeneratedandsampled.
|     | for clustering |     | gene | expression | data | to  | identify | cancer |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ---- | ---------- | ---- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
signicantly
subtypes.129 Such an analysis is more expensive 7 Conclusions
thancharacterisingsingleminima,butformanyapplications,
thequalityandreproducibilityofthesolutionareessential.
|     |          |     |      |     |     |     |     |     | Important         | relationships |                  | exist    | between | physical    |          | molecular  |
| --- | -------- | --- | ---- | --- | --- | --- | --- | --- | ----------------- | ------------- | ---------------- | -------- | ------- | ----------- | -------- | ---------- |
|     |          |     |      |     |     |     |     |     | energy landscapes |               | and              | abstract | machine | learning    |          | loss land- |
|     | 6 Future |     | work |     |     |     |     |     |                   |               |                  |          |         |             |          |            |
|     |          |     |      |     |     |     |     |     | scapes.           | In this       | contribution     |          | we have | highlighted | some     | of the     |
|     |          |     |      |     |     |     |     |     | recent work       | on            | physics-inspired |          | machine |             | learning | and how    |
Manyapplications ofenergylandscapesremainunexploredin theoreticalmethodsfromoneeldmaybeappliedtotheother.
thecontextofmachinelearning.Inthissection,wewilloutline We have discussed how various metrics, such as the heat
a few interesting areas of future work that would build capacity,catchmentbasinvolume,orfrustrationindexcanhelp
substantiallyontheenergylandscapesmethodology.Firstly,it to improve and explain robustness, accuracy, and importantly
will be interesting to see advances in understanding the interpretability in machine learning. Many of the connections
physics-inspired analogues of machine learning. For example, betweenthesetwoeldsremaintobeexploredandexploited.
understandinginmoredetailtherelationshipbetweenminima Energy landscapes provide important insight to answer
contributing to the heat capacity and the importance (both in questions in machine learning, irrespective of the underlying
terms of accuracy and robustness) of these minima in an model, because they focus on the structure of the solution
inferencetask.Furthermore,manyotherconcepts,suchasthe space. More generally, exploiting a well understood method-
dynamical analogues in machine learning systems, remain ology is a promising approach to vastly increase the set of
largely unexplored. Understanding the usefulness of such problemsthatmachinelearningcanbeappliedto.Thehopeis
metricsmaygivefurtherinsightsfromthephysicalsciencesto thatmethodsfromthephysicalsciencescanworkinconjunc-
the more abstract, black-box world of machine learning. In tionwithmachinelearningmethodstogivepractitionersmore
condence
general,physics-inspiredmachinelearningseemstobeagood trust and in their predictions, as well as greater
©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2024,3,637–648 | 645

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     | TutorialReview |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
understanding of what a given model is actually doing. Ulti- et al., Advances in neural information processing systems,
mately, this approach could facilitate further growth in the 2020,vol.33,pp.1877–1901.
inuencethatmachinelearninghasonsocietyasawhole.
|                   |     |     |     |     |     |     | 12 A. Ramesh,     | P. Dhariwal,    | A. Nichol,        | C. Chu and | M. Chen,  |
| ----------------- | --- | --- | --- | --- | --- | --- | ----------------- | --------------- | ----------------- | ---------- | --------- |
|                   |     |     |     |     |     |     | arXiv,            | 2022, preprint, | arXiv:2204.06125. | DOI:       | 10.48550/ |
| Data availability |     |     |     |     |     |     | arXiv.2204.06125. |                 |                   |            |           |
13 R.Gal,Y.Alaluf,Y.Atzmon,O.Patashnik,A.H.Bermano,
Inthisreviewarticle,nonoveldatawasanalysedorstudied. G. Chechik and D. Cohen-Or, arXiv, 2022, preprint,
arXiv:2208.01618,DOI:10.48550/arXiv.2208.01618.
Conflicts
of interest 14 F. No´e, A. Tkatchenko, K. Müller and C. Clementi, Annu.
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
Rev.Phys.Chem.,2020,71,361–390.
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO Therearenoconictstodeclare.
|     |     |     |     |     |     |     | 15 Y. Cooper, | arXiv, 2018, | preprint, | arXiv:1804.10200, | DOI: |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --------- | ----------------- | ---- |
10.48550/arXiv.1804.10200.
Tinˇo,
Acknowledgements 16 Y. Zhang, P. A. Leonardis and K. Tang, IEEE
|     |     |     |     |     |     |     | Transactions | on Emerging | Topics | in Computational |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------ | ---------------- | --- |
DJW gratefully acknowledges an International Chair at the Intelligence,2021.
InterdisciplinaryInstituteforArticialIntelligenceat3iACote
17 Q.ZhangandS.Zhu,Front.Inf.Technol.Electron.Eng.,2018,
| d'Azur, supported |     | by the | French government, |     | with | reference | 19,27–39. |     |     |     |     |
| ----------------- | --- | ------ | ------------------ | --- | ---- | --------- | --------- | --- | --- | --- | --- |
number ANR-19-P3IA-0002, which has provided interactions 18 L.H.Gilpin, D.Bau,B.Z. Yuan,A.Bajwa,M.Specter and
thatfurtheredthepresentresearchproject.MPNacknowledges L. Kagal, 2018 IEEE 5th International Conference on data
funding from Downing College, Cambridge. LD and EOP-K scienceandadvancedanalytics,DSAA,2018,pp.80–89.
Z.C.Lipton,Queue,2018,16,31–57.
| would like | to acknowledge |     | this work | was | supported | by the | 19  |     |     |     |     |
| ---------- | -------------- | --- | --------- | --- | --------- | ------ | --- | --- | --- | --- | --- |
HartreeNationalCentreforDigitalInnovation–acollaboration 20 A. J. Ballard, R. Das, S. Martiniani, D. Mehta, L. Sagun,
betweenScienceandTechnologyFacilitiesCouncilandIBM.LD J. D. Stevenson and D. J. Wales, Phys. Chem. Chem. Phys.,
|                   |     |     | nancial |         |        |           | 2017,19,12585–12603. |     |     |     |     |
| ----------------- | --- | --- | -------- | ------- | ------ | --------- | -------------------- | --- | --- | --- | --- |
| also acknowledges |     | the |          | support | of the | EPSRC via |                      |     |     |     |     |
aknowledgetransferfellowship. 21 M. P. Niroomand, C. T. Cafolla, J. W. R. Morgan and
D.J.Wales,Mach.Learn.:Sci.Technol.,2022,3,015019.
Notes and references 22 S.R.Chitturi,P.C.Verpoort,D.J.Wales,etal.,Mach.Learn.:
Sci.Technol.,2020,1,023002.
1 D.J.Wales,EnergyLandscapes,CambridgeUniversityPress, 23 M. V. Narkhede, P. P. Bartakke and M. S. Sutaone, Artif.
| Cambridge,2003. |     |     |     |     |     |     | Intell.Rev.,2022,55,291–322. |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
2 J. A. Joseph, K. Röder, D. Chakraborty, R. G. Mantell and 24 F.Draxler, K.Veschgini, M.Salmhofer andF. Hamprecht,
D.J.Wales,Chem.Commun.,2017,53,6974–6988. International conference on machine learning, 2018, pp.
| 3 J.N.MurrellandK.J.Laidler,Trans.FaradaySoc.,1968,64, |     |     |     |     |     |     | 1309–1318. |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
371–377.
25 B.Neyshabur,S.Bhojanapalli,D.McAllesterandN.Srebro,
4 D.Silver,T.Hubert,J.Schrittwieser,I.Antonoglou,M.Lai, Advancesinneuralinformationprocessingsystems,2017,vol.
| A.Guez,M.Lanctot,L.Sifre,D.Kumaran,T.Graepeletal., |     |     |     |     |     |     | 30. |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arXiv, 2017, preprint arXiv:1712.01815, DOI: 10.48550/ 26 I. J. Goodfellow, O. Vinyals and A. M. Saxe, arXiv, 2014,
arXiv.1712.01815. preprint,arXiv:1412.6544,DOI:10.48550/arXiv.1412.6544.
5 D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou, 27 J. Lucas, J. Bae, M. R. Zhang, S. Fort, R. Zemel and
A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai, A. Bolton, R. Grosse, arXiv, 2021, preprint, arXiv:2104.11044, DOI:
etal.,Nature,2017,550,354–359.
10.48550/arXiv.2104.11044.
6 C. Berner, G. Brockman, B. Chan, V. Cheung, P. Debiak, 28 J. Frankle, arXiv, 2020, preprint, arXiv:2012.06898, DOI:
C. Dennison, D. Farhi, Q. Fischer, A. Hashme, C. Hesse 10.48550/arXiv.2012.06898.
et al., arXiv, 2019, preprint arXiv:1912.06680, DOI: 29 T. J. Vlaar and J. Frankle, International Conference on
10.48550/arXiv.1912.06680. MachineLearning,2022,pp.22325–22341.
7 S. Grigorescu, B. Trasnea, T. Cocias and G. Macesanu, J. 30 S. Du, J. Lee, H. Li, L. Wang and X. Zhai, International
FieldRobot.,2020,37,362–386. conferenceonmachinelearning,2019,pp.1675–1685.
8 J. Jumper, R. Evans, A. Pritzel, T. Green, M. Figurnov, 31 P.C.Verpoort,A.A.LeeandD.J.Wales,Proc.Natl.Acad.Sci.
|                 |     |     |                  |     |           | ˇ ´ıdek, | U.S.A.,2020,117,21857–21864. |     |     |     |     |
| --------------- | --- | --- | ---------------- | --- | --------- | -------- | ---------------------------- | --- | --- | --- | --- |
| O. Ronneberger, |     | K.  | Tunyasuvunakool, |     | R. Bates, | A. Z     |                              |     |     |     |     |
A.Potapenko,etal.,Nature,2021,596,583–589. 32 L.DicksandD.J.Wales,J.Chem.Phys.,2022,156,054109.
9 A.Davies,P.Veliˇckovi´c,L.Buesing,S.Blackwell,D.Zheng, 33 M.Chouza,S.RobertsandS.Zohren,arXiv,2018,preprint,
N.Tomaˇsev,R.Tanburn,P.Battaglia,C.Blundell,A.Juh´asz,
arXiv:1803.09119,DOI:10.48550/arXiv.1803.09119.
etal.,Nature,2021,600,70–74. 34 C.E.Rasmussen,Summerschoolonmachinelearning,2003,
pp.63–71.
| 10 P. Budzianowski |     | and | I. Vuli´c, | arXiv, | 2019, | preprint |     |     |     |     |     |
| ------------------ | --- | --- | ---------- | ------ | ----- | -------- | --- | --- | --- | --- | --- |
arXiv:1907.05774,DOI:10.48550/arXiv.1907.05774. 35 A.LaioandM.Parrinello,Proc.Natl.Acad.Sci.U.S.A.,2002,
11 T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, 99,12562–12576.
P.Dhariwal,A.Neelakantan,P.Shyam,G.Sastry,A.Askell
646 | DigitalDiscovery,2024,3,637–648 ©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
| TutorialReview |     |     |     |     |     |     |     |     | DigitalDiscovery |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- |
36 G. M. Torrie and J. P. Valleau, Chem. Phys. Lett., 1974, 28, 67 L. J. Munro and D. J. Wales, Phys. Rev. B: Condens. Matter
| 578. |     |     |     |     |     | Mater.Phys.,1999,59,3969–3980. |     |     |     |
| ---- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- |
37 Y.SugitaandY.Okamoto,Chem.Phys.Lett.,1999,314,141. 68 G. Henkelman and H. J´onsson, J. Chem. Phys., 1999, 111,
| 38 J. H´enin, | T.  | Leli´evre, M. | R. Shirts, | O.  | Valsson and | 7010–7022. |     |     |     |
| ------------- | --- | ------------- | ---------- | --- | ----------- | ---------- | --- | --- | --- |
L.Delemotte,LivingJ.Comput.Mol.Sci.,2022,4,1583. 69 Y.Kumeda,L.J.MunroandD.J.Wales,Chem.Phys.Lett.,
2001,341,185–194.
39 Z.LiandH.A.Scheraga,Proc.Natl.Acad.Sci.U.S.A.,1987,
84,6611–6615. 70 GMIN: A program for basin-hopping global optimisation,
40 D. J. Wales and J. P. K. Doye, J. Phys. Chem. A, 1997, 101, basin-sampling, and parallel tempering, http://www-
| 5111. |     |     |     |     |     | wales.ch.cam.ac.uk/soware.html. |     |     |     |
| ----- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
41 D. J. Wales and H. A. Scheraga, Science, 1999, 285, 1368– 71 OPTIM: A program for geometry optimisation and pathway
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO calculations,http://www-wales.ch.cam.ac.uk/soware.html.
1372.
42 E.S.Henault,M.H.RasmussenandJ.H.Jensen,ChemRxiv, 72 PATHSAMPLE:Aprogramforgeneratingconnectedstationary
2020,DOI:10.26434/chemrxiv.12152661.v1. point databases and extracting global kinetics, http://www-
43 C.J.PickardandR.J.Needs,J.Phys.:Condens.Matter,2011, wales.ch.cam.ac.uk/soware.html.
| 23,053201. |     |     |     |     |     | 73 pyl:APythonpackagetosurveyLFLsinMLmodels. |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- |
18th
44 D. Arthur and S. Vassilvitskii, Proc. of the Ann. ACM- 74 G.C.CawleyandN.L.C.Talbot,J.Mach.Learn.Res.,2007,
| SIAMSymp.onDiscreteAlgorithms,2007,pp.1027–1035. |     |     |     |     |     | 8,841–861. |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
Hoffmann,
45 A. H. Mohammad, C. Vineed, S. Saeed and 75 J. Chen, K. de Hoogh, J. Gulliver, B. O. Hertel,
J.Z.Mohammed,PatternRecognit.Lett.,2009,30,994–1002.
|     |     |     |     |     |     | M. Ketzel, | M. Bauwelinck, |     | A. Van Donkelaar, |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ----------------- |
46 O.Bachem,M.Lucic,S.H.HassaniandA.Krause,Proc.of U.A.Hvidtfeldt,K.Katsouyanni,et al.,Environ.Int.,2019,
| the30thInt.Conf.onNeuralInformationProcessingSystems, |     |     |     |     |     | 130,104934. |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
2016,pp.55–63. 76 V.K.DeSouza,J.D.Stevenson,S.P.Niblett,J.D.Farrelland
47 C.E. Rasmussen and C.K. I. Williams, Gaussian processes D.J.Wales,J.Chem.Phys.,2017,146,124103.
C.E.Shannon,BellSyst.Tech.J.,1948,27,379–423.
| formachinelearning,MITPress,2005. |     |     |     |     |     | 77  |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
48 D.C.LiuandJ.Nocedal,Math.Program.,1989,45,503–528. 78 D.J.Wales,Phys.Rev.E,2017,95,030105.
J.Nocedal,Math.Comput.,1980,35,773–782.
| 49  |     |     |     |     |     | 79 A.V.Bradley,C.A.Gomez-UribeandM.R.Vuyyuru,Mach. |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
50 C.G.Broyden,J.Inst.Math.ItsAppl.,1970,6,76–90. Learn.:Sci.Technol.,2022,3,045002.
51 R.Fletcher,Comput.J.,1970,13,317–322. 80 M. P. Niroomand, J. W. R. Morgan, C. T. Cafolla and
D.Goldfarb,Math.Comput.,1970,24,23–26.
| 52  |     |     |     |     |     | D.J.Wales,Mach.Learn.:Sci.Technol.,2022,3,025004. |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
53 D.F.Shanno,Math.Comput.,1970,24,647–656. 81 D.J.Wales,Int.Rev.Phys.Chem.,2006,25,237–282.
F.No´eandS.Fischer,Curr.Opin.Struct.Biol.,2008,18,154–
| 54 R. H.                   | Byrd, P. | Lu, J. Nocedal | and | C. Zhu, | SIAM J. Sci. | 82   |     |     |     |
| -------------------------- | -------- | -------------- | --- | ------- | ------------ | ---- | --- | --- | --- |
| Comput.,1995,16,1190–1208. |          |                |     |         |              | 162. |     |     |     |
55 C.Zhu,R.H.Byrd,P.LuandJ.Nocedal,ACMTrans.Math. 83 J.M.Carr andD.J.Wales, Phys. Chem.Chem. Phys., 2009,
| Sow.,1997,23,550–560. |     |     |     |     |     | 11,3341–3354. |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
56 K. A. Wang, G. Pleiss, J. R. Gardner, S. Tyree, 84 D. Prada-Gracia, J. G´omez-Gardenes, P. Echenique and
K.Q.WeinbergerandA.G.Wilson,NeurIPS,2019. F.Falo,PLoSComput.Biol.,2009,5,e1000415.
57 J. Wenger, G. Pleiss, P. Hennig, J. Cunningham and 85 C. P. Massen and J. P. K. Doye, Phys. Rev. E, 2005, 71,
| J.Gardner,Proc.Mach.Learn.Res.,2022,162,23751–23780. |     |     |     |     |     | 046101. |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
58 D.P.KingmaandJ.L.Ba,2015,preprint,arxiv:1412.6980, 86 D.Kannan,D.J.Sharpe,T.D.SwinburneandD.J.Wales,J.
| DOI:10.48550/arXiv.1412.6980. |     |     |     |     |     | Chem.Phys.,2020,153,244108. |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- |
59 L.Bottou,F.E.CurtisandJ.Nocedal,SIAMRev.,2018,60,1. 87 J. P. Doye and C. P. Massen, J. Chem. Phys., 2005, 122,
| 60 N. Metropolis, |     | A. W. Rosenbluth, |     | M. N. | Rosenbluth, | 084105. |     |     |     |
| ----------------- | --- | ----------------- | --- | ----- | ----------- | ------- | --- | --- | --- |
A. H. Teller and E. Teller, J. Chem. Phys., 1953, 21, 1087– 88 J. P. K. Doye and C. P. Massen, arXiv, 2007, preprint,
| 1092.                                                |     |     |     |     |     | arxiv:cond-mat/0612150, |     | DOI: | 10.48550/arXiv.cond-mat/ |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | ---- | ------------------------ |
| 61 S.A.TrygubenkoandD.J.Wales,J.Chem.Phys.,2004,120, |     |     |     |     |     | 0612150.                |     |      |                          |
2082–2094. 89 J. W. R. Morgan, D. Mehta and D. J. Wales, Phys. Chem.
Chem.Phys.,2017,19,25498–25508.
62 D.Sheppard,R.TerrellandG.Henkelman,J.Chem.Phys.,
| 2008,128,134106. |     |     |     |     |     | 90 H.Eyring,Chem.Rev.,1935,17,65. |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- |
63 G.Mills,H.J´onssonandG.K.Schenter,Surf.Sci.,1995,324, 91 M.G.EvansandM.Polanyi,Trans.FaradaySoc.,1935,31,
| 305–337. |     |     |     |     |     | 875. |     |     |     |
| -------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
64 H. J´onsson, G. Mills and K. W. Jacobsen, Classical and 92 S. A. Trygubenko and D. J. Wales, Mol. Phys., 2006, 104,
1497–1507.
| quantum | dynamics | in condensed | phase | simulations, | World |     |     |     |     |
| ------- | -------- | ------------ | ----- | ------------ | ----- | --- | --- | --- | --- |
Scientic,Singapore,1998,ch.16,pp.385–404. 93 S.A.TrygubenkoandD.J.Wales,J.Chem.Phys.,2006,124,
| 65 G. Henkelman, |     | B. P. Uberuaga | and | H. J´onsson, | J. Chem. | 234110. |     |     |     |
| ---------------- | --- | -------------- | --- | ------------ | -------- | ------- | --- | --- | --- |
Phys.,2000,113,9901–9904. 94 A. Banerjee and D. J. Wales, Phys. Condens. Matter., 2021,
| 66 G. Henkelman |     | and H. J´onsson, | J. Chem. | Phys., | 2000, 113, | 34,034004. |     |     |     |
| --------------- | --- | ---------------- | -------- | ------ | ---------- | ---------- | --- | --- | --- |
9978–9985.
©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2024,3,637–648 | 647

View Article Online
| DigitalDiscovery |     |     |     |     |     |     | TutorialReview |     |
| ---------------- | --- | --- | --- | --- | --- | --- | -------------- | --- |
95 D. J. Sharpe and D. J. Wales, J. Chem. Phys., 2020, 153, 120 S. Srinivas and F. Fleuret, arXiv, 2020, preprint,
| 024121. |     |     |     | arXiv:2006.09128,DOI:10.48550/arXiv.2006.09128. |     |     |     |     |
| ------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
D.J.Wales,J.Phys.Chem.Lett.,2022,13,6349–6358.
| 96  |     |     |     | 121 K.Röder,G.Stirnemann,A.Dock-Bregeon,D.J.Walesand |     |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
97 D. J. Sharpe and D. J. Wales, J. Chem. Phys., 2021, 155, S.Pasquali,NucleicAcidsRes.,2019,373–389.
140901. 122 K. Röder and D. J. Wales, Front. Mol. Biosci., 2022, 9,
| 98 P. G. | Mezey, Potential | Energy Hypersurfaces, | Elsevier, | 820792. |     |     |     |     |
| -------- | ---------------- | --------------------- | --------- | ------- | --- | --- | --- | --- |
Amsterdam,1987. 123 M.P.NiroomandandD.J.Wales,ICLR2023Workshopon
99 S. Raschka, arXiv, 2018, preprint, arXiv:1811.12808, DOI: PhysicsforMachineLearning,2023.
10.48550/arXiv.1811.12808. 124 J.C.Dunn,J.Cybersecur.,1974,4,95–104.
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
100 P. Chaudhari, A. Choromanska, S. Soatto, Y. LeCun, 125 D. L. Davies and D. W. Bouldin, IEEE Trans. Pattern Anal.
 .MA 65:61:3 6202/1/6 no dedaolnwoD .4202 yraurbeF 80 no dehsilbuP .elcitrA sseccA nepO Mach.Intell.,1979,1,224–227.
| C. Baldassi, | C. Borgs, | J. Chayes, | L. Sagun and |     |     |     |     |     |
| ------------ | --------- | ---------- | ------------ | --- | --- | --- | --- | --- |
R.Zecchina,J.Stat.Mech.:TheoryExp.,2019,2019,124018. 126 P.J.Rousseeuw,Comput.Appl.Math.,1987,20,53–65.
101 P. Foret, A. Kleiner, H. Mobahi and B. Neyshabur, arXiv, 127 R.Tibshirani,G.WaltherandT.Hastie,J.R.Stat.Soc.Ser.B
2020, preprint, arXiv:2010.01412, DOI: 10.48550/ Methodol.,2001,63,411–423.
arXiv.2010.01412. 128 E. Schubert, arXiv, 2023, preprint, arxiv:2212.12189, DOI:
102 M. Andriushchenko and N. Flammarion, International 10.48550/arXiv.2212.12189.
ConferenceonMachineLearning,2022,pp.639–668. 129 Y. Wu, L. Dicks and D. J. Wales, arXiv, 2023, preprint,
103 F. H. Stillinger and T. A. Weber, J. Stat. Phys., 1988, 52, arxiv:2305.17279,DOI:10.48550/arXiv.2305.17279.
1429–1445.
|     |     |     |     | 130 A. Svensson, | J. Dahlin | and T. B. Schön, | 2015 IEEE | 6th |
| --- | --- | --- | --- | ---------------- | --------- | ---------------- | --------- | --- |
104 S.HochreiterandJ.Schmidhuber,NeuralComput.,1997,9, International Workshop on Computational Advances in
| 1–42.            |        |                       |              |              |                      |         |           | 477– |
| ---------------- | ------ | --------------------- | ------------ | ------------ | -------------------- | ------- | --------- | ---- |
|                  |        |                       |              | Multi-Sensor | Adaptive Processing, | CAMSAP, | 2015, pp. |      |
| 105 G. E. Hinton | and D. | Van Camp, Proceedings | of the sixth | 480.         |                      |         |           |      |
annual conference on Computational learning theory, 1993, 131 R. M. Neal, arXiv, 1997, preprint, arxiv:physics/9701026,
pp.5–13.
DOI:10.48550/arXiv.physics/9701026.
106 Y.Zhang,A.M.Saxe,M.S.AdvaniandA.A.Lee,Mol.Phys., 132 C. K. Williams and C. E. Rasmussen, Neural Information
2018,116,3214–3223.
ProcessingSystems,NIPS,1996.
107 Y.Yang,C.Rashtchian,H.Zhang,R.R.Salakhutdinovand 133 A. Garbuno-Inigo, F. A. DiazDelaO and K. Zuev, Comput.
K. Chaudhuri, Advances in neural information processing Stat.DataAnal.,2016,103,367–383.
systems,2020,vol.33,pp.8588–8601.
|     |     |     |     | 134 P.Del Moral, | A. Doucet | and A. Jasra, | J. R. Stat. Soc. | Ser. B |
| --- | --- | --- | --- | ---------------- | --------- | ------------- | ---------------- | ------ |
108 M.S.Pepe,T.CaiandG.Longton,Biometrics,2006,62,221– Methodol.,2006,68,411–436.
| 229. |     |     |     | 135 M.A.Osborne,S.J.Roberts,A.Rogers,S.D.Ramchurnand |     |     |     |     |
| ---- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
109 S.Hashem,NeuralNetworks,1997,10,599–614. N.R.Jennings,2008InternationalConferenceonInformation
110 H.JinandY.Lu,Stat.Probab.Lett.,2009,79,2321–2327. ProcessinginSensorNetworks(ipsn2008),2008,pp.109–120.
L.Breiman,Mach.Learn.,1996,24,123–140.
| 111 |     |     |     | 136 Y.Saatçi,R.D.TurnerandC.E.Rasmussen,ICML-10,2010, |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
112 J.Azimi,A.FernandX.Fern,AdvancesinNeuralInformation pp.927–934.
D.K.AgarwalandA.E.Gelfand,Stat.Comput.,2005,15,61–
| ProcessingSystems,2010,vol.23. |                 |                      |     | 137 |     |     |     |     |
| ------------------------------ | --------------- | -------------------- | --- | --- | --- | --- | --- | --- |
| 113 J.Gonaz´alez,Z.            | Dai,P.Hennigand | N.Lawrence,Articial |     | 69. |     |     |     |     |
Intell.Stat.,2016,pp.648–657. 138 D.Petelin,M.GasperinandV.Sm´ıdl,IFACProc.Vol.,2014,
47,5011–5016.
| 114 M. Groves | and E. O. | Pyzer-Knapp, arXiv, | 2018, preprint, |     |     |     |     |     |
| ------------- | --------- | ------------------- | --------------- | --- | --- | --- | --- | --- |
arXiv:1806.01159v2,DOI:10.48550/arXiv.1806.01159. 139 J. M. Hern´andez-Lobato, M. W. Hoffman and
115 J. Wilson, V. Borovitskiy, A. Terenin, P. Mostowsky and Z. Ghahramani, Advances in neural information processing
10292–
M. Deisenroth, Int. Conf. Mach. Learn., 2020, pp. systems,2014,vol.27.
| 10302. |     |     |     | 140 G.D.Ath,R.M.EversonandJ.E.Fieldsend,Proc.Genetic. |     |     |     |     |
| ------ | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
Evol.Comput.Conf.Companion,2021,pp.1860–1869.
| 116 M. Adachi, | S. Kayakawa, | S. Hamid, | M. J. rgensen, |     |     |     |     |     |
| -------------- | ------------ | --------- | -------------- | --- | --- | --- | --- | --- |
H.OberhauserandM.A.Obsourne,arXiv,2023,preprint, 141 Y. Saikai, arXiv, 2022, preprint, arxiv:2208.13960, DOI:
arxiv:2301.11832,DOI:10.48550/arXiv.2301.11832. 10.48550/arXiv.2208.13960.
117 M. Galar, A. Fernandez, E. Barrenechea, H. Bustince and 142 V.LalchandandC.E.Rasmussen,Proc.Mach.Learn.Res.,
| F. Herrera, | IEEE Trans. | Syst. Man Cybern.: | Syst. C, 2011, | 2020,1–12. |     |     |     |     |
| ----------- | ----------- | ------------------ | -------------- | ---------- | --- | --- | --- | --- |
42,463–484.
|     |     |     |     | 143 F. Leibfried, | V. Dutordoir, | S. T. John | and N. Durrange, |     |
| --- | --- | --- | --- | ----------------- | ------------- | ---------- | ---------------- | --- |
118 M.Zhang,PatternRecognit.,2022,124,108428. arXiv, 2020, preprint, arxiv:2012.13962, DOI: 10.48550/
119 D. Alvarez-Melis and T. S. Jaakkola, arXiv, 2018, preprint, arXiv.2012.13962.
arXiv:1806.08049,DOI:10.48550/arXiv.1806.08049.
648 | DigitalDiscovery,2024,3,637–648 ©2024TheAuthor(s).PublishedbytheRoyalSocietyofChemistry
