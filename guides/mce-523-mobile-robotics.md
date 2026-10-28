# MCE 523 — Mobile Robotics

*2 Units · 500 Level, Harmattan · BMAS analogue: MCT 521 · FUTO Mechatronics*

## Overview

A mobile robot is a machine that moves through an unknown world, decides where it is, and chooses where to go next. This course joins mechanical locomotion, sensors, computer vision, localisation and artificial intelligence into one autonomous system.

Papers are short-answer and explanatory: define, classify, compare, sketch a block diagram, explain a method. Three papers are available (2019, 2020/2021, 2021/2022).

**Note on scope:** BMAS MCT 521 is written as an artificial-intelligence course. The FUTO course is broader — locomotion, perception, SLAM and planning — with AI as one component. The taught textbook and papers define the balance.

## Synopsis (BMAS MCT 521, verbatim)

> "Artificial intelligence programming techniques, basic problem solving techniques, knowledge acquisition and representation; artificial intelligent language (LISP and PROLOG). Computer interface, machine learning, natural language understanding, knowledge-based and expert systems, computer vision, robotics, relationship AI to software engineering and database methodology. Societal impact of AI and robotics. Machine vision and pattern recognition. Applications of identification trees, neural nets, genetics algorithms and other learning paradigms."

## Sources

- **Siegwart, Nourbakhsh & Scaramuzza, _Introduction to Autonomous Mobile Robots_** (Drive folder PDF) — Ch. 1 (pp. 1–12) overview; Ch. 2 (pp. 13–46) locomotion; Ch. 3 (pp. 47–88) kinematics, maneuverability, workspace; Ch. 4 (pp. 89–180) perception, sensors, feature extraction; Ch. 5 (pp. 181–256) localisation; Ch. 6 (pp. 257–320) planning and navigation; Ch. 7 application studies.
- **Lynch & Park, _Modern Robotics_ Ch. 13** (Drive folder PDF; free videos) — wheeled mobile robots, omnidirectional wheels, nonholonomic constraints, odometry.
- **_MCE 523 – Machine Vision_** (7 pp., typed) — machine-vision system types, camera calibration, stereopsis.
- **_Mobile Robotics Class Notes_** — handwritten scans; use only as a topic checklist.
- **Past papers:** 2019/2020, 2020/2021, 2021/2022. Question numbers below refer to these.
- **Gap:** SLAM mathematics and ROS are not taught; the textbook covers SLAM theory, and ROS is not examinable.

- **Not included:** textbooks and lecturer notes are not redistributed here; see [\docs/sources.md\](../docs/sources.md).

## Course Content Summary

| Concept | Importance | Exam likelihood |
|---|---|---|
| Locomotion and kinematics | Essential | High (2/3) |
| Sensors: proprioceptive and exteroceptive | Essential | **Very high** (3/3) |
| Perception and computer vision | Essential | **Very high** (3/3) |
| Localisation and mapping (SLAM) | Essential | Medium (1/3) |
| Path planning and obstacle avoidance | Essential | High (2/3) |
| Control architectures | Important | Medium (1/3) |
| AI, machine learning and RL | Essential | **Very high** (3/3) |
| Robot programming and ROS | Supporting | Low |
| Applications and societal impact | Supporting | Medium |
| Actuators and drives | Supporting | Medium (1/3) |

## Course Content Details

### 1. Locomotion and kinematics

Locomotion is how the robot moves; kinematics is how its wheel or leg speeds become a body velocity.

**Study:** Siegwart Ch. 2 (pp. 13–46) locomotion and Ch. 3 (pp. 47–88) kinematics and constraints; Modern Robotics Ch. 13 §13.1–13.3 (free) for the wheel-constraint derivation.
**Exam:** 2019/20 Q1 (applications), Q5 (Grübler mobility); 2020/21 Q1 (obstacle sensor, indirectly).

- [ ] **Locomotion types** — wheeled, legged, tracked, hopping, flying, swimming; terrain and efficiency trade-offs.
- [ ] **Wheel configurations** — differential drive, Ackermann, synchronous, omnidirectional, mecanum; sketch each.
- [ ] **Differential drive kinematics** — linear and angular velocity from the wheel speeds:
  $$v=\frac{v_r+v_l}{2},\qquad \omega=\frac{v_r-v_l}{L}$$
  Derive the forward and inverse mapping to $(x,y,\theta)$.
- [ ] **Non-holonomic constraints** — no sideways slip; why a car cannot move sideways; holonomic vs non-holonomic.
- [ ] **Odometry** — integrate wheel encoder counts; systematic and non-systematic errors; drift.
- [ ] **Degrees of freedom** — chassis DOF vs wheel DOF; omnidirectional platforms.

### 2. Sensors

A mobile robot needs to know its own state and the world. Sensors are classified by what they measure and where the measurement originates.

**Study:** Siegwart Ch. 4 §4.1 (pp. 89–145) — classification, performance, wheel/heading sensors, beacons, ranging, vision; _Machine Vision_ notes §1.1.
**Exam:** 2020/21 Q1(a)–(d), Q5(a)–(b); 2021/22 Sec B Q1(a)–(b).

- [ ] **Proprioceptive vs exteroceptive** — encoders, IMU, gyro, compass vs ultrasonic, infrared, laser, camera, GPS; table of what each measures.
- [ ] **Active vs passive** — emit energy vs receive ambient; examples and trade-offs.
- [ ] **Range sensors** — ultrasonic (time of flight, cone, specular reflection), infrared (triangulation, intensity), laser scanner (2-D/3-D, scan rate).
- [ ] **Inertial sensors** — accelerometer, gyroscope, magnetometer; bias, drift, integration error.
- [ ] **GPS** — trilateration, accuracy, indoor failure; differential GPS.
- [ ] **Sensor selection** — range, resolution, field of view, cost, power, environment; fusion rationale.

### 3. Perception and computer vision

Perception turns raw signals into a model of the world. Vision is the richest and hardest modality.

**Study:** Siegwart Ch. 4 §4.1.8 (pp. 117–145) and §4.3 (feature extraction); _Machine Vision_ notes §1.1–1.2; Modern Robotics Ch. 13 §13.4 (odometry).
**Exam:** 2020/21 Q5, Q6; 2021/22 Sec B Q3.

- [ ] **Image formation** — pinhole model, intrinsics, extrinsics, lens distortion; pixel to ray.
- [ ] **Camera calibration** — chessboard, intrinsic/extrinsic parameters, reprojection error.
- [ ] **Features** — edges, corners, blobs; Harris, SIFT/SURF/ORB (awareness); descriptor matching.
- [ ] **Stereo vision** — depth from disparity:
  $$Z=\frac{fb}{d}$$
  Cover rectification and stereo matching.
- [ ] **Omnidirectional vision** — catadioptric mirror, panoramic image, unwrapping; advantages for navigation.
- [ ] **Object recognition** — classical pipeline vs CNN; training data, accuracy, real-time constraints.
- [ ] **Visual servoing** — image-based vs position-based; closed-loop control from camera feedback.

### 4. Localisation and mapping

Localisation answers "where am I?"; mapping answers "what does the world look like?"; SLAM does both at once.

**Study:** Siegwart Ch. 5 (pp. 181–256) — Bayes, Kalman and particle filters, mapping.
**Exam:** No direct question; it is the theory behind 2020/21 Q2 (RFID identification) and any SLAM variant.

- [ ] **Dead reckoning** — odometry + IMU; error growth; why it cannot stand alone.
- [ ] **Map representations** — occupancy grid, feature map, topological map, point cloud; resolution and memory.
- [ ] **Markov and Kalman localisation** — belief, prediction, update; extended Kalman filter for nonlinear motion.
- [ ] **Particle filter** — Monte Carlo localisation, samples, weights, resampling; kidnapped-robot problem.
- [ ] **SLAM** — simultaneous localisation and mapping; EKF-SLAM, graph SLAM, loop closure (awareness).
- [ ] **Landmarks** — natural vs artificial; data association; consistency.

### 5. Path planning and obstacle avoidance

Planning finds a route; obstacle avoidance keeps the robot alive while following it.

**Study:** Siegwart Ch. 6 (pp. 257–320) planning and navigation; Modern Robotics Ch. 10 (graph search, potential fields) for the algorithms.
**Exam:** 2020/21 Q1 (obstacle detection and avoidance).

- [ ] **Configuration space** — robot as a point, obstacles grown by the robot radius; C-space obstacles.
- [ ] **Graph search** — Dijkstra, A*, heuristic admissibility; grid vs roadmap.
- [ ] **Sampling planners** — RRT, PRM; probabilistic completeness; narrow passages.
- [ ] **Reactive avoidance** — bug algorithms, potential fields, vector field histogram; local minima.
- [ ] **Coverage and exploration** — frontier-based exploration, lawnmower coverage; when each applies.
- [ ] **Trajectory generation** — smooth paths, curvature limits, velocity profiles, dynamic constraints.

### 6. Control architectures

Architecture decides how perception, planning and actuation are organised — and what happens when they disagree.

**Study:** Siegwart Ch. 3 §3.6 (motion control) and Ch. 6 (navigation and control); Modern Robotics Ch. 11 (control) for the loop.
**Exam:** 2019/20 Q3–Q4 (servo model and parameter calculation); 2021/22 Q1 (inverter).

- [ ] **Deliberative** — sense–plan–act; world model; slow but optimal.
- [ ] **Reactive** — behaviour-based, subsumption; fast, no model, local traps.
- [ ] **Hybrid** — three-layer architecture; planner, sequencer, controller.
- [ ] **Behaviour arbitration** — priority, fusion, voting; example of wall-following plus obstacle avoidance.
- [ ] **Control loops** — PID for heading and speed; trajectory tracking; dead reckoning correction.

### 7. Artificial intelligence and learning

The BMAS core: how a robot represents knowledge and improves with experience.

**Study:** class notes on AI definitions and factors; Russell & Norvig, _AI: A Modern Approach_ Ch. 1–3 (agents, search) only if the notes are unclear.
**Exam:** 2020/21 Q3, Q4.

- [ ] **AI fundamentals** — definition, strong vs weak AI, agents, environments; factors affecting AI (data, compute, algorithms).
- [ ] **Search and problem solving** — state space, BFS/DFS, heuristic search, game trees.
- [ ] **Knowledge representation** — logic, rules, semantic networks, frames, ontologies; expert systems.
- [ ] **Machine learning** — supervised, unsupervised, reinforcement; training vs inference; overfitting.
- [ ] **Reinforcement learning** — state, action, reward, policy, value; Q-learning and policy gradient (awareness).
- [ ] **Neural networks** — perceptron, layers, activation, backpropagation; CNN for vision.
- [ ] **Other paradigms** — genetic algorithms, fuzzy logic, identification trees; LISP/PROLOG (historical).

### 8. Programming, applications and society

Short-answer material that connects the theory to deployed robots.

**Study:** Siegwart Ch. 7 (application studies); class notes on applications and society.
**Exam:** 2019/20 Q1 (five application areas); 2020/21 Q2 (RFID stolen-item detection).

- [ ] **Robot software** — ROS nodes, topics, services, tf; simulation (Gazebo); why middleware matters.
- [ ] **Applications** — warehouse AGV, agricultural robot, medical delivery, planetary rover, drone, service robot.
- [ ] **Societal impact** — employment, safety, privacy, liability, regulation; ethical design.
- [ ] **Actuators and drives** — DC motor, BLDC, stepper, servo; inverter and PWM; battery and power budget.
- [ ] **System integration** — payload, compute, power, communication; failure modes and fail-safe behaviour.

## How to use this

Each topic has a **Study** line, an **Exam** line and a checklist. The paper mixes definitions, diagrams and one numerical question: read the cited pages, draw the sensor/kinematic diagram, then answer the named questions. Tick a box when you can explain the principle and sketch it.

**Refresh before starting (no new textbook):** kinematics — relative velocity, wheel rolling constraints; linear algebra — matrix multiplication and 2×2 inverse; probability — conditional probability and Gaussian basics (for localisation); circuits — resistor–inductor transients for the 2021/22 Q1/Q3 questions.

**Priority:** sensors and their interfacing, camera/stereopsis, AI definitions, and applications are repeated. Kinematics and localisation are conceptually heavier but appear less often. If time is short, secure the descriptive questions first.
