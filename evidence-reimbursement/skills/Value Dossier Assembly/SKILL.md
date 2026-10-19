---
name: value-dossier-assembly
description: "Use only after the job Payer Engagement & HTA Submission Execution is chosen, to do Value Dossier Assembly."
---

# Value Dossier Assembly

## Execution formula
Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.3.1.1 Value Dossier Assembly.
Prompt: PS-DH.03.01.3.1.1 Value Dossier Assembly.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Value Dossier Assembly — Prompt (PS05)

## Task
Assemble the digital-health value pack for {product} from evidence already decided. Not the Access AMCP file.

## Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.01.3`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

## Output
A bounded digital value pack: evidence already decided; named payers already collected; [GAP] missing pieces. Do not write Access AMCP or JCA. Mark unresolved facts [GAP].

## Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Digital coverage only. Access AMCP / HTA / list-net stay on PS-04.02. Do not invent a code, price, or coverage decision. Not Access AMCP or national HTA (`PS-04.02`). Digital coverage pathway stays on Coverage & Access Strategy. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

The library job value-dossier is design partners and cannot be started. Assemble only from evidence already in the conversation, and mark every missing section as a gap.
