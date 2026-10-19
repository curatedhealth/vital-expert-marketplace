---
name: payer-value-narrative
description: "Only while the Digital Health Library connector is connected. Use only after the job Evidence Translation & Stakeholder Communication Delivery is chosen, to do Payer Value Narrative."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Payer Value Narrative

## Execution formula
Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 19 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.2.1.2 Payer Value Narrative.
Prompt: PS-DH.01.02.2.1.2 Payer Value Narrative.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Payer Value Narrative — Prompt (PS05)

## Task
Write the payer value narrative from the same evidence base, fair-balanced for the named market.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for Payer Value Narrative. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Write from evidence already retrieved. Do not promise a price or coverage.
