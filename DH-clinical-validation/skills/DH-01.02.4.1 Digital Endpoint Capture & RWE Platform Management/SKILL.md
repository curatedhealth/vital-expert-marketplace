---
name: "DH-01.02.4.1 Digital Endpoint Capture & RWE Platform Management"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.02.4.1 Digital Endpoint Capture & RWE Platform Management. Use when the user asks for Digital Endpoint Instrumentation, RWE Data Pipeline Management, Signal Detection Analysis, Search literature, Open a literature record, Link a trial, Grade evidence, Check a retraction, Build an evidence table. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.1 Digital Endpoint Capture & RWE Platform Management

Heading: DH-01.02.4 Digital Evidence Generation.
Core: DH-01.02 Clinical Validation & Evidence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.02.4.1.1 Digital Endpoint Instrumentation

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 30 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.1.1 Digital Endpoint Instrumentation.
Prompt: PS-DH.01.02.4.1.1 DH-01.02.4.1.1 Digital Endpoint Instrumentation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.4.1.1 Digital Endpoint Instrumentation

### Task
Draft the digital-endpoint instrumentation brief for {product} from measures the operator already named.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.02.4`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded instrumentation brief: endpoints already named; capture path; [GAP] missing sensors or sources. Do not invent a signal. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a trial result, endpoint, or regulatory evidence claim. Protocol design stays on DH-01.02.1 Clinical Study Design. Trial ops stay on DH-01.02.3 Clinical Operations. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Use the endpoint and device the buyer named.


## DH-01.02.4.1.2 RWE Data Pipeline Management

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 32 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.1.2 RWE Data Pipeline Management.
Prompt: PS-DH.01.02.4.1.2 DH-01.02.4.1.2 RWE Data Pipeline Management.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.4.1.2 RWE Data Pipeline Management

### Task
Run the real-world evidence pipeline from capture through a source-traced analytic table.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.4.1.2 RWE Data Pipeline Management. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Use the source and the cohort the buyer named. Unpublished data stays a gap.


## DH-01.02.4.1.3 Signal Detection Analysis

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 30 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.1.3 Signal Detection Analysis.
Prompt: PS-DH.01.02.4.1.3 DH-01.02.4.1.3 Signal Detection Analysis.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.4.1.3 Signal Detection Analysis

### Task
Analyze digital signals for valid detections, and mark noise or unresolved facts [GAP].

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.4.1.3 Signal Detection Analysis. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Use signals already retrieved. Do not invent an adverse event.


## DH-01.02.4.1.4 Search literature

Worker: not bound.
Skill: CF-12.01.02.4.1.4 Search literature.
Prompt: not bound.
Template: not bound.
Tool: `literature.search_literature`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the claim or the product. Unpublished data stays a gap.


## DH-01.02.4.1.5 Open a literature record

Worker: not bound.
Skill: CF-12.01.02.4.1.5 Open a literature record.
Prompt: not bound.
Template: not bound.
Tool: `literature.get_record`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Open one hit the search already returned.


## DH-01.02.4.1.6 Link a trial

Worker: not bound.
Skill: CF-12.01.02.4.1.6 Link a trial.
Prompt: not bound.
Template: not bound.
Tool: `literature.find_trial`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Link a registry entry for the study already opened.


## DH-01.02.4.1.7 Grade evidence

Worker: not bound.
Skill: CF-12.01.02.4.1.7 Grade evidence.
Prompt: not bound.
Template: not bound.
Tool: `literature.grade_evidence`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Grade the study already opened. Keep the grade beside the record.


## DH-01.02.4.1.8 Check a retraction

Worker: not bound.
Skill: CF-12.01.02.4.1.8 Check a retraction.
Prompt: not bound.
Template: not bound.
Tool: `literature.check_retraction`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Flag a retraction. A clear record is still reported as clear.


## DH-01.02.4.1.9 Build an evidence table

Worker: not bound.
Skill: CF-12.01.02.4.1.9 Build an evidence table.
Prompt: not bound.
Template: not bound.
Tool: `literature.build_evidence_table`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Build the table from the graded records already opened.
