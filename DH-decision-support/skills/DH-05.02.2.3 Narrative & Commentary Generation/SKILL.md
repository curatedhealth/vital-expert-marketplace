---
name: "DH-05.02.2.3 Narrative & Commentary Generation"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.2.3 Narrative & Commentary Generation. Use when the user asks for Commentary claim, Driver, Commentary text. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.2.3 Narrative & Commentary Generation

Heading: DH-05.02.2 Executive Dashboards & Reporting.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.2.3.1 Commentary claim

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.3.1 Commentary claim.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.3. The other skills under this competency do a different job.

### What it does
Write the sentence the commentary will stand on.

### Method
1. Name the metric move you will explain.
2. Name the comparison (prior period or target).
3. Refuse a sentence the metric does not support.

### Do not
Do not explain a move you have not measured.

### Output
One sentence tied to a metric.

A missing fact stays [GAP].

## DH-05.02.2.3.2 Driver

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.3.2 Driver.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.3. The other skills under this competency do a different job.

### What it does
Name the driver you will cite.

### Method
1. Name the breakdown (segment, site, product) that accounts for the move.
2. Show the numbers in that breakdown.
3. Stop if no breakdown accounts for the move, and say so.

### Do not
Do not invent a driver.

### Output
A driver with numbers, or a stop.

A missing fact stays [GAP].

## DH-05.02.2.3.3 Commentary text

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.3.3 Commentary text.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.3. The other skills under this competency do a different job.

### What it does
Write the commentary from the sentence and the driver.

### Method
1. Use the sentence and the driver only.
2. Name the action the audience might take, as a question rather than an order, unless the decision frame named an action.
3. Date the commentary and name the author.

### Do not
Do not add a second claim.

### Output
A dated commentary.

A missing fact stays [GAP].
