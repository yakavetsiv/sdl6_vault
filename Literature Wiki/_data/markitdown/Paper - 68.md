---
type: literature-note
source_note: "Papers/Paper - 68.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/68.pdf"
converter: "microsoft/markitdown"
---
AI4X – Accelerate Conference 2026, Singapore, 16–19 June 2026

Affordable 3D Printed Automation for Self-Driving Laboratory: Expanding Access
to High-Throughput Experimentation
Sayan Doloi1, Maloy Das2, Yujia Li3, Zen Han Choa4, Xingchi Xiaoa5, Matthew Osvaldo6, John Hanna7,
Leonard Ng Wei Tat  8
1-8School of Materials Science and Engineering (MSE), Nanyang Technological University, 50 Nanyang Ave,
Singapore 639798.

7University of Warwick, Department of Physics, Millburn House, Coventry CV4 7AL, United Kingdom

Correspondence to: [Assistant Prof. Leonard Ng Wei Tat] Email: leonard.ngwt@ntu.edu.sg

1.  Introduction

Laboratory  automation  through  self-driving
labs  represents  a  transformative  approach  to
accelerating scientific discovery, particularly in
chemical  sciences,  biological  sciences,  materi-
als science, and high-throughput  experimenta-
tion.  However,  widespread  adoption  of  these
technologies faces a significant barrier: the pro-
hibitive  costs  of  commercial  automation  sys-
tems, which can range from tens to hundreds of
thousands  of  dollars. This financial hurdle  has
created  a  technological  divide,  limiting  access
primarily to well-funded institutions and leav-
ing many research facilities unable to leverage
the benefits of automated experimentation.  3D
printing technology emerges as a democratizing
force in this landscape, offering a revolutionary
solution  to  the  accessibility  challenge.  By  ena-
bling the production of customizable laboratory
equipment at a fraction of the cost of commer-
cial  alternatives,  3D  printing  is  transforming
how  researchers  approach  laboratory  automa-
tion.  This  approach  not  only  reduces  financial
barriers  but  also promotes innovation through
open-source  designs,  allowing  researchers  to
share, modify, and improve upon existing solu-
tions. This review addresses a critical gap in the
current literature by exploring  both the trans-
formation of low-cost Fused Deposition Model-
ling (FDM) 3D printers into sophisticated auto-
mation  platforms  and  the  use  of  FDM  3D-
printed components to develop a broad range of
affordable laboratory automation systems. Fur-
thermore,  we  explore  how  strategic  modifica-
tions enable these systems to serve as automatic
liquid  handlers,  robotic  arms,  automated  sam-
ple  preparation  and  detection  systems,  chemi-
cal  reactionware,  automated  imaging  systems
and bioprinting units. The integration of these
modified 3D-printed components with machine
learning  and  artificial  intelligence  algorithms
creates unprecedented opportunities for devel-
oping accessible, highly flexible self-driving la-
boratories.

2. Use of 3D Printing for SDL applications

Fig. 1 Cost comparison between Commercially avail-
able systems to 3D-printing alternatives

Self-driving  laboratories  (SDLs)  represent  a
rapidly  advancing  field  that  integrates  auto-
mated  physical  experimentation  with  intelli-
gent,  algorithm-driven  decision-making.  By
combining  robotics,  artificial  intelligence,  and
automation  technologies,  SDLs  autonomously
select and execute experiments without human
intervention. These systems have the potential
to  transform  research  in  chemistry,  materials
science, biology, and beyond by enabling itera-
tive  experimentation  at  unprecedented  speeds
and scales [1-3]. Through the automation of re-
petitive tasks and the integration of intelligent
decision-making,  SDLs  enhance  experimental
efficiency, reproducibility, and scalability, pav-
ing the way for rapid advancements in scientific
discovery [4–7]. However, widespread adoption
of these technologies faces a significant barrier
due to the prohibitive costs of commercial auto-
mation systems, which can range from  tens  to
hundreds of thousands of dollars. This financial
hurdle has created a technological divide, limit-
ing access primarily to well-funded institutions
and  leaving  many  research  facilities  unable  to
leverage the benefits of automated experimen-
tation.  In  this  context,  3D  printing  technology
emerges  as  a  democratizing  force,  offering  a

AI4X – Accelerate Conference 2026, Singapore, 16–19 June 2026

Fig. 2 Development of Low-Cost 3D-Printed SDL Components: A focus on affordable and accessible solutions for
self-driving labs.

revolutionary solution to the accessibility chal-
lenge. With the rapid growth of 3D printing and
the  emergence  of  customizable,  open-source,
low-cost Fused Deposition Modelling (FDM) 3D
printers, it is now possible to develop different
components of SDLs as shown in the Fig. 2, tai-
lored to specific needs and integrate them into
SDLs.  With  the  ability  to  fabricate  intricate
parts  layer  by  layer,  FDM  stands  out  for  its
adaptability, low cost, and accessibility, making
it  ideal  for  the  development  of  SDL  hardware.
Recent  advances  in  open-source  3D  printing
have  further  democratized  access  to  this  tech-
nology, allowing researchers  worldwide to  de-
sign  and  share  bespoke  solutions  tailored  to
their  unique  experimental  needs.  By  enabling
laboratory
the  production  of  customizable
equipment at a fraction of the cost of commer-
cial alternatives as shown in the Fig. 1, 3D print-
ing  is  transforming  how  researchers  approach
laboratory automation. For example, traditional
automated  liquid  handling  systems,  essential
for  high-throughput  workflows,  often  cost  be-
tween $10,000 and $60,000, making them un-
attainable  for  many  smaller  labs.  In  contrast,
3D-printed  solutions  like  the  FINDUS  liquid
handler  and  the  EvoBot  platform  offer  compa-
rable precision and functionality for tasks such
as reagent dispensing, sample mixing, and cell
culture  maintenance  at  costs  as  low  as  $400
[4,5].  In  the  realm  of  sample  preparation,  de-
tection, and laboratory automation, 3D-printed
innovations  have  led  to  the  development  of
tools  such  as  automated  sampler,  mixture  and
liquid handlers etc [6-14]. Similarly, affordable
imaging  solutions  like  FlyPi  and  OpenFlexure
leverage modular components and open-source

software to deliver advanced functionalities, in-
cluding  fluorescence  and  live-cell  imaging,  for
under  $1,000  [15,16].  Additionally,  3D-printed
alternatives  to  commercial  robotic  arms  and
grippers, such as the Soft Hand and Insta Grasp,
provide  cost-effective  and  adaptable  solutions
for  tasks  like  pipetting,  reagent  mixing,  and
sample  transfer  [17,18].  The  integration  of  3D
printing  with open-source principles  is  pivotal
in  democratizing  SDLs.  Platforms  like  Arduino
and  Raspberry  Pi  enable  the  creation  of  low-
cost, programmable devices that seamlessly in-
tegrate with 3D-printed hardware [19,20].
This open-access, collaborative approach drives
innovation  by  allowing  researchers  to  rapidly
prototype, share designs, and improve upon ex-
isting  solutions.  3D  printing  technology  will
generate the scope of further research interest
for democratizing SDL considering different as-
pects of laboratory automation and digitization
at economic and sustainable way. By highlight-
ing  the  versatility,  cost-effectiveness,  and  ac-
cessibility  of  3D  printing  technology,  this  re-
view aims to inspire a broader audience within
the scientific  community  to  actively adopt and
innovate with these technologies. Researchers,
educators,  and  industry  professionals  are  en-
couraged to leverage 3D printing for the devel-
opment  of  customized,  low-cost  laboratory
equipment  tailored  to  specific  experimental
needs. Ultimately, this democratization of SDLs
through 3D printing has the potential to accel-
erate  scientific  discoveries,  improve  resource
optimization,  and  make  advanced  research
methodologies  accessible  to  laboratories  with
limited funding and infrastructure.

AI4X – Accelerate Conference 2026, Singapore, 16–19 June 2026

Acknowledgments

L. N. W. T. acknowledges funding from the Sin-
gapore Ministry of Education Tier 1 grants
(RS14/23 and RG86/23).

References

[1]  S.  Back,  A.  Aspuru-Guzik,  M.  Ceriotti,  G.
Gryn’ova, B. Grzybowski, G. H. Gu, J. Hein, K. Hippal-
gaonkar, R. Hormázabal, Y. Jung, S. Kim, W. Y. Kim,
S. M. Moosavi, J. Noh, C. Park, J. Schrier, P. Schwaller,
K. Tsuda, T. Vegge, O. A. Von Lilienfeld, and A. Walsh.
Digital Discovery, pp. 23–33, 2024.

[2] R. W. Epps, A. A. Volk, M. Y. S. Ibrahim, and M.
Abolhasani. Chem, pp. 2541–2545, 2021.

[3]  H.  G.  Martin,  T.  Radivojevic,  J.  Zucker,  K.  Bou-
chard, J. Sustarich, S. Peisert, D. Arnold, N. Hillson,
G. Babnigg, J. M. Marti, C. J. Mungall, G. T. Beckham,
L.  Waldburger,  J.  Carothers,  S.  Sundaram,  D.
Agarwal, B. A. Simmons, T. Backman, D. Banerjee, D.
Tanjore,  L.  Ramakrishnan,  and  A.  Singh.  Current
Opinion in Biotechnology, article 102881, 2023.

[4]  F.  Barthels,  U.  Barthels,  M.  Schwickert,  and  T.
Schirmeister. SLAS Technology, pp. 190–199, 2020.

[5] A. Faiña, B. Nejati, and K. Stoy. Applied Sciences,
article 814, 2020.

[6] M. C. Carvalho. HardwareX, article e00215, 2021.

[7] M. C. Carvalho and B. D. Eyre. Methods in Ocean-
ography, pp. 23–32, 2013.

[8] J. P. Efromson, S. Li, and M. D. Lynch. HardwareX,
article e00177, 2021.

[9] S. A. Longwell and P. M. Fordyce. Lab on a Chip,
pp. 93–106, 2020.

[10]  M.  C.  Carvalho  and  R.  H.  Murray.  HardwareX,
pp. 10–38, 2018.

[11] M. Dyga, C. Oppel, and L. J. Gooßen. HardwareX,
article e00211, 2021.

[12] M. S. Cubberley and W. A. Hess. Journal of Chem-
ical Education, pp. 72–74, 2017.

[13] J. M. Pearce, N. C. Anzalone, and C. L. Heldt. SLAS
Technology, pp. 510–516, 2016.

[14] S. Eggert, P. Mieszczanek, C. Meinert, and D. W.
Hutmacher. HardwareX, article e00152, 2020.

[15] A. Maia Chagas, L. L. Prieto-Godino, A. B. Arren-
berg, and T. Baden. PLoS Biology, article e2002702,
2017.

[16] J. T. Collins, J. Knapper, J. Stirling, J. Mduda, C.
Mkindi, V. Mayagaya, G. A. Mwakajinga, P. T. Nyakyi,
V. L. Sanga, D. Carbery, L. White, S. Dale, Z. Jieh Lim,
J.  J.  Baumberg,  P.  Cicuta,  S.  McDermott,  B.  Voden-
icharski, and R. Bowman. Biomedical Optics Express,
p. 2447, 2020.

[17] H. Li, C. J. Ford, M. Bianchi, M. G. Catalano, E.
Psomopoulou,  and  N.  F.  Lepora.  IEEE  Robotics  and
Automation Letters, pp. 8745–8751, 2022.

[18]  X.  Zhou  and  A.  J.  Spiers.  In  Proceedings  of  the
2023  IEEE/RSJ  International  Conference  on  Intelli-
gent  Robots and  Systems (IROS), IEEE,  Detroit, MI,
USA, pp. 4555–4561, 2023.

[19] M. Coakley and D. E. Hurt. SLAS Technology, pp.
489–495, 2016.

[20]  J.  Courtemanche,  S.  King,  and  D.  Bouck.  SLAS
Technology, pp. 448–455, 2018.
