---
name: "DH-01.06.1.1 Adaptive Intervention Design & Personalisation Engine Development"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.06.1.1 Adaptive Intervention Design & Personalisation Engine Development. Use when the user asks for Adaptive Logic Design, Personalisation Model Development, Tailoring Rule Validation. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.06.1.1 Adaptive Intervention Design & Personalisation Engine Development

Heading: DH-01.06.1 Personalization Engine.
Core: DH-01.06 Digital Therapeutic Design.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.06.1.1.1 Adaptive Logic Design

Worker: Behavior-Change Designer (`behavior-change-designer`). 10 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.1.1.1 Adaptive Logic Design.
Prompt: PS-DH.01.06.1.1.1 Adaptive Logic Design.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Draft the adaptive-logic design for {product} from tailoring rules the operator already named.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.06.1`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded logic brief: rules already named; inputs already decided; [GAP] missing rules. Do not invent an efficacy claim. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a mechanism, safety claim, or engagement outcome. Safety claims stay on Safety & Efficacy. Engagement loops stay on Engagement Mechanics. Platform stays on DTx Architecture. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.1.1.2 Personalisation Model Development

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 17 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.1.1.2 Personalisation Model Development.
Prompt: PS-DH.01.06.1.1.2 Personalisation Model Development.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Specify the personalization model, with the safety rationale behind each rule.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Personalisation Model Development. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.1.1.3 Tailoring Rule Validation

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.1.1.3 Tailoring Rule Validation.
Prompt: PS-DH.01.06.1.1.3 Tailoring Rule Validation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Validate tailoring rules so personalization does not drift into unsafe behavior.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Tailoring Rule Validation. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
