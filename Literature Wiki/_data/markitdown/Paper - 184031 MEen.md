---
tags:
  - literature
  - type/paper
type: literature-note
source_note: "Papers/Paper - 184031 MEen.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/184031_MEen.pdf"
converter: "microsoft/markitdown"
---
HAMILTON Heater Shaker
User Manual

          624175/03         December 2010

DOMINIQUE DUTSCHER SASImportant Notice

This guide may not be used or reproduced in any way whatsoever without the express
written consent of Hamilton Bonaduz AG.

Copyright  2000 - 2010 Hamilton Bonaduz AG, All Rights Reserved.
MICROLAB® is a registered trademark of Hamilton Bonaduz AG.

Microtiter is a registered trademark of Dynatech Laboratories.

Microsoft Visual C++ 2005 is a registered trademark of Microsoft Corporation

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

Table of Contents

1

1.1

1.2

1.3

General Information ....................................................................................... 4

About this Manual.......................................................................................................4

Intended Use of the HAMILTON Heater Shaker .......................................................4

Operation.....................................................................................................................5

1.4
Safety Precautions and Hazards ...............................................................................5
1.4.1  General Precautions ................................................................................................................... 5
1.4.2  Chemical Precautions................................................................................................................. 6
1.4.3  Electrical Safety Precautions...................................................................................................... 7
1.4.4  Hazards ...................................................................................................................................... 7
1.4.5  Disposal ...................................................................................................................................... 8
1.4.6  Contacting Hamilton ................................................................................................................... 8

2

Description of the HAMILTON Heater Shaker.............................................. 9

2.1

General description of the HAMILTON Heater Shaker ............................................9

2.2
Installation...................................................................................................................9
2.2.1  Up to two HHS via TCC .............................................................................................................. 9
2.2.2  Up to eight HHS via HSB and USB port ................................................................................... 10

2.3

2.4

3

Computer Requirements..........................................................................................11

Software Requirements............................................................................................11

HHS Library .................................................................................................. 12

3.1

The HAMILTON Heater Shaker commands ............................................................13

4

Programming the HAMILTON Heater Shaker ............................................ 16

4.1
Example 1: Controlling only one HAMILTON Heater Shaker................................17
4.1.1  Step by Step Analysis of Example 1......................................................................................... 17

4.2

Safety measures upon method abort .....................................................................21

4.3
Example 2: Controlling multiple HAMILTON Heater Shakers...............................22
4.3.1  Step by Step analysis of example 2 ......................................................................................... 23

4.4  Monitoring the performance of the HAMILTON Heater Shaker ............................27

5

6

7

7.1

7.2

8

A

B

Verification ................................................................................................... 29

Maintenance ................................................................................................. 29

Technical Specifications ............................................................................. 30

HAMILTON Heater Shaker........................................................................................30

HAMILTON Heater Shaker Box (HSB).....................................................................32

Appendix....................................................................................................... 33

Ordering Information................................................................................................33

Glossary ....................................................................................................................35

624175/03

3

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

1  General Information

You  should  read  through  the  entire  manual  before  beginning  to  operate  your  HAMILTON
Heater Shaker (HHS). This first chapter should be read with particular attention. It contains
important  information  about  the  use  of  HHS.  For  further  information  on  your  ML  STAR
instrument, we recommend to read the documentation shipped with your MICROLAB STAR
Line instrument.

1.1  About this Manual

This manual is to help users to operate the HAMILTON Heater Shaker correctly and safely.

Warnings  and  notes  are  included  in  this  manual  to  emphasize  important  and  critical
instructions.  They  are  printed  in  italics,  begin  with  the  word  'Attention'  accompanied  by  the

 symbol, or the word ‘Note’ accompanied by the

 symbol, as appropriate.

[...]

Push buttons and their corresponding description.

“...”  Description for all kinds of entry fields, control fields, check boxes, lists, etc.

___  References to Manuals, figures, sections, etc.
HAMILTON’s MICROLAB® STAR, STARPlus and STARlet are in the following summarized as
ML STAR Line.

1.2

Intended Use of the HAMILTON Heater Shaker

The HHS is a compact module designed for operation on the ML STAR Line robotic pipetting
workstation.  It  is  not  suitable  as  stand  alone  product.  The  HHS  is  used  for  heating  and
shaking  of  standard  microtiter  plates  in  SBS  format  (Society  for  Biomolecular  Sciences).  In
order to get efficient and evenly distributed heating of plates, specific adapters are required.

NOTE

The HHS is only intended to be used in combination with the ML STAR Line. A
stand alone operation of the HHS is not foreseen.

624175/03

4

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

1.3  Operation

For operation of the HHS, a specific library is required (see chapter “HHS Library”).

NOTE

The maximum shaking speed of the HHS depends on the Orbit and the type of
labware used (see chapter “Technical Specifications”).

NOTE

An  efficient  heating  of  the  liquid  is  only  achieved  if  the  appropriate  adapter  for
the labware is used. The heating time and the maximum temperature, which can
be reached for the liquid inside the plate, is dependent on the amount of liquid,
the size / weight of the used labware, the size / weight of the used adapter and
the connection between the plate and the adapter.

1.4  Safety Precautions and Hazards

The  following  section  describes  the  main  safety  considerations,  electrical  and  biological,  in
operating this product, and the main hazards involved.

ATTENTION

Read the following safety notices carefully before using the HHS.

1.4.1  General Precautions

1.4.1.1

Instrument

Installation and Verification of the HHS have to be performed by trained service engineers.

For  repair  or  shipment,  the  HHS  must  be  decontaminated  if  it  was  in  a  laboratory
environment with infected or hazardous materials. The HHS must be repacked in the original
packaging.

Only  original  HHS-specific  parts  and  tools  may  be  used  with  the  HHS,  e.g.  adapters.
Commercially available liquid containers, such as microtiter plates and tubes, may of course
be used.

1.4.1.2  Operating the HAMILTON Heater Shaker

When  using  the  HHS,  Good  Laboratory  Practices  (GLP)  must  be  observed.  Suitable
protective  clothing,  safety  glasses  and  protective  gloves  must  be  worn,  particularly  when
dealing  with  a  malfunction  of  the  instrument  where  the  risk  of  contamination  from  spilled
liquids exists.

624175/03

5

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

1.4.1.3  Method Programming

Perform  test  runs  first  with  water  and  then  with  the  final  liquids,  prior  to  routine  use.  The
method has to be validated by the programmer.

ATTENTION

When  working  with  samples,  which  will  be  used  in  particularly  sensitive  tests,
take into account the evaporation that may occur while the HHS is running. Be
aware that heating of liquids will affect the pipetting process, as well as shaking
the labware can influence the precision of pipetting.

ATTENTION

When shaking labware, the speed has to be adjusted to the type of labware and
the volume within the labware to prevent cross-contamination due to spillages.

Further information on the maximum shaking speed for MTP and DWP can be found in the
chapter “Technical Specifications”.

1.4.1.4  Loading of Labware

The  appropriate  labware  can  either  be  loaded  manually  by  Hand  or  automatically  by  using
the  iSwap  or  the  CO-RE  Grip  from  the  ML  STAR  Line  instrument.  Or,  by  other  robotic
handling devices, which can reach the labware on the HHS device.

1.4.1.5  Work Routine

ATTENTION

Do not touch the HHS during run time and also not shortly after finishing a run,
as  it  might  be  hot.  Wait  until  the  HHS  has  cooled  down  to  room  temperature,
which can take up to 1 hour.

1.4.2  Chemical Precautions

If the HHS is used for toxic or irritant chemicals, the user is responsible to take appropriate
actions  for  protections.  This  is  especially  important  when  toxic  chemicals  can  evaporate
during the heating process. Flammable liquids must not be heated on the HHS as they might
cause a fire.

Evaporation  of  hazardous  liquids  can  cause  corrosion  of  the  ML  STAR  Line.  Use  a  lid  to
cover the labware or an extractor hood to protect the user and the instrument.

If  the  HHS  becomes  contaminated  with  biohazardous  or  chemical  material,  it  should  be
cleaned  and  decontaminated.  Wear  gloves  when  handling  with  a  contaminated  HHS.  Any
surfaces on which liquid is spilled must be decontaminated.

Do  not  use  disinfecting  materials,  which  contain  hypochlorite  (Javel  water,  Chlorox)  or
bleaching fluids.

624175/03

6

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

1.4.3  Electrical Safety Precautions

ATTENTION

Before  connecting  or  disconnecting  the  HHS  either  from  or  to  a  ML  STAR
instrument or Heater Shaker Box (HSB) make sure that the ML STAR or HSB is
switched  off.  Only  when  the  ML  STAR  or  the  HSB  is  switched  off  it  is  safe  to
connect  or disconnect HHS  devices.  Not  obeying  this  may  result  in  damage  of
the HHS.

1.4.4  Hazards

Explanation of warning and attention labels:

On the HHS device the following Labels are available

Hot Surface

Avoid contact of HHS. Surfaces are hot and may cause personal injury if touched.

Biohazard Warning

HHS  device  may  be  contaminated,  Good  Laboratory  Practices  (GLP)  must  be
observed.

PC / USB Connection

Use only the appropriate shielded cables. Signals can be interfered if using a total
cable length of more than 5m.

On the HSB device the following Labels are available

Power connection

Connect only to earth-grounded outlet

Biohazard Warning

HSB  device  may  be  contaminated,  Good  Laboratory  Practices  (GLP)  must  be
observed.

624175/03

7

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

1.4.5  Disposal

At the end of the instruments life cycle, please contact your local Hamilton representative
regarding disposal of the instrument.

The European Community requires from manufacturers to organize the disposal and waste
of electrical and electronic equipment (WEEE). For this reason, HAMILTON Bonaduz AG
took part to organize the disposal of STAR Line products through a European disposal
network. Please contact your local HAMILTON representative for further information about
the recycling procedure.

Otherwise local disposal regulations are to be observed.

1.4.6  Contacting Hamilton

Europe, Africa and Asia:

HAMILTON Bonaduz AG

CH-7402 Bonaduz / Switzerland

Americas, Far East and Pacific Rim:

HAMILTON Company
P.O. Box 10030

Reno, NV 89520-0012 USA

Phone

+41 81 660 60 60

Toll Free
Phone

+1 (800) 648-5950
+1 (775) 858-3000

HAMILTON Company URL

www.hamiltonrobotics.com
www.hamiltoncompany.com

624175/03

8

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

2  Description of the HAMILTON Heater Shaker

2.1  General description of the HAMILTON Heater Shaker

The HHS is designed to heat and / or shake standard microtiter plates in SBS format.

The maximum shaking speed depends on the labware used. For details, see chapter “HHS
Library”. Shaking can be performed clockwise or counter-clockwise.

Before heating or shaking is started, the plates are locked and positioned in the centre of the
HHS. When heating or shaking has finished the plates are unlocked and can then easily be
removed from the HHS.

The  HHS  can  be  heated  to  temperatures  up  to  105°C.  The  temperature  is  constantly
measured  by  two  sensors,  one  located  in  the  middle  and  one  at  the  edge  of  the  adapter
plate.

2.2

Installation

Generally; the HHS will be installed by trained service engineers.

Up  to  8  HHS  modules  can  be  integrated  into  one  ML  STAR  Line  instrument.  When
integrating  more  than  2  heater  shakers,  the  additional  Heater  Shaker  Box  is  required  for
control.

Up to 4 HHS have to be mounted onto one carrier baseplate for heater-shakers. Where HHS
for deepwell (archive) plates shall be positioned directly onto the carrier baseplate and HHS
for standard plates can be positioned rised up by using the HHS support block.

Note

Carrier base plate and support block have to be ordered separately.

For Ordering information see chapter “Appendix A“.

2.2.1  Up to two HHS via TCC

It  is  possible  to  integrate  one  or  two  HHS  directly  into  a  ML  STAR  instrument  (via  TCC
connector, see picture below).

Up to two HHS connected to the TCC connector of the Periphery Connector Board of the ML STAR
instrument

624175/03

9

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

2.2.2  Up to eight HHS via HSB and USB port

If more than two HHS are required, the Heater Shaker Box (HSB) is needed. One HHS (HHS
master)  is  connected  to  the  USB  port  of  the  PC  and  to  the  HSB  and  serves  as  master
module. In addition to the master HHS, up to seven additional HHS (HHS slave 1……7) can
be connected to the HSB. The HSB serves a power supply and as a signal distributor for all
the HHS slaves.

Up to eight HHS connected to the Heater Shaker Box and to the PC which is controlling the ML STAR
instrument

624175/03

10

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

2.3  Computer Requirements

The  PC  controlling  the  ML  STAR  Line  instrument  will  be  used  to  control  HHS  devices
installed on the ML STAR Line instrument.

2.4  Software Requirements

The HHS specific library “ HslHamHeaterShakerLib.hsl” will provide a set of commands to
control the HHS device.

The HHS library can be run with any of the following ML STAR Line Software Versions:











MICROLAB STAR IVD V3.2.3

MICROLAB STAR IVD V4.2.x

MICROLAB STAR IVD V4.3.x

MICROLAB STAR Venus one 4.2.x

MICROLAB® STAR Venus two 4.3.x

These Versions are referred as ML STAR Line Software in the following chapters. For further
information  please  consult  the  appropriate  “Operators  Manual”  available  with  your  ML
STARLine instrument.

624175/03

11

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

3  HHS Library

The HHS library provides several functions to control the HHS, such as shaking and heating
settings.  The  functions  can  be  integrated  into  standard  methods  of  the  ML  STAR  Line
instrument.

To  install  the  library  execute  the  file  “InstallHHSLibrary_Vx.x.exe”.  If  needed,  obtain  the
library, from your local HAMILTON representative.

Confirm the question that you want to install this addition. The heater shaker library will be
installed automatically.

NOTE

The library requires the following Microsoft Package, which will be installed
automatically during the setup procedure.

Microsoft Visual C++ 2005 Redistributable Package (x86)

In  order  to  use  the  library,  it  has  to  be  selected  in  the  Method  Editor.  Go  to  “Method”  →
“Libraries…” → “Add libraries” and select the file “HslHamHeaterShakerLib.hsl”.

624175/03

12

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

3.1  The HAMILTON Heater Shaker commands

The table below gives an overview of commands included in the HHS library:

Command

Icon

Action performed

Create Star Device

Creates  the  device  number  which  must  be  used  as
input parameter for each function of this library.

Create USB Device

Creates  the  device  number  which  must  be  used  as
input parameter for each function of this library.

Terminate

Start Shaker

Start All Shaker

Start Shaker Timed

Start All Shaker Timed

Wait For Shaker

The connection to the ML Star Line instrument and/or
USB device is terminated. Note that this function does
not stop the heating or shaking process of the heater
shaker.

This function starts the shaking process. If necessary,
the  heater  shaker  will  be  initialized.  Before  the
shaking  process  is  started,  the  plate  is  locked.
Shaking  has  to  be  stopped  by  the  “Stop  Shaker”
command.  Terminating  the  connection  will  not  stop
shaking.  However,  shaking  is  stopped  upon  method
abort.

Start  shaking  on  all  initialized  shakers.  Shakers  that
have  not  been  initialized  are  not  addressed.  The
plates are locked before the shaking process.

Start  shaking  for  an  indicated  time.  If  necessary,  the
heater  shaker  will  be  initialized.  Before  the  shaking
process  is  started,  the  plate  is  locked.  After  shaking,
the  plate
the
“SetPlateLock” function.

to  be  opened  with

lock  has

Start  shaking  on  all  initialized  heater  shakers  for  an
indicated  time.  The  plates  are  locked  before  the
shaking  process.  After  shaking,  the  plate  lock  has  to
be opened with the “SetPlateLock” function.

Wait  for  the  heater  shaker  to  finish.  The  plate  is
unlocked  after  shaking  has  been  stopped.  This
command  is  only  used  in  combination  with  “Start
Shaker Timed” or “Star All Shaker Timed”.

624175/03

13

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

Stop Shaker

Stop shaking and unlock plate.

Stop All Shaker

Stop shaking on all heater shakers. The plates will be
unlocked subsequently.

Set shaker parameter

Set  shaking  parameters,  such  as  shaking  direction,
shaking speed and acceleration.

Get Shaker Parameter

Get  shaking  parameters,  such  as  shaking  direction,
shaking speed and acceleration.

Start Temp Control

Wait for Temp Control

Start  temperature  control  on  the  heater  shaker (must
be  greater  than  ambient  temperature  plus  5°C).
Temperature  control  has  to  be  stopped  by  the  “Stop
Temp  Control”  function  or  will  be  constantly  on.
Terminating  the  connection  will  not  stop  heating.
However, heating is stopped upon method abort.

Wait  until  the  heater  shaker  has  reached  the  set
temperature.  This  function  will  wait  until  the  defined
temperature is reached and is stable for 180 seconds.
Only then, the method will continue.

Stop Temp Control

Stop temperature control of the heater shaker.

Get Temperature

Receive the current temperature of the heater shaker.

Set Temperature
Parameter

Get Temperature
Parameter

Get Temperature State

Send Firmware
Command

Set  parameters  for  temperature  control.  In  most
cases,  the  default  settings  can  be  used  and  this
function is not needed.

Receive the parameters for temperature control.

Get  the  status  of  the  temperature  control.  The
temperature  should  be  within  a  defined  temperature
range.

Send a firmware command to the heater shaker.

624175/03

14

DOMINIQUE DUTSCHER SAS

Set Plate Lock

Set Simulation

Set USB Trace

Begin Monitoring

HAMILTON Heater Shaker

Open  or  close  the  plate  lock.  The  plate  is  always
locked automatically before shaking is started, but this
command is useful to position and fix the plate in the
center  of  the  flat  bottom  adapter  before  pipetting,  or
when  using  the  commands  “Start  Shaker  Timed”  or
“Start  All  Shaker  Timed”  as  these  commands  do  not
open the plate lock after shaking.

Set  run  mode  to  simulation  for  all  functions  in  this
library. In simulation mode, no signals are sent to the
HHS.

Turn on/off tracing of communication to and from USB
port.

Start  to  monitor  the  performance  of  the  HHS.  This
function  monitors  the  temperature  and  speed  in  the
background.  The  tolerated  range  of  the  temperature
can  be  set  with  the  function  “SetTempParameter”.
The  tolerated  range  of  speed  is  defined  in  this
function.  The  status  of  the  temperature  can  be
requested  in  a  defined  interval  and  is  then  written  to
the trace file.

End Monitoring

Finish monitoring the performance of a HHS.

Get Shaker Speed

Get the shaking speed of a HHS.

Get Serial Number

Get the serial number a HHS.

Get Firmware Version

Get the firmware version of a HHS.

624175/03

15

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

4  Programming the HAMILTON Heater Shaker

The following two examples demonstrate the use of the HHS.

Before  using  the  HHS,  a  connection  and  device  number  has  to  be  generated.  After  the
connection has been established, the heater shaker will be initialized.

The  library  offers  two  commands  for  this  task,  depending  on  the  kind  of  connection
determined  by  the  hardware.  For  connections  made  via  TCC,  use  the  command
“CreateStarDevice”  (used  for  connecting  1  or  2  heater  shakers);  otherwise  use  the
command  “CreateUSBDevice”.  In  both  cases,  a  device  number  is  generated  that  can  be
stored in a variable. This variable must be used in all other commands of the library to control
the heater shaker.

Number
of HHS

1-2

1-8

Library function

Create Star Device

(Establish a connection to 1 or 2 shakers connected via TCC)

Create USB Device

(Establish a connection to up to 8 heater shakers using the heater
shaker box)

NOTE

It is required to establish a connection to all heater shakers that will be used in
the  method.  If  for  example,  only  two  out  of  four  shakers  have  been  initialized
then only these two shakers can be started with the “StartAllShaker” function.

NOTE

The  help  function  contains  a  description  of  all  functions  of  the  heater  shaker
library  with  a  description  of  parameters  passed  to  the  functions  or  obtained  by
them. You can access the help documentation by clicking on the yellow question

mark

 within the dialog windows.

624175/03

16

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

4.1  Example 1: Controlling only one HAMILTON Heater Shaker

In this first example, a single heater shaker is connected via the ML STAR Line instrument
TCC connector. The heater shaker is heated to 65°C followed by shaking for 10 min at 200
rpm. A detailed description of all steps can be found in the following section.

Overview of a method to run the heater shaker at 200 rpm for 10 minutes at 65°C.

4.1.1  Step by Step Analysis of Example 1

Step  1:  Create  a  connection  to  the  shaker  with  the  command  “CreateStarDevice”.  The
node can be “1” or “2” if the heater shaker is connected via TCC. You can assign the device
number, which is generated by this command, to any variable of your choice. This variable
has to be used for all subsequent commands regarding the control of the heater shaker.

624175/03

17

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

NOTE

If you insert a step in the method, the first time, on the frame the add-on New is
trailed.

If you have a method inserted and you want to edit it, the add-on Edit is inserted.

Step 2: Use the variable containing the device number to access the correct heater shaker.
Set  the  temperature  to  65°C.  If  you  choose  the  “waitForTempReached”  option  with  the
setting “1”, the method will halt at this step until the defined temperature has been reached
and is stable for 180 seconds. Only then the method will continue with the next step. If you
do  not  want  to  pause  your  method,  but  carry  out  other  tasks  in  parallel  to  the  heating
process, you should set “waitForTempReached” to “0”. At a later time, you can check for
the  temperature,  and  if  necessary  wait  for  the  heating  process  to  finish  using  the
“WaitForTempCtrl” command.

624175/03

18

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

Step  3:  Here,  the  shaking  parameters,  shaking  speed  and  duration  of  shaking  can  be  set.
The speed is defined in rpm and the time in seconds. The shaking speed ranges from 30 rpm
to 2500 rpm. The maximum speed depends on the orbit and adapter of the shaker and must
not  exceed  the  maximum  given  in  the  “Technical  Specifications”.  Any  function  to  start
shaking will also close the plate lock automatically.

Step 4: This command will wait until the shaker defined by the device number has finished
the timed shaking process. If the shaker is already finished before this function is called, the
method  will  immediately  proceed  with  the  next  step.  This  function  will  also  open  the  plate
lock.

624175/03

19

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

Step 5: As heating is controlled independently from shaking, the heating process has to be
terminated explicitly. Otherwise, the heater shaker will continue heating even if it is not used
anymore.

Step 6: If the heater shaker will not be used any longer, the connection can be terminated. At
the end of a method or upon abort, the connection is automatically terminated and will stop
heating as well as shaking. Finally the plate lock will open.

624175/03

20

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

The figure above shows a schematic view of the heating and shaking process as in example 1.

4.2  Safety measures upon method abort

If  the  method  is  aborted,  the  heater  shaker  will  automatically  be  stopped.  This  implies  that
the  heating  and  shaking  process  is  stopped,  the  plate  lock  is  opened  and  finally,  the
connection to the heater shaker is terminated. No further precautions within the submethod
“OnAbort” are required.

624175/03

21

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

4.3  Example 2: Controlling multiple HAMILTON Heater Shakers

This  second  example  shows  the  usage  of  multiple  heater  shakers  via  USB  and  the  heater
shaker box. The connection via USB and HSB is needed in order to control more than two
heater  shakers.  The  Method  is  using  three  heater  shakers  with  different  temperature
settings.

624175/03

22

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

4.3.1  Step by Step analysis of example 2

Step 1-3: Create a connection to all heater shakers you want to use in this method using the
function  “CreateUSBDevice”.  It  is  required  to  initialize  each  shaker  individually  in  order  to
create  a  device  number  and  to  control  the  heater  shaker  throughout  the  method.  Heater
shakers that are not initialized cannot be started with the “StartAllShaker” function.

The  usedNode  can  range  from  1  to  8,  depending  on  the  number  of  heater  shakers  in  use.
Node 1 corresponds to the master heater shaker.

The deviceNumber is stored in a variable, which is needed to control the heater shaker in all
following functions.

624175/03

23

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

Step 4-6: Set the temperatures for each individual heater shaker, for example to 50°, 60° und
70°C  as  shown  below.
the  option
“waitForTempReached” has to be set to “0”, so that all shakers are heated in parallel.

If  working  with  several  heater  shakers,

Step 7-9: Wait until all heater shakers have reached the set temperature before proceeding
with the method.

624175/03

24

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

Step  10-12:  The  “SetShakerParameter”  function  can  be  used  to  change  the  shaking
direction or acceleration of the heater shaker. Usually, the default settings can be used. The
default  settings  are  clockwise  shaking  and  an  acceleration  of  1250.  The  shaking  direction
can be changed by entering “1” for counter-clockwise shaking. The value for the acceleration
(shakingAccRamp)  ranges from 630 to 125000. The default setting of 1250 corresponds to
acceleration from 0 to the maximum speed of 2500 rpm within two seconds.

Step 13: All shakers can be started in parallel. The shaking speed is set to 2000 rpm. This
function will automatically close the plate lock on all shakers.

624175/03

25

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

Step  16:  To  finish  shaking  of  all  shakers  at  the  same  time  use  the  “StopAllShaker”
function.  This  function  does  not  require  any  device  numbers  but  will  stop  all  initialized
shakers and will automatically open the plate lock.

Step 17-19: The temperature control of the heater shaker can be terminated after its usage.
If  the  temperature  control  is  not  stopped,  heating  will  continue  even  after  terminating  the
shaking process.

624175/03

26

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

Step 20: The connections to the heater shakers are terminated. This step can be omitted at
the end of a method, as the connections to all heater shakers are automatically terminated at
the end of a method or upon abort of a method.

4.4  Monitoring the performance of the HAMILTON Heater Shaker

For some applications, it might be desirable to monitor the performance of the heater shaker.
The  library  offers  the  possibility  to  monitor  the  shaking  speed  and  temperature  during  an
application.  The  status  of  the  heater  shaker  is  continuously  written  to  the  trace  file.  The
settings  for  the  monitoring  can  be  adjusted  within  the  functions  “BeginMonitoring”  and
“SetTempParameter”.

Within  the  function  “BeginMonitoring”  you  can  define  the  intervals,  how  often  the
performance  of  the  heater  shaker  will  be  checked,  and  the  deviation  from  the  set  shaking
speed  that  will  be  tolerated.  You  can  also  decide  which  action  will  be  taken  if  monitoring
reports an out of range measurement.

All  settings  regarding  the  temperature  control  have  to  be  made  within  the  function
“SetTempParameter”. However, the default settings are usually sufficient.

After monitoring you can examine the return value from the function “EndMonitoring”. The
function reports whether heating or shaking or both were out of range.

624175/03

27

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

ATTENTION

Placing a cold plate on the hot heater shaker will cool down the heater shaker so
that the temperature might fall below the defined tolerated temperature range. In
this case, the “BeginMonitoring” function will return an error although heating
is working correctly.

To  avoid  this  kind  of  error,  the  function  “StartTempCtrl”  has  to  be  used
immediately before the transport step. This results in heating the heater shaker
again  until  the  temperature  is  stable  for  3  min.  Monitoring  is  paused  during
“StartTempCtrl” step.

Example of the monitoring function:

624175/03

28

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

5  Verification

It is recommended that HHS devices are verified twice a year, preferably in combination with
Preventive Maintenance of the ML STAR instrument.

If the HHS is used for IVD applications, it must be verified twice a year.

Refer to the ML STAR Line Operator’s Manual for further information or contact your local
Hamilton representative.

6  Maintenance

Hamilton  recommends  cleaning  the  HHS  regularly  to  prolong  its  life-span.  In  case  of
contamination  or  spillages  clean  the  HHS  immediately.  The  HHS  must  be  turned  off  and
cooled down for the maintenance procedure. Follow the maintenance procedure described in
the ML STAR Line Operator’s Manual. There are no further actions required.

ATTENTION

Do not clean the HHS when it is still hot!

Wait  until  the  HHS  has  cooled  down  to  room  temperature  before  starting  the
cleaning procedure.

624175/03

29

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

7  Technical Specifications

7.1  HAMILTON Heater Shaker

Instrument
Dimensions

Weight

Labware

Width (X)

Height (Z)

Depth (Y)

150 mm

2500 g

90 mm

105 mm

Standard microtiter plates with adapter
Standard deep well plates with adapter

Maximum weight (incl. adapter): 500 g

Temperature
Specifications*

Temperature

Ramp from 25°C

Deviation
compared to
target temp

Tolerance
Band for
measurement
and control:
Deviation on
plate (middle to
edge position)

37°C

60°C

90°C

100°C

105°C

in 3 min

in 10 min

in 20 min

in 30 min

In 35 min

36.0°-38.0°C

35.0°-39.0°C

58.5°-61.5°C

57.0°-63.0°C

88.0°-92.0°C

86.0°-94.0°C

97.5°-102.5°C

95.0°-105.0°C

102.5°-107.5°C

100°-110°C

Features of the
Heater Shaker

Temperature control

From 5°C above ambient
temperature to 105°C

Shaking directions

Acceleration

Deceleration

Shaking orbits:
(peak to peak)

*Measured on top of the MTP flat bottom plate

Controlled by two sensors
(located in the middle and at
the edge of the adapter plate)

clockwise and counter-
clockwise

2.0 s (from 0 to max rpm)

2.0 s (from max rpm to 0)

1.5 mm

2.0 mm

3.0 mm

624175/03

30

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

Features of the
Heater Shaker
(cont.) ¹

Recommended shaking speed in rpm depending on labware and
shaking orbit

Orbit

1.5 mm

MTP
Not
available

DWP

Sarstedt

2000

1800

customized
Not
available

2.0 mm

2500

2000

3.0 mm

2400

1800

Not
available
Not
available

2000

1800

Operating Data

Power consumption

Installation category

Pollution Degree

Temperature range

Relative humidity

Noise level

Altitude

Life time

Indoor use only

Storage and
Transportation

Temperature range

Relative humidity

41 V / 140 W (max.)
supplied by ML STAR Line
instrument or HSB

II

2

15°C - 35°C

15% - 85%

<65 dBA with max. speed

Max. 2000 m above sea level

6 years

-25°C - +70°C

10% - 90%

(non-condensing)

Communication

CAN via TCC connector or via USB

¹  The  Heater  Shaker  can  always  be  adjusted  from  100  to  2500  rpm  not  depending  the
version.

624175/03

31

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

7.2  HAMILTON Heater Shaker Box (HSB)

Instrument
Dimensions

Weight

Operating Data

Width (X)

Height (Z)

Depth (Y)

270 mm

6000 g

Voltage

90 mm

210 mm

100-240 VAC

Frequency

47-63 Hz

Power consumption

1000 VA (max.)

Delayed action fuse

250V 10 AT F

Installation category

Pollution Degree

II

2

Temperature range

15°C - 35°C

Relative humidity

15% - 85%

Noise level

<65 dBA

Altitude

Life time

Indoor use only

Max. 2000 m above sea level

6 years

Storage and
Transportation

Temperature range

-25°C - +70°C

Relative humidity

10% - 90%

(non-condensating)

HHS connectors

8

624175/03

32

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

8  Appendix

A

Ordering Information

Heater Shaker

Part number

Description

199037

HEATER SHAKER 1.5MM NUNC DWP 96 2ML

Heater  Shaker  with  1.5mm  shaking  orbit  and  fitted
adapter  for  plates  (Shaking  speed:  100  -2000  rpm,
Temperature  control:  RT+5°C  -  105°C,  max.  loading:
300g)

199027

HEATER SHAKER 1.5MM SARSTEDT 48 X 1.5ML

Heater  Shaker  with  1.5mm  shaking  orbit  and  fitted
adapter  for  plates  (Shaking  speed:  100  -1800  rpm,
Temperature  control:  RT+5°C  -  105°C,  max.  loading:
300g)

Sarstedt Tubes 1.5ml:

199033

HEATER SHAKER 2.0MM MTP FLAT BOTTOM

Heater Shaker with 2.0mm shaking orbit and flat bottom
adapter (Shaking speed: 100 -2500 rpm, Temperature
control: RT+5°C - 105°C, max. loading: 300g)

199038

HEATER SHAKER 2.0MM NUNC DWP 96 2ML

Heater Shaker with 2.0mm shaking orbit and fitted
adapter for plates (Shaking speed: 100 -2000 rpm,
Temperature control: RT+5°C - 105°C, max. loading:
300g)

199034

HEATER SHAKER 3.0MM FLAT BOTTOM

Heater Shaker with 3.0mm shaking orbit and flat bottom
adapter (Shaking speed: 100 -2400 rpm, Temperature
control: RT+5°C - 105°C, max. loading: 300g)

199039

HEATER SHAKER 3.0MM NUNC DWP 96 2ML

Heater Shaker with 3.0mm shaking orbit and fitted
adapter for plates (Shaking speed: 100 -1800 rpm,
Temperature control: RT+5°C - 105°C, max. loading:
300g)

624175/03

33

DOMINIQUE DUTSCHER SASHAMILTON Heater Shaker

Heater Shaker

Part number

Description

188318

HEATER SHAKER 2.0MM MTP FLAT BOTTOM APE

Heater Shaker with 2.0mm shaking orbit and the option
to be equipped with a customized adapter. The labware
has to be sent to Hamilton Bonaduz.
(Shaking speed depends on used adapter, Temperature
control: RT+5°C - 105°C, max. loading: 300g)

188319

HEATER SHAKER 3.0MM MTP FLAT BOTTOM APE

Heater  Shaker  with  3.0mm  shaking  orbit  and  the  option
to be equipped with a customized adapter. The labware
Bonaduz.
to
has
(Shaking speed depends on used adapter, Temperature
control: RT+5°C - 105°C, max. loading: 300g)

Hamilton

sent

be

to

Heater Shaker Accesories

Part number

Description

190755

HEATER SHAKER BOX

Needed if more than two HAMILTON Heater Shakers are
integrated  (or  the  connectors  “TCC1”,  “TCC2”  on  the
STAR  are  occupied  by  other  devices).  One  heater
shaker module is connected to a USB port of the PC and
serves  as  master  module  for  up  to  seven  additional
HHS’s.  The  modules  are  connected  to  the  external
heater shaker box (HSB), which serves as power supply
and as signal distributor.

199013

HAMILTON  HEATER  SHAKER  SUPPORT  BLOCK
FOR MTP

Hamilton Heater Shaker support block for MTP. Used to
raise the heater shaker on the carrier base if MTP's are
processed.

187001

PLT_CAR_L4_Shaker

Template  carrier  with  4  positions  for  Hamilton  Heater
Shaker (7T).

610766

624043

624294

VENUS two – Operator’s Manual

VENUS two - Programmer’s Manual

MANUALS STAR/LET IVD 4.3:

IVD Operator’s Manual

IVD Programmer’s Manual

624175/03

34

DOMINIQUE DUTSCHER SAS

HAMILTON Heater Shaker

B

Glossary

HHS

HSB

MTP

DWP

TCC

SBS

HAMILTON Heater Shaker

Heater Shaker Box

Microtiter plate in standard SBS format

Deep well plate in standard SBS format

Temperature controlled carrier

Standard format of the Society for Biomolecular Screening

Labware

Orbit /
Amplitude

Refer to movable items to be placed on the instruments, such as carriers,
containers, plates or racks.

The  Orbit  (Rotation  Distance)  is  defined  as  peak  to  peak  distance  in one
direction, e.g. distance between extreme positions in the Y-Direction of the
Plate measured in millimeters [mm].

The  Amplitude  is  defined  as  the  distance  from  the  center  of  the  shaking
movement and it is 50% of the peak to peak distance.

624175/03

35

DOMINIQUE DUTSCHER SAS

HAMILTON Bonaduz AG

Via Crusch 8

CH-7402 Bonaduz

Switzerland

Tel. +41 81 660 60 60

infoservice@hamiltonrobotics.com
http://www.hamiltonrobotics.com

DOMINIQUE DUTSCHER SAS
