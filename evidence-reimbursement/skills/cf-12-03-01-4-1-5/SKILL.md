---
name: cf-12-03-01-4-1-5
description: "Use only after the job Coverage Pathway Design and Benefit Access Strategy Execution (CF-12.03.01.4.1) is chosen, to do Read status history."
---

# Read status history

Code: CF-12.03.01.4.1.5.

## Execution formula
Worker: not bound.
Skill: CF-12.03.01.4.1.5 Read status history.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.get_status_history`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for the scheme. An empty history is a gap.
