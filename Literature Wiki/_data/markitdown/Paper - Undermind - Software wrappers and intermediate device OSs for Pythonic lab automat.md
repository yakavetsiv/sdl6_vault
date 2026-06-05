---
type: literature-note
source_note: "Papers/Paper - Undermind - Software wrappers and intermediate device OSs for Pythonic lab automat.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/Undermind - Software wrappers and intermediate device OSs for Pythonic lab automation.pdf"
converter: "microsoft/markitdown"
---
Undermind

REPORT CREATED ON
1/12/2026

Research Report on

Software wrappers and intermediate device OSs for Pythonic lab
automation

Full search query: I want to find research on software wrappers, integration frameworks, SDKs, and operating-system-like intermediary layers—im-
plemented in any language but usable from Python—for all communication protocols used in laboratory automation (including but not limited to
ROS/ROS2, SiLA/SiLA2, gRPC, REST-based APIs, OPC UA, and message-oriented protocols), with explicit inclusion and characterization of Apes
OS™ as a representative “intermediate device OS” approach, primarily in wet-lab contexts but also covering other laboratory equipment, and to
construct a comparison table that (1) highlights protocol/transport support, (2) identifies and characterizes available REST APIs and their exposure
to Python, (3) describes each system’s device abstraction model, and additionally collects information on the presence and capabilities of any
stateful device-manager/intermediate layer, workflow/orchestration features, lab-domain focus, and maturity/community characteristics

Summary

The search finds several concrete, Python-usable “intermediate OS / integration middleware” exemplars (most prominently HELAO
[1], OpenFlexure/LabThings [3,4,5], and UniLabOS [2]) plus many Python-centric device SDKs and orchestrators, but no paper in
this corpus explicitly documents Apes OS™, so it must be brought in from external sources for comparison.

Overview: What This Corpus Can and Cannot Support

What is well covered

• Python-implemented or Python-accessible integration layers that:

• Expose devices via HTTP/REST or similar remote APIs (HELAO [1], OpenFlexure/LabThings [3,4,5], LABS [12]).

• Act as stateful intermediaries between heterogeneous devices and higher-level logic (HELAO [1], labscript [11],

OpenFlexure server [4], UniLabOS [2]).

• Provide explicit device abstraction models (drivers/actions/experiments in HELAO [1]; WoT Thing Descriptions in

LabThings [4,5]; resource graphs and CRUTD operations in UniLabOS [2]; liquid-handling abstractions in PyLabRobot
[6]).

• Python-native device SDKs and lab frameworks with strong abstraction but less emphasis on standards-based protocol

bridging:

• Liquid handling: PyLabRobot [6], Pyhamilton [25].

• Microscopy/Imaging: Python(cid:17)Microscope [8,9], ImSwitch [27], AEcroscoPy [10], OpenFlexure [3,4].

• Physics/shot-based control and behavior rigs: labscript [11], pyControl [13].

• Electrochemistry and synthesis orchestration: LABS [12], AEcroscoPy [10], electrochemistry ICE/pyro frameworks

[21,22,23].

• Explicit use of standard protocols with at least some Python involvement:

• OPC UA: implemented as a southbound protocol in HELAO [1] and UniLabOS [2].

• SiLA2 / gRPC: used for bioreactor and LHS integration in [7]; central in the LAPP concept and pilot implementation

[17,18,19,26,18].

• ROS/ROS2 / DDS: foundational in UniLabOS [2] and in the LAPP family [17,19,26,18].

• REST/HTTP + WoT: core to OpenFlexure/LabThings [3,4,5] and web frontends like LABS [12].

• Message-oriented / RPC: ZeroMQ in labscript [11], Pyro in ORNL’s ICE frameworks [21,22,23].

What is missing

• Apes OS™: no article in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28] mentions or charac-

terizes it. Its protocol support, device model, REST/gRPC/Python APIs, and OS-like behavior must come from external technical
or white-paper sources.

• Full protocol matrices: very few works present a systematic enumeration of all transports they support; most name only one

or a small set (e.g., OPC UA in HELAO [1], SiLA2/gRPC in [7], ROS2/OPC UA/Modbus in UniLabOS [2]).

• Unified cross-protocol gateways specifically for wet-lab devices and Python: we see promising pieces (SiLA2 + Python
in [7], ROS2 + OPC UA in UniLabOS [2], OPC UA in HELAO [1]), but not a single open-source framework that cleanly bridges
all of ROS/ROS2, SiLA2, OPC UA, gRPC, REST, and brokers with a well-defined Python SDK.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 1/43

Undermind

REPORT CREATED ON
1/12/2026

Core “Intermediate OS / Integration Layer” Exemplars

HELAO: Python/HTTP Hierarchical Lab Automation with OPC UA Support [1]

• Protocols & transports

• Southbound: arbitrary device drivers; specifically reports support for OPC UA along with serial, TCP/IP, and vendor-spe-

cific libraries [1].

• Northbound: all device “drivers” and higher-level “actions” are asynchronous Python FastAPI web servers, exposing

HTTP/REST endpoints [1].

• Python exposure & APIs

•

Implemented in Python 3.8+; device drivers and actions are Python classes whose methods are auto-exposed via FastAPI
[1].

• An orchestrator (also Python) calls these HTTP endpoints; experiments are encoded as Python dictionaries (se-

quence-of-events specifications) [1].

• Python clients can either call the REST API (e.g., via requests/httpx) or import components directly when co-located.

• Device abstraction & OS-like behavior

• Three-layer hierarchy:

• Drivers (per-device HTTP servers) ’ Actions (compound operations, also HTTP servers) ’ Experiments (Python

dictionaries orchestrated by a central orchestrator) [1].

• Each device server is long-lived and stateful; HELAO defines asynchronous locks and concurrency control for device

sharing across instruments [1].

• Explicit support for distributed deployment across multiple hosts/OSes; devices can be shared between experiments

and instruments [1].

• Workflow/orchestration

• The orchestrator executes experiment dictionaries, handling parallel actions, non-blocking commands, and hard-

ware-in-the-loop optimization [1].

•

Integrates “aux” software devices (ML, data analysis) as drivers, enabling closed-loop active-learning workflows [1].

• Lab-domain focus & maturity

• Focused on materials science and electrochemistry; demonstrated in multi-instrument, spatially distributed self-driving

experiments [1].

• Open-source, explicitly compared to ROS, ChemOS, bluesky as a lightweight alternative [1]; adopted and cited in ChemOS

2.0 and IvoryOS [16,14].

Relevance to your comparison table: HELAO is the clearest example in this corpus of a Python-implemented, HTTP/REST-ex-
posed, stateful “device OS” with some OPC UA southbound support. It should be a primary row in your table for: protocol coverage,
REST API shape, Python exposure, device hierarchy, and stateful orchestration.

OpenFlexure & LabThings: WoT/REST Device Services with Python Clients [3,4,5]

• Protocols & transports

• Southbound: local device drivers for microscope hardware (motors, cameras); serial/USB and vendor APIs [4].

• Northbound:

• HTTP REST API conforming to the W3C Web of Things (properties/actions/events) [3,4].

• Device capabilities described using Thing Descriptions and OpenAPI specifications [3,4,5].

• Python exposure & APIs

• Server implemented in Python (Flask + Python(cid:17)LabThings library) running on an embedded Raspberry Pi [4].

• Provides an explicit Python scripting client; any language with HTTP can control the microscope [3,4].

• LabThings Retro extends this with Python client/server libraries for retrofitted legacy devices (serial RS(cid:17)232/USB bridged

to WoT/REST) [5].

• Device abstraction & OS-like behavior

• Each instrument (microscope, retrofitted legacy device) is a W3C Thing with:

• Properties (readable state), actions (commands), and events (notifications) [3,4,5].

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 2/43

Undermind

REPORT CREATED ON
1/12/2026

• Servers are always-on, stateful endpoints:

• Handle low-level initialization and concurrency.

• Allow multiple simultaneous clients; microscope remains configured between sessions [4].

• Extensions and “semantic typing” of capabilities support adding higher-level automation primitives (e.g., Z-stacks, tiled

scanning, autofocus) [4].

• Workflow/orchestration

• Basic automation routines (e.g., Z-stack) are implemented as server-side actions [4].

• More complex workflows are scripted via the Python client or GUI; no standalone DAG engine is described.

• Lab-domain focus & maturity

• Domino focus: optical microscopy (OpenFlexure) and legacy instrument retrofits (LabThings Retro) [3,4,5].

• Widely used open-source platform, with SD images and multiple repositories; LabThings Retro adds detailed hardware

build instructions [5].

Relevance to your comparison table: OpenFlexure/LabThings provide an important reference design for WoT/REST-based
device abstraction usable from Python, including explicit Thing Descriptions and OpenAPI. They do not cover ROS/SiLA/OPC
UA/gRPC/brokers, but are exemplary for REST/WoT column entries, device abstraction semantics, and lightweight stateful de-
vice-management patterns.

UniLabOS: ROS2/DDS-Based “AI-Native Operating System” for Labs [2]

• Protocols & transports
• Southbound:

• ROS 2 / DDS is the primary middleware [2].

• Explicit support for Modbus, PLCs, OPC UA, and generic TCP/IP, with mention of legacy serial/GPIB/USB [2].

• Northbound:

• Not fully detailed in the excerpt; likely exposed via ROS2 services/topics/actions and perhaps higher-level APIs.

• No explicit REST/gRPC/Python SDK description is given.

• Python exposure & APIs

• The paper does not state a dedicated Python SDK. However:

• ROS2 has standard Python client libraries (rclpy) and Python can consume ROS2-based services/actions.

• OPC UA and TCP/IP support would enable Python clients via existing OPC UA Python libraries and socket/gRPC

bindings.

• For your table, you can mark Python-enabled via ROS2/OPC UA tooling, but not a bespoke Python SDK.

• Device abstraction & OS-like behavior

• Explicitly pitched as an OS for autonomous labs:

• Driver-as-a-service model: each driver registers capabilities dynamically via AST inspection [2].

• Dual-topology resource model:

• A hierarchical resource tree (logical organization of resources).

• A physical graph (actual connectivity and placement) [2].

• Defines six canonical device classes (sensors, connectors, material processors, characterization, logistics, virtual

devices) and A/R/A&R abstractions [2].

• Operations expressed via CRUTD (Create, Read, Update, Transfer, Delete) transactions on materials and states [2].

• Maintains digital twins:

• Telemetry-driven shadow states.

• Pre-dispatch validation using robotics tools like RViz/MoveIt to ensure feasible actions before execution [2].

• Stateful device manager and orchestration

•

Implements a device registry, resource graph, and long-lived driver services [2].

• Distributed edge–cloud architecture for multi-node orchestration across heterogeneous instruments [2].

• Supports dynamic driver registration without restarts (AST-based capability discovery) [2].

• Lab-domain focus & maturity

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 3/43

Undermind

REPORT CREATED ON
1/12/2026

• Demonstrated on liquid-handling, modular organic synthesis, distributed electrolyte foundries, and compute-in-

tensive closed-loop cases [2].

• Recent (2025) but conceptually comprehensive; can be treated as the most fully articulated “device OS” in this corpus.

Relevance to your comparison table: UniLabOS is the main exemplar that simultaneously claims OS-like semantics, multi-pro-
tocol southbound support (ROS2, OPC UA, Modbus, PLC, TCP/IP), and a rich device/material abstraction model. For Python,
you will need to rely on ROS2/OPC UA client libraries rather than a documented dedicated SDK.

labscript: Early Python “Experiment OS” for Hardware-Timed Experiments [11]

• Protocols & transports

• Device communication via vendor APIs and ZeroMQ for inter-component messaging; data stored and shuttled via HDF5

files [11].

• No use of ROS/SiLA/OPC UA/gRPC/REST.

• Python exposure & APIs

• Entire stack is Python-centric at the user level: experiments are authored as Python scripts that are compiled into

low-level hardware instruction sequences [11].

• Device abstraction & OS-like behavior

• Shot-based, hardware-timed model: each experiment is a “shot” with a time-ordered instruction list [11].

• Central BLACS controller maintains hardware connections, shot queue, and execution state [11].

• Device drivers conform to type-specific Python interfaces.

• Workflow/orchestration

• Provides a multi-stage pipeline: Python script ’ compiled shots ’ queued execution ’ analysis [11].

• Support for parameter sweeps and autonomous optimization through the mise component [11].

• Lab-domain focus & maturity

• Physics experiments (cold atoms, quantum optics, etc.) [11].

• Mature, long-standing user community; conceptually foundational for Python-based orchestrators.

Relevance to your comparison table: labscript is a strong exemplar for stateful orchestration and experiment queues, but
protocol rows will largely be “custom/ZeroMQ” and it lacks standardized cross-protocol bridging.

ChemOS and IvoryOS: Orchestration Above Device Layers [15,16,14]

• ChemOS (1.0 and 2.0) [15,16]

• Multi-module self-driving lab orchestrator with learning, robotics, characterization, DB, user interaction, and online analysis

[15].

• Devices are integrated by custom communication protocol and interaction layers per platform, but protocols (ROS,

SiLA, OPC UA, REST) are not specifically enumerated in [15].

• Primarily a workflow/AI orchestration framework, not a device OS or standard protocol bridge.

•

IvoryOS [14]

• An interoperable orchestrator for heterogeneous Python-based SDLs, generating web UIs dynamically from Python

components [14].

• Provides drag-and-drop workflow design and iterative/closed-loop execution; integrates multiple existing SDLs, including

those built on PyLabRobot and HELAO [14].

• Treats underlying SDLs as components rather than defining its own device protocol; northbound is a web UI and

configuration layer, southbound is function calls into existing Python code.

Relevance to your comparison table: Both should appear in the workflow/orchestration section rather than as core device OS
layers; protocol support is opaque or delegated to underlying frameworks.

Python Device-Abstraction Frameworks Without Strong Protocol Bridging

These systems are key for understanding Python-based device models and internal statefulness but generally lack standardized
protocol bridging or network-facing REST/gRPC APIs.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 4/43

Undermind

REPORT CREATED ON
1/12/2026

PyLabRobot & Pyhamilton (Liquid Handling) [6,25]

• Pyhamilton [25]

• Hamilton-specific Python SDK for liquid handlers; supports complex pipetting, plate coordination, and closed-loop

protocols (e.g., culture maintenance via plate readers) [25].

• No ROS/SiLA/OPC UA/REST; control is via Hamilton firmware and vendor APIs.

• PyLabRobot [6]

• Generalizes to a hardware-agnostic Python interface for multiple vendors (Hamilton, Tecan, Opentrons, BMG) [6].

• Backends speak to devices via direct USB/firmware (PyUSB, pylibftdi) or HTTP where available [6].

• Maintains deck and labware state, preventing invalid moves and enabling conflict detection [6].

Use in your table: Emphasize:

• No standard protocol focus (but some HTTP backends).

• Strong capability-based abstraction (pipetting, deck model).

• Stateful resource management within the Python process.

Python-Microscope & ImSwitch (Microscopy) [8,9,27]

• Python(cid:17)Microscope defines canonical device interfaces (cameras, stages, etc.) with multiple vendor implementations and

distributed device servers [8].

•

ImSwitch builds multi-unit microscopy workflows using ImSwitch scripting and shared filesystem synchronization, not network
APIs [27].

• No ROS/SiLA/OPC UA/REST; network aspects are Python-specific.

AEcroscoPy (Scanning Probe/STEM) [10]

• Python “hyper-language” above instrument-specific LabVIEW VIs and FPGA hardware [10].

• Uniform data model (sidpy.dataset), logging, ML integration [10].

• No standard protocols; Python communicates via Windows interop and low-level I/O.

pyControl (Behavioral rigs) [13], LABS [12], PLACE [24]

• All are Python orchestration layers with device abstractions and GUIs or web interfaces.

• Underlying transports are vendor-specific or custom; no ROS/SiLA/OPC UA/REST/gRPC described in abstracts [12,13,24].

Use in your table: These frameworks will primarily inform:

• Device abstraction column (what is the conceptual model: state machine, resource model, etc.).

• Stateful management (tracking rig state, electrochemical setups, experiment batches).

• Lab-domain specialization (wet-lab vs physics vs neuroscience).

Protocol- and Standard-Centric Efforts with Python Involvement

SiLA2/gRPC in Bioreactors and LAPP [7,17,18,19,26,18]

• Bioreactor dynamic scheduling [7]

• SiLA2 servers for a 48-parallel bioreactor; Python Scheduler and LHS Server manage dynamic, constraint-based

scheduling [7].

• C# gRPC client embedded in Hamilton VENUS; Python side transmits parameter arrays and method names, not generic

SiLA2 stubs [7].

• LAPP & LAPP-DT [17,19,26] and mobERT pilot [18]

• Conceptual design: plug-and-play mobile manipulators with SiLA/SiLA2, ROS, OPC UA, and a digital twin of devices and

robot action primitives [17,19,26].

• Pilot uses SiLA2 and a commercial scheduler (Biosero GBG) to automate HPLC sample prep [18].

• Python involvement is mentioned as a possible SiLA implementation language, but no explicit Python APIs are given.

Use in your table: These works are vital for:

• Showing SiLA2/gRPC and ROS as serious candidates for lab-wide standardization.

• Filling the protocol coverage column for SiLA2/ROS, even when Python is only indirectly involved.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 5/43

Undermind

REPORT CREATED ON
1/12/2026

ORNL Instrument-Computing Ecosystems (Pyro-based) [21,22,23]

• Python wrappers around vendor APIs, exposed over the network via Pyro; Jupyter notebooks orchestrate workflows from

remote machines [21,22,23].

• Clear separation of control and data planes (Pyro vs NAS mounts) [23].

• No SiLA/ROS/OPC UA/REST; the protocol is Python-specific RPC.

Use in your table: Illustrative of:

• A minimalist intermediate layer: gateway computers, wrapped APIs, Python RPC.

• How far Python-based RPC alone can go before needing standardized schemas and protocols.

Implications for Your Planned Comparison Table

Given these findings, you can structure the table roughly as:

1. Core device-OS/integration-middleware rows:

• HELAO [1]

• UniLabOS [2]

• OpenFlexure / LabThings [3,4,5]

•

labscript [11]

• ChemOS (1.0/2.0) [15,16]

•

IvoryOS [14]

• SiLA2 bioreactor/LHS stack [7]

• LAPP (concept + pilot) [17,18,19,26,18]

• SmartLab [28] (requires deeper protocol reading)

1. Python device-abstraction and orchestration frameworks (no standard protocol bridging but relevant models):

• PyLabRobot [6], Pyhamilton [25]

• Python(cid:17)Microscope [8,9], ImSwitch [27]

• AEcroscoPy [10]

• LABS [12], PLACE [24]

• pyControl [13]

• ORNL ICE frameworks (Pyro) [21,22,23]

1. Protocol coverage columns

• ROS/ROS2: UniLabOS [2]; LAPP [17,19,26,18].

• SiLA/SiLA2 (gRPC): Bioreactor/LHS scheduling [7]; LAPP & pilot [17,18,19,26,18].

• OPC UA: HELAO [1]; UniLabOS [2].

• REST/HTTP/WoT: OpenFlexure/LabThings [3,4,5]; HELAO [1]; LABS [12]; possibly SmartLab [28].

• Message-oriented: ZeroMQ (labscript) [11]; Pyro (ORNL ICE) [21,22,23]; DDS via ROS2 in UniLabOS [2].

1. Python exposure columns

• Native Python SDK: PyLabRobot [6], Pyhamilton [25], Python(cid:17)Microscope [8], AEcroscoPy [10], labscript [11], pyControl

[13], LABS [12], PLACE [24].

• HTTP/REST Python client: HELAO [1]; OpenFlexure/LabThings [3,4,5]; LABS [12].

• Python via ROS2/OPC UA: UniLabOS [2].

• Python via SiLA2/gRPC: potential but not fully documented; bioreactor stack uses mixed Python/C# [7].

1. Device abstraction models

• WoT resource/actions/events: OpenFlexure/LabThings [4,5].

• Driver/action/experiment layering: HELAO [1].

• CRUTD + resource graphs/digital twins: UniLabOS [2].

• Feature-based SiLA2: Bioreactor stack [7]; LAPP [17,19,26,18].

• Pipetting & deck models: PyLabRobot [6], Pyhamilton [25].

• Type-based device classes: Python(cid:17)Microscope [8].

• State-machine tasks: pyControl [13].

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 6/43

Undermind

REPORT CREATED ON
1/12/2026

• Shot-based hardware-timed model: labscript [11].

1. Stateful device manager & workflow columns

• Explicit stateful device management: HELAO [1]; OpenFlexure server [4]; UniLabOS [2]; labscript [11]; PyLabRobot [6];

pyControl [13].

• Workflow engines / orchestrators: ChemOS [15,16]; HELAO [1]; labscript [11]; IvoryOS [14]; SiLA2 bioreactor scheduler

[7]; LAPP pilot [18]; LABS [12].

Positioning Apes OS™ in Light of This Corpus

Because Apes OS™ is absent from the retrieved references, you will need to:

• Retrieve its architecture, protocol support, and API documentation from external sources (technical docs, white papers,

patents, or vendor website).

• Place it conceptually alongside:

• UniLabOS [2] (for OS-like device/resource modeling and multi-protocol bridging).

• HELAO [1] and OpenFlexure/LabThings [3,4,5] (for Python-compatible REST APIs and device-as-service designs).

• LAPP/SiLA2 [17,18,19,26,18] (if Apes OS supports SiLA2 or similar feature/capability models).

• Map Apes OS™ into your table across:

• Southbound protocol coverage: which of ROS/ROS2, SiLA/SiLA2, OPC UA, fieldbuses, gRPC, vendor SDKs it

supports.

• Northbound interfaces: presence and nature of REST/gRPC/Python SDK.

• Device abstraction: whether it follows feature-based, WoT-style, resource/graph-based, or other models.

• Stateful management & workflow features: device registry, session handling, locking, digital twins, integration with

external schedulers or built-in workflow engines.

• Lab-domain focus and maturity: wet-lab emphasis, vendor and community adoption.

Bottom Line for Your Project

• The literature supports a rich landscape of Python-centered lab integration, ranging from tightly-coupled SDKs to

full-fledged OS-like layers.

• HELAO [1] and OpenFlexure/LabThings [3,4,5] are the strongest Python + REST exemplars; UniLabOS [2] is the strongest

multi-protocol, ROS2/OPC UA-based lab OS exemplar.

• SiLA2/gRPC and ROS/ROS2/OPC UA appear in concrete lab contexts (bioreactors, mobile manipulators, UniLabOS), but

their Python client/tooling is usually implicit rather than deeply documented.

• To complete your comparison—especially the explicit characterization of Apes OS™—you will need to augment this corpus

with non-article technical sources, then align Apes OS’s features against these clearly defined reference systems along the
protocol, API, device-model, and statefulness axes.

Categories

Comparative dimensions used across papers

Key aspects compared

Across the retrieved works, the most relevant axes—given your goal of characterizing “wrapper/framework / intermediate OS layers
usable from Python” and protocol coverage—are:

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 7/43

Undermind

REPORT CREATED ON
1/12/2026

• Protocol / transport support

• Northbound API and Python exposure pattern

• Device abstraction model (RPC vs resources, features/capabilities, information models)

• Stateful device-manager / intermediate-OS behavior

• Workflow / orchestration capabilities

• Lab-domain focus (wet lab, microscopy, electrochemistry, physics, etc.)

• Maturity / community characteristics (open source, breadth of deployment)

Below, I group and compare the “top” systems into three clusters:

1. Intermediate OS / orchestration frameworks with explicit network APIs usable from Python.

1. Python-centric device abstraction libraries (less emphasis on network protocol bridging).

1. Standards- and protocol-centric works (SiLA/ROS/OPC UA / Pyro, often partial toward your criteria).

A final subsection explicitly addresses Apes OS™ (not present in the current corpus).

1. Intermediate OS / orchestration frameworks with network APIs

This group comes closest to “operating-system-like intermediary layers” and multi-device orchestration.

Comparison table: intermediate-OS / orchestration systems

System

Protocol / trans-
port support (ex-
plicit)

Northbound API
& Python expo-
sure

Device abstrac-
tion model

HELAO (Hierar-
chical Experimen-
tal Laboratory Au-
tomation and Or-
chestration) [1]

Southbound: arbi-
trary device dri-
vers; explicitly in-
cludes OPC UA
among support-
ed protocols [1].
Uses OS-specif-
ic drivers, serial,
etc. Northbound:
HTTP/REST over
FastAPI [1].

UniLabOS [2]

Southbound:
ROS 2/DDS,
Modbus, PLCs,
OPC UA, and
generic TCP/IP,
with mention of
legacy
serial/GPIB/USB
[2]. Northbound
transport not fully
specified in
excerpt (likely via
ROS 2 or
higher-level APIs).

Devices (“drivers”)
and higher-lev-
el “actions” are
async Python
web servers-
. Functions of
Python classes
are exposed as
HTTP endpoints
via FastAPI; or-
chestrator is a
Python process
calling these end-
points [1]. Python
is both im-
plementation and
client-level lan-
guage.

Described as an
“AI-native OS”
with
driver-as-a-ser-
vice; drivers
register
capabilities via
AST inspection [2].
The excerpt does
not explicitly
mention a Python
SDK or
REST/gRPC
bindings. Python
usability is
therefore implied
only indirectly
(ROS 2/gRPC
tooling) and
cannot be
asserted.

3-layer model: de-
vice drivers ’
actions ’ ex-
periments. Dri-
vers wrap phys-
ical devices; ac-
tions group driver
calls; experiments
are Python dic-
tionaries describ-
ing sequences
[1]. Conceptually
RPC-like, capa-
bility-oriented.

Rich
resource/device
model: dual
topology
(hierarchical
resource tree +
physical graph)
and typed
A/R/A&R
abstractions; six
standardized
device classes
(sensors,
connectors,
material
processors,
characterization,
logistics, virtual
devices) [2].
Operations
expressed via a
transactional
CRUTD protocol
(Create/Read/Up-
date/Trans-
fer/Delete) for
materials and
states [2].

Stateful device
manager / inter-
mediate layer

Yes: every device
is a long-lived web
server; HELAO
uses asynchro-
nous locks and
shared state to
coordinate ac-
cess and device
sharing, including
distributed mul-
ti-computer setups
[1]. Device servers
maintain configu-
ration and state
between calls.

Yes: explicit device
registry, resource
model, digital
twin synchro-
nization (teleme-
try-based shad-
ow state, pre-dis-
patch validation
with RViz/MoveIt)
and multi-node
orchestration [2].
Emphasizes per-
sistent device and
material life-cycle
management.

Workflow / or-
chestration

Lab-domain fo-
cus & maturity

Materials
science /
electrochemistry
(e.g., autonomous
electrolyzer
experiments) [1].
Open-source,
Python 3.8+,
positioned as a
lightweight
alternative to
ROS/ChemOS/bluesky
[1]. Has visible
uptake (citations,
cross-references
[16]).

Explicitly targets
autonomous lab-
oratories (chem-
istry and mate-
rials) [2]. Archi-
tecture-level de-
sign, with multiple
case studies list-
ed; publication is
recent, so com-
munity maturity is
emerging.

Orchestrator
interprets
experiment
dictionaries and
calls actions;
framework
supports parallel
hard-
ware-in-the-loop
active-learning,
aux “software
devices” (ML,
analysis), and
provenance
logging (HDF5 to
KaDI4Mat/figshare)
[1]. Workflow is
programmatic, not
GUI-based.

Supports dis-
tributed orches-
tration across
edge–cloud, with
transactional op-
erations and dig-
ital-twin validation;
used for modu-
lar organic syn-
thesis, liquid han-
dling, and dis-
tributed electrolyte
foundry cases [2].
However the de-
tailed workflow
description is only
partially visible in
the excerpt.

Southbound:
device drivers for

Server
implemented in

WoT-style Thing
Description:

Yes: an al-
ways-running em-

Provides automa-
tion primitives (Z(cid:17)s-

Optical
microscopy,

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 8/43

Undermind

OpenFlexure +
Python(cid:17)LabThings
server [3,4]

LabThings Retro
[5]

labscript suite
[11]

ChemOS 1.0 [15]

motors, cameras,
etc. on
Raspberry Pi;
uses local driver
interfaces (e.g.,
camera SDKs) [4].
No
ROS/SiLA/OPC UA/gRPC
use. Northbound:
HTTP REST
following W3C
Web of Things
(properties/ac-
tions/events) [3,4].

Python with
Flask and the
Python(cid:17)LabThings
library [4].
Exposes HTTP
API documented
via OpenAPI,
enabling
autogenerated
clients. A
dedicated Python
scripting client is
provided; any
language that can
do HTTP can
control the
microscope [3,4].

Southbound:
seri-
al/RS(cid:17)232/USB to
legacy devices
(syringe pump
etc.) via ESP32
controller [5].
Northbound:
HTTP/REST Web
of Things with
Thing
Descriptions and
OpenAPI [5]. No
ROS/SiLA/OPC UA/gRPC
mentioned.

Uses LabThings
ESP32 library
on microcontroller
plus Python client
and server li-
braries [5]. Python
scripts control
retrofitted devices
via HTTP and
Thing Descrip-
tions; OpenAPI
enables auto-
generated Python
clients.

Southbound:
vendor APIs and
low-level drivers;
supports external
control programs
(e.g., BIAS) when
specific
OS/language
needed [11].
Inter-component
comms via HDF5
shot files and
ZeroMQ sockets
[11]. No
ROS/SiLA/OPC UA/REST/gRPC.

Entirely
Python-centric at
the user level:
experiments
authored as
Python scripts that
compile to
hardware
instruction
sequences [11].
The runtime uses
ZeroMQ and HDF
file exchange.
Python is both
orchestrator and
configuration
language.

Protocols are
described
generically as
“communication
protocol and
interaction layers”,
implemented per
hardware platform
[15]. Specific
transports
(ROS/SiLA/OPC
UA/REST) are not
enumerated in the
excerpt.

Modular architec-
ture; does not
specify a single
language, but giv-
en the ecosys-
tems integrated
(Phoenics, SMAC,
etc.) Python is
used on the learn-
ing side. The ex-
cerpt does not
confirm a Python
SDK for device
control.

REPORT CREATED ON
1/12/2026

properties,
actions, events
[3,4]. Capabilities
are semantically
typed; extension
hooks allow
additional
automation
routines to be
added. Each
microscope is a
“Thing” with typed
capabilities.

bedded server on
the microscope
provides persis-
tent continuity; de-
vice state and
configuration sur-
vive client ses-
sions [4]. Supports
multiple simulta-
neous clients; in-
cludes discovery
via mDNS. Acts as
a lightweight de-
vice OS for the
microscope class.

tacks, tile scans,
autofocus) ex-
posed as actions
[4]. No gener-
al DAG engine,
but users can
build higher-level
workflows via the
Python client or
web GUI.

especially
low-cost
OpenFlexure
microscopes [3,4].
Open-source,
globally deployed
in community labs
and education;
multiple repos and
SD images are
maintained.

Device abstraction
via WoT Thing
Descriptions,
mapping legacy
commands to
properties/ac-
tions/events [5].
Capability(cid:17)oriented
abstraction over
serial protocols.

Limited: acts as
a gateway per
device; maintains
some mapping
and connection
state, but no global
registry or reser-
vation semantics
are described [5].

Demonstrates
closed-loop
feedback
(OpenFlexure
microscope +
syringe pump) [5],
but no generic
workflow engine;
orchestration is
done in Python
scripts or Jupyter.

Focus on retro-
fitting older lab
equipment (Cat-
egory 1 &
2 devices) [5].
Open-source, with
hardware and
software build in-
structions on Git-
Lab; community
still early.

Strongly
shot-based,
hardware-timed
model:
experiments are
specified as
time-ordered
sequences; device
drivers implement
a standard
interface for each
device type;
pseudoclock used
to synchronize
instructions [11].

Yes: BLACS con-
troller acts as
a central ex-
periment con-
troller and shot
queue, manages
hardware connec-
tions and execu-
tion state; supports
parameter sweeps
and closed-loop
optimization via
the mise compo-
nent [11].

Provides a full
pipeline: exper-
iment definition
(Python) ’ com-
pilation ’ execu-
tion (BLACS) ’
analysis; supports
autonomous op-
timization loops
through mise [11].
Orchestration is
centered on dis-
crete shots rather
than continuous
operations.

Designed for
atomic/optical
physics and
similar
hardware-timed
experiments [11].
Open-source, with
a long-standing
user base in the
physics
community.

Partial: a cen-
tral workflow
manager orches-
trates six modules
[15]. Device reg-
istry/session se-
mantics are not
clearly described;
device abstraction
appears to be
per-integration.

Yes: the cen-
tral workflow man-
ager coordinates
learning, robot-
ics, characteriza-
tion, DB, etc., for
closed-loop opti-
mization; target is
self-driving labs
[15].

Modules for learn-
ing, robotics/au-
tomation, charac-
terization, data-
bases, researcher
interaction, and
online analysis
[15]. Device con-
trol happens via
a “robotics/au-
tomation module”
that maps ab-
stract parameters
to hardware-spe-
cific commands
[15].

Focus on chem-
ical self-dri-
ving laborato-
ries with mul-
tiple demonstra-
tion platforms [15].
Widely known and
cited; open-source
repo exists, but
level of gener-
ic, reusable de-
vice abstraction is
less explicit than
HELAO.

Positioned as
an “orchestra-
tion architec-
ture” for chemi-
cal SDLs, build-
ing on ChemOS
and citing HELAO
[1,15,16].

–

–

–

–

ChemOS 2.0 [16]

Abstract not avail-
able; not enough
information in the
excerpt to reliably
characterize pro-
tocol coverage or
APIs.

IvoryOS [14]

Exposes “web
interfaces” to
Python-based
SDLs; underlying
transport is HTTP
(web) but the
excerpt does not
state REST vs

IvoryOS wraps
Python-based
SDLs,
introspecting
components and
automatically
generating web
interfaces [14].

IvoryOS treats
each SDL compo-
nent as a Python
component with
exposed func-
tions; these are
surfaced as UI el-
ements and work-

Partial: IvoryOS
works as a
higher-level or-
chestrator over
existing Python
SDLs; it does
not itself main-
tain device ses-

Strong workflow
focus: a work-
flow manager
with drag-and-drop
design, no(cid:17)-
code iterative
execution, hu-
man(cid:17)in(cid:17)the(cid:17)loop and

Cross-domain
self-driving labs
(six SDLs across
two institutes) [14].
Open-source, but
oriented to
wrapping Python
SDLs rather than

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 9/43

Undermind

SmartLab [28]

Workflows are
designed via a
drag-and-drop
web UI, but
underlying
operations map to
Python functions
in SDLs [14].

Supports “remote
operation” through
high-level com-
mands [28]. Im-
plementation de-
tails of Python
APIs or SDKs are
not included in the
excerpt.

flow nodes [14].
The abstraction
is SDL-API-cen-
tric, not a univer-
sal device model.

Described as a hi-
erarchical com-
putational plat-
form; more detail
on the device ab-
straction model is
not present in the
summary [28].

sions beyond what
SDLs provide [14].
No explicit de-
vice registry for
heterogeneous in-
struments is de-
scribed in the ex-
cerpt.

Implied: SmartLab
acts as an inter-
operable labora-
tory platform en-
abling remote and
automated exper-
iments [28]. De-
tails on device
registry/state are
lacking in the ex-
cerpt.

websockets, nor
any
ROS/SiLA/OPC
UA/gRPC use [14].

Described as
“inter-
net-of-things-based”
with a legacy
equipment
classification and
retrofitting
methodology [28].
The excerpt does
not name specific
protocols (e.g.,
MQTT vs REST)
or standards
(ROS, SiLA, OPC
UA).

REPORT CREATED ON
1/12/2026

closed(cid:17)loop modes
[14].

providing a
lab-protocol
bridging layer.

Demonstrates re-
mote education
and fully automat-
ed material test-
ing workflows (90
specimens manu-
factured and test-
ed automatically)
[28].

Focus on engi-
neering / manu-
facturing labora-
tory with mobile
manipulator and
mechanical testing
[28]. Open-source
and hierarchical;
integration details
are not fully visible
in the summary.

Key comparative observations in this group

• HELAO [1] and OpenFlexure/LabThings [3,4] are the clearest examples of Python-implemented, HTTP-exposed inter-

mediate layers that:

• Wrap diverse devices behind web APIs.

• Maintain persistent state on the device side.

• Provide reasonably clear device abstraction models (drivers/actions/experiments in HELAO; WoT Thing descriptions in

LabThings/OpenFlexure).

• UniLabOS [2] is the most explicit about multi-protocol southbound support (ROS2, OPC UA, Modbus, PLCs) and a rich
resource / digital-twin model, but the available excerpt does not specify Python client interfaces or REST/gRPC exposure.

•

labscript [11] is strongly Python-first and provides OS-like orchestration (shot queue, multiple devices, autonomous opti-
mization), but its transport is not standards-based; it relies on ZeroMQ + HDF5 and per-device drivers.

• ChemOS [15] and IvoryOS [14] emphasize orchestration and workflow layers; their descriptions of device abstractions and
network protocol bridging are more limited than HELAO/UniLabOS. IvoryOS is explicitly orchestrator-on-top-of-Python
SDLs, not a base device OS.

2. Python-centric device abstraction libraries (limited network/standards support)

These systems provide reusable device abstractions and sometimes multi-device coordination, but they are not primarily net-
work/protocol-bridging OSes.

Comparison table: Python device-abstraction frameworks

System

Protocol / trans-
port support

Python exposure Device abstrac-

tion model

PyLabRobot [6]

A pure Python li-
brary/SDK; users
import PyLabRo-
bot and call its API
directly [6].

Southbound:
device-specific
backends using
direct
firmware/USB
(via PyUSB,
pylibftdi) and
HTTP where the
hardware exposes
it [6]. No
ROS/SiLA/OPC UA/gRPC/mes-
sage-broker
coverage.

Hardware-agnos-
tic
liquid-handling
abstraction:
backends
implementing
ABCs, canonical
deck and
labware models,
pipetting actions
(aspirate/dis-
pense), etc. [6].

Stateful manag-
er / intermediate
behavior

Yes, at the SDK
level: maintains
resource/device
state to validate
positions and
avoid conflicts [6].
No separate
server: state lives
in the Python
process.

Workflow / or-
chestration

Lab-domain fo-
cus & maturity

Enables scripted
protocols and
interactive control
(REPL/Jupyter)
with a
browser-based
simulator; but no
built-in DAG
engine or
scheduler is
described [6].

Liquid-handling
robots and
accessories
(Hamilton, Tecan,
Opentrons, BMG
plate readers) [6].
Open-source and
actively extended;
used by the
community [6,14].

Pyhamilton [25]

Southbound:
Hamilton robotic
firmware and
associated
hardware;
protocol described
through vendor
APIs. No
ROS/OPC UA/etc.
reported [25].

Python package-
; users program
Hamilton robots
via Python classes
for actions (aspi-
rate/dispense) and
consumables [25].

Robot-centric
pipetting/plate
abstractions,
complex patterns,
multi-plate
coordination [25].

Maintains experi-
ment state and in-
tegrates feedback
(e.g., plate read-
er) for closed-loop
culture mainte-
nance [25].

Focused on
Hamilton liq-
uid handlers-
; well adopted
within open-source
biology automation
[25,6].

Provides ad-
vanced pro-
tocols (mul-
ti-plate processes,
real-time control),
but workflow log-
ic is expressed in
Python scripts, not
a generic sched-
uler [25].

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 10/43

Undermind

Python(cid:17)Micro-
scope [8,9]

AEcroscoPy [10]

LABS [12]

PLACE [24]

pyControl [13]

ImSwitch frame-
work [27]

REPORT CREATED ON
1/12/2026

A Python library-
; devices can run
as remote Python
processes, but the
primary interface is
Python import and
use [8].

Type-based de-
vice classes-
: cameras, stages,
etc., each with
a defined inter-
face; concrete im-
plementations for
multiple vendors
[8].

Yes, via dis-
tributed de-
vice servers that
maintain state and
synchronize with
hardware triggers
[8]. However, this
is not a stan-
dards-based net-
work API.

Used as a back-
end for Micro-
scope(cid:17)Cockpit and
for complex cus-
tom microscopes;
orchestration is
largely through
higher-level GUIs
or user scripts [8].

Microscopy,
targeted at
custom/multi-ven-
dor setups [8].
Open-source and
integrated with
other projects
[3,27].

Southbound: ven-
dor-specific APIs
for cameras, fil-
ter wheels, light
sources, stages;
supports distribu-
tion across mul-
tiple computers
via networked
device servers
[8]. Transport
uses Python-lev-
el remote calls;
no ROS/OPC
UA/REST.

Python pack-
age (AEcroscoPy)
is the hyper-lan-
guage; users call
Python functions
that command
LabVIEW VIs and
FPGA [10].

Southbound:
LabVIEW virtual
instruments,
FPGA hardware,
vendor-specific
instrument VIs
[10].
Communication
between Python
and LabVIEW via
pywin32; no
ROS/SiLA/REST/OPC
UA.

Cross-platform
abstraction over
multiple
SPM/STEM
instruments,
returning
standardized
sidpy.dataset
objects with rich
metadata [10].

Yes at the appli-
cation level: logs
all commands,
tracks scans/tra-
jectories, and can
orchestrate exter-
nal devices via
FPGA I/O [10].

Supports remote
processing serv-
er for sidpy
datasets and ML(cid:17)-
driven adaptive
experiments [10];
workflow is coded
in Python.

Scanning probe
and STEM
microscopy/char-
acterization for
materials [10].

Python backend
plus a web inter-
face; users con-
figure experiments
via GUI and scripts
[12].

Flexible backend
architecture to in-
tegrate multiple
lab devices; details
of the abstraction
model are not giv-
en in the abstract
[12].

Some stateful or-
chestration: al-
lows switching be-
tween devices and
modifying para-
meters; specific
registry/state se-
mantics not de-
tailed [12].

Focused on or-
chestrating au-
tomated electro-
chemical synthe-
sis with batch
scheduling [12].

Electrochemical
synthesis
automation; open
source [12].

Protocols not
specified;
described as a
Python-based
backend with
multiple device
integrations [12].
No
ROS/SiLA/OPC
UA/REST
mentioned in the
excerpt.

Communication to
hardware is
via vendor-specific
APIs; protocols are
not detailed in the
abstract [24].

Python package;
users write Python
automation code
that seamless-
ly integrates with
Python post-pro-
cessing [24].

Modular organi-
zation with clear
design principles;
supports data ac-
quisition and ex-
periment control
[24].

Acts as a lab
automation frame-
work for its
domain; details
of session/state
management not
available in the
abstract [24].

Workflow is script-
ed in Python; no
explicit workflow
engine is de-
scribed [24].

Laser-ultrasound
experiments;
general lab
automation
concepts [24].

Hardware mod-
ules communicate
via custom proto-
col; no ROS/OPC
UA/REST etc.
specified [13].

Python task de-
finitions (extend-
ed state machine
syntax) and a
GUI for controlling
many setups [13].

Multi-unit syn-
chronization via
shared filesys-
tem and file
watching, not via
network protocols
[27]. Device con-
nections via local
Python APIs.

Python-based
(ImSwitch +
napari), with a
scripting API
(imscripting) and
control module
(imcontrol) [27].

Behavioral tasks
as finite state
machines; hard-
ware modules ex-
pose standardized
signals controlled
by the task [13].

ImSwitch pro-
vides a script-
ing API for hard-
ware and data;
devices are con-
figured and con-
trolled via Python
modules [27].

Yes: central con-
trol software man-
ages multiple se-
tups, runs tasks
in parallel, logs
metadata [13].

Workflow is
the task state
machine; high
throughput mul-
ti-rig operation
[13].

Behavioral neu-
roscience ex-
periments [13].
Open-source, with
extensive online
documentation.

Orchestration via
user scripts
and napari-based
GUI; no generic
lab-wide scheduler
[27].

Advanced
microscopy for
concurrent
acquisition/recon-
struction/analysis
[27].

Yes: the
acquisition
computer runs
scripts that control
devices and
manage data;
concurrency
handled via
mul-
ti-process/file-watch-
er pattern [27].

Comparative notes

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 11/43

Undermind

REPORT CREATED ON
1/12/2026

• Systems like PyLabRobot [6], Pyhamilton [25], Python(cid:17)Microscope [8], AEcroscoPy [10], pyControl [13], ImSwitch [27]
provide strong device abstractions and some internal statefulness but do not position themselves as protocol-bridging
intermediate OS layers, nor do they expose standard network APIs (with the partial exception of ImSwitch’s indirect file-based
multi-node model).

• For your comparison table, they are important as Python-native device layers, but they generally lack:

• Multi-protocol southbound support (ROS/SiLA/OPC UA, etc.).

• A generic network-facing northbound API beyond Python imports.

• Cross-vendor, cross-domain device registries.

3. Standards- and protocol-centric integration efforts (SiLA, ROS, Pyro, etc.)

This group addresses standard protocols or distributed integration but often without a full OS-like device layer or explicit Python
usability at the northbound side.

Comparison table: protocol- and standards-focused works

System / Concept

Protocols / trans-
ports

Python exposure

Device abstraction &
integration pattern

Stateful manager /
workflow

Domain & notes

Bioreactor dynam-
ic scheduling with
SiLA 2 [7]

SiLA 2 device servers
for bioreactors and
sensors (i.e.,
gRPC/protobuf over
HTTP/2), plus a C#
gRPC client
embedded in the LHS
vendor software [7].
No
ROS/OPC UA/REST/bro-
ker use reported.

Core components
(Scheduler, LHS
Server, Simulator) are
written in Python [7].
However, Python talks
to LHS via a mini-
mal message payload
and gRPC is han-
dled in C#; Python
is not using generic
SiLA2/gRPC stubs for
all devices.

SiLA 2 provides stan-
dardized device in-
terfaces; LHS Serv-
er translates Python
scheduler messages
to VENUS methods
(C# arrays etc.) [7].
The system uses LHS
as the low-level ex-
ecutor and does not
attempt to normalize
all device semantics.

Yes: dynamic sched-
uler with real-time
prioritization, con-
straints, and a simu-
lator/digital twin [7]. It
explicitly avoids dupli-
cating vendor respon-
sibilities like labware
tracking.

Parallel bioreac-
tors + Hamilton
LHS; dynamic, con-
straint-aware sched-
uling [7].

LAPP framework &
LAPP(cid:17)DT (conceptual
+ pilot) [17,19,26,18]

Explicitly references
SiLA/SiLA 2, ROS-
, OPC UA, and
enterprise workflow
tools (BPMN/Camun-
da) [17,19,26]. Pilot
implementation uses
SiLA 2 and Biosero
GBG scheduler [18].

The concept pa-
pers note that
SiLA features can
be implemented in
Python [17], but do
not describe concrete
Python SDKs or APIs.

Device Integration
Concepts in Labora-
tory Automation [20]

Survey-level discus-
sion; mentions SiLA,
OPC UA, and other
integration approach-
es [20].

Not specified.

Al-Najjar et al.
instrument-comput-
ing ecosystems
(Pyro-based)
[21,22,23]

Uses Pyro (Python
Remote Objects) for
remote instrument
control [21,22,23].
Data transfer via NAS
mounts; firewall rules
manage network
ports [23]. No
ROS/SiLA/OPC UA/REST.

Python wrappers
around vendor APIs;
Pyro exposes re-
mote methods to
Jupyter notebooks
for workflow orches-
tration [21,22,23].

Proposes LAPP-Ac-
tion Primitives
(LAPP(cid:17)APs) and
LAPP Robot Action
Primitives (RAPs) as
standardized struc-
tural representations
of device operations
[17,26]; a cloud data-
base stores device
metadata and ro-
bot positions (digi-
tal twin) to enable
plug-and-play.

Conceptual taxonomy
of integration archi-
tectures in a biophar-
ma lab [20].

Ad-hoc remote-API
wrapping: each in-
strument API is
wrapped and exposed
via Pyro; no stan-
dardized cross-de-
vice abstraction model
[21,22,23].

Yes conceptually: a
digital twin layer
storing device coor-
dinates, robot poses,
and interaction pat-
terns [19,26], inte-
grated with schedulers
(Camunda, Biosero
GBG) [18].

Focus on mobile
manipulators in
life-science labs,
teaching-free
integration, and
plug-and-play
[17,18,19,20,26,18].
Implementation
details of the “OS” are
still evolving.

Discusses hierarchi-
cal integration and
functional distinctions,
but not a concrete
framework.

Yes, in a light-
weight way: sin-
gle-board comput-
ers act as lo-
cal controllers/gate-
ways; remote steer-
ing plus real-time
ML-based adaptation
(e.g., abnormal I–V
detection) [21,22].

Background context
on integration patterns
[20].

Electrochemistry and
microscopy (Nion mi-
croscopes) [21,22,23].
These systems be-
have like minimalist
device OSs but lack
standardized proto-
cols or a device reg-
istry.

Comparative insights

• SiLA 2 appears in [7] and in the LAPP work [17,18,19,26,18] as the primary lab-device protocol standard; however:
[7] uses it mainly at the driver level, with the orchestrator not directly exposed via generic SiLA2/Python APIs.

•

• LAPP is largely conceptual in the referenced texts; Python exposure and northbound APIs are not yet concretely

described.

• The Al(cid:17)Najjar ecosystem [21,22,23] is a practical example of turning multiple instruments into remote services via Pyro, with
Python as both wrapper and client language. It matches several of your criteria (gateway computers, stateful remote control,
Jupyter-based orchestration) but does not use standard lab protocols nor define a shared device model beyond what individual
wrappers provide.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 12/43

Undermind

REPORT CREATED ON
1/12/2026

4. Apes OS™ and explicit gaps in the current corpus

Your brief explicitly asked for “explicit inclusion and characterization of Apes OS™ as a representative intermediate device
OS approach”. Within the provided references [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]:

• No paper explicitly mentions or characterizes Apes OS™.

• The summaries for HELAO [1], UniLabOS [2], OpenFlexure/LabThings [3,4,5], PyLabRobot [6], ChemOS [15,16], IvoryOS
[14], LAPP [17,18,19,20,26,18], SmartLab [28], and the Pyro-based ecosystems [21,22,23] contain no references to
Apes OS™, nor to a directly comparable proprietary intermediate device OS by that name.

• Consequently, I cannot provide a protocol matrix, device model description, or Python exposure characterization for Apes

OS™ from this corpus.

Implications for your comparison table

• For now, Apes OS™ must be added from external sources, not from the current literature set.

• Conceptually, Apes OS™ belongs in the same comparison class as HELAO [1], UniLabOS [2], and possibly SmartLab [28]:

• A stateful intermediate OS for devices, with a northbound API and southbound protocol adapters.

• When you integrate external Apes OS™ documentation, you will want to align its features along the same axes used here:

• Supported southbound protocols (e.g., serial, OPC UA, SiLA2, custom TCP).

• Northbound APIs and Python exposure (REST/gRPC/Python SDK).

• Device abstraction model (capabilities/features vs resources vs information model).

• Session/device registry semantics, workflow integration, and lab-domain specialization.

5. Synthesis: how the “top findings” compare

From the standpoint of your specific research goal:

• Best exemplars of an intermediate OS with clear Python and HTTP exposure

• HELAO [1] and OpenFlexure/LabThings [3,4] stand out:

• Both use Python to implement a persistent server per device/experiment, exposing HTTP/REST APIs.

• Both maintain long-lived state and support multi-client networked control.

• HELAO additionally supports OPC UA as a southbound protocol [1], aligning more directly with your protocol

coverage axis.

• Most protocol-rich architecture (even if Python exposure is less explicit)

• UniLabOS [2]:

• Explicitly supports ROS 2, OPC UA, Modbus, PLC, TCP/IP.

• Defines a device OS-like resource model (CRUTD, dual topology, digital twin), supporting multi-node orchestration.

• Python usability will likely come via ROS 2 / gRPC tooling, but this is not spelled out in the excerpt.

• Most mature workflow/orchestration layers

• ChemOS [15] and labscript [11] are long-standing orchestration frameworks:

• ChemOS: multi-module architecture for self-driving labs, integrating learning, robotics, characterization, DB, and

interaction [15].

•

labscript: mature shot-based, hardware-timed orchestration with editor, execution, and autonomous optimization
[11].

•

IvoryOS [14] introduces a no-code workflow UI over Python SDLs, but delegates device abstraction to the underlying
SDLs.

• Strong Python device abstraction layers lacking broad protocol bridging

• PyLabRobot [6], Pyhamilton [25], Python(cid:17)Microscope [8], AEcroscoPy [10], pyControl [13], ImSwitch [27], LABS

[12], PLACE [24]:

• Provide robust, reusable Python APIs and stateful abstractions for their domains.

• Do not primarily address multi-protocol integration (ROS/SiLA/OPC UA) or exposure of a reusable northbound

network API (with the exception of some file/network patterns).

For constructing your final comparison table, I recommend:

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 13/43

Undermind

REPORT CREATED ON
1/12/2026

• Treating HELAO [1], UniLabOS [2], OpenFlexure/LabThings [3,4,5], labscript [11], ChemOS [15], IvoryOS [14], SmartLab

[28], and the Pyro ecosystems [21,22,23] as the core intermediate/OS-like entries.

• Treating PyLabRobot [6], Pyhamilton [25], Python(cid:17)Microscope [8], AEcroscoPy [10], pyControl [13], LABS [12], PLACE

[24], ImSwitch [27] as Python device-layer exemplars, noting their lack of multi-protocol bridging.

• Adding Apes OS™ from external documentation and aligning it against these systems on the axes used above.

Timeline

Chronological Evolution of Intermediate Layers and Python(cid:17)Accessible Lab Integration

2013–2015: Early Python(cid:17)Centric Control Stacks Without Standard Protocols

labscript suite (2013) – hardware(cid:17)timed physics experiments

• Conceptual contribution: labscript is one of the earliest clearly modular, Python(cid:17)centric “experiment OS”–like stacks, though

focused on shot(cid:17)based physics experiments (BEC, quantum optics) rather than wet labs [11].

• Architecture:

• Python scripts compile to hardware instruction sequences, queued and executed by BLACS; analysis is integrated via

HDF + ZeroMQ [11].

• Provides a central controller and a modular driver architecture but no use of ROS/SiLA/OPC UA/gRPC/REST; uses

ZeroMQ as the primary network protocol.

• Significance for the later field:

• Demonstrates an early pattern of Python as the orchestration language, with a central controller and pluggable device

drivers.

•

Introduces ideas of queue(cid:17)based orchestration, parameter sweeps, and autonomous optimization loops, which later
reappear in self(cid:17)driving lab stacks [11,15,16,14].

PLACE (2015) – general Python package for lab automation

• Scope: open(cid:17)source Python package for “Laboratory Automation, Control, and Experimentation” with modular organization and

clear design principles [24].

• Characteristics:

• Explicitly lab(cid:17)automation(cid:17)oriented (laser–ultrasound example), but the communication layer and device abstraction model

are not built on ROS/SiLA/OPC UA/etc. [24].

• Functions primarily as a Python SDK + framework rather than an intermediate OS or protocol bridge.

• Historical role:

• Shows early recognition that a general, extensible Python framework for lab automation is valuable.

• Still largely monolithic and stack(cid:17)specific, without standardized multi(cid:17)protocol integration.

Pattern of this phase (2013–2015):

• Python already acts as a unifying language, but most work:

• Uses ad(cid:17)hoc communication (ZeroMQ, custom protocols, vendor APIs).

• Focuses on single domain stacks (physics, a particular lab) with limited aspirations to cross(cid:17)lab or cross(cid:17)protocol

interoperability.

• Lacks explicit device registries or OS(cid:17)like, multi(cid:17)protocol intermediate layers.

2016–2019: Emergence of Self(cid:17)Driving Labs and High(cid:17)Level Orchestrators (Proto(cid:17)Intermediate Layers)

ChemOS (2020, but conceptually a 2010s culmination)

• Positioning: One of the first widely cited “orchestration software” systems for self(cid:17)driving laboratories [15].

• Key ideas:

• A central workflow manager coordinating learning (Bayesian optimization, etc.), robotics/automation, characterization,

databases, and human interaction [15].

• Emphasizes abstracting experiment planning from hardware specifics.

• Limitations vs later systems:

• Treats instrument integration as a per(cid:17)setup engineering task (“implement communication protocol and interaction

layers”), without a standardized device model or explicit protocol bridging (ROS/SiLA/OPC UA/gRPC) [15].

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 14/43

Undermind

• Historical impact:

REPORT CREATED ON
1/12/2026

• Establishes self(cid:17)driving labs and AI(cid:17)driven experiment planning as a core application.

• Provides an early “orchestrator above a heterogeneous device layer,” paving the way for more explicit intermediate OS

layers in ChemOS 2.0 [16], HELAO [1], IvoryOS [14], and UniLabOS [2].

Device Integration Concepts in Laboratory Automation (2020)

• Content: Conceptual analysis of integration strategies in a biopharmaceutical context, distinguishing hierarchical layers and

integration functions [20].

•

Impact:

• Provides a taxonomy of integration approaches in lab automation, anticipating later work on LAPP and digital twins

[17,19,26].

• Recognizes the need for standardized protocols (SiLA, OPC UA, etc.) but remains conceptual.

2020–2021: Strong Move Toward Web/REST and Explicit Device Abstractions

OpenFlexure microscope + LabThings (2021)

• OpenFlexure stack (Collins/Bowman group)

• Simplifying the OpenFlexure microscope software with the Web of Things [4] and related work [3]:

• Embedded Python server (Flask) on Raspberry Pi, exposing microscope capabilities via HTTP REST APIs

following W3C Web of Things (WoT) (properties/actions/events) and documented with OpenAPI [4].

• Provides a Python client, browser GUI, desktop app; devices become stateful network services that persist across

client sessions [4].

• Uses mDNS for discovery and supports extension hooks and semantic typing for capabilities [4].

• LabThings Retro (2023)

• Extends this concept to legacy equipment with an ESP32(cid:17)based retrofit plus LabThings libraries, representing

RS(cid:17)232/USB devices as WoT Things with REST APIs and OpenAPI documentation [5].

• Significance:

• One of the earliest REST/WoT device abstraction stacks explicitly tied to Python usability [3,4,5].

• Begins to realize a device(cid:17)as(cid:17)service pattern that is network(cid:17)native and protocol(cid:17)described (WoT TD + OpenAPI), though

still domain(cid:17)specific (microscopy/retrofits) and not a full intermediate OS.

Python(cid:17)Microscope & related imaging frameworks (Dobbie/Testa clusters)

• Python(cid:17)Microscope (2021) [8,9]:

• Provides abstract base classes for microscope devices (cameras, stages, beams, etc.), with concrete implementations

for many vendors [8].

• Supports distributed devices across multiple computers and uses hardware triggers for synchronization; communi-

cates over Python(cid:17)level RPC, not standard lab protocols [8].

•

ImSwitch/napari (2023) [27]:

• Builds a higher(cid:17)level microscopy automation framework using Python(cid:17)Microscope and local Python scripting; orches-

tration via file(cid:17)watching rather than network protocols [27].

• Significance:

• Establishes robust Python(cid:17)native device abstraction models for imaging, with distributed control and some stateful

management, but without ROS/SiLA/OPC UA/gRPC/REST bridging.

Pyhamilton (2021) – high(cid:17)throughput liquid handling

• Contribution: A Python SDK for Hamilton liquid handlers enabling hardware(cid:17)agnostic pipetting logic, complex scheduling,

closed(cid:17)loop feedback with plate readers, etc. [25].

• Pattern:

• Strong device abstraction (unified pipetting and deck model) and advanced orchestration logic [25].

• Still single(cid:17)vendor(cid:17)family(cid:17)centered, with no standardized protocol layer or protocol bridging.

• Legacy:
•

Influences later liquid(cid:17)handling abstractions like PyLabRobot [6], and is cited in orchestration work (IvoryOS) [14].

HELAO (2021) – hierarchical experimental lab automation & orchestration

• Key step toward intermediate OS behavior [1]:

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 15/43

Undermind

REPORT CREATED ON
1/12/2026

• Every device is a Python FastAPI web server; higher(cid:17)level “actions” are also web servers; experiments are Python dicts

executed by an orchestrator via HTTP [1].

• Supports distributed instruments across multiple machines/OS, device sharing, and both blocking/non(cid:17)blocking driver

semantics [1].

• Explicitly supports OPC UA among its device protocols [1].

• Provides asynchronous locks and explicit concurrency control; integrates provenance logging and FAIR(cid:17)style data

management [1].

• Historical significance:

• One of the first explicitly OS(cid:17)like, HTTP(cid:17)centered, Python(cid:17)first device layers in materials science.

• Positions itself as a lightweight alternative to ROS/ChemOS/bluesky [1], foreshadowing later more OS(cid:17)like architectures

(UniLabOS [2], IvoryOS [14]).

LAPP concept (2021, Wolf/Széll)

• Towards Robotic Laboratory Automation Plug & Play [17]:

•

Introduces LAPP: a framework for plug(cid:17)and(cid:17)play robotic integration with a mobile manipulator, using:
• Cloud database of device interface definitions and LAPP Action Primitives (LAPP(cid:17)APs) [17].

• Explicit references to SiLA, OPC UA, and ROS, and to business process tools (BPMN/Camunda) for orchestration

[17].

• Conceptualizes a device registry + standardized action descriptions, but does not yet implement a full intermediate

OS or Python API.

•

Importance:

• Provides a bridge between robotics (ROS) and lab automation protocols (SiLA/OPC UA) at the conceptual level.

• Lays groundwork for later digital twin work in LAPP(cid:17)DT [19,26] and the SiLA2(cid:17)based pilot [18].

Trend in 2020–2021:

• Clear migration from local(cid:17)only Python stacks to networked, service(cid:17)oriented architectures using:

• HTTP/REST + OpenAPI/WoT (OpenFlexure, LabThings) [3,4,5].

• FastAPI/HTTP for distributed device/action servers (HELAO) [1].

• Emergence of explicit device abstraction layers and first OS(cid:17)like features (stateful servers, locks, device sharing, multi(cid:17)lab

orchestration).

• Standard protocols (OPC UA, SiLA, ROS) start to appear, but mostly at concept/prototype level, with limited Python(cid:17)targeted

tooling in these papers.

2022–2023: Broadening Across Domains and First Explicit Use of SiLA2/gRPC in Python(cid:17)Based Systems

SiLA2(cid:17)based dynamic scheduling for bioreactors (2022)

• Control of parallelized bioreactors I [7]:

•

Implements SiLA2 device servers for a 48(cid:17)parallel bioreactor system, which implies gRPC/protobuf transport [7].

• A Python LHS Scheduler calls an LHS Server that embeds a C# gRPC client into Hamilton’s VENUS environment [7].

• Focus: dynamic scheduling & prioritization, real(cid:17)time adaptation, with a simulator/digital twin concept [7].

• Significance:

• Demonstrates SiLA2 + gRPC in a production(cid:17)like high(cid:17)throughput bioprocessing environment, with Python components in

the orchestration layer.

• Shows a hybrid approach: preserve vendor method editor semantics while layering an external, Python(cid:17)driven scheduler.

LAPP(cid:17)DT and teaching(cid:17)free robot integration (2022)

• Survey and concept proposal [19] and arXiv extension [26]:

• Defines LAPP(cid:17)DT, a digital twin capturing device coordinate systems, standardized robot positions, and metadata for

teaching(cid:17)free mobile manipulator integration [19,26].

• Emphasizes ROS for robot control and SiLA as the lab automation protocol, with a planned SiLA–ROS bridge [19,26].

• Remains largely conceptual; no explicit Python APIs are described.

•

Impact:

• Reinforces the digital twin + standardized protocol trajectory.

• Positions SiLA/ROS interoperability as a key technical target.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 16/43

Undermind

REPORT CREATED ON
1/12/2026

pyControl (2022) – behavior neuroscience experiments

• Characteristics: Python(cid:17)based state machine language, custom I/O modules, centralized GUI for many setups [13].

• Relevance to timeline:

• Another example of a Python(cid:17)native intermediate layer with strong device abstraction and workflow semantics, but no

use of ROS/SiLA/OPC UA/gRPC/REST.

• Contributes to the broader ethos of open, Python(cid:17)based lab control frameworks.

Electrochemistry instrument(cid:17)computing ecosystems (2023, ORNL group)

• Cross(cid:17)facility orchestration of electrochemistry experiments [21], normality detection [22], and cyber framework [23]:

•

Implement Python wrappers around vendor APIs, and expose them over the network via Pyro (Python Remote Objects)
[21,22,23].

• Supporting remote Jupyter(cid:17)based orchestration, with separated data and control planes [21,22,23].

• Trends:

• Reinforces the pattern of Python(cid:17)wrapped devices exposed via custom RPC (Pyro), but not via standardized lab

protocols or OS(cid:17)like device registries.

AEcroscoPy (2023) – autonomous microscopy/electron microscopy framework

• Contribution: Python package as a “hyper(cid:17)language” coordinating LabVIEW VIs and FPGA(cid:17)based control for SPM/STEM

instruments [10].

• Relevance:

• Provides a cross(cid:17)vendor Python abstraction but is domain(cid:17)specific and does not adopt ROS/SiLA/OPC UA/gRPC/REST

[10].

• Shows the pattern of Python layered on top of existing legacy environments (LabVIEW/VIs), similar in spirit to

LHS/SiLA2 architecture [7].

LABS (2023) – orchestration for electrochemical synthesis

• Summary: Open(cid:17)source Python software with a web interface and flexible backend to orchestrate automated electrochemical

synthesis setups [12].

• Trend:

• Another Python + web UI orchestration platform, but there is no explicit use of standardized integration protocols in the

provided excerpt [12].

• Shows the spread of Python(cid:17)based orchestrators across chemistry.

PyLabRobot (2023) – hardware(cid:17)agnostic liquid(cid:17)handling SDK

• Contribution: Provides a hardware(cid:17)agnostic Python abstraction for liquid handlers and accessories, with pluggable back-

ends for Hamilton, Tecan, Opentrons, and BMG plate readers [6].

• Architecture:

• Backends translate canonical commands into device(cid:17)specific firmware or HTTP calls; uses PyUSB/pylibftdi to talk to

firmware where appropriate [6].

• Maintains internal stateful resource management (deck, labware positions) and includes simulation tools [6].

• Significance:

• Extends the device(cid:17)abstraction model pioneered by Pyhamilton [25] into a multi(cid:17)vendor ecosystem.

• Still largely single(cid:17)protocol per backend and not explicitly bridging ROS/SiLA/OPC UA, but is an important building block

for higher(cid:17)level orchestrators (e.g., IvoryOS cites it [14]).

Trend in 2022–2023:

• Proliferation across domains (bioreactors, electrochemistry, microscopy, neuroscience, liquid handling).

• First concrete SiLA2/gRPC deployment with Python components [7].

• Consolidation of Python(cid:17)centric device SDKs with increasingly rich abstractions (PyLabRobot, AEcroscoPy, pyControl,

LABS).

• Still relatively little unified “device OS” thinking; each stack solves integration in its own niche.

2024–2025: Emergence of Explicit Lab “Operating Systems” and Cross(cid:17)SDL Orchestrators

ChemOS 2.0 (2024)

• Full details are not included in the excerpt, but as a successor to ChemOS [15] and a reference point for UniLabOS and IvoryOS

[2,14,16]:

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 17/43

Undermind

REPORT CREATED ON
1/12/2026

• Likely moves ChemOS closer to a modular orchestration architecture with clearer interfaces between learning, device

control, and data layers [16].

• Continues to function primarily as a workflow orchestrator rather than a low(cid:17)level device OS.

• Significance:

• Demonstrates the maturation of orchestration frameworks for self(cid:17)driving labs, influencing newer systems [2,14].

IvoryOS (2025, Hein group) – interoperable web interface for Python(cid:17)based SDLs

• Concept: Presents itself as an orchestrator that auto(cid:17)generates web interfaces for Python(cid:17)based self(cid:17)driving labs (SDLs)

[14].

• Key features:

• Plug(cid:17)in architecture: IvoryOS discovers Python components and their functions and exposes them via a drag(cid:17)and(cid:17)drop

workflow GUI [14].

• A workflow manager supports iterative and closed(cid:17)loop execution, human(cid:17)in(cid:17)the(cid:17)loop operation, and integration with

existing Python lab frameworks (PyLabRobot [6], HELAO [1], ChemOS(cid:17)like systems [16], etc.) [14].

• Position in the stack:

• Primarily a northbound orchestrator/UI that sits above existing Python(cid:17)level device and experiment abstractions.

•

It does not define a new protocol like ROS/SiLA, but normalizes Python APIs into a common interface; the protocol
surface is essentially HTTP/web UI + Python call semantics.

• Historical role:

• Represents a shift from single(cid:17)lab, single(cid:17)stack frameworks to a meta(cid:17)orchestrator spanning multiple, independently

developed SDLs [14].

• Focuses more on human accessibility and interoperability of Python SDLs than on protocol(cid:17)level standardization.

UniLabOS (2025, Zhang group) – AI(cid:17)native OS for autonomous labs

• Most explicit expression of a “device OS” concept in this corpus [2].

• Architectural features:

• Built on ROS 2 / DDS, using a driver(cid:17)as(cid:17)a(cid:17)service model and distributed edge–cloud architecture [2].

•

Implements a dual(cid:17)topology resource model: hierarchical resource tree + physical graph, covering devices, materials,
and logistics [2].

• Defines typed device abstractions (A/R/A&R) and a CRUTD protocol (Create, Read, Update, Transfer, Delete) for

managing materials and long(cid:17)running operations [2].

• Southbound supports Modbus, PLCs, ROS 2, OPC UA, and TCP/IP, with mentions of legacy serial/GPIB/USB [2].

• Maintains digital twins synchronized with telemetry, and performs pre(cid:17)dispatch validation using robotics tooling

(RViz/MoveIt) [2].

• Role vs HELAO and LabThings:

• Where HELAO [1] and LabThings [4,5] are Python + HTTP frameworks with some OS(cid:17)like features, UniLabOS is a

ROS2(cid:17)native, protocol(cid:17)bridging intermediate OS with explicit device registry, resource model, and transactional
semantics [2].

•

It is AI(cid:17)native by design, integrating planning and validation tightly with the device layer [2].

• Gap for this survey:

• The excerpt does not describe Python SDKs or REST/gRPC bindings explicitly, but such bindings are likely straight-

forward given ROS2 and TCP/IP support [2].

• Historical significance:

• Marks a major conceptual convergence: ROS2 + OPC UA + traditional industrial protocols under a single, lab(cid:17)oriented

OS with a rich device/material model.

LAPP pilot implementation with mobERT (2024)

• Paper: Practical SiLA2(cid:17)based implementation of the LAPP concept with a mobile manipulator (mobERT) and Biosero GBG

scheduler [18].

• Contributions:

• Demonstrates SiLA2 as the integration protocol for heterogeneous lab environments, automating HPLC sample prepa-

ration [18].

• Shows a hierarchical workflow decomposition and plug(cid:17)and(cid:17)play configuration in a real pharmaceutical lab setting [18].

• Trend:

• Confirms a path from conceptual frameworks (LAPP, LAPP(cid:17)DT) [17,19,26] to production(cid:17)level, SiLA2(cid:17)centric imple-

mentations.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 18/43

Undermind

REPORT CREATED ON
1/12/2026

SmartLab (2025) – remote interoperable manufacturing lab platform

• Scope: A “fully open(cid:17)source hierarchical computational laboratory automation platform” integrating mechanical test devices,

robotics (mobile manipulator), and legacy equipment retrofitting [28].

• Highlights:

•

Introduces a legacy equipment classification and retrofitting methodology (resonant with LabThings Retro [5]).

• Enables intercontinental remote education and fully automated test campaigns [28].

• Protocol and OS aspects:

• The abstract indicates a hierarchical platform and IoT(cid:17)based communication, but does not give details on

ROS/SiLA/OPC UA/gRPC/REST; deeper study is needed.

• Significance:

• Extends the “remote, interoperable lab” narrative to engineering and education, suggesting these OS(cid:17)like paradigms

are generalizing beyond wet labs.

Trend in 2024–2025:

• Emergence of explicit “Operating System” metaphors (UniLabOS [2]) and meta(cid:17)orchestrators (IvoryOS [14]) on top of the

ecosystem of Python(cid:17)based device frameworks.

• Protocol(cid:17)bridging OS layers become more explicit, especially with ROS2 + OPC UA + industrial protocols (UniLabOS) [2]

and SiLA2(cid:17)based plug(cid:17)and(cid:17)play (LAPP pilot) [18].

•

Increasing concern with digital twins, material lifecycle management, and resource graphs, not only command issuing.

Thematic Trends and Conceptual Trajectories

1. From Device(cid:17)Local Scripts to Networked Device(cid:17)as(cid:17)Service Models

• Early systems (labscript [11], PLACE [24], Python(cid:17)Microscope [8]) treated devices as local libraries or modules.

• Around 2020–2021, frameworks like OpenFlexure/LabThings [3,4,5] and HELAO [1] move to device(cid:17)as(cid:17)service, where

devices run as networked servers with REST/HTTP APIs and standard descriptions (OpenAPI, WoT TD).

• By 2025, UniLabOS [2] generalizes this into an OS(cid:17)like driver(cid:17)as(cid:17)a(cid:17)service model with ROS2/DDS under the hood and

standardized device/resource abstractions.

2. Growing Adoption of Standard Integration Protocols (SiLA2, OPC UA, ROS/ROS2, gRPC)

• SiLA2 + gRPC:

•

Initially conceptual in LAPP [17,19,26], operationalized for bioreactors [7] and mobile manipulator integration [18].

• SiLA2’s gRPC/protobuf basis provides a route to auto(cid:17)generated Python stubs, although explicit use of those is not

detailed in these papers.

• OPC UA:

• HELAO mentions OPC UA among supported device protocols [1].

• UniLabOS positions OPC UA alongside Modbus and PLCs as a southbound protocol [2].

• ROS/ROS2:

• Proposed as the robot backbone in LAPP/LAPP(cid:17)DT [17,19,26] and used natively in UniLabOS [2].

• ROS2’s DDS backbone and QoS features are explicitly used for robust device networking in UniLabOS [2].

• gRPC beyond SiLA2:

• Explicit gRPC usage appears in the SiLA2 bioreactor control [7].

• Many Python(cid:17)centric stacks (HELAO, LabThings) stay with HTTP/REST, but the field clearly recognizes the value of

IDL(cid:17)based, multi(cid:17)language RPC (gRPC/SiLA2).

Overall, the direction of travel is toward formal IDL(cid:17)driven protocols (SiLA2, OPC UA information models, ROS2 interfaces) with
autogenerated Python bindings, although most concrete Python integrations in these papers are still ad(cid:17)hoc or REST(cid:17)based.

3. Increasingly Rich Device Abstraction Models

•

Imperative, device(cid:17)specific commands (Pyhamilton [25], PLACE [24], AeCroscoPy [10]) evolve into hardware(cid:17)agnostic
command sets and capability(cid:17)oriented interfaces (PyLabRobot [6], Python(cid:17)Microscope [8]).

• Lab things & OpenFlexure adopt WoT semantics (properties/actions/events) [4,5], which is a REST(cid:17)friendly device model.

• HELAO defines a layered model: drivers ’ actions ’ experiments, where actions are composition units exposed as services

[1].

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 19/43

Undermind

REPORT CREATED ON
1/12/2026

• SiLA2 and LAPP push toward feature(cid:17)based capabilities and action primitives, including mechanical interaction definitions

[17].

• UniLabOS codifies a resource(cid:17)centric model with A/R/A&R devices, CRUTD operations, and material life(cid:17)cycle semantics [2].

This shows a progression from ad(cid:17)hoc driver functions to semantically meaningful, composable capability models—a
prerequisite for OS(cid:17)like intermediate layers and cross(cid:17)lab orchestration.

4. From Stateless Calls to Stateful Device Managers and Digital Twins

• Many early frameworks effectively treat devices as stateless or manage state implicitly in the controller.

• OpenFlexure/LabThings explicitly provide stateful device servers that remain initialized and handle multiple clients [4,5].

• HELAO adds asynchronous locks, multi(cid:17)threaded concurrency, and explicit driver/action state [1].

•

labscript uses a queued shot model plus BLACS, which is stateful at the shot level [11].

• PyLabRobot tracks deck and labware state, preventing conflicts and enabling validation [6].

• SiLA2 bioreactor control [7] and LAPP(cid:17)DT [19,26] introduce simulators/digital twins and scheduling state.

• UniLabOS explicitly encodes digital twins and resource graphs as first(cid:17)class entities [2].

Overall, there is a clear movement toward stateful intermediate layers with device registries, concurrency control, and digital twins,
which is central to the “device OS” concept.

5. Workflow and Orchestration: From Scripts to Dedicated Engines

• Script(cid:17)only orchestration: labscript [11], PLACE [24], Pyhamilton [25], AEcroscoPy [10], ImSwitch [27], LABS [12] mainly rely

on Python scripts or minimal UI scheduling.

•

Integrated schedulers:

•

labscript’s BLACS + mise components support queued, parameter(cid:17)sweep and closed(cid:17)loop experiments [11].

• HELAO orchestrates experiments encoded as Python dictionaries, including parallel hardware(cid:17)in(cid:17)the(cid:17)loop runs [1].

• SiLA2 bioreactor stack uses a Python Scheduler plus simulator [7].

• High(cid:17)level orchestrators:

• ChemOS and ChemOS 2.0 [15,16] focus on learning(cid:17)centric orchestration across devices and labs.

•

IvoryOS introduces no(cid:17)code workflow design and cross(cid:17)SDL orchestration with iterative/closed(cid:17)loop support [14].

• LAPP considers BPMN/Camunda scheduling and uses Biosero GBG in its pilot [17,18].

• UniLabOS couples resource(cid:17)graph management and transaction semantics with orchestration [2].

The trend is toward formal workflow engines that operate not at the level of low(cid:17)level commands but at the level of capabilities
and resource states—key for robust intermediate OS layers.

6. Python Exposure: From Scripting Language to First(cid:17)Class Client of Protocol(cid:17)Bridging Layers

• Early works treat Python mostly as an orchestration/scripting language operating directly on device drivers (labscript [11],

PLACE [24]).

• Web(cid:17)based frameworks (OpenFlexure/LabThings [3,4,5], HELAO [1]) deliberately expose HTTP APIs and Python clients.

• SiLA2 and OPC UA bring the possibility of auto(cid:17)generated Python stubs, though those are not always explicitly documented

in these papers.

• The ORNL ICE work [21,22,23] and others use Python wrappers as network facades via Pyro or REST.

• Recent OS(cid:17)like systems (UniLabOS [2]) almost certainly support Python clients via ROS2 and TCP/IP, though explicit SDKs

are not described in detail.

Across the timeline, Python has gone from a local scripting environment to a primary northbound client of intermediate layers
and standard protocols.

Key Clusters of Contributors and Their Trajectories

Aspuru(cid:17)Guzik / Sim / Gao / Zhang cluster: Self(cid:17)Driving Labs ’ Lab OS

• ChemOS (2017–2020) [15] ’ ChemOS 2.0 (2024) [16]:

• Pioneers the self(cid:17)driving lab orchestration concept with a strong AI planning focus.

• UniLabOS (2025) [2]:

• Pushes the concept down to the device layer, creating an AI(cid:17)native operating system over ROS2/OPC UA/industrial

protocols.

•

Impact:

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 20/43

Undermind

REPORT CREATED ON
1/12/2026

• This group has been central in shaping both the orchestration and OS layers of autonomous labs, suggesting future
work will further integrate learning, planning, and device OS semantics and perhaps standardize northbound interfaces
(e.g., Python SDKs, REST/gRPC) around UniLabOS(cid:17)like abstractions.

Esvelt / Wierenga / Hein cluster: Liquid Handling & IvoryOS

• Pyhamilton (2021) [25] ’ PyLabRobot (2023) [6]:

• Develops hardware(cid:17)agnostic Python abstractions for liquid handling and accessories.

•

IvoryOS (2025) [14]:

• Cites PyLabRobot and others as pluggable backends [14], and builds a cross(cid:17)SDL orchestrator and UI generator on

top of Python frameworks.

•

Impact:

• This cluster shows a trajectory from device(cid:17)specific SDK ’ multi(cid:17)device abstraction ’ cross(cid:17)platform orchestrator, likely

to continue toward standardized Python component schemas and better protocol(cid:17)level interoperability.

Bowman / Collins / Cicuta cluster: WoT(cid:17)Based Device Services

• OpenFlexure software with WoT [3,4] and LabThings Retro [5]:

• Lead the WoT/REST/OpenAPI(cid:17)centric approach for microscopes and legacy equipment.

•

Impact:

• They establish a pattern for retrofitting legacy devices into HTTP/WoT ecosystems with good Python support.

• Their work suggests a future where WoT(cid:17)style descriptions could serve as one of the northbound representations over

which OS(cid:17)like layers (e.g., UniLabOS, Apes(cid:17)like systems) operate.

Wolf / Széll / Galambos cluster: LAPP, LAPP(cid:17)DT, and SiLA2+ROS

• Works [17,19,20,26,18] form a coherent trajectory:

• From conceptual device integration taxonomies [20] ’ plug(cid:17)and(cid:17)play mobile manipulator framework [17] ’ digital twin

and SiLA–ROS bridge concepts [19,26] ’ SiLA2(cid:17)based pilot [18].

•

Impact:

• Focused on robot–lab integration and plug(cid:17)and(cid:17)play discovery, this cluster is likely to drive standardized mechanical
action primitives and digital twin schemas that could become part of future protocol standards or OS(cid:17)level capabilities.

Microscopy / Imaging clusters (Dobbie/Testa/Bowman)

• Python(cid:17)Microscope [8,9] + ImSwitch [27] + OpenFlexure [3,4] form a rich ecosystem for imaging.

•

Impact:

• They provide well(cid:17)developed Python device abstraction models and distributed control patterns that could be mapped

into OS(cid:17)like systems via SiLA/OPC UA/ROS wrappers.

ORNL Dai / Bridges cluster: Instrument(cid:17)Computing Ecosystems

• Papers [21,22,23] show a consistent Pyro(cid:17)based remote control and data(cid:17)plane separation for electrochemistry and

microscopy.

•

Impact:

• While they do not adopt standardized lab protocols, they illustrate practical cyber(cid:17)infrastructure patterns (control vs

data plane, Jupyter(cid:17)based steering) that will likely be imported into future OS(cid:17)like systems.

Relation to Apes OS™ and Future Directions

• Apes OS™ does not appear in these references, which means:

• The “intermediate device OS” idea is clearly present in multiple independent lines of work (HELAO [1], labscript [11],

UniLabOS [2], IvoryOS [14], OpenFlexure/LabThings [3,4,5]), even without explicit Apes OS citations.

• UniLabOS is the most fully articulated device OS analogue in this corpus [2]; HELAO and LabThings are more “lightweight

OS” or stateful integration middleware [1,4,5].

• For your planned comparison including Apes OS™, the existing timeline suggests:

• Apes OS™ can be positioned as one point in a broader trajectory toward stateful, protocol(cid:17)bridging device OS layers.

• To integrate it into this historical narrative, you can compare:

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 21/43

Undermind

REPORT CREATED ON
1/12/2026

•

•

•

Its protocol coverage (ROS/SiLA/gRPC/REST/OPC UA/message brokers) against UniLabOS, HELAO, and
LabThings.

Its device abstraction model against SiLA2 features, WoT TDs, CRUTD/A&R in UniLabOS, and Python(cid:17)Micro-
scope/PyLabRobot abstractions.

Its stateful device management and workflow hooks against HELAO’s action/expt hierarchy [1], ChemOS 2.0’s
orchestration [16], and IvoryOS’s workflow manager [14].

Given the trends, the future direction of the field is likely to emphasize:

• Convergence of protocols:

• Bridging SiLA2, OPC UA, ROS2, and REST/WoT into unified OS layers with clear Python (and other language) SDKs.

• Formal device and material models:

• Adoption of companion specifications, ontologies, and digital twin schemas (e.g., LAPP(cid:17)DT) as part of the device

OS core.

• Standardized Python component schemas:

• Similar to what IvoryOS implicitly assumes [14], enabling plug(cid:17)and(cid:17)play orchestration across heterogeneous Python SDLs.

• AI(cid:17)native semantics:

• Tight coupling between planning/learning and device/resource layer semantics (as in UniLabOS [2] and ChemOS 2.0

[16]).

This context will help you situate Apes OS™ and other systems within a historically grounded progression from early Python
control scripts through web(cid:17)based device services to modern lab operating systems.

Foundational Work

Which papers form the foundational references on this topic?

The below table shows the resources that are most often cited by the relevant papers on this topic. This is measured by the reference
rate, which is the fraction of relevant papers that cite a resource. Use this table to determine the most important core papers to be
familiar with if you want to deeply understand this topic. Some of these core papers may not be directly relevant to the topic, but
provide important context.

Ref.

[16]

[141]

[142]

[143]

[144]

[145]

[122]

[146]

[147]

[33]

[148]

[6]

[25]

[149]

[150]

Reference
Rate

Title

Cited By These Relevant Papers

0.70

0.43

0.34

0.34

0.25

0.20

0.17

0.16

0.16

0.15

0.15

0.15

0.15

0.12

0.12

ChemOS 2.0: An orchestration architecture for chemical self-driving
laboratories

[2, 14]

OCTOPUS: operation control system for task optimization and job par-
allelization via a user-optimal scheduler

Self-Driving Laboratories for Chemistry and Materials Science

AlabOS: A Python-based Reconfigurable Workflow Management
Framework for Autonomous Laboratories

[14]

[14]

[14]

Array programming with NumPy

[3, 4, 6, 8]

An autonomous laboratory for the accelerated synthesis of novel mate-
rials

[5, 14]

Robotic microscopy for everyone: the OpenFlexure microscope

IPython: A System for Interactive Scientific Computing

Computer Control of Microscopes Using µManager

An Open-Source Modular Framework for Automated Pipetting and
Imaging Applications

Flexible automation accelerates materials discovery

PyLabRobot: An Open-Source, Hardware Agnostic Interface for Liq-
uid-Handling Robots and Accessories

[3, 4, 5]

[3, 4, 6]

[3, 4, 8]

[4, 5]

[14, 16]

[14]

Enabling high(cid:16)throughput biology with flexible open(cid:16)source automation

[6, 7]

A one-piece 3D printed flexure translation stage for open-source mi-
croscopy.

[3, 4]

PyTorch: An Imperative Style, High-Performance Deep Learning Library [6, 8]

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 22/43

REPORT CREATED ON
1/12/2026

Undermind

[151]

[137]

[152]

[81]

[78]

0.12

0.12

0.11

0.11

0.11

High-throughput Approaches to Uncover Synergistic Drug Combina-
tions in Leukemia

[6]

The Internet of Things comes to the lab

Advanced methods of microscope control using ¼Manager software.

Smart device paradigm, Standardization for online labs

RESTlabs: A prototype web 2.0 architecture for Remote Labs

[3, 4]

[3, 4]

[3, 4]

[3, 4]

Adjacent Work

Which papers cite the same foundational papers as relevant papers?

Use this table to discover related papers on adjacent topics, to gain a broader understanding of the field and help generate ideas
for useful new research directions.

Ref.

[43]

[167]

[168]

[141]

[142]

[169]

[143]

[170]

[171]

[172]

[173]

[174]

[175]

[176]

[32]

[177]

[178]

[179]

[180]

[181]

Adjacency
score

Title

References These Foundational Papers

1.25

1.19

1.19

1.16

0.98

0.98

0.78

0.78

0.78

0.78

0.78

0.78

0.69

0.66

0.64

0.60

0.60

0.57

0.57

0.57

Reproducibility in automated chemistry laboratories using computer
science abstractions

[1, 6, 16, 44, 128]

Seamless integration of legacy robotic systems into a self-driving labo-
ratory via NIMO: a case study on liquid handler automation

[1, 12, 16]

Self-driving laboratories with artificial intelligence: An overview of
process systems engineering perspective

[6, 16, 17, 25, 44]

OCTOPUS: operation control system for task optimization and job par-
allelization via a user-optimal scheduler

[1, 12, 16]

Self-Driving Laboratories for Chemistry and Materials Science

[1, 6, 16]

Towards a Modular Architecture for Science Factories

[16, 17, 25, 44]

AlabOS: A Python-based Reconfigurable Workflow Management
Framework for Autonomous Laboratories

An affordable platform for automated synthesis and electrochemical
characterization

Engineering a Sustainable Future: Harnessing Automation, Robotics,
and Artificial Intelligence with Self-Driving Laboratories

A dynamic knowledge graph approach to distributed self-driving labo-
ratories

[1, 16]

[1, 16]

[1, 16]

[1, 16]

A Case Study of Multimodal, Multi-institutional Data Management for the
Combinatorial Materials Science Community

[1, 16]

Designing workflows for materials characterization

Steering towards safe self-driving laboratories

Perspectives for artificial intelligence in bioprocess automation.

Self-Driving Laboratory Optimizes the Lower Critical Solution Temper-
ature of Thermoresponsive Polymers

[1, 16]

[16, 44]

[16, 17]

[14, 16]

An open-source peristaltic pump with multiple independent channels for
laboratory automation

[14, 16]

Evaluating large language model agents for automation of atomic force
microscopy

[16]

Delocalized, asynchronous, closed-loop discovery of organic laser
emitters

Bohrium + SciMaster: Building the Infrastructure and Ecosystem for
Agentic Science at Scale

Advancing materials discovery through artificial intelligence

[16]

[16]

[16]

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 23/43

Undermind

REPORT CREATED ON
1/12/2026

Chat History

Conversation from 1/12/2026

ARES OS

ARES OS is the Air Force Research Laboratory’s open(cid:17)source “autonomous research system” operating system – a general(cid:17)pur-
pose framework for building self(cid:17)driving lab robots rather than a single, fixed setup.

ARES OS

What ARES OS is

From AFRL and related sources:

• Origin & purpose

• Developed at AFRL’s Materials and Manufacturing Directorate to speed materials R&D (initially carbon nanotubes,

now also additive manufacturing and flow chemistry). (Open-source software enables scientists to expedite research
> WIN THE FUTURE > News)

• Made available as open(cid:17)source around 2020–2021; downloadable after filling an AFRL form and also referenced on

GitHub. (Open-source software enables scientists to expedite research > WIN THE FUTURE > News)

• Architecture (high level)

• ARES OS has a core / universal module plus plug(cid:17)ins that connect to:

• Experimental tools/instruments (microscopes, gas controllers, 3D printers, etc.).

• Analysis modules (to process experimental outputs).

• Planning modules (AI/ML algorithms that choose the next experiments). (Open-source software enables scien-

tists to expedite research > WIN THE FUTURE > News)

•

It is explicitly designed to support closed(cid:17)loop autonomous experimentation: design experiment ’ execute ’ analyze
’ choose next experiment.

•

Implementation & language

• The current implementation is primarily in C#/.NET; in an IEEE Spectrum interview, Maruyama notes “currently it’s
programmed in C#” and says they’d like to add direct Python connections to make it easier for Python users to
build research robots. (Let Robots Do Your Lab Work - IEEE Spectrum)

• Use cases

• Deployed on multiple autonomous research robots at AFRL (e.g., carbon nanotube growth, additive manufacturing,

flow chemistry). (Using ARES OS™ software to build your own autonomous research robot | NIST)

• An “Educational ARES OS” variant targets low(cid:17)cost classroom self(cid:17)driving labs (e.g., ~$300 3D(cid:17)printer setups for
schools and university teaching labs). (AI research robots key to ‘democratizing and revolutionizing science,’
world-class AFRL researcher says > Air Force > Features)

• Position in the self(cid:17)driving lab landscape

• NIST and others describe ARES OS as a general(cid:17)purpose autonomous research software platform that struc-

tures:

• hardware/software interface modules,

• analytical feedback,

• AI/ML planners,explicitly to lower the barrier to building autonomous research systems. (Using ARES OS™

software to build your own autonomous research robot | NIST)

•

It is listed alongside HELAO, ChemOS 2.0, PLACE, etc., in community “awesome self(cid:17)driving labs” software lists.
(Software - Awesome Self-Driving Labs)

How it fits our earlier “lab OS / integration layer” axes

Based on public, non(cid:17)paper sources (not the Undermind literature corpus):

• Southbound protocols

• ARES OS does not appear to commit to a single lab protocol (ROS, SiLA2, OPC UA, etc.); instead, you write plug(cid:17)ins
to talk to vendor(cid:17)specific APIs, DAQ hardware, or controllers by whatever comms they use (serial, TCP, vendor SDKs).
I have not seen official documentation claiming built(cid:17)in SiLA2/ROS/OPC(cid:17)UA bridges.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 24/43

Undermind

• Northbound / Python exposure

REPORT CREATED ON
1/12/2026

• As of the IEEE interview, Python is not the primary programming language; the core is C#, and “direct Python

connects” are described as a future goal. (Let Robots Do Your Lab Work - IEEE Spectrum)

• So compared with HELAO or OpenFlexure (which already expose clean HTTP APIs and Python clients), ARES OS

is less Python(cid:17)centric today, though conceptually it is intended to be language(cid:17)agnostic.

• Device abstraction model

• ARES OS organizes systems into:

• device(cid:17)control modules (interfaces to specific instruments),

• analysis modules, and

• planning modules (AI/ML),with experiments executed as part of an integrated closed loop. (Using ARES OS™

software to build your own autonomous research robot | NIST)

•

It’s capability(cid:17)oriented and experiment(cid:17)centric, but the public descriptions do not emphasize a formal information model
like SiLA “features” or OPC UA companion specs.

• Stateful intermediate OS behavior

• Yes – by design ARES OS is a stateful intermediate layer: it keeps track of experiment campaigns, can run on the
order of ~100 autonomous experiments per day vs ~1 manually, and uses past results to plan the next steps. (Anyone
Can Download An Autonomous ‘Research Robot’ From The Air Force Research Laboratory)

• Workflow/orchestration

• Embeds its own planning/orchestration via AI/ML modules rather than being “just” a thin device wrapper. Many

deployments are full self(cid:17)driving labs (CNT synthesis, 3D printing, etc.).

Relation to the Undermind corpus we discussed

• ARES OS was not among the 28 academic papers in the Undermind search results you saw; information here is coming

from:

• AFRL news releases,

• NIST impact story,

• media coverage (Forbes, IEEE Spectrum),

• community software lists.

•

In terms of concept, ARES OS sits in the same broad category as:

• HELAO (Python + FastAPI, some OPC UA)

• UniLabOS (ROS2/DDS + OPC UA/Modbus/PLC; explicit “lab OS”)

• but implemented primarily in C# with a plug(cid:17)in architecture, and with future(cid:17)oriented Python connectivity.

What would you like to do next with ARES OS?
Examples:

• Place ARES OS as a row in your comparison table vs HELAO/UniLabOS/OpenFlexure.

• Drill into how feasible it is to control ARES(cid:17)based systems from Python today.

• Map ARES OS’s architecture more formally onto the device(cid:17)OS abstraction layers we outlined earlier.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 25/43

Undermind

REPORT CREATED ON
1/12/2026

References

[1] Enabling Modular Autonomous Feedback(cid:16)Loops in Materials Science through Hierarchical Experimental Laboratory Automation and Orchestration

F. Rahmanian, ..., and H. Stein. Advanced Materials Interfaces, 2021. 47 citations.
100% Topic Match
Demonstrates a hierarchical, Python-accessible orchestration framework for distributed lab devices.
Implements device drivers as asynchronous HTTP servers (FastAPI), grouping drivers into action servers; experiments encoded as Python dictionaries and invoked
via REST endpoints.
Relevant: lists supported devices/protocols (Table 1) and mentions OPC UA; distinguishes blocking vs non(cid:17)blocking drivers, supports device sharing, async locks,
provenance (HDF5’KaDI4Mat), and positions itself as lightweight alternative to ROS/ChemOS—good candidate for comparison if you need REST/Python SDK
exposure and stateful intermediate orchestration.

[2] UniLabOS: An AI-Native Operating System for Autonomous Laboratories

Jing Gao, ..., and Linfeng Zhang. ArXiv, 2025. 1 citations.
100% Topic Match
Proposes an AI-native, OS-style intermediate layer (UniLabOS) for autonomous laboratories.
Implements a distributed edge–cloud, ROS 2/DDS-based driver-as-a-service with typed A/R/A&R device abstractions and a CRUTD transactional protocol for
material lifecycle.
Southbound support includes Modbus, PLC, ROS 2, OPC UA, TCP/IP (serial/GPIB/USB noted); demonstrates multi-node orchestration and digital-twin sync, but
paper excerpts do not describe SiLA/SiLA2, gRPC/REST endpoints, message-broker use, Python SDKs, or any explicit Apes OS™ comparison.

[3] Modern Microscopy with the Web of Things: The OpenFlexure Microscope Software Stack

J. Collins, ..., and R. Bowman. ArXiv, 2021. 10 citations.
100% Topic Match
Demonstrates a Web-of-Things-based client–server stack for instrument control.
Implements an embedded Raspberry Pi server exposing an HTTP/WoT API described with OpenAPI, plus a web GUI and a Python scripting client.
Relevant for Python-accessible REST/HTTP integration and autogenerated clients, but lacks ROS/SiLA/OPC UA/gRPC/message-broker support and does not
describe device registries, session management, or built-in workflow/orchestration.

[4] Simplifying the OpenFlexure microscope software with the web of things

J. Collins, ..., and R. Bowman. Royal Society Open Science, 2021. 4 citations.
100% Topic Match
Demonstrates a Web-of-Things REST-based, Python-accessible device server for an open-source microscope.
Implements a Flask/Python server (Python-LabThings) on Raspberry Pi exposing WoT properties/actions/events and OpenAPI; clients: browser GUI, Electron app,
Python/MATLAB scripts via HTTP.
Relevant as a stateful intermediate device layer with device registry, persistent sessions, extension hooks and autogenerated clients; no mention of ROS/ROS2,
SiLA/SiLA2, OPC UA, gRPC or message-broker support.

[5] Using old laboratory equipment with modern Web-of-Things standards: a smart laboratory with LabThings Retro

Samuel McDermott, ..., and P. Cicuta. Royal Society Open Science, 2023. 1 citations.
100% Topic Match
Demonstrates a retrofit that exposes legacy lab instruments as Web-of-Things (WoT) REST devices.
Implements an ESP32 gateway + LabThings ESP32 library to bridge serial/USB (RS(cid:17)232) devices to HTTP/REST WoT APIs, using Thing Descriptions and OpenAPI;
provides Python client/server libraries.
Relevant: supports serial-category legacy devices, autogen Python clients via OpenAPI, but is not a stateful intermediate OS nor a full workflow/orchestration engine
(demo shows closed(cid:17)loop only).

[6] PyLabRobot: An Open-Source, Hardware Agnostic Interface for Liquid-Handling Robots and Accessories

Rick P. Wierenga, ..., and K. Esvelt. bioRxiv, 2023. 30 citations.
100% Topic Match
Demonstrates a hardware-agnostic Python SDK for liquid-handling robots.
Implements a unified device-abstraction layer with backends translating to vendor firmware/HTTP, canonical deck/labware models, and Python ABCs.
Relevant: provides Python-first SDK, stateful resource tracking, simulator and tooling; does NOT document ROS/SiLA/OPC UA/gRPC/REST gateways, mes-
sage-broker support, workflow engine, or any Apes OS™ characterization.

[7] Control of parallelized bioreactors I: dynamic scheduling software for efficient bioprocess management in high-throughput systems

L. Bromig, ..., and D. Weuster(cid:16)Botz. Bioprocess and Biosystems Engineering, 2022. 8 citations.
100% Topic Match
Proposes a Python-implemented dynamic scheduler/orchestration stack for parallel mL bioreactors.
Implements Scheduler, LHS Server, Simulator, and SiLA2 device servers (gRPC/protobuf); Python”C# interop via COM-embedded gRPC client for Hamilton VENUS.
Relevant: explicit SiLA2/gRPC and Python exposure, stateful scheduling/resource management and simulator present; lacks ROS/OPC UA/REST/broker support
and no general device(cid:17)registry/OS abstraction beyond scheduler-server.

[8] Python-Microscope – a new open-source Python library for the control of microscopes

David Miguel Susano Pinto, ..., and I. Dobbie. Journal of Cell Science, 2021. 15 citations.
100% Topic Match
Demonstrates a Python library that abstracts and controls heterogeneous microscope hardware.
Implements typed device interfaces (cameras, stages, light sources, etc.), concrete drivers, networked device distribution, and hardware-triggered synchronization
in Python.
Relevant as a device-abstraction and Python-accessible wrapper for lab instruments (supports multi-host setups); lacks explicit coverage of ROS/SiLA/OPC
UA/gRPC/REST or intermediate OS/stateful device-manager features—more a driver/SDK layer than an orchestration/intermediary OS.

[9] Python-Microscope: high performance control of arbitrarily complex and scalable bespoke microscopes

David Miguel, ..., and I. Dobbie. Journal Not Provided, 2021. 3 citations.
99% Topic Match
No summary or abstract available

[10] AEcroscopy: A Software–Hardware Framework Empowering Microscopy Toward Automated and Autonomous Experimentation

Yongtao Liu, ..., and R. Vasudevan. Small Methods, 2023. 19 citations.
99% Topic Match
Demonstrates a Python(cid:17)centric software–hardware platform for automated microscopy.
Implements a Python package (AEcroscoPy) plus LabVIEW VIs and an FPGA to wrap vendor backends, provide standardized datasets, logging, and remote
processing.
Lacks use of standard lab integration protocols (ROS/SiLA/OPC UA/gRPC/REST/message brokers), has no device registry/session management or embedded
workflow engine, and does not mention Apes OS™.

[11] A scripted control system for autonomous hardware-timed experiments.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 26/43

Undermind

REPORT CREATED ON
1/12/2026

P. Starkey, ..., and R. Anderson. The Review of scientific instruments, 2013. 52 citations.
98% Topic Match
Demonstrates a Python-centric, modular experiment-control stack for hardware-timed (shot-based) experiments.
Implements Python-authored experiments compiled into low-level hardware instructions, queued/executed by BLACS, synchronized by a pseudoclock; components
communicate via HDF shot files and ZeroMQ; supports parameter sweeps and closed(cid:17)loop optimization.
Relevant as an open-source, cross-platform device-wrapper/orchestration example (physics/shot focus); lacks SiLA/OPC/ROS/gRPC/REST support, typed device
models, or an explicit persistent device registry/OS semantics.

[12] LABS: Laboratory Automation and Batch Scheduling - A Modular Open Source Python Program for the Control of Automated Electrochemical
Synthesis with a Web Interface.

Maximilian M. Hielscher, ..., and S. R. Waldvogel. Chemistry, an Asian journal, 2023. 10 citations.
94% Topic Match
Proposes an open-source Python-based lab automation and batch-scheduling system (LABS).
Implements a modular backend and web frontend to orchestrate multiple devices, modify routines/parameters, and monitor experiments.
Relevant if you need a Python-accessible orchestration layer, but paper lacks details on protocol support (ROS/SiLA/OPC UA/gRPC/REST), device abstraction
model, stateful device manager semantics, or community/maturity beyond a single electrochemical use case.

[13] Open-source, Python-based, hardware and software for controlling behavioural neuroscience experiments

T. Akam, ..., and M. Walton. eLife, 2022. 32 citations.
93% Topic Match
Demonstrates a Python-based open-source control framework for behavioral neuro experiments.
Implements task specification as Python extended state machines, hardware modules, and a GUI for parallel setups.
Relevant as a device-control stack with Python SDK and stateful session/experiment management, but focused on specific hardware and behavioral tasks (not a
general lab-instrument integration layer nor supporting protocols like ROS/SiLA/OPC UA/gRPC/REST).

[14] IvoryOS: an interoperable web interface for orchestrating Python-based self-driving laboratories

Wenyu Zhang, ..., and Jason E. Hein. Nature Communications, 2025. 4 citations.
90% Topic Match
Proposes an open-source orchestrator (IvoryOS) for Python-based self-driving laboratories.
Implements dynamic web UIs and a drag-and-drop workflow manager that auto-updates based on plugged Python components and their capabilities.
Relevant if you need a Python-accessible orchestration/UI layer; paper lacks detailed protocol bridging (ROS/SiLA/OPC UA/gRPC/REST) or low-level device-wrapper
characterization—focus is on high-level SDL interoperability, no explicit mention of stateful device-manager semantics, protocol support, or Apes OS™ comparison.

[15] ChemOS: An orchestration software to democratize autonomous discovery

L. Roch, ..., and Alán Aspuru-Guzik. PLoS ONE, 2020. 118 citations.
83% Topic Match
Proposes a portable, modular orchestration framework for self-driving laboratories.
Implements a central workflow manager plus modules for learning, robotics control, characterization, databases, researcher interaction, and online analysis to map
abstract plans to hardware.
Lacks explicit protocol listings or detailed Python/REST/gRPC/SiLA/OPC UA bindings in the paper excerpt; hardware integration requires manual implementation
of communication/interaction layers and no explicit device registry/stateful intermediate OS is described.

[16] ChemOS 2.0: An orchestration architecture for chemical self-driving laboratories

Malcolm Sim, ..., and Alán Aspuru-Guzik. Matter, 2024. 49 citations.
72% Topic Match
No summary or abstract available

[17] Towards Robotic Laboratory Automation Plug & Play: The "LAPP" Framework

Ádám Wolf, ..., and K. Széll. SLAS technology, 2021. 41 citations.
63% Topic Match
Proposes a protocol-agnostic plug(cid:17)and(cid:17)play framework for robotic lab automation.
Describes a MoMa mobile manipulator using SLAM/vision to discover devices and fetch interface/protocol definitions and LAPP(cid:17)Action Primitives from a cloud
registry.
Lacks concrete wrapper/SDK/REST/gRPC/OPC UA implementation details or a Python SDK; cites SiLA/OPC UA/ROS and enterprise schedulers as compatible
technologies.

[18] Towards Robotic Laboratory Automation Plug & Play: LAPP Pilot Implementation with the mobERT Mobile Manipulator

Ádám Wolf, ..., and K. Széll. 2024 IEEE 22nd Jubilee International Symposium on Intelligent Systems and Informatics (SISY), 2024. 2 citations.
61% Topic Match
Demonstrates a SiLA 2–based plug-and-play robotic lab integration (LAPP) pilot.
Implements a mobERT mobile manipulator integrated via SiLA 2, hierarchical workflow decomposition, and Biosero GBG scheduler for HPLC sample prep.
Relevant because it describes a reusable SiLA2 wrapper/adapter and workflow orchestration in a wet(cid:17)lab setting; lacks explicit mention of Python APIs,
REST/gRPC/OPC-UA bridging, or stateful intermediate-OS features (device registry, session management) in the summary.

[19] Towards Robotic Laboratory Automation Plug & Play: Survey and Concept Proposal on Teaching-free Robot Integration with the LAPP Digital
Twin.

Ádám Wolf, ..., and P. Galambos. SLAS technology, 2022. 5 citations.
53% Topic Match
Proposes a teaching-free, plug-&-play integration framework for mobile manipulators in labs.
Defines a digital-twin data model (device coordinate frames, predefined robot poses, metadata) plus fiducial-vision localization and cites ROS and SiLA (with a
planned SiLA–ROS bridge) for interoperability.
High-level/conceptual only: no implementation, SDKs/wrappers, Python APIs, stateful device-manager details, workflow engine, or specific characterization of Apes
OS™.

[20] Device Integration Concepts in Laboratory Automation

Ádám Wolf, ..., and K. Széll. 2020 IEEE 24th International Conference on Intelligent Engineering Systems (INES), 2020. 10 citations.
48% Topic Match
Analyzes device-integration approaches for laboratory automation systems.
Reviews hierarchical/function-based integration concepts and discusses two concrete implementation examples in a biopharma lab context.
Provides conceptual comparison of integration patterns (protocol/adapter, central managers, workflow roles) but lacks detailed protocol lists, explicit Python SDK
examples, or thorough characterization of REST/gRPC/SiLA/ROS/OPC UA support—useful for high-level framing but insufficient alone to populate the detailed
comparison table.

[21] Cross-Facility Orchestration of Electrochemistry Experiments and Computations

Anees Al-Najjar, ..., and S. Dai. Proceedings of the SC '23 Workshops of the International Conference on High Performance Computing, Network,
Storage, and Analysis, 2023. 3 citations.
41% Topic Match
Demonstrates a networked orchestration ecosystem for electrochemistry instruments.
Implements Python wrappers and custom Pyro client–server modules to enable remote operation and automated workflows (Jupyter-driven) across pumps, fraction
collectors, potentiostats.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 27/43

Undermind

REPORT CREATED ON
1/12/2026

Relevant because it provides Python-accessible device wrappers and a stateful remote-control layer for lab instruments, but focuses on a specific electrochemistry
setup (proprietary/custom adapters, no mention of SiLA/ROS/OPC(cid:17)UA/gRPC standards or broader device registry/intermediate OS features).

[22] Normality of I-V Measurements Using ML

Anees Al-Najjar, ..., and S. Dai. 2023 IEEE 19th International Conference on e-Science (e-Science), 2023. 2 citations.
34% Topic Match
Demonstrates a Python-based instrument-computing ecosystem for adaptive electrochemistry experiments.
Implements Python wrappers for vendor APIs and Pyro client–server modules to execute instrument commands remotely from a Jupyter notebook.
No evidence of standard lab protocols (ROS/SiLA/OPC UA/gRPC/REST/message brokers), unified device-abstraction, device registry/stateful intermediate OS, or
workflow engine; Apes OS™ not mentioned.

[23] Cyber Framework for Steering and Measurements Collection Over Instrument-Computing Ecosystems

Anees Al-Najjar, ..., and Craig Bridges. 2023 IEEE International Conference on Smart Computing (SMARTCOMP), 2023. 3 citations.
31% Topic Match
Demonstrates a Python-based cyber framework for remote steering and measurement collection.
Wraps vendor instrument APIs in cross-platform Python, exposes them via Pyro RPC, and separates network control/data planes for transfers.
Lacks use of ROS/SiLA/OPC UA/gRPC/REST/message brokers, has no device registry/session management or built-in orchestration (not Apes OS™); demon-
strated on Nion microscopes with Jupyter-driven workflows.

[24] PLACE

Jami L. Johnson, ..., and K. van Wijk. Journal of Laboratory Automation, 2015. 286 citations.
20% Topic Match
Demonstrates a Python-based, open-source laboratory automation/control framework (PLACE).
Implements a modular, extensible Python package for experiment automation, data acquisition, and analysis integration.
Relevant if you need a Python-native SDK/wrapper for device automation, but paper lacks explicit protocol bridging (ROS/SiLA/OPC UA/gRPC/ MQTT) or an
intermediate device-OS/manager; evaluate for device abstraction and workflow features by checking code/examples for driver interfaces and stateful device
management.

[25] Enabling high(cid:16)throughput biology with flexible open(cid:16)source automation

Emma J. Chory, ..., and K. Esvelt. Molecular Systems Biology, 2021. 55 citations.
13% Topic Match
Demonstrates an open-source Python SDK for Hamilton liquid(cid:17)handling automation.
Implements Python classes for robot actions/consumables, scheduling, simulation, error handling, and closed(cid:17)loop control with integrated plate reader.
Hardware(cid:17)specific (Hamilton + custom peripherals); no evidence of REST/gRPC/OPC UA/ROS/SiLA, cross(cid:17)device registry, protocol bridging, networked northbound
APIs, or any Apes OS™ characterization.

[26] Towards Robotic Laboratory Automation Plug & Play: Teaching-free Robot Integration with the LAPP Digital Twin

Ádám Wolf, ..., and P. Galambos. ArXiv, 2022. 0 citations.
13% Topic Match
Proposes a digital-twin-based framework for teaching-free robot integration in labs.
Implements a DT storing robot-relevant info (standardized arm positions) and outlines top-level scheduling/orchestration (evaluating BPMN, LabOP).
Relevant points: uses ROS for low-level control, discusses SiLA and a possible SiLA–ROS bridge; lacks concrete intermediate-OS/device-manager implementation
details, explicit protocol matrix (gRPC/REST/OPC UA/brokers), Python APIs, stateful registry/session behavior, or any Apes OS™ characterization.

[27] An open-source microscopy framework for simultaneous control of image acquisition, reconstruction, and analysis

Xavier Casas Moreno, ..., and Ilaria Testa. HardwareX, 2023. 9 citations.
11% Topic Match
Demonstrates a Python-based microscopy automation framework for concurrent acquisition, reconstruction, and analysis.
Implements this by running user Python scripts on acquisition hosts, using ImSwitch (imscripting/imcontrol) + imreconstruct and a napari file-watcher to synchronize
via shared filesystem (Zarr/HDF5/OME(cid:17)Zarr).
Relevant notes: focused on microscopy/wet(cid:17)lab imaging; no network APIs or protocol bridges (ROS/SiLA/OPC UA/gRPC/REST/message brokers), no device registry
or stateful intermediate “OS”, and orchestration limited to file-watching rather than a workflow engine.

[28] SmartLab: Flexible and interoperable manufacturing laboratory system for remote education and research using a mobile manipulator

Won-Jae Yun, ..., and Sung-Hoon Ahn. J. Comput. Des. Eng., 2025. 0 citations.
8% Topic Match
Proposes an open-source, hierarchical lab automation platform for remote operation with a mobile manipulator.
Implements IoT-based retrofits for legacy equipment, a device hierarchy, and high-level command interfaces to run remote experiments and education.
Ambiguity: paper mentions interoperability and IoT communication but does not detail supported protocols (ROS/SiLA/OPC UA/gRPC/REST) or explicit Python
SDK/REST bindings—check full text for protocol stacks, device abstraction model, stateful device-manager, and workflow/orchestration features.

[29] Instrumentino: An Open-Source Software for Scientific Instruments.
Israel Joel Koenka, ..., and P. Hauser. Chimia, 2015. 19 citations.
7% Topic Match
Abstract: Scientists often need to build dedicated computer-controlled experimental systems. For this purpose, it is becoming common to employ open-source
microcontroller platforms, such as the Arduino. These boards and associated integrated software development environments provide affordable yet powerful solutions
for the implementation of hardware control of transducers and acquisition of signals from detectors and sensors. It is, however, a challenge to write programs that
allow interactive use of such arrangements from a personal computer. This task is particularly complex if some of the included hardware components are connected
directly to the computer and not via the microcontroller. A graphical user interface...

[30] An Intelligent Automation Platform for Rapid Bioprocess Design

Tianyi Wu and Yuhong Zhou. Jala (Charlottesville, Va.), 2014. 17 citations.
7% Topic Match
Abstract: Bioprocess development is very labor intensive, requiring many experiments to characterize each unit operation in the process sequence to achieve
product safety and process efficiency. Recent advances in microscale biochemical engineering have led to automated experimentation. A process design workflow
is implemented sequentially in which (1) a liquid-handling system performs high-throughput wet lab experiments, (2) standalone analysis devices detect the data,
and (3) specific software is used for data analysis and experiment design given the user’s inputs. We report an intelligent automation platform that integrates these
three activities to enhance the efficiency of such a workflow. A multiagent intelligent architecture...

[31] The qPCRBot: Combining Automated Data Handling, Standardization, and Robotic Labware Transport for Better qPCR Measurements

Henning Zwirnmann, ..., and Sami Haddadin. 2025 IEEE International Conference on Robotics and Automation (ICRA), 2025. 0 citations.
5% Topic Match
Abstract: Laboratory automation is a key driver for higher efficiency and reproducibility of experiments and measurements in natural science laboratories. One
process that is particularly susceptible to both manual errors in the physical handling of labware, faulty data analyses, and incomplete reporting is the quantitative
Polymerase Chain Reaction (qPCR). It is a ubiquitous analysis method in biolaboratories to amplify and measure the amount of a specific DNA sequence in a
sample. Our system, which we call the qPCRBot, addresses these issues through three key pillars: automating data analysis and handling processes, standardizing
data management and system communication protocols, and utilizing a...

[32] Self-Driving Laboratory Optimizes the Lower Critical Solution Temperature of Thermoresponsive Polymers

Guoyue Xu, ..., and Tengfei Luo. ArXiv, 2025. 0 citations.
4% Topic Match

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 28/43

Undermind

REPORT CREATED ON
1/12/2026

Abstract: To overcome the inherent inefficiencies of traditional trial-and-error materials discovery, the scientific community is increasingly developing autonomous
laboratories that integrate data-driven decision-making into closed-loop experimental workflows. In this work, we realize this concept for thermoresponsive polymers
by developing a low-cost,"frugal twin"platform for the optimization of the lower critical solution temperature (LCST) of poly(N-isopropylacrylamide) (PNIPAM). Our
system integrates robotic fluid-handling, on-line sensors, and Bayesian optimization (BO) that navigates the multi-component salt solution spaces to achieve
user-specified LCST targets. The platform demonstrates convergence to target properties within a minimal number of experiments. It strategically explores the
parameter space, learns from informative"off-target"results, and...

[33] An Open-Source Modular Framework for Automated Pipetting and Imaging Applications

Ouyang Wei, ..., and Benedict Diederich. bioRxiv, 2021. 21 citations.
4% Topic Match
Abstract: The number of samples in biological experiments are continuously increasing, but complex protocols and human experimentation in many cases lead to
suboptimal data quality and hence difficulties in reproducing scientific findings. Laboratory automation can alleviate many of these problems by precisely reproducing
machine-readable protocols. These instruments generally require high up-front investments and due to lack of open APIs they are notoriously difficult for scientists
to customize and control outside of the vendor-supplied software. Here, we demonstrate automated, high-throughput experiments for interdisciplinary research in
life science that can be replicated on a modest budget, using open tools to ensure reproducibility by...

[34] Not your grandmother’s toolbox – the Robotics Toolbox reinvented for Python

Peter Corke and Jesse Haviland. 2021 IEEE International Conference on Robotics and Automation (ICRA), 2021. 106 citations.
4% Topic Match
Abstract: For 25 years the Robotics Toolbox for MATLAB® has been used for teaching and research worldwide. This paper describes its successor – the Robotics
Toolbox for Python. More than just a port, it takes advantage of popular open-source packages and resources to provide platform portability, fast browser-based 3D
graphics, quality documentation, fast numerical and symbolic operations, powerful IDEs, shareable and web-browseable notebooks all powered by GitHub and the
open-source community. The new Toolbox provides well-known functionality for spatial mathematics (homogeneous transformations, quaternions, triple angles and
twists), trajectories, kinematics (zeroth to second order), dynamics and a rich assortment of robot models....

[35] Facile Integration of Robots into Experimental Orchestration at Scientific User Facilities

Chandima Fernando, ..., and Phillip M. Maffettone. 2024 IEEE International Conference on Robotics and Automation (ICRA), 2024. 2 citations.
3% Topic Match
Abstract: Integration of robots into scientific user facilities, such as the National Synchrotron Light Source II, improves their efficiency and capacity. Many such
facilities use the opensource Bluesky project for experimental control and orchestration. However, there remains an open challenge in deploying robotic solutions at
these facilities that are reconfigurable, extensible, and compatible with pre-existing software infrastructure. Herein, we introduce a framework that uses the Robotic
Operating System 2 (ROS2) and Bluesky to provide extensible robotic applications, while working under the operational constraints of a large-scale user facility. We
demonstrated this framework by integrating a robotic arm to pick and place...

[36] Autonomous Elemental Characterization Enabled by a Low Cost Robotic Platform Built Upon a Generalized Software Architecture

Xuan Cao, ..., and Michael L. Whittaker. ArXiv, 2025. 0 citations.
3% Topic Match
Abstract: Despite the rapidly growing applications of robots in industry, the use of robots to automate tasks in scientific laboratories is less prolific due to lack of
generalized methodologies and high cost of hardware. This paper focuses on the automation of characterization tasks necessary for reducing cost while maintaining
generalization, and proposes a software architecture for building robotic systems in scientific laboratory environment. A dual-layer (Socket.IO and ROS) action server
design is the basic building block, which facilitates the implementation of a web-based front end for user-friendly operations and the use of ROS Behavior Tree for
convenient task planning and execution....

[37] Autonomous mobile robots for exploratory synthetic chemistry

Tianwei Dai, ..., and Andrew I. Cooper. Nature, 2024. 133 citations.
2% Topic Match
Abstract: Autonomous laboratories can accelerate discoveries in chemical synthesis, but this requires automated measurements coupled with reliable deci-
sion-making1,2. Most autonomous laboratories involve bespoke automated equipment3–6, and reaction outcomes are often assessed using a single, hard-wired
characterization technique7. Any decision-making algorithms8 must then operate using this narrow range of characterization data9,10. By contrast, manual
experiments tend to draw on a wider range of instruments to characterize reaction products, and decisions are rarely taken based on one measurement alone. Here
we show that a synthesis laboratory can be integrated into an autonomous laboratory by using mobile robots11–13 that operate equipment and make decisions...

[38] Wrapyfi: A Python Wrapper for Integrating Robots, Sensors, and Applications across Multiple Middleware

Fares Abawi, ..., and Stefan Wermter. 2024 19th ACM/IEEE International Conference on Human-Robot Interaction (HRI), 2023. 7 citations.
2% Topic Match
Abstract: Message oriented and robotics middleware play an important role in facilitating robot control, abstracting complex functionality, and unifying communication
patterns between sensors and devices. However, using multiple middleware frameworks presents a challenge in integrating different robots within a single system.
To address this challenge, we present Wrapyfi, a Python wrapper supporting multiple message oriented and robotics middleware, including ZeroMQ, YARP, ROS,
and ROS 2. Wrapyfi also provides plugins for exchanging deep learning framework data, without additional encoding or preprocessing steps. Using Wrapyfi eases
the development of scripts that run on multiple machines, thereby enabling cross-platform communication and workload distribution. We...

[39] A RoboStack Tutorial: Using the Robot Operating System Alongside the Conda and Jupyter Data Science Ecosystems

Tobias Fischer, ..., and Michael Milford. IEEE Robotics & Automation Magazine, 2021. 12 citations.
2% Topic Match
Abstract: The Robot Operating System (ROS) has become the de facto standard middleware in the robotics community [1]. ROS bundles everything, from low-level
drivers to tools that transform among coordinate systems, to state-of-the-art perception and control algorithms. One of ROS’s key merits is the rich ecosystem of
standardized tools to build and distribute ROS-based software.

[40] Microscope-Cockpit: Python-based bespoke microscopy for bio-medical science

M. Phillips, ..., and I. Dobbie. Wellcome Open Research, 2021. 14 citations.
2% Topic Match
Abstract: We have developed “Microscope-Cockpit” (Cockpit), a highly adaptable open source user-friendly Python-based GUI environment for precision control of
both simple and elaborate bespoke microscope systems. The user environment allows next-generation near-instantaneous navigation of the entire slide landscape
for efficient selection of specimens of interest and automated acquisition without the use of eyepieces. Cockpit uses “Python-Microscope” (Microscope) for
high-performance coordinated control of a wide range of hardware devices using open source software. Microscope also controls complex hardware devices such
as deformable mirrors for aberration correction and spatial light modulators for structured illumination via abstracted device models. We demonstrate the advantages
of...

[41] The middleware revolution: bridging automation gaps in laboratory processes.

Bill Harten. MLO: medical laboratory observer, 2012. 2 citations.
2% Topic Match
No summary or abstract available

[42] Heron: A Knowledge Graph editor for intuitive implementation of python based experimental pipelines

G. Dimitriadis, ..., and A. Akrami. bioRxiv, 2024. 1 citations.
1% Topic Match
Abstract: To realise a research project idea, an experimenter faces a series of conflicting design and implementation considerations, regarding both its hardware
and software components. For instance, the ease of implementation, in time and expertise, should be balanced against the ease of future reconfigurability and
number of ‘black box’ components. Other, often conflicting, considerations include the level of documentation and ease of reproducibility, resource availability as
well as access to online communities. To alleviate this balancing act between opposing requirements we present Heron, a new Python-based platform to construct
and run experimental and data analysis pipelines. Heron’s main principle is to...

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 29/43

Undermind

REPORT CREATED ON
1/12/2026

[43] Reproducibility in automated chemistry laboratories using computer science abstractions

Richard B. Canty and M. Abolhasani. Nature Synthesis, 2024. 17 citations.
1% Topic Match
No summary or abstract available

[44] ARChemist: Autonomous Robotic Chemistry System Architecture*

Hatem Fakhruldeen, ..., and Andrew I. Cooper. 2022 International Conference on Robotics and Automation (ICRA), 2022. 41 citations.
1% Topic Match
Abstract: Automated laboratory experiments have the potential to propel new discoveries, while increasing reproducibility and improving scientists' safety when
handling dangerous materials. However, many automated laboratory workflows have not fully leveraged the remarkable advancements in robotics and digital lab
equipment. As a result, most robotic systems used in the labs are programmed specifically for a single experiment, often relying on proprietary architectures or
using unconventional hardware. In this work, we tackle this problem by proposing a novel robotic system architecture specifically designed with and for chemists,
which allows the scientist to easily reconfigure their setup for new experiments. Specifically, the system's...

[45] Enabling reactive microscopy with MicroMator

Z. Fox, ..., and Grégory Batt. Nature Communications, 2022. 34 citations.
1% Topic Match
Abstract: Microscopy image analysis has recently made enormous progress both in terms of accuracy and speed thanks to machine learning methods and improved
computational resources. This greatly facilitates the online adaptation of microscopy experimental plans using real-time information of the observed systems and
their environments. Applications in which reactiveness is needed are multifarious. Here we report MicroMator, an open and flexible software for defining and driving
reactive microscopy experiments. It provides a Python software environment and an extensible set of modules that greatly facilitate the definition of events with
triggers and effects interacting with the experiment. We provide a pedagogic example...

[46] pyControl: Open source, Python based, hardware and software for controlling behavioural neuroscience experiments

T. Akam, ..., and M. Walton. bioRxiv, 2021. 7 citations.
1% Topic Match
Abstract: Laboratory behavioural tasks are an essential research tool. As questions asked of behaviour and brain activity become more sophisticated, the ability to
specify and run richly structured tasks becomes more important. An increasing focus on reproducibility also necessitates accurate communication of task logic to
other researchers. To these ends we developed pyControl, a system of open source hardware and software for controlling behavioural experiments comprising; a
simple yet flexible Python-based syntax for specifying tasks as extended state machines, hardware modules for building behavioural setups, and a graphical user
interface designed for efficiently running high throughput experiments on many setups in...

[47] Middleware solutions for service-oriented remote laboratories: A review

M. Tawfik, ..., and M. Castro. 2014 IEEE Global Engineering Education Conference (EDUCON), 2014. 8 citations.
1% Topic Match
No summary or abstract available

[48] REMS: Middleware for Robotics Education and Development
Yusuke Tanaka and Ankur M. Mehta. ArXiv, 2022. 0 citations.
1% Topic Match
Abstract: This paper introduces REMS, a robotics middleware and control framework that is designed to introduce the Zen of Python to robotics and to improve
robotics education and development flow. Although existing middleware can serve hardware abstraction and modularity, setting up environments and learning
middleware-specific syntax and procedures are less viable in education. They can curb opportunities to understand robotics concepts, theories, and algorithms.
Robotics is a field of integration; students and developers from various backgrounds will be involved in programming. Establishing Pythonic and object-oriented
robotic framework in a natural way can enhance modular and abstracted programming for better readability, reusability,...

[49] Experiment Specification, Capture and Laboratory Automation Technology (ESCALATE): a software pipeline for automated chemical experi-
mentation and data management

Ian M. Pendleton, ..., and Joshua Schrier. MRS Communications, 2019. 61 citations.
1% Topic Match
Abstract: Applying artificial intelligence to materials research requires abundant curated experimental data and the ability for algorithms to request new experiments.
ESCALATE (Experiment Specification, Capture and Laboratory Automation Technology)—an ontological framework and opensource software package—solves
this problem by providing an abstraction layer for human- and machine-readable experiment specification, comprehensive and extensible (meta-) data capture,
and structured data reporting. ESCALATE simplifies the initial data collection process, and its reporting and experiment generation mechanisms simplify machine
learning integration. An initial ESCALATE implementation for metal halide perovskite crystallization was used to perform 55 rounds of algorithmically-controlled
experiment plans, capturing 4336 individual experiments.

[50] PyRobot: An Open-source Robotics Framework for Research and Benchmarking

Adithyavairavan Murali, ..., and A. Gupta. ArXiv, 2019. 113 citations.
1% Topic Match
Abstract: This paper introduces PyRobot, an open-source robotics framework for research and benchmarking. PyRobot is a light-weight, high-level interface on top of
ROS that provides a consistent set of hardware independent mid-level APIs to control different robots. PyRobot abstracts away details about low-level controllers and
inter-process communication, and allows non-robotics researchers (ML, CV researchers) to focus on building high-level AI applications. PyRobot aims to provide
a research ecosystem with convenient access to robotics datasets, algorithm implementations and models that can be used to quickly create a state-of-the-art
baseline. We believe PyRobot, when paired up with low-cost robot platforms such as LoCoBot,...

[51] Autonomous Liquid-handling Robotics Scripting for Accessible and Responsible Protein Engineering

Yuan Gao, ..., and Tong Si. bioRxiv, 2025. 0 citations.
1% Topic Match
No summary or abstract available

[52] Design of an API for Integrating Robotic Software Frameworks

Min Ho Lee, ..., and B. MacDonald. Unknown journal, 2014. 5 citations.
0% Topic Match
No summary or abstract available

[53] Controlling and scripting laboratory hardware with open-source, intuitive interfaces: OpenFlexure Voice Control and OpenFlexure Blockly

Samuel McDermott, ..., and Pietro Cicuta. Royal Society Open Science, 2022. 1 citations.
0% Topic Match
Abstract: Making user interaction with laboratory equipment more convenient and intuitive should promote experimental work and help researchers to complete their
tasks efficiently. The most common form of interaction in current instrumentation is either direct tactile, with buttons and knobs, or interfaced through a computer,
using a mouse and keyboard. Scripting is another function typical of smart and automated laboratory equipment, yet users are currently required to learn bespoke
programming languages and libraries for individual pieces of equipment. In this paper, we present two open-source, novel and intuitive ways of interacting with and
scripting laboratory equipment. We choose the OpenFlexure family...

[54] Open-source multi-purpose remote laboratory for IoT education

D. Pirrone, ..., and Dario Assante. 2021 IEEE Global Engineering Education Conference (EDUCON), 2021. 13 citations.
0% Topic Match

Abstract: With the constant growth of devices connected to the internet, many researchers focus their interest on the development of Remote Laboratories, taking
advantage of the numerous electronic open-source platforms. The aim of this work is to propose a compact solution (hardware and software) for the implementation

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 30/43

Undermind

REPORT CREATED ON
1/12/2026

of a low-cost open-access remote laboratory. The key concept is using Python, a programming language that is strong, flexible and rich of free external packages.
Specifically, Python is used at the same time as: (i) a microframework with server functionalities, (ii) a control unit that drives an Arduino microcontroller and a
Raspberry Pi microcomputer....

[55] DAQling: an open-source data acquisition framework

M. Boretto, ..., and Viktor Vilhelm Sonesten. EPJ Web of Conferences, 2020. 6 citations.
0% Topic Match
Abstract: The Data AcQuisition (DAQ) software for most applications in high energy physics is composed of common building blocks, such as a networking layer,
plug-in loading, configuration, and process management. These are often re-invented and developed from scratch for each project or experiment around specific
needs. In some cases, time and available resources can be limited and make development requirements difficult or impossible to meet. Moved by these premises,
our team developed an open-source lightweight C++ software framework called DAQling, to be used as the core for the DAQ systems of small and medium-sized
experiments and collaborations. The framework offers a...

[56] EvoBot: An Open-Source, Modular, Liquid Handling Robot for Scientific Experiments

A. Faíña, ..., and K. Støy. Applied Sciences, 2020. 39 citations.
0% Topic Match
Abstract: Commercial liquid handling robots are rarely appropriate when tasks change often, which is the case in the early stages of biochemical research. In order
to address it, we have developed EvoBot, a liquid handling robot, which is open-source and employs a modular design. The combination of an open-source and a
modular design is particularly powerful because functionality is divided into modules with simple, well-defined interfaces, hence customisation of modules is possible
without detailed knowledge of the entire system. Furthermore, the modular design allows end-users to only produce and assemble the modules that are relevant
for their specific application. Hence, time...

[57] Improving the Scalability and Replicability of Embedded Systems Remote Laboratories Through a Cost-Effective Architecture

Aitor Villar-Martínez, ..., and D. López-de-Ipiña. IEEE Access, 2019. 35 citations.
0% Topic Match
Abstract: Online remote laboratories are a particularly promising tool for effective STEM education. They offer online universal access to different hardware devices
in which students can experiment and can test and improve their knowledge. However, most of them have two significant limitations. First, given that most of them
are developed as, or evolve from single-user proofs of concept, they have no scalability provisions other than full laboratory replication. And second, when this is
done, cost efficiency is often neglected. This paper presents the requirements for the creation of a novel remote laboratory architecture focused on, but not limited
to, embedded systems...

[58] Lab Automation

Aditya Batkamwar, ..., and Dr.Devashri Kodgire. International Journal for Research in Applied Science and Engineering Technology, 2023. 0
citations.
0% Topic Match
Abstract: Abstract: This lab automation project aims to revolutionize scientific workflows by implementing a comprehensive system that integrates cutting-edge
technologies to streamline processes and enhance accuracy in laboratory settings. Leveraging robotics, sensor networks, and advanced software, our solution
automates repetitive tasks, minimizes human error, and accelerates experimentation cycles. The system's modular design allows seamless integration into existing
laboratory infrastructure, ensuring adaptability across diverse research domains. Through real-time data monitoring and analysis, our automation solution not only
increases efficiency but also facilitates data-driven decision-making. This project represents a significant step towards the future of laboratory operations, fostering
scientific advancements by optimizing resource...

[59] Laboratory as a Service (LaaS): a Novel Paradigm for Developing and Implementing Modular Remote Laboratories

M. Tawfik, ..., and M. Castro. Int. J. Online Eng., 2014. 52 citations.
0% Topic Match
Abstract: The increasing adoption of remote laboratories in education along with the shift from eLearning 2.0 towards eLearning 3.0, have demanded several
considerations in their implementation and delivery format. In response to these needs, this contribution introduces a novel model, Laboratory as a Service (LaaS),
for developing remote laboratories as independent component modules and implementing them as a set of loosely-coupled services to be consumed with a high
level of abstraction and virtualization. LaaS aims to tackle the common concurrent challenges in remote laboratories developing and implementation such as
inter-institutional sharing, interoperability with other heterogeneous systems, coupling with heterogeneous services and...

[60] Implement of Data Communication in Smart Factory with OPC-UA Architecture

Yang You, ..., and Ke Li. 2023 5th International Conference on Electronics and Communication, Network and Computer Technology (ECNCT),
2023. 0 citations.
0% Topic Match
Abstract: In response to the increasing demand for information collection and data communication in automated control devices in an intelligent manufacturing
factory, this paper proposes an OPC UA-based intelligent communication method for factory automation and discusses its communication principles and network
architecture in detail. This paper also explores the integration of OPC UA with devices such as industrial robot ROS systems and sensor-embedded systems and
introduces a Python-based data communication program design method. Ultimately, this paper successfully develops an MES robot monitoring module based on
the OPC UA architecture and conducts a case study. The practical application results show that OPC...

[61] Modular Web-Based Interactive Hybrid Laboratory Framework for Research and Education

Zhongcheng Lei, ..., and Jingang Lai. IEEE Access, 2018. 35 citations.
0% Topic Match
Abstract: Online laboratories are offering new experimental potential for research and education purposes. This paper investigates the design and implementation of
a web-based hybrid laboratory framework for research and education. Based on the previous work of the Networked Control System Laboratory (NCSLab), a hybrid
laboratory with a highly modular design providing plug-in free online experiments is discussed. The proposed modular design of the NCSLab is provided in four
aspects as hardware, software, control algorithms, and deployment, which covers all of the phases that compose an online experimental platform. The experiments
that are integrated into the NCSLab for research and education are...

[62] Lowering the Entrance Hurdle for Lab Automation: An Artificial Intelligence(cid:16)Supported, Interactive Robotic Arm for Automated, Repeated Testing
Procedures

Stefan Conrad, ..., and T. Speck. Advanced Intelligent Systems, 2025. 2 citations.
0% Topic Match
Abstract: Laboratory automation is crucial for improving efficiency and enhancing reproducibility in scientific workflows. However, industrial solutions mostly do not fit
the needs of scientific institutions, such as cost efficiency, customizability, and flexibility in fast iteration cycles. This study presents a laboratory automation system
that integrates affordable robotics and artificial intelligence (AI)(cid:16)driven functionalities in a modular architecture to address key challenges in research environments.
The system uses a robotic arm and a large language model (LLM) as a lab assistant, enabling natural language interaction and task orchestration. In contrast to
fully autonomous systems, this approach emphasizes a collaborative human(cid:16)in(cid:16)the(cid:16)loop model, ensuring...

[63] ROS-LLM: A ROS framework for embodied AI with task feedback and structured reasoning

Christopher E. Mower, ..., and Haitham Bou-Ammar. ArXiv, 2024. 27 citations.
0% Topic Match
Abstract: We present a framework for intuitive robot programming by non-experts, leveraging natural language prompts and contextual information from the Robot
Operating System (ROS). Our system integrates large language models (LLMs), enabling non-experts to articulate task requirements to the system through a chat
interface. Key features of the framework include: integration of ROS with an AI agent connected to a plethora of open-source and commercial LLMs, automatic
extraction of a behavior from the LLM output and execution of ROS actions/services, support for three behavior modes (sequence, behavior tree, state machine),
imitation learning for adding new robot actions to the library of...

[64] An Approach to Bridge ROS 1 and ROS 2 Devices into an OPC UA-based Testbed for Industry 4.0

Quang-Duy Nguyen, ..., and P. Bellot. 2022 IEEE 1st Industrial Electronics Society Annual On-Line Conference (ONCON), 2022. 3 citations.
0% Topic Match

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 31/43

Undermind

REPORT CREATED ON
1/12/2026

Abstract: ROS 1 and ROS 2 are two widely-used robotic middleware. One of their essential features is to enable two robots with the same middleware, ROS 1 or
ROS 2, to connect directly and collaborate. However, two robots running two different middleware can only communicate by additionally using one of the bridge
solutions available in the robotic community. It is even more challenging when deploying these robots as part of an OPC UA - based industrial testbed. The first
challenge is to network the robots with other OPC UA devices. Second, a testbed environment sometimes requires a robot to join the...

[65] A Modular Robotic Platform for Biological Research: Cell Culture Automation and Remote Experimentation

Jungmin Hamm, ..., and Kwanwoo Shin. Advanced Intelligent Systems, 2024. 15 citations.
0% Topic Match
Abstract: Robotic arms are now commonplace in diverse settings and are poised to play a crucial role in automating laboratory tasks. However, biological experiments
remain challenging for automation due to their dependence on human factors, such as researchers’ skills and experience. This article introduces robotic automation
and remote control for both general and biological research tasks through a modularized platform comprising a robotic arm, auxiliary tools, and software. This
platform facilitates fully automated or remote execution of key experiments in chemistry and biology, including liquid handling, mixing, cell seeding, culturing, and
genetic manipulation. The robot interfaces seamlessly with standard laboratory equipment...

[66] Survey of Remote Laboratories Using Service Oriented Architectures

D. Ponta, ..., and Paolo Buschiazzo. Int. J. Online Eng., 2009. 9 citations.
0% Topic Match
Abstract: Remote access to real laboratories can enhance traditional educational paths with practical experiences. However, most of the existing remote laboratories
cannot communicate with each other and they are not yet completely integrated with common educational platforms such as Learning Management Systems. These
problems could be tackled by offering to end users remote experiments as distributed services using web service technology. The paper examines the architectures
of remote laboratories developed by three institutions: DIBE ISILab (Internet Shared Instrumentation Laboratory), HPI DCL (Distributed Control Laboratory) and
MIT iLab. Their front-end services are compared and discussed. The paper details how end-user applications interact...

[67] Integration of Sensors, Controllers and Instruments Using a Novel OPC Architecture
Isaías González, ..., and J. Márquez. Sensors (Basel, Switzerland), 2017. 40 citations.
0% Topic Match
Abstract: The interconnection between sensors, controllers and instruments through a communication network plays a vital role in the performance and effectiveness
of a control system. Since its inception in the 90s, the Object Linking and Embedding for Process Control (OPC) protocol has provided open connectivity for monitoring
and automation systems. It has been widely used in several environments such as industrial facilities, building and energy automation, engineering education and
many others. This paper presents a novel OPC-based architecture to implement automation systems devoted to R&D and educational activities. The proposal is a
novel conceptual framework, structured into four functional layers where...

[68] Research and deployment of a Python-based software framework for large-scale physical experiment control

Shouteng Xia, ..., and Jie Yang. Journal of Instrumentation, 2023. 0 citations.
0% Topic Match
Abstract: This paper presents a python-based, open-source framework for slow control systems used in particle physics experiments. The framework includes
several functions such as display, data query, alarm, log and remote monitoring, etc. The data communication utilizes the MQTT (Message Queuing Telemetry
Transport) protocol, ensuring real-time and reliable data transmission. The object-oriented programming approach ensures each functional module's independence
and reusability, making them easily interchangeable and extendable through configuration files in various applications. Finally, two case deployment applications of
the framework are provided, where both of them are tested with Docker.

[69] A Configurable Skill Oriented Architecture Based on OPC UA

Jorge Blesa Gracia, ..., and Wilfried Wöber. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2022. 1 citations.
0% Topic Match
Abstract: Over the last years, research done in automation and industrial robotics has established the foundations for skill-oriented systems based on the OPC UA
standard. Nevertheless, utilizing these advances in other areas of robotics research can be challenging and time consuming. We present a framework aiming to
reduce this entry threshold. Our solution is an open source, easy to configure tool based on OPC UA, that provides with a hardware agnostic, skill-oriented, event
driven interface to systems. The framework allows integrating external hardware and software by means of plugins. It also provides a mechanism for endowing skills
with hardware agnostic motion...

[70] Achieving Reproducibility and Closed-Loop Automation in Biological Experimentation with an IoT-Enabled Lab of the Future

Ben Miles and Peter L Lee. SLAS Technology, 2018. 38 citations.
0% Topic Match
Abstract: A robotic cloud laboratory driven by a state-of-the-art unified laboratory operating system integrates automated hardware, humans, and sensors. This lab
of the future system enables researchers to transparently and collaboratively create, optimize, and organize biological experiments to achieve more reproducible
results, perform around-the-clock experimentation, and more efficiently navigate the vast parameter space of biology.

[71] A mobile robot bridging manual and automated bioscientific workflows by applying the Swiss army knife principle

Nicole Rupp, ..., and Thole Zuchner. Scientific Reports, 2025. 0 citations.
0% Topic Match
Abstract: The complexity and diversity of bioscientific research laboratories, creates significant challenges for automation. Their varying workflows, personnel, and
instruments, often hinder smaller research laboratories to benefit from automated processes, as existing systems seem unsuitable due to low flexibility. Therefore,
we developed a versatile robotic system designed to automate a broad range of bioscience laboratory processes. Central to our system and novel, compared to all
other kinds of laboratory automation concepts, is a multifunctional end effector, inspired by the Swiss-army-knife, capable of executing multiple tasks, including an
operating finger, a camera system, a gripper, and a pipette. This end effector is...

[72] Unlocking the potential of Robot Manipulators: Seamless Integration Framework

Mikel Bueno, ..., and Phil Webb. 2024 IEEE 20th International Conference on Automation Science and Engineering (CASE), 2024. 1 citations.
0% Topic Match
Abstract: This study introduces a groundbreaking framework designed to enhance the adaptability and efficiency of robot manipulators in manufacturing, leveraging
ROS 2 and a modular middleware to transcend traditional robotic constraints. The framework's efficacy is exemplified through a pick-and-place task, serving
not merely as a demonstration but as robust evidence of the framework's ability to enable complex object manipulation tasks far beyond repetitive activities. By
integrating advanced perception capabilities with a YOLOv8-based object detection model and an OpenCV-based pose estimation module, the framework showcases
a seamless interaction between sophisticated software tools and robotic hardware. This integration not only simplifies the incorporation...

[73] Interoperability of Remote Laboratories Systems

H. Yeung, ..., and S. Murray. Int. J. Online Eng., 2010. 23 citations.
0% Topic Match
Abstract: There has been growing interest in, and development of, remotely accessible laboratories as a mechanism for improving access and flexibility, and enabling
sharing of facilities. Differences in focus, philosophy, approach or domain have led to quite different technical solutions in supporting remote laboratories. Whilst
this diversity represents a significant strength in terms of the ability to explore different issues and support diverse applications, it does however potentially hamper
the sharing of labs between different institutions. Investigation into interoperability between two remote lab platforms has realized a need for a common application
protocol to achieve the goals remote labs aims to...

[74] An Implementation of Microservices Based Architecture for Remote Laboratories

Mohammed Moussa, ..., and Abderrahmane Boumehdi. Unknown journal, 2020. 5 citations.
0% Topic Match
No summary or abstract available

[75] Sequence Planner: A Framework for Control of Intelligent Automation Systems

M. Dahl, ..., and P. Falkman. Applied Sciences, 2022. 6 citations.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 32/43

Undermind

REPORT CREATED ON
1/12/2026

0% Topic Match
Abstract: This paper presents a framework that tackles the challenges met in the development of automation systems featuring collaborative robotics and other
machines that have some degree of autonomy. These machines rely on online algorithms for both sensing and acting in order to achieve a very high level of flexibility.
To take advantage of these new machines and algorithms, control systems must also be increasingly flexible. In this paper, we present a framework for control of
this new class of intelligent automation systems called Sequence Planner (SP), which helps with control of both traditional automation equipment and machines
with autonomy. To...

[76] Lab-as-a-Service (LaaS): A Middleware Approach for Internet-Accessible Laboratories
Eyhab Al-Masri. 2018 IEEE Frontiers in Education Conference (FIE), 2018. 6 citations.
0% Topic Match
Abstract: [Work in Progress] The proliferation of cloud computing and web-based technologies have made it possible for universities to expand their academic
networks reaching a wider range of students. In an effort to expand offered services while reducing costs, universities began exploring the use of distributed
software platforms and middleware infrastructures to make laboratories accessible over the Internet. However, there are major challenges in the way these platforms
enable students to effectively interact with a remote laboratory environment. In this paper, we introduce a remotely-controlled middleware infrastructure called
Lab-as-a-Service (LaaS) that is based on cloud computing and service-oriented architecture (SOA) concepts....

[77] TALOS (Total Automation of LabVIEW Operations for Science): A framework for autonomous control systems for complex experiments

M. Volponi, ..., and N. Zurlo. Review of Scientific Instruments, 2024. 4 citations.
0% Topic Match
Abstract: Modern physics experiments are frequently very complex, relying on multiple simultaneous events to happen in order to obtain the desired result. The
experiment control system plays a central role in orchestrating the measurement setup: However, its development is often treated as secondary with respect to the
hardware, its importance becoming evident only during the operational phase. Therefore, the AEg(cid:4)IS (Antimatter Experiment: Gravity, Interferometry, Spectroscopy)
collaboration has created a framework for easily coding control systems, specifically targeting atomic, quantum, and antimatter experiments. This framework, called
Total Automation of LabVIEW Operations for Science (TALOS), unifies all the machines of the experiment in...

[78] RESTlabs: A prototype web 2.0 architecture for Remote Labs

J. Zornig, ..., and H. Dinh. 2012 9th International Conference on Remote Engineering and Virtual Instrumentation (REV), 2012. 6 citations.
0% Topic Match
No summary or abstract available

[79] Design and implementation of a Framework for remote experiments in education

Pavel Kuriscák, ..., and J. N. Silva. 2022 8th International Engineering, Sciences and Technology Conference (IESTEC), 2022. 6 citations.
0% Topic Match
Abstract: Remote Controlled laboratories are a teaching and learning tool that increasingly becomes fundamental in the teaching and learning processes at all levels.
A study of available systems highlights a series of limitations on the used programming languages, overall architecture, and network communication patterns that
hinder these systems to be further adopted. Current technologies and modern WEB architectures allow the resolution of such limitations. Here we present the FREE
(Framework for Remote Experiments in Education) platform, a novel system, that, using modern technologies, architectures, and programming practices, will be
easier to integrate with external tools and services and new experiments. FREE...

[80] Towards Increased Flexibility and Interoperability in Distributed Process Control Applications

Ahsan Zia and David Hästbacka. 2020 IEEE Conference on Industrial Cyberphysical Systems (ICPS), 2020. 1 citations.
0% Topic Match
Abstract: The modern process automation plants are changing into flexible designs, which raises the requirements for distributively controlled logic, a high degree
of interoperability, dynamic reconfiguration and software reusability. Thus, creating an opportunity to integrate the distributed control system standards and platform
independent communication protocols. In this paper, we propose the use of OPC UA to increase interoperability of communication and the utilization of Arrowhead
Framework to enhance interoperable service compositions of control applications implemented in IEC 61499. The concept is outlined for the integration and modeling
of a distributed control system for a FESTO laboratory batch process system. A control...

[81] Smart device paradigm, Standardization for online labs

C. Salzmann and D. Gillet. 2013 IEEE Global Engineering Education Conference (EDUCON), 2013. 34 citations.
0% Topic Match
No summary or abstract available

[82] The smartLab: Experimental and environmental control and monitoring of the chemistry laboratory

Stephen Wilson and J. Frey. 2009 International Symposium on Collaborative Technologies and Systems, 2009. 7 citations.
0% Topic Match
No summary or abstract available

[83] fROS: A Generic Fieldbus Framework for ROS

Daniel Schneider, ..., and Daniel Watzenig. IEEE Transactions on Intelligent Vehicles, 2024. 4 citations.
0% Topic Match
Abstract: As the development of advanced driver assistance systems (ADAS) continues, more and more software functions and sensors are being introduced to the
market. This is accompanied by an increase in the amount of data that has to be transmitted to multiple receivers in the vehicle under hard real-time requirements.
The use of deterministic and non-deterministic Fieldbus protocols enables communication between sensor and actuator or ECUs. For the purpose of verifying and
validating the developed software modules, but also for type approval, an objective and thus data-driven toolchain is mandatory. By using suitable middleware such
as Robotic Operating System (ROS), the...

[84] An Open-Source Framework for Automated High-Throughput Cell Biology Experiments

Pavel Katunin, ..., and A. Nikolaev. Frontiers in Cell and Developmental Biology, 2021. 3 citations.
0% Topic Match
Abstract: Modern data analysis methods, such as optimization algorithms or deep learning have been successfully applied to a number of biotechnological and
medical questions. For these methods to be efficient, a large number of high-quality and reproducible experiments needs to be conducted, requiring a high degree
of automation. Here, we present an open-source hardware and low-cost framework that allows for automatic high-throughput generation of large amounts of cell
biology data. Our design consists of an epifluorescent microscope with automated XY stage for moving a multiwell plate containing cells and a perfusion manifold
allowing programmed application of up to eight different solutions....

[85] A ROS2-Based Framework for Industrial Automation Systems

Jiazhen He, ..., and Xin Fu. 2022 2nd International Conference on Computer, Control and Robotics (ICCCR), 2022. 15 citations.
0% Topic Match
Abstract: With the development of industrial manufacturing towards flexibility and efficiency, the automation equipment, including manipulator, automated guide
vehicle (AGV), Computer numerical control machine tools (CNC) and other intelligent individuals, has become an indispensable part of industrial system. In order
to build a reliable and robust automation system rapidly, a reasonable software framework for controlling the automation equipment is necessary. To address this
problem, this paper proposes a framework for construction of an industrial automation system. The system consists of 2 parts, which are motion control system
(MCS) and OpenPLC. The MCS is based on ROS2, which provides real-time communication middleware....

[86] Autonomous Integration of Bench-Top Wet Lab Equipment

Zachary Logan, ..., and Mohammad Goli. 2025 22nd International Conference on Ubiquitous Robots (UR), 2024. 0 citations.
0% Topic Match
Abstract: Laboratory automation is an expensive and complicated endeavor with limited inflexible options for smallscale labs. We developed a prototype system for
tending to a bench-top centrifuge using computer vision methods for color detection and circular Hough Transforms to detect and localize centrifuge buckets. Initial

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 33/43

Undermind

REPORT CREATED ON
1/12/2026

results showed that the prototype is capable of automating the usage of regular bench-top lab equipment. Experimental results showed the computer vision system
to have successful detection rate of 98%, a 70% success rate for removing test tubes from a centrifuge and a 95% success rate for inserting them.

[87] Requirements and Challenges in the Configuration of a Real-Time Node for OPC UA Publish-Subscribe Communication

Rebekka Neumann, ..., and A. Verl. 2023 29th International Conference on Mechatronics and Machine Vision in Practice (M2VIP), 2023. 1
citations.
0% Topic Match
Abstract: Factory automation is evolving from a hierarchical structure towards an interconnected architecture in which systems at different levels can communicate
seamlessly with each other. This requires an appropriate replacement of proprietary fieldbus systems in the automation sector. A promising solution to implement
cross-plane end-to-end real-time capable communication between computing nodes is proposed in literature. The usage of Open Platform Communication Unified
Architecture (OPC UA) as the information model with the Publish-Subscribe (PubSub) communication mechanism in combination with Time Sensitive Networking
(TSN) is presented to fulfill the requirements for message transmission. In contrast to the state of the art of configuring...

[88] Engineering biology and automation–Replicability as a design principle

Matthieu Bultelle, ..., and Richard Kitney. Engineering Biology, 2024. 4 citations.
0% Topic Match
Abstract: Abstract Applications in engineering biology increasingly share the need to run operations on very large numbers of biological samples. This is a direct
consequence of the application of good engineering practices, the limited predictive power of current computational models and the desire to investigate very large
design spaces in order to solve the hard, important problems the discipline promises to solve. Automation has been proposed as a key component for running large
numbers of operations on biological samples. This is because it is strongly associated with higher throughput, and with higher replicability (thanks to the reduction
of human input). The...

[89] Laboratory Automation and Middleware.

M. Riben. Surgical pathology clinics, 2015. 16 citations.
0% Topic Match
No summary or abstract available

[90] Towards Robot Software Abstraction: ROS 2-Based Framework for Object Handling within a Robot Cell

Mikel Bueno Viso, ..., and Phil Webb. 2024 IEEE 22nd International Conference on Industrial Informatics (INDIN), 2024. 0 citations.
0% Topic Match
Abstract: Recent advancements in industrial automation have led to the development of increasingly adaptable and reconfigurable systems, driven by the necessity
for flexibility and efficiency in manufacturing. This paper introduces a ROS 2-based software framework tailored for object handling within a robot cell, addressing
challenges pertaining to reconfigurability, modularity, and interoperability. The proposed solution simplifies the deployment process of robotic applications and
provides a standardized ROS 2-based platform, making it particularly beneficial for small and medium automation enterprises that require frequent reprogramming
and adaptation of robot cells to different settings. By ensuring software and hardware agnosticism, the framework presents a comprehensive...

[91] Chemistry Lab Automation via Constrained Task and Motion Planning

N. Yoshikawa, ..., and Florian Shkurti. ArXiv, 2022. 11 citations.
0% Topic Match
Abstract: Chemists need to perform many laborious and time-consuming experiments in the lab to discover and understand the properties of new materials. To
support and accelerate this process, we propose a robot framework for manipulation that autonomously performs chemistry experiments. Our framework receives
high-level abstract descriptions of chemistry experiments, perceives the lab workspace, and autonomously plans multi-step actions and motions. The robot interacts
with a wide range of lab equipment and executes the generated plans. A key component of our method is constrained task and motion planning using PDDLStream
solvers. Preventing collisions and spillage is done by introducing a constrained motion...

[92] An Accessible Python Framework for Real-Time Magnetic Tweezers Microscope Control and Image Processing

James A. London, ..., and Richard Fishel. bioRxiv, 2025. 0 citations.
0% Topic Match
Abstract: Magnetic tweezers are a popular biophysical instrument for manipulating and measuring single molecules. Most groups rely on custom-built setups tailored
to specific experiments, making it challenging to implement and share software. Typically, image acquisition and hardware control are automated via LabVIEW,
while real-time video processing is implemented in C++/CUDA libraries. Live processing can eliminate the need to store raw video, enabling high throughput,
fast acquisition rates, and simplified experimental workflows. However, no open-source general-purpose software framework currently unifies these capabilities for
magnetic tweezers experiments. Here, we introduce MagTrack and MagScope open-source Python-based tools designed to fill this gap. MagTrack is...

[93] From Platform to Knowledge Graph: Evolution of Laboratory Automation

Jiaru Bai, ..., and Markus Kraft. JACS Au, 2022. 70 citations.
0% Topic Match
Abstract: High-fidelity computer-aided experimentation is becoming more accessible with the development of computing power and artificial intelligence tools. The
advancement of experimental hardware also empowers researchers to reach a level of accuracy that was not possible in the past. Marching toward the next
generation of self-driving laboratories, the orchestration of both resources lies at the focal point of autonomous discovery in chemical science. To achieve such a
goal, algorithmically accessible data representations and standardized communication protocols are indispensable. In this perspective, we recategorize the recently
introduced approach based on Materials Acceleration Platforms into five functional components and discuss recent case studies...

[94] A Plugin-Based Software Framework for Data Acquisition and Online Processing

Shaoshuai Fan, ..., and Hangchang Zhang. IEEE Transactions on Nuclear Science, 2025. 0 citations.
0% Topic Match
Abstract: In order to address the diverse requirements for data acquisition (DAQ) and online data processing in small-scale high-energy experiments, such as
detector research and preliminary research experiments, this article proposes a highly scalable software framework based on a plugin-based design concept. In
the design, the data processing flow is broken down into basic data processing units. A plugin manager has been implemented based on the design pattern of
dependency injection, allowing the framework to achieve management of plugins. Users are then able to freely assemble these units into customized data processing
flow by configuration files. The framework permits the development...

[95] Middleware Interoperability for Robotics: A ROS–YARP Framework

Miguel Aragão, ..., and Alexandre Bernardino. Frontiers Robotics AI, 2016. 11 citations.
0% Topic Match
Abstract: Middlewares are fundamental tools for progress in research and applications in robotics. They enable the integration of multiple heterogeneous sensing
and actuation devices, as well as providing general purpose modules for key robotics functions (kinematics, navigation, planning). However, no existing middleware
yet provides a complete set of functionalities for all robotics applications, and many robots may need to rely on more than one framework. This paper focuses on
the interoperability between two of the most prevalent middleware in robotics: YARP and ROS. Interoperability between middlewares should ideally allow users to
execute existing software without the necessity of: (i) changing the...

[96] Improving Data Acquisition For a Quartz Crystal Microbalance Electrochemical Sensor

Darine Hadj Bechir, ..., and Hubert Perrot. 2025 IEEE 22nd International Multi-Conference on Systems, Signals & Devices (SSD), 2025. 0
citations.
0% Topic Match
Abstract: This article explores the development of a scalable, contemporary interface designed to replace outdated laboratory control systems. Utilizing Python open
source codes like PyVISA, PyQt, and the Prologix GPIB-USB controller, this solution automates the measurement of essential parameters, including frequency and
voltage. It meets the requirements of contemporary electrochemical studies with its real-time data acquisition, enhance precision and user-friendly interface. The
new developed interface is a flexible to promote scientific investigation since it guarantees dependently, flexibility and enhanced performance.

[97] Integrating PLCs and Robots into the ROS 2 Ecosystem

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 34/43

Undermind

REPORT CREATED ON
1/12/2026

Moritz Chemnitz, ..., and Artur Fritz. 2024 IEEE 29th International Conference on Emerging Technologies and Factory Automation (ETFA), 2024.
0 citations.
0% Topic Match
Abstract: To stimulate the connection between robotics and industrial control systems, this work presents a solution for integrating Programmable Logic Controllers
(PLCs) into the Robot Operating System 2 (ROS 2), based on the IEC 61499 standard. For this purpose, we have developed a framework that automatically
generates all code for the PLC and ROS 2. Limitations regarding usable data types are discussed, and we demonstrate the functionality by interconnecting a robot
and a PLC.

[98] TARMAC: A Taxonomy for Robot Manipulation in Chemistry
Kefeng Huang, ..., and Jihong Zhu. ArXiv, 2025. 0 citations.
0% Topic Match
Abstract: Chemistry laboratory automation aims to increase throughput, reproducibility, and safety, yet many existing systems still depend on frequent human
intervention. Advances in robotics have reduced this dependency, but without a structured representation of the required skills, autonomy remains limited to
bespoke, task-specific solutions with little capacity to transfer beyond their initial design. Current experiment abstractions typically describe protocol-level steps
without specifying the robotic actions needed to execute them. This highlights the lack of a systematic account of the manipulation skills required for robots in
chemistry laboratories. To address this gap, we introduce TARMAC - a Taxonomy for Robot Manipulation in...

[99] Laboratory Information Management Systems - An Approach as an Integration Platform within Flexible Laboratory Automation for Application
in Life Sciences

Bernd Göde, ..., and Norbert Stoll. 2007 IEEE International Conference on Automation Science and Engineering, 2007. 15 citations.
0% Topic Match
No summary or abstract available

[100] An Open-Source Multi-Robot Framework System for Collaborative Environments Based on ROS2

Francisco Yumbla, ..., and Hyungpil Moon. IEEE Access, 2025. 3 citations.
0% Topic Match
Abstract: Despite the rise of robotics and automation in industrial applications, the widespread adoption of collaborative robotics still needs to be improved due to the
lack of interoperability between robots and the low adaptability of existing systems. Solving this problem would mean a significant advance in robotics and industrial
automation. Under this context, an open-source MultiRobot Framework based on ROS2 was developed in the present research to effectively communicate and
coordinate robotics agents and sensors in closed collaborative environments. A simulation-based control and software design was performed using the GAZEBO
tool. A centralized architecture was obtained with an autonomous navigation module...

[101] Protocol Performance in Robotics: Analyzing ADS vs. UDP Protocols for ROS2 and TwinCAT Integration

Brenno Domingues, ..., and L. G. Trabasso. 2025 Brazilian Conference on Robotics (CROS), 2025. 0 citations.
0% Topic Match
Abstract: The adoption of robots for everyday tasks has surged, fueled by technological advancements. Contemporary robotic designs focus on expanding operational
workspaces, enhancing flexibility, and overcoming challenges such as singularities. Successful task execution depends on the effective integration of robust hardware
and software. Key hardware considerations include the design of links for reach and the connection of joints to motors, drivers, and sensors. The software serves
as an interface for controlling these components and must accurately reflect the robot’s kinematics. Effective communication between hardware and software is
essential for optimal operation. While commercial software often conflicts with unconventional robotic designs, open-source...

[102] OpenLH: Open Liquid-Handling System for Creative Experimentation with Biology

Gilad Gome, ..., and Oren Zuckerman. Proceedings of the Thirteenth International Conference on Tangible, Embedded, and Embodied
Interaction, 2019. 53 citations.
0% Topic Match
Abstract: The biological prototyping revolution is in motion, and new tools are needed to empower HCI researchers, designers, makers, and bio-enthusiasts to
experiment with live organisms. We present OpenLH, a liquid handling system that empowers users to conduct accurate and repetitive experiments with live biology
in a sterile, open, and affordable way. OpenLH integrates a commercially available robotic arm with custom 3D printed parts, a modified pipette, and a visual
block-based programming interface. The system is as accurate as commercial liquid handlers, capable of repetitive tasks in micro-scale accuracy, easy to operate,
and supports multi-materials including biomaterials, microorganisms and cell cultures....

[103] An Automated Lab(cid:16)On(cid:16)A(cid:16)Chip Approach for Pollen Tube Growth Manipulation in a Controlled Chemical Environment

Jiawei Zhu, ..., and Bradley J. Nelson. Advanced Science, 2025. 0 citations.
0% Topic Match
Abstract: Laboratory automation is successfully implemented across a wide range of applications, from space exploration to oceanic research, facilitating data
collection and analysis while improving precision in biological and medical fields. The future of robotic laboratory automation is closely tied to advancements in
miniaturization. Thus, automation of lab(cid:16)on(cid:16)a(cid:16)chip (LoC) systems–integrating complex laboratory tasks onto a small chip–holds great potential for scientific research,
including the study of model organisms and cells. Here, an automated continuous(cid:16)flow(cid:16)based LoC device designed to investigate and manipulate the growth of pollen
tubes (PTs)–fastest(cid:16)growing cells in nature–within controlled chemical environments is presented. The automated LoC approach allows for...

[104] Flexible software architecture for user-interface and machine control in laboratory automation.

E. B. Arutunian, ..., and S. Moody. BioTechniques, 1998. 17 citations.
0% Topic Match
Abstract: We describe a modular, layered software architecture for automated laboratory instruments. The design consists of a sophisticated user interface, a machine
controller and multiple individual hardware subsystems, each interacting through a client-server architecture built entirely on top of open Internet standards. In our
implementation, the user-interface components are built as Java applets that are downloaded from a server integrated into the machine controller. The user-interface
client can thereby provide laboratory personnel with a familiar environment for experiment design through a standard World Wide Web browser. Data management
and security are seamlessly integrated at the machine-controller layer using QNX, a real-time...

[105] Towards OPC UA over Shared Memory as an Open Intra-Host Middleware for Automation Software

Thomas Barth, ..., and Martin Ruskowski. 2025 IEEE 30th International Conference on Emerging Technologies and Factory Automation (ETFA),
2025. 0 citations.
0% Topic Match
Abstract: The increasing virtualization of automation software and its decoupling from hardware introduces a significant change in industrial automation. This
transition allows classical operational technology software instances, such as programmable logic controllers, to coexist on the same host system alongside
applications from various domains. Such coexistence offers substantial potential for a more efficient interconnection between applications from different areas,
overcoming typical limitations associated with conventional interfaces. However, current middleware solutions for automation applications are often proprietary and
not standardized. In this paper, we present an initial concept for an intra-host middleware based on the OPC Unified Architecture, employing a centralized data...

[106] Integrating a Pipette Into a Robot Manipulator With Uncalibrated Vision and TCP for Liquid Handling

Junbo Zhang, ..., and Kensuke Harada. IEEE Transactions on Automation Science and Engineering, 2024. 10 citations.
0% Topic Match
Abstract: This paper presents a system integration approach for a 6-DoF (Degree of Freedom) collaborative robot to operate a pipette for liquid dispensing. Its
technical development is three-fold. First, we designed an end-effector for holding and triggering manual pipettes. Second, we took advantage of direct teaching to
specify global labware poses and planned robotic motion based on them. Third, we leveraged hand-mounted cameras and visual classifiers to predict and correct
positioning errors, which allowed precisely attaching pipettes and tips without calibration. Through experiments and analysis, we confirmed that the developed
system, especially the planning and visual recognition methods, could help secure...

[107] A Solution to the Generalized ROS Hardware IO Problem - A Generic Modbus/TCP Device Driver for PLCs, Sensors and Actuators

Arne Wendt and Thorsten Schüppstuhl. 2021 26th IEEE International Conference on Emerging Technologies and Factory Automation (ETFA ),
2021. 2 citations.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 35/43

Undermind

REPORT CREATED ON
1/12/2026

0% Topic Match
Abstract: The Robot Operating System (ROS) provides a software framework, and ecosystem of knowledge and community supplied resources to rapidly develop and
prototype intelligent robotics applications. By standardizing communication, configuration and invocation of software modules, ROS facilitates reuse of device-driver
and algorithm implementations. Using existing implementations of functionality allows users to assemble their robotics application from tested and known-good
capabilities. Despite the efforts of the ROS-Industrial consortium and projects like ROSIN to bring ROS to industrial applications and integrate industrial hardware,
we observe a lack of options to generically integrate basic physical IO. In this work we lay out and provide...

[108] A toolkit for remote laboratory design & development

E. Lindsay, ..., and B. Stumpers. 2011 First Global Online Laboratory Consortium Remote Laboratories Workshop, 2011. 29 citations.
0% Topic Match
Abstract: Remote laboratories are an increasingly prevalent instructional tool for undergraduate engineering laboratory classes. This increased prevalence brings
with it a need to change the model of how remote laboratories are developed. The earlier remote laboratories were developed by individual academics combining
their discipline-specific skills with their own ability to implement remote operation. This “cottage industry” model allows for significant local innovation; however it
does not support widespread or sustainable implementation of remote laboratories. In order to make remote laboratories a mainstream technology, it is essential
that potential academic users are well informed and well supported in considering remote laboratories. There...

[109] Software Framework for Controlling Unsupervised Scientific Instruments

Benjamin Schmid, ..., and J. Huisken. PLoS ONE, 2016. 1 citations.
0% Topic Match
Abstract: Science outreach and communication are gaining more and more importance for conveying the meaning of today’s research to the general public. Public
exhibitions of scientific instruments can provide hands-on experience with technical advances and their applications in the life sciences. The software of such
devices, however, is oftentimes not appropriate for this purpose. In this study, we describe a software framework and the necessary computer configuration that
is well suited for exposing a complex self-built and software-controlled instrument such as a microscope to laymen under limited supervision, e.g. in museums or
schools. We identify several aspects that must be met...

[110] Do it yourself (DIY) liquid handling robot for evolutionary search exploration

A. Müller, ..., and S. Rasmussen. Unknown journal, 2015. 2 citations.
0% Topic Match
Abstract: Open source hardware has made it significantly easier to build custom scientific instrumentation, in particular in the recent wake of open-source 3D printing
technology (Jones et al., 2011). The main advantages of DIY scientific instruments include (i) significantly lower instrumentation costs, (ii) possibility for open-ended
special purpose functions to address research-specific problems, (iii) deeper understanding of the scientific problem under investigation as the instrumentation is
designed simultaneously, as well as (iv) providing an excellent student learning tool. We present the ChemBot: a programmable liquid handling robot, which is able
to realize a series of desired functions and processes. The goal...

[111] AUTOSAR AP and ROS 2 Collaboration Framework

Ryudai Iwakami, ..., and Takuya Azumi. 2024 27th Euromicro Conference on Digital System Design (DSD), 2024. 1 citations.
0% Topic Match
Abstract: The field of autonomous vehicle research is advancing rapidly, necessitating platforms that meet real-time performance, safety, and security requirements
for practical deployment. AUTOSAR Adaptive Platform (AUTOSAR AP) is widely adopted in development to meet these criteria; however, licensing constraints and
tool implementation challenges limit its use in research. Conversely, Robot Operating System 2 (ROS 2) is predominantly used in research within the autonomous
driving domain, leading to a disparity between research and development platforms that hinders swift commercialization. This paper proposes a collaboration
framework that enables AUTOSAR AP and ROS 2 to communicate with each other using a Data Distribution...

[112] Recent advancements in laboratory automation technology and their impact on scientific research and laboratory procedures
Abdullah Omar Mohammed Omair, ..., and Mustafa Othman Albulushi. International journal of health sciences, 2023. 3 citations.
0% Topic Match
Abstract: This article examines the latest developments in laboratory automation technologies and their influence on scientific research and laboratory protocols.
The research examines the incorporation of robotic sample handling systems, artificial intelligence and machine learning algorithms, sophisticated software and
hardware, and safety improvements in laboratory automation systems. The research emphasizes the advantages of laboratory automation technologies, such as
improved efficiency, repeatability, and safety in the laboratory setting. The study also examines the ramifications of automation technology on scientific research,
including the hastening of scientific advancements and the creation of innovative remedies and cures. Moreover, the study highlights the obstacles linked to...

[113] An Autonomous Intelligent Robot for Reagent Handling in Biological Laboratories

Huizhou Zhao, ..., and Xingguang Duan. 2025 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM), 2025. 0
citations.
0% Topic Match
Abstract: In recent years, the increasing prominence of biological research has highlighted safety risks and high-intensity workloads faced by laboratory operators.
To address these challenges, this study proposes an autonomous intelligent robot for reagent handling in biological laboratories. By combining an autonomous
mobile robot with a collaborative robotic arm, the system is designed to automate the complex tasks in biological laboratory environments. The system integrates
vision-based positioning, laser navigation algorithms, and a master-slave teleoperation control framework to enable automated execution of complex tasks such as
sample transfer, pipetting, and diverse non-standardized operations. A series of experiments validate the system’s functionality, demonstrating...

[114] Automatic Integration of Simulated Systems into OPC UA Networks

Jan Reitz and J. Roßmann. 2020 IEEE 16th International Conference on Automation Science and Engineering (CASE), 2020. 6 citations.
0% Topic Match
Abstract: This paper demonstrates the integration of OPC Unified Architecture (OPC UA) communication capabilities in a simulation framework.The proposed
approach is based on a data mapping from the simulation’s meta data model to the OPC UA information model and a concurrent architecture based on message
passing between the OPC UA server and the simulation software.The data mapping utilizes the simulation’s and OPC UA’s reflection mechanisms to automatically
generate OPC UA address spaces from simulation models. The inverse mapping is used to automatically generate simulation model structure from queries to an
existing OPC UA server. The concurrent architecture enables large numbers of...

[115] The modular design of an internet-based laboratory

A. Azad. Unknown journal, 2008. 0 citations.
0% Topic Match
No summary or abstract available

[116] #40;5==>5 C?@02;5=85 <8:@>A:>?><

Leica DM IRM =0 >A=>25 B5E=>;>388 8=B5@=5B0 25I59

and  . (cid:16). $8;8??>2

. Unknown journal, 2017. 0 citations.

(cid:16). !. !07>=>20, ...,
0% Topic Match
Abstract: The organization of any research activity involves obtaining and analyzing the results of ongoing research. This is a complex and time-consuming process,
requiring large human costs and unique expensive equipment. The problem of using such unique equipment can make research difficult or even impossible at all.
One of the ways to solve this problem can be the creation of remote access labs working in the collective mode. An important feature of remote access to equipment
is the possibility of obtaining primary information and the correct organization of its transmission between individual subsystems and consumers. Convenient and
mobile tools in such...

[117] Core Processes in Intelligent Robotic Lab Assistants: Flexible Liquid Handling

Dennis Knobbe, ..., and Sami Haddadin. 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2022. 17 citations.
0% Topic Match
Abstract: Laboratory automation is a suitable solution to establish higher reproducibility with less manual work and thus higher quality standards in life sciences. To
date, mobile robots are capable of performing autonomous pick-and-place tasks in the laboratory, and specialized pipetting machines can be used for sequenced
liquid handling. However, the complex and creative process of developing new research protocols requires flexible robotic systems that can perform tasks such as

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 36/43

Undermind

REPORT CREATED ON
1/12/2026

pipetting in more versatile ways. In addition, the correct technique, according to ISO standards, has a great influence on precision and accuracy and therefore on
reproducibility. This paper introduces our Intelligent Robotic...

[118] Potential of Embedded Processors and Cloud for Remote Experimentation

M. M. Uddin, ..., and A. Azad. Unknown journal, 2020. 2 citations.
0% Topic Match
No summary or abstract available

[119] The next wave of innovation in laboratory automation: systems for auto-verification, quality control and specimen quality assurance

A. Brown and T. Badrick. Clinical Chemistry and Laboratory Medicine (CCLM), 2022. 20 citations.
0% Topic Match
Abstract: Abstract Laboratory automation in clinical laboratories has made enormous differences in patient outcomes, with a wide range of tests now available that
are accurate and have a rapid turnaround. Total laboratory automation (TLA) has mechanised tube handling, sample preparation and storage in general chemistry,
immunoassay, haematology, and microbiology and removed most of the tedious tasks involved in those processes. However, there are still many tasks that must
be performed by humans who monitor the automation lines. We are seeing an increase in the complexity of the automated laboratory through further platform
consolidation and expansion of the reach of molecular genetics...

[120] ROS-like framework using modern development concepts and microservices

M. Ivanou, ..., and Alexander Maloletov. 2021 International Conference "Nonlinearity, Information and Robotics" (NIR), 2021. 6 citations.
0% Topic Match
Abstract: The Robot Operating System (ROS) has established itself as a useful set of software libraries and tools that can help to build robot applications. It provides
services such as hardware abstraction, low-level device management, implementation of frequently used functions, inter-process message passing, and package
management. ROS is good for small static research environments, however, it does not scale so well to large real-world applications. Besides, there is no security
model, the test approach is unclear, the library versions can be incompatible. The paper presents a survey, the results of which show that many ROS users have
problems with such modern...

[121] Experimental research control software system

I. A. Cohn, ..., and A. N. Vystavkin. Journal of Physics: Conference Series, 2014. 0 citations.
0% Topic Match
Abstract: A software system, intended for automation of a small scale research, has been developed. The software allows one to control equipment, acquire
and process data by means of simple scripts. The main purpose of that development is to increase experiment automation easiness, thus significantly reducing
experimental setup automation efforts. In particular, minimal programming skills are required and supervisors have no reviewing troubles. Interactions between
scripts and equipment are managed automatically, thus allowing to run multiple scripts simultaneously. Unlike well-known data acquisition commercial software
systems, the control is performed by an imperative scripting language. This approach eases complex control and data...

[122] Robotic microscopy for everyone: the OpenFlexure microscope

J. Collins, ..., and R. Bowman. Biomedical Optics Express, 2019. 119 citations.
0% Topic Match
Abstract: Optical microscopes are an essential tool for both the detection of disease in clinics, and for scientific analysis. However, in much of the world access
to high-performance microscopy is limited by both the upfront cost and maintenance cost of the equipment. Here we present an open-source, 3D-printed, and
fully-automated laboratory microscope, with motorised sample positioning and focus control. The microscope is highly customisable, with a number of options
readily available including trans- and epi-illumination, polarisation contrast imaging, and epi-florescence imaging. The OpenFlexure Microscope has been designed
to enable low-volume manufacturing and maintenance by local personnel, vastly increasing accessibility. We have...

[123] Behavioral Analysis of ROS motion planners integrated with Robotics Middleware Framework (RMF)

Mayank Deshpande and N. Kamalanathan. 2022 IEEE 4th International Conference on Cybernetics, Cognition and Machine Learning Applica-
tions (ICCCMLA), 2022. 1 citations.
0% Topic Match
Abstract: Robot operating system (ROS) is one of the most popular middleware for robot applications, being integrated with the majority of projects in robotics.
Since the rollout of ROS2 having an improved communication stack than ROS1 with its real-time data distribution service (DDS) protocol, the problem of robot
interoperability has been one of the most sought problems. Although many different multi-robot management frameworks have been developed, only a few of them
are open-sourced. In this paper, we present a study that evaluates one such interoperability framework called “Robotics Middleware Framework (RMF)”. Herein,
RMF is integrated with “Free Fleet” an open-source robot...

[124] Detecting Gripping Failure in a Liquid Handling Robot with a Break Beam Sensor

Ádám Wolf, ..., and K. Széll. 2020 IEEE 18th International Symposium on Intelligent Systems and Informatics (SISY), 2020. 1 citations.
0% Topic Match
Abstract: The importance of comprehensive automation in biotechnological and pharmaceutical laboratories is gaining more and more importance. Liquid handler
robots have been present in these facilities for a long time. New technologies and approaches, such as individual in-house solutions utilizing low-cost hardware
and open-source software to implement Internet-of-Things concepts, are opening up new possibilities in extending functionality flexibly. In this paper, a concept is
presented for the detection of potential gripping failures in a liquid handler robot with an infrared break beam sensor. During the problematic step, the robot has to
pick up an object from a container rack, while the...

[125] Utilizing Social Media and Video Games to Control #DIY Microscopes
Maxime Leblanc-Latour, ..., and A. Pelling. bioRxiv, 2016. 2 citations.
0% Topic Match
Abstract: Open-source lab equipment is becoming more widespread with the popularization of fabrication tools such as 3d-printers, laser cutters, CNC machines,
open source microcontrollers and open source software. Although many pieces of common laboratory equipment have been developed, software control of these
items is sometimes lacking. Specifically, control software that can be easily implemented and enable user-input and control over multiple platforms (PC, smartphone,
web, etc.). The aim of this proof-of-principle study was to develop and implement software for the control of a low-cost, 3d-printed microscope. Here, we present
two approaches, which enable microscope control by exploiting the functionality of the...

[126] Abstracts of papers presented at the ISLAR (International Symposium on Laboratory Automation and Robotics) 2001

A. Fermier and Ramon L. Rodriguez John Troisi. Journal of Automated Methods and Management in Chemistry, 2002. 0 citations.
0% Topic Match
Abstract: s of papers presented at the ISLAR (International Symposium on Laboratory Automation and Robotics) 2001 The 19th International Symposium on
Laboratory Automation and Robotics provided presentations on state-of-the-art developments in laboratory automation and robotics. The symposium programme
included papers and posters on all aspects of the technology. These comprised: managing laboratory automation (drug discovery); bioanalytical analysis; managing
laboratory automation in drug discovery development and QC laboratory; functional genomics strategies and high throughput screening; advanced integration
strategies; method development and global methods transfer; compound handling and logistics; combinatorial chemistry and automated synthesis ; high throughput
LC-MS-MS; increasing eæ ciency in dissolution...

[127] RoombaCreate® for Remote Laboratories

A. Azad and Pramod Kaushik. Int. J. Online Eng., 2014. 6 citations.
0% Topic Match
Abstract: Internet has advanced significantly with the aid of electronics and communication technologies. This allows us to undertake ambitious activities over the
Internet, which are unthinkable even few years back. With this new scenario, performing experiments that involve real hardware remotely over the web is now a
reality. Controlling hardware experiments remotely is labeled as remote laboratory. Considering the complexities of technologies involved with remote laboratories,
hardware experimental systems need to be customized before they can be integrated within a remote laboratory system. One such system is a mobile robot that
can be used for various student learning laboratory activities. This...

[128] Powering the world’s robots—10 years of ROS

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 37/43

Undermind

REPORT CREATED ON
1/12/2026

Lin Zhang, ..., and Guang-Zhong Yang. Science Robotics, 2017. 24 citations.
0% Topic Match
No summary or abstract available

[129] The Laboratory Automation Protocol (LAP) Format and Repository: A Platform for Enhancing Workflow Efficiency in Synthetic Biology

Ana-Mariya Anhel, ..., and Ángel Goñi-Moreño. ACS Synthetic Biology, 2023. 6 citations.
0% Topic Match
Abstract: Laboratory automation deals with eliminating manual tasks in high-throughput protocols. It therefore plays a crucial role in allowing fast and reliable synthetic
biology. However, implementing open-source automation solutions often demands experimental scientists to possess scripting skills, and even when they do, there
is no standardized toolkit available for their use. To address this, we present the Laboratory Automation Protocol (LAP) Format and Repository. LAPs adhere to
a standardized script-based format, enhancing end-user implementation and simplifying further development. With a modular design, LAPs can be seamlessly
combined to create customized, target-specific workflows. Furthermore, all LAPs undergo experimental validation, ensuring their reliability....

[130] From Concepts to Applications: A Comprehensive Overview of ROS

Esmeralda Kadena, ..., and Zóltan Rajnai. 2025 IEEE 12th International Conference on Computational Cybernetics and Cyber-Medical Systems
(ICCC), 2025. 0 citations.
0% Topic Match
Abstract: This paper explores the Robot Operating System (ROS), a foundational open-source middleware designed to facilitate robotics development by integrating
hardware and software. It provides essential tools and algorithms enabling efficient programming of complex robotic systems. This work delves into the core
components of ROS, including its computational graph model, parameter servers, and messaging systems, while highlighting tools that enhance system capabilities.
Additionally, the paper reviews navigation algorithms, from traditional ones to advanced path-planning techniques, emphasizing their applications in autonomous
mobile robotics. Comparisons of robotics software platforms illustrate the diversity and adaptability required to meet the demands of modern robotics. In...

[131] AUTOMAÇÃO LABORATORIAL: UM DOMÍNIO DE APLICAÇÃO E UM SOFTWARE DE APOIO

Luiz Maurício da Silva Cunha. Unknown journal, 1993. 0 citations.
0% Topic Match
Abstract: Laboratory Automation Systems can automate a significative portion of tasks involved in the process of investigating a product. Such systems, in addition
to providing for quick and precise capture of data from input devices, also allows fast analysis of those data, thus helping users to take faster decisions. This
dissertation reviews concepts related to communication interfaces, man-machine interfaces , software development environments, application generators and
systems for laboratory automation with the objective of laying the foundations for the development of a prototype system for laboratory automation (SAL). This
system allows that laboratory technicians with small knowledge of computer programming be...

[132] Integration of Analytical Instruments with Computer Scripting

M. C. Carvalho. Journal of Laboratory Automation, 2013. 13 citations.
0% Topic Match
Abstract: Automation of laboratory routines aided by computer software enables high productivity and is the norm nowadays. However, the integration of different
instruments made by different suppliers is still difficult, because to accomplish it, the user must have knowledge of electronics and/or low-level programming. An
alternative approach is to control different instruments without an electronic connection between them, relying only on their software interface on a computer. This
can be achieved through scripting, which is the emulation of user operations (mouse clicks and keyboard inputs) on the computer. The main advantages of this
approach are its simplicity, which enables people with...

[133] Labassistant: a web-based general-purpose software for the delivery and administration of computer based laboratory sessions

E. Kehris, ..., and G. Fragidis. Unknown journal, 2003. 2 citations.
0% Topic Match
No summary or abstract available

[134] The Role of Robotics in the Laboratory of the 80s

J. N. Little. Journal of Research of the National Bureau of Standards, 1988. 0 citations.
0% Topic Match
Abstract: A new technology, robotics, already being used in other fields, is slated to have a major impact in automating operations and procedures performed in
chemistry laboratories during the eighties. Introduced only 5 years ago, it has become the fastest growing new technology for the laboratory. An introduction to
laboratory robotics, which combines the technologies of chemistry, analytical instrumentation, computers and robotics, will be presented first. Laboratory automation,
once limited to computerized data reduction, can now include sample handling and sample preparation, wet chemistry procedures, and instrumental analysis.
Laboratory robots, utilizing programmable computers, can be easily reprogrammed to do a variety...

[135] An end-to-end solution for automation of biological protocols

Vishal Gupta. Unknown journal, 2017. 0 citations.
0% Topic Match
Abstract: The inability to reproduce the results of biological research has long been the elephant in the room. Non-reproducibility of results causes billions of dollars
in losses in money, time and other resources. This slows down over all scientific progress. There are some important factors which contribute to the reproducibility
problem. There is ambiguity in experimental method specification, human error introduced while conducting experiment and lack of data sharing standards. Recently,
some interesting approaches have been developed to alleviate the reproducibility problem. They are the use of 1) programming languages for removing ambiguity
in experimental method specification, 2) use of robotic...

[136] Special issue on software framework for Robot system integration

K. Ohara, ..., and Mirko Bordignon. Advanced Robotics, 2022. 0 citations.
0% Topic Match
Abstract: Software frameworks such as simulators, testing tools, robot middleware, and platforms are essential technologies in system integration in robotics.
Software frameworks divide certain functionalities into abstracted common functions and specific individual functions and contribute to solvingmany problems in
one scheme. Simulators and test tools allow you tomakemore types of trials more times than in reality. The framework of middleware and platforms promotes
modularization and containerization, which contributes to system reusability and increased flexibility. In general, researchers tend to think of a framework as a black
box and focus on how to use it. However, the abstraction and commonalities of functions...

[137] The Internet of Things comes to the lab
Jeffrey Perkel. Nature, 2017. 121 citations.
0% Topic Match
No summary or abstract available

[138] PythonRobotics: a Python code collection of robotics algorithms
Atsushi Sakai, ..., and Alexis Paques. ArXiv, 2018. 102 citations.
0% Topic Match
Abstract: This paper describes an Open Source Software (OSS) project: PythonRobotics. This is a collection of robotics algorithms implemented in the Python
programming language. The focus of the project is on autonomous navigation, and the goal is for beginners in robotics to understand the basic ideas behind each
algorithm. In this project, the algorithms which are practical and widely used in both academia and industry are selected. Each sample code is written in Python3
and only depends on some standard modules for readability and ease of use. It includes intuitive animations to understand the behavior of the simulation.

[139] Uma Proposta de Framework para Sistemas de Software de Controle para Plataformas de Robótica Social

M. Rocha, ..., and D. Muchaluat-Saade. Proceedings of the 30th Brazilian Symposium on Multimedia and the Web (WebMedia 2024), 2024. 0
citations.
0% Topic Match

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 38/43

Undermind

REPORT CREATED ON
1/12/2026

Abstract: There is a gap in open-source robotic platforms that can be customized according to application needs and available resources. Software systems for
robots are usually complex due to the need to control multiple sensors and actuators in real time, while simultaneously and asynchronously performing tasks and
responding to unexpected situations. In this context, a well-designed architecture that could facilitate building and using robots is desirable. This work proposes
a framework for the development of control systems for social robotics platforms. The framework is modular and easily extensible, as it uses an object-oriented
approach and adopts the publish-subscribe paradigm for asynchronous...

[140] THE ROLE OF TEST AUTOMATION FRAMEWORKS IN ENHANCING SOFTWARE RELIABILITY: A REVIEW OF SELENIUM, PYTHON,
AND API TESTING TOOLS

Sheratun Noor Jyoti, ..., and Sai Praveen Kudapa. International Journal of Business and Economics Insights, 2024. 1 citations.
0% Topic Match
Abstract: Software reliability is a critical quality attribute that determines the stability, performance, and user trustworthiness of modern applications. As software
systems grow in complexity, manual testing becomes insufficient for detecting defects and ensuring consistent functionality across frequent iterations. Test automation
frameworks have emerged as essential tools to streamline validation, improve fault detection, and enhance overall system reliability. This review explores the role of
prominent automation technologies—Selenium, Python-based frameworks, and Application Programming Interface (API) testing tools—in strengthening software
reliability. Selenium remains a cornerstone for automated web interface testing due to its cross-browser support, integration with continuous integration/continuous
delivery (CI/CD) pipelines, and...

[141] OCTOPUS: operation control system for task optimization and job parallelization via a user-optimal scheduler

H. Yoo, ..., and S. Han. Nature Communications, 2024. 7 citations.
Not measured Topic Match
Abstract: The material acceleration platform, empowered by robotics and artificial intelligence, is a transformative approach for expediting material discovery
processes across diverse domains. However, the development of an operating system for material acceleration platform faces challenges in simultaneously managing
diverse experiments from multiple users. Specifically, when it is utilized by multiple users, the overlapping challenges of experimental modules or devices can lead
to inefficiencies in both resource utilization and safety hazards. To overcome these challenges, we present an operation control system for material acceleration
platform, namely, OCTOPUS, which is an acronym for operation control system for task optimization and job parallelization...

[142] Self-Driving Laboratories for Chemistry and Materials Science

Gary Tom, ..., and Alán Aspuru-Guzik. Chemical Reviews, 2024. 262 citations.
Not measured Topic Match
Abstract: Self-driving laboratories (SDLs) promise an accelerated application of the scientific method. Through the automation of experimental workflows, along with
autonomous experimental planning, SDLs hold the potential to greatly accelerate research in chemistry and materials discovery. This review provides an in-depth
analysis of the state-of-the-art in SDL technology, its applications across various scientific disciplines, and the potential implications for research and industry. This
review additionally provides an overview of the enabling technologies for SDLs, including their hardware, software, and integration with laboratory infrastructure.
Most importantly, this review explores the diverse range of scientific domains where SDLs have made significant contributions, from...

[143] AlabOS: A Python-based Reconfigurable Workflow Management Framework for Autonomous Laboratories

Yuxing Fei, ..., and Gerbrand Ceder. ArXiv, 2024. 10 citations.
Not measured Topic Match
Abstract: AlabOS is a workflow orchestration framework designed to address the increased complexity in autonomous laboratories, featuring a reconfigurable
experiment workflow model and a resource reservation mechanism.

[144] Array programming with NumPy

Charles R. Harris, ..., and T. Oliphant. Nature, 2020. 18037 citations.
Not measured Topic Match
Abstract: Array programming provides a powerful, compact and expressive syntax for accessing, manipulating and operating on data in vectors, matrices and
higher-dimensional arrays. NumPy is the primary array programming library for the Python language. It has an essential role in research analysis pipelines in fields
as diverse as physics, chemistry, astronomy, geoscience, biology, psychology, materials science, engineering, finance and economics. For example, in astronomy,
NumPy was an important part of the software stack used in the discovery of gravitational waves1 and in the first imaging of a black hole2. Here we review how a
few fundamental array concepts lead to a...

[145] An autonomous laboratory for the accelerated synthesis of novel materials

N. Szymanski, ..., and G. Ceder. Nature, 2023. 587 citations.
Not measured Topic Match
Abstract: An autonomous laboratory, the A-Lab, is presented that combines computations, literature data, machine learning and active learning, which discovered
and synthesized 41 novel compounds from a set of 58 targets after 17 days of operation. To close the gap between the rates of computational screening and
experimental realization of novel materials^ 1 , 2 , we introduce the A-Lab, an autonomous laboratory for the solid-state synthesis of inorganic powders. This platform
uses computations, historical data from the literature, machine learning (ML) and active learning to plan and interpret the outcomes of experiments performed using
robotics. Over 17 days of continuous...

[146] IPython: A System for Interactive Scientific Computing

Fernando Pérez and B. Granger. Computing in Science & Engineering, 2007. 2855 citations.
Not measured Topic Match
No summary or abstract available

[147] Computer Control of Microscopes Using µManager

A. Edelstein, ..., and N. Stuurman. Current Protocols in Molecular Biology, 2010. 1629 citations.
Not measured Topic Match
No summary or abstract available

[148] Flexible automation accelerates materials discovery

B. MacLeod, ..., and C. Berlinguette. Nature Materials, 2021. 67 citations.
Not measured Topic Match
No summary or abstract available

[149] A one-piece 3D printed flexure translation stage for open-source microscopy.

J. P. Sharkey, ..., and R. Bowman. The Review of scientific instruments, 2015. 119 citations.
Not measured Topic Match
Abstract: Open source hardware has the potential to revolutionise the way we build scientific instruments; with the advent of readily available 3D printers, mechanical
designs can now be shared, improved, and replicated faster and more easily than ever before. However, printed parts are typically plastic and often perform poorly
compared to traditionally machined mechanisms. We have overcome many of the limitations of 3D printed mechanisms by exploiting the compliance of the plastic
to produce a monolithic 3D printed flexure translation stage, capable of sub-micron-scale motion over a range of 8 × 8 × 4 mm. This requires minimal post-print
clean-up and...

[150] PyTorch: An Imperative Style, High-Performance Deep Learning Library
Adam Paszke, ..., and Soumith Chintala. ArXiv, 2019. 48593 citations.
Not measured Topic Match
Abstract: Deep learning frameworks have often focused on either usability or speed, but not both. PyTorch is a machine learning library that shows that these two
goals are in fact compatible: it was designed from first principles to support an imperative and Pythonic programming style that supports code as a model, makes
debugging easy and is consistent with other popular scientific computing libraries, while remaining efficient and supporting hardware accelerators such as GPUs.
In this paper, we detail the principles that drove the implementation of PyTorch and how they are reflected in its architecture. We emphasize that every aspect of
PyTorch...

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 39/43

Undermind

REPORT CREATED ON
1/12/2026

[151] High-throughput Approaches to Uncover Synergistic Drug Combinations in Leukemia

Emma J. Chory, ..., and Benjamin Z. Stanton. bioRxiv, 2022. 7 citations.
Not measured Topic Match
Abstract: We report a comprehensive drug synergy study in acute myeloid leukemia (AML). In this work, we investigate 11 cell lines spanning both MLL-rearranged
and non-rearranged subtypes. The work comprises a resource for the community, with many synergistic drug combinations that could not have been predicted a
priori, and open source code for automation and analyses. We base our definitions of drug synergy on the Chou-Talalay method, which is useful for visualizations
of synergy experiments in isobolograms, and median-effects plots, among other representations. Our key findings include drug synergies affecting the chromatin
state, specifically in the context of regulation of the...

[152] Advanced methods of microscope control using ¼Manager software.

A. Edelstein, ..., and N. Stuurman. Journal of biological methods, 2014. 1776 citations.
Not measured Topic Match
Abstract: ¼Manager is an open-source, cross-platform desktop application, to control a wide variety of motorized microscopes, scientific cameras, stages, illuminators,
and other microscope accessories. Since its inception in 2005, ¼Manager has grown to support a wide range of microscopy hardware and is now used by thousands
of researchers around the world. The application provides a mature graphical user interface and offers open programming interfaces to facilitate plugins and scripts.
Here, we present a guide to using some of the recently added advanced ¼Manager features, including hardware synchronization, simultaneous use of multiple
cameras, projection of patterned light onto a specimen, live slide...

[153] Matplotlib: A 2D Graphics Environment

John D. Hunter. Computing in Science & Engineering, 2007. 22920 citations.
Not measured Topic Match
No summary or abstract available

[154] Systematic molecular evolution enables robust biomolecule discovery
E. DeBenedictis, ..., and K. Esvelt. Nature Methods, 2021. 51 citations.
Not measured Topic Match
No summary or abstract available

[155] Automation isn't automatic

M. Christensen, ..., and J. Hein. Chemical Science, 2021. 38 citations.
Not measured Topic Match
Abstract: Automation has become an increasingly popular tool for synthetic chemists over the past decade. Recent advances in robotics and computer science have
led to the emergence of automated systems that execute common laboratory procedures including parallel synthesis, reaction discovery, reaction optimization,
time course studies, and crystallization development. While such systems offer many potential benefits, their implementation is rarely automatic due to the highly
specialized nature of synthetic procedures. Each reaction category requires careful execution of a particular sequence of steps, the specifics of which change with
different conditions and chemical systems. Careful assessment of these critical procedural requirements and identification...

[156] An open-source technology platform to increase reproducibility and enable high-throughput production of tailorable gelatin methacryloyl
(GelMA) - based hydrogels

Sebastian Eggert, ..., and D. Hutmacher. Materials & Design, 2021. 11 citations.
Not measured Topic Match
No summary or abstract available

[157] A versatile and customizable low-cost 3D-printed open standard for microscopic imaging
Benedict Diederich, ..., and R. Heintzmann. Nature Communications, 2020. 129 citations.
Not measured Topic Match
Abstract: Modern microscopes used for biological imaging often present themselves as black boxes whose precise operating principle remains unknown, and whose
optical resolution and price seem to be in inverse proportion to each other. With UC2 (You. See. Too.) we present a low-cost, 3D-printed, open-source, modular
microscopy toolbox and demonstrate its versatility by realizing a complete microscope development cycle from concept to experimental phase. The self-contained
incubator-enclosed brightfield microscope monitors monocyte to macrophage cell differentiation for seven days at cellular resolution level (e.g. 2 ¼m). Furthermore,
by including very few additional components, the geometry is transferred into a 400 Euro light...

[158] Automation Solutions for Analytical Measurements: Concepts and Applications

Heidi Fleischer and K. Thurow. Unknown journal, 2017. 28 citations.
Not measured Topic Match
No summary or abstract available

[159] Flexible and Accessible Automated Operation of Miniature Chromatography Columns on a Liquid Handling Station.

S. Konstantinidis, ..., and A. Velayudhan. Biotechnology journal, 2018. 16 citations.
Not measured Topic Match
No summary or abstract available

[160] Enhancing bioreactor arrays for automated measurements and reactive control with ReacSight

F. Bertaux, ..., and Grégory Batt. Nature Communications, 2020. 38 citations.
Not measured Topic Match
Abstract: Small-scale, low-cost bioreactors provide exquisite control of environmental parameters of microbial cultures over long durations. Their use is gaining
popularity in quantitative systems and synthetic biology. However, existing setups are limited in their measurement capabilities. Here, we present ReacSight, a
strategy to enhance bioreactor arrays for automated measurements and reactive experiment control. ReacSight leverages low-cost pipetting robots for sample
collection, handling and loading, and provides a flexible instrument control architecture. We showcase ReacSight capabilities on three applications in yeast. First,
we demonstrate real-time optogenetic control of gene expression. Second, we explore the impact of nutrient scarcity on fitness and cellular...

[161] ChemOS: Orchestrating autonomous experimentation

L. Roch, ..., and Alán Aspuru-Guzik. Science Robotics, 2018. 135 citations.
Not measured Topic Match
Abstract: ChemOS aims to catalyze the expansion of autonomous laboratories and to disrupt the conventional approach to experimentation. ChemOS aims to
catalyze the expansion of autonomous laboratories and to disrupt the conventional approach to experimentation.

[162] CellProfiler 3.0: Next-generation image processing for biology

C. McQuin, ..., and Anne E Carpenter. PLoS Biology, 2018. 1679 citations.
Not measured Topic Match
Abstract: CellProfiler has enabled the scientific research community to create flexible, modular image analysis pipelines since its release in 2005. Here, we describe
CellProfiler 3.0, a new version of the software supporting both whole-volume and plane-wise analysis of three-dimensional (3D) image stacks, increasingly common
in biomedical research. CellProfiler’s infrastructure is greatly improved, and we provide a protocol for cloud-based, large-scale image processing. New plugins
enable running pretrained deep learning models on images. Designed by and for biologists, CellProfiler equips researchers with powerful computational tools via a
well-documented user interface, empowering biologists in all fields to create quantitative, reproducible image analysis workflows.

[163] Implementation of an Automated High-Throughput Plasmid DNA Production Pipeline

K. Billeci, ..., and Stephen Monteclaro. Journal of Laboratory Automation, 2016. 6 citations.
Not measured Topic Match

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 40/43

Undermind

REPORT CREATED ON
1/12/2026

Abstract: Biologics sample management facilities are often responsible for a diversity of large-molecule reagent types, such as DNA, RNAi, and protein libraries.
Historically, the management of large molecules was dispersed into multiple laboratories. As methodologies to support pathway discovery, antibody discovery, and
protein production have become high throughput, the implementation of automation and centralized inventory management tools has become important. To this end,
to improve sample tracking, throughput, and accuracy, we have implemented a module-based automation system integrated into inventory management software
using multiple platforms (Hamilton, Hudson, Dynamic Devices, and Brooks). Here we describe the implementation of these systems with a...

[164] Wavefront(cid:16)sensorless adaptive optics with a laser(cid:16)free spinning disk confocal microscope

S. Hussain, ..., and M. Booth. Journal of Microscopy, 2020. 9 citations.
Not measured Topic Match
Abstract: Adaptive optics is being applied widely to a range of microscopies in order to improve imaging quality in the presence of specimen-induced aberrations. We
present here the first implementation of wavefront-sensorless adaptive optics for a laser-free, aperture correlation, spinning disk microscope. This widefield method
provides confocal-like optical sectioning through use of a patterned disk in the illumination and detection paths. Like other high-resolution microscopes, its operation
is compromised by aberrations due to refractive index mismatch and variations within the specimen. Correction of such aberrations shows improved signal level,
contrast and resolution.

[165] Stable stimulated emission depletion imaging of extended sample regions

Jonatan Alvelid and Ilaria Testa. Journal of Physics D: Applied Physics, 2019. 18 citations.
Not measured Topic Match
Abstract: Stimulated emission depletion (STED) nanoscopy has become one of the most used nanoscopy techniques over the last decade. However, most recordings
are done in specimen regions no larger than 10–30 × 10–30 ¼m2 due to aberrations, instability and manual mechanical stages. Here, we demonstrate automated
2D and 3D STED nanoscopy of extended sample regions up to 0.5 × 0.5 mm2 by using a scanning system that maintains stationary beams in the back focal plane.
The setup allows up to 80–100 × 80–100 ¼m2 field of view (FOV) with uniform spatial resolution, a mechanical stage allowing sequential tiling to record larger...

[166] ACQ4: an open-source software platform for data acquisition and analysis in neurophysiology research

Luke Campagnola, ..., and P. Manis. Frontiers in Neuroinformatics, 2014. 59 citations.
Not measured Topic Match
Abstract: The complexity of modern neurophysiology experiments requires specialized software to coordinate multiple acquisition devices and analyze the collected
data. We have developed ACQ4, an open-source software platform for performing data acquisition and analysis in experimental neurophysiology. This software
integrates the tasks of acquiring, managing, and analyzing experimental data. ACQ4 has been used primarily for standard patch-clamp electrophysiology, laser
scanning photostimulation, multiphoton microscopy, intrinsic imaging, and calcium imaging. The system is highly modular, which facilitates the addition of new
devices and functionality. The modules included with ACQ4 provide for rapid construction of acquisition protocols, live video display, and customizable analysis
tools....

[167] Seamless integration of legacy robotic systems into a self-driving laboratory via NIMO: a case study on liquid handler automation

Ryo Tamura, ..., and Shoichi Matsuda. Science and Technology of Advanced Materials: Methods, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[168] Self-driving laboratories with artificial intelligence: An overview of process systems engineering perspective

Youhyun Kim, ..., and Jonggeol Na. Comput. Chem. Eng., 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[169] Towards a Modular Architecture for Science Factories

Rafael Vescovi, ..., and Ian T Foster. ArXiv, 2023. 13 citations.
Not measured Topic Match
Abstract: Advances in robotic automation, high-performance computing (HPC), and artificial intelligence (AI) encourage us to conceive of science factories: large,
general-purpose computation- and AI-enabled self-driving laboratories (SDLs) with the generality and...

[170] An affordable platform for automated synthesis and electrochemical characterization

Sergio Pablo-García, ..., and Alán Aspuru-Guzik. Device, 2024. 9 citations.
Not measured Topic Match
No summary or abstract available

[171] Engineering a Sustainable Future: Harnessing Automation, Robotics, and Artificial Intelligence with Self-Driving Laboratories

S. Sadeghi, ..., and M. Abolhasani. ACS Sustainable Chemistry &amp; Engineering, 2024. 26 citations.
Not measured Topic Match
No summary or abstract available

[172] A dynamic knowledge graph approach to distributed self-driving laboratories
Jiaru Bai, ..., and Markus Kraft. Nature Communications, 2024. 48 citations.
Not measured Topic Match
Abstract: The ability to integrate resources and share knowledge across organisations empowers scientists to expedite the scientific discovery process. This
is especially crucial in addressing emerging global challenges that require global solutions. In this work, we develop an architecture for distributed self-driving
laboratories within The World Avatar project, which seeks to create an all-encompassing digital twin based on a dynamic knowledge graph. We employ ontologies
to capture data and material flows in design-make-test-analyse cycles, utilising autonomous agents as executable knowledge components to carry out the
experimentation workflow. Data provenance is recorded to ensure its findability, accessibility, interoperability, and reusability. We demonstrate...

[173] A Case Study of Multimodal, Multi-institutional Data Management for the Combinatorial Materials Science Community

Sarah I. Allec, ..., and Apurva Mehta. Integrating Materials and Manufacturing Innovation, 2023. 3 citations.
Not measured Topic Match
Abstract: Although the convergence of high-performance computing, automation, and machine learning has significantly altered the materials design timeline,
transformative advances in functional materials and acceleration of their design will require addressing the deficiencies that currently exist in materials informatics,
particularly a lack of standardized experimental data management. The challenges associated with experimental data management are especially true for
combinatorial materials science, where advancements in automation of experimental workflows have produced datasets that are often too large and too complex
for human reasoning. The data management challenge is further compounded by the multimodal and multi-institutional nature of these datasets, as they tend...

[174] Designing workflows for materials characterization

S. Kalinin, ..., and R. Vasudevan. Applied Physics Reviews, 2023. 17 citations.
Not measured Topic Match
Abstract: Experimental science is enabled by the combination of synthesis, imaging, and functional characterization organized into evolving discovery loop. Synthesis
of new material is typically followed by a set of characterization steps aiming to provide feedback for optimization or discover fundamental mechanisms. However,
the sequence of synthesis and characterization methods and their interpretation, or research workflow, has traditionally been driven by human intuition and is highly
domain specific. Here, we explore concepts of scientific workflows that emerge at the interface between theory, characterization, and imaging. We discuss the
criteria by which these workflows can be constructed for special cases of multiresolution...

[175] Steering towards safe self-driving laboratories

Shi Xuan Leong, ..., and Alán Aspuru-Guzik. Nature Reviews Chemistry, 2025. 12 citations.
Not measured Topic Match

No summary or abstract available

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 41/43

Undermind

REPORT CREATED ON
1/12/2026

[176] Perspectives for artificial intelligence in bioprocess automation.

L. M. Helleckes, ..., and Héctor García Martín. Current opinion in biotechnology, 2025. 0 citations.
Not measured Topic Match
No summary or abstract available

[177] An open-source peristaltic pump with multiple independent channels for laboratory automation

Michael Buchhorn, ..., and Dominik Dworschak. Digital Discovery, 2025. 0 citations.
Not measured Topic Match
Abstract: An open-source peristaltic pump with fully independent channels and quick-swap cassettes was developed to meet the complex liquid handling demands
of self-driving labs and modern automated, data-driven experimental setups.

[178] Evaluating large language model agents for automation of atomic force microscopy

Indrajeet Mandal, ..., and N. M. A. Krishnan. Nature Communications, 2025. 2 citations.
Not measured Topic Match
Abstract: Large language models (LLMs) are transforming laboratory automation by enabling self-driving laboratories (SDLs) that could accelerate materials
research. However, current SDL implementations rely on rigid protocols that fail to capture the adaptability and intuition of expert scientists in dynamic experimental
settings. Here, we show that LLM agents can automate atomic force microscopy (AFM) through our Artificially Intelligent Lab Assistant (AILA) framework. Further,
we develop AFMBench—a comprehensive evaluation suite challenging LLM agents across the complete scientific workflow from experimental design to results
analysis. We find that state-of-the-art LLMs struggle with basic tasks and coordination scenarios. Notably, models excelling at materials science...

[179] Delocalized, asynchronous, closed-loop discovery of organic laser emitters
Felix Strieth-Kalthoff, ..., and Alán Aspuru-Guzik. Science, 2024. 79 citations.
Not measured Topic Match
Abstract: Contemporary materials discovery requires intricate sequences of synthesis, formulation, and characterization that often span multiple locations
with specialized expertise or instrumentation. To accelerate these workflows, we present a cloud-based strategy that enabled delocalized and asynchronous
design-make-test-analyze cycles. We showcased this approach through the exploration of molecular gain materials for organic solid-state lasers as a frontier
application in molecular optoelectronics. Distributed robotic synthesis and in-line property characterization, orchestrated by a cloud-based artificial intelligence
experiment planner, resulted in the discovery of 21 new state-of-the-art materials. Gram-scale synthesis ultimately allowed for the verification of best-in-class
stimulated emission in a thin-film device. Demonstrating the...

[180] Bohrium + SciMaster: Building the Infrastructure and Ecosystem for Agentic Science at Scale

Linfeng Zhang, ..., and E. Weinan. ArXiv, 2025. 1 citations.
Not measured Topic Match
Abstract: AI agents are emerging as a practical way to run multi-step scientific workflows that interleave reasoning with tool use and verification, pointing to a shift
from isolated AI-assisted steps toward \emph{agentic science at scale}. This shift is increasingly feasible, as scientific tools and models can be invoked through
stable interfaces and verified with recorded execution traces, and increasingly necessary, as AI accelerates scientific output and stresses the peer-review and
publication pipeline, raising the bar for traceability and credible evaluation. However, scaling agentic science remains difficult: workflows are hard to observe and
reproduce; many tools and laboratory systems are not agent-ready;...

[181] Advancing materials discovery through artificial intelligence

Martin Otyepka, ..., and Michal Otyepka. Applied Materials Today, 2025. 1 citations.
Not measured Topic Match
No summary or abstract available

[182] Towards greener-by-design fine chemicals. Part 2: technological frontiers.

Theodore A Gazis, ..., and Gianvito Vilé. Chemical Society reviews, 2025. 0 citations.
Not measured Topic Match
Abstract: Over the past three decades, the pharmaceutical and agrochemical sectors have embarked on a transformative journey towards greener-by-design
processes, firmly rooted in the principles of green chemistry. Building on this foundation, green engineering frameworks have expanded the focus beyond
environmental concerns to encompass product quality, economic viability, and the evolving demands of modern healthcare. At the heart of this transformation is
continuous and smart manufacturing due to its capacity to reduce raw material use, waste, and energy consumption. While attention has understandably centered
on replacing or refining conventional batch operations, the breadth of progress is far wider. Advanced analytics and...

[183] Bulky Phosphine Ligands Promote Palladium-Catalyzed Protodeboronation.

C. Ser, ..., and Alán Aspuru-Guzik. Journal of the American Chemical Society, 2025. 0 citations.
Not measured Topic Match
Abstract: The Suzuki-Miyaura cross-coupling reaction is plagued by protodeboronation, an undesirable side reaction with water that consumes the boronic acid
derivatives required for the cross-coupling reaction. Meticulous mechanistic studies have previously established protodeboronation to be highly sensitive to the
nature of the boronic reagent and reaction conditions. Particularly, the presence of bases, which are essential for the Suzuki-Miyaura coupling, is known to catalyze
protodeboronation. However, protodeboronation catalyzed by palladium-phosphine complexes, the benchmark catalyst system for Suzuki-Miyaura cross-coupling,
has been understudied compared to its base-catalyzed counterpart. We demonstrate, using automated high-throughput experimentation, comprehensive compu-
tational mechanistic analyses and kinetic modeling, that protodeboronation is...

[184] Spacer: Towards Engineered Scientific Inspiration

Minhyeong Lee, ..., and Juneau Jung. ArXiv, 2025. 0 citations.
Not measured Topic Match
Abstract: Recent advances in LLMs have made automated scientific research the next frontline in the path to artificial superintelligence. However, these systems
are bound either to tasks of narrow scope or the limited creative capabilities of LLMs. We propose Spacer, a scientific discovery system that develops creative
and factually grounded concepts without external intervention. Spacer attempts to achieve this via'deliberate decontextualization,'an approach that disassembles
information into atomic units - keywords - and draws creativity from unexplored connections between them. Spacer consists of (i) Nuri, an inspiration engine that
builds keyword sets, and (ii) the Manifesting Pipeline that refines these sets into...

[185] PQPAS: A High-Accuracy Pneumatic Quantitative Powder Auto-Sampling Workstation

Kaiyue Zheng, ..., and Chunlin Chen. 2025 IEEE 26th China Conference on System Simulation Technology and its Applications (CCSSTA), 2025.
0 citations.
Not measured Topic Match
Abstract: In current chemical laboratories, the utilization of automated machinery and robotic systems has become ubiquitous, as they adeptly manage tasks that
are arduous, monotonous, and hazardous, with a particular emphasis on high-throughput screening. While autonomous robots have been employed for tasks such
as container transfer and sampling, their efficacy is often constrained by the absence of sophisticated equipment. The development of equipment for handling
solid-state materials, especially compared to liquid sampling, has been relatively neglected and typically fails to accommodate dynamic variations in powders
throughout experimental procedures. To address this, we have engineered and deployed a high-precision pneumatic quantitative powder...

[186] Enabling large language models for real-world materials discovery

Santiago Miret and N. M. A. Krishnan. Nature Machine Intelligence, 2025. 16 citations.
Not measured Topic Match
No summary or abstract available

[187] A Grassroots Network and Community Roadmap for Interconnected Autonomous Science Laboratories for Accelerated Discovery

Rafael Ferreira da Silva, ..., and N. Washburn. Workshop Proceedings of the 54th International Conference on Parallel Processing, 2025. 5
citations.

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 42/43

Undermind

REPORT CREATED ON
1/12/2026

Not measured Topic Match
Abstract: Scientific discovery is being revolutionized by AI and autonomous systems, yet current autonomous laboratories remain isolated islands unable to
collaborate across institutions. We present the Autonomous Interconnected Science Lab Ecosystem (AISLE), a grassroots network transforming fragmented
capabilities into a unified system that shorten the path from ideation to innovation to impact and accelerates discovery from decades to months. AISLE addresses
five critical dimensions: (1) cross-institutional equipment orchestration, (2) intelligent data management with FAIR compliance, (3) AI-agent driven orchestration
grounded in scientific principles, (4) interoperable agent communication interfaces, and (5) AI/ML-integrated scientific education. By connecting autonomous agents
across institutional boundaries, autonomous...

[188] A revolutionary paradigm in chemistry and materials science research: self-driving laboratories.

Jiaxuan Qiu, ..., and Longlu Wang. Chemical communications, 2025. 2 citations.
Not measured Topic Match
Abstract: A self-driving laboratory (SDL), an automated experimental platform that integrates machine learning algorithms and robotics, has the potential to
revolutionize traditional research methods and accelerate progress in chemistry and materials science. However, despite its significant potential, the development
and practical application of SDLs have not yet met expectations. To date, only a limited number of SDLs have been successfully constructed and applied in
research, mainly due to the challenges involved in fostering interdisciplinary collaboration and achieving high levels of system integration. In this review, we present
a comprehensive overview of recent SDL applications in chemistry and materials science. Firstly, SDLs...

[189] Empowering Generalist Material Intelligence with Large Language Models
Wenhao Yuan, ..., and Fengqi You. Advanced Materials, 2025. 5 citations.
Not measured Topic Match
Abstract: Large language models (LLMs) are steering the development of generalist materials intelligence (GMI), a unified framework integrating conceptual
reasoning, computational modeling, and experimental validation. Central to this framework is the agent(cid:16)in(cid:16)the(cid:16)loop paradigm, where LLM(cid:16)based agents function as
dynamic orchestrators, synthesizing multimodal knowledge, specialized models, and experimental robotics to enable fully autonomous discovery. Drawing from
a comprehensive review of LLMs’ transformative impact across representative applications in materials science, including data extraction, property prediction,
structure generation, synthesis planning, and self(cid:16)driven labs, this study underscores how LLMs are revolutionizing traditional tasks, catalyzing the agent(cid:16)in(cid:16)the(cid:16)loop
paradigm, and bridging the ontology(cid:16)concept(cid:16)computation(cid:16)experiment continuum. Then the unique...

[190] A Helping Hand: A Survey About AI-Driven Experimental Design for Accelerating Scientific Research

Lukas Nolte and Sven Tomforde. Applied Sciences, 2025. 6 citations.
Not measured Topic Match
Abstract: Designing and conducting experiments is a fundamental process across various scientific disciplines, such as materials science, biology, medicine, and
chemistry. However, experimental research still predominantly relies on traditional, time-consuming, resource-intensive, and costly trial-and-error experimentation
approaches that hinder rapid discovery, reproducibility, and scalability. Recent advances in artificial intelligence (AI) and machine learning (ML) offer promising
alternatives, but a comprehensive overview of their implementations in experimental design is lacking. This research fills this gap by providing a structured overview
and analysis of existing frameworks for AI-driven experimental design, supporting researchers in selecting and developing suitable AI-driven approaches to automate
and accelerate their...

[191] El Agente: An Autonomous Agent for Quantum Chemistry

Yunheng Zou, ..., and Al'an Aspuru-Guzik. ArXiv, 2025. 26 citations.
Not measured Topic Match
No summary or abstract available

[192] Local reaction condition optimization via machine learning

Wenhuan Song and Honggang Sun. Journal of Molecular Modeling, 2025. 1 citations.
Not measured Topic Match
No summary or abstract available

[193] Artificial Intelligence Meets Laboratory Automation in Discovery and Synthesis of Metal–Organic Frameworks: A Review

Yiming Zhao, ..., and Zhuo Wang. Industrial &amp; Engineering Chemistry Research, 2025. 15 citations.
Not measured Topic Match
No summary or abstract available

[194] Adaptive representation of molecules and materials in Bayesian optimization
M. Rajabi-Kochi, ..., and S. M. Moosavi. Chemical Science, 2025. 6 citations.
Not measured Topic Match
Abstract: Bayesian optimization (BO) is increasingly used in molecular optimization and in guiding self-driving laboratories for automated materials discovery. A
crucial aspect of BO is how molecules and materials are represented as feature vectors, where both the completeness and compactness of these representations
can influence the efficiency of the optimization process. Traditionally, a fixed representation is chosen by expert chemists or applying data-driven feature selection
methods on available labeled datasets. However, when dealing with novel optimization tasks, prior knowledge or large datasets are often unavailable, and relying
on these even can introduce bias into the search process. In this work, we...

[195] Enhancing FAIRdata by providing digital workflows from data generation to the publication of data: an open source approach described for
cyclic voltammetry

David Herrmann, ..., and Stefan Bräse. Chemical Science, 2025. 1 citations.
Not measured Topic Match
Abstract: Analytical data in chemistry and other disciplines is usually generated in different formats and lacks common data and metadata standards that are
necessary for a FAIR handling of research data. In the work presented herein, we describe a workflow that uses non-standardized, in some cases proprietary, data
formats from cyclic voltammetry measurements coming from individual devices as an instructive example, to yield open, standardized data that are annotated with
rich metadata. The presented workflow includes concepts, software and infrastructure that can be used to support the whole data life cycle from the measurement
of data to the publication of data...

[196] Balancing autonomy and expertise in autonomous synthesis laboratories

Xiaozhao Liu, ..., and Yan Zeng. Nature Computational Science, 2025. 6 citations.
Not measured Topic Match
No summary or abstract available

[197] Foundational Large Language Models for Materials Research

Vaibhav Mishra, ..., and N. M. A. Krishnan. ArXiv, 2024. 15 citations.
Not measured Topic Match
Abstract: Materials discovery and development are critical for addressing global challenges. Yet, the exponential growth in materials science literature comprising
vast amounts of textual data has created significant bottlenecks in knowledge extraction, synthesis, and scientific reasoning. Large Language Models (LLMs) offer
unprecedented opportunities to accelerate materials research through automated analysis and prediction. Still, their effective deployment requires domain-specific
adaptation for understanding and solving domain-relevant tasks. Here, we present LLaMat, a family of foundational models for materials science developed through
continued pretraining of LLaMA models on an extensive corpus of materials literature and crystallographic data. Through systematic evaluation, we demonstrate
that LLaMat...

View this report online at:
https://app.undermind.ai/report/33784a934841ec686799b46239c648f89fc34bc70406e5124e85073cc01ba69a

Page 43/43
