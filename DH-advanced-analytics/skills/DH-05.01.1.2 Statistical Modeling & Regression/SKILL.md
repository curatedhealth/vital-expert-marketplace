---
name: "DH-05.01.1.2 Statistical Modeling & Regression"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.01.1.2 Statistical Modeling & Regression. Use when the user asks for Model target, Fit and check, Model limit. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.01.1.2 Statistical Modeling & Regression

Heading: DH-05.01.1 Statistical Modeling & Inference.
Core: DH-05.01 Advanced Analytics & Data Science.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.01.1.2.1 Model target

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.2.1 Model target.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.2. The other skills under this competency do a different job.

### What it does
Name what the regression is predicting or explaining.

### Method
1. Name the outcome and the unit of the row.
2. Name the predictors you will use and the ones you will not.
3. Name the use (description or prediction).

### Do not
Do not add a predictor because it is in the table.

### Output
A target, a unit, a predictor list.

A missing fact stays [GAP].

## DH-05.01.1.2.2 Fit and check

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.2.2 Fit and check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.2. The other skills under this competency do a different job.

### What it does
Fit the model and check the assumption you named.

### Method
1. Fit on a stated sample and hold out a stated sample when the use is prediction.
2. Check the assumption (linearity, separation, leakage) that would invalidate the use.
3. Record the metric that matches the use, not every metric.

### Do not
Do not pick the metric after seeing which one looks best.

### Output
A fit note: sample, check, metric.

A missing fact stays [GAP].

## DH-05.01.1.2.3 Model limit

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.2.3 Model limit.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.2. The other skills under this competency do a different job.

### What it does
Write where the model must not be used.

### Method
1. Name the population or the period outside the sample.
2. Name the decision it must not drive.
3. Name the owner who may promote it.

### Do not
Do not deploy a descriptive model as a clinical score.

### Output
A limit and an owner.

A missing fact stays [GAP].
