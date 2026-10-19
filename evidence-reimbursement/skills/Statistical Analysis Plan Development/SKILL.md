---
name: "Statistical Analysis Plan Development"
description: "Only while the Digital Health Library connector is connected. Use only after the job Clinical Study Protocol Design & Endpoint Selection is chosen, to do Statistical Analysis Plan Development."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Statistical Analysis Plan Development

## Execution formula
Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 20 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.1.1.3 Statistical Analysis Plan Development.
Prompt: PS-DH.01.02.1.1.3 Statistical Analysis Plan Development.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Statistical Analysis Plan Development — Prompt (PS05)

## Task
Write the statistical analysis plan for the digital-evidence study, including estimands and missing-data rules.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for Statistical Analysis Plan Development. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Write the plan from the endpoint and the comparison the buyer named.
