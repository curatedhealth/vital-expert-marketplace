---
name: "DH-01.06.1.2 Personalisation Effectiveness Assessment & Adaptation Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.06.1.2 Personalisation Effectiveness Assessment & Adaptation Quality Monitoring. Use when the user asks for Personalisation Adaptation Monitoring, personalisation pass rule, personalisation miss owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.06.1.2 Personalisation Effectiveness Assessment & Adaptation Quality Monitoring

Heading: DH-01.06.1 Personalization Engine.
Core: DH-01.06 Digital Therapeutic Design.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.06.1.2.1 Personalisation Adaptation Monitoring

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.1.2.1 Personalisation Adaptation Monitoring.
Prompt: PS-DH.01.06.1.2.1 Personalisation Adaptation Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Watch whether personalization improves outcomes without unsafe drift, and list the gaps.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Personalisation Adaptation Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.1.2.2 personalisation pass rule

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.1.2.2 personalisation pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.06.1.2. The other skills under this competency do a different job.

### What it does
Write the pass rule for personalisation before scoring another rule.

### Method
1. List the elements that count: rule, population, and outcome watched.
2. Set a pass or fail for each element on one rule.
3. Name the element that blocks release if it fails.

### Do not
Do not score a unit before this rule exists.

### Output
A pass rule for one rule.

A missing fact stays [GAP].

## DH-01.06.1.2.3 personalisation miss owner

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.1.2.3 personalisation miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.06.1.2. The other skills under this competency do a different job.

### What it does
Assign each failed element on personalisation to a person.

### Method
1. Take a rule that failed at least one element.
2. Name the product owner for each failed element.
3. State the date the element will be rechecked, or that the unit is stopped.

### Do not
Do not close a failed element because the existing assessment skill already described it.

### Output
An owner and a recheck date per failed element.

A missing fact stays [GAP].
