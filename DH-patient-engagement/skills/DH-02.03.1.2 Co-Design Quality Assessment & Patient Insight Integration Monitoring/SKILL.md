---
name: "DH-02.03.1.2 Co-Design Quality Assessment & Patient Insight Integration Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.03.1.2 Co-Design Quality Assessment & Patient Insight Integration Monitoring. Use when the user asks for Co-design trace, Participant fit, Unresolved point. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.03.1.2 Co-Design Quality Assessment & Patient Insight Integration Monitoring

Heading: DH-02.03.1 Patient Insights & Co-Design.
Core: DH-02.03 Patient Engagement & Advocacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.03.1.2.1 Co-design trace

Worker: Patient Experience Designer (`patient-experience-designer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.1.2.1 Co-design trace.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.1.2. The other skills under this competency do a different job.

### What it does
Check that a shipped change traces to a capture.

### Method
1. List changes claimed to come from co-design.
2. Point each change at a capture row.
3. Mark a change with no capture as not from this research.

### Do not
Do not credit co-design for a change the team already planned.

### Output
A trace from change to capture.

A missing fact stays [GAP].

## DH-02.03.1.2.2 Participant fit

Worker: Patient Experience Designer (`patient-experience-designer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.1.2.2 Participant fit.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.1.2. The other skills under this competency do a different job.

### What it does
Check that the participants matched the question.

### Method
1. Compare recruited roles with the participant type on the question.
2. Note a session that did not include that type.
3. State whether the decision still stands.

### Do not
Do not treat staff standing in for patients as patient co-design.

### Output
A fit note.

A missing fact stays [GAP].

## DH-02.03.1.2.3 Unresolved point

Worker: Patient Experience Designer (`patient-experience-designer`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.1.2.3 Unresolved point.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.1.2. The other skills under this competency do a different job.

### What it does
Assign a repeated point that was not decided.

### Method
1. Name the point and the count.
2. Name the owner.
3. Name the date the accept, defer, or refuse will be written.

### Do not
Do not leave a repeated point only in the transcript.

### Output
An owner and a decision date.

A missing fact stays [GAP].
