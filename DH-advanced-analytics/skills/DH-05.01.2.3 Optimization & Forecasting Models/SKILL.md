---
name: "DH-05.01.2.3 Optimization & Forecasting Models"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.01.2.3 Optimization & Forecasting Models. Use when the user asks for Forecast target, Forecast and interval, Optimization constraint. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.01.2.3 Optimization & Forecasting Models

Heading: DH-05.01.2 Machine Learning Applications.
Core: DH-05.01 Advanced Analytics & Data Science.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.01.2.3.1 Forecast target

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.3.1 Forecast target.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.3. The other skills under this competency do a different job.

### What it does
Name the quantity and the horizon.

### Method
1. Name the quantity, the grain, and the horizon.
2. Name the decision that uses the forecast.
3. Name the baseline you will beat (last period, seasonal naive).

### Do not
Do not forecast without a baseline.

### Output
A target, a horizon, a baseline.

A missing fact stays [GAP].

## DH-05.01.2.3.2 Forecast and interval

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.3.2 Forecast and interval.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.3. The other skills under this competency do a different job.

### What it does
Produce the forecast and an interval.

### Method
1. Fit on a stated history.
2. Report the point and the interval on a holdout horizon.
3. Compare it with the baseline on that same horizon.

### Do not
Do not report accuracy on the history you fit.

### Output
A holdout comparison against the baseline.

A missing fact stays [GAP].

## DH-05.01.2.3.3 Optimization constraint

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.3.3 Optimization constraint.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.3. The other skills under this competency do a different job.

### What it does
Write the constraint the optimizer must not break.

### Method
1. Name the decision variables.
2. Name the constraint (capacity, safety stock, fairness, budget).
3. Name who may relax the constraint.

### Do not
Do not return an optimum that breaks a safety constraint.

### Output
Variables, a constraint, and who may relax it.

A missing fact stays [GAP].
