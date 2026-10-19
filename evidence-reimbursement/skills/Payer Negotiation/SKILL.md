---
name: payer-negotiation
description: "Only while the Digital Health Library connector is connected. Use only after the job Payer Engagement & HTA Submission Execution is chosen, to do Payer Negotiation."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Payer Negotiation

## Execution formula
Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.3.1.3 Payer Negotiation.
Prompt: PS-DH.03.01.3.1.3 Payer Negotiation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Payer Negotiation — Prompt (PS05)

## Task
Prepare the payer negotiation from the value story, without invented coverage claims.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for Payer Negotiation. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound. Not the Market Access roof (`PS-04.02`).

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Prepare points from a status the buyer or an earlier tool result already supplied. Do not promise coverage.
