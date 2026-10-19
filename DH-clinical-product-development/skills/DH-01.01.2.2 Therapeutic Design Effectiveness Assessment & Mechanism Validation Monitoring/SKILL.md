---
name: "DH-01.01.2.2 Therapeutic Design Effectiveness Assessment & Mechanism Validation Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.01.2.2 Therapeutic Design Effectiveness Assessment & Mechanism Validation Monitoring. Use when the user asks for Mechanism check, Mechanism score, Mechanism miss. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.01.2.2 Therapeutic Design Effectiveness Assessment & Mechanism Validation Monitoring

Heading: DH-01.01.2 Therapeutic Design.
Core: DH-01.01 Clinical Product Development.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.01.2.2.1 Mechanism check

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.2.2.1 Mechanism check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.2.2. The other skills under this competency do a different job.

### What it does
Define what counts as evidence the mechanism happened.

### Method
1. Name the link you will check (action taken, change observed, outcome moved).
2. Name the measure for that link.
3. Name a link you cannot measure yet, and mark it [GAP].

### Do not
Do not treat use of the app as proof of the outcome.

### Output
A check per link, or a gap.

A missing fact stays [GAP].

## DH-01.01.2.2.2 Mechanism score

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.2.2.2 Mechanism score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.2.2. The other skills under this competency do a different job.

### What it does
Score one study or one live cohort against the check.

### Method
1. Name the cohort and the version of the intervention.
2. Mark each measurable link met or missed, with the source.
3. Do not score the link marked [GAP].

### Do not
Do not fill a gap with a proxy you did not name in advance.

### Output
A score for the measurable links.

A missing fact stays [GAP].

## DH-01.01.2.2.3 Mechanism miss

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.2.2.3 Mechanism miss.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.2.2. The other skills under this competency do a different job.

### What it does
Assign a missed link.

### Method
1. Name the link and the owner (design, evidence, or population).
2. State whether the component changes or the claim is narrowed.
3. Name the version that will carry the change.

### Do not
Do not keep a claim for a link that missed.

### Output
An owner, a change or a narrowed claim, and a version.

A missing fact stays [GAP].
