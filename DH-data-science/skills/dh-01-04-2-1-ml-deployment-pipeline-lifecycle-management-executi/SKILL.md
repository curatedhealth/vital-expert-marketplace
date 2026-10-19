---
name: dh-01-04-2-1-ml-deployment-pipeline-lifecycle-management-executi
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.04.2.1 ML Deployment Pipeline & Lifecycle Management Execution. Use when the user asks for Model promotion rule, Pipeline run, Drift watch. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04.2.1 ML Deployment Pipeline & Lifecycle Management Execution

Heading: DH-01.04.2 MLOps & Monitoring.
Core: DH-01.04 Data Science & AI/ML.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.04.2.1.1 Model promotion rule

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.2.1.1 Model promotion rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.2.1. The other skills under this competency do a different job.

### What it does
Write how a model version moves from experiment to the product.

### Method
1. Name the stages (experiment, validation, production).
2. Name the record each stage requires (dataset version, metric, approver).
3. Name who can promote, and who cannot.

### Do not
Do not promote from a notebook path.

### Output
A promotion rule.

A missing fact stays [GAP].

## DH-01.04.2.1.2 Pipeline run

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.2.1.2 Pipeline run.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.2.1. The other skills under this competency do a different job.

### What it does
Record one run that could be promoted.

### Method
1. Name the code version, the data version, and the metric on the holdout.
2. Name the approver, or say the run is not approved.
3. Store the run id.

### Do not
Do not overwrite a previous run's metric.

### Output
A run record.

A missing fact stays [GAP].

## DH-01.04.2.1.3 Drift watch

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.2.1.3 Drift watch.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.2.1. The other skills under this competency do a different job.

### What it does
Name the signal that pulls a production model back.

### Method
1. Name the input or the outcome you will watch.
2. Name the threshold.
3. Name who is paged and what they may do (retrain, roll back, or stop the decision).

### Do not
Do not watch a metric the product does not log.

### Output
A signal, a threshold, and an action.

A missing fact stays [GAP].
