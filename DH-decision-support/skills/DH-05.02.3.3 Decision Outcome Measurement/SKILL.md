---
name: "DH-05.02.3.3 Decision Outcome Measurement"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.3.3 Decision Outcome Measurement. Use when the user asks for Outcome of the decision, Outcome measurement, Bet review. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.3.3 Decision Outcome Measurement

Heading: DH-05.02.3 Decision Intelligence Products.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.3.3.1 Outcome of the decision

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.3.1 Outcome of the decision.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.3. The other skills under this competency do a different job.

### What it does
Name the outcome that shows the decision product worked.

### Method
1. Use the metric from the bet.
2. Name the window after the user acts.
3. Name the comparison (before the product, or users who did not get it).

### Do not
Do not use page views as the outcome.

### Output
An outcome, a window, a comparison.

A missing fact stays [GAP].

## DH-05.02.3.3.2 Outcome measurement

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.3.2 Outcome measurement.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.3. The other skills under this competency do a different job.

### What it does
Measure it.

### Method
1. Count the outcome in the window.
2. Keep the comparison.
3. State the number of users.

### Do not
Do not report a change without the comparison.

### Output
A measurement.

A missing fact stays [GAP].

## DH-05.02.3.3.3 Bet review

Worker: Data & Analytics Lead (`data-analytics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.3.3.3 Bet review.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.3.3. The other skills under this competency do a different job.

### What it does
Keep, change, or stop the product.

### Method
1. Compare the measurement with the bet.
2. Choose keep, change the insertion, or stop.
3. Name the owner of that choice.

### Do not
Do not keep a product whose outcome was not measured.

### Output
A choice and an owner.

A missing fact stays [GAP].
