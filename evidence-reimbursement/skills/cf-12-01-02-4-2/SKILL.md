---
name: cf-12-01-02-4-2
description: "Start the job Digital Evidence Quality Assessment and Signal Detection Effectiveness Monitoring (CF-12.01.02.4.2) in Clinical Validation and Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Digital Evidence Quality Assessment and Signal Detection Effectiveness Monitoring

Code: CF-12.01.02.4.2. Mission: CF-12.01.02.4.

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Digital Signal Detection Monitoring. Skill `cf-12-01-02-4-2-1`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.2.1 Digital Signal Detection Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Digital evidence pass rule. Skill `cf-12-01-02-4-2-2`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Digital evidence miss owner. Skill `cf-12-01-02-4-2-3`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
