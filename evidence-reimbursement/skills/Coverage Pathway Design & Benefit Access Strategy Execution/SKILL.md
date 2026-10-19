---
name: coverage-pathway-design-and-benefit-access-strategy-execution
description: "Start the job Coverage Pathway Design & Benefit Access Strategy Execution in Market Access & Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Coverage Pathway Design & Benefit Access Strategy Execution

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Coverage Pathway Mapping. Skill `coverage-pathway-mapping`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 6 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.4.1.1 Coverage Pathway Mapping. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Access Strategy Design. Skill `access-strategy-design`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.4.1.2 Access Strategy Design. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Benefit Design. Skill `benefit-design`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 6 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.4.1.3 Benefit Design. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Read the market matrix. Skill `read-the-market-matrix`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `market-access-dh.get_market_matrix`.
- Read status history. Skill `read-status-history`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `market-access-dh.get_status_history`.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
