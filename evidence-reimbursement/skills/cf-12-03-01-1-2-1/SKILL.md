---
name: cf-12-03-01-1-2-1
description: "Use only after the job VBC Contract Effectiveness Assessment and Outcomes Achievement Monitoring (CF-12.03.01.1.2) is chosen, to do Outcomes Achievement Monitoring."
---

# Outcomes Achievement Monitoring

Code: CF-12.03.01.1.2.1.

## Execution formula
Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.1.2.1 Outcomes Achievement Monitoring.
Prompt: PS-DH.03.01.1.2.1 Outcomes Achievement Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Outcomes Achievement Monitoring — Prompt (PS05)

## Task
Watch whether the VBC contract is delivering the outcomes it promised, and list missed metrics.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for Outcomes Achievement Monitoring. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound. Not the Market Access roof (`PS-04.02`).

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Compare the outcome the buyer named with the result the buyer supplied.
