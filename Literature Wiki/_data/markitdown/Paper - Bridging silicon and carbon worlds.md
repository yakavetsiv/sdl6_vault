---
type: literature-note
source_note: "Papers/Paper - Bridging silicon and carbon worlds.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Akbarialiabad-2024-Bridging-silicon-and-carbon-worlds-.pdf"
converter: "microsoft/markitdown"
---
npj | systems biology and applications

Perspective

Published in partnership with the Systems Biology Institute

Bridging silicon and carbon worlds with
digital twins and on-chip systems in drug
discovery

https://doi.org/10.1038/s41540-024-00476-9

Hossein Akbarialiabad1,2,3, Mahdiyeh Sadat Seyyedi
Alireza Haghighi7,8,9 & Joseph C. Kvedar10

4, Shahram Paydar5, Adrina Habibzadeh6,

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

This perspective discusses the convergence of digital twin (DT) technology and on-the-chip systems
as pivotal innovations in precision medicine, substantially advancing drug discovery. DT leverages
extensive health data to create dynamic virtual patient models, enabling predictive insights and
optimized treatment strategies. Concurrently, on-the-chip systems from the Carbon world replicate
human biological processes on microﬂuidic platforms, providing detailed insights into disease
mechanisms and pharmacological interactions. The convergence of these technologies promises to
revolutionize drug development by enhancing therapeutic precision, accelerating discovery timelines,
and reducing costs. Speciﬁcally, it assesses their role in drug development, from reﬁning therapeutic
precision to expediting discovery timelines and reducing the ﬁnal price. Nevertheless, integrating
these technologies faces challenges, including data collection and privacy concerns, technical
intricacies, and clinical adoption barriers. This manuscript argues for interdisciplinary cooperation to
navigate these challenges, positing DTs and on-the-chip technologies as foundational elements in
personalized healthcare and drug discovery.

Background
The realm of precision medicine − the new term for personalized medicine1
− is witnessing a monumental shift with the emergence of digital twin (DT)
technology and on-the-chip systems. This conﬂuence represents a sig-
niﬁcant leap towards a future where healthcare is not only customized to the
individual’s genetic and environmental context but also predictive and
precision-driven. This perspective delves into the implications of these
technologies for drug discovery, a ﬁeld poised to beneﬁt immensely from
such advancements.

Digital twin technology: revolutionizing patient-speciﬁc
treatment
Generally, DT technology refers to creating virtual models that replicate
real-world entities, systems, or processes using real-time data. These
digital replicas enable simulations and predictions by continuously
updating and synchronizing with their physical counterparts. Biomedical

DTs are precise digital replicas of biological systems that aim to model
complex biological processes across various scales, from molecules to
entire organs2. These virtual models integrate diverse datasets, encom-
passing multi-omics data, environmental exposures, and real-time phy-
siological data, to dynamically mirror and predict individual health
outcomes and treatment responses. In the context of drug discovery, DTs
serve as a powerful tool for simulating drug interactions at the molecular
level, predicting potential side effects, and assessing efﬁcacy before clinical
trials. This reduces the time and cost associated with bringing new drugs to
market. By creating patient-speciﬁc DT, healthcare providers can simulate
how different treatment options would affect an individual, leading to
more accurate and effective personalized treatment plans, marking a
departure from the one-size-ﬁts-all paradigm. Pharmaceutical companies
can use DTs to generate data required for regulatory submissions,
potentially replacing some in vivo studies with in silico trials, and speeding
up the approval process for new therapies3,4.

1St George and Sutherland Clinical School, University of New South Wales, Sydney, NSW, Australia. 2Nuvance Global Health Program, CT, USA. 3American
Canadian Medical School, Portsmouth, Dominica. 4Burn and wound healing research center, Amiralmomenin Hospital, Shiraz University of Medical Sciences,
Shiraz, Iran. 5Department of Surgery, Shiraz University of Medical Sciences, Shiraz, Iran. 6Department of Neurosurgery, Fasa University of Medical Sciences,
Fasa, Iran. 7Department of Genetics, Harvard Medical School, Boston, MA, USA. 8The Broad Institute of MIT and Harvard, Cambridge, MA, USA. 9Department of
Medicine, Brigham and Women’s Hospital and Harvard Medical School, Boston, MA, USA. 10Department of Dermatology, Harvard Medical School, Boston, MA,
USA.

e-mail: jkvedar@mgb.org

npj Systems Biology and Applications |

 (2024) 10:150

1

https://doi.org/10.1038/s41540-024-00476-9

Perspective

As of now, various companies have reported establishing several DT
models of single-cells5,6, some bioprocesses like cell culture7, organs8–10, and
even the cardiovascular system11,12. For instance, the Living Heart Project10
represents a groundbreaking initiative in using DT technology to advance
cardiovascular science. The project focuses on creating a highly detailed
virtual model of a human heart, referred to as the Living Heart Human
Model, that can simulate various physical and biological processes of the
heart, including electrical activity, blood ﬂow, and tissue mechanics. It aims
to revolutionize how heart-related medical devices are developed and tested,
using these simulations to predict how new devices interact with the human
heart. However, this project has some limitations in mimicking the human
heart function completely, including a lack of heterogeneity between cells’
response to electrical conduction, poor parameter identiﬁcation for muscle
contraction, and employing a simpliﬁed ﬂuid resistance model. Another
example is the skin DT which mimics the skin barrier function and is
beneﬁcial
research, especially transdermal drug
delivery13,14. Additionally, several DT projects have been launched for cancer
research and personalized treatment approaches15,16. However, these are
mainly available as commercial offerings with limited methodological
details that are publicly accessible17. It should be noted that although it has
potential in medicine and health care, the use of this technology is still in its
infancy18. The development and implementation of digital twins in bio-
face signiﬁcant challenges. Therefore,
medicine still
to
acknowledge that current DT models, despite their capabilities, cannot fully
replicate the complexity of biological systems and are replicas of a small part
of their whole functions. For instance, DeepLife and Turbine both report
they established DTs of single cells, but their models incorporate multi-
omics data to replicate and analyze cell pathways related to drug response5,6.
Possible reasons for this include difﬁculties in collecting data, technical
hurdles, interdisciplinary collaboration and funding challenges, and ethical
issues3. However, ongoing advancements in the ﬁeld continue to push the
boundaries of what DTs can achieve.

in pharmaceutical

is crucial

it

On-the-chip systems: bridging the gap between bench
and bedside
On-the-chip technologies, encompassing cell-on-the-chip, organ-on-the-
chip, and human-on-the-chip, refer to physical microﬂuidic devices
designed to mimic the biological and physiological functions of cells, tissues,
or organ systems in a controlled environment19. These technologies allow
for precise control and observation of biological processes, offering insights
into disease mechanisms and drug responses and providing scalable and
ethically viable alternatives to animal testing20,21. Scientists struggle to
overcome on-the-chip technology challenges and boost its applications.
One of the most critical hurdles is vascularization, which involves devel-
oping a universal medium with all nutrients and growth factors for various
cell types to mimic blood22. Now, with the help of multi-omics and DTs, it is
possible to create a single medium containing all the necessary nutrients and
growth factors for various cell types. By using the genome-scale metabolic
model (GEM), we can visualize global networks of metabolic pathways and
identify crucial bioreactions and components for all the involved cells23.
Maintaining cellular interactions over extended periods is another chal-
lenge. DT models could potentially address this by simulating the precise
nutrient ﬂow necessary to sustain cell cultures within these systems. This
allows researchers to predict and prevent issues before they arise24. Another
critical obstacle to industrializing the technology is the lack of a standard
manufacturing protocol. This not only hinders large-scale and cost-effective
production but impedes the process of drug testing22,25. For on-chip systems,
a standard manufacturing protocol heavily relies on designing and con-
ducting thousands of experiments to identify the most suitable components
(i.e., biomaterials, biosensors, or living cells) that bring the most promising
results26. It is evident that one of the most advantageous aspects of DTs is
their rapid processing ability. As a result, we can simulate hundreds of
experiments in a virtual environment and analyze the results in a shorter
time frame. Additionally, Some key factors that affect the reliability of on-
chip results, including real-time monitoring, considering genomic diversity,

and incorporating mechanical forces like shear stress, are largely absent
from the on-chip technologies currently available24,27. However, these issues
could be overcome by integrating DT technology as it can use the results
from the on-chip experiment, evaluate the effect of other factors on them,
and provide us more precise and realistic outcomes.

(cid:129) Cell-on-the-Chip: These tools are designed to mimic the behavior and
interactions of cells within a controlled micro-environment. By
providing a platform for studying cellular responses to various stimuli,
cell-on-the-chip technology plays a crucial role in uncovering
fundamental disease mechanisms and screening potential therapeutic
agents at the cellular level. Besides routine topics, cell-on-the-chips are
unique choices for extreme environment and aerospace medical
research since scientists can mimic extreme temperature and
microgravity conditions through them28.

(cid:129) Organ-on-the-Chip: This represents a more sophisticated approach
where speciﬁc organ functions are replicated on microﬂuidic chips.
Organ-on-the-chip systems offer a detailed view of how organs
respond to drugs, toxins, and other treatments, bridging the gap
between insights gained at the cellular level and their implications for
organ health and function. This technology holds immense promise for
advancing our understanding of organ-speciﬁc diseases and develop-
ing targeted therapies. Organ-on-chip technology offers greater clinical
relevance when compared to traditional two-dimensional single-cell or
cell-line biology models. This was highlighted in a 2017 study
conducted by AstraZeneca, which assessed 110 compounds for drug-
induced liver injury24,29. The EVATAR is a groundbreaking 3D organ-
on-a-chip platform designed to simulate the female reproductive
system and liver, replicating the human 28-day menstrual cycle
through hormone regulation. The EVATAR is valuable for research on
fertility, hormonal drug interactions, and diseases like cervical cancer
and endometriosis. It also supports drug development, toxicological
studies, and advances in contraception and infertility treatments by
enabling controlled,
in-depth analysis of single and multi-tissue
interactions30.

(cid:129) Human-on-the-Chip: As

the most comprehensive application,
human-on-the-chip models could integrate data from multiple cellular
and organ chips to simulate a holistic version of the physiological
system of the human body. These systems can replicate the genetic and
phenotypic variations seen in humans, enabling the prediction of
holistic simulations of health outcomes, disease progression, and
treatment efﬁcacy personalized to individual patients. This innovation
aims to enhance patient care, minimize adverse drug effects, and
improve healthcare efﬁciency. Additionally, human-on-chip platforms
provide a more accurate and cost-effective alternative to traditional
animal models in drug testing and toxicity assessments, addressing key
challenges in the pharmaceutical industry31,32.

Optimizing interaction for enhanced medical insights
Integrating DTs and on-chip systems advances precision medicine. While
ML algorithms enhance DT predictions, DTs can also use rule-based or
hybrid approaches. The accuracy of these models depends on the quality
and relevance of input data. Collecting such data is costly and time-con-
suming, so on-chip systems, capable of mimicking real-world processes
efﬁciently, are critical for reﬁning DT models. According to these, we suggest
an integration of on-the-chip technologies and DTs to create a feedback
loop that enriches both domains (Fig. 1), ensures efﬁcient use of resources,
and maximizes the potential for discovery and innovation:

(cid:129) From Chip to DT: Data generated from on-the-chip experiments
provide real-world insights that validate and reﬁne DT models’
assumptions and algorithms. This empirical foundation enhances the
accuracy of digital simulations,
improving predictive power and
reliability.

(cid:129) From DT to Chip: Conversely, DTs can identify potential biological
interactions and treatment outcomes that may not be readily apparent,
guiding the design and focus of on-the-chip experiments.

npj Systems Biology and Applications |

 (2024) 10:150

2

https://doi.org/10.1038/s41540-024-00476-9

Perspective

Fig. 1 | Intricate associations between the different levels of human, digital twins,
and on-chip technologies. The diagram illustrates the complex and interconnected
relationships between different biological levels, from organelles to the human body
as a whole, and their associated digital twins (DTs) and on-chip technologies. These
connections are crucial for advancing drug discovery, as integrating DTs with on-
chip systems allows for more precise and efﬁcient simulations and experiments. The

arrows in the diagram emphasize the dynamic interaction between these biological
levels, their DT counterparts, and the on-chip systems. This integration creates a
feedback loop, where insights gained from DTs inform on-chip experiments, and
ﬁndings from these experiments, in turn, reﬁne the DT models. This continuous
process optimizes resource utilization, accelerates discoveries, and drives innovation
in drug development.

Through these years, several companies and research groups have
made some advancements in relatively integrating DTs and on-the-chip
technologies. In the case of drug development, the DigiLoCS framework
represents a signiﬁcant advancement in predictive pharmacokinetics.
DigiLoCS combines the detailed biological data from liver-on-chip systems
with sophisticated mathematical models to visually represent the liver’s drug
processing functions. DigiLoCS models complex biological processes, such
as drug metabolism, permeability, and partitioning, within the liver-on-chip
system, and it has been shown to outperform traditional methods in pre-
dicting human liver clearance. One of the main challenges in integrating
DTs with organ-on-chip systems is accurately modeling the complex
interactions within the liver. Traditional models often oversimplify these
processes, leading to signiﬁcant underprediction of drug clearance. This is
important because inadequate understanding of drug clearance can lead to
underdosing or toxicity33,34.

Individualized and precision medicine has also progressed at a fast
pace; for instance, DIGIPREDICT has established a model to assess
disease progression in COVID-19 patients and the need for early

intervention in case of serious complications. This technology uses
organ-on-the-chip to select the suitable biomarkers combination for
predicting cytokine storm by its early signs in high-risk patients. This
technology uses smart patches of nanosensors that analyze sweat to
detect biomarkers and send data to a smartphone35. While the DIGI-
PREDICT project has made commendable progress in integrating
digital
to
acknowledge that it has not yet produced groundbreaking outcomes.
The project is still developing, and signiﬁcant work remains to be done
before its full potential can be realized.

twin technology with clinical practice,

is important

Another area that beneﬁts from integrating DT technology and on-the-
chip systems is cancer therapy, which requires personalized treatment
approaches due to the variability in patient responses. Furthuremore, by
combining DTs with microﬂuidic platforms such as cancer on-a-chip and
radiopharmaceutical on-a-chip researchers can simulate and optimize
radiopharmaceutical therapy based on patient-speciﬁc data36. This inte-
gration allows for precise predictions of treatment outcomes, enabling tai-
lored therapy plans that improve effectiveness and reduce side effects.

it

npj Systems Biology and Applications |

 (2024) 10:150

3

https://doi.org/10.1038/s41540-024-00476-9

Perspective

Although even the DT concept is newfound in the healthcare era,
integrating it with other systems like on-the-chip technology and enhancing
its application is progressing expeditiously. Therefore, it is imaginable that
the early application of these technologies will probably be in the next few
years. However, the widespread clinical adoption of these technologies will
likely take longer, requiring signiﬁcant advancements in technology and
regulatory frameworks.

Potential areas of implementation in medicine

(cid:129) Catalyzed Pharmaceutical Development: DTs and on-the-chip
technologies enable the rapid screening of new medicinal compounds
without the ethical and logistical complexities of traditional testing
methods, including probable fatal unexpected adverse effects of new
drugs and drug toxicity. Additionally, the estimated time of bringing a
new drug to market is about 10 years and the attrition rate for drug
targets is as much as 96%. The convergence of these technologies is able
to choose compounds with a higher chance of effectiveness to enter the
trials and reduce time and costs2. However, employing these requires a
tremendous intellectual and ﬁnancial resource. One solution to solve
this problem is to collaborate with the pharmaceutical industry. As we
mentioned before, DigiLoCS can be a good example in this area33,34.
(cid:129) Personalized Treatment Regimens: Merging these two technologies
could potentially boost the feasibility of personalized medicine based
on individual models in carbon and silicon worlds. In this way, patients
are prescribed more effective drugs with lower doses and fewer side
effects which increases their treatment compliance and decreases the
burden on the health system37,38. For this area, the integrated model
developed by Abdollahi et al. is an example that helps cancer patients36.
(cid:129) Enhanced Disease Modeling: The combination of DTs with on-the-
chip systems allows for sophisticated disease modeling, facilitating a
deeper understanding of disease mechanisms and the identiﬁcation of
novel therapeutic targets. One potential model for the proposed
integrated technology is DIGIPREDICT. It aims to help early diagnosis
of COVID-19 complications and better understand the disease35.
(cid:129) Discontinued Animal Testing: Using animals for drug discovery has
always been an excellent debate for ethical and practical reasons. Fre-
quent failure of animal models to predict drug responses in humans
also puts their use in basic research in doubt19. In this case, the inte-
gration of DT and on-the-chip systems provides more precise and
realistic results and will impede animal testing and euthanization.

Model for application
As we mentioned before, any ﬁeld in medical research or health care system
has the potential to take its outcome quality to the next level of excellence
using DTs and on-the-chip technology integration. Here, we choose der-
matology merely as an example of broader implications and based on our
ﬁeld of interest and its unique challenges and direct impact on patient
quality of life to concretize this framework. Considering the application to
atopic dermatitis (AD), a complex skin condition characterized by
inﬂammation and barrier disruption, the steps for our simpliﬁed approach
would be:

(cid:129) Stage 1: Data Collection and Model Development: Developing a DT of
the AD patient’s skin by integrating genomic data, behavioral factors,
historical treatment responses, and current skin conditions. Simulta-
neously, creating a skin-on-the-chip model that replicates the AD-
affected skin environment.

(cid:129) Stage 2: Simulation and Experimentation: Simulate treatment
responses using the DTs, identifying potential therapeutic agents.
Experimenting with these agents on the skin-on-the-chip, observing
direct effects on skin barrier function and inﬂammatory markers.
(cid:129) Stage 3: Feedback and Reﬁnement: This step compares simulation and
experimentation results to identify discrepancies and reﬁnes the DT
model accordingly. It enhances the model’s predictive accuracy for
future treatments.

(cid:129) Stage 4: Clinical Application and Monitoring: Implementing and
testing the most promising treatments identiﬁed through the inte-
grated simulation-experimentation approach in clinical trials. Mon-
itoring patient outcomes via wearable technology and relevant medical
IoT (Internet of Things), using data to personalize the DT further and
adjust treatments as necessary.

Challenges and pathways to integration
Despite their promise, the path to integrating these technologies into clinical
practice and drug discovery is laden with hurdles:

(cid:129) Data Quality, Collection, and Management: As we mentioned before,
the strength of DTs is based on their structured data entry and their
underlying algorithm. Therefore, gathered data should be standardized
and reported digitally to facilitate comparability. Poor or missing data
can lead to improper predictions and recommendations. Also, studies
show DTs would exaggerate racial and other biases and reinforce
they trained with poor-quality data18.
healthcare inequalities if
Conversely, some human traits, such as thinking, reactions, and
behavior, are unpredictable and challenging to measure quantitatively.
Moreover, a suitable interface is needed to integrate multi-dimensional
information from various sources.

(cid:129) Data Privacy, Data Security, and Ethical Considerations: Managing
sensitive patient data and ensuring privacy and consent are paramount
concerns that require stringent regulatory frameworks. Patients need to
be conﬁdent about data security and transparency of use; otherwise,
these advanced technologies could cause mistrust in patients and
destroy physician-patient rapport.

(cid:129) Technical Complexity and Resource Intensity: The development and
maintenance of DT and on-the-chip models demand substantial
computational resources and expertize, calling for collaborative efforts
across disciplines and sectors. Current DTs mostly use ‘black box’ AI,
which makes it difﬁcult for healthcare providers to trust their
outcomes. Thus, there is a need for developing more models based
on interpretable algorithms.

(cid:129) Clinical Adoption, Regulatory Approval, and Financial Justiﬁcation:
innovation and clinical
Bridging the gap between technological
application involves navigating regulatory landscapes, adapting
healthcare infrastructures, and managing ﬁnancial burdens to
accommodate these new technologies. For instance, in adapting to
these new technologies, the FDA recently started the Medical Device
Development Tools (MDDT) program to prequalify AI models and
digital health tools and accelerate the approval process. In fact, due to
the complexity and multidisciplinary nature of these technologies,
regulatory frameworks have to use advisory committees consisting of
data scientists, healthcare professionals, and engineers39. In terms of
ﬁnancial justiﬁcation, although developing this cutting-edge technol-
ogy requires massive funding and investment, ultimately, it could
provide optimized care for patients and low ﬁnal costs for industries.
One main incentive for the industry section could be that the
convergence of DTs and on-the-chip systems results in accelerated
drug development and fewer discovered drugs failing in further clinical
trials. Additionally, personalized treatment approaches employ the
most valuable agents with the minimum optimal doses; consequently,
fewer drugs will be prescribed, and patient outcomes will improve.
(cid:129) Feasibility: Regardless of logistical challenges, dosage adjustment
would be required as there are differences between in vivo and in vitro
settings, even with the most precise modeling techniques.

Looking ahead: a future deﬁned by personalization
The integration of DT and on-the-chip technologies represents an evolution
and a revolution in precision medicine. These technologies can signiﬁcantly
improve outcomes for patients with intricate conditions by enabling more
precise, predictive, and patient-centered care. Although DT and on-the-chip
technologies still face several challenges for their wide application, their
integration can overcome shortcomings by providing a synergistic effect.

npj Systems Biology and Applications |

 (2024) 10:150

4

https://doi.org/10.1038/s41540-024-00476-9

Perspective

However, the integration process is challenging and fraught with various
obstacles, generally categorized as technology development and adoption
regulation. Data collection and management, technical hurdles in product
manufacturing, and the feasibility of clinical application are related to
technology development challenges. Developing a system for registering
and sorting standardized data is a principal and complex challenge, espe-
cially when dealing with multi-dimensional and divergent data sources. The
collected data must represent the entire human race to avoid racial biases.
Despite the assistance on-the-chip systems provide in collecting individual
data, training the DTs with general human information is still necessary to
generate more accurate predictions. Furthermore, developing a reliable DT
and manufacturing a detailed on-the-chip system is crucial for making the
proposed integrated technology feasible, and they require strong teamwork
among experts from different disciplines. On the other side, data privacy
and security, ethical considerations, clinical adoption, and regulatory
approvals are related to technology adoption regulation challenges. Data
privacy and security are fundamentals of any technology related to digital
health. In this case, the autonomy of the patients is crucial and technology
developers must carefully consider their consent while using their data.
Patients may not be willing to accept these technologies unless they are
conﬁdent about the transparency of usage and the security of their sensitive
health data. This is especially important for data used in drug discovery
research, as it has the potential to be misused for criminal purposes such as
bioterrorism. This is why regulatory agencies play a signiﬁcant role in the
safe clinical adoption of new technologies. They must scrutinize all aspects
of any new technology, identify potential pitfalls, and create proper laws.
The road ahead will undoubtedly require a concerted effort to address the
ethical, technical, and clinical challenges. However, the promise of deli-
vering treatments that are as unique as the individuals they aim to help is an
inspiring vision that drives the ﬁeld forward.

Conclusion
As we embrace these transformative technologies, it is clear that the future of
precision medicine and pharmaceutical development lies in our ability to
harness the full potential of digital twins and on-the-chip systems. This
journey, though complex, paves the way for a new era of healthcare, where
drug discovery is accelerated, treatments are demystiﬁed, and patient care is
profoundly personalized. The collaboration of scientists, clinicians, ethicists,
and policymakers will be crucial in realizing this future, ensuring that as we
advance, we do so with a commitment to improving patient outcomes,
ethical standards, and equitable access for all.

Received: 13 August 2024; Accepted: 25 November 2024;

References
1. Delpierre, C. & Lefèvre, T. Precision and personalized medicine: What

their current deﬁnition says and silences about the model of health
they promote. Implication for the development of personalized health.
Front. Sociol. 8, 1112159 (2023).
Akbarialiabad, H., Pasdar, A. & Murrell, D.F. Digital twins in dermatology,
current status, and the road ahead. npj Digit. Med. 7, 228 (2024).
3. Barros, M. T. et al. From multiscale biophysics to digital twins of

2.

tissues and organs: future opportunities for in-silico pharmacology.
IEEE Trans. Mol. Biolog. Multi-Scale Commun. https://doi.org/10.
48550/arXiv.2306.02369 (2024).
Laubenbacher, R., Mehrad, B., Shmulevich, I. & Trayanova, N. Digital
twins in medicine. Nat. Comput. Sci. 4, 184–191 (2024).

4.

5. Baptista, J. How digital twins of human cells are accelerating drug

discovery. Biopharma Dealmakers (2022). https://www.nature.com/
articles/d43747-022-00108-3 (accessed 2 Dec 2024).

6. Nagy, S. AI-powered cancer cell simulations will be used to identify
novel disease positioning strategies in Cancer Research UK’s latest
biotech partnership. Turbine (2023). https://turbine.ai/news/ai-

powered-cancer-cell-simulations-will-be-used-to-identify-novel-
disease-positioning-strategies-in-cancer-research-uks-latest-
biotech-partnership/ (accessed 2 Dec 2024).

7. Mauch, K. Insilico launches comprehensive portfolio of predictive

Digital Twins for cell culture process development. Insilico
Biotechnology (2019). https://www.insilico-biotechnology.com/
news/insilico-launches-comprehensive-portfolio-of-predictive-
digital-twins (accessed 2 Dec 2024).

8. Mansi, T. A Digital Twin of the Heart. Siemens (2019). https://www.

9.

siemens.com/global/en/company/about/history/specials/175-years/
digital-twin-of-the-heart.html (accessed 2 Dec 2024).
Lu, W. et al. Digital Twin Brain: a simulation and assimilation platform
for whole human brain. arXiv preprint arXiv:2308.01241, https://doi.
org/10.48550/arXiv.2308.01241 (2023).

10. Baillargeon, B., Rebelo, N., Fox, D. D., Taylor, R. L. & Kuhl, E. The living
heart project: a robust and integrative simulator for human heart
function. Eur. J. Mech.-A/Solids 48, 38–47 (2014).

11. Mantilla, D. et al. Clinical impact of Sim & Size® simulation software in
the treatment of patients with cerebral aneurysms with ﬂow-diverter
Pipeline stents. Interven. Neuroradiol. 29, 47–55 (2023).

12. Contarino, C., Chifari, F., D'Souza, G. A. & Herbertson, L. H. Validation
of a Multiscale Computational Model Using a Mock Circulatory Loop
to Simulate Cardiogenic Shock. ASAIO J. 69, e502–e512 (2023).
13. Gupta, R., Dwadasi, B. S., Rai, B. & Mitragotri, S. Effect of chemical
permeation enhancers on skin permeability: In silico screening using
molecular dynamics simulations. Sci. Rep. 9, 1–12 (2019).

14. Akbarialiabad, H. & Murrell, D. F. A new dawn for orphan diseases in
dermatology: The transformative potential of digital twins. J. Eur.
Acad. Dermatol. Venereol. 38, 2309–2310 (2024).

15. Stahlberg, E. A. et al. Exploring approaches for predictive cancer

patient digital twins: Opportunities for collaboration and innovation.
Front. Digit. Health. 4, 1007784, (2022).

16. Min, R. Researchers in Spain are creating ‘digital twins’ to treat breast
cancer. https://www.euronews.com/health/2023/12/05/researchers-
in-spain-are-creating-digital-twins-to-treat-breast-cancer (2023).

17. Bordukova, M., Makarov, N., Rodriguez-Esteban, R., Schmich, F. &
Menden, M. P. Generative artiﬁcial intelligence empowers digital twins
in drug discovery and clinical trials. Expert Opin. Drug Discov. 19,
33–42 (2024).

18. Voigt, I. et al. Digital twins for multiple sclerosis. Front. Immunol. 12,

19.

669811 (2021).
Ingber, D. E. Human organs-on-chips for disease modelling, drug
development and personalized medicine. Nat. Rev. Genet. 23,
467–491 (2022).

20. Teixeira Carvalho, D. J., Moroni, L. & Giselbrecht, S. Clamping strategies
for organ-on-a-chip devices. Nat. Rev. Mater. 8, 147–164 (2023).
21. Leung, C. M. et al. A guide to the organ-on-a-chip. Nat. Rev. Methods

Prim. 2, 33 (2022).

22. Srivastava, S. K., Foo, G. W., Aggarwal, N. & Chang, M. W. Organ-on-
chip technology: Opportunities and challenges. Biotechnol. Notes 5,
8–12 (2024).

23. Silberberg, Y. Development of Advanced Feed Media and Supplements
(Webcast Recap). https://www.bioprocessintl.com/cell-culture-media/
development-of-advanced-feed-media-and-supplements (2024).
24. Low, L. A., Mummery, C., Berridge, B. R., Austin, C. P. & Tagle, D. A.

Organs-on-chips: into the next decade. Nat. Rev. Drug Discov. 20,
345–361 (2021).

25. Norden, A. The Future of Organ on a Chip: Technical and Intellectual
Property Challenges. https://www.gje.com/resources/the-future-of-
organ-on-a-chip-technical-and-intellectual-property-challenges/#_
edn2 (2023).

26. Piergiovanni, M. et al. Organ on chip: building a roadmap towards

standardisation. Report No. JRC126163, (JRC126163 Joint Research
Centre (JRC) 2021).

npj Systems Biology and Applications |

 (2024) 10:150

5

https://doi.org/10.1038/s41540-024-00476-9

Perspective

27. Möller, J. & Pörtner, R. Digital twins for tissue culture techniques—

concepts, expectations, and state of the art. Processes 9, 447 (2021).
28. Vashi, A., Sreejith, K. R. & Nguyen, N.-T. Lab-on-a-chip technologies

for microgravity simulation and space applications. Micromachines
14, 116 (2023).

29. Bentwich, I. Pharma’s Bio-AI revolution. Drug Discov. Today 28,

Author contributions
H.A. conceived of the presented idea and made the initial draft. J.K., S.P.,
and A.H. expanded and developed the concept. H.A. and M.S. wrote the
manuscript. H.A., M.S., S.P., and A.H. edited the ﬁnal version. J.K.
supervised the whole work. Every contributor has read and approved the
ﬁnal version of the manuscript.

103515 (2023).

30. Xiao, S. et al. A microﬂuidic culture model of the human reproductive
tract and 28-day menstrual cycle. Nat. Commun. 8, 14584 (2017).
31. Kaushik, P., Kaushik, M., Jacob, S. & Parvez, S. in Microﬂuidics and

Multi Organs on Chip 289-324 (Springer, 2022).

32. Wang, Y. et al. Emerging trends in organ-on-a-chip systems for drug

screening. Acta Pharmaceutica Sin. B 13, 2483–2509 (2023).
33. Maass, C. Organ-On-Chips And Digital Twins. https://esqlabs.com/

news-20230307-2-2-2/#:~:text=The%20Rise%20of%20Digital%
20Twin%20Platforms&text=It%20involves%20creating%20a%
20virtual,allowing%20for%20analysis%20and%20optimization.
Access date: 02 Dec 2024.

34. Aravindakshan, M. R., Mandal, C., Pothen, A. & Maass, C. DigiLoCS: A

leap forward in predictive organ-on-chip simulations. bioRxiv : the
preprint server for biology, 2024.2003.2028.587123, https://doi.org/
10.1101/2024.03.28.587123 (2024).

35. digipredict.eu. Edge AI-deployed DIGItal Twins for PREDICTing

disease progression and need for early intervention in infectious and
cardiovascular diseases beyond COVID-19. https://www.digipredict.
eu/about/ (2021).

36. Abdollahi, H. et al. Radiopharmaceutical therapy on-a-chip: a

perspective on microﬂuidic-driven digital twins towards personalized
cancer therapies. Sci. Bull. 68, 1983–1988 (2023).

37. Trasta, A. Personalized medicine and proper dosage: Over- and

undertreatment of chronic diseases endanger patients’ health and
strain public health systems. EMBO Rep. https://doi.org/10.15252/
embr.201845957 (2018).

38. Swen, J. J. et al. A 12-gene pharmacogenetic panel to prevent
adverse drug reactions: an open-label, multicentre, controlled,
cluster-randomised crossover implementation study. Lancet 401,
347–356 (2023).

39. Venkatesh, K. P., Raza, M. M. & Kvedar, J. C. Health digital twins as
tools for precision medicine: Considerations for computation,
implementation, and regulation. npj Digital Med. 5, 150 (2022).

Competing interests
The authors declare no competing interests.

Ethics Approval
As the nature of this study did not involve any human or animal subjects,
interventions, or data collection, ethics committee approval was not
required.

Additional information
Correspondence and requests for materials should be addressed to
Joseph C. Kvedar.

Reprints and permissions information is available at
http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional
claims in published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if you modiﬁed the licensed material. You
do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons
licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted use,
you will need to obtain permission directly from the copyright holder. To
view a copy of this licence, visit http://creativecommons.org/licenses/by-
nc-nd/4.0/.

Acknowledgements
This study did not receive any external funding. All resources and facilities
used were provided by the authors themselves or their respective
institutions.

© The Author(s) 2024

npj Systems Biology and Applications |

 (2024) 10:150

6
