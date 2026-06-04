---
source_note: "Papers/Paper - Leung,-Chak-Ming-2022-05-12-A-guide-to-the-organ-on-a-chip.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Leung,-Chak-Ming-2022-05-12-A-guide-to-the-organ-on-a-chip.pdf"
converter: "microsoft/markitdown"
---
University of Groningen

A guide to the organ-on-a-chip

Leung, Chak Ming; de Haan, Pim; Ronaldson-Bouchard, Kacey; Kim, Ge-Ah; Ko, Jihoon;
Rho, Hoon Suk; Chen, Zhu; Habibovic, Pamela; Jeon, Noo Li; Takayama, Shuichi
Published in:
Nature Reviews Methods Primers

DOI:
10.1038/s43586-022-00118-6

IMPORTANT NOTE: You are advised to consult the publisher's version (publisher's PDF) if you wish to cite from
it. Please check the document version below.

Document Version
Publisher's PDF, also known as Version of record

Publication date:
2022

Link to publication in University of Groningen/UMCG research database

Citation for published version (APA):
Leung, C. M., de Haan, P., Ronaldson-Bouchard, K., Kim, G.-A., Ko, J., Rho, H. S., Chen, Z., Habibovic,
P., Jeon, N. L., Takayama, S., Shuler, M. L., Vunjak-Novakovic, G., Frey, O., Verpoorte, E., & Toh, Y.-C.
(2022). A guide to the organ-on-a-chip. Nature Reviews Methods Primers, 2(1), Article 33.
https://doi.org/10.1038/s43586-022-00118-6

Copyright
Other than for strictly personal use, it is not permitted to download or to forward/distribute the text or part of it without the consent of the
author(s) and/or copyright holder(s), unless the work is under an open content license (like Creative Commons).

The publication may also be distributed here under the terms of Article 25fa of the Dutch Copyright Act, indicated by the “Taverne” license.
More information can be found on the University of Groningen website: https://www.rug.nl/library/open-access/self-archiving-pure/taverne-
amendment.

Take-down policy
If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately
and investigate your claim.

Downloaded from the University of Groningen/UMCG research database (Pure): http://www.rug.nl/research/portal. For technical reasons the
number of authors shown on this cover page is limited to 10 maximum.

Download date: 26-10-2025

A guide to the organ- on- a- chip

 5, Hoon Suk Rho6, Zhu Chen7,13, Pamela Habibovic

 6 ✉, Noo Li Jeon5 ✉,

 2,14, Kacey Ronaldson- Bouchard3, Ge- Ah Kim

 4,

Chak Ming Leung1,14, Pim de Haan
Jihoon Ko
Shuichi Takayama
Olivier Frey10 ✉, Elisabeth Verpoorte

 8,9 ✉, Michael L. Shuler

 7 ✉, Gordana Vunjak- Novakovic3 ✉,
 11,12 ✉

 2 ✉ and Yi- Chin Toh

Abstract | Organs- on- chips (OoCs) are systems containing engineered or natural miniature
tissues grown inside microfluidic chips. To better mimic human physiology, the chips are designed
to control cell microenvironments and maintain tissue- specific functions. Combining advances
in tissue engineering and microfabrication, OoCs have gained interest as a next- generation
experimental platform to investigate human pathophysiology and the effect of therapeutics in
the body. There are as many examples of OoCs as there are applications, making it difficult for
new researchers to understand what makes one OoC more suited to an application than another.
This Primer is intended to give an introduction to the aspects of OoC that need to be considered
when developing an application- specific OoC. The Primer covers guiding principles and
considerations to design, fabricate and operate an OoC, as well as subsequent assaying
techniques to extract biological information from OoC devices. Alongside this is a discussion of
current and future applications of OoC technology, to inform design and operational decisions
during the implementation of OoC systems.

The organ-on-a-chip (OoC) is an intriguing scientific
and technological development in which biology is
coupled with microtechnology1,2 to mimic key aspects
of human physiology. The chip takes the form of a
microfluidic device containing networks of hair- fine
microchannels for guiding and manipulating minute
volumes (picolitres up to millilitres) of solution3–5. The
organ is a more relatable term that refers to the min-
iature tissues grown and residing in the microfluidic
chips, which can recapitulate one or more tissue- specific
functions. Although they are much simpler than native
tissues and organs, scientists have discovered that these
systems can often serve as effective mimics of human
physiology  and  disease.  OoCs  comprise  advanced
in vitro technology that enables experimentation with
biological cells and tissues outside the body. This is
achieved by containing them inside vessels conditioned
to sustain a reasonable semblance of the in vivo envi-
ronment, from a biochemical and physical point of view.
Working on the microscale lends a unique opportunity
to attain a higher level of control over the microenviron-
ment that ensures tissue life support, as well as a means
to directly observe cell and tissue behaviour.

The OoC is a relatively recent addition to the tool-
box of model biological systems available to life science
researchers to probe aspects of human pathophysiol-
ogy and disease. These systems cover a spectrum of
physiological relevance, with 2D cell cultures the least

relevant, followed in increasing order by 3D cell cultures,
organoids and OoCs. Unsurprisingly, the use of model
organisms such as mice and Drosophila physiologically
exceeds engineered tissue approaches6,7. While biologi-
cal complexity increases with physiological relevance in
model organisms, this unfortunately leads to increased
experimental difficulty. In vivo physiological processes
are, in many ways, the least accessible to direct investi-
gation in mice, humans and other mammals, despite sig-
nificant advances in in vivo imaging. However, 2D and
3D cell cultures, such as spheroids and stem cell- derived
organoids, sacrifice some aspects of in vivo relevance to
facilitate experimentation. The OoC may be regarded as
a bridging technology, offering the ability to work with
complex cell cultures, while providing better engineered
microenvironments to maximize the model.

Following  on  from  early  concepts,  including
animal- on- a- chip8, body- on- a- chip9 and breathing
lung- on- a- chip 10,  research  in  the  OoC  and  micro-
physiological systems fields has grown exponentially;
evidenced by numerous excellent reviews published
recently1,2,11.  Recognition  of  OoC  technology  now
extends far beyond university laboratories, driven by a
need to better understand the human physiology under-
lying health and disease, and to find new approaches to
improve the human condition. The World Economic
Forum, for instance, selected the OoC as one of the top
ten emerging technologies in 2016 (ref.12). This indicates

 1

✉e- mail: p.habibovic@
maastrichtuniversity.nl;
njeon@snu.ac.kr;
takayama@gatech.edu;
mshuler@hesperosinc.com;
gv2131@columbia.edu;
olivier.frey@insphero.com;
e.m.j.verpoorte@rug.nl;
yichin.toh@qut.edu.au

https://doi.org/10.1038/
s43586-022-00118-6

PRIMERNATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 0123456789();:
Author addresses

1Integrative Sciences and Engineering Programme, National University of Singapore,
Singapore, Singapore.
2Pharmaceutical Analysis Group, Groningen Research Institute of Pharmacy, University
of Groningen, Groningen, Netherlands.
3Laboratory for Stem Cells and Tissue Engineering, Department of Biomedical
Engineering, Columbia University, New York, NY, USA.
4School of Materials Science and Engineering, Georgia Institute of Technology, Atlanta,
GA, USA.
5Department of Mechanical Engineering, Seoul National University, Seoul, Republic
of Korea.
6MERLN Institute for Technology Inspired Regenerative Medicine, Maastricht University,
Maastricht, Netherlands.
7Nancy E. and Peter C. Meinig School of Biomedical Engineering, Cornell University,
Ithaca, NY, USA.
8The Wallace H. Coulter Department of Biomedical Engineering, Georgia Institute
of Technology and Emory School of Medicine, Atlanta, GA, USA.
9Parker H. Petit Institute for Bioengineering and Biosciences, Georgia Institute
of Technology, Atlanta, GA, USA.
10InSphero AG, Schlieren, Switzerland.
11School of Mechanical, Medical and Process Engineering, Queensland University
of Technology, Brisbane, Queensland, Australia.
12Centre for Biomedical Technologies, Queensland University of Technology, Brisbane,
Queensland, Australia.
13Present address: Bio- Rad Laboratories, Hercules, CA, USA.
14These authors contributed equally: Chak Ming Leung, Pim de Haan.

that there is a strong need for human- like testing sys-
tems in the pharmaceutical industry and also a matu-
rity of the OoC technologies to build them. Similarly,
cosmetic, food and chemical industries stand to benefit
enormously from OoC technologies for both produc-
tion and testing, as society seeks humanized in vitro
alternatives to animal testing.

OoC technology has benefited from converging
advances in tissue engineering and microfabrication.
Cell  and  tissue  engineering  have  progressed  from
primitive 2D monocultures to complex 3D co- culture
systems. Much emphasis has been placed on cellu-
lar microenvironment and geometrical arrangement,
which enables cell manipulation to achieve cell polariza-
tion13–15, direct cell–cell interaction16,17 and propagation
of chemical and electrical signalling18–20. Besides more
advanced cell lines21, handling of primary cell sources
and integrating them into artificial structures to promote
organ- like functions has become more robust and relia-
ble22,23. The emergence of induced pluripotent stem cell
(iPSC) technology promises personalization of OoCs,
as patient- specific cells can be differentiated from iPSCs
obtained from individual donors and incorporated into
the OoCs24–26. This allows study of disease phenotypes
and drug responses in a patient- specific manner27.

The second driving force behind OoC success has
been microsystems technology, the umbrella term for
fabrication processes borrowed from integrated circuit
industry. This approach uses lithographic pattern transfer
to create structures in the nanometre and micrometre
range28,29.  Milestones  in  the  development  of  OoCs
are coupled with key technological developments in
microsystems technology (Box 1). First used in ana-
lytical chemistry to engineer laboratory- on- a- chip
devices3,30–32, microsystems technology has driven the
development of both microfluidic and miniaturized

Microsystems technology
A set of technologies for
fabrication of planar devices
having microscale and
nanoscale features. organ-
on-a-chip (ooC)- containing
microfluidic channels and
integrated electrical and
non- electrical components
are often fabricated using
microsystems technology.

Lithographic pattern
transfer
A microfabrication technique
in which micrometre- sized
features are transferred from
a mould into a silicone polymer,
usually poly(dimethylsiloxane)
(PDMS).

Single- organ systems
organ- on- a- chip systems
with only one organ or tissue
modelled.

Multi- organ systems
organ- on- a- chip systems
with multiple tissues that
are representative of organ
systems are being modelled.
A fluidic circuit is embedded
in the device to connect the
different organ compartments
and allow for inter- organ
communication via soluble
paracrine signalling factors.

2 | Article citation ID:            (2022) 2:33

actuator and sensing capabilities of OoCs. This has
resulted in a shift to how in vitro bioreactor and cell
biological systems are designed33,34, operated35–39 and
monitored38,40,41. Gone are the typical flat polystyrene
(PS) surfaces of the well plate or Petri dish. In vitro
organ function can now be observed in chips individu-
alized for the organ of interest. The chips are tailored to
replicate cellular and extracellular features of the organ
that can respond to biochemical and physical cues to
maintain and simulate organ function. Crucially, OoC
systems enable multi- parametric read- outs of organ
function,  providing  a  window  into  the  integrated
biology of humans and animals.

OoC technologies have advanced and matured sub-
stantially and it is predicted that interest will continue
to grow in the coming years. However, for those new to
the field, it may seem as if there are at least as many
examples of OoCs in the literature as there are appli-
cations. Deciding where to start may be daunting. This
Primer is designed to introduce the aspects of OoCs that
need to be considered when developing an experiment.
Important inventions over the past two decades are
summarized, with the goal of illustrating how these have
advanced the field. The Primer covers guiding principles
and considerations to design, fabricate and operate an
OoC as well as subsequent assaying techniques to extract
biological information. Also included is a discussion of
applications for OoC technology.

Experimentation
OoCs are designed to provide a suitably in vivo- like
environment to guide a collection of cells to assem-
ble into a 3D tissue capable of replicating one or more
organ- level functions or to culture organotypic tissue to
retain function. This section gives an overview of choices
and considerations when designing an OoC tailored to a
particular in vitro tissue experiment. OoC development
should be guided by its context of use, which is related
to the application area it will be used for, and defines
the expected data42,43. The considerations, strategies and
equipment needed for any general OoC experiment are
reviewed in the order they present themselves when set-
ting up a new experiment (fig. 1). Finally, several case
studies of single- organ and multi- organ OoCs provide
insight into the development of these systems for specific
applications in drug research.

Conceptualization and design
Single- organ systems often achieve a high degree of bio-
logical authenticity, allowing evaluation of the response
of a specific organ to a compound or mixture of com-
pounds. Multi- organ systems provide a framework to
examine the potential interaction of one organ with
at least one other, principally through the exchange
of metabolites or soluble signalling molecules. Both
single- OoC and multi- OoC systems are often referred
to as microphysiological systems, as they are designed to
model features of human or animal biology within a
microscale culture44. Multi- OoC systems, which model
the physiological systemic response in the body, are
commonly referred to as body- on- a- chip35. The choice
of a single- organ or multi- organ system depends on the

www.nature.com/nrmpPrimer0123456789();: Solid organ chips
organ- on- a- chip systems
that are representative of
parenchymal or mesenchymal
organ tissues, such as the liver,
tumour, pancreas, bone and
cartilage. Cells are often
cultured as a 3D tissue mass or
embedded in an extracellular
matrix (eCM) analogue where
they may directly interact with
one another and with the
culture substrate and medium
in a defined manner.

Barrier tissue chips
organ- on- a- chip systems
that are representative of
endothelial and epithelial
tissues, such as the vascular
endothelium, gut, and corneal
and skin epithelium, that
function as a living barrier
to regulate active and/or
passive transport of molecules.
Cells are often attached to a
porous surface separating two
different compartments.

desired functionalities needed for the system to be a
good model of the physiological processes. The degree
of complexity should be kept to the minimum required
to represent the biological application without introduc-
ing unnecessary factors that make the system difficult
to use and analyse. Multi- organ systems tend to involve
more complex engineering design than single- organ
systems. This allows control of the transport and dis-
tribution  of  culture  media  between  the  individual
organs. Consequently, there is a trend in the OoC sys-
tems that have been developed, where single- OoCs are
more biologically detailed models of an organ whereas
multi- OoCs use less detailed organ models and focus on
the systemic interactions between organs35.

The  next  design  consideration  is  to  decide  the
approach for forming functional tissues within the OoC.
In a top- down or organotypic approach, a primary
tissue — for example, an organ slice from a biopsy — or
engineered tissue — such as a preformed organoid —
is incorporated into the OoC system. In a bottom- up
approach, isolated cells from primary, immortalized
lines or stem cell- derived sources are cultured inside
an a priori empty microfluidic environment, which
supports the remodelling of the cells into a functional
neo- tissue. The selected strategy informs the design
of the OoC architectures. This serves a dual purpose of
organizing and supporting cells within the OoC in a
specific cell culture configuration, as well as routing
fluids, such as the culture medium, to connect tissue
components in a manner that reflects their connectivity
in vivo. Although there are many variations of OoC
device architectures, they can generally be divided into
two classes, based on the organ system they create.

The first comprises solid organ chips, where cells are
cultured as 3D tissue masses that can interact with one
another and the culture medium in a defined manner.
Examples of this architecture type include micro- pillar
and microwell arrays that are often used in liver (fig. 1),
tumour, cardiac and adipose OoCs11,45. The second class
contains barrier tissue chips, where the device architec-
ture supports the cells to form a natural barrier between
fluid compartments. This allows selective transport
processes across the barrier to be studied. These archi-
tectures are typically found in gut, lung and skin OoCs
(fig.  1). The choices for either architecture and the
culture strategy depend on the final functionality of
the OoC46.

Material selection and fabrication
The choice of material depends on numerous factors,
including the functionality of the final device, micro-
fabrication strategy, read- outs and biocompatibility.
A typical OoC device consists of various material com-
binations to build the final device. Amongst the most
commonly used materials are silicone rubber, such as
poly(dimethylsiloxane) (PDMS); glass; and thermoplas-
tics such as PS, poly(methyl methacrylate) (PMMA),
polycarbonate (PC) or cyclic olefin copolymer (COC).
However, there is no perfect standard material, as dif-
ferent materials have their advantages and disadvan-
tages (TABle  1). Decisions regarding material choice
are often a compromise between desired functionality,
access to fabrication facilities and development stage
of the pro duct (Supplementary Fig. 1). Glass is robust
and inert, but expensive and requires advanced pro-
cessing facilities. Silicon allows fabrication of intricate

Box 1 | Milestones in the development of organs- on- chips and experimental techniques

The biological and technical complexity of organ-on-a-chip (OoC) systems has increased over the past two decades, which
mirrors the growing desire of researchers for more in- depth information about biological systems. Significant milestones
are listed (see the figure, left), with novel experimental techniques highlighted (see the figure, right). The tops of the blue
bars line up with the approximate dates that the techniques started to be reported in the literature.

Organ-on-a-chip milestones

• Miniaturized total analysis system

• Cell patterning in microchannels

• Cell handling in microchannels

• Cell culture in microchannels

• Single OoC

• Multiple OoCs

Experimental focus
3D (Bio)Printing

Scaling

Dosing experiments; ADME-Tox

Control of incubation parameters

Surface modiﬁcation for cell patterning

Mechanical and material cues

Introduction of PDMS and so lithography

• Spheroid/iPSC-derived OoC

Cell seeding — good practice/cell lines, primary cells, iPSCs

• 3D cultures

Today

Microﬂuidic cell perfusion: pumping, media, etc.

Mixing and generation of gradients

Microfabrication of microchannels

• OoC for regenerative medicine

Chip design

• OoC disease models

• Personalized OoC models

Late
1980s

1990s

2000s

2010s

2020s

Degree of complexity

ADME- Tox, absorption, distribution, metabolism, excretion and toxicology; iPSC, induced pluripotent stem cell;
PDMS, poly(dimethylsiloxane).

 3

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
b  Material selection
    and fabrication

c  Selection of
    biological elements

d  Supporting life
    inside devices

• Perfusion
• Incubators
• Mechanical stimulation
• Controls and sensors

a  Conceptualization
    and design

Organ 1: barrier type.
Cells cultured on ECM-
coated membrane

Organ 2: 3D-cultured
tissue, e.g. organoid,
with parenchyme

Medium 2

Pump 2

Medium 1

Pump 1

TEER sensor

Incubator
O2, CO2, temperature

Cytokines

Mechanical actuators

Microscope

Fig. 1 | Experimental set-up for a generic two-organ system with supporting peripheral equipment. a | Design and
conceptualization of the organ-on-a-chip (OoC) system need to factor in number of organ models, how they are commu-
nicating and culture configuration of each organ model. b | Materials and fabrication technique need to be selected for
construction of the OoC device, depending on scale, read- out functionality and feature resolution required. Sterilization
and surface modification are tied to material choices. c | Choice of cell sources (primary, immortalized, stem cell- derived)
will need to balance between biological functionality and practical operability of device. d | Finally, OoC system will
be operated with peripheral equipment including pumps, incubators, sensors and microscopes to properly maintain,
stimulate and monitor cells inside the OoC system. ECM, extracellular matrix; TEER, transepithelial electrical resistance.

nano structures to form on- chip sensors or barrier
gratings, although this is expensive and laborious due
to the need for clean- room facilities. Moreover, it is
not transparent, presenting compatibility issues with
conventional inverted microscopes. Thermoplastics
ensure transparency and are easy to mass- produce,
but are challenging when creating complex designs at
the prototyping phase. Currently, PDMS is the most
widely used material for development of OoC devices
because devices with high- resolution microstructures

and nanostructures can be easily produced by replica
moulding in PDMS from microfabricated templates.
PDMS is ideal for biological applications due to its
biocompatibility, optical transparency and gas perme-
ability. Furthermore, the elasticity of PDMS has been
exploited to apply mechanical stimulation to cells10.
Recently, breakthrough technology has been proposed
that enables high- speed and high- quality PDMS 3D pro-
cessing through laser pyrolysis47. However, this material
is known to adsorb and absorb a wide range of (bio)

4 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();:
Micro- milling
A microfabrication technique
in which structures are carved
into a solid block of material
by a computer- controlled
milling tool.

PDMS- based soft
lithography
A collection of techniques for
replicating structures in the
elastic silicone rubber, poly
(dimethylsiloxane) (PDMS),
or using PDMS stamps to print
molecules in patterns onto
device surfaces.

chemicals, which may influence experimental results,
especially for drug testing applications48,49.

3D printing and plastic- based OoC mass production
via injection moulding.

PS is one of the alternatives often seen in standard
cell culture tools, such as tissue culture flasks and multi-
well plates, as well as newly developed OoCs50,51. What is
noteworthy is that production yield, which is one of the
obstacles of the existing OoC fabrication method, can be
solved by mass production through injection moulding,
whereas single prototypes are made by micro- milling. This
productivity can provide a route to efficient OoC- based
high- throughput screening that allows automated test-
ing of a large number of drug compounds for a specific
biological target. Injection moulding is not suitable for
OoC models having complex designs and functional fea-
tures such as stretching. The fabrication method should
thus be adopted considering the experimental purpose.
Meanwhile, as 3D printing technology advances,
some groups have reported OoC models generated by
3D printing (or additive manufacturing)52. This method
quickly and accurately creates complex 3D structures
that have been difficult to create with the other methods
mentioned so far. The use of 3D- printed microfluidic
devices for OoC applications is currently limited by
inadequate optical transparency, as resin formula-
tions and post- processing steps are not yet optimized
for this property. In addition, the biocompa tibility of
3D- printed resins also needs to be verified. Nonetheless,
OoC  technology  has  reached  a  point  where  effec-
tive  fabrication  methods  can  be  adopted  through
material selection based on experimental purposes
(fig. 2). Various options have been presented, including
etched microchannel configuration via PDMS- based
soft lithography, production of complex structures via

Sterilization. OoC devices differ from conventional cell
culture platforms (such as multiwell plates) due to their
3D architectures and the materials from which they
are fabricated, as highlighted by a previous review53.
However, performing cell culture in OoC devices shares
similar  requirements  with  conventional  platforms.
Sterility of the OoC devices must therefore be ensured
to avoid microbial contamination, including in the var-
ious microfluidic components that will be used to set
up the entire OoC system. The variation in materials
used in OoC devices and microfluidic components
requires additional precaution in choosing the appro-
priate sterilization methods to prevent component
damage. Inappropriate use of sterilization methods
may cause damage to the OoC devices and microfluidic
components, resulting in undesirable leaks during sys-
tem assembly. Many common plastics such as PMMA
and PC may not be suitable for conventional autoclave
sterilization due to their low thermal resistance. Other
methods of sterilization, such as UV or ethanol treat-
ment, are often employed in the laboratory setting,
although these methods should be used with caution.
UV penetration may be limited by the material’s opacity
and ability to absorb the germicidal UV rays. Ethanol
soaking is not compatible with some materials, such
as PMMA, as they may be partially dissolved. Ethanol
can also be absorbed into PDMS devices if soaked for
extended periods of time (longer than overnight), which
can adversely affect cells when it is subsequently leached
out. Gamma irradiation and ethylene oxide treatment

Table 1 | Most common materials used for fabricating OoCs, their advantages and drawbacks and their main purpose in OoC devices

Materials

PDMS10,315,316

Advantages

Gas- permeability

Optical transparency

Elasticity

Biocompatibility

Drawbacks

Experimental model

Absorption of small molecules

Disease modelling

Difficulty in mass production

Mechanical and chemical stimuli

Electrode patterning

Thermoplastics277,317

Optical transparency

Rigidity

Drug screening

Mass production

Cost- effective

Low absorption

Difficulty in producing complex
structures

Low permeability

Large- scale experimentations

3D printing resins318,319

High mechanical and thermal properties

Autofluorescence

Low cost

Complexity and design freedom

Opacity

Toxicity

Low permeability

Surface roughness

3D design modelling

Rapid prototyping

Glass320

Optical transparency

Laborious fabrication

Electrode patterning

Inert

Biocompatibility

Low autofluorescence

Fragile

Expensive

Silicon321,322

Low absorption

Generation of high- resolution channels on the
nanoscale

OoC, organ-on-a-chip; PDMS, poly(dimethylsiloxane).

Laborious fabrication due to need
for clean- room facilities

On- chip sensors

Formation of diffusive barriers

Expensive

 5

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
Purpose of experiments

• Complex and elaborate microstructure

(tunable membrane, cantilever)

High resolution

• Mechanical tunability (exert mechanical

forces)

• Gas permeability (hypoxic condition)

Rapid processing

• Biocompatibility

• Microelectrode array (gold or platinum)

• Non-conducting substrate

• Chemical durability

• Large-scale drug screening (HCS equipment)

• Small-molecule screening (low surface

absorption)

• High-throughput screening

• Low cost and ready-made

• Rapid prototyping

• Scalable manufacturing

• Complexity and design freedom

• Biocompatibility (natural

or synthetic bio-ink)

• 3D cellular architecture

Material and fabrication selection

a  PDMS-based so lithography

b  PDMS-based laser processing

c  Glass PDMS-based lithography

d  Thermoplastic-based injection moulding
     (mass production)

e  UV curable resin-based 3D printing

f  Hydrogel-based 3D bioprinting

Fig. 2 | Material selection and fabrication according to the purpose of the experiment. a,b | With biological compati-
bility and tunable mechanical properties, poly(dimethylsiloxane) (PDMS) is fabricated using soft lithography to develop
an elaborate microstructure323 (part a) or 3D rapid prototyping by laser processing47 (part b). c | Integrated device fabri-
cation with gold- or platinum- deposited substrate such as an electrode array324. d | For large- scale experiments such as
high- throughput screening, plastic- based injection moulding could be selected50,51. e,f | For rapid prototyping with a high
degree of design freedom, resin- based (part e) or hydrogel- based (part f) 3D printing is available325,326. HCS, high- content
screening.

should be the preferred sterilization options in industrial
or clinical settings.

Surface treatment. Treatment of device surfaces that
come into contact with cells may be necessary to ensure
biocompatibility or enhance cell adhesion. In 3D sphe-
roid or organoid cultures, treatment with pluronic acid
is often adopted to passivate the chip surface to prevent
undesirable spheroid or organoid dissociation via poten-
tial cell attachment. This is crucial, as loss of the 3D tissue
architecture may cause a concomitant loss in physio-
logical organ function54. On the other hand, protein and
extracellular matrix (ECM) coatings may be used if we
wish to promote cell attachment to the chip substrate.
These coatings are a must for the formation of attached,
confluent monolayers of cells needed to emulate the
intestinal epithelium in the gut14,55, for instance, or
the endothelium in blood–brain barrier (BBB) OoCs56–58.

To create higher- fidelity (patho)physiological models,
tissue- specific and disease- specific matrices may be
used, for example to induce crypt- like structures in
gut- on- a- chip devices59,60. These can include complex
biomatrices such as Matrigel, or simpler biomatrices
derived from fibrin or collagen. Cells can be mixed with
the liquid precursor of these biomatrices, which can be
subsequently loaded into the OoC device and allowed to
polymerize into a gel. Some organs such as the liver and
skin require a 3D microenvironment in order to attain
physiological function, and hence biomatrices can serve
as a useful scaffold for cells to remodel into a 3D struc-
ture. Biomatrices may also be essential for maintenance
or differentiation of certain cell types. For example,
Matrigel has been found to promote neuronal mainte-
nance and differentiation in neural stem cells61, whereas
culturing of myoblasts within a suspended overhanging
fibrin- based gel promoted myogenic differentiation62.

6 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: Selection of biological elements
Here, we focus the discussion mainly on the selec-
tion of isolated cells because they are more commonly
employed in OoCs. The integration of tissue slices into
microfluidic devices has been previously reviewed63.
There are several criteria when selecting an appropriate
cell source that should be considered in the context of
the application of the OoC.

Patient specificity. If the OoC is intended to model
physiological  variations  in  individuals  or  specific
patient (for example, diseased versus healthy) popu-
lations, primary and stem cell- derived cells are both
viable options. However, primary cells are often less
accessible due to a lack of both availability of donor
tissues and well- established protocols for isolating the
cells from the tissues with high purity. With the advent
of iPSC technology64, patient- derived stem cells become
more accessible with minimal invasiveness. iPSCs can
be differentiated into various cell lineages, and are par-
ticularly useful when one is trying to generate human
leukocyte antigen (HLA) or patient- matched tissues in
a multi- OoC system65.

Intrinsic functionality of the cells. OoCs often need
to recapitulate tissue- specific physiological functions
that are essential for their intended application, such
as xenobiotic metabolism in the liver, barrier functions
for the intestine and skin, and contractility of cardiac
and skeletal muscles. Many immortalized cell lines as
well as human pluripotent stem cell- derived cells often
express a limited subset or fraction of the functional
capacity as compared with primary cells66. Although
primary cells may possess the full in vivo complement
of cellular functions, they often lose their tissue- specific
functions rapidly when maintained in vitro67, which may
limit the useful time window of the OoC, especially for
long- term studies. Primary cells can have inter- donor
variability, which may pose a challenge for data repro-
ducibility when not looking at patient- specific responses.
Therefore, it is helpful to prioritize the different cellular
functions based on the intended application of the OoC
when considering different cell sources.

Expansion capacity. Expansion capacity refers to the
ability of the cells to undergo proliferation in vitro and
directly relates to the number of cells that can be practi-
cally generated for seeding into an OoC device. Although
microfluidic devices house a minute number of cells
(typically in the order of 103–105 cells), their design can
influence how many cells are practically needed during
the seeding process. This may be limiting for primary
cells, which have no or limited doubling capacity before
they undergo senescence. Although human iPSCs can be
expanded indefinitely, the differentiation and cell har-
vesting process can result in significant cell loss, cap-
ping the number of cells that one can produce in a single
batch. On the other hand, when using immortalized cell
lines which have high proliferation rates, one needs to
consider the minute cell culture volumes present in OoC
devices to prevent nutrient depletion as well as occlusion
of the fluidic channels by the growing tissue mass.

Supporting cell types. The stromal environment of
tissues is composed of supporting cells (such as fibro-
blasts, pericytes and vasculature) that often contribute
to the functionality of the engineered tissue, and play
major roles in disease progression. The incorporation
of stromal cells into engineered tissues has been shown
to modulate cell signalling and structural support via
modification and deposition of the ECM, and influ-
ence whether a drug treatment will succeed or fail. The
stroma is dramatically changed in the context of disease,
particularly with respect to systemic diseases such as
fibrosis and cancer. Thus, the inclusion of stromal cells
and their proper microenvironment can be critical in
recapitulating specific tissue functionality and physio-
logical responses that are representative of the in vivo
situation.

Functional time window. iPSCs need to be differenti-
ated for 2–3 weeks to mature into specific cell lineages.
Primary cells forming barrier tissues, such as the skin,
BBB and intestinal epithelium, often require an extended
culture period to remodel into cell sheets with well-
established cell–cell contacts to have physiological bar-
rier functions68. The device design and operation should
be sufficiently robust to cater to long- term cultures (typi-
cally a few weeks) if on- chip stem cell differentiation and
tissue maturation are considered.

Additional cell considerations for systemic studies.
For systemic studies, the presence of a functional cir-
culatory system (blood or surrogate with different cell
types) and the immune system may be required. Both
are challenging to work with and both elements have
been underdeveloped up until now.

Supporting life inside the device
Selection of cell culture medium. For a single- OoC
involving only a single cell type, culture medium that
was originally formulated for conventional cultures can
similarly be adopted. An added complexity for media
selection is introduced when generating single/multi-
OoCs that involve multiple cell types, each having dif-
ferent nutrient requirements. The optimized co- culture
medium must be able to maintain the viability and
functional phenotype of each distinct cell population.
Once this criterion is satisfied, we can then consider the
suitability of the medium in supporting downstream
assays without undesired interference. In the optimiza-
tion of a suitable co- culture medium for OoC applica-
tions, many groups have adopted various mixtures of
the original culture medium used for each individual
cell type with relatively good outcomes. These include
multicellular OoC models mimicking adipose tissue69,
and also multi- organ OoC models recapitulating liver–
kidney  interactions70  and  liver–adipose–skin–lung
interactions71. However, with an increasing number of
different cell types being co- cultured, the optimization
of a suitable co- culture medium becomes more chal-
lenging. Compartmentalization of cells into individual
compartments via permeable membranes can circum-
vent the need for a common co- culture medium, thus
allowing for cell- specific media to be supplied to each

 7

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
Media perfusion
The delivery of cell culture
medium to the living elements
inside a microchannel using
convective fluid flow driven by
external forces generated
by pumps or gravity, in order
to supply nutrients and remove
its metabolites.

Shear stress
friction on a cell surface
caused by the moving of fluids
over that surface.

Reynolds number
(re). A dimensionless
parameter that describes
the ratio of a fluid’s inertial
forces to viscous forces.
Commonly used as a measure
to determine whether fluid
flow is laminar or turbulent.

Péclet number
(Pe). A dimensionless
parameter that describes
the ratio of convective to
diffusive mass transport.
Commonly used as a measure
to determine the primary
mode of mass transport.

Damköhler number
(Da). A dimensionless
parameter that describes the
ratio of diffusion to reactive
timescales. Commonly used
as a measure to determine the
overall efficacy of a reaction
process.

Effective culture time
The period of time whereby
a cell culture is able to receive
sufficient biochemical factors
essential for survival and
maintenance of its phenotype.

compartment while still permitting paracrine inter-
actions between the compartments, as shown in OoC
devices mimicking the liver72 and skin73. If possible,
serum- free media should be considered as sera consti-
tute a large source of variation and may interfere with
assays74. Media should be optimized in experiments
with the OoC, starting with the most commonly used
cell culture medium for non- OoC work with the same
cells, such as minimal essential medium (MEM)- based
medium for epithelial cell cultures or endothelial cell
growth medium (ECGM) for endothelial cells.

Creation of perfusion circuits. Media perfusion is a hall-
mark of OoC devices, serving as a circulatory system
mimic that maintains a concentration gradient for
nutrient and waste convective transport. To drive media
perfusion through the OoC device, various pumps have
been adapted for OoC applications (Supplementary
Fig. 2). These include conventional syringe pumps75,76,
microvalve- driven actuator pumps77,78 and peristal-
tic pumps38,79. Alternatively, various groups have also
adopted hydrostatic pressure- based pump- free systems
to drive perfusion80–82. The choice of pumps will greatly
depend on whether the culture runs on a one- pass type
of perfusion flow or a recirculatory flow configuration.
Conventional syringe pumps and pump- free gravity-
driven flows typically support one- pass perfusion flows,
whereas other pump variants such as peristaltic pumps
are amenable to driving recirculatory flow. Recently,
however, we have seen the emergence of OoC devices
with gravity- driven recirculatory flows, which removes
the need for physical pumps, hence minimizing overall
system complexity while still mimicking soluble factor
crosstalk between multiple organ compartments82–86. The
choice for either type of flow and for the flow rate (vol-
ume per time) depends on the needs of the organ model
and the in vivo situation, including the appropriate level
of shear stress induced by flow over a tissue surface.

One- pass flow ensures a stable supply of fresh nutri-
ents, but inter- tissue communication is only possible
in one direction (namely downstream). A recirculat-
ing flow has the advantage of recirculating signalling
molecules,  which  allows  chemical  communication
between the different elements of a multi- organ device.
Recirculation, however, does not allow for continuous
replenishment of nutrients, and will lead to an accumu-
lation of waste products. Although OoC systems can be
operated for several days without medium exchange,
periodic removal of a portion of medium from the OoC
with replacement by fresh medium is necessary. This
removal has the useful consequence that material is
provided for offline analysis. The fraction removed and
frequency of removal can be variable24,87. Fluid volume in
an OoC is also very limited, particularly in a design that
emulates physiologically realistic values of the ratio of
blood/interstitial fluid to body mass85. The amount
of sample that can be withdrawn is thus small (<100 µl
medium per day, even if full replacement is used). Partial
fluid replacement is preferred to sustain more physio-
logical conditions, so samples of only 25–50 µl per day
may be available for offline analysis in systems emulating
realistic fluid to cell ratios.

Besides the use of pump/gravity- driven perfusion
flows to drive organ OoC interactions, another method
adopted is the transfer of conditioned medium from one
single- OoC (such as the liver) to another single- OoC
(such as the kidney) in a sequential manner88,89. This is
known as functional coupling of OoCs88, whereas the
perfusion methods described above with direct inter-
actions between OoC modules are known as physi-
cal coupling of OoCs. Functional coupling does away
with the technical challenge of incorporating pumps
or means of creating gravity- driven flow, and the need
for interconnections between different OoC modules.
However, it should be noted that functional coupling
may not be useful when monitoring real- time cross-
talk interactions between OoC modules, such as the
gut–liver axis. Furthermore, certain cell- secreted fac-
tors may need to be continuously concentrated due to
their highly degradable nature90. As such, the transfer
of conditioned medium from one OoC to another may
result in the loss of an effective amount of these cell-
secreted factors, with remaining numbers of factors
insufficient to elicit a response in the target OoC. Physical
coupling would be more appropriate in the scenarios
mentioned above.

Control of the cell microenvironment. Cells interact with
soluble factors, the ECM and neighbouring cells in a 3D
milieu with specific physico- chemical properties. This is
collectively known as the cell microenvironment, which
must be carefully controlled in the OoC system for cells
to function properly. As compared with conventional
bulk cell culture systems, OoC systems offer more pre-
cise control over the cell microenvironment because the
geometries of the culture chamber and the associated
physical and chemical phenomena of fluids are defined
with microscale resolution (in the order of 101–102 µm).
The unique physics of microfluidics results in fun-
damental differences between microfluidic- based and
conventional static cell cultures. Common phenomena
observed in conventional macroscale cell cultures, such
as bubble formation, evaporation and nutrient deple-
tion, are exacerbated by the microscale volumes and
material choices of OoCs, and can dramatically alter
osmolality, pH and nutrient availability. It is critical
to have a working knowledge of how various physical
forces and mass transport phenomena at the micro-
scale influence the presentation of various biochemi-
cal and mechanical cues, such as cytokines and shear
stress, respectively. Dimensionless numbers expressing
the relative dominance of competing physical pheno-
mena that are relevant to microenvironmental con-
trol include the reynolds number (Re; inertial/viscous
forces), Péclet number (Pe; convective/diffusive trans-
port) and Damköhler number (Da; diffusion/reaction
timescales). Their links to various environmental fac-
tors, such as shear stress and soluble factor signalling,
have been previously explained91. For instance, the Da
of critical biochemical factors, such as growth factors
and glucose, in cell cultures can be used to estimate
the effective culture time in an OoC device. Owing to the
smaller  dimensions  of  OoCs  compared  with  con-
ventional well plates, the Da of biochemical factors is

8 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: much smaller, implying that their reaction time dom-
inates over diffusion time. Consequently, in a static
diffusion- dominated OoC, the time interval between
medium change is often shorter than that of the macro-
scale culture system, and can be scaled based on the
relative change in channel height, h, and the known
effective culture time of the macroscale culture sys-
tem91. Perfusing the OoC at flow rates such that the Pe
to Da ratio is high (≫1) ensures sufficient convective
delivery of these biochemical factors without limiting
cell uptake92,93.

Microfluidic control of environmental factors is often
coupled. For example, the fluid shear stress and mass
transport regime of soluble factors are both functions of
flow velocity, which means changing the perfusion flow
rate of an OoC can alter both shear stress magnitude and
soluble signalling at the same time. Dimensionless num-
bers can be used to guide device dimensions and oper-
ating parameters to selectively keep one environmental
factor constant (at least from the biological perspective
that there are minimal effects on cells) while varying
another. For example, when operating a multiplexed
device to examine effects of different shear stress magni-
tudes on cells, the Pe can be used to ensure that all of the
cells are in the convective mass transport zone (Pe > 1).
This would help decouple effects of shear stress from
autocrine soluble signalling as secreted factors would
be washed away. Conversely, when trying to study the
effects of secreted autocrine or paracrine factors, it may
be preferable to operate at flow rates where all cells are
subjected to shear stresses below a set threshold. This
is particularly important to prevent detrimental effects
on shear- sensitive cells, such as embryonic stem cells
(<10–3 dynes cm–2)92, primary neurons (<10–3 dynes cm–2)94
and hepatocytes (<10–1 dynes cm –2)95,96. On the other
hand, cells that experience shear stress physiologi-
cally have been reported to exhibit enhanced differ-
entiated cell phenotypes and functions over a certain
optimal range of shear stress magnitudes, as exempli-
fied by intestinal epithelial cells (~10–2 dynes cm–2)97,98,
airway epithelial cells (5 × 10–1 dynes cm –2)99,100, bone
cells (10–1–101 dynes cm–2)100 and cardiovascular cells
(100–101 dynes cm–2)100,101.

Care must be taken to ensure proper equilibration
of culture medium with the gaseous environment. The
gaseous composition of the air is important for main-
taining proper oxygen concentration and physiological
pH (7.0–7.4). Depending on the needs of the OoC, oxy-
gen may be kept at atmospheric levels (21%), lowered
or removed to recreate hypoxic (<10%)102 to anaerobic
systems, or increased to improve oxygenation of tissue
sections. Most conventional cell culture media (such as
DMEM or RPMI 1640) are formulated with bicarbo-
nate buffers, which yield a physiological pH of 7.0–7.4
only when equilibrated with 5% carbon dioxide. Hence,
5% carbon dioxide is typically used in conventional
cell culture incubators. If the OoC is operated outside
a conventional incubator, such as on a heating block
or transparent indium–tin oxide heaters under atmos-
pheric conditions, the medium pH can be maintained
by the addition of HEPES buffer103 or pre- equilibrating
the medium in a 5% carbon dioxide environment, first,

before delivery into the OoC device34. Cells grown in
OoCs may have a different baseline function from those
grown in conventional cell culture grown on tissue cul-
ture plastics. Therefore, one needs to be careful when
attributing differences observed between OoCs and con-
ventional cell culture to the specific environmental cue
being applied through the microfluidic device.

Monitoring OoC status. Different read- out options and
controls are necessary to monitor the status of the OoC
during culturing and experimentation. The most com-
mon control is visual microscopic inspection of the OoC
to regularly check whether the cells or tissue sections are
normal in appearance (size, number, shape and so on)
and there are no abnormalities (such as air bubbles or
microbial contaminations) that will lead to device fail-
ure. Air bubbles may arise during device operation, such
as upon connecting a new syringe with medium. This is
undesirable as moving air bubbles can be destructive to
cells in the microchannels by the interfacial force they
exert. Ideally, air bubble formation should therefore be
avoided by carefully connecting the tubing and forcing
the air out before cells are introduced. In the presence
of an air bubble, if the bubble is not obstructing the
medium perfusion flow and cells are protected from
direct bubble interaction (such as when cells are trapped
in hydrogel/micro- pillar arrays), it is better to leave the
air bubbles and allow them to dissolve into the medium
or diffuse through the chip if the chip is gas permeable.
However, if there is a high likelihood that the air bub-
bles will come into direct contact with the cells or block
medium perfusion flow, flushing out the bubble may
be essential to preserve the experimental set- up. When
attempting to flush out air bubbles, extra care has to be
taken to not dislodge the cells or break the chip’s seal
with the large forces required to extract the air bubbles.
Engineering controls such as the implementation of an
on- chip or external bubble trap ahead of the cell cul-
ture chamber can also greatly eliminate the risk of air
bubbles directly interacting with the cells. Other flow
obstructions may be caused by fibres or accumulated
debris, which can generally not be solved when cells are
already present; the experiment can then continue if the
obstruction is not in an essential place, or aborted if it
is blocking an essential flow. Microbial contaminations
are indicated by the presence of bacteria or yeasts inside
the microchannel and always result in the termination
of the experiment.

Case studies
Here,  we  provide  insight  into  the  development  of
single- organ and multi- organ OoC systems for specific
applications, with a special emphasis on OoCs for drug
research including absorption, distribution, metab-
olism, excretion and toxicology (ADME- Tox). We
discuss conceptualization and design, material selec-
tion and fabrication, selection of biological elements
and supporting life inside the device. The examples
considered in this section exhibit evolution in their
designs that are commensurate with advances in both
microfabrication and biological models over the past
decade. Once one or multiple research questions have

 9

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
Aa

Ba

Ca

Cell culture insert

Oral dose

IV dose

Drug in
medium

Well

Medium

15 mm

Ab

Bb

7-MPS platform

Apical
compartment

Drug

Basolateral
compartment

Cell

Collagen

Membrane

Gut

Transwell

Brain

Liver
scaﬀold

2 cm

Cb

Medium access
port A

Medium access
port B

Electrodes

2

3

1

4

5

Connector

Top gasket,
deﬁnes ﬂow path

Bottom gasket,
deﬁnes tissue
positions

Fig. 3 | Schematic drawings of the single-OoCs and multi- OoCs
highlighted in this section. A | Gut- on- a- chip device for drug absorption
studies104: Transwell cell culture insert that was the inspiration for
this gut- on- a- chip (part Aa); and flowing microsystem, with uptake of
drug molecules from apical channel and transport into basolateral channel
(part Ab). B | Reconfigurable multi- organ- on- a- chip (OoC): includes four,
seven or ten different organ models that can interact with one another via
microchannels107 (part Ba); and various layers of device, including all
connections for cell culture media and pneumatic channels to actuate
integrated micropumps (part Bb). C | Multi- OoC developed consisting of

several OoC compartments together in one device108: all microchannels
and chambers filled with green dye for visualization (part Ca); and elements
(1,  liver  chamber;  2  and  4,  heart  chamber  with  cantilevers  and
microelectrode arrays; 3, vulva cancer chamber; 5, breast cancer chamber)
contained in device, as well as medium access ports and integrated
read- out structures (part Cb). IV, intravenous; MPS, microphysiological
system. Parts Aa and Ab adapted from ref.104, Springer Nature Limited.
Parts Ba and Bb adapted from ref.107, CC BY 4.0 (https://creativecommons.
org/licenses/by/4.0/). Parts Ca and Cb adapted with permission from ref.108,
AAAS.

been formulated, these can be translated into a list of
functional requirements and technical specifications
that guide the construction and implementation of the
OoC system.

The desired functionalities of the system should
be leading in its design. The first decision is between
a single- organ or multi- organ system. Single- organ
systems tend to be more suited to study specific tissue
and organ functions, without having the complexity
of other organ systems involved. Multi- organ systems
are more suited to study interactions between different
organ compartments, such as when the functions of one
organ affect the functioning of another organ. We use
drug absorption through the intestinal epithelium as an
example of a single- organ system, and highlight different

multi- organ systems investigating the metabolism of a
drug in the liver and its subsequent therapeutic or toxic
effects in other target organs.

Single- organ OoC systems. Intestinal absorption of
orally administered drugs is commonly evaluated in
Transwell assays, where a layer of intestinal epithelial
cells is cultured on a permeable insert placed in one of
the wells of a cell culture plate. These intestinal cells act
as the barrier between the top compartment (mimicking
the gut lumen) and the bottom compartment (mimick-
ing the bloodstream); drug absorption can be measured
over time by analysing samples taken from both com-
partments. This intestinal absorption process has been
translated into a microfluidic format104 (fig. 3A).

10 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: The barrier consisting of intestinal cells grown on
a porous membrane was retained, but replaced the
static top and bottom compartments of the Transwell
with microchannels containing a dynamic flow of cell
medium (conceptualization and design). PDMS was
used because it is a transparent, biocompatible and
mouldable silicone rubber, with moulds produced by
photolithography, and the membrane was pretreated
with a collagen surface coating to improve cell adhesion
(material selection and fabrication). Caco-2 cells, the
gold- standard cell line for drug absorption studies, were
cultured inside the microchannel; these cells lack many
other functions that intestinal epithelial cells have, but
they are very suitable for absorption studies (selection
of biological elements). The intestinal OoCs were kept
in an incubator, with the cell medium provided by two
syringe pumps without recirculation (supporting life
inside the device). The device was inspected by optical
microscopy, and the permeability of model drugs was
monitored using high- performance liquid chromatog-
raphy and fluorescence- based assays with samples of the
OoC effluent.

A more complex intestinal single- organ OoC was
developed to address whether enteric coronavirus infec-
tions could be modelled in an OoC format, including the
testing of antiviral drugs105. The process of viral infec-
tion is far more complex, and requires multiple different
organ functions, including immune components, to be
present. A similar two- channel OoC as above was used,
based on a porous membrane, but with the inclusion
of more biological functionalities such as the barrier
function of both the intestinal epithelium and the blood
vessel wall, as well as an immune component (concep-
tualization and design). The OoC consisted of stretcha-
ble silicone rubber with two channels and a permeable
membrane, pretreated with collagen and Matrigel. The
stretchability of the membrane was exploited to actuate
peristalsis- like motions of the tissue (material selection
and fabrication). Intestinal organoids were cultured
from patient biopsy samples. Endothelial cells were cul-
tured on the other side of the membrane, to include the
functions of intestinal blood vessels. Peripheral blood
mononuclear cells were isolated from patient blood and
inserted into the bottom microchannel of the device to
act as blood vessels (selection of biological elements).
All incubation conditions, including flows and cyclic
stretching, were controlled by a commercially available
apparatus (supporting life inside the device). Various dif-
ferent read- outs, including on- chip fluorescent staining
and offline gene analysis, were used to assess enteric viral
infections in a single- OoC format.

Multi- organ OoC systems. A first multiple- organ system
on a chip was designed to mimic systemic distribution
of, and toxicity response to, the compound naphtha-
lene106. The device contained a combination of four
compartments representing the lung, liver, fat and other
tissues. The dimensions of the tissue compartments
and microchannels connecting them were specifically
designed to mimic systemic blood flow distribution
and residence times in the respective organs; after
passing through the lung, fluid flow was volumetrically

distributed to the fat (9%), liver (25%) and other tissue
(66%) compartments. The study was focused on mim-
icking the toxicity of naphthalene metabolites, generated
by the liver, on lung cells. The different compartments,
therefore, had essential interconnections in the form of
microchannels that allowed the distribution and metab-
olism  of  these  compounds  (conceptualization  and
design). The device was assembled from etched silicon
and machined PMMA, which yielded very well- defined
channels. These materials allowed for optical inspection
of the compartments on the chip (material selection and
fabrication). The lung and the liver compartments con-
tained rat cell lines, whereas the fat and other tissue com-
partments remained cell- free, thereby not participating
in the biological response but serving to better emulate
the proportion of drugs distributed to the biologically
active liver and lung compartments (selection of biolog-
ical elements). Peristaltic pumps were used to recirculate
media through the different organ compartments (sup-
porting life inside the device). The distribution, metab-
olism and toxicology of compounds could be studied
with this device. The introduction of a flow component
into conventionally static cell culture models allowed the
study of inter- organ interactions, which would not have
been possible in a non- OoC format. However, extrapola-
tion from this miniaturized rat- based system to humans
remained difficult. Today, it has become possible to use
human organoids or spheroids, or even simpler cell lines
of human origin, in this type of experiment to eliminate
the need to take species differences into account.

A  different  approach  for  a  multi- OoC  for  drug
metabolism was developed later, aimed at developing
a physiologically relevant multi- organ system for drug
discovery107 (fig. 3B). This system included four, seven or
ten organ models, which were coupled with integrated
fluidic circuitry to study organ interactions (concep-
tualization and design). This integrated device was
fabricated with easier to process polysulfone and poly-
urethane, with integrated air pressure- controlled valves
as built- in pumps to recirculate media in a more control-
lable fashion (material selection and fabrication). The
organs modelled were of human origin (primary cells,
from cell lines and iPSC- derived cells) and included the
kidney, muscle, liver and gut, amongst others (selection
of biological elements). The pumping system was incor-
porated into the final device, requiring only external air
pressure to regulate the valves by software (supporting
life inside the device). The drug diclofenac was admin-
istered to the gut section of this system, where it was
absorbed and, subsequently, distributed among the other
organ models. The complexity that this system allowed
was necessary to answer a more complex scientific ques-
tion, but was met with an increase in the complexity of
the peripheral system, with various pieces of supporting
equipment required (including a 36- channel pressure/
vacuum controller). This added complexity leads to
additional costs for setting up the system, and a large
laboratory footprint for a miniaturized system.

Another, different, approach for a multi- OoC was
reported for the efficacy and toxicity testing of various
anticancer agents108 (fig. 3C). This system contained a
reconfigurable design with multiple organs, including

 11

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
Aa  Integrated sensors

TEER

      Oﬄine measurement
Ac
      of soluble analytes

MEA

Cantilevers

LC/MS

Pump

Reservoir

OoC system

Commercial biomarker assay kits

Ab  Online measurement
      of soluble analytes

Ad  Live-cell imaging

O2

O2

B

Ba  Immunoﬂuorescence imaging

Bb Lysis + isolation kits

Western blotting
Western blotting
Western blotting
WWWW t

bl tti

RT-PCR, NGS

solid tumour- derived cells and leukaemia to study
effects of the anticancer agents on their target as well
as toxic effects on other organs (conceptualization and
design). The system was composed of PDMS, glass and
plastics, and so was easily fabricated (material selection
and fabrication). Cancer cell lines modelling various
malignant conditions were cultured in the OoC, similar

to other systems (selection of biological elements). The
device was pumpless, and hence more user- friendly as
it required fewer supporting machines (supporting life
inside the device). The entire device was placed on a
rocking shaker for gravity- induced recirculating flows,
thereby greatly reducing its laboratory footprint. A sys-
tem such as this is more suited for biological applications,

12 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: ◀

Fig. 4 | Collecting biological results from OoC systems. A | In situ measurements
during operation of a recirculating organ-on-a-chip (OoC) system allow for near real- time
assessment of cell states and functionality: integrated electrodes and cantilevers in OoC
devices can be configured to measure various electromechanical signals indicative of
transepithelial electrical resistance (TEER)127, electrophysiological signals using micro-
electrode arrays (MEAs)133 and cell/tissue contractility using cantilevers327 (part Aa);
integrated biochemical sensors in the OoC device can provide online measurement of
various soluble analytes, such as secreted proteins via immunosensors328 and dissolved
oxygen329 (part Ab); sampling of recirculating medium can be used for offline measure-
ment of soluble biomarkers using assay kits or liquid chromatography/mass spectrometry
(LC/MS) (part Ac); and device can be coupled to an optical set- up for live- cell imaging to
track cell functions such as migration330 (part Ad). B | End point measurements are often
used to interrogate cell states at transcriptome and protein levels: expression of specific
biomarkers can be imaged by immunohistochemical and/or cytochemical techniques
(part Ba); and cells or tissues in the OoC device can be lysed and further processed
for transcriptional and protein expression analysis (part Bb). NGS, next- generation
sequencing. Part Aa adapted with permission from ref.127, RSC, ref.133, Elsevier, and
ref.327, Elsevier. Part Ad adapted with permission from ref.330, PNAS.

with  less  emphasis  on  the  exact  manipulations  of
individual microchannels in the device.

In general, the use of single- OoCs has two phases.
In the first — preparatory — phase, biological elements
such as cells or organoids are introduced in the micro-
channels of the device. These living elements need time
in order to settle properly in the device. They may need
time to proliferate to confluency in the microchannels
(such as in the case of a barrier model), or for cell dif-
ferentiation into the cell types that occur in a particular
organ in vivo. In the second — experimentation — phase,
the device has matured enough in terms of physiological
relevance and functionality to be used in experimenta-
tion. Multi- OoC systems have the same two operational
phases. The different single- OoC compartments are usu-
ally cultured separately in the first phase. When each of
the single- OoCs has reached the required level of mat-
uration (which is dictated by the desired functionality),
the single- OoCs can be combined into an interconnected
multi- OoC with a common cell culture medium. After
combining all of the required elements in one multi- OoC
device in a sustainable fashion, the multi- OoC system
may be used for experimentation.

Results
OoC systems are complex and entail significant effort,
often with long experimental times (up to 28 days).
Being able to collect maximal information is important
and requires a combination of offline and in situ analy-
sis (fig. 4). When evaluating read- outs, it is important
to consider the timescale of measurement versus the
physiological timescale (which can be seconds to days),
the required spatial resolution on a system level and organ
level, and whether the measurement is quantitative or
qualitative. Measurements that are on the same timescale
as the physiological response are critical. For instance,
a change in cardiac conduction velocity can be meas-
ured in seconds, whereas changes in cell viability, if they
occur at all, may take many hours. For example, resolving
the propagation of action potentials in neural networks
not only requires sub- millisecond recording but also a
dense array of sensing points. Ideally, the read- outs can
be related to a relevant biological or clinical end point.
In vitro to in vivo extrapolation is key to understanding

the mechanism of action of a drug or chemical on the
body. Also, multi- organ systems monitored simultane-
ously with various organ- specific and local read- outs can
lead directly to mechanistic insights of the whole- body
response and organ resolution. In parti cular for drug
development, it allows the measurement of not only the
response of the target organ (the efficacy) but also side
effects on other organs (the toxicity)35.

Offline, online and in situ analysis
To profile OoC homeostasis and response to externally
applied chemical or physical stimuli, the intermittent
measurement of multiple compounds simultaneously is
highly desirable. Offline high- performance liquid chro-
matography/mass spectrometry (HPLC/MS) or multi-
plexed (bead- based) protein- binding/DNA- binding
assays often remain the most practical techniques in
this regard, as both allow measurement of a wide range
of different chemicals at the same time, of which many
are responsive biomarkers. Both offline approaches can
be performed in microlitre volumes of sample, which
are compatible with the flow rates commonly used in
one- pass perfusion, or removed periodically from recir-
culating medium circuits. Various commercial assay
kits can be used as an alternative for selected biomark-
ers (such as albumin, lactate dehydrogenase, alanine
amino transferase, aspartate aminotransferase and urea,
for liver systems), although possible interference due
to medium components (particularly serum) must be
carefully considered. In very low- volume systems, the
number of measurements that can be made with such
kits is quite limited, although new microarray techniques
allow use of very low volumes (<5 µl) and parallelization
of measurements (cell health assays).

Online or in situ measurements of the supernatant
can offer measurements of nutrients and metabolites
with minimal time delays. Small sensors are typically
used, based on optical detection exploiting dyes109.
In situ measurement of dissolved oxygen in OoCs has
been reviewed in detail110–112. Dissolved oxygen is a key
parameter in metabolism, especially in terms of CYP450
activity in the liver113–115. Dissolved oxygen and pH can
both be measured using microprobes or pH- sensitive
patches9. Optical detection requires the use of micro-
scopy or optical fibres; automated techniques to reduce
time and labour have been suggested116,117. Some analytes
such as glucose and lactate can be measured by using
electrochemical enzyme- based biosensors41,118. These
online, near continuous measurements are desirable
as periodic measurements may miss important fluctu-
ations in response. If sensors or patches are integrated
as arrays at close distance or in direct contact with tis-
sues structures, analyte concentrations can be spatially
resolved.

Measuring cell phenotype and function
Although biomarkers provide important biological
insights into the body’s response to drugs, cosmetics,
food ingredients and environmental exposure to chem-
icals, it is often the functional tissue response that
may be the most informative. Ideally, the functional
measurements are non- destructive and readily adapted

 13

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
Transepithelial electrical
resistance
(Teer). The electrical
resistance across a cell layer
or tissue layer. generally used
as a measure to determine
the overall integrity and
permeability of the cell/tissue
layer; a higher Teer indicates
better integrity or cell
confluency.

to in situ analysis, particularly in systems with contin-
uous recirculation of medium over extended periods
(such as 28 days). These measurements should also
provide rapid insights into responses — often within
minutes — in order to achieve relatively high temporal
resolution with respect to the timescale of the functions
being monitored.

End point analyses. Although highly informative when
it comes to cell status, gene and protein analyses in
OoCs are difficult to do online, and may require that
the device be dismantled to perform end point histol-
ogy, lytic assays, transcriptomics and even cell viabil-
ity assays119,120. A chip design concept that allows easy
removal of tissues with no detrimental effect on tissue
structure and morphology becomes essential in order to
obtain representative results as well as maintain spatial
organization of the cells in the tissue. Analysis of circu-
lating cells such as immune cells and tumour cells can be
done using medium samples taken from OoC devices121.
However, many microfluidic devices can destroy circu-
lating cells during experiments, so it is essential that
the fluid dynamics be considered during device design.
In other cases, cells have to be removed from the tissues
in the device. Techniques to remove cells without dam-
age do exist, but can be difficult to implement, requir-
ing expertise to perform. For effective quantification,
removal of all of the cells may be important so as not to
bias the results.

Microscopy and high- content imaging. Microscopy and
high- content imaging are among the most widespread
analytical methods in cell biology, and thus also the
most common measurement of cell and tissue function
is visual inspection in OoC devices. Most OoC devices
are constructed from optically transparent materials,
such as glass, PDMS and thermoplastics, and can be
constructed to fall within the imaging depth of con-
ventional epifluorescence or confocal microscopes. It is
thus possible to perform in situ staining of the cells and
tissues in- chip with fluorescent stains or antibodies to
assess cell viability or expression of specific biomarkers,
by using the microfluidic function of the OoC to deliver
the necessary reagents122.

In recent years, microscopy techniques including
confocal microscopy and light- sheet microscopy, as
well as imaging sample preparation protocols (clearing,
staining and so on) and analysis, have been signifi-
cantly advanced and adapted to deal with complex,
3D multicellular constructs. High- content imaging has
the strength to provide both spatial and temporal infor-
mation of cells and tissue morphology to help research-
ers untangle disease pathophysiology and assess novel
therapies more effectively. Microscopy in OoC systems
requires an optical window to the cells, along with a
design specification that allows placement and align-
ment of the OoC on a microscope stage. Successful
microscopy requires optimized matching of the tissue
model, preparation protocols (fixing, staining, clearing)
and microscopy method with the protocol for image
and data analysis123. Machine learning algorithms can
serve as a powerful tool to aid image and data analysis.

An example would be the use of deep learning convolu-
tional neural networks to track invasiveness of tumour
spheroids124.

Transepithelial  electrical  resistance.  Transepithelial
electrical resistance (TEER) is a commonly used tech-
nique to measure the integrity and permeability of any
barrier tissue (such as the gastrointestinal tract, the kid-
ney and the BBB). Native barrier tissues in the body have
TEER values associated with their function. The tight-
est barrier is the BBB with values of 1,500–8,000 Ω.cm2
(ref.125), whereas the proximal tube in the kidney has
a value of about 70 Ω.cm2 (ref.126). Organ and tissue
models should show physiologically accurate values.
In some cases, tissue models can give values far greater
than physiological values, whereas others fall short of
realistic values. The completeness of the model is a
determining factor in these situations, especially where
the physio logical system consists of several cell types and
the model uses only a subset of these.

The measurement of TEER values in microscale
systems can be done using the Ohm’s law method or
impedance spectroscopy, using either microelectrodes
integrated into the device during its fabrication127–129
or inserted into the device before an experiment129,130.
Impedance spectroscopy, when combined with a fitting
algorithm, provides a more accurate representation of
TEER values than the Ohm’s law method, whereas the
Ohm’s law method is easier to apply. Impedance spectro-
scopy further allows measurement of tissue size and
integrity131. For both types of measurement, the elec-
trodes must be placed accurately, and the surface area
used in the calculation must be appropriate as a uniform
current density must be generated throughout the entire
barrier tissue. Applications of TEER to OoC devices have
been reviewed previously128,132–134.

Microelectrode arrays and cantilevers. Other func-
tional measurements include microelectrode arrays
(MEAs) to measure electrical activity in cells and tis-
sues, and cantilevers to measure force generation by
cells133,135. The MEA system is much more suitable for
application to OoCs than the patch clamp. This method
typically relies on a 2D array of cells that allows, using
the heart as an example, estimates of conduction veloc-
ity, beat frequency and field potential duration as an
analogue for the QT interval136. MEAs can be applied
to the heart, neuromuscular junctions, skeletal muscle
contractions and neuronal systems137–140. For instance,
action potential propagation between presynaptic and
postsynaptic chambers connected by microtunnels has
been described141. Mechanical forces such as contractile
force generation by cells and/or tissues is also critical
to many organ functions. They can be measured non-
destructively and in near real time by integrating micro-
cantilevers in OoC devices, in which cells are patterned
onto silicon cantilevers with optical or electronical
detection of their deflection142,143. Meanwhile, a recent
study showed that both MEAs and electrodes for TEER
measurements can be integrated into chips during their
fabrication to achieve multiple functional measurement
in a TEER–MEA heart chip144.

14 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: The choice of read- outs will depend heavily on the
issues to be addressed. Generally speaking, the advan-
tage of most OoC in vitro systems is that they are easier
to probe directly than animal models are, irrespective
of the analytical approach chosen. OoCs lend themselves
to microscopic imaging and small- volume sampling
for both offline and online analysis. There has been a
remarkable upsurge recently in the availability of small
sensors for real- time probing of biological systems. Their
application to real- time in situ monitoring of incuba-
tion conditions, biomarkers and organ function in OoC
has obvious advantages not only for the development of
improved OoC but also for the range of experiments that
become possible with OoC systems.

Applications
The majority of OoCs are developed with an intended
application in mind. In this section, we highlight the
various advantageous features of current OoCs for use
by commercial organizations interested in testing and
predicting compound efficacy and side effects, and bio-
logical researchers looking to use OoCs to mimic the
complexity of normal or diseased states in humans.

Most OoC prototypes at the pre- commercialization
developmental stage generally cannot fulfil the dual
purposes of multiplexing and biological complexity
simultaneously. As an in vitro system, OoCs also can-
not comprehensively capture the entire physiology of an
organ or body. Hence, the final commercialized form
factor of an OoC system is often informed by the tis-
sue functions and read- outs that are essential for the
intended application (fig. 5). Consequently, one should
discern between the necessary and desirable features of
an OoC device at different stages of its translational pro-
cess. This should ideally be done in consultation with the
intended end users.

Commercial compound testing
Pharmaceutical and chemical compounds. Commercial
use of OoC systems has been focused primarily on drug
development36,145–147. The ability to estimate both efficacy
and toxicity for humans in preclinical trials is a huge
advantage in allowing a company to choose candidates
that have a higher chance of becoming approved drugs.
OoC systems can be used throughout preclinical and
clinical trials, and coupling OoCs with physiologically
based pharmacokinetic (PK) or pharmacodynamic (PD)
models offers a rational basis to guide this process37.

The appropriate OoC system changes from rela-
tively simple to increasingly complex due to the differ-
ent goals of each stage of drug development. Typically,
simpler and more highly focused systems that provide
relatively high throughput are needed in mid- preclinical
trials, whereas multi- organ human- based models are
needed towards the end of preclinical trials to predict
both efficacy and toxicity. The complexity is not only in
the device itself and integrated analytics but also in the
complexity of the biological organ module. The major-
ity of OoC companies focus on single- organ modules,
although some provide multi- organ systems. Human
multi- organ models alone or when coupled with a math-
ematical model37,148–150 have the potential to provide both

efficacy and toxicity information on human response in
preclinical studies108.

There are numerous issues in terms of scaling data of
a multi- organ OoC system to predict human response,
including direct scaling, residence time- based scaling,
allometric scaling and multifunctional scaling140,151–153.
Each of these approaches has advantages, although
residence- time approaches are the simplest to use. The
residence time, defined as the volume of the reactor
divided by the total flow rate, is easily applied and con-
trols the degree of conversion of a reactant and formation
of metabolites independent of reactor size (which can
range from a few microlitres up to tens of thousands of
litres). A residence- time approach should be effective if
the microphysiological system uses organ chambers sized
to be in correct physiological ratios with an appropriate
ratio of flow of a blood surrogate to each organ.

Biomaterial testing. Many medical treatment modali-
ties rely on the use of biomaterials, including surgical
and medical devices (such as catheters, surgical plates,
screws or extracorporeal systems), implants and artificial
tissue replacements. OoC platforms can be used to study
the biocompatibility and efficacy of biomaterials in an
environ ment that is representative of the (patho)physio-
logy of the organ or tissue to be replaced, repaired or
regenerated. An important consideration is the integra-
tion of various biomaterials into the microfluidic OoC
systems for fast and parallelized biocompatibility or bio-
functionality testing154,155. Numerous different solutions
for facile and versatile integration of biomaterials of
various geometries156,157 or bonding strategies have been
reported158. Biomaterial samples that have to be inte-
grated into OoC systems require miniaturization, which
may be challenging for some material types. Moreover,
it is important to prove that the effects observed with
miniaturized samples are representative of the situation
in the body.

The ability of OoC systems to achieve precise control
of environmental factors are of great use for understand-
ing structural–functional relationships of a biomaterial.
By controlling the presentation of various cell micro-
environmental cues in the OoC, one can conduct a
systematic study of how these environmental factors
interact with specific biomaterial properties, such as
roughness159,160, stiffness161,162, wettability163 and topo-
graphy164–167, which in turn regulate cells’ behaviours,
such as adhesion, proliferation and differentiation on
the biomaterial.

Biological research
Disease modelling. The use of OoC systems for disease
modelling enables the investigation of both inherited
and acquired disease in a human setting, overcoming
inter- species differences that hamper data extrapola-
tion. Specifically, many of the genetic networks impli-
cated in human disease differ substantially between
human and murine models, the most common animal
model deployed, which greatly limits their utility for
disease modelling168. Similarly, the immune systems of
mice and humans show significant differences in both
innate and adaptive immunity, limiting their use in

 15

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
A  Hepatoxicity testing

B  Drug/therapeutics bioactivation

Ac

3D liver OrganoPlate
(MIMETAS)

Ba   Nutraceutical bioactivation
        (liver–vascular)

Aa

PEARL array
(CellASIC)

Ab

Robotox
system

Ad

Perfused liver
multiwell plate

Ae

Liver chip
(Emulate)

Bb  Embryotoxicity
         (liver-EBs)

Biological complexity

Microstructure-
supported 3D
culture

Collagen-
sandwich
culture

Mixed 3D
spheroids

Microstructure-
supported mixed
3D cultures

Parenchymal–vascular
compartmentalized
cultures

Entire chamber
ﬂuidically linked

Vascular compartments
ﬂuidically linked

Monocultures

Multicell cultures

Multi-organ OoCs

C  Disease modelling

D  PDPK studies

Ca  NASH model
        (InSphero)

Cb   NAFLD model

Da  Human-on-a-chip
        (Hesperos)

Db  Microphysiological
        system

c Liver metastasis mode
Cc  Liver metastasis model
       (CN Bio)

Cd  Liver–pancreas
       diabetic model
       (TissUse)

Dc  Human Emulation System (Emulate)

evaluating immune- related diseases such as multiple
sclerosis169. OoC systems provide a human- specific
experimental platform to mechanistically study human
diseases with complex aetiologies because they can inte-
grate genetic factors (through use of patient- derived
or genetically engineered stem cells harbouring the

disease- driving genetic mutations or predispositions),
environmental factors (such as exposure to drugs or
mechanical stresses170 through precise control over the
cell microenvironment) and systemic crosstalk with
other organ systems, including immune cells and the
microbiome (through engineering multi- OoCs with

16 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: ◀

Fig. 5 | Biological complexity and form factor of an OoC system. Complexity and
form factor of OoCs are dependent on its intended application as illustrated by the
liver OoC. Different applications of liver OoC may require varying complexity in culture
configuration from hepatocyte monocultures to co- culture with other hepatic cells that
better mimic liver physiology. Aa–e | Toxicology testing requires multiplexed arrays for
increased throughput. Ba–b | Liver OoCs that mimic liver- bioactivation of drugs or
nutraceuticals involved co- culturing liver with the tissue targeted by the drug. Ca–d | Liver
disease models often require increased biological complexity with both parenchymal
and non- parenchymal cells to recapitulate disease mechanisms. Da–c | Drug pharmaco-
dynamics (PD) and pharma cokinetics (PK) models will include the liver OoC as the
metabolizing organ along side other organs involved in drug absorption, distribution
and excretion connected in a recirculating circuit. EBs, embryoid bodies; NAFLD,
non-alcoholic fatty liver disease; NASH, non- alcoholic steatohepatitis; PEARL, perfusion
array liver system. Part Aa adap ted from ref.331, CC BY 3.0 (https://creativecommons.org/
licenses/by/3.0/). Part Ab adapted with permission from ref.332, Elsevier. Part Ac adapted
from ref.333, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Part Ad adapted
with permission from ref.334, RSC. Part Ae ©Emulate. Part Ba adapted with permission
from ref.77, RSC. Part Bb adapted from ref.335, CC BY 4.0 (https://creativecommons.org/
licenses/by/4.0/). Part Ca courtesy of InSphero AG, Schlieren. Part Cb adapted with
permission from ref.336, Wiley. Part Cc “PhysioMimix™ Liver- on- a- Chip (MPS- LC12)
consumable plate”. Part Cd adapted from ref.303, CC BY 4.0 (https://creativecommons.org/
licenses/by/4.0/). Part Da adapted from ref.337, Springer Nature Limited. Part Db adapted
from ref.107, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

recirculatory flows). There are already some demon-
strated examples where OoC systems have been able to
demonstrate the importance of interplay between differ-
ent aetiological factors in the manifestation of clinically
relevant disease phenotypes. For example, engineered
heart tissues made from diseased cells harbouring a des-
moplakin mutation only show clinical arrhythmogenic
cardiomyopathy when exposed to dynamic mechani-
cal loading171. Another example demonstrated that the
inclusion of regulatory T cells and T helper 17 immune
cells and environmental agents (short- chain fatty acids)
into a gut–liver multi- OoC could successfully recapitu-
late paradoxical modulation of inflammatory bowel
disease that was dependent on activated CD4+ T cells172.
The development of disease models is of increasing
importance for the clinical development of efficacious
therapeutics and provides a model for rare diseases where
clinical development and trials may be limited by small
patient cohorts. Additionally, OoC platforms can ena-
ble studies of systemic disease in the human setting for
diseases that currently have minimal other models avail-
able, including cancer metastasis, inflammation, fibrosis
and ageing. It is expected that the inherent complexity
of systemic diseases can be mechanistically evaluated
to a greater extent as multi- OoC technol ogy continues to
advance. To fully attain this, OoC platforms should be
developed in a way that enables spatio-temporal tracking
of cell and tissue states, modularity to enable multi- tissue
studies for systemic diseases, inclusion of functional
stromal cell populations that drive disease progression
(such as immune cells, fibroblasts and vasculature) and
validated disease cell sources. Benchmarking of diseased
cells against healthy cells in the same system should serve
as a control to interpret the differences in the diseased
phenotype from those related to the in vitro setting.
Biomarkers of clinical relevance should similarly be eval-
uated within the OoC platforms, enabling a more direct
comparison with the clinical phenotype for enhanced
benchmarking of platform utility.

Probing and mimicking the cell microenvironment.
Microenvironmental control of cells is a well- established
concept in cell biology. OoC systems have been used
extensively to manipulate different environmental fac-
tors (such as shear stress, autocrine/paracrine soluble
factors, cell–cell and cell–ECM interactions) at physiol-
ogically relevant length and timescales so as to elucidate
their effects on cell phenotypes and functions. This idea
is particularly well demonstrated in the context of the
stem cell and tumour microenvironments, as evidenced
by the number of reviews on these topics173–176. We cover
some of the common design strategies that are used in
OoC devices to control and probe the functional roles
of biochemical and mechanical environmental factors.

Soluble biochemical factors, such as morphogens and
cytokines, can be controlled in OoC systems by manipu-
lating fluid mass transport properties at microscale res-
olution, and therefore OoC systems offer a more precise
method to study the effects of paracrine and autocrine
signalling compared with conventional techniques, such
as conditioned medium or changing cell density177. By
selectively changing channel dimensions and flow veloc-
ity, one can tune between diffusion- dominated (Pe < 1)
transport, where secreted factors remain in the cell vicin-
ity for binding to receptors, and convection- dominated
transport, where secreted factors are removed from the
cell vicinity177. Soluble factors can also be applied exoge-
nously to microfluidic cell cultures with spatio- temporal
control over the concentrations and compositions that
cells are exposed to. This is often accomplished by cou-
pling a convection- based concentration gradient gener-
ator178,179 or combinatorial mixer180,181 to the cell culture
chambers. Alternatively, static diffusion- based gradi-
ents can be applied to shear- sensitive cell types without
exposing them to direct flow. This can be achieved by
sandwiching a porous matrix between the source and
sink reservoirs182 or balancing the pressures between
multiple channels that feed into a static chamber where
concentration gradients are being established178,179,183.

Devices that are designed to study cell–cell inter-
actions often attempt to control the spatial localization
and relative abundance of different cell types using cell
patterning184–186 or geometrical microstructures (such as
microwells) to physically constrain the cells187,188. This
allows for better control over the number of interacting
partners as well as the spatio- temporal dynamics of the
interaction process compared with random co- cultures.
Control over cell–cell and cell–ECM interactions becomes
coupled when using cell patterning techniques to modu-
late the number of neighbouring cells because this is
reliant on patterning adhesive ECM proteins on the sub-
strates to which the cells then attach. Proper experimental
designs to vary cell–cell interactions while maintaining
cell–ECM interactions to be consistent, such as uniform
coating with a well- defined ECM protein such as fibro-
nectin, can help circumvent this problem. OoC devices for
probing cell–ECM interactions aim to modulate either the
biochemical composition of the ECM proteins being pat-
terned onto the substrate189 or the substrate’s mechanical
properties, such as stiffness or topography. The latter usu-
ally involves replacing glass with other materials — such
as PDMS or polyacrylamide hydrogel — as the cell culture

 17

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
Excitation threshold
The minimal electrical
potential required for the
tissue to contract in response
to electrical signal.

Maximum capture rate
The highest beat rate that
is the maximum rate of
synchronous contraction
under an electric field voltage
corresponding to twice the
excitation threshold.

substrates in the OoC device, whereby the stiffness190,191
or surface topographies192,193 of the substrates can be
precisely controlled.

OoC devices are well suited for applying a range of
physical environmental stimuli on cells. As fluid flow is
inherent in many OoC systems, these systems are used
to mimic physiological shear stresses exerted by blood
and interstitial fluids. By designing multiplexed chan-
nels with varying geometries, one can simultaneously
apply shear stress over a range of magnitudes to probe
the effects of shear stress on cell proliferation, differen-
tiation and functions119,194,195. Alternatively, fluid shear is
used to enhance the functional maturity of microvascula-
tures in many organotypic tissues. OoC devices can also
be designed to apply mechanical tensile or compressive
forces to cells for mimicking breathing- induced stretch-
ing of the airway, peristalsis- like motions of the gut or
contractility of cardiac tissues196. This is often achieved
by growing cells on thin flexible PDMS membranes that
are incorporated into the OoC device such that they can
be flexed cyclically by vacuum or pressure pneumatic
actuators. To better recapitulate the electrophysiological
functions of neural and cardiac tissues, electrical stimula-
tion has been built into OoC devices by integrating in situ
MEAs that are microfabricated as part of the device197 or
electrodes that are inserted into the OoC system196.

Single- organ tissue functions
Liver. The cell source, composition and culture configu-
ration of the liver OoC dictates the extent of liver- specific
functions that the device can recapitulate198–200. Key liver-
specific functions that should be present in in vitro liver
models include expression of phase I or II metabolizing
enzymes (such as CYP450, UGT and GST), albumin
synthesis and biliary excretory functions201,202. Ideally,
the synthetic and metabolic functions of liver OoCs —
characterized by albumin secretion levels and CYP450
activities, respectively — should be benchmarked to
that of freshly thawed cryopreserved primary human
hepato cytes over different culture periods. This provides
a clear indication of the application utility of the liver
OoC system (together with the selected choice of cell
source such as iPSC- derived hepatocytes) as cryopre-
served primary human hepatocytes are currently the
gold standard in drug metabolism studies203. Hepato-
cyte mono cultures in a conducive configuration, such as
3D spheroid and sandwich cultures, can maintain syn-
thetic and metabolic functions for a short period of
time (3–7 days) and, to some extent, exhibit hepatocyte
repolarization and biliary excretory functions204–208.
Co- cultures with non- parenchymal liver cells such as
liver sinusoidal endothelial cells, Kupffer cells and hepatic
stellate cells are essential for longer- term (~14 days)
maintenance of metabolic and synthetic functions and
enhanced biliary excretion72,209–212. These multi- culture
liver OoCs can more comprehensively capture the full
repertoire of liver- specific functions important for more
accurate prediction of human responses in both pharma-
ceutical preclinical testing and liver disease modelling.
Kupffer and stellate cells aid in modelling non- alcoholic
fatty liver disease and liver cancer because these dis-
eases often involve inflammation and fibrosis processes

mediated by liver- specific macrophages (Kupffer cells)
and pericytes (stellate cells)212,213.

Heart. Cardiac OoCs should ideally facilitate the matura-
tion of cardiomyocytes and their coupling with support-
ing cells. The two functions to aim for are the robust and
synchronous contractile function and electrical activity
associated with a positive force–frequency relationship
and fast calcium handling. These functions are evaluated
using a set of key read- outs that include the beat rate, force
of contraction, excitation threshold, maximum capture rate
and conduction velocity. To achieve electromechanical
maturity, heart tissues need to display adult- like gene
expression profiles, ultrastructure (orderly registers of
sarcomeres, high density of mitochondria, networks
of transverse tubules) and oxidative metabolism.

The choice of cell source, culture configuration and
environmental stimulus all have a profound impact on
recapitulating a functional cardiac tissue. For a long
time, immature phenotypes of human heart muscle
derived from iPSCs have limited their utility for bio-
logical and medical research. Human heart muscle has
been grown from iPSC- derived cardiomyocytes and
fibroblasts in hydrogel anchored at the two ends that
also allowed the measurement of the contraction force
through the deflection of PDMS posts or cantilevers.
Electrical stimulation applied with gradually increasing
intensity, causing macroscopic contractions of the form-
ing muscle, has markedly advanced tissue maturation214.
Other studies have shown that the atrial versus ventricu-
lar specification of engineered cardiac tissues could be
achieved by gradually increasing the stimulation fre-
quency215. Both tissue models were used to investigate
genetic and acquired cardiac diseases.

BBB and nervous tissues. The BBB is an important struc-
ture that maintains brain homeostasis and protects the
brain from exposure to molecules or pathogens that are
circulating in the bloodstream. Drugs for brain diseases
need to cross this barrier to arrive at the site of action,
whereas other drugs should not cross the BBB58,216. BBB
OoCs need to recapitulate the function of this specialized
barrier tissue by recreating the compartmentalization of
multiple cell types. BBB OoCs often consist of two com-
partments separated by a thin membrane, with the vas-
culature compartment lined with brain endothelial cells,
whereas the brain compartment is formed with pericytes
and astrocytes57,217–219. TEER values across BBB OoCs are
typically obtained as a measure of barrier integrity. BBB
OoCs should be engineered to have TEER values that fall
within the appropriate range (~1,500–8,000 Ω.cm2) for it
to have physiological value in functional drug studies or
disease modelling. Performing studies across longer time
frames requires culturing the BBB OoCs in hypoxic con-
ditions to maintain BBB integrity for longer periods of
time (up to a week). In comparison, BBB OoC cultures
in normoxia lost barrier integrity after 2 days220.

Spinal cord OoCs recreate the blood–spinal cord
barrier similar to BBB chips. Although spinal cord
OoCs may share a similar compartmentalized design
as BBB OoCs due to the similar roles of the blood–
spinal cord barrier and BBB, key biological differences

18 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: prevent interchangeable use221. Rather than using per-
icytes and astrocytes in the brain compartment, spinal
cord OoCs incorporate cells that can differentiate into
spinal motor neurons, such as iPSC- derived spinal
neural progenitor cells25.

Applications involving neurotoxicity testing or mod-
elling human brain diseases will require OoC systems
that not only maintain the survival of neurons and
glial cells but also their electrophysiological functions.
Electrophysiological functions from neurons can typi-
cally be visualized through calcium fluxes, whereas the
presence of glial cells can be checked by screening for
their respective neural markers. Major central nervous
system glial cell types include astrocytes and microglia,
which can be identified by screening for GFAP and
CD45, respectively. Myelin- producing cell types include
oligodendrocytes in the central nervous system and
Schwann cells in the peripheral nervous system, both
of which can be characterized by screening for myelin
basic protein222. Recapitulation of fully functional neu-
ral networks in vitro from isolated cells is extremely
challenging due to the complex cellular organization of
brain tissues, and so OoC systems increasingly look to
integrate organotypic models such as brain organoids or
organotypic brain slices223–225 instead of single cells226–228.
Peripheral nervous system OoCs or nerve OoCs mostly
focus on strategies and culture configurations that pro-
mote motor neuron regeneration as indicated by neu-
rite growth and myelination by Schwann cells229, which
can then be applied to see how drugs230 or pathogens231
modulate these processes.

Epithelium. Epithelium forms a protective layer on the
upper respiratory tract, skin and the corneal layer of the
eye, while also serving to facilitate the exchange of sub-
stances in the gut and lung. Most epithelium OoC systems
for the respiratory tract10,232–236, skin73,237–239, gut14,55,240,241
and cornea242–244 have a multi- compartment design
where two distinct fluidic channels are separated by a
porous membrane or hydrogel. Epithelial cells from the
res pective organs are then used to seed one side of
the porous membrane to mimic the epithelial layer. For
airway and skin OoCs, the epithelium is cultured under
an air–liquid interface to mimic in vivo conditions10,245.
Epithelial barrier functions can be characterized in multi-
ple ways, the first of which is to screen for tight junction
markers such as claudin and occludin, which are ubi-
quitous in all epithelia246. Another way is to charac terize
the TEER across the epithelium barrier, similar to that
of BBB OoCs. Compared with BBB OoCs, in vivo TEER
reference values are not currently very well character-
ized for epithelial tissues. In vitro TEER values, on the
other hand, have been obtained for lung- on- chip (500–
900 Ω.cm2)10,247,248, gut-on-chip (400–4,000 Ω.cm2)14,249,250,
skin- on- chip (1,000–6,000 Ω.cm2)239,251,252 and cornea-
on- chip (500–1,000 Ω.cm2)242,244,253. The large variation
in TEER values for gut- on- chip and skin- on- chip could
be due to variations in the cell source and microenviron-
mental culture conditions used in the different OoC
models. Epithelium of the lung, gut and cornea are con-
stantly exposed to mechanical forces within the body,
namely cyclic stretching during lung respiration and gut

peristalsis, along with blinking- generated shear stresses
in the cornea. Exposure to these mechanical forces has
been shown to greatly improve epithelium maturity of
on- chip skin237,239, gut14,241 and cornea242. Other functional
characteristics of the epithelium include mucus secretion
by goblet cells232–235 and the presence of specialized pro-
trusion structures on the epithelium surfaces, namely
beating cilia on the upper airway epithelium that sweep
mucous- coated foreign particles out of the airway232,235,
and villus crypt- like structures on the gut epithelium to
increase the surface area for nutrient absorption14,55,241.
In the case of the skin, multiple layers of epithelium
stack above one another to produce a stratified layer that
contributes to the protective properties of skin254.

Multi- organ functions in ADME- Tox
Predicting human ADME- Tox in preclinical trials using
an OoC system (most likely with physiologically based
PK models) allows measurement of the response of the
target organ (the efficacy) as well as any side effects on
other organs (the toxicity)35,255. Many organ functions
need to be considered for drug ADME- Tox applications.
Absorption of drugs can occur not only through the gut
but also the skin, lungs and direct injection, and all of
these have been modelled with multi- organ OoC systems.
Adipose tissue is particularly important for distribution of
lipophilic compounds256 and is, unfortunately, neglected
in many multi- organ microphysiological models. For a
multi- OoC model to mimic distribution of any chemi-
cal or drug, a compartment for other tissues is necessary
to capture the retention of any compound in tissues not
specifically included in the model; no OoC system can
explicitly capture every organ or tissue type in the body257.
Further adsorption/absorption occurs through internal
barriers such as the BBB and these are critical to consider.
The liver is essential as it is the primary site for metabo-
lism, although the gut is also important as it houses many
of the CYP450 enzymes and a gut–liver model is particu-
larly important for orally ingested drugs and chemicals258.
Although elimination occurs through several routes, the
kidney is particularly important and also a challenge
to fully model; many kidney OoC models focus on the
proximal tube, but neglect other aspects of kidney oper-
ation259,260. Toxicological side effects can occur in many
tissues although toxicity in the liver, heart, kidney, bone
marrow and immune systems are the most common.
Thus, a multi- organ OoC system that can accurately cap-
ture multiple aspects of ADME- Tox is quite demanding.
Many multi- organ OoC systems focus on some selected
aspects of ADME- Tox using only 3 or 4 organs, although
it is possible to construct and operate a multi- organ OoC
system with up to 14 organ compartments261.

Reproducibility and data deposition
Development and deployment of OoCs require the coor-
dination of various multidisciplinary elements, such as
cells, biomaterials, engineering controls, interconnects
and sensors. Reproducibility of OoC systems largely
depends on the correct matching and interplay of the dif-
ferent elements as well as their isolated reproducibility.
The more variability single elements present, the more
the error propagates, and the more difficult consistent

 19

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
outcomes become. In general, modularity and the pos-
sibility of individual and timed quality control of the sin-
gle elements greatly increases system yield and directly
dependent reproducibility of experiments using OoC
systems. Understanding robustness and producing data
of statistical relevance additionally require a minimal
number of replicates per conditions. Increasing physio-
logical complexity needs consideration of operational
complexity and potential limited scalability.

Sources of variability
A major challenge for reproducibility consists of min-
imizing system or background variability to maxi-
mally resolve the systems’ responses to stimuli and test
parameters, such as compounds or mechanical cues. The
manufacturing and assembly of microfluidic chips and
components need to adhere to operation processes —
in which checklists are used to verify dimensions and
device characteristics, and their compliance with pre-
defined specifications — rather than relying on manual
fabrication processes. PDMS replica moulding used for
prototyping provides great design flexibility and short
iteration times to explore new approaches and is cen-
tral in the early stage of the product life cycle. The over-
all manual process and assembly tends to have a high
user dependency and laboratory dependency, making
reproducibility more challenging. Industrial processes
such as injection moulding are highly standardized,
thus enabling reproducible mass fabrication; however,
they require a substantial initial investment fixing the
device design, and have some feature restrictions (min-
imal dimensions, limited aspect ratio, de- moulding
draft). It is thus important that developers keep these
requirements and limitations of industrial manufac-
turing processes in mind to ensure transferability once
design features of prototypes are set and commercializa-
tion becomes an option262. Variability increases with the
number of components of a system. Process monitor-
ing sensors and their feedback to flow, temperature and
gas concentration control ensure stability in long- term
experiments263.

The central — and also most variable — components
are the cells and tissues and their extracellular natural or
synthetic matrix or scaffold. Cell line sourcing, cultur-
ing and expansion can be well controlled and has been
thoroughly characterized over the years, but the physio-
logical relevance of cell lines is limited in OoC systems
and they show genetic instability2. Primary cells closely
resemble their tissue of origin. Optimized culturing
protocols and the embedding of primary cells in a near
in vivo environment as, for example, stroma, ECM and so
on have resulted in increased lifespan of the cells and
preserved tissue- specific function and phenotype. Major
challenges lie in ensuring continuous access and control
of donor- to- donor variability and batch- to- batch variability.
Adult stem cells or pluripotent stem cells can be expan-
ded indefinitely in culture and can give rise to many cell
types. Substantial effort is made to reduce line- to- line
variability across different iPSC lines and ensure better
maturation of differentiated derivatives. Ensuring repro-
ducibility on the cell level, tissue level and biomaterial
level require staged quality and functional control of

the source material, before it is introduced into the OoC
system prior to an experiment. Quality standards and
procedures are currently being discussed and need to be
defined in a tissue- specific manner.

Technical issues such as bubbles and contamination
are a major challenge to reproducibility in device set- up
and operation. System assembly and initialization need
to follow defined protocols with minimal user depend-
ency. Transferring the majority of processes to robotic
systems is preferred. Predefined kits including all mate-
rials and cells or assay- ready products that are shipped
ready to use are options for simplifying or even elimi-
nating OoC device assembly and preparation prior to
the actual experiment for the end user.

Standardization
Standardization is a central tool to ensure reproducibil-
ity in an OoC system’s internal interfaces (cell–surface
interactions and matrix composition), as well as its
external interfaces. These external interfaces include,
but are not limited to, external instruments such as liq-
uid handling, plate automation, operation systems and
read- out instruments including microscopy and analy-
tical instruments; interfaces to other OoC devices to
create higher- order multi- tissue systems by their con-
nection though tubing or liquid ports; comparability on
the functional level and experimental outcome of dif-
ferent organ- on- a- chip systems representing the same
organ type (between systems, between laboratories, over
time and with respect to historical data); data outcome
structure, format and conditions as inputs to in silico
models; and data format and content allowing transla-
tion to clinical and animal data. Defining tissue- specific
functional parameters with unified normalization and
commonly agreed reference compounds is a current pro-
ject for different overarching organizations (for example,
ECVAM264–266, IQ- MPS, NA3Rs).

Standardization has to be implemented on differ-
ent levels. Cell- based and technical standards will help
improve compatibility between instruments and ensure
reliable operation and controlled supply chains. Organ
type- based  standards,  such  as  defined  functional
parameters, minimal requirements on viability and
lifetime or standardized quality criteria, allow better
selection and compatibility between different providers
as well as better fitting the purpose. Finally, the sys-
tem’s quality and performance need to comply with
application- based standards, including for example a
correct prediction of liver toxicity of a set of reference
compounds or true replication of a mechanism of action
of a substance.

Data and validation
The wide range of available OoC devices and approaches
requires the production and accessibility of reference
compound and clinical data for verifying and validating
findings. The public availability of this type of data will
enable comparison of different OoC devices in order to
select the best system for a given study, and for regu-
latory bodies to classify and value data originating from
OoC systems. An example is the University of Pittsburgh
Microphysiology Systems Database (MPS Db), which

Donor- to- donor variability
Variation in phenotypes and
functions of primary cells that
are due to inherent genetic and
physiological differences (such
as age, sex, ethnicity) between
the donors.

Batch- to- batch variability
Variation that arises from
in vitro cell culture processes,
such as cell expansion and
differentiation. As cell culture
is a batch process (as opposed
to a continuous process),
variation can arise due to
different operators, equipment
and reagent sources used
across the different batches.

Line- to- line variability
Variation that exists between
different induced pluripotent
stem cell (iPSC) lines due to the
inter- patient heterogeneity
from which the iPSC lines are
derived.

20 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: has been designed to aggregate, manage and integrate
data obtained from OoC systems with human and ani-
mal exposure data. Data included in the MPS Db pertain
to tissue- specific functional biomarkers, tissue morpho-
logy, transcriptomics and proteomics. Reference data for
preclinical assays must be reported in assay- specific for-
mats, such as dose–response curves including commonly
used analysis parameters such as the half- maximal
inhibitory concentration (IC50).

Reporting standards
There are currently no specific reporting standards that
have been agreed. However, to enhance academic pro-
gress and further the development of OoCs, it would be
preferred to publish experimental details as completely as
possible. Deposition of experimental raw data including
metadata into a central space should enable other labo-
ratories to reproduce results. An example of information
that should be shared is the reporting of cell lines, the
exact medium composition for culturing, precise incuba-
tion times, local cell culture practices, the batch of serum
used and passage numbers used, all of which influence
cell phenotype and organ functions. Another example
is reporting on the selection of the region of interest —
both spatially and temporally. This becomes necessary
if it is not possible to extract information from the com-
plete device, and if the region is not representative of the
entire OoC, it could yield biased results.

Some  of  the  challenges  and  opportunities  were
outlined in a recent international consortium effort to
standardize and report minimal information for exper-
iments in 3D cell culture267. Even the most basic of infor-
mation needed for reproducibility such as media type
are often unreported or ambiguous. For example, the
properties of a 3D cell spheroid are completely differ-
ent depending on whether the same culture medium,
DMEM, contains high or low glucose formulation; this
detail is often missing in publications. When experi-
mental protocols are shared and followed, variability
is significantly reduced, although still not completely
eliminated, even with cell line culture. Given the system
complexity of OoCs, development of reporting stand-
ards is even more significant and challenging than it is
for 3D cell culture. Advances in standardized commer-
cial OoC hardware, defined media and human- relevant
iPSCs enable a broader availability and are helping the
community to base their research on a common ground.
Based on this, there is currently a high need for devel-
oping basic and application- specific assay protocols and
minimal experiment information reporting standards
for OoCs.

Limitations and optimizations
OoCs  are  useful  in  vitro  models  bridging  the  gap
between conventional cell cultures and animal models or
human subjects. Although many organ systems and their
functions can be modelled using OoC devices, the phys-
iological relevance of OoCs is generally less validated
than that of organoids and other in vitro models268. To
match the existing capabilities of OoC technology with
the best applications, it is important to understand some
of their current limitations and challenges for the field269:

OoC designs, manufacturing and operating procedures
have not yet been standardized, and so end users need
to invest time and resources to set up the system and
customize the testing assays, which inevitably limits the
experimental throughput of OoCs; data acquisition from
OoC systems remains overly reliant on end point assays,
which limits the spatio- temporal resolution of biological
information that is important to minimize the effects of
sample- to- sample variability and allow dynamic studies;
and biological information extracted from OoCs needs
to be validated with those of existing in vitro and animal
models to determine how accurately OoCs can mimic
human responses.

Although OoCs promise to simulate human physio-
logical processes, there are engineering limitations to
reaching the full complexity of human physiology. The
numbers of vessels, tubes and ducts in human tissues
and organs are still too complex to be fully recreated in
engineered systems. Even relatively simple channel net-
works can be challenging to operate robustly and effi-
ciently with throughput required to cover variabilities
that arise from biological heterogeneity. To contribute to
discovery- driven research and drug discovery, the high
cost of OoCs typically necessitates prescreening to create
a smaller pool of test conditions or candidate molecules
in advance.

Many  OoC  system  designs  and  operations  are
focused on trying to reproduce physiological tissue
architectures and functions, and therefore less empha-
sis is placed on testing assays and read- outs. However,
for OoCs to be routinely deployed for standardized
testing of drugs and chemicals, such as those stipulated
in OECD testing guidelines, the compatibility of the
designed OoCs with common laboratory instruments
for data acquisition and downstream analyses is an
important practical consideration. If OoC devices can
be designed to have reagent interfacing and cell imag-
ing layouts that are similar to those of standard culture
plasticware and glassware, the technology will be more
approachable for biological end users as the workflow
and associated hardware and software for analyses would
be familiar and mostly already present in the laboratory.
An example involves fitting 20 microfluidic devices in
a 96- well PS plate and using a plate reader to quantify
luminescence in each device270.

Manually connecting devices to pumps can be chal-
lenging and decrease instrument compatibility. Use
of gravity- driven flow — which can be established by
tilting a device back and forth to drive fluid between
two reservoirs at different ends of the device — can
eliminate  the  need  for  external  tubing  and  reduce
the risk of introducing hard to remove bubbles in the
circuit219,270,271. Use of such gravity- driven flow, however,
may introduce unwanted variability or bidirectional
shear to the cells. An alternative strategy is to implement
bespoke periphery benchtop instruments with graphical
user interfaces to automate and scale up liquid handling
in OoC devices89,107.

In terms of data collection, many commercial analy-
sis tools are still difficult to adapt for OoCs. For exam-
ple, commercial chopstick electrodes used for measuring
TEER will not provide accurate reading of in- channel

 21

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
cell barriers in most cases. Some have fabricated and
integrated sensors and assays that are customized for
OoC systems. Multiple biosensors have been integrated
to monitor multiple biochemical factors, and integration
of bubble traps has allowed for long- term operation of
multi- organ systems38. For monitoring real- time insulin
secretion in an islet- on- chip in response to a change in
glucose concentration, fluorescence anisotropy was used
to measure the degree of binding between FITC- insulin
and insulin antibody272. This no- wash sensing tech-
nique allowed on- chip analysis of very small volumes
of samples in real time. Chip- integrated sensors with
high spatio- temporal resolution are needed for mon-
itoring the distribution of signalling molecules within
the cell culture compartment. The reader is referred to
other reviews for more in- depth analysis of challenges
and  opportunities  for  integrating  various  on- chip
biosensors263,273–275.

It is imperative that biological results obtained from
OoCs, such as drug testing responses, are systematically
validated with those obtained from existing in vitro and
animal models or even clinical data. This is to ensure
that responses obtained from OoC experiments are due
to differences in cell functionality, and not a result of
experimental artefacts that can arise even with correct
instrumentation and calibration of sensors. For example,
a less sensitive drug dose response in an OoC may be
later found to be due to adsorption of the drug to the
PDMS surface48. Applying a surface coating to PDMS
or using a different substrate may prevent this issue276,277.
Channel design, including the dimensions, curvature
and surface topography, is an important factor affect-
ing cell responses such as cell organization, alignment
and the degree of differentiation278,279. Media perfusion
in OoCs not only subjects cells to shear stress but also
alters effective cell to media volume ratios, which can
have unintended effects on cells. For example, fluid shear
stress applied to epithelial cells in the intestine- on- chip
was thought to be driving the stronger differentiation of
the cells and formation of 3D topology compared with
static cultures; however, it was found that the continuous
dilution of the Wnt antagonist DKK1 was responsible
for the more pronounced formation of villi under con-
ditions of flow. The same effect could be achieved in the
absence of flow by simply having a larger basal com-
partment to mitigate the inhibitory effect of DKK1 on
villi morphogenesis280. Thus, the opportunity and chal-
lenge of OoCs are that the same cells and reagents can
give rise to different cellular responses compared with
conventional cultures.

Validation studies using paradigm compounds with
well- characterized mechanisms of action or responses
in humans are needed to discern between real biological
differences and experimental artefacts due to changes in
materials or operating conditions in OoCs. The num-
ber of test compounds required for validation studies
depends on the application of interest. For example, the
predictive accuracy of a hepatotoxicity screening OoC
model may be validated with a large number (>10–20)
of positive and negative drugs281 or 2–3 pipeline com-
pounds that are known to fail because of hepatotox-
icity during preclinical trials72. A brain OoC model of

Alzheimer disease can be validated with two or three
known compounds that target specific cell types or sig-
nalling processes282. The OoC system should be devel-
oped to a stage where there is sufficient throughput
and reproducibility to meet the needs of the required
validation studies.

Outlook
OoC  technology  is  on  track  to  becoming  widely
accepted as a human- specific experimental platform
for preclinical research and therapeutics testing. This
shift is largely based on the results of in vitro studies
using these platforms becoming increasingly predictive
of clinical data for integrated human physiology. Not
surprisingly, numerous OoC start- ups launched from
academic laboratories are starting to fill the commercial
space for drug testing in the pharmaceutical industry45,
including GSK283, Roche and Pfizer284. Nonetheless,
there are some important challenges that still need to
be overcome269, and so we foresee that future develop-
ments for OoC technology will likely focus on making
the platform (1) more standardized, (2) compatible with
imaging, analytical instruments, robotics and mass pro-
duction, and (3) user- friendly so that it can be widely
adopted by non- specialist end users. We anticipate
increased efforts to develop OoCs that allow incorpo-
ration of the immune system285, metabolism286, micro-
biome287 and innervation288,289. These systems impact the
health and functionality of organ systems in the body
and are needed for achieving the desired functionality
in (patho)physiological studies, but are recapitulated in
animal models only to a limited extent290.

Platform development
OoCs have mostly been developed in academic labora-
tories at production throughputs of just a set of devices
per day, so that the standardization and quality control
remain limited. The major obstacle to general acceptance
of OoCs to commercial or academic end users is, ulti-
mately, determined by the quality and quantity of bio-
logical data. Many OoCs lack the robustness, ease of use
and level of throughput to generate the large amounts
of reliable biological data required for OoC validation.

To support broader use in biological research and
drug development, standardized OoCs need to become
as available as cell culture plates, implying that they need
to be reliably manufactured on an industrial scale269.
Approaches such as injection moulding, long established
in the manufacture of high volumes of plastic products
at low cost, are attractive for OoC manufacture where
their context of use demands high throughput50,51. As
OoCs often consist of several layers, the ability to man-
ufacture many plastic chips may need to be coupled to
parallel developments in the automation of chip align-
ment, assembly and bonding. With increased awareness
and emphasis on manufacturability, we are also seeing
more OoC systems being fabricated from new mate-
rials using additive manufacturing techniques such as
3D printing291. These techniques are constantly being
improved with respect to production speed, and provide
a largely assembly- free approach to device construction.
They are thus a promising alternative for high- volume

22 | Article citation ID:            (2022) 2:33

www.nature.com/nrmpPrimer0123456789();: OoC production. The other major advantage of addi-
tive manufacturing is the ability to rapidly prototype
new OoC designs. This can have a profound influence
on how OoC designers develop their systems, as itera-
tive refinement can be performed far more rapidly and
effectively.

Higher availability of inexpensive OoCs would facil-
itate the adoption of this technology by end users in the
life sciences. Future technology efforts should also focus
on the development of more user- friendly OoC plat-
forms that require less skill and experience to operate2.
OoC prototypes typically are surrounded by a battery
of syringe pumps connected to the OoC by tubing and
valve arrays, as well as multiple reservoirs of medium,
heating elements and other apparatus to maintain tis-
sue viability and function; all of this peripheral equip-
ment requires maintenance. Moreover, it makes the step
towards experiments in parallel OoC more difficult, as
each additional OoC often requires additional pumps,
valves and tubing. Ready- to- use solutions will involve
better design of OoC interfaces with peripheral instru-
mentation to reduce experimental footprints, as well as
miniaturization of the actual OoC. This, in turn, will
make OoC platforms more robust, easier to use and
inherently more automatable.

Finally, OoC technology will be more readily adopted
if it fits into the current biological research ecosystem,
so that more molecular and functional data can be
measured using existing analytical and imaging instru-
ments. Currently, OoC approaches are mostly used to
address questions where low to moderate throughput
is sufficient. High- throughput applications, such as the
screening of new chemical entities in the drug discov-
ery process, are based on simpler cell cultures that are
tested in well plate formats using robotic liquid han-
dling. However, the use of OoC platforms at this early
stage to produce more predictive tissue responses has
been proposed. This will improve the selection of new
chemical entities based on their safety, pharmacological
and efficacy properties, minimizing the costly attrition
of compounds at later stages283. We expect that some cur-
rent OoC technologies based on relatively simple designs
will be scaled up according to the standardized multi-
well plate format292. These systems will find good use in
many present- day screening applications besides drug
development. Robotics and machine learning will also
be implemented to automate operation and data analy-
sis for these OoC systems11. Clearly, further instrumen-
tal development of more complex OoCs for improved
throughput will also benefit the wider implementation of
these platforms. We also anticipate that a new generation
of OoC systems will integrate physical and biological
sensors for in situ real- time dynamic stimulation and
measurement of cell and tissue responses at a molecular
or functional level.

Multi- OoCs are noteworthy in that they need to be
configurable so that the types and the order of tissues
can be selected based on the biological question studied.
Therefore, we will likely see more innovation in modular
OoC designs with reversible interconnections between
different organ systems77,293,294 so that users can easily
configure the number and order of interacting organs

in a single- pass or recirculatory perfusion system. These
approaches are modular, allowing organ tissue cultures
to be established before linking different organs to one
another. In one approach, researchers have developed
a translational organ- on- a- chip platform, which uses a
fluidic circuit board containing integrated channels as
a baseplate into which microfluidic building blocks (the
OoC) can be plugged in any desired configuration. This
platform has as one of its objectives the standardization
of OoC technology295. A different concept for modular-
ity involves the design of a device with interconnected
chambers, into which glass coverslips bearing separately
prepared cell cultures or gel mixtures with cells are intro-
duced108. Recently, a novel multi- organ chip was reported
in which matured human heart, liver, bone and skin
tissue niches are linked by recirculating vascular flow,
to allow for the recapitulation of interdependent organ
functions. Each tissue is cultured in its own optimized
environment and is separated from the common vascu-
lar flow by a selectively permeable endothelial barrier.
The interlinked tissues were shown to maintain their
molecular, structural and functional phenotypes over
4 weeks of culture, recapitulate the PK and PD profiles of
doxorubicin in humans, and allow for the identification
of early microRNA biomarkers of cardiotoxicity27.

Biological applications
A broad area where we expect to see continued innova-
tion is the development of multi- OoC systems to mimic
systemic physiology of the human body. This utility was
previously developed mostly in the context of evaluating
the safety and efficacy of pharmaceutical compounds,
which we expect to be extended to other therapeu-
tic agents, including nanomedicine, cell therapies and
engineered tissue replacements. With new knowledge
being generated on the systemic nature of many chronic
human diseases, there are also burgeoning opportuni-
ties for OoC systems to replace animals to model these
diseases in a human- specific context. An example in this
area is modelling metabolic crosstalk. Multi- OoCs offer
a unique way to model the interactions between meta-
bolically active organs, such as skeletal muscle, the liver,
adipose tissue, the pancreas and the gut, to regulate the
use and storage of energy through metabolic homeo-
stasis296,297. Dysfunction in this metabolic crosstalk gives
rise to metabolic diseases such as type 2 diabetes and
non- alcoholic fatty liver disease, which is a growing
global health concern298. Liver–gut multi- OoC systems
have been created to model the gut–liver axis in hepatic
steatosis299–301,  and  metabolic  crosstalk  in  muscle–
adipose16 and pancreas–liver302,303 systems has already
been modelled in multi- OoC systems. The challenge
for the next generation of metabolic multi- OoCs will
be to incorporate more organs into the crosstalk, hence
recapitulating more physiological metabolic phenotypes.
The incorporation of patient microbiota through the gut
OoCs can potentially offer us the opportunity to exper-
imentally investigate various gut microbiome dysbiosis,
which have been correlated to many chronic diseases
through metagenome- wide association studies304,305.

Every  tissue  within  the  human  body  contains
immune cells and their homeostasis determines tissue

 23

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
health and pathology. With the advent of immunothera-
pies and improvement in protocols to expand and main-
tain immune cell populations in vitro, there is increasing
impetus to incorporate both adaptive and innate immune
components into OoC systems306,307. In the context of
cancer immunotherapy, researchers have started utiliz-
ing OoCs to investigate cancer cell–immune cell inter-
actions in 3D environments308. There are also efforts to
form lymphatic vessels within OoCs to study how cancer
cells remodel the tumour microenvironment309. Recent
studies also highlight the roles of endothelial–immune
cell  or  pathogen  crosstalk  in  modulating  immune
response310,311. Given significant species differences in
the immune system and the high sensitivity of immune
cells to a multitude of molecular, cellular and mecha-
nical factors, human cell- based OoCs with highly con-
trolled microenvironments are positioned to fill many
important unmet needs. The complexity of the immune
system presents many challenges as well as opportuni-
ties. Contributions towards these needs can span from
innate immune response- mimicking biomaterials312 that
can be easily incorporated into any cell culture to sophis-
ticated long- term OoCs that recreate diseases involving
multiple types of immune cell285. Overall, OoC models
that adequately include human immune systems stand
to provide a much needed human- specific context, as
the majority of studies are carried out in murine mod-
els which often fall short of mimicking human- specific
immune physiology. Innervation may also be required
to model diseases resulting from neurological disorders,
and to advance the biological fidelity of tissues that are
normally innervated288,289.

Finally, OoC systems that are based on the use of
iPSCs and organoids offer an unprecedented opportu-
nity to study patient diversity (racial and ethnic back-
ground, sex, age, state of health or disease) as a biological
variable, and to conduct patient- specific studies of the
progression of disease and effects of treatment. By look-
ing for commonalities between the clinical and in vitro
data, we can identify early- stage biomarkers, monitor
disease progression and determine optimal therapeutic

treatment regimens in a personalized manner. However,
the technicalities for routine integration of iPSC- derived
organoids with microfluidic devices remain to be resol-
ved. Existing methods often generate large organoids
(approximately millimetres in diameter) and require
extended (approximately weeks) differentiation times.
Therefore, OoC systems need to either significantly
alter their design and dimensions to accommodate large
preformed organoids313 or invest substantial efforts to
adapt and optimize differentiation protocols for in situ
organoid differentiation on- chip314. iPSCs may also start
playing a larger role in filling the need for reliable access
to functional immune cells. Given the universal impor-
tance of patient- specific immune cells for many diseases
and their treatment, it will be important to incorporate
immune  organs  (such  as  bone  marrow  and  lymph
nodes) into the OoC platforms285 to provide renewable
sources of both the innate and the adaptive immune
cells, rather than adding the patient’s immune cells
into the tissues or perfusate. Another approach would
be to use a common HLA- null iPSC line to generate
agnostic tissues that can be combined with the patient’s
immune cells269.

In summary, the goal of this Primer was to explore
the use of OoC in biological research and highlight the
emerging opportunities and the unmet challenges. We
described the design and applications of OoCs rep-
resenting a single tissue unit and those representing
multi- tissue units linked by microfluidic flow to reca-
pitulate complex physiological functions such as cancer
metastasis, inflammation and infection. Although OoCs
consist of relatively simple tissues, compared with their
native counterparts, they are able to approximate one
or few organ- level functions: barrier function of the
lung, contractile function of the heart or filtration in
the kidney. We conclude that OoCs are poised to become
broadly accepted in biological research, as they offer bio-
logic fidelity along with experimental control in human
tissue settings.

Published online xx xx xxxx

1.  Bhatia, S. N. & Ingber, D. E. Microfluidic

2.

organs- on-chips. Nat. Biotechnol. 32, 760–772
(2014).
Low, L. A., Mummery, C., Berridge, B. R., Austin, C. P.
& Tagle, D. A. Organs- on-chips: into the next decade.
Nat. Rev. Drug. Discov. 20, 345–361 (2021).
3.  Manz, A., Graber, N. & Widmer, H. M. Miniaturized

total chemical analysis systems: a novel concept
for chemical sensing. Sens. Actuator B Chem. 1,
244–248 (1990).
This pioneering paper introduces the concept
of micro total analysis systems integrated into
microfluidic chips, which led, in turn, to the
introduction of OoCs and integrated read- out
systems.

4.  Harrison, D. J., Manz, A., Fan, Z. H., Ludi, H. &

Widmer, H. M. Capillary electrophoresis and sample
injection systems integrated on a planar glass chip.
Anal. Chem. 64, 1926–1932 (1992).

5.  Whitesides, G. M. The origins and the future of

6.

7.

microfluidics. Nature 442, 368–373 (2006).
Sahlgren, C. et al. Tailored approaches in drug
development and diagnostics: from molecular design
to biological model systems. Adv. Healthc. Mater. 6,
1700258 (2017).
Jackson, E. L. & Lu, H. Three- dimensional models
for studying development and disease: moving on
from organisms to organs- on-a- chip and organoids.
Integr. Biol. 8, 672–683 (2016).

24 | Article citation ID:            (2022) 2:33

8.

9.

Sin, A., Baxter, G. & Shuler, M. Animal on a Chip:
A Microscale Cell Culture Analog Device for Evaluating
Toxicological and Pharmacological Profiles Vol. 4560
PWM (SPIE, 2001).
Sin, A. et al. The design and fabrication of three-
chamber microscale cell culture analog devices with
integrated dissolved oxygen sensors. Biotechnol. Prog.
20, 338–345 (2004).
This paper is the first to provide a detailed
description of the construction of a multi- OoC
system based on a physiologically based PK model.
10.  Huh, D. et al. Reconstituting organ- level lung functions

on a chip. Science 328, 1662–1668 (2010).
This paper is one of the pioneering works on lung
OoC, which demonstrates a functional alveolar–
capillary interface that is responsive to pathogen
infection.

11.  Ronaldson- Bouchard, K. & Vunjak- Novakovic, G.

Organs- on-a- chip: a fast track for engineered human
tissues in drug development. Cell Stem Cell 22,
310–324 (2018).

12.  World Economic Forum. Top 10 emerging technologies of
2016. World Economic Forum https://www.weforum.org/
reports/top-10-emerging- technologies-of-2016 (2016).

13.  Jang, K.-J. & Suh, K.-Y. A multi- layer microfluidic

device for efficient culture and analysis of renal tubular
cells. Lab Chip 10, 36–42 (2010).

that experiences intestinal peristalsis- like motions
and flow. Lab Chip 12, 2165–2174 (2012).
This work is one of the first gut OoC papers showing
that physical stretching of the cell culture substrate
and fluid perfusion can enhance the differentiation
of Caco-2 cells into an intestinal epithelium with
physiological architectures and functions.
15.  Bokhari, M., Carnachan, R. J., Cameron, N. R. &

Przyborski, S. A. Culture of HepG2 liver cells on three
dimensional polystyrene scaffolds enhances cell
structure and function during toxicological challenge.
J. Anat. 211, 567–576 (2007).

16.  Shahin- Shamsabadi, A. & Selvaganapathy, P. R. A 3D

self- assembled in vitro model to simulate direct and
indirect interactions between adipocytes and skeletal
muscle cells. Adv. Biosyst. 4, 2000034 (2020).

17.  Wang, Y., Wang, L., Guo, Y., Zhu, Y. & Qin, J.

Engineering stem cell- derived 3D brain organoids
in a perfusable organ- on-a- chip system. RSC Adv. 8,
1677–1685 (2018).

18.  Lee, S.-R. et al. Modeling neural circuit, blood–brain
barrier, and myelination on a microfluidic 96 well
plate. Biofabrication 11, 035013 (2019).

19.  Jang, J. M., Lee, J., Kim, H., Jeon, N. L. & Jung, W.

One- photon and two- photon stimulation of neurons
in a microfluidic culture system. Lab Chip 16,
1684–1690 (2016).

14.  Kim, H. J., Huh, D., Hamilton, G. & Ingber, D. E.

Human gut- on-a- chip inhabited by microbial flora

20.  Park, S. M. et al. Reconstruction of in vivo- like in vitro
model: enabling technologies of microfluidic systems

www.nature.com/nrmpPrimer0123456789();: for dynamic biochemical/mechanical stimuli.
Microelectron. Eng. 203–204, 6–24 (2019).

21.  Herzog, N., Katzenberger, N., Martin, F., Schmidtke, K. U.
& Küpper, J.-H. Generation of cytochrome P450
3A4-overexpressing HepG2 cell clones for
standardization of hepatocellular testosterone
6β- hydroxylation activity. J. Cell. Biotechnol. 1,
15–26 (2015).

22.  Moysidou, C.-M., Barberio, C. & Owens, R. M.
Advances in engineering human tissue models.
Front. Bioeng. Biotechnol. 8, 620962 (2021).

23.  Gallagher, L. B. et al. Pre- culture of mesenchymal stem
cells within RGD- modified hyaluronic acid hydrogel
improves their resilience to ischaemic conditions.
Acta Biomater. 107, 78–90 (2020).

24.  Ramme, A. P. et al. Autologous induced pluripotent
stem cell- derived four- organ-chip. Future Sci. OA 5,
FSO413 (2019).

25.  Sances, S. et al. Human iPSC- derived endothelial cells

and microengineered organ- chip enhance neuronal
development. Stem Cell Rep. 10, 1222–1236 (2018).

43.  FDA- NIH Biomarker Working Group. BEST (Biomarkers,
EndpointS, and other Tools) Resource (US Food and
Drug Administration & National Institutes of Health,
2016).

44.  US Food and Drug Administration. Advancing

alternative methods at FDA. US Food and Drug
Administration https://www.fda.gov/science- research/
about- science-research- fda/advancing- alternative-
methods- fda#:~:text=FDA%20Definitions&text=
MPS%20platforms%20may%20comprise%20
mono,inclusion%20of%20organoid%20cell%20
formations (2022).

45.  Zhang, B. & Radisic, M. Organ- on-a- chip devices

advance to market. Lab Chip 17, 2395–2420 (2017).
This review discusses the commercialization
trajectory of OoC technologies into the drug
discovery market.

46.  Verpoorte, E. et al. in 2015 Transducers — 2015

18th International Conference on Solid- State Sensors,
Actuators and Microsystems (TRANSDUCERS)
224–227 (IEEE, 2015).

26.  Rowe, R. G. & Daley, G. Q. Induced pluripotent stem

47.  Shin, J. et al. Monolithic digital patterning of

cells in disease modelling and drug discovery. Nat.
Rev. Genet. 20, 377–388 (2019).

27.  Ronaldson- Bouchard K., et al. Inter- organ chips with

matured tissue niches linked by vascular perfusion.
Nat. Biomed. Eng. (in the press).
This paper reports a multi- tissue chip system
in which matured human tissues are linked by
recirculating vascular flow, allowing for the
maintenance of their phenotypes, communication
across endothelial barriers and recapitulation
of interdependent organ functions.

28.  Duffy, D. C., McDonald, J. C., Schueller, O. J. A. &

Whitesides, G. M. Rapid prototyping of microfluidic
systems in poly(dimethylsiloxane). Anal. Chem. 70,
4974–4984 (1998).

polydimethylsiloxane with successive laser pyrolysis.
Nat. Mater. 20, 100–107 (2021).
This study describes a novel laser- based
fabrication technique for PDMS devices; a high-
resolution technique suitable for rapid prototyping
and production of a small series of devices
(10–100 devices), while also being a good
alternative to replication moulding.

48.  Toepke, M. W. & Beebe, D. J. PDMS absorption of
small molecules and consequences in microfluidic
applications. Lab Chip 6, 1484–1486 (2006).

49.  Wang, J. D., Douville, N. J., Takayama, S. & ElSayed, M.
Quantitative analysis of molecular absorption into
PDMS microfluidic channels. Ann. Biomed. Eng. 40,
1862–1873 (2012).

29.  Xia, Y. & Whitesides, G. M. Soft lithography. Annu. Rev.

50.  Ko, J. et al. Tumor spheroid- on-a- chip: a standardized

Mater. Sci. 28, 153–184 (1998).

30.  Reyes, D. R., Iossifidis, D., Auroux, P.-A. & Manz, A.
Micro total analysis systems. 1. Introduction, theory,
and technology. Anal. Chem. 74, 2623–2636 (2002).
31.  Verpoorte, E. M. J. et al. Three- dimensional micro flow
manifolds for miniaturized chemical analysis systems.
J. Micromech. Microeng. 4, 246–256 (1994).
32.  Dittrich, P. S. & Manz, A. Lab- on-a- chip: microfluidics

in drug discovery. Nat. Rev. Drug. Discov. 5, 210–218
(2006).

33.  Meyvantsson, I. & Beebe, D. J. Cell culture models
in microfluidic systems. Annu. Rev. Anal. Chem. 1,
423–449 (2008).

34.  Kim, L., Toh, Y.-C., Voldman, J. & Yu, H. A practical
guide to microfluidic perfusion culture of adherent
mammalian cells. Lab Chip 7, 681–694 (2007).
This paper offers practical help for setting up
a microfluidic perfusion cell culture system,
such as dealing with bubbles, proper control
of temperature and gas equilibration in media.

35.  Sung, J. H. et al. Recent advances in body- on-a- chip

systems. Anal. Chem. 91, 330–351 (2019).
36.  Allwardt, V. et al. Translational roadmap for the

organs- on-a- chip industry toward broad adoption.
Bioengineering 7, 112 (2020).

37.  Abaci, H. E. & Shuler, M. L. Human- on-a- chip design

strategies and principles for physiologically based
pharmacokinetics/pharmacodynamics modeling.
Integr. Biol. 7, 383–391 (2015).

38.  Zhang, Y. S. et al. Multisensor- integrated organs-

on-chips platform for automated and continual in situ
monitoring of organoid behaviors. Proc. Natl Acad.
Sci. USA 114, E2293–E2302 (2017).

39.  Frey, O., Misun, P. M., Fluri, D. A., Hengstler, J. G. &
Hierlemann, A. Reconfigurable microfluidic hanging
drop network for multi- tissue interaction and analysis.
Nat. Commun. 5, 4250 (2014).
This paper introduces interconnected hanging
drops and unifies spheroid aggregation of different
organ types and their cross- communication in a
parallel format.

40.  Santbergen, M. J. C., van der Zande, M.,

Bouwmeester, H. & Nielen, M. W. F. Online and
in situ analysis of organs- on-a- chip. TrAC Trends
Anal. Chem. 115, 138–146 (2019).

41.  Misun, P. M., Rothe, J., Schmid, Y. R. F., Hierlemann, A.
& Frey, O. Multi- analyte biosensor interface for
real- time monitoring of 3D microtissue spheroids
in hanging- drop networks. Microsyst. Nanoeng. 2,
16022 (2016).

42.  Hargrove- Grimes, P., Low, L. A. & Tagle, D. A.

Microphysiological systems: stakeholder challenges
to adoption in drug development. Cell Tissues Organs
211, 69–81 (2022).

microfluidic culture platform for investigating tumor
angiogenesis. Lab Chip 19, 2822–2833 (2019).
51.  Lee, Y. et al. Microfluidics within a well: an injection-
molded plastic array 3D culture platform. Lab Chip
18, 2433–2440 (2018).
This paper presents the basis for high- throughput
microfluidic organ- on-a- chip design that is amenable
for 3D co- cultures. Furthermore, the device designs
described here are compatible with 3D printing
and injection moulding such that they offer an
alternative to traditional PDMS- based chips.

52.  Homan, K. A. et al. Flow- enhanced vascularization and
maturation of kidney organoids in vitro. Nat. Methods
16, 255–262 (2019).

53.  Berthier, E., Young, E. W. K. & Beebe, D. Engineers

are from PDMS- land, biologists are from Polystyrenia.
Lab Chip 12, 1224–1237 (2012).
This paper highlights how differences in the
inherent material properties of PS and PDMS
can lead to disparity between conventional and
microfluidic cell cultures.

54.  Jensen, C. & Teng, Y. Is it time to start transitioning

from 2D to 3D cell culture? Front. Mol. Biosci. 7, 33
(2020).

55.  Kim, H. J., Li, H., Collins, J. J. & Ingber, D. E.
Contributions of microbiome and mechanical
deformation to intestinal bacterial overgrowth and
inflammation in a human gut- on-a- chip. Proc. Natl
Acad. Sci. USA 113, E7–E15 (2016).

56.  Maoz, B. M. et al. A linked organ- on-chip model of
the human neurovascular unit reveals the metabolic
coupling of endothelial and neuronal cells. Nat.
Biotechnol. 36, 865–874 (2018).

57.  Brown, J. A. et al. Recreating blood–brain barrier

physiology and structure on chip: a novel neurovascular
microfluidic bioreactor. Biomicrofluidics 9, 054124
(2015).

58.  Ahn, S. I. et al. Microengineered human blood–brain
barrier platform for understanding nanoparticle
transport mechanisms. Nat. Commun. 11, 175
(2020).

59.  Esch, M. B. et al. On chip porous polymer membranes
for integration of gastrointestinal tract epithelium
with microfluidic ‘body- on-a- chip’ devices. Biomed.
Microdevices 14, 895–906 (2012).

60.  Wang, Y. et al. Capture and 3D culture of colonic

crypts and colonoids in a microarray platform.
Lab Chip 13, 4625–4634 (2013).

61.  Uemura, M. et al. Matrigel supports survival and

neuronal differentiation of grafted embryonic stem
cell- derived neural precursor cells. J. Neurosci. Res.
88, 542–551 (2010).

62.  Afshar Bakooshli, M. et al. A 3D culture model of

innervated human skeletal muscle enables studies

of the adult neuromuscular junction. eLife 8, e44530
(2019).

63.  Horowitz, L. F., Rodriguez, A. D., Ray, T. & Folch, A.

Microfluidics for interrogating live intact tissues.
Microsyst. Nanoeng. 6, 69 (2020).
This article is a reference for readers interested
in the integration of live intact tissue slices into a
microfluidic system.

64.  Shi, Y., Inoue, H., Wu, J. C. & Yamanaka, S. Induced

pluripotent stem cell technology: a decade of progress.
Nat. Rev. Drug Discov. 16, 115–130 (2017).

65.  van den Berg, A., Mummery, C. L., Passier, R. &

van der Meer, A. D. Personalised organs- on-chips:
functional testing for precision medicine. Lab Chip 19,
198–205 (2019).

66.  Diederichs, S. & Tuan, R. S. Functional comparison
of human- induced pluripotent stem cell- derived
mesenchymal cells and bone marrow- derived
mesenchymal stromal cells from the same donor.
Stem Cell Dev. 23, 1594–1610 (2014).
67.  Verma, A., Verma, M. & Singh, A. in Animal

Biotechnology 2nd edn (eds Verma, A. S. & Singh, A.)
269–293 (Academic, 2020).

68.  Yeste, J., Illa, X., Alvarez, M. & Villa, R. Engineering
and monitoring cellular barrier models. J. Biol. Eng.
12, 18 (2018).

69.  Yang, F., Cohen, R. N. & Brey, E. M. Optimization of

co- culture conditions for a human vascularized adipose
tissue model. Bioengineering 7, 114 (2020).
70.  Chang, S.-Y. et al. Human liver–kidney model

elucidates the mechanisms of aristolochic acid
nephrotoxicity. JCI Insight 2, e95978 (2017).

71.  Zhang, C., Zhao, Z., Abdul Rahim, N. A., van Noort, D.

& Yu, H. Towards a human- on-chip: culturing multiple
cell types on a chip with compartmentalized
microenvironments. Lab Chip 9, 3185–3192 (2009).

72.  Jang, K. J. et al. Reproducing human and cross- species

drug toxicities using a liver- chip. Sci. Transl. Med. 11,
eaax5516 (2019).

73.  Wufuer, M. et al. Skin- on-a- chip model simulating
inflammation, edema and drug- based treatment.
Sci. Rep. 6, 37471 (2016).

74.  Even, M. S., Sandusky, C. B. & Barnard, N. D. Serum-

free hybridoma culture: ethical, scientific and safety
considerations. Trends Biotechnol. 24, 105–108
(2006).

75.  Kongsuphol, P. et al. In vitro micro- physiological model
of the inflamed human adipose tissue for immune-
metabolic analysis in type II diabetes. Sci. Rep. 9,
4887 (2019).

76.  Massa, S. et al. Bioprinted 3D vascularized tissue

model for drug toxicity analysis. Biomicrofluidics 11,
044109 (2017).

77.  Ong, L. J. Y. et al. Self- aligning Tetris- Like (TILE)

modular microfluidic platform for mimicking multi-
organ interactions. Lab Chip 19, 2178–2191 (2019).
This paper demonstrates a modular design of
assembling pre- established tissue chips into a
recirculating multi- OoC system.

78.  Satoh, T. et al. A pneumatic pressure- driven multi-
throughput microfluidic circulation culture system.
Lab Chip 16, 2339–2348 (2016).

79.  Lee, K. K. et al. Human stomach- on-a- chip with

luminal flow and peristaltic- like motility. Lab Chip 18,
3079–3085 (2018).

80.  Ong, L. J. Y. et al. A pump- free microfluidic 3D

perfusion platform for the efficient differentiation of
human hepatocyte- like cells. Biotechnol. Bioeng. 114,
2360–2370 (2017).

81.  Yu, F. et al. A pump- free tricellular blood–brain barrier

on- a-chip model to understand barrier property and
evaluate drug response. Biotechnol. Bioeng. 117,
1127–1136 (2020).

82.  Lohasz, C., Rousset, N., Renggli, K., Hierlemann, A. &
Frey, O. Scalable microfluidic platform for flexible
configuration of and experiments with microtissue
multiorgan models. SLAS Technol. 24, 79–95 (2019).
This paper describes a scalable and automation-
compatible multi- spheroid culture system in a
microtitre plate format based on gravity- driven
flow that is actuated by tilting.

83.  Wang, Y. I. & Shuler, M. L. UniChip enables long- term
recirculating unidirectional perfusion with gravity-
driven flow for microphysiological systems. Lab Chip
18, 2563–2574 (2018).

84.  Oleaga, C. et al. Multi- organ toxicity demonstration

in a functional human in vitro system composed of
four organs. Sci. Rep. 6, 20030 (2016).

85.  Chen, L., Yang, Y., Ueno, H. & Esch, M. B. Body- in-a-

cube: a microphysiological system for multi- tissue
co- culture with near- physiological amounts of blood
surrogate. Microphys. Syst. 4, 1 (2020).

 25

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
86.  Yang, Y. et al. Pumpless microfluidic devices for

generating healthy and diseased endothelia. Lab Chip
19, 3212–3219 (2019).

87.  Maschmeyer, I. et al. A four- organ-chip for

interconnected long- term co- culture of human
intestine, liver, skin and kidney equivalents. Lab Chip
15, 2688–2699 (2015).

88.  Vernetti, L. et al. Functional coupling of human
microphysiology systems: intestine, liver, kidney
proximal tubule, blood–brain barrier and skeletal
muscle. Sci. Rep. 7, 42296 (2017).
This paper combines multiple single- OoCs by
manual transfer of culture medium from one organ
to the next to simulate multi- organ functions;
termed ‘functional’ coupling rather than direct
coupling of organs in a flow- through system.

89.  Novak, R. et al. Robotic fluidic coupling and

interrogation of multiple vascularized organ chips.
Nat. Biomed. Eng. 4, 407–420 (2020).

90.  van Midwoud, P. M. et al. On- line HPLC analysis
system for metabolism and inhibition studies in
precision- cut liver slices. Anal. Chem. 83, 84–91
(2011).

91.  Young, E. W. & Beebe, D. J. Fundamentals of

microfluidic cell culture in controlled micro-
environments. Chem. Soc. Rev. 39, 1036–1048
(2010).
This review covers fundamental concepts on how
microfluidics alter physical and biochemical
microenvironmental factors, which are important
for successful microscale cell culture.

anticancer therapeutics. Sci. Transl. Med. https://doi.
org/10.1126/scitranslmed.aav1386 (2019).
Together with Viravaidya et al. (2004) and Edington
et al. (2018), this paper and the above- mentioned
papers have been selected as case studies to
highlight evolution in the design of multi- OoC
systems for ADME- Tox studies.

109. Grist, S. M., Chrostowski, L. & Cheung, K. C. Optical

oxygen sensors for applications in microfluidic cell
culture. Sensors 10, 9286–9316 (2010).

110.  Rivera, K. R., Yokus, M. A., Erb, P. D., Pozdin, V. A. &
Daniele, M. Measuring and regulating oxygen levels
in microphysiological systems: design, material, and
sensor considerations. Analyst 144, 3190–3215
(2019).

111.  Oomen, P. E., Skolimowski, M. D. & Verpoorte, E.

Implementing oxygen control in chip- based cell and
tissue culture systems. Lab Chip 16, 3394–3414
(2016).

112.  Brennan, M. D., Rexius- Hall, M. L., Elgass, L. J. &
Eddington, D. T. Oxygen control with microfluidics.
Lab Chip 14, 4305–4318 (2014).

113.  Scheidecker, B. et al. Induction of in vitro metabolic
zonation in primary hepatocytes requires both near-
physiological oxygen concentration and flux. Front.
Bioeng. Biotechnol. 8, 524 (2020).

114.  Farzaneh, Z. et al. Dissolved oxygen concentration
regulates human hepatic organoid formation
from pluripotent stem cells in a fully controlled
bioreactor. Biotechnol. Bioeng. 117, 3739–3756
(2020).

92.  Blagovic, K., Kim, L. Y. & Voldman, J. Microfluidic

115.  Kietzmann, T. Metabolic zonation of the liver: the

perfusion for regulating diffusible signaling in stem
cells. PLoS ONE 6, e22892 (2011).

93.  Przybyla, L. M. & Voldman, J. Attenuation of extrinsic
signaling reveals the importance of matrix remodeling
on maintenance of embryonic stem cell self- renewal.
Proc. Natl Acad. Sci. USA 109, 835–840 (2012).
94.  Bhattacharjee, N. & Folch, A. Large- scale microfluidic
gradient arrays reveal axon guidance behaviors in
hippocampal neurons. Microsyst. Nanoeng. 3, 17003
(2017).

95.  McCarty, W. J., Usta, O. B. & Yarmush, M. L.

A microfabricated platform for generating
physiologically-relevant hepatocyte zonation. Sci. Rep.
6, 26868 (2016).

96.  Tilles, A. W., Baskaran, H., Roy, P., Yarmush, M. L.
& Toner, M. Effects of oxygenation and flow on the
viability and function of rat hepatocytes cocultured
in a microchannel flat- plate bioreactor. Biotechnol.
Bioeng. 73, 379–389 (2001).

97.  Lindner, M., Laporte, A., Block, S., Elomaa, L. &

Weinhart, M. Physiological shear stress enhances
differentiation, mucus- formation and structural 3D
organization of intestinal epithelial. Cell Vitro. Cell 10,
2062 (2021).

98.  Marrero, D. et al. Gut- on-a- chip: mimicking and

monitoring the human intestine. Biosens. Bioelectron.
181, 113156 (2021).

99.  Trieu, D., Waddell, T. K. & McGuigan, A. P.

A microfluidic device to apply shear stresses to
polarizing ciliated airway epithelium using air flow.
Biomicrofluidics 8, 064104 (2014).

100. Arora, S., Srinivasan, A., Leung, M. C. & Toh, Y.-C.

Bio- mimicking shear stress environments for enhancing
mesenchymal stem cell differentiation. Curr. Stem Cell
Res. Ther. 15, 414–427 (2020).

101.  Ergir, E., Bachmann, B., Redl, H., Forte, G. & Ertl, P.
Small force, big impact: next generation organ- on-a-
chip systems incorporating biomechanical cues. Front.
Physiol. 9, 1417 (2018).

102. Takano, A., Tanaka, M. & Futai, N. On- chip multi- gas

incubation for microfluidic cell cultures under hypoxia.
Biomicrofluidics 8, 061101 (2014).

103. Toh, Y.-C. et al. A novel 3D mammalian cell perfusion-

culture system in microfluidic channels. Lab Chip 7,
302–309 (2007).

104. Imura, Y., Asano, Y., Sato, K. & Yoshimura, E.

A microfluidic system to evaluate intestinal
absorption. Anal. Sci. 25, 1403–1407 (2009).
105. Bein, A. et al. Enteric coronavirus infection and

treatment modeled with an immunocompetent human
intestine- on-a- chip. Front. Pharmacol. 12, 718484
(2021).

106. Viravaidya, K., Sin, A. & Shuler, M. L. Development of
a microscale cell culture analog to probe naphthalene
toxicity. Biotechnol. Prog. 20, 316–323 (2004).

107.  Edington, C. D. et al. Interconnected

microphysiological systems for quantitative biology
and pharmacology studies. Sci. Rep. 8, 4530 (2018).

108. McAleer, C. W. et al. Multi- organ system for the

evaluation of efficacy and off- target toxicity of

26 | Article citation ID:            (2022) 2:33

oxygen gradient revisited. Redox Biol. 11, 622–630
(2017).

116.  Sung, J. H., Choi, J. R., Kim, D. & Shuler, M. L.

Fluorescence optical detection in situ for real- time
monitoring of cytochrome P450 enzymatic activity of
liver cells in multiple microfluidic devices. Biotechnol.
Bioeng. 104, 516–525 (2009).

117.  Choi, J. R., Sung, J. H., Shuler, M. L. & Kim, D.

Investigation of portable in situ fluorescence optical
detection for microfluidic 3D cell culture assays.
Opt. Lett. 35, 1374–1376 (2010).

118.  Weltin, A. et al. Cell culture monitoring for drug

screening and cancer research: a transparent,
microfluidic, multi- sensor microsystem. Lab Chip 14,
138–146 (2014).

119.  Toh, Y. C. & Voldman, J. Fluid shear stress primes

mouse embryonic stem cells for differentiation in a self-
renewing environment via heparan sulfate proteoglycans
transduction. FASEB J. 25, 1208–1217 (2011).
120. Vit, F. F. et al. A modular, reversible sealing, and
reusable microfluidic device for drug screening.
Analytica Chim. Acta 1185, 339068 (2021).
121. Morsink, M. A. J., Willemen, N. G. A., Leijten, J.,

Bansal, R. & Shin, S. R. Immune organs and immune
cells on a chip: an overview of biomedical applications.
Micromachines 11, 849 (2020).

122. Chen, Y. Y. et al. Clarifying intact 3D tissues on a

microfluidic chip for high- throughput structural analysis.
Proc. Natl Acad. Sci. USA 113, 14915–14920 (2016).

123. Wardwell- Swanson, J. et al. A framework for

optimizing high- content imaging of 3D models for
drug discovery. SLAS Discov. 25, 709–722 (2020).

124. Chen, Z. et al. Automated evaluation of tumor

spheroid behavior in 3D culture using deep learning-
based recognition. Biomaterials 272, 120770
(2021).

125. Wolff, A., Antfolk, M., Brodin, B. & Tenje, M. In vitro
blood- brain barrier models — an overview of
established models and new microfluidic approaches.
J. Pharm. Sci. 104, 2727–2746 (2015).

126. Brown, C. D. A. et al. Characterisation of human

tubular cell monolayers as a model of proximal tubular
xenobiotic handling. Toxicol. Appl. Pharmacol. 233,
428–438 (2008).

127. Henry, O. Y. F. et al. Organs- on-chips with integrated

electrodes for trans- epithelial electrical resistance
(TEER) measurements of human epithelial barrier
function. Lab Chip 17, 2264–2271 (2017).
128. van der Helm, M. W. et al. Direct quantification of

transendothelial electrical resistance in organs-
on-chips. Biosens. Bioelectron. 85, 924–929 (2016).
129. Demircan Yalcin, Y. & Luttge, R. Electrical monitoring
approaches in 3-dimensional cell culture systems:
toward label- free, high spatiotemporal resolution,
and high- content data collection in vitro. Organs-
on-a- Chip 3, 100006 (2021).

130. Elbakary, B. & Badhan, R. K. S. A dynamic perfusion
based blood–brain barrier model for cytotoxicity
testing and drug permeation. Sci. Rep. 10, 3788
(2020).

131. Bürgel, S. C., Diener, L., Frey, O., Kim, J. Y. &

Hierlemann, A. Automated, multiplexed electrical
impedance spectroscopy platform for continuous
monitoring of microtissue spheroids. Anal. Chem. 88,
10876–10883 (2016).

132. Srinivasan, B. et al. TEER measurement techniques

for in vitro barrier model systems. J. Lab. Autom. 20,
107–126 (2015).
This paper reviews different methods of making
TEER measurements in barrier tissues, and their
strengths and weaknesses, and addresses issues
where the technique is applied incorrectly.

133. Soucy, J. R., Bindas, A. J., Koppes, A. N. & Koppes, R. A.

Instrumented microphysiological systems for
real-time measurement and manipulation of cellular
electrochemical processes. iScience 21, 521–548
(2019).

134. Ferrari, E., Palma, C., Vesentini, S., Occhetta, P. &

Rasponi, M. Integrating biosensors in organs- on-chip
devices: a perspective on current strategies to monitor
microphysiological systems. Biosensors 10, 110
(2020).
This review covers the integration of sensors into
OoC devices for real- time measurements of oxygen,
soluble metabolites (for example, glucose or lactate
cytokines), TEER and electrical activity.

135. Oleaga, C. et al. A human in vitro platform for the

evaluation of pharmacology strategies in cardiac
ischemia. APL. Bioeng. 3, 036103 (2019).

136. Kussauer, S., David, R. & Lemcke, H. hiPSCs derived
cardiac cells for drug and toxicity screening and
disease modeling: what micro- electrode-array analyses
can tell us. Cells 8, 1331 (2019).

137. van de Wijdeven, R. et al. A novel lab- on-chip platform
enabling axotomy and neuromodulation in a multi-
nodal network. Biosens. Bioelectron. 140, 111329
(2019).

138. Oiwa, K. et al. A device for co- culturing autonomic

neurons and cardiomyocytes using micro- fabrication
techniques. Integr. Biol. 8, 341–348 (2016).

139. Yuan, X. et al. Versatile live- cell activity analysis

platform for characterization of neuronal dynamics at
single- cell and network level. Nat. Commun. 11, 4854
(2020).

140. Sung, J. H., Wang, Y. & Shuler, M. L. Strategies for

using mathematical modeling approaches to design
and interpret multi- organ microphysiological systems
(MPS). APL Bioeng. 3, 021501 (2019).
This paper provides a useful guide to design
principles and scaling rules for multi- OoC systems
to be used for PK and PD studies.

141. Moutaux, E., Charlot, B., Genoux, A., Saudou, F. &

Cazorla, M. An integrated microfluidic/microelectrode
array for the study of activity- dependent intracellular
dynamics in neuronal networks. Lab Chip 18,
3425–3435 (2018).

142. Stancescu, M. et al. A phenotypic in vitro model for

the main determinants of human whole heart function.
Biomaterials 60, 20–30 (2015).

143. Coln, E. A. et al. Piezoelectric BioMEMS cantilever
for measurement of muscle contraction and for
actuation of mechanosensitive cells. MRS Commun. 9,
1186–1192 (2019).

144. Maoz, B. M. et al. Organs- on-chips with combined
multi- electrode array and transepithelial electrical
resistance measurement capabilities. Lab Chip 17,
2294–2302 (2017).

145. Balijepalli, A. & Sivaramakrishan, V. Organs- on-chips:
research and commercial perspectives. Drug. Discov.
Today 22, 397–403 (2017).

146. Livingston, C. A., Fabre, K. M. & Tagle, D. A.

Facilitating the commercialization and use of organ
platforms generated by the microphysiological
systems (Tissue Chip) program through public–
private partnerships. Comput. Struct. Biotechnol. J.
14, 207–210 (2016).

147. Reyes, D. R. et al. Accelerating innovation and
commercialization through standardization of
microfluidic- based medical devices. Lab Chip 21,
9–21 (2021).

148. Fabre, K. et al. Introduction to a manuscript series

on the characterization and use of microphysiological
systems (MPS) in pharmaceutical safety and ADME
applications. Lab Chip 20, 1049–1057 (2020).

149. Sung, J. H., Kam, C. & Shuler, M. L. A microfluidic
device for a pharmacokinetic–pharmacodynamic
(PK–PD) model on a chip. Lab Chip 10, 446–455
(2010).

150. Tatosian, D. A. & Shuler, M. L. A novel system for

evaluation of drug mixtures for potential efficacy in
treating multidrug resistant cancers. Biotechnol. Bioeng.
103, 187–198 (2009).

www.nature.com/nrmpPrimer0123456789();: 151. Stokes, C. L., Cirit, M. & Lauffenburger, D. A.

Physiome- on-a- chip: the challenge of “scaling”
in design, operation, and translation of micro-
physiological systems. CPT Pharmacomet. Syst.
Pharmacol. 4, 559–562 (2015).

152. Wikswo, J. P. et al. Scaling and systems biology for
integrating multiple organs- on-a- chip. Lab Chip 13,
3496–3511 (2013).

153. Yu, J. et al. Quantitative systems pharmacology

approaches applied to microphysiological systems
(MPS): data interpretation and multi- MPS integration.
CPT Pharmacomet. Syst. Pharmacol. 4, 585–594
(2015).

154. Bai, J. et al. A novel 3D vascular assay for evaluating

angiogenesis across porous membranes. Biomaterials
268, 120592 (2021).

155. Carter, S. D., Barbe, L., Tenje, M. & Mestres, G.
Exploring microfluidics as a tool to evaluate the
biological properties of a titanium alloy under dynamic
conditions. Biomater. Sci. 8, 6309–6321 (2020).

156. Chueh, B. H. et al. Leakage- free bonding of porous
membranes into layered microfluidic array systems.
Anal. Chem. 79, 3504–3508 (2007).

157. Winkler, T. E., Feil, M., Stronkman, E., Matthiesen, I.

& Herland, A. Low- cost microphysiological systems:
feasibility study of a tape- based barrier- on-chip for
small intestine modeling. Lab Chip 20, 1212–1226
(2020).

158. Schneider, S., Gruner, D., Richter, A. & Loskill, P.

Membrane integration into PDMS- free microfluidic
platforms for organ- on-chip and analytical chemistry
applications. Lab Chip 21, 1866–1885 (2021).
159. Kuo, C. H., Xian, J., Brenton, J. D., Franze, K. &

Sivaniah, E. Complex stiffness gradient substrates
for studying mechanotactic cell migration. Adv. Mater.
24, 6059–6064 (2012).

160. Zink, C., Hall, H., Brunette, D. M. & Spencer, N. D.
Orthogonal nanometer–micrometer roughness
gradients probe morphological influences on cell
behavior. Biomaterials 33, 8055–8061 (2012).
161. Kim, T. H. et al. Creating stiffness gradient polyvinyl

alcohol hydrogel using a simple gradual freezing–
thawing method to investigate stem cell differentiation
behaviors. Biomaterials 40, 51–60 (2015).

162. Oh, S. H., An, D. B., Kim, T. H. & Lee, J. H. Wide- range
stiffness gradient PVA/HA hydrogel to investigate stem
cell differentiation behavior. Acta Biomater. 35,
23–31 (2016).

163. Mei, Y. et al. Combinatorial development of

biomaterials for clonal growth of human pluripotent
stem cells. Nat. Mater. 9, 768–778 (2010).

164. Jana, S., Levengood, S. K. & Zhang, M. Anisotropic

materials for skeletal- muscle-tissue engineering.
Adv. Mater. 28, 10588–10612 (2016).

165. Kim, D.-H. et al. Mechanosensitivity of fibroblast cell
shape and movement to anisotropic substratum
topography gradients. Biomaterials 30, 5433–5444
(2009).

166. Park, J. et al. Directed migration of cancer cells guided
by the graded texture of the underlying matrix.
Nat. Mater. 15, 792–801 (2016).

167. Zhou, Q. et al. Screening platform for cell contact

guidance based on inorganic biomaterial micro/
nanotopographical gradients. ACS Appl. Mater.
Interfaces 9, 31433–31445 (2017).

168. Perlman, R. L. Mouse models of human disease:

an evolutionary perspective. Evol. Med. Public Health
2016, 170–176 (2016).

169. Mestas, J. & Hughes, C. C. W. Of mice and not men:
differences between mouse and human immunology.
J. Immunol. 172, 2731–2738 (2004).

170. Dellaquila, A., Thomée, E. K., McMillan, A. H. &

Lesher- Pérez, S. C. in Organ- on-a- Chip (eds Hoeng, J.,
Bovard, D. & Peitsch, M. C.) 133–180 (Academic,
2020).

171. Bliley, J. M. et al. Dynamic loading of human

engineered heart tissue enhances contractile function
and drives a desmosome- linked disease phenotype.
Sci. Transl. Med. 13, eabd1817 (2021).

172. Trapecar, M. et al. Gut–liver physiomimetics reveal

paradoxical modulation of IBD- related inflammation
by short- chain fatty acids. Cell Syst. 10, 223–239.e9
(2020).

173. Ahn, J., Sei, Y. J., Jeon, N. L. & Kim, Y. Tumor

microenvironment on a chip: the progress and future
perspective. Bioengineering 4, 64 (2017).
174. Park, D., Lim, J., Park, J. Y. & Lee, S. H. Concise

review: stem cell microenvironment on a chip: current
technologies for tissue engineering and stem cell
biology. Stem Cell Transl. Med. 4, 1352–1368 (2015).

175. Selimović, Š., Kaji, H., Bae, H. & Khademhosseini, A.
in Microfluidic Cell Culture Systems 2nd edn

(eds Borenstein, J. T., Tandon, V., Tao, S. L &
Charest, J. L) 31–63 (Elsevier, 2019).

176. Shang, M., Soon, R. H., Lim, C. T., Khoo, B. L. &
Han, J. Microfluidic modelling of the tumor micro-
environment for anti- cancer drug development.
Lab Chip 19, 369–386 (2019).

177. Przybyla, L. & Voldman, J. Probing embryonic

stem cell autocrine and paracrine signaling using
microfluidics. Annu. Rev. Anal. Chem. 5, 293–315
(2012).
This review paper explains the physics governing
the use of microfluidic cell culture to control the
presentation of soluble factors to cells in order
to investigate paracrine and autocrine signalling.
178. Toh, A. G. G., Wang, Z. P., Yang, C. & Nguyen, N.-T.

Engineering microfluidic concentration gradient
generators for biological applications. Microfluidics
Nanofluidics 16, 1–18 (2014).

179. Wang, X., Liu, Z. & Pang, Y. Concentration gradient
generation methods based on microfluidic systems.
RSC Adv. 7, 29966–29984 (2017).

180. Gómez- Sjöberg, R., Leyrat, A. A., Pirone, D. M.,

Chen, C. S. & Quake, S. R. Versatile, fully automated,
microfluidic cell culture system. Anal. Chem. 79,
8557–8563 (2007).

181. Titmarsh, D. M. et al. Induction of human iPSC- derived
cardiomyocyte proliferation revealed by combinatorial
screening in high density microbioreactor arrays.
Sci. Rep. 6, 24637 (2016).

182. Cosson, S. & Lutolf, M. P. Hydrogel microfluidics for
the patterning of pluripotent stem cells. Sci. Rep. 4,
4462 (2014).

183. Manfrin, A. et al. Engineered signaling centers for the

spatially controlled patterning of human pluripotent
stem cells. Nat. Methods 16, 640–648 (2019).

184. Rhee, S. W. et al. Patterned cell culture inside

microfluidic devices. Lab Chip 5, 102–107 (2005).
185. Chiu, D. T. et al. Patterned deposition of cells and
proteins onto surfaces by using three- dimensional
microfluidic systems. Proc. Natl Acad. Sci. USA 97,
2408–2413 (2000).

186. Jeon, K. J. et al. Combined effects of flow- induced

shear stress and micropatterned surface morphology
on neuronal differentiation of human mesenchymal
stem cells. J. Biosci. Bioeng. 117, 242–247 (2014).

187. Tu, C. et al. A microfluidic chip for cell patterning
utilizing paired microwells and protein patterns.
Micromachines 8, 1 (2017).

188. Skelley, A. M., Kirak, O., Suh, H., Jaenisch, R. &

Voldman, J. Microfluidic control of cell pairing and
fusion. Nat. Methods 6, 147–152 (2009).

189. Flaim, C. J., Chien, S. & Bhatia, S. N. An extracellular
matrix microarray for probing cellular differentiation.
Nat. Methods 2, 119–125 (2005).

190. McCain, M. L., Yuan, H., Pasqualini, F. S., Campbell, P. H.
& Parker, K. K. Matrix elasticity regulates the optimal
cardiac myocyte shape for contractility. Am. J. Physiol.
Heart Circul. Physiol. 306, H1525–H1539 (2014).

191. Vázquez- Victorio, G. et al. Building a microfluidic cell

culture platform with stiffness control using Loctite
3525 glue. Lab Chip 19, 3512–3525 (2019).

192. Pasman, T., Grijpma, D., Stamatialis, D. & Poot, A. Flat
and microstructured polymeric membranes in organs-
on-chips. J. R. Soc. Interface 15, 20180351 (2018).

193. Arora, S., Lin, S., Cheung, C., Yim, E. K. F. & Toh, Y.-C.

Topography elicits distinct phenotypes and functions in
human primary and stem cell derived endothelial cells.
Biomaterials 234, 119747 (2020).

194. Chau, L., Doran, M. & Cooper- White, J. A novel

multishear microdevice for studying cell mechanics.
Lab Chip 9, 1897–1902 (2009).

195. Arora, S., Lam, A. J. Y., Cheung, C., Yim, E. K. F. &
Toh, Y.-C. Determination of critical shear stress for
maturation of human pluripotent stem cell- derived
endothelial cells towards an arterial subtype.
Biotechnol. Bioeng. 116, 1164–1175 (2019).

196. Visone, R. et al. A microscale biomimetic platform for
generation and electro- mechanical stimulation of 3D
cardiac microtissues. APL. Bioeng. 2, 046102 (2018).

197. Duc, P. et al. Human neuromuscular junction on micro-
structured microfluidic devices implemented with a
custom micro electrode array (MEA). Lab Chip 21,
4223–4236 (2021).

198. Beckwitt, C. H. et al. Liver ‘organ on a chip’. Exp. Cell

Res. 363, 15–25 (2018).

201. Khetani, S. R. & Bhatia, S. N. Microscale culture
of human liver cells for drug development.
Nat. Biotechnol. 26, 120–126 (2008).

202. Sivaraman, A. et al. A microscale in vitro physiological

model of the liver: predictive screens for drug
metabolism and enzyme induction. Curr. Drug Metab.
6, 569–591 (2005).

203. Boon, R. et al. Amino acid levels determine metabolism

and CYP450 function of hepatocytes and hepatoma
cell lines. Nat. Commun. 11, 1393 (2020).
204. Chao, P., Maguire, T., Novik, E., Cheng, K. C. &

Yarmush, M. L. Evaluation of a microfluidic based cell
culture platform with primary human hepatocytes for
the prediction of hepatic clearance in human.
Biochem. Pharmacol. 78, 625–632 (2009).

205. Goral, V. N. et al. Perfusion- based microfluidic device
for three- dimensional dynamic primary human
hepatocyte cell culture in the absence of biological
or synthetic matrices or coagulants. Lab Chip 10,
3380–3386 (2010).

206. Hegde, M. et al. Dynamic interplay of flow and

collagen stabilizes primary hepatocytes culture in a
microfluidic platform. Lab Chip 14, 2033–2039
(2014).

207. Lee, P. J., Hung, P. J. & Lee, L. P. An artificial liver

sinusoid with a microfluidic endothelial- like barrier for
primary hepatocyte culture. Biotechnol. Bioeng. 97,
1340–1346 (2007).

208. Toh, Y. C. et al. A microfluidic 3D hepatocyte chip for

drug toxicity testing. Lab Chip 9, 2026–2035 (2009).
209. Clark, A. M. et al. A liver microphysiological system of
tumor cell dormancy and inflammatory responsiveness
is affected by scaffold properties. Lab Chip 17, 156–168
(2016).

210.  Deng, J. et al. A liver- on-a- chip for hepatoprotective

activity assessment. Biomicrofluidics 14, 064107
(2020).

211.  Vernetti, L. A. et al. A human liver microphysiology

platform for investigating physiology, drug safety, and
disease models. Exp. Biol. Med. 241, 101–114
(2016).

212. Ströbel, S. et al. A 3D primary human cell- based
in vitro model of non- alcoholic steatohepatitis for
efficacy testing of clinical drug candidates. Sci. Rep.
11, 22765 (2021).

213. Müller, F. A. & Sturla, S. J. Human in vitro models of

nonalcoholic fatty liver disease. Curr. Opin. Toxicol.
16, 9–16 (2019).

214. Ronaldson- Bouchard, K. et al. Advanced maturation
of human cardiac tissue grown from pluripotent stem
cells. Nature 556, 239–243 (2018).

215. Zhao, Y. et al. A platform for generation of chamber-

specific cardiac tissues and disease modeling. Cell
176, 913–927.e918 (2019).

216. Kaisar, M. A. et al. New experimental models of the
blood–brain barrier for CNS drug discovery. Expert
Opin. Drug Discov. 12, 89–103 (2017).

217. Herland, A. et al. Distinct contributions of astrocytes
and pericytes to neuroinflammation identified in a 3D
human blood–brain barrier on a chip. PLoS ONE 11,
e0150360 (2016).

218. Wang, J. D., Khafagy el, S., Khanafer, K., Takayama, S.
& ElSayed, M. E. Organization of endothelial cells,
pericytes, and astrocytes into a 3D microfluidic in vitro
model of the blood–brain barrier. Mol. Pharm. 13,
895–906 (2016).

219. Wevers, N. R. et al. A perfused human blood–brain

barrier on- a-chip for high- throughput assessment
of barrier function and antibody transport. Fluids
Barriers CNS 15, 23 (2018).

220. Park, T.-E. et al. Hypoxia- enhanced blood–brain

barrier chip recapitulates human barrier function and
shuttling of drugs and antibodies. Nat. Commun. 10,
2621 (2019).

221. Jin, L. Y. et al. Blood–spinal cord barrier in spinal cord
injury: a review. J. Neurotrauma 38, 1203–1224
(2021).

222. Zheng, W. et al. Differentiation of glial cells from

hiPSCs: potential applications in neurological diseases
and cell replacement therapy. Front. Cell. Neurosci.
12, 239 (2018).

223. Chiaradia, I. & Lancaster, M. A. Brain organoids for
the study of human neurobiology at the interface of
in vitro and in vivo. Nat. Neurosci. 23, 1496–1508
(2020).

199. Deng, J. et al. Engineered liver- on-a- chip platform to

224. Eugène, E. et al. An organotypic brain slice

mimic liver functions and its biomedical applications:
a review. Micromachines 10, 676 (2019).

200. Starokozhko, V. & Groothuis, G. M. Judging the value

preparation from adult patients with temporal lobe
epilepsy. J. Neurosci. Methods 235, 234–244
(2014).

of ‘liver- on-a- chip’ devices for prediction of toxicity.
Expert Opin. Drug Metab. Toxicol. 13, 125–128
(2017).

225. Schwarz, N. et al. Long- term adult human brain slice
cultures as a model system to study human CNS
circuitry and disease. eLife 8, e48417 (2019).

 27

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
254. Roberts, N. & Horsley, V. Developing stratified

278. Werner, M. et al. Surface curvature differentially

226. Cakir, B. et al. Engineering of human brain organoids
with a functional vascular- like system. Nat. Methods
16, 1169–1175 (2019).

227. Liu, J., Pan, L., Cheng, X. & Berdichevsky, Y. Perfused
drop microfluidic device for brain slice culture- based
drug discovery. Biomed. Microdevices 18, 46 (2016).

228. Wang, Y., Wang, L., Zhu, Y. & Qin, J. Human brain
organoid- on-a- chip to model prenatal nicotine
exposure. Lab Chip 18, 851–860 (2018).
229. Sharma, A. D. et al. Engineering a 3D functional

human peripheral nerve in vitro using the nerve- on-a-
chip platform. Sci. Rep. 9, 8921 (2019).

230. Hyung, S. et al. A 3D disease and regeneration model

of peripheral nervous system- on-a- chip. Sci. Adv. 7,
eabd9749 (2021).

231. Johnson, B. N. et al. 3D printed nervous system on a

chip. Lab Chip 16, 1393–1400 (2016).

232. Benam, K. H. et al. Small airway- on-a- chip enables
analysis of human lung inflammation and drug
responses in vitro. Nat. Methods 13, 151–157 (2016).

233. Humayun, M., Chow, C. W. & Young, E. W. K.

epithelia: lessons from the epidermis and thymus.
WIREs Dev. Biol. 3, 389–402 (2014).

255. Ma, C., Peng, Y., Li, H. & Chen, W. Organ- on-a- chip:
a new paradigm for drug development. Trends
Pharmacol. Sci. 42, 119–133 (2021).

256. Viravaidya, K. & Shuler, M. L. Incorporation of 3T3-L1
cells to mimic bioaccumulation in a microscale cell
culture analog device for toxicity studies. Biotechnol.
Prog. 20, 590–597 (2004).

257. Renggli, K. & Frey, O. in Organ- on-a- chip

(eds Hoeng, J., Bovard, D. & Peitsch, M. C.) 393–427
(Academic, 2020).

258. Picollet- D’hahan, N., Zuchowska, A., Lemeunier, I. &

Le Gac, S. Multiorgan- on-a- chip: a systemic approach
to model and decipher inter- organ communication.
Trends Biotechnol. 39, 788–810 (2021).
This paper provides a comprehensive review of the
various applications of multi- OoCs and the different
design approaches of coupling individual organ
systems.

Microfluidic lung airway- on-a- chip with arrayable
suspended gels for studying epithelial and smooth
muscle cell interactions. Lab Chip 18, 1298–1309
(2018).

259. Lee, J. & Kim, S. Kidney- on-a- chip: a new technology

for predicting drug efficacy, interactions, and drug-
induced nephrotoxicity. Curr. Drug Metab. 19,
577–583 (2018).

234. Shrestha, J. et al. A rapidly prototyped lung- on-a- chip

260. Lee, J., Kim, K. & Kim, S. in Methods in Cell Biology

model using 3D- printed molds. Organs- on-a- Chip 1,
100001 (2019).

235. Si, L. et al. A human- airway-on- a-chip for the rapid

identification of candidate antiviral therapeutics and
prophylactics. Nat. Biomed. Eng. 5, 815–829 (2021).
236. Zamprogno, P. et al. Second- generation lung- on-a- chip
with an array of stretchable alveoli made with a
biological membrane. Commun. Biol. 4, 168 (2021).

Vol. 146 (eds Doh, J., Fletcher, D. & Piel, J.) 85–104
(Academic, 2018).

261. Miller, P. G. & Shuler, M. L. Design and demonstration
of a pumpless 14 compartment microphysiological
system. Biotechnol. Bioeng. 113, 2213–2227 (2016).

262. Piergiovanni, M., Leite, S. B., Corvi, R. & Whelan, M.
Standardisation needs for organ on chip devices. Lab
Chip 21, 2857–2868 (2021).

237. Ataç, B. et al. Skin and hair on- a-chip: in vitro skin

263. Kilic, T., Navaee, F., Stradolini, F., Renaud, P. &

models versus ex vivo tissue maintenance with
dynamic perfusion. Lab Chip 13, 3555–3561 (2013).

Carrara, S. Organs- on-chip monitoring: sensors and
other strategies. Microphysiol. Syst. 2, 1–32 (2018).

238. Lee, S. et al. Construction of 3D multicellular

microfluidic chip for an in vitro skin model. Biomed.
Microdevices 19, 22 (2017).

239. Sriram, G. et al. Full- thickness human skin- on-chip

with enhanced epidermal morphogenesis and barrier
function. Mater. Today 21, 326–340 (2018).

240. de Haan, P. et al. A versatile, compartmentalised gut-

on-a- chip system for pharmacological and toxicological
analyses. Sci. Rep. 11, 4920 (2021).

241. Kasendra, M. et al. Duodenum intestine- chip for
preclinical drug assessment in a human relevant
model. eLife 9, e50135 (2020).

242. Abdalkader, R. & Kamei, K. I. Multi- corneal barrier-

on-a- chip to recapitulate eye blinking shear stress
forces. Lab Chip 20, 1410–1417 (2020).

243. Bai, J., Fu, H., Bazinet, L., Birsner, A. E. &

D’Amato, R. J. A method for developing novel 3D
cornea- on-a- chip using primary murine corneal
epithelial and endothelial cells. Front. Pharmacol. 11,
453 (2020).

244. Bennet, D., Estlack, Z., Reid, T. & Kim, J. A micro-

engineered human corneal epithelium- on-a- chip for
eye drops mass transport evaluation. Lab Chip 18,
1539–1551 (2018).

245. Cao, X. et al. Invited review: human air–liquid-

interface organotypic airway tissue models derived
from primary tracheobronchial epithelial cells —
overview and perspectives. In Vitro Cell Dev. Biol.
Anim. 57, 104–132 (2021).

246. Chiba, H., Osanai, M., Murata, M., Kojima, T. &

Sawada, N. Transmembrane proteins of tight junctions.
Biochim. Biophys. Acta 1778, 588–600 (2008).
247. Park, J. Y. et al. Development of a functional airway-
on-a- chip by 3D cell printing. Biofabrication 11,
015002 (2018).

248. Stucki, J. D. et al. Medium throughput breathing

human primary cell alveolus- on-chip model. Sci. Rep.
8, 14359 (2018).

249. Gijzen, L. et al. An intestine- on-a- chip model of plug-

and-play modularity to study inflammatory processes.
SLAS Technol. 25, 585–597 (2020).

250. van der Helm, M. W. et al. Non- invasive sensing
of transepithelial barrier function and tissue
differentiation in organs- on-chips using impedance
spectroscopy. Lab Chip 19, 452–463 (2019).
251. Zoio, P., Lopes- Ventura, S. & Oliva, A. Barrier- on-a-

chip with a modular architecture and integrated
sensors for real- time measurement of biological
barrier function. Micromachines 12, 816 (2021).

252. Ramadan, Q. & Ting, F. C. W. In vitro micro-

physiological immune- competent model of the human
skin. Lab Chip 16, 1899–1908 (2016).

253. Yu, Z., Hao, R., Zhang, Y. & Yang, H. in 2021 IEEE 34th

Int. Conf. Micro Electro Mechanical Systems (MEMS)
982–985 (IEEE, 2021).

264. EU Science Hub. European Union Reference Laboratory
for alternatives to animal testing. EURL ECVAM.
Europrean Commission https://ec.europa.eu/jrc/en/
eurl/ecvam (2021).

265. Piergiovanni, M. et al. Organ on Chip: Building a

Roadmap Towards Standardisation (European
Commission, 2021).

266. Piergiovanni, M. et al. Putting Science into Standards

workshop on standards for organ- on-chip. Stem Cell
Rep. 16, 2076–2077 (2021).

267. Peirsman, A. et al. MISpheroID: a knowledgebase and
transparency tool for minimum information in spheroid
identity. Nat. Methods 18, 1294–1303 (2021).
268. Greaney, A. M. et al. Platform effects on regeneration

by pulmonary basal cells as evaluated by single- cell
RNA sequencing. Cell Rep. 30, 4250–4265.e6 (2020).

269. Vunjak- Novakovic, G., Ronaldson- Bouchard, K. &

Radisic, M. Organs- on-a- chip models for biological
research. Cell 184, 4597–4611 (2021).
This article is complementary to the present
Primer and provides a perspective of how the
tissue engineering paradigm, which involves the
integration of cells, scaffolds and bioreactors, has
been applied to drive the development of OoCs
intended for biological research.

270. Johnson, B. P. et al. A microphysiological approach to
evaluate effectors of intercellular hedgehog signaling
in development. Front. Cell Dev. Biol. 9, 621442
(2021).

271. Komeya, M. et al. Pumpless microfluidic system driven
by hydrostatic pressure induces and maintains mouse
spermatogenesis in vitro. Sci. Rep. 7, 15459 (2017).
272. Glieberman, A. L. et al. Synchronized stimulation and

continuous insulin sensing in a microfluidic human
islet on a chip designed for scalable manufacturing.
Lab Chip 19, 2993–3010 (2019).

273. Modena, M. M., Chawla, K., Misun, P. M. &

Hierlemann, A. Smart cell culture systems: integration
of sensors and actuators into microphysiological
systems. ACS Chem. Biol. 13, 1767–1784 (2018).
274. Liao, Z. et al. Microfluidic chip coupled with optical

biosensors for simultaneous detection of multiple
analytes: a review. Biosens. Bioelectron. 126,
697–706 (2019).

275. Hiramoto, K., Ino, K., Nashimoto, Y., Ito, K. & Shiku, H.

Electric and electrochemical microfluidic devices for
cell analysis. Front. Chem. 7, 396 (2019).
276. van Meer, B. J. et al. Small molecule absorption

by PDMS in the context of drug response bioassays.
Biochem. Biophys. Res. Commun. 482, 323–328
(2017).

277. Kim, S. et al. Anchor- IMPACT: a standardized
microfluidic platform for high- throughput
antiangiogenic drug screening. Biotechnol. Bioeng.
118, 2524–2535 (2021).

28 | Article citation ID:            (2022) 2:33

regulates stem cell migration and differentiation via
altered attachment morphology and nuclear
deformation. Adv. Sci. 4, 1600347 (2017).

279. Wang, J. D. Development of a 3D in Vitro Model of the

Blood–Brain Barrier in Layered Microfluidic Devices.
PhD thesis, Univ. of Michigan (2015).

280. Shin, W., Hinojosa, C. D., Ingber, D. E. & Kim, H. J.
Human intestinal morphogenesis controlled by
transepithelial morphogen gradient and flow-
dependent physical cues in a microengineered
gut-on-a- chip. iScience 15, 391–406 (2019).
281. Albrecht, W. et al. Prediction of human drug- induced

liver injury (DILI) in relation to oral doses and blood
concentrations. Arch. Toxicol. 93, 1609–1637 (2019).
282. Park, J. et al. A 3D human triculture system modeling

neurodegeneration and neuroinflammation in
Alzheimer’s disease. Nat. Neurosci. 21, 941–951
(2018).

283. Ekert, J. E. et al. Recommended guidelines for

developing, qualifying, and implementing complex
in vitro models (CIVMs) for drug discovery. SLAS
Discov. 25, 1174–1190 (2020).

284. Kopec, A. K. et al. Microphysiological systems in early
stage drug development: perspectives on current
applications and future impact. J. Toxicol. Sci. 46,
99–114 (2021).

285. Chou, D. B. et al. On- chip recapitulation of clinical
bone marrow toxicities and patient- specific
pathophysiology. Nat. Biomed. Eng. 4, 394–406
(2020).

286. LaValley, D. J., Miller, P. G. & Shuler, M. L. Pumpless,

unidirectional microphysiological system for testing
metabolism- dependent chemotherapeutic toxicity.
Biotechnol. Prog. 37, e3105 (2021).

287. McCracken, K. W. et al. Modelling human development
and disease in pluripotent stem- cell-derived gastric
organoids. Nature 516, 400–404 (2014).

288. Park, D., Lee, J., Chung, J. J., Jung, Y. & Kim, S. H.
Integrating organs- on-chips: multiplexing, scaling,
vascularization, and innervation. Trends Biotechnol.
38, 99–112 (2020).

289. Vila, O. F. et al. Bioengineered optogenetic model of
human neuromuscular junction. Biomaterials 276,
121033 (2021).

290. Habert, R. et al. Concerns about the widespread use
of rodent models for human risk assessments of
endocrine disruptors. Reproduction 147, R119–R129
(2014).

291. Sun, H., Jia, Y., Dong, H., Dong, D. & Zheng, J.

Combining additive manufacturing with microfluidics:
an emerging method for developing novel organs-
on-chips. Curr. Opin. Chem. Eng. 28, 1–9 (2020).
This review provides an update on the integration
of additive manufacturing technologies such as 3D
printing to fabricate OoC devices.

292. Trietsch, S. J., Israëls, G. D., Joore, J., Hankemeier, T.
& Vulto, P. Microfluidic titer plate for stratified 3D cell
culture. Lab Chip 13, 3548–3554 (2013).
This paper presents a stratified 3D cell culture
platform with side- by-side gel and liquid lanes in a
microtitre plate format. Cells in neighbouring lanes
can interact, and analysis can be done in high
throughput.

293. Esch, M. B., Ueno, H., Applegate, D. R. & Shuler, M. L.
Modular, pumpless body- on-a- chip platform for the co-
culture of GI tract epithelium and 3D primary liver
tissue. Lab Chip 16, 2719–2729 (2016).

294. Loskill, P., Marcus, S. G., Mathur, A., Reese, W. M. &
Healy, K. E. μOrgano: a lego®-like plug & play system
for modular multi- organ-chips. PLoS ONE 10,
e0139587 (2015).

295. Vollertsen, A. R. et al. Facilitating implementation

of organs- on-chips by open platform technology.
Biomicrofluidics 15, 051301 (2021).

296. Castillo- Armengol, J., Fajas, L. & Lopez- Mejia, I. C.
Inter- organ communication: a gatekeeper for
metabolic health. EMBO Rep. 20, e47903 (2019).
297. Gancheva, S., Jelenik, T., Álvarez- Hernández, E. &

Roden, M. Interorgan metabolic crosstalk in human
insulin resistance. Physiol. Rev. 98, 1371–1415
(2018).

298. Ogurtsova, K. et al. IDF Diabetes Atlas: global

estimates for the prevalence of diabetes for 2015 and
2040. Diabetes Res. Clin. Pract. 128, 40–50 (2017).
299. Yang, J. et al. Integrated gut–liver- on-a- chip platform
as an in vitro human model of non- alcoholic fatty liver
disease. Preprint at bioRxiv https://doi.org/10.1101/
2020.06.10.141606 (2020).

300. Lee, S. Y. & Sung, J. H. Gut–liver on a chip toward an

in vitro model of hepatic steatosis. Biotechnol. Bioeng.
115, 2817–2827 (2018).

www.nature.com/nrmpPrimer0123456789();: resistance across epithelial and endothelial barriers.
Anal. Chem. 82, 2505–2511 (2010).

317. Poussin, C. et al. 3D human microvessel- on-a- chip

model for studying monocyte- to-endothelium adhesion
under flow — application in systems toxicology. Altex
37, 47–63 (2020).

318. Mori, N., Morimoto, Y. & Takeuchi, S. Skin integrated

333. Bircsak, K. M. et al. A 3D microfluidic liver model
for high throughput compound toxicity screening
in the OrganoPlate®. Toxicology 450, 152667
(2021).

334. Domansky, K. et al. Perfused multiwell plate for
3D liver tissue engineering. Lab Chip 10, 51–58
(2010).

301. Jeon, J.-W., Lee, S. H., Kim, D. & Sung, J. H. In vitro

hepatic steatosis model based on gut–liver- on-a- chip.
Biotechnol. Prog. 37, e3121 (2021).

302. Essaouiba, A. et al. Development of a pancreas–liver
organ- on-chip coculture model for organ- to-organ
interaction studies. Biochem. Eng. J. 164, 107783
(2020).

303. Bauer, S. et al. Functional coupling of human pancreatic
islets and liver spheroids on- a-chip: towards a novel
human ex vivo type 2 diabetes model. Sci. Rep. 7,
14620 (2017).

304. Cho, I. & Blaser, M. J. The human microbiome: at the
interface of health and disease. Nat. Rev. Genet. 13,
260–270 (2012).

305. Tan, H.-Y. & Toh, Y.-C. What can microfluidics do for
human microbiome research? Biomicrofluidics 14,
051303 (2020).
This review highlights OoC systems that specifically
model microbial–mammalian host tissue
interactions.

with perfusable vascular channels on a chip.
Biomaterials 116, 48–56 (2017).

319. Ong, L. J. Y. et al. A 3D printed microfluidic

perfusion device for multicellular spheroid cultures.
Biofabrication 9, 045005 (2017).

320. Asif, A., Kim, K. H., Jabbar, F., Kim, S. & Choi, K.

Real- time sensors for live monitoring of disease and
drug analysis in microfluidic model of proximal tubule.
Microfluid. Nanofluidics 24, 1–10 (2020).

321. Khoshfetrat Pakazad, S., Savov, A., van de Stolpe, A.
& Dekker, R. A novel stretchable micro- electrode
array (SMEA) design for directional stretching of cells.
J. Micromech. Microeng. 24, 034003 (2014).

306. Polini, A. et al. Towards the development of human

322. Liu, Y. et al. Adipose- on-a- chip: a dynamic

immune- system-on- a-chip platforms. Drug Discov. Today
24, 517–525 (2019).
This review provides an overview of key
characteristics of the human immune system and
how different aspects of human immunity can be
modelled by OoC systems.

microphysiological in vitro model of the human
adipose for immune- metabolic analysis in type II
diabetes. Lab Chip 19, 241–253 (2019).

323. Huh, D. et al. Microfabrication of human organs-
on-chips. Nat. Protoc. 8, 2135–2157 (2013).

324. Zhang, W., Zhang, H., Williams, S. E. & Zhou, A.

307. Miller, C. P., Shin, W., Ahn, E. H., Kim, H. J. &

Kim, D.-H. Engineering microphysiological immune
system responses on chips. Trends Biotechnol. 38,
857–872 (2020).

308. Park, D. et al. High- throughput microfluidic 3D

cytotoxicity assay for cancer immunotherapy
(CACI- IMPACT Platform). Front. Immunol. 10,
1133 (2019).

309. Lee, S. et al. Modeling 3D human tumor lymphatic

vessel network using high- throughput platform.
Adv. Biol. 5, 2000195 (2021).

310.  Hind, L. E., Ingram, P. N., Beebe, D. J. &

Huttenlocher, A. Interaction with an endothelial
lumen increases neutrophil lifetime and motility in
response to P. aeruginosa. Blood 132, 1818–1828
(2018).

311.  Hind, L. E. et al. Immune cell paracrine signaling

drives the neutrophil response to A. fumigatus in
an infection- on-a- chip model. Cell. Mol. Bioeng. 14,
133–145 (2021).

312. Weerappuli, P. D. et al. Extracellular trap- mimicking
DNA–histone mesostructures synergistically activate
dendritic cells. Adv. Healthc. Mater. 8, 1900926
(2019).

313. Tao, T. et al. Microengineered multi- organoid system
from hipscs to recapitulate human liver–islet axis in
normal and type 2 diabetes. Adv. Sci. 9, e2103495
(2022).

314. Yin, F. et al. HiPSC- derived multi- organoids-on- chip

system for safety assessment of antidepressant drugs.
Lab Chip 21, 571–581 (2021).

315. Osaki, T., Uzel, S. G. M. & Kamm, R. D. On- chip 3D

neuromuscular model for drug screening and precision
medicine in neuromuscular disease. Nat. Protoc. 15,
421–449 (2020).

316. Douville, N. J. et al. Fabrication of two- layered

channel system with embedded electrodes to measure

Microfabricated three- electrode on- chip PDMS device
with a vibration motor for stripping voltammetric
detection of heavy metal ions. Talanta 132, 321–326
(2015).

325. Lee, B. et al. 3D micromesh- based hybrid bioprinting:
multidimensional liquid patterning for 3D microtissue
engineering. NPG Asia Mater. 14, 6 (2022).

326. Kang, H.-W. et al. A 3D bioprinting system to produce
human- scale tissue constructs with structural integrity.
Nat. Biotechnol. 34, 312–319 (2016).
327. Lee, S.-Y., Kim, D.-S., Kim, E.-S. & Lee, D.-W.

Nano-textured polyimide cantilever for enhancing
the contractile behavior of cardiomyocytes and its
application to cardiac toxicity screening. Sens. Actuators
B Chem. 301, 126995 (2019).

328. Riahi, R. et al. Automated microfluidic platform of

bead- based electrochemical immunosensor integrated
with bioreactor for continual monitoring of cell
secreted biomarkers. Sci. Rep. 6, 24598 (2016).
329. Schmittlein, C., Meier, R. J., Sauer, L., Liebsch, G. &
Wegener, J. Monitoring oxygenation in microfluidic
cell culture using 2D sensor foils as growth substrate.
PreSens https://www.presens.de/knowledge/
publications/application- note/monitoring-
oxygenation-in- microfluidic-cell- culture-using-2d-
sensor-foils- as-growth- substrate-full- text-1681 (2019).

330. Zervantonakis, I. K. et al. Three- dimensional

microfluidic model for tumor cell intravasation and
endothelial barrier function. Proc. Natl Acad. Sci. USA
109, 13515–13520 (2012).

331. LeCluyse, E. L., Witek, R. P., Andersen, M. E. &
Powers, M. J. Organotypic liver culture models:
meeting current challenges in toxicity testing.
Crit. Rev. Toxicol. 42, 501–548 (2012).

332. Zhang, S. et al. A robust high- throughput sandwich

cell- based drug screening platform. Biomaterials 32,
1229–1241 (2011).

335. Boos, J. A., Misun, P. M., Michlmayr, A., Hierlemann,
A. & Frey, O. Microfluidic multitissue platform for
advanced embryotoxicity testing in vitro. Adv. Sci. 6,
1900294 (2019).

336. Freag, M. S. et al. Human nonalcoholic steatohepatitis
on a chip. Hepatol. Commun. 5, 217–233 (2021).

337. Herland, A. et al. Quantitative prediction of human

pharmacokinetic responses to drugs via fluidically
coupled vascularized organ chips. Nat. Biomed. Eng.
4, 421–436 (2020).

Acknowledgements
This work was supported by National Institute of Health (NIH)
(U10A214300) awarded to M.L.S.; NIH (UG3EB025765,
CA249799, P41 EB027062 and R01HL136414), National
Science Foundation (NSF1647837), National Aeronautics
and Space Administration (NASA NNX16A069A) and BARDA
(75A50121C00017) awarded to G.V.- N.; National Research
Foundation of Korea (No. 2021R1A3B1077481) awarded to
N.L.J.;  Australian  Research  Council  (FT180100157,
DP200101658) awarded to Y.- C.T.; and National University of
Singapore Graduate School (NUSGS) Integrative Sciences and
Engineering Programme (ISEP) scholarship awarded to C.M.L.

Author contributions
Introduction (E.V., Y.- C.T., O.F. and G.V.- N.); Experimentation
(E.V., C.M.L., Y.- C.T., P.d.H., K.R.- B., G.V.- N., J.K. and N.L.J.);
Results (Y.- C.T., O.F. and M.L.S.); Applications (C.M.L., Y.- C.T.,
K.R.- B., G.V.- N., M.L.S., Z.C., H.S.R. and P.H.); Reproducibility
and data deposition (O.F., S.T. and P.d.H.); Limitations and
optimizations (G.- A.K. and S.T.); Outlook (C.M.L., Y.- C.T.,
G.V.- N., E.V., G.- A.K. and S.T.); Overview of the Primer (E.V.,
Y.- C.T., C.M.L. and P.d.H.).

Competing interests
O.F. is member of the management team of InSphero com-
mercializing 3D organ systems. K.R.- B. and G.V.- N. are
co- founders of Tara Biosystems, a Columbia University
start- up company commercializing organs- on- a- chip with
human heart muscle. M.L.S. is CEO and President of
Hesperos, Inc. All other authors declare no competing
interests.

Peer review information
Nature Reviews Methods Primers thanks Mandy Esch,
Zhongze Gu and the other, anonymous, reviewer(s) for their
contribution to the peer review of this work.

Publisher’s note
Springer Nature remains neutral with regard to jurisdictional
claims in published maps and institutional affiliations.

Supplementary information
The online version contains supplementary material available
at https://doi.org/10.1038/s43586-022-00118-6.

© Springer Nature Limited 2022

 29

NATURE REvIEWS | MEthODS PriMErS | Article citation ID:            (2022) 2:33 Primer0123456789();:
