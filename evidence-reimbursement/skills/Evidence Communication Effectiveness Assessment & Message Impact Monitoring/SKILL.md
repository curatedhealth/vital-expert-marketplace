---
name: evidence-communication-and-message-impact
description: "Only while the Digital Health Library connector is connected. Start the job Evidence Communication Effectiveness Assessment & Message Impact Monitoring in Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Evidence Communication Effectiveness Assessment & Message Impact Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Message Impact Monitoring. Skill `message-impact-monitoring`. Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 13 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.2.2.1 Message Impact Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- evidence communication pass rule. Skill `evidence-communication-pass-rule`. Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 13 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- evidence communication miss owner. Skill `evidence-communication-miss-owner`. Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 13 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
