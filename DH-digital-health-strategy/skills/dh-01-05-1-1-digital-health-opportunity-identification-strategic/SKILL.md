---
name: dh-01-05-1-1-digital-health-opportunity-identification-strategic
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.05.1.1 Digital Health Opportunity Identification & Strategic Vision Development. Use when the user asks for Opportunity Identification, Strategic Vision Articulation, Build-Partner-Buy Assessment. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.05.1.1 Digital Health Opportunity Identification & Strategic Vision Development

Heading: DH-01.05.1 Strategic Vision.
Core: DH-01.05 Digital Health Strategy & Vision.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.05.1.1.1 Opportunity Identification

Worker: Behavior-Change Designer (`behavior-change-designer`). 31 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.1.1.1 Opportunity Identification.
Prompt: PS-DH.01.05.1.1.1 Opportunity Identification.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Find the digital-health opportunity and rank it against the evidence you have.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Opportunity Identification. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.05.1.1.2 Strategic Vision Articulation

Worker: Chief Digital Health Officer (`chief-digital-health-officer`). 16 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.1.1.2 Strategic Vision Articulation.
Prompt: PS-DH.01.05.1.1.2 Strategic Vision Articulation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Articulate the digital-health vision for {product} from opportunities the operator already named.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.05.1`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded vision brief: opportunity already named; build-partner-buy facts already decided; [GAP] missing choices. Do not invent a market size. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a market size, competitor share, or build-partner-buy decision. Market census stays on Market Intelligence. Tech scenarios stay on Technology Foresight. Operating model stays on Execution Leadership. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.05.1.1.3 Build-Partner-Buy Assessment

Worker: Chief Compliance Officer (`chief-compliance-officer-digital-health`). 17 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.05.1.1.3 Build-Partner-Buy Assessment.
Prompt: PS-DH.01.05.1.1.3 Build-Partner-Buy Assessment.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Decide build, partner, or buy for the opportunity, with the rationale and the gaps.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Build-Partner-Buy Assessment. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
