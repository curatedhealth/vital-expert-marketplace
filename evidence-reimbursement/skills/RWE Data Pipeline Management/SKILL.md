---
name: "RWE Data Pipeline Management"
description: "Only while the Digital Health Library connector is connected. Use only after the job Digital Endpoint Capture & RWE Platform Management is chosen, to do RWE Data Pipeline Management."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# RWE Data Pipeline Management

## Execution formula
Worker: AI/ML Governance Director (`ai-ml-governance-director`). 32 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.1.2 RWE Data Pipeline Management.
Prompt: PS-DH.01.02.4.1.2 RWE Data Pipeline Management.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# RWE Data Pipeline Management — Prompt (PS05)

## Task
Run the real-world evidence pipeline from capture through a source-traced analytic table.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for RWE Data Pipeline Management. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Use the source and the cohort the buyer named. Unpublished data stays a gap.
