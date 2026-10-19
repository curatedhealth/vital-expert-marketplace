---
name: "DH-01.02.1.1 Clinical Study Protocol Design & Endpoint Selection"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.02.1.1 Clinical Study Protocol Design & Endpoint Selection. Use when the user asks for Study Protocol Drafting, Endpoint & COA Selection, Statistical Analysis Plan Development. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.1.1 Clinical Study Protocol Design & Endpoint Selection

Heading: DH-01.02.1 Clinical Study Design.
Core: DH-01.02 Clinical Validation & Evidence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.02.1.1.1 Study Protocol Drafting

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 21 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.1.1.1 Study Protocol Drafting.
Prompt: PS-DH.01.02.1.1.1 DH-01.02.1.1.1 Study Protocol Drafting.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.1.1.1 Study Protocol Drafting

### Task
Draft the study protocol for {product} from the indication, population, and endpoints the operator already has.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.02.1`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded protocol brief: population; endpoints already named; [GAP] missing design facts. Do not invent a result or write the evidence dossier. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a trial result, endpoint, or regulatory evidence claim. Evidence packaging stays on DH-01.02.2 Evidence Communication. Trial ops stay on DH-01.02.3 Clinical Operations. RWE capture stays on DH-01.02.4 Digital Evidence Generation. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Draft from the question, population, and endpoint the buyer named.


## DH-01.02.1.1.2 Endpoint & COA Selection

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 21 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.1.1.2 Endpoint & COA Selection.
Prompt: PS-DH.01.02.1.1.2 DH-01.02.1.1.2 Endpoint & COA Selection.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.1.1.2 Endpoint & COA Selection

### Task
Select clinical and COA endpoints that can prove the digital product works, with the measurement rationale.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.1.1.2 Endpoint & COA Selection. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Select from endpoints the buyer named. Do not invent a clinical outcome assessment.


## DH-01.02.1.1.3 Statistical Analysis Plan Development

Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 20 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.1.1.3 Statistical Analysis Plan Development.
Prompt: PS-DH.01.02.1.1.3 DH-01.02.1.1.3 Statistical Analysis Plan Development.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.1.1.3 Statistical Analysis Plan Development

### Task
Write the statistical analysis plan for the digital-evidence study, including estimands and missing-data rules.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.1.1.3 Statistical Analysis Plan Development. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Write the plan from the endpoint and the comparison the buyer named.
