---
name: coverage-pathway-mapping
description: "Use only after the job Coverage Pathway Design & Benefit Access Strategy Execution is chosen, to do Coverage Pathway Mapping."
---

# Coverage Pathway Mapping

## Execution formula
Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 6 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.4.1.1 Coverage Pathway Mapping.
Prompt: PS-DH.03.01.4.1.1 Coverage Pathway Mapping.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Coverage Pathway Mapping — Prompt (PS05)

## Task
Map the digital coverage pathway for {product} from benefit facts the operator already has.

## Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.01.4`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

## Output
A bounded pathway map: benefits already named; geographies already decided; [GAP] missing markets. Do not write Access launch sequence. Mark unresolved facts [GAP].

## Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Digital coverage only. Access AMCP / HTA / list-net stay on PS-04.02. Do not invent a code, price, or coverage decision. Not Access Launch Pathways (`PS-04.02.05`). Patient hubs stay on PS-06.01. Coding stays on Coding, Pricing & Contracting. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Use a market matrix already retrieved. Do not infer coverage from the product name.
