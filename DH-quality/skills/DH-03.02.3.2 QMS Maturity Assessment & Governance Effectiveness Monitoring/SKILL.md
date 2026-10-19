---
name: "DH-03.02.3.2 QMS Maturity Assessment & Governance Effectiveness Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.02.3.2 QMS Maturity Assessment & Governance Effectiveness Monitoring. Use when the user asks for QMS maturity check, QMS score, QMS repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.02.3.2 QMS Maturity Assessment & Governance Effectiveness Monitoring

Heading: DH-03.02.3 QMS Strategy & Governance.
Core: DH-03.02 Quality Management & Compliance.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.02.3.2.1 QMS maturity check

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.3.2.1 QMS maturity check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.3.2. The other skills under this competency do a different job.

### What it does
Define the maturity you are claiming.

### Method
1. Name the processes in scope.
2. A pass for a process is an owner, a record from the last period, and a review of that record.
3. Name the period.

### Do not
Do not claim maturity from a handbook.

### Output
A maturity rule.

A missing fact stays [GAP].

## DH-03.02.3.2.2 QMS score

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.3.2.2 QMS score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.3.2. The other skills under this competency do a different job.

### What it does
Score each in-scope process.

### Method
1. Mark owner present, record present, review present.
2. A process missing any one fails.
3. Name the failed process.

### Do not
Do not average the processes into a single green score.

### Output
A score per process.

A missing fact stays [GAP].

## DH-03.02.3.2.3 QMS repair

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.3.2.3 QMS repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.3.2. The other skills under this competency do a different job.

### What it does
Assign a failed process.

### Method
1. Name the owner.
2. State the record or the review that is missing.
3. Name the next governance date that must see it.

### Do not
Do not raise the maturity claim while the process fails.

### Output
An owner and the next governance date.

A missing fact stays [GAP].
