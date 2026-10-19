---
name: "DH-02.03.1.1 Patient Research & Co-Design Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.03.1.1 Patient Research & Co-Design Execution. Use when the user asks for Research question, Session capture, Design change from co-design. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.03.1.1 Patient Research & Co-Design Execution

Heading: DH-02.03.1 Patient Insights & Co-Design.
Core: DH-02.03 Patient Engagement & Advocacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.03.1.1.1 Research question

Worker: Patient Experience Designer (`patient-experience-designer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.1.1.1 Research question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.1.1. The other skills under this competency do a different job.

### What it does
Write the question this co-design session will answer.

### Method
1. Name the decision the question serves.
2. Name who will be in the session (patient, carer, or both) and why.
3. Name what the session will not decide.

### Do not
Do not recruit before the question is written.

### Output
A question, a participant type, and a non-goal.

A missing fact stays [GAP].

## DH-02.03.1.1.2 Session capture

Worker: Patient Experience Designer (`patient-experience-designer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.1.1.2 Session capture.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.1.1. The other skills under this competency do a different job.

### What it does
Capture what participants said against the question.

### Method
1. Record claims in their words.
2. Separate a request from an observation.
3. Note how many participants raised each point.

### Do not
Do not replace their words with a product requirement in the capture.

### Output
A capture: words, request or observation, count.

A missing fact stays [GAP].

## DH-02.03.1.1.3 Design change from co-design

Worker: Patient Experience Designer (`patient-experience-designer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.1.1.3 Design change from co-design.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.1.1. The other skills under this competency do a different job.

### What it does
Turn a repeated point into a design change or a refusal.

### Method
1. Take points raised by more than one participant.
2. Accept a change, defer it, or refuse it, with a reason.
3. Name the product version that will show an accepted change.

### Do not
Do not accept a change that contradicts a safety constraint without saying so.

### Output
A decision per repeated point.

A missing fact stays [GAP].
