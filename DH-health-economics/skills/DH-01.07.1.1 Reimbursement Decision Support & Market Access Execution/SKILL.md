---
name: "DH-01.07.1.1 Reimbursement Decision Support & Market Access Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.07.1.1 Reimbursement Decision Support & Market Access Execution. Use when the user asks for Access pathway, Access dossier item, Submission readiness. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.07.1.1 Reimbursement Decision Support & Market Access Execution

Heading: DH-01.07.1 Market Access Support.
Core: DH-01.07 Health Economics & Value Demonstration.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.07.1.1.1 Access pathway

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.1.1.1 Access pathway.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Use a pathway the buyer or an earlier matrix already supplied.


## DH-01.07.1.1.2 Access dossier item

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.1.1.2 Access dossier item.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Write one dossier item from evidence already in the conversation.


## DH-01.07.1.1.3 Submission readiness

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.1.1.3 Submission readiness.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

List the items present and the items missing. Do not file a submission.
