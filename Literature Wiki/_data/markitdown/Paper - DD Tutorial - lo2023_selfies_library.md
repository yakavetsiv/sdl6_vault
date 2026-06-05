---
tags:
  - literature
  - type/paper
  - lit/ai-methods
  - lit/digital-discovery
type: literature-note
---

Digital
Discovery
| TUTORIAL |     | REVIEW |     |     |     |     |     |     |     | View Article Online |     |     |     |
| -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
View Journal | View Issue
|     |     |     | Recent | advances |     | in the | self-referencing |     |     |     | embedded |     |     |
| --- | --- | --- | ------ | -------- | --- | ------ | ---------------- | --- | --- | --- | -------- | --- | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  strings (SELFIES) library
Citethis:DigitalDiscovery,2023,2,
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO 897
Alston Lo, *a Robert Pollice, abc AkshatKumar Nigam,d Andrew D. White, e
|     |     |     | Mario Krennf | and | Ala´n Aspuru-Guzikabgh |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------ | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
String-basedmolecularrepresentationsplayacrucialroleincheminformaticsapplications,andwiththe
growing success of deep learning in chemistry, have been readily adopted into machine learning
pipelines.However,traditionalstring-basedrepresentationssuchasSMILESareoftenpronetosyntactic
and semantic errors when produced by generative models. To address these problems, a novel
representation, SELF-referencing embedded strings (SELFIES), was proposed that is inherently 100%
robust, alongside an accompanying open-source implementation called selfies. Since then, we have
generalizedSELFIEStosupportawiderrangeofmoleculesandsemanticconstraints,andstreamlinedits
Received17thMarch2023
underlying grammar. We have implemented this updated representation in subsequent versions of
Accepted23rdJune2023
selfies, where we have also made major advances with respect to design, efficiency, and supported
| DOI:10.1039/d3dd00044c |     |     |     |     |     |     | selfies |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
features. Hence, we present the current status of (version 2.1.1) in this manuscript. Our library,
rsc.li/digitaldiscovery selfies,isavailableatGitHub(https://github.com/aspuru-guzik-group/selfies).
specicationofmoleculesinamannerthatcanbeparsedeffi-
1. Introduction
|                                                     |     |     |     |     |     | ciently,   | and which | is readable |     | for humans | at  | least for | small |
| --------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --------- | ----------- | --- | ---------- | --- | --------- | ----- |
| Inrecentyears,machinelearning(ML)hasbecomeapowerful |     |     |     |     |     | molecules. |           |             |     |            |     |           |       |
tool to tackle challenging problems in chemistry. Machine However, in an ML setting, this grammar can carry two
|                    |     |               |                   |     |              | intrinsic | weaknesses. | First, | many | strings | constructed |     | from |
| ------------------ | --- | ------------- | ----------------- | --- | ------------ | --------- | ----------- | ------ | ---- | ------- | ----------- | --- | ---- |
| learning pipelines |     | involve three | crucial elements: |     | data, repre- |           |             |        |      |         |             |     |      |
sentations,andmodels.Choosingtheproperrepresentationis SMILES symbols are syntactically invalid due to the rigidity of
important as it denes the space of models available to work theSMILESgrammar,i.e.,thestringscannotbeinterpretedas
withthedata,aswellasimpactingdirectlymodelperformance. molecular graphs.4,5 In particular, SMILES requires branch
For molecules, one of the more widely-used classes of repre- brackets and ring numbers to appear in matching pairs (e.g.,
|            |        |           |                   |     |              | C(CC and | C1C are | invalid), | so  | a single | misplaced | or missing |     |
| ---------- | ------ | --------- | ----------------- | --- | ------------ | -------- | ------- | --------- | --- | -------- | --------- | ---------- | --- |
| sentations | encode | molecules | as strings (i.e., | the | string-based |          |         |           |     |          |           |            |     |
molecular representations).These representations arepopular token could ruin the validity of a SMILES string. Thisis prob-
sincetheycanleveragetherichcollectionofMLtoolsthathave lematic because ML models that produce SMILES strings,
been developed for sequential data.1,2 Historically, the most especially generative models, can be prone to these syntactic
employed string representation is the Simplied Molecular errors, rendering a signicant fraction of their output mean-
|            |       |                  |       |                |     | ingless. | One strategy | is  | to constrain |     | the ML | architecture | to  |
| ---------- | ----- | ---------------- | ----- | -------------- | --- | -------- | ------------ | --- | ------------ | --- | ------ | ------------ | --- |
| Input Line | Entry | System (SMILES), | which | was introduced | by  |          |              |     |              |     |        |              |     |
Weiningerin1988.3Currently,SMILEShasbecomethedefacto reduce the number of invalid structures, which has been
standard representation in cheminformatics and has histori- demonstratedsuccessfullyintheliterature.6–8Thisapproach,of
callybeenakeycomponentofcentralapplicationsintheeld, signicant effort
|     |     |     |     |     |     | course, | needs |     | computational |     |     | and cannot | be  |
| --- | --- | --- | --- | --- | --- | ------- | ----- | --- | ------------- | --- | --- | ---------- | --- |
suchaschemicaldatabases.ThemainappealofSMILESisits transferreddirectlytoothersystemswithoutmodelretraining,
|                   |     |          |              |     |              | model architecture |     | adjustments, |     | or  | domain-specic |     | design |
| ----------------- | --- | -------- | ------------ | --- | ------------ | ------------------ | --- | ------------ | --- | --- | -------------- | --- | ------ |
| simple underlying |     | grammar, | which allows | for | the rigorous |                    |     |              |     |     |                |     |        |
considerations.Analternativeandmorefundamentalsolution
|     |     |     |     |     |     | is to dene | representations |     | that | are inherently |     | robust. | A rst |
| --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | ---- | -------------- | --- | ------- | ------ |
aDepartmentofComputerScience,UniversityofToronto,Canada.E-mail:alston.lo@ steptowardsthisdirectionwastakenbyDeepSMILES,9astring-
mail.utoronto.ca;r.pollice@rug.nl;alan@aspuru.com
basedrepresentationderivedfromSMILESthatreworkedsome
| bChemical Physics | Theory | Group, Departmentof | Chemistry, | University | ofToronto, |             |               |     |             |        |       |            |     |
| ----------------- | ------ | ------------------- | ---------- | ---------- | ---------- | ----------- | ------------- | --- | ----------- | ------ | ----- | ---------- | --- |
|                   |        |                     |            |            |            | of its most | syntactically |     | susceptible | rules. | While | DeepSMILES |     |
Canada
cStratinghInstituteforChemistry,UniversityofGroningen,TheNetherlands solves most of the syntactical errors, it does not address the
dDepartmentofComputerScience,StanfordUniversity,California,USA second weakness of SMILES, namely, that even syntactically
|     |     |     |     |     |     | valid strings | may | not | necessarily | correspond |     | to a physical |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ----------- | ---------- | --- | ------------- | --- |
eDepartmentofChemicalEngineering,UniversityofRochester,USA
fMaxPlanckInstitutefortheScienceofLight(MPL),Erlangen,Germany molecule. Typically, this occurs when a string represents
gVectorInstituteforArticialIntelligence,Toronto,Canada a molecular graph that exceeds normal chemical valences, in
hCanadianInstituteforAdvancedResearch(CIFAR)LebovicFellow,Toronto,Canada
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,897–908 | 897

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |     |     | TutorialReview |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
Atimelineofthevariousreleasesofselfies
| whichcasewecallthestringsemanticallyinvalid.Forexample, |          |      |           |              |         |       |           | Table1  |           |                               |     |     |     |
| ------------------------------------------------------- | -------- | ---- | --------- | ------------ | ------- | ----- | --------- | ------- | --------- | ----------------------------- | --- | --- | --- |
| the SMILES                                              | string   | CO]C | is        | semantically | invalid |       | because   | it      |           |                               |     |     |     |
|                                                         | species |      |           |              |         |       |           | Version | Year(s)   | Description                   |     |     |     |
| erroneously                                             |          | a    | trivalent | oxygen       | atom,   | which | is chemi- |         |           |                               |     |     |     |
| callyunstableandreactive.                               |          |      |           |              |         |       |           |         |           | (cid:2)Initialreleaseofseles |     |     |     |
|                                                         |          |      |           |              |         |       |           | 0.1.1   | (Jun)2019 |                               |     |     |     |
To eliminate both syntactic and semantic invalidities in (cid:2)Releaseofselesthatimplementsthe
|     |     |     |     |     |     |     |     | 0.2.4 | (Oct)2019 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | --- | --- | --- |
representationfromKrennetal.10
string-basedmolecularrepresentationsonafundamentallevel,
|             |     |                    |     |        |     |                  |     |       | 2020–21 | (cid:2)Expandedthesupportofselestoagreater |     |     |     |
| ----------- | --- | ------------------ | --- | ------ | --- | ---------------- | --- | ----- | ------- | ------------------------------------------- | --- | --- | --- |
| an entirely |     | new representation |     | termed |     | SELF-referencIng |     | 1.0.x |         |                                             |     |     |     |
subsetofSMILESstrings,includingstringswith
| Embedded | Strings | (SELFIES) |     | has been | proposed | by  | some | of  |     |     |     |     |     |
| -------- | ------- | --------- | --- | -------- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- |
aromaticatoms,isotopes,chargedspecies,and
us.10Byconstruction,SELFIESis100%robusttobothsyntactic certainstereochemicalspecications.Todoso,
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
and semantic errors. That is, any combination of SELFIES theunderlyinggrammarusedbyseleswas
species
symbols a molecular graph that obeys chemical bothstreamlinedandgeneralized
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO
valences. This is achieved through a small Chomsky type-2, (cid:2)Addedsupportforthecustomizationofthe
semanticconstraintsusedbyseles
context-free grammar11 that is augmented with self- (cid:2)Signicantlyimprovedtheefficiencyof
| referencing | functions |     | to handle | the | generation | of  | branches |     |     |     |     |     |     |
| ----------- | --------- | --- | --------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
translationbetweenSELFIESandSMILES
| and rings. | Sinceits | release, | SELFIES |     | has enabled | or  | improved |     |     |     |     |     |     |
| ---------- | -------- | -------- | ------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
(cid:2)Addedavarietyofutilityfunctionstomakethe
design12–15
numerous applications, ranging from molecular to handlingofSELFIESstringsconvenient
interpretability16 to image-to-string and string-to-string trans- 2.0.x 2021 (cid:2)UpdatedtheSELFIESalphabettobemore
| lations,17,18 |     |          |          |     |             |     |            |     |     | human-readableandstandardized |     |     |     |
| ------------- | --- | -------- | -------- | --- | ----------- | --- | ---------- | --- | --- | ----------------------------- | --- | --- | --- |
|               | and | has been | extended | to  | incorporate |     | functional |     |     |                               |     |     |     |
(cid:2)Improvedhandlingofstereochemical
groupsandotherfragments.19Foranextensivesummaryofits specicationsinSELFIESinvolvingringbonds
| applications               | and | opportunities, |     | we refer | readers | to  | the recent |       |      |                                              |     |     |     |
| -------------------------- | --- | -------------- | --- | -------- | ------- | --- | ---------- | ----- | ---- | -------------------------------------------- | --- | --- | --- |
|                            |     |                |     |          |         |     |            | 2.1.x | 2022 | (cid:2)Addedsupportforexplainingtranslations |     |     |     |
| communitypaperonSELFIES.20 |     |                |     |          |         |     |            |       |      | betweenSELFIESandSMILESthrough               |     |     |     |
Herein, we introduce seles 2.1.1, the latest version of the attributions
open-sourcePythonimplementationofSELFIES.Inparticular,
| we provide | a   | detailed | look | into its | history, | developments, |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ---- | -------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
underlyingalgorithms,design,andperformance.Togetherwith are translated into SELFIES. Furthermore, we handle species
withpartialcharges,radicals,explicithydrogens,non-standard
| the community, |     | we have | recently | overviewed |     | potential | exten- |     |     |     |     |     |     |
| -------------- | --- | ------- | -------- | ---------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- |
isotopes,andstereochemicaldenitionsinafullysyntactically
| sions and | formulated |     | 16 concrete | future | projects | for | SELFIES |     |     |     |     |     |     |
| --------- | ---------- | --- | ----------- | ------ | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
and other robust molecular string representations.20 We hope andsemanticallyrobustway.Besidesthestandardconstraints
|     |     |     |     |     |     |     |     | for the number |     | of valences, | users can | now specify | their own |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --------- | ----------- | --------- |
thatthismanuscriptwillalsohelpindevelopingsomeofthese
extensions and ideas. Our soware package seles can be constraints and we provide built-in relaxed and stricter
“pip seles” constraint presets that can be selected conveniently. Most
| installed | with | install |     | and | is available |     | at GitHub |     |     |     |     |     |     |
| --------- | ---- | ------- | --- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
(https://github.com/aspuru-guzik-group/seles) under the recently, we introduced the ability to trace the connection
Apache 2.0 license, along with comprehensive documentation between input and output tokens when translating between
|     |     |     |     |     |     |     |     | SELFIES | and SMILES. | Table | 1 gives | a brief changelog | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ----- | ------- | ----------------- | ------ |
andtutorials.
majorreleasesofselesandtheirassociatedadvancements.
|             |     |     |          |     |     |     |     | While      | the ideas  | outlined | in the         | initial publication10 | that        |
| ----------- | --- | --- | -------- | --- | --- | --- | --- | ---------- | ---------- | -------- | -------------- | --------------------- | ----------- |
| 2. Timeline |     | and | advances |     |     |     |     |            |            |          |                |                       |             |
|             |     |     |          |     |     |     |     | ensure the | validityof | the      | representation | remain at             | the core of |
seles,
Theseleslibraryversionthatimplementedtherepresentation the manifold implementation improvements and
fromKrennetal.10wasrstreleasedasseles0.2.4in2019.This extensionsarethenoveltiesthatwedetailinthispaper.Here-
|     |     |     |     |     |     |     |     | aer, | specied |     |     | seles |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | ------ | --- |
older version provided an API of two translation functions unless otherwise, we will use to refer to
seles2.1.1inparticularandSELFIEStorefertotherepresen-
| where | a restricted | subset | of organic, |     | uncharged, | nonaromatic |     |     |     |     |     |     |     |
| ----- | ------------ | ------ | ----------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
tationthatseles2.1.1implements.Wewillprovideacomplete
SMILESstringscouldbeconvertedtoandfromSELFIESstrings.
Inaddition,theinternalalgorithmsbehindselesreliedheavily andformaldescriptionoftheupdatedrepresentationinSection
3anddescribetheAPIofselesinSection4.
| on direct   | string | manipulations, |              | so they | were  | computationally |            |     |     |     |     |     |     |
| ----------- | ------ | -------------- | ------------ | ------- | ----- | --------------- | ---------- | --- | --- | --- | --- | --- | --- |
| inefficient | and    | difficult      | to maintain. |         | Since | then,           | seles has |     |     |     |     |     |     |
undergone several major redesigns that have signicantly 3. SELFIES specification
advancedthealgorithmichandlingofbothSMILESandSELF-
IES. Most importantly, the underlying grammar of seles has Being 100% robust, every string of SELFIES symbols corre-
beenstreamlined and generalizedinsubsequent versions.We sponds to a SMILES string that is both syntactically and
will now describe the changes up until seles 2.1.1, the most semantically valid. Recall that we call a SMILES string seman-
recentversionofselesatthetimeofpublicationofthiswork. ticallyvalidifitissyntacticallyvalidandrepresentsamolecular
|     |     | modication |     |     |     | seles |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
One major we made is that now uses graphthatobeysnormalchemicalvalences.
directed molecular graphs to internally represent SMILES and Within SELFIES, these chemical valences are encoded as
SELFIESstrings.Thishasaffordedselesgreaterefficiencyand aconstraintfunctionn:A/ℕ ;whereAisaniteuniverseof
0
exibility,andenabledanumberofadditionalextensionstobe the atom types (e.g., A¼fC;N;O;F;.g) of interest and
made. For example, we added support for aromatic molecules ℕ ¼ℕWf0g: The valences represented by n dictate that an
0
n(type(A))
bykekulizingSMILESstringswitharomaticsymbolsbeforethey atom A must assume incident bonds in total. Note
898 | DigitalDiscovery,2023,2,897–908 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
| TutorialReview |     |     |     |     |     |     |     |     |     |     |     |     |     | DigitalDiscovery |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
semanticallyunique,i.e.,differentatomsymbolsarenotinter-
thatifaSMILESstringobeysthevalencesk,eachofitsatomsA
makesatmostn(type(A))explicitbondswithinthestring.There changeable. This is not the case in SMILES due to shorthand
isapossibly-strictinequalityinthiscaseduetothewaySMILES abbreviations in how attached hydrogens and charge can be
automaticallyaddsimplicithydrogensuntilchemicalvalences represented. For example, the SMILES atom symbol pairs
aresatised.Inpractice,themappingnisrationallychosento ([Fe++],[Fe+2])and([CH],[CH1])areinterchangeable.Tocreate
align with both physical considerations and established a more standardized alphabet of symbols, we remove this
cheminformatics packages such as RDKit.21 For example, redundancyinSELFIES.
aplausiblesettingmightmap 3.1.2. Branch symbols. The general SELFIES branch
symbolhastheform
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
|     | n(C)=4,n(N)=3,n(O)=2,n(F)=1 |     |     |     |     |     | (1) |     |     |     |            |     |     |     |     |
| --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
|     |                             |     |     |     |     |     |     |     |     |     | [bBranch‘] |     |     |     | (5) |
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO whichisthedefaultbehaviourofseles(seeSection4.3).
|     |     |     |     |     |     |     |     |     | b ˛ | {3, = |     |     |     |     | ‘ ˛ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
We formulate chemical valences in this manner to empha- where , #} is a SMILES-like bond symbol and
| sizethatalthoughSELFIESdependsonn,itisnotxedtoany |     |     |     |     |     |     |     | {1,2,3}. |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
particularsettingofn.Thatistosay,SELFIEScanenforcerule
|     |     |     |     |     |     |     |     | 3.1.3. | Ring | symbols. | SELFIES | ring | symbols | can befurther |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | -------- | ------- | ---- | ------- | ------------- | --- |
sets induced by any arbitrary mapping n:A/ℕ ; even if they subdividedintotwosub-types.Theseareoftheform
0
| are not | chemically | meaningful. |     | To  | highlight | an  | absurd |     |     |     |     |     |     |     |     |
| ------- | ---------- | ----------- | --- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
½bRing‘(cid:3)
|     |     |     |     | n($) = |     |     |     |     |     |     |     |     |     |     | (6) |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
example, the uniform constraints 1000 can be used in ½b b Ring‘(cid:3)
1 2
principle,whichcorrespondstoeffectivelyhavingnosemantic
whereb˛{3,=,#}and
| constraints | at all. | In this | sense, | SELFIES | can be | thought | of  | as  |     |     |     |     |     |     |     |
| ----------- | ------- | ------- | ------ | ------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ageneralframeworkforanadjustablesetofconstraintsn.Inthe
|     |     |     |     |     |     |     |     |     | b   | ,b ˛{−,/,\},andnotbothb |     |     | =b  | =−  | (7) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
ensuing discussion, we will describe SELFIES under the 1 2 1 2
|            |      |      |            |     |          | n   | xed |                 |     |      |         |     |     |                |     |
| ---------- | ---- | ---- | ---------- | --- | -------- | --- | ---- | --------------- | --- | ---- | ------- | --- | --- | -------------- | --- |
| assumption | that | some | constraint |     | function |     | is   |                 |     |      |         |     | ‘ ˛ |                |     |
|            |      |      |            |     |          |     |      | are SMILES-like |     | bond | symbols | and | {1, | 2, 3}, similar | to  |
beforehand.
branchsymbols.Thesecondringsymboltype(eqn(6))isused
tohandlestereochemicalspecicationsacrossringbonds(see
3.1. Syntax
Section3.5).
Before explaining the SELFIES specication, we make a brief 3.1.4. Miscellaneous symbols. SELFIEShasafewauxiliary
aside and give an overview of the form of SELFIES strings. symbolsthatarenotcoretotherepresentation.Thesesymbols
Simply,avalidSELFIESstringisanynitesequenceofSELFIES stillhavecommonusecasesandarespeciallyrecognizedbythe
symbols joined together. For ease of visual partitioning, all functionsinselesthattranslatebetweenSELFIESstringsand
SELFIES symbols are enclosed by square brackets. Hence, SMILESstrings(seeSection4.1):
agenericSELFIESstringisoftheform (cid:2) The dot symbol, which can be used to express multiple
disconnectedfragmentsinasingleSELFIESstring,similartoits
[.][.][.]/[.][.]
|           |      |               |     |                  |     |        | (2) | roleinSMILES.Thedotsymbolisinterpretedbytreatingitas |     |           |             |     |        |            |         |
| --------- | ---- | ------------- | --- | ---------------- | --- | ------ | --- | ---------------------------------------------------- | --- | --------- | ----------- | --- | ------ | ---------- | ------- |
|           |      |               |     |                  |     |        |     | delimiter                                            | and | splitting | the SELFIES |     | string | across the | symbol. |
| where the | . is | a placeholder | for | a symbol-specic |     | token. | We  |                                                      |     |           |             |     |        |            |         |
Then,eachtokenistreatedasanindependentSELFIESstring.
| can further | categorize |     | SELFIES | symbols | into four | main | types, |         |           |                      |     |         |     |            |         |
| ----------- | ---------- | --- | ------- | ------- | --------- | ---- | ------ | ------- | --------- | -------------------- | --- | ------- | --- | ---------- | ------- |
|             |            |     |         |         |           |      |        | (cid:2) | The [nop] | (for “no-operation”) |     | symbol, |     | which is a | special |
namely, atom, ring, branch, and miscellaneous, and charac- paddingsymbolignoredbyseles.
terizethesyntaxofeachinthefollowing.Throughout,let3be
|           |        |     |         |         |        |        |        | Table          | 2   | provides examples |     | of SELFIES |     | atom, branch, | and |
| --------- | ------ | --- | ------- | ------- | ------ | ------ | ------ | -------------- | --- | ----------------- | --- | ---------- | --- | ------------- | --- |
|           |        |     |         |         | ðsÞn ; | s      | s ,.,s |                |     |                   |     |            |     |               |     |
| the empty | string | and | given n | strings | i i¼1  | let 1, | 2      | n ringsymbols. |     |                   |     |            |     |               |     |
denotetheirconcatenation.
| 3.1.1.     | Atom | symbols. | The | general | SELFIES | atom | symbol |      |                   |     |     |     |     |     |     |
| ---------- | ---- | -------- | --- | ------- | ------- | ---- | ------ | ---- | ----------------- | --- | --- | --- | --- | --- | --- |
| hastheform |      |          |     |         |         |      |        | 3.2. | TheSELFIESgrammar |     |     |     |     |     |     |
½ba(cid:3) Now, we return to explaining the practical algorithm used to
(3)
|     |     | a¼a | a   | a a | a   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
iso elem chiral H (cid:4) deriveSMILESstringsfromtheircorrespondingSELFIESstrings.
whereb˛{3,=,#,/,\}isaSMILES-likebondsymboland Todoso,werstintroducethenotionofacontext-freegrammar.
Acontext-freegrammarGisatupleG=(V,S,R,S),whereVand
a ˛f3;1;2;3;.g Saredisjointnitesetsofnonterminalandterminalsymbols,
iso
|     | a   | ˛felement |     | symbolsg |     |     |     |                                                   |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | -------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | elem      |     |          |     |     |     | respectively,R4V×(VWS)*isaniterelation,†andS˛Vis |     |     |     |     |     |     |     |
|     | a   | ˛f3;@;@@g |     |          |     |     | (4) |                                                   |     |     |     |     |     |     |     |
chiral
a ˛f3;H0;H1;.;H9g a so-called start symbol. Under G, strings of terminal symbols
H
a ˛f3;þ1;(cid:5)1;þ2;(cid:5)2;þ3.g canbederivedbyperforminganitesequenceofreplacements
(cid:4)
|     |     |     |     |     |     |     |     | startingwiththesingle-symbolstrings |     |     |     |     | =S.Ateachstept,ifthe |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- |
0
|              |         |     |           |         |     |               |     | currentstrings |     | containsanonterminalsymbolA˛V(i.e.,s |     |     |     |     | =   |
| ------------ | ------- | --- | --------- | ------- | --- | ------------- | --- | -------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
|              |         |     |           | type(a) |     |               |     |                |     | t                                    |     |     |     |     | t   |
| collectively | specify | an  | atom type |         | in  | a SMILES-like |     |                |     |                                      |     |     |     |     |     |
fashion(theatom'sisotopenumber,atomicnumber,chirality,
†TheKleenestarofanitesetofsymbolsA,denotedA*,isthesetofallstrings
| number | of attached | hydrogens, |     | and charge, | respectively, |     | and |     |     |     |     |     |     |     |     |
| ------ | ----------- | ---------- | --- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
formedbyconcatenatingnitely-manysymbolsfromA,whichincludestheempty
| sometimes | optionally). |     | Notably, | each SELFIES |     | atom symbol |     | is string. |     |     |     |     |     |     |     |
| --------- | ------------ | --- | -------- | ------------ | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,897–908 | 899

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |     |     |     |     | TutorialReview |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
Table2 ExampleSELFIESsymbols,bysymboltype Thederivationofasimplechainstartswiththeinitialstring
s =S.RecallthattheSELFIESsymbolsdictatehowproduction
0
| Type |     |     |     | Examples |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rulesareapplied.Forsimplechains,thisisachievedbyhaving
[#13C],[]O],[C@@H1],[N+1] eachpairofSELFIESatomsymbolandnonterminalsymbolA˛
Atom
[Branch3],[#Branch1],[]Branch2] VdetermineaproductionruleoftheformA/aA ′ ,wherea˛
Branch
|      |     |     |     | []Ring1],[/\Ring3],[Ring2] |     |     |     | S*  |               |        |     | ′ ˛ W | {3}.  |            |     |
| ---- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | ------------- | ------ | --- | ----- | ----- | ---------- | --- |
| Ring |     |     |     |                            |     |     |     |     | is a terminal | string | and | A V   | Then, | a sequence | of  |
Misc. .,[nop] replacements is iteratively performed by treating the SELFIES
stringasaqueueQofSELFIESsymbols.Ateachstep,thehead
r Ar forr ,r ˛(VWS)*)andthereisan(A,a)˛R,thenwe ofQispopped‡and,withanonterminalsymbolinthecurrent
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
1 2 1 2 strings ,isusedtoselectandapplyaproductionruletogetthe
| re pla ce A | w ith | a to get | the next | string | s =  | r ar . | For this |             | t   |            |     |                              |     |     |     |
| ----------- | ----- | -------- | -------- | ------ | ---- | ------ | -------- | ----------- | --- | ---------- | --- | ---------------------------- | --- | --- | --- |
|             |       |          |          |        | t+ 1 | 1 2    |          | nextstrings |     | .Notethats |     | =Sisitselfasinglenonterminal |     |     |     |
(A, a) ˛
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO reason, tuples R are called produ c tion r ule s, and are t+1 0
|     |     |     |     |     |     |     |     | symbol, |     | and each rule | induced | by  | a SELFIES | atom | symbol |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------- | ------- | --- | --------- | ---- | ------ |
suggestivelynotatedA/a.Thederivationterminatesonceonly
terminal symbols remain. The derivation of SMILES strings replaces one nonterminal symbol by another. Hence,
|     |     |     |     |     |     |     |     | throughout |     | the derivation, |     | the current | string | s   | will always |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | --- | ----------- | ------ | --- | ----------- |
under SELFIES is similar to the preceding process. In fact, t
containatmostonenonterminalsymbolandthereisneverany
| a context-free | grammar |     | underlies | SELFIES, | which | we  | call the |     |     |     |     |     |     |     |     |
| -------------- | ------- | --- | --------- | -------- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ambiguityastohoworwhichproductionruleisapplied.Once
SELFIESgrammar.
thecurrentstringhasonlyterminalsymbolsorQisempty,the
Specically,theSELFIESgrammartakes
nite,
(cid:1) (cid:3) process ends (since SELFIES strings are termination
V ¼ S;X ;X ;X ;.;X necessarilyoccurs).ThenalderivedSMILESstringisreadoff
|     |     | 1   | 2 3 | maxnðAÞ |     |     | (8) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S¼fSMILESsymbols;e:g:;C;¼;ð;.g
bydroppingallnonterminalsymbols.
wheremaxnðAÞisthemaximumvalenceofallatomtypes.The We now fully enumerate the SELFIES atom symbol to
productionrulemapping.Let[ba]beagenericatomsymbol,as
productionrulesRwillbecharacterizedlater.GivenaSELFIES
describedineqn(3).Basedonthissymbol,werstdenethe
string,itscorrespondingSMILESstringisthenderivedthrough
| a trajectory | of  | replacements |     | starting | from S, | as previously |     | terminalstring |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | -------- | ------- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
(
modications
| described.                                               | However, | there | are | two further |     |     | that |     |     |     | a;  | a˛O |     |     |     |
| -------------------------------------------------------- | -------- | ----- | --- | ----------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                          |          |       |     |             |     |     |      |     |     | a~¼ |     | if  |     |     |     |
| providesSELFIESitsstrongrobustness.First,thereplacements |          |       |     |             |     |     |      |     |     |     |     |     |     |     | (9) |
½a(cid:3); otherwise
| that are | performed | are | not chosen | arbitrarily, |     | but are | instead |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ---------- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
dictated by the SELFIES string of interest. At each derivation where O¼fB;C;N;O;S;P;F;Cl;Br;Ig are the symbols of
| step,thenextsymboloftheSELFIESstringisreadoffandfully |     |     |     |     |     |     |     |          |     |               |         |         |     |        | a~     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | ------- | ------- | --- | ------ | ------ |
|                                                       |     |     |     |     |     |     |     | elements |     | in the SMILES | organic | subset. | The | string | can be |
species
which production rule is applied. We systematically thoughtofastransformingaintotheSMILESsyntax.Then[ba]
designthissymbol-to-rulemappingsuchthatthenalderived together with the nonterminal symbol S ˛ V species the
SMILESstringwillalwaysbevalid.Second,SELFIESaugments
productionrule:
| the grammar |     | with self-referencing |     | functions. |     | These | self- |     |     |     |     |     |     |     |     |
| ----------- | --- | --------------------- | --- | ---------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
referencing functions manipulate the derivation process in S/ãX (10)
‘
morecomplicatedwaysthansimplereplacements,sotheyare
where‘=n(type(a))isthevalenceoftheatomtypespeciedby
notproductionrules.However,asbefore,themannerinwhich
these self-referencing functionsare applied is also dictated by a, and we hereaer dene X = 3 to be the empty string to
0
handlethecasewhere‘=0.Theatomsymbol[ba]togetherwith
thesymbolsintheSELFIESstring.Thus,aSELFIESstringcan
|     |     |     |     |     |     |     |     |     |     | ˛   | 1#i#maxnðAÞ; |     |     | species |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | -------- | --- |
beviewedasarecipeofinstructions(thesymbols)thatguides the symbol X V, where a produc-
i
tionoftheform:
stringderivationundertheSELFIESgrammar.
(
|     |     |     |     |     |     |     |     |     |     |     | b Yðd | Þa~X ;        | i f ‘ . | 0   |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------- | ------- | --- | ---- |
|     |     |     |     |     |     |     |     |     |     | X / |       | 0 ‘(cid:5)d 0 |         |     | (11) |
|     |     |     |     |     |     |     |     |     |     | i   | 3;    |               | i f ‘ ¼ | 0   |      |
3.3. Simplechainderivation
=min(‘,i,d(b)).Here,d(b)isafunctionthatreturns
|         |          |                |     |              |     |         |         | whered | 0   |     |     |     |     |     |     |
| ------- | -------- | -------------- | --- | ------------ | --- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Herein, | we begin | by considering |     | the simplest |     | type of | SELFIES |        |     |     |     |     |     |     |     |
theorderofthebondtyperepresentedbyb:
| strings, | those that | correspond |     | to simple | chains | of atoms. |     | In  |     |     |     |     |     |     |     |
| -------- | ---------- | ---------- | --- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8
>><1;
| SMILES,simplechainsofatomsarerepresentedbysequences |     |     |     |     |     |     |     |     |     |     |     | b˛f3;=;n |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
|                                                     |     |     |     |     |     |     |     |     |     |     |     | if       | g   |     |     |
of alternating atom and bond SMILES symbols, the latter of dðbÞ¼ 2; b¼¼
|                                                     |     |     |     |     |     |     |     |     |     |     | >>:3; | if  |     |     | (12) |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ---- |
| whichcansometimesbeleimplicitbyconvention.Examples |     |     |     |     |     |     |     |     |     |     |       | b¼# |     |     |      |
if
ofsuchSMILESstringsincludeCCCC(n-butane)andO]C]O
(carbon dioxide). Analogously, in SELFIES, simple chains are b b
|     |     |     |     |     |     |     |     | and | Y(n) | is a function | that | demotes | into | a SMILES | token |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | ---- | ------- | ---- | -------- | ----- |
representedbysequencesofSELFIESatomsymbols,whichcan representingabondoflowerordern#d(b):
| be understood |     | as playing | a   | similar role | as  | a grouping |     | of  |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aSMILESatomsymbolanditsprecedingSMILESbondsymbol.
SimplechainsaretheeasiesttoderiveinSELFIES,becausethe
| process | occurs | only through | mere | replacements, |     | as in | regular |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------ | ---- | ------------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
‡TopopordequeuetheheadofaqueueQmeanstofetchandthenremovethe
| context-freegrammars. |     |     |     |     |     |     |     | oldestiteminQ: |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
900 | DigitalDiscovery,2023,2,897–908 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
| TutorialReview |     |     |     |     |     |     |     |     |     |     |     |     | DigitalDiscovery |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
8
>><b; T ab le 3 T he s y m b o l s su c c ee d in g a b r an c h o r r in g S E L F IE S s y m b o la re
if dðbÞ¼n
|                                         |     |         |        |       |          |                |      | s o                                | m et ime s | ov e r lo a | d e d w i th | a n u m | e ri c in d e x , w h | ic h i s d e | te r m in e d b y |
| --------------------------------------- | --- | ------- | ------ | ----- | -------- | -------------- | ---- | ---------------------------------- | ---------- | ----------- | ------------ | ------- | --------------------- | ------------ | ----------------- |
|                                         |     | b YðnÞ¼ | 3;     | i f d | b s n    | 1              |      |                                    |            |             |              |         |                       |              |                   |
|                                         |     |         | >>:¼   | ð     | Þ ¼      |                | (13) | thefollowingsymbol-to-indexmapping |            |             |              |         |                       |              |                   |
|                                         |     |         | ;      | d     | b s n    |                |      |                                    |            |             |              |         |                       |              |                   |
|                                         |     |         |        | i f ð | Þ ¼      | 2              |      |                                    |            |             |              |         |                       |              |                   |
|                                         |     |         |        |       |          |                |      | Index                              |            | Symbol      |              |         | Index                 |              | Symbol            |
|                                         |     |         |        |       |          |                |      | 0                                  |            | [C]         |              |         | 8                     |              | [#Branch2]        |
| Ineqn(10)and(11),thenonterminalsymbolsX |     |         |        |       |          | areintuitively |      |                                    |            |             |              |         |                       |              |                   |
|                                         |     |         |        |       |          | m              |      | 1                                  |            | [Ring1]     |              |         | 9                     |              | [O]               |
| memorizing                              | the | maximum | number |       | of bonds | that the       | most |                                    |            |             |              |         |                       |              |                   |
|                                         |     |         |        |       |          |                |      | 2                                  |            | [Ring2]     |              |         | 10                    |              | [N]               |
[]N]
recently derived atom can adopt; the nonterminal symbol X m 3 [Branch1] 11
|     |     |     |     |     |     |     |     |     |     | []Branch1] |     |     |     |     | []C] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ---- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  canbeunderstoodasencodingthatthelastatomcanmakeat 4 12
most mbonds. Whenthe nextatom is derived, thebond con- 5 [#Branch1] 13 [#C]
|     |     |     |     |     |     |     |     | 6   |     | [Branch2] |     |     | 14  |     | [S] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO nectingittotheprecedingatomhasitsorderdecreasedmini- []Branch2]
|     |     |     |     |     |     |     |     | 7   |     |     |     |     | 15  |     | [P] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mallysuchthatthebondconstraintsarealwayssatised.
Allothersymbolsareassignedindex0
| Examples: | To  | show | these | production | rules | in a | concrete |     |     |     |     |     |     |     |     |
| --------- | --- | ---- | ----- | ---------- | ----- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
setting,wewilltranslatetheSELFIESstring
Q¼½¼C(cid:3)½O(cid:3)½#C(cid:3)½F(cid:3)½C(cid:3) (14) The derivation process extends that for simple chains (in
Section3.3),wherewepopSELFIESsymbolsstep-by-stepoffof
aqueueQ.Weonlyaddanadditionalruleforwhenwedequeue
alongwiththeconstraintsineqn(1).Thederivationofitscorre-
|     |     |     |     |     |     |     |     | a   | branch | symbol | from Q.Let | this | symbol be[bBranch‘], |     | asin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ---------- | ---- | -------------------- | --- | ---- |
spondingSMILESstringwouldproceedstep-wiseasfollows: eqn(5),andletAbeanonterminalsymbolinthecurrentstring
|     |     |     |     |     |     |     |     | s.  | ˛   |     |     | species |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
S 0CX ð½¼C(cid:3)Þ If A {S, X }, then this the application of the
|     |     |     | 4   |     |     |     |     | t   |     | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0COX ð½O(cid:3)Þ productionruleA/A.Effectively,thebranchsymbolisignored
1
0 C O C X ð ½ # C (cid:3)Þ (15) inthiscase.IfA=X fori$2,thenweperformareplacement:
|     |     |     |          | 3   |              |     |     |     |     |     | i   |     |     |     |     |
| --- | --- | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 0 C O CF | 3 ð | ½ F(cid:3) Þ |     |     |     |     |     |     |     |     |     |     |
0done:
|     |     |     |     |     |     |     |     |     |     |     | A/rX |     |     |     | (18) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
i−d 0
| whereeachlines |         | 0s      | ([ba])isusedtodenoteastepofthe |             |     |        |     |        |     |                                          |     |     |     |     |     |
| -------------- | ------- | ------- | ------------------------------ | ----------- | --- | ------ | --- | ------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
|                |         | t       | t+1                            |             |     |        |     | whered |     | =min(i−1,d(b)),andr˛S*isaSMILESsubstring |     |     |     |     |     |
|                |         |         |                                |             |     | [ba].  |     |        | 0   |                                          |     |     |     |     |     |
| derivation     | process | induced | by                             | the SELFIES |     | symbol | The |        |     |                                          |     |     |     |     |     |
obtainedthroughthefollowingrecursiveprocess.
| nal derived | SMILES | string | in  | this | case | is COCF. Now, | for |     |     |     |     |     |     |     |     |
| ------------ | ------ | ------ | --- | ---- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
First,‘symbolsarepoppedfromQandconvertedintointeger
amorecomplicatedexample,considertheSELFIESstring
/,c‘bethe
|     |     |     |     |     |     |     |     | valuesbythemappingsummarizedinTable3.Letc |     |     |     |     |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Q¼½CH3(cid:3)½13CH1(cid:3)½#O(cid:3)
|     |     |     |     |     |     |     | (16) | indices | in  | rst-to-last | order | of  | retrieval. In | the event | that Q |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --- | ------------ | ----- | --- | ------------- | --------- | ------ |
containsfewerthan‘symbols,themissingindicesaresettohave
identied
|     |     |     |     |     |     |     |     | a   | default | value of | 0. Next, | these | indices are |     | with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | -------- | ----- | ----------- | --- | ---- |
underthesameconstraints.Thederivationproceedsas
anaturalnumberN˛ℕbytreatingthemashexadecimaldigits:
X 0½CH3(cid:3)X
ð½CH3(cid:3)Þ
|     |     |         | 1                   |             |         |             |      |     |     |     |       | X‘  |              |     |      |
| --- | --- | ------- | ------------------- | ----------- | ------- | ----------- | ---- | --- | --- | --- | ----- | --- | ------------ | --- | ---- |
|     |     | 0 ½ C H | 3 (cid:3) ½ 1 3 C H | 1 (cid:3) X | ð ½1 3C | H 1(cid:3)Þ |      |     |     |     |       |     |              |     |      |
|     |     |         |                     | 2           |         |             | (17) |     |     |     | N ¼1þ |     | 16‘(cid:5)kc |     | (19) |
0 ½ C H 3 (cid:3) ½ 1 3 C H 1 (cid:3) ¼ O3 ð ½ ¼ O (cid:3)Þ k
k¼1
0done:
Then,NsymbolsfromQ(orallsymbolsinQ;
iffewerexist)are
producingthenalSMILESstring[CH3][13CH1]]O.Notethat
consumedtoformanewSELFIESstring,andwithstartsymbol
isotopes are assumed to share the same valence, and when S¼X (insteadofS=Sasbefore),thissubstringisrecursively
d
| hydrogen                | atoms | are specied |     | in an | atom | type, its valence |     | is     | 0                    |     |     |               |     |          |     |
| ----------------------- | ----- | ------------ | --- | ----- | ---- | ----------------- | --- | ------ | -------------------- | --- | --- | ------------- | --- | -------- | --- |
|                         |       |              |     |       |      |                   |     | derive | d intoaSMILESstringr |     |     | .Wetaker=3ifr |     | =3,andr= |     |
| decrementedaccordingly. |       |              |     |       |      |                   |     |        |                      |     |     | 0             |     | 0        |     |
(r )otherwise.§
0
|     |     |     |     |     |     |     |     |     | Examples: | To  | provide | an overview | of branch | derivation, | we  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | ----------- | --------- | ----------- | --- |
3.4. Branchderivation translateaSELFIESstringrepresentingaceticacid:
So far, we discussed chains of atoms, and their connectivity. Q¼½O(cid:3)½C(cid:3)½¼Branch1(cid:3)½C(cid:3)½¼O(cid:3)½¼C(cid:3) (20)
However,mostmoleculesaremorecomplexthansimplelinear
chains.Therefore,now,wetalkaboutthederivationsofbranches
|     |     |     |     |     |     |     |     | Processing |     | the rst | two SELFIES |     | symbols [O][C] | results | in the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ----------- | --- | -------------- | ------- | ------ |
(followed by rings in the subsequent section). In SMILES, ,aerwhichthesymbol[]Branch1]isdequeued.
stringOCX
| branches | are | specied | by enclosing |     | a SMILES | substring |     | in  |     | 3   |     |     |     |     |     |
| -------- | --- | -------- | ------------ | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Since‘=1,weconsumethenextsymbol[C]inQandidentifyit
parentheses,whichcanberecursivelynested;forexample,CC(]
withN=1.Hence,wecreatetheSELFIESsubstring[]O]from
O)O(aceticacid)andC(]O)(C(]O)O)O(oxalicacid).InSELFIES,
branchesarespeciedbySELFIESbranchsymbols,andsimilar
|                                                    |          |       |      |            |        |        |     | §Aminortechnicalityoccursifr |     |         | 0startswithabranchparentheses(,inwhichcase |     |                             |     |     |
| -------------------------------------------------- | -------- | ----- | ---- | ---------- | ------ | ------ | --- | ---------------------------- | --- | ------- | ------------------------------------------ | --- | --------------------------- | --- | --- |
| to atom                                            | symbols, | every | pair | of SELFIES | branch | symbol | and |                              |     |         |                                            |     |                             |     |     |
|                                                    |          |       |      |            |        |        |     | risoftheform((a              |     | 1),.,(a | m)a m+1)forstringsa                        |     | ˛S*thatdonotstartwith(.This |     |     |
| nonterminalsymboldeterminesomeruleonhowtomodifythe |          |       |      |            |        |        |     |                              |     |         |                                            |     | k                           |     |     |
wouldresultinaninvalidSMILESstringbecausebranchescannotstartwithother
| current | string. | We can | encode | branched |     | trees of atoms |     | in  |     |     |     |     |     |     |     |
| ------- | ------- | ------ | ------ | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
branchesinSMILES.Toamendthis,wenaturallyinterpretandreplacerwiththe
SELFIESbysequencesofatomandbranchsymbols. string(a 1),.,(a m)(a m+1).
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,897–908 | 901

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |          |     | TutorialReview |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------------- | --- |
|                  |     |     | Q   |     |     |     |     |     |     | species |     |                | le |
popping the next symbol in and, with start symbol X , Although a ring symbol a closure between the
2
recursivelyderiveitintotheSMILESsubstringr=(]O).Then, andrightringatoms,suchabondcannotbenaivelyaddedsince
| performingthereplacementineqn(18)givesthestringOC(]O) |     |     |     |     |     |        |       |          |     |             |         | le |           |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ------ | ----- | -------- | --- | ----------- | ------- | --- | --------- |
|                                                       |     |     |     |     |     | it may | cause | valences | to  | be violated | for the |     | ring atom |
X ,andprocessingthelastsymbol[]C]inQnallyproduces immediately(e.g.,considerthecasewherethisatomhasalready
1
a SMILES string OC(]O)C for acetic acid. Another SELFIES attaineditsmaximumvalence)orinthefuture.Hence,SELFIES
stringthatcorrespondstoOC(]O)Cis: postponesthecreationofringclosurestoanalpost-processing
|     |                                                                                         |     |     |     |      | step. Instead, |     | the | ring closure | candidates |     | are | pushed to |
| --- | --------------------------------------------------------------------------------------- | --- | --- | --- | ---- | -------------- | --- | --- | ------------ | ---------- | --- | --- | --------- |
|     | Q¼½O(cid:3)½C(cid:3)½¼Branch2(cid:3)½C(cid:3)½Ring1(cid:3)½¼O(cid:3)½F(cid:3)½¼C(cid:3) |     |     |     | (21) |                |     |     |              |            |     |     |           |
R;
|     |     |     |     |     |     | a temporary | queue |     | and | once all | the SELFIES | symbols | have |
| --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | --- | -------- | ----------- | ------- | ---- |
beenprocessed,theitemsinRarerevisitedinrst-to-lastorder.
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
The derivation is largely similar to that before. The major Basedonthestateoftheringatoms,acandidatemayberejected
differenceisthatwhenthebranchsymbolisdequeued,thenext
(andnoringbondismade)orexecuted.
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO ‘=2symbols[C][Ring1]areidentiedwithN=1+16(0)+1=2,
|                                                       |     |     |     |     |     | Specically, |      | given | a potential |        | ring closure | indicated | by         |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | ---- | ----- | ----------- | ------ | ------------ | --------- | ---------- |
| andthen,theSELFIESsubstring[]O][F]isusedtoagainderive |     |     |     |     |     |              | [b   | ‘],   |             |        |              |           |            |
|                                                       |     |     |     |     |     | symbol       | Ring | let   | m 1 and     | m 2 be | the number   | of        | additional |
r=(]O).
bondsthattheleandrightringatomscanmake,respectively.
|     |     |     |     |     |     | Ifm =0orm |         | =0,wemustrejectthecandidatesinceadding |        |     |                 |     |             |
| --- | --- | --- | --- | --- | --- | --------- | ------- | -------------------------------------- | ------ | --- | --------------- | --- | ----------- |
|     |     |     |     |     |     | 1         |         | 2                                      |        |     |                 |     |             |
|     |     |     |     |     |     | the ring  | closure | would                                  | exceed | one | of the valences |     | of the ring |
3.5. Ringderivation
|     |     |     |     |     |     | atom. The | candidate |     | is also | rejected | if its le | and | right ring |
| --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------- | -------- | ---------- | --- | ---------- |
Thenalfeaturethatisnecessarytocapturethediversevariety
|     |     |     |     |     |     | atoms are | not | distinct, | to  | avoid unphysical |     | self-loops. | Other- |
| --- | --- | --- | --- | --- | --- | --------- | --- | --------- | --- | ---------------- | --- | ----------- | ------ |
ofmoleculesistheabilitytoencoderingclosures.InSMILES, wise,thecandidateisaccepted,and,assumingthereisnopre-
thisisachievedbypairednumerictagsthatindicatetwosepa- existingbondbetweenitstworingatoms,weformanewbond
=min(d(b
rate atoms are joined together; for example, CC1CCC1 (meth- oforderd 0 1 ),m 1 ,m 2 )betweenthem.Ifapriorbond
ylcyclobutane).Byaddingbondcharactersbeforethenumbers, doesexist(e.g.,ifaduplicateringclosureisspeciedearlierin
SMILES can also specify ring closures of higher bond orders, R), then we increment the order of this existing bond as
suchasC]1CCCC]1(cyclopentene).InSELFIES,ringclosures
|     |     |     |     |     |     | necessary. | That | is, if | the existing | bond | is of | order d | , then we |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ------ | ------------ | ---- | ----- | ------- | --------- |
1
arespeciedbyringsymbols,whichbehavesimilarlytobranch promoteittoabondofpotentially-higherordermin(3,d +d ).
|     |     |     |     |     |     |     |     |     |     |     |     |     | 1 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
symbols.ThederivationprocessextendsthatinSection3.4. Examples: We translate a SELFIES string representing
| Pereqn(6),therearetwoformsofSELFIESringsymbols.To |     |     |     |     |     | methylcyclobutane: |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
simplifytheensuingdiscussion,however,wewillbeginbyonly
|                                      |      |             |                |              |         |                                         |     | Q¼½C(cid:3)½C(cid:3)½C(cid:3)½C(cid:3)½C(cid:3)½Ring1(cid:3)½Ring2(cid:3) |     |     |        |            | (25) |
| ------------------------------------ | ---- | ----------- | -------------- | ------------ | ------- | --------------------------------------- | --- | ------------------------------------------------------------------------- | --- | --- | ------ | ---------- | ---- |
|                                      |      | rst        |                | [b           | ‘]      |                                         |     |                                                                           |     |     |        |            |      |
| considering                          | the  | form.       | When a         | ring symbol  | Ring    | is                                      |     |                                                                           |     |     |        |            |      |
| poppedfromthequeueofSELFIESsymbolsQ; |      |             |                | anonterminal |         |                                         |     |                                                                           |     |     |        |            |      |
|                                      |      |             |                |              |         | TherstvesymbolsproducethestringCCCCCX |     |                                                                           |     |     |        | ,aerwhich |      |
| symbol                               | A in | the current | derived string | is used to   | specify |                                         |     |                                                                           |     |     |        | 4          |      |
|                                      |      |             |                |              |         |                                         |     |                                                                           |     |     | Since‘ | =          |      |
aproductionrule.IfA=S,thenweapplytheruleA/A,andthe the ringsymbol [Ring1]isdequeued. 1, thenext and
ringsymboliseffectivelyskipped.IfA=Xi,thenwereplace: nalsymbol[Ring2]speciesasingleringbondbetweenthenal
|     |     |     |     |     |     | C and its | N = | 3rd preceding |     | atom. | This produces | the | SMILES |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | ----- | ------------- | --- | ------ |
A/X
i−min(i,d(b)) (22) stringCC1CCC1.Notethatincrementingtheindexingsymbol:
|     |     |     |     |     |     |     | Q¼½C(cid:3)½C(cid:3)½C(cid:3)½C(cid:3)½C(cid:3)½Ring1(cid:3)½Branch1(cid:3) |     |     |     |     |     | (26) |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------------------- | --- | --- | --- | --- | --- | ---- |
Inaddition,weconsumethenext‘symbolsofQ(orallsymbolsin
Q; iffewerexist)tospecifyanumberN˛ℕbyeqn(19).Then,the
ringsymbolwouldindicatethataringclosureshouldbeformed increments the distance of the ring closure, hence producing
| between | the ring-initiating |     | atom and | the N-th atom | previously |     |     |     |     |     |     |     |     |
| ------- | ------------------- | --- | -------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
aSMILESstringforcyclopentaneC1CCCC1.Appendingacopy
derivedfromit(orsimply,therstatomiflessthanNsuchatoms
oftheringandindexsymbols:
exist).Here,thederivationorderistheorderinwhichatomsare
Q¼½C(cid:3)½C(cid:3)½C(cid:3)½C(cid:3)½C(cid:3)
(27)
realizedthroughtheproductionrulesineqn(10)and(11).Byring- ½Ring1(cid:3)½Ring2(cid:3)½Ring1(cid:3)½Ring2(cid:3)
initiatingatom,wealsomeantheatomatwhichbondswouldbe
madeiftheringsymbolwereinsteadanatomsymbol.Oen,this incrementsthebondorderoftheringclosureandproducesthe
SMILESstringCC]1CCC]1.
coincideswiththelast-derivedatom,asisthecasein:
|     |     |     |     |     |     | Thesecondringsymbolform[b |     |     |     |     | b Ring‘]ineqn(3)behaves |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- |
|     |     |     |     |     |     |                           |     |     |     | 1   | 2                       |     |     |
NC(C)COC*†X (23) nearly identically to [Ring ‘], and is used to support specica-
4
|     |     |     |     |     |     | tion of | stereochemistry |     | across | single | ring | bonds. | The only |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ------ | ------ | ---- | ------ | -------- |
wherethering-initiatingandlast-derivedatomsaremarkedwith differenceoccurswhenaringclosurecandidateproducedby[b
1
anasteriskanddagger,respectively.However,thisisnotthecase b Ring‘]isaccepted,andanewringbondisaddedbetweenthe
2
whenthelast-derivedatomlieswithinafully-derivedbranch: tworingatoms.Inthiscase,ifb ˛{/,\},thenweaddthebond
1
|     |     |                   |     |     |     | characterb | beforethenumericringtagontheleringatom, |     |     |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | ---------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | NC(C)COC*(C)(C†)X |     |     |     |            | 1                                        |     |     |     |     |     |     |
1 (24) and similar ly with b and the right ring atom. For instance, if
2
[/−Ring1]
|             |        |       |                       |           |       | the example | eqn | (25) | used | the symbol |     |     | instead of |
| ----------- | ------ | ----- | --------------------- | --------- | ----- | ----------- | --- | ---- | ---- | ---------- | --- | --- | ---------- |
| Forbrevity, | wewill | refer | to thering-initiating | atomasthe | right |             |     |      |      |            |     |     |            |
[Ring1],thenthederivedSMILESstringwouldbeCC/1CCC1.
| ring atom | and | its counterpart | the le | ring atom, as | the latter |     |     |     |     |     |     |     |     |
| --------- | --- | --------------- | ------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
precedestheformerinaSMILESstringunderderivationorder.
902 | DigitalDiscovery,2023,2,897–908 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
| TutorialReview |     |     |     |     |     |     |     |     |     |     |     | DigitalDiscovery |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
4. Library design aromaticatomsymbols(e.g.,c)inthesamewayasSMILES,so
|     |     |     |     |     |     | encoder( | ) performs | an  | internal | kekulization |     | if it is | passed an |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | -------- | ------------ | --- | -------- | --------- |
Theseleslibraryisdesignedtobefast,lightweight,anduser-
aromaticSMILESstring.Line7guardsagainsterrorsraisedby
friendly.Asmallbutnicefeatureofselesisthatitalsorequires encoder( ) when being passed SMILES strings that are syntac-
ticallyinvalid,semanticallyinvalid(i.e.,violatetheconstraints
noextradependencies.Atitscore,therearetwofunctionsthat
facilitate the interconversion between SELFIES strings and described in the next subsection), or unsupported. An unsup-
SMILESstrings.Formoreadvancedusage,weprovidefunctions ported SMILES string uses features of SMILES that are not
|              |     |            |          |             | seles | implementedinSELFIES,suchasthewildcard*andquadruple |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | -------- | ----------- | ------ | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| to customize | the | underlying | semantic | constraints | that   |                                                     |     |     |     |     |     |     |     |
enforces and operates upon. The default constraints are given bond $ symbols; the API reference of seles further details
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
inTable4,andareintendedfororganicmoleculeswithsingle, whichSMILESstringsarecurrentlysupported.Line10applies
double, or triple bonds. Finally, we also provide a variety of the roundtrip( ) function to a SMILES string c1ccccc1 for
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO
utility functions for manipulating SELFIES strings. The benzene.Indeed,thisround-triptranslationrecoversaSMILES
|     |     |     |     |     |     | C1]CC]CC]C1 |     |     |     | different |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --------- | --- | --- | --- |
following describes each type of function in more detail and string that is than the original
provides potential use case examples. All code snippets are string,butstillspeciesthe(kekulized)benzenemolecule.
writteninPython,withselesbeingaPythonlibrary. In greater detail, given an input SMILES string, encoder( )
rst
|     |     |     |     |     |     | performs | a      | kekulization |         | if it contains |       | any aromatic | atom   |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ------------ | ------- | -------------- | ----- | ------------ | ------ |
|     |     |     |     |     |     | symbols, | as was | in the       | example | above.         | Next, | the actual   | trans- |
4.1. Corefunctions
|     |     |     |     |     |     | lation process | begins. |     | In the | simplest | case, | if the input | repre- |
| --- | --- | --- | --- | --- | --- | -------------- | ------- | --- | ------ | -------- | ----- | ------------ | ------ |
SELFIES strings can conveniently be created from and turned sents a simple atom chain, then a translation to SELFIES is
intoSMILESstringsusingthefunctionsencoder()anddecoder( performed by essentially grouping each atom symbol with its
),respectively.ThelatterderivesaSMILESstringfromaSELF- precedingbondsymbol,ifany.Forexample,theSMILESstring
IES string, using the procedure described in Section 3. The O][13CH]C#N would be partitioned into O, ] [13CH], C, #N
former performs the translation in the reverse direction such andturnedrespectivelyintoSELFIESsymbols[O][]13CH1][C]
that passing a SMILES string through the composition deco- [#N].Branchesarerecursivelytranslatedandtheresultisused
der(encoder())isalwaysguaranteedtorecoveraSMILESstring toworkbackwardstondtheappropriatebranchandindexing
that represents the same molecule (but not necessarily the symbolstoprepend.Iftherearemultipleplausiblechoices,we
originalSMILESstringitself).TherecoveredSMILESstringwill use the one in which the branch symbol [bBranch‘] has ‘
also maintain themolecular traversal order(i.e., the specica- minimizedandbrepresentingthebondconnectingthebranch
totheparentchain.Forinstance,C(]O)Oisencodedas[C][]
| tion order | of the | atoms) | of the | original string. | The following |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | ------ | ---------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
excerptdenesatoyfunctionroundtrip()thatillustratesthis: Branch1][C][]O][O] instead of [C][#Branch2][C][C][]O][O],
C(]O)O
|     |     |     |     |     |     | despite both | SELFIES |     | strings | producing |     |     | under the |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ------- | --------- | --- | --- | --------- |
derivationprocess.Finally,ringclosuresarehandledsimilarly
|     |     |     |     |     |     | in that we | work | backwards |     | to nd | the appropriate |     | ring and |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | --------- | --- | ------ | --------------- | --- | -------- |
indexingsymbols.Iftherearemultiplechoices,weusetheone
|     |     |     |     |     |     | in which  | the ring | symbol | [b                  | Ring ‘] | (or [b | b Ring | ‘]) has ‘  |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | ------------------- | ------- | ------ | ------ | ---------- |
|     |     |     |     |     |     |           |          |        |                     |         |        | 1 2    |            |
|     |     |     |     |     |     |           |          | b(or b | b                   |         |        |        |            |
|     |     |     |     |     |     | minimized | and      |        | 1 , 2 )representing |         | the    | bond   | ofthe ring |
closure.
|     |     |     |     |     |     | 4.1.1. | SELFIES | and | SMILES. | The | core | functions | of seles |
| --- | --- | --- | --- | --- | --- | ------ | ------- | --- | ------- | --- | ---- | --------- | --------- |
interconvertbetweenSELFIESandSMILES;andinSection3,we
presentthemethodofinterpretingSELFIESstringsbyderiving
SMILESstringsunderasimpleaugmentedgrammar,following
Line5translatestheSMILESstringforbenzeneintotheSELF-
thepreviousSELFIESpaper.10However,itisimportanttonote
| IES string | in Line | 11. | Notably, | SELFIES does | not support |     |     |     |     |     |     |     |     |
| ---------- | ------- | --- | -------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
thatSELFIESisnotconceptuallyreliantonSMILES,andwemay
|     |     |     |     |     |     | just as naturally |     | interpret | SELFIES |     | strings | through | deriving |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | ------- | --- | ------- | ------- | -------- |
moleculargraphs.Infact,beforeversion2.0.0,bothencoder()
Table4 Thedefaultconstraintsusedbyselfies.Allatomtypesother
|            |            |        |       |                 |              | and decoder( | )   | were | implemented |     | as direct | string-to-string |     |
| ---------- | ---------- | ------ | ----- | --------------- | ------------ | ------------ | --- | ---- | ----------- | --- | --------- | ---------------- | --- |
| than those | explicitly | listed | below | are constrained | to 8 maximum |              |     |      |             |     |           |                  |     |
bonds,whichactsasacatch-allconstraint translations. We have since refactored the functions to
converttheinputstringtoanintermediategraph-basedrepre-
Maximumbonds
|             |     |         |     |          |          | sentation,                         | which  | is subsequently |       | transcribed |          | in          | the target |
| ----------- | --- | ------- | --- | -------- | -------- | ---------------------------------- | ------ | --------------- | ----- | ----------- | -------- | ----------- | ---------- |
|             |     |         |     |          |          | representation.                    |        | Future          | work  | could       | then     | expose this | graph      |
| Element     |     | Charge0 |     | Charge+1 | Charge−1 |                                    |        |                 |       |             |          |             |            |
|             |     |         |     |          |          | representation                     |        | with a          | clean | interface,  | allowing | users       | to use     |
|             |     |         |     | —        | —        | selesinaSMILES-independentmanner. |        |                 |       |             |          |             |            |
| H,F,Cl,Br,I |     | 1       |     |          |          |                                    |        |                 |       |             |          |             |            |
| B           |     | 3       |     | 2        | 4        | 4.1.2.                             | Random | SELFIES.        |       | Since       | every    | string of   | SELFIES    |
| C           |     | 4       |     | 5        | 3        |                                    |        |                 |       |             |          |             |            |
|             |     |         |     |          |          | symbols                            | can be | derived         | into  | a valid     | SMILES   | string,     | we can     |
| N           |     | 3       |     | 4        | 2        |                                    |        |                 |       |             |          |             |            |
generaterandombutvalidSMILESstringsbypassingrandom
| O   |     | 2   |     | 3   | 1   |         |         |         |          |     |           |       |         |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | -------- | --- | --------- | ----- | ------- |
|     |     |     |     |     |     | SELFIES | strings | through | decoder( | ).  | To sample | these | SELFIES |
| P   |     | 5   |     | 6   | 4   |         |         |         |          |     |           |       |         |
S 6 7 5 strings, we use the get_semantic_robust_alphabet( ) utility
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,897–908 | 903

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |     |     | TutorialReview |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
function, which returns a subset of semantically constrained constraints.Bychoosingasetofconstraintsinaccordancewith
SELFIESsymbols: chemical valences, 100% robustness can be achieved. Speci-
cally,selesusestheconstraintsinTable4bydefault.
However,alimitationofthedefaultconstraintsisthatSELFIES
|     |     |     |     |     |     |     | cannot represent | existing | molecules |     | that violate | them, | such as |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | --------- | --- | ------------ | ----- | ------- |
perchloricacid(whichfeaturesahypervalentClmaking7bonds).
Moreover,thecatch-allconstraintmaybetoorelaxedtoensurethe
validityofSELFIESstringscontainingatomtypesoutsidethosein
Table4(e.g.,Si,Se).Hence,usersmaywishtoinsteadusecustom
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
constraintsthataretailoredtotheSELFIESstringsbeingworked
seles
|     |     |     |     |     |     |     | with. To | this end, |     | provides | the key | function | set_se- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | -------- | ------- | -------- | ------- |
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO NotethatbychangingthepoolofSELFIESsymbolsfromwhich
mantic_constraints().Thefollowingprovidesaminimalexample:
| we sample | from, we | can change | the distribution |     | of  | produced |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | ---------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
molecules.
4.2. Explainingtranslation
| To explain | translations | between | SELFIES | and | SMILES, | both |     |     |     |     |     |     |     |
| ---------- | ------------ | ------- | ------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
encoder()anddecoder()supportanattributeagthatenables
| attributions | of the output | string | symbol(s) | to  | symbol(s) | in the |     |     |     |     |     |     |     |
| ------------ | ------------- | ------ | --------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
inputstring:
|     |     |     |     |     |     |     | Here, the    | constraints  | dictionary          |     | encodes | a set | of custom   |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | ------------------- | --- | ------- | ----- | ----------- |
|     |     |     |     |     |     |     | constraints; | specically, | explicitconstraints |     |         | onthe | neutral and |
±1chargedvariantsofC(asinTable4)andacatch-allconstraint
|     |     |     |     |     |     |     | (of 4 maximum | bonds). | Line | 8 then | sets | constraints | as the |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ---- | ------ | ---- | ----------- | ------ |
underlyingsemanticconstraintsthatseleswilloperateunder,
|     |     |     |     |     |     |     | which changes | the            | subsequent | behaviour |                  | of encoder( | ) and       |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | ---------- | --------- | ---------------- | ----------- | ----------- |
|     |     |     |     |     |     |     | decoder( )    | appropriately. | Note       | that      | the pre-existing |             | constraints |
arefullyreplacedinLine8;anyconstraintthatisnotexplicitly
speciedinconstraintswouldbethusremoved.
|     |     |     |     |     |     |     | For convenience, |     | seles | provides | a   | couple | of preset |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | -------- | --- | ------ | --------- |
modied.
|     |     |     |     |     |     |     | constraints | to serve | as templates | that | can | be easily |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------------ | ---- | --- | --------- | --- |
Thesecanbeobtainedasfollows:
Thecurrently-setconstraintscanalsobeviewedby:
| The attributions | are | a list | of AttributionMap |     | objects, | one for |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | ----------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
eachoutputsymbol.EachAttributionMapcontainstheoutput
|     |     |     |     |     |     |     | 4.4. Utilityfunctions |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
symbol,itsindex,andalistofAttributionobjects,eachofwhich
Theseleslibraryprovidesanumberofutilityandconvenience
holdsaninputsymbol(anditsindex)thatisresponsibleforthe
|                |      |      |                 |     |        |        | functions. | Two basic  | utility | functions | are          | len_seles( | ), which    |
| -------------- | ---- | ---- | --------------- | --- | ------ | ------ | ---------- | ---------- | ------- | --------- | ------------ | ----------- | ----------- |
| output symbol. | Note | that | a single output |     | symbol | may be |            |            |         |           |              |             |             |
|                |      |      |                 |     |        |        | computes   | the number | of      | symbols   | in a SELFIES |             | string, and |
attributed to multiple input symbols because it may be deter- split_seles(),whichtokenizesaSELFIESstringintoaniterable
| mined by | both atom | symbols | and branch |     | or ring | symbols. |     |     |     |     |     |     |     |
| -------- | --------- | ------- | ---------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
ofitsconstituentsymbols:
Tracingtherelationshipbetweensymbolscanenablealignment
betweenSMILESandSELFIESsothatper-atompropertiescan
beconnectedonbothsidesofthetranslation.
4.3. Customizationfunctions
| The seles | library dynamically |     | constructs | its | derivation | rules |     |     |     |     |     |     |     |
| ---------- | ------------------- | --- | ---------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
prespecied Furthermore,selesincludesfunctionstoextractavocabulary
| from a | set of |     | constraints, | which | dictate | the |     |     |     |     |     |     |     |
| ------ | ------ | --- | ------------ | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
maximumnumberofbondsthateachatomtypeinamolecule of symbols from a dataset of SELFIES strings, and to convert
mayform.ThederivationrulesthenensurethateachSELFIES SELFIES strings into label or one-hot encodings. Consider the
string corresponds to a molecular graph satisfying the set followingexample:
904 | DigitalDiscovery,2023,2,897–908 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
| TutorialReview |     |     |     |     |     |     |     |     |     | DigitalDiscovery |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
Anoverviewofselfiesutilityfunctions
Table5
| Function |     |     |     | Description |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
len_seles()
ComputesthesymbollengthofaSELFIESstring
split_seles()
TokenizesaSELFIESstringintoitsconstituentsymbols
get_alphabet_from_seles()
ExtractsaminimalvocabularyfromadatasetofSELFIESstrings
seles_to_encoding()
ConvertsaSELFIESstringintoalabeland/orone-hotencoding
encoding_to_seles()
RecoversaSELFIESstringfromitslabeland/orone-hotencoding
get_semantic_robust_alphabet() Providesanalphabetofsemantically-constrainedSELFIESsymbols
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
|     |     |     |     | 5. Results |     | and | discussion |     |     |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | ---------- | --- | --- | --- | --- |
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO
|     |     |     |     | seles        |             |     |       |         | efficient |                |              |
| --- | --- | --- | --- | ------------- | ----------- | --- | ----- | ------- | --------- | -------------- | ------------ |
|     |     |     |     | The           | library     | is  | quick | and     |           | in its         | translation, |
|     |     |     |     | despite being | implemented |     |       | in pure | Python.   | To demonstrate |              |
this,weprovidesomesimplebenchmarksofitscorefunctions
encoder()anddecoder().Thefollowingexperimentswererun
|     |     |     |     | on Google | Colaboratory, |     | which | uses | two | 2.20 GHz | Intel(R) |
| --- | --- | --- | --- | --------- | ------------- | --- | ----- | ---- | --- | -------- | -------- |
Xeon(R)CPUs.
5.1. Roundtriptranslation
Here,weconsidertheroundtriptranslationtask,whereaSMILES
|     |     |     |     | string is | translated | to  | SELFIES | and | then | back to | SMILES (see |
| --- | --- | --- | --- | --------- | ---------- | --- | ------- | --- | ---- | ------- | ----------- |
Specically,
|     |     |     |     | Section 4.1).   |     |       | we   | translate | the | Developmental    | Thera- |
| --- | --- | --- | --- | --------------- | --- | ----- | ---- | --------- | --- | ---------------- | ------ |
|     |     |     |     | peutics Program |     | (DTP) | open | compound  |     | collection,22,23 | which  |
containsalittleover300kSMILESstringsandisasetofmole-
|     |     |     |     | cules which   | have      | been        | tested   | experimentally |                | for potential   | treat-     |
| --- | --- | --- | --- | ------------- | --------- | ----------- | -------- | -------------- | -------------- | --------------- | ---------- |
|     |     |     |     | ment against  |           | cancer      | and      | the acquired   |                | immunodeciency |            |
|     |     |     |     | syndrome      | (AIDS).24 | Translating |          | the            | full           | dataset into    | SELFIES    |
|     |     |     |     | strings with  | encoder(  |             | ) takes  | 136 s,         | and recovering |                 | the SMILES |
|     |     |     |     | dataset using | decoder() |             | takes116 | s,             | for a          | total roundtrip | trans-     |
Here,wearegivenalistdatasetofSELFIESstrings.Line7uses
autilityfunctionofselestoextractthesetalphabetofSELFIES lation time of 252 s. Fig. 2plots how this roundtriptime scales
|     |     |     |     | with molecular |     | size. Notably, |     | we obtain |     | all of these | times by |
| --- | --- | --- | --- | -------------- | --- | -------------- | --- | --------- | --- | ------------ | -------- |
symbolsthatappearinthedataset,whichisusedinLine13to
createasymboltoindexmappingtermedstoi.Next,lines17–22 averagingover3replicatetrials.
seles_to_encoding(
| use another | utility function |     | ) to create |     |     |     |     |     |     |     |     |
| ----------- | ---------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
alabelandone-hotencodingoftherstSELFIESstringinthe 5.2. RandomSELFIES
dataset.Underthehood,thisfunctionrstpadstheinputstring
|     |     |     |     | First, we | sample | 1000xed-length |     | SELFIESstringsandtranslate |     |     |     |
| --- | --- | --- | --- | --------- | ------ | --------------- | --- | -------------------------- | --- | --- | --- |
tolengthpad_to_lenbyappendingtoitsufficientlymanycopies
|               |                             |       |              | them to         | SMILES, | per | Section | 4.1. | We try | this experiment | with |
| ------------- | --------------------------- | ----- | ------------ | --------------- | ------- | --- | ------- | ---- | ------ | --------------- | ---- |
| of the symbol | [nop] (for “no-operation”), | which | is a special | differentsymbol |         |     |         |      |        |                 |      |
lengthsandalphabetsfromwhichtheSELFIES
seles
padding symbol in that is automatically ignored by stringsarebuilt.Fig.1showstheresultingdistributionofSMILES
decoder().Then,thepaddedSELFIESstringistokenized,and
stringsandthetimeittakestodecodeeachfullbatchofrandom
stoiisusedtoconverteachofitssymbolsintointegerlabelsand reaffirms
|     |     |     |     | SELFIES | strings. | Performing |     | this | experiment |     | the |
| --- | --- | --- | --- | ------- | -------- | ---------- | --- | ---- | ---------- | --- | --- |
one-hot vectors. Since the padded SELFIES string may now robustnessofSELFIESanddemonstratestheeaseinwhichwecan
contain[nop],thissymbolmustbeaddedtostoi,whichisdone createrandomvalidmoleculeswithoutapplyinganylters,pre-or
throughLine8.Lastly,thereverseencodingcanbeperformed
post-selection.InFig.1a,weshowhowSELFIESstringssampled
usingtheencoding_to_seles()utility:
fromabasicalphabettranslatetorandommolecules;animpor-
tantobservationisthatthegeneratedmoleculesarerathersmall,
independentoftheSELFIESlengthchosen.Thatismainlycaused
|     |     |     |     | by the inclusion |     | of multi-bonds |     | and | low-valence | atoms | in the |
| --- | --- | --- | --- | ---------------- | --- | -------------- | --- | --- | ----------- | ----- | ------ |
consideredalphabet,whichexhausttheavailablevalencesofthe
constituentatomsandthenleadtoanearlierterminationofthe
|     |     |     |     | derivation. | A simple | workaround |     | is  | to instead | use | an alphabet |
| --- | --- | --- | --- | ----------- | -------- | ---------- | --- | --- | ---------- | --- | ----------- |
withoutmulti-bondsandlow-valenceatomtypes,asillustratedin
|     |     |     |     |                |           |            |     |                   |     | shied      | signi- |
| --- | --- | --- | --- | -------------- | --------- | ---------- | --- | ----------------- | --- | ----------- | ------- |
|     |     |     |     | Fig. 1b.       | Here, the | molecular  |     | size distribution |     | is          |         |
|     |     |     |     | cantly towards | larger    | molecules, |     | especially        |     | when longer | SELFIES |
Table 5 summarizes the various utility functions introduced stringaresampled.Hence,thisshowcaseshowtocreateverylarge
withinthissection.
andvalidrandommolecules.
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,897–908 | 905

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |     | TutorialReview |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
 .MA 25:61:3 6202/1/6 no dedaolnwoD .3202 yluJ 10 no dehsilbuP .elcitrA sseccA nepO
ForafixedalphabetA;
Fig.1 1000SELFIESstringsweregeneratedbyuniformlysamplingLsymbolsfromanalphabet.Then,weplotthesize
WetakeAtobethe69symbolsreturnedbyget_semantic_robus-
| distribution | oftheresultingmoleculesfor | varyingsymbollengthsL.(a) |     |     |     |     |     |     |     |     |     |
| ------------ | -------------------------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t_alphabet()underthedefaultsemanticconstraints.(b)Wefilterthealphabetin(a)to19symbolsbyremovingallatomsymbols[ba]whereb˛
{=,#}orn(type(a))=1,andremovingallbranchandringsymbolsexceptfor[Branch1]and[Ring1].ThisdecreasesthechancethattheSELFIES
derivationprocessisterminatedearly,causingthederivedmoleculestobelarger.(c)ThetimetakentotranslateeachbatchofrandomSELFIES
stringstoSMILESusingdecoder(),measuredbyaveragingover20replicatetrials.
that,weimplementedallnecessaryfunctionalityinthelibrary
itselfsothatitdoesnotrequireanyotherpackages.Addition-
ally,weaddedseveralutilityfunctionstothelibrarytosupport
commonusecases.Apartfromthesetwoprimegoals,wealso
madesignicanteffortstomake
theimplementationfasteras
|     |     |     |     |     | SELFIES | has | been | employed | in many | performance-critical |     |
| --- | --- | --- | --- | --- | ------- | --- | ---- | -------- | ------- | -------------------- | --- |
applicationsandworkows.
|     |     |     |     |     | Overall,              | the      | SELFIES  | community              |           | has grown   | rapidly and we |
| --- | --- | --- | --- | --- | --------------------- | -------- | -------- | ---------------------- | --------- | ----------- | -------------- |
|     |     |     |     |     | are actively          | engaging |          | in constructive        |           | discussions | about the      |
|     |     |     |     |     | currentimplementation |          |          | andfutureimprovements. |           |             | Whileself-     |
|     |     |     |     |     | ies 2.1.1             | supports | almost   | all                    | important | features    | of SMILES,     |
|     |     |     |     |     | there are             | still    | many new | features               | on        | our agenda. | We outlined    |
manyoftheminarecentperspective,20forexample,extensions
Fig. 2 The roundtrip translation time of 1000 randomly-sampled to polymers, crystals, molecules with non-covalent bonds, or
SMILESstringsfromtheDTPopencompoundcollectionasafunction reactions. Our vision is that SELFIES will become a standard
ofsize,measuredinnumberofatoms.
|     |     |     |     |     | computer      | representation |              | for | molecular | matter.         | We encourage |
| --- | --- | --- | --- | --- | ------------- | -------------- | ------------ | --- | --------- | --------------- | ------------ |
|     |     |     |     |     | the community |                | to implement |     | it into   | their workows, | report       |
errorsinthecurrentimplementation,andproposechangesand
| 6. Conclusions |     | and outlook |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
newfeaturesthatwillhelpthemtosucceedintheirgoals.
Sinceitsrstreleasein2019,theseleslibraryhasundergone
signicantchangesandexperiencedadrastictransformationin
Data availability
| terms of both | capabilities  | and code design. | All       | of these modi- |        |         |     |           |           |                      |     |
| ------------- | ------------- | ---------------- | --------- | -------------- | ------ | ------- | --- | --------- | --------- | -------------------- | --- |
| cations were | executed with | two major        | premises, | namely, (1)    | seles |         |     |           |           |                      |     |
|               |               |                  |           |                | The    | library | is  | available | at GitHub | (https://github.com/ |     |
extendingitsfunctionalityandcapabilitytosupportallfeatures
|     |     |     |     |     | aspuru-guzik-group/seles). |     |     | Our | benchmarking |     | scripts were |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ------------ | --- | ------------ |
of the SMILES representation and (2) retaining or even run on Google Colab and are also available at our repository
improvinguponitssimplicityanduser-friendliness.Toachieve (https://github.com/aspuru-guzik-group/seles/blob/
906 | DigitalDiscovery,2023,2,897–908 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

TutorialReview DigitalDiscovery
f38eeea4c8b60ce412fa917adb9258b89d4e8efc/examples/ 5 B. Sanchez-Lengeling and A. Aspuru-Guzik, Inverse
benchmark_v2_1_1.ipynb). molecular design using machine learning: generative
modelsformatterengineering,Science,2018,361,360–365.
Author contributions 6 M. J. Kusner, B. Paige and J. M. Hern´andez-Lobato,
Proceedings of the 34th International Conference on Machine
Learning,vol.70,2017,pp.1945–1954.
A. L.: conceptualization (equal), data curation (lead), formal
analysis (lead), investigation (lead), methodology (lead), so- 7 M. Olivecrona, T. Blaschke, O. Engkvist and H. Chen,
ware (lead), validation (lead), visualization (lead), writing – Molecular de-novo design through deep reinforcement
original dra (lead), writing – review & editing (lead). R. P.: learning,J.Cheminf.,2017,9,48.
8 M. Popova, O. Isayev and A. Tropsha, Deep reinforcement
conceptualization (equal), funding acquisition (supporting),
methodology (equal), project administration (equal), soware learningfordenovodrugdesign,Sci.Adv.,2018,4,eaap7885.
(equal), supervision (equal), writing – original dra (equal), 9 N. O’Boyle and A. Dalke, DeepSMILES: an adaptation of
writing – review & editing (equal). A. K. N.: conceptualization SMILES for use in machine-learning of chemical
structures, ChemRxiv, 2018, DOI: 10.26434/
(equal), funding acquisition (supporting), methodology (sup-
porting), soware (supporting), writing – original dra (sup- chemrxiv.7097960.v1.
porting), writing – review & editing (equal). A. D. W.: 10 M. Krenn, F. H¨ase, A. Nigam, P. Friederich and A. Aspuru-
methodology (supporting), soware (supporting), writing – Guzik, Self-referencing embedded strings (SELFIES):
original dra (supporting), writing – review & editing a 100% robust molecular string representation, Mach.
Learn.:Sci.Technol.,2020,1,045024.
(supporting). M. K.: conceptualization (equal), methodology
(equal), project administration (equal), soware (equal), 11 J.E.Hopcro,R.MotwaniandJ.D.Ullman,Introductionto
supervision (equal), writing – original dra (equal), writing – automata theory, languages, and computation, Addison-
Wesley,Boston,MA,2006.
review & editing (equal). A. A. -G: conceptualization (equal),
12 A. Nigam, R. Pollice, M. Krenn, G. dos Passos Gomes and
fundingacquisition(lead),projectadministration(supporting),
resources (lead), supervision (supporting), writing – review & A. Aspuru-Guzik, Beyond generative models: superfast
editing(supporting). traversal, optimization, novelty, exploration and discovery
(STONED) algorithm for molecules using SELFIES, Chem.
Conflicts of interest
Sci.,2021,12,7079–7090.
13 C. Shen, M. Krenn, S. Eppel and A. Aspuru-Guzik, Deep
molecular dreaming: inverse machine learning for de-novo
Therearenoconictstodeclare.
molecular design and interpretability with surjective
representations,Mach.Learn.:Sci.Technol.,2021,2,03LT02.
Acknowledgements 14 L. A. Thiede, M. Krenn, A. Nigam and A. Aspuru-Guzik,
Curiosity in exploring chemical spaces: intrinsic rewards
R. P. acknowledges funding through a Postdoc. Mobility for molecular reinforcement learning, Mach. Learn.: Sci.
fellowship by the Swiss National Science Foundation (SNSF, Technol.,2022,3,035008.
Project No. 191127). A. K. N. acknowledges funding from the 15 P.Eckmann,K.Sun,B.Zhao,M.Feng,M.GilsonandR.Yu,
Bio-XStanfordInterdisciplinaryGraduateFellowship(SGIF).A. International Conference on Machine Learning, 2022, pp.
A.-G.thanksAndersG.Frøsethforhisgeneroussupport.A.A.-G. 5777–5792.
also acknowledges the support of Natural Resources Canada
16 G. P. Wellawatte, A. Seshadri and A. D. White, Model
andtheCanada150ResearchChairsprogram.
agnostic generation of counterfactual explanations for
molecules,Chem.Sci.,2022,13,3697–3705.
References 17 K. Rajan, A. Zielesny and C. Steinbeck, DECIMER: towards
deep learning for chemical image recognition, J. Cheminf.,
1 W. A. Warr, Representation of chemical structures, Wiley 2020,12,65.
Interdiscip.Rev.:Comput.Mol.Sci.,2011,1,557–579. 18 K. Rajan, A. Zielesny and C. Steinbeck, STOUT: SMILES to
2 D. S. Wigh, J. M. Goodman and A. A. Lapkin, A review of IUPAC names using neural machine translation, J.
molecular representation in the age of machine learning, Cheminf.,2021,13,34.
WileyInterdiscip.Rev.:Comput.Mol.Sci.,2022,12,e1603. 19 A.H.Cheng,A.Cai,S.Miret,G.Malkomes,M.Phielippand
3 D.Weininger,SMILES,achemicallanguageandinformation A. Aspuru-Guzik, Group SELFIES: a robust fragment-based
system.1.Introductiontomethodologyandencodingrules, molecular string representation, Digital Discovery, 2023, 2,
J.Chem.Inf.Comput.Sci.,1988,28,31–36. 748–758.
4 R. G´omez-Bombarelli, J. N. Wei, D. Duvenaud, 20 M. Krenn, Q. Ai, S. Barthel, N. Carson, A. Frei, N. C. Frey,
J. M. Hern´andez-Lobato, B. S´anchez-Lengeling, P.Friederich,T.Gaudin,A.A.Gayle,K.M.Jablonka,etal.,
D. Sheberla, J. Aguilera-Iparraguirre, T. D. Hirzel, SELFIES and the future of molecular string
R. P. Adams and A. Aspuru-Guzik, Automatic chemical representations,Patterns,2022,3,100588.
design using a data-driven continuous representation of 21 G. Landrum, et al., RDKit: Open-Source Cheminformatics,
molecules,ACSCent.Sci.,2018,4,268–276. 2006,https://www.rdkit.org/.
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,897–908 | 907
.MA
25:61:3
6202/1/6
no
dedaolnwoD
.3202 yluJ
10
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

DigitalDiscovery TutorialReview
22 J. H. Voigt, B. Bienfait, S. Wang and M. C. Nicklaus, 24 G. W. Milne, M. C. Nicklaus, J. S. Driscoll, S. Wang and
Comparison of the NCI open database with seven large D. Zaharevitz, National cancer institute drug information
chemical structural databases, J. Chem. Inf. Comput. Sci., system 3D database, J. Chem. Inf. Comput. Sci., 1994, 34,
2001,41,702–712. 1219–1224.
23 W.-D. Ihlenfeldt, J. H. Voigt, B. Bienfait, F. Oellien and
M. C. Nicklaus, Enhanced CACTVS browser of the Open
NCIDatabase,J.Chem.Inf.Comput.Sci.,2002,42,46–57.
908 | DigitalDiscovery,2023,2,897–908 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry
.MA
25:61:3
6202/1/6
no
dedaolnwoD
.3202 yluJ
10
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