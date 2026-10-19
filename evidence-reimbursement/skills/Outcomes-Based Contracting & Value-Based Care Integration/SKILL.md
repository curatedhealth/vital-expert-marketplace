---
name: outcomes-based-contracting-and-value-based-care-integration
description: "Only while the Digital Health Library connector is connected. Start the job Outcomes-Based Contracting & Value-Based Care Integration in Market Access & Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Outcomes-Based Contracting & Value-Based Care Integration

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Outcomes Metric Definition. Skill `outcomes-metric-definition`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.1.1.1 Outcomes Metric Definition. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Risk-Sharing Model Design. Skill `risk-sharing-model-design`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.1.1.2 Risk-Sharing Model Design. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Outcomes Contract Structuring. Skill `outcomes-contract-structuring`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.1.1.3 Outcomes Contract Structuring. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
