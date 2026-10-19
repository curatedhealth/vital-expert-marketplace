---
name: "DH-03.01.1.1 Outcomes-Based Contracting & Value-Based Care Integration"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.01.1.1 Outcomes-Based Contracting & Value-Based Care Integration. Use when the user asks for Outcomes Metric Definition, Risk-Sharing Model Design, Outcomes Contract Structuring. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.01.1.1 Outcomes-Based Contracting & Value-Based Care Integration

Heading: DH-03.01.1 Value-Based Care & Outcomes Contracts.
Core: DH-03.01 Market Access & Reimbursement.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.01.1.1.1 Outcomes Metric Definition

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.1.1.1 Outcomes Metric Definition.
Prompt: PS-DH.03.01.1.1.1 Outcomes Metric Definition.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Define outcomes metrics for {product} from measures the operator already named. Digital coverage only.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.01.1`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded metric brief: measures already named; contract facts already decided; [GAP] missing measures. Do not write the Access AMCP dossier. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Digital coverage only. Access AMCP / HTA / list-net stay on PS-04.02. Do not invent a code, price, or coverage decision. Not Access AMCP (`PS-04.02`). Coding/price stays on DH-03.01.2 Coding, Pricing & Contracting. HTA file stays on Access HTA. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Ask the buyer which outcome the contract will measure.

## DH-03.01.1.1.2 Risk-Sharing Model Design

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.1.1.2 Risk-Sharing Model Design.
Prompt: PS-DH.03.01.1.1.2 Risk-Sharing Model Design.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Design the risk-sharing model for the digital product, with the evidence behind each term.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Risk-Sharing Model Design. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound. Not the Market Access roof (`PS-04.02`).

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Ask the buyer how the parties share risk. Do not invent a share.

## DH-03.01.1.1.3 Outcomes Contract Structuring

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.1.1.3 Outcomes Contract Structuring.
Prompt: PS-DH.03.01.1.1.3 Outcomes Contract Structuring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Structure the outcomes contract so payment ties to a provable result.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Outcomes Contract Structuring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound. Not the Market Access roof (`PS-04.02`).

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Structure only the terms the buyer has already named.
