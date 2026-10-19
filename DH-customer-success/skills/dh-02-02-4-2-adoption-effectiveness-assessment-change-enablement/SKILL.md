---
name: dh-02-02-4-2-adoption-effectiveness-assessment-change-enablement
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.02.4.2 Adoption Effectiveness Assessment & Change Enablement Quality Monitoring. Use when the user asks for Adoption after training, Adoption score, Enablement follow-up. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02.4.2 Adoption Effectiveness Assessment & Change Enablement Quality Monitoring

Heading: DH-02.02.4 Adoption & Change Enablement.
Core: DH-02.02 Customer Success & Implementation.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.02.4.2.1 Adoption after training

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.4.2.1 Adoption after training.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.4.2. The other skills under this competency do a different job.

### What it does
Define adoption as the trained task done in production.

### Method
1. Use the task card.
2. Set the window after training.
3. Set the share of trained users who must complete the task.

### Do not
Do not use session attendance as adoption.

### Output
An adoption rule.

A missing fact stays [GAP].

## DH-02.02.4.2.2 Adoption score

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.4.2.2 Adoption score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.4.2. The other skills under this competency do a different job.

### What it does
Score the site in that window.

### Method
1. Count trained users and users who completed the task.
2. Keep the user role, not the user name, in the summary.
3. Note the old step if it is still in use.

### Do not
Do not report a rate without the denominator.

### Output
A score: trained, completed, old step still used.

A missing fact stays [GAP].

## DH-02.02.4.2.3 Enablement follow-up

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.4.2.3 Enablement follow-up.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.4.2. The other skills under this competency do a different job.

### What it does
Assign a site that missed the rule.

### Method
1. Name whether the task, the training, or the workflow is wrong.
2. Name the owner.
3. Name the date of the next session or the workflow change.

### Do not
Do not schedule the same session again without saying what changes.

### Output
An owner and a different next step.

A missing fact stays [GAP].
