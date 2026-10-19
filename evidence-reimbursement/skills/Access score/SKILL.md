---
name: "Access score"
description: "Only while the Digital Health Library connector is connected. Use only after the job Market Access Effectiveness Assessment & Reimbursement Outcome Monitoring is chosen, to do Access score."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Access score

## Execution formula
Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.1.2.2 Access score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Score only with the formula and the inputs the buyer supplied.
