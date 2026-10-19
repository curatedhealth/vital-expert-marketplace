---
name: find-scheme-precedents
description: "Use only after the job Coverage Strategy Effectiveness Assessment and Access Rate Monitoring is chosen, to do Find scheme precedents."
---

# Find scheme precedents

## Execution formula
Worker: not bound.
Skill: CF-12.03.01.4.2.4 Find scheme precedents.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.find_scheme_precedents`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for the scheme and the indication. An empty scheme is a gap.
