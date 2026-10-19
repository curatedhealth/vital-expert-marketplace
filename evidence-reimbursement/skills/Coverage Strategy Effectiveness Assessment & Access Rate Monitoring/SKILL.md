---
name: coverage-strategy-and-access-monitoring
description: "Start the job Coverage Strategy Effectiveness Assessment & Access Rate Monitoring in Market Access & Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Coverage Strategy Effectiveness Assessment & Access Rate Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Access Rate Monitoring. Skill `access-rate-monitoring`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.4.2.1 Access Rate Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- coverage strategy pass rule. Skill `coverage-strategy-pass-rule`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- coverage strategy miss owner. Skill `coverage-strategy-miss-owner`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Find scheme precedents. Skill `find-scheme-precedents`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `market-access-dh.find_scheme_precedents`.
- Watch a scheme. Skill `watch-a-scheme`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `market-access-dh.watch_scheme`.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
