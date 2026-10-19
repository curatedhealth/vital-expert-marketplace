---
name: cf-12-01-02-3-1
description: "Start the job Decentralised Trial Execution and Clinical Operations Management (CF-12.01.02.3.1) in Clinical Validation and Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Decentralised Trial Execution and Clinical Operations Management

Code: CF-12.01.02.3.1. Mission: CF-12.01.02.3.

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Decentralised Trial Setup. Skill `cf-12-01-02-3-1-1`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 11 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.3.1.1 Decentralised Trial Setup. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Remote Data Capture Operations. Skill `cf-12-01-02-3-1-2`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 22 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.3.1.2 Remote Data Capture Operations. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Trial Data Integrity Management. Skill `cf-12-01-02-3-1-3`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 23 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.3.1.3 Trial Data Integrity Management. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
