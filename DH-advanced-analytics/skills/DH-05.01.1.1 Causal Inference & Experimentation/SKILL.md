---
name: "DH-05.01.1.1 Causal Inference & Experimentation"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.01.1.1 Causal Inference & Experimentation. Use when the user asks for Causal question, Design choice, Estimate record. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.01.1.1 Causal Inference & Experimentation

Heading: DH-05.01.1 Statistical Modeling & Inference.
Core: DH-05.01 Advanced Analytics & Data Science.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.01.1.1.1 Causal question

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.1.1 Causal question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.1. The other skills under this competency do a different job.

### What it does
Write the causal question before choosing a method.

### Method
1. Name the treatment, the outcome, and the population.
2. Name the decision the answer will change.
3. Name a confounder you can see and one you cannot.

### Do not
Do not start with a model class.

### Output
A question: treatment, outcome, population, confounders.

A missing fact stays [GAP].

## DH-05.01.1.1.2 Design choice

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.1.2 Design choice.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.1. The other skills under this competency do a different job.

### What it does
Choose the design that the data can support.

### Method
1. State whether you have an experiment, a natural experiment, or only observational rows.
2. Name the method (trial, difference-in-differences, matching) that fits that fact.
3. Refuse a causal claim when the design cannot support it, and say what you will estimate instead.

### Do not
Do not call an observational association an effect.

### Output
A design, or a refusal.

A missing fact stays [GAP].

## DH-05.01.1.1.3 Estimate record

Worker: AI/ML Healthcare Researcher (`ai-ml-healthcare-researcher`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.1.1.3 Estimate record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.1.1. The other skills under this competency do a different job.

### What it does
Record the estimate with its uncertainty.

### Method
1. Report the estimate, the interval, and the sample.
2. State the assumption that, if wrong, reverses the decision.
3. Point at the code and the data version.

### Do not
Do not report a point estimate alone.

### Output
An estimate, an interval, a breaking assumption, a data version.

A missing fact stays [GAP].
