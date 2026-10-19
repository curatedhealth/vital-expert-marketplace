---
name: "DH-03.02.4.2 CAPA Effectiveness Assessment & Compliance Operations Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.02.4.2 CAPA Effectiveness Assessment & Compliance Operations Quality Monitoring. Use when the user asks for CAPA effectiveness check, CAPA score, Ineffective CAPA. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.02.4.2 CAPA Effectiveness Assessment & Compliance Operations Quality Monitoring

Heading: DH-03.02.4 Audit, CAPA, and Compliance Ops.
Core: DH-03.02 Quality Management & Compliance.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.02.4.2.1 CAPA effectiveness check

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.4.2.1 CAPA effectiveness check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.4.2. The other skills under this competency do a different job.

### What it does
Define effectiveness as the problem not recurring.

### Method
1. Name the preventive action.
2. Name the window and the record you will read (the same audit clause, or the same complaint code).
3. A pass is no recurrence in the window. A fail is a recurrence, or no check performed.

### Do not
Do not call a CAPA effective because it was closed on time.

### Output
An effectiveness rule.

A missing fact stays [GAP].

## DH-03.02.4.2.2 CAPA score

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.4.2.2 CAPA score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.4.2. The other skills under this competency do a different job.

### What it does
Score open and recently closed CAPA.

### Method
1. List each plan as open, checked and effective, or checked and failed.
2. Keep the finding id.
3. Note a complaint whose reportability decision is missing.

### Do not
Do not score a closed-on-time CAPA as effective without the check.

### Output
A score.

A missing fact stays [GAP].

## DH-03.02.4.2.3 Ineffective CAPA

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.4.2.3 Ineffective CAPA.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.4.2. The other skills under this competency do a different job.

### What it does
Assign a failed effectiveness check.

### Method
1. Name the owner.
2. State the new cause or the same cause.
3. Open a new action. Do not reopen the old one as if the check had not failed.

### Do not
Do not close the finding while the new action is open.

### Output
A new action and an owner.

A missing fact stays [GAP].
