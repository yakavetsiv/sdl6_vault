---
tags:
  - literature
  - type/paper
title: "PyLabRobot: An open-source, hardware-agnostic interface for liquid-handling robots and accessories"
zotero_item_key: Q8R3X4BE
zotero_attachment_key: KFAEZTDS
date: "2023-10-20"
type: zotero-pdf-fulltext
---

# PyLabRobot: An open-source, hardware-agnostic interface for liquid-handling robots and accessories

## Metadata

- Zotero item key: `Q8R3X4BE`
- Zotero attachment key: `KFAEZTDS`
- Authors: Rick P. Wierenga, Stefan M. Golas, Wilson Ho, Connor W. Coley, Kevin M. Esvelt
- Date: 2023-10-20
- DOI: 10.1016/j.device.2023.100111
- URL: https://www.cell.com/device/abstract/S2666-9986(23)00170-9
- Attachment title: Full Text PDF
- Indexed characters: 55728

## Extracted Text

Article
PyLabRobot: An open-source, hardware-agnostic interface for liquid-handling robots and accessories
Graphical abstract
Highlights
d A universal, open-source Python interface for liquid-handling robots and accessories
d Works on any modern operating system: Windows, macOS, Linux, Raspberry Pi OS
d Includes a browser-based simulator and works with LLM assistants
d Can be used interactively for rapid protocol debugging and iteration
Authors
Rick P. Wierenga, Stefan M. Golas, Wilson Ho, Connor W. Coley, Kevin M. Esvelt
Correspondence esvelt@mit.edu
In brief
PyLabRobot is an open-source framework that empowers researchers, including non-specialists, to interactively program a wide range of liquid-handling robots and accessories using Python or an LLM assistant. It supports various hardware models (including Hamiltons and Tecans) through a single interface; works on Windows, Linux, macOS, and Raspberry Pi OS; and includes a simulator for safe code testing. By making it easy to program laboratory robots and share methods, PyLabRobot accelerates discoveries while improving reproducibility and safety.
A
B
Wierenga et al., 2023, Device 1, 100111 October 20, 2023 a 2023 Published by Elsevier Inc. https://doi.org/10.1016/j.device.2023.100111
ll


Article
PyLabRobot: An open-source, hardware-agnostic interface for liquid-handling robots and accessories
Rick P. Wierenga,1,2 Stefan M. Golas,2 Wilson Ho,2,3 Connor W. Coley,4 and Kevin M. Esvelt2,5,* 1Leiden University, 2311 EZ Leiden, Zuid-Holland, the Netherlands 2Media Lab, Massachusetts Institute of Technology, Cambridge, MA 02139, USA 3Department of Computer Science, Massachusetts Institute of Technology, Cambridge, MA 02139, USA 4Department of Chemical Engineering, Massachusetts Institute of Technology, Cambridge, MA 02139, USA 5Lead contact *Correspondence: esvelt@mit.edu https://doi.org/10.1016/j.device.2023.100111
SUMMARY
Liquid-handling robots are often limited by proprietary interfaces that are only compatible with a single type of robot and operating system, restricting method sharing and slowing development. Here, we present PyLabRobot, an open-source, cross-platform Python interface capable of programming diverse liquidhandling robots, including Hamilton STARs and Vantages, Tecan EVOs, and Opentron OT-2s. PyLabRobot provides an interface for a universal set of commands and deck layout representations while enabling the control of diverse accessory devices. The interface can work with any liquid-handling robot capable of aspirating and dispensing precise volumes of liquid within a Cartesian coordinate system. In addition to the already integrated robots, we include guidance on integrating new liquid-handling systems and accessories. We validated the framework through unit tests and application demonstrations, including a browser-based simulator, a position calibration tool, and a path-teaching tool for complex movements. PyLabRobot provides a flexible, open, and collaborative programming environment for laboratory automation.
INTRODUCTION
Pipetting, the act of moving small amounts of liquids around, is the foundation of many biology and chemistry experiments. Pipetting fundamentally involves four operations: the mounting of tips on a pipettor, aspirating (moving liquid into the tip), dispensing (moving liquid out of the tip), and removing the tip from the pipettor. Liquid-handling robots automate these operations, in principle making them versatile tools capable of executing a wide range of experiments in much higher
throughput and with higher precision than is possible for humans while also increasing the safety and security of the laboratory environment. Robots are capable of performing many protocols, including mammalian tissue culture,1 organoid culture,2 hydrogel production,3 directed evolution,4 combinatorial drug screening,5 plasmid assembly,6–8 and high-throughput genomics sequencing.9 Liquid handlers can also be integrated with computational resources such as machine learning models to perform closed-loop feedback control over iterated experiments.10–13 However, current robots are limited by a ubiquitous
THE BIGGER PICTURE Many wet-lab biology protocols can be executed by liquid-handling robots, which increase the reproducibility and speed of experiments. However, these robots are often programmed with unwieldy proprietary interfaces that are daunting even for automation specialists. We developed PyLabRobot, an open-source, cross-platform framework that lets researchers program their liquid-handling robots and accessory equipment through an interactive and universal Python interface while enabling protocols to be easily shared with the community. We provide integrations for four different liquid-handling robots (including Hamilton STAR and Tecan Freedom EVO) and one plate reader, as well as guidance for researchers looking to create and share their own equipment integrations. Drawing on the strong tradition of open-source software, we hope that PyLabRobot will accelerate biological discoveries by making laboratory automation accessible to researchers who are not robot specialists or expert programmers.
Device 1, 100111, October 20, 2023 a 2023 Published by Elsevier Inc. 1
ll


reliance on inflexible proprietary software—without commandlevel control—as the sole medium for creating and executing protocols, sharply constraining their versatility, accessibility, and compatibility with external equipment and software. In principle, the basic operations of loading disposable tips, aspirating and dispensing precise volumes of liquid, moving plates, and interfacing with accessories such as plate readers are highly similar across liquid-handling robots, suggesting that a protocol written for one robot could be readily adapted to another. In practice, idiosyncratic proprietary interfaces prevent developers from creating protocols that are interoperable across robots. Without easy sharing and adaptation, researchers are forced to write programs in proprietary formats using a limited library of tools that they cannot modify or extend. Graphical interfaces also prevent developers from freely integrating abstractions, tools, and libraries that are typical in other areas of software development. Furthermore, because proprietary robot interfaces are typically not freely available to the public, there is little opportunity for newcomers to gain experience through educational, testing, or hobbyist usage. Each interface is an essentially unique and highly complex application that must be learned anew for each manufacturer, meaning proficiency does not readily translate across different robotic platforms. These factors sharply constrain the number of developers who can effectively program liquid-handling robots, resulting in an industry-wide personnel bottleneck for these roles. Some of the problems of proprietary software are mitigated by friendlier user-facing ‘‘application programming interfaces’’ (APIs) such as PyHamilton14 for Hamilton robots, the C# interface for Tecan Fluents, and the HTTP API for Opentrons. By decoupling the programming environment from the execution environment, APIs provide a useful layer of abstraction allowing for greater flexibility and the use of widely known programming languages. However, manufacturer-specific APIs still do not allow protocols and resources developed for one type of robot to be used on others. The issue of standardization to facilitate interoperability has yet to be adequately addressed by any existing interface. Several projects to create standardized lab automation interfaces have been created, such as SiLA,15 LabOp,16 Emerald Cloud Lab’s Symbolic Lab Language,17 and Puppeteer,18 but only the last of these supports command-level control of liquid-handling robots. See Table 1 for an aspect-by-aspect comparison.
Open-source applications outshine proprietary counterparts in their flexibility, accessibility, and compatibility with an extensive array of software development tools. Open source enables users to contribute changes that address their own context-specific needs and draw upon the work and troubleshooting advice of others who have already integrated debugging and testing utilities20 and artificial intelligence (AI) code assistants.9 This allows for continuous improvement with features sourced from the widest possible pool of developers. These advantages have resulted in essentially all of the most widely used software development tools being open source, notably NumPy,21 Jupyter Notebook,22 and PyTorch.23 Open-source software as such constitutes the foundation of modern software applications. An open-source interface for liquid-handling robots would dramatically improve protocol development efficiency and enable methods to be freely shared and reproduced across diverse operating system (OS) and hardware configurations. Here, we present PyLabRobot, an open-source Python framework that provides a maximally flexible and accessible environment for creatively programming liquid-handling robots and accessories (GitHub: https://github.com/PyLabRobot/ pylabrobot).
RESULTS
PyLabRobot is designed to make developing and sharing protocols for liquid-handling robots and their accessories straightforward and accessible to users with a variety of skill levels. The framework is built to run on Windows, macOS, Linux, and Raspberry Pi OS, allowing for accessibility to users of all major operating systems, and is organized into several subpackages for different hardware platforms and adjacent software (Table 2). PyLabRobot increases the accessibility of laboratory automation by using standardized interfaces that enable a hardware-agnostic programming environment (Figure 1).
Hardware-agnostic and interactive interface
Users begin programming a laboratory device by instantiating a class from the interface layer, such as LiquidHandler or PlateReader. Having the ability to control robots using atomic, low-level commands provides considerable power and flexibility compared with traditional protocol-level control. By
Table 1. PyLabRobot has several inherent advantages over similar projects
Project
Programmatic interface Open source
Interactive command-level control Supports any operating system Supports multiple robots
Hamilton VENUS X – – –
Tecan EVOware X – – –
Opentrons X X X –
PyHamilton19 X X X –
SiLA15 X – X –
LapOp16 X X – – X
Puppeteer8 X – – –
ECL17 X – – X X
PyLabRobot X X X X X
X’s are added for all aspects that, to the best of our knowledge, have been practically implemented for a project.
2 Device 1, 100111, October 20, 2023
Article
ll


executing commands in real time, PyLabRobot enables developers to receive immediate feedback, allowing for rapid debugging and iteration as well as optimization of spatial positioning, liquid-handling parameters, and other physical variables. This paradigm is particularly powerful in combination with interactive tools like REPLs (read-evaluate-print loops), IPython,24 and Jupyter Notebooks.22 Having the flexibility that is enabled by com
mand-level control is critical to researchers for them to implement highly specialized methods, potentially allowing entire experiments to be automated.
Deck layout and labware model
The user specifies their own unique configuration of labware on a robot deck with Resource, a class capable of capturing the attributes and methods defining most commonly used labware. Any configuration of labware on a robot deck can be represented as a set of instances of Resource and its subclasses and can be modified at runtime. Each instance is defined by its name attribute, which serves as a unique identifier in the deck representation that every protocol can rely upon. These names typically refer to function rather than exact labware, which allows for robot-agnostic protocols. For example, a protocol specifying aspiration from a resource named ‘‘bacteria lagoons’’ will be interpreted by referencing the deck layout to obtain the specific labware definition and location. Semantic relations between labware are stored in a directed, rooted tree (an arborescence), using the children and parent attributes of Resource, where the deck is the root of the tree (its parent is None). Spatial relations between resources are stored in the location attribute on Resource, which defines a resource’s location with respect to its immediate parent as a Cartesian coordinate. This allows locations to simultaneously be conceptualized as offsets. Absolute locations of resources are computed lazily by recursively adding a resource parent’s location until the deck (root) is reached (Figure 2). Key advantages of this approach include a straightforward implementation of moving resources (only the parent’s location has to be modified for all of its children to be likewise changed) and the ability to define resources (e.g., a plate with wells) without considering them in their broader context of a deck.
AB
Figure 1. PyLabRobot software architecture
(A) The operator typically interacts with the interface layer (yellow). An instance of the LiquidHandler class communicates with the robot using a backend from the execution layer (purple) specific to the hardware in use. In this example, the Tecan Freedom EVO backend is selected. Because the available hardware capabilities are conveyed to LiquidHandler by the execution layer, the user need only specify the configuration of the deck in order to translate methods developed for a different system to their own. (B) Additional hardware devices mounted on the deck or nearby, such as plate readers, can be simultaneously controlled using an equivalent architecture. Due to the open-source nature of PyLabRobot, the entire community can make use of a new hardware system as soon as one individual writes an appropriate backend.
Table 2. Package organization
Subpackage name Description
liquid_handling base classes and tools for communicating with liquidhandling robots and tracking robot state
liquid_handling. backends
backends for translating liquidhandling commands to robotspecific commands
liquid_handling. liquid_classes
default parameters for handling different types of liquids
plate_reading base classes and tools for working with plate readers
resources base classes and implementations for specifying labware attributes and methods and deck layouts
server HTTP server that receives and executes liquid-handling commands
utils generic high-level utilities
Implementations for specific categories of equipment (such as liquidhandling robots and plate readers) have their own module. The resources module provides a shared foundation for describing labware and deck layouts.
Device 1, 100111, October 20, 2023 3
Article
ll


Subclasses of Resource capture additional behavior and constraints of particular labware types. The following are the most important subclasses of Resource in PyLabRobot.
d Deck serves as the root of all resources in the deck layout arborescence described above. Exploiting the similarity between resource-to-resource relations, the Deck class is a subclass of Resource with a few minor modifications. First, it maintains a mapping of a resource’s name to a reference to thaft resource. This allows random access of resources in O(1), which is particularly useful when checking for naming collisions. The choice to only include this functionality in this subclass was made for space efficiency. Second, the deck calls a callback method on assignment of resources, so that LH can listen for changes in deck geometry and, if necessary, communicate those to a backend. Each robot implementation currently includes a subclass of Deck to define its unique deck geometry. The HamiltonDeck subclass additionally includes a method to load VENUS’s lay files into the PyLabRobot model. d Carrier is an abstract base class for tip rack and plate carriers. Both provide a fixed number of well-defined spots, each of which can accommodate at most 1 tip rack or plate, respectively. Carrier mirrors this constraint by overriding the assign_child_resource method to require one of these fixed spots and raising an error if the requested spot is already occupied.
d Container is an abstract base class (ABC) for resources that contain liquid and uses a volume tracker to keep track of the used and free volume. Subclasses include Trough and Well. Volume trackers will be explained in more detail later on. d ItemizedResource is a generic ABC for resources that contain children in a uniform grid configuration, most notably Plate and TipRack. It provides convenience methods for indexing these children using conventional alphanumeric notation (<row letter><column number>, e.g., ‘‘A1’’) and integer indices, as well as a method for traversing them. Plate and TipRack have associated types of Well and TipSpot, respectively.
The user can subclass Resource as well as the abovementioned subclasses to further encapsulate specific labware properties. For example, a user may subclass ItemizedResource with an associated subclass Container to represent a rack of vials. Each instance of Resource can serialize and deserialize itself and its children to and from JSON format using the serialize and deserialize methods, respectively. Serialization is the process of turning in-memory data into a format that allows for storing, transmitting, and sharing of data; deserialization is the loading of serialized data into memory. The recursive and flexible implementation means users and developers rarely have to write their own deserializers; custom resources can automatically be saved to disk as standalone objects as well as included in saved
A
C
B
Figure 2. The Resource model computing the absolute position of a well
(A) Visualization of the Resource model. The locations of wells are defined with respect to the bottom left of the plate. (B) The arborescence represents the computation of the location of resource A (well) in resource D (deck). The absolute location of the bottom left of the well is the sum of the location vectors between it and the deck. (C) An implementation of the algorithm for computing the location of a given instance of Resource.
4 Device 1, 100111, October 20, 2023
Article
ll


deck layout files. Thanks to JSON’s flexibility and versatility, saved resource definitions and labware configurations can be easily read by a wide range of external software.
Standardized operations
The four foundational liquid-handling operations (aspirate, dispense, tip pickup, and tip drop) form the foundation of the liquid_handling package and correspond to methods on LiquidHandler and LiquidHandlerBackend (pick_up_ tips, drop_tips, aspirate, dispense), as well as four data classes to transfer the data between them (Pickup, Drop, Aspiration, Dispense). These classes capture all commonly used liquid-handling parameters. All operations are parameterized by the Resource on which the operation is performed, an offset with respect to the default operation location, and the tip to be used. For aspirations and dispenses, additional parameters include liquid volume, liquid height with respect to the bottom of the well, type of liquid handled (water, ethanol, etc.), flow rate (pipetting speed), blowout air volume (to remove excess liquid after a dispense), and transport air volume (to ensure no droplets fall out of the tip). If the robot has multiple pipetting channels, one instance of such a class may be passed to a backend method per channel, as long as they are of the same type, with the expectation that the operations are executed simultaneously. Any parameters not part of this format will be passed onto the backend directly to ensure that the user can still use the high-level interface layer even if their robot exposes non-standard parameters. Some parameters need not be specified explicitly (i.e., they may be None), in which case a backend should choose the most appropriate values. Having command-level control offers several advantages. Firstly, it provides greater flexibility in creating protocols compared with the limited ‘‘transfer’’-level of control found in
other programs. This flexibility becomes crucial when dealing with multiple aspirations and dispenses or when precise timing is essential. Secondly, command-level control greatly simplifies the process of writing new robot backends. If many operations are carried out simultaneously on a single tip rack or microplate using a special pipetting head, such as the CoRe-96 head on Hamilton’s STAR, the -TipRack and -Plate variants of each of the methods and classes should be used (PickupTipRack, DropTipRack, AspirationPlate, DispensePlate). These variants differ in how they store tips—as a list rather than a single element, for example. In addition, a Move operation exists to capture the parameters of resource movement. Composition of the unit operations, such as the discard operation (drop tip in trash) and the transfer operations (combined aspirate and dispense), are performed at the LiquidHandler level and above (Table 3). The responsibilities of each backend are minimized to make adding new robot models as easy as possible (Figure 3).
Monitoring and parallelization
PyLabRobot uses ‘‘Tracker’’ objects to track and validate the physical state of the robot, including the presence of tips in a tip rack and liquids in wells and other liquid containers. This information is used to catch potential errors before executing operations on hardware, which can be costly, as well as to facilitate higher-level features like return_tips. Trackers use a transaction pattern when validating and saving operations. Before a command is sent to a machine, operations are validated against the queued and present state. For example, before aspirating, the system verifies that enough space will be available in the tip after all previously queued operations have been executed. If validation passes, the operation is added to the queue. Many
Table 3. Basic liquid-handling operations available through PyLabRobot
LH method Description Backend method(s)
pick_up_tips pick up tips from a tip rack pick_up_tips
drop_tips put tips back in a tip rack, reuse allowed drop_tips
discard_tips dispose of the tips, reuse not allowed drop_tips
return_tips return the mounted tips to where they were picked up drop_tips
aspirate aspirate from a container aspirate
dispense dispense to a container dispense
transfer transfer liquid from one container to another aspirate, dispense
pick_up_tips96 pick up 96 tips from a tip rack using a single head pick_up_tips96
drop_tips96 drop 96 tips to a tip rack with a single head, reuse allowed drop_tips96
discard_tips96 dispose of 96 tips to the trash location, reuse disallowed drop_tips96
return_tips96 return all 96 tips to the tip rack where they were picked up drop_tips96
aspirate96 aspirate from a container using 96 channels at once aspirate96
dispense96 dispense to a container using 96 channels at once dispense96
move_resource move a resource to a new location move_resource
move_plate move a plate to a new location move_resource
move_lid move a plate lid to a new location move_resource
Composite operations exist in the interface layer for reusability but are implemented on the backend as multiple fundamental operations to minimize the responsibility in backends, making adding new backends and devices easier.
Device 1, 100111, October 20, 2023 5
Article
ll


operations may be queued in this manner. After that, the operations in the queue are executed in order. If all operations execute successfully on the machine, the entire queue is either committed (the current state is updated to be the queued state); otherwise, changes are rolled back (the queued actions are deleted). Tip trackers track the presence of tips on the pipetting head and tip spots in a tip rack and can distinguish between fixed or disposable tips; volume trackers track the liquids in liquid containers such as wells and mounted tips. Executing steps of automation protocols typically takes a meaningful amount of time, during which other tasks can or must be executed.4,19 Using Python’s asyncio library makes it easy to compose protocols that run steps in parallel (Figure 4).
Simulator
To lower the barrier of entering the field of lab automation, as well as to more easily validate the correctness of the library and
methods, a browser-based simulator was created to allow people to use PyLabRobot without having to have any specialized hardware. This simulator is part of the open-source package and can be run locally. The simulator is controlled using the SimulatorBackend, a subclass of WebsocketBackend with additional support for simulator-specific functionality. For example, this backend provides methods for updating the ‘‘physical’’ state of the deck, like placing tips and liquids on the deck. The browser-based part of the simulator mirrors the robotagnostic resource model and is dynamically constructed and modified during a simulator run. This, combined with the fact that the backend passes along all information received by LiquidHandlerBackends, means that the simulator works with any robot for which a deck model exists in PyLabRobot. The only code a developer has to write to add a new robot to the simulator is to enforce machine-specific constraints,
Figure 3. Basic liquid-handling operations
(A) Schematic representation of an aspiration operation. The offset of the well is not pictured. (B) The method header for aspiration on LiquidHandler. Type annotations help programmers use the library. Optional values need not be specified, signifying that the backend should determine an appropriate default value. (C) Standard form operations can be serialized into and deserialized from JSON format to store or transfer them. (D) transfer is an example of a composite operation because it calls two commands: aspirate and dispense. serially_dilute is a higher-level composite operation that includes a loop to repeatedly call another composite operation. By defining composite operations in terms of low-level commands, PyLabRobot is maximally expressive and extensible.
6 Device 1, 100111, October 20, 2023
Article
ll


such as the specific configuration of pipetting channels (see Figure 5).
Graphical labware layout editor
A graphical labware layout editor was developed to make designing deck layouts faster and more accessible. The labware editor reuses the same UI components used in the simulator for maintainability and visual consistency. The editor can also be used to edit the initial state of a deck by editing the presence of tips in tip racks and liquids in wells and other liquid containers. After validating that the layout has no spatial conflicts, these data are saved to a layout and to a state JSON file on disk, both of which can be loaded into PyLabRobot.
Applications Demos
The PyLabRobot Art Studio (GitHub: https://github.com/ rickwierenga/pylabrobot-art-studio), an application that prints users’ 12 3 8 drawings using watercolor paint, demonstrates PyLabRobot’s ability to interactively execute complicated liquid-handling operations on an Opentrons. The demo includes a web server and custom UI. The demo reuses tips when possible, which can be thought of as a way to eliminate contamination. Both the integration with external libraries and the dynamic pattern of liquid handling would be (virtually) impossible to achieve with traditional software.
Figure 4. PyLabRobot example script
This will move 100 mL liquid from the first to the second column. The tips are returned to their pickup location. The refilling of the washer station, a STAR-specific operation, is done simultaneously. The program ends after the longest running task finishes.
The Game of Life demo (GitHub: https:// github.com/rickwierenga/plr-game-of-life) demonstrates the plate reader integration in PyLabRobot by running a Game of Life simulation,25 using wells as the exclusive memory medium by using crystal violet dye to indicate ‘‘living wells.’’
Labware position calibration, path teaching, and interactivity
A common challenge in creating custom deck layouts is calibrating positions of labware to a set of coordinates in 3D space. To alleviate this, we created a tool called PyLabRobot Resource Locator Program (PLR-RLP, GitHub: https://github.com/ PyLabRobot/resource-locator-program) that exploits PyLabRobot’s interactive control over a machine to move a pipetting tip to an arbitrary location and assign notyet-located labware at that location. In addition, this same program can be used to pick up and release resources at arbitrary locations and to design traversal paths for moving objects. The program can be controlled using a keyboard, a GUI, and a video game controller. LLM assistant
Programmatic robot interfaces are naturally conducive to integration with large language model (LLM) assistants. One common use of LLM coding assistants is to provide a natural language prompt for which the assistant writes code. This can enable users who are less skilled with programming, or even completely unskilled with Python, to work with liquid-handling robots.26 To provide a wider group of biologists with access to laboratory automation, OpenAI’s GPT-3.5 model was provided with examples of PyLabRobot code and then used to convert natural language prompts directly into usable robot code. Table 4 provides a number of prompts and outputs from the OpenAI GPT-3.5 model after being given examples of PyLabRobot code. A Jupyter notebook containing the example data can be found at GitHub: https:// github.com/stefangolas/PyLabRobot_LLM_Example.
DISCUSSION
As an open-source library capable of operating diverse liquidhandling robots and other laboratory hardware, PyLabRobot provides scientists with the ability to share protocols and benefit from one another’s work, improving efficiency and access. Furthermore, by providing uniform interfaces to different families of automation devices, PyLabRobot allows users to focus on hardware
Device 1, 100111, October 20, 2023 7
Article
ll


capabilities when buying new machines, in addition to making it easier to mix and match (custom) hardware for their specific use case. At the same time, developers are free to directly interact with lower-level abstractions. For example, a developer seeking to use capabilities not available in the standardized interface layer is free to bypass this layer and call methods on a backend directly. By allowing researchers to write protocols using Python, one of the most widely accessible programming languages, the library simultaneously lowers the barrier to entry for researchers who have less experience in writing software, allows experts to switch to a new hardware platform without learning a new interface and rewriting all of their protocols, and offers more freedom when developing new protocols. Python is distinctly advanta
geous for this context because it has an extremely large ecosystem of libraries for use cases that synergize with lab automation, particularly data analytics, bioinformatics, and machine learning.27 The flexibility of an open-source framework allows for easy integration of libraries, tools, and abstractions into developer workflows. Encapsulation of code into reusable abstractions is ubiquitous in software development but has only been minimally deployed within lab automation. Code reusability has benefits for developer productivity and experimental scale and reproducibility, and the open-source nature of PyLabRobot enables the nucleation of a developer ecosystem that facilitates maximum distribution of shared resources.
Table 4. Examples of natural language prompts to control PyLabRobot
Prompt Code output
Aspirate 20 mL from the first and last wells in column 2 asp_poss = [plate[8], plate[15]]
lh.aspirate([asp_poss], vols=[20]*2)
Pick up tips and aspirate 200 mL from column 1 and dispense 50 mL to columns 5, 6, and 7
tips_poss = [tip_0[i] for i in range(8)] lh.pick_up_tips(tips_poss) asp_poss = [plate[i] for i in range(8)] lh.aspirate(asp_poss, vols = [200]*8) disp_cols = [4,5,6] for col in disp_cols: disp_poss = [plate[idx] for idx in range(8*col,8*col+8)] lh.dispense(disp_poss, [50]*8)
Perform a serial dilution of 50 mL along the first column of plate_0 for i in range(7):
lh.pick_up_tips([tip_0[i]]) lh.aspirate([plate_0[i]], vols=[50]) lh.dispense([plate_0[i+1]], vols=[50], mix_cycles=[2], mix_volume=[25]) lh.drop_tips([tip_0[i]])
Aspirate from the first column of plate_0 and dispense 30 mL to each well in the bottom-left diagonal half of plate_1
asp_poss = [plate_0[i] for i in range(0,8)] lh.aspirate([asp_poss], vols = [240]*8) for i in range(0, 8): disp_poss = [plate_1[8*j+i] for j in range(0, i+1)] lh.dispense([disp_poss], [30]*len(disp_poss))
GPT-3.5 can generate PyLabRobot code to perform desired tasks. The modular structure and defined deck layouts of PyLabRobot improve reliability, while the simulator permits testing prior to robot use. By targeting the interface layer, this code works on all robots compatible with PyLabRobot.
AB
Figure 5. The simulator
(A) A Jupyter notebook that interactively uses PyLabRobot. (B) The simulator running in a web browser to visualize the resources during a run. Tip presence and volumes are visualized in the simulator. Parts of commands sent over a Websocket connection during execution of each cell are visualized; command responses are not visualized.
8 Device 1, 100111, October 20, 2023
Article
ll


The advent of LLMs solidifies the benefits of a universal programmatic interface to liquid-handling robots. These models are capable of translating natural language prompts into Python code, allowing experimentalists with minimal programming experience to automate protocols. LLM agents can design and execute experiments on robots by parsing scientific literature.26 The modular structure of PyLabRobot enables such an agent to autonomously perform experiments on a range of liquid-handling robots with maximum flexibility and interoperability. Already compatible with Hamilton, Tecan, and Opentrons liquid-handling robots and BMG plate readers, PyLabRobot can readily be extended to interface with other liquid-handling robots (including open-source models such as the EvoBot28) and lab automation equipment, enabling them to be run from any OS and interact with a huge computing ecosystem. As additional hardware and protocols are added to the repertoire, labs will obtain greater benefit from using PyLabRobot, incentivizing manufacturers to provide PyLabRobot-compatible drivers for their equipment. We hope all laboratory automation equipment will eventually be operable using a highly flexible and OS-agnostic interface, enabling all users to benefit from a massive library of shared protocols that can readily be adapted for any purpose.
EXPERIMENTAL PROCEDURES
Resource availability Lead contact
Further information and requests for resources should be directed to Kevin Esvelt (esvelt@mit.edu). Materials availability
This study did not generate any new materials. Data and code availability
The code produced at the time of writing is available at GitHub: https://doi.org/ 10.5281/zenodo.8362842. The development of this library is an ongoing community effort, and we recommend accessing the newest version of the library at GitHub: https://github.com/PyLabRobot/pylabrobot.
Software development best practices
PyLabRobot, as a foundation for higher-level libraries and applications, must be stable. To ensure quality across the board, several software development best practices are used. The library makes use of automated systems running on GitHub Actions and on developers’ machines. Releases of the library are automatically pushed to the Python Package Index (PyPI) so that they may easily be installed by the user. Static code analysis
Mypy29 is used to enforce static typing rules, as a way to mitigate some of the downsides of Python’s dynamic typing system as well as provide the user with additional usage information. PyLint30 is used to statically analyze code for errors and bad practices and to ensure consistent code style, which is particularly helpful as the community of contributors to the project grows. Automated testing
Each commit must pass a battery of tests before it is merged into the central repository. Tests are executed using Pytest.20 At the execution layer, unit tests are used to ensure that user input produces consistent machine-level commands and, if possible, that they are transmitted correctly. This ensures that, as long as the interface to external software is consistent, PyLabRobot functions correctly. All tests can be run without requiring access to any specialized hardware. Documentation
Documentation (available at https://docs.pylabrobot.org) is generated using Sphinx,31 one of the most popular tools to generate documentation from Python docstrings. Pylint is set up to force each public class and all methods and func
tions to have a docstring, thereby making sure the entire library is well documented. This has the additional benefit of keeping code and documentation close in the codebase. The autodoc extension is used to automatically and recursively generate documentation for various modules and submodules. Using MySTNB,32 integrated tutorials can be written in an interactive format (Jupyter Notebook22), allowing the end user to easily run the provided examples in their own laboratory.
Code simulation
Traditionally, all development for liquid-handling robots required ownership of a physical machine, which hindered learners and development tremendously. It is still true that some facets of development will require physical access to a robot, which will be mitigated by placing trust on authorities such as manufacturers and through peer review. The simulator is a powerful tool that aids development without access to specialized hardware. ABCs
PyLabRobot provides a number of classes that define the general behavior of concepts such as backends, robot decks, or deck resources through ABCs. Classes that define specific implementations of one of these abstractions are defined as subclasses of the corresponding ABC. Defining classes to represent abstractions of each concept enables functionality to be generalized and enforced across each of the particular subclasses. This enforces standardization in how diverse instruments and systems are implemented so that developers can expect predictable behavior from PyLabRobot resources (such as robot backends), even for future integrations. The standard may be updated to accommodate future developments in lab automation. Error handling
PyLabRobot draws upon Python’s exception handling capabilities to provide a familiar and proven way of handling errors. Both the interface layer and backends may generate and raise errors, which can be ‘‘caught’’ (handled) by the user at any point in the call stack; uncaught errors result in program termination. Trackers allow the interface layer to anticipate errors (as described in monitoring and parallelization), which are raised before a command is submitted for execution to the backend. Errors that may be raised by PyLabRobot are listed in Table 5.
Open-source community Open-source community
Users are able to make changes to their local copy of the package to accommodate their own automation equipment or make updates to existing code and are encouraged to merge these changes back into the main branch of the project for distribution to the wider community using pull requests. Contributions will be merged by the project maintainers after a code review to ensure compliance with PyLabRobot standards and best software development practices. The process of downloading PyLabRobot for development and making changes that will be available to the wider community entails the use of the version-control tool git. Git enables online-hosted codebases to be copied into one’s local file system and modified while maintaining a record of the origin and any subsequent changes. The changes may then be retained in a separate branch indefinitely or merged back into the original branch. Git provides the ability to merge codebases with a shared origin and resolve conflicting code changes where necessary. Forum
The greatest benefits of open-source software require a flourishing community to share code and assist one another with problem-solving and troubleshooting. We consequently built and now host an active forum to promote knowledge sharing in lab automation (https://forums.pylabrobot.org). Described by one user as a ‘‘huge improvement over the popular private channels of communication,’’ it has grown to feature 20+ posts per day on a wide variety of laboratory automation topics.
Labware libraries
Labware definitions taken from Hamilton, Tecan, and Opentrons software have been translated into the hardware-agnostic labware model described in the results. Hardware agnosticity has been verified by using resources taken from the Hamilton labware library on an Opentrons robot and vice versa. Traditionally, the user would have been required to manually copy information from
Device 1, 100111, October 20, 2023 9
Article
ll


one program to the other, provided that this information is even accessible and that the second program allows the creation of custom resources, assumptions that are not always guaranteed. This library of hardware-agnostic labware definitions could serve as the basis for an online universal labware database that would facilitate interoperability across robot platforms.
Web connectivity
Web-based protocols provide a powerful, versatile, and extendible interoperability layer for communicating between different programs and computers. Included in PyLabRobot is an application-level protocol for interfacing with liquid-handling robots and plate readers, as well as a client and server implementation. The SerializingBackend is available as a transmission-layer neutral encoder. The two web protocols supported by PyLabRobot are HTTP and Websockets,33 for which transmission is implemented by the WebsocketBackend and HTTPBackendServer backends. An HTTP server is provided that decodes the data and sends them to an instance of LiquidHan
dler. It must be explicit that this protocol can be implemented by any program, meaning PyLabRobot may run just on the server or the client side, or both, or nowhere.
Backends
Backends constitute the execution layer of PyLabRobot and are OS-agnostic software objects that instruct robots to execute certain operations, possibly by directly sending instructions to the machine in the form of firmware instructions or HTTP requests. Because the responsibilities of a backend in PyLabRobot are limited to the minimal set of hardware instructions, developing a backend for a new robot is a well-defined process that can be completed without making changes to the broader ecosystem. In essence, the developer has to write code that takes as input the standardized operations, executes these operations on their machine, and reports any errors that may have occurred. Learning how to send specific hardware instructions typically involves executing protocols through an existing interface, intercepting data sent to the robot (e.g., with Wireshark or by looking at firmware logs generated by the manufacturer’s application), and analyzing these data. Manufacturer documentation should be used where available to assist with this analysis. The developer should now be able to implement the functions laid out in the backend ABC for a particular device. This comparatively low-effort system of integrating new machines into a well-tested ecosystem with an existing interface layer benefits developers because it allows them to focus on specific hardware and eliminates any duplicated work. Further, integrations shared with the PyLabRobot community will be maintained at no cost to the original developer while providing the community with more powerful tools, thus providing strong incentives for collaborative efforts to improve the PyLabRobot framework. Hamilton STAR and STARlet
The STAR backend (the STAR class) provides an OS-agnostic interface to the Hamilton STAR and STARlet robots that has been verified to work with Windows, macOS, and Raspberry Pi OS. The backend communicates directly with the robot’s firmware over a USB connection. Firmware commands sent by the STAR backend are based on those generated by Hamilton’s Venus application and by documentation provided in Hamilton reference manuals. The PyLabRobot STAR interface works with multiple USB drivers thanks to PyUSB.34 During testing, the libusbK driver was used on Windows, libUSB on macOS, and the driver provided by the OS on Raspberry Pi OS (Debian Linux). This creates a communication channel to the robot that is completely open source.
Hamilton Vantage
The Vantage backend (the Vantage class) provides an OS-agnostic interface to the Hamilton Vantage. It is based on commands sent and logs generated by Venus on Vantage, the STAR backend, and documentation available through the TCP interface. This backend uses PyUSB to interface with the machine’s USB interface.
Tecan Freedom EVO
The EVO backend (the EVO class) provides an OS-agnostic interface to the Tecan Freedom EVO and has been validated to work on Windows and macOS. Analogous to STAR, EVO uses firmware command strings based on those generated by the EVOWare application and documented in the manufacturer’s reference manuals and sends them to the machine using PyUSB. Opentrons OT-2
The Opentrons backend (the OpentronsBackend class) provides a PyLabRobot backend to the Opentrons OT-2. It sends commands using the Opentrons HTTP API, for which a Python wrapper was written (GitHub: https:// github.com/rickwierenga/opentrons-python-api). The server serving these requests runs on the onboard Raspberry Pi and is written by the Opentrons company and open-source community. PyLabRobot can either run on the onboard computer or an external computer. This provides an advantage over the usual mode of operation where protocols are stored on device, potentially making having a single source of truth the user’s concern, limiting the ecosystem a protocol may interact with, and typically forcing the user to run entire protocols at once rather than interactively. Since the Opentrons API currently has to maintain its own deck model, PyLabRobot’s deck model is mirrored in the background using the
Table 5. An overview of the errors that can be raised by PyLabRobot
Error Cause(s)
ResourceNotFoundError a particular resource was expected to exist but could not be found
TooLittleLiquidError raised by the volume tracker or backend when d more liquid is requested to be aspirated than exists in a well d more liquid is requested to be dispensed than exists in a tip
TooLittleVolumeError raised by the volume tracker or backend when d aspirating would exceed tip capacity d dispensing would exceed container capacity
HasTipError raised by the volume tracker or backend when d a tip is already mounted on a channel during tip pickup d a tip is already present in a tip rack during tip drop
NoTipError raised by the volume tracker or backend when d no tip is present in a tip rack during tip pickup d no tip is mounted on a channel during tip drop
NoChannelError no suitable channel is available for liquid handling
HamiltonError device-specific errors raised by a Hamilton device
TecanError device-specific errors raised by a Tecan device
NoPlateError a plate is requested from a plate reader, but no plate is present
UnknownResourceType raised when attempting to load a resource of an unknown type
Errors are raised using Python’s error mechanisms and may be handled by the user at any point in the call stack; unhandled errors cause program termination.
10 Device 1, 100111, October 20, 2023
Article
ll


assigned_resource_callback and unassigned_resource_callback callback methods. ClarioSTAR
The ClarioSTAR backend (the ClarioSTAR class) provides an OSagnostic interface to the ClarioSTAR plate reader. It uses the FTDI USB to RS-232 protocol to send instructions to the machine. This backend is based on commands sent by the ClarioSTAR Control software. Pylibftdi35 is used as a Python frontend to libftdi, the library used to communicate with the machine.
ACKNOWLEDGMENTS
The authors would like to thank Dana Gretton, Emma Chory, Jon Bloom, Alvaro Cuevas, Eric Sindelar, Ben Ray, Priyanka Raghavan, and Wenhao Gao for constructive feedback. We would also like to thank Ben Gregor, Eyal Perry, David Kong, Priyanka Raghavan, Wenhao Gao, and Christian Ulmer for assistance with procuring documentation and hardware vital to the success of this project. We are deeply grateful for support from Reid Hoffman, the Open Philanthropy Project, the National Institutes of Health (grants no. R21AI158169 and DP2AI136597), and the MIT Media Lab.
AUTHOR CONTRIBUTIONS
R.P.W. and S.M.G. conceived of the idea. R.P.W. and W.H. developed the PyLabRobot software library with advice from S.M.G. and K.M.E. R.P.W. and S.M.G. validated the software and developed the applications. R.P.W., S.M.G., C.W.C., and K.M.E. procured the devices and materials. R.P.W., S.M.G., and K.M.E. wrote the paper with input from all authors. K.M.E. procured funding.
DECLARATION OF INTERESTS
The authors declare no competing interests.
Received: July 9, 2023 Revised: August 22, 2023 Accepted: September 20, 2023 Published: October 20, 2023
REFERENCES
1. Coston, M.E., Gregor, B.W., Arakaki, J., Borensztejn, A., Do, T.P., Fuqua, M.A., Haupt, A., Hendershott, M.C., Leung, W., Mueller, I.A., et al. (2020). Automated hiPSC culture and sample preparation for 3D live cell microscopy. Preprint at bioRxiv. https://doi.org/10.1101/2020.12.18.423371.
2. Brandenberg, N., Hoehnel, S., Kuttler, F., Homicsko, K., Ceroni, C., Ringel, T., Gjorevski, N., Schwank, G., Coukos, G., Turcatti, G., and Lutolf, M.P. (2020). High-throughput automated organoid culture via stem-cell aggregation in microcavity arrays. Nat. Biomed. Eng. 4, 863–874.
3. Eggert, S., Kahl, M., Bock, N., Meinert, C., Friedrich, O., and Hutmacher, D.W. (2021). An open-source technology platform to increase reproducibility and enable high-throughput production of tailorable gelatin methacryloyl (GelMA) - based hydrogels. Mater. Des. 204, 109619.
4. DeBenedictis, E.A., Chory, E.J., Gretton, D.W., Wang, B., Golas, S., and Esvelt, K.M. (2022). Systematic molecular evolution enables robust biomolecule discovery. Nat. Methods 19, 55–64.
5. Chory, E.J., Wang, M., Ceribelli, M., Michalowska, A.M., Golas, S., Beck, E., Klumpp-Thomas, C., Chen, L., McKnight, C., Itkin, Z., et al. (2023). High-throughput approaches to uncover synergistic drug combinations in leukemia. SLAS Discov. 28, 193–201. https://doi.org/10.1016/j.slasd. 2023.04.004.
6. Billeci, K., Suh, C., Di Ioia, T., Singh, L., Abraham, R., Baldwin, A., and Monteclaro, S. (2016). Implementation of an Automated High-Throughput Plasmid DNA Production Pipeline. J. Lab. Autom. 21, 765–778.
7. Ortiz, L., Pavan, M., McCarthy, L., Timmons, J., and Densmore, D.M. (2017). Automated Robotic Liquid Handling Assembly of Modular DNA Devices. J. Vis. Exp., e54703. https://doi.org/10.3791/54703.
8. Walsh, D.I., 3rd, Pavan, M., Ortiz, L., Wick, S., Bobrow, J., Guido, N.J., Leinicke, S., Fu, D., Pandit, S., Qin, L., et al. (2019). Standardizing Automated DNA Assembly: Best Practices, Metrics, and Protocols Using Robots. SLAS Technol. 24, 282–290.
9. GitHub Copilot. https://copilot.github.com/.
10. Higgins, K., Valleti, S.M., Ziatdinov, M., Kalinin, S.V., and Ahmadi, M. (2020). Chemical Robotics Enabled Exploration of Stability in Multicomponent Lead Halide Perovskites via Machine Learning. ACS Energy Lett. 5, 3426–3436.
11. Ahmadi, M., Ziatdinov, M., Zhou, Y., Lass, E.A., and Kalinin, S.V. (2021). Machine learning for high-throughput experimental exploration of metal halide perovskites. Joule 5, 2797–2822.
12. Higgins, K., Ziatdinov, M., Kalinin, S.V., and Ahmadi, M. (2021). HighThroughput Study of Antisolvents on the Stability of Multicomponent Metal Halide Perovskites through Robotics-Based Synthesis and Machine Learning Approaches. J. Am. Chem. Soc. 143, 19945–19955.
13. Tamasi, M.J., Patel, R.A., Borca, C.H., Kosuri, S., Mugnier, H., Upadhya, R., Murthy, N.S., Webb, M.A., and Gormley, A.J. (2022). Machine Learning on a Robotic Platform for the Design of Polymer-Protein Hybrids. Adv. Mater. 34, e2201809.
14. Chory, E.J., Gretton, D.W., DeBenedictis, E.A., and Esvelt, K.M. (2021). Enabling high-throughput biology with flexible open-source automation. Mol. Syst. Biol. 17, e9942.
15. Ba ̈ r, H., Hochstrasser, R., and Papenfuß, B. (2012). SiLA: Basic standards for rapid integration in laboratory automation. J. Lab. Autom. 17, 86–95.
16. Bryce, D.. The laboratory open protocol language (LabOP). https:// bioprotocols.github.io/labop/about.
17. Emerald Cloud Lab: Remote Controlled Life Sciences Lab https://www. emeraldcloudlab.com/.
18. Vasilev, V., Liu, C., Haddock, T., Bhatia, S., Adler, A., Yaman, F., Beal, J., Babb, J., Weiss, R., and Densmore, D.. A software stack for specification and robotic execution of protocols for synthetic biological engineering. https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=779b0 e9a23a77c496483223307f86c5cfb11dd48.
19. Chory, E.J., Gretton, D.W., DeBenedictis, E.A., and Esvelt, K.M. (2020). Flexible open-source automation for robotic bioengineering. Preprint at bioRxiv. https://doi.org/10.1101/2020.04.14.041368.
20. Krekel, H., Oliveira, B., Pfannschmidt, R., Bruynooghe, F., Laugher, B., and Bruhin, F.. Pytest. https://github.com/pytest-dev/pytest/.
21. Harris, C.R., Millman, K.J., van der Walt, S.J., Gommers, R., Virtanen, P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N.J., et al. (2020). Array programming with NumPy. Nature 585, 357–362.
22. Loizides, F., and Schmidt, B. (2016). Positioning and Power in Academic Publishing: Players, Agents and Agendas: Proceedings of the 20th International Conference on Electronic Publishing (IOS Press).
23. Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., Killeen, T., Lin, Z., Gimelshein, N., Antiga, L., et al. (2019). Pytorch: An imperative style, high-performance deep learning library. Adv. Neural Inf. Process. Syst. 32.
24. Perez, F., and Granger, B.E. (2007). IPython: A System for Interactive Scientific Computing. Comput. Sci. Eng. 9, 21–29.
25. Gardner, M. (1970). The fantastic combinations of John conway’s new solitaire game ’life. Sci. Am. 223, 20–123.
26. Boiko, D.A., MacKnight, R., and Gomes, G. (2023). Emergent autonomous scientific research capabilities of large language models. Preprint at arXiv. https://doi.org/10.48550/arXiv.2304.05332.
27. Pe ́ rez, F., Granger, B.E., and Hunter, J.D. (2011). Python: An Ecosystem for Scientific Computing. Comput. Sci. Eng. 13, 13–21.
Device 1, 100111, October 20, 2023 11
Article
ll


28. Fain ̃ a, A., Nejati, B., and Stoy, K. (2020). EvoBot: An Open-Source, Modular, Liquid Handling Robot for Scientific Experiments. Appl. Sci. 10, 814.
29. Mypy Contributors. Mypy. https://github.com/python/mypy.
30. Pylint Contributors. Pylint. https://github.com/pylint-dev/pylint.
31. Sphinx contributors: The Sphinx documentation generator. https://github. com/sphinx-doc/sphinx.
32. MyST-NB Contributors. MyST-NB. https://github.com/executablebooks/ MyST-NB.
33. Melnikov, A., and Fette, I. The Websocket Protocol. RFC 6455.
34. PyUSB Contributors. PyUSB. https://github.com/pyusb/pyusb.
35. Pylibftdi Contributors. Pylibftdi. https://github.com/codedstructure/pylibftdi.
12 Device 1, 100111, October 20, 2023
Article
ll
