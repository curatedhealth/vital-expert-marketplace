---
name: "DH-02.01.1.2.5 Read commercial changes"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.1.2 is chosen, to do Read commercial changes. Catalogue job product-watch. Tool commercial-dh.get_deltas."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.1.2.5 Read commercial changes

Worker: not bound.
Skill: CF-12.02.01.1.2.5 Read commercial changes.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.get_deltas`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Read what changed since the watch. Copy only what, event_date, observed_at, and source_url. Do not invent a change.

Catalogue job: `product-watch`.

