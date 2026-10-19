---
name: dh-02-02-2-2-expansion-effectiveness-assessment-renewal-rate-mon
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.02.2.2 Expansion Effectiveness Assessment & Renewal Rate Monitoring. Use when the user asks for Renewal rate definition, Cohort score, Expansion result. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02.2.2 Expansion Effectiveness Assessment & Renewal Rate Monitoring

Heading: DH-02.02.2 Expansion & Renewal.
Core: DH-02.02 Customer Success & Implementation.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.02.2.2.1 Renewal rate definition

Worker: Digital Partnerships Director (`digital-partnerships-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.2.2.1 Renewal rate definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.2.2. The other skills under this competency do a different job.

### What it does
Define the renewal rate you will report.

### Method
1. Name the cohort (accounts with a renewal date in the period).
2. Define renewed as a signed continuation of the same unit or a written successor.
3. Exclude pilots that were never annual contracts.

### Do not
Do not count a verbal intent as renewed.

### Output
A cohort definition.

A missing fact stays [GAP].

## DH-02.02.2.2.2 Cohort score

Worker: Digital Partnerships Director (`digital-partnerships-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.2.2.2 Cohort score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.2.2. The other skills under this competency do a different job.

### What it does
Score the cohort.

### Method
1. List each account as renewed, lost, or open.
2. Keep the contract id.
3. Separate a loss on price from a loss on an open implementation.

### Do not
Do not drop open accounts from the denominator.

### Output
A cohort score with contract ids.

A missing fact stays [GAP].

## DH-02.02.2.2.3 Expansion result

Worker: Digital Partnerships Director (`digital-partnerships-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.2.2.3 Expansion result.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.2.2. The other skills under this competency do a different job.

### What it does
Record whether ready accounts took the growth offer.

### Method
1. Match offers to signed expansions.
2. Name offers that were refused and the reason given.
3. Assign an owner where the reason was an unseen result.

### Do not
Do not count a meeting as an expansion.

### Output
A match of offers to outcomes.

A missing fact stays [GAP].
