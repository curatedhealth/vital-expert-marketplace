---
name: "DH-03.03.2.1 Multi-Region Regulatory Alignment & Harmonisation Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.03.2.1 Multi-Region Regulatory Alignment & Harmonisation Execution. Use when the user asks for Cross-Jurisdiction Requirement Mapping, Harmonised Evidence Planning, Regional Submission Adaptation, List jurisdictions. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.03.2.1 Multi-Region Regulatory Alignment & Harmonisation Execution

Heading: DH-03.03.2 Global Harmonization.
Core: DH-03.03 Regulatory Strategy & Submissions.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.03.2.1.1 Cross-Jurisdiction Requirement Mapping

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 15 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.2.1.1 Cross-Jurisdiction Requirement Mapping.
Prompt: PS-DH.03.03.2.1.1 Cross-Jurisdiction Requirement Mapping.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Map cross-jurisdiction requirements for {product} from regions the operator already named.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.03.2`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded requirement map: jurisdictions already named; overlays already decided; [GAP] missing regions. Do not invent an agency outcome. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. FDA PCCP final guidance 4 December 2024 and GMLP. Do not invent a class, predicate, or agency outcome. PCCP stays on DH-03.03.1 AI/ML Regulatory. US class/predicate stay on DH-03.03.3 Regulatory Strategy. EU MDR / AI Act live here, not on Access. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.2.1.2 Harmonised Evidence Planning

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 29 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.2.1.2 Harmonised Evidence Planning.
Prompt: PS-DH.03.03.2.1.2 Harmonised Evidence Planning.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Plan the harmonized evidence package so one study set can serve multiple regulators.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Harmonised Evidence Planning. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.2.1.3 Regional Submission Adaptation

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 15 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.2.1.3 Regional Submission Adaptation.
Prompt: PS-DH.03.03.2.1.3 Regional Submission Adaptation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Adapt the submission for each named region without inventing local requirements.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Regional Submission Adaptation. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.2.1.4 List jurisdictions

Worker: not bound.
Skill: CF-12.03.03.2.1.4 List jurisdictions.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.list_jurisdictions`. This call is not counted. Do not close it with Verify.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Call this when the buyer asks which registers are loaded. This call is not counted. It returns stored authorization and safety-event counts, the last load date, and the sources.
