# MCE 501 — Introduction to Robotics

*2 Units · 500 Level, Harmattan · BMAS: MCT 501 · FUTO Mechatronics*

## Overview

Robotics is the study of machines that sense, decide and act. This course builds the kinematic and sensory foundation: how a robot is built, how many ways it can move, how to describe where its hand is, and how to command it. The mathematics is coordinate geometry — but it must be exact.

Paper: 3 hours, **answer any 5 of 6**, 20 marks each. Questions are computational: mobility counts, joint types, sensors, frame mapping, DH tables, control diagrams. The 2019/2020 paper is typed; the other two are scans.

## Synopsis (BMAS, verbatim)

> "Automation and Robotics. Robot Classification. Robot Specifications. Direct Kinematics: Mathematical background. D-H representation. The Arm equation. Examples Inverse Kinematics: The inverse kinematics problem and its solution. Tool configuration. Examples of various robots. Introduction to Manipulator Dynamics: Lagrange's Equation, Lagrange-Euler Dynamic Model. Use of Sensors and Vision System in Robotic System."

## Sources

Open only the chapters named below; each topic's **Study** line narrows it further.

- **Niku, _Introduction to Robotics_** (Drive folder PDF) — Ch. 1 (pp. 1–32) anatomy, classification, specifications, applications; Ch. 2 (pp. 33–113) matrices, DH, forward and inverse kinematics; Ch. 4 (pp. 147–177) dynamics; Ch. 6 (pp. 203–265) motion control; Ch. 7 (pp. 266–318) actuators; Ch. 8 (pp. 319–349) sensors; Ch. 9 (pp. 350–422) vision.
- **Lynch & Park, _Modern Robotics_** (Drive folder PDF; free videos online) — Ch. 2 (pp. 11–58) DOF and Grübler; Ch. 3 (pp. 59–136) rigid-body motions; Ch. 4 (pp. 137–170) forward kinematics; Ch. 6 (pp. 219–244) inverse kinematics; Ch. 8 (pp. 271–324) dynamics; Ch. 11 (pp. 403–460) control.
- **Jazar, _Theory of Applied Robotics_, Ch. 5** (HOD extract) — the DH convention and arm equation your lecturer uses. Use this for DH; use Modern Robotics for the geometry behind it.
- **Choset, _An Introduction to Robot Kinematics_** (slide PDF) — pp. 5–24 DOF, Grübler and joints; pp. 38–67 frames and homogeneous transforms; pp. 68–76 worked 2R/3R forward kinematics.
- **Past papers:** 2019/2020 (typed), 2020/2021, 2021/2022. All question numbers refer to these.
- **Online:** [Modern Robotics video supplements](https://modernrobotics.northwestern.edu/) — watch only the Chapter 2, 3, 4, 6, 8 and 11 clips named in each topic.
- **Gap:** no taught notes on inverse kinematics or Lagrange dynamics; the textbook chapters cover them.
- **Not included:** textbooks and lecturer notes are not redistributed here; see [`docs/sources.md`](../docs/sources.md).

## Course Content Summary

| Concept | Importance | Exam likelihood |
|---|---|---|
| Automation and robot anatomy | Essential | High (3/3) |
| Classification and specifications | Essential | High (2/3) |
| Joint types and DOF | Essential | **Very high** (3/3) |
| Grübler/Kutzbach mobility | Essential | **Very high** (3/3) |
| Frames and transforms | Essential | High (2/3) |
| Forward kinematics and DH | Essential | **Very high** (3/3) |
| Inverse kinematics | Important | Low (0/3), BMAS |
| Manipulator dynamics | Important | Low (0/3), BMAS |
| Sensors and transducers | Essential | **Very high** (3/3) |
| Control and time response | Essential | High (3/3) |
| Actuators and motor models | Supporting | Medium (1/3) |
| Vision, end-effectors | Supporting | Medium (1/3) |

## Course Content Details

### 1. Anatomy, classification and specifications

A robot is a system: manipulator, end-effector, actuators, transmission, sensors, controller and power supply. Specifications let you choose one.

**Study:** Niku Ch. 1 (pp. 1–32) — §1.3 classification, §1.7 components, §1.13 characteristics, §1.16 applications; Modern Robotics Ch. 2 §2.5 (task space and workspace, pp. 32–36); Jazar Ch. 5 opening pages.
**Exam:** 2019/20 Q5(a), Q6(a)–(b); 2020/21 Q3(c); 2021/22 Q5(b).

- [ ] **Automation vs robotics** — fixed, programmable, flexible; hard vs soft; when a robot pays.
- [ ] **Anatomy** — base, links, joints, end-effector, actuators, transmission (gear, belt, ball screw, harmonic drive), sensors, controller.
- [ ] **Specifications** — payload, reach, DOF, accuracy vs repeatability vs resolution, speed, cycle time.
- [ ] **Geometry** — Cartesian (PPP), cylindrical (RPP), spherical (RRP), SCARA, articulated (RRR), delta; sketch workspaces.
- [ ] **Drive and control** — electric/hydraulic/pneumatic; servo vs non-servo; point-to-point vs continuous path.
- [ ] **Six basic motions** — traverse (vertical, horizontal, radial), wrist rotation, swing, roll; map to joints.

### 2. Joints and degrees of freedom

Every paper has a mobility count. Count links, classify joints, apply Grübler.

**Study:** Modern Robotics Ch. 2 §2.2–2.2.2 (pp. 15–22; Grübler on p. 17); Niku §1.8–1.9 (pp. 8–11); Choset pp. 5–24; [MR Ch. 2 videos](https://modernrobotics.northwestern.edu/).
**Exam:** 2019/20 Q1(a)–(b), Q2(a), Q3, Q5(b); 2020/21 Q3(a)–(b), Q4; 2021/22 Q5(a), Q6(a).

- [ ] **Joint types and DOF** — revolute 1, prismatic 1, helical 1, cylindrical 2, universal 2, spherical 3, planar 3.
- [ ] **Planar Grübler** — for a planar mechanism with $N$ links and $J_1$ full / $J_2$ half joints:
  $$M=3(N-1)-2J_1-J_2$$
  Identify $N$, $J_1$ and $J_2$ before substituting.
- [ ] **Spatial Kutzbach** — for a spatial mechanism:
  $$M=6(N-1)-5J_1-4J_2-3J_3-2J_4-J_5$$
- [ ] **Benchmarks** — 4-link planar chain with 9 DOF (find joint type); Delta 17 links/21 joints; quadcopter with 4 helical joints; 2R arm.
- [ ] **Changing a joint** — revolute → spherical adds DOF; universal → revolute removes one; effect on workspace and control.

### 3. Frames, rotations and homogeneous transforms

Kinematics is bookkeeping between frames. Get the convention right and the rest is matrix multiplication.

**Study:** Modern Robotics Ch. 3 §3.1–3.3 (pp. 59–110); Niku §2.4–2.7 (pp. 36–59); Choset pp. 38–67; [MR Ch. 3 videos](https://modernrobotics.northwestern.edu/).
**Exam:** 2021/22 Q3(iii), Q4; 2020/21 Q5(a).

- [ ] **Rotation matrices** — $R_x(\theta)$, $R_y(\theta)$, $R_z(\theta)$; orthonormality, $\det R=+1$, $R^{-1}=R^{\top}$, composition order.
- [ ] **Frame mapping** — a point in frame $B$ expressed in frame $A$:
  $${}^{A}P={}^{A}_{B}R\,{}^{B}P+{}^{A}P_{B_{\mathrm{org}}}$$
  Know the rotate-then-translate order and the reverse.
- [ ] **Homogeneous transform** — $4\times4$ block form; inverse by transpose and negated translation.
- [ ] **Worked mapping** — B rotated $60^\circ$ about Z and translated $(15,10,0)$ from A; map $(10,5,0)$.
- [ ] **Orientation conventions** — Euler ZYZ, roll-pitch-yaw, axis-angle, quaternions (awareness); why 3 angles fail globally.

### 4. Forward kinematics and DH

Given joint values, where is the tool? DH turns this into a product of four-parameter matrices.

**Study:** Jazar Ch. 5 (DH table and arm equation — the lecturer's convention); Niku Ch. 2 §2.8–2.12 (pp. 59–86; DH is §2.12); Choset pp. 68–76; Modern Robotics Ch. 4 (pp. 137–170) for the product-of-exponentials cross-check.
**Exam:** 2020/21 Q5(a)–(b); 2021/22 Q3(i)–(iii).

- [ ] **DH parameters** — $a_i$, $\alpha_i$, $d_i$, $\theta_i$; which is variable for revolute vs prismatic.
- [ ] **Frame assignment** — Z along joint axis, X along common normal, origin at intersection; parallel and intersecting axes.
- [ ] **DH table** — 3R planar, 3R spatial, spherical wrist; write every row.
- [ ] **Link transform** — the four-parameter DH matrix:
  $${}^{i-1}T_i=R_z(\theta_i)\,T_z(d_i)\,T_x(a_i)\,R_x(\alpha_i)$$
- [ ] **Arm equation** — multiply the link transforms, then attach the tool:
  $${}^{0}T_n={}^{0}T_1\,{}^{1}T_2\cdots{}^{n-1}T_n,\qquad {}^{0}T_{\text{tool}}={}^{0}T_n\,{}^{n}T_{\text{tool}}$$
- [ ] **Worked example** — 2R planar, $L_1=3$ cm, $L_2=2$ cm, $\theta_1=45^\circ$, $\theta_2=15^\circ$: find $x,y,\phi$.

### 5. Inverse kinematics

Given a tool pose, what joint values? Solutions may not exist, may be multiple, may be singular.

**Study:** Niku Ch. 2 §2.13–2.15 (pp. 87–96); Modern Robotics Ch. 6 (pp. 219–244); Choset pp. 25–27.
**Exam:** No direct question in the three papers; it is how you check the forward solution in 2020/21 Q5 and 2021/22 Q3.

- [ ] **Existence and uniqueness** — workspace boundary, reachable vs dexterous, elbow-up/down, flip.
- [ ] **2R analytic** — solve the elbow angle first, then the shoulder:
  $$\cos\theta_2=\frac{x^2+y^2-L_1^2-L_2^2}{2L_1L_2}$$
  $$\theta_1=\operatorname{atan2}(y,x)-\operatorname{atan2}\!\left(L_2\sin\theta_2,\;L_1+L_2\cos\theta_2\right)$$
  Keep both elbow-up and elbow-down solutions.
- [ ] **Geometric method** — law of cosines and triangle construction for a 3R planar arm.
- [ ] **Wrist decoupling** — solve wrist centre, then orientation; why 6R arms simplify.
- [ ] **Singularities** — Jacobian determinant zero, lost DOF, high joint rates; Newton–Raphson (awareness).

### 6. Manipulator dynamics

Dynamics relates torque to motion. Lagrange is an energy method: $L=T-V$, then differentiate.

**Study:** Modern Robotics Ch. 8 §8.1–8.3 (pp. 271–305); Niku Ch. 4 (pp. 147–177); [MR Ch. 8 videos](https://modernrobotics.northwestern.edu/).
**Exam:** No direct question; background for computed-torque control in 2020/21 Q2 and 2021/22 Q2.

- [ ] **Energies** — link kinetic (translation + rotation), potential, generalised force.
- [ ] **Lagrange equation** — for each generalised coordinate:
  $$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)-\frac{\partial L}{\partial q_i}=\tau_i,\qquad L=T-V$$
  Derive the one-link and two-link cases.
- [ ] **Model form** — the standard manipulator equation:
  $$M(q)\ddot q+C(q,\dot q)\dot q+g(q)=\tau$$
  Identify the inertia, Coriolis/centrifugal and gravity terms.
- [ ] **Newton–Euler** — recursive force/moment balance; computational advantage (awareness).
- [ ] **Use** — computed-torque control, payload effect, gravity compensation.

### 7. Sensors and transducers

Sensors are examined every year: classification plus one calculation. Learn the physics.

**Study:** Niku Ch. 8 (pp. 319–349) — tactile, proximity, encoders, resolvers; lecture-note headings on tactile/non-tactile sensors.
**Exam:** 2019/20 Q4(a), Q6(c); 2021/22 Q6(b)–(c).

- [ ] **Internal vs external** — encoders, resolvers, tachometers, limit switches vs tactile, force/torque, proximity, range, vision.
- [ ] **Tactile vs non-tactile** — switch, resistive, capacitive, piezoelectric vs inductive, capacitive, ultrasonic, optical, Hall, laser.
- [ ] **Proximity physics** — inductive (eddy current, metal only), capacitive (dielectric), ultrasonic (time of flight), optical (reflective/through-beam).
- [ ] **Inductive calculation** — reluctance model of the sensor coil:
  $$L=\frac{N^2}{\mathcal{R}}$$
  Relate the inductance change to the oscillator amplitude shift and the switching threshold.
- [ ] **Characteristics** — sensitivity, resolution, linearity, accuracy, range, response time, time constant, drift, dead band.
- [ ] **Selection** — material, range, environment, output (NPN/PNP, analogue), safety.

### 8. Control and response

The loop is examined as a block diagram plus a first-order calculation.

**Study:** Modern Robotics Ch. 11 §11.1–11.2 (pp. 403–430; error response and linear error dynamics); Niku Ch. 6 (pp. 203–265); [MR Ch. 11 videos](https://modernrobotics.northwestern.edu/).
**Exam:** 2020/21 Q1(a)–(d), Q2(a)–(c); 2021/22 Q2(a)–(c).

- [ ] **Block diagram** — reference → error → controller → actuator → robot → sensor → feedback; explain each block.
- [ ] **Error response** — steady-state error to step/ramp; proportional vs integral action.
- [ ] **First order** — unit-step response of a first-order loop:
  $$y(t)=K\left(1-e^{-t/\tau}\right)$$
  Read the time constant, rise time and settling time from the curve.
- [ ] **Second order** — natural frequency, damping ratio, overshoot, settling time (awareness).
- [ ] **Stability** — Routh–Hurwitz, root locus, Bode/Nyquist (awareness); why high gain oscillates.
- [ ] **PID** — joint servo loop, feedforward, computed torque, tuning intuition.

### 9. Actuators, vision and applications

Short-answer material linking mechanics to the real machine.

**Study:** Niku Ch. 7 (pp. 266–318) actuators and drives; Ch. 9 (pp. 350–422) vision overview; Niku §1.16 for applications.
**Exam:** 2021/22 Q1(a)–(c); 2019/20 Q6(b); 2021/22 Q5(b).

- [ ] **DC servo** — torque–speed curve, back-EMF, torque constant, gear ratio, reflected inertia.
- [ ] **Thermal model** — steady-state temperature rise and its time constant:
  $$P=I^2R,\qquad \Delta T=P R_{\mathrm{th}},\qquad \tau_{\mathrm{th}}=R_{\mathrm{th}}C_{\mathrm{th}}$$
- [ ] **State-space motor** — states current and speed; matrices from electrical and mechanical equations.
- [ ] **Vision** — camera model, image formation, feature extraction, pose estimation, visual servoing (overview).
- [ ] **Programming and safety** — teach pendant, lead-through, offline; work envelope, interlocks, emergency stop.

## How to use this

Each topic has a **Study** line (what to read), an **Exam** line (the questions that topic unlocks) and a checklist. Work one topic at a time: read only the cited pages, work two or three end-of-chapter problems, then attempt the named past questions with the book closed. Tick a box only when you can do that.

**Refresh before starting (no new textbook):** statics — free-body diagrams, moments and couples; dynamics — kinetic and potential energy, mass moment of inertia, work–energy; linear algebra — matrix multiplication, transpose, inverse, 3×3 determinant; trigonometry — sine and cosine rules, compound angles.

**Priority:** mobility counts, joint types, the 2R forward solution and the sensor classifications are near-certain marks. DH and frame mapping are the next tier. Inverse kinematics and Lagrange dynamics are in the synopsis but absent from all three papers — leave them until the rest is solid.
