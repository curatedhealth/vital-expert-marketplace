---
name: cf-12-01-07-1-1-2
description: "Use only after the job Reimbursement Decision Support and Market Access Execution (CF-12.01.07.1.1) is chosen, to do Access dossier item."
---

# Access dossier item

Code: CF-12.01.07.1.1.2.

## Execution formula
Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.1.1.2 Access dossier item.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Write one dossier item from evidence already in the conversation.
