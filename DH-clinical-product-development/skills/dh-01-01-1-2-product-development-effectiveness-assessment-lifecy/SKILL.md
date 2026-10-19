---
name: dh-01-01-1-2-product-development-effectiveness-assessment-lifecy
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.01.1.2 Product Development Effectiveness Assessment & Lifecycle Quality Monitoring. Use when the user asks for Lifecycle measure, Stage score, Stage repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.01.1.2 Product Development Effectiveness Assessment & Lifecycle Quality Monitoring

Heading: DH-01.01.1 Product Development.
Core: DH-01.01 Clinical Product Development.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.01.1.2.1 Lifecycle measure

Worker: Digital Health Product Manager (`digital-health-product-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.1.2.1 Lifecycle measure.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.1.2. The other skills under this competency do a different job.

### What it does
Define a healthy move from one stage to the next.

### Method
1. Name the stages you will compare.
2. Name the evidence that the owed work product was accepted.
3. Name a move that does not count (a slide status with no work product).

### Do not
Do not score a stage from a roadmap color.

### Output
A measure and the evidence it requires.

A missing fact stays [GAP].

## DH-01.01.1.2.2 Stage score

Worker: Digital Health Product Manager (`digital-health-product-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.1.2.2 Stage score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.1.2. The other skills under this competency do a different job.

### What it does
Score the current stage.

### Method
1. Read the gate record.
2. Mark the owed work product present or missing.
3. Note how long the stage has been open.

### Do not
Do not mark a missing work product as in progress and then as passed.

### Output
A score: present or missing, and days open.

A missing fact stays [GAP].

## DH-01.01.1.2.3 Stage repair

Worker: Digital Health Product Manager (`digital-health-product-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.1.2.3 Stage repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.1.2. The other skills under this competency do a different job.

### What it does
Assign a stage that has no accepted work product.

### Method
1. Name the missing item and the owner.
2. State whether the next stage stays blocked.
3. Name the date the gate will be read again.

### Do not
Do not unblock the next stage while the item is missing.

### Output
An owner, a block, and a reread date.

A missing fact stays [GAP].
