---
name: "DH-01.07.2.2 Economic Model Validity Assessment & Cost-Effectiveness Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.07.2.2 Economic Model Validity Assessment & Cost-Effectiveness Monitoring. Use when the user asks for Model validity check, Model score, Model repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.07.2.2 Economic Model Validity Assessment & Cost-Effectiveness Monitoring

Heading: DH-01.07.2 Economic Modeling.
Core: DH-01.07 Health Economics & Value Demonstration.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.07.2.2.1 Model validity check

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.2.2.1 Model validity check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Check the inputs already shown. Do not replace a buyer input.


## DH-01.07.2.2.2 Model score

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.2.2.2 Model score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Score only with the rule the buyer supplied.


## DH-01.07.2.2.3 Model repair

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.2.2.3 Model repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Name the input the buyer said is wrong.
