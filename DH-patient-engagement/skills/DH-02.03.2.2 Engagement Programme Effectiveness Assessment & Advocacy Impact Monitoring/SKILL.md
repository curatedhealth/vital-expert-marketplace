---
name: "DH-02.03.2.2 Engagement Programme Effectiveness Assessment & Advocacy Impact Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.03.2.2 Engagement Programme Effectiveness Assessment & Advocacy Impact Monitoring. Use when the user asks for Engagement result definition, Activity score, Programme change. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.03.2.2 Engagement Programme Effectiveness Assessment & Advocacy Impact Monitoring

Heading: DH-02.03.2 Engagement Programs & Advocacy.
Core: DH-02.03 Patient Engagement & Advocacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.03.2.2.1 Engagement result definition

Worker: Digital Marketing Manager (`digital-marketing-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.2.2.1 Engagement result definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.2.2. The other skills under this competency do a different job.

### What it does
Define the result that matches the purpose.

### Method
1. Use the action named in the purpose, not attendance.
2. Set the period.
3. Name the record that proves the action.

### Do not
Do not use follower counts when the purpose was a specific action.

### Output
A result definition.

A missing fact stays [GAP].

## DH-02.03.2.2.2 Activity score

Worker: Digital Marketing Manager (`digital-marketing-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.2.2.2 Activity score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.2.2. The other skills under this competency do a different job.

### What it does
Score activities in the period.

### Method
1. Count the result per activity from the named record.
2. Mark an activity with no record as unscored.
3. Note a claim used that was not on the activity's allowed list.

### Do not
Do not score an unscored activity as zero without saying the record was missing.

### Output
A score per activity.

A missing fact stays [GAP].

## DH-02.03.2.2.3 Programme change

Worker: Digital Marketing Manager (`digital-marketing-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.2.2.3 Programme change.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.2.2. The other skills under this competency do a different job.

### What it does
Stop or change an activity that missed the result.

### Method
1. Name the activity.
2. State stop, change the audience, or change the content.
3. Name the owner and the next date.

### Do not
Do not add a new activity before deciding on the one that missed.

### Output
One decision per missed activity.

A missing fact stays [GAP].
