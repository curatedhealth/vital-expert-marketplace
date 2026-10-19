---
name: "DH-05.02.1.2 Self-Service Templates & Tooling"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.1.2 Self-Service Templates & Tooling. Use when the user asks for Template purpose, Template contents, Template retirement. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.1.2 Self-Service Templates & Tooling

Heading: DH-05.02.1 Self-Service BI Enablement.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.1.2.1 Template purpose

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.2.1 Template purpose.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.2. The other skills under this competency do a different job.

### What it does
Write what one self-service template is for.

### Method
1. Name the audience and the decision.
2. Name the certified metrics it may use.
3. Name the fields the audience may filter.

### Do not
Do not give a template raw tables when a certified metric exists.

### Output
A template purpose.

A missing fact stays [GAP].

## DH-05.02.1.2.2 Template contents

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.2.2 Template contents.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.2. The other skills under this competency do a different job.

### What it does
Build the template from those metrics.

### Method
1. Place the metrics and the allowed filters.
2. Name the empty state when a filter returns nothing.
3. Name the owner who fixes a broken metric.

### Do not
Do not add a local calculation that disagrees with the semantic layer.

### Output
A template and an owner.

A missing fact stays [GAP].

## DH-05.02.1.2.3 Template retirement

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.2.3 Template retirement.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.2. The other skills under this competency do a different job.

### What it does
Retire a template that no longer matches a decision.

### Method
1. Name the template and the last date it was used, if known.
2. Name the template that replaces it, or say none.
3. Name who tells the audience.

### Do not
Do not leave two templates for the same decision.

### Output
A retirement note.

A missing fact stays [GAP].
