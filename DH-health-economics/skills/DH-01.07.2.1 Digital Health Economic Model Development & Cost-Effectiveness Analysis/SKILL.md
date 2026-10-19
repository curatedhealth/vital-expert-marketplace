---
name: "DH-01.07.2.1 Digital Health Economic Model Development & Cost-Effectiveness Analysis"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.07.2.1 Digital Health Economic Model Development & Cost-Effectiveness Analysis. Use when the user asks for Economic question, Model inputs, Model result, Run a budget impact model, Run a launch price anchor. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.07.2.1 Digital Health Economic Model Development & Cost-Effectiveness Analysis

Heading: DH-01.07.2 Economic Modeling.
Core: DH-01.07 Health Economics & Value Demonstration.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.07.2.1.1 Economic question

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.2.1.1 Economic question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Write the decision the model has to answer, in the buyer's words.


## DH-01.07.2.1.2 Model inputs

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.2.1.2 Model inputs.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

List every input. Leave a blank input blank.


## DH-01.07.2.1.3 Model result

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.07.2.1.3 Model result.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Report a result only from inputs already shown.


## DH-01.07.2.1.4 Run a budget impact model

Worker: not bound.
Skill: CF-12.01.07.2.1.4 Run a budget impact model.
Prompt: not bound.
Template: not bound.
Tool: `analytics.budget-impact-model`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Collect the population, the current mix, the new-treatment cost, and the uptake curve from the buyer. Show every input beside the net impact.


## DH-01.07.2.1.5 Run a launch price anchor

Worker: not bound.
Skill: CF-12.01.07.2.1.5 Run a launch price anchor.
Prompt: not bound.
Template: not bound.
Tool: `analytics.vba-price-anchor`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Collect the comparator cost, the incremental QALYs, and the willingness-to-pay thresholds from the buyer. The result is a ceiling, not a launched price.
