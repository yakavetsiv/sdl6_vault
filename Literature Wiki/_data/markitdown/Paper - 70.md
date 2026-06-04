---
source_note: "Papers/Paper - 70.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/70.pdf"
converter: "microsoft/markitdown"
---
|     |     | AI4X  | – Accelerate Conference 2026, Singapore, 16 |     |     | –19 June 2026 |     |     |     |
| --- | --- | ----- | ------------------------------------------- | --- | --- | ------------- | --- | --- | --- |
Self -Driven  Process Optimization in Pneumatic 3D Printing: From Static Ensemble
|     |     | Learning to Autonomous Bayesian  |                |                     |     |     | Method |     |     |
| --- | --- | -------------------------------- | -------------- | ------------------- | --- | --- | ------ | --- | --- |
|     |     |                                  | Maxime  Goulet | 1, Audrey Laventure |     |     | 1      |     |     |
1[Département de Chimie,  Institut Courtois,  Université de Montréal, 1375 Avenue Thérèse -Lavoie -Roux,
|     |                      |     | Montréal, Québec H2V 0B3, Canada |     |                                |     | ]   |     |     |
| --- | -------------------- | --- | -------------------------------- | --- | ------------------------------ | --- | --- | --- | --- |
|     | Correspondence to: [ |     | Maxime Goulet                    |     | ] maxime.goulet.3@umontreal.ca |     |     |     |     |
nozzle target), the process highlighted the inef-
| 1.  Introduction |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ficiency of static data collection, necessitating a
Pneumatic extrusion -based 3D printing enables  more agile hardware -software solution .
| the fabrication of complex  |     | architectures with  |     |     |     |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
materials ranging from low -viscosity solutions  3. Self -Optimizing Hardware Architec ture
to high -viscosity molten polymers. However,
|                      |     |                         |     |     | One of t                 | he core  | contributions |  of this work     | is the  |
| -------------------- | --- | ----------------------- | --- | --- | ------------------------ | -------- | ------------- | ----------------- | ------- |
| optimizing the multi |     | -dimensional parameter  |     |     |                          |          |               |                   |         |
|                      |     |                         |     |     | introduction of a custom |          |               | -engineered, open | -       |
space, encompassing pressure, temperature,
source pneumatic printing head capable of dis-
| speed and |  others,  remains a persistent bottle- |     |     |     |     |     |     |     |     |
| --------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tinct thermal management and pressure con-
| neck, typically requiring laborious trial |     |     | -and-er- |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
trol. Unlike standard commercial heads, this
| ror or exhaustive dataset generation |     |     |  [1]. Stand- |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
system is designed to process a broad rheologi-
| ard open | -loop printers lack the adaptability re- |     |     |     |                                |     |     |                   |     |
| -------- | ---------------------------------------- | --- | --- | --- | ------------------------------ | --- | --- | ----------------- | --- |
|          |                                          |     |     |     | cal spectrum, transitioning se |     |     | amlessly between  |     |
quired to navigate these complex process win-
|     |     |     |     |     | liquid solutions and viscous melts |     |     |  while being  |     |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | ------------- | --- |
dows, particularly when transitioning between
|                          |                                   |                      |     |     | easily interchangeable              |     |          | . The hardware is cou-    |          |
| ------------------------ | --------------------------------- | -------------------- | --- | --- | ----------------------------------- | --- | -------- | ------------------------- | -------- |
| solution -based and melt |                                   | -based extrusion     |     |     |                                     |     |          |                           |          |
|                          |                                   |                      |     |     | pled with a                         |     | Bayesian |   optimization algorithm  |          |
| modes.  This             | work  presents                    |  the development of  |     |     |                                     |     |          |                           |          |
|                          |                                   |                      |     |     | that replaces the exhaustive grid   |     |          |                           | -search  |
| a novel, self            | -optimizing 3D printing architec- |                      |     |     |                                     |     |          |                           |          |
|                          |                                   |                      |     |     | method. Instead of relying on a pre |     |          | -existing da-             |          |
ture designed to autonomously identify optimal
|     |     |     |     |     | tabase, the syste |     | m utilizes a  | gaussian  | process  |
| --- | --- | --- | --- | --- | ----------------- | --- | ------------- | --------- | -------- |
processing conditions. We propose a transition
surrogate model to actively select the next set
| from static, data | -heavy machine learning mod- |     |     |     |     |     |     |     |     |
| ----------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
of printing parameters based on an acquisition
els to an active learning framework utilizing
|                        |          |                         |                  |     | function. This          |         | process  | allows  for a self     | -driven  |
| ---------------------- | -------- | ----------------------- | ---------------- | --- | ----------------------- | ------- | -------- | ---------------------- | -------- |
| Bayesia n Optimization |          |  [2], implemented on a  |                  |     |                         |         |          |                        |          |
|                        |          |                         |                  |     | intelligent             |  explor | ation    |  and  exploit ation of |  the     |
| custom, open           | -source  | heated                  | pneumatic print  |     |                         |         |          |                        |          |
|                        |          |                         |                  |     | parameter space in real |         |          | -time.                 |          |
head.
|                                  |     |     |              |     | 4. Methodological Synthesis and Validation |     |     |     |     |
| -------------------------------- | --- | --- | ------------ | --- | ------------------------------------------ | --- | --- | --- | --- |
| 2. Foundational Data and Process |     |     | ing  Charac- |     |                                            |     |     |     |     |
terization   The efficacy of the new Bayesian system is vali-
|             |                                     |     |     |     | dated against the ground |     |     | -truth data established  |     |
| ----------- | ----------------------------------- | --- | --- | --- | ------------------------ | --- | --- | ------------------------ | --- |
| To validate |  the necessity and accuracy of the  |     |     |     |                          |     |     |                          |     |
in our foundational PCL study. We demonstrate
proposed autonomous system, an extensive
|     |     |     |     |     | that the self |     | -optimizing printer converges on  |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --------------------------------- | --- | --- |
foundational study was first conducted using
|                   |                              |     |     |     | the optimal  |     | print  fidelity |   metrics   defined by  |     |
| ----------------- | ---------------------------- | --- | --- | --- | ------------ | --- | --------------- | ----------------------- | --- |
| poly(caprolactone | ) (PCL) on a commercial Hot  |     |     |     |              |     |                 |                         |     |
specific filament height, width, and surface to-
Melt Extrusion (HME) system. Comprehensive
|     |     |     |     |     | pology targets |     |  using a fraction of the samples  |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --------------------------------- | --- | --- |
material characterization, including Thermo-
required by the static ensemble approach. By in-
gravimetric Analysis (TGA) and Differential
tegrating the material constraints identified via
Scanning Calorimetry (DSC), defined the safe
|     |     |     |     |     | thermal and rheological characterization |     |     |     |   di- |
| --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | ----- |
thermal processing window (60 °C to 265 °C)
rectly into the optimization loop, the system
| and crysta | llization kinetics | . The upper limit was  |     |     |     |     |     |     |     |
| ---------- | ------------------ | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
avoids material degradation while maximizing
strictly enforced to prevent oxidative degrada-
|                                      |                               |     |           |     | print speed and fidelity |     |     | .   |     |
| ------------------------------------ | ----------------------------- | --- | --------- | --- | ------------------------ | --- | --- | --- | --- |
| tion mechanisms common in polyesters |                               |     |   [3].    |     |                          |     |     |     |     |
| Rheological                          | studies helped identify       |     | the shear | -   |                          |     |     |     |     |
|                                      |                               |     |           |     | 5. Conclusion            |     |     |     |     |
| thinning behaviour                   |  critical for extrusion, map- |     |           |     |                          |     |     |     |     |
ping a viscosity range from  80 Pa·s to  750 Pa·s.  This research bridges the gap between material
A static dataset of 840 samples was generated  science and autonomous robotics. By moving
via a fixed -interval grid search, analysing print  beyond static datasets to an active, Bayesian -
fidelity through stereomicroscopy and  stylus  driven approach, we demonstrate a scalable
profilometry. While ensemble learning models  method for rapidly adopting novel polymers in
trained on this data successfully predicted opti- additive manufacturing. The pro posed open -
mal  printing  parameters (minimizing  height,  source hardware and control framework signif-
| width and  | filament deviation from the 0.2 mm  |     |     |     |     |     |     |     |     |
| ---------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

AI4X – Accelerate Conference 2026, Singapore, 16 –19 June 2026
icantly reduce material waste and characteriza- References
tion time, paving the way for truly autonomous,
multi -material 3D printers . [1] Meng, L., McWilliams, B., Jarosinski, W. et
al. Machine Learning in Additive Manufactur-
Acknowledgments ing: A Review. JOM 72, 2363 –2377 (2020).
[2] B. Shahriari, K. Swersky, Z. Wang, R. P. Ad-
MG thanks the Fonds de Recherche du Québec, ams and N. de Freitas . Taking the Human Out
Secteur Nature et Technologie, for a doctoral of the Loop: A Review of Bayesian Optimiza-
scholarship. AL acknowledges the financial sup- tion. Proc. IEEE 104(1), 148-175 (2016).
port from the Canada Research Chair program, [3] Persenaire O, Alexandre M, Degée P, Dubois
the Natural Sciences and Engineering Research P. Mechanisms and kinetics of thermal degra-
Council of Canada (NSERC) and from the Can- dation of poly(epsilon -caprolactone). Biom-
ada Foundation for Innovation (CFI). All au- acromol . 2(1), 288-294 (2001).
thors would like to acknowledge the Fondation
Courtois for its support for the research instal-
lations.
