---
name: run-a-budget-impact-model
description: "Use only after the job Digital Health Economic Model Development and Cost-Effectiveness Analysis is chosen, to do Run a budget impact model."
---

# Run a budget impact model

## Execution formula
Worker: not bound.
Skill: CF-12.01.07.2.1.4 Run a budget impact model.
Prompt: not bound.
Template: not bound.
Tool: `analytics.budget-impact-model`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Collect the population, the current mix, the new-treatment cost, and the uptake curve from the buyer. Show every input beside the net impact.
