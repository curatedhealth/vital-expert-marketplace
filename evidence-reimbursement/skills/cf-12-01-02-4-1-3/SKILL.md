---
name: cf-12-01-02-4-1-3
description: "Use only after the job Digital Endpoint Capture and RWE Platform Management (CF-12.01.02.4.1) is chosen, to do Signal Detection Analysis."
---

# Signal Detection Analysis

Code: CF-12.01.02.4.1.3.

## Execution formula
Worker: AI/ML Governance Director (`ai-ml-governance-director`). 30 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.1.3 Signal Detection Analysis.
Prompt: PS-DH.01.02.4.1.3 Signal Detection Analysis.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Signal Detection Analysis — Prompt (PS05)

## Task
Analyze digital signals for valid detections, and mark noise or unresolved facts [GAP].

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for Signal Detection Analysis. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Use signals already retrieved. Do not invent an adverse event.
