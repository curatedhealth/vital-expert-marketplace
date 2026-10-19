---
name: dh-01-04-1-1-ai-bias-detection-regulatory-grade-governance-imple
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.04.1.1 AI Bias Detection & Regulatory-Grade Governance Implementation. Use when the user asks for Bias question, Bias test, Governance control. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04.1.1 AI Bias Detection & Regulatory-Grade Governance Implementation

Heading: DH-01.04.1 Responsible AI.
Core: DH-01.04 Data Science & AI/ML.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.04.1.1.1 Bias question

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.1.1.1 Bias question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.1.1. The other skills under this competency do a different job.

### What it does
Name the harm and the group this model could disadvantage.

### Method
1. Name the model, the decision it influences, and the groups you will compare.
2. Name the error that harms (false alert, missed deterioration, denied access).
3. Name a group you cannot see in the data, and mark it [GAP].

### Do not
Do not claim fairness from overall accuracy.

### Output
A harm, groups, and an unseen group.

A missing fact stays [GAP].

## DH-01.04.1.1.2 Bias test

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.1.1.2 Bias test.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.1.1. The other skills under this competency do a different job.

### What it does
Run the comparison on a stated dataset.

### Method
1. Name the dataset and the version of the model.
2. Report the error rate for each group you can see.
3. Do not report a group marked [GAP].

### Do not
Do not average the groups into one number and stop.

### Output
Error rates by group, with the dataset version.

A missing fact stays [GAP].

## DH-01.04.1.1.3 Governance control

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.1.1.3 Governance control.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.1.1. The other skills under this competency do a different job.

### What it does
Name the control if a group is worse.

### Method
1. Name the threshold that blocks release.
2. Name who may accept a difference, and the reason they must write.
3. Name the monitoring that continues after release.

### Do not
Do not release a blocked difference without that written reason.

### Output
A threshold, an acceptor, and the monitoring.

A missing fact stays [GAP].
