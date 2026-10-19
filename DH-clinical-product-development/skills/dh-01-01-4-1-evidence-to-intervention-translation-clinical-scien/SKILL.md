---
name: dh-01-01-4-1-evidence-to-intervention-translation-clinical-scien
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.01.4.1 Evidence-to-Intervention Translation & Clinical Science Application. Use when the user asks for Evidence claim map, Intervention rule, Translation limit. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.01.4.1 Evidence-to-Intervention Translation & Clinical Science Application

Heading: DH-01.01.4 Clinical Science Translation.
Core: DH-01.01 Clinical Product Development.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.01.4.1.1 Evidence claim map

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.4.1.1 Evidence claim map.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.4.1. The other skills under this competency do a different job.

### What it does
Map each product claim to the evidence that supports it.

### Method
1. List the claims the product will make.
2. Point each claim at a study, a guideline, or mark it [GAP].
3. Name a claim you will not make.

### Do not
Do not write an intervention from a claim that is [GAP].

### Output
A map: claim, source or gap, and a claim refused.

A missing fact stays [GAP].

## DH-01.01.4.1.2 Intervention rule

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.4.1.2 Intervention rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.4.1. The other skills under this competency do a different job.

### What it does
Turn a supported claim into a rule the product follows.

### Method
1. Take a claim that has a source.
2. Write the rule (who receives the intervention, when, and what they are shown or asked).
3. Name the claim text the user will see, matching the source.

### Do not
Do not widen the population beyond the source.

### Output
A rule and the claim text.

A missing fact stays [GAP].

## DH-01.01.4.1.3 Translation limit

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.4.1.3 Translation limit.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.4.1. The other skills under this competency do a different job.

### What it does
Write where the evidence does not justify the product.

### Method
1. Name the population, dose, or duration the source does not cover.
2. Name the product behavior that stays off because of that limit.
3. Name who may reopen the limit when new evidence exists.

### Do not
Do not reopen the limit because a stakeholder asked.

### Output
A limit, the behavior that stays off, and who may reopen it.

A missing fact stays [GAP].
