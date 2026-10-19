---
name: "DH-05.02.3.1 Decision Product Discovery"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.3.1 Decision Product Discovery. Use when the user asks for Decision product user, Product bet, Discovery evidence. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.3.1 Decision Product Discovery

Heading: DH-05.02.3 Decision Intelligence Products.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.3.1.1 Decision product user

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.1.1 Decision product user.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.1. The other skills under this competency do a different job.

### What it does
Name the user and the decision the product will sit inside.

### Method
1. Name the role and the moment they decide.
2. Name the current tool they decide in.
3. Name the decision you will not put in this product.

### Do not
Do not discover a decision product from a list of charts.

### Output
A user, a moment, a current tool, a refusal.

A missing fact stays [GAP].

## DH-05.02.3.1.2 Product bet

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.1.2 Product bet.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.1. The other skills under this competency do a different job.

### What it does
Write the bet.

### Method
1. State what the user will do in the product that they cannot do in the current tool.
2. State the metric that will show they did it.
3. Name the smallest version.

### Do not
Do not bet on a platform rewrite.

### Output
A bet, a metric, a smallest version.

A missing fact stays [GAP].

## DH-05.02.3.1.3 Discovery evidence

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.1.3 Discovery evidence.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.1. The other skills under this competency do a different job.

### What it does
Record the evidence for the bet.

### Method
1. Name the users you spoke to and the moment you watched.
2. Quote the step they cannot do today.
3. Stop the bet if you did not see that step.

### Do not
Do not substitute a stakeholder interview for watching the moment.

### Output
Evidence or a stopped bet.

A missing fact stays [GAP].
