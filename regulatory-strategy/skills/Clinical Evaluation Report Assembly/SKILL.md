---
name: clinical-evaluation-report-assembly
description: "Only while the Digital Health Library connector is connected. Use only after the job Regulatory Submission Preparation & Dossier Assembly Execution is chosen, to do Clinical Evaluation Report Assembly."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Clinical Evaluation Report Assembly

## Execution formula
Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.4.1.1 Clinical Evaluation Report Assembly.
Prompt: PS-DH.03.03.4.1.1 Clinical Evaluation Report Assembly.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt
# Clinical Evaluation Report Assembly — Prompt (PS05)

## Task
Assemble the clinical evaluation report so the first pass does not bounce.

## Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

## Output
A bounded draft for Clinical Evaluation Report Assembly. Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.


## Template
## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.
