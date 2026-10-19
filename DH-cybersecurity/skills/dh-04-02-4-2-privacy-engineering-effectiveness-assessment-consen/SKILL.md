---
name: dh-04-02-4-2-privacy-engineering-effectiveness-assessment-consen
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.02.4.2 Privacy Engineering Effectiveness Assessment & Consent Compliance Monitoring. Use when the user asks for Consent text versus practice, Withdrawal test, Consent compliance owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.02.4.2 Privacy Engineering Effectiveness Assessment & Consent Compliance Monitoring

Heading: DH-04.02.4 Privacy & Consent.
Core: DH-04.02 Cybersecurity & Privacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.02.4.2.1 Consent text versus practice

Worker: Privacy Engineering Director (`privacy-engineering-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.4.2.1 Consent text versus practice.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.4.2. The other skills under this competency do a different job.

### What it does
Compare the consent text with what the system does.

### Method
1. Read the current consent text.
2. List the processing the system performs on that data class.
3. Mark each processing step as described, broader than described, or missing from the text.

### Do not
Do not review a draft text against a future design.

### Output
A comparison of text and processing.

A missing fact stays [GAP].

## DH-04.02.4.2.2 Withdrawal test

Worker: Privacy Engineering Director (`privacy-engineering-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.4.2.2 Withdrawal test.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.4.2. The other skills under this competency do a different job.

### What it does
Test that a withdrawal stops the processing it promises to stop.

### Method
1. Execute a withdrawal in a non-production environment.
2. Check the jobs, exports, and model inputs that should have stopped.
3. Record any job that still ran.

### Do not
Do not pass the test because the preference flag flipped.

### Output
A test note: what stopped, what still ran.

A missing fact stays [GAP].

## DH-04.02.4.2.3 Consent compliance owner

Worker: Privacy Engineering Director (`privacy-engineering-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.4.2.3 Consent compliance owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.4.2. The other skills under this competency do a different job.

### What it does
Assign the mismatch or the failed withdrawal.

### Method
1. Name the owner of the text and the owner of the job, if they differ.
2. State which one must change.
3. Set the version that should contain the fix.

### Do not
Do not assign both owners without saying who moves first.

### Output
One owner, one version.

A missing fact stays [GAP].
