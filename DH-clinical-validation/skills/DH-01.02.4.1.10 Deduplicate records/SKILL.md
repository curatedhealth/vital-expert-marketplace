---
name: "DH-01.02.4.1.10 Deduplicate records"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.4.1 is chosen, to do Deduplicate records. Catalogue job evidence-table. Tool literature.deduplicate."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.1.10 Deduplicate records

Worker: not bound.
Skill: CF-12.01.02.4.1.10 Deduplicate records.
Prompt: not bound.
Template: not bound.
Tool: `literature.deduplicate`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Pass records this job already retrieved. Do not start a new search. A record the tool does not collapse stays as its own row.

Catalogue job: `evidence-table`.

