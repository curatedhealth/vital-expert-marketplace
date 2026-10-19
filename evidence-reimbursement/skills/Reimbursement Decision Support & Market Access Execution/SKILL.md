---
name: reimbursement-decision-support-and-market-access-execution
description: "Only while the Digital Health Library connector is connected. Start the job Reimbursement Decision Support & Market Access Execution in Health Economics & Value Demonstration. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Reimbursement Decision Support & Market Access Execution

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Access pathway. Skill `access-pathway`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Access dossier item. Skill `access-dossier-item`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Submission readiness. Skill `submission-readiness`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
