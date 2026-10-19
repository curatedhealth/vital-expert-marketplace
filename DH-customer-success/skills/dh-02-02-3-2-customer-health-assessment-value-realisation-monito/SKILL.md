---
name: dh-02-02-3-2-customer-health-assessment-value-realisation-monito
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.02.3.2 Customer Health Assessment & Value Realisation Monitoring. Use when the user asks for Health threshold review, Value evidence check, Unsupported note owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02.3.2 Customer Health Assessment & Value Realisation Monitoring

Heading: DH-02.02.3 Customer Health & Value Realization.
Core: DH-02.02 Customer Success & Implementation.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.02.3.2.1 Health threshold review

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.3.2.1 Health threshold review.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.3.2. The other skills under this competency do a different job.

### What it does
Check that the thresholds still match the offer.

### Method
1. Read the current signal list.
2. Flag a threshold no account has ever met.
3. Flag a signal that is no longer stored.

### Do not
Do not lower a threshold only to turn accounts green.

### Output
A review of thresholds.

A missing fact stays [GAP].

## DH-02.02.3.2.2 Value evidence check

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.3.2.2 Value evidence check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.3.2. The other skills under this competency do a different job.

### What it does
Check that a value note is backed by a signal.

### Method
1. Take the notes sent in the period.
2. Match each claimed result to a signal row.
3. Mark a note with no signal row as unsupported.

### Do not
Do not accept a narrative in place of the signal.

### Output
A match of notes to signals.

A missing fact stays [GAP].

## DH-02.02.3.2.3 Unsupported note owner

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.3.2.3 Unsupported note owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.3.2. The other skills under this competency do a different job.

### What it does
Assign unsupported notes.

### Method
1. Name the author of the note.
2. State whether the note is withdrawn or the signal is added.
3. Name the date of the correction.

### Do not
Do not leave an unsupported note in the account record.

### Output
An owner and a correction date.

A missing fact stays [GAP].
