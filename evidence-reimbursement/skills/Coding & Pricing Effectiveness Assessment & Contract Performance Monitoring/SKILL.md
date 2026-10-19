---
name: coding-and-pricing-effectiveness
description: "Only while the Digital Health Library connector is connected. Start the job Coding & Pricing Effectiveness Assessment & Contract Performance Monitoring in Market Access & Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Coding & Pricing Effectiveness Assessment & Contract Performance Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Contract Performance Monitoring. Skill `contract-performance-monitoring`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.2.2.1 Contract Performance Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- coding and pricing pass rule. Skill `coding-and-pricing-pass-rule`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- coding and pricing miss owner. Skill `coding-and-pricing-miss-owner`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
