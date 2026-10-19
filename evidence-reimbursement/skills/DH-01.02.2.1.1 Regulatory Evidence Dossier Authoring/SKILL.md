---
name: "DH-01.02.2.1.1 Regulatory Evidence Dossier Authoring"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.2.1 Evidence Translation & Stakeholder Communication Delivery is chosen, to do DH-01.02.2.1.1 Regulatory Evidence Dossier Authoring."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.2.1.1 Regulatory Evidence Dossier Authoring

## Execution formula
Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 25 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.2.1.1 Regulatory Evidence Dossier Authoring.
Prompt: PS-DH.01.02.2.1.1 DH-01.02.2.1.1 Regulatory Evidence Dossier Authoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# DH-01.02.2.1.1 Regulatory Evidence Dossier Authoring

## Task
Author the regulatory evidence dossier for {product} from studies the operator already has.

## Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.02.2`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

## Output
A bounded evidence dossier: studies already in hand; audience; [GAP] missing studies. Do not invent a trial or write the Access AMCP file. Mark unresolved facts [GAP].

## Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a trial result, endpoint, or regulatory evidence claim. Protocol design stays on DH-01.02.1 Clinical Study Design. Access AMCP stays on PS-04.02. Digital coverage narrative stays on PS-DH.03.01. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Author from studies already in the conversation. Mark a missing study as a gap.
