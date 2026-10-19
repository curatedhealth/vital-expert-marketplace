---
name: predetermined-change-control-plan-authoring
description: "Only while the Digital Health Library connector is connected. Use only after the job AI/ML Device Regulatory Pathway Navigation & Submission Execution is chosen, to do Predetermined Change Control Plan Authoring."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Predetermined Change Control Plan Authoring

## Execution formula
Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 14 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.1.1.2 Predetermined Change Control Plan Authoring.
Prompt: PS-DH.03.03.1.1.2 Predetermined Change Control Plan Authoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt
# Predetermined Change Control Plan Authoring — Prompt (PS05)

## Task
Author a Predetermined Change Control Plan for {product}'s AI-enabled device software function: Description of Modifications, Modification Protocol, and Impact Assessment.

## Inputs
- Product, intended use, and the AI-enabled device software function in scope.
- Pathway if named (510(k), De Novo, or PMA). Do not invent a pathway or a predicate.
- Planned modification types, data and retraining methods, and any performance or labeling facts the operator already has.

## Output
A bounded FDA PCCP draft: Description of Modifications (what may change, inside intended-use bounds); Modification Protocol (data, retraining, performance evaluation, update and labeling steps); Impact Assessment (safety and effectiveness of the listed changes). Mark unresolved facts `[GAP]`.

## Guardrails
No invented evidence, performance, predicates, or authorization status. `[GAP]` when inputs are missing. Quality-system and cybersecurity work stay on `PS-DH.03.02`. EU MDR / AI Act stay on `PS-DH.03.03.2`. Generic class and predicate stay on `PS-DH.03.03.3`. Generic dossier and CER stay on `PS-DH.03.03.4`. Access AMCP stays on `PS-04.02`. Not a CF05 skill.


## Template
## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.
