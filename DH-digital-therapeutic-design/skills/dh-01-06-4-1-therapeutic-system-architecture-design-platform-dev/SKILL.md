---
name: dh-01-06-4-1-therapeutic-system-architecture-design-platform-dev
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.06.4.1 Therapeutic System Architecture Design & Platform Development. Use when the user asks for SaMD Architecture Design, Platform Component Development, Data-Flow & Integration Design. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.06.4.1 Therapeutic System Architecture Design & Platform Development

Heading: DH-01.06.4 DTx Architecture.
Core: DH-01.06 Digital Therapeutic Design.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.06.4.1.1 SaMD Architecture Design

Worker: Behavior-Change Designer (`behavior-change-designer`). 21 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.4.1.1 SaMD Architecture Design.
Prompt: PS-DH.01.06.4.1.1 SaMD Architecture Design.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Draft the SaMD architecture for {product} from components the operator already named.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.06.4`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded architecture brief: components already named; data flows already decided; [GAP] missing components. Do not invent an integration. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a mechanism, safety claim, or engagement outcome. Interoperability stay on hidden PS-DH.04.01 until suites exist. PCCP stays on AI/ML Regulatory. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.4.1.2 Platform Component Development

Worker: Behavior-Change Designer (`behavior-change-designer`). 21 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.4.1.2 Platform Component Development.
Prompt: PS-DH.01.06.4.1.2 Platform Component Development.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Specify the platform components the therapeutic runs on, with change-control notes.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Platform Component Development. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.4.1.3 Data-Flow & Integration Design

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 22 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.4.1.3 Data-Flow & Integration Design.
Prompt: PS-DH.01.06.4.1.3 Data-Flow & Integration Design.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Design data flow and integrations so provenance is preserved.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Data-Flow & Integration Design. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
