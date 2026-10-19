---
name: dh-03-03-3-1-global-regulatory-pathway-strategy-classification-m
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.03.3.1 Global Regulatory Pathway Strategy & Classification Management. Use when the user asks for SaMD Risk Classification, Regulatory Pathway Selection, Intended-Use Definition, Classify a product, Read pathway precedents, Find predicates, Search devices, Open an authorization, Compare authorizations, Read market status. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.03.3.1 Global Regulatory Pathway Strategy & Classification Management

Heading: DH-03.03.3 Regulatory Strategy.
Core: DH-03.03 Regulatory Strategy & Submissions.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.03.3.1.1 SaMD Risk Classification

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 31 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.3.1.1 SaMD Risk Classification.
Prompt: PS-DH.03.03.3.1.1 SaMD Risk Classification.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Classify SaMD risk for the named product, with the rationale.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for SaMD Risk Classification. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.3.1.2 Regulatory Pathway Selection

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 29 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.3.1.2 Regulatory Pathway Selection.
Prompt: PS-DH.03.03.3.1.2 Regulatory Pathway Selection.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Select the regulatory pathway for {product} from classification facts the operator already has.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.03.3`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded pathway brief: class/predicate facts already decided; [GAP] missing class facts. Do not invent a predicate or write the PCCP. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. FDA PCCP final guidance 4 December 2024 and GMLP. Do not invent a class, predicate, or agency outcome. PCCP stays on DH-03.03.1 AI/ML Regulatory. Dossier assembly stays on DH-03.03.4 Submission Excellence. Multi-region overlay stays on DH-03.03.2 Global Harmonization. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.3.1.3 Intended-Use Definition

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 29 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.3.1.3 Intended-Use Definition.
Prompt: PS-DH.03.03.3.1.3 Intended-Use Definition.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Define intended use so classification and claims stay consistent.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Intended-Use Definition. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.3.1.4 Classify a product

Worker: not bound.
Skill: CF-12.03.03.3.1.4 Classify a product.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.classify_product`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the product. Do not infer a class from text alone. The United States register is the deepest. Europe and the United Kingdom are partial where the connector says so.

## DH-03.03.3.1.5 Read pathway precedents

Worker: not bound.
Skill: CF-12.03.03.3.1.5 Read pathway precedents.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.get_pathway_precedents`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the product code or the EMDN code. Keep this separate from classification and from the predicate chain.

## DH-03.03.3.1.6 Find predicates

Worker: not bound.
Skill: CF-12.03.03.3.1.6 Find predicates.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.find_predicates`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the device. This chain is United States predicate links. Other jurisdictions do not use it.

## DH-03.03.3.1.7 Search devices

Worker: not bound.
Skill: CF-12.03.03.3.1.7 Search devices.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.search_devices`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the product or the manufacturer. The name needs at least three characters. Software devices only, unless the buyer asks for every stored device. A missing row is a gap.

## DH-03.03.3.1.8 Open an authorization

Worker: not bound.
Skill: CF-12.03.03.3.1.8 Open an authorization.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.get_authorization`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for one reference: a 510(k), De Novo, or PMA number, a Basic UDI-DI, or an SRN with the trade name. Return the stored fields with their source. A missing record is a gap.

## DH-03.03.3.1.9 Compare authorizations

Worker: not bound.
Skill: CF-12.03.03.3.1.9 Compare authorizations.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.compare_authorizations`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for two to twelve references. A cell the source does not state is not assessable. UK registration and Swiss devices stay a gap. Do not infer a class, a pathway, or a safety count.

## DH-03.03.3.1.10 Read market status

Worker: not bound.
Skill: CF-12.03.03.3.1.10 Read market status.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.get_market_status`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the product name or one reference. This task is where the product is authorized. Reimbursement fields from this tool stay a gap.
