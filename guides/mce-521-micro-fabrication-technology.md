# MCE 521 — Micro-fabrication Technology

*2 Units · 500 Level, Harmattan · BMAS analogue: MCT 519 · FUTO Mechatronics*

## Overview

Micro-fabrication is how a grain of sand becomes a processor: crystal growth, wafering, oxidation, lithography, etching, doping, deposition, metallisation, packaging. The same process stack makes MEMS sensors, and that is why a mechatronics student studies it.

This is a descriptive, process-sequence course: name the step, state its purpose, draw the cross-section, and explain the trade-offs. No past paper exists in the supplied material, so weightings below are inferred from the BMAS scope and standard courses.

## Synopsis (BMAS MCT 519, verbatim)

> "Crystal growth, thermal oxidation, photolithography, etching, diffusion, iron implantation, film deposition, metallization, layout, process integration, IC manufacturing, MEMS, CAD tools for microfabrication (eg. SUPREM, PROLITH etc.). Future trends and challenges."

## Sources

**No lecture notes or past papers for MCE 521 were supplied** — the topic list is from BMAS MCT 519. Use these instead, in this order:

- **[MIT 6.777J, _Design and Fabrication of MEMS_](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/)** (free lecture notes) — Lectures 1–4 are a four-part microfabrication sequence covering cleanrooms, crystal growth, oxidation, lithography, etching, diffusion, implantation and deposition; Lecture 19 is packaging; Lecture 24 is a capacitive-accelerometer process flow. This is your main "chapter" source.
- **Campbell, _Fabrication Engineering at the Micro- and Nanoscale_** — cite the process chapters by name (crystal growth, oxidation, diffusion, implantation, lithography, etching, deposition, metallization, integration). Chapter numbers differ between editions, so use the title.
- **Jaeger, _Introduction to Microelectronic Fabrication_** — short chapters that map one-to-one onto the topics; use it for worked calculations.
- **Madou, _Fundamentals of Microfabrication and Nanotechnology_** — only for MEMS process flows and non-silicon micromachining.
- **Evidence:** all detail is external or inferred; there is no FUTO paper to calibrate depth.

- **Not included:** textbooks and lecturer notes are not redistributed here; see [\docs/sources.md\](../docs/sources.md).

## Course Content Summary

| Concept | Importance | Exam likelihood |
|---|---|---|
| Cleanroom and wafer preparation | Essential | Unknown (no paper) |
| Crystal growth and wafering | Essential | Unknown |
| Thermal oxidation | Essential | Unknown |
| Photolithography | Essential | **Highest** (core of the course) |
| Etching (wet and dry) | Essential | Unknown |
| Diffusion and ion implantation | Essential | Unknown |
| Film deposition (CVD/PVD/epitaxy) | Essential | Unknown |
| Metallisation and interconnect | Important | Unknown |
| Process integration and IC flow | Important | Unknown |
| MEMS fabrication | Essential | Unknown |
| CAD tools (SUPREM, PROLITH) | Supporting | Unknown |
| Future trends and challenges | Optional | Unknown |

## Course Content Details

### 1. Cleanrooms and wafer preparation

Micro-fabrication needs a particle-free, temperature- and humidity-controlled environment. Contamination is measured in particles per cubic foot, and a single speck can kill a die.

**Study:** [MIT 6.777J Lecture 1](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/) (microfabrication I: cleanrooms, contamination, wafers); Campbell, the cleanroom/contamination chapter; Jaeger Ch. 1 (overview of microfabrication).
**Exam:** No paper exists. Expect "define a cleanroom class and explain contamination sources" — write the definition, the class table and three controls.

- [ ] **Cleanroom classes** — ISO 14644-1 classes (ISO 1–9) vs the old US Federal 209E (Class 1–100 000); what class each process needs.
- [ ] **Contamination sources** — particles, metals, organics, ions; human body, equipment, chemicals, air.
- [ ] **Cleanroom practice** — gowning, air showers, laminar flow, positive pressure, HEPA/ULPA filters.
- [ ] **Wafer specifications** — diameter (100/150/200/300 mm), thickness, orientation (100), resistivity, doping type, flat/notch.
- [ ] **Wafer cleaning** — RCA clean (SC-1, SC-2), HF dip, DI rinse, drying; what each step removes.
- [ ] **Getting started** — substrate choice (Si, GaAs, glass, SOI); why silicon dominates.

### 2. Crystal growth and wafering

The crystal must be a single, defect-free lattice before any device can be built on it.

**Study:** [MIT 6.777J Lectures 1–2](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/); Campbell, "Crystal Growth" and "Wafer Preparation"; Jaeger Ch. 2.
**Exam:** No paper. Expect "Czochralski vs float-zone" and a wafer-specification question.

- [ ] **Czochralski process** — seed, melt, pulling, rotation, doping; pull rate vs diameter.
- [ ] **Float-zone process** — RF coil, no crucible, high purity; comparison with CZ.
- [ ] **Defects** — point defects, dislocations, stacking faults, twins; how growth controls them.
- [ ] **Wafering** — ingot grinding, slicing (wire saw), lapping, etching, polishing; material loss.
- [ ] **Epitaxy** — homoepitaxy vs heteroepitaxy; CVD epitaxial reactor; why a lightly doped layer is grown.
- [ ] **Quality metrics** — resistivity, flatness, TTV, bow, warp, particles.

### 3. Thermal oxidation

Silicon oxidises to $\mathrm{SiO_2}$, an excellent insulator and mask. The Deal–Grove model explains the kinetics.

**Study:** [MIT 6.777J Lecture 2](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/); Campbell, "Thermal Oxidation"; Jaeger Ch. 3. Derive the Deal–Grove linear–parabolic result.
**Exam:** No paper. Expect "explain oxidation, sketch the Deal–Grove curve, and state two uses of the oxide".

- [ ] **Purpose** — gate dielectric, field oxide, masking layer, passivation.
- [ ] **Deal–Grove model** — linear (reaction-limited) and parabolic (diffusion-limited) growth:
  $$x^2+Ax=Bt$$
  Identify $A$, $B$ and the crossover thickness.
- [ ] **Dry vs wet oxidation** — $\mathrm{O_2}$ vs $\mathrm{H_2O}$; rate, density, quality; which for gate oxide.
- [ ] **Process variables** — temperature, time, pressure, crystal orientation; thickness calculation.
- [ ] **Masking** — $\mathrm{SiO_2}$ as a diffusion/implant barrier; etch selectivity.
- [ ] **Characterisation** — ellipsometry, C–V measurement, breakdown field.

### 4. Photolithography

Lithography transfers a pattern from a mask to the wafer. It is the most expensive and most critical step.

**Study:** [MIT 6.777J Lecture 3](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/); Campbell, "Lithography"; Jaeger Ch. 6. Know the photoresist steps and the resolution limit.
**Exam:** No paper. Expect "list the lithography steps in order and explain contact vs projection alignment".

- [ ] **Process sequence** — vapour prime (HMDS) → resist spin → soft bake → align → expose → post-exposure bake → develop → inspect.
- [ ] **Resist types** — positive vs negative; exposure changes solubility; resolution and contrast.
- [ ] **Exposure tools** — contact, proximity, projection, stepper, scanner; wavelength (g-line, i-line, KrF, ArF, EUV).
- [ ] **Resolution** — Rayleigh criterion and depth of focus:
  $$R=\frac{k_1\lambda}{NA},\qquad \mathrm{DOF}=\frac{k_2\lambda}{NA^2}$$
  Know what numerical aperture buys and what it costs.
- [ ] **Masks and alignment** — mask materials, alignment marks, overlay error, mask bias.
- [ ] **Advanced techniques** — phase-shift mask, OPC, immersion lithography, double patterning, EUV.

### 5. Etching

Etching removes material selectively. The two families are wet (chemical) and dry (plasma).

**Study:** [MIT 6.777J Lectures 3–4](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/); Campbell, "Etching"; Jaeger Ch. 7. Compare wet, plasma and RIE, and isotropic vs anisotropic.
**Exam:** No paper. Expect "compare wet and dry etching" and "explain selectivity and anisotropy".

- [ ] **Wet etching** — isotropic, selectivity, etch rate; HF for $\mathrm{SiO_2}$, KOH for Si, HNA for Si.
- [ ] **Dry etching** — plasma, RIE, DRIE, ion milling; anisotropic, high aspect ratio.
- [ ] **Etch metrics** — selectivity, anisotropy, etch rate, uniformity, endpoint detection, undercut.
- [ ] **Wet vs dry** — comparison table: directionality, damage, cost, waste, feature size.
- [ ] **Stopping layers** — oxide/nitride, etch-stop layers, SOI buried oxide.
- [ ] **Applications** — contact holes, trenches, MEMS release, through-silicon vias.

### 6. Diffusion and ion implantation

Doping changes conductivity. Diffusion is thermal; implantation is ballistic, followed by annealing.

**Study:** [MIT 6.777J Lectures 2–3](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/); Campbell, "Diffusion" and "Ion Implantation"; Jaeger Ch. 4–5. Know Fick's laws and the implant profile.
**Exam:** No paper. Expect "compare diffusion and implantation" plus a junction-depth or dose calculation.

- [ ] **Diffusion** — Fick's laws, concentration profiles (erfc, Gaussian), drive-in vs predeposition.
- [ ] **Diffusion furnace** — tube, gas supply, temperature uniformity, wafer boat.
- [ ] **Ion implantation** — ion source, acceleration, mass analysis, beam scanning, dose and energy.
- [ ] **Implant profiles** — projected range $R_p$, straggle, channeling, tilt and twist.
- [ ] **Annealing** — damage recovery, dopant activation, rapid thermal annealing; diffusion trade-off.
- [ ] **Comparison** — diffusion vs implantation: profile control, dose accuracy, damage, throughput, cost.

### 7. Film deposition

Thin films are added for conductors, insulators and semiconductors. CVD is chemical; PVD is physical.

**Study:** [MIT 6.777J Lecture 4](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/); Campbell, "Deposition" (CVD, PVD, epitaxy); Jaeger Ch. 8. Compare CVD, sputtering and evaporation.
**Exam:** No paper. Expect "compare CVD and PVD" and "why a conformal step coverage matters".

- [ ] **CVD** — APCVD, LPCVD, PECVD, MOCVD; reaction, mass transport, temperature; polysilicon, $\mathrm{SiO_2}$, $\mathrm{Si_3N_4}$.
- [ ] **PVD** — evaporation, sputtering; step coverage, adhesion, stress.
- [ ] **Epitaxial growth** — vapour-phase epitaxy, MBE; abrupt interfaces, superlattices.
- [ ] **ALD** — self-limiting monolayers, conformality, high-k dielectrics.
- [ ] **Film properties** — thickness, uniformity, stress, density, refractive index, step coverage.
- [ ] **Selection** — temperature budget, conformality, deposition rate, cost, application.

### 8. Metallisation, interconnect and packaging

Devices must be wired together and connected to the outside world without introducing resistance or contamination.

**Study:** [MIT 6.777J Lecture 19](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/) (packaging); Campbell, "Metallization"; Jaeger Ch. 9. Know interconnect metals, silicides and bond types.
**Exam:** No paper. Expect "list the functions of metallisation" and "describe wire bonding vs flip-chip".

- [ ] **Metallisation** — aluminium vs copper; silicide; barrier layers (TiN, TaN); adhesion layers.
- [ ] **Interconnect** — multilevel metal, via, damascene process; RC delay, electromigration.
- [ ] **Contacts** — ohmic contact, Schottky contact, contact resistance, anneal.
- [ ] **Packaging** — die attach, wire bonding, flip-chip, encapsulation; thermal and mechanical stress.
- [ ] **Yield and reliability** — defect density, killer defects, accelerated testing, failure analysis.

### 9. Process integration, MEMS and CAD tools

A process flow is a sequence of modules, each affecting the next. MEMS adds release and 3-D structuring.

**Study:** [MIT 6.777J Lectures 1–4 recap and Lecture 24](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/) (capacitive accelerometer case study); Campbell, "Process Integration"; Madou for MEMS process flows.
**Exam:** No paper. Expect "draw a process flow for a simple device" and "name three CAD tools used in MEMS".

- [ ] **Process integration** — front-end vs back-end, thermal budget, module order, design rules.
- [ ] **CMOS flow** — well → isolation → gate → source/drain → contact → metal → passivation; cross-sections.
- [ ] **MEMS processes** — bulk micromachining (KOH, DRIE), surface micromachining (sacrificial layer), wafer bonding, LIGA.
- [ ] **MEMS examples** — accelerometer, pressure sensor, gyroscope, micro-mirror, lab-on-chip.
- [ ] **CAD tools** — SUPREM for process simulation, PROLITH for lithography, L-Edit for layout, Coventor for MEMS.
- [ ] **Future trends** — EUV, 3-D ICs, chiplets, 2-D materials, quantum devices, sustainability (water, energy, PFAS).

## How to use this

Each topic has a **Study** line and a checklist; the **Exam** line states the likely question because no past paper exists. Read one MIT lecture, then the matching book chapter, then write the answer to the likely question from memory. Tick a box when you can draw the process and explain each step.

**Refresh before starting (no new textbook):** chemistry — oxidation, reduction, acids/bases, plasmas; physics — diffusion, crystal lattices, Miller indices; optics — diffraction and numerical aperture (for lithography resolution).

**Priority:** oxidation, lithography, etching and diffusion/implantation are the core four and carry most of the marks in any microfab paper. Packaging and CAD tools are short-answer topics. Do not read Madou cover to cover — use it only for process-flow diagrams.
