---
name: ai-ml-pathway-selection
description: "Only while the Digital Health Library connector is connected. Use only after the job AI/ML Device Regulatory Pathway Navigation & Submission Execution is chosen, to do AI/ML Pathway Selection."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# AI/ML Pathway Selection

## Execution formula
Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 18 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.1.1.1 AI/ML Pathway Selection.
Prompt: PS-DH.03.03.1.1.1 AI/ML Pathway Selection.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt
# AI/ML Pathway Selection — Prompt (PS05)

## Task
Select the AI/ML device pathway, including whether a Predetermined Change Control Plan is required.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for AI/ML Pathway Selection. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.


## Template
## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.
