---
name: harmonisation-effectiveness-and-compliance-monitoring
description: "Only while the Digital Health Library connector is connected. Start the job Harmonisation Effectiveness Assessment & Cross-Region Compliance Monitoring in Regulatory Strategy & Submissions. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Harmonisation Effectiveness Assessment & Cross-Region Compliance Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Cross-Region Compliance Monitoring. Skill `cross-region-compliance-monitoring`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 31 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.2.2.1 Cross-Region Compliance Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- cross-region compliance pass rule. Skill `cross-region-compliance-pass-rule`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 27 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- cross-region compliance miss owner. Skill `cross-region-compliance-miss-owner`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 27 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
