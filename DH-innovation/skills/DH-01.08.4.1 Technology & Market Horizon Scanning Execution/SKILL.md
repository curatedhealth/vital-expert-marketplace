---
name: "DH-01.08.4.1 Technology & Market Horizon Scanning Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.08.4.1 Technology & Market Horizon Scanning Execution. Use when the user asks for Signal Collection, Signal Triage & Filtering, Disruption Assessment. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.08.4.1 Technology & Market Horizon Scanning Execution

Heading: DH-01.08.4 Horizon Scanning.
Core: DH-01.08 Innovation & Emerging Technologies.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.08.4.1.1 Signal Collection

Worker: Chief Digital Health Officer (`chief-digital-health-officer`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.08.4.1.1 Signal Collection.
Prompt: PS-DH.01.08.4.1.1 Signal Collection.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Draft the horizon-signal collection brief for {product} from sources the operator already named.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.08.4`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded collection brief: sources already named; triage already decided; [GAP] missing sources. Do not invent a disruption. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a technology readiness score, partner term, or horizon signal. Foresight scenarios stay on Technology Foresight. Leftover USR shells stay unsigned and are not this front. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.08.4.1.2 Signal Triage & Filtering

Worker: Chief Digital Health Officer (`chief-digital-health-officer`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.08.4.1.2 Signal Triage & Filtering.
Prompt: PS-DH.01.08.4.1.2 Signal Triage & Filtering.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Triage and filter horizon signals so noise does not enter the map.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Signal Triage & Filtering. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.08.4.1.3 Disruption Assessment

Worker: Chief Digital Health Officer (`chief-digital-health-officer`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.08.4.1.3 Disruption Assessment.
Prompt: PS-DH.01.08.4.1.3 Disruption Assessment.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Assess which signals would disrupt the current play, and state the evidence.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Disruption Assessment. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
