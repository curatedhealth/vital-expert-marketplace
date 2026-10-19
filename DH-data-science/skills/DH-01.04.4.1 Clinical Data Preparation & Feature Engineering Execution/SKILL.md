---
name: "DH-01.04.4.1 Clinical Data Preparation & Feature Engineering Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.04.4.1 Clinical Data Preparation & Feature Engineering Execution. Use when the user asks for Cohort rule, Feature definition, Data handoff. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04.4.1 Clinical Data Preparation & Feature Engineering Execution

Heading: DH-01.04.4 Data & Modeling.
Core: DH-01.04 Data Science & AI/ML.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.04.4.1.1 Cohort rule

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.4.1.1 Cohort rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.4.1. The other skills under this competency do a different job.

### What it does
Write who is in the dataset.

### Method
1. Name the population, the time window, and the care setting.
2. Name the exclusions.
3. Name the unit of a row (patient, encounter, device-day).

### Do not
Do not pull every row in the warehouse.

### Output
A cohort rule.

A missing fact stays [GAP].

## DH-01.04.4.1.2 Feature definition

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.4.1.2 Feature definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.4.1. The other skills under this competency do a different job.

### What it does
Define one feature so it can be rebuilt.

### Method
1. Name the feature, the source field, and the window it is computed over.
2. Name the value that means missing.
3. Name a feature you will not use because it leaks the outcome or it is not available at decision time.

### Do not
Do not use a feature that is only known after the outcome.

### Output
A definition, and a feature refused.

A missing fact stays [GAP].

## DH-01.04.4.1.3 Data handoff

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.4.1.3 Data handoff.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.4.1. The other skills under this competency do a different job.

### What it does
Hand the dataset to the model owner with its limits.

### Method
1. Name the dataset version and the cohort rule.
2. Name the missingness that remains.
3. Name who may change the cohort rule.

### Do not
Do not hand a dataset with no version.

### Output
A handoff: version, missingness, who may change the rule.

A missing fact stays [GAP].
