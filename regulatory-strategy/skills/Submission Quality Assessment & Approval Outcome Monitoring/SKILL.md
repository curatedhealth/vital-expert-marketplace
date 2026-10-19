---
name: submission-quality-assessment-and-approval-outcome-monitoring
description: "Only while the Digital Health Library connector is connected. Start the job Submission Quality Assessment & Approval Outcome Monitoring in Regulatory Strategy & Submissions. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Submission Quality Assessment & Approval Outcome Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Submission Approval Outcome Monitoring. Skill `submission-approval-outcome-monitoring`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 28 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.4.2.1 Submission Approval Outcome Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- submission quality pass rule. Skill `submission-quality-pass-rule`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 26 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- submission quality miss owner. Skill `submission-quality-miss-owner`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 26 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
