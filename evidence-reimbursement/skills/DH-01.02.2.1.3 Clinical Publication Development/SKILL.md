---
name: "DH-01.02.2.1.3 Clinical Publication Development"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.2.1 Evidence Translation & Stakeholder Communication Delivery is chosen, to do DH-01.02.2.1.3 Clinical Publication Development."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.2.1.3 Clinical Publication Development

## Execution formula
Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 19 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.2.1.3 Clinical Publication Development.
Prompt: PS-DH.01.02.2.1.3 DH-01.02.2.1.3 Clinical Publication Development.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# DH-01.02.2.1.3 Clinical Publication Development

## Task
Draft the clinical publication from the study findings, with provenance and unresolved facts marked [GAP].

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for DH-01.02.2.1.3 Clinical Publication Development. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Draft from the study record the buyer or a literature tool already supplied.
