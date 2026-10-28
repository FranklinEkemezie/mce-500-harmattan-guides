# MCE 517 — Computer Aided Manufacturing

*2 Units · 500 Level, Harmattan · BMAS analogue: MCT 403 · FUTO Mechatronics*

## Overview

CAM is manufacturing run by computer: the design data becomes a numerical-control program, the program drives the machine, and the whole factory is linked into one information system. The course covers NC/CNC hardware and programming, computer-integrated manufacturing, and rapid prototyping.

Paper: 2 hours, **answer any four questions, at least one from each section**. Sections separate manufacturing/NC from CIM/CAD-CAM. Two papers are available (2020/2021, 2021/2022).

**Note on scope:** BMAS MCT 403 describes CAM as "advanced technologies… rapid product development… Design For Manufacture". The FUTO paper is more conventional: NC, CNC, DNC, CIM, 3D printing, CAD/CAM software. The papers define the taught scope.

## Synopsis (BMAS MCT 403, verbatim)

> "In-depth study of some advanced technologies adopted by leading design and manufacturing industries worldwide. Exploring rapid product development and technologies aimed at reducing product development lead-time within a Design For Manufacture (DFM) context."

## Sources

- **_MCE 517 – Computer Aided Manufacturing_** (17 pp.) — §1 what CAM is (pp. 2–3); §2 CNC applications and machine types (pp. 3–9); §3 operation of CNC machines (pp. 10–14); §4 application software (pp. 15–16); §5 safety (pp. 16–17).
- **_CADCAMLAB_** (66k characters) — CAD experiments 1–9 (pp. 3–44) and CAM experiments 1–4 (pp. 45–60): AutoCAD part programming, APT 2-D contour, CNC machining.
- **_02-3DPrinting_** (Coros slides) — additive vs subtractive, FDM/SLA/SLS, support and resolution issues.
- **_Numerical Control_** — scanned notes; use for the NC procedure and coordinate systems, not as your main text.
- **Past papers:** 2020/2021 and 2021/2022. Question numbers below refer to these.
- **Gap:** no taught chapter on CIM or DFM; CIM comes from the class diagram, DFM from general manufacturing knowledge.

- **Not included:** textbooks and lecturer notes are not redistributed here; see [\docs/sources.md\](../docs/sources.md).

## Course Content Summary

| Concept | Importance | Exam likelihood |
|---|---|---|
| Manufacturing systems and CAM | Essential | High (2/2) |
| NC principles and components | Essential | **Very high** (2/2) |
| NC motion control and coordinates | Essential | **Very high** (2/2) |
| NC part programming (G/M codes) | Essential | High (1/2) |
| CNC, DNC and adaptive control | Essential | High (2/2) |
| CNC block diagram and merits | Essential | High (2/2) |
| CIM and factory automation | Essential | High (2/2) |
| Rapid prototyping and 3D printing | Essential | **Very high** (2/2) |
| CAD/CAM software and transforms | Important | High (1/2) |
| Advanced processes (laser, EDM, EBM) | Important | High (2/2) |
| Design for manufacture | Supporting | Low |

## Course Content Details

### 1. Manufacturing systems and CAM

CAM is the use of computers to plan, manage and control manufacturing. It sits between CAD and the physical machine.

**Study:** CAM book §1 (pp. 2–3) and §2 (pp. 3–9); class notes.
**Exam:** 2020/21 Sec A Q1(a).

- [ ] **Manufacturing types** — job shop, batch, mass, continuous; volume–variety relationship.
- [ ] **Automation levels** — manual, mechanised, semi-automatic, automatic, computer-integrated.
- [ ] **CAM functions** — process planning, NC programming, scheduling, quality control, inventory, maintenance.
- [ ] **CAD/CAM/CAE** — design, analysis, manufacturing data flow; the product model as the single source.
- [ ] **Benefits and costs** — lead time, flexibility, quality, labour; capital, skills, integration cost.

### 2. Numerical control: principles and components

NC is control by numbers: a program of coordinates and functions drives the machine tool.

**Study:** CAM book §2–3 (pp. 3–14); _Numerical Control_ scan; CADCAMLAB CAM experiment 4 (pp. 57–60).
**Exam:** 2020/21 Sec A Q2(a)–(c); 2021/22 Q5(c).

- [ ] **NC definition** — program, machine control unit, machine tool, feedback; open-loop vs closed-loop.
- [ ] **Components** — tape/program input, MCU, interpolator, servo drives, feedback (encoder/resolver), machine tool.
- [ ] **NC vs conventional** — repeatability, complex geometry, setup time, capital, skill.
- [ ] **Advantages and disadvantages** — five advantages and three disadvantages (a recurring 5-mark question).
- [ ] **NC procedure** — part drawing → process planning → tool selection → program → verification → machining.
- [ ] **Coordinate systems** — machine zero, workpiece zero, fixed vs floating zero; absolute vs incremental positioning.

### 3. Motion control and interpolation

The controller must turn a block of coordinates into a smooth path. The three motion types are examinable with diagrams.

**Study:** CAM book §3 (pp. 10–14); CADCAMLAB CAM experiments 3–4 (APT 2-D contour and machining, pp. 48–60).
**Exam:** 2020/21 Sec A Q3(a); 2021/22 Q3(b).

- [ ] **Point-to-point** — no controlled path, drilling/spotting; sketch.
- [ ] **Straight-cut** — axis-parallel milling; sketch.
- [ ] **Contouring/continuous path** — simultaneous axes, interpolation; sketch.
- [ ] **Interpolation** — linear, circular, helical; how the interpolator generates intermediate points.
- [ ] **Feed and speed** — feed rate, spindle speed, cutting speed, depth of cut; units and G-codes.
- [ ] **Accuracy** — resolution, backlash, leadscrew error, thermal distortion; closed-loop correction.

### 4. NC part programming

A part program is a sequence of blocks. Each block has a sequence number, words and a end-of-block character.

**Study:** CADCAMLAB pp. 45–60 (APT part programming and machining); CAM book §4 (software, pp. 15–16).
**Exam:** 2020/21 Sec A Q3(b).

- [ ] **Block format** — N, G, M, X/Y/Z, F, S, T; word address format; example block explained.
- [ ] **G-codes** — G00 rapid, G01 linear, G02/G03 circular, G17/18/19 planes, G90/G91 absolute/incremental, G20/G21 units.
- [ ] **M-codes** — M03/M04 spindle on, M05 stop, M06 tool change, M08/M09 coolant, M30 end.
- [ ] **Canned cycles** — drilling, tapping, boring; why they save blocks.
- [ ] **Programming methods** — manual, conversational, CAM-generated; verify by simulation before cutting.
- [ ] **Worked example** — write a simple contour program for a rectangular pocket with a tool change.

### 5. CNC, DNC and adaptive control

CNC puts a computer in the controller; DNC puts a computer above many machines; adaptive control changes feeds in real time.

**Study:** CAM book §1(a)–(b) and §2 (CNC merits and restrictions, DNC); class notes.
**Exam:** 2020/21 Sec A Q1(c), Q3(c); 2021/22 Q1 (DNC), Q4.

- [ ] **CNC architecture** — CPU, memory, interpolator, PLC, servo interface, operator panel; block diagram.
- [ ] **CNC vs NC** — software flexibility, storage, compensation, diagnostics, communication.
- [ ] **DNC** — behind-the-reader vs direct numerical control; distributing programs, collecting data.
- [ ] **Adaptive control** — sensors (force, torque, temperature), constraints, optimisation; AC vs ACO.
- [ ] **Merits** — productivity, accuracy, flexibility, unmanned operation; limitations (cost, maintenance, programming).

### 6. Computer-integrated manufacturing

CIM integrates design, planning, production and business into one system. It is an architecture, not a single machine.

**Study:** class notes (CIM definition, components, hierarchy); CAM book §1–2 for the automation background. There is no dedicated chapter — use the lecture diagram.
**Exam:** 2020/21 Sec B Q4(c); 2021/22 Q3(a).

- [ ] **CIM definition** — integration of CAD, CAM, CAP, MRP, business systems; data consistency.
- [ ] **Components** — CAD, CAM, CAPP, FMS, robotics, AS/RS, inspection, networks, databases.
- [ ] **FMS** — flexible manufacturing system, cells, pallets, tool management; when it pays.
- [ ] **Information flow** — order → design → process plan → schedule → machine → inspection → dispatch.
- [ ] **Benefits and barriers** — reduced lead time, quality; cost, standards, skills, change management.

### 7. Rapid prototyping and 3D printing

Additive manufacturing builds a part layer by layer. It is the fastest route from CAD to a physical prototype.

**Study:** _02-3DPrinting_ slides (pp. 1–25: additive vs subtractive, FDM, SLA, SLS, design issues).
**Exam:** 2020/21 Sec A Q1(b); 2021/22 Q1.

- [ ] **Principle** — CAD model → STL → slicing → layer deposition → post-processing.
- [ ] **FDM** — filament, heated nozzle, layer adhesion; materials ABS, PLA, PETG; advantages and limitations.
- [ ] **SLA/DLP** — photopolymer resin, laser/LCD, resolution, post-cure.
- [ ] **SLS** — powder bed, laser sintering, unsintered powder support; materials nylon, metal.
- [ ] **Other processes** — LOM, binder jetting, material jetting, DED; compare speed, cost, accuracy, material.
- [ ] **Applications** — prototyping, tooling, spare parts, medical implants; DFM rules for additive.

### 8. CAD/CAM software and geometric transformation

CAM software takes a geometric model and produces toolpaths. The mathematics is transformation of coordinates.

**Study:** CADCAMLAB CAD experiments 1–9 (pp. 3–44) — primitives, layers, isometric/orthographic, 3-D viewing; CAM book §4.
**Exam:** 2020/21 Sec B Q1(a)–(c), Q2; 2021/22 Q6(a)–(d).

- [ ] **Modelling** — wireframe, surface, solid; parametric and feature-based modelling.
- [ ] **Transformations** — translation, scaling, rotation, reflection, shear; homogeneous $4\times4$ matrix.
- [ ] **Worked transform** — rotate a point $45^\circ$ about the origin, then translate by $(10,5)$; give the matrix.
- [ ] **Toolpath generation** — roughing, finishing, tool selection, stepover, gouge avoidance.
- [ ] **Simulation and post-processing** — verify, then post-process to a machine-specific G-code dialect.

### 9. Advanced processes and DFM

Modern CAM includes non-traditional processes and design rules that make manufacture cheap.

**Study:** CAM book §2(d)(v) and (viii)–(xi) (turret press, EDM, EBM, laser, CMM, pp. 7–9); CADCAMLAB.
**Exam:** 2020/21 Sec A Q4(b); 2021/22 Q5(a).

- [ ] **Laser cutting** — beam, kerf, heat-affected zone; speed vs thickness.
- [ ] **EDM** — wire and die-sinking; conductive materials, electrode wear, surface finish.
- [ ] **EBM** — electron beam in vacuum; welding, drilling, additive.
- [ ] **CMM** — coordinate measuring machine, probe, tolerance verification; reverse engineering.
- [ ] **Turret press** — punching, nibbling, tool turret; nesting and material utilisation.
- [ ] **DFM rules** — minimise parts, standardise, design for the process, tolerances, assembly; cost drivers.

## How to use this

Each topic has a **Study** line, an **Exam** line and a checklist. The paper is descriptive plus one transformation calculation: memorise the definitions and lists, and practise the 2-D/3-D rotation questions until they are mechanical. Tick a box when you can write the answer without notes.

**Refresh before starting (no new textbook):** coordinate geometry — 2-D rotation about the origin and about an arbitrary point, 3-D rotation matrices, homogeneous coordinates; basic machining — turning, milling, drilling, and what a turret press does.

**Priority:** NC components and procedure, CNC/DNC/adaptive differences, 3-D printing, CIM, and the transformation question are all near-certain. Advanced processes (EBM, EDM, laser, CMM) are one short question — learn one line each.
