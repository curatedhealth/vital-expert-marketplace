---
name: "Evidence Translation & Stakeholder Communication Delivery"
description: "Only while the Digital Health Library connector is connected. Start the job Evidence Translation & Stakeholder Communication Delivery in Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Evidence Translation & Stakeholder Communication Delivery

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Regulatory Evidence Dossier Authoring. Skill `regulatory-evidence-dossier-authoring`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 25 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.2.1.1 Regulatory Evidence Dossier Authoring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Payer Value Narrative. Skill `payer-value-narrative`. Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 19 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.2.1.2 Payer Value Narrative. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Clinical Publication Development. Skill `clinical-publication-development`. Worker: Cybersecurity Architect, Digital Health (`cybersecurity-architect-digital-health`). 19 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.2.1.3 Clinical Publication Development. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
