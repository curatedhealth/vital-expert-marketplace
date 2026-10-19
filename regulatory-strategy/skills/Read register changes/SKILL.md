---
name: read-register-changes
description: "Only while the Digital Health Library connector is connected. Use only after the job Regulatory Strategy Effectiveness Assessment & Pathway Success Monitoring is chosen, to do Read register changes."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Read register changes

## Execution formula
Worker: not bound.
Skill: CF-12.03.03.3.2.6 Read register changes.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.get_register_deltas`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for the same subject as the watch, and a since date. An empty log means no change recorded. `regulatory-dh.get_deltas` is this same tool. Call one of them, not both.
