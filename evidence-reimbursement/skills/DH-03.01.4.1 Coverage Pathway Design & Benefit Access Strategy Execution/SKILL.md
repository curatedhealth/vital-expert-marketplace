---
name: "DH-03.01.4.1 Coverage Pathway Design & Benefit Access Strategy Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.01.4.1 Coverage Pathway Design & Benefit Access Strategy Execution. Use when the user asks for Coverage Pathway Mapping, Access Strategy Design, Benefit Design, Read the market matrix, Read status history. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.01.4.1 Coverage Pathway Design & Benefit Access Strategy Execution

Heading: DH-03.01.4 Coverage & Access Strategy.
Core: DH-03.01 Market Access & Reimbursement.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.01.4.1.1 Coverage Pathway Mapping

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 6 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.4.1.1 Coverage Pathway Mapping.
Prompt: PS-DH.03.01.4.1.1 Coverage Pathway Mapping.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Map the digital coverage pathway for {product} from benefit facts the operator already has.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.01.4`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded pathway map: benefits already named; geographies already decided; [GAP] missing markets. Do not write Access launch sequence. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Digital coverage only. Access AMCP / HTA / list-net stay on PS-04.02. Do not invent a code, price, or coverage decision. Not Access Launch Pathways (`PS-04.02.05`). Patient hubs stay on PS-06.01. Coding stays on DH-03.01.2 Coding, Pricing & Contracting. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Use a market matrix already retrieved. Do not infer coverage from the product name.

## DH-03.01.4.1.2 Access Strategy Design

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.4.1.2 Access Strategy Design.
Prompt: PS-DH.03.01.4.1.2 Access Strategy Design.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Design the benefit-access strategy, with the evidence and policy levers per market.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Access Strategy Design. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound. Not the Market Access roof (`PS-04.02`).

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Turn a matrix already in the conversation into a choice. Do not promise coverage.

## DH-03.01.4.1.3 Benefit Design

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 6 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.4.1.3 Benefit Design.
Prompt: PS-DH.03.01.4.1.3 Benefit Design.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Design the benefit so coverage can convert into actual patient access.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Benefit Design. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound. Not the Market Access roof (`PS-04.02`).

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Record the benefit design the buyer supplies. Do not design one.

## DH-03.01.4.1.4 Read the market matrix

Worker: not bound.
Skill: CF-12.03.01.4.1.4 Read the market matrix.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.get_market_matrix`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the category. An empty scheme is a gap. Europe is partial where the connector says the scheme is not loaded.

## DH-03.01.4.1.5 Read status history

Worker: not bound.
Skill: CF-12.03.01.4.1.5 Read status history.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.get_status_history`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the scheme. An empty history is a gap.
