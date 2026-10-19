---
name: dh-01-04-3-2-model-validation-quality-assessment-performance-mon
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.04.3.2 Model Validation Quality Assessment & Performance Monitoring. Use when the user asks for Validation completeness, Validation score, Validation miss. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04.3.2 Model Validation Quality Assessment & Performance Monitoring

Heading: DH-01.04.3 Model Development & Validation.
Core: DH-01.04 Data Science & AI/ML.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.04.3.2.1 Validation completeness

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.3.2.1 Validation completeness.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.3.2. The other skills under this competency do a different job.

### What it does
Define a complete validation.

### Method
1. A pass has an intended use, a locked dataset that is not the training set, and a pre-named metric.
2. A fail is a missing population presented as validated.
3. Name the model you will score.

### Do not
Do not pass on an internal demo.

### Output
A completeness rule.

A missing fact stays [GAP].

## DH-01.04.3.2.2 Validation score

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.3.2.2 Validation score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.3.2. The other skills under this competency do a different job.

### What it does
Score the record.

### Method
1. Check each required item.
2. Quote the metric and the dataset version.
3. Mark the absent population as not validated.

### Do not
Do not treat a high metric as completeness.

### Output
A score.

A missing fact stays [GAP].

## DH-01.04.3.2.3 Validation miss

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.3.2.3 Validation miss.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.3.2. The other skills under this competency do a different job.

### What it does
Assign an incomplete validation.

### Method
1. Name the missing item and the owner.
2. State whether the model may influence a decision.
3. Name the date the record will be complete.

### Do not
Do not let an incomplete model influence the named decision.

### Output
An owner and whether the decision waits.

A missing fact stays [GAP].
