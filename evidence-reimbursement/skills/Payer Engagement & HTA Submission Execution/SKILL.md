---
name: payer-engagement-and-hta-submission-execution
description: "Only while the Digital Health Library connector is connected. Start the job Payer Engagement & HTA Submission Execution in Market Access & Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Payer Engagement & HTA Submission Execution

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Value Dossier Assembly. Skill `value-dossier-assembly`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.3.1.1 Value Dossier Assembly. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- HTA Submission Preparation. Skill `hta-submission-preparation`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.3.1.2 HTA Submission Preparation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Payer Negotiation. Skill `payer-negotiation`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.3.1.3 Payer Negotiation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
