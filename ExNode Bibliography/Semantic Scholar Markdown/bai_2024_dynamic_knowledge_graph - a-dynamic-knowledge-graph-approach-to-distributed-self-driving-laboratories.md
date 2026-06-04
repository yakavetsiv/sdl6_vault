---
title: "A dynamic knowledge graph approach to distributed self-driving laboratories"
doi: 10.1038/s41467-023-44599-9
source_url: https://www.nature.com/articles/s41467-023-44599-9.pdf
source_file: bai_2024_dynamic_knowledge_graph - a-dynamic-knowledge-graph-approach-to-distributed-self-driving-laboratories.pdf
type: semantic-scholar-oa-fulltext
---

# A dynamic knowledge graph approach to distributed self-driving laboratories

## Metadata

- DOI: 10.1038/s41467-023-44599-9
- Source URL: https://www.nature.com/articles/s41467-023-44599-9.pdf
- Downloaded file: [[Semantic Scholar PDFs/bai_2024_dynamic_knowledge_graph - a-dynamic-knowledge-graph-approach-to-distributed-self-driving-laboratories|bai_2024_dynamic_knowledge_graph - a-dynamic-knowledge-graph-approach-to-distributed-self-driving-laboratories.pdf]]
- Extracted characters: 74045

## Extracted Text

Article

https://doi.org/10.1038/s41467-023-44599-9

A dynamic knowledge graph approach to
distributed self-driving laboratories

Received: 14 July 2023

Accepted: 21 December 2023

Check for updates

;
,
:
)
(

0
9
8
7
6
5
4
3
2
1

;
,
:
)
(

0
9
8
7
6
5
4
3
2
1

1, Sebastian Mosbach 1,2, Connor J. Taylor3,4,8, Dogancan Karan2,

Jiaru Bai
Kok Foong Lee5, Simon D. Rihm 1,2, Jethro Akroyd 1,2, Alexei A. Lapkin 1,2,4 &
Markus Kraft

1,2,6,7

The ability to integrate resources and share knowledge across organisations
empowers scientists to expedite the scientiﬁc discovery process. This is
especially crucial in addressing emerging global challenges that require global
solutions. In this work, we develop an architecture for distributed self-driving
laboratories within The World Avatar project, which seeks to create an all-
encompassing digital twin based on a dynamic knowledge graph. We employ
ontologies to capture data and material ﬂows in design-make-test-analyse
cycles, utilising autonomous agents as executable knowledge components to
carry out the experimentation workﬂow. Data provenance is recorded to
ensure its ﬁndability, accessibility, interoperability, and reusability. We
demonstrate the practical application of our framework by linking two robots
in Cambridge and Singapore for a collaborative closed-loop optimisation for a
pharmaceutically-relevant aldol condensation reaction in real-time. The
knowledge graph autonomously evolves toward the scientist’s research goals,
with the two robots effectively generating a Pareto front for cost-yield opti-
misation in three days.

The concept of laboratory automation, recently reinterpreted as self-
driving laboratories (SDLs)1,2, has been in existence since the 1960s,
when ref. 3 introduced the ﬁrst automated chemistry hardware. Since
then, SDLs have gained widespread adoption in chemistry4–7, materials
science8,9, biotechnology10,11 and robotics12, resulting in accelerated
scientiﬁc discovery and societal development. However, the imple-
mentation of SDLs can be challenging and typically requires a highly
specialised team of researchers with expertise in chemistry, engi-
neering, and computer science. Consequently, studies are often con-
ducted by large research groups within a single organisation. Even in
cases where collaborations occur between research groups, the SDL is
usually centralised within the same laboratory.

In response to the pressing global challenges of today, there is a
growing consensus within the scientiﬁc community that a paradigm
shift towards a globally collaborative research network is necessary13–15.
This shift requires decentralising SDLs to integrate different research
groups to contribute their expertise towards solving emerging
problems16. Such decentralisation holds great potential in supporting
various tasks ranging from automating the characterisation of epis-
temic uncertainty in experimental research17 to advancing human
exploration in deep space18. Achieving this vision is not an easy task
and entails three major challenges. The ﬁrst challenge is efﬁciently
orchestrating heterogeneous resources19, which includes hardware
from different vendors and diverse computing environments.

1Department of Chemical Engineering and Biotechnology, University of Cambridge, Philippa Fawcett Drive, Cambridge CB3 0AS, UK. 2Cambridge Centre for
Advanced Research and Education in Singapore (CARES), 1 Create Way, CREATE Tower, #05-05, Singapore 138602, Singapore. 3Astex Pharmaceuticals, 436
Cambridge Science Park Milton Road, Cambridge CB4 0QA, UK. 4Innovation Centre in Digital Molecular Technologies, Yusuf Hamied Department of
Chemistry, University of Cambridge, Lensﬁeld Road, Cambridge CB2 1EW, UK. 5CMCL Innovations, Sheraton House, Cambridge CB3 0AX, UK. 6School of
Chemical and Biomedical Engineering, Nanyang Technological University, 62 Nanyang Drive, 637459 Singapore, Singapore. 7The Alan Turing Institute,
London NW1 2DB, UK. 8Present address: Faculty of Engineering, University of Nottingham, University Park, Nottingham NG7 2RD, UK.

e-mail: mk306@cam.ac.uk

Nature Communications | 

(2024) 15:462 

1


Article

https://doi.org/10.1038/s41467-023-44599-9

standardising language

The second challenge is sharing data across organisations20, which
requires
research is
communicated21. During this process, the source and metadata of the
research need to be tracked to facilitate reproducibility, which leads to
the third challenge of data provenance recording following FAIR
principles – Findable, Accessible, Interoperable and Reusable22.

in which the

Many attempts have been made to tackle these challenges with
different focuses. For resource orchestration, middleware such as
ChemOS23, ESCALATE24, and HELAO25 exist to glue different compo-
nents within an SDL and abstract the hardware resources. For data
sharing, χDL26,27 and AnIML28 are examples of standard protocols
developed for synthesis and analysis respectively. In the realm of data
provenance, Mitchell et al.29 proposed a data pipeline to support the
modelling of the COVID pandemic, whereas ref. 30 devised a knowl-
edge graph to record experiment provenance in materials research.
Although these studies provide insights into building a collaborative
research environment, they are developed in isolation with customised

Fig. 1 | An overview of the World Avatar approach towards globally connected
laboratory digital twins. a Three interrelated aspects of a chemical research
laboratory that need to be represented, adapted from36. The handler set pertains to
the tasks demanding the physical involvement of mobile units. The experiment set
includes stationary units, speciﬁcally hardware and chemicals. The laboratory set
represents the environmental conditions and building infrastructure. The inter-
secting regions symbolise the nuanced roles within the laboratory, requiring
expertise in the delineated sets. At the intersection of these three circles is the
World Avatar project, an initiative aiming to proﬁciently integrate expertise across
these essential facets. This paper focuses on the automation of chemical reaction
optimisation, a task that can be viewed as part of the daily work of many research
scientists. The illustrations of the lab glass and atoms were created using istock-
photo.com. b Two labs in Cambridge and Singapore are linked to demonstrate real-
time collaborative closed-loop optimisation. The process is triggered by a goal
request from a research scientist, and all data provenance is preserved. The
developed infrastructure in this work contributes to the establishment of dis-
tributed self-driving laboratories.

data interfaces. Enhancing interoperability both within and between
these systems is essential to establish a truly connected research
network.

As discussed in our previous work31,32, semantic web technol-
ogies such as knowledge graphs33 offer a viable path forward.
Ontologies abstract both resources and data using the same notion,
allowing for a common language between participants when allo-
cating tasks and sharing results. The World Avatar34,35 is such a
knowledge graph that aims to encompass all aspects of scientiﬁc
research laboratories as shown in Fig. 1a in their entirety: The
experiment itself,
including its physical setup and underlying
chemistry; moving handlers that can be of human or robotic nature;
and the laboratory providing necessary infrastructure and
resources36. The World Avatar goes beyond static knowledge
representation by encoding software agents as executable knowl-
edge components, enabling dynamicity and continuous incor-
poration of new concepts and data while preserving connections to
existing information. As the knowledge graph expands, this char-
acteristic allows for capturing data provenance from experimental
processes as knowledge statements, effectively acting as a living
copy of the real world. This dynamic knowledge graph streamlines
the immediate dissemination of data between SDLs, offering a
promising holistic solution to the aforementioned challenges32,37
and the pursuit of the Nobel Turing Challenge36,38.

In this work, we demonstrate a proof-of-concept for a distributed
network of SDLs enabled by a dynamic knowledge graph. This signiﬁes
the ﬁrst step towards digital research scientists (as shown in Fig. 1a)
collaborating autonomously. To illustrate the effectiveness of this
approach, as shown in Fig. 1b, we present a demonstration using two
robots in Cambridge and Singapore collaborating on a multi-objective
closed-loop optimisation problem in response to a goal request from
scientists.

Results
Architecture of distributed SDLs
Closed-loop optimisation in SDLs is a dynamic process that revolves
around design-make-test-analyse (DMTA) cycles39,40. Compared to
machine learning systems and scientiﬁc workﬂows that only capture
data ﬂows, SDLs offer an integrated approach by orchestrating both
computational and physical resources. This involves the integration of
data and material ﬂows, as well as the interface that bridges the gap
between the virtual and physical worlds. To this end, we propose a
conceptual architecture of distributed SDLs that effectively incorpo-
rates all three ﬂows, as illustrated in Fig. 2a.

The proposed architecture presents a framework to enable sci-
entists to set research goals and resource restrictions for a particular
chemical reaction and have them trigger a closed-loop process in
cyberspace. The process is initiated by the monitoring component,
which parses the research goals and requests the iterations needed to
achieve the objectives. The iterating component collects prior infor-
mation about the design space and passes it on to the component that
designs the next experiment. The algorithm employed, as well as the
availability of prior data, determines the combination of design vari-
ables to be proposed within the search space provided by the scientist.
Subsequently, the proposed physical experimentation is scheduled for
execution in one of the available laboratories, similar to the scheduling
of high-performance computing jobs41. The suggested conditions are
translated to the machine-actionable recipe that enables the control of
hardware for reaction and characterisation. In the physical world, this
is reﬂected in the material ﬂow between the two pieces of equipment.
The data processing component is then responsible for computing the
objectives by analysing the complete job information and raw data. If
the resources are still available, a comparison of these objectives with
the research goals determines whether the system should proceed to
the next iteration.

Nature Communications | 

(2024) 15:462 

2


Article

https://doi.org/10.1038/s41467-023-44599-9

Fig. 2 | An illustration of a distributed self-driving laboratories (SDLs) archi-
tecture. a Conceptual framework of components used to build a network of dis-
tributed SDLs for closed-loop optimisation. The framework encompasses a holistic
integration of data, software, hardware, and workﬂow, taking into account the ﬂow
of information within cyberspace and materials within physical space. Initiated by
the scientist speciﬁcations, these ﬂows autonomously evolve across cyber and
physical spaces until they accomplish the research goals or exhaust allocated
resources. The illustration of the design of experiments was created by ref. 81.

b Dynamic knowledge graph approach that is structured into three layers. The ﬁrst
layer represents the real world, where hardware is located and reactions take place.
The second layer consists of a dynamic knowledge graph in cyberspace, hosting
information such as the digital twin of the hardware and chemical data. The third
layer comprises active agents that continually monitor the status of the knowledge
graph, dynamically restructuring it, and actuating changes in the real world. The
illustration of docker was created using ﬂickr.com.

This architecture liberates the scientists from routine work,
however, it also poses challenges in the implementation in terms of
ensuring robustness, scalability, maintainability, safety, and ethics.
Ideally, the system should enable seamless integration of new devices,
resources, and algorithms without disrupting the system’s overall
functioning. It is also critical to allow for dynamic adaption to changes
in research goals and resource restrictions.

We believe dynamic knowledge graph technology can help with
realising this architecture32. Speciﬁcally, as illustrated in Fig. 2b, this
technology abstracts the software components as agents that receive

inputs and produce outputs. The ﬂow of data between these compo-
nents is represented as messages exchanged among these agents.
Physical entities can be virtualised as digital twins in cyberspace,
enabling real-time control and eliminating geospatial boundaries when
multiple labs are involved. This reformulation of the closed-loop
optimisation problem as information travelling through the knowl-
edge graph and reﬂecting their changes in the real world offers a
powerful framework for achieving true distributed SDLs. In this way,
we can think of an occurrence of physical experimentation as a
sequence of actions that dynamically generates information about a

Nature Communications | 

(2024) 15:462 

3


Article

https://doi.org/10.1038/s41467-023-44599-9

reaction experiment as it progresses in time, analogous to computa-
tional workﬂows42.

are utilised by a DesignOfExperiment study to propose new
experiments.

This work is part of a series of papers introducing a holistic
approach to lab automation by including all aspects of research
laboratories (see Fig. 1a) in an all-encompassing digital twin36. By
employing dynamic knowledge graphs that integrate knowledge
models from different domains, we can address the challenges related
to interoperability and adaptability commonly encountered in
platform-based approaches32. The goal-driven architecture facilitates
reasoning across the knowledge base, allowing high-level, abstract
goals to be decomposed into speciﬁc sub-goals and more tangible
tasks. Within this framework, humans play a dual role, functioning
both as goal setters and operators (when necessary) for executing and
intervening in experiments. When acting as operators, humans can be
represented in the knowledge graph similarly to robots, and they
receive instructions in a human-readable format. This facilitates the
realisation of a hybrid and evolving digital
laboratory, bridging
potential “interim technology gaps”43. The operations described in this
work are carried out through robotic handling, with humans primarily
involved in the preparation of initial materials and the maintenance of
the equipment.

Chemical ontologies and digital twins
The realisation of SDLs requires a connection between abstract
chemistry knowledge and concrete hardware for execution21. This calls
for a set of connected ontologies, as identiﬁed in our previous analysis
on the gaps in current semantic representations for chemical
digitalisation32. Figure 3 presents a selection of concepts and rela-
tionships as an effort to address these gaps. These concepts span
various levels of abstraction involved in scientiﬁc research, ranging
from the high-level research goals, through the conceptual level of
chemical reactions and the mathematical level of design of experi-
ments, down to the physical execution of reaction experiments and
the laboratory digital twin. We describe below ontologies’ cross-
domain characteristics, for technical details on each ontology please
see Supplementary Information section A.1.

For closed-loop optimisation in SDLs, we draw parallels between
the pursuit of optimal objectives and the reasoning cycles involved in
pursuing a goal44,45. The multi-objective problem can be formulated as
a GoalSet which comprises individual Goals. Each goal is associated
with speciﬁed dimensional quantities that can be achieved by a Plan,
which consists of multiple Steps to be carried out by corresponding
agents. From the implementation perspective, this is akin to a spe-
cialised research sub-domain within the scientiﬁc workﬂow commu-
nity that focuses on the management of iterative workﬂows abstracted
as directed cyclic graphs46. In this regard, we adopt the derived
information framework42, a knowledge-graph-native approach, to
manage the iterative workﬂow.

In developing chemical ontologies for SDLs, we draw upon the
lessons learnt in creating ontologies for chemical plants. One promi-
nent example is the OntoCAPE material and chemical process system47
ontology, which describes materials from three aspects: the Chemi-
calSpecies that reﬂects the intrinsic characteristics, Material as
part of the phase system which describes macroscopic thermo-
dynamic behaviour, and MaterialAmount that refers to a concrete
occurrence of an amount of matter in the physical world. Building on
this foundation, we introduce OntoReaction, an ontology that cap-
tures knowledge in wet-lab reaction experiments, and OntoDoE, an
ontology for the design of experiments (DoE) in optimisation cam-
paigns. As an effort to align with existing data, OntoReaction draws
inspiration from established schemas used in chemical reaction data-
bases like ORD48 and UDM49. ReactionExperiment is a concrete
realisation of a ChemicalReaction that is sampled at a set of
ReactionConditions and measures certain PerformanceIndica-
tors. When grouped together, they can form HistoricalData that

In the development of our hardware ontologies, we have expan-
ded upon concepts from the Smart Applications REFerence (SAREF)
ontology50, which is widely adopted in the ﬁeld of the Internet of
Things. We introduce OntoLab to represent the digital twin of a
laboratory, comprising a group of LabEquipment and Chemi-
calContainers that contain ChemicalAmount. Furthermore, we
create OntoVapourtec and OntoHPLC as ontologies for the equipment
involved in this work, linking them to the concrete realisation aspect of
OntoCAPE. We establish the link between abstract chemical knowledge
and hardware by translating ReactionCondition to Para-
meterSetting, which can be combined to form EquipmentSet-
tings for conﬁguration.

Contextualised reaction informatics
By utilising ontologies as blueprints, we can instantiate reaction
information while preserving connections to contextual recordings.
The reaction we choose for demonstration is an aldol condensation
reaction between benzaldehyde 1 (bold numbers for reference) and
acetone 2, catalysed by sodium hydroxide 3 to yield the target product
benzylideneacetone 451, which is pharmaceutically relevant and can be
used to treat idiopathic vomiting as an NK-1 receptor inhibitor52.
Additionally, reported side products include dibenzylideneacetone 5
and further condensation products from acetone polymerisation. The
choice of this well-studied reaction is deliberate, aimed at explaining
the contribution of our work to developing distributed SDLs to a broad
audience, and an application to more interesting chemistry will be
presented in a subsequent paper.

Figure 4 provides an illustrative representation of the chosen
reaction in the knowledge graph as viewed through various roles
within a laboratory, each with its unique perspective on the same
chemical. Taking the starting material benzaldehyde as an example,
it demonstrates how a knowledge graph can enhance the daily work
of different roles. A chemist, more interested in conceptual
description, might look at benzaldehyde as a reactant and search
for relevant species information. A data scientist might examine its
concentration to determine the appropriate usage of other chemi-
cals when designing conditions for a particular reaction experi-
ment. Meanwhile, the 3D digital twin built on top of the knowledge
graph offers a lab manager a centralised hub for real-time mon-
itoring of lab status53, ensuring the availability of an internal stan-
dard that can be mixed with the physical existence of benzaldehyde
to enable characterisation during the actual execution of the
experiment. In practice, the same individual might play several
roles, and the emphasis here is on the cross-domain interoperability
facilitated by the amalgamation of different aspects into a uniﬁed
knowledge graph. This integration ensures the relevance of infor-
mation to a diverse range of users while maintaining human over-
sight. Consequently, this approach may present opportunities for
the enhancement of various digital applications, such as the utili-
sation of virtual reality for laboratory training54.

The integration of chemical knowledge from PubChem,
represented by OntoSpecies for unique species identiﬁcation55,
serves as a critical link between these facets of chemicals. It enables
the identiﬁcation of potential input chemicals based on the reactant
and solvent during DoE and allows for the selection of appropriate
sources of starting materials from multiple chemical containers (see
Supplementary Information section A.2). Another aspect enabled
by this disambiguation of species relates to the representation of
chemical impurities. In this case study, all starting materials were
procured and used as received, with purities exceeding 99% for
liquid chemicals and 97% for NaOH pellets (see Supplementary
Table S4). The impurities are categorised as unknown components,
indicated using the data property
and their presence is

Nature Communications | 

(2024) 15:462 

4


Article

https://doi.org/10.1038/s41467-023-44599-9

Fig. 3 | A selection of concepts and relationships capturing different aspects in
self-driving laboratories (SDLs). The concepts are categorised based on their level
of abstraction, spanning from high-level research goals to conceptual descriptions
of chemical reactions and the mathematical expression of design of experiments,
as well as the physical execution of reaction experiments and the laboratory digital

twin. These concepts are interlinked with the OntoCAPE Material System, repre-
senting an effort to enhance interoperability with the community initiatives. Their
namespaces correspond to the colour coding. For complete knowledge repre-
sentation and namespace deﬁnitions see Supplementary Information section A.1.1.

for

OntoLab:containsUnidentiﬁedComponent
OntoLab:-
ChemicalAmount, a concept used for representing the concrete
appearances of chemicals in the physical world. In terms of the
collected reaction products, this representation is employed to
signify the existence of (at least one) OntoHPLC:Chromato-
gramPoint in the OntoHPLC:HPLCReport that is designated
OntoHPLC:unidentiﬁed. A more comprehensive representation
of impurities can be achieved in conjunction with concentration-
related concepts, such as OntoCAPE:Molarity, which we shall
incorporate in future work. For concrete examples of ontology
instantiation see Supplementary Information section A.1.

Goal-driven knowledge dynamics
Figure 5 presents a high-level overview of the goal-driven evolution of
the knowledge graph during closed-loop optimisation. The dynamicity
of the knowledge graph is enabled by the presence of software agents
that realise each component of the distributed architecture and facil-
itate the ﬂow of information within the graph. The process begins with
the goal derivation stage where the scientist initiates a goal request.
The Reaction Optimisation Goal (ROG) Agent translates this request
into a machine-readable statement that captures the scientist’s inten-
tion. To accommodate all objectives, a goal set is formulated
that considers each objective as a reward function for the agents’

Nature Communications | 

(2024) 15:462 

5


Article

https://doi.org/10.1038/s41467-023-44599-9

Fig. 4 | A snapshot of reaction views from different perspectives. a A chemist
view of a reaction is based on the chemical structures. b A data scientist view of a
reaction is based on the experiment conditions and resulting performance indi-
cators. c A lab manager view of a reaction is based on hardware status and chemical

availability. d The knowledge graph representation puts chemical informatics into
context, allowing for queries and answers across these varied layers of abstraction
(views). The colour coding corresponds to the ontological expression.

Nature Communications | 

(2024) 15:462 

6


Article

https://doi.org/10.1038/s41467-023-44599-9

Fig. 5 | Autonomous workﬂow triggered in response to goal requests from
scientists as information travels within the knowledge graph. a The Reaction
Optimisation Goal (ROG) Agent translates the speciﬁcation of a scientist into a
machine-readable statement and instantiates it into the knowledge graph. b The
Reaction Optimisation Goal Iteration (ROGI) Agent initiates the design-make-test-

analyse cycle, during which other agents query information from the digital twin
and actuate the hardware. c The progress of goal pursuit is assessed after each
iteration, determining whether to proceed to the next cycle. Steps (b) and (c) are
iterated until either goals are achieved or resources are depleted.

operations. For each participating laboratory, a Goal Iteration
Derivation instance is created using the derived information
framework42 and requested for execution by the Reaction Optimisa-
tion Goal Iteration (ROGI) Agent.

The goal iteration stage plays a central role in the evolution of the
dynamic knowledge graph. It involves the ROGI Agent initiating the
ﬂow of information among the participating agents towards achieving
the goals. This process begins with the ROGI Agent creating tasks for
the corresponding agents according to the DMTA cycle, including the
DoE Agent, Schedule Agent, and Post-Processing Agent. The DoE Agent
perceives the knowledge graph to retrieve prior data and chemical
stock available for experiments and then proposes a new experiment.
The Schedule Agent evaluates the hardware available in the speciﬁed
laboratory according to the proposed conditions and subsequently
selects the most appropriate hardware to execute the experiment. This
is accomplished by generating tasks for the agents responsible for
managing the selected digital twin. These agents actuate the equip-
ment to perform reaction and characterisation in the physical world.
When the HPLC report is generated, the Post-Processing Agent ana-
lyses the chromatogram data to calculate the objectives.

During the third stage, the ROG Agent utilises the obtained results
to determine whether the next iteration should be pursued. To do so, it
checks if the Pareto front of the multi-objective fulﬁls the pre-deﬁned
goals and if the resources are still available. The reaction experiment
performed in the current iteration then becomes historical data, ser-
ving as input for the succeeding round of the Goal Iteration
Derivation across all participating SDLs. Afterwards, a new request
will be made to the ROGI Agent to start a new iteration, forming a self-
evolving feedback loop.

To ensure correct data dependencies and the order of task
execution, we employed the derived information framework42 to
manage the iterative workﬂow. We implemented each software agent
using the derivation agent template provided by the framework. Once
deployed, these agents autonomously update the knowledge graph to
actively reﬂect and inﬂuence the state of the world.

This approach enables ﬂexibility and extensibility in the system.
As the digital twin of each lab is represented as a node in the knowl-
edge graph, new hardware can be added or removed during the
optimisation campaign by simply modifying the list of participating
laboratories. The experimental allowance can also be updated when
more chemicals become available. The system also supports data
sharing across organisations at the very moment the data are gener-
ated. Details on the internal logic and technical aspects of the agents in
the knowledge graph implementation are available in the Supple-
mentary Information section A.2.

Collaborative closed-loop optimisation
To demonstrate the scalability and modularity, the knowledge graph
approach was applied to a real-time collaborative closed-loop opti-
misation distributed over two SDLs in Cambridge and Singapore. The
objectives selected are run material cost and yield that were sampled
for a search space of molar equivalents (relative to benzaldehyde 1) of
acetone 2, NaOH 3, residence time and reaction temperature. The
research goals and restrictions were populated in the knowledge graph
via a web front end. As no prior experimental data was provided, the
agents start experiments with random conditions and gradually
update their beliefs using TSEMO algorithm56. Before running the
optimisation, two labs were veriﬁed to produce consistent results for

Nature Communications | 

(2024) 15:462 

7


Article

https://doi.org/10.1038/s41467-023-44599-9

Pareto Front

Cambridge

Singapore

450

400

350

300

250

200

)
1
-
L
£
(

t
s
o
C

(a)

150

0

20

40

60

80

100

Yield (%)

200

250

300
Cost (£ L-1)

350

400

0

20

40

60

80

Cambridge

Singapore

Yield (%)

Cambridge

Singapore

(b)

(c)

Fig. 6 | Objectives and design variables of experiments conducted in the closed-
loop optimisation campaign in distributed self-driving laboratories (SDLs).
Each dot refers to a single run. The animation of the optimisation progress is
available in Supplementary Movie 1. Interactive versions of 3D plots are available in
Supplementary Movies 2 and 3 for cost and yield objectives, respectively. Source
data are provided as a Source Data ﬁle. a Pareto front plot of the yield and cost

objectives for the aldol condensation reaction collaboratively optimised by two
distributed SDLs. b Three-dimensional plot of the four sampled design variables
colour coded for run material cost during the closed-loop optimisation. The size of
the dots denotes the molar equivalents of 3 in each run. c Three-dimensional plot of
the four sampled design variables colour coded for yield during the closed-loop
optimisation. The size of the dots denotes the molar equivalents of 3 in each run.

two control conditions, in line with the practice of Shields et al.57. For
experimental details see Supplementary Information section A.3.

Figure 6a presents the cost-yield objectives consisting of 65 data
points collected during the self-optimisation. Throughout the opera-
tion, two SDLs share the results with each other when proposing new
experimental conditions. The real-time collaboration demonstrated
faster advances in the Pareto front with the highest yield of 93%. The
chemicals used in this study were obtained from different vendors
compared to ref. 51, the cost is therefore not directly comparable due
to different prices. Although not considered in the optimisation, the
environment factor and space-time yield were found to be highly

correlated to the yield objective. The best values obtained are 26.17
and 258.175 g L−1 h−1 when scaled to the same benzaldehyde injection
volume (5 mL), both outperformed the previous study51.

Figure 6b, c illustrate the inﬂuence of the continuous variables on
the cost and yield objectives, with their interactive versions as Sup-
plementary Movie 2 and 3, respectively. The cost is calculated to count
for the molar amount of input chemicals sourced from the pumps
for the reaction. Therefore,
it increases linearly with the molar
equivalents of the starting materials. Similarly as identiﬁed by ref. 51,
reaction temperature has a positive correlation with the yield of
reaction, whereas the residence time shows a poor correlation.

Nature Communications | 

(2024) 15:462 

8


Article

https://doi.org/10.1038/s41467-023-44599-9

Upon examination of the molar equivalent of acetone 2, it can be
observed that its further increase after 30 results in a reduction in
yield. This decrease can be attributed to the formation of more side
product 5 and other further condensation products of acetone and
benzaldehyde.

Notably, the Singapore setup encountered an HPLC failure after
running for approximately 10 h. This caused peak shifting of the
internal standard which resulted in a wrongly identiﬁed peak that gives
more than 3500% yield. This point is considered abnormal by the
agents and therefore not utilised in the following DoE. An email noti-
ﬁcation was sent to the developer for maintenance which took the
hardware out of the campaign. The asynchronous and distributed
design enabled the Cambridge side to further advance the Pareto front
for the cost-yield trade-offs. It is also notable that the product peak was
missed for one run at the Cambridge side due to a small shift of the
peak which gives a yield of 0%. This point was taken into consideration
in the DoE, but fortunately, it did not affect the ﬁnal Pareto front as the
corrected yield is still Pareto-dominated. The optimisation campaign
was stopped since no more signiﬁcant improvement was observed in
terms of hypervolume, and also due to requests for repurposing the
equipment for other projects. The complete provenance records
(knowledge graph triples) are provided as Supplementary Data, along
with an interactive animation of the optimisation progress extracted
from them as Supplementary Movie 1.

Discussion
In this contribution, we presented a dynamic knowledge graph
approach to realise a conceptual architecture for distributed SDLs. We
developed ontologies to represent various aspects of chemical
knowledge and hardware digital twins involved in a closed-loop opti-
misation campaign. By employing autonomous agents as executable
knowledge components to update and restructure the knowledge
graph, we have enabled collaborative management of data and mate-
rial ﬂow across SDLs. Our approach allows scientists to initiate the
autonomous workﬂow by setting up a goal request, which triggers the
ﬂow of information through the knowledge graph as the experi-
mentation workﬂow progresses.

As a proof-of-concept demonstration, we applied the system to an
aldol condensation reaction using two setups across different parts of
the globe. Despite the differences in conﬁgurations, the reaction data
produced by both machines were interoperable owing to the layered
knowledge abstraction. Throughout the experiment, the system
recorded all data provenance as the knowledge graph evolved
autonomously, providing opportunities
informed machine
learning58. Our collaborative approach resulted in faster data genera-
tion and advanced the Pareto front while exhibiting resilience to
hardware failure.

for

The implementation of this work has provided valuable insights
and identiﬁed areas for future improvement in the realm of dynamic
knowledge graph systems. In terms of orchestration, it is crucial for the
system to be robust to network disruption since it is distributed over
the internet. We have implemented measures to ensure that agents
deployed in the lab can handle internet cut-offs and resume operations
once back online. To minimise downtime during reconnection, future
developments could provide on-demand, localised deployment of
critical parts of the knowledge graph to sustain uninterrupted
operation.

For efﬁcient optimisation and data quality, it is critical to have
control conditions in place when adding new setups to the network,
and only those generated results within the tolerance should be
approved. Complex reactions with high-dimensional domains may not
be sufﬁciently evaluated using only two control conditions. This
highlights the persisting challenges in maintaining data quality and
opens avenues for incorporating strategic cross-workﬂow validation
experiments.

To increase the system’s robustness against software and hard-
ware malfunctions, regular backups of all data in the central knowl-
edge graph should be implemented. Hardware failures during the self-
optimisation campaign, which resulted in abnormal data points, also
revealed an unresolved issue in automated quality control monitoring.
This accentuates the need for a practical solution to bridge the interim
technology gap, such as implementing a human-in-the-loop strategy
for the effective monitoring of unexpected experimental results.

Further development could also be made to federate the SDLs,
where each lab hosts its data and digital twins locally and only exposes
its capabilities in the central registry (a “yellow page”) without
revealing conﬁdential information. An authentication and authorisa-
tion mechanism should be added to control access to the equipment
and grant permission for federated learning.

When reﬂecting on the vision of distributed SDLs, our approach
exhibits both commonalities and distinctions when compared to
contemporary designs. Table 1 summarises the key design features, to
the best of our knowledge, as they relate to the three major challenges,
with the ﬁrst challenge further divided into the abstraction of resour-
ces and workﬂow coordination.

In terms of resource abstraction, all approaches (including the
one presented in this work) employ a modular design that considers
hardware limitations in granularity. This modularity is key for a
seamless integration of new resources into a plug-and-play system.
However, the way resources are exposed to the coordinator varies and
this signiﬁcantly impacts the orchestration of workﬂows across
laboratories. This applies to both workﬂow template encoding and its
actual execution. The dynamic knowledge graph approach uses agents
acting as lab resource wrappers with knowledge graph access. Agents
can register for jobs and proactively execute tasks assigned to the
digital twin of the resources they manage. This approach is preferable
compared to the practices in the remote procedure call paradigm,
where lab resources are made accessible as web servers. Based on our
experience, it can raise concerns among IT staff when exposing
resources across university or company ﬁrewalls. Similar to agents, our
approach encodes the workﬂow in the knowledge graph with each step
overseen by an agent. Compared to encoding workﬂows as a sequence
of function calls in scripting languages (such as Python), where
execution may struggle with asynchronous workﬂows evolving during
optimisation, our approach allows for real-time workﬂow assembly
and modiﬁcation. For a detailed technical discussion,
interested
readers can refer to the derived information framework42.

The integration of data serialisation and storage within workﬂow
aims to ease community adoption. As seen in Table 1, practices range
from transmitting diverse ﬁle formats to enforcing a uniﬁed data
representation. Starting with ad hoc extraction-transformation-
loading tools for new devices prototyping is practical and minimally
disruptive when upgrading a single lab. However, we ﬁnd this
approach less effective for scaling up to a large network of SDLs32. This
limitation is the driving force behind the development of the dynamic
knowledge graph approach, despite the initial cost required for
creating ontologies that capture a collective understanding of the
ﬁeld. Our design delegates the responsibility of digesting and trans-
lating ontologies into the requisite language and ﬁle formats to
autonomous agents. Compared to adopting a central coordinator to
handle data transfer and format translation, our approach emphasises
information propagation within a uniﬁed data layer, obviating the need
for peer-to-peer data transfer and alleviating network congestion.
Drawing an analogy to self-driving cars, once the “driving rules”
(ontologies) are learned, SDLs are granted permission to drive on the
“road” (information ﬂow). Compared to traditional relational data-
bases used in other studies, where schema modiﬁcation can be chal-
lenging,
in the dynamic
knowledge graph enhances its extensibility. Organising concepts and
relationships within a knowledge graph is also more intuitive than

the open-world assumption inherent

Nature Communications | 

(2024) 15:462 

9


Article

https://doi.org/10.1038/s41467-023-44599-9

i

i

.
e
c
v
e
d
h
c
a
e
o
t
g
n
d
n
o
p
s
e
r
r
o
c
e
l
b
a
t
e
s
a
b
a
t
a
d
e
h
t

e
l
k
c
p

i

,
.

g
.
e
,
s
t
a
m
r
o
f
e
l
ﬁ
e
s
r
e
v
d
n

i

i

i

e
c
v
e
d
h
c
a
e
d
n
a

r
o
f
e
l
b
i
s
n
o
p
s
e
r
o
s
l
a
s
i

i

r
o
t
a
n
d
r
o
o
c
e
h
T
.
s
l
l
a
c
n
o
i
t
c
n
u
f

e
r
a
s
b
o

j

i

l
a
n
o
i
t
a
t
u
p
m
o
c
g
n
m
u
s
n
o
c
-
e
m
T
.
s
r
e
v
r
e
s

i

s
t
n
e
m
e
r
u
s
a
e
m
g
n
i
r
u
d
d
e
t
c
e
l
l

o
c
a
t
a
d
a
t
e
m
e
c
v
e
D

i

i

-
r
i
d
b
r
o
f

i

m
u
d
e
m
s
s
e
l
-
e
l
ﬁ
a
s
a
d
e
y
o
p
m
e
s
i

l

8
2
L
M
n
A

I

2
/
P
T
T
H
d
n
a
C
P
R
g
g
n
i
s
u
s
l
l
a
c
n
o
i
t
c
n
u
f

f
o
e
c
n
e
u
q
e
s
A

i

s
e
r
u
t
a
e
F
A
L
S
s
a
d
e
t
c
a
r
t
s
b
a
e
r
a
s
n
o
i
t
c
n
u
f
e
r
a
w
d
r
a
H

8
2
A
L
S

i

e
c
n
a
n
e
v
o
r
p
l
a
t
n
e
m

i
r
e
p
x
E

e
g
a
r
o
t
s
d
n
a
n
o
i
t
a
s
i
l
a
i
r
e
s
a
t
a
D

n
o
i
t
a
r
t
s
e
h
c
r
o
w
o
ﬂ
k
r
o
W

n
o
i
t
c
a
r
t
s
b
a
e
c
r
u
o
s
e
R

e
c
n
e
r
e
f
e
R

)
s
L
D
S
(

i

s
e
i
r
o
t
a
r
o
b
a
l
g
n
v
i
r
d
-
f
l
e
s
d
e
t
u
b
i
r
t
s
i
d
f
o
n
o
i
t
a
s
i
l
a
e
r
e
h
t

s
d
r
a
w
o
t
k
r
o
w
s
i
h
t
d
n
a
s
n
g
i
s
e
d
y
r
a
r
o
p
m
e
t
n
o
c
n
e
e
w
t
e
b
n
o
s
i
r
a
p
m
o
C

|

1
e
l
b
a
T

.
s
e
l
ﬁ
L
M
X
n

i

d
e
r
o
t
s
e
r
a

d
n
a
s
m
e
t
s
y
s

t
n
e
m
e
g
a
n
a
m
n
o
i
t
a
m
r
o
f
n

i

y
r
o
t
a
r
o
b
a
l

n
e
e
w
t
e
b
n
o
i
s
s
i
m
s
n
a
r
t

a
t
a
d

l
a
c
i
t
y
l
a
n
a
l
a
n
o
i
t
c
e

.
s
m
e
t
s
y
s
a
t
a
d
y
h
p
a
r
g
o
t
a
m
o
r
h
c

.
s
l
o
c
o
t
o
r
p

r
i
e
h
t
h
t
i

i

w
e
r
u
t
c
e
t
i
h
c
r
a
e
c
v
r
e
s
-
o
r
c
m
a
g
n
w
o

i

i

l
l

o
f

i

.
e
n
h
c
a
m
e
t
a
t
s
a
s
a
d
e
b
i
r
c
s
e
d
r
u
o
v
a
h
e
b

i

n

i

s
p
m
a
t
s
e
m

i
t
h
t
i

w
d
e
r
o
t
s
e
r
a
s
g
o

l

n
o
i
t
u
c
e
x
e
b
o
J

i

r
o
t
a
n
d
r
o
o
c
l
a
r
t
n
e
c
e
h
t
n
e
e
w
t
e
b
d
e
m
a
e
r
t
s
e
r
a
a
t
a
D

n
o
h
t
y
P
f
o
e
c
n
e
u
q
e
s
a
s
e
t
u
c
e
x
e
r
o
t
a
n
d
r
o
o
c
l
a
r
t
n
e
c
e
h
T

i

i

A
L
S
s
a
d
e
t
c
a
r
t
s
b
a
e
r
a
e
r
a
w
d
r
a
h
d
n
a
e
r
a
w

t
f
o
s
h
t
o
B

6
7
S
O
m
e
h
C

g
n
m

i

i
t
n
o
i
t
a
r
e
p
o
d
e
l
i
a
t
e
d
e
h
T
.
s
e
l
p
i
r
t
s
a
k
r
o
w
e
m
a
r
f

n
o
i
t
a
l
s
n
a
r
t

i

l

l
a
c
g
o
o
t
n
o
r
i
e
h
T
.
r
e
v
r
e
s
e
l
ﬁ
a
n
o
d
e
r
o
t
s

i

i

g
n
n
a
t
b
o
n

i
s
n
o
i
t
a
t
i

m

i
l

I

i

P
A
o
t
g
n
w
o
d
e
d
r
o
c
e
r

t
o
n
s
i

n

i

d
e
r
o
t
s
e
r
a
n
o
i
t
a
c
o

l

r
e
v
r
e
s
e
l
ﬁ
e
h
t
o
t

i

s
r
e
t
n
o
p
d
n
a

.
t
n
e
g
a
e
r
a
w

t
f
o
s
e
v
i
t
c
e
p
s
e
r
e
h
t
y
b
d
e
g
a
n
a
m
p
e
t
s

-
i
r
e
d
e
h
t
g
n
i
s
u
d
e
p
p
a
r
w
s
i

,
s
e
c
r
u
o
s
e
r
e
r
a
w

t
f
o
s
o
t

.
e
t
a
l
p
m
e
t

t
n
e
g
a
n
o
i
t
a
v

i

-
e
c
v
e
d
f
o
g
n
i
t
s
i
s
n
o
c
a
m
e
h
c
s
a
h
t
i

w
e
s
a
b
a
t
a
d

l
a
n
r
e
t
n

i

i

.
s
e
l
b
a
t
c
ﬁ
c
e
p
s
-
e
c
v
e
d
d
n
a
c
i
t
s
o
n
g
a

i

.

e
r
a
w

t
f
o
s

-
k
r
o
w

f
o
n
o
i
t
u
c
e
x
e
e
h
t
h
t
i

i

w
d
e
t
a
c
o
s
s
a
a
t
a
d
a
t
e
M

d
e
v
r
e
s
d
n
a
e
s
a
b
a
t
a
d
L
Q
S
e
r
g
t
s
o
P
a
n

i

d
e
r
o
t
s
e
r
a
a
t
a
D

”
e
t
a
l
p
m
e
T
t
n
e
m

i
r
e
p
x
E
“

r
o
f
d
e
d
o
c
n
e
s
p
e
t
s

f
o
e
c
n
e
u
q
e
s
A

-
r
u
o
s
e
r

t
c
a
r
t
s
b
a
o
t
d
e
s
u
s
i

k
r
o
w
e
m
a
r
f
o
g
n
a
D
e
h
T

j

4
2
E
T
A
L
A
C
S
E

n

i

s
e
c
n
a
t
s
n

i

t
n
e
m

i
r
e
p
x
e
h
t
i

w
d
e
r
o
t
s
e
r
a
s
p
e
t
s
w
o
ﬂ

i

a
t
a
d
e
h
t
e
s
i
l
a
i
r
e
s
t
a
h
t
s
t
n
o
p
d
n
e
8
7
I
P
A
T
S
E
R
o
g
n
a
D
a
v

i

j

i

.
s
t
n
o
p
d
n
e

I

i

P
A
T
S
E
R
a
v
e
l
b
i
s
s
e
c
c
a
d
n
a

.
e
s
a
b
a
t
a
d

l
a
n
o
i
t
a
l
e
r
e
h
t

.

n
o
i
t
c
e
p
s
n

i

d
n
a
r
e
f
s
n
a
r
t
b
e
w

r
o
f

t
a
m
r
o
f

N
O
S
J
o
t
n

i

e
m
a
s
e
h
t
n

i

d
e
d
r
o
c
e
r
e
r
a
”
s
n
o
i
t
c
a
“

.
s
t
n
e
m
e
r
u
s
a
e
m

l
a
t
n
e
m

i
r
e
p
x
e
e
h
t

f
o
a
t
a
d
a
t
e
M

s
a
e
l
ﬁ
5
F
D
H

e
h
t
n

i

”
s
t
e
s
a
t
a
d
“
d
n
a
”
s
p
u
o
r
g
“

s
a
d
e
d
r
o
c
e
r
e
r
a
a
t
a
D

l
a
n
o
i
t
u
t
i
t
s
n

i

o
t
n

i

d
e
t
i
s
o
p
e
d
d
n
a

t
a
m
r
o
f
e
l
ﬁ
5
F
D
H

s
l
l
a
c

I

P
A
f
o
e
c
n
e
u
q
e
s
a
s
e
t
u
c
e
x
e
r
o
t
a
n
d
r
o
o
c
l
a
r
t
n
e
c
A

i

.
)
s
n
o
i
t
c
n
u
f
n
o
h
t
y
P
s
a
d
e
p
p
a
r
w

(

9
7
I
P
A
t
s
a
F
s
u
o
n
o
r
h
c
n
y
s
a
d
n
a
l
a
c
h
c
r
a
r
e
h
s
a
d
e
t
n
e
s

i

i

-
e
r
p
e
r
e
r
a

)
”
s
n
o
i
t
c
a
“
(

s
n
o
i
t
c
n
u
f

r
i
e
h
t
d
n
a
e
c
v
e
D

i

5
2

O
E
L
A
H

i

.
s
t
n
o
p
d
n
e

I

P
A
T
S
E
R
s
a
s
e
c

n
o
i
t
a
m
r
o
f
n

i

d
e
v
i
r
e
d
e
h
t

y
b
d
e
d
r
o
c
e
r

s
i

w
o
ﬂ
k
r
o
w

e
r
a
)

S
L
X
d
n
a
V
S
C

,
.

.

g
e
(

s
e
l
i
F
.

e
l
b
i
s
s
o
p
r
e
v
e
r
e
h
w

a
o
t
g
n
i
r
r
e
f
e
r
h
c
a
e
h
p
a
r
g
e
g
d
e
l
w
o
n
k
e
h
t
n

i

”
s
n
o
i
t
a
v
i
r
e
d
“

i

n
k
a
,
e
c
a
f
r
e
t
n

i

l

o
r
t
n
o
c
s
t
i

e
r
e
h
w

,

h
p
a
r
g
e
g
d
e
l
w
o
n
k

.
e
s
a
b
a
t
a
d

l
a
n
o
i
t
a
l
e
r
e
h
t
n

i

s
e
c
n
a
t
s
n

i

t
n
e
m

i
r
e
p
x
e

.

e
s
a
b
a
t
a
d
L
Q
S
e
r
g
t
s
o
P

h
t
i

w
d
e
r
o
t
s
e
r
a

a
t
a
d
a
t
e
m

r
e
h
t
o
d
n
a
,
s
n
o
i
t
c
a

a
n

i

n
o
i
t
p
i
r
c
s
e
d
s
i
s
e
h
t
n
y
s
e
h
t
h
t
i

w
d
e
l
d
n
u
b
d
n
a

-
c
u
r
t
s
n

i

e
l
b
a
n
o
i
t
c
a
-
e
n
h
c
a
m
o
t
n

i

i

.
t
p
i
r
c
s
n
o
h
t
y
P
a
n

i

s
n
o
i
t

d
e
l
i

p
m
o
c
r
e
t
a
l

s
i

i

h
c
h
w

n
a
c
t
i

t
a
h
t

s
n
o
i
t
c
a
e
r

i

l
a
c
m
e
h
c
n

i

s
n
o
i
t
a
r
e
p
o
t
i
n
u

.

e
t
u
c
e
x
e

d
e
m
r
o
f
r
e
p

l
a
u
t
c
a
e
h
t

,
s
n
o
i
t
c
u
r
t
s
n

i

e
r
a
w
d
r
a
H

t
a
m
r
o
f
e
l
ﬁ
e
v
i
t
a
n
r
i
e
h
t
n

i

t
p
e
k
e
r
a
s
t
r
o
p
e
r
s
i
s
y
l
a
n
a
e
h
T

,
t
a
m
r
o
f
L
M
X
n

i

d
e
s
s
e
r
p
x
e
s
i
s
p
e
t
s
s
i
s
e
h
t
n
y
s
f
o
e
c
n
e
u
q
e
s
e
h
T

e
h
t
n
o
d
e
s
a
b
d
e
t
c
a
r
t
s
b
a
/
d
e
s
i
r
o
g
e
t
a
c
s
i

e
r
a
w
d
r
a
H

,

0
8
6
2
L
D
χ

.
s
e
i
r
o
t
i
s
o
p
e
r

.
s
r
e
v
r
e
s
b
e
w

e
h
t
n

i

p
e
t
s
h
c
a
e
f
o
n
o
i
t
a
t
o
n
n
a
s
t
u
p
t
u
o
/
s
t
u
p
n

i

e
h
T

)
s
e
l
p
i
r
t
(

t
a
m
r
o
f

i

l

l
a
c
g
o
o
t
n
o
n

i

d
e
s
s
e
r
p
x
e
e
r
a
a
t
a
D

f
o
s
h
p
a
r
g
c
i
l
c
y
c
a
d
e
t
c
e
r
i
d
s
a
d
e
s
s
e
r
p
x
e
e
r
a
s
e
l
c
y
c
A
T
M
D

a
n

i

i

n
w

t

i

l
a
t
i
g
d
a
s
a
d
e
s
i
l
a
u
t
r
i
v
s
i

e
r
a
w
d
r
a
H

k
r
o
w
s
i
h
T

.
y
t
i
r
a
l
u
n
a
r
g
f
o

l
e
v
e
l

s
i
h
t

t
a
n
o
i
t
a
m
r
o
f
n

i

.

e
r
o
t
s
e
l
p
i
r
t
e
h
t

traditional tabular structures. However, this ﬂexibility may come at the
cost of performance issues when handling extensive data volumes,
especially when dealing with data on the scale of ORD. To counter this,
technologies such as ontology-based data access59 can create a virtual
knowledge graph from relational databases, combining the strengths
of both approaches.

Our approach to experimental provenance differs from others
due to hardware constraints. It focuses less on exact operation timing,
such as robotic arm motions, and more on capturing inputs and out-
puts within DMTA cycles. This facilitates high-level analysis, enabling
answering questions like “which experiments from lab A informed the
DoE study for a speciﬁc reaction in lab B”. This capability has been
effectively demonstrated in the interactive Pareto progress animation
provided in Supplementary Movie 1. However, for a deeper under-
standing of epistemic uncertainties associated with operations in
complex reactions, it is imperative to expand the ontologies for a more
granular abstraction of the experimental procedures. A potential
expansion in this regard could involve the ontologisation of χDL.

Looking forward, achieving a globally collaborative research net-
work requires collective efforts. As the knowledge graph aims to reﬂect
a communal understanding of the ﬁeld, involving different stake-
holders early on can accelerate collaboration and increase the chance
of success. Speciﬁcally, there exists an opportunity for using knowl-
edge graph technology as an integration hub for all aforementioned
initiatives. Industrial partners are encouraged to work together and
provide a uniﬁed API for interacting with their proprietary software
and hardware interfaces. This can be facilitated by efforts such as OPC
UA60 and SiLA28. Recent studies have shown the successful exchange of
HPLC methods between vendors in the Chromatography Data System
(CDS), demonstrating the potential for the ontology-based approach61.
Collaboration between scientists and industry is also important at
various stages of research and development62.

Overall, we believe the dynamic knowledge graph approach
demonstrated in this work provides the ﬁrst evidence of its potential to
establish a network of globally distributed SDLs. Although we focus on
ﬂow chemistry in this study, the principles are generic. The same
approach can be applied to DMTA cycles for other domains should
relevant ontologies and agents be made available, for example, to
support research in deep space18.

Methods
The World Avatar knowledge graph
This work follows the best practices in the World Avatar project. All
ontologies and agents are version-controlled on GitHub. We provide
our thought process during the development below. The same prin-
ciples can be followed for self-optimisation applications in other
domains.

Ontology development. Developing ontologies is often an iterative
process and it is not a goal in and of itself63. As suggested in32,36,37, we
follow the steps from specifying target deliverables to conceptualising
relevant concepts and ﬁnally implementing codes for queries. Aimed
at capturing data and material ﬂow in distributed SDLs, the relevant
concepts range from the reaction experiment to the hardware
employed to conduct it. In the World Avatar, ontologies are typically
developed to be digested by software agents which mimic the human
way of conducting different tasks64. Therefore, the development draws
inspiration from relevant software tools51,65,66 and existing reaction
database schemas48,49. Views of the domain experts67–69 are also con-
sulted to better align with the communal understanding of the subject.
During iterations, competency questions are used to test if the
ontologies meet case study requirements. The answers to these
questions are provided in the form of SPARQL queries that are exe-
cuted by the agents during their operations. Another essential aspect
to consider is data instantiation, where we adopted pydantic to

n
a
n

i

e
n
o
d
s
i

e
g
a
r
o
t
s
e
h
T
.

V
S
C
d
n
a
,

N
O
S
J

,
t
c
e
b
o

j

/
e
r
a
w
d
r
a
h
h
c
a
e
y
b
d
e
r
i
u
q
e
r

t
a
m
r
o
f
e
h
t
n

i

s
e
l
ﬁ
b
o

j

g
n
i
t
a
e
r
c

.
1
4

M
R
U
L
S
n
o
7
7

A
D

i
i

A
y
b
d
e
g
a
n
a
m

Nature Communications | 

(2024) 15:462 

10


Article

https://doi.org/10.1038/s41467-023-44599-9

simplify the querying and processing of data from the knowledge
graph. Overall, the ontology development process starts as easily as
drawing concepts and their relationships on a whiteboard and then
gradually materialising them in code.

Agent development. Following the development of ontologies,
agents are deﬁned as executables that process inputs and generate
outputs. Their I/O signatures are represented following OntoAgent70.
At the implementation level, all agents inherit the DerivationAgent
template in Python provided by the derived information framework42.
Speciﬁcally, agents utilise the asynchronous communication mode
when interacting with the knowledge graph as conducting experi-
ments is inherently a time-consuming process. Each of the agents
monitors the jobs assigned to itself and records the progress of
execution in the knowledge graph. The derived information frame-
work does most of the work behind the scenes, leaving the developer
with the only task of implementing each agent’s internal logic. As
agents modify the knowledge graph and subsequently actuate the real
world autonomously once active, it is important to make sure they
behave as expected. In this regard, unit and integration tests are pro-
vided to help with responsible development. For instance, the inte-
gration tests in folder RxnOptGoalAgent/tests simulate the behaviour
of distributed SDLs to verify that the data ﬂows are as expected upon
goal request from scientists. Detailed descriptions of tests for each
agent can be found in section A.2 of the Supplementary Information.

Distributed deployment. Taking inspiration from remote control
practices in lab automation71–73, the knowledge graph is designed to
span across the internet. It follows deployment practices commonly
used by cloud-native applications and is implemented through docker
containers. The triplestore and ﬁle server containing the knowledge
statements are deployed at internet-resolvable locations. Depending
on capabilities, agents are located at different host machines. Those
who monitor and control the hardware are deployed in the corre-
sponding laboratory for security reasons. They transmit data collected
from the hardware to the knowledge graph and in reverse conﬁgure
and actuate the equipment when a new experiment arises. At start-up,
agents register their OntoAgent instances in the knowledge graph,
then act autonomously should tasks be assigned to them. Altogether,
these agents form a distributed network that facilitates the transfer of
information within the knowledge graph and bridges cyberspace and
the physical world.

Flow chemistry platforms
This work connects two similar automated ﬂow chemistry platforms
located in Cambridge and Singapore. The method of sourcing input
chemicals differs, with a liquid handler employed in Cambridge and
reagent bottles utilised in Singapore. We provide below brief
descriptions of the experimental setup. All chemicals were used as
received.

acetonitrile running at a rate of 2 mL min−1. All compounds are
detected at an absorption wavelength of 254 nm.

Singapore lab. On the Singapore side, the experimental setup consists
of two Vapourtec R2 pump modules, one Vapourtec R4 reactor mod-
ule, one 6-port 2-position VICI switch valve equipped with 60 nL
sampling rotor, and an Agilent 1260 Inﬁnity II system equipped with a
G1311B quaternary pump, Eclipse XDB-C18 column (Agilent product
number: 961967-302), and G1314F variable wavelength detector
(VWD). The input chemical for the reaction is sourced from three
reagent bottles that are directly attached to the Vapourtec pumps:
pump A contains 0.5 M benzaldehyde 1 in acetonitrile (with 0.05 M
naphthalene as an internal standard), pump B contains 6.73 M acetone
2 in acetonitrile (50% v/v in acetonitrile), and pump C contains 0.1 M
NaOH 3 in ethanol. The following HPLC quaternary pump method for
online HPLC is used: the initial mobile phase was a 5:95 (v/v) binary
mixture of acetonitrile and water ﬂowing at 0.2 mL min−1. Immediately
after sample injection, the ﬂow rate and ratio of acetonitrile to water
were steadily changed to 1 mL min−1 and 95:5 (v/v) during the ﬁrst
5 min. At a ﬂow rate of 1 mL min−1, the binary mixture ratio is then
returned to 5:95 (v/v) acetonitrile:water over 1.5 min in a linear gra-
dient. This binary mixture ratio is held constant at 1 mL min−1 for the
next 1.5 min, after which the analysis is complete (after a total of 8 min),
and the method returns to a ﬂow rate of 0.2 mL min−1. The VWD
wavelength was changed over the 8 min analysis time as follows: the
absorption wavelength is 248 nm for the initial 6.05 min and then
switched to 228 nm until the end of acquisition.

Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.

Data availability
Research data generated in this study has been deposited in the Uni-
versity of Cambridge data repository under accession code https://doi.
org/10.17863/CAM.9705874. Source data are provided with this paper.
The tabular format of relevant experimental results that were dis-
played in Fig. 6 is provided in the Source Data XLSX ﬁle. Source data
are provided with this paper.

repository

Code availability
All the codes developed are publicly available on The World
Avatar GitHub
https://github.com/cambridge-cares/
TheWorldAvatar or the Zenodo repository at https://doi.org/10.5281/
zenodo.1015123675. The docker images of agents are available at
GitHub’s public registry located at ghcr.io/cambridge-cares/:
doe_agent:1.2.0, vapourtec_schedule_agent:1.2.0, vapourtec_agent:1.2.
0, hplc_agent:1.2.0, hplc_postpro_agent:1.2.0, rxn_opt_goal_iter_agent:
1.2.0, and rxn_opt_goal_agent:1.0.0. The deployment instructions can
be found in folder TheWorldAvatar/Deploy/pips.

Cambridge lab. On the Cambridge side, the experimental setup
consists of two Vapourtec R2 pump modules, one Vapourtec R4
reactor module, one Gilson GX-271 liquid handler, one four-way VICI
switching valve (CI4W.06/.5 injector), and Shimadzu CBM-20A
HPLC analytical equipment equipped with Eclipse XDB-C18 column
(Agilent part number: 993967-902). To initiate the reaction, the
liquid handler dispenses a 2 mL solution of 0.5 M benzaldehyde 1
dissolved in acetonitrile (with 0.06 M biphenyl as an internal stan-
dard) into the sample loop of pump A. Acetone 2 (50% v/v in acet-
onitrile) and 0.1 M NaOH 3 in ethanol are similarly loaded into
sample loops for pump B and C. After being transferred by the
switching valve, the product (benzylideneacetone 4) is analysed
using online HPLC. The HPLC analysis lasts 17 min, with a mobile
phase consisting of an 80:20 (v/v) binary mixture of water and

References
1.

Häse, F., Roch, L. M. & Aspuru-Guzik, A. Next-generation experi-
mentation with self-driving laboratories. Trends Chem. 1,
282–291 (2019).

2. Abolhasani, M. & Kumacheva, E. The rise of self-driving labs in

chemical and materials sciences. Nat. Synth. 2, 483–492 (2023).

3. Merriﬁeld, R. B., Stewart, J. M. & Jernberg, N. Instrument for auto-

mated synthesis of peptides. Anal. Chem. 38, 1905–1914 (1966).
4. Coley, C. W. et al. A robotic platform for ﬂow synthesis of organic

5.

compounds informed by AI planning. Science 365,
eaax1566 (2019).
Steiner, S. et al. Organic synthesis in a modular robotic system
driven by a chemical programming language. Science 363,
eaav2211 (2019).

Nature Communications | 

(2024) 15:462 

11


Article

https://doi.org/10.1038/s41467-023-44599-9

6.

Burger, B. et al. A mobile robotic chemist. Nature 583,
237–241 (2020).

8.

7. Chatterjee, S., Guidi, M., Seeberger, P. H. & Gilmore, K. Automated
radial synthesis of organic molecules. Nature 579, 379–384 (2020).
Tabor, D. P. et al. Accelerating the discovery of materials for clean
energy in the era of smart automation. Nat. Rev. Mater. 3,
5–20 (2018).
Zhu, Q. et al. An all-round AI-chemist with a scientiﬁc mind. Natl.
Sci. Rev. 9, nwac190 (2022).

9.

10. King, R. D. et al. The automation of science. Science 324,

85–89 (2009).

28. Schäfer, B. Data exchange in the laboratory of the future – a glimpse
at AnIML and SiLA (2018) https://doi.org/10.1002/gitlab.17270/full/.
accessed 30 May 2023.

29. Mitchell, S. N. et al. FAIR data pipeline: provenance-driven data
management for traceable scientiﬁc workﬂows. Philos. Trans. R.
Soc. A 380, 20210300 (2022).

30. Statt, M. J. et al. The materials experiment knowledge graph. Digital

Discov. 2, 909–914 (2023).

31. Menon, A., Krdzavac, N. B. & Kraft, M. From database to knowledge

graph-using data in chemistry. Curr. Opin. Chem. Eng. 26,
33–37 (2019).

11. Elder, S. et al. Cross-platform Bayesian optimization system for
autonomous biological assay development. SLAS Technol. 26,
579–590 (2021).

32. Bai, J. et al. From platform to knowledge graph: evolution of

laboratory automation. JACS Au 2, 292–309 (2022).

33. Hogan, A. et al. Knowledge graphs. ACM Comput. Surv. 54,

12. Yang, H. et al. Automatic strain sensor design via active learning and

1–37 (2022).

data augmentation for soft machines. Nat. Mach. Intell. 4,
84–94 (2022).

13. Stach, E. et al. Autonomous experimentation systems for materials

development: a community perspective. Matter 4,
2702–2726 (2021).

14. Delgado-Licona, F. & Abolhasani, M. Research acceleration in self-
driving labs: technological roadmap toward accelerated materials
and molecular discovery. Adv. Intell. Syst. 5, 2200331 (2022).

34. Akroyd, J., Mosbach, S., Bhave, A. & Kraft, M. Universal Digital
Twin - A Dynamic Knowledge Graph. Data-Centric Eng. 2,
e14 (2021).

35. Lim, M. Q., Wang, X., Inderwildi, O. & Kraft, M. The World Avatar – A
World Model for Facilitating Interoperability. in Intelligent Dec-
arbonisation: Can Artiﬁcial Intelligence and Cyber-Physical Systems
Help Achieve Climate Mitigation Targets?, 39–53 (Springer Inter-
national Publishing, 2022).

15. Leins, D. A., Haase, S. B., Eslami, M., Schrier, J. & Freeman, J. T.

36. Rihm, S. D. et al. The Digital Lab Framework as Part of The World

Collaborative methods to enhance reproducibility and accelerate
discovery. Digital Discov. 2, 12–27 (2023).

Avatar Preprint at https://como.ceb.cam.ac.uk/preprints/
314/ (2023).

16. Seifrid, M., Hattrick-Simpers, J., Aspuru-Guzik, A., Kalil, T. & Cran-

37. Kondinski, A., Bai, J., Mosbach, S., Akroyd, J. & Kraft, M. Knowledge

ford, S. Reaching critical MASS: crowdsourcing designs for the next
generation of materials acceleration platforms. Matter 5,
1972–1976 (2022).

engineering in chemistry: from expert systems to agents of crea-
tion. Acc. Chem. Res. 56, 128–139 (2023).

38. Kitano, H. Nobel turing challenge: creating the engine for scientiﬁc

17. Ren, Z., Ren, Z., Zhang, Z., Buonassisi, T. & Li, J. Autonomous
experiments using active learning and AI. Nat. Rev. Mater. 8,
563–564 (2023).

18. Sanders, L. M. et al. Biological research and self-driving labs in deep
space supported by artiﬁcial intelligence. Nat. Mach. Intell. 5,
208–219 (2023).

19. Pyzer-Knapp, E. O. et al. Accelerating materials discovery using

artiﬁcial intelligence, high performance computing and robotics.
npj Comput. Mater. 8, 84 (2022).

20. Coley, C. W., Eyke, N. S. & Jensen, K. F. Autonomous discovery in the
chemical sciences Part II: outlook. Angew. Chem. Int. Ed. 59,
23414–23436 (2020).

21. Wilbraham, L., Mehr, S. H. M. & Cronin, L. Digitizing chemistry using
the chemical processing unit: from synthesis to discovery. Acc.
Chem. Res. 54, 253–262 (2021).

22. Wilkinson, M. D. et al. The FAIR guiding principles for scientiﬁc data

management and stewardship. Sci. Data 3, 160018 (2016).
23. Roch, L. M. et al. ChemOS: orchestrating autonomous experi-

mentation. Sci. Robot. 3, eaat5559 (2018).

discovery. npj Syst. Biol. Appl. 7, 1–12 (2021).

39. Coley, C. W., Eyke, N. S. & Jensen, K. F. Autonomous discovery in the
chemical sciences part I: progress. Angew. Chem. Int. Ed. 59,
22858–22893 (2020).

40. Taylor, C. J. et al. A brief introduction to chemical reaction optimi-

zation. Chem. Rev. 123, 3089–3126 (2023).

41. Yoo, A. B., Jette, M. A. & Grondona, M. SLURM: Simple Linux Utility
for Resource Management. in Job Scheduling Strategies for Parallel
Processing, 44–60 (Springer Berlin Heidelberg, 2003).
42. Bai, J. et al. A derived information framework for a dynamic

knowledge graph and its application to smart cities. Future Gener.
Comput. Syst. 152, 112–126 (2024).

43. Holland, I. & Davies, J. A. Automation in the life science research

laboratory. Front. Bioeng. Biotechnol. 8, 571777 (2020).

44. Rao, A. S. & Georgeff, M. P. Modeling rational agents within a BDI-
Architecture. in Proceedings of the Second International Conference
on Principles of Knowledge Representation and Reasoning, KR’91,
473-484 (Morgan Kaufmann Publishers Inc., San Francisco, CA,
USA, 1991).

24. Pendleton, I. M. et al. Experiment Speciﬁcation, Capture and

45. Stein, H. S. & Gregoire, J. M. Progress and prospects for accel-

Laboratory Automation Technology (ESCALATE): a software pipe-
line for automated chemical experimentation and data manage-
ment. MRS Commun. 9, 846–859 (2019).

25. Rahmanian, F. et al. Enabling modular autonomous feedback-loops
in materials science through hierarchical experimental laboratory
automation and orchestration. Adv. Mater. Interfaces 9,
2101987 (2022).

erating materials science with automated and autonomous work-
ﬂows. Chem. Sci. 10, 9640–9649 (2019).

46. Krämer, M., Würz, H. M. & Altenhofen, C. Executing cyclic scientiﬁc

workﬂows in the cloud. J. Cloud Comput. 10, 1–26 (2021).
47. Morbach, J., Yang, A. & Marquardt, W. OntoCAPE - a large-scale

ontology for chemical process engineering. Eng. Appl. Artif. Intell.
20, 147–161 (2007).

26. Mehr, S. H. M., Craven, M., Leonov, A. I., Keenan, G. & Cronin, L. A

48. Kearnes, S. M. et al. The open reaction database. J. Am. Chem. Soc.

universal system for digitization and automatic execution of the
chemical synthesis literature. Science 370, 101–108 (2020).
27. Hein, J., Rauschen, R., Guy, M. & Cronin, L. Universal chemical

143, 18820–18826 (2021).

49. Pistoia Alliance. Uniﬁed Data Model (2020) https://github.com/

PistoiaAlliance/UDM. accessed 30 May 2023.

programming language for robotic synthesis reproducibility
research square platform LLC. https://doi.org/10.21203/rs.3.rs-
2761997/v1 (2023).

50. Daniele, L., Garcia-Castro, R., Lefrançois, M. & Poveda-Villalon, M.
SAREF: The Smart Applications REFerence ontology (2020) https://
saref.etsi.org/core/v3.1.1/. Accessed 21 Feb 2023.

Nature Communications | 

(2024) 15:462 

12


Article

https://doi.org/10.1038/s41467-023-44599-9

51.

Jeraal, M. I., Sung, S. & Lapkin, A. A. A machine learning-
enabled autonomous ﬂow chemistry platform for process
optimization of multiple reaction metrics. Chem. Methods 1,
71–77 (2021).

52. Park, J. S., Hu, P., Lin, Y. & Reinsalu, L. A. Composition and Method
for Preventing, Reducing, Alleviating or Treating Idiopathic Vomit-
ing (2020) https://testpubchem.ncbi.nlm.nih.gov/patent/US-
10548935-B2. US Patent 10,548,935. Accessed 11 Feb 2023.
53. Quek, H. Y. et al. BIM-GIS Integration: Knowledge Graphs in a World
of Data Silos Preprint at https://como.ceb.cam.ac.uk/preprints/
311/ (2023).

54. Dreyer, J. A. et al. Digitalisering af Forskning og Undervisning på

DTU Kemiteknik. Dan. Kemi 104, 6–11 (2023).

74. Bai, J. et al. Research data supporting “A Dynamic Knowledge

Graph Approach to Distributed Self-Driving Laboratories”. Apollo -
University of Cambridge Repository https://doi.org/10.17863/CAM.
97058 (2023).

75. Bai, J. et al. A Dynamic Knowledge Graph Approach to Distributed
Self-Driving Laboratories. Zenodo https://doi.org/10.5281/zenodo.
10151236 (2023).

76. Sim, M. et al. ChemOS 2.0: An Orchestration Architecture for

Chemical Self-Driving Laboratories Preprint at https://doi.org/10.
26434/chemrxiv-2023-v2khf (2023).

77. Huber, S. P. et al. AiiDA 1.0, a Scalable Computational Infrastructure
for Automated Reproducible Workﬂows and Data Provenance. Sci.
Data 7, 300 (2020).

55. Pascazio, L. et al. Chemical species ontology for data integration

78. Django Developers. Web APIs for Django (2023) https://github.

and knowledge discovery. J. Chem. Inf. Model. 63,
6569–6586 (2023).

com/encode/django-rest-framework accessed 19 October 2023.

79. FastAPI Developers. FastAPI Framework (2023) https://github.com/

56. Bradford, E., Schweidtmann, A. M. & Lapkin, A. Efﬁcient multi-
objective optimization employing gaussian processes, spectral
sampling and a genetic algorithm. J. Glob. Optim. 71,
407–438 (2018).

tiangolo/fastapi accessed 9 October 2023.

80. Rohrbach, S. et al. Digitization and validation of a chemical synth-

esis literature. Science 377, 172–180 (2022).

81. Agnihotri, A. & Batra, N. Exploring bayesian optimization. Dis-

57. Shields, B. J. et al. Bayesian reaction optimization as a tool for

till (2020).

chemical synthesis. Nature 590, 89–96 (2021).

58. von Rueden, L. et al. Informed machine learning - a taxonomy and
survey of integrating prior knowledge into learning systems. IEEE
Trans. Knowl. Data Eng. 35, 614–633 (2021).

59. Calvanese, D. et al. Ontop: answering SPARQL queries over rela-

tional databases. Semant. Web 8, 471–487 (2016).
60. OPC Foundation. Uniﬁed Architecture (2023) https://

opcfoundation.org/about/opc-technologies/opc-ua/ accessed 8
March 2023.

61. Pistoia Alliance. Update from the Pistoia Alliance’s Methods Hub
Project (2022) https://www.pistoiaalliance.org/methods/april-
2022-methods-database-hplc-uv-methods/ accessed 10 Feb 2023.

62. Christensen, M. et al. Automation isn’t automatic. Chem. Sci. 12,

15473–15490 (2021).

63. Staab, S. & Studer, R. Handbook on Ontologies (Springer Science &

Business Media, 2010).

64. Kondinski, A. et al. Automated rational design of metal–organic

polyhedra. J. Am. Chem. Soc. 144, 11713–11728 (2022).

65. Guo, J. et al. Automated chemical reaction extraction from scien-

tiﬁc literature. J. Chem. Inf. Model. 62, 2035–2045 (2021).
66. Felton, K. C., Rittig, J. G. & Lapkin, A. A. Summit: benchmarking

machine learning methods for reaction optimisation. Chem. Meth-
ods 1, 116–122 (2021).

67. Plutschack, M. B., Pieber, B., Gilmore, K. & Seeberger, P. H. The

Hitchhiker’s guide to ﬂow chemistry. Chem. Rev. 117,
11796–11893 (2017).

68. Garud, S. S., Karimi, I. A. & Kraft, M. Design of computer experi-
ments: a review. Comput. Chem. Eng. 106, 71–95 (2017).

69. Clayton, A. D. et al. Algorithms for the self-optimisation of chemical

reactions. React. Chem. Eng. 4, 1545–1554 (2019).

70. Zhou, X., Eibeck, A., Lim, M. Q., Krdzavac, N. B. & Kraft, M. An agent
composition frramework for the J-Park simulator - a knowledge
graph for the process industry. Comput. Chem. Eng. 130,
106577 (2019).

71. Fitzpatrick, D. E., Maujean, T., Evans, A. C. & Ley, S. V. Across-the-

world automated optimization and continuous-ﬂow synthesis of
pharmaceutical agents operating through a Cloud-Based Server.
Angew. Chem. Int. Ed. 57, 15128–15132 (2018).

72. Ramírez, J. et al. A virtual laboratory to support chemical reaction

engineering courses using real-life problems and industrial soft-
ware. Educ. Chem. Eng. 33, 36–44 (2020).

73. CMU Cloud Lab (2023) https://cloudlab.cmu.edu/ accessed 12

May 2023.

Acknowledgements
This research was supported by the National Research Foundation,
Prime Minister’s Ofﬁce, Singapore, under its Campus for Research
Excellence and Technological Enterprise (CREATE) programme, and
Pharma Innovation Platform Singapore (PIPS) via grant to CARES Ltd
“Data2Knowledge, C12”. This project was cofunded by European
Regional Development Fund via the project “Innovation Centre in Digital
Molecular Technologies”, UKRI via project EP/S024220/1 “EPSRC Centre
for Doctoral Training in Automated Chemical Synthesis Enabled by
Digital Molecular Technologies”. Part of this work was also supported by
Towards Turing 2.0 under the EPSRC Grant EP/W037211/1. The authors
thank Dr. Andrew C. Breeson for his helpful suggestions on graphical
design. J.B. acknowledges ﬁnancial support provided by CSC Cam-
bridge International Scholarship from Cambridge Trust and China
Scholarship Council. C.J.T. is a Sustaining Innovation Postdoctoral
Research Associate at Astex Pharmaceuticals and thanks Astex Phar-
maceuticals for funding, as well as his Astex colleagues Chris Johnson,
Rachel Grainger, Mark Wade, Gianni Chessari, and David Rees for their
support. S.D.R. acknowledges ﬁnancial support from Fitzwilliam Col-
lege, Cambridge, and the Cambridge Trust. M.K. gratefully acknowl-
edges the support of the Alexander von Humboldt Foundation. For the
purpose of open access, the author has applied a Creative Commons
Attribution (CC BY) licence to any Author Accepted Manuscript version
arising.

Author contributions
M.K., A.A.L., J.B. and S.M. conceived the project. J.B., S.M. and M.K.
designed the ontological representation and agent workﬂow. J.B.
implemented the ontologies/agents and deployed the knowledge
graph under the advisement of S.M. and K.F.L. The chemistry and
HPLC method were developed by C.J.T. (Cambridge) and D.K. (Sin-
gapore). D.K. and C.J.T. validated the calculation of objective func-
tions. The self-optimisation campaign involving two labs was set up
by C.J.T. (hardware and chemicals in Cambridge), D.K. (hardware and
chemicals in Singapore) and J.B. (software on both sides and goal
request). M.K. and A.A.L. acquired funding and administrated the
project. J.B. draughted the body of this manuscript and SI with inputs
from S.M., J.A., S.D.R. and C.J.T. All authors provided feedback on the
manuscript.

Competing interests
The authors declare no competing interests.

Nature Communications | 

(2024) 15:462 

13


Article

https://doi.org/10.1038/s41467-023-44599-9

Additional information
Supplementary information The online version contains
supplementary material available at
https://doi.org/10.1038/s41467-023-44599-9.

Correspondence and requests for materials should be addressed to
Markus Kraft.

Peer review information Nature Communications thanks Martin Seifrid,
and the other, anonymous, reviewer(s) for their contribution to the peer
review of this work. A peer review ﬁle is available.

Reprints and permissions information is available at
http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons license, and indicate if
changes were made. The images or other third party material in this
article are included in the article’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons license and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this license, visit http://creativecommons.org/
licenses/by/4.0/.

© The Author(s) 2024

Nature Communications | 

(2024) 15:462 

14
