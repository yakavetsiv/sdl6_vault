---
source_note: "Papers/Paper - d5dd00336a.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/d5dd00336a.pdf"
converter: "microsoft/markitdown"
---
Digital
Discovery
| COMMIT |     |     |     |     |     |     |     |     |     | View Article Online |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- |
View Journal | View Issue
|     |     | Commit: |     | Digital |     | pipette: | open | hardware |     | for | liquid |     |
| --- | --- | ------- | --- | ------- | --- | -------- | ---- | -------- | --- | --- | ------ | --- |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT  transfer in self-driving laboratories
 .MA 60:43:2 6202/32/1 no dedaolnwoD .5202 rebmevoN 91 no dehsilbuP .elcitrA sseccA nepO
Citethis:DigitalDiscovery,2026,5,93
|     |     | Naruki | Yoshikawa,  |      | †*abc | Kevin Angers,      |     | †a Kourosh        | Darvish, | abe |     |     |
| --- | --- | ------ | ----------- | ---- | ----- | ------------------ | --- | ----------------- | -------- | --- | --- | --- |
|     |     | Sargol | Okhovatian, |      | ad    | Dawn Bannerman,    |     | ad Ilya Yakavets, |          | ae  |     |     |
|     |     | Milica | Radisic     | *ade | and   | Ala´n Aspuru-Guzik |     | *abefg            |          |     |     |     |
Preciseliquidhandlingisanessentialoperationforself-drivinglaboratories.In2023,weintroducedthe
digital pipette, a low-cost, 3D-printed device that enables accurate liquid transfer by robotic arms.
However,theinitialversionlackedmechanismstopreventcross-contaminationwhenhandlingmultiple
Received31stJuly2025
Accepted7thNovember2025 liquids. In this commit paper, we present the digital pipette v2, an updated design that mitigates
contaminationriskbyallowingroboticarmstoexchangepipettetips.Thenewhardwareachievesliquid
DOI:10.1039/d5dd00336a handlingaccuracywithinthepermissibleerrorrangedefinedbyISO8655-2,supportingabroaderrange
| rsc.li/digitaldiscovery |     | ofexperimentsinvolvingmultipleliquids. |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oen
1 Introduction pipettes.4,5 These systems employ customized end-
|     |     |     |     |     |     | effectors,     | which | limit the robotic |     | arm's versatility | for          | other |
| --- | --- | --- | --- | --- | --- | -------------- | ----- | ----------------- | --- | ----------------- | ------------ | ----- |
|     |     |     |     |     |     | tasks, because |       | manual pipettes   | are | not suitable      | for standard |       |
Self-drivinglaboratories(SDLs)1havebeenacceleratingthepace
two-ngered
of scientic discovery by integrating automated experiments robot grippers, due to their shape and control
with articial intelligence (AI) for efficient decision-making. mechanism. While electronic pipettes with digital control
Given the central role of liquid handling in many experi- interfaces can serve as a potential alternative, most are ergo-
mental workows, the precise automation of this process is nomicallydesignedforhumanoperationanddonotintegrate
wellwithstandardrobotgrippers.Moreover,theircontrolAPIs
acriticalcomponentofSDLs.Consequently,variousautomated
areoenproprietary,whichhindersthedevelopmentofopen-
| liquid-handling | devices | have been developed |     | and | are now |     |     |     |     |     |     |     |
| --------------- | ------- | ------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
available commercially2 or as open-source hardware. Popular source control soware. The high cost of commercial elec-
liquid handling devices such as the OT-2 (Opentrons) and tronic pipettes further limits their adoption in budget-
Science Jubilee3 perform automated pipetting within conned conscious laboratories. Although several open-source liquid
|              |              |             |       |         |     | handling | tools | have been developed |     | for gantry-type | robots,6,7 |     |
| ------------ | ------------ | ----------- | ----- | ------- | --- | -------- | ----- | ------------------- | --- | --------------- | ---------- | --- |
| spaces using | gantry-based | mechanisms. | These | systems |     | are      |       |                     |     |                 |            |     |
typically limited to vertical pipetting at xed positions on integratingthemwithroboticarmsremainschallenging.
standardwellplates.Whiletheyareeffectiveformanyroutine Toaddresstheseproblems,weintroducedourdigitalpipette
experiments,someworkowsrequiremoreadvancedpipetting
in2023.8Thedeviceincorporatesalow-costcommercialsyringe
capabilities. For example, 3D cell culture demands delicate and a linear actuator to control its plunger within a at-sided
|     |     |     |     |     |     | enclosure, | enabling | precise | liquid handling | through | electrical |     |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | ------- | --------------- | ------- | ---------- | --- |
motiontominimizemechanicalstressduringpipetting,aswell
asangledpipettingtoreachthebottomedgesofcultureplates. signalsandeliminatingtheneedfordexterousmanipulations.
Pipettingontonon-standardordynamictargets,suchasplants Its simple design has facilitated adoption beyond the original
or small animals, necessitates real-time, computer vision- developmentteam,suchasintegrationintotheScienceJubilee
guidedfeedbacktoensureaccurateliquidplacement. platform.9 A major limitation of the initial version was its
Torealizemoreexibleliquidhandling,recentstudieshave inability to handle multiple liquids without risking cross-
explored the use of robotic arms equipped with manual contamination. Although disposable pipette tips are
|     |     |     |     |     |     | commonly | used | to prevent | contamination, | the | design | of the |
| --- | --- | --- | --- | --- | --- | -------- | ---- | ---------- | -------------- | --- | ------ | ------ |
commercialsyringewasincompatiblewiththesetips.
aUniversityofToronto,Toronto,ON,Canada.E-mail:yoshikawa.naruki@tmd.ac.jp;
Thiscommitpaperpresentsthedigitalpipettev2,updatedto
m.radisic@utoronto.ca;alan@aspuru.com
|     |     |     |     |     |     | handle multiple |     | liquids without |     | contamination | by  | using |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | --- | ------------- | --- | ----- |
bVectorInstitute,Toronto,ON,Canada
cInstituteofScienceTokyo,Tokyo,Japan disposable pipette tips (Fig. 1). We replaced the commercial
dTorontoGeneralHealthResearchInstitute,Toronto,ON,Canada syringe with a 3D-printed one compatible with commercial
|     |     |     |     |     |     | 10 mL pipette |     | tips. This modication |     | enables | the robot | to  |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------------- | --- | ------- | --------- | --- |
eAccelerationConsortium,Toronto,ON,Canada
fCanadianInstituteforAdvancedResearch,Toronto,ON,Canada handlemultipleliquidswithoutcontamination,broadeningthe
gNVIDIA,Toronto,ON,Canada range of possible experiments. Detailed descriptions of the
†Theseauthorscontributedequallytothiswork.
©2026TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2026,5,93–97 | 93

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     | Commit |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
 .MA 60:43:2 6202/32/1 no dedaolnwoD .5202 rebmevoN 91 no dehsilbuP .elcitrA sseccA nepO
Fig.1 Functionalitiesofthedigitalpipettev2.Itenablesliquidhandlingwithoutcross-contaminationusingdisposablepipettetips.Tipscanbe
attachedfromatiprackanddetachedusinganexternaltipremover.
updateddesignanditsexperimentalevaluationareprovidedin original version was a positive (direct) displacement (Type D)
| thefollowingsections.Thedatainthispaperarealsoshownin |     |     |     | pipette. |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
ourotherworkintroducingtheapplicationofthishardware.10 To keep the syringe airtight, we used a stereolithography
|     |     |     |     | apparatus     | (SLA) printer,   | which enables |     | more precise | printing      |
| --- | --- | --- | --- | ------------- | ---------------- | ------------- | --- | ------------ | ------------- |
|     |     |     |     | than low-cost | fused deposition | modeling      |     | (FDM)        | printers. The |
2 Design
|     |     |     |     | head of | the syringe barrel | (Fig. 2(c)) | is designed |     | to accommo- |
| --- | --- | --- | --- | ------- | ------------------ | ----------- | ----------- | --- | ----------- |
dateapipettetip(BRANDpipettetips,volume1–10mL,Sigma-
2.1 Pipettedesign
|     |     |     |     | Aldrich). | To keep the overall | length | of  | the device | short, the |
| --- | --- | --- | --- | --------- | ------------------- | ------ | --- | ---------- | ---------- |
Thedigitalpipettev2consistsoffour3D-printedcomponents:
radiusofthebarrelisdesignedtocoverthenominalvolume(10
| the platform, | syringe, cover, | and plunger. | A photo | of the |     |     |     |     |     |
| ------------- | --------------- | ------------ | ------- | ------ | --- | --- | --- | --- | --- |
mL)within5cmtoenabletheuseofasmallerlinearactuator
assembledpipettealongsidetheCADmodelsisshowninFig.2.
thantheoneusedintheoriginalversion.Theplunger(Fig.2(d))
Themostsignicantdifferencefromtheoriginalversionisthe
hasagroovetoattachanO-ringtoensureanairtightsealwithin
useofa3D-printedsyringedesignedtoaccommodateapipette
|                  |                 |         |               | the syringe | piece. Grease | (MOLYKOTE |     | High-Vacuum | Grease, |
| ---------------- | --------------- | ------- | ------------- | ----------- | ------------- | --------- | --- | ----------- | ------- |
| tip. As a result | of this change, | the new | version falls | into the    |               |           |     |             |         |
DuPont)isusedtomaintainanairtightconnectionbetweenthe
categoryofanairdisplacement(TypeA)pipette,11whereasthe
|     |     |     |     | pipette | tip and the syringe | body, | as well | as the | O-ring and |
| --- | --- | --- | --- | ------- | ------------------- | ----- | ------- | ------ | ---------- |
syringebarrel.Alinearactuatorwithastrokeof5cm(L16-50-63-
6-R,Actuonix),securedtotheplatform(Fig.2(b))usingscrews
|     |     |     |     | and a mounting | bracket,           | pulls | on the     | plunger         | to generate |
| --- | --- | --- | --- | -------------- | ------------------ | ----- | ---------- | --------------- | ----------- |
|     |     |     |     | suction        | inside the pipette | tip.  | An Arduino | microcontroller |             |
interfaceswiththerobotworkstationviaUSB-serialcommuni-
cationtocontrolthelinearactuator,enablingoperationofthe
pipetteusingastandardrobotgripperwithoutextensivehard-
waremodications.Thecover(Fig.2(e))holdsthesyringetothe
|     |     |     |     | platform | and is xed   | with tape   | to ensure | stability. | The 3D     |
| --- | --- | --- | --- | -------- | ------------- | ----------- | --------- | ---------- | ---------- |
|     |     |     |     | models   | were designed | with Fusion | 360       | (Autodesk  | Inc.). The |
platformandthecoverwereprintedwithwhiteANYCUBICPLA
|                  |                  |                 |           | using a | KP3S printer       | (KINGROON | Tech    | Co., Ltd), | and the  |
| ---------------- | ---------------- | --------------- | --------- | ------- | ------------------ | --------- | ------- | ---------- | -------- |
| Fig. 2 (a) Photo | of the assembled | digital pipette | v2. (b–e) | 3D CAD  |                    |           |         |            |          |
|                  |                  |                 |           | syringe | and plunger pieces | were      | printed | with Clear | Resin V4 |
modelsofthedigitalpipettev2components:(b)platform,(c)syringe
|     |     |     |     | (Formlabs | Inc.) using a | Form 3L | printer | (Formlabs | Inc.). The |
| --- | --- | --- | --- | --------- | ------------- | ------- | ------- | --------- | ---------- |
barrel,(d)plunger,and(e)cover.
94 | DigitalDiscovery,2026,5,93–97 ©2026TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
|     | Commit |     |     |     |     |     |     |     |     |     |     |     |     | DigitalDiscovery |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
effort
Table1 Costanalysisofourproposeddigitalpipettev2 pipetting systems. To reduce the calibration and
improvepositioningexibility,wedevelopedaforce-feedback-
|     | Parts |     |     |     |     |     | Price(USD) |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
basedpositioningsysteminwhichtherobotmovesthepipette
alongaspiraltrajectorywhilemonitoringtheforceattheend
|     | Linearactuator(ActuonixL16-50-63-6-R)         |     |     |     |     |     | 70  |     |          |           |             |           |     |            |             |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----------- | --------- | --- | ---------- | ----------- |
|     |                                               |     |     |     |     |     |     |     | effector | to locate | the correct | insertion |     | point. For | pipette tip |
|     | Est.3DprintingcostforPLAparts(platform,cover) |     |     |     |     |     | 35  |     |          |           |             |           |     |            |             |
xed
Est.3Dprintingcostforresinparts(syringe,plunger) 125 removal, the robot moves to a position to hook the
Electronicparts(Arduino,cables,connectors) 40 pipettetipontotheremoverandthenpullsthepipetteupward
|     |     |     |     |     |     |     |     |     | to extract | the tip. | Further | details | are | provided | in our other |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------- | ------- | --- | -------- | ------------ |
work.10
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
|  .MA 60:43:2 6202/32/1 no dedaolnwoD .5202 rebmevoN 91 no dehsilbuP .elcitrA sseccA nepO | pipette  | can   | be assembled |          | in under | 10 minutes,  | excluding | the |              |     |     |     |     |     |     |
| ---------------------------------------------------------------------------------------- | -------- | ----- | ------------ | -------- | -------- | ------------ | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
|                                                                                          | printing | time, | with         | detailed | assembly | instructions | and       | CAD |              |     |     |     |     |     |     |
|                                                                                          |          |       |              |          |          |              |           |     | 3 Evaluation |     |     |     |     |     |     |
modelsavailableinourGitHubrepository(https://github.com/
ac-rad/digital-pipette-v2).
|     |     |                |     |           |           |           |                 |     | We evaluated  | the     | pipette's | liquid | dispensing | accuracy | using         |
| --- | --- | -------------- | --- | --------- | --------- | --------- | --------------- | --- | ------------- | ------- | --------- | ------ | ---------- | -------- | ------------- |
|     |     | The electrical |     | circuitis | unchanged | fromthe   | initialversion. |     |               |         |           |        |            |          |               |
|     |     |                |     |           |           |           |                 |     | a gravimetric | testing | procedure |        | described  | in the   | International |
|     | We  | use an         | Uno | 328 AVR   | Dev Board | (Creatron | Inc., Canada),  |     |               |         |           |        |            |          |               |
whichiscompatiblewiththeArduinoUnoRev3,tocontrolthe StandardonPiston-OperatedVolumetricApparatus(ISO8655-
|     |     |     |     |     |     |     |     |     | 6).12 In | this procedure, |     | the weight | of  | dispensed | volume was |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ---------- | --- | --------- | ---------- |
linearactuator.Theactuatorispoweredbya6VDCsupplyand
measuredusinga0.1mgprecisionbalance(AUX220Analytical
|     | communicates |     | with | the | controller | PC through | USB serial. | It  |     |     |     |     |     |     |     |
| --- | ------------ | --- | ---- | --- | ---------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
receivesa5VpulsesignalfromtheArduinothatdeterminesits Balance, Shimadzu), and the systematic and random errors
werecalculatedfromthemeandeliveredvolumeovermultiple
extensionlength.
|     |     |              |     |     |     |     |     |     | iterations | at target    | volumes | of          | 1 mL, 5 | mL, and 10       | mL. While |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ------- | ----------- | ------- | ---------------- | --------- |
|     |     |              |     |     |     |     |     |     | a robotic  | arm operated |         | the pipette | in      | this evaluation, | other     |
|     | 2.2 | Costanalysis |     |     |     |     |     |     |            |              |         |             |         |                  |           |
detailsoftheevaluationfollowedtheoriginalpaper.8Basedon
Theapproximatepricesforthecomponentsusedtobuildthe
|     |     |     |     |     |     |     |     |     | the experimental |     | conditions |     | (temperature | 23.4 | °C and air |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --- | ------------ | ---- | ---------- |
digitalpipettev2areshowninTable1.The3Dprintingprices
pressure100.4kPa),aZcorrectionfactorof1.0036wasusedfor
|     | were | estimated |     | using | online printing | services | (Xometry, |     | calculation. |     |     |     |     |     |     |
| --- | ---- | --------- | --- | ----- | --------------- | -------- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Shapeways),whicharelikelytobehigherthantheactualcost
|     |     |     |     |     |     |     |     |     | Table | 2 summarizes | the | results, | reporting | the | mean deliv- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | -------- | --------- | --- | ----------- |
(cid:1)
of the raw materials. Our pipette can be built for under 300 eredvolumeV ,thesystematicerrorh,andtherandomerrorC .
|     |     |     |     |     |     |     |     |     |     |     |     |     | s   |     | v   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
USD, which falls within the typical price range of laboratory signicantly
|     |     |     |     |     |     |     |     |     | The observed | errors | were |     |     | below the | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ---- | --- | --- | --------- | ------- |
micropipettes,whichgenerallycostbetween50and350USD.
|     |     |     |     |     |     |     |     |     | permissible | limits | dened | by  | ISO 8655-2,11 | indicating | high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------ | --- | ------------- | ---------- | ---- |
repeatabilityofthedigitalpipettev2.
|     | 2.3 | Attachmentanddetachmentofpipettetips |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Inaddition,fourexperiencedhumanoperatorsperformed
|     |     |        |         |          |               |      |               |     | the same | gravimetric | testing | procedure |     | to compare | the reli- |
| --- | --- | ------ | ------- | -------- | ------------- | ---- | ------------- | --- | -------- | ----------- | ------- | --------- | --- | ---------- | --------- |
|     | We  | used a | pipette | tip rack | for attaching | tips | and a pipette | tip |          |             |         |           |     |            |           |
remover for detaching them (Fig. 3). Both are printed using abilityofthedigitalpipettev2withmanualpipetting(Fig.4).
a Form 3L printer with Formlabs Rigid 10 K Resin. Their To evaluate the pipetting performance when handling small
|     |     |     |     |     |     |     |     |     | volumes, | we tested | dispensing |     | at 0.2 | mL, 1 mL, | and 5 mL. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | --- | ------ | --------- | --------- |
designsarealsoavailableinthesameGitHubrepository.
ve
Attaching pipette tips requires highly accurate alignment, Each operator performed replicates at each volume. For
|     |       |              |     |         |             |     |         |          | the0.2mLand1mLvolumes, |     |     |     | astandardP1000pipettewas |     |     |
| --- | ----- | ------------ | --- | ------- | ----------- | --- | ------- | -------- | ---------------------- | --- | --- | --- | ------------------------ | --- | --- |
|     | which | necessitates |     | careful | calibration |     | in many | existing |                        |     |     |     |                          |     |     |
usedasthehumanbaseline,whilea5mLserologicalpipette
|     |     |     |     |     |     |     |     |     | was used  | for the  | 5 mL volume. |     | Operators | were instructed | to        |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------------ | --- | --------- | --------------- | --------- |
|     |     |     |     |     |     |     |     |     | carefully | aspirate | the desired  |     | volume    | and dispense    | it fully, |
mirroringtheprocedurefollowedbythedigitalpipettev2.For
|     |     |     |     |     |     |     |     |     | Table2 | Resultsofthegravimetrictest.Thesystematicerrorh |     |     |     |     | andthe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------------------------------------------- | --- | --- | --- | --- | ------ |
s
|     |     |     |     |     |     |     |     |     | randomerrorC | obtainedfromthegravimetrictestareshownwiththe |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------------------------------------------- | --- | --- | --- | --- | --- |
v
|     |     |     |     |     |     |     |     |     | values of | the original | version8 | and | the maximum | permissible | errors |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | -------- | --- | ----------- | ----------- | ------ |
definedbyISO8655-2
(cid:1)
|     |     |     |     |     |     |     |     |     | Volume(mL) | Device/standard |     |     | V (mL) | h   | (%) C (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | --- | ------ | --- | --------- |
|     |     |     |     |     |     |     |     |     |            |                 |     |     |        | s   | v         |
−0.09
|     |     |     |     |     |     |     |     |     | 10.0 | Digitalpipettev2 |     |     | 9.9909  |      | 0.10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------------- | --- | --- | ------- | ---- | ---- |
|     |     |     |     |     |     |     |     |     |      | Digitalpipettev1 |     |     | 10.0083 | 0.08 | 0.07 |
—
|     |     |     |     |     |     |     |     |     |     | ISO8655 |     |     |     | 0.6 | 0.3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
−0.10
|     |     |     |     |     |     |     |     |     | 5.0 | Digitalpipettev2 |     |     | 4.9949 |     | 0.16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------ | --- | ---- |
−0.16
|     |     |     |     |     |     |     |     |     |     | Digitalpipettev1 |     |     | 4.9922 |     | 0.14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------ | --- | ---- |
—
|     |     |     |     |     |     |     |     |     |     | ISO8655 |     |     |     | 1.2 | 0.6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
−0.49
|     |     |     |     |     |     |     |     |     | 1.0 | Digitalpipettev2 |     |     | 0.9951 |     | 0.58 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------ | --- | ---- |
−1.1
Fig.3 CADmodelsof(a)thepipettetiprack,and(b)thepipettetip Digitalpipettev1 0.9887 0.76
—
|     | remover. |     |     |     |     |     |     |     |     | ISO8655 |     |     |     | 6.0 | 3.0 |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
©2026TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2026,5,93–97 | 95

View Article Online
| DigitalDiscovery |     |     |     |     |     |     |     |     |     |     |     |     |     | Commit |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
 .MA 60:43:2 6202/32/1 no dedaolnwoD .5202 rebmevoN 91 no dehsilbuP .elcitrA sseccA nepO
|     |     |     |     |     |     |     | Fig.6 Pipettecalibrationplotforsixpulselengthsbetween1235and |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
1242ms,usedtocalibratethepipettefor10mLexpulsion.
Fig.4 Gravimetriccomparisonofthedigitalpipettev2withhuman
pipettors,forvolumesof0.2mL,1mL,and5mL.ALevene'stestwas 4 Conclusions
conductedtocomparethevariancesbetweenthetwogroups(digital
pipettev2vs.human). Inthiscommitpaper,wepresentedthedigitalpipettev2,which
supportstheattachmentanddetachmentofpipettetipsbyusing
|         |                    |       |      |               |     |         | a 3D-printed | syringe. | The     | new     | design              | enables | robotic | arms to |
| ------- | ------------------ | ----- | ---- | ------------- | --- | ------- | ------------ | -------- | ------- | ------- | ------------------- | ------- | ------- | ------- |
| the 0.2 | mL and 1 mL tests, | there | were | no signicant |     | differ- |              |          |         |         |                     |         |         |         |
|         |                    |       |      |               |     |         | handle       | multiple | liquids | without | cross-contamination |         |         | while   |
encesinvariancebetweenthetwogroups(p=0.8754andp=
maintainingtheaccuracyspeciedbyinternationalstandards.
0.6533, respectively). However, for the 5 mL test, the digital Although the new design broadens the scope of supported
|     |     | signicantly |     |     |     |     | =   |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pipette v2 demonstrated lower variance (p experiments,severallimitationsremain.First,thecurrentsyringe
0.0046). requires grease between the pipette tip and the syringe to
maintainanairtightseal,unlikemostcommercialpipettes.This
3.1 Calibration isduetosurfaceroughnessresultingfromthelimitedprecision
|     |     |     |     |     |     |     | of 3D printing. | The | need | for | greasing | increases | maintenance |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---- | --- | -------- | --------- | ----------- | --- |
Thelinearactuatorinthedigitalpipettev2isoperatedbya5V
costs.Inthefuture,alternativefabricationmethods,suchasCNC
| signal,    | where the pulse  | length  | determines |        | the actuator's |         |                                 |     |            |     |        |              |           |         |
| ---------- | ---------------- | ------- | ---------- | ------ | -------------- | ------- | ------------------------------- | --- | ---------- | --- | ------ | ------------ | --------- | ------- |
|            |                  |         |            |        |                |         | machining,                      | may | be adopted | to  | obtain | smoother     | surfaces, | as      |
| extension. | The relationship | between | pulse      | length | (in            | ms) and |                                 |     |            |     |        |              |           |         |
|            |                  |         |            |        |                |         | demonstratedinthedevelopmentofa |     |            |     |        | tipholderfor |           | OpenLab |
| delivered  | volume (in mL)   | was     | measured   | aer   | assembling     | the     |                                 |     |            |     |        |              |           |         |
oen
|     |     |     |     |     |     |     | Automata.13 | Second, | biochemical |     | experiments |     |     | involve |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ----------- | --- | ----------- | --- | --- | ------- |
pipette,andtheoptimalpulselengthforthetargetvolumeswas
|            |                    |     |             |       |        |     | handling | very small | liquid | volumes | around |     | 1 mL. | While the |
| ---------- | ------------------ | --- | ----------- | ----- | ------ | --- | -------- | ---------- | ------ | ------- | ------ | --- | ----- | --------- |
| determined | from the resulting |     | calibration | plots | before | the |          |            |        |         |        |     |       |           |
nominalvolumeofthedigitalpipettecanbeadjustedbymodi-
| evaluation. | The calibration | should | be  | performed | regularly |     | to  |     |     |     |     |     |     |     |
| ----------- | --------------- | ------ | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fyingthesyringedesign,achievingmL-levelaccuracymayrequire
| maintain | high accuracy. | Example | calibration |     | plots | for the |                            |     |     |          |     |               |     |           |
| -------- | -------------- | ------- | ----------- | --- | ----- | ------- | -------------------------- | --- | --- | -------- | --- | ------------- | --- | --------- |
|          |                |         |             |     |       |         | higher-precisionactuators. |     |     | Finally, | the | currentsystem |     | relies on |
10mLtargetvolumeareshowninFig.5and6.
|     |     |     |     |     |     |     | an external         | pipette | tip      | remover,   | whereas    | most  | commercial |        |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ------- | -------- | ---------- | ---------- | ----- | ---------- | ------ |
|     |     |     |     |     |     |     | micropipettes       | are     | equipped | with       | a built-in | tip   | ejection   | mecha- |
|     |     |     |     |     |     |     | nism. Incorporating |         | such     | a function |            | would | require    | a more |
complexmechanicaldesignthatcanbeactuatedbyanexternal
|     |     |     |     |     |     |     | signal.Wewill | continue |     | developing | open | hardwarefor |     | precise, |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | ---------- | ---- | ----------- | --- | -------- |
automatedliquidhandlingwithroboticarms.
|     |     |     |     |     |     |     | Author                   | contributions |     |              |     |         |                 |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | ------------- | --- | ------------ | --- | ------- | --------------- | --- |
|     |     |     |     |     |     |     | N. Y: conceptualization, |               |     | methodology, |     | writing | – originaldra. |     |
K.A:investigation,visualization,writing–originaldra.K.D.:
projectadministration,writing–review&editing.S.O.,D.B.,I.
|     |     |     |     |     |     |     | Y.: investigation, |     | writing | – review | & editing. |     | M. R., | A. A. G.: |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------- | -------- | ---------- | --- | ------ | --------- |
supervision,writing–review&editing,fundingacquisition.
Conflicts
of interest
Fig.5 Pipettecalibrationplotforsixpulselengthsbetween1250and
Therearenoconictstodeclare.
1750ms.Errorbarsareincludedbutnotvisible.
96 | DigitalDiscovery,2026,5,93–97 ©2026TheAuthor(s).PublishedbytheRoyalSocietyofChemistry

View Article Online
| Commit |     |     |     |     |     |     | DigitalDiscovery |     |
| ------ | --- | --- | --- | --- | --- | --- | ---------------- | --- |
Data availability 6 10cc Syringe Tool, https://jubilee3d.com/index.php?
title=10cc_Syringe_Tool,accessed,October12,2025.
les
The design and source code used in this paper can be 7 ElectronicMicropipettes,https://docs.openlabautomata.xyz/
found at https://github.com/ac-rad/digital-pipette-v2 (DOI: Mini-Docs/Tools/Micropipetas/,accessed,October12,2025.
|     |     |     |     | 8 N. Yoshikawa, | K. Darvish, | M. G. | Vakili, A. | Garg and |
| --- | --- | --- | --- | --------------- | ----------- | ----- | ---------- | -------- |
https://doi.org/10.5281/zenodo.17549134).
A.Aspuru-Guzik,DigitalDiscovery,2023,2,1745–1751.
Acknowledgements 9 B. Pelkie, S. Baird, E. Aissi, K. Aspuru-Takata, Y. Cao,
|     |     |     |     | J. H. Chang, | K. Gambhir, | W. S. Hale, | L. Hao, C. | Hattrick, |
| --- | --- | --- | --- | ------------ | ----------- | ----------- | ---------- | --------- |
This research was undertaken thanks in part to funding J. Hein, D. Luo, O. Melville, M. Ngan, L. L. B. Nyeland,
.ecneciL detropnU 0.3 noitubirttA snommoC evitaerC a rednu desnecil si elcitra sihT
 .MA 60:43:2 6202/32/1 no dedaolnwoD .5202 rebmevoN 91 no dehsilbuP .elcitrA sseccA nepO providedtotheUniversityofToronto'sAccelerationConsortium N. Peek, M. Politi, E. E. Rajkumar, A. Siemenn,
fromtheCanadaFirstResearchExcellenceFund,grantnumber B. Subbaraman, S. Vasquez, J. Watchorn, W. Zhang,
CFREF-2022-00042.N.Y.issupportedbyJSPSKAKENHIGrant R. Ziskason, L. Pozzo, T. Buonassisi and T. Vegge,
NumberJP25K21333.S.O.issupportedbyNSERCCGS.
ChemRxiv,2025,DOI:10.26434/chemrxiv-2025-zhkrf.
|     |     |     |     | 10 K. Angers, | K. Darvish, | N. Yoshikawa, | S. Okhovatian, |     |
| --- | --- | --- | --- | ------------- | ----------- | ------------- | -------------- | --- |
References D. Bannerman, I. Yakavets, F. Shkurti, A. Aspuru-Guzik
|     |     |     |     | and M. | Radisic, | arXiv, 2025. | DOI: | 10.48550/ |
| --- | --- | --- | --- | ------ | -------- | ------------ | ---- | --------- |
1 G.Tom,S.P.Schmid,S.G.Baird,Y.Cao,K.Darvish,H.Hao, arXiv.2505.14941.
| S. Lo, | S. Pablo-Garc´ıa, | E. M. Rajaonson, | M. Skreta,        |                  |              |                      |     |         |
| ------ | ----------------- | ---------------- | ----------------- | ---------------- | ------------ | -------------------- | --- | ------- |
|        |                   |                  |                   | 11 International | Organization | for Standardization, |     | Piston- |
|        |                   |                  | Strieth-Kalthoff, |                  |              | –                    |     |         |
N. Yoshikawa, S. Corapi, G. D. Akkoc, F. operated volumetric apparatus Part 2: Pipettes,
M. Seifrid and A. Aspuru-Guzik, Chem. Rev., 2024, 124, International Organization for Standardization Technical
9633–9732.
ReportISO8655-2:2022(en),2022.
2 M.A.Torres-Acosta,G.J.LyeandD.Dikicioglu,Biochem.Eng. 12 International Organization for Standardization, Piston-
J.,2022,188,108713. operated volumetric apparatus – Part 6: Gravimetric reference
3 Science Jubilee, https://github.com/machineagency/science- measurement procedure for the determination of volume,
jubilee,accessed,October12,2025. International Organization for Standardization Technical
| 4 D. Knobbe, | H. Zwirnmann, | M. Eckhoff | and S. Haddadin, |     |     |     |     |     |
| ------------ | ------------- | ---------- | ---------------- | --- | --- | --- | --- | --- |
ReportISO8655-6:2022(en),2022.
IEEE/RSJ International Conference on Intelligent Robots and 13 Tip Holder, https://docs.openlabautomata.xyz/Mini-Docs/
Systems (IROS), 2022. DOI: 10.1109/ Tools/Micropipette/Tip-holder/,accessed,October12,2025.
IROS47612.2022.9981636.
| 5 J. Zhang, | W. Wan, N. | Tanaka, M. Fujita, | K. Takahashi and |     |     |     |     |     |
| ----------- | ---------- | ------------------ | ---------------- | --- | --- | --- | --- | --- |
K.Harada,IEEETrans.Autom.Sci.Eng.,2024,21,5503–5522.
©2026TheAuthor(s).PublishedbytheRoyalSocietyofChemistry DigitalDiscovery,2026,5,93–97 | 97
