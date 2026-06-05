---
tags:
  - literature
  - type/paper
  - lit/sdl
type: literature-note
source_note: "Papers/Paper - d3dd00115f.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/d3dd00115f.pdf"
converter: "microsoft/markitdown"
---
Digital
Discovery
PAPER
Digital pipette: open hardware for liquid transfer in
†
self-driving laboratories
Citethis:DigitalDiscovery,2023,2,
1745
Naruki Yoshikawa, *ab Kourosh Darvish, ab Mohammad Ghazi Vakili, a
Animesh Garg *ab and Ala´n Aspuru-Guzik *abc
Self-drivinglaboratoriesarebeinginvestigatedasapotentialmeanstoacceleratethematerialdiscovery
process. Accurate liquid handling is an essential operation in the context of chemical laboratories, and
consequently a self-driving laboratory will require robotic liquid handling and transfer. Although many
pipettes are available for human scientists, robots cannot manipulate these pipettes due to the
limitations of current robot gripper morphology. We propose an intuitive yet elegant design for a 3D-
printeddigitalpipettedesignedforrobotstocarryoutchemicalexperiments.Itcostslessthan200USD,
and the simple design with three parts enables a new user to assemble one in 10 minutes. We
Received14thJune2023 conducted a performance evaluation that closely followed ISO 8655-6. Our results show that robots
Accepted27thSeptember2023
with the digital pipette could conduct accurate liquid delivery with 0.2% random error for the nominal
DOI:10.1039/d3dd00115f
volume (10 mL). This performance is comparable to commercially available liquid handling devices,
rsc.li/digitaldiscovery whosetypicalrandomerrorsare0.3%.
1 Introduction limited due to the delayed feedback from the sensors.3 This
study seeks to overcome these limitations by providing
In a self-driving lab, robots carry out experiments autono-
asimpleandaffordablesolutionthatcanbeextendedtomany
mouslyandselectthenextexperimenttoperformusingAIor roboticsettings.
optimization approaches.1,2 Among different approaches Accurateliquidhandlingiscrucialinscienticexperiments,
toward self-driving laboratories, we aim to introduce and various liquid-transferring instruments have been devel-
ageneral-purposerobotthatconductschemicalexperiments, oped to improve accuracy and safety, such as the Pasteur
using common hardware and affordable customized tools. pipette, the volumetric pipette, and the micropipette. These
Specialized hardware for lab automation is expensive and pipettes are widely available, but they are mainly designed for
oenlacksexibility.Itusuallyrequiresadditionalhardware manual human operation. Typical robotic hands are not as
to expand its functionality. On the other hand, general-
dexterousashumanhands,soitisdifficulttohandlecommon
purpose robots are expandable with soware and enable lab manual pipettes found in labs. It would require laborious
automation that maximizes existing resources. A large set of engineeringtomakerobotsusepipettesdesignedforhumans.
operations, such as reagent addition, stirring, and tempera-
Forexample,whenusingarobotwithatwo-ngergripper,the
turecontrol,canbeimplementedbyprogrammingarobotto gripperisusedtoholdthepipette,anditcannotpushabutton
use common lab tools. Since most existing chemistry instru- orrubberbulbstodispenseliquids.Inaddition,controllingthe
ments are designed for human use, introducing a robot that amount of transferred liquid requires visual perception skills,
conducts experiments in a similar way to humans has the suchasdetectingthesurfaceofliquidsorreadingthenumbers
potentialtorealizeahigherlevelofintegrationofinstruments on a scale. Solving these technical difficulties requires addi-
at a lower cost. One of the common tasks that robots must tional development time or specialized hardware. Specialized
perform accurately in chemistry, materials science, and end-effectors for triggering pipettes have been proposed to
biology self-driving laboratories is the transfer of liquids. operatecommerciallyavailablepipettes.4,5However,theseend-
Pouringliquidsforchemistryexperimentsusingarobotarm
effectorslimitthecapabilitiesoftherobothandtooperateother
and regular glassware has been proposed, but its accuracy is objects.Anthropomorphichandsmayhandlemanualpipettes,
but they impose many technical challenges on soware
development.
aUniversityofToronto,Canada.E-mail:naruki.yoshikawa@mail.utoronto.ca
bVectorInstituteforArticialIntelligence,Canada.E-mail:garg@cs.toronto.edu Creatingcustomhardwareforaparticularusageisnecessary
cCanadianInstituteforAdvancedResearch(CIFAR),Canada.E-mail:alan@aspuru.
whencommercialitemsdonotfullltherequirementsforthe
com task. 3D printers have been utilized as an inexpensive and
†Electronic supplementary information (ESI) available. See DOI: ubiquitous method to manufacture customized labwares.6,7
https://doi.org/10.1039/d3dd00115f
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,1745–1751 | 1745
.MA
53:82:2
6202/32/1
no
dedaolnwoD
.3202 rebotcO
40
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
View Journal | View Issue

DigitalDiscovery Paper
Therehavebeenproposed3D-printedliquidhandlingdevices,
such as syringe pumps,8–11 liquid handling workstation12 and
a desktop liquid dispenser.13 They are typically designed as
independent devices and are not intended to be used with
a general-purpose robot arm. A syringe pump operated by
a robot arm14 is one of the few examples of 3D-printed liquid
handling devices designed for a general-purpose robot. 3D
printedmicropipettesarealsoproposed;however,theiractua-
tion mechanisms are designed for dexterous human ngers,
suchaspushingaplunger15,16orrotatinggears.17
In this paper, we propose a 3D-printed digital pipette
designed for two-nger robot grippers. The proposed pipette
offers an accurate liquid handling skill to our chemistry lab
Fig.2 (a)3DCADmodelforthedigitalpipette:(i)platform,(ii)plunger
automationframework3showninFig.1.Ourpipetteusesalow-
holder,(iii)syringecover.(b)Pictureoftheassembledpipette.
costcommercialsyringetoholdliquidsandalinearactuatorto
handletheplungerofthesyringe.Thelinearactuatorenables
precise control of the syringe plunger. To address the pipette
handling problem with a two-nger robot gripper, our device differentlaboratorysettings.Thesecapabilities,combinedwith
aspiratesanddispensesliquidsbysendingacommandthrough its precision and versatility, make our pipette an attractive
a serial communication protocol. Moreover, the volume of solution for various applications in the self-driving laboratory
liquid to transfer can be specied by a serial command from eld. Our device enhances the capabilities of robot arms,
aPC.Thiscommand islatertransformedintothelinearactu- makingthemmoreaccessibleforself-drivinglabdevelopment.
ator control signal. This control mechanism does not require The device can be applied to a variety of experiments that
any visual perception skills. The portable shape with at requirequantitativeanalysis,suchassolubilitymeasurements.
surfacesmakesgraspingbytwo-ngerrobotgripperseasierand This study represents a step forward in the eld of lab auto-
more reliable. This open and affordable hardware equips mation by providing a cost-effective and versatile solution for
a general-purpose robot with liquid handling ability without preciseliquidhandling.
limitingitsexistingcapabilitiesinperformingothertasks,such
asmanipulation. 2 Methods
The design of the pipette is publicly available under the
creativecommonslicense.Inaddition,thecodeforcontrolling Ourdigitalpipetteprovidesalow-costliquidhandlingsolution
theproposedpipetteisavailablewiththedocumentation.Users toageneral-purposerobotarm.Inthissection,wewillexplain
canexpandourdesigntoadjusttotheirindividualneeds.Our itsdesignandourevaluationapproach.
pipette design can be used with any general industrial robot
withasimplegripper,makingiteasytointegrateintoexisting 2.1 Pipettedesign
automatedlaboratorysetups.Thelowcostofourdesignmakes Wewilldescribethedesignofthedigitalpipetteandthecostto
it feasible to develop and deploy multiple devices for use in buildone.
Fig.1 Chemistrylabautomationframework.3Theframeworktakesinstructionsfromusersandgeneratesataskandmotionplanbasedonthe
inputfromperceptionmodules.Thegeneratedplanispassedtotheskillmoduleforexecutionandrealizedbychemicalinstrumentsandrobot
arms.Theproposeddigitalpipetteworksastheliquidhandlingskillinthisframework.
1746 | DigitalDiscovery,2023,2,1745–1751 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry
.MA
53:82:2
6202/32/1
no
dedaolnwoD
.3202 rebotcO
40
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

Paper DigitalDiscovery
Table1 Costanalysisoftheproposedpipette
Parts Price Details
Linearactuator 70USD ActuonixL16-100-63-6-R
3Dprinting 60USD Estimatedcosttoprintallparts
Electronicparts 40USD Arduino,cables,connectors
10mLsyringe 1USD NORM-JECTLuerSolo(10mL)
extendsit.ThecontrollerPCsendsanintegerNtoArduinovia
serialcommunication,andtheArduinosendsaNmicrosecond
pulsetotheactuator.Thelengthofthepulsethatcorresponds
toeachvolumemayvarybecauseofprintingaccuracyandthe
individual characteristic ofthe actuator.The pulse lengthwas
calibrated by measuring the weight of dispensed water using
Fig.3 CircuitdiagramofArduinoandthelinearactuator.Thesignal
aweighingscale.
pin(white)ofthelinearactuatorisconnectedtopin8ofArduinoUno,
thepowerpin(red)is connectedto6Vpower,andthegroundpin 2.1.4 Cost analysis. Table1 shows the approximate prices
(black) is connected to the GND. Arduino is connected to a PC via for the components that were used in assembling the pipette.
aUSBcable. Pleasenotethatthecostof3Dprintingdependsontheprinting
methods. The cost of the printing materials we consumed to
build one pipette was around 30 USD. The estimated costs of
2.1.1 Overview. The design ofourdigitalpipetteis shown
onlineprintingserviceswere64.76USDinXometry,§and58.57
in Fig. 2. The pipette is composed of three parts: a platform,
USD in Shapeways.{ Our proposed pipette costs less than 200
a plunger holder, and a syringe cover. They are available on
USDintotal,whichiscomparabletotypicalmicropipettesused GitHub,‡ where rendered STL les can be viewed. A linear
inachemistrylaboratory,whosecostrangesin50–350USD.
actuatorisfastenedtotheplatformwithscrewsandamounting
bracket. The plunger of the 10 mL syringe and the tip of the
2.2 Manualgravimetrictest
linear actuator are connected together by the plunger holder.
The syringe barrelis fastened by the platform and the syringe The digital pipette was evaluated by gravimetric testing based
cover. The linear actuator is operated by an Arduino that ontheinternationalstandardonpipettes(ISO8655-6(ref.18)).
communicateswiththerobotworkstationthroughaUSB-serial We measured the weight of the delivered water using a scale.
communication protocol. The total length of the pipette is The weighing value at i-th test m i is converted into a volume
37cm.Becauseofitssimplicity,ittakeslessthan10minforan usingaformula
inexperienced user to build the pipette. Detailed building
instructionisalsoavailableintheGitHubrepository. V i =m i ×Z (1)
2.1.2 3D printing. The 3D models of the pipette were
whereZistheZcorrectionfactorthatdependsonthetemper-
designed with Fusion 360 (Autodesk Inc.). The platform was
atureandairpressureatmeasurementtakenfromthetablein
printedwithForm3L(FormlabsInc.)usingFormlabsRigid10K
thestandard.18Sincethewatertemperaturewas22°Candthe
Resin.Theplungerholderandsyringecoverwereprintedwith
airpressurewas100.8kPa,Z=1.0033(mLmg −1)wasusedfor
a KP3S printer (KINGROON Tech Co., Ltd) using ANYCUBIC (cid:1)
calculation.ThemeandeliveredvolumeV iscalculatedby
PLA3DPrinterFilament(Grey).Therigidresinwassuitablefor
Pn
theplatformbecauseofitsrigidness,andPLAwassuitablefor V
i
movablepartsbecauseofitslightnessandexibility.
V ¼ i¼1 (2)
n
2.1.3 Circuit. The pipette operates a syringe with a linear
actuatorcontrolledbyanArduinothatcommunicateswiththe
controller PC. We used L16-100-63-6-R (Actuonix, Canada) as The systematic error e and its percent expression h are
s s
a linear actuator. The linear actuator is lightweight (74 g) and calculatedby
provides enough force (maximum 100 N) to operate a large
syringe.Itisconnectedtoa6VDCpowerinputandArduino. e s =V(cid:1) −V s (3)
NORM-JECTLuerSolo10mLwasusedasacommondisposal
syringe.WeusedUno328AVRDevBoard(CreatronInc.,Can- h s =100%×(V(cid:1) −V s )/V s (4)
ada), which is compatible with Arduino Uno Rev3. The circuit
whereV istheselectedtestvolume.Therandomerrors andits
diagramisshowninFig.3.TheArduinoisconnectedtoaPCvia s r
percentexpressionC arecalculatedby
aUSBcableandcontrolsthelinearactuator.Theactuatortakes V
a5Vpulsesignaltodecidethelengthofitsextension.A1.0ms
pulsesignalfullyretractstheactuator,anda2.0mssignalfully §https://www.xometry.com/WechoseStandardoptiontomakeaquote.
{https://www.shapeways.com/ We chose White Natural Versatile Plastic,
Economy Manufacturing Speed, and Standard Shipping to United States to
‡https://github.com/ac-rad/digital-pipette/ makeaquote.
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,1745–1751 | 1747
.MA
53:82:2
6202/32/1
no
dedaolnwoD
.3202 rebotcO
40
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

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |     |     |     |     | Paper |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
vffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
u
uPn (cid:3) (cid:4) a scale with a resolution of 0.01 g. To ensure the tip of the
2
u V (cid:2)V syringewasimmersedinthewater,theexperimentwaspaused
|     |     |     | t   | i   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | s ¼ | i¼1 |     |     |     |     |     |     |     |     |     |     |     |
r n(cid:2)1 (5) when the amount of water in the beaker was lowered and
resumedaermovingwaterbetweenbeakers.Wecontinuedthe
|     |     |     |         |           |     |     | experiment | until  | the | total test | number      |     | reached | 100. The  |
| --- | --- | --- | ------- | --------- | --- | --- | ---------- | ------ | --- | ---------- | ----------- | --- | ------- | --------- |
|     |     | C   | =100%×s | /V(cid:1) |     | (6) |            |        |     |            |             |     |         |           |
|     |     | V   |         | r         |     |     | maximum    | number | of  | continuous | experiments |     | was     | 100 for 1 |
mL,50for5mL,and30for10mL.Thesamecalibrationvalue
| We used | ultrapure | water | from | the | Thermo Barnstead | Gen- |          |            |     |                |     |          |         |        |
| ------- | --------- | ----- | ---- | --- | ---------------- | ---- | -------- | ---------- | --- | -------------- | --- | -------- | ------- | ------ |
|         |           |       |      |     |                  |      | was used | throughout |     | the experiment |     | for each | volume. | We set |
PurexCADUltrapureWatersystem.Thepipetteaspirateswater
|     |     |     |     |     |     |     | a5sdelayaersendingasignaltothepipette |     |     |     |     |     | towaitforthe |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
fromabeakeranddispensesitontoaPetridish.Theweightof movement of the actuator. The systematic and random errors
 .MA 53:82:2 6202/32/1 no dedaolnwoD .3202 rebotcO 40 no dehsilbuP .elcitrA sseccA nepO thedeliveredwaterwasmeasuredbyascalewitharesolutionof
werecalculatedusingthesameformulaintheprevioussection.
| 0.1 mg. | The scale | was tared | each | time | just before | dispensing |     |     |     |     |     |     |     |     |
| ------- | --------- | --------- | ---- | ---- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Z=1.0037wasusedfor1and10mLandZ=1.0040for5mL
| watertoreducetheerror |        |             | causedbyevaporation. |         | Although        | the     |          |         |          |     |             |     |        |             |
| --------------------- | ------ | ----------- | -------------------- | ------- | --------------- | ------- | -------- | ------- | -------- | --- | ----------- | --- | ------ | ----------- |
|                       |        |             |                      |         |                 |         | based on | the air | pressure | and | temperature |     | at the | time of the |
| proposed              | device | is designed | for                  | robots, | this evaluation | is per- |          |         |          |     |             |     |        |             |
experiment.
| formed | by a human | because | we  | could | not mount | the high- |     |     |     |     |     |     |     |     |
| ------ | ---------- | ------- | --- | ----- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
specied
| resolution | (0.1 | mg) scale |     | by  | the standard | in our |     |     |     |     |     |     |     |     |
| ---------- | ---- | --------- | --- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
robot operation environment. The device was handled by 2.4 Evaluationofcalibrationandresolution
sendingacommandfromalaptopconnectedtothedevice.As Theproposedpipetteoperatesasyringewithalinearactuator
speciedbythestandard,wetested100%,50%,and10%ofthe controlledbyapulsesignalwitharesolutionof1ms.Thepulse
| nominal | volume | (i.e., 10 | mL, 5 | mL, and | 1 mL). A | commercial |             |             |     |         |        |        |       |       |
| ------- | ------ | --------- | ----- | ------- | -------- | ---------- | ----------- | ----------- | --- | ------- | ------ | ------ | ----- | ----- |
|         |        |           |       |         |          |            | length that | corresponds |     | to each | target | volume | needs | to be |
micropipette(TransferpetteS1–10mL)wastestedfollowingthe
determinedbeforeusetoconsiderprintingandassemblyerrors
same protocol as a baseline. A graduate student with and the characteristics of the individual actuator and syringe.
biochemistryexperimentexperienceconductedthisstudy,and The optimal pulse length is determined by measuring the
the repeatability of errors was double-checked by an experi- transferred volume withdifferentpulse lengths. The pipetting
mentalchemist.Pleasenotethatwehadtoignoresomedetails performance was measured by changing the pulse length at
in ISO 8655-6 because of the nature of the device and the aspirationtodemonstratethecalibrationprocessandevaluate
limitation of the equipment. For example, we did not change theresolution.Waterdeliverytestswereconducted10timesfor
the tip during the test because the proposed pipette does not eachpulselengthinthesamemannerastheroboticpipetting
support tip replacement, and the humidity of the room (25%) experiment. The pulse length to dispense liquid was xed at
wasoutoftheallowedrange(45–85%). 1820 ms, where the plunger is fully pushed. Based on the
temperatureandairpressureattesttime,Z=1.0037wasused
inthecalculation.
2.3 Roboticpipettingtest
| We evaluated | the | performance |     | of the | pipette by transferring |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ------ | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Evaluationoftheeffectofviscosity
2.5
waterwithaFrankaEmikarobotequippedwithaRobotiq2F-85
gripper that has two ngers. The robot is equipped with an To evaluate the effect of liquid viscosity on the pipette perfor-
additional servo motor to increase the dexterity of the robot. mance,theroboticliquidtransfertestwasconductedforsugar
different
Detailsoftherobotaredescribedelsewhere.3Fig.4showsthe solutions with concentrations. The viscosity of the
experimental setup. The robotgraspsthe pipetteat thebegin- sugar solution rapidly changes as its concentration increases.
ningoftheexperiment.Therobotrepeatedlydeliversdeionized Sugarsolutionswerepreparedbymixinggranularsugar(Lantic
water between two beakers. The amount of delivered water is Inc., Canada) and deionized water. The temperature of the
measured by the difference in the weight of a beaker using solutionusedintheevaluationwas25°C.Theexperimentwas
Fig.4 Roboticpipettingtestsetup.(a)Therobotmovesthepipetteontopofabeaker,(b)therobotimmersesthepipetteinwaterandaspirates
it,(c)therobotmovesthepipetteontopofanotherbeakeranddispensesthewater.Theamountofdeliveredwaterismeasuredbyascale.
1748 | DigitalDiscovery,2023,2,1745–1751 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
|     | Paper    |     |       |          |                |     |         |      |     |     |     |     | DigitalDiscovery |     |     |
| --- | -------- | --- | ----- | -------- | -------------- | --- | ------- | ---- | --- | --- | --- | --- | ---------------- | --- | --- |
|     | repeated | ten | times | for each | concentration, |     | and the | mean | and |     |     |     |                  |     |     |
standarddeviationofthetransferredweightwerereported.The
|     | performance |     | of the       | commercial | micropipette |     | (Transferpette |      | S      |     |     |     |     |     |     |
| --- | ----------- | --- | ------------ | ---------- | ------------ | --- | -------------- | ---- | ------ | --- | --- | --- | --- | --- | --- |
|     | 1–10        | mL) | was measured | as         | a baseline.  | We  | chose          | 5 mL | as the |     |     |     |     |     |     |
targetvolume.
|                                                                                         | 3          | Results               |            | and discussion |      |              |     |          |      |     |     |     |     |     |     |
| --------------------------------------------------------------------------------------- | ---------- | --------------------- | ---------- | -------------- | ---- | ------------ | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
| .ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT     | 3.1        | Manualgravimetrictest |            |                |      |              |     |          |      |     |     |     |     |     |     |
|  .MA 53:82:2 6202/32/1 no dedaolnwoD .3202 rebotcO 40 no dehsilbuP .elcitrA sseccA nepO | The        | result                | of the     | gravimetric    | test | is shown     | in  | Table 2. | The  |     |     |     |     |     |     |
|                                                                                         | systematic |                       | and random | errors         | of   | the proposed |     | pipette  | were |     |     |     |     |     |     |
below the maximal permissible errors for single channel Fig.6 Therelationshipbetweenpulselengthandtransferredvolume
pipettes specied in the standard,19 and the performance was ofwater.Theroboticliquidtransferexperimentwasrepeated10times
foreachpulselength.Theformulaoftheregressionlineisy=−0.019x
|     | comparable |     | with a | commercial | micropipette. |     | Please | note | that |     |     |     |     |     |     |
| --- | ---------- | --- | ------ | ---------- | ------------- | --- | ------ | ---- | ---- | --- | --- | --- | --- | --- | --- |
+34.872.
|     | the   | system   | error for | the micropipette |          | was      | consistent | with       | the |     |     |     |     |     |     |
| --- | ----- | -------- | --------- | ---------------- | -------- | -------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     | value | reported | by        | the manufacturer |          | (0.31%), | but        | the random |     |     |     |     |     |     |     |
|     | error | was      | larger    | than the         | reported | value    | (0.06%),   | possibly   |     |     |     |     |     |     |     |
becauseofthedifferenceintheprociencyofpipettehandling.
Gravimetrictestingresults(n=10)
Table2
|     |        |     |                 |     | (cid:1) |      | h     |     |         |     |     |     |     |     |     |
| --- | ------ | --- | --------------- | --- | ------- | ---- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     | Volume |     | Device/standard |     | V       | (mL) | s (%) |     | C V (%) |     |     |     |     |     |     |
|     | 10.0mL |     | Ours            |     | 10.0083 |      | 0.08  |     | 0.07    |     |     |     |     |     |     |
|     |        |     | Micropipette    |     | 10.0170 |      | 0.17  |     | 0.15    |     |     |     |     |     |     |
|     |        |     | ISO8655         |     | —       |      | 0.60  |     | 0.30    |     |     |     |     |     |     |
|     | 5.0mL  |     | Ours            |     | 4.9922  |      | −0.16 |     | 0.14    |     |     |     |     |     |     |
|     |        |     | Micropipette    |     | 5.0025  |      | 0.05  |     | 0.12    |     |     |     |     |     |     |
|     |        |     | ISO8655         |     | —       |      | 1.2   |     | 0.60    |     |     |     |     |     |     |
1.0mL Ours 0.9887 −1.1 0.76 Fig.7 Therelationshipbetweenpulselengthandtransferredvolume
Micropipette 1.0349 3.49 0.64 of water around 10 mL. The robotic liquid transfer experiment was
ISO8655 — 6.0 3.0 repeated10timesforeachpulselength.Allpulselengthsareinteger
values,butthepointsaredodgedforthex-axistoincreasevisibility.
Theformulaoftheregressionlineisy=−0.018x+33.684.Basedon
thisresult,1286mspulsewasusedfor10mL.
Roboticpipettingevaluationresults(n=100)
Table3
|     |            |     |     | (cid:1) |     | h   |       |     | 3.2 Roboticpipettingevaluation |      |        |            |        |             |     |
| --- | ---------- | --- | --- | ------- | --- | --- | ----- | --- | ------------------------------ | ---- | ------ | ---------- | ------ | ----------- | --- |
|     | Volume(mL) |     |     | V (mL)  |     |     | s (%) |     | C V (%)                        |      |        |            |        |             |     |
|     |            |     |     |         |     |     |       |     | Table 3 and                    | Fig. | 5 show | the result | of the | evaluation. | The |
|     | 10.0       |     |     | 10.011  |     |     | 0.11  |     | 0.20                           |      |        |            |        |             |     |
systematicandrandomerrorswerewithinpermissibleerrorsin
|     | 5.0 |     |     | 4.989 |     | −0.22 |     |     | 0.26 |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
1.0 1.002 0.17 2.40 ISO 8655-2. The experiment did not involve any recalibration,
signicant
|     |     |     |     |     |     |     |     |     | and no |     | degradation | in performance |     | was observed. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------- | -------------- | --- | ------------- | --- |
(cid:1)=
Fig.5 Distributionofthetransferredliquidintheroboticpipettingexperimentforthreedifferentvolumes(n=100).(a)10.0mLpipetting(V
|     |     |     |     |     |     | (cid:1) |     |     |     | (cid:1) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
10.011,s =0.020),(b)5.0mLpipetting(V =4.989,s =0.013),(c)1.0mLpipetting(V =1.002,s =0.024).
|     |     | r   |     |     |     |     | r   |     |     |     | r   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,1745–1751 | 1749

View Article Online
|     | DigitalDiscovery |     |     |     |     |     |     |     |     |     |     |     | Paper |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Roboticpipettingfordifferentviscosity(n=10).Concentrationisthemasspercentofthesolution,viscosityistheliteraturevaluefor
Table4
sucrosesolutionat20°C,20thetargetistheweightof5mLsolutionexpectedfromtheliteraturedensityat20°C,andoursandmicropipetteare
theweightofdeliveredsolutionbyeachmethodwrittenintheformatofaverage±standarddeviation(averagerelativedeviationfromthetarget
in%)
Concentration(%) Viscosity(mPas) Target(g) Ours(g) Micropipette(g)
|                                                                                      |      |     |     |        |     |     |     |       | 4.978(cid:3)0.011(−0.26) |     |     | 4.984(cid:3)0.014(−0.14) |     |
| ------------------------------------------------------------------------------------ | ---- | --- | --- | ------ | --- | --- | --- | ----- | ------------------------ | --- | --- | ------------------------ | --- |
|                                                                                      | 0.0  |     |     | 1.002  |     |     |     | 4.991 |                          |     |     |                          |     |
|                                                                                      |      |     |     |        |     |     |     |       | 5.376(cid:3)0.019(−0.54) |     |     | 5.389(cid:3)0.019(−0.30) |     |
|                                                                                      | 20.0 |     |     | 1.945  |     |     |     | 5.405 |                          |     |     |                          |     |
|                                                                                      |      |     |     |        |     |     |     |       | 5.878(cid:3)0.013(−0.12) |     |     | 5.845(cid:3)0.016(−0.68) |     |
|                                                                                      | 40.0 |     |     | 6.162  |     |     |     | 5.885 |                          |     |     |                          |     |
|                                                                                      |      |     |     |        |     |     |     |       | 6.447(cid:3)0.017(+0.26) |     |     | 6.354(cid:3)0.031(−1.18) |     |
| .ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  | 60.0 |     |     | 58.487 |     |     |     | 6.430 |                          |     |     |                          |     |
 .MA 53:82:2 6202/32/1 no dedaolnwoD .3202 rebotcO 40 no dehsilbuP .elcitrA sseccA nepO
For example, both the systematic and random errors for any 4 Conclusions
|     | continuous | 10  | tests during | 100 | pipetting | were | within | the |     |     |     |     |     |
| --- | ---------- | --- | ------------ | --- | --------- | ---- | ------ | --- | --- | --- | --- | --- | --- |
permissiblerange.Ittook66mintodeliver1mLofwater100 We have developed open-source hardware to conduct precise
times.Therandomerrorinthisexperimentwaslargerthanthe liquidhandlingwithatwo-ngerrobotichandwithoutcustom-
valuereportedinthemanualexperiment.Onemajorreasonis ization. The performance was comparable to a commercially
the lack of perception of the syringe status. When the pipette available micropipette in various liquid transfer tasks. The
aspiratedwater,onedropofwateroenremainedatthetipof performance attained by the pipette is also comparable with
thesyringe.Humanscoulddetectthedropandremoveit,but other automatic commercial liquid dispensing hardware. For
therobotcarriedthepipettewithoutremovingthedropsinceit example, the liquid dispenser of Chemspeed (Chemspeed
didnotobservethesyringeandthemovementtoremoveadrop
|     |     |     |     |     |     |     |     | Technologies) | provides | 0.5% accuracy | (systematic | error) | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ------------- | ----------- | ------ | --- |
wasnotimplemented.Theweightofthedropcouldincreasethe 0.3%precision(randomerror)for1–10mLwater,accordingto
randomerror.Thevibrationoftherobotarmmightaffectthe the manual. The largest pipette (P1000 GEN2) of OT-2 Liquid
Handler(Opentrons)offers0.7%accuracyand0.15%precision
|     | handling | of the | pipette | and contribute |     | to the | higher | error. |     |     |     |     |     |
| --- | -------- | ------ | ------- | -------------- | --- | ------ | ------ | ------ | --- | --- | --- | --- | --- |
Although the robot attained enough accuracy specied in the for1000mL.21Theproposedlow-costhardwareenablesageneral-
internationalstandard,theperceptionofthesyringestatusand
purposerobotarmtodeliverliquidinasimilarperformanceto
more human-like movement may help increase the moreexpensivespecializedhardware.Thislowersthebarrierto
performance. introducingaccurateliquidhandlingforself-drivinglabs.
Althoughweuseda10mLsyringeinourdesign,thenominal
3.3 Calibrationandresolution volume can be adjusted by using a different syringe. Smaller
syringeenableshigheraccuracyinsmall-amountpouring,and
|     | The relationship |     | between | the | pulse | length | and transferred |     |     |     |     |     |     |
| --- | ---------------- | --- | ------- | --- | ----- | ------ | --------------- | --- | --- | --- | --- | --- | --- |
largersyringesaresuitableforadifferentpurposethatrequires
volumeofwaterisshowninFig.6.Thelengthofthepulseand
moreamountofliquid.Sincethedesignoftheproposedpipette
transferredvolumeareinalinearrelationshipand1msdiffer-
|     |         |              |         |             |     |      |         | is freely | available under | the creative | commons | license, | users |
| --- | ------- | ------------ | ------- | ----------- | --- | ---- | ------- | --------- | --------------- | ------------ | ------- | -------- | ----- |
|     | ence in | pulse length | roughly | corresponds |     | with | 0.02 mL | of the    |                 |              |         |          |       |
caneasilysketchnewpipettesstartingfromourdesign.
transferredvolume.Thedetailedplotbetween1280and1290ms
|     |     |     |     |     |     |     |     | Sinceattachingand |     | replacingthosepartswitharobotarm |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------------------------------- | --- | --- | --- |
isshowninFig.7todemonstratethecalibrationprocess.The
makestherobotmovementcomplex,ourpipettecurrentlydoes
linearrelationshipstillholdsinthisplotandwecouldcalibrate
|     |                 |     |        |                 |     |         |           | not have | needles or | pipette | tips that would | help | to avoid |
| --- | --------------- | --- | ------ | --------------- | --- | ------- | --------- | -------- | ---------- | ------- | --------------- | ---- | -------- |
|     | the transferred |     | volume | by a resolution |     | of 0.02 | mL. Since | the      |            |         |                 |      |          |
contamination.Althoughwecanprepareaseparatepipettefor
absoluterandomerrorstayedalmostconstantvalueforallpulse
|     |          |              |        |       |           |     |          | each liquid, | this solution | is costly. | Extending | our | device to |
| --- | -------- | ------------ | ------ | ----- | --------- | --- | -------- | ------------ | ------------- | ---------- | --------- | --- | --------- |
|     | lengths, | the relative | random | error | increased |     | when the | target       |               |            |           |     |           |
handlemultipleliquidswithoutcross-contaminationispartof
|     | volume                                                | decreased, | e.g.,     | 5% for | 0.5 mL,    | 15%  | for 0.1 | mL. A          |              |     |     |     |     |
| --- | ----------------------------------------------------- | ---------- | --------- | ------ | ---------- | ---- | ------- | -------------- | ------------ | --- | --- | --- | --- |
|     | differentpipettewithasmallsyringemaybenecessaryforthe |            |           |        |            |      |         | ourfuturework. |              |     |     |     |     |
|     | precise                                               | handling   | of liquid | that   | is smaller | than | 10%     | of the         |              |     |     |     |     |
|     | nominalvolume.                                        |            |           |        |            |      |         | Data           | availability |     |     |     |     |
3.4 Effectofviscosity The design les and source code used in this paper can be
|     |     |     |     |     |     |     |     | found | at https://github.com/ac-rad/digital-pipette |     |     |     | (DOI: |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------------------------------------- | --- | --- | --- | ----- |
Table4showstheresultoftheevaluation.Theperformanceof
https://doi.org/10.5281/zenodo.7893805).
|     | the pipette | remained | stable | under | different | viscosities |     | and it |     |     |     |     |     |
| --- | ----------- | -------- | ------ | ----- | --------- | ----------- | --- | ------ | --- | --- | --- | --- | --- |
wasconsistentwithacommercialmicropipetteandthevalues
expected from the literature. For example, at 40% concentra- Author contributions
|     | tion, our | digital | pipette | showed | a −0.12% | deviation | from | the |     |     |     |     |     |
| --- | --------- | ------- | ------- | ------ | -------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
target value on average, whereas the commercial micropipette Conceptualization, N. Y., K. D., A. G., A. A.-G.; methodology,
hada−0.68%deviation.Thisresultsuggeststhattheproposed N.Y.;soware,N.Y.;resources:N.Y.;writing–originaldra,
pipette can support various liquids with a wide range of N.Y.;writing–review&editing,K.D.,M.G.V.,A.G.,andA.A.-
|     | viscosity. |     |     |     |     |     |     | G.,fundingacquisition,A.A.-G. |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
1750 | DigitalDiscovery,2023,2,1745–1751 ©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
| Paper |     |     |     |     |     |     |     |     | DigitalDiscovery |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
Conflicts
of interest 8 B.Wijnen,E.J.Hunt,G.C.AnzaloneandJ.M.Pearce,PLoS
One,2014,9,e107216.
Therearenoconictstodeclare. M.S.CubberleyandW.A.Hess,J.Chem.Educ.,2017,94,72–
9
74.
| Acknowledgements |                  |            |     |                   | 10 A.Samokhin,J.Anal.Chem.,2020,75,416–421. |           |           |        |                  |     |
| ---------------- | ---------------- | ---------- | --- | ----------------- | ------------------------------------------- | --------- | --------- | ------ | ---------------- | --- |
|                  |                  |            |     |                   | 11 A. Gervasi,                              | P. Cardol | and P. E. | Meyer, | HardwareX, 2021, | 9,  |
| We thank         | the Acceleration | Consortium | for | nancial support, | e00199.                                     |           |           |        |                  |     |
Sebastian Arellano-Rubach and Kevin Angers for helping with 12 F.Barthels,U.Barthels,M.SchwickertandT.Schirmeister,
graphics, and Florian Shkurtifor the useful discussions. N.Y. SLASTechnol.,2020,25,190–199.
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
thanksthesupportfromtheNSERC-GoogleIndustrialResearch 13 R. Keesey, R. LeSuer and J. Schrier, HardwareX, 2022, 12,
 .MA 53:82:2 6202/32/1 no dedaolnwoD .3202 rebotcO 40 no dehsilbuP .elcitrA sseccA nepO
| ChairAward(IRCPJ547644-18). |     |     |     |     | e00319. |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
14 J.X.-Y.Lim,D.Leow,Q.-C.PhamandC.-H.Tan,IEEETrans.
| References |     |     |     |     | Autom.Sci.Eng.,2020,18,2185–2190. |             |            |     |                  |     |
| ---------- | --- | --- | --- | --- | --------------------------------- | ----------- | ---------- | --- | ---------------- | --- |
|            |     |     |     |     | 15 M. D.                          | Brennan, F. | F. Bokhari | and | D. T. Eddington, |     |
1 M. Seifrid, R. Pollice, A. Aguilar-Granda, Z. Morgan Chan, Micromachines,2018,9,191.
| K. Hotta, | C. T. Ser, | J. Vestfrid, | T. C. | Wu and A. Aspuru- |                  |           |           |     |                   |     |
| --------- | ---------- | ------------ | ----- | ----------------- | ---------------- | --------- | --------- | --- | ----------------- | --- |
|           |            |              |       |                   | 16 S. Chinchane, | H. Kadam, | K. Mowade |     | and J. M. Pearce, | J.  |
Guzik,Acc.Chem.Res.,2022,55,2454–2466.
OpenHardw.,2022,6,1.
2 M.AbolhasaniandE.Kumacheva,Nat.Synth.,2023,1–10. J.Bravo-Martinez,HardwareX,2018,3,110–116.
17
3 N. Yoshikawa, A. Z. Li, K. Darvish, Y. Zhao, H. Xu, 18 International Organization for Standardization, Piston-
A. Kuramshin, A. Aspuru-Guzik, A. Garg and F. Shkurti, operated volumetric apparatus – part 6: gravimetric reference
| arXiv, 2023,      | preprint, | arxiv:2212.09672v2, |     | DOI: 10.48550/ |                       |           |         |               |            |     |
| ----------------- | --------- | ------------------- | --- | -------------- | --------------------- | --------- | ------- | ------------- | ---------- | --- |
|                   |           |                     |     |                | measurement           | procedure | for the | determination | of volume, | ISO |
| arXiv.2212.09672. |           |                     |     |                | 8655-6:2022(en),2022. |           |         |               |            |     |
4 D. Knobbe, H. Zwirnmann, M. Eckhoff and S. Haddadin, 19 International Organization for Standardization, Piston-
–
2022 IEEE/RSJ International Conference on Intelligent Robots operated volumetric apparatus part 2: pipettes, ISO 8655-
| andSystems(IROS),2022,pp.2335–2342. |     |     |     |     | 2:2022(en),2022. |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
5 J.Zhang,W.Wan,N.Tanaka,M.FujitaandK.Harada,arXiv,
|     |     |     |     |     | 20 CRC Handbook | of Chemistry | and | Physics, | ed. J. R. Rumble, |     |
| --- | --- | --- | --- | --- | --------------- | ------------ | --- | -------- | ----------------- | --- |
2022, preprint, arxiv:2207.01214, DOI: 10.48550/ CRC Press/Taylor & Francis, Boca Raton, FL, 103rd edn
| arXiv.2207.01214. |     |     |     |     | (InternetVersion2022),2022. |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
6 T. Baden, A. M. Chagas, G. Gage, T. Marzullo, L. L. Prieto- 21 OT-2PipettesbyOpentrons,https://opentrons.com/products/
GodinoandT.Euler,PLoSBiol.,2015,13,e1002086. pipettes/,(accessed:June2023).
7 A.J.Capel,R.P.Rimington,M.P.LewisandS.D.Christie,
Nat.Rev.Chem.,2018,2,422–436.
©2023TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2023,2,1745–1751 | 1751
