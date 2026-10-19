---
name: "DH-01.01.1.1 Clinical Product Lifecycle Management & Development Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.01.1.1 Clinical Product Lifecycle Management & Development Execution. Use when the user asks for Lifecycle stage, Development increment, Stage gate record. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.01.1.1 Clinical Product Lifecycle Management & Development Execution

Heading: DH-01.01.1 Product Development.
Core: DH-01.01 Clinical Product Development.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.01.1.1.1 Lifecycle stage

Worker: Digital Health Product Manager (`digital-health-product-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.1.1.1 Lifecycle stage.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.1.1. The other skills under this competency do a different job.

### What it does
Name the stage this digital health product is in, and what that stage must produce.

### Method
1. Name the product and the stage (concept, clinical evidence, regulated release, or post-market).
2. Name the work product that stage owes (intended use, evidence plan, release record, or surveillance note).
3. Name the stage you will not start until that work product exists.

### Do not
Do not run a regulated release while the intended use is still a concept.

### Output
A stage, the work product it owes, and the stage it blocks.

A missing fact stays [GAP].

## DH-01.01.1.1.2 Development increment

Worker: Digital Health Product Manager (`digital-health-product-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.1.1.2 Development increment.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.1.1. The other skills under this competency do a different job.

### What it does
Define the increment the team will finish in this stage.

### Method
1. Name the user, the task, and the build that contains it.
2. Name what is outside the increment.
3. Name who accepts the increment.

### Do not
Do not add a clinical claim to the increment that is not in the evidence plan.

### Output
An increment, its exclusions, and the acceptor.

A missing fact stays [GAP].

## DH-01.01.1.1.3 Stage gate record

Worker: Digital Health Product Manager (`digital-health-product-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.1.1.3 Stage gate record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.1.1. The other skills under this competency do a different job.

### What it does
Record whether the work product is complete enough to leave the stage.

### Method
1. Check the owed work product against the stage.
2. Pass, or name the missing item.
3. Name the date and the person who decided.

### Do not
Do not advance the stage because the calendar date arrived.

### Output
A gate record: pass or missing item, date, person.

A missing fact stays [GAP].
