---
type: literature-note
source_note: "Papers/Paper - 267.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/267.pdf"
converter: "microsoft/markitdown"
---
AI4X – Accelerate Conference 2026, Singapore, 16–19 June 2026

 DIY, Modular Automation Platform Built from Affordable Components for

Directed Evolution and Molecular Biology, Toward Closed-Loop Workflows

Takanori Uzawa, Rikiya Watanabe
RIKEN Pioneering Research Institute, Japan

Correspondence to: [Takanori UZAWA] tuzawa@riken.jp

Many  experiments  in  materials  science  and
chemical/biological  engineering  rely  on  itera-
tive,
trial-and-error  workflows:  preparing
many  samples  under  slightly  different  condi-
tions,  running  measurements,  and  repeating
this cycle over long periods to optimize function
and performance. In practice, these workflows
often involve routine liquid handling and sam-
ple transfers that must be executed consistently
to ensure reproducibility. However, performing
such  repetitive  procedures  manually  is  time-
consuming, physically demanding, and prone to
human error and day-to-day variability.

In this study, we use directed evolution as a con-
crete  testbed  for  iterative  molecular  discovery
workflows, where functional peptides and pro-
teins  are  obtained  through  repeated  selection
cycles that must be executed reproducibly over
long  periods.  This  repetitive  manual  work  not
only places a significant burden on researchers
but also introduces risks of human error and in-
consistency. To overcome these challenges, we
built a do-it-yourself (DIY) laboratory automa-
tion  system  by  integrating  an  open-source  liq-
uid  handling  robot  (Opentrons,  OT-2)  with  a
six-axis robotic arm (uFactory, xArm). Notably,
this system was assembled in-house using com-
mercially available components, aiming to bal-
ance accessibility and affordability without re-
lying on expensive, highly customized solutions.

With  this  DIY  system,  we  automated  major
steps in a directed evolution workflow, includ-
ing  in  vitro  transcription  and  translation,  nu-
cleic acid purification, binding selection, wash-
ing, and elution processes. A full run operated
for  ~11  hours  with  ~1  hour  of  human  involve-
ment  mainly  for  initial  sample  preparation.
Through  a  series  of  test  experiments  against
four  protein  targets,  the  system  successfully
identified peptides that bind to three out of the
four targets; the only negative result was BSA,
consistent  with  its  well-known  promiscuous
binding.

Crucially,  the  six-axis  arm  complements  OT-2
by  automating  physical  sample  logistics  be-
tween  devices,  enabling  a  more  end-to-end

workflow than liquid handling alone. The arm-
integrated  peripherals
include  temperature
control,  automated  cap  opening/closing,  and
magnetic-bead  capture  modules,  enabling  ro-
bust handling of tube-based workflows. A par-
ticularly  noteworthy  achievement  is  that  our
system  selected  binding  peptides  for  targets
that  had  previously  resisted
identification
through  manual  experiments  by  skilled  re-
searchers,  highlighting  its  potential  to  reduce
manual  labor  while  improving  reproducibility
and success rates.

All  operations  are  executed  from  structured
protocol files with automatic logging of step pa-
rameters and sample states, improving tracea-
bility and reproducibility. Building on these re-
sults,  we  are  expanding  the  platform  toward
general molecular biology and iterative experi-
mental  loops  by  integrating  additional  instru-
ments—thermal  cycling,  gel  electrophoresis
with automated readout, and nucleic acid quan-
tification with data ingestion. To keep the plat-
form modular, we are implementing standard-
ized  interfaces  (Model  Context  Protocol,  MCP)
that  separate  workflow  execution  from  device
control and measurement readout, thereby sup-
porting the development of closed-loop experi-
mental  workflows.  Beyond  directed  evolution,
the same architecture is applicable to iterative
experimental  loops  common  in  materials  dis-
covery,  where  repeatable  sample  preparation,
purification, and measurement cycles are criti-
cal.

Fig. 1: Overview of the DIY laboratory automa-
tion platform.

Acknowledgments

AI4X – Accelerate Conference 2026, Singapore, 16–19 June 2026

This work was supported by the RIKEN Incen-
tive Research Fund and JST ASPIRE.
