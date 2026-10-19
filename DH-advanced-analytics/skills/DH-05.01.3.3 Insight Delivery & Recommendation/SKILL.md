---
name: "DH-05.01.3.3 Insight Delivery & Recommendation"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.01.3.3 Insight Delivery & Recommendation. Use when the user asks for Recommendation statement, Delivery to the owner, Unresolved question. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.01.3.3 Insight Delivery & Recommendation

Heading: DH-05.01.3 Advanced Analytics Consulting.
Core: DH-05.01 Advanced Analytics & Data Science.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.01.3.3.1 Recommendation statement

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.3.3.1 Recommendation statement.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.3.3. The other skills under this competency do a different job.

### What it does
Write the recommendation in the decision maker's choice.

### Method
1. State the recommended action and the alternative.
2. State the evidence that supports it, with the source.
3. State the condition that would change the recommendation.

### Do not
Do not write a recommendation that restates the data without an action.

### Output
An action, evidence, and a change condition.

A missing fact stays [GAP].

## DH-05.01.3.3.2 Delivery to the owner

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.3.3.2 Delivery to the owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.3.3. The other skills under this competency do a different job.

### What it does
Deliver it to the person who decides.

### Method
1. Name the person and the date.
2. Record the question they asked that you could not answer.
3. Record the action they chose, if they chose in the meeting.

### Do not
Do not file the recommendation only in a slide folder.

### Output
A delivery record.

A missing fact stays [GAP].

## DH-05.01.3.3.3 Unresolved question

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.3.3.3 Unresolved question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.3.3. The other skills under this competency do a different job.

### What it does
Park a question that blocked the action.

### Method
1. Name the question and the missing data.
2. Name the owner of the data.
3. Name whether the action waits.

### Do not
Do not recommend an action that depends on data marked [GAP].

### Output
A parked question and whether the action waits.

A missing fact stays [GAP].
