---
name: cf-12-01-02-3-2
description: "Start the job Trial Operations Effectiveness Assessment and Execution Quality Monitoring (CF-12.01.02.3.2) in Clinical Validation and Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Trial Operations Effectiveness Assessment and Execution Quality Monitoring

Code: CF-12.01.02.3.2. Mission: CF-12.01.02.3.

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Trial Execution Quality Monitoring. Skill `cf-12-01-02-3-2-1`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.3.2.1 Trial Execution Quality Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Trial operations pass rule. Skill `cf-12-01-02-3-2-2`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Trial operations miss owner. Skill `cf-12-01-02-3-2-3`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 14 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
