---
name: dh-01-06-2-1-therapeutic-safety-efficacy-standards-implementatio
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.06.2.1 Therapeutic Safety & Efficacy Standards Implementation. Use when the user asks for Mechanism-of-Action Specification, Safety-by-Design Implementation, Efficacy Evidence Linkage. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.06.2.1 Therapeutic Safety & Efficacy Standards Implementation

Heading: DH-01.06.2 Safety & Efficacy.
Core: DH-01.06 Digital Therapeutic Design.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.06.2.1.1 Mechanism-of-Action Specification

Worker: Behavior-Change Designer (`behavior-change-designer`). 14 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.2.1.1 Mechanism-of-Action Specification.
Prompt: PS-DH.01.06.2.1.1 Mechanism-of-Action Specification.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Specify the mechanism of action for {product} from evidence the operator already has.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.06.2`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded mechanism brief: claimed mechanism already decided; safety flags already named; [GAP] missing evidence. Do not invent an outcome. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a mechanism, safety claim, or engagement outcome. Adaptive logic stays on Personalization Engine. PCCP stays on AI/ML Regulatory. Quality/cyber stay on hidden PS-DH.03.02. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.2.1.2 Safety-by-Design Implementation

Worker: Behavior-Change Designer (`behavior-change-designer`). 18 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.2.1.2 Safety-by-Design Implementation.
Prompt: PS-DH.01.06.2.1.2 Safety-by-Design Implementation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Implement safety-by-design controls the therapeutic must meet before use.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Safety-by-Design Implementation. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.2.1.3 Efficacy Evidence Linkage

Worker: Behavior-Change Designer (`behavior-change-designer`). 28 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.2.1.3 Efficacy Evidence Linkage.
Prompt: PS-DH.01.06.2.1.3 Efficacy Evidence Linkage.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Link efficacy claims to the evidence that supports them, and mark [GAP] where it does not.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Efficacy Evidence Linkage. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].
