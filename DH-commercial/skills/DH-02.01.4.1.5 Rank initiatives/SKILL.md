---
name: "DH-02.01.4.1.5 Rank initiatives"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.4.1 is chosen, to do Rank initiatives. Catalogue job partner-prioritization. Tool analytics.rice."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.4.1.5 Rank initiatives

Worker: not bound.
Skill: CF-12.02.01.4.1.5 Rank initiatives.
Prompt: not bound.
Template: not bound.
Tool: `analytics.rice`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

The buyer supplies id, reach, impact, confidence, and effort. Impact is 0.25, 0.5, 1, 2, or 3. The rank does not invent a number.

Catalogue job: `partner-prioritization`.

