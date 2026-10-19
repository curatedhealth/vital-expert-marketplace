---
name: cf-12-03-01-3-1
description: "Start the job Payer Engagement and HTA Submission Execution (CF-12.03.01.3.1) in Market Access and Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Payer Engagement and HTA Submission Execution

Code: CF-12.03.01.3.1. Mission: CF-12.03.01.3.

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Value Dossier Assembly. Skill `cf-12-03-01-3-1-1`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.3.1.1 Value Dossier Assembly. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- HTA Submission Preparation. Skill `cf-12-03-01-3-1-2`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.3.1.2 HTA Submission Preparation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Payer Negotiation. Skill `cf-12-03-01-3-1-3`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.3.1.3 Payer Negotiation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
