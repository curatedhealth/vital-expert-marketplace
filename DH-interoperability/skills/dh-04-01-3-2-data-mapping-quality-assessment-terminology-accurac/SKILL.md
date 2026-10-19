---
name: dh-04-01-3-2-data-mapping-quality-assessment-terminology-accurac
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.01.3.2 Data Mapping Quality Assessment & Terminology Accuracy Monitoring. Use when the user asks for Map sample definition, Blinded clinical review, Map error classes. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.01.3.2 Data Mapping Quality Assessment & Terminology Accuracy Monitoring

Heading: DH-04.01.3 Data Exchange & Terminology.
Core: DH-04.01 Clinical Integration & Interoperability.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.01.3.2.1 Map sample definition

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.3.2.1 Map sample definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.3.2. The other skills under this competency do a different job.

### What it does
Decide which map rows will be checked and what rate counts as a pass.

### Method
1. State the sample size and how rows are drawn (random, or stratified by code system).
2. Define exact-match rate and unmatched rate.
3. Set the threshold the map must clear before production use.

### Do not
Do not sample only the rows that were hand-checked yesterday.

### Output
A sampling note with the two rates and the threshold.

A missing fact stays [GAP].

## DH-04.01.3.2.2 Blinded clinical review

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.3.2.2 Blinded clinical review.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.3.2. The other skills under this competency do a different job.

### What it does
Have a clinician review a subset without seeing the mapper's equivalence label.

### Method
1. Draw a subset from the sample.
2. Ask the reviewer to say whether the target code is acceptable for the stated use.
3. Compare the reviewer's judgment to the equivalence label and count disagreements.

### Do not
Do not use the person who wrote the map as the only reviewer.

### Output
A disagreement count and the rows the reviewer rejected.

A missing fact stays [GAP].

## DH-04.01.3.2.3 Map error classes

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.3.2.3 Map error classes.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.3.2. The other skills under this competency do a different job.

### What it does
Group the errors so the next map version fixes a class, not a single row.

### Method
1. Class each error (wrong target system, equivalence too strong, stale code, uncoded source).
2. Attach the class to the map version.
3. Name the class that blocks the threshold.

### Do not
Do not publish a new map version that leaves the blocking class untouched.

### Output
An error-class table tied to the map version.

A missing fact stays [GAP].
