---
name: search-safety-events
description: "Only while the Digital Health Library connector is connected. Use only after the job Regulatory Strategy Effectiveness Assessment & Pathway Success Monitoring is chosen, to do Search safety events."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Search safety events

## Execution formula
Worker: not bound.
Skill: CF-12.03.03.3.2.5 Search safety events.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.search_safety_events`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for the product code, the manufacturer, or the EMDN code. A missing recall or MAUDE row is a gap.
