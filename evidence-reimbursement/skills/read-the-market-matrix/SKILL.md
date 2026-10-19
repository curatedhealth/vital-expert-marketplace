---
name: read-the-market-matrix
description: "Use only after the job Coverage Pathway Design and Benefit Access Strategy Execution is chosen, to do Read the market matrix."
---

# Read the market matrix

## Execution formula
Worker: not bound.
Skill: CF-12.03.01.4.1.4 Read the market matrix.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.get_market_matrix`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for the category. An empty scheme is a gap. Europe is partial where the connector says the scheme is not loaded.
