---
name: "DH-02.03.4.2 Health Equity Effectiveness Assessment & Accessibility Compliance Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.03.4.2 Health Equity Effectiveness Assessment & Accessibility Compliance Monitoring. Use when the user asks for Equity evidence, Reach score, Equity follow-up. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.03.4.2 Health Equity Effectiveness Assessment & Accessibility Compliance Monitoring

Heading: DH-02.03.4 Health Equity & Accessibility.
Core: DH-02.03 Patient Engagement & Advocacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.03.4.2.1 Equity evidence

Worker: Health Equity & Digital Access Lead (`health-equity-access-lead`). 1 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.4.2.1 Equity evidence.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.4.2. The other skills under this competency do a different job.

### What it does
Define the evidence that a change reached the group.

### Method
1. Name the change and the group.
2. Name the record (completed task, supported site, language used).
3. Set the period.

### Do not
Do not use a policy statement as evidence.

### Output
An evidence definition.

A missing fact stays [GAP].

## DH-02.03.4.2.2 Reach score

Worker: Health Equity & Digital Access Lead (`health-equity-access-lead`). 1 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.4.2.2 Reach score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.4.2. The other skills under this competency do a different job.

### What it does
Score whether the group used the change.

### Method
1. Count the record in the period.
2. Compare it with the users in that group, or mark the denominator [GAP].
3. Keep the definition you used.

### Do not
Do not report a rate without a denominator.

### Output
A score or an explicit gap.

A missing fact stays [GAP].

## DH-02.03.4.2.3 Equity follow-up

Worker: Health Equity & Digital Access Lead (`health-equity-access-lead`). 1 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.4.2.3 Equity follow-up.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.4.2. The other skills under this competency do a different job.

### What it does
Assign a change that did not reach the group.

### Method
1. Name the owner.
2. State whether the change or the measurement was wrong.
3. Name the next period you will score.

### Do not
Do not close the question because the change shipped.

### Output
An owner and a next period.

A missing fact stays [GAP].
