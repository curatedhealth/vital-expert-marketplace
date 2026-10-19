---
name: cf-12-03-01-3-2
description: "Start the job HTA Submission Quality Assessment and Payer Engagement Effectiveness Monitoring (CF-12.03.01.3.2) in Market Access and Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# HTA Submission Quality Assessment and Payer Engagement Effectiveness Monitoring

Code: CF-12.03.01.3.2. Mission: CF-12.03.01.3.

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Payer Engagement Effectiveness Monitoring. Skill `cf-12-03-01-3-2-1`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.3.2.1 Payer Engagement Effectiveness Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- HTA submission pass rule. Skill `cf-12-03-01-3-2-2`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- HTA submission miss owner. Skill `cf-12-03-01-3-2-3`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
