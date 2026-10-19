---
name: build-an-evidence-table
description: "Use only after the job Digital Endpoint Capture and RWE Platform Management is chosen, to do Build an evidence table."
---

# Build an evidence table

## Execution formula
Worker: not bound.
Skill: CF-12.01.02.4.1.9 Build an evidence table.
Prompt: not bound.
Template: not bound.
Tool: `literature.build_evidence_table`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Build the table from the graded records already opened.
