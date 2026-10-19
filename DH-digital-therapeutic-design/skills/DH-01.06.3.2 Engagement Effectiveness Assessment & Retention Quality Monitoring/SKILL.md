---
name: "DH-01.06.3.2 Engagement Effectiveness Assessment & Retention Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.06.3.2 Engagement Effectiveness Assessment & Retention Quality Monitoring. Use when the user asks for Engagement & Retention Monitoring, engagement retention pass rule, engagement retention miss owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.06.3.2 Engagement Effectiveness Assessment & Retention Quality Monitoring

Heading: DH-01.06.3 Engagement Mechanics.
Core: DH-01.06 Digital Therapeutic Design.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.06.3.2.1 Engagement & Retention Monitoring

Worker: Behavior-Change Designer (`behavior-change-designer`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.3.2.1 Engagement & Retention Monitoring.
Prompt: PS-DH.01.06.3.2.1 Engagement & Retention Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Watch engagement and retention, and list the drop-off points.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Engagement & Retention Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

A missing fact stays [GAP].

## DH-01.06.3.2.2 engagement retention pass rule

Worker: Behavior-Change Designer (`behavior-change-designer`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.3.2.2 engagement retention pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.06.3.2. The other skills under this competency do a different job.

### What it does
Write the pass rule for engagement retention before scoring another cohort.

### Method
1. List the elements that count: cohort, return action, and window.
2. Set a pass or fail for each element on one cohort.
3. Name the element that blocks release if it fails.

### Do not
Do not score a unit before this rule exists.

### Output
A pass rule for one cohort.

A missing fact stays [GAP].

## DH-01.06.3.2.3 engagement retention miss owner

Worker: Behavior-Change Designer (`behavior-change-designer`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.06.3.2.3 engagement retention miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.06.3.2. The other skills under this competency do a different job.

### What it does
Assign each failed element on engagement retention to a person.

### Method
1. Take a cohort that failed at least one element.
2. Name the engagement owner for each failed element.
3. State the date the element will be rechecked, or that the unit is stopped.

### Do not
Do not close a failed element because the existing assessment skill already described it.

### Output
An owner and a recheck date per failed element.

A missing fact stays [GAP].
