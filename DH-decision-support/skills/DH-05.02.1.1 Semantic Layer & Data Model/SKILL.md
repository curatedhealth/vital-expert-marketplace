---
name: "DH-05.02.1.1 Semantic Layer & Data Model"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.1.1 Semantic Layer & Data Model. Use when the user asks for Metric on the semantic layer, Entity the metric hangs on, Layer change. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.1.1 Semantic Layer & Data Model

Heading: DH-05.02.1 Self-Service BI Enablement.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.1.1.1 Metric on the semantic layer

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.1.1 Metric on the semantic layer.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.1. The other skills under this competency do a different job.

### What it does
Define one metric in the semantic layer.

### Method
1. Name the metric, the grain, and the formula.
2. Name the certified source tables.
3. Name the metrics that must not be recomputed beside it.

### Do not
Do not leave the formula only in a dashboard.

### Output
A metric definition in the layer.

A missing fact stays [GAP].

## DH-05.02.1.1.2 Entity the metric hangs on

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.1.2 Entity the metric hangs on.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.1. The other skills under this competency do a different job.

### What it does
Name the business entity the metric describes.

### Method
1. Name the entity (account, patient-episode, order) and its key.
2. Name which attributes are allowed as filters.
3. Name an attribute that is not a filter because it leaks or it is unstable.

### Do not
Do not let every column become a filter.

### Output
An entity, a key, and allowed filters.

A missing fact stays [GAP].

## DH-05.02.1.1.3 Layer change

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.1.3 Layer change.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.1. The other skills under this competency do a different job.

### What it does
Change the metric without breaking published dashboards.

### Method
1. Name the change and the dashboards that use the metric.
2. State whether the change is a new version or a correction.
3. Name who is told before the correction ships.

### Do not
Do not correct a formula silently.

### Output
A change, the dashboards, and who is told.

A missing fact stays [GAP].
