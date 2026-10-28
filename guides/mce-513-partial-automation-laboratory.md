# MCE 513 — Partial Automation Laboratory

*2 Units · 500 Level, Harmattan · BMAS: MCT 513 · FUTO Mechatronics*

## Overview

This is the practical automation course: you programme a PLC, wire its inputs and outputs, connect it to a fieldbus, and watch it on a SCADA screen. The examination is still written, so the laboratory work is tested as theory — ladder diagrams drawn from a process description, fieldbus comparisons, and SCADA architecture.

Papers are 2 hours and split into two sections: Section A is PLC hardware and ladder logic; Section B is industrial communication and SCADA. Three papers are available (2019/2020, 2020/2021, 2021/2022).

## Synopsis (BMAS MCT 513, verbatim)

> "Partial Automation :- Factory Automation Factory Automation study fields: - PLC programming level 1 - 3 - Industrial communication - Fieldbus - DC/AC motor - SCADA - Touch panel - Assembly/disassembly or Mechatronics part systems"

## Sources

- **PLC 1 (Bolton, _Programmable Logic Controllers_)** — Ch. 1 §1.1–1.4 controllers, hardware, architecture, PLC systems; Ch. 2 §2.1–2.3 input/output devices and applications; Ch. 4 §4.4–4.6 networks, processing inputs, I/O addresses.
- **PLC 2** — continuation of Ch. 4 (I/O processing, networks, addresses).
- **PLC 3** — Ch. 5 §5.1–5.7 ladder diagrams, logic functions, latching, multiple outputs, function blocks, program examples.
- **_MCE 513 – Field Buses_** — Ch. 1 introduction (definition, OSI mapping, response time) and Ch. 2 WorldFIP.
- **_SCADA_** — Ch. 7 of _Measurement & Instrumentation Systems_ (architecture, RTUs, functions).
- **Course folder extras:** _Mce 513 Ladder diagrams_; _Graphe Fonctionnel de Commande Étape Transition_ (GRAFCET); _Partial Automation Laboratory_ manual (experiments); term paper.
- **Past papers:** 2019/2020, 2020/2021, 2021/2022, plus the exam AOC.
- **Online:** [RealPars articles](https://www.realpars.com/blog/) — search "ladder logic", "latching", "sinking and sourcing", "PROFIBUS", "SCADA".
- **Gap:** motor drives beyond the starter circuit are not taught; answer those from general drive theory.

- **Not included:** textbooks and lecturer notes are not redistributed here; see [\docs/sources.md\](../docs/sources.md).

## Course Content Summary

| Concept | Importance | Exam likelihood |
|---|---|---|
| PLC architecture and scan cycle | Essential | **Very high** (3/3) |
| Ladder logic and latching | Essential | **Very high** (3/3) |
| Timers and counters | Essential | High (2/3) |
| I/O devices, sourcing/sinking | Essential | High (3/3) |
| Sensors and signal conditioning | Important | Medium (2/3) |
| Fieldbus and the OSI model | Essential | **Very high** (3/3) |
| SCADA, HMI and touch panels | Essential | High (3/3) |
| DC/AC motors and drives | Important | Medium (2/3) |
| Sequence and batch control | Important | High (2/3) |
| Installation, safety, commissioning | Supporting | Low |

## Course Content Details

### 1. PLC architecture and operation

A PLC is a rugged computer that reads inputs, executes a stored program, and writes outputs — repeatedly, forever. Everything else follows from the scan cycle.

**Study:** PLC 1 Ch. 1 §1.1–1.4 (controllers, hardware, internal architecture, PLC systems); Mehta Ch. 2 §2.2–2.5 as a second explanation; RealPars "PLC Modules Explained".
**Exam:** 2019/20 Q3(a)–(b); 2020/21 Q4(a)–(d); 2021/22 Q6(a)–(b).

- [ ] **Architecture** — CPU, memory (ROM/RAM/EEPROM), input and output modules, power supply, backplane, communication module.
- [ ] **Scan cycle** — input scan → program scan → output update → housekeeping; scan time and why it matters.
- [ ] **Memory and addressing** — input/output/internal/timer/counter registers; bit, byte, word addressing; symbolic vs absolute.
- [ ] **Forms of PLC** — compact, modular, rack; fixed vs expandable I/O; distributed I/O.
- [ ] **PLC vs relay vs PC** — advantages, disadvantages, application envelope.
- [ ] **Selection** — I/O count and type, scan time, memory, communication, environment, cost.

### 2. Ladder logic and latching

Ladder logic is a drawing of a relay circuit. The examiner gives a process description and asks for the rungs.

**Study:** PLC 3 Ch. 5 §5.1–5.5 (ladder diagrams, logic functions, latching, multiple outputs, entering programs); _Mce 513 Ladder diagrams_; RealPars "PLC Latching vs Sealing".
**Exam:** 2019/20 Q1–Q2; 2020/21 Q1(a)–(b), Q5(d); 2021/22 Q1, Q2.

- [ ] **Basic symbols** — normally open, normally closed, coil, set/reset, timer, counter; power rails and rung numbering.
- [ ] **Boolean correspondence** — AND (series), OR (parallel), NOT (normally closed); convert a Boolean expression to a rung and back.
- [ ] **Latching** — seal-in circuit with a start button and stop button; why the stop must be normally closed and wired fail-safe.
- [ ] **Interlocking** — forward/reverse, star/delta; prevent simultaneous coils.
- [ ] **Design method** — list inputs/outputs, write the truth table or sequence, draw rungs, simulate, then hand over.
- [ ] **Worked example** — batch mixing: fill valve, low-level switch, heater, agitator, discharge valve, with timers and interlocks.

### 3. Timers, counters and sequence control

Timers and counters turn ladder logic from combinational into sequential — this is what makes automation possible.

**Study:** PLC 3 Ch. 5 §5.6–5.7 (function blocks, program examples); _Graphe Fonctionnel de Commande Étape Transition_ (GRAFCET/SFC); Mehta Ch. 2 §2.8 (SFC and ST).
**Exam:** 2019/20 Q4 (batch mixing ladder); 2020/21 Q1(b); 2021/22 Q1.

- [ ] **Timer types** — on-delay (TON), off-delay (TOF), retentive (RTO); timing diagram for each.
- [ ] **Timer parameters** — preset, accumulated, time base; resolution and maximum delay.
- [ ] **Counters** — up, down, up/down; preset, accumulated, reset; applications (batching, parts counting).
- [ ] **Sequence control** — step-by-step using set/reset or a state integer; grafcet/SFC (awareness).
- [ ] **Worked example** — star–delta starter with a 10 s transition; conveyor that counts 12 parts then stops.

### 4. Input and output devices

The PLC only knows what its I/O tells it. Choosing and wiring the device is half the engineering.

**Study:** PLC 1 Ch. 2 §2.1–2.3 (input and output devices); PLC 2 Ch. 4 §4.5–4.6 (processing inputs, I/O addresses); Mehta Ch. 2 §2.4.
**Exam:** 2019/20 Q1(c); 2020/21 Q1(c), Q5(a)–(c); 2021/22 Q5(a)–(b).

- [ ] **Discrete inputs** — push button, selector switch, limit switch, reed switch, photoelectric, proximity, float switch, pressure switch.
- [ ] **Discrete outputs** — relay, triac, transistor; contactor, solenoid valve, indicator lamp, alarm.
- [ ] **Sourcing vs sinking** — PNP (sourcing) vs NPN (sinking); wiring to a PLC input; common terminal.
- [ ] **Analogue I/O** — 4–20 mA, 0–10 V, RTD, thermocouple; resolution, scaling, filtering.
- [ ] **Signal conditioning** — isolation, amplification, noise, shielded cable, grounding.
- [ ] **Device selection** — voltage, current, IP rating, environment, response time, fail-safe state.

### 5. Sensors and measurement

Sensors convert a physical variable into a signal the PLC can read. Know the principle, the range and the failure mode.

**Study:** PLC 1 Ch. 2 §2.1 (sensor types and characteristics); Mehta Ch. 2 §2.4; RealPars "Industrial Sensors".
**Exam:** 2020/21 Q5(b) (six sensor performance features); 2021/22 Q5(b).

- [ ] **Sensor performance** — range, span, sensitivity, accuracy, repeatability, resolution, hysteresis, linearity, drift, response time.
- [ ] **Position** — encoder (incremental/absolute), potentiometer, LVDT, laser distance.
- [ ] **Proximity** — inductive, capacitive, ultrasonic, optical; target material and range.
- [ ] **Process sensors** — pressure (strain gauge, capacitive), temperature (RTD, thermocouple, thermistor), flow (orifice, electromagnetic, ultrasonic), level (float, ultrasonic, radar).
- [ ] **Calibration** — zero and span, traceability, calibration record; why it is a maintenance task.

### 6. Fieldbus and industrial communication

Fieldbus replaces a bundle of wires with a digital network. The examiner tests the OSI model and protocol comparison.

**Study:** _Field Buses_ Ch. 1 (pp. 1–20: definition, advantages, OSI mapping) and Ch. 2 (WorldFIP); Mehta Ch. 10 §10.1–10.2 and Ch. 12–13.
**Exam:** 2019/20 Q5–Q7; 2020/21 Q2(a)–(c), Q3(a)–(b); 2021/22 Q3.

- [ ] **Fieldbus concept** — master/slave, producer/consumer, deterministic vs best-effort; why digital beats 4–20 mA.
- [ ] **OSI seven layers** — physical, data link, network, transport, session, presentation, application; which layers a fieldbus uses.
- [ ] **Protocols** — PROFIBUS DP/PA, Modbus RTU/TCP, Foundation Fieldbus, CAN/CANopen, DeviceNet, WorldFIP, PROFINET, EtherCAT.
- [ ] **Comparison table** — speed, distance, topology, determinism, max nodes, application; learn the CAN/PROFIBUS/WorldFIP comparison asked in 2020/2021.
- [ ] **Network hardware** — repeater, hub, bridge, switch, router, gateway; collision domain and segmentation.
- [ ] **Cabling and termination** — shielded twisted pair, termination resistors, grounding, segment length, drop lines.

### 7. SCADA, HMI and touch panels

SCADA is the operator's window on the plant. It acquires data, displays it, logs it and raises alarms.

**Study:** _SCADA_ Ch. 7 (pp. 1–20); Mehta Ch. 7 §7.1–7.6; RealPars SCADA articles.
**Exam:** 2019/20 Q8–Q10; 2020/21 Q6; 2021/22 Q4.

- [ ] **SCADA architecture** — field devices → RTU/PLC → communication → master station (server) → HMI clients; historian.
- [ ] **Functions** — data acquisition, supervisory control, alarming, trending, reporting, event logging.
- [ ] **HMI design** — mimic diagram, faceplates, navigation, colour standards, alarm priority, operator error.
- [ ] **Touch panel** — configuration software, tags, screens, recipes, alarms; panel vs PC-based HMI.
- [ ] **Communication** — OPC, Modbus/TCP, DNP3, IEC 60870-5-104; poll vs report-by-exception.
- [ ] **Security** — network segregation, authentication, audit trail, remote access risk.

### 8. Motors, drives and actuators

The laboratory uses DC and AC motors. The written paper asks for the principle and the starting method.

**Study:** _Partial Automation Laboratory_ manual (experiments); PLC 1 Ch. 2 §2.4.1.10 (solenoid valves); RealPars "Motor Control Methods Explained".
**Exam:** 2020/21 Q1(a) (motor starter); otherwise supports the ladder questions.

- [ ] **DC motor** — separately excited, shunt, series, compound; torque–speed characteristic; speed control by armature voltage and field.
- [ ] **Three-phase induction motor** — rotating field, slip, torque–speed curve, starting current.
- [ ] **Starting methods** — DOL, star–delta, autotransformer, soft starter, VFD; current and torque comparison.
- [ ] **VFD** — rectifier, DC link, inverter, PWM; volts-per-hertz control; harmonics.
- [ ] **Actuators** — solenoid valve, pneumatic cylinder, servo motor, stepper; positioning and feedback.

### 9. Installation, commissioning and safety

A panel that works on the bench must survive the plant. This section is short-answer only.

**Study:** Mehta Ch. 5 (functional safety); _Electrical Safety_ slides (lecturer); RealPars "How to Troubleshoot a Series Emergency Stop Circuit".
**Exam:** 2020/21 Q5(c); 2021/22 Q5(c).

- [ ] **Panel practice** — layout, DIN rail, wire numbering, ferrules, segregation of power and signal, labelling.
- [ ] **Commissioning** — insulation test, continuity, point-to-point I/O check, dry run, loop tuning, handover.
- [ ] **Safety** — emergency stop category, guard interlock, lock-out/tag-out, fail-safe wiring, risk assessment.
- [ ] **Documentation** — P&ID, wiring diagram, I/O list, ladder printout, operating manual, as-built drawings.
- [ ] **Troubleshooting** — symptom → section → device → signal; use of multimeter, forcing, online monitoring.

## How to use this

Each topic has a **Study** line, an **Exam** line and a checklist. This is a drawing-heavy paper: read the cited pages, then redraw every ladder rung and block diagram from memory before checking. Tick a box only when you can draw it and explain each rung.

**Refresh before starting (no new textbook):** basic circuits — relay coil, NO/NC contact, series/parallel; binary and hexadecimal; no calculus is needed.

**Priority:** ladder logic (latching, timers, batch sequence), PLC architecture, fieldbus/OSI and SCADA are the four recurring questions. Sourcing/sinking and sensor characteristics are short, cheap marks. Learn to draw the scan cycle and the OSI stack as diagrams.
