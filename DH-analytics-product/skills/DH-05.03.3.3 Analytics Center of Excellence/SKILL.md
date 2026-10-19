---
name: "DH-05.03.3.3 Analytics Center of Excellence"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.03.3.3 Analytics Center of Excellence. Use when the user asks for CoE charter, CoE decision log, CoE dispute. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.03.3.3 Analytics Center of Excellence

Heading: DH-05.03.3 Analytics Governance & Enablement.
Core: DH-05.03 Analytics Product Management & Enablement.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.03.3.3.1 CoE charter

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.3.1 CoE charter.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.3. The other skills under this competency do a different job.

### What it does
Write what the analytics center of excellence decides.

### Method
1. Name the decisions it owns (certification, priority, standards).
2. Name the decisions it does not own (a product team's roadmap).
3. Name the seats.

### Do not
Do not make the CoE the owner of every dashboard.

### Output
A charter.

A missing fact stays [GAP].

## DH-05.03.3.3.2 CoE decision log

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.3.2 CoE decision log.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.3. The other skills under this competency do a different job.

### What it does
Log a decision the charter allows.

### Method
1. Name the decision, the date, and the seats present.
2. Name the standard or the metric it affects.
3. Name who must carry it out.

### Do not
Do not log a decision outside the charter as a CoE decision.

### Output
A log entry.

A missing fact stays [GAP].

## DH-05.03.3.3.3 CoE dispute

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.3.3 CoE dispute.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.3. The other skills under this competency do a different job.

### What it does
Record a dispute between the CoE and a product team.

### Method
1. Name the dispute (a metric definition, a priority).
2. Name which charter line applies.
3. Name who resolves it if the charter does not.

### Do not
Do not resolve a dispute by silence.

### Output
A dispute and a resolver.

A missing fact stays [GAP].
