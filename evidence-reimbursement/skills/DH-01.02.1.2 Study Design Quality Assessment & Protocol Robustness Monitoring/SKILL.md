---
name: "DH-01.02.1.2 Study Design Quality Assessment & Protocol Robustness Monitoring"
description: "Only while the Digital Health Library connector is connected. Start the job DH-01.02.1.2 Study Design Quality Assessment & Protocol Robustness Monitoring in DH-01.02 Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.1.2 Study Design Quality Assessment & Protocol Robustness Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- DH-01.02.1.2.1 Protocol Robustness Monitoring. Skill `protocol-robustness-monitoring`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 17 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.1.2.1 DH-01.02.1.2.1 Protocol Robustness Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- DH-01.02.1.2.2 protocol robustness pass rule. Skill `protocol-robustness-pass-rule`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 17 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- DH-01.02.1.2.3 protocol robustness miss owner. Skill `protocol-robustness-miss-owner`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 17 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
