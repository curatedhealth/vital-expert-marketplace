---
name: dh-02-04-4-2-healthcare-ux-effectiveness-assessment-usability-qu
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.04.4.2 Healthcare UX Effectiveness Assessment & Usability Quality Monitoring. Use when the user asks for Usability task score, Control check, UX release note. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.04.4.2 Healthcare UX Effectiveness Assessment & Usability Quality Monitoring

Heading: DH-02.04.4 Healthcare UX Design.
Core: DH-02.04 User Experience Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.04.4.2.1 Usability task score

Worker: Service Design Director (`service-design-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.4.2.1 Usability task score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.4.2. The other skills under this competency do a different job.

### What it does
Score the task with people in the role.

### Method
1. Use the task from the task fit.
2. Observe a stated number of people in that role.
3. Record completion, the misread if it happened, and the old step if they returned to it.

### Do not
Do not use the designer as a participant.

### Output
A score: completed, misread, returned to the old step.

A missing fact stays [GAP].

## DH-02.04.4.2.2 Control check

Worker: Service Design Director (`service-design-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.4.2.2 Control check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.4.2. The other skills under this competency do a different job.

### What it does
Check that the safety control is on the shipped screen.

### Method
1. Open the build.
2. Confirm identity, units, and timestamp where the misread note required them.
3. Mark a missing control as a fail.

### Do not
Do not pass the screen because the mock had the control.

### Output
A control check against the build.

A missing fact stays [GAP].

## DH-02.04.4.2.3 UX release note

Worker: Service Design Director (`service-design-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.4.2.3 UX release note.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.4.2. The other skills under this competency do a different job.

### What it does
Decide whether this task screen ships.

### Method
1. Block shipment if the misread has no control or if participants returned to the old step.
2. Name the owner of a block.
3. Record the decision against the build.

### Do not
Do not ship a task screen that failed the role-based score.

### Output
A decision and a build.

A missing fact stays [GAP].
