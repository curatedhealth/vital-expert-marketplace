---
name: clinical-study-protocol-design-and-endpoint-selection
description: "Only while the Digital Health Library connector is connected. Start the job Clinical Study Protocol Design & Endpoint Selection in Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Clinical Study Protocol Design & Endpoint Selection

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Study Protocol Drafting. Skill `study-protocol-drafting`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 21 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.1.1.1 Study Protocol Drafting. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Endpoint & COA Selection. Skill `endpoint-and-coa-selection`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 21 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.1.1.2 Endpoint & COA Selection. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Statistical Analysis Plan Development. Skill `statistical-analysis-plan-development`. Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 20 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.1.1.3 Statistical Analysis Plan Development. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
