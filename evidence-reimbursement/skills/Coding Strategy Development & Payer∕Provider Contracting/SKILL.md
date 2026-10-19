---
name: coding-strategy-development-and-payer-provider-contracting
description: "Start the job Coding Strategy Development & Payer/Provider Contracting in Market Access & Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Coding Strategy Development & Payer/Provider Contracting

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Coding Pathway Strategy. Skill `coding-pathway-strategy`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.2.1.1 Coding Pathway Strategy. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Pricing Strategy. Skill `pricing-strategy`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.2.1.2 Pricing Strategy. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Contract Negotiation. Skill `contract-negotiation`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 4 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.2.1.3 Contract Negotiation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
