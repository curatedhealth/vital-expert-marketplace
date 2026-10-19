---
name: cross-jurisdiction-requirement-mapping
description: "Only while the Digital Health Library connector is connected. Use only after the job Multi-Region Regulatory Alignment & Harmonisation Execution is chosen, to do Cross-Jurisdiction Requirement Mapping."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Cross-Jurisdiction Requirement Mapping

## Execution formula
Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 15 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.2.1.1 Cross-Jurisdiction Requirement Mapping.
Prompt: PS-DH.03.03.2.1.1 Cross-Jurisdiction Requirement Mapping.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt
# Cross-Jurisdiction Requirement Mapping — Prompt (PS05)

## Task
Map cross-jurisdiction requirements for {product} from regions the operator already named.

## Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.03.2`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

## Output
A bounded requirement map: jurisdictions already named; overlays already decided; [GAP] missing regions. Do not invent an agency outcome. Mark unresolved facts [GAP].

## Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. FDA PCCP final guidance 4 December 2024 and GMLP. Do not invent a class, predicate, or agency outcome. PCCP stays on AI/ML Regulatory. US class/predicate stay on Regulatory Strategy. EU MDR / AI Act live here, not on Access. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.


## Template
## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.
