---
name: "Digital Health Economic Model Development & Cost-Effectiveness Analysis"
description: "Only while the Digital Health Library connector is connected. Start the job Digital Health Economic Model Development & Cost-Effectiveness Analysis in Health Economics & Value Demonstration. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Digital Health Economic Model Development & Cost-Effectiveness Analysis

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Economic question. Skill `economic-question`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Model inputs. Skill `model-inputs`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Model result. Skill `model-result`. Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one. Prompt: not bound. Template: not bound. Tool: not bound.
- Run a budget impact model. Skill `run-a-budget-impact-model`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `analytics.budget-impact-model`.
- Run a launch price anchor. Skill `run-a-launch-price-anchor`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `analytics.vba-price-anchor`.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
