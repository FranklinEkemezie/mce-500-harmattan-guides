# MCE 515 — Project I

*3 Units · 500 Level, Harmattan · BMAS analogue: MCT 599 / MCT 413 · FUTO Mechatronics*

## Overview

Project I is the first half of the final-year project. You choose an engineering problem, prove it is worth solving, review what others have done, and produce a defensible design and work plan. The deliverable is a proposal and interim report, not a finished machine — but the design must be buildable in Project II.

There is no written examination. Assessment is continuous: topic approval, proposal, literature review, progress reports, and an interim presentation/defence. Marks reward method, evidence and clarity, not ambition.

**Note on scope:** there is no BMAS entry for MCE 515. The closest official descriptions are MCT 599 Final Year Project (6 units) and MCT 413 Group Project (2 units), quoted below. The rest of this guide is standard final-year project practice.

## Synopsis (BMAS analogues, verbatim)

> **MCT 599:** "Final Year Project (6 Units: PH 270) Undergraduate Project."
>
> **MCT 413:** "Group Project (2 Units: PH 90) Identifying problem requirements. Generating and evaluating design concepts; design and fabrication. Design control software. Testing and debugging of systems. Documentation of design and results."

## Sources

- **BMAS MCT 599 and MCT 413** — the only official scope statements for the project.
- **Kumar, _Research Methodology: A Step-by-Step Guide for Beginners_** — use the chapters by title: formulating a research problem; reviewing the literature; research design; constructing an instrument; selecting a sample; ethics. These map directly onto topics 1–4 and 8.
- **Creswell, _Research Design_** — Ch. 1 (selecting an approach), Ch. 2 (literature review), Ch. 3 (theory), Ch. 4 (writing strategies and ethics). Read only the chapter that matches your project type.
- **Beer & McMurrey, _A Guide to Writing as an Engineer_** — proposal, report-writing, graphics and oral-presentation chapters.
- **[Purdue OWL IEEE style](https://owl.purdue.edu/owl/research_and_citation/ieee_style/ieee_overview.html)** — general format, in-text citation, reference list, tables and figures. This is the citation standard to follow.
- **FUTO project guidelines** — departmental format for proposal, report and defence; confirm the current edition with your supervisor.
- **Gap:** no past papers or marked reports; the deliverables below are inferred from typical Nigerian departmental practice.

- **Not included:** textbooks and lecturer notes are not redistributed here; see [\docs/sources.md\](../docs/sources.md).

## Course Content Summary

| Component | Importance | Assessment weight |
|---|---|---|
| Topic selection and scope | Essential | High (approval gate) |
| Problem statement and objectives | Essential | **Very high** |
| Literature review | Essential | **Very high** |
| Methodology and design | Essential | **Very high** |
| Simulation and modelling | Important | Medium |
| Prototyping and fabrication plan | Important | Medium |
| Testing and validation plan | Important | Medium |
| Technical writing and format | Essential | **Very high** |
| Presentation and defence | Essential | High |
| Project management and ethics | Supporting | Medium |

## Course Content Details

### 1. Topic selection and scope

A good project is narrow enough to finish and broad enough to matter. Scope creep is the main reason projects fail.

**Study:** Kumar, the "Formulating a research problem" chapter (topic, scope, feasibility); Beer & McMurrey, the proposal/planning chapter; your department's project guidelines (confirm the current edition with your supervisor).
**Exam:** No paper. Deliverable: a one-page topic brief — title, scope, deliverables, constraints.

- [ ] **Problem source** — industry attachment, staff research, community need, existing system weakness; keep a one-page justification.
- [ ] **Feasibility** — technical (skills, tools), economic (budget), time (two semesters), ethical and safety.
- [ ] **Scope statement** — what is in, what is out, and the boundary conditions; one paragraph you can defend.
- [ ] **Title** — specific, measurable, no "design and construction of a modern…"; include the variable and the method.
- [ ] **Supervisor fit** — expertise, availability, laboratory access; agree expectations in writing.
- [ ] **Approval gate** — departmental topic form, signed; keep copies of every submission.

### 2. Problem statement and objectives

The problem statement says what is wrong and why it matters; the objectives say what you will do about it.

**Study:** Kumar, "Formulating a research problem" (problem statement, aim, objectives, hypotheses); Creswell Ch. 1 (choosing an approach) and Ch. 3 (the use of theory).
**Exam:** No paper. Deliverable: problem statement, aim, and 3–5 SMART objectives.

- [ ] **Background** — context, current practice, cost or risk of the status quo; cite evidence.
- [ ] **Problem statement** — one paragraph: gap, consequence, why now; no solution language.
- [ ] **Aim** — one sentence, broad but bounded.
- [ ] **Specific objectives** — 3–5 measurable verbs (design, model, fabricate, test, evaluate); each maps to a chapter.
- [ ] **Research questions** — optional for engineering, useful for evaluation projects.
- [ ] **Success criteria** — quantitative targets (accuracy, response time, cost, efficiency) set before design.

### 3. Literature review

The review proves you know the field and shows the gap your project fills. It is not a summary of every paper you found.

**Study:** Kumar, "Reviewing the literature"; Creswell Ch. 2; [Purdue OWL IEEE reference list](https://owl.purdue.edu/owl/research_and_citation/ieee_style/ieee_overview.html) for formatting.
**Exam:** No paper. Deliverable: 15–25 reviewed sources with a written gap statement.

- [ ] **Search strategy** — keywords, databases (IEEE Xplore, ScienceDirect, Google Scholar), inclusion/exclusion criteria; record searches.
- [ ] **Source quality** — peer-reviewed journals, conference papers, standards, textbooks; avoid blogs and undated web pages.
- [ ] **Thematic structure** — group by method or sub-problem, not by author; compare approaches in tables.
- [ ] **Critical appraisal** — strengths, limitations, assumptions, conflicting results; state your position.
- [ ] **Gap statement** — what is missing, and how your project addresses it; one paragraph.
- [ ] **Citation practice** — IEEE numeric style, consistent; reference manager (Zotero/Mendeley); never cite unread work.

### 4. Methodology and design

Methodology is the logic of the project; design is the engineering. Both must be reproducible.

**Study:** Kumar, "Research design", "Constructing an instrument for data collection" and "Selecting a sample"; Creswell Ch. 1.
**Exam:** No paper. Deliverable: methodology chapter with block diagram, materials, and test plan.

- [ ] **Methodology type** — analytical, experimental, simulation, design-and-build, case study; justify the choice.
- [ ] **System architecture** — block diagram, subsystems, interfaces, data and power flow.
- [ ] **Design calculations** — load, torque, power, material, tolerance, thermal; show units and assumptions.
- [ ] **Component selection** — specifications, datasheets, availability, cost; a selection matrix with weights.
- [ ] **CAD and drawings** — assembly, part drawings, dimensions, tolerances, bill of materials.
- [ ] **Risk and mitigation** — technical, schedule, safety, ethics; a short risk register.

### 5. Simulation, prototyping and testing

Project I should prove the concept on paper or in simulation; Project II builds it.

**Study:** no textbook chapter — use your CAD/analysis tool documentation; Beer & McMurrey, the chapter on reporting data and graphics.
**Exam:** No paper. Deliverable: results chapter with figures and an error/uncertainty discussion.

- [ ] **Modelling** — MATLAB/Simulink, ANSYS, Proteus, SolidWorks, Python; state assumptions and boundary conditions.
- [ ] **Simulation plan** — cases, parameters, expected outputs, validation against theory or literature.
- [ ] **Prototype plan** — breadboard, 3D print, machined parts; what is proved at each stage.
- [ ] **Test plan** — variables, instruments, sample size, acceptance criteria, safety.
- [ ] **Data analysis** — mean, deviation, error, regression, plots; choose the analysis before collecting data.
- [ ] **Ethics** — informed consent, animal/human subjects, hazardous materials, plagiarism, authorship.

### 6. Technical writing and format

Marks are lost on presentation. Follow the departmental format exactly and write in plain, precise English.

**Study:** Beer & McMurrey, the report-writing and source-documentation chapters; [Purdue OWL IEEE general format, in-text citation and reference list](https://owl.purdue.edu/owl/research_and_citation/ieee_style/ieee_overview.html).
**Exam:** No paper. Deliverable: full report in the departmental format.

- [ ] **Structure** — title page, declaration, certification, dedication, acknowledgements, abstract, table of contents, list of figures/tables, chapters, references, appendices.
- [ ] **Chapter logic** — Introduction → Literature Review → Methodology → Design/Implementation → Results → Discussion → Conclusion.
- [ ] **Figures and tables** — numbered, captioned, referenced in text, readable in black and white.
- [ ] **Equations** — numbered, symbols defined, units consistent; use an equation editor.
- [ ] **Referencing** — IEEE style, every claim cited, no orphan references; check plagiarism report.
- [ ] **Editing** — one idea per paragraph, active voice, consistent tense, proofread aloud, check page limits.

### 7. Presentation and defence

The defence tests whether you understand your own work. Prepare for the question, not just the slide.

**Study:** Beer & McMurrey, the oral-presentation chapter; Purdue OWL "Writing in Engineering" for slide text.
**Exam:** No paper. Deliverable: 10–12 slides and a five-minute defence.

- [ ] **Slide deck** — 10–15 slides: problem, aim, objectives, literature gap, method, design, expected results, timeline, references.
- [ ] **Timing** — rehearse to 80% of the allotted time; leave room for questions.
- [ ] **Visuals** — one message per slide, large fonts, diagrams over text, consistent template.
- [ ] **Delivery** — eye contact, pace, avoid reading; define acronyms; practise with a colleague.
- [ ] **Question bank** — why this method, why this component, what if it fails, cost, novelty, limitations.
- [ ] **Panel etiquette** — listen fully, answer directly, admit uncertainty, take notes, thank the panel.

### 8. Project management and ethics

A project is delivered by managing time, people and records — not by working harder at the end.

**Study:** Kumar, the "Ethics in research" chapter; Creswell Ch. 4 (ethical considerations); departmental supervision and safety rules.
**Exam:** No paper. Deliverable: Gantt chart, risk register and ethics/safety checklist.

- [ ] **Work breakdown** — tasks, durations, dependencies; Gantt chart across both semesters.
- [ ] **Milestones** — proposal, literature review, design freeze, simulation, interim report, defence.
- [ ] **Supervision** — weekly log, agenda, decisions recorded; bring work, not just questions.
- [ ] **Records** — laboratory notebook, datasheets, receipts, code repository, version control.
- [ ] **Professional ethics** — honesty in results, safety of participants, environmental impact, confidentiality.
- [ ] **Contingency** — 20% time buffer; a fallback design if a component is unavailable.

## How to use this

There is no exam paper: the "Exam" line names the **deliverable** that proves the topic. Work in order, because each deliverable feeds the next. Tick a box when the deliverable is written and your supervisor has seen it.

**Refresh before starting (no new textbook):** technical writing — paragraph structure, active voice, figure captions; referencing — IEEE in-text numbering and reference-list order; basic statistics — mean, standard deviation, error bars.

**Priority:** problem statement and literature review carry the most weight in a project grade, and they are the two that students rush. Write them first and revise them last. Do not start building until the methodology chapter is approved.
