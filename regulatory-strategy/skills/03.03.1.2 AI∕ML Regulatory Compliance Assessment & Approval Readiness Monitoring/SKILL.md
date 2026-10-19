---
name: "AI/ML Regulatory Compliance Assessment & Approval Readiness Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in 03.03.1.2 AI/ML Regulatory Compliance Assessment & Approval Readiness Monitoring. Use when the user asks for AI/ML Approval Readiness Monitoring, AI/ML regulatory readiness pass rule, AI/ML regulatory readiness miss owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# 03.03.1.2 AI/ML Regulatory Compliance Assessment & Approval Readiness Monitoring

Heading: 03.03.1 AI/ML Regulatory.
Core: DH-03.03 Regulatory Strategy & Submissions.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## 03.03.1.2.1 AI/ML Approval Readiness Monitoring

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 31 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.1.2.1 AI/ML Approval Readiness Monitoring.
Prompt: PS-DH.03.03.1.2.1 AI/ML Approval Readiness Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Watch AI/ML approval readiness before you file, and list PCCP or pathway gaps.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for AI/ML Approval Readiness Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## 03.03.1.2.2 AI/ML regulatory readiness pass rule

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 27 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.1.2.2 AI/ML regulatory readiness pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## 03.03.1.2.3 AI/ML regulatory readiness miss owner

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 27 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.1.2.3 AI/ML regulatory readiness miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.
