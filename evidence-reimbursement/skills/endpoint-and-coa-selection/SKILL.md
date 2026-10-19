---
name: endpoint-and-coa-selection
description: "Use only after the job Clinical Study Protocol Design and Endpoint Selection is chosen, to do Endpoint and COA Selection."
---

# Endpoint and COA Selection

## Execution formula
Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 21 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.1.1.2 Endpoint & COA Selection.
Prompt: PS-DH.01.02.1.1.2 Endpoint & COA Selection.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Endpoint & COA Selection — Prompt (PS05)

## Task
Select clinical and COA endpoints that can prove the digital product works, with the measurement rationale.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for Endpoint & COA Selection. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Select from endpoints the buyer named. Do not invent a clinical outcome assessment.
