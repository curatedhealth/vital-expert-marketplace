---
name: dh-01-05-3-1-technology-evolution-anticipation-foresight-executi
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.05.3.1 Technology Evolution Anticipation & Foresight Execution. Use when the user asks for Technology Trend Analysis, Scenario Construction, Strategic Implication Assessment. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.05.3.1 Technology Evolution Anticipation & Foresight Execution

Heading: DH-01.05.3 Technology Foresight.
Core: DH-01.05 Digital Health Strategy & Vision.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.05.3.1.1 Technology Trend Analysis

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 11 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.3.1.1 Technology Trend Analysis.
Prompt: PS-DH.01.05.3.1.1 Technology Trend Analysis.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Draft the technology-trend brief for {product} from signals the operator already collected.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.05.3`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded trend brief: signals already collected; scenarios already named; [GAP] missing signals. Do not invent readiness. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a market size, competitor share, or build-partner-buy decision. Scouting a specific tech stays on Emerging Tech Evaluation. Horizon collection stays on Horizon Scanning. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.05.3.1.2 Scenario Construction

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 11 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.3.1.2 Scenario Construction.
Prompt: PS-DH.01.05.3.1.2 Scenario Construction.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Construct foresight scenarios for the named modality, with assumptions stated.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Scenario Construction. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.05.3.1.3 Strategic Implication Assessment

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 11 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.3.1.3 Strategic Implication Assessment.
Prompt: PS-DH.01.05.3.1.3 Strategic Implication Assessment.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Assess the strategic implication of each foresight scenario for the current play.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Strategic Implication Assessment. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
