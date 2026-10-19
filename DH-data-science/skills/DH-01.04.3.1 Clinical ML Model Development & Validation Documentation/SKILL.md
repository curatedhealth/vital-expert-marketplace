---
name: "DH-01.04.3.1 Clinical ML Model Development & Validation Documentation"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.04.3.1 Clinical ML Model Development & Validation Documentation. Use when the user asks for Clinical model intended use, Validation dataset, Validation record. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04.3.1 Clinical ML Model Development & Validation Documentation

Heading: DH-01.04.3 Model Development & Validation.
Core: DH-01.04 Data Science & AI/ML.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.04.3.1.1 Clinical model intended use

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.3.1.1 Clinical model intended use.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.3.1. The other skills under this competency do a different job.

### What it does
Write the intended use before validation.

### Method
1. Name the user, the input, the output, and the decision the output may support.
2. Name the decision the output must not make.
3. Name the population.

### Do not
Do not validate a model whose intended use is 'clinical decision support' with no decision named.

### Output
An intended use and a decision it must not make.

A missing fact stays [GAP].

## DH-01.04.3.1.2 Validation dataset

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.3.1.2 Validation dataset.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.3.1. The other skills under this competency do a different job.

### What it does
Lock the dataset the validation will use.

### Method
1. Name the source, the inclusion rule, and the count.
2. State how it differs from the training data, including site or time.
3. Name a population in the intended use that is absent, and mark it [GAP].

### Do not
Do not validate on the training rows.

### Output
A locked dataset, and a gap if the population is absent.

A missing fact stays [GAP].

## DH-01.04.3.1.3 Validation record

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.3.1.3 Validation record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.3.1. The other skills under this competency do a different job.

### What it does
Write the result against the intended use.

### Method
1. Report the metric you named before the run, on the locked dataset.
2. Report the result on the group named in the bias question, if this model has one.
3. Name the model version and the person who accepts the record.

### Do not
Do not add a metric after the run to improve the story.

### Output
A record: metric, version, acceptor.

A missing fact stays [GAP].
