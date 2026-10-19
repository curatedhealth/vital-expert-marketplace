---
name: "DH-05.01.2.2 Recommendation & Personalization"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.01.2.2 Recommendation & Personalization. Use when the user asks for Recommendation unit, Policy, Recommendation log. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.01.2.2 Recommendation & Personalization

Heading: DH-05.01.2 Machine Learning Applications.
Core: DH-05.01 Advanced Analytics & Data Science.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.01.2.2.1 Recommendation unit

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.2.1 Recommendation unit.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.2. The other skills under this competency do a different job.

### What it does
Name what is being recommended to whom.

### Method
1. Name the user and the item (content, action, next step).
2. Name the objective (complete a task, not click).
3. Name a recommendation you will not make.

### Do not
Do not optimize a click when the objective is a completed clinical task.

### Output
A unit, an objective, a refusal.

A missing fact stays [GAP].

## DH-05.01.2.2.2 Policy

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.2.2 Policy.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.2. The other skills under this competency do a different job.

### What it does
Write the rule that produces the recommendation.

### Method
1. State the inputs the policy may use.
2. State the rule or the model version.
3. State how a person refuses the recommendation.

### Do not
Do not use an input the user was not told about when the product says it explains the recommendation.

### Output
A policy: inputs, version, refusal path.

A missing fact stays [GAP].

## DH-05.01.2.2.3 Recommendation log

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.2.2.3 Recommendation log.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.2.2. The other skills under this competency do a different job.

### What it does
Log what was recommended and what was done.

### Method
1. Log the user role, the item, the policy version, and the time.
2. Log accept, dismiss, or no action.
3. Keep the log long enough to review a complaint.

### Do not
Do not log the recommendation without the outcome.

### Output
A log definition.

A missing fact stays [GAP].
