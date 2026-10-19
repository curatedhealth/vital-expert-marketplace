---
name: ai-ml-compliance-and-approval-readiness
description: "Only while the Digital Health Library connector is connected. Start the job AI/ML Regulatory Compliance Assessment & Approval Readiness Monitoring in Regulatory Strategy & Submissions. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# AI/ML Regulatory Compliance Assessment & Approval Readiness Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- AI/ML Approval Readiness Monitoring. Skill `ai-ml-approval-readiness-monitoring`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 31 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.1.2.1 AI/ML Approval Readiness Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- AI/ML regulatory readiness pass rule. Skill `ai-ml-regulatory-readiness-pass-rule`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 27 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- AI/ML regulatory readiness miss owner. Skill `ai-ml-regulatory-readiness-miss-owner`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 27 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
