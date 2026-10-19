---
name: dh-01-08-1-1-emerging-technology-evaluation-fit-for-purpose-asse
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.08.1.1 Emerging Technology Evaluation & Fit-for-Purpose Assessment. Use when the user asks for Technology Scouting, Fit-for-Purpose Assessment, Feasibility Scoring. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.08.1.1 Emerging Technology Evaluation & Fit-for-Purpose Assessment

Heading: DH-01.08.1 Emerging Tech Evaluation.
Core: DH-01.08 Innovation & Emerging Technologies.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.08.1.1.1 Technology Scouting

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 10 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.08.1.1.1 Technology Scouting.
Prompt: PS-DH.01.08.1.1.1 Technology Scouting.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Draft the technology-scouting brief for {product} from candidates the operator already named.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.08.1`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded scouting brief: candidates already named; fit facts already collected; [GAP] missing scores. Do not invent readiness. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a technology readiness score, partner term, or horizon signal. Foresight scenarios stay on Technology Foresight. Prototypes stay on Prototype & Experimentation. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.08.1.1.2 Fit-for-Purpose Assessment

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 10 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.08.1.1.2 Fit-for-Purpose Assessment.
Prompt: PS-DH.01.08.1.1.2 Fit-for-Purpose Assessment.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Judge whether the named technology is fit for purpose, with a readiness verdict.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Fit-for-Purpose Assessment. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.08.1.1.3 Feasibility Scoring

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 10 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.08.1.1.3 Feasibility Scoring.
Prompt: PS-DH.01.08.1.1.3 Feasibility Scoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Score feasibility of the named technology, and mark unresolved facts [GAP].

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Feasibility Scoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
