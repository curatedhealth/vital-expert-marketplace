---
name: "DH-02.04.3.1 Patient & Clinician User Research Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.04.3.1 Patient & Clinician User Research Execution. Use when the user asks for Study question, Session evidence, Research action. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.04.3.1 Patient & Clinician User Research Execution

Heading: DH-02.04.3 User Research.
Core: DH-02.04 User Experience Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.04.3.1.1 Study question

Worker: Patient Experience Designer (`patient-experience-designer`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.3.1.1 Study question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.3.1. The other skills under this competency do a different job.

### What it does
Write the user-research question.

### Method
1. Name the decision the study serves.
2. Name the participant (patient or clinician) and the task.
3. Name what this study will not answer.

### Do not
Do not recruit clinicians for a patient task, or the reverse, without saying so.

### Output
A question, a participant, a task, a non-goal.

A missing fact stays [GAP].

## DH-02.04.3.1.2 Session evidence

Worker: Patient Experience Designer (`patient-experience-designer`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.3.1.2 Session evidence.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.3.1. The other skills under this competency do a different job.

### What it does
Record what happened in the task.

### Method
1. Record where the participant succeeded and where they stopped.
2. Use their words for a confusion.
3. Count participants who hit the same stop.

### Do not
Do not write the finding before the sessions.

### Output
A session record: stops, words, counts.

A missing fact stays [GAP].

## DH-02.04.3.1.3 Research action

Worker: Patient Experience Designer (`patient-experience-designer`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.3.1.3 Research action.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.3.1. The other skills under this competency do a different job.

### What it does
Turn a repeated stop into an action.

### Method
1. Take stops hit by more than one participant.
2. Name the design or content change, or refuse it with a reason.
3. Name the release that will show an accepted change.

### Do not
Do not file the research as insight with no action.

### Output
An action or a refusal per repeated stop.

A missing fact stays [GAP].
