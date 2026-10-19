---
name: dh-01-01-3-2-integration-effectiveness-assessment-cross-function
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.01.3.2 Integration Effectiveness Assessment & Cross-Functional Alignment Monitoring. Use when the user asks for Handoff measure, Handoff score, Alignment repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.01.3.2 Integration Effectiveness Assessment & Cross-Functional Alignment Monitoring

Heading: DH-01.01.3 Cross-Functional Integration.
Core: DH-01.01 Clinical Product Development.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.01.3.2.1 Handoff measure

Worker: Chief Digital Health Officer (`chief-digital-health-officer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.3.2.1 Handoff measure.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.3.2. The other skills under this competency do a different job.

### What it does
Define a completed handoff.

### Method
1. Use the integration point.
2. A pass is the work product received by the named receiver, not a message sent.
3. Name the period you will score.

### Do not
Do not count a sent message as a received handoff.

### Output
A pass rule and a period.

A missing fact stays [GAP].

## DH-01.01.3.2.2 Handoff score

Worker: Chief Digital Health Officer (`chief-digital-health-officer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.3.2.2 Handoff score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.3.2. The other skills under this competency do a different job.

### What it does
Score the open dependencies in that period.

### Method
1. List each dependency as received, late, or still open.
2. Keep the work product name.
3. Separate a late clinical evidence handoff from a late copy handoff.

### Do not
Do not drop an open dependency from the list.

### Output
A score.

A missing fact stays [GAP].

## DH-01.01.3.2.3 Alignment repair

Worker: Chief Digital Health Officer (`chief-digital-health-officer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.3.2.3 Alignment repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.3.2. The other skills under this competency do a different job.

### What it does
Assign a handoff that did not arrive.

### Method
1. Name the owner who owes the work product.
2. State the decision that stays blocked.
3. Name the date you will look again.

### Do not
Do not unblock the decision because the meeting happened.

### Output
An owner, a blocked decision, and a date.

A missing fact stays [GAP].
