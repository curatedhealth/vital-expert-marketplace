---
name: dh-01-07-3-1-real-world-outcomes-evidence-generation-study-execu
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.07.3.1 Real-World Outcomes Evidence Generation & Study Execution. Use when the user asks for Outcomes question, Study execution record, Outcome result. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.07.3.1 Real-World Outcomes Evidence Generation & Study Execution

Heading: DH-01.07.3 Outcomes Research.
Core: DH-01.07 Health Economics & Value Demonstration.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.07.3.1.1 Outcomes question

Worker: Digital Clinical Trials Director (`digital-clinical-trials-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.3.1.1 Outcomes question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Write the outcomes question in the buyer's words.


## DH-01.07.3.1.2 Study execution record

Worker: Digital Clinical Trials Director (`digital-clinical-trials-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.3.1.2 Study execution record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Record the study steps the buyer supplied.


## DH-01.07.3.1.3 Outcome result

Worker: Digital Clinical Trials Director (`digital-clinical-trials-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.3.1.3 Outcome result.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Report a result only from a study already in the conversation.
