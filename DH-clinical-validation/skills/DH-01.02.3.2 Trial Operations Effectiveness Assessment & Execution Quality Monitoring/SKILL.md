---
name: "DH-01.02.3.2 Trial Operations Effectiveness Assessment & Execution Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.02.3.2 Trial Operations Effectiveness Assessment & Execution Quality Monitoring. Use when the user asks for Trial Execution Quality Monitoring, trial operations pass rule, trial operations miss owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.3.2 Trial Operations Effectiveness Assessment & Execution Quality Monitoring

Heading: DH-01.02.3 Clinical Operations.
Core: DH-01.02 Clinical Validation & Evidence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.02.3.2.1 Trial Execution Quality Monitoring

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.3.2.1 Trial Execution Quality Monitoring.
Prompt: PS-DH.01.02.3.2.1 DH-01.02.3.2.1 Trial Execution Quality Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.3.2.1 Trial Execution Quality Monitoring

### Task
Watch trial-ops quality so execution does not silently fail, and list the ops gaps.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.3.2.1 Trial Execution Quality Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Compare the plan the buyer supplied with the result the buyer supplied.


## DH-01.02.3.2.2 trial operations pass rule

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.3.2.2 trial operations pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Write the pass rule in the buyer's words.


## DH-01.02.3.2.3 trial operations miss owner

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.3.2.3 trial operations miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Name the owner the buyer named.
