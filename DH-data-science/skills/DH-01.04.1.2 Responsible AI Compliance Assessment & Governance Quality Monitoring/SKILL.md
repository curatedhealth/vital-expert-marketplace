---
name: "DH-01.04.1.2 Responsible AI Compliance Assessment & Governance Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.04.1.2 Responsible AI Compliance Assessment & Governance Quality Monitoring. Use when the user asks for Governance evidence, Release score, Governance miss. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04.1.2 Responsible AI Compliance Assessment & Governance Quality Monitoring

Heading: DH-01.04.1 Responsible AI.
Core: DH-01.04 Data Science & AI/ML.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.04.1.2.1 Governance evidence

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.1.2.1 Governance evidence.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.1.2. The other skills under this competency do a different job.

### What it does
Define the evidence a responsible-AI release must have.

### Method
1. Name the bias test, the intended use, and the human who can override the model.
2. A missing item is a fail.
3. Name the release you will score.

### Do not
Do not accept a policy statement in place of the test.

### Output
An evidence list.

A missing fact stays [GAP].

## DH-01.04.1.2.2 Release score

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.1.2.2 Release score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.1.2. The other skills under this competency do a different job.

### What it does
Score the release.

### Method
1. Check each item and keep the record id.
2. Mark pass or fail.
3. Note a group that was [GAP] at test time and is still unseen.

### Do not
Do not pass a release with an unseen group presented as tested.

### Output
A score.

A missing fact stays [GAP].

## DH-01.04.1.2.3 Governance miss

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.04.1.2.3 Governance miss.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.04.1.2. The other skills under this competency do a different job.

### What it does
Assign a failed item.

### Method
1. Name the owner.
2. State whether release waits.
3. Name the date the item will be present.

### Do not
Do not ship the model while a failed item is open.

### Output
An owner and whether release waits.

A missing fact stays [GAP].
