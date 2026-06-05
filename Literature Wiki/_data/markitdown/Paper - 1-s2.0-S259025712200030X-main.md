---
tags:
  - literature
  - type/paper
  - lit/nanomedicine
  - lit/ai-methods
type: literature-note
source_note: "Papers/Paper - 1-s2.0-S259025712200030X-main.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/1-s2.0-S259025712200030X-main.pdf"
converter: "microsoft/markitdown"
---
Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

Contents lists available at ScienceDirect

Current Research in Pharmacology and Drug Discovery

journal homepage: www.journals.elsevier.com/current-research-in-pharmacology-
and-drug-discovery

Evaluation of synergism in drug combinations and reference models for
future orientations in oncology

Diana Duarte a, b, Nuno Vale a, c, d, *

a OncoPharma Research Group, Center for Health Technology and Services Research (CINTESIS), Rua Dr. Pl(cid:1)acido da Costa, 4200-450, Porto, Portugal
b Faculty of Pharmacy, University of Porto, Rua Jorge Viterbo Ferreira, 228, 4050-313, Porto, Portugal
c Department of Community Medicine, Information and Health Decision Sciences (MEDCIDS), Faculty of Medicine, University of Porto, Al. Prof. Hern^ani Monteiro, 4200-
319, Porto, Portugal
d CINTESIS@RISE, Faculty of Medicine, University of Porto, Al. Prof. Hern^ani Monteiro, 4200, 319, Porto, Portugal

A R T I C L E I N F O

A B S T R A C T

Keywords:
Synergy
Drug combination
Oncology
Combination index
Bliss
Loewe

Current cancer therapy includes a variety of strategies that can comprise only one type of treatment or a com-
bination of multiple treatments. Chemotherapy is still the gold standard for cancer therapy, though sometimes
associated with undesired side effects and the development of drug resistance. For this reason, drug combination
is an approach that has been proposed to overcome the problems related to monotherapy and several studies have
already demonstrated the superiority of combined therapies compared to monotherapy. The main goal when
designing and evaluating drug combinations is to achieve synergistic effects by demonstrating that the combined
effects are greatly superior to the expected from the additive effects of the single drugs, allowing for dosage
reduction and therefore decreasing toxicity. Nevertheless, synergism quantiﬁcation is not a simple task due to the
different deﬁnitions of additivity and over the years several reference models have been proposed based on
different assumptions and with different mathematical frameworks. In this review, we begin to cover the available
treatment options for cancer therapy, with emphasis on the importance of drug combinations in cancer therapy.
We next describe the classical reference models that have been proposed for synergism evaluation, usually
classiﬁed as effect-based and dose-effect based methods, with a brief analysis of the current limitations of these
models. We also describe here the novel methods for the accurate quantiﬁcation of drug interactions in combined
treatments. At the end of this manuscript, we covered some of the most recent preclinical and clinical combination
studies that reﬂect the importance of the appropriate, accurate and precise application of the concepts and
methodologies here described for the evaluation of synergism.

1. Introduction

Biological organisms are composed of complex subsystems that
interact dynamically at different levels, with functions that are com-
plemented to avoid system malfunctions (Vakil and Trappe, 2019). When
a disease develops, it means that these subsystems are not working in a
proper way and rather than focusing on a single component of the con-
dition, treatment should focus on the disease's multifaceted problems.
(Vakil and Trappe, 2019). Current cancer therapy includes a variety of
strategies that can comprise only one type of treatment or a combination
of two or more types of treatment. The treatment plan is usually deﬁned
based on criteria related to the type of cancer, the stage of the tumor and
Institute, 2015a). Next,
patient characteristics

(National Cancer

according to the National Cancer Institute (NIH) guidelines, we will
describe the currently available cancer treatment options (Fig. 1).

Chemotherapy includes all drugs used in cancer therapy and acts on
the cell cycle by preventing or reducing the growth of tumoral cells,
whose growth rate is higher than normal cells (National Cancer Institute,
2015b). This strategy can be used for the treatment of cancer or for
ameliorating associated cancer symptoms, by shrinking tumors. This
pharmacological approach is used in different cancers, alone or com-
bined with other strategies, such as surgery, radiotherapy, etc. Chemo-
therapeutic drugs can also be administered before surgery or radiation
therapy to decrease tumor size (neoadjuvant chemotherapy) or after
surgery or radiotherapy to destroy the remaining cells (adjuvant
chemotherapy) (National Cancer Institute, 2015b). Chemotherapy lacks

* Corresponding author. OncoPharma Research Group, Center for Health Technology and Services Research (CINTESIS), Rua Dr. Pl(cid:1)acido da Costa, 4200-450, Porto,

Portugal.

E-mail address: nunovale@med.up.pt (N. Vale).

https://doi.org/10.1016/j.crphar.2022.100110
Received 26 March 2022; Received in revised form 22 April 2022; Accepted 7 May 2022
2590-2571/© 2022 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-
nc-nd/4.0/).

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

Fig. 1. Available options for cancer therapy. The most common approaches are surgery (whenever possible), chemotherapy (mono or combination therapy) and
radiotherapy or a combination of these approaches.

cell speciﬁcity affecting both tumoral and normal cells with elevated
growth rates, such as mouth, hair, or intestine cells, resulting in several
side effects such as mouth lesions, sickness, and hair loss. Chemotherapy
can be administered orally, intravenously, by muscular injection, intra-
thecal,
Intravenous chemo-
therapy may also be administered using catheters or ports (National
Cancer Institute, 2015b).

intraarterial or topical.

intraperitoneal,

Hormone therapy is a strategy used to treat cancer by slowing or
stopping cancer cell growth or to ease cancer symptoms. This strategy
acts by decreasing the body's capacity to produce hormones that
contribute to cancer development and growth or by changing hormones'
normal behavior in the body (National Cancer Institute, 2015c). Hor-
mone therapy is commonly used to treat hormone-dependent cancers,
such as prostate and breast cancer, being co-administered with other
cancer therapeutics. Hormone therapy can be administered as neo-
adjuvant or adjuvant therapy (National Cancer Institute, 2015c). This
strategy can also cause several side effects by interfering with the hor-
monal balance and include hot ﬂashes, weakened bones, diarrhea, fa-
tigue, etc. (National Cancer Institute, 2015c). Hormone therapies can be
given orally or by intramuscular injection. Ovaries or testicles' removal
can also be done to stop hormone production (National Cancer Institute,
2015c).

Radiotherapy makes use of high doses of radiation to destroy or
reduce cancer cell growth by damaging their DNA. Cancer cells with DNA
damage that cannot be repaired cannot divide and trigger mechanisms of
cell death (National Cancer Institute, 2010). This process is not imme-
diate, and some time may be needed for the DNA to be damaged enough
to kill cancer cells. This treatment can cause side effects as it can cause
cell damage to healthy cells surrounding the tumor. Radiotherapy can be
external or internal and the choice of administration depends on the type
and size of the tumors, the intrinsic characteristics of the tumor cells as
well as the characteristics of the patient (National Cancer Institute,

2

2010). Both external and internal radiation therapies are local treatments
and aim at the speciﬁc location of the tumor. Internal radiation therapy
can be solid (brachytherapy) or liquid (systemic therapy). Brachytherapy
consists of the administration of seeds, ribbons, or capsules that contain a
radiation source and is commonly applied for the treatment of head and
neck, breast, cervix, and prostate cancers (National Cancer Institute,
2010). Systemic therapy usually refers to a treatment that extends all
over the body, looking for and destroying tumoral cells. Radioactive
iodine, for example, is commonly used for the treatment of thyroid
cancer. Commonly, radiotherapy is combined with surgery or chemo-
therapy (National Cancer Institute, 2010).

The immune system is involved in the detection and destruction of
abnormal cells. Several times, immune cells known as tumor-inﬁltrating
lymphocytes (TILs) are found in and around tumors, suggesting that the
immune system recognizes the tumor cells as strange bodies. In fact,
patients with TILs-positive tumors have a better prognosis than patients
whose tumors are absent of these cells (National Cancer Institute, 2019).
In most cases, the cancer cells can avoid the destruction by the immune
system and start growing and dividing. This response happens when
cancer cells undergo genetic changes, leading to the production of sur-
face proteins or changes in the tumor microenvironment, masking them
to the immune system and interfering with the way the immune system
responds to the cancer cells (National Cancer Institute, 2019). Immuno-
therapy modulates the immune system of the patient to destroy cancer
cells and although it has been approved for many types of cancer, it is not
as used as the previously mentioned types of treatment. It includes the
use of inhibitors of immune checkpoints, T-cell transfer therapy, mono-
clonal antibodies, treatment vaccines or modulators of the immune sys-
tem (National Cancer Institute, 2019). Immune checkpoint inhibitors are
drugs that block immune checkpoints, decreasing the immunological
responses (National Cancer Institute, 2019). T-cell transfer therapy in-
immune cells from the tumor and their
volves the removal of

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

modiﬁcation to improve their activity against tumor cells. The most
active T cells in the tumor are selected, modiﬁed in the lab, and put back
into the patient's body (National Cancer Institute, 2019). Monoclonal
antibodies are proteins that recognize and bind to speciﬁc targets on
cancer cells, for better recognition by the immune system. Treatment
vaccines act by enhancing the response of the patient immune system to
cancer cells and immune system modulators modulate the patient's im-
mune response against cancer cells. Immunotherapy can be given via
oral, intravenous, topical or intravesical (National Cancer Institute,
2019).

Surgery is indicated for in situ solid tumors and is currently used in
several types of cancer (National Cancer Institute, 2015d), except for
leukemia or more advanced cancers. It consists of the surgical removal of
the tumor from the body and usually involves cuts with scalpels, which
results in side effects such as pain or elevated risk of infections. There are
other alternatives such as cryosurgery, lasers, hyperthermia, and photo-
dynamic therapy (National Cancer Institute, 2015d).

Laser treatment makes use of beams of light to cut through the tissue
and can be applied for precise surgeries or to destroy tumor cells (Na-
tional Cancer Institute, 2015e). Lasers are mostly used to treat basal cell
carcinoma, cervical, vaginal, esophageal, and non-small cell lung cancer.
Hyperthermia damages and destroys cancer cells by exposing them to
high temperatures (National Cancer Institute, 2015e). This treatment can
also increase the sensitivity of cancer cells to radiation or chemotherapy.
Hyperthermia is not yet commonly used but is under investigation in
clinical trials (National Cancer Institute, 2015e). Photodynamic therapy
makes use of light-reacting drugs and when the tumor is irradiated, drugs
are activating, destroying cancer cells (National Cancer Institute, 2015f).
This type of treatment is used to treat or alleviate symptoms caused by
skin cancer, mycosis fungoides, and non-small cell lung cancer (National
Cancer Institute, 2015f).

Targeted therapy is an approach that involves the targeting of
important proteins involved in carcinogenesis. Most targeted therapies
rely on the use of small-molecule drugs and monoclonal antibodies
(National Cancer Institute, 2014). Monoclonal antibodies, such as tras-
tuzumab, pembrolizumab, and rituximab, are synthetic proteins that
bind to speciﬁc sites in cancer cells, marking them for destruction by the
immune system. They can also directly stop cancer cell growth and
induce cell death (National Cancer Institute, 2014). This therapy only
works for patients whose tumors express targets for these monoclonal
antibodies, so biomarker testing (by biopsy) is usually performed prior to
treatment choice. In general, targeted therapies can act in different ways:
help the immune system to destroy tumor cells, act directly on cancer cell
growth, inhibit angiogenesis, cause cancer cell death and can also affect
hormone production (National Cancer Institute, 2014). They can also be
combined with toxins, chemotherapeutic drugs or even radiation to
perform selective delivery of cell-killing substances. Targeted therapy has
some weaknesses such as the appearance of resistance and the difﬁculty
of developing new drugs for some targets (National Cancer Institute,
2014).

Blood-forming stem cells are responsible for the formation and
renewal of blood cells. A stem cell transplant originated from bone
marrow, bloodstream, or umbilical cord allows restoring blood-forming
stem cells in patients affected by chemotherapy or radiotherapy, help-
ing them to a faster recovery after these treatments (National Cancer
Institute, 2015g). In multiple myeloma and other types of leukemia, this
therapy is the most frequent type of treatment and makes use of donor
healthy leukocytes to defeat the cancer cells from the patient (National
Cancer Institute, 2015g).

Despite the wide availability of treatments for cancer therapy,
chemotherapy still plays a major key role in the treatment of this disease.
Nevertheless, it is often accompanied by off-target effects that result in
undesired effects and also by the development of drug resistance
(Smalley et al., 2006). The discovery and approval of novel drugs for
cancer therapy is a process that is time and cost-consuming, making the
pharmaceutical industry reformulate existing drugs into combination

products. Although treatment with single compounds may be beneﬁcial,
several recent studies have reported the improved results of combina-
tions of two or more compounds compared to the use of single drugs
(Dear et al., 2013; Kim et al., 2020; Klimaszewska-Wi(cid:1)sniewska et al.,
2018; Lee et al., 2019; Sasaki et al., 2010; Vakil and Trappe, 2019). With
the recent advances in Omics and Cell Biology, the understanding of
cancer as a complex disease comprised of interconnected pathways has
increased the interest in the use of drug combinations in oncotherapy
(Keith et al., 2005; Podolsky and Greene, 2011; Zimmermann et al.,
2007).

2. Classical reference models for the analysis of drug
combinations

Drug combination has been used in several areas such as cancer
(Webster, 2016), asthma (Saleh, 2008), AIDS (Moreno et al., 2019), etc.
This strategy exploits the susceptibility of different molecular pathways
involved in the genesis of a certain disease to the different mechanism of
actions of each individual drug, aiming to improve the efﬁciency of the
treatment, decrease cytotoxicity to normal cells and reduce the devel-
opment of drug resistance (Foucquier and Guedj, 2015). When
combining two or more drugs, the main objective is to achieve positive
interaction effects, by demonstrating superior evidence on the beneﬁcial
combination of two or more drugs compared to each drug individually
(Tang et al., 2015). Basically, achieve more with less. To make the best of
the combination of drugs, it is important to efﬁciently ﬁnd a way to prove
that the drug combination has more beneﬁts than both drugs alone. Over
the years, research in this area resulted in several theoretical and
experimental manuscripts (Chou, 2010; Lederer et al., 2019; Roell et al.,
2017), that described those interaction effects mostly as synergistic or
antagonistic, that represent, respectively, more or fewer effects than the
expected additive effect from each drug individually (Foucquier and
Guedj, 2015).

Deﬁning additivity is not as simple as it may seem and throughout the
years several authors have proposed different formal deﬁnitions and
approaches to apply this concept in clinical practice (Chou, 2006; Geary,
2013). In this review, we provide the most commonly used reference
models for the evaluation of synergism in drug combinations, with a
mathematical framework to perform the accurate evaluation of drug
interactions in combination models. Next, we will describe the most

Fig. 2. Most well-known reference models for the analysis of drug combina-
tions. Current approaches can be divided into effect-based or dose-effect based
and are described by different mathematical frameworks, based on different
deﬁnitions of additivity.

3

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

common reference models for drug combinations, which can be classiﬁed
as effect-based and dose-effect based (Fig. 2).

2.1. Effect-based approaches

These methods are based on the effects of each individual drug within
a combination to assess a positive interaction effect (Foucquier and
Guedj, 2015). Effect-based strategies englobe four main strategies:
Combination Subthresholding, Highest Single Agent, Response Addi-
tivity, and Bliss Independence model (Foucquier and Guedj, 2015). The
term “effect”, sometimes referred to as response, is usually evaluated by
cell death, viability, growth rate, among others, being indicative of the
measured or phenotype effect. Throughout the manuscript, the descrip-
tion of theorems assumes two drugs, A and B, given at doses a and b, with
observed effects EA and EB. The effect of drug A combined with drug B is
given by EAB (Foucquier and Guedj, 2015).

2.1.1. Combination Subthresholding

The Combination Subthresholding is the most simple approach based
on the concept that the combination of ineffective doses of drugs gen-
erates signiﬁcant effects. Contrary to other reference models, this sig-
niﬁcant effect is deﬁned based on P-values obtained from statistical tests
by comparison with control (untreated groups) (Foucquier and Guedj,
2015). The observed effect is usually considered statistically signiﬁcant
when p < 0.05 (Fig. 3). Although this approach is sometimes still used,
the observed effects may not be accurate and do not necessarily be
representative of signiﬁcant differences if the difference between what is
signiﬁcant or not, is not necessarily signiﬁcant (Foucquier and Guedj,
2015; Nieuwenhuis et al., 2011).

2.1.2. Highest Single Agent (HSA)

This reference model is also known as the Gaddum's noninteraction or
cooperative effect (Geary, 2013; Leh(cid:1)ar et al., 2007) and assumes a pos-
itive combination interaction when the drug combination (EAB) elicits a
greater response than the highest single agent (EAB > max (EA, EB))
(Fig. 4). This represents an improvement of the Combination Sub-
thresholding as it allows the calculation of a combination index (CI) by
the following equation: CI ¼ max ðEA; EBÞ
. If the value obtained for CI is
EAB
positive, statistical signiﬁcance is evaluated by comparing drug combi-
nation effects with the single drug more effective using the p value of the
statistical test (Foucquier and Guedj, 2015). This reference model is more
advantageous as it evaluates if differences are signiﬁcant rather than the
difference of signiﬁcance. Nevertheless, this model only compares the
drug combination effect to the most effective individual drug (highest

Fig. 4. Demonstration of the Highest Single Agent approach. This model as-
sumes a positive interaction effect when the drug combination induces a greater
response than the highest single agent. Based on EA¼30, EB¼20 and EAB¼65.
Adapted from (Foucquier and Guedj, 2015).

single agent), not taking into account the expected additive effect of both
drugs involved in the combination (Foucquier and Guedj, 2015). This
makes this model suitable only for drug combinations where one of the
drugs is inactive for all tested concentrations. Normally, this approach
usually gives more optimistic results because it has the lowest threshold
for considering synergism among all reference models (Vlot et al., 2019).

2.1.3. Response additivity

This reference model is also known as Linear Interaction Effect
(Slinker, 1998) and assumes that a positive interaction occurs when the
drug combination (EAB) elicits a greater effect than the sum of the indi-
vidual drugs’ effects (EAB > EA þ EB) (Fig. 5). The CI can be calculated as:
CI ¼ EAþEB
, where the P-value means the signiﬁcance of the interaction
EAB
effect in factorial analysis of variance of the individual and combined
effects (Slinker, 1998). Compared to the previously mentioned reference
model, the Response additivity approach represents an improvement as it
compares the effects from the combination with the expected effects from
the single drugs, assuming their effect to be additive. Nevertheless, the
determination of synergism using this model implies the drugs have
linear dose-effect curves, which may not be true for many drugs used in
pharmacological studies (Caudle and Williams, 1993).

Fig. 3. Demonstration of the Response Additivity approach. This model assumes
synergistic effects when the drug combination induces a greater response than
the sum of the individual drugs’ effects. Based on EA¼30, EB¼20 and EAB¼65.
Adapted from (Foucquier and Guedj, 2015).

Fig. 5. Demonstration of the Response Additivity approach. This model assumes
synergistic effects when the drug combination induces a greater response than
the sum of the individual drugs’ effects. Based on EA¼30, EB¼20 and EAB¼65.
Adapted from (Foucquier and Guedj, 2015).

4

D. Duarte, N. Vale

2.1.4. Bliss independence

This approach is one of the most popular models and was ﬁrst
introduced in the 1930s (Berenbaum, 1989; BLISS, 1939; Geary, 2013;
Greco et al., 1995). This model assumes that both drugs used in drug
combinations act independently and do not interfere with the other,
assuming that drugs act on different sites of action (Fig. 6) (Greco et al.,
1995). Nevertheless, this model assumes both drugs contribute to the
observed effect. In this approach, the drug effects from single and com-
bination treatments are expressed in the form of a probability (0 (cid:2) E (cid:2) 1)
and the expected combined effect can be deﬁned as: EAB ¼ EA þ EBð1 (cid:3)
EAÞ, where EA and EB represent the observed effects of drug A and B,
respectively, and EAB the effect of drug A combined with drug B. The
calculation index for following this approach can be calculated as CI ¼
EAþEB(cid:3)EAEB
, being indicative of synergy, antagonism or additivity when
EAB

CI is under, above or equal to 1, respectively (Foucquier and Guedj,
2015). This model of non-interactivity is one of the effect-based ap-
proaches that has survived to the critics over time. Although this model is
widely used in the pharmaceutical ﬁeld and is more accurate than the
previous ones, it still presents some limitations (Goldoni and Johansson,
2007): it depends on the knowledge of mechanisms of action and most of
the times drugs have several,
intricate and possibly undetermined
mechanisms of action (Greco et al., 1995); then, this model presumes that
drugs follow an exponential dose-effect response, which is not applicable
for all drugs (Berenbaum, 1989); ﬁnally, this model only ﬁts for effects
that can be ranged in probabilities from 0 to 1 (Foucquier and Guedj,
2015).

2.2. Dose-effect-based approaches

More recently, novel approaches have been proposed to surpass the
limitations of the previously mentioned reference models. Especially for
drugs that have nonlinear dose-effect curves, dose–effect-based ap-
proaches represent an improvement as they take into account the dose of
each drug that results in the same quantitative effect (Berenbaum, 1977).
This reference model considers the dose-effect curves of each drug and
provides signiﬁcant and unequivocal deﬁnitions of synergy, additivity,
and antagonism (Foucquier and Guedj, 2015). Importantly, to evaluate if
there is an interaction effect in a drug combination, it is essential to ﬁrst
deﬁne a non-interactive effect, which can be achieved by null reference
models (Lederer et al., 2019).

2.2.1. Loewe Additivity

The Loewe additivity model is a null reference model and the most
well-known dose–effect-based approach. It was ﬁrst mentioned by Frei in

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

1913 and further described using a mathematical framework by Loewe in
1926 (Berenbaum, 1977; Loewe, 1927; LOEWE, 1953; Loewe and
Muischnek, 1926). This model is based on the isobole representation to
deﬁne the additive effect. This reference model assumes the dose
equivalence principle, meaning the dose a from Drug A is equivalent to
the dose ba of drug B and vice-versa, for any given effect. It also assumes
the sham combination principle, meaning that dose ba can be added to
any dose b of drug B to achieve an additive effect, which is not a char-
acteristic of other null reference models (Lederer et al., 2019). The ad-
ditive effects depend on the dose-curves of each drug and can be deﬁned
as Effect ða þ bÞ ¼ EAða þ abÞ ¼ EBðb þ baÞ ¼ EAB.

(cid:3)

(cid:1)

R ¼ A
B

This model assumes that individual drugs have a constant potency
ratio
, meaning their doses have the same ratio at each level of
effect. Graphically, this means the drugs have parallel dose-response
curves and achieve the same maximum effects (Tallarida, 2012). This
interaction can be deﬁned by the following mathematical equations: a þ
ab ¼ A ↔ a þ b (cid:4) R ¼ A ↔ a þ b (cid:4) A
¼ A, which is behind the Loewe
B
Additivity equation and many other dose-based approaches that derived
¼ 1:
from this reference model: a
A
The CI derived from the Loewe Additivity is calculated by: CI ¼ a
þ b
B
A
(Berenbaum, 1977; Chou and Talalay, 1983, 1984). When CI is under 1,
it means that the doses a and b that are necessary to produce a combined
effect are lower than the ones predicted from additivity, which is indic-
ative of synergistic interactions between the two drugs. When the CI
value is above 1, the doses from each individual drug that produces a
combined effect are greater than the ones predicted from additivity,
meaning that drug interaction is antagonistic (Berenbaum, 1977; Chou
and Talalay, 1983, 1984).

þ b
B

Isobologram analysis was ﬁrst introduced in 1995 by Greco et al.
(1995) and is a graphical approach to the Loewe Additivity model,
allowing an easy interpretation of the interaction of two drugs in a given
combination (Tallarida, 2012). It is a graphical representation that has
represented the doses of drug A and drug B in the x and y-axis and in-
dicates the collection of all dose combinations of the drugs that achieve a
desired percentage of effect.

In this graphical representation, there is a line with a negative slope
that represents the additive effect (also known as additive isobole),
where deviations from additivity indicate synergism or antagonism
(Fig. 7) (Chou, 2006; Grabovsky and Tallarida, 2004). It represents the
expected combined effect of a drug combination using doses a and b from

Fig. 6. Demonstration of the Bliss Independence approach. This model assumes
that both drugs act independently and do not interfere with each other. Based on
EA¼30, EB¼20 and EAB¼65. Adapted from (Foucquier and Guedj, 2015).

Fig. 7. Demonstration of the Loewe Additivity approach (isobologram). The
diagonal line represents the additive effect (also known as additive isobole) and
deviations from additivity are indicative of synergism or antagonism. Adapted
from (Foucquier and Guedj, 2015).

5

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

two drugs A and B and can be calculated by the equation b ¼ B (cid:3) B
(cid:4) a,
A
where doses of A and B are represented on the x and y-axis. This means
that when the doses from individual drugs necessary to achieve a com-
bined effects are lower than the corresponding ones described from the
additivity line (i.e., are located below the line), this can be translated as
synergy (CI < 1). A drug pair located on the additive isobole means that
CI ¼ 1 and therefore indicates additivity, whereas a drug pair located
above this isobole is indicative that higher doses of each individual drug
are necessary to produce the expected combined effect and therefore are
related with antagonism (CI > 1) (Foucquier and Guedj, 2015). This
approach does not rely on the drugs’ dose-response relationship neither
their mechanism of interaction, being only affected by the concentration
of the drugs used in the combination. This means that one drug pair can
be synergic for one dosage and antagonist for another therapeutic
regimen (Berenbaum, 1989).

(cid:3)

(cid:1)

¼

D
Dm

Just like the previous reference models, the Loewe Additivity model
also presents some limitations, mostly related to the dose-effect curves of
each individual agent. It is only designed for drugs that have dose-
response curves described by the Hill equation (also called sigmoid or
logistic function) but sometimes the determination of these curves re-
quires lots of data that can be time and money consuming (Sidorov et al.,
2019). Also, some drugs have dose-response curves that are difﬁcult to
model, making the Loewe Additivity model useless (Zhao et al., 2014). In
addition, many drugs do not ﬁt in the isobole straight line: this can be a
result of drugs that do not have a constant potent ratio, hence resulting in
non-parallel dose-response curves and/or when the individual drugs do
not achieve the same maximum effects (Grabovsky and Tallarida, 2004).
Many null reference models are based on the concept of isoboles. The
Chou-Talalay approach, proposed by Chou and Talalay is still one of the
most used in biological studies to quantify drug interactions, especially
synergism. This reference model has been built based on the Loewe
Additivity model (Chou and Talalay, 1983, 1984) and incorporates the
median-effect equation, derived from the uniﬁed theory mass-action law
m, where D represents
principle, represented by the equation fa
fu
the drug dosage or concentration, fa the inhibited fraction by the drug
dose D, fu the unaffected fraction, Dm the dose that causes 50% inhibi-
tion and m the coefﬁcient indicating the shape of the dose-effect curve.
The model is also described by a (r) value, that indicates the ﬁtting of the
data to the mass-action law. The values of (m), (Dm), and (r) for each
single drug are the dose-effect parameters required for the implementa-
tion of the Chou-Talalay theorem. In this way, the uniﬁed theory estab-
lishes the common link between single and multiple entities, and ﬁrst
order and higher order dynamics. The general equation that describes
this model, previously mentioned, is derived from the Michaelis-Menten,
Hill, Henderson-Hasselbalch, and Scatchard equations, the most impor-
tant ones in biochemistry and biophysics, and also resulted in the
development of the CI theorem, which offers a quantitative determina-
tion of synergism in drug combinations (Chou, 2010). It has been
improved by including the principle of mass action to analyze the com-
bined effects of a given combination and is now the subject of a huge
number of publications. The combination index for a two-drug combi-
nation can be calculated as following: CI ¼ ðDÞ
, where (Dx)1
1
ðDxÞ
1
represents the dose of the drug D1 alone that inhibits the growth of cells
by x% and (Dx)2 is the dose of the drug D2 alone that inhibits the growth
of cells by x%. It has its own graphical representation consisting of a plot
of CI versus effect, where CI < 1, CI ¼ 1 and CI > 1 indicate synergism,
additivity and antagonism, respectively (Fig. 8).

þ ðDÞ
2
ðDxÞ
2

2.2.2. Zero interaction potency (ZIP)

This is one of the most recent reference models proposed for the
evaluation of expected responses in drug combinations, being a hybrid
approach between the Bliss Independence and the Loewe Additivity
models (Yadav et al., 2015). This approach evaluates the drugs’ in-
teractions by comparing changes in the potency of the dose-response
curves between individual and combined drugs, not being affected by

6

Fig. 8. Fa-CI plot proposed by Chou and Talalay, based on Loewe Additivity
model. Fa indicates the observed effect and CI<1, CI¼1 and CI > 1 indicate
synergism, additivity and antagonism, respectively. Adapted from (Rodea-Pa-
lomares et al., 2015).

the pharmacodynamics of the compounds in combination. It assumes
that drugs are independent and do not interact with each other when
combined, resulting in minimal changes in their response curves when
combined (Yadav et al., 2015). This means that the accurate ﬁtting of the
dose-response curves is crucial for the determination of parameters like
the relative half-maximal effect concentration (EC50) and the slope,
which can be a difﬁcult challenge if data is of poor quality, for example
(Vlot et al., 2019).

Table 1 summarizes the advantages and disadvantages of the previ-
ously described references models used to assess the pharmacological
together with the mathematical
interaction in drug combinations,
framework behind the calculation the expected additive effect and CI
values for each model.

3. Current limitations of the classical combination models

As demonstrated in the previous sections, current reference models
for the evaluation of synergism have been improved over the years but
there are still some general limitations to the classical combination
models (Chou, 2010; Foucquier and Guedj, 2015; Ma and Motsinger-Reif,
2019).

The ﬁrst limitation in the analysis of drug combinations is the
misleading of the term “synergy” (Roell et al., 2017). In most clinical
studies and throughout the literature, this term is often used to justify the
combination of drugs in therapy, but many times this term is not clearly
deﬁned and commonly used without the proper knowledge underlying
the concept and the methods necessary to evaluate it (Lederer et al.,
2019; Ocana et al., 2012). Most of the time, synergy is not evaluated nor
calculated using the appropriate reference models and results are inter-
preted as synergism only by comparison of results obtained from simple
experimental assays, rather than included in a mathematical approach
and without information about the dose-effect curves for single drugs.
For example, sometimes, better-observed effects in drug combinations
are often described as synergy when indeed it is only a potentiation of the
effects of the two drugs combined if only one drug is active alone
(Foucquier and Guedj, 2015).

Another limitation is that, to date, there is not a standard reference
model to evaluate synergism. All available reference models have limi-
tations and while some fail to provide clear deﬁnitions of additivity,
others rely on data about the drug's mechanism of action, do not cover
rare and speciﬁc cases like drugs that do not follow the ideal dose-
response curves, or are not intuitive and user friendly (Shafer, 2012).
The Loewe Additivity model is the most improved reference model, but it
is also limited by the large amount of data required to make precise
synergy analysis, which is particularly important when the data is

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

Table 1
Advantages, disadvantages and mathematical framework of the reference models described in this manuscript used to assess the pharmacological interaction in drug
combinations.

Reference model

Pros

Cons

Mathematical Framework

Combination

Subthresholding

(cid:5) Most simple approach

(cid:5) Effect-based approach
(cid:5) Signiﬁcant effects are deﬁned based on P-values
(cid:5) The observed effects may not be accurate and

do not necessarily be representative of
signiﬁcant differences

(cid:5) Does not allow the calculation of a combination

index (CI)

(cid:5) Least accurate reference model

The observed effect is considered statistically
signiﬁcant when p < 0.05

Highest Single Agent

(cid:5) Allows the calculation of a combination index

(cid:5) Effect-based approach

(CI)

(cid:5) Gives more optimistic results among all

(cid:5) Does not take into account the expected

reference models

additive effect of both drugs involved in the
combination

(cid:5) Suitable only for drug combinations where one

of the drugs is inactive for all tested
concentrations

Response additivity

(cid:5) Allows the calculation of a combination index

(cid:5) Effect-based approach

(CI)

(cid:5) Takes into account the effects of both drugs in
the combination, assuming their effect to be
additive

(cid:5) Implies the drugs to have linear dose-effect

curves

Bliss Independence

(cid:5) One of the most popular
(cid:5) Allows the calculation of a combination index

(cid:5) Effect-based approach
(cid:5) Depends on the knowledge of mechanisms of

(CI)

action of the drugs

(cid:5) Takes into account the effects of both drugs in

(cid:5) Presumes that drugs follow an exponential

the combination

dose-effect response

(cid:5) Assumes that both drugs act independently and

(cid:5) Only ﬁts for effects that can be ranged in

do not interfere with the other

(cid:5) Allows combinations of more than 2 drugs

probabilities from 0 to 1

(cid:5) EAB ¼ max (EA, EB)

(cid:5) CI ¼

max ðEA; EBÞ
EAB

(cid:5) EAB ¼ EA þ EB

(cid:5) CI ¼ EA þ EB
EAB

(cid:5) EAB ¼ EA þ EBð1 (cid:3) EAÞ
(cid:5) CI ¼ EA þ EB (cid:3) EAEB

EAB

Loewe Additivity

(cid:5) Most well-known dose–effect-based approach

(cid:5) Only designed for drugs that have dose-

(cid:5) EAB ¼ EAða þ abÞ ¼ EBðb þ baÞ

(cid:5) Allows the calculation of a combination index

(cid:5) Requires more data and sometimes raw data

(CI)

preprocessing

(cid:5) Take into account the dose of each drug

(cid:5) Only ﬁt to drugs that have a constant potent

(cid:5) CI ¼ a
A

þ b
B

response curves described by the Hill equation

ratio.

(cid:5) Assumes the dose equivalence and the sham

combination principles

(cid:5) Graphical approach (isobologram)
(cid:5) Does not rely on the drugs' dose-response rela-
tionship nor their mechanism of interaction
(cid:5) Allows combinations of more than 2 drugs

Zero Interaction

Potency

(cid:5) One of the most recent reference models

(cid:5) Requires accurate ﬁtting of the dose-response

(cid:5) Dose-effect based approach
(cid:5) Assumes that drugs are independent and do not

(cid:5) Requires data of good quality
(cid:5) Does not allow combinations of more than 2

curves

(cid:5) EAB ¼

interact with each other when combined

(cid:5) It is not affected by the pharmacodynamics of

drugs

the compounds in combination

(cid:5)λA

(cid:4) ½A(cid:6)
EC50;A
(cid:4) ½A(cid:6)
EC50;A

(cid:5)λA

1 þ

(cid:5)λB

(cid:4) ½B(cid:6)
EC50;B
(cid:4) ½B(cid:6)
EC50;B

1 þ
(cid:5)λB

þ

(cid:5)λA

(cid:3)

(cid:5)λB

(cid:4) ½A(cid:6)
EC50;A
(cid:4) ½A(cid:6)
EC50;A

1 þ

(cid:5)λA

(cid:4) ½B(cid:6)
EC50;B
(cid:4) ½B(cid:6)
EC50;B

1 þ

(cid:5)λB

expensive or difﬁcult to determine (Foucquier and Guedj, 2015). On the
other hand, effect-based approaches are more limited but can still pro-
vide enough evidence of positive combination effects, with fewer data.
Another limitation is that most of the time, the analysis of drug in-
teractions in the clinical trials involving drug combinations is impaired
by intense practical and ethical constraints, which makes it hard to
collect sufﬁcient data to clearly and properly support synergy. Also, the
choice of the reference model in each step of the investigational process
must be tailored to the data available at each discovery step. For example,
in in vitro studies, the Highest Single Agent, Bliss Independence, and
Loewe Additivity may be the most appropriate reference models to ﬁnd
promising drug pairs for evaluation of their mechanisms of action or to
proceed for further clinical research (Borisy et al., 2003; Cokol et al.,
2011; Leh(cid:1)ar et al., 2007, 2009; Wientjes, 2010; Zhao et al., 2004),
whereas in further preclinical studies the Loewe Additivity with CI and
Isobologram analysis may be more appropriate to determine more

precisely the combination effects (Foucquier and Guedj, 2015). In clinical
studies in humans, the recommendations from the Food and Drug
Administration (FDA) (US FDA, 2013) together with the European
Medicines Agency (EMA) (European Medicines Agency Committee for
Human Medicinal Products, 2017) and the World Health Organization
(WHO) (World Health Organization, 2005) determine that there must be
a strong and rational basis for the use of combination therapies supported
by previous preclinical studies that also justify the use of combined
agents over individual drugs and their improved safety proﬁle for the
proposed disease. Nevertheless, extrapolating in vitro results to animals
or even humans is not well established and raise several questions, being
far from being consensual among the scientiﬁc community (Ram, 2019).
Generally, drug combination clinical trials include four experimental
groups that are treated with placebo, drug A, drug B or a combination of
drug A þ drug B and it must be clearly demonstrated that combination
therapy has a great efﬁcacy than both drugs alone, using the same or even

7

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

lower doses than the individual agents, while still maintaining a safety
proﬁle (Chou, 2010; Woodcock et al., 2011).

The fourth limitation is related to the optimization of dose ratios.
Since cells do not differentiate single drugs or their combination, two
drugs combined at a given ratio could be considered as a third that has its
own dose-effect relation (Chou, 2010). So, rather than evaluating if a
drug combination is synergistic, scientists must ask what dose ratio op-
timizes their synergy (Keith et al., 2005). To do so, the design of exper-
imental analysis must evaluate a different set of ﬁxed ratios and explore
what doses ﬁt well to reach the desired synergistic effects (Ma and
Motsinger-Reif, 2019). These experiments should always be performed in
preclinical studies before further clinical trials (Foucquier and Guedj,
2015).

When analyzing drug combination results, one must also take into
account that biological experiments regularly have associated some type
of experimental error (Foucquier and Guedj, 2015). Although the Highest
Single Agent and Response Additivity reference models take into account
the statistical signiﬁcance, the Bliss Independence and Loewe Additivity
models do not allow statistical signiﬁcance interpretation, because they
do not have the mathematical background necessary for statistical eval-
uation (Foucquier and Guedj, 2015). The software CompuSyn (http
://www.combosyn.com), based on the Chou-Talalay theory, follows
the Loewe Additivity model and assumes the Median-Effect approach of
Chou and Talalay to assess the statistical signiﬁcance of the experiments,
representing an improvement over other approaches (Chou, 2010).

Another aspect when referring to the previously mentioned ap-
proaches is the use of drug combinations with more than two drugs, a
common practice in cancer therapy, for example. Indeed, these ap-
proaches can be further extended for use of any drugs in combination. For
example, for the Loewe Additivity model, the CI can be calculated by the
following equation: CI ¼ a
þ … þ n
N. Nevertheless, such generaliza-
A
tion does not permit the quantiﬁcation of each drugs’ contribution to the
combination, implying that a synergistic combination of three or more
drugs could be the result of only two drugs, for example (Foucquier and
Guedj, 2015). Therefore, it is really important to rationally design the
experimental protocols to demonstrate that, for example, in a triple
combination using drugs A, B and C, A and B are synergistic, and that the
combination of A þ B (considered as a new single agent) with the drug C
is also synergistic (Foucquier and Guedj, 2015).

þ b
B

4. Recent methods for directly quantifying drug synergism

Loewe additivity and Bliss independence approaches have been
dominant in the ﬁeld of synergism, together with the work proposed by
Chou and Talalay. Still, there is no consensus among the scientiﬁc
community regarding the appropriate use of these reference models.
Recently, there has been an increase in the number of publications
related to the deﬁnition of synergism, such as the “lack-of-ﬁt” model
(Lederer et al., 2019) or the rediscovered Hand model (Hand, 2000;
Sinzger et al., 2019). Novel ways to evaluate synergism in drug combi-
nation studies also appeared such as the ZIP model (Yadav et al., 2015),
Combeneﬁt (SANE) (Di Veroli et al., 2016), Bivariate Response to Ad-
ditive Interacting Doses (BRAID) (Twarog et al., 2016), Schindler's Hill
partial differential equation (Schindler, 2017), the SynergyFinder soft-
ware (Zheng et al., 2022), the Multi-dimensional Synergy of Combina-
tions (MuSyC) (Meyer et al., 2019), the effective dose model (Zimmer
et al., 2016) and the copula model (Lambert and Dawson, 2019), for
example. Next, we will describe some of the most common methods for
directly quantifying and evaluating drug synergism (Ma
and
Motsinger-Reif, 2019).

Response surface modeling is an approach based on a 3D plot rep-
resentation to describe the interaction effects in drug combinations.
Basically, doses of drugs A and B are plotted on the x and y-axis and the
expected combined effects (response) are plotted on the z-axis, creating a
3D surface. Synergism or antagonism is measured as deviations from this

surface and depends on the value of z. It allows the use of both Bliss
Independence and Loewe additivity models for the estimation of the
expected effects (Ma and Motsinger-Reif, 2019).

Recently, more user-friendly approaches have gained attention for the
quantiﬁcation of drug interactions. CompuSyn, a computer software
based on the Chou-Talalay theorem, has been developed to make synergy
determination more user-friendly, enhancing the usage of this reference
model for the evaluation of drug interactions in combination studies. To
use this software, raw data must be analyzed and normalized to convert
responses in value between 0 and 1 (Chou, 2010).

Another approach is the Mixlow (i.e. Mixed-effects Loewe) method-
ology, developed by Boik, Newman, and Boik in 2008 (Boik et al., 2008).
This approach is based mainly on three elements: a nonlinear
mixed-effects model for the estimation of the sigmoidal curve parameters
from the concentration-response curves, the Loewe index, and a method
for evaluation of statistical signiﬁcance for the index. It is an improve-
ment of the Chou-Talalay method as it is more accurate in the estimation
of the parameters, includes the evaluation of conﬁdence intervals and
dismisses the need for previous data processing (Boik et al., 2008).

More recently, Hennessey et al. (2010) (Hennessey et al., 2010)
proposed a novel model for the evaluation of dose-response curves and
synergy determination. The Bayesian model uses hierarchical nonlinear
regression to describe the variability between and within experiments
and in the observed responses of the controls. To do so, the authors used
Markov chain Monte Carlo (MCMC) for data ﬁtting and a modiﬁed
version of Loewe additivity to infer about synergism in drug combina-
tions while incorporating variables related to variability and uncertainty
related intrinsically with the experiments. The authors found this
approach to be more precise in drug synergism estimation than the
Chou-Talalay methodology (Hennessey et al., 2010).

5. Oncological preclinical studies based on combination models

The evaluation of synergism in preclinical trials involving in vitro
assays is a common practice and nowadays many in vivo drug combina-
tion studies using animal models are based on the results obtained in
studies using cell lines. We searched the database PubMed using the
terms ‘in vivo’ and ‘synergy’ and ‘cancer’ and limited the results to a
period from 2019 to 2022. The selected studies will next be analyzed to
ﬁnd if in vivo combination studies make correct use of the term synergy
and to evaluate which reference models they employ to assess drug
interactions.

One of the reference papers for the evaluation of drug synergism in in
vivo studies is the one published by Fu et al., in 2016 (Fu et al., 2016),
from the research group led by Ting-Chao Choug. The authors studied the
combination of two anticancer drugs that target microtubule polymeri-
zation: Taxotere and T607 compound. They found these drugs are syn-
ergic against human colon carcinoma HCT-116 xenograft mice. The
authors
the
interactions
median-effect equation of the mass-action law and the CI theorem pro-
posed by Chou-Talalay, demonstrating the basic concepts and experi-
mental design aspects important for the quantitative analysis of drug
interaction dynamics in complex biological systems (Fu et al., 2016).

determine drug

quantitatively

using

A recent study from Skeberdyte (Skeberdyt _e et al., 2020)evaluated
the effect of the combination of salinomycin and dichloroacetate in lung
carcinoma. Salinomycin acts on cancer stem cells and dichloroacetate
inhibits the pyruvate dehydrogenase kinase. The authors performed in
vitro studies using two and three-dimensional cell cultures of Lewis lung
carcinoma (LLC1) cells and also in vivo studies using an LLC1-C57BL/6
mouse model. The authors successfully proved that this drug combina-
tion has synergistic effects in vitro using the Chou-Talalay method by
testing several doses below IC50 from both monotherapies using a
non-constant ratio drug design. The authors also proved this combination
increased the survival rate of mice, reduced metastasis occurrence and
also decreased the population of cancer stem cells, proving the beneﬁts of
this combination both in vitro and in vivo (Skeberdyt _e et al., 2020).

8

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

Another study from Xu et al. (2019) attempted to evaluate the po-
tential of the combination of ABT199 and irinotecan in RAS-mutant lung
cancer cells. The authors selected this in vitro model as KRAS mutation is
very frequent in non-small cancer lung cancer (NSCLC). Irinotecan is one
of the most well-known chemotherapeutic drugs commonly used for
metastatic colorectal cancer and ABT199 is an investigational drug with
high efﬁcacy of the BCL-2 inhibitor. Using different human NSCLC cell
lines (H441, A549, H838 and H522), the authors have successfully
demonstrated that this drug combination inhibits lung cancer cell growth
and enhanced apoptosis, being synergistic with CIs under 0.7. Further in
vivo studies suggests this combination induces tumor size and weight
reduction, demonstrating the potent in vivo efﬁcacy of the combination
(Xu et al., 2019).

Ghosh et al. (2019) recently studied the anticancer effect of the
combination of methylglyoxal, an agent with a well-established anti-
carcinogenic effect and 5-ﬂuorouracil (5-FU), an antineoplastic agent
commonly used for several types of cancer, for breast cancer treatment.
This research group evaluated the effect of this drug combination both in
vitro using MCF-7 breast cancer cells and in vivo and successfully found
synergism using the Chou-Talalay theorem. In vivo studies revealed that
EAC (Ehrlich Ascites Carcinoma) bearing mice and BALB/c mouse 4T1
breast tumor models exhibited tumor regression and fewer side effects
when treated with this combination compared to single agents (Ghosh
et al., 2019).

in three breast cancer cell

Buocikova and her colleagues (Buocikova et al., 2022) recently
studied the combination of the DNA methyltransferase (DNMT) inhibitor
decitabine with the anthracycline antibiotic doxorubicin for breast can-
cer. They ﬁrst evaluated the synergism of sequential decitabine þ
doxorubicin treatment
lines (JIMT-1,
MDA-MB-231 and T-47D) after assessing their inﬂuence on the cyto-
toxicity, genotoxicity, apoptosis, and migration capacity of these cells.
The mathematical framework employed for drug synergism was based on
the Chou-Talalay method using the CI to quantify drug interactions. They
further conﬁrmed these results using an orthotopic xenograft mouse
model, demonstrating the potential of epigenetic drugs in the modulation
of cancer cells’ sensitivity to antineoplastic agents (Buocikova et al.,
2022).

Another study combined Cisplatin-loaded poly(L-glutamic acid)-graft-
methoxy poly(ethylene glycol) complex nanoparticles with different
PD1/PD-L1 inhibitors and evaluated their cytotoxic effect in different
types of cells (LLC, H1299, A549, B16F10, ID8, and U14) and female
C57BL/6 mice. They found this combination to cause tumor PD-L1
overexpression time-dependent in vitro and increased tumor PD-L1 sig-
nals after 72 h of treatment in vivo. Different from the previously
mentioned studies, this work employed the Q value method of Zhengjun
Jin to analyze the synergistic interaction of the combination group for
tumor therapy (in vivo). Taken together, these authors demonstrated the
potential clinical treatment of Cisplatin-loaded poly(L-glutamic acid)-
graft-methoxy poly(ethylene glycol) complex nanoparticles with different
PD1/PD-L1 inhibitors for cancer therapy (Shen et al., 2021).

In another study, the authors attempted to combine gemcitabine, a
deoxycytidine nucleoside analog commonly used for the treatment of
advanced or metastatic pancreatic cancer, with Troxacitabine (Troxa-
tyl™), an unnatural L-nucleoside analog that demonstrates potent anti-
tumor activity. The authors performed in vitro studies using different
pancreatic adenocarcinoma cell lines (AsPC-1, Capan-2, MIA PaCa-2 and
Panc-1)
isobologram and
combination-index methods of Chou and Talalay. The authors then
evaluated the effects of both drugs, alone or combined in nude mice
transplanted with human pancreatic (AsPC-1) tumors and concluded that
both drugs were more than additive at safer doses and schedules, being
potential candidates for further evaluation in patients with advanced
pancreatic cancer (Damaraju et al., 2007).

and evaluated synergism using the

S(cid:1)anchez et al. (2019) recently studied the combination of docetaxel, a
chemotherapeutic agent, and capsaicin, an ingredient of hot chili pep-
pers, for the treatment of prostate cancer. The authors used two prostate

cancer cell lines (LNCaP and PC-3) for the in vitro studies and xenograft
prostate cancer models to further evaluate this combination in vivo. Using
the Chou-Talalay reference model, they found that docetaxel and
capsaicin have synergistic effects in the inhibition of LNCaP and PC-3 cell
growth, reﬂecting a CI under 1 for most of the combinations evaluated in
the work. In vivo results reinforced the synergistic effects of this combi-
nation in the reduction of tumor growth in xenograft prostate cancer
models (S(cid:1)anchez et al., 2019).

Recently, another study aimed to study if the synergism between the
drugs vincristine and irinotecan also extend to eribulin, another micro-
tubule inhibitor for the treatment of childhood solid tumors. The authors
combined vincristine or eribulin with irinotecan and studied their anti-
cancer effect in vitro and xenograft models. CIs were calculated based on
the Bliss model of independence and the Loewe additivity model. They
found the eribulin combination to be very effective in these xenograft
models, but not synergistic in vitro (Robles et al., 2020).

Despite the huge number of publications stating synergism in animal
experiments, what we found is that most papers are not able to really
prove drug synergism in vivo, assuming synergistic interactions based on
the in vitro results and using only one reference model for assessing the
drug interactions (usually the Chou-Talalay theorem). According to Chou
(2010), the quantiﬁcation of synergy in vitro and in animals is based on
the same principles, requiring a minimum of 65 nude mice for accurate
results (Chou, 2010). We believe that, for most of the combination
studies, synergism is only determined in vitro because the determination
in vivo is more expensive, time-consuming and introduces more vari-
ability. Most of the studies then extrapolate the results from in vitro to
animals, “which is a general and separate biomedical problem which is
not expected to be solved by the Chou-Talalay method” (Chou, 2010).

The recent studies from our research group explore the combination
of repurposed drugs and antineoplastic agents for the treatment of breast
and colon cancer, following the experimental design proposed for Chou-
Talalay for the accurate prediction of drug synergism (Duarte et al., 2021,
2022; Duarte and Vale, 2020). Although our results were only performed
in vitro, drug interaction was evaluated using more than one reference
model (usually Loewe, Bliss, HSA, ZIP and Chou-Talalay methods), giv-
ing more support to the obtained results and providing a more robust
basis for further research in animal models or clinical trials.

6. Oncological clinical trials based on preclinical synergism
evaluation

Most clinical trials are often supported by preclinical studies that state
to have found synergistic drug combinations. Although synergism is the
gold standard desired when referring to drug combinations in cancer
therapy, this term is commonly misused, as we previously stated. Another
aspect is that, even if one achieves synergism in a certain combination of
drugs, this does not necessarily mean that the combination will be indeed
useful for cancer therapy. The potential for clinical use of combining
drugs in clinical trials should also be measured by the therapeutic index,
a concept that relates the relative toxicity of an anticancer treatment to its
toxicity in normal tissues, rather than only by the quantiﬁcation of syn-
ergism (Ocana et al., 2012).

A report from 2012 from Ocana et al. (2012) attempted to evaluate if
clinical trials that frequently evaluate drug combinations were well
designed and if they used correctly the term synergy, based on strong
evidence from preclinical studies (Ocana et al., 2012). The authors have
found, at the time, that only 13.6% of the preclinical studies included the
evaluation of synergism based on isobologram analysis and 7.6% based
on the Chou-Talalay method. Regarding preclinical studies involving
animal models, only 39% evaluated the therapeutic index, concluding
that most phase I and II studies did not perform the appropriate back-
ground methods for correctly assessing synergism (Ocana et al., 2012).
Also, a recent paper argues that synergism has not been proved in
most clinical trials, especially those regarding studies that combine
inhibitors with each other and with other
various checkpoint

9

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

antineoplastic drugs (Palmer et al., 2022). This review analyzed thirteen
Phase III clinical trials and found no synergistic interactions, just additive
effects of each therapy, only synergism previously supported in animal
models. Although this is not necessarily a bad thing, it is still not the good
thing that all scientists have been looking at and reﬂects, once again, the
misuse of the term synergism among clinical studies (Palmer et al.,
2022).

Indeed, in a perspective published by Chou in 2010 (Chou, 2010), he
states that it is generally not possible to determine synergism in clinical
trials, based on scientiﬁc, practical and ethical reasons (Chou, 2010) that
we already discussed in section 3. He claims that most clinical trials that
employ the term “synergism” are not well supported by the available
data, especially in studies where only a single dose was tested for a single
drug, mentioning the importance of preclinical evaluation for accurate
and robust results to support clinical trials in humans (Chou, 2010).

Here, we performed a Pubmed search using the same methodology as
described by Ocana et al. (2012). We searched for the terms ‘synergy’ or
‘synergistic’ and ‘cancer’ and limited the search for studies in humans,
clinical trials over the last year (2021–2022). Next, we will mention some
of the most recent clinical trials in oncology that are based on preclinical
studies claiming synergism.

Kang et al. (2022) published the results from a recent randomized,
multicenter, double-blind, placebo-controlled, phase II-III clinical trial
(NCT02746796) for the evaluation of the combination of immune
checkpoint inhibitor nivolumab and oxaliplatin versus placebo plus
oxaliplatin. This combination is intended to be used as ﬁrst-line therapy
for the treatment of patients with HER2-negative, unresectable advanced
or recurrent gastric or gastro-esophageal junction cancer (Kang et al.,
2022). This study was based on previous preclinical studies that sup-
ported the additive or synergistic antitumor effects of the combination of
immune checkpoint inhibitors with oxaliplatin. The authors found that a
combination of nivolumab and oxaliplatin enhanced progression-free
survival but not overall survival and concluded this drug combination
has the potential to be used as a ﬁrst-line treatment for patients with this
type of cancer (Kang et al., 2022).

Jain et al. (2021) recently conducted a single-center, phase II non-
randomized trial (NCT02756897) to study the combination of ibrutinib
and venetoclax in the treatment of chronic lymphocytic leukemia (Jain
et al., 2021). The study is based on preclinical studies that demonstrate
the synergism of Bruton tyrosine kinase inhibitors with the Bcl-2 inhib-
itor venetoclax. The authors found this combination can be advantageous
for previously untreated patients with chronic lymphocytic leukemia
(Jain et al., 2021).

Another study from Cousin et al. (2021) performed a single-arm,
multicentric phase II trial (REGOMUNE) to assess regorafenib plus ave-
lumab for the treatment of patients with microsatellite stable colorectal
cancer, based on previous preclinical results that demonstrated that this
combination is synergic. The authors concluded that regorafenib com-
bined with avelumab successfully modulates antitumor immunity in
some patients with this type of cancer (Cousin et al., 2021).

A phase Ib randomized, open-label, multicenter study studied the
combination of alpelisib with everolimus (cid:7) exemestane in solid tumors.
This study claims to be based on preclinical models that demonstrated a
synergistic effect between and with alpelisib. Everolimus inhibits
mTORC1, alpelisib acts on the phosphatidylinositol 3-kinase catalytic
subunit p110α blockage and exemestane is an antineoplastic drug
already used for cancer therapy. The authors conclude that this combi-
nation is safe, manageable and reversible and the pharmacokinetics of
each drug did not change signiﬁcantly when in combination (Curigliano
et al., 2021).

Another phase I clinical trial (NCT01677559) aimed to combine an
aurora kinase A inhibitor (alisertib) and nab-paclitaxel, a chemothera-
peutic agent, for refractory high-grade neuroendocrine tumors. The au-
thors refer that this trial is based on preclinical studies that have
demonstrated that the combination of alisertib plus paclitaxel is synergic

in rapidly proliferative cancers. Moreover, the authors successfully found
that the proposed combination has is safe, manageable and reversible
and demonstrated promising preliminary efﬁcacy (Lim et al., 2021).

Hong et al. (2021) recently published the results from a phase Ib study
(NCT02124148) where it was evaluated the combination of prexasertib
and samotolisib. Prexasertib is a CHK1 Inhibitor and samotolisib is a dual
PI3K/mTOR inhibitor. This clinical trial is based on previous studies that
demonstrated that prexasertib alone has moderate anticancer activity
and other preclinical data in triple-negative breast cancer cells,
MDA-MB-231 orthotopic xenograft tumors, and TNBC patient-derived
xenograft mouse models that also supported this combination. The au-
thors found this combination to be effective in preclinical models and
preliminary effective, with some degree of toxicity associated (Hong
et al., 2021).

Another phase I, open-label, dose-escalation study was performed by
Amin et al. (2021), for the determination of the maximal tolerated dose
of docetaxel in combination with temsirolimus for the treatment of re-
fractory solid tumors. Temsirolimus selectively inhibits mTOR and
docetaxel is an antineoplastic drug belonging to the class of taxanes. This
trial was based on preclinical results that demonstrated that combination
of taxanes and mTOR inhibitors to be additive or synergic in different
types of cancer cells. The authors found this combination to be very toxic
and not suitable for cancer treatment (Amin et al., 2021).

Taken together, the mentioned clinical trials, which are usually
phases I and II, demonstrate that synergism in preclinical studies is
usually the justiﬁcation for the clinical evaluation of drug combinations
in cancer-related studies, clarifying the importance of the accurate and
reliable drug interaction quantiﬁcation in this type of studies.

7. Conclusions and prospects

Drug combination is a strategy that has been studied extensively over
the last century and its advantages over monotherapy have been recog-
nized by several scientists. Due to the recent advances in the under-
standing of the biological concepts behind several diseases, the interest in
using drug combinations to improve the efﬁcacy of the available thera-
pies has dramatically increased. Over the years, research in this area has
resulted in many theoretical and experimental papers, involving re-
searchers from different disciplines. Despite the different approaches
developed to evaluate the interaction of drugs in combination therapies,
all reference models still present some limitations, and their choice must
be adequate to the available data and type of study (in vitro, in vivo or
clinical trial). Future studies must aim to rigorously apply the models and
concepts herein described for the appropriate interpretation of combi-
nation effects, and, whenever possible, the analysis of drug combinations
may beneﬁt from the cooperative use of different approaches. The use of
the term synergism in animal studies must be carefully employed and
only when the determination of drug synergism was indeed validated
using an appropriate reference model. Synergism in clinical trials should
also be mentioned when there is robust information from previous pre-
further
clinical studies. Also,
research should be always performed in order to elucidate the mecha-
nisms of action by which drugs act both alone and combined, to help
improve the combination experiment design. In silico approaches, such
as PBPK models, can also represent a potential tool for the evaluation of
drug synergism in vivo or in further clinical trials.

in addition to evaluating synergism,

Funding

This research was ﬁnanced by FEDER—Fundo Europeu de Desen-
volvimento Regional funds through the COMPETE 2020—Operational
Programme for Competitiveness and Internationalization (POCI),
Portugal 2020, and by Portuguese funds through Fundaç~ao para a Ci^encia
e a Tecnologia (FCT) in the framework of the project IF/00092/2014/
CP1255/CT0004 and CHAIR in Onco-Innovation.

10

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

CRediT authorship contribution statement

Diana Duarte: Writing – original draft. Nuno Vale: Writing – review

& editing, Supervision.

Declaration of competing interest

The authors declare that they have no known competing ﬁnancial
interests or personal relationships that could have appeared to inﬂuence
the work reported in this paper.

Acknowledgements

This article was supported by National Funds through FCT-Fundaç~ao
para a Ci^encia e a Tecnologia, I.P., within CINTESIS, R&D Unit (Refer-
ence UIDB/4255/2020). Diana Duarte acknowledges FCT for funding her
PhD grant (SFRH/BD/140734/2018).

References

Amin, M., Gao, F., Terrero, G., Picus, J., Wang-Gillam, A., Suresh, R., Ma, C., Tan, B.,

Baggstrom, M., Naughton, M.J., Trull, L., Belanger, S., Fracasso, P.M., Lockhart, A.C.,
2021. Phase I study of docetaxel and temsirolimus in refractory solid tumors. Am. J.
Clin. Oncol. 44 (9), 443–448. https://doi.org/10.1097/COC.0000000000000852.

Berenbaum, M.C., 1989. What is synergy? Pharmacol. Rev. 41 (2), 93–141.
Berenbaum, M.C., 1977. Synergy, additivism and antagonism in immunosuppression. A

critical review. Clin. Exp. Immunol. 28 (1), 1–18.

Bliss, C.I., 1939. The toxicity OF POISONS applied jointly. Ann. Appl. Biol. 26 (3),

585–615. https://doi.org/10.1111/j.1744-7348.1939.tb06990.x.

Boik, J.C., Newman, R.A., Boik, R.J., 2008. Quantifying synergism/antagonism using

nonlinear mixed-effects modeling: a simulation study. Stat. Med. 27 (7), 1040–1061.
https://doi.org/10.1002/SIM.3005.

Borisy, A.A., Elliott, P.J., Hurst, N.W., Lee, M.S., Leh(cid:1)ar, J., Price, E.R., Serbedzija, G.,
Zimmermann, G.R., Foley, M.A., Stockwell, B.R., Keith, C.T., 2003. Systematic
discovery of multicomponent therapeutics. Proc. Natl. Acad. Sci. Unit. States Am. 100
(13), 7977–7982. https://doi.org/10.1073/pnas.1337088100.

Buocikova, V., Longhin, E.M., Pilalis, E., Mastrokalou, C., Miklikova, S., Cihova, M.,

Poturnayova, A., Mackova, K., Babelova, A., Trnkova, L., El Yamani, N., Zheng, C.,
Rios-Mondragon, I., Labudova, M., Csaderova, L., Kuracinova, K.M., Makovicky, P.,
Kucerova, L., Matuskova, M., Cimpan, M.R., Dusinska, M., Babal, P.,
Chatziioannou, A., Gabelova, A., Rund(cid:1)en-Pran, E., Smolkova, B., 2022. Decitabine
potentiates efﬁcacy of doxorubicin in a preclinical trastuzumab-resistant HER2-
positive breast cancer models. January Biomed. Pharmacother. 147, 112662. https://
doi.org/10.1016/j.biopha.2022.112662.

Caudle, R.M., Williams, G.M., 1993. The misuse of analysis of variance to detect synergy
in combination drug studies. Pain 55 (3), 313–317. https://doi.org/10.1016/0304-
3959(93)90006-B.

Chou, T.-C., Talalay, P., 1984. Quantitative analysis of dose-effect relationships: the

combined effects of multiple drugs or enzyme inhibitors. Adv. Enzym. Regul. 22 (C),
27–55. https://doi.org/10.1016/0065-2571(84)90007-4.

Chou, T.-C.T.C., 2006. Theoretical basis, experimental design, and computerized

simulation of synergism and antagonism in drug combination studies. Pharmacol.
Rev. 58 (3), 621–681. https://doi.org/10.1124/pr.58.3.10.

Chou, T.C., 2010. Drug combination studies and their synergy quantiﬁcation using the
chou-talalay method. Cancer Res. 70 (2), 440–446. https://doi.org/10.1158/0008-
5472.CAN-09-1947.

Chou, T.C., Talalay, P., 1983. Analysis of combined drug effects: a new look at a very old
problem. Trends Pharmacol. Sci. 4 (C), 450–454. https://doi.org/10.1016/0165-
6147(83)90490-X.

Cokol, M., Chua, H.N., Tasan, M., Mutlu, B., Weinstein, Z.B., Suzuki, Y., Nergiz, M.E.,

Costanzo, M., Baryshnikova, A., Giaever, G., Nislow, C., Myers, C.L., Andrews, B.J.,
Boone, C., Roth, F.P., 2011. Systematic exploration of synergistic drug pairs. Mol.
Syst. Biol. 7 (1), 544. https://doi.org/10.1038/msb.2011.71.

Cousin, S., Cantarel, C., Guegan, J.-P., Gomez-Roca, C., Metges, J.-P., Adenis, A.,
Pernot, S., Bellera, C., Kind, M., Auzanneau, C., Le Loarer, F., Soubeyran, I.,
Bessede, A., Italiano, A., 2021. Regorafenib-avelumab combination in patients with
microsatellite stable colorectal cancer (REGOMUNE): a single-arm, open-label, phase
II trial. Clin. Cancer Res. 27 (8), 2139–2147. https://doi.org/10.1158/1078-
0432.CCR-20-3416.

Curigliano, G., Martin, M., Jhaveri, K., Beck, J.T., Tortora, G., Fazio, N., Maur, M.,

Hubner, R.A., Lahner, H., Donnet, V., Ajipa, O., Li, Z., Blumenstein, L., Andre, F.,
2021. Alpelisib in combination with everolimus (cid:7) exemestane in solid tumours:
phase Ib randomised, open-label, multicentre study. Eur. J. Cancer 151 49–62.
https://doi.org/10.1016/j.ejca.2021.03.042.

Damaraju, V.L., Bouffard, D.Y., Wong, C.K.W., Clarke, M.L., Mackey, J.R., Leblond, L.,
Cass, C.E., Grey, M., Gourdeau, H., 2007. Synergistic activity of troxacitabine
(TroxatylTM) and gemcitabine in pancreatic cancer. BMC Cancer 7, 1–11. https://
doi.org/10.1186/1471-2407-7-121.

Dear, R.F., McGeechan, K., Jenkins, M.C., Barratt, A., Tattersall, M.H.N., Wilcken, N.,

2013. Combination versus sequential single agent chemotherapy for metastatic breast
cancer. Cochrane Database Syst. Rev. 2021 (3). https://doi.org/10.1002/
14651858.CD008792.pub2.

Di Veroli, G.Y., Fornari, C., Wang, D., Mollard, S., Bramhall, J.L., Richards, F.M.,
Jodrell, D.I., 2016. Combeneﬁt: an interactive platform for the analysis and
visualization of drug combinations. Bioinformatics 32 (18), 2866–2868. https://
doi.org/10.1093/bioinformatics/btw230.

Duarte, D., Cardoso, A., Vale, N., 2021. Synergistic growth inhibition of HT-29 colon and

MCF-7 breast cancer cells with simultaneous and sequential combinations of
antineoplastics and CNS drugs. Int. J. Mol. Sci. 22 (14), 7408. https://doi.org/
10.3390/ijms22147408.

Duarte, D., R^ema, A., Amorim, I., Vale, N., 2022. Drug combinations: a new strategy to
extend drug repurposing and epithelial-mesenchymal transition in breast and colon
cancer cells. Biomolecules 12 (2), 190. https://doi.org/10.3390/biom12020190.

Duarte, D., Vale, N., 2020. New trends for antimalarial drugs: synergism between

antineoplastics and antimalarials on breast cancer cells. Biomolecules 10 (12), 1–20.
https://doi.org/10.3390/biom10121623.

European Medicines Agency Committee for Human Medicinal Products, 2017. Committee
for Human Medicinal Products (CHMP) Guideline on Clinical Development of Fixed
Combination Medicinal Products.

Foucquier, J., Guedj, M., 2015. Analysis of drug combinations: current methodological
landscape. Pharmacol. Res. Perspect. 3 (3), e00149. https://doi.org/10.1002/
prp2.149.

Fu, J., Zhang, N., Chou, J.H., Dong, H.J., Lin, S.F., Ulrich-Merzenich, G.S., Chou, T.C.,

2016. Drug combination in vivo using combination index method: Taxotere and T607
against colon carcinoma HCT-116 xenograft tumor in nude mice. Synergy 3 (3),
15–30. https://doi.org/10.1016/j.synres.2016.06.001.

Geary, N., 2013. Understanding synergy. Am. J. Physiol. Metab. 304 (3), E237–E253.

https://doi.org/10.1152/ajpendo.00308.2012.

Ghosh, S., Pal, A., Ray, M., 2019. Methylglyoxal in combination with 5-Fluorouracil elicits

improved chemosensitivity in breast cancer through apoptosis and cell cycle
inhibition. October 2018 Biomed. Pharmacother. 114, 108855. https://doi.org/
10.1016/j.biopha.2019.108855.

Goldoni, M., Johansson, C., 2007. A mathematical approach to study combined effects of
toxicants in vitro: evaluation of the Bliss independence criterion and the Loewe
additivity model. Toxicol. Vitro 21 (5), 759–769. https://doi.org/10.1016/
j.tiv.2007.03.003.

Grabovsky, Y., Tallarida, R.J., 2004. Isobolographic analysis for combinations of a full

and partial agonist: curved isoboles. J. Pharmacol. Exp. Therapeut. 310 (3), 981–986.
https://doi.org/10.1124/jpet.104.067264.

Greco, W.R., Bravo, G., Parsons, J.C., 1995. The search for synergy: a critical review from

a response surface perspective. Pharmacol. Rev. 47 (2), 331–385.

Hand, D.J., 2000. Synergy in Drug Combinations. Springer, Berlin, Heidelberg,

pp. 471–475. https://doi.org/10.1007/978-3-642-58250-9_38.

Hennessey, V.G., Rosner, G.L., Bast, R.C., Chen, M.Y., 2010. A Bayesian approach to dose-
response assessment and synergy and its application to in vitro dose-response studies.
Biometrics 66 (4), 1275–1283. https://doi.org/10.1111/J.1541-0420.2010.01403.X.
Hong, D.S., Moore, K.N., Bendell, J.C., Karp, D.D., Wang, J.S., Ulahannan, S.V., Jones, S.,
Wu, W., Donoho, G.P., Ding, Y., Capen, A., Wang, X., Bence Lin, A., Patel, M.R., 2021.
Preclinical evaluation and phase Ib study of prexasertib, a CHK1 inhibitor, and
samotolisib (LY3023414), a dual PI3K/mTOR inhibitor. Clin. Cancer Res. 27 (7),
1864–1874. https://doi.org/10.1158/1078-0432.CCR-20-3242.

Jain, N., Keating, M., Thompson, P., Ferrajoli, A., Burger, J.A., Borthakur, G.,
Takahashi, K., Estrov, Z., Sasaki, K., Fowler, N., Kadia, T., Konopleva, M.,
Alvarado, Y., Yilmaz, M., DiNardo, C., Bose, P., Ohanian, M., Pemmaraju, N.,
Jabbour, E., Kanagal-Shamanna, R., Patel, K., Wang, W., Jorgensen, J., Wang, S.A.,
Garg, N., Wang, X., Wei, C., Cruz, N., Ayala, A., Plunkett, W., Kantarjian, H.,
Gandhi, V., Wierda, W.G., 2021. Ibrutinib plus venetoclax for ﬁrst-line treatment of
chronic lymphocytic leukemia. JAMA Oncol. 7 (8), 1213. https://doi.org/10.1001/
jamaoncol.2021.1649.

Kang, Y.-K., Chen, L.-T., Ryu, M.-H., Oh, D.-Y., Oh, S.C., Chung, H.C., Lee, K.-W.,
Omori, T., Shitara, K., Sakuramoto, S., Chung, I.-J., Yamaguchi, K., Kato, K.,
Sym, S.J., Kadowaki, S., Tsuji, K., Chen, J.-S., Bai, L.-Y., Oh, S.-Y., Choda, Y.,
Yasui, H., Takeuchi, K., Hirashima, Y., Hagihara, S., Boku, N., 2022. Nivolumab plus
chemotherapy versus placebo plus chemotherapy in patients with HER2-negative,
untreated, unresectable advanced or recurrent gastric or gastro-oesophageal junction
cancer (ATTRACTION-4): a randomised, multicentre, double-blind, placebo-contr.
Lancet Oncol. 23 (2), 234–247. https://doi.org/10.1016/S1470-2045(21)00692-6.

Keith, C.T., Borisy, A.A., Stockwell, B.R., 2005. Multicomponent therapeutics for

networked systems. Nat. Rev. Drug Discov. 4 (1), 71–78. https://doi.org/10.1038/
NRD1609.

Kim, H., Lee, S.J., Lee, I.K., Min, S.C., Sung, H.H., Jeong, B.C., Lee, J., Park, S.H., 2020.
Synergistic effects of combination therapy with akt and mtor inhibitors on bladder
cancer cells. Int. J. Mol. Sci. 21 (8), 1–12. https://doi.org/10.3390/ijms21082825.
Klimaszewska-Wi(cid:1)sniewska, A., Hałas-Wi(cid:1)sniewska, M., Grzanka, A., Grzanka, D., 2018.
Evaluation of anti-metastatic potential of the combination of ﬁsetin with paclitaxel
on a549 non-small cell lung cancer cells. Int. J. Mol. Sci. 19 (3), 1–18. https://
doi.org/10.3390/ijms19030661.

Lambert, R.J.W., Dawson, D.A., 2019. New models for the time dependent toxicity of

individual and combined toxicants. Toxicol. Res. (Camb). 8 (4), 509. https://doi.org/
10.1039/C9TX00005D.

Lederer, S., Dijkstra, T.M.H., Heskes, T., 2019. Additive dose response models: deﬁning

synergy. November Front. Pharmacol. 10, 1–15. https://doi.org/10.3389/
fphar.2019.01384.

11

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

Lee, J.O., Kang, M.J., Byun, W.S., Kim, S.J.S.A., Seo, I.H., Han, J.A., Moon, J.W.,

Kim, J.H., Kim, S.J.S.A., Lee, E.J., In Park, S., Park, S.H., Kim, H.S., 2019. Metformin
overcomes resistance to cisplatin in triple-negative breast cancer (TNBC) cells by
targeting RAD51. Breast Cancer Res. 21 (1), 1–18. https://doi.org/10.1186/s13058-
019-1204-2.

Leh(cid:1)ar, J., Krueger, A.S., Avery, W., Heilbut, A.M., Johansen, L.M., Price, E.R.,

Rickles, R.J., Short, G.F., Staunton, J.E., Jin, X., Lee, M.S., Zimmermann, G.R.,
Borisy, A.A., 2009. Synergistic drug combinations tend to improve therapeutically
relevant selectivity. Nat. Biotechnol. 27 (7), 659–666. https://doi.org/10.1038/
NBT.1549.

Leh(cid:1)ar, J., Zimmermann, G.R., Krueger, A.S., Molnar, R.A., Ledell, J.T., Heilbut, A.M.,

Short, G.F., Giusti, L.C., Nolan, G.P., Magid, O.A., Lee, M.S., Borisy, A.A.,
Stockwell, B.R., Keith, C.T., 2007. Chemical combination effects predict connectivity
in biological systems. Mol. Syst. Biol. 3 (1), 80. https://doi.org/10.1038/
msb4100116.

Lim, K.-H., Opyrchal, M., Acharya, A., Boice, N., Wu, N., Gao, F., Webster, J.,

Lockhart, A.C., Waqar, S.N., Govindan, R., Morgensztern, D., Picus, J., Tan, B.R.,
Baggstrom, M.Q., Maher, C.A., Wang-Gillam, A., 2021. Phase 1 study combining
alisertib with nab-paclitaxel in patients with advanced solid malignancies. Eur. J.
Cancer 154, 102–110. https://doi.org/10.1016/j.ejca.2021.06.012.

Loewe, S., 1927. Die Mischarznei - versuch einer allgemeinen Pharmakologie der
Arzneikombinationen. Klin. Wochenschr. 6 (23), 1077–1085. https://doi.org/
10.1007/BF01890305.

Loewe, S., 1953. The problem of synergism and antagonism of combined drugs.

Arzneimittelforschung 3 (6), 285–290.

combined with irinotecan for treatment of pediatric cancer xenografts. Clin. Cancer
Res. 26 (12), 3012–3023. https://doi.org/10.1158/1078-0432.CCR-19-1822.
Rodea-Palomares, I., Gonz(cid:1)alez-Pleiter, M., Martín-Betancor, K., Rosal, R., Fern(cid:1)andez-

Pi~nas, F., 2015. Additivity and interactions in ecotoxicity of pollutant mixtures: Some
Patterns, Conclusions, and open questions. Toxics 3 (4), 342–369. https://doi.org/
10.3390/TOXICS3040342.

Roell, K.R., Reif, D.M., Motsinger-Reif, A.A., 2017. An introduction to terminology and
methodology of chemical synergy—perspectives from across disciplines. Front.
Pharmacol. 8. https://doi.org/10.3389/fphar.2017.00158.

Saleh, J.A., 2008. Combination therapy in asthma: a review. Niger. J. Med. 17 (3),

238–243. https://doi.org/10.4314/NJM.V17I3.37377.

S(cid:1)anchez, B.G., Bort, A., Mateos-G(cid:1)omez, P.A., Rodríguez-Henche, N., Díaz-Laviada, I.,
2019. Combination of the natural product capsaicin and docetaxel synergistically
kills human prostate cancer cells through the metabolic regulator AMP-activated
kinases. Cancer Cell Int. 19 (1), 1–14. https://doi.org/10.1186/s12935-019-0769-2.

Sasaki, K., Tsuno, N.H., Sunami, E., Tsurita, G., Kawai, K., Okaji, Y., Nishikawa, T.,
Shuno, Y., Hongo, K., Hiyoshi, M., Kaneko, M., Kitayama, J., Takahashi, K.,
Nagawa, H., 2010. Chloroquine potentiates the anti-cancer effect of 5-ﬂuorouracil on
colon cancer cells. July 2010 BMC Cancer 10, 370. https://doi.org/10.1186/1471-
2407-10-370.

Schindler, M., 2017. Theory of synergistic effects: Hill-type response surfaces as “null-
interaction” models for mixtures. Theor. Biol. Med. Model. 14 (1), 1–16. https://
doi.org/10.1186/s12976-017-0060-y.

Shafer, S.L., 2012. All models are wrong. Anesthesiology 116 (2), 240–241. https://

doi.org/10.1097/ALN.0B013E318242A4A7.

Loewe, S., Muischnek, H., 1926. Über kombinationswirkungen - mitteilung: Hilfsmittel
der Fragestellung. Arch. für Exp. Pathol. und Pharmakologie 114 (5–6), 313–326.
https://doi.org/10.1007/BF01952257.

Shen, N., Yang, C., Zhang, X., Tang, Z., Chen, X., 2021. Cisplatin nanoparticles possess

stronger anti-tumor synergy with PD1/PD-L1 inhibitors than the parental drug. Acta
Biomater. 135, 543–555. https://doi.org/10.1016/j.actbio.2021.08.013.

Ma, J., Motsinger-Reif, A., 2019. Current methods for quantifying drug synergism.

Sidorov, P., Naulaerts, S., Ariey-Bonnet, J., Pasquier, E., Ballester, P.J., 2019. Predicting

Proteomics bioinforma. Curr. Res. 1 (2), 43–48.

Meyer, C.T., Wooten, D.J., Paudel, B.B., Bauer, J., Hardeman, K.N., Westover, D.,

Lovly, C.M., Harris, L.A., Tyson, D.R., Quaranta, V., 2019. Quantifying drug
combination synergy along potency and efﬁcacy axes. Cell Syst 8 (2), 97–108.
https://doi.org/10.1016/j.cels.2019.01.003 e16.

Moreno, S., Perno, C.F., Mallon, P.W., Behrens, G., Corbeau, P., Routy, J.P., Darcis, G.,
2019. Two-drug vs. three-drug combinations for HIV-1: do we have enough data to
make the switch? HIV Med. 20 2–2012. https://doi.org/10.1111/HIV.12716.
National Cancer Institute, 2019. Immunotherapy for cancer - National cancer Institute
[WWW Document] Natl. Cancer Inst. URL https://www.cancer.gov/about-cancer/
treatment/types/immunotherapy accessed 3.18.22.

synergism of cancer drug combinations using NCI-ALMANAC data. Front. Chem. 7
(July), 1–13. https://doi.org/10.3389/fchem.2019.00509.

Sinzger, M., Vanhoefer, J., Loos, C., Hasenauer, J., 2019. Comparison of null models for
combination drug therapy reveals Hand model as biochemically most plausible. Sci.
Rep. 9 (1), 1–15. https://doi.org/10.1038/s41598-019-38907-x.

Skeberdyt _e, A., Sarapinien _e, I., Krasko, J.A., Barakauskien _e, A., (cid:3)Zilionyt _e, K.,

Prokarenkait _e, R., Su(cid:3)zied _elis, K., Bukelskien _e, V., Jarmalait _e, S., 2020. Salinomycin
and dichloroacetate synergistically inhibit Lewis lung carcinoma cell proliferation,
tumor growth and metastasis. Biochem. Biophys. Res. Commun. 523 (4), 874–879.
https://doi.org/10.1016/j.bbrc.2019.12.107.

Slinker, B.K., 1998. The statistics of synergism. J. Mol. Cell. Cardiol. 30 (4), 723–731.

National Cancer Institute, 2015a. Types of cancer treatment - National cancer Institute

https://doi.org/10.1006/JMCC.1998.0655.

[WWW Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/about-cancer/t
reatment/types. accessed 3.18.22.

National Cancer Institute, 2015b. Chemotherapy to treat cancer - National cancer

Institute [WWW Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/about
-cancer/treatment/types/chemotherapy. accessed 3.18.22.

National Cancer Institute, 2015c. Hormone therapy for cancer - National cancer Institute
[WWW Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/about-cancer/tr
eatment/types/hormone-therapy. accessed 3.18.22.

National Cancer Institute, 2015d. Surgery for cancer - National cancer Institute [WWW
Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/about-cancer/treatme
nt/types/surgery. accessed 3.18.22.

National Cancer Institute, 2015e. Hyperthermia to treat cancer - National cancer Institute
[WWW Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/about-cancer/tr
eatment/types/hyperthermia. accessed 3.18.22.

National Cancer Institute, 2015f. Photodynamic therapy to treat cancer - National cancer
Institute [WWW Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/about
-cancer/treatment/types/photodynamic-therapy. accessed 3.18.22.

National Cancer Institute, 2015g. Stem cell transplants in cancer treatment - National

cancer Institute [WWW Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/
about-cancer/treatment/types/stem-cell-transplant. accessed 3.18.22.

National Cancer Institute, 2014. Targeted therapy for cancer - National cancer Institute
[WWW Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/about-cancer/t
reatment/types/targeted-therapies. accessed 3.18.22.

National Cancer Institute, 2010. Radiation therapy for cancer - National cancer Institute
[WWW Document]. Natl. Cancer Inst. URL. https://www.cancer.gov/about-cance
r/treatment/types/radiation-therapy. accessed 3.18.22.

Nieuwenhuis, S., Forstmann, B.U., Wagenmakers, E.J., 2011. Erroneous analyses of
interactions in neuroscience: a problem of signiﬁcance. Nat. Neurosci. 14 (9),
1105–1107. https://doi.org/10.1038/NN.2886.

Ocana, A., Amir, E., Yeung, C., Seruga, B., Tannock, I.F., 2012. How valid are claims for
synergy in published clinical studies? Ann. Oncol. 23 (8), 2161–2166. https://
doi.org/10.1093/annonc/mdr608.

Palmer, A.C., Izar, B., Hwangbo, H., Sorger, P.K., 2022. Predictable clinical beneﬁts
without evidence of synergy in trials of combination therapies with immune-
checkpoint inhibitors. Clin. Cancer Res. 28 (2), 368–377. https://doi.org/10.1158/
1078-0432.CCR-21-2275.

Podolsky, S.H., Greene, J.A., 2011. Combination drugs — Hype, Harm, and Hope. N. Engl.

J. Med. 365 (6), 488–491. https://doi.org/10.1056/NEJMp1106161.

Ram, R., 2019. Extrapolation of animal research data to humans: an analysis of the

evidence. In: Animal Experimentation: Working towards a Paradigm Change. BRILL,
pp. 341–375. https://doi.org/10.1163/9789004391192_016.

Robles, A.J., Kurmasheva, R.T., Bandyopadhyay, A., Phelps, D.A., Erickson, S.W., Lai, Z.,
Kurmashev, D., Chen, Y., Smith, M.A., Houghton, P.J., 2020. Evaluation of eribulin

Smalley, K.S.M., Haass, N.K., Brafford, P.A., Lioni, M., Flaherty, K.T., Herlyn, M., 2006.

Multiple signaling pathways must be targeted to overcome drug resistance in cell
lines derived from melanoma metastases. Mol. Cancer Therapeut. 5 (5), 1136–1144.
https://doi.org/10.1158/1535-7163.MCT-06-0084.

Tallarida, R.J., 2012. Revisiting the isobole and related quantitative methods for assessing
drug synergism. J. Pharmacol. Exp. Therapeut. 342 (1), 2–8. https://doi.org/
10.1124/jpet.112.193474.

Tang, J., Wennerberg, K., Aittokallio, T., 2015. What is synergy? The Saariselkï¿½
agreement revisited. Front. Pharmacol. 6 (SEP), 1–5. https://doi.org/10.3389/
fphar.2015.00181.

Twarog, N.R., Stewart, E., Hammill, C.V., Shelat, A.A., 2016. BRAID: a unifying paradigm
for the analysis of combined drug action. Sci. Rep. 6 (1), 25523. https://doi.org/
10.1038/srep25523.

US FDA, 2013. Guidance for industry: codevelopment of two or more new investigational

drugs for use in combination. Fda (1), 1–5.

Vakil, V., Trappe, W., 2019. Drug combinations: mathematical modeling and networking

methods. Pharmaceutics 11 (5), 1–31. https://doi.org/10.3390/
pharmaceutics11050208.

Vlot, A.H.C., Aniceto, N., Menden, M.P., Ulrich-Merzenich, G., Bender, A., 2019. Applying
synergy metrics to combination screening data: agreements, disagreements and
pitfalls. Drug Discov. Today 24 (12), 2286–2298. https://doi.org/10.1016/
j.drudis.2019.09.002.

Webster, R.M., 2016. Combination therapies in oncology. Nat. Rev. Drug Discov. 15 (2),

81–82. https://doi.org/10.1038/nrd.2016.3.

Wientjes, M.G., 2010. Comparison of methods for evaluating drug-drug interaction. Front.

Biosci. E2 (1), 86. https://doi.org/10.2741/e86.

Woodcock, J., Grifﬁn, J.P., Behrman, R.E., 2011. Development of novel combination

therapies. N. Engl. J. Med. 364 (11), 985–987. https://doi.org/10.1056/
NEJMp1101548.

World Health Organization, 2005. Annex 5 Guidelines for registration of ﬁxed-dose. WHO

Tech. Rep. Ser. (929), 94–142.

Xu, Y., Zong, S., Gao, X., Zhang, H., Wang, B., Li, P., Liu, T., Li, S., 2019. Combined
treatment of ABT199 and irinotecan suppresses KRAS-mutant lung cancer cells.
October 2018 Gene 688, 1–6. https://doi.org/10.1016/j.gene.2018.11.018.

Yadav, B., Wennerberg, K., Aittokallio, T., Tang, J., 2015. Searching for drug synergy in
complex dose–response landscapes using an interaction potency model. Comput.
Struct. Biotechnol. J. 13, 504–513. https://doi.org/10.1016/j.csbj.2015.09.001.
Zhao, L., Wientjes, M.G., Au, J.L.S., 2004. Evaluation of combination chemotherapy. Clin.
Cancer Res. 10 (23), 7994–8004. https://doi.org/10.1158/1078-0432.CCR-04-1087.

Zhao, W., Sachsenmeier, K., Zhang, L., Sult, E., Hollingsworth, R.E., Yang, H., 2014.

A new Bliss independence model to analyze drug combination data. J. Biomol. Screen
19 (5), 817–821. https://doi.org/10.1177/1087057114521867.

12

D. Duarte, N. Vale

Current Research in Pharmacology and Drug Discovery 3 (2022) 100110

Zheng, S., Wang, W., Aldahdooh, J., Malyutina, A., Shadbahr, T., Tanoli, Z., Pessia, A.,
Tang, J., 2022. SynergyFinder plus: toward better interpretation and annotation of
drug combination screening datasets. Genomics. Proteomics Bioinformatics. https://
doi.org/10.1016/j.gpb.2022.01.004.

Zimmer, A., Katzir, I., Dekel, E., Mayo, A.E., Alon, U., 2016. Prediction of

multidimensional drug dose responses based on measurements of drug pairs. Proc.

Natl. Acad. Sci. U. S. A 113 (37), 10442–10447. https://doi.org/10.1073/
PNAS.1606301113.

Zimmermann, G.R., Leh(cid:1)ar, J., Keith, C.T., 2007. Multi-target therapeutics: when the
whole is greater than the sum of the parts. Drug Discov. Today 12 (1–2), 34–42.
https://doi.org/10.1016/j.drudis.2006.11.008.

13
