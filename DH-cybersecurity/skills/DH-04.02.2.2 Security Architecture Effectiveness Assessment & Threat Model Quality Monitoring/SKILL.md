---
name: "DH-04.02.2.2 Security Architecture Effectiveness Assessment & Threat Model Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.02.2.2 Security Architecture Effectiveness Assessment & Threat Model Quality Monitoring. Use when the user asks for Threat coverage check, Residual risk score, Model update trigger. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.02.2.2 Security Architecture Effectiveness Assessment & Threat Model Quality Monitoring

Heading: DH-04.02.2 Security Architecture.
Core: DH-04.02 Cybersecurity & Privacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.02.2.2.1 Threat coverage check

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.2.2.1 Threat coverage check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.2.2. The other skills under this competency do a different job.

### What it does
Check that every recorded threat has a mitigation or an acceptance.

### Method
1. Read the threat register.
2. Mark each threat covered, accepted, or open.
3. Count open threats by hop.

### Do not
Do not treat a tool scan as a threat model.

### Output
A coverage count and the open threats.

A missing fact stays [GAP].

## DH-04.02.2.2.2 Residual risk score

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.2.2.2 Residual risk score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.2.2. The other skills under this competency do a different job.

### What it does
Score what remains after the mitigations.

### Method
1. For each covered threat, state what the control does not stop.
2. Rate the remainder high only when the asset is identifiable patient data or a therapy-controlling function.
3. Say when the score was made and against which design version.

### Do not
Do not score residual risk before the threat list exists.

### Output
A residual-risk note per high remainder.

A missing fact stays [GAP].

## DH-04.02.2.2.3 Model update trigger

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.2.2.3 Model update trigger.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.2.2. The other skills under this competency do a different job.

### What it does
State what change forces the model to be redrawn.

### Method
1. Name the changes that count (new third party, new write-back, new device).
2. Name who watches for those changes.
3. Record the last design version the model matches.

### Do not
Do not leave the model undated.

### Output
A trigger list and the design version.

A missing fact stays [GAP].
