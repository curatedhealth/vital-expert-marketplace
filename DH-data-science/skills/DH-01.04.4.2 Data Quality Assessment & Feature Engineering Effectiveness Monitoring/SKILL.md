---
name: "DH-01.04.4.2 Data Quality Assessment & Feature Engineering Effectiveness Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.04.4.2 Data Quality Assessment & Feature Engineering Effectiveness Monitoring. Use when the user asks for Data quality rule, Data quality score, Feature repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04.4.2 Data Quality Assessment & Feature Engineering Effectiveness Monitoring

Heading: DH-01.04.4 Data & Modeling.
Core: DH-01.04 Data Science & AI/ML.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.04.4.2.1 Data quality rule

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.4.2.1 Data quality rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.4.2. The other skills under this competency do a different job.

### What it does
Define the checks this dataset must pass.

### Method
1. Name the checks (unit of row, exclusion count, missingness of the decision-time features, no outcome leak).
2. Set a fail for each.
3. Name the dataset version.

### Do not
Do not use a single completeness percentage as the only check.

### Output
A rule.

A missing fact stays [GAP].

## DH-01.04.4.2.2 Data quality score

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.4.2.2 Data quality score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.4.2. The other skills under this competency do a different job.

### What it does
Run the checks.

### Method
1. Run each check and keep the count.
2. Mark pass or fail.
3. Name a feature that failed the leak check.

### Do not
Do not drop a failed feature quietly and report a pass.

### Output
A score.

A missing fact stays [GAP].

## DH-01.04.4.2.3 Feature repair

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.4.2.3 Feature repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.4.2. The other skills under this competency do a different job.

### What it does
Assign a failed check.

### Method
1. Name the owner.
2. State whether the feature is removed or redefined.
3. Name the new dataset version.

### Do not
Do not train on the failed version.

### Output
An owner and a new version.

A missing fact stays [GAP].
