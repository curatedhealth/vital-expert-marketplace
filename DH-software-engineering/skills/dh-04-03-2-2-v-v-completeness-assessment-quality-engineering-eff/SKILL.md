---
name: dh-04-03-2-2-v-v-completeness-assessment-quality-engineering-eff
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.03.2.2 V&V Completeness Assessment & Quality Engineering Effectiveness Monitoring. Use when the user asks for Trace from hazard to case, Build under test, Open validation miss. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.03.2.2 V&V Completeness Assessment & Quality Engineering Effectiveness Monitoring

Heading: DH-04.03.2 Quality Engineering.
Core: DH-04.03 Software Engineering Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.03.2.2.1 Trace from hazard to case

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.2.2.1 Trace from hazard to case.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.2.2. The other skills under this competency do a different job.

### What it does
Check that each hazard has at least one case.

### Method
1. List the hazards from the intended-use note.
2. Point each hazard at a verification or validation case.
3. Mark a hazard with no case as an open gap.

### Do not
Do not count a unit test that does not exercise the hazard.

### Output
A trace table: hazard, case id, or gap.

A missing fact stays [GAP].

## DH-04.03.2.2.2 Build under test

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.2.2.2 Build under test.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.2.2. The other skills under this competency do a different job.

### What it does
Confirm the cases were run on the build that will ship.

### Method
1. Compare the build id on the case records with the release candidate.
2. List cases that were run on an older build.
3. Require those cases to be repeated or explicitly waived.

### Do not
Do not carry a pass forward across a build that changed the hazardous function.

### Output
A build-match list.

A missing fact stays [GAP].

## DH-04.03.2.2.3 Open validation miss

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.2.2.3 Open validation miss.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.2.2. The other skills under this competency do a different job.

### What it does
Decide what happens to a miss before release.

### Method
1. State whether the miss blocks release.
2. If it does not block, name who accepted it and what the user is told.
3. If it blocks, name the owner of the fix.

### Do not
Do not close a miss by editing the expected result after the run.

### Output
A release decision per open miss.

A missing fact stays [GAP].
