---
name: "DH-01.02.2.2.1 Message Impact Monitoring"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.2.2 Evidence Communication Effectiveness Assessment & Message Impact Monitoring is chosen, to do DH-01.02.2.2.1 Message Impact Monitoring."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.2.2.1 Message Impact Monitoring

## Execution formula
Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 13 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.2.2.1 Message Impact Monitoring.
Prompt: PS-DH.01.02.2.2.1 DH-01.02.2.2.1 Message Impact Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# DH-01.02.2.2.1 Message Impact Monitoring

## Task
Measure whether the evidence message landed and stayed fair-balanced, and list the impact gaps.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for DH-01.02.2.2.1 Message Impact Monitoring. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Compare the message the buyer supplied with the response the buyer supplied.
