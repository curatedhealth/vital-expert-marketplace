---
name: "DH-05.02.1.3 User Enablement & Training"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.1.3 User Enablement & Training. Use when the user asks for Enablement task, Practice record, Support after the session. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.1.3 User Enablement & Training

Heading: DH-05.02.1 Self-Service BI Enablement.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.1.3.1 Enablement task

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.3.1 Enablement task.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.3. The other skills under this competency do a different job.

### What it does
Name the task the user will do in the tool.

### Method
1. Name the role and the task (answer one decision with the template).
2. Name the template they will use.
3. Name what you will not train.

### Do not
Do not train the whole platform.

### Output
A task and a template.

A missing fact stays [GAP].

## DH-05.02.1.3.2 Practice record

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.3.2 Practice record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.3. The other skills under this competency do a different job.

### What it does
Record who completed the task.

### Method
1. Name the session and the roles.
2. Record who produced an answer from the template.
3. Record who could not, and the step they stopped on.

### Do not
Do not count attendance as enablement.

### Output
A practice record.

A missing fact stays [GAP].

## DH-05.02.1.3.3 Support after the session

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.1.3.3 Support after the session.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.1.3. The other skills under this competency do a different job.

### What it does
Name who answers the next question.

### Method
1. Name the owner for a broken metric.
2. Name the owner for a wrong filter.
3. Name how a user reaches them.

### Do not
Do not end enablement at the session.

### Output
Two owners and a path.

A missing fact stays [GAP].
