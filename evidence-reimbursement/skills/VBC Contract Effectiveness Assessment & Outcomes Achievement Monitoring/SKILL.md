---
name: vbc-contract-effectiveness-and-outcomes
description: "Only while the Digital Health Library connector is connected. Start the job VBC Contract Effectiveness Assessment & Outcomes Achievement Monitoring in Market Access & Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# VBC Contract Effectiveness Assessment & Outcomes Achievement Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Outcomes Achievement Monitoring. Skill `outcomes-achievement-monitoring`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.1.2.1 Outcomes Achievement Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- value-based contract pass rule. Skill `value-based-contract-pass-rule`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- value-based contract miss owner. Skill `value-based-contract-miss-owner`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
