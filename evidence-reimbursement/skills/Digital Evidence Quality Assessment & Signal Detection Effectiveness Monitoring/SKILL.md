---
name: digital-evidence-quality-and-signal-detection
description: "Only while the Digital Health Library connector is connected. Start the job Digital Evidence Quality Assessment & Signal Detection Effectiveness Monitoring in Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Digital Evidence Quality Assessment & Signal Detection Effectiveness Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Digital Signal Detection Monitoring. Skill `digital-signal-detection-monitoring`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.2.1 Digital Signal Detection Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- digital evidence pass rule. Skill `digital-evidence-pass-rule`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- digital evidence miss owner. Skill `digital-evidence-miss-owner`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 29 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
