---
name: cf-12-03-01-4-1
description: "Start the job Coverage Pathway Design and Benefit Access Strategy Execution (CF-12.03.01.4.1) in Market Access and Reimbursement. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Coverage Pathway Design and Benefit Access Strategy Execution

Code: CF-12.03.01.4.1. Mission: CF-12.03.01.4.

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Coverage Pathway Mapping. Skill `cf-12-03-01-4-1-1`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 6 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.4.1.1 Coverage Pathway Mapping. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Access Strategy Design. Skill `cf-12-03-01-4-1-2`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.4.1.2 Access Strategy Design. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Benefit Design. Skill `cf-12-03-01-4-1-3`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 6 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.01.4.1.3 Benefit Design. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Read the market matrix. Skill `cf-12-03-01-4-1-4`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `market-access-dh.get_market_matrix`.
- Read status history. Skill `cf-12-03-01-4-1-5`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `market-access-dh.get_status_history`.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
