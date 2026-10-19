---
name: "DH-05.01.2.1 Prediction & Classification Modeling"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.01.2.1 Prediction & Classification Modeling. Use when the user asks for Prediction target, Train and holdout, Score limit. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.01.2.1 Prediction & Classification Modeling

Heading: DH-05.01.2 Machine Learning Applications.
Core: DH-05.01 Advanced Analytics & Data Science.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.01.2.1.1 Prediction target

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.1.1 Prediction target.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.1. The other skills under this competency do a different job.

### What it does
Define the label the classifier will learn.

### Method
1. Name the event, the time window, and the unit.
2. Write the label rule so two people would label a row the same way.
3. Name rows that are excluded (insufficient follow-up, wrong population).

### Do not
Do not use a proxy label without naming what it is a proxy for.

### Output
A label rule and an exclusion rule.

A missing fact stays [GAP].

## DH-05.01.2.1.2 Train and holdout

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.1.2 Train and holdout.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.1. The other skills under this competency do a different job.

### What it does
Train on one set and report on another.

### Method
1. State the split, including any split by patient or site so the same person is not in both.
2. Report the metric you chose before training.
3. Report performance on the group that would be harmed by a miss, not only the average.

### Do not
Do not report training-set performance as the result.

### Output
A holdout result, including the harmed group.

A missing fact stays [GAP].

## DH-05.01.2.1.3 Score limit

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.1.3 Score limit.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.1. The other skills under this competency do a different job.

### What it does
Write the limit on using the score.

### Method
1. Name who may see the score and what action it may trigger.
2. Name the population outside the training support.
3. Name the owner of a review before it triggers an action.

### Do not
Do not connect a score to a clinical action without that owner.

### Output
A use limit and a reviewer.

A missing fact stays [GAP].
