---
name: "DH-01.06.3.1 Sustained Engagement Pattern Design & Behavioural Mechanics Implementation"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.06.3.1 Sustained Engagement Pattern Design & Behavioural Mechanics Implementation. Use when the user asks for Behavioural Mechanics Design, Engagement Loop Construction, Adherence Optimisation. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.06.3.1 Sustained Engagement Pattern Design & Behavioural Mechanics Implementation

Heading: DH-01.06.3 Engagement Mechanics.
Core: DH-01.06 Digital Therapeutic Design.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.06.3.1.1 Behavioural Mechanics Design

Worker: Behavior-Change Designer (`behavior-change-designer`). 9 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.3.1.1 Behavioural Mechanics Design.
Prompt: PS-DH.01.06.3.1.1 Behavioural Mechanics Design.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Draft the behavioral-mechanics design for {product} from engagement facts the operator already has.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.06.3`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded mechanics brief: loops already named; adherence facts already decided; [GAP] missing loops. Do not invent retention. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a mechanism, safety claim, or engagement outcome. Patient hubs / adherence programs stay on PS-06.01. Adaptive logic stays on Personalization Engine. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.3.1.2 Engagement Loop Construction

Worker: Behavior-Change Designer (`behavior-change-designer`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.3.1.2 Engagement Loop Construction.
Prompt: PS-DH.01.06.3.1.2 Engagement Loop Construction.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Construct the engagement loop, with adherence metrics and the evidence behind each mechanic.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Engagement Loop Construction. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.3.1.3 Adherence Optimisation

Worker: Behavior-Change Designer (`behavior-change-designer`). 9 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.3.1.3 Adherence Optimisation.
Prompt: PS-DH.01.06.3.1.3 Adherence Optimisation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Optimize adherence without manipulation, and state the trade-offs.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Adherence Optimisation. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
