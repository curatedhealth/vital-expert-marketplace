---
name: dh-03-01-2-2
description: "Only while the Digital Health Library connector is connected. Run one task in 03.01.2.2 Coding & Pricing Effectiveness Assessment & Contract Performance Monitoring. Use when the user asks for Contract Performance Monitoring, coding and pricing pass rule, coding and pricing miss owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# 03.01.2.2 Coding & Pricing Effectiveness Assessment & Contract Performance Monitoring

Heading: 03.01.2 Coding, Pricing & Contracting.
Core: DH-03.01 Market Access & Reimbursement.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## 03.01.2.2.1 Contract Performance Monitoring

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.2.2.1 Contract Performance Monitoring.
Prompt: PS-DH.03.01.2.2.1 Contract Performance Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Watch coding, price, and contract performance after close, and list drift.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Contract Performance Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound. Not the Market Access roof (`PS-04.02`).

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Compare the contract terms the buyer supplied with the result the buyer supplied.

## 03.01.2.2.2 coding and pricing pass rule

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.2.2.2 coding and pricing pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Write the pass rule in the buyer's words.

## 03.01.2.2.3 coding and pricing miss owner

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.2.2.3 coding and pricing miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Name the owner the buyer named.
