---
name: dh-01-05-4-1-strategy-to-operations-translation-execution-leader
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.05.4.1 Strategy-to-Operations Translation & Execution Leadership. Use when the user asks for Operating Model Design, Roadmap & Milestone Planning, Execution Governance. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.05.4.1 Strategy-to-Operations Translation & Execution Leadership

Heading: DH-01.05.4 Execution Leadership.
Core: DH-01.05 Digital Health Strategy & Vision.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.05.4.1.1 Operating Model Design

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.4.1.1 Operating Model Design.
Prompt: PS-DH.01.05.4.1.1 Operating Model Design.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Draft the operating-model brief for {product} from the vision already decided.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.05.4`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded operating-model brief: owners already named; milestones already decided; [GAP] missing owners. Do not invent a budget. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a market size, competitor share, or build-partner-buy decision. Vision stays on Strategic Vision. Health-system adoption stays on hidden PS-DH.02.02 until suites exist. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.05.4.1.2 Roadmap & Milestone Planning

Worker: Behavior-Change Designer (`behavior-change-designer`). 32 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.4.1.2 Roadmap & Milestone Planning.
Prompt: PS-DH.01.05.4.1.2 Roadmap & Milestone Planning.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Sequence the roadmap and milestones with explicit dependencies.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Roadmap & Milestone Planning. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.05.4.1.3 Execution Governance

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 28 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.4.1.3 Execution Governance.
Prompt: PS-DH.01.05.4.1.3 Execution Governance.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Set execution governance so the roadmap can be steered without silent drift.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Execution Governance. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
