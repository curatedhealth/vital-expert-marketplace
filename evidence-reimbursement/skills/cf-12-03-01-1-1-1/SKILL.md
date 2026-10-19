---
name: cf-12-03-01-1-1-1
description: "Use only after the job Outcomes-Based Contracting and Value-Based Care Integration (CF-12.03.01.1.1) is chosen, to do Outcomes Metric Definition."
---

# Outcomes Metric Definition

Code: CF-12.03.01.1.1.1.

## Execution formula
Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.1.1.1 Outcomes Metric Definition.
Prompt: PS-DH.03.01.1.1.1 Outcomes Metric Definition.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Outcomes Metric Definition — Prompt (PS05)

## Task
Define outcomes metrics for {product} from measures the operator already named. Digital coverage only.

## Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.01.1`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

## Output
A bounded metric brief: measures already named; contract facts already decided; [GAP] missing measures. Do not write the Access AMCP dossier. Mark unresolved facts [GAP].

## Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Digital coverage only. Access AMCP / HTA / list-net stay on PS-04.02. Do not invent a code, price, or coverage decision. Not Access AMCP (`PS-04.02`). Coding/price stays on Coding, Pricing & Contracting. HTA file stays on Access HTA. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Ask the buyer which outcome the contract will measure.
