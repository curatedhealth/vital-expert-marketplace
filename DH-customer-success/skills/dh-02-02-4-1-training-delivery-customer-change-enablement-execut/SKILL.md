---
name: dh-02-02-4-1-training-delivery-customer-change-enablement-execut
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.02.4.1 Training Delivery & Customer Change Enablement Execution. Use when the user asks for Training task, Session record, Change that stays. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02.4.1 Training Delivery & Customer Change Enablement Execution

Heading: DH-02.02.4 Adoption & Change Enablement.
Core: DH-02.02 Customer Success & Implementation.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.02.4.1.1 Training task

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.4.1.1 Training task.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.4.1. The other skills under this competency do a different job.

### What it does
Name the task training must leave the user able to do.

### Method
1. Name the role and the task from the day-one workflow.
2. Name the steps the user performs, not the slides they watch.
3. Name what the user does not need to learn in this session.

### Do not
Do not train features that are outside the site's scope.

### Output
A task card: role, steps, out of scope.

A missing fact stays [GAP].

## DH-02.02.4.1.2 Session record

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.4.1.2 Session record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.4.1. The other skills under this competency do a different job.

### What it does
Record who was trained on that task.

### Method
1. Name the session date, the site, and the attendees by role.
2. Record whether each attendee completed the task once.
3. Record who was in the role and did not attend.

### Do not
Do not count attendance as completion.

### Output
A session record with completion.

A missing fact stays [GAP].

## DH-02.02.4.1.3 Change that stays

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.4.1.3 Change that stays.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.4.1. The other skills under this competency do a different job.

### What it does
Name the old step that should stop after training.

### Method
1. Name the workaround or the old system.
2. Name who checks, after a stated number of days, that it stopped.
3. Name what happens if it did not stop.

### Do not
Do not end enablement at the session.

### Output
A check date and the old step.

A missing fact stays [GAP].
