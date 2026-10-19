---
name: run-a-launch-price-anchor
description: "Only while the Digital Health Library connector is connected. Use only after the job Digital Health Economic Model Development & Cost-Effectiveness Analysis is chosen, to do Run a launch price anchor."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Run a launch price anchor

## Execution formula
Worker: not bound.
Skill: CF-12.01.07.2.1.5 Run a launch price anchor.
Prompt: not bound.
Template: not bound.
Tool: `analytics.vba-price-anchor`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Collect the comparator cost, the incremental QALYs, and the willingness-to-pay thresholds from the buyer. The result is a ceiling, not a launched price.
