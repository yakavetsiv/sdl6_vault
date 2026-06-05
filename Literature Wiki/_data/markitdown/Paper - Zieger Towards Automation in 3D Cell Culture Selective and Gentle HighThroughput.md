---
tags:
  - literature
  - type/paper
  - lit/biofabrication
  - lit/ai-methods
type: literature-note
source_note: "Papers/Paper - Zieger Towards Automation in 3D Cell Culture Selective and Gentle HighThroughput.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Adv Healthcare Materials - 2024 - Zieger - Towards Automation in 3D Cell Culture  Selective and Gentle High%E2%80%90Throughput.pdf"
converter: "microsoft/markitdown"
---
RESEARCH ARTICLE

www.advhealthmat.de

Towards Automation in 3D Cell Culture: Selective and
Gentle High-Throughput Handling of Spheroids and
Organoids via Novel Pick-Flow-Drop Principle

Viktoria Zieger,* Daniel Frejek, Stefan Zimmermann, Guilherme A. A. Miotto,
Peter Koltay, Roland Zengerle, and Sabrina Kartmann

3D cell culture is becoming increasingly important for mimicking
physiological tissue structures in areas such as drug discovery and
personalized medicine. To enable reproducibility on a large scale, automation
technologies for standardized handling are still a challenge. Here, a novel
method for fully automated size classiﬁcation and handling of cell aggregates
like spheroids and organoids is presented. Using microﬂuidic ﬂow generated
by a piezoelectric droplet generator, aggregates are aspirated from a reservoir
on one side of a thin capillary and deposited on the other side, encapsulated
in free-ﬂying nanoliter droplets to a target. The platform has aggregate
aspiration and plating eﬃciencies of 98.1% and 98.4%, respectively, at a
processing throughput of up to 21 aggregates per minute. Cytocompatibility
of the method is thoroughly assessed with MCF7, LNCaP, A549 spheroids
and colon organoids, revealing no adverse eﬀects on cell aggregates as shear
stress is reduced compared to manual pipetting. Further, generic size-selective
handling of heterogeneous organoid samples, single-aggregate-dispensing
eﬃciencies of up to 100% and the successful embedding of spheroids or
organoids in a hydrogel with subsequent proliferation is demonstrated. This
platform is a powerful tool for standardized 3D in vitro research.

or personalized therapy approaches.[1] In
particular, multicellular aggregates such
as spheroids or organoids are candidates
to bridge the gap between standard 2D
cell culture and complex, expensive, eth-
and time-consuming
ically debatable,
xenografts.[2,3] Research using 3D cell
culture models typically involves many
manual steps.[3] The increased complexity
of the models introduces a wide range of
inter- as well as intra-sample heterogeneity
with respect to variations in size, shape, cell
composition, and architecture of individual
cell aggregates. This heterogeneity chal-
lenges the interpretation of study results
involving assessments such as prolifera-
tion, growth, and invasion behavior.[4] In
addition, diﬀerent handling steps, varia-
tions due to diﬀerent operators, low levels
of automation or low throughput reduce
the comparability of results and limit the
potential of 3D in vitro studies.[5]

1. Introduction

3D in vitro models are useful tools to mimic in vivo behavior
under physiological conditions, for example, for drug screening

V. Zieger, S. Zimmermann, P. Koltay, R. Zengerle, S. Kartmann
Laboratory for MEMS Applications
IMTEK- Department of Microsystems Engineering
University of Freiburg
Georges-Koehler-Allee 103, D-79110 Freiburg, Germany
E-mail: viktoria.zieger@imtek.uni-freiburg.de
D. Frejek, G. A. A. Miotto, R. Zengerle, S. Kartmann
Hahn-Schickard
Georges-Koehler-Allee 103, D-79110 Freiburg, Germany

The ORCID identiﬁcation number(s) for the author(s) of this article
can be found under https://doi.org/10.1002/adhm.202303350
© 2024 The Authors. Advanced Healthcare Materials published by
Wiley-VCH GmbH. This is an open access article under the terms of the
Creative Commons Attribution-NonCommercial License, which permits
use, distribution and reproduction in any medium, provided the original
work is properly cited and is not used for commercial purposes.

DOI: 10.1002/adhm.202303350

Only a few techniques focus on the
placement
of 3D cell aggregates, which is essential to establish standard-
ized and user-controlled conditions for diﬀerent tasks and appli-
cations in 3D cell culture.

controlled

handling

and

One established technique for automated positioning of cell
aggregates is the Pick-and-Place method.[6] The spheroids are
partially or completely drawn into a pipette tip or thin capillary
by negative pressure. To place the spheroids to the desired target
position, the pressure is simply reversed. This method has been
widely used for example to study spheroid sprouting, to establish
assays with patient-derived organoids or to investigate eﬃcacy of
anticancer agents.[7,8] However, the method typically results in
low throughput rates of only two to four spheroids per minute,
large transferred volumes of liquid (several microliters) with each
pick, and high mechanical stress on the spheroids.[7,9] In addi-
tion, there is no solution for picking closely spaced spheroids in-
dividually. This means that the spheroid concentration and their
distribution in the reservoir must be optimized for each applica-
tion to minimize sample loss and avoid unspeciﬁc or unintended
picks.

Noncontact dispensing respectively Drop-on-Demand meth-
ods provide an alternative option for automated deposition of
spheroids or organoids. As previously shown by Gutzweiler and

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (1 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

www.advancedsciencenews.com

www.advhealthmat.de

Kartmann et al. and Dornhof and Zieger et al., it is possible to
deliver cell aggregates encapsulated in small free-ﬂying droplets
to a desired target position.[10,11] Common to all reported Drop-
on-Demand systems is that sorting for speciﬁc markers, such as
spheroid size, can only be done by detecting spheroid properties
in the nozzle region of the dispenser and placing spheroids with
diﬀerent properties to diﬀerent positions.[12] The eﬃciency of the
approach is therefore highly dependent on the proportion of the
desired fraction in the sample. Furthermore, technical challenges
such as nozzle clogging are common with impure and highly
concentrated samples.[13]

Other reported methods for the individual transfer of cell
aggregates either rely on exploitation of mechanical or ﬂuid-
driven spheroid manipulation, magnetic collection of spheroids
or acoustic bioprinting.[14] However, these techniques are typi-
cally limited to speciﬁc samples or culture conditions, custom
consumables, complex setups, and low throughput. To improve
standardization and automation in 3D cell culture, we see a
clear need for a technology that can provide a generic, sample-
independent way to handle spheroids or organoids with suﬃcient
selectivity, throughput, accuracy and eﬃciency, with the option to
handle heterogeneous samples in a user-conﬁgurable manner.

To address this need, we developed a new approach for well-
controlled and selective single spheroid or organoid deposition.
Our novel Pick-Flow-Drop principle combines elements of both,
the Pick-and-Place and the Drop-on-Demand method to opti-
mize processing eﬃciency, sample recovery and (selective) con-
trol over transferred cell aggregates. Cell aggregates are aspirated
from a reservoir and guided through a thin capillary at the end
of which a Drop-on-Demand dispenser deposits them to a de-
sired target location. We investigated the necessary measures to
provide reliable and targeted aspiration and precise single aggre-
gate deposition. Further, we demonstrated the size-selective and
high-throughput handling of heterogeneous cell aggregate sam-
ples, their fully automated deposition into hydrogel substrates
and evaluated the cytocompatibility of the process with diﬀer-
ent aggregate types. The platform can be used in a variety of ar-
eas within the 3D in vitro ﬁeld, from basic research, tissue engi-
neering, drug discovery and screening, to personalized therapy
in clinical settings.

2. Results and Discussion

2.1. Pick-Flow-Drop principle for Handling of Cell Aggregates

The Pick-Flow-Drop principle for selective handling of cell aggre-
gates is shown in Figure 1a. The procedure is integrated in our in-
house developed prototype of a spheroid and organoid process-
ing platform to enable a fully automated process (Figure 1b). One
end of a disposable polyimide capillary, with an inner diameter of
250 μm and a length of 110 mm, is immersed in a reservoir, e.g.,
a 35 mm Petri dish, containing the sample in culture medium
(aspirating end). The other end of the capillary (dispensing end)
is clamped into a Drop-on-Demand dispenser (PipeJet, P9 dis-
penser, BioFluidix GmbH, Germany).

The piezoelectric dispenser squeezes the capillary tube by ad-
justable parameters in the range of 10 to 25 μm at a frequency of
5 to12 Hz, resulting in the ejection of droplets ranging from 8 to
22 nL. According to the so-called PipeJet principle the continu-

ous droplet ejection leads to an associated capillary reﬁlling due
to capillary forces.[15] Therefore, each droplet ejection generates
a suction pulse at the aspirating end, which can be used to aspi-
rate targeted 3D cell aggregates from the reservoir into the cap-
illary. Prior to droplet ejection associated with aspiration in the
reservoir, the cell aggregates in the reservoir are allowed to sedi-
ment to the bottom of the reservoir, where they can be monitored
by a camera system (Figure 1c). Object detection in the reservoir
is performed using a threshold-based image segmentation algo-
rithm. The capillary opening in the reservoir near the bottom of
the Petri dish is detected as a dark circle of known size in the
image. All other detected objects are potential aspiration candi-
dates. Their position, area, circularity and distance to the nearest
neighbor are measured. When a cell aggregate is selected for aspi-
ration based on matching preset characteristics such as size and
shape, the xy-stage on which the reservoir is mounted moves the
selected aggregate below the opening of the aspirating capillary
end. The capillary is lowered onto the object to close proximity
to the bottom of the reservoir and remains there for the dura-
tion of one droplet ejection, ≈130 ms, so that the object is sucked
into the capillary (Figure 1d). Then, the capillary is raised again
and the reservoir stage moves the next object under the aspirat-
ing capillary end. The lowering and raising of the capillary to as-
pirate an object is hereafter referred to as the aspiration motion.
Throughout the entire process, including the lowering and lifting
of the capillary, there is constant droplet ejection at the dispens-
ing end so that aspirated cell aggregates are eﬃciently transferred
through the capillary with each pressure pulse. A single spheroid
or organoid travels through the capillary to the dispensing end in
≈1 min. Typically, several aggregates are aspirated one after an-
other and are transported simultaneously in a train-like manner
with the unidirectional ﬂow through the capillary. Whenever an
aggregate reaches the dispensing end, it is individually dispensed
in a nanoliter droplet. Therefore, a second camera system de-
tects and tracks aggregates in the nozzle region of the dispensing
end (Figure 1e).[10,11] Most ejected droplets will not contain any
aggregate and will be directed to a waste compartment. Droplets
that are predicted by the software to contain an aggregate are de-
posited at a speciﬁc target position by moving the target plate
below the capillary oriﬁce with a second motorized xy-stage.

The droplet impact position on the target substrate varies
only within a radius of 55 μm around the target, as previously
reported.[10] As a result, a predeﬁned number of spheroids and
organoids can be plated in individual wells of all standard mi-
croplate formats and even in wells of 1,536 microwell high-
throughput screening plates as shown exemplarily in Figure S1
(Supporting Information) for a MCF7 tumor cell line spheroid.
Since cell aggregates are delivered in nanoliter droplets, dilu-
tion of the target volume is minimized. The target substrate is
mounted on a heat-dissipating cold plate connected to a recircu-
lating chiller so that the target substrate can be cooled as needed.
All components in contact with the sample, namely the reservoir
(Petri dish), the capillary and the target plate (microwell plate),
are disposable and can be easily replaced after each run. In addi-
tion, the platform itself could ﬁt under a sterile bench.

Typically, organoids and spheroids are harvested and resus-
pended in cell culture medium prior to being processed with
the platform. However, the spheroid and organoid processing
platform can also aspirate single cell aggregates directly from

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (2 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

Figure 1. Pick-Flow-Drop method for controlled handling of 3D cell aggregates. a) Schematic representation of the Pick-Flow-Drop principle: The sample
reservoir containing 3D cell aggregates in suspension is monitored by a camera. A motorized xy-stage moves the reservoir to place detected aggregates
for aspiration underneath the aspirating end of the capillary. Aspirated aggregates are transported in a train of previously aspirated aggregates through
the capillary to the droplet dispenser at the dispensing capillary end. Once an aggregate is detected by a second camera system at the dispensing
nozzle, it can be deposited at a speciﬁc target position with a second motorized xy-stage. b) Photo of the Pick-Flow-Drop module implemented into the
in-house developed prototype of a spheroid and organoid processing platform. c) Exemplary image taken with the reservoir monitoring camera of MCF7
spheroids at the bottom of the reservoir. The dark spot in the center shows the aspirating capillary end. On the right side: Magniﬁcation of the aspirating
capillary end right before and right after aspiration of a spheroid. Scale bars: 250 μm. d) Side view of the aspirating capillary end showing the lowering
and raising of the capillary in the reservoir to aspirate a polymer microsphere. Scale bar: 200 μm. e) Images of the dispensing capillary end showing a
MCF7 spheroid approaching the oriﬁce of the capillary. The blue region marks the volume that will be ejected with the next droplet. Once a spheroid is
detected within this volume, the target plate is moved to deliver the spheroid to the desired location. Scale bar: 200 μm.

polymerized hydrogels, such as from hydrogel domes in a 24-
well plate, and deliver them to a desired target location, as shown
in Figure S2 (Supporting Information). To minimize the shear
forces on the cell aggregates, the following work was performed
with spheroids or organoids in liquid suspension, e.g., standard
cell culture media or PBS, if not denoted otherwise. In addition,
also capillaries with a larger inner diameter, e.g. 500 μm, can be
used, to process larger cell aggregates.

2.2. Enabling Targeted Aspiration of Cell Aggregates

to Drop-on-Demand approaches,

In contrast
the Pick-Flow-
Drop principle oﬀers the advantage of processing only speciﬁc
spheroids or organoids. It allows for precise aspiration of tar-
geted spheroids or organoids while leaving all unwanted sample
components in the reservoir. This means that only the target ob-
ject should be aspirated during the aspiration movement of the

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (3 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

Figure 2. Investigation of the aspiration height and aspiration radius to enable robust selective aspiration. a) Simulated ﬂow velocity ﬁeld in the capillary
and near the capillary opening in the reservoir. The ﬂow ﬁeld was simulated with an average ﬂow rate of 96 nL s−1 and a capillary height of 150 μm
above the reservoir bottom. b) Critical aspiration height from which spheroids in the order of 60–180 μm are aspirated into the capillary within 2 s.
c) Microscopic images showing the eﬀect of the aspirating capillary end 100 μm above the reservoir bottom on nearby MCF7 spheroids. Scale bar:
200 μm. d) Generated time-dependent aspiration radius for diﬀerent stationary heights ha of the capillary opening above the reservoir bottom. Each dot
marks the time point when a MCF7 spheroid with a certain initial distance from the center of the capillary opening was drawn into the lumen of the
capillary. During the measurements, droplets of a volume of 12 nL were continuously ejected with a frequency of 8 Hz at the dispensing capillary end.
e) Aspiration radius generated by a total aspiration motion. Each bar shows the calculated size of the aspiration radius that would be generated due to
diﬀerent minimum capillary aspiration heights hmin approached during the aspiration motion. The upper x-axis shows the dwell time td,a of the capillary
opening within the aspiration regime calculated with Equation (2) for the approached minimum capillary height.

capillary. However, the aspiration ﬂow in the reservoir aﬀects not
only objects directly below the aspirating capillary end, but also
nearby objects, as shown schematically by the simulated ﬂow ve-
locity proﬁle in Figure 2a. Two criteria must be met during the
aspiration process to allow targeted aspiration of a single aggre-
gate:

First, when the reservoir stage is moving or when cell aggre-
gate aspiration is not desired, the capillary opening must be suf-
ﬁciently far from the reservoir bottom to prevent unintentional
aspiration of sedimented objects. However, the opening must re-

main submerged in the liquid to avoid air bubble aspiration. The
maximum height of the capillary above the bottom, where a suf-
ﬁcient aspiration force is present is termed critical height hcrit. If
the capillary is below hcrit, it is within the aspiration regime for
sedimented aggregates.

To determine hcrit, the capillary opening was slowly lowered
over a MCF7 spheroid from a height of 1 mm above the bottom.
Within a spheroid diameter range of 55 μm to 180 μm, there was
no dependency between hcrit and the spheroid size. The average
critical height was found to be hcrit = (280 ± 42) μm (Figure 2b).

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (4 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

Given the potential presence of objects larger than 280 μm in
more heterogeneous samples, for all subsequent experiments
the capillary is raised 500 μm above the bottom of the reservoir
to avoid accidental aggregate aspiration during stage movement
and is only lowered when intending to aspirate an aggregate.

The second criterion that must be met is to ensure that only
the target object is aspirated, respectively the unintentional aspi-
ration of objects near the target must be avoided. The area from
which objects are aspirated after a given period of aspiration time
is deﬁned by the aspiration radius Ra. We ﬁrst measured Ra with
a stationary aspirating capillary opening in the x, y, and z direc-
tions in the reservoir, so that no aspiration motion was performed
(Figure 2c,d). In this way, we were able to study the inﬂuence of
diﬀerent aspiration heights ha of the capillary opening above the
bottom on the aspiration radius. Due to the increased ﬂow ve-
locities around the capillary opening at small ha, the aspiration
radius increases more rapidly. We did not observe a spheroid size-
dependent eﬀect on the aspiration radius within the considered
spheroid diameter range of 30 to 140 μm (Figure S3, Supporting
Information).

The data presented in Figure 2d has a logarithmic trend and
the following curve was ﬁtted n times to n − 1 data points of each
ha condition

Ra (t) = A ⋅ ln (B ⋅ t − C) + D

(1)

The parameters A, B, C and D vary with the set stationary as-

piration height ha of the capillary.

Next, we approximated the aspiration radius generated during
the automated aspiration motion. As mentioned above, the as-
piration motion consists of lowering the capillary from outside
of the aspiration regime to a preset minimum aspiration height
hmin, waiting at hmin for exactly one droplet ejection to aspirate the
object, and raising the capillary again. Droplets are continuously
ejected during the lowering and lifting. For each set minimum
aspiration height hmin to which the capillary is lowered, we calcu-
lated the total dwell time td,a of the capillary opening within the
aspiration regime, which increases as hmin decreases

)

(
hmin

=

td,a

(hcrit − hmin) ⋅ (vd + vu)
⋅ vu

vd

+

1
fd

(2)

whereas vd = 1 mm s−1 and vu = 2 mm s−1 are the velocities
at which the capillary is lowered and raised again, respectively,
and fd = 8 Hz is the droplet dispensing frequency. Shortening
the dwell time by increasing the speed of the capillary move-
ment is only possible to a limited extent since diving down too
quickly would possibly displace the target objects. With the cal-
culated dwell times td,a and the ﬁt parameters found for the data
in Figure 2e with Equation (1), we estimated the aspiration radius
Ra(td,a(hmin)) generated by a complete aspiration motion. The in-
creased capillary opening dwell time in the aspiration regime due
to decreased hmin during an aspiration motion prolongs the time
in which cell aggregate aspiration occurs. This results in larger
aspiration radii as shown in Figure 2e.

In contrast, for large minimum aspiration heights hmin, the as-
piration radius generated during the aspiration motion would be
zero. This means that a single pressure pulse would not be suﬃ-
cient to successfully aspirate a targeted aggregate. In general, we

found a minimum aspiration height hmin of 150 μm of the capil-
lary during the aspiration motion to be a good compromise. It al-
lows robust cell aggregate aspiration with a single pressure pulse,
short dwell times in the aspiration regime and a suﬃciently small
aspiration radius of (226.1 ± 2.5) 𝜇m. In all subsequent experi-
ments, the preset minimum aspiration height was 150 μm, re-
quiring spheroids or organoids to be at least 226.1 μm apart to
ensure targeted aspiration without accidental intake of neighbor-
ing aggregates. To accommodate potential aspiration radius devi-
ations from uneven reservoir mounting or capillary stage errors,
only objects with a minimum safety distance of 270 μm from
their closest neighbors are chosen for targeted aspiration. This
is illustrated in Figure S4 (Supporting Information) and referred
to as safety clearance condition (SCC) for targeted object aspira-
tion. This is the basis for eﬃcient and reliable selective organoid
or spheroid handling and a high process quality.

To avoid that the sample recovery during targeted aspiration
depends on the sample density in the reservoir, the platform fea-
tures an implemented mixing function. Once all detected ob-
jects satisfying the SCC have been aspirated, droplet ejection is
paused and the reservoir is vigorously moved in a cross-like re-
ciprocal pattern in the x and y direction to randomly redistribute
the remaining objects. Then, another round of targeted aspira-
tion is performed (for more details, see Supplementary Text and
Figure S5, Supporting Information). This allows aspirating all
cell aggregates in a targeted and controlled manner over time un-
til the entire reservoir is completely depleted from aggregates.

2.3. Aspiration Rate and Single Aggregate Aspiration Eﬃciency

To evaluate aspiration rate and eﬃciency, the targeted aspiration
process with the SCC described above was investigated for vari-
ous spheroid densities in the reservoir. The aspiration rate was
determined as the total number of aspiration motions of the cap-
illary per minute. Single aggregate aspiration eﬃciency was cal-
culated as the ratio of aspiration motions resulting in a single
spheroid aspiration to the total number of aspiration motions.
We ﬁrst investigated the eﬀect of the aggregate density on the
aspiration rate and eﬃciency. We measured aspiration rate and
single spheroid aspiration eﬃciency for MCF7 spheroid densi-
ties in the range of 0.5 spheroids mm−2 to 10.4 spheroids mm−2,
corresponding to 500 to 10,000 spheroids in a 35 mm Petri dish.
At spheroid densities ≥2.1 spheroids mm−2, the platform per-
formed (21.8 ± 0.9) aspiration motions per minute with a single
spheroid aspiration eﬃciency of (98.4 ± 3.1)%. This results in
an average spheroid aspiration rate of (21.5 ± 1.5) spheroids per
minute. For spheroid densities ≥2.1 spheroids mm−2, we did not
observe any signiﬁcant eﬀects on the aspiration rate or aspiration
eﬃciency depending on the number of spheroids in the reservoir
(see also Table S1 in the Supporting Information).

At a low spheroid density of 0.5 spheroids mm−2 in the reser-
voir, which corresponds to 500 spheroids in a 35 mm Petri dish,
we observed a slight decrease in the aspiration rate to (18.3 ±
1.2) aspiration movements per minute. This is due to the larger
distances between the spheroids in the reservoir and thus longer
travel times of the reservoir stage. In addition, single spheroid as-
piration eﬃciency and spheroid aspiration rate decreased to (96.5
± 2.5)% and (17.7 ± 0.9) spheroids per minute, respectively. The

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (5 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

Table 1. Aspiration rate, aggregate aspiration rate and aspiration eﬃciency
for diﬀerent sample types. The aspiration rate describes the number of
aspiration motions per minute, the aggregate aspiration rate describes the
number of single aggregate aspiration events per minute. For each sample
type, aspiration rate and eﬃciency were measured three times over the
course of at least one minute. Cell aggregate density in the reservoir was
in all cases between 0.5 spheroids mm−2 and 2.1 spheroids mm−2.

Table 2. Detection accuracy and plating eﬃciency with PFD for MCF7
spheroids (diameter range 80–180 μm), A549 spheroids (diameter range
100–180 μm) and CRC organoids (diameter range 50–100 μm). Detection
accuracy describes the ratio of aggregates passing the capillary detected
by the software algorithm to aggregates as observed by a researcher (N
≥ 3, n ≥ 384 for each sample type). Plating eﬃciency describes the ratio
of aggregates passing the capillary to aggregates deposited in individual
wells of a 384 MWP (N ≥ 3, n ≥ 96 for each sample type).

Sample type

Aspiration
rate [min−1]

Aggregate aspiration
rate [min−1]

Aspiration
eﬃciency [%]

Sample type

MCF7 spheroids

A549 spheroids

CRC organoids

19.8 ± 1.9

19.7 ± 0.3

20.2 ± 0.2

19.2 ± 1.9

19.4 ± 0.7

19.9 ± 0.4

96.6 ± 2.4

98.4 ± 2.2

98.5 ± 2.1

slightly lower aspiration eﬃciency was due to false positive detec-
tion in all cases. As described above, the image segmentation for
object detection in the reservoir used in this study was threshold
based. Therefore, sparsely populated reservoirs were more likely
to produce false positives due to misinterpretation of shadows or
dirt.

Next, we measured the aspiration rate and single aggregate as-
piration eﬃciency for diﬀerent spheroid sample types, namely
MCF7 spheroids and A549 spheroids. In addition, we tested au-
tomated aspiration with heterogeneous murine colorectal can-
cer (CRC) organoids, the characteristics of which have been de-
scribed in detail in the literature.[16] For all sample types, the den-
sity of cell aggregates in the reservoir ranged from 0.5 spheroids
mm−2 to 2.1 spheroids mm−2, corresponding to 500 to 2000 cell
aggregates in a 35 mm Petri dish. In general, high aggregate aspi-
ration eﬃciencies of over 95% were achieved with an aspiration
rate of 19.4 aggregates per minute, which was independent of the
sample type (see Table 1). We did not observe multiple aggregates
aspirated within a single aspiration motion, demonstrating an ap-
propriately deﬁned SCC for targeted single aggregate aspiration.
Overall, the aspiration process proved to be highly eﬃcient, in-
dependent of the sample type and largely independent of sample
density in the reservoir.

2.4. Accurate Control of the Number of Deposited Aggregates Via
Single Aggregate Dispensing

Next, we examined the deposition characteristics of the spheroid
and organoid processing platform. As mentioned above, a sec-
ond camera system observing the dispensing end of the capil-
lary is used to count the number of spheroids or organoids that
pass through and are dispensed (Figure 1a,e). As in the reser-
voir, detection of objects in the nozzle region is threshold based.
We veriﬁed the reliability of the automatic object detection for
three diﬀerent sample types (MCF7 spheroids, A549 spheroids,
and CRC organoids) by comparing the detection of passing ag-
gregates with aggregates observed by an experienced researcher
by reviewing the recorded image series. We also evaluated the
plating eﬃciency for the three diﬀerent sample types by com-
paring the number of aggregates passing through the capillary
with the number of aggregates successfully plated in individual
wells of a 384 MWP. Table 2 summarizes the results. In general,
detection errors can occur when two aggregates overlap and are
not detected as two individuals, or when the aggregate is very

Detection accuracy
[%]

Plating eﬃciency
[%]

MCF7 spheroids

A549 spheroids

CRC organoids

100 ± 0

97.6 ± 2.5

97.4 ± 2.6

99.8 ± 0.8

97.7 ± 1.7

98.8 ± 0.9

translucent and therefore produces weak signals in the threshold
image. In addition, gas bubbles in the capillary can cause false de-
tection or even dispensing failure. However, the dispensing pa-
rameters and the arrangement of the capillary inlet and outlet
are optimized so that no gas bubbles were observed during dis-
pensing. Unsuccessful aggregate deposition can occur if the dis-
pensed droplets are deﬂected during droplet ejection, for exam-
ple, due to electrostatic eﬀects or unfavorable aggregate position
within the drop during detachment from the nozzle. Overall, a
very high detection accuracy and plating eﬃciency of over 95%
is achieved, regardless of the sample type. This demonstrates a
high reliability of the controlled deposition of cell aggregates.

In addition to good detection accuracy and plating eﬃciency,
we investigated single aggregate dispensing eﬃciency. Single ag-
gregate dispensing occurs when only one aggregate is encapsu-
lated in an ejected droplet. Single aggregate dispensing provides
maximum control over the number of aggregates plated, while
still plating each passing cell aggregate for highly eﬃcient sam-
ple handling. Although only one aggregate is aspirated at a time,
aggregates of diﬀerent sizes and shape travel through the capil-
lary at diﬀerent velocities. If the time between two successive as-
pirations is too short, multiple spheroids or organoids may reach
the ejection area of the dispenser at the same time and cannot be
individually plated on a target position (Figure 3a).

Single aggregate dispensing eﬃciency is deﬁned as the ratio of
single aggregate dispensing events (exactly one aggregate within
the ejection area in the dispensing capillary end) to total aggre-
gate dispensing events (at least one aggregate within the ejection
area in the dispensing capillary end).

We determined the single aggregate dispensing eﬃciency for
diﬀerent aggregate dispensing rates. These were achieved by
adding pauses before initiating the aspiration movements, thus
slowing the aspiration rate and increasing the distance between
two cell aggregates within the capillary. Single aggregate dis-
pensing eﬃciencies for diﬀerent sample types and dispensing
rates are shown in Figure 3b. The lower the aggregate through-
put, the higher the success rate of dispensing a maximum of
one aggregate in a droplet. The greater the size and shape het-
erogeneity of a sample, the more the throughput must be re-
duced to achieve 100% single aggregate dispensing eﬃciency.
For MCF7 spheroids, which are very uniform in size and shape,
a single aggregate dispensing eﬃciency of 100% was achieved
at spheroid dispensing rates of ≤16 spheroids per minute. A549
spheroids are uniform in size, but varied in shape in the form of

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (6 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

Figure 3. Single aggregate dispensing eﬃciency. a) Diﬀerent types of ejected droplets: “void” dispensing (droplet without cell aggregate), single aggre-
gate dispensing and multi aggregate dispensing. Single aggregate dispensing occurs when only one cell aggregate passes through the blue area in the
dispensing capillary end corresponding to the next ejected droplet. Multiaggregate ejection occurs when more than one cell aggregate is present in the
area marked in blue. Scale bar: 200 μm. b) Single aggregate dispensing eﬃciencies for diﬀerent sample types and varying throughputs. Dispensing rates
greater than 21 aggregates per minute correspond to the nontargeted aspiration mode (N = 3, n ≥ 96).

various protrusions or buds. Here, a consistent single spheroid
dispensing eﬃciency of 100% was achieved at dispensing rates
≤10 spheroids per minute. For the highly heterogeneous CRC
organoid sample, a high single organoid dispensing eﬃciency
of (98.4 ± 1.1)% was observed at a throughput of less than 9
organoids per minute.

However, even at high throughput rates of 21 aggregates per
minute, the Pick-Flow-Drop principle achieves on average very
high single aggregate dispensing eﬃciencies of ≥94%, indepen-
dent of the sample type. In addition, the highest sample through-
put can be achieved with a nontargeted aspiration mode. In this
mode, the SCC is ignored and no aspiration motion is performed,
so that the capillary remains at minimum aspiration height at all
times. This resulted in a spheroid dispensing rate of 30 spheroids
per minute, for which we still measured a single spheroid dis-
pensing eﬃciency of over 90%.

We can therefore conclude that the Pick-Flow-Drop approach
is well suited for controlled cell aggregate handling and dispens-
ing, oﬀers various modes of operation and provides a high degree
of tracking, documentation and control of the number of cell ag-
gregates delivered to a desired target location. Depending on the
requirements of a speciﬁc application in terms of throughput or
accuracy of the number of aggregates plated, diﬀerent parame-
ters can be easily selected without changing the handling method
or protocol.

2.5. Cytocompatibility of PFD Process

To investigate whether the described Pick-Flow-Drop process has
detrimental eﬀects on 3D cell aggregates, we performed viabil-
ity, apoptosis and necrosis assays on four diﬀerent sample types,
namely MCF7 spheroids, A549 spheroids, LNCaP spheroids and
CRC organoids. LNCaP spheroids were selected as a sensitive
sample because they had already grown for more than 14 days
and had reached their proliferation limit with diameters of 180–
260 μm at the time of PFD processing.

We placed the sample suspended in complete spheroid or
organoid culture medium in the reservoir and processed it with
the platform prototype, including multiple random redistribu-

tions in the reservoir via the mixing function, targeted aspiration,
transport through the capillary, and delivery to a microwell plate.
The wells of the microwell plate were preloaded with basement
membrane extract (BME) matrix. Throughout the process, the
MWP was maintained at 4 °C using the platform’s cooling mod-
ule to allow for complete immersion of spheroids or organoids
when dispensing into the hydrogel.

For comparison, we also prepared cell aggregates via manual
pipetting (MP) by resuspending them in the BME hydrogel be-
fore plating them into wells, as is commonly done for organoid
seeding, propagation and screening. We ensured that the aggre-
gate concentration in each well was comparable to the number of
aggregates deposited with the platform. After plating, the MWPs
were transferred to the incubator. After 30 min, complete culture
medium was added to the wells. Immediately after plating, diﬀer-
ences were evident as wells ﬁlled by manual pipetting contained
loose cells and cell debris. In contrast, wells ﬁlled by PFD con-
tained visibly less cell debris and loose cells, as droplets without
cell aggregates are placed in waste wells (Figure 4a,b).

Four hours after plating, viability was assessed by the quan-
tiﬁcation of present ATP. Compared to cell aggregates seeded by
manual pipetting, we did not observe a signiﬁcant immediate ef-
fect on the viability of cell aggregates after automated handling
with the platform, regardless of sample type (Figure 4c). Apop-
tosis and necrosis were assessed 24 h after plating (Figure 4d,e).
Apoptosis was measured by detecting the luminescence signal as-
sociated with Annexin V binding to phosphatidylserine exposed
on the cell surface. Necrosis was detected as a ﬂuorescence sig-
nal corresponding to loss of membrane integrity. In general, cell
aggregates processed by PFD tended to result in weaker signals
associated with apoptosis or necrosis compared to samples sub-
jected to manual resuspension in hydrogel. We believe that this
is partly due to the presence of cell debris and loose cells in
the manually plated test wells (Figure 4a,b). These loose cells
are most likely undergoing apoptosis or necrosis and may con-
tribute to a higher signal. In addition, during pipetting and re-
suspension in the hydrogel, cell aggregates are exposed to very
high shear stress for a short time, which signiﬁcantly exceeds the
shear stress present during PFD (see Supporting Information).
Increased ﬂuid shear stress is known to induce apoptosis.[17] In

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (7 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

Figure 4. Cytocompatibility of PFD. a) Exemplary image of MCF7 spheroids embedded in basement membrane extract (BME) with PFD and by manual
pipetting one hour after plating. Scale bar: 200 μm. b) Exemplary image of CRC organoids embedded in BME with PFD and by manual pipetting one
hour after plating. Scale bar: 200 μm. c) Cell viability 4 h after plating either via PFD or via manual pipetting (MP). Three technical replicates, n ≥ 60 for
each sample type and each condition. d) Measured luminescence signal due to Annexin V binding to exposed phosphatidylserine on the cell surface as
an indicator of apoptosis 24 h post plating. Three technical replicates, n ≥ 60 for each sample type and each condition. e) Measured loss of membrane
integrity as indicator of secondary necrosis 24 h post plating. Three technical replicates, n≥60 for each sample type and each condition. f) Normalized
area of unprocessed cell aggregates and aggregates that were processed with the spheroid and organoid processing platform. Each condition shows data
of n ≥ 60. Aggregates with diameters larger than 240 μm were not considered for aspiration and are therefore excluded from the data set. g) Exemplary
proliferation of an MCF7 spheroid that was automatically embedded in BME over the course of several days. Day 1 was the day of embedding. Scale
bar: 100 μm. h) Fold change in diameter of MCF7 spheroids after they were embedded in basal membrane extract with the platform. n = 34. Spheroids
were automatically delivered into the hydrogel on day 1. Data was tested for normal distribution and the two-tailed t-test was performed. P-values ≥ 0.05
were considered nonsigniﬁcant (n.s.).

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (8 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

addition, the high shear stress may cause fragmentation of large
aggregates, potentially exposing a necrotic core, which we hy-
pothesize to be the reason for the increased necrotic signal mea-
sured for LNCaP spheroids subjected to manual pipetting.

We also measured the sizes as 2D areas of unprocessed cell
aggregates in the reservoir and compared them to those of pro-
cessed aggregates (Figure 4f). Again, we did not observe any
signiﬁcant eﬀects or fragmentation of cell aggregates and con-
clude that there are no measurable eﬀects on aggregate integrity.
We also investigated whether a change in medium could have
a negative eﬀect on cytocompatibility, as serum components of
complete culture media provide protection against shear stress.
Therefore, we checked integrity, viability, apoptosis and necrosis
for MCF7 spheroids and LNCaP spheroids that were kept in PBS
instead of complete culture medium during processing with the
platform. The results are shown in Figure S6 (Supporting Infor-
mation). In general, cytocompatibility does not seem to be neg-
atively aﬀected compared to manually pipetted cell aggregates.
In addition, we have included in Figure S6 (Supporting Informa-
tion) the results of the measured H2O2 level as an indicator of
ROS generation of MCF7 spheroids two hours after plating with
the platform. We saw no signiﬁcant diﬀerence in H2O2 levels be-
tween spheroids handled with the platform and those handled
by pipetting alone. To assess whether there are any long-term
negative eﬀects on proliferation, we observed MCF7 spheroids
embedded with the platform in BME for several days. We found
overall good proliferation and growth (Figure 4g,h). The growth
rate was in the same range as reported in the literature.[18]

Taken together, we conclude that for all sample types tested,
there were no measurable negative eﬀects on cytocompatibility as
a result of processing with the platform. Instead, cell debris and
loose cells in test wells were visibly avoided through controlled
deposition, potentially leading to reduced apoptosis and necrosis
signals. This can be beneﬁcial for standardized, highly controlled
assessment of drug response by reducing unwanted background
noise from nonviable aggregate fragments.

2.6. Size-Selective Handling of Heterogeneous 3D Cell Aggregate
Samples

The controlled aspiration motion in combination with the SCC
allows for targeted aspiration of cell aggregates and enables auto-
mated selective handling. By monitoring the reservoir, it is possi-
ble to detect characteristics such as size and shape of cell aggre-
gates and select only those cell aggregates that meet pre-set pa-
rameters for targeted aspiration. This is particularly important in
heterogeneous samples where many diﬀerent sizes and shapes
of cell aggregates are present and only a speciﬁc fraction is el-
igible, for example, for drug screening, culture propagation or
other downstream analyses. Therefore, we tested automated size-
selective handling of the heterogeneous murine CRC organoid
sample using the spheroid and organoid processing platform.
Organoids were cultured in domes of BME matrix and exhibited
diﬀerent sizes and shapes just before harvesting (Figure 5a). A
pre-scan of the harvested sample in the platform reservoir also
showed this wide size distribution (Figure 5b). We set diﬀerent
size limits for selective organoid aspiration in three consecutive
runs. Within a size fraction run, all aspirated organoids were to

be plated into a single well of a 96-well plate. The sizes of the de-
livered organoids in these wells were then analyzed (Figure 5c–f).
We found that the delivered organoids conformed well to the pre-
set size limits and that cellular debris in the target wells was vis-
ibly minimized compared to the source reservoir. User-deﬁned
size limits should be considered as soft limits, since organoids
and spheroids may appear to be of diﬀerent sizes in 2D images
from diﬀerent perspectives. Outliers may occur due to the thresh-
old based aggregate detection and a misinterpretation of the size
depending on the set exposure levels or image distortions such
as shadows. The eﬀects of such distortions will be reduced by
applying deep learning-based image segmentation algorithms in
the future.

The platform is capable of accurately and exclusively recover-
ing even minor present size-speciﬁc subfractions with high eﬃ-
ciency > 90% from the reservoir (Figure S7, Supporting Informa-
tion). All aspirated cell aggregates were delivered to the target well
without any loss. Further, we did not observe a size-dependent
eﬀect on the detection accuracy in the nozzle or the plating eﬃ-
ciency. We conclude that the platform is able to provide reliable
delivery of diﬀerent size fractions of heterogeneous samples with
high sample recovery. With the PFD process, eﬃcient and spe-
ciﬁc handling does not require a minimum number of cell ag-
gregates present in a sample to be processed. In contrast, we can
even ﬁlter out minor present fractions of the sample with a very
high recovery. Thus, we provide a generic handling method for
many diﬀerent samples as well as downstream workﬂows and
protocols.

3. Conclusion

We have developed a generically applicable selective handling
platform for 3D cell aggregates based on the Pick-Flow-Drop prin-
ciple. Cell aggregates such as spheroids or organoids are selec-
tively aspirated from a reservoir, transported by a microﬂuidic
ﬂow through a thin capillary and deposited at a target position
within a nanoliter droplet. We evaluated the characteristics of
the microﬂuidic aspiration that allowed us to establish a gener-
alized, highly controlled and targeted particle aspiration. No fur-
ther tweaks or adjustments were required to maintain a highly ef-
ﬁcient and reliable process as sample concentration, sample ho-
mogeneity, aggregate sizes, desired throughput, sample type and
culture conditions varied. We demonstrated the capabilities of the
system by testing the fully automated deposition of spheroids and
organoids in an extracellular matrix mimicking hydrogel. Based
on the embedded cell aggregates, we then evaluated the cytocom-
patibility of the PFD process using cell viability, apoptosis, necro-
sis, and H2O2 assays. No detrimental eﬀects of the process were
observed in all assays for diﬀerent aggregate types, and there
is even evidence of an advantage over manual pipetting. Shear
stress is reduced compared to manual pipetting, and cell debris
in test wells was visibly minimized, which can be beneﬁcial for
clear drug response assessment. The PFD process appears to be
a genuinely gentle method for handling various cell aggregates
such as spheroids and organoids.

Further, we showed the robust handling of highly heteroge-
neous organoid samples and the accurate extraction of only size-
speciﬁc subfractions of a sample. Until now, this has typically
involved manual ﬁltering steps, resulting in sample loss and

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (9 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

Figure 5. Size-selective aspiration and delivery of CRC organoids. a) CRC organoids in basal membrane extract dome before harvesting. Scale bar:
1000 μm. b) Initial size distribution of the organoids in the reservoir before selective aspiration started. c) Size distribution of the delivered organoids.
For selective aspiration, three diﬀerent size limits (indicated by the gray dashed boxes) were deﬁned within which the size of the aspirated organoids
should fall. All organoids aspirated within a size-speciﬁc aspiration run were delivered into the well of a 96-well plate. The box shows the size distribution
of the delivered organoids for each size limit. d–f) Microscopic stitched images of the organoids delivered to the individual wells within the three
size-speciﬁc aspiration runs. Scale bar: 1000 μm, inlet scale bar: 200 μm.

time-intensive procedures. The automated selective aspiration is
a very useful tool, as it allows to tackle the cellular heterogene-
ity of organoids with increased hands-oﬀ time. Applications in-
clude the separation of tumor cell organoids from nontumor cell
organoids, which is typically accomplished by costly and time-
consuming growth factor deprivation.[19] Detecting ﬂuorescence-
based markers can be easily implemented in the future. No-
tably, the mixing function of the reservoir allows targeted aspi-
ration of the entire sample, resulting in high sample recovery ef-
ﬁciencies even when only size-speciﬁc subfractions of a sample
are extracted. This demonstrates the suitability of the spheroid
and organoid processing platform for automated and generic
handling of impure samples or samples containing only small
numbers of tissue fragments or organoids as found in clinical
settings.[20]

The spheroid and organoid processing platform addresses cur-
rent shortcomings in 3D cell culture research that arise from
the complexity of establishing and expanding organoid cul-

tures, achieving suﬃcient reproducibility, and minimizing time
and resource consumption.[21–23] As remarkable studies have
already shown, patient derived organoids can be used to pre-
dict the response to various cancer therapeutics in the treat-
ment of patients.[21,22,24] However, the high heterogeneity of
samples, as well as the variety of sample-speciﬁc requirements
for handling, cultivation, or downstream drug eﬃcacy assess-
ment, has limited the high-throughput exploitation of 3D in
vitro studies and the understanding of underlying biological
mechanisms. Our platform helps take advantage of the hetero-
geneity in organoid samples that reﬂects the complex carcino-
genesis. The platform reduces the manual workload while in-
creasing the analytical assessment options through the detec-
tion of multiple sorting markers and selective organoid han-
dling. This simpliﬁes and standardizes the functional analy-
sis of organoid models in order to make reliable statements
about the precision of therapy in personalized oncology. Due to
their self-assembly and self-organization capabilities, it is also

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (10 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

Figure 6. Detailed scheme of the spheroid and organoid processing platform prototype. 1. xy-stage for reservoir, 2. reservoir (Petri dish), 3. reservoir
illumination light, 4. mirror to guide reservoir image light to reservoir camera, 5. reservoir camera, 6. capillary holder attached to capillary z-stage, 7.
aspiration capillary, 8. capillary z-stage, 9. PipeJet, 10. manual ﬁne-alignment xyz-stage for PipeJet, 11. dispenser illumination light, 12. dispenser camera,
13. microwell plate on substrate cooling block, 14. xy-stage for microwell plate, 15. connection for recirculating chiller.

feasible to use the platform for precise positioning of spheroids
or organoids as building blocks for tissue engineering and 3D
bioprinting. Deposition of spheroids of diﬀerent cell types could
enable easy cocultivation and realization of spatial heterogene-
ity of the printed tissue in order to mimic in vivo tissue more
closely. The Pick-Flow-Drop principle is compatible with a wide
variety of samples and culture conditions, as well as down-
stream workﬂows such as drug screening, sample propagation,
or speciﬁc research questions involving size, sample number,
type, or morphology-dependent eﬀects. We see its great poten-
tial for personalized medicine in the clinical setting, for accel-
erating drug discovery and screening in the preclinical setting,
and for contributing to a fundamental understanding of disease
pathways.

4. Experimental Section

Platform Design and Components: Custom parts of the spheroid and
organoid processing platform were 3D printed in PETG on a Prusa MK3S
(Prusa Research, Czech Republic). The capillary for aspiration and droplet
delivery was a thin polyimide tube with an inner diameter of 250 μm and a
length of 11 cm (Zeus Industrial Products, USA). The capillary holder for
inserting the capillary into the reservoir was a 4 mm thick laser-cut PMMA
plate.

Multiple motorized stages were used to provide automated movement
of speciﬁc parts. The reservoir was moved with two linear stages with a
travel range of 50 mm and 100 mm, respectively (Zaber Technologies,
Canada). The target substrate was moved with a motorized aperture xy-
stage with a travel range of 100 mm × 120 mm (Zaber Technologies,
Canada). The movement of the capillary was controlled by a translation
stage with a range of 30 mm, the adjustment of the focal plane of the
reservoir camera by a stage with a range of 50 mm (both from Standa
LTD, Lithuania).

A 12MP CMOS camera (Imaging Development Systems, Germany)
with a 6.5× zoom lens system (Thorlabs, Inc., USA) was used to monitor
the sample in the reservoir. A 5MP CMOS camera (Imaging Development

Systems, Germany) with a second 6.5× zoom lens system was integrated
into the setup to image the nozzle at the dispensing end of the capillary
as well as ejected droplets.

A membrane pump and a pneumatic cylinder enabled automated pre-

ﬁlling of the capillary with liquid from the reservoir.

Droplet generation was performed using a noncontact dispenser
(PipeJet P9, Bioﬂuidix, Germany). The capillary was clamped to the dis-
penser and the piezo stack actuator of the PipeJet squeezed the tube in a
periodic motion to dispense droplets. The capillary forces caused contin-
uous reﬁlling of the tube. To determine the volume of the ejected droplets
and to adjust the PipeJet parameters if necessary, a computer-based im-
age analysis algorithm was used as previously described in literature.[10,25]
Brieﬂy, captured images of ejected droplets were analyzed using an image
segmentation algorithm. The background was subtracted and the drop
contour was detected. The drop was assumed to be a stack of multiple
cylinders. All cylinders have a height equal to the pixel size, and the diam-
eters were given by the length of each detected pixel row. To obtain the
ejected drop volume, the sum of all cylinder volumes was calculated. Un-
less otherwise stated, the PipeJet parameters were set to dispense droplets
with a volume in the range of 10–12 nL at a frequency in the range of 7–8
Hz.

Substrate cooling was provided by a recirculating chiller (Fryka GmbH,
Germany) connected to a heat-dissipating cold plate and a custom-
designed aluminum microplate holder.

In order to control all the moving parts and functions of the platform, a
software based on C++ has been developed in-house. A detailed scheme
with all components is shown in Figure 6.

Cell Culture and Spheroid Generation: The benchmarking of the de-
veloped platform was performed with multicellular tumor spheroids. For
this purpose, the breast cancer cell line MCF7, the human prostate can-
cer cell line LNCaP, and the human lung cancer cell line A549 were used
(all obtained from BIOSS Center for Biological Signaling Studies, Freiburg,
Germany). MCF7 and A549 cells were cultured at 37 °C and 5% CO2 in
Dulbecco’s modiﬁed Eagle’s medium (DMEM), high glucose, GlutaMAX
supplement, pyruvate (Thermo Fisher Scientiﬁc, USA) supplemented with
10% fetal bovine serum (FBS, Thermo Fisher Scientiﬁc, USA) and 1% peni-
cillin/streptomycin (Thermo Fisher Scientiﬁc, USA). LNCaP cells were cul-
tivated in RPMI-1640 medium (Sigma-Aldrich, USA) supplemented with
10% FBS, 2 × 10−3 m Glutamine and 1% penicillin/streptomycin.

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (11 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

To prepare large numbers of spheroids for our experiments, we used
Corning Elplasia 12K ﬂasks (Corning, USA) according to the manufac-
turer’s instructions. Brieﬂy, cells were harvested and resuspended in 25 mL
DMEM or RPMI medium supplemented with 10% FBS and 1% peni-
cillin/streptomycin. The cell concentration was adjusted to provide a spe-
ciﬁc number of cells per cavity in the ﬂasks to generate spheroids of dif-
ferent sizes. We worked in a range of 50–100 cells per cavity. This resulted
in spheroid diameters ranging from ≈50 to 260 μm. The spheroid ﬂasks
remained in the incubator for at least three days. Mature spheroids were
then harvested by rinsing the ﬂasks with PBS.

Suspensions containing harvested spheroids were centrifuged at 150 g
for 5 minutes. The supernatant was removed and the spheroids were re-
suspended in 4–5 mL of DMEM or RPMI medium supplemented with 10%
FBS and 1% penicillin/streptomycin (complete spheroid culture medium).
Organoid Culture: To assess the automated selective handling of the
platform, we worked with heterogeneous colorectal cancer (CRC) mouse
organoids kindly provided by Prof. Tilman Brummer (Institute of Molec-
ular Medicine and Cell Research, University of Freiburg, Germany). Tis-
sue isolation, colony formation and organoid generation are described in
detail by Reischmann et al. and were approved by the German Govern-
ment Commission for animal protection and the local ethics committee
(X-15/09H; X-18/06C; X-19/05C).[16] Organoids were propagated with mi-
nor modiﬁcations compared to[16]. Brieﬂy, organoids were cultivated in
domes of 4 mg mL−1 basement membrane extract BME (Cultrex Reduced
Growth Factor Basement Membrane Extract, Type 2, Pathclear, R&D Sys-
tems, Inc., USA). Organoids were harvested by disrupting the matrix dome
by pipetting up and down and rinsing the sample container with ice-cold
0.1% BSA-PBS solution. The sample was collected in a 15 mL tube coated
with 1% BSA. Organoids were mechanically disrupted by pipetting up and
down several times and passed through a 30 μm cell strainer. Organoids
were washed out from the strainer and collected in a centrifuge tube. The
sample was centrifuged at 200 × g for 5 min at 4 °C, the supernatant was
removed and the organoids were resuspended in 4 mg mL−1 BME matrix.
The organoid-hydrogel mixture was seeded in 30 μL domes onto a 24-well
plate and placed into the incubator at 37 °C. After polymerization of the
hydrogel, the domes were covered with 500 μL of complete organoid cul-
ture medium (3D Tumorsphere Medium XF, supplemented with 10% FBS,
1% penicillin/streptomycin and 8 ng mL−1 bFGF, Thermo Fisher Scientiﬁc,
USA). Medium was changed twice a week and organoids were passaged
once a week.

To gently harvest CRC organoids to benchmark the platform, the
medium was removed and 300 μL Cultrex Organoid Harvesting Solution
(R&D Systems, Inc., USA) was added. After 30 min at 4 °C, the hydro-
gel was dissolved. The sample was passed through a 30 μm cell strainer.
Organoids were washed out from the ﬁlter, collected in a 1% BSA-coated
tube and centrifuged at 200 × g for 4 min. The supernatant was removed
and the organoids were resuspended in 4–5 mL complete organoids cul-
ture medium.

Cytocompatibility Assays: To determine cell viability of the spheroids
or organoids, the viability assay CellTiterGlo 3D (Promega, USA) was per-
formed according to the manufacturer’s instructions. The background sig-
nal of noncell containing wells was subtracted and the received signal was
divided by the number of cell aggregates present in each well. Apoptosis
and necrosis were assessed using the RealTime-Glo Annexin V Apoptosis
and Necrosis Assay (Promega, USA) according to the manufacturer’s in-
structions. Signals were normalized with the signal obtained for manually
pipetted cell aggregates. ROS generation was assessed using the ROS-
Glo H2O2 Assay (Promega, USA). All signals were read using a Tecan
Spark20M plate reader.

Computational Fluid Dynamics Simulation: Computational ﬂuid dy-
namics (CFD) simulations were performed using the Fluid Flow module
of Comsol version 5.4.[26] We approximated the pulsed ﬂow due to droplet
ejection as a steady-state laminar ﬂow with the mean ﬂow rate ̄Q

̄Q = VDrop

⋅ fDrop

(4)

where VDrop is the average volume of dispensed droplets and fDrop is the
droplet ejection frequency.

Data and Image Analysis: Deposited spheroids or organoids were im-
aged either with the reservoir camera module of the platform or with 4× or
10× magniﬁcation of an inverted light microscope (CKX41, Olympus K.K.,
Japan). The area A of cell aggregates was measured either with ImageJ or
with custom written Python scripts using the scikit-image packages.[27]
The diameter d of the cell aggregates was calculated as

d = 2 ⋅

√

A∕𝜋

(5)

Statistical Analysis: For data visualized in box plots, the boxes extend
from the ﬁrst to the third quartile of the data, and the whiskers extend
from the edges of each box to the last data point in the 1.5 × interquar-
tile range. The center line of the box marks the median, and circles
indicate outliers. For data visualized in bar plots, the height of each bar
represents the mean of the data with error bars as ± standard deviation
(s.d.). Error bar plots show means ± s.d. Means are expressed with
± s.d.

Statistical tests were carried out with the python SciPy module
“scipy.stats.”[28] After normal distribution was tested with the D’Agostino-
Pearson test for normality, the statistical evaluation of the data was per-
formed with the two-tailed t-test, unless otherwise stated. P-values ≥ 0.05
were considered nonsigniﬁcant (n.s.), while signiﬁcant P-values were cat-
egorized as *P < 0.05, **P < 0.01 and ***P < 0.001.

Supporting Information

Supporting Information is available from the Wiley Online Library or from
the author.

Acknowledgements

The authors thank Jasmin Traichel and Prof. Dr. Tilman Brummer for
providing us with CRC mouse organoids and valuable handling in-
structions and cultivation protocols. Further, the authors thank Ellen
Woehr for her assistance with organoid culture. The authors thank
our ADAPT / ADAPT-2 partner 2cureX GmbH for their valuable con-
tributions to initial device speciﬁcations and usability testing. Funding:
German Federal Ministry of Education and Research, research grant
ADAPT (161L0235A/161L0235B/161L0235C, SK/PK/2cureX GmbH). Ger-
man Federal Ministry of Education and Research, research grant ADAPT-2
(16LW0335K/16LW0336/16LW0337, SK/SZ/2cureX GmbH).

Open access funding enabled and organized by Projekt DEAL.

Conﬂict of Interest

V.Z., S.K., D.F. have submitted the basic concept of the Pick-Flow-Drop
principle for patent.

Data Availability Statement

The data that support the ﬁndings of this study are available from the cor-
responding author upon reasonable request.

Keywords

automation, high-throughput, microﬂuidics, organoids, spheroids

Received: October 2, 2023
Revised: December 28, 2023
Published online: February 11, 2024

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (12 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

[1] a) K. Duval, H. Grover, L.-H. Han, Y. Mou, A. F. Pegoraro, J. Fredberg,
Z. Chen, Physiology 2017, 32, 266. b) J. C. Fontoura, C. Viezzer, F.
G. dos Santos, R. A. Ligabue, R. Weinlich, R. D. Puga, D. Antonow,
P. Severino, C. Bonorino, Mater. Sci. Eng., C: Mater. Biol. Appl. 2020,
107, 110264.

[2] C. Jubelin, J. Muñoz-Garcia, L. Griscom, D. Cochonneau, E. Ollivier,
M.-F. Heymann, F. M. Vallette, L. Oliver, D. Heymann, Cell Biosci.
2022, 12, 155.

[3] C. Jensen, Y. Teng, Front. Mol. Biosci. 2020, 7, 33.
[4] a) S. Kim, S. Choung, R. X. Sun, N. Ung, N. Hashemi, E. J. Fong, R.
Lau, E. Spiller, J. Gasho, J. Foo, S. M. Mumenthaler, SLAS Discovery
2020, 25, 744. b) A. J. Walsh, J. A. Castellanos, N. S. Nagathihalli, N.
B. Merchant, M. C. Skala, Pancreas 2016, 45, 863.

[5] M. Kapałczy´nska, T. Kolenda, W. Przybyła, M. Zaj ˛aczkowska, A.
Teresiak, V. Filas, M. Ibbs, R. Bli´zniak, Ł. Łuczewski, K. Lamperska,
Arch. Med. Sci. 2018, 14, 910.

[6] a) K. Kretzschmar, H. Clevers, Dev. Cell 2016, 38, 590. b)
Yamaha Motor Co., Ltd., The Cell Picking and Imaging Sys-
tem. CELL HANDLER | Yamaha Motor Co., Ltd. 25.12.2023,
c) MIMETAS
https://global.yamaha-motor.com/business/hc/;
B.V, Flyer: Automated versus manual placement of spheroids in
OrganoPlate Graft. 25.12.2023, https://www.mimetas.com/ﬁles/
products/OrganoPlate%20Graft/2021MIMETAS-Yamaha-manual-
vs-automated-cell-placement_Flyer.pdf .

[7] B. Ayan, D. N. Heo, Z. Zhang, M. Dey, A. Povilianskas, C. Drapaca, I.

T. Ozbolat, Sci. Adv. 2020, 6, eaaw5111.

[8] a) A. Higa, N. Takahashi, G. Hiyama, H. Tamura, H. Hoshi, K.
Shimomura, S. Watanabe, M. Takagi, J. Visual. Exp. 2021, 172, e62668;
b) N. Takahashi, A. Higa, G. Hiyama, H. Tamura, H. Hoshi, Y.
Dobashi, K. Katahira, H. Ishihara, K. Takagi, K. Goda, N. Okabe, S.
Muto, H. Suzuki, K. Shimomura, S. Watanabe, M. Takagi, Oncol. Lett.
2021, 21, 406,; c) J. Kondo, T. Ekawa, H. Endo, K. Yamazaki, N. Tanaka,
Y. Kukita, H. Okuyama, J. Okami, F. Imamura, M. Ohue, K. Kato, T.
Nomura, A. Kohara, S. Mori, S. Dan, M. Inoue, Cancer Sci. 2019, 110,
345.

[9] a) B. Ayan, Y. Wu, V. Karuppagounder, F. Kamal, I. T. Ozbolat,
Sci. Rep. 2020, 10, 13148. b) I. Grexa, A. Diosdi, M. Harmati,
A. Kriston, N. Moshkov, K. Buzas, V. Pietiäinen, K. Koos,
P. Horvath, Sci. Rep. 2021, 11, 14813; c) Sartorius Lab In-
|
struments GmbH & Co. KG., Cell Selection and Retrieval
CellCelector
https://www.sartorius.
com/en/products/cell-selection-and-retrieval?utm_source=
google&utm_medium=cpc&utm_campaign=CellCelector&utm_
term=dynamic_ads&utm_content=search&gad_source=
1&gclid=Cj0KCQiA7aSsBhCiARIsALFvovxeQqcSIWJkp6dNnM_
uihA32dAVqdzsW1Obx24DAjZ6SWmnftnoDhwaAlytEALw_wcB.
J. Dornhof, V. Zieger, J. Kieninger, D. Frejek, R. Zengerle, G. A. Urban,
S. Kartmann, A. Weltin, Lab Chip 2022, 22, 4369.

25.12.2023.

Sartorius.

|

[10]

[11] L. Gutzweiler, S. Kartmann, K. Troendle, L. Benning, G. Finkenzeller,
R. Zengerle, P. Koltay, G. B. Stark, S. Zimmermann, Biofabrication
2017, 9, 25027.

[12] a) S. Cosson, M. Bennet, O. Krispin, P. Kollhof, M. Horn, S. Clerc, G.
Tourniaire, Bolster your conﬁdence with your 3D cellular aggregates
assay with automated bulk spheroids and organoids isolation
and sorting. 31.08.2023. https://www.cellenion.com/wp-content/
uploads/2022/02/Cellenion_Poster_SLAS2022_02022022-1.pdf ; b)
S. Cosson, S. Ruiz, F. Beurton, M. Bennet, G. Tourniaire, Automated
3D spheroids sorting, isolation and dispense. 27.11.2023. https:
//www.cellenion.com/wp-content/uploads/2023/06/26-AppNote-
Automated-3D-spheroids-sorting-isolation-and-dispense.pdf .
[13] V. Mironov, R. P. Visconti, V. Kasyanov, G. Forgacs, C. J. Drake, R. R.

Markwald, Biomaterials 2009, 30, 2164.

[14] a) A. M. Blakely, K. L. Manning, A. Tripathi, J. R. Morgan, Tissue Eng.,
Part C: Methods 2015, 21, 737; b) B. C. Ip, F. Cui, A. Tripathi, J. R.

Morgan, Biofabrication 2016, 8, 25015. c) A. Stern, B. Thompson, K.
Williams, R. McClellan, S. Gebhart, J. Hartman, SLAS Discovery 2022,
27, 201. d) J. G. Roth, L. G. Brunel, M. S. Huang, Y. Liu, B. Cai, S.
Sinha, F. Yang, S. P. Pașca, S. Shin, S. C. Heilshorn, Nat. Commun.
2023, 14, 4346. e) M. Lang, W. Wang, X. Chen, T. Woodﬁeld, in IEEE
Int. Conf. on Automation Science and Engineering, IEEE, Piscataway,
NJ 2010; f) H. Chen, Z. Wu, Z. Gong, Y. Xia, J. Li, L. Du, Y. Zhang, X.
Gao, Z. Fan, H. Hu, Q. Qian, Z. Ding, S. Guo, Adv. Healthcare Mater.
2022, 11, e2102784.

[15] W. Streule, T. Lindemann, G. Birkle, R. Zengerle, P. Koltay, JALA Char-

lottesv. Va 2004, 9, 300.

[16] N. Reischmann, G. Andrieux, R. Griﬃn, T. Reinheckel, M. Boerries, T.

Brummer, Oncogene 2020, 39, 6053.

[17] a) M. J. Mitchell, M. R. King, New J. Phys. 2013, 15, 15008. b) J. Yin, L.
Sunuwar, M. Kasendra, H. Yu, C.-M. Tse, C. C. Talbot, T. Boronina, R.
Cole, K. Karalis, M. Donowitz, Am. J. Physiol. Gastrointest. Liver Phys-
iol. 2021, 320, G258.
Pengnam,

Patrojanasophon, W.
Radchatawedchakoon, B. Yingyongnarongkul, P. Opanasopit, P.
Charoensuksai, Pharmaceutics 2021, 13, 550. b) M. Di Donato, P.
Giovannelli, A. Migliaccio, A. Bilancio, Int. J. Mol. Sci. 2022, 23,
9008.

Plianwong,

[18] a)

S.

S.

P.

[19] Z. Zhao, X. Chen, A. M. Dowbaj, A. Sljukic, K. Bratlie, L. Lin, E. L. S.
Fong, G. M. Balachander, Z. Chen, A. Soragni, M. Huch, Y. A. Zeng,
Q. Wang, H. Yu, Nat. Rev. Methods Primers 2022, 2, 94.

[20] a) Y. Hu, X. Sui, F. Song, Y. Li, K. Li, Z. Chen, F. Yang, X. Chen, Y.
Zhang, X. Wang, Q. Liu, C. Li, B. Zou, X. Chen, J. Wang, P. Liu, Nat.
Commun. 2021, 12, 2581,; b) C. Zhou, Y. Wu, Z. Wang, Y. Liu, J. Yu,
W. Wang, S. Chen, W. Wu, J. Wang, G. Qian, A. He, Cancer Med. 2023,
12, 14375.

[21] M. van de Wetering, H. E. Francies, J. M. Francis, G. Bounova, F. Iorio,
A. Pronk, W. van Houdt, J. van Gorp, A. Taylor-Weiner, L. Kester, A.
McLaren-Douglas, J. Blokker, S. Jaksani, S. Bartfeld, R. Volckman, P.
van Sluis, V. S. W. Li, S. Seepo, C. Sekhar Pedamallu, K. Cibulskis, S.
L. Carter, A. McKenna, M. S. Lawrence, L. Lichtenstein, C. Stewart, J.
Koster, R. Versteeg, A. van Oudenaarden, J. Saez-Rodriguez, R. G. J.
Vries, et al., Cell 2015, 161, 933.

[22] M. A. Foo, M. You, S. L. Chan, G. Sethi, G. K. Bonney, W.-P. Yong, E.
K.-H. Chow, E. L. S. Fong, L. Wang, B.-C. Goh, Biomark Res. 2022, 10,
10.

[23] Z. Fang, P. Li, F. Du, L. Shang, L. Li, Exp. Hematol. Oncol. 2023, 12,

69.

[24] G. Vlachogiannis, S. Hedayat, A. Vatsiou, Y. Jamin, J. Fernández-
Mateos, K. Khan, A. Lampis, K. Eason, I. Huntingford, R. Burke,
M. Rata, D.-M. Koh, N. Tunariu, D. Collins, S. Hulkki-Wilson, C.
Ragulan, I. Spiteri, S. Y. Moorcraft, I. Chau, S. Rao, D. Watkins, N.
Fotiadis, M. Bali, M. Darvish-Damavandi, H. Lote, Z. Eltahir, E. C.
Smyth, R. Begum, P. A. Clarke, J. C. Hahne, et al., Science 2018, 359,
920.

[25] a) D. Liang, T. G. Muniyogeshbabu, L. Tanguy, A. Ernst, R. Zengerle,
P. Koltay, in 1st International Conference on Micro Fluidic Handling
Systems, 2012, p. 95 ﬀ.; b) ISO, ISO 23783-2:2022 Automated liquid
handling systems Part 2: Measurement procedures for the determi-
nation of volumetric performance. 25.12.2023. https://www.iso.org/
standard/76958.html.

[26] COMSOL Multiphysics, COMSOL 5.4 Documentation CFD Module
User’s Guide. 25.12.2023, https://doc.comsol.com/5.4/docserver/
#!/com.comsol.help.cfd/html_CFDModuleManual.html.

[27] S. van der Walt, J. L. Schönberger, J. Nunez-Iglesias, F. Boulogne, J.

D. Warner, N. Yager, E. Gouillart, T. Yu, Peer J. 2014, 2, e453.

[28] P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D.
Cournapeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J.
van der Walt, M. Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R. J.
Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey, ˙I. Polat, J. VanderPlas,
D. Laxalde, J. Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C.

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (13 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensewww.advancedsciencenews.com

www.advhealthmat.de

R. Harris, A. M. Archibald, SciPy 1.0 Contributors, et al., Nat. Methods
2020, 17, 261.

[29] A. Sekimoto, Y. Kanemaru, Y. Okano, K. Kanie, R. Kato, M. Kino-oka,

Regener. Ther. 2019, 12, 83.

[30] C. Poon, J. Mech. Behav. Biomed. Mater. 2022, 126, 105024.

[31] F. Koch, K. Tröndle, G. Finkenzeller, R. Zengerle, S. Zimmermann, P.

Koltay, Int. J. Bio print. 2020, 20, e00094.

[32] K. I. W. Kane, E. Lucumi Moreno, C. M. Lehr, S. Hachi, R. Dannert,
R. Sanctuary, C. Wagner, R. M. T. Fleming, J. Baller, AIP Adv. 2018, 8,
https://doi.org/10.1063/1.5067382.

Adv. Healthcare Mater. 2024, 13, 2303350

2303350 (14 of 14)

© 2024 The Authors. Advanced Healthcare Materials published by Wiley-VCH GmbH

 21922659, 2024, 9, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adhm.202303350, Wiley Online Library on [09/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
