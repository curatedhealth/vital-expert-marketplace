---
name: dh-03-02-4-1-audit-execution-capa-complaint-handling-management
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.02.4.1 Audit Execution & CAPA Complaint Handling Management. Use when the user asks for Audit finding, CAPA plan, Complaint record. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.02.4.1 Audit Execution & CAPA Complaint Handling Management

Heading: DH-03.02.4 Audit, CAPA, and Compliance Ops.
Core: DH-03.02 Quality Management & Compliance.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.02.4.1.1 Audit finding

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.4.1.1 Audit finding.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.4.1. The other skills under this competency do a different job.

### What it does
Record one finding.

### Method
1. Name the clause or the procedure, the evidence, and the date.
2. Name the owner.
3. Classify major or minor by the rule you write down, not by preference.

### Do not
Do not close an audit with unrecorded findings.

### Output
A finding: clause, evidence, owner, class.

A missing fact stays [GAP].

## DH-03.02.4.1.2 CAPA plan

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.4.1.2 CAPA plan.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.4.1. The other skills under this competency do a different job.

### What it does
Write the correction and the action that prevents repeat.

### Method
1. Name the correction (fix this instance).
2. Name the cause.
3. Name the preventive action and how you will know it worked.

### Do not
Do not write a CAPA that is only 'retrain the person' unless the cause is that the person was not trained.

### Output
A correction, a cause, and a preventive action.

A missing fact stays [GAP].

## DH-03.02.4.1.3 Complaint record

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.4.1.3 Complaint record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.4.1. The other skills under this competency do a different job.

### What it does
Record a complaint separately from an audit finding.

### Method
1. Name the product, the version, the event, and the date received.
2. State whether it is a reportable event under the rule you name, or not, and why.
3. Name the owner of the investigation.

### Do not
Do not decide reportability after the deadline without recording that the deadline was missed.

### Output
A complaint and a reportability decision.

A missing fact stays [GAP].
