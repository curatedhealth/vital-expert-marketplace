---
name: dh-01-01-4-2-translation-fidelity-assessment-scientific-rigour-m
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.01.4.2 Translation Fidelity Assessment & Scientific Rigour Monitoring. Use when the user asks for Fidelity check, Fidelity sample, Fidelity repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.01.4.2 Translation Fidelity Assessment & Scientific Rigour Monitoring

Heading: DH-01.01.4 Clinical Science Translation.
Core: DH-01.01 Clinical Product Development.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.01.4.2.1 Fidelity check

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.4.2.1 Fidelity check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.4.2. The other skills under this competency do a different job.

### What it does
Define fidelity as the product rule matching the source.

### Method
1. Take one claim from the map.
2. Compare the user-facing text and the population with the source.
3. A fail is a wider population, a stronger verb, or a missing caveat the source had.

### Do not
Do not pass fidelity because the citation is present.

### Output
A fail rule.

A missing fact stays [GAP].

## DH-01.01.4.2.2 Fidelity sample

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.4.2.2 Fidelity sample.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.4.2. The other skills under this competency do a different job.

### What it does
Score a sample of claims.

### Method
1. Take the claims that shipped in this version.
2. Mark each match or fail, and quote the differing words.
3. Mark a claim with no source as fail.

### Do not
Do not sample only the claims that match.

### Output
A sample with quotes.

A missing fact stays [GAP].

## DH-01.01.4.2.3 Fidelity repair

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.4.2.3 Fidelity repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.4.2. The other skills under this competency do a different job.

### What it does
Assign a failed claim.

### Method
1. Name whether the product text or the claim map changes.
2. Name the owner.
3. Name the version that must not ship the failed text.

### Do not
Do not ship the failed text while the repair is open.

### Output
An owner and a version that blocks the text.

A missing fact stays [GAP].
