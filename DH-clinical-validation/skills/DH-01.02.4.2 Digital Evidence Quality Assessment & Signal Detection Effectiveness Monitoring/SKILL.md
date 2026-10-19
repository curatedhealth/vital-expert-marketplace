---
name: "DH-01.02.4.2 Digital Evidence Quality Assessment & Signal Detection Effectiveness Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.02.4.2 Digital Evidence Quality Assessment & Signal Detection Effectiveness Monitoring. Use when the user asks for Digital Signal Detection Monitoring, digital evidence pass rule, digital evidence miss owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.2 Digital Evidence Quality Assessment & Signal Detection Effectiveness Monitoring

Heading: DH-01.02.4 Digital Evidence Generation.
Core: DH-01.02 Clinical Validation & Evidence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.02.4.2.1 Digital Signal Detection Monitoring

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.2.1 Digital Signal Detection Monitoring.
Prompt: PS-DH.01.02.4.2.1 DH-01.02.4.2.1 Digital Signal Detection Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.4.2.1 Digital Signal Detection Monitoring

### Task
Watch whether digital-signal detection is valid enough to use as evidence, and list invalid detections.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.4.2.1 Digital Signal Detection Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Compare the signal rule the buyer supplied with the result already retrieved.


## DH-01.02.4.2.2 digital evidence pass rule

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.2.2 digital evidence pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Write the pass rule in the buyer's words.


## DH-01.02.4.2.3 digital evidence miss owner

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.2.3 digital evidence miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Name the owner the buyer named.
