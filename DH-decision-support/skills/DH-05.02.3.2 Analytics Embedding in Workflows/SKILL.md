---
name: "DH-05.02.3.2 Analytics Embedding in Workflows"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.3.2 Analytics Embedding in Workflows. Use when the user asks for Workflow insertion point, Action from the number, Embed owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.3.2 Analytics Embedding in Workflows

Heading: DH-05.02.3 Decision Intelligence Products.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.3.2.1 Workflow insertion point

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.2.1 Workflow insertion point.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.2. The other skills under this competency do a different job.

### What it does
Name the screen or step where the analytic appears.

### Method
1. Name the host workflow and the step.
2. Name the number or recommendation that appears there.
3. Name what is removed from that step.

### Do not
Do not add a link out to a dashboard and call it embedded.

### Output
An insertion point and a removal.

A missing fact stays [GAP].

## DH-05.02.3.2.2 Action from the number

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.2.2 Action from the number.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.2. The other skills under this competency do a different job.

### What it does
Name the action the user can take without leaving the step.

### Method
1. Name the action.
2. Name the write-back or the task it creates.
3. Name the action that still requires another system.

### Do not
Do not claim the workflow changed if the user must export.

### Output
An action and a write-back, or an export you will not claim.

A missing fact stays [GAP].

## DH-05.02.3.2.3 Embed owner

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.2.3 Embed owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.2. The other skills under this competency do a different job.

### What it does
Name who owns the insertion when the number is wrong.

### Method
1. Name the owner of the metric.
2. Name the owner of the host workflow.
3. Name which one stops the display when the metric is stale.

### Do not
Do not leave a stale number on a clinical step.

### Output
Two owners and a stop rule.

A missing fact stays [GAP].
