---
name: "Trial Operations Effectiveness Assessment & Execution Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Start the job Trial Operations Effectiveness Assessment & Execution Quality Monitoring in Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Trial Operations Effectiveness Assessment & Execution Quality Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Trial Execution Quality Monitoring. Skill `trial-execution-quality-monitoring`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.3.2.1 Trial Execution Quality Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- trial operations pass rule. Skill `trial-operations-pass-rule`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- trial operations miss owner. Skill `trial-operations-miss-owner`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
