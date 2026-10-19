---
name: regulatory-strategy-effectiveness-and-pathway-monitoring
description: "Only while the Digital Health Library connector is connected. Start the job Regulatory Strategy Effectiveness Assessment & Pathway Success Monitoring in Regulatory Strategy & Submissions. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Regulatory Strategy Effectiveness Assessment & Pathway Success Monitoring

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Regulatory Pathway Success Monitoring. Skill `regulatory-pathway-success-monitoring`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.3.2.1 Regulatory Pathway Success Monitoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- regulatory pathway pass rule. Skill `regulatory-pathway-pass-rule`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- regulatory pathway miss owner. Skill `regulatory-pathway-miss-owner`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Watch a register. Skill `watch-a-register`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.watch_register`.
- Search safety events. Skill `search-safety-events`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.search_safety_events`.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
