# MCE 511 — Process Automation Management

*3 Units · 500 Level, Harmattan · BMAS analogue: MCT 511 · FUTO Mechatronics*

## Overview

This course is about running an automated plant, not just wiring one. It covers the technology — PLCs, DCS, field networks, fire-and-gas systems, motor starters — and the management layer above it: maintenance, reliability, safety, KPIs, outsourcing and return on investment. Exam questions regularly cross the boundary, e.g., "explain predictive maintenance, then compute availability from MTBF and MTTR".

The paper mixes definitions, comparisons, block diagrams, short calculations and one management case. Three papers are available (2019/2020, 2020/2021, 2021/2022).

**Note on scope:** BMAS MCT 511 is a 2-unit PLC/closed-loop laboratory. FUTO's MCE 511 is a 3-unit management-oriented course; the papers, not the BMAS paragraph, define what is taught.

## Synopsis (BMAS MCT 511, verbatim)

> "PLC programming higher functions - PLC-programming analogue in/outputs - 2-step controller - Basics in closed loop control - Closed loop temperature control - Closed loop pressure control - Closed loop flow control - Closed loop level control. Laboratory"

## Sources

- **Mehta & Reddy, _Industrial Process Automation Systems_** (Drive folder PDF) — the backbone. Ch. 1 industrial automation (§1.1–1.13); Ch. 2 PLC (§2.1–2.8); Ch. 3 DCS (§3.1–3.8); Ch. 5 functional safety and SIS; Ch. 6 fire and gas (§6.1–6.7); Ch. 7 SCADA; Ch. 8 PAC; Ch. 9 serial/Modbus; Ch. 10 networks and OSI; Ch. 11–13 HART, PROFIBUS, Foundation Fieldbus; Ch. 14 wireless; Ch. 16 asset management; Ch. 18 system maintenance; Ch. 19 advanced control; Ch. 21 alarms; Ch. 23 MES.
- **Lecturer notes (Drive folder):** _MCE 511 Material_ = Mehta Ch. 6 (F&G); _Plant Maintenance_ (lecturer slides); _Electrical Safety_ (lecturer slides); _Note on Wireless Communication_ (Nevo Networks workshop); _Note 26 Aug 2021_.
- **Past papers:** 2019/2020, 2020/2021, 2021/2022, plus the lecturer's exam AOC 2019–2021. Question numbers below refer to the papers.
- **Online:** [RealPars articles](https://www.realpars.com/blog/) — search "PLC latching", "sinking and sourcing", "PROFIBUS", "SCADA", "motor starter" for one-page explanations that match the questions.
- **Gap:** ERP/PPC and linear programming appear only in the past papers; those parts are marked as inference.

- **Not included:** textbooks and lecturer notes are not redistributed here; see [\docs/sources.md\](../docs/sources.md).

## Course Content Summary

| Concept | Importance | Exam likelihood |
|---|---|---|
| Process automation and PAC | Essential | **Very high** (3/3) |
| PLCs and motor starters | Essential | **Very high** (3/3) |
| Industrial networks, topology, OSI | Essential | High (2/3) |
| Distributed control systems | Essential | High (2/3) |
| Fire-and-gas (F&G) systems | Essential | **Very high** (3/3) |
| Electrical safety | Important | Medium (2/3) |
| Maintenance management | Essential | **Very high** (3/3) |
| Reliability and failure analysis | Important | High (2/3) |
| Wireless communication and security | Important | Medium (2/3) |
| Management tools: ERP, ROI, KPIs, LP | Important | High (2/3) |
| Closed-loop control | Supporting | Medium (2/3) |
| Standards and documentation | Supporting | Low |

## Course Content Details

### 1. Process automation and the PAC

Automation replaces human action in a process with instruments, controllers and actuators. A PAC is the modern controller that merges PLC, DCS and PC functions.

**Study:** Mehta Ch. 1 §1.1–1.13 (evolution, duties, functional topology) and Ch. 8 (PAC); lecturer note of 26 Aug 2021; RealPars "Industrial Automation Control Systems 101".
**Exam:** 2019/20 Q6; 2020/21 Q7.

- [ ] **Automation hierarchy** — field, control, supervisory, MES, ERP; what each layer decides and its time scale.
- [ ] **Process vs discrete vs batch** — continuous variables, sequencing, recipes; which controller suits each.
- [ ] **PAC definition and architecture** — CPU, I/O, communication, HMI; PAC vs PLC vs DCS vs PC-based control.
- [ ] **Benefits and economics** — throughput, quality, safety, energy, labour; capital cost, payback, ROI.
- [ ] **Instrumentation** — sensors, transmitters (4–20 mA, HART), final elements, signal standards.

### 2. PLCs and motor starters

Motor control is the most common automation task. The examiner expects you to draw the power and control circuits and explain the logic.

**Study:** Mehta Ch. 2 §2.1–2.8 (hardware, architecture, I/O, ladder/FBD/IL/SFC/ST); RealPars "What Is Ladder Logic" and "Motor Control Methods Explained"; PLC 1 Ch. 1 as backup.
**Exam:** 2019/20 Q1–Q3; 2020/21 Q1(a)–(b); 2021/22 Q1(a), Q2(a)–(c).

- [ ] **PLC architecture** — CPU, memory, input/output modules, power supply, backplane; scan cycle (input → program → output).
- [ ] **PLC vs relay logic** — advantages: reprogrammable, fewer wires, diagnostics, timers/counters, communication.
- [ ] **Motor starter types** — DOL, star–delta, auto-transformer, soft starter, VFD; current and torque characteristics.
- [ ] **Forward–reverse** — interlocking, why both contactors cannot close; control and power diagrams.
- [ ] **Protection** — overload relay, fuse/MCB, earth leakage, phase failure; coordination.
- [ ] **PLC implementation** — ladder for DOL and star–delta with timers; I/O list and addressing.

### 3. Industrial networks, topology and the OSI model

Automation systems are distributed, so communication is examined as architecture, not as protocol trivia.

**Study:** Mehta Ch. 10 §10.1–10.3 (OSI and TCP/IP), Ch. 9 (Modbus), Ch. 11–13 (HART, PROFIBUS, Foundation Fieldbus); RealPars "industrial communication protocols".
**Exam:** 2020/21 Q2(a)–(b); 2021/22 Q2(b).

- [ ] **Topologies** — bus, star, ring, tree, mesh; cost, fault tolerance, determinism.
- [ ] **OSI seven layers** — function of each; which layers fieldbus implements; TCP/IP mapping.
- [ ] **Fieldbus vs Ethernet** — determinism, speed, distance, power over the bus; PROFIBUS, Modbus, Foundation Fieldbus, PROFINET.
- [ ] **Media and hardware** — twisted pair, coax, fibre; repeater, hub, bridge, switch, router.
- [ ] **Redundancy and security** — ring redundancy, segmentation, firewalls, DMZ; why flat networks are dangerous.

### 4. Distributed control systems

A DCS distributes control across many controllers but presents one operator view. It dominates large continuous plants.

**Study:** Mehta Ch. 3 §3.1–3.8 (DCS architecture, diagnostics, controllers, workstations).
**Exam:** 2020/21 Q2(c).

- [ ] **DCS architecture** — field level, control level, supervisory level; operator station, engineering station, historian.
- [ ] **DCS vs PLC** — scale, redundancy, loop ownership, cost, application; when each is chosen.
- [ ] **Design factors** — I/O count, redundancy, scan time, environment, expansion, vendor support.
- [ ] **Databases and alarms** — tag database, alarm prioritisation, event logging, trend display.
- [ ] **Integration** — DCS to PLC, to SCADA, to ERP; OPC and gateways.

### 5. Fire-and-gas systems

F&G protects people and assets. It must detect, alarm, and execute shutdown independently of the control system.

**Study:** Mehta Ch. 6 §6.1–6.7 (pp. 217 ff.); _MCE 511 F&G and PAC Material_ (same chapter, typed).
**Exam:** 2019/20 Q4, Q5; 2020/21 Q5, Q6.

- [ ] **Detector types** — ionization and optical smoke, heat, flame (IR/UV), gas (catalytic, IR, electrochemical); placement and coverage.
- [ ] **Ionization smoke detector** — chamber, Americium source, ion current, smoke reduces current, threshold alarm.
- [ ] **Logic** — voting (1oo1, 2oo2, 2oo3), cause-and-effect matrix, alarm vs trip.
- [ ] **ESD and interlocks** — emergency shutdown, safety instrumented system, SIL levels.
- [ ] **F&G vs PAC** — independence, certified components, proof testing, why not on the process PLC.

### 6. Electrical safety

Automation work means working near live equipment. Safety is examinable as procedure and as hardware.

**Study:** Mehta Ch. 5 (functional safety, SIS, safety life cycle); _Electrical Safety_ slides (lecturer) pp. 1–18.
**Exam:** 2020/21 Q1(b); 2021/22 Q1(b); 2021/22 Q6 (failure modes).

- [ ] **Hazards** — electric shock, arc flash, burns, fire; effects of current on the body.
- [ ] **Protection** — earthing, RCD/ELCB, fuses, MCB, isolation, lock-out/tag-out.
- [ ] **Safe working** — permit to work, isolation and proving dead, PPE, arc-flash boundary.
- [ ] **Hazardous areas** — zones, intrinsic safety, explosion-proof enclosures, purging.
- [ ] **Standards** — IEC 60364, IEC 61508/61511, Nigerian electricity regulations.

### 7. Maintenance management

Maintenance is the largest operating cost in an automated plant. The examiner asks you to compare strategies and compute their effect.

**Study:** _Plant Maintenance_ slides (lecturer) — definitions, types, planning, costs; Mehta Ch. 18 (system maintenance) and Ch. 16 (asset management).
**Exam:** 2020/21 Q3(a)–(d); 2021/22 Q4, Q7(a)–(d).

- [ ] **Strategies** — reactive, preventive, predictive, condition-based, reliability-centred, total productive.
- [ ] **Predictive techniques** — vibration, thermography, oil analysis, ultrasound; what each detects.
- [ ] **Metrics** — availability and reliability:
  \$\=\frac{MTBF}{MTBF+MTTR},\qquad R(t)=e^{-t/MTBF}\$\$
- [ ] **Planning** — work orders, spares, shutdown/overhaul planning, backlog, scheduling.
- [ ] **Outsourcing** — third-party service contracts, SLAs, when to outsource vs keep in-house.
- [ ] **Worked example** — given failures and repair times, compute MTBF, MTTR, availability and the effect of halving MTTR.

### 8. Reliability and failure analysis

Failures are data. The course wants structured analysis, not blame.

**Study:** Mehta Ch. 16 §16.4–16.6 (fault models, calculation model) and Ch. 18; _Plant Maintenance_ slides (MTBF, availability).
**Exam:** 2020/21 Q4(b)–(c); 2021/22 Q6.

- [ ] **Failure modes** — random, wear-out, misuse; bathtub curve.
- [ ] **FMEA/FMECA** — severity, occurrence, detection, RPN; build a small table.
- [ ] **Pareto analysis** — rank causes, cumulative percentage, the vital few.
- [ ] **Root-cause analysis** — 5-whys, fishbone, fault tree.
- [ ] **Availability and spares** — redundancy, standby, spares holding cost.

### 9. Wireless communication and security

Wireless sensors remove cabling but add interference and attack surface.

**Study:** Mehta Ch. 14 §14.1–14.8; _Note on Wireless Communication_ pp. 1–12 (SSID, authentication, MAC filtering).
**Exam:** 2020/21 Q4(a).

- [ ] **Wireless standards** — Wi-Fi, Bluetooth, ZigBee, WirelessHART, ISA100; range, power, determinism.
- [ ] **Propagation** — attenuation, multipath, interference, Fresnel zone; site survey.
- [ ] **Security** — authentication, encryption, SSID hiding, MAC filtering, rogue access points, WPA2/3.
- [ ] **Industrial threats** — Stuxnet-style attacks, unauthorised entry, insider threat; defence in depth.
- [ ] **Design** — when wireless is justified; battery life; coexistence with existing networks.

### 10. Management tools and control loops

The management half of the course: planning, justifying and measuring automation.

**Study:** Mehta Ch. 19 (advanced control), Ch. 21 (alarm management), Ch. 23 (MES); lecturer note of 26 Aug 2021.
**Exam:** 2021/22 Q3, Q5(a)–(b).

- [ ] **Production planning** — ERP, MRP, PPC, MES; information flow from order to shop floor.
- [ ] **Linear programming** — formulate an objective and constraints; graphical solution; interpret the optimum.
- [ ] **Financial appraisal** — capex, opex, payback, NPV, IRR, ROI; simple worked case.
- [ ] **KPIs** — OEE, yield, downtime, energy per unit, first-pass quality; leading vs lagging.
- [ ] **Closed-loop control** — sensor → controller → valve; PID; tuning; temperature, pressure, flow and level loops.
- [ ] **Documentation** — P&ID, loop drawings, cause-and-effect, SOPs, handover.

## How to use this

Each topic has a **Study** line, an **Exam** line and a checklist. This is a management-flavoured course: memorise the structures (layers, hierarchies, maintenance types) and practise sketching them, then answer the past question in note form. Tick a box when you can draw the diagram and name the parts without notes.

**Refresh before starting (no new textbook):** basic electrical circuits — relay coils, contacts, motor starter circuits; elementary probability — MTBF and availability; no mathematics beyond arithmetic is needed.

**Priority:** PLC scan cycle, ladder logic, F&G subsystems, maintenance types/costs and the failure-mode table are repeated across papers. DCS and fieldbus are usually one question each. ERP/PPC is a single question — learn the diagram, not the theory.
