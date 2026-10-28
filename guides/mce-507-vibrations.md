# MCE 507 — Vibrations

*2 Units · 500 Level, Harmattan · BMAS: MCT 507 · FUTO Mechatronics*

## Overview

Every machine that moves oscillates, and vibration is the study of that oscillation: how to predict it, measure it, and stop it from destroying the machine or the product. The course starts with one mass on one spring and ends with multi-degree-of-freedom systems, isolation and balancing.

Papers are calculation-heavy: derive the equation of motion, find natural frequency and damping, compute the response, then interpret it. The 2020/2021 paper is the available sample.

## Synopsis (BMAS, verbatim)

> "Mechanical systems with one and several degrees of freedom, free, forced, and damped vibrations. Vibration problem solution by nodal analysis. Continuous systems, including exact and finite-element methods. Approximate methods of solution; Computer solutions: Vibration Isolation and absorption. Machine balancing."

## Sources

- **Rao, _Mechanical Vibrations_** (Drive folder PDF, 800+ pp.) — a reference, not a novel. Ch. 1 §1.6–1.7 (pp. 14–27) SHM and dynamics review; Ch. 2 §2.2–2.12 (pp. 55–110) springs, damping, inertia, equivalent systems; Ch. 3 (pp. 137–204) free vibration and log decrement; Ch. 4 (pp. 205–312) harmonic excitation, magnification, transmissibility, isolation; Ch. 6–8 (pp. 383–592) two-DOF and MDOF; Ch. 10 (pp. 633–688) continuous systems; Ch. 11 (pp. 689–736) FEM.
- **Lecturer handout, _Mechanical Vibrations_ (Ch. 13)** — the taught sequence and notation. Read this first for every topic; it is short.
- **Past paper:** 2020/2021, seven questions. Question numbers below refer to it. The 2023 Section A/B paper exists only as images; check it against topics 7–9.
- **Online:** [MIT 2.003SC](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) — the "Mechanical Vibration", "Vibration of Multi-Degree-of-Freedom Systems" and "Lagrange Equations" units. Use it when Rao's derivation is too dense.
- **Gap:** the taught notes stop at SDOF forced vibration; MDOF, isolation and balancing come from Rao.
- **Not included:** textbooks and lecturer notes are not redistributed here; see [`docs/sources.md`](../docs/sources.md).

## Course Content Summary

| Concept | Importance | Exam likelihood |
|---|---|---|
| Definitions, SHM, elements | Essential | High |
| SDOF free vibration, $\omega_n$ | Essential | **Very high** |
| Equilibrium, energy, Rayleigh methods | Essential | **Very high** |
| Damping and logarithmic decrement | Essential | **Very high** |
| Forced vibration, magnification | Essential | **Very high** |
| Transmissibility and isolation | Important | Medium |
| MDOF and modal analysis | Important | Medium |
| Continuous systems, approximate methods | Supporting | Low |
| Finite-element method | Supporting | Low |
| Machine balancing | Important | Medium |
| Vibration measurement | Supporting | Medium |

## Course Content Details

### 1. Fundamentals and simple harmonic motion

Vibration is oscillation about equilibrium. The three elements — mass, spring, damper — produce every equation in the course.

**Study:** Rao Ch. 1 §1.6–1.7 (pp. 14–27); the lecturer's handout, opening sections; [MIT 2.003SC "Mechanical Vibration" unit](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/).
**Exam:** 2020/21 Q2(a)–(b).

- [ ] **Definitions** — period, frequency, amplitude, phase, natural frequency, resonance, damping; degrees of freedom.
- [ ] **SHM** — displacement, velocity and acceleration:
  $$x=A\sin(\omega_n t+\phi),\qquad v=A\omega_n\cos(\omega_n t+\phi),\qquad a=-\omega_n^2 x$$
  Acceleration leads displacement by $180^\circ$.
- [ ] **Types** — free vs forced, damped vs undamped, longitudinal/transverse/torsional, linear vs nonlinear.
- [ ] **Elements** — the three ideal elements:
  $$F=kx,\qquad F=c\dot x,\qquad F=m\ddot x$$
  Derive the equivalent stiffness for springs in series and parallel.
- [ ] **Simple pendulum** — small-angle equation and natural frequency:
  $$\ddot\theta+\frac{g}{l}\theta=0,\qquad \omega_n=\sqrt{\frac{g}{l}}$$
  Compound pendulum: $\omega_n=\sqrt{mg\bar r/I_O}$.

### 2. Free vibration of SDOF systems

Free vibration is the system talking to itself. Its frequency depends only on mass and stiffness.

**Study:** Rao Ch. 3 §3.1–3.6 (pp. 137–160); the lecturer's handout (free vibration).
**Exam:** 2020/21 Q2, Q3(a)–(b).

- [ ] **Equation of motion** — undamped free vibration:
  $$m\ddot x+kx=0$$
  Write the general solution and fix the two constants from the initial conditions.
- [ ] **Natural frequency** — spring–mass system:
  $$\omega_n=\sqrt{\frac{k}{m}},\qquad f_n=\frac{\omega_n}{2\pi},\qquad \tau_n=\frac{2\pi}{\omega_n}$$
  Static-deflection method: $\omega_n=\sqrt{g/\delta_{st}}$.
- [ ] **Equivalent systems** — reflect masses and stiffnesses through gears/levers; find the equivalent $m_{eq}$, $k_{eq}$.
- [ ] **Transverse vibration** — beam stiffness for the two standard cases:
  $$k=\frac{3EI}{L^3}\ \text{(cantilever)},\qquad k=\frac{48EI}{L^3}\ \text{(simply supported, centre load)}$$
- [ ] **Torsional vibration** — shaft stiffness and natural frequency:
  $$k_t=\frac{GJ}{L},\qquad \omega_n=\sqrt{\frac{k_t}{J}}$$
  Reflect geared shafts to one speed before substituting.

### 3. Energy, equilibrium and Rayleigh methods

When the equation of motion is awkward, energy methods give the natural frequency without solving it.

**Study:** Rao Ch. 2 §2.9–2.12 (pp. 87–110) for free-body, static-deflection and equivalent systems; the lecturer's handout for the equilibrium, energy and Rayleigh derivations (the lecturer's notation is the one examined).
**Exam:** 2020/21 Q1 (equivalent system), Q3(a) (energy at the nth cycle).

- [ ] **Equilibrium method** — sum forces/moments about the static equilibrium position; gravity cancels with static deflection.
- [ ] **Energy method** — for conservative free vibration:
  $$T+V=\text{constant}\quad\Longrightarrow\quad \frac{d}{dt}(T+V)=0$$
  For SHM, $T_{\max}=V_{\max}$.
- [ ] **Rayleigh quotient** — with an assumed mode shape:
  $$\omega_n^2=\frac{V_{\max}}{T^{*}_{\max}}$$
  It always overestimates $\omega_n$; a better shape gives a closer bound.
- [ ] **Dunkerley** — combine component frequencies; lower bound on fundamental frequency.
- [ ] **Worked example** — mass on a beam, spring–mass–pulley system; derive $\omega_n$ both ways and compare.

### 4. Damping and logarithmic decrement

Real systems lose energy. Damping changes both the frequency and the rate of decay, and the log decrement is how you measure it.

**Study:** Rao Ch. 3 §3.4–3.9 (pp. 147–174) — underdamped, critical, overdamped and Coulomb damping; log decrement is in §3.4; the lecturer's handout (damped free vibration).
**Exam:** 2020/21 Q3(a)–(c).

- [ ] **Damping types** — viscous, Coulomb, structural/hysteretic; which model the course uses.
- [ ] **Damped equation** — free vibration with viscous damping:
  $$m\ddot x+c\dot x+kx=0,\qquad \zeta=\frac{c}{2\sqrt{km}},\qquad \omega_d=\omega_n\sqrt{1-\zeta^2}$$
- [ ] **Regimes** — underdamped ($\zeta<1$), critically damped ($\zeta=1$), overdamped ($\zeta>1$); sketch all three.
- [ ] **Logarithmic decrement** — from two successive peaks:
  $$\delta=\ln\frac{x_1}{x_2}=\frac{2\pi\zeta}{\sqrt{1-\zeta^2}}$$
  Small damping: $\zeta\approx\delta/2\pi$. For $n$ cycles, $\delta=\frac{1}{n}\ln(x_1/x_{n+1})$.
- [ ] **Worked example** — amplitude falls from 20 mm to 5 mm in 5 cycles: find $\delta$, $\zeta$, $c$ and $\omega_d$.

### 5. Forced vibration and magnification

Forced vibration is the response to an external excitation. Resonance is the dangerous case where the excitation frequency approaches $\omega_n$.

**Study:** Rao Ch. 4 §4.1–4.5 (pp. 205–234) — harmonic excitation, rotating unbalance, support excitation; the lecturer's handout (forced vibration, magnification factor).
**Exam:** 2020/21 Q5(a)–(d), Q6, Q7.

- [ ] **Harmonic force** — equation and steady-state amplitude:
  $$m\ddot x+c\dot x+kx=F_0\sin\omega t,\qquad x_p(t)=X\sin(\omega t-\phi)$$
- [ ] **Magnification factor** — amplitude ratio and frequency ratio:
  $$M=\frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}},\qquad r=\frac{\omega}{\omega_n}$$
  Sketch $M$ against $r$ for several $\zeta$.
- [ ] **Phase** — phase lag of the response:
  $$\tan\phi=\frac{2\zeta r}{1-r^2}$$
  At resonance, $\phi=90^\circ$.
- [ ] **Resonance** — peak location and peak value:
  $$r_{\mathrm{peak}}=\sqrt{1-2\zeta^2},\qquad M_{\mathrm{peak}}=\frac{1}{2\zeta\sqrt{1-\zeta^2}}$$
  Mark the half-power bandwidth.
- [ ] **Base excitation** — support motion $y=Y\sin\omega t$; derive the response and transmissibility.
- [ ] **Periodic excitation** — Fourier series of a periodic force; superposition of harmonics; why the fundamental dominates.

### 6. Transmissibility, isolation and absorption

Isolation stops vibration reaching a sensitive object; absorption cancels it at the source. Both are design problems.

**Study:** Rao Ch. 4 §4.6–4.8 (pp. 234–244) and §4.11 (seismic instruments, pp. 255–259); [MIT 2.003SC "Mechanical Vibration" unit](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/).
**Exam:** 2020/21 Q6(b) (transmissibility comment); supports Q6(a).

- [ ] **Transmissibility** — force and motion transmission ratio:
  $$T_r=\sqrt{\frac{1+(2\zeta r)^2}{(1-r^2)^2+(2\zeta r)^2}}$$
- [ ] **Isolation region** — isolation begins at
  $$r>\sqrt{2}$$
  A soft mount works because it lowers $r$; the penalty is static deflection.
- [ ] **Isolator design** — choose $k$ and $c$ from the required $T_r$ and the allowable static deflection.
- [ ] **Vibration absorber** — tuned mass damper; tuning $\omega_a=\omega_n$, effect on the two peaks.
- [ ] **Worked example** — machine of 100 kg on isolators, 20% transmissibility at 1500 rpm: find $k$.

### 7. Multi-degree-of-freedom systems

Real structures have many masses and many natural frequencies. Matrix methods replace the single equation with an eigenvalue problem.

**Study:** Rao Ch. 6 (pp. 383–458) two-DOF, Ch. 7 (pp. 459–532) modelling, Ch. 8 (pp. 533–592) free vibration and modes; [MIT 2.003SC MDOF unit](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/).
**Exam:** No question in the 2020/21 paper; check the 2023 Section B images.

- [ ] **Two-DOF system** — matrix equation of motion:
  $$M\ddot q+Kq=0$$
  Derive the frequency equation $\det(K-\omega^2M)=0$.
- [ ] **Eigenvalue problem** — natural frequencies and mode shapes:
  $$(K-\omega^2M)\phi=0,\qquad \det(K-\omega^2M)=0$$
- [ ] **Mode shapes** — nodes, orthogonality, normalisation; sketch the first two modes.
- [ ] **Nodal analysis** — build the stiffness and mass matrices by summing at nodes; boundary conditions.
- [ ] **Modal superposition** — decouple using modal coordinates; forced response as sum of modes.
- [ ] **Worked example** — two masses connected by three springs; find $\omega_1,\omega_2$ and mode shapes.

### 8. Continuous systems and approximate methods

A beam or shaft has infinite DOF. Exact solutions exist for simple geometry; approximate methods handle the rest.

**Study:** Rao Ch. 10 (pp. 633–688) continuous systems; Ch. 11 (pp. 689–736) FEM and Rayleigh–Ritz.
**Exam:** No direct question; background for the 2023 Section B.

- [ ] **Axial and torsional bars** — wave equation, fixed–fixed and free–free boundary conditions.
- [ ] **Beam bending vibration** — Euler–Bernoulli frequencies:
  $$\omega_n=\lambda_n^2\sqrt{\frac{EI}{\rho A L^4}}$$
  Learn $\lambda_n$ for fixed–fixed, simply supported and cantilever ends.
- [ ] **Rayleigh–Ritz** — assumed mode shape, minimise the quotient; one-term approximation.
- [ ] **Finite-element method** — discretise into elements, element mass and stiffness matrices, assemble, solve eigenproblem.
- [ ] **Computer solutions** — MATLAB `eig`, ANSYS/ABAQUS modal analysis; interpret mode shapes and frequencies.

### 9. Balancing and measurement

Unbalance is a rotating mass eccentricity; it produces a centrifugal force at running speed. Balancing removes it.

**Study:** Rao §4.4.2 rotating unbalance (p. 222) and §4.11 seismic vibration-measuring instruments (pp. 255–259); the lecturer's handout for the measurement definitions.
**Exam:** No direct question in 2020/21.

- [ ] **Static vs dynamic unbalance** — single-plane vs two-plane; when each applies.
- [ ] **Balancing methods** — trial mass, influence coefficients, vector diagram; residual unbalance and ISO grade.
- [ ] **Measurement chain** — accelerometer, charge amplifier, FFT analyser; why accelerometers dominate.
- [ ] **MEMS accelerometer** — proof mass, spring, damping; response below resonance; bandwidth.
- [ ] **Condition monitoring** — vibration signature, bearing frequencies, envelope analysis; predictive maintenance link.

## How to use this

Each topic has a **Study** line, an **Exam** line and a checklist. Read only the cited pages, copy the derivation once by hand, then attempt the named question with the book closed. Tick a box only when you can set up the equation yourself.

**Refresh before starting (no new textbook):** dynamics — free-body diagrams, work–energy, moment of inertia, rolling without slipping; statics — spring forces and static deflection; calculus — differentiation of sine/cosine and the chain rule; complex numbers — for the phasor solution of damped systems.

**Priority:** the equivalent-system derivation, the SHM general solution, log decrement, and magnification factor/phase curves are the whole 2020/21 paper. MDOF and continuous systems are lower yield unless the 2023 Section B confirms them.
