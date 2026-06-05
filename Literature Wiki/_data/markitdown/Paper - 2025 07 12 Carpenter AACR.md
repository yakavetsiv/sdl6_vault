---
tags:
  - literature
  - type/paper
  - lit/ai-methods
type: literature-note
source_note: "Papers/Paper - 2025 07 12 Carpenter AACR.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/2025_07_12_Carpenter_AACR.pdf"
converter: "microsoft/markitdown"
---
at Harvard and MIT

Accelerating oncology drug discovery
with the power of microscopy and AI

Anne E. Carpenter, PhD
Carpenter–Singh lab

IMAGING
PLATFORM

🟦

@DrAnneCarpenter
@shantanuXsingh

Download PDF of slides here: http://broad.io/CarpenterSlides
       (talk content is non-conﬁdential)

Give feedback on this talk: http://broad.io/CarpenterFeedback

Kari Herrington, PhD (kah-sage.com)

AI is getting better at some tasks faster than others

IMAGING
PLATFORM

Replication

Transcription

Translation

DNA
(genome)

mRNA
(transcriptome)

Protein
(proteome)

It’s… messy

Connecting proteins to diseases:
྾ There are not simple rules we can follow.
྾ There's not enough direct data to train on.
྾ We cannot experiment on humans

Cell phenotypes

?

Disease
phenotypes

Protein structure

྾ ྾

྾

྾

A revolution in how we use images

IMAGING
PLATFORM

    Measure known

phenotypes

    Profile to characterize
       samples

High-content screening

Image-based profiling
(using the Cell Painting assay)

Extracting features from images

IMAGING
PLATFORM

Sample prep

Microscopy

Image analysis:
Segmentation

100’s of
384-well plates

1000’s of images/ plate;
~5 channels/image

~500 cells/ image

Measure everything
Counts, Shapes, Sizes, Intensities, Textures, Correlations, Relationships

thousands of features / cell

60-80% of “high-content” studies use

only 1 or 2 cellular features

Singh, et al. J Biomol Screen, 2014

Impact of machine learning on image analysis

IMAGING
PLATFORM

Cited in 2,400+ papers per year, 20,000+ total

New! Deep learning for phenotype classification

Online Q&A: 31,000+ posts/year

Beth Cimini’s lab,
Broad Institute

Caicedo and Cimini, Roadmap on Deep Learning for Microscopy arxiv 2023; Lucas et al. Open-source deep-learning software for bioimage segmentation. Mol Bio Cell 2021

Measure everything

Counts, Shapes, Sizes, Intensities,

Textures, Correlations, Relationships

~1500 features / cell

Impact on patients: successful clinical trials

IMAGING
PLATFORM

Alisertib for
Myeloﬁbrosis

Leukemias &
Lymphomas

Crispino lab
(Gangat et al. Clin Cancer
Research 2019)

Vienna hospitals + ETH Zurich
(Snijder B et al. Lancet Haematology 2017;
Kornauth et al. Cancer Discovery 2022)

A revolution in how we use images

IMAGING
PLATFORM

    Measure known

phenotypes

    Profile to characterize
       samples

Image-based screening
(High-content screening)

Image-based profiling
(using the Cell Painting assay)

Beth Cimini lab

Carpenter–Singh lab

IMAGING
PLATFORM

What if a diseased cell
could tell us
what’s wrong with it?

Images often faithfully report on diseases

IMAGING
PLATFORM

Nucleus

ER

Wikipedia

Nucleoli/cyto RNA

Actin/Golgi/PM

Singh & Kisku, IEEE ISED 2018 eLife
DB from Ferry, et al. 2014

Mitochondria

The Cell Painting assay

Image-based proﬁling: use images to create signatures of
genes, compounds and diseases

IMAGING
PLATFORM

Cell Painting
assay
(6 dyes)

image
analysis

s
l
l

e
c
0
0
0
1
>

,

>1,000 features

Profile 1

Profile 2

Profile 3

Gustafsdottir, et al. PLOS ONE 2013
Bray, et al. Nature Protocols 2016
Cimini, et al. Nature Protocols 2023

measure
similarities/connections
to link drugs to genes to
disease states
and to predict assay
outcomes

Perturbation 1

Perturbation 2

Perturbation 3

“So genocentric
has modern biology become
that we have forgotten that the real units
of function and structure in an organism
are cells and not genes.”

—Sydney Brenner (2002)

Kari Herrington, PhD
(kah-sage.com)

IMAGING
PLATFORM

IMAGING
PLATFORM

Cell Painting compares favorably to mRNA proﬁling (and 10-1000x cheaper)

Identify chemical

regulators of pathways

“query” signature of

a gene

Cluster compounds
by mechanism

mRNA
images
both
only
only
(24%)
(27%)
(20%)

Database of

compounds

Effective compounds were conﬁrmed

for 3 out of 7 genes tested;

Identiﬁed 2 sarcoma therapeutic leads

Rohban, et al. Cell Systems 2022

neither
(30%)

44% of mechanism classes
were self-similar using images
(93 of 210 tested)

Way, Natoli, Adeboye, et al., Cell Systems 2022

Predict compounds’
activities in diverse assays

chem.
structures
(16)

mRNA
profiles
(19)

morphology
profiles (28)

Accurate activity
predictions for 5-10% of assays run
at the Broad;
60- and 250-fold increase in hit
rate at Janssen

Moshkov, et al. Nat Comm 2023
Simm, et al. Cell Chem Bio 2018

Predict compound

library diversity
55%

35
36
35% 36%
%
%

44%

structures
mRNA proﬁles
morph proﬁles
random

Improved hit rate
50% increase vs randomly
chosen compounds

Wawer, et al. PNAS 2014

Robots to the rescue!

IMAGING
PLATFORM

Assay

Small molecule library

Can we speed up individual steps
using automation, clever biotech, AI?

Hits     leads

Can we surpass human capabilities?

INPUT

OUTPUT

diseased cell lines, genes

screenable disease phenotype

gene/disease phenotype

chemical regulators

compound

target information (genes or

annotated compounds)

compound variants

SAR information

genes

gene variants

genes with similar function

variant impact information

Preclinical studies
Clinical trials

Effective drug

Transforming drug discovery via image-based proﬁling

IMAGING
PLATFORM

Assay

Can we identify signatures of disease?
Then screen drugs to reverse the signature?

Small molecule library

Hits     leads

Preclinical studies
Clinical trials

Effective drug

Healthy

Disease + drug?

Disease

Image-based proﬁling can identify hallmarks of disease…
and drugs to reverse them

IMAGING
PLATFORM

+ drug?

Healthy

Disease (CCM knockdown)

VE Cadherin
Actin
DNA

 Gibson, et al. Circulation 2015

 Disclosure: Anne
Carpenter serves on
Recursion’s Scientific
Advisory Board

Obesity example: metabolic disorders

IMAGING
PLATFORM

Melina Claussnitzer lab  -   Laber et al. Cell Genomics 2023 and Glunk, et al. Nat Metabolism 2023

Neuro example: psychosis

IMAGING
PLATFORM

Step 1: Identify unhealthy morphology change

(less mitochondrial dispersion)

Healthy person

Bipolar patient

Step 2: Test drugs to reverse the unhealthy morphology

Bruce Cohen lab (in progress) and Ralda Nehme lab - Tegtmeyer et al. (in press) Nature Communications

Rare disease examples

IMAGING
PLATFORM

Healthy

Diseased

3,500 human
genetic variants
tested

250 disease
phenotypes
discovered

Mikko Taipale lab (Lacoste, et al. Cell 2024)

NIH IGVF Consortium: test
80,000 new variants

VISTA Consortium: screen
~500 drugs x ~100 diseases

Cancer Example: Drug susceptibility
Determine drug susceptibility for individual patients’ tumor cells

Treat patient tumor cells with
various drugs & combinations

. . .

. . . . . . . . . . . .

Morphological
changes within
24 hours?

Cell
death at
2 weeks

Morphological changes inherent,
prior to treatment, that indicate
susceptibility or resistance?

Kelley, et al. eLife 2023

IMAGING
PLATFORM

Beth Cimini

Gregory Way

Tarun Kapoor
Rockefeller U

Adi Berman

Megan Kelley

Niklas Rindtorff

Jesse Boehm,

Broad Institute

Cancer Example: rapid virtual screening

IMAGING
PLATFORM

Control
(no perturbation)

YAP1 gene
suppressed
(Hippo pathway)

t

h
w
o
r
g

l
l

e
c
a
m
o
c
r
a
S

→ Founded SyzOnc to pursue

Do any
chemical-perturbation
images in our database
match?

Retrospective evaluation:
32% success rate finding correct matches

Prospective testing:
>42% success rate finding compounds that
work (7 pathways)

Karin Eisinger lab - Rohban et al. Cell Systems 2022

Test it on already-known gene-compound pairs:

20 genes out of 63 tested (32%) had correct compounds in the top

1% of the list (p = 0.026)

Karin Eisinger,
U Penn

Ashley
Fuller

Transforming drug discovery via Cell Painting

IMAGING
PLATFORM

Assay

Can we identify gene/allele
functions by grouping similar
genes and alleles?

Small molecule library

Hits     leads

Preclinical studies
Clinical trials

Effective drug

Genes cluster based on
morphological proﬁle similarity

IMAGING
PLATFORM

HeLa (baseline)

            Whole genome CRISPR knockouts: pooled

Cell Painting

      Bar coding

         Image analysis

           Cluster morphological profiles

Proteins in

the same

complex

(CORUM)

Broad Imaging
Platform
Beth Cimini
Erin Weisbart
Greg Way
Marzieh Haghighi
Shantanu Singh
Anne Carpenter

Claussnitzer Lab/Novo
Nordisk Foundation
Melina Claussnitzer
Thiago Batista
Joaquín Pérez-Schindler

Jan Lab
John Yong
Calvin Jan

Ramezani*, Weisbart*, Bauman*, Singh*, et al. Nat Methods 2025

JT Neal Lab
Meraj Ramezani
Maria Lozada
Julia Bauman
Celeste Diaz
Sanam Kavari

Blainey Lab
Avtar Singh
Paul Blainey

Proteins that

physically

interact

(STRING)

JUMP-Cell Painting Consortium dataset is now available

IMAGING
PLATFORM

(Joint Undertaking for Morphological Proﬁling)

⁌  13,000 overexpressed genes
⁌  8,000 CRISPR knockdowns
⁌  116,000 (+ 30,000) small molecules
5 replicates each in human U2OS cells
1.6 billion single cells
2,378 plates (384 well) = 913,152 wells
200 TB of images, similar amount of extracted features

Partners:
- Broad Institute
- Amgen
- AstraZeneca
- Bayer
- Biogen
- Eisai

- Janssen
- Ksilink
- Merck Healthcare
KGaA (Germany)
- Pﬁzer
- Servier
- Takeda

Supporting Partners:
- Nomic bio
- PerkinElmer
- Verily
- Google Research
- Horizon Discovery
- Ardigen

Collaborators:
- Pistoia Alliance
- Umea University
- Stanford University

JUMP Hub to access the data, exploration
tools, and learn more:
http://broad.io/jump

Data Storage at the Cell Painting Gallery supported by
the AWS Open Data Sponsorship Program

Chandrasekaran  et al. Biorxiv; Accepted Nat Methods 2025

JUMPrr exploration tools now online!

IMAGING
PLATFORM

Try them yourself:
broad.io/jump →  “JUMPrr tools”

For any gene or chemical
perturbation:

⁌ How do the cells look?
⁌ Which other profiles
are the most similar?
⁌ Which are its most
distinctive morphological
features?

Transforming drug discovery via Cell Painting

IMAGING
PLATFORM

Assay

Small molecule library

Hits     leads

Preclinical studies
Clinical trials

Predict drug response for
particular patients

Effective drug

L1000

Variants of unknown signiﬁcance are a growing problem

IMAGING
PLATFORM

“Your cancer sequencing results are in!
Your tumor has a ____ mutation in the
BRAF gene.”

“So what does that mean?”

“I’ve no idea.”

Source unknown

Morphological proﬁling characterizes alleles

IMAGING
PLATFORM

Overexpress 353 alleles
found in lung cancer

Cell Painting

Image
analysis

Cluster
morphological
profiles

82% of alleles have a phenotype

Genes in known pathways cluster

Alleles cluster by gain of function/loss of function

Caicedo et al. CVPR 2018
Caicedo et al. Mol Bio Cell 2022  -  http://broad.io/cmvip

Mohammad
Rohban

Juan Caicedo

Shantanu Singh

Jesse Boehm

Xiaoyun Wu

Angela Brooks

Alice Berger

Matthew
Meyerson

Image-based proﬁling characterizes alleles

IMAGING
PLATFORM

Overexpress BRAF alleles
found in lung cancer

Cell Painting correlations
between pairs of alleles

Cell Painting

Image
analysis

Cluster
morphological
profiles

These are not
constitutively
activating mutants

Mohammad
Rohban

Juan Caicedo

Shantanu Singh

Jesse Boehm

1.0

0.4

-0.2

Xiaoyun Wu

Angela Brooks

CTNNB1

KEAP1

EGFR

STK11

Caicedo et al. Mol Bio Cell 2022  -  http://broad.io/cmvip

Alice Berger

Matthew
Meyerson

Image-based
proﬁling:
accelerating
many steps of
drug discovery

(Rohban eLife 2017,
Chandrasekaran Nat
Methods 2025, Ramezani
Nat Methods 2025)

(Gibson Circulation 2015; Lacoste,
Haghighi et al. Cell 2024)

IMAGING
PLATFORM

Can we speed up individual steps
using automation, clever biotech, AI?

(Simm Cell Chem Bio 2018,
Rohban Cell Systems 2022)

Can we surpass human capabilities?

Applications reviewed in: Chandrasekaran,
et al. Nat Reviews Drug Discovery (2020);
Seal, et al. Nature Methods (2024)

Best practices reviewed in:  Caicedo, et al.
Nature Methods (2017)

Annual conferences: CytoData, SBI2

(Gustafsdottir PLOS One 2013, Ljosa
JBS 2013, Way Cell Systems 2022)

off-target effects,

(Nyffeler Tox Appl Pharmacol 2019
& 2020, Nyffeler SLAS Discov
2021, Willis SLAS Discov 2020,
Way MBoC 2021, Trapotsi Biorxiv
2022)

(Wawer PNAS 2014)

(Gerry JACS 2016, Nelson Org Letters
2016, Melillo JACS 2018)

(Kornauth Cancer Discovery
2022, Caicedo MBoC 2022)

Download PDF of slides here: http://broad.io/CarpenterSlides

Robots to the rescue!

IMAGING
PLATFORM

Assay

Small molecule library

Can we speed up individual steps
using automation, clever biotech, AI?

Hits     leads

Can we surpass human capabilities?

INPUT

OUTPUT

diseased cell lines, genes

screenable disease phenotype

gene/disease phenotype

chemical regulators

compound

target information (genes or

annotated compounds)

compound variants

SAR information

genes

gene variants

genes with similar function

variant impact information

Preclinical studies
Clinical trials

Effective drug

Gratitude

IMAGING
PLATFORM

Biologist wanting to learn image analysis?

Join our Postdoctoral Training Program in

Bioimage Analysis

Anne Carpenter
Shantanu Singh

Johan Fredin-Haslum
Alexandr Kalinin
Ksenija Krasina
Ankur Kumar
Alán Fernando Muñoz González
Runxi Shen

Many thanks to our
many collaborators,
especially in Beth
Cimini’s lab!

Recent major funding for this work provided by:
• NIH NIGMS P41 GM135019
• NIH NIGMS R35 GM122547 MIRA
• Mass Life Sci Center

Disclosure:  We receive honoraria for talks at various companies and
serve as scientific advisors or founders for:
- Anne: Recursion, SyzOnc, Quiver Bioscience
- Shantanu: Dewpoint Therapeutics, Deepcell, Waypoint Bio

S.D.G.

anne@broadinstitute.org

Download PDF of slides here: http://broad.io/CarpenterSlides

Got feedback on this talk? http://broad.io/CarpenterFeedback

Open positions!

Postdoc: Data science/ML

Postdoc: Training Program in Bioimage Analysis

Download free, at

cellprofiler.org

Computational? Within 3 years of earning

PhD? Become a Schmidt Fellow at the Broad

Earned your PhD in Sweden?

Wallenberg postdoc fellowship at the

Broad Institute (due Nov)
