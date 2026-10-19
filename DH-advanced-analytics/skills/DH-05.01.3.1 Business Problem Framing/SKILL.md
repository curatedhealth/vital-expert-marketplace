---
name: "DH-05.01.3.1 Business Problem Framing"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.01.3.1 Business Problem Framing. Use when the user asks for Decision frame, Question list, Frame review. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.01.3.1 Business Problem Framing

Heading: DH-05.01.3 Advanced Analytics Consulting.
Core: DH-05.01 Advanced Analytics & Data Science.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.01.3.1.1 Decision frame

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.3.1.1 Decision frame.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.3.1. The other skills under this competency do a different job.

### What it does
Frame the business problem as a decision.

### Method
1. Name the decision maker and the choice they have.
2. Name what they will do differently if the analysis says yes or no.
3. Name the analysis you will not do because it does not change the choice.

### Do not
Do not start with a dataset.

### Output
A decision, two actions, and a refusal.

A missing fact stays [GAP].

## DH-05.01.3.1.2 Question list

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.3.1.2 Question list.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.3.1. The other skills under this competency do a different job.

### What it does
Write the questions that decide the choice.

### Method
1. Write the few questions whose answers change the action.
2. Name the data that can answer each one, or mark [GAP].
3. Order them so a gap early stops later work.

### Do not
Do not add a question that does not change the action.

### Output
An ordered question list.

A missing fact stays [GAP].

## DH-05.01.3.1.3 Frame review

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.01.3.1.3 Frame review.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.01.3.1. The other skills under this competency do a different job.

### What it does
Confirm the frame with the decision maker.

### Method
1. Show them the choice and the two actions.
2. Record what they changed.
3. Stop if they cannot name an action.

### Do not
Do not proceed on an unconfirmed frame.

### Output
A confirmed frame or a stop.

A missing fact stays [GAP].
