---
name: ai-ml-device-pathway-and-submission
description: "Only while the Digital Health Library connector is connected. Start the job AI/ML Device Regulatory Pathway Navigation & Submission Execution in Regulatory Strategy & Submissions. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# AI/ML Device Regulatory Pathway Navigation & Submission Execution

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- AI/ML Pathway Selection. Skill `ai-ml-pathway-selection`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 18 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.1.1.1 AI/ML Pathway Selection. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Predetermined Change Control Plan Authoring. Skill `predetermined-change-control-plan-authoring`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 14 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.1.1.2 Predetermined Change Control Plan Authoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- AI/ML Submission Assembly. Skill `ai-ml-submission-assembly`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 18 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.1.1.3 AI/ML Submission Assembly. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
