---
name: dh-01-04-2-2-mlops-effectiveness-assessment-model-drift-monitori
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.04.2.2 MLOps Effectiveness Assessment & Model Drift Monitoring. Use when the user asks for MLOps check, Promotion score, Drift response. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04.2.2 MLOps Effectiveness Assessment & Model Drift Monitoring

Heading: DH-01.04.2 MLOps & Monitoring.
Core: DH-01.04 Data Science & AI/ML.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.04.2.2.1 MLOps check

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.2.2.1 MLOps check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.2.2. The other skills under this competency do a different job.

### What it does
Define a healthy promotion.

### Method
1. A pass has a run id, a holdout metric, and an approver.
2. A fail is a production model with no run id.
3. Name the period.

### Do not
Do not pass a model because it is popular with users.

### Output
A check.

A missing fact stays [GAP].

## DH-01.04.2.2.2 Promotion score

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.2.2.2 Promotion score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.2.2. The other skills under this competency do a different job.

### What it does
Score the models in production.

### Method
1. List each model version, its run id, and whether the drift watch has fired.
2. Mark a fired watch as open.
3. Note a model with no watch.

### Do not
Do not ignore a fired watch because the average metric is fine.

### Output
A score.

A missing fact stays [GAP].

## DH-01.04.2.2.3 Drift response

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.2.2.3 Drift response.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.2.2. The other skills under this competency do a different job.

### What it does
Assign a fired watch.

### Method
1. Name the owner.
2. State retrain, roll back, or stop the decision.
3. Name the version that replaces the current one, or the time the decision stays stopped.

### Do not
Do not leave a fired watch with no action.

### Output
An action and a version or a stop.

A missing fact stays [GAP].
