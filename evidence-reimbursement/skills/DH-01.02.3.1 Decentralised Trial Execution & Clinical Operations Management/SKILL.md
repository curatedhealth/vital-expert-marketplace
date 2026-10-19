---
name: "DH-01.02.3.1 Decentralised Trial Execution & Clinical Operations Management"
description: "Only while the Digital Health Library connector is connected. Start the job DH-01.02.3.1 Decentralised Trial Execution & Clinical Operations Management in DH-01.02 Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.3.1 Decentralised Trial Execution & Clinical Operations Management

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- DH-01.02.3.1.1 Decentralised Trial Setup. Skill `decentralised-trial-setup`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 11 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.3.1.1 DH-01.02.3.1.1 Decentralised Trial Setup. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- DH-01.02.3.1.2 Remote Data Capture Operations. Skill `remote-data-capture-operations`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 22 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.3.1.2 DH-01.02.3.1.2 Remote Data Capture Operations. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- DH-01.02.3.1.3 Trial Data Integrity Management. Skill `trial-data-integrity-management`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 23 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.3.1.3 DH-01.02.3.1.3 Trial Data Integrity Management. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
