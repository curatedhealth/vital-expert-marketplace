---
name: "DH-05.01.1.3 Bayesian & Uncertainty Quantification"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.01.1.3 Bayesian & Uncertainty Quantification. Use when the user asks for Uncertainty question, Posterior or interval, Sensitivity of the prior. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.01.1.3 Bayesian & Uncertainty Quantification

Heading: DH-05.01.1 Statistical Modeling & Inference.
Core: DH-05.01 Advanced Analytics & Data Science.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.01.1.3.1 Uncertainty question

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.3.1 Uncertainty question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.3. The other skills under this competency do a different job.

### What it does
Name the uncertainty the decision needs.

### Method
1. Name the quantity (a rate, a treatment effect, a forecast).
2. Name the decision threshold.
3. Name whether a prior will be used, and its source.

### Do not
Do not use a prior you cannot cite.

### Output
A quantity, a threshold, a prior or none.

A missing fact stays [GAP].

## DH-05.01.1.3.2 Posterior or interval

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.3.2 Posterior or interval.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.3. The other skills under this competency do a different job.

### What it does
Produce the uncertainty statement.

### Method
1. Compute the interval or the posterior for the quantity.
2. Show the probability of crossing the decision threshold, if that was the question.
3. Show the data version.

### Do not
Do not replace the interval with a star rating.

### Output
An uncertainty statement tied to the threshold.

A missing fact stays [GAP].

## DH-05.01.1.3.3 Sensitivity of the prior

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.3.3 Sensitivity of the prior.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.3. The other skills under this competency do a different job.

### What it does
Show what changes if the prior is wrong.

### Method
1. Refit with a stated alternative prior, or with no prior.
2. Say whether the threshold decision changes.
3. Keep both results.

### Do not
Do not hide the result that reverses the decision.

### Output
Both results and whether the decision holds.

A missing fact stays [GAP].
