---
name: dh-01-02-1-2-study-design-quality-assessment-protocol-robustness
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.02.1.2 Study Design Quality Assessment & Protocol Robustness Monitoring. Use when the user asks for Protocol Robustness Monitoring, protocol robustness pass rule, protocol robustness miss owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.1.2 Study Design Quality Assessment & Protocol Robustness Monitoring

Heading: DH-01.02.1 Clinical Study Design.
Core: DH-01.02 Clinical Validation & Evidence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.02.1.2.1 Protocol Robustness Monitoring

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 17 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.1.2.1 Protocol Robustness Monitoring.
Prompt: PS-DH.01.02.1.2.1 DH-01.02.1.2.1 Protocol Robustness Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.1.2.1 Protocol Robustness Monitoring

### Task
Score whether the protocol and endpoints will hold up under review, and list the robustness gaps.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.1.2.1 Protocol Robustness Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Check the protocol text the buyer supplied.


## DH-01.02.1.2.2 protocol robustness pass rule

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 17 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.1.2.2 protocol robustness pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Write the pass rule in the buyer's words.


## DH-01.02.1.2.3 protocol robustness miss owner

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 17 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.1.2.3 protocol robustness miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Name the owner the buyer named.
