---
name: dh-02-01-1-2-commercial-execution-effectiveness-assessment-launc
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.01.1.2 Commercial Execution Effectiveness Assessment & Launch Performance Monitoring. Use when the user asks for Launch measure definition, Launch week score, Launch miss owner, Watch a product, Read commercial changes. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.1.2 Commercial Execution Effectiveness Assessment & Launch Performance Monitoring

Heading: DH-02.01.1 Commercial Execution.
Core: DH-02.01 Commercial & GTM Strategy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.01.1.2.1 Launch measure definition

Worker: Digital Adoption Lead (`digital-adoption-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.1.2.1 Launch measure definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.1.2. The other skills under this competency do a different job.

### What it does
Define what a successful launch week looks like.

### Method
1. Name the counts that matter (accounts reached, claims used, meetings held).
2. Set a threshold for each count and the week it applies to.
3. Exclude vanity counts that no one will act on.

### Do not
Do not use revenue as the only launch-week measure when the contract cycle is longer.

### Output
A measure sheet with a threshold per count.

A missing fact stays [GAP].

## DH-02.01.1.2.2 Launch week score

Worker: Digital Adoption Lead (`digital-adoption-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.1.2.2 Launch week score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.1.2. The other skills under this competency do a different job.

### What it does
Score the launch week against that sheet.

### Method
1. Pull the counts for the named week from the system of record.
2. Mark each measure met or missed and keep the source row.
3. Separate a missed briefing from a missed customer meeting.

### Do not
Do not fill a missing count with an estimate.

### Output
A score for the week, with source rows.

A missing fact stays [GAP].

## DH-02.01.1.2.3 Launch miss owner

Worker: Digital Adoption Lead (`digital-adoption-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.1.2.3 Launch miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.1.2. The other skills under this competency do a different job.

### What it does
Assign each miss.

### Method
1. Name the owner of each missed measure.
2. State whether the next step is a briefing, a claim fix, or a stopped claim.
3. Leave an owner blank only when the role does not exist, and say so.

### Do not
Do not close a miss because the week ended.

### Output
An owner and a next step per miss.

A missing fact stays [GAP].

## DH-02.01.1.2.4 Watch a product

Worker: not bound.
Skill: CF-12.02.01.1.2.4 Watch a product.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.watch_product`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Register the watch and return the snapshot hashes. One watch per tenant. Deltas are a later call.

Catalogue job: `product-watch`.

## DH-02.01.1.2.5 Read commercial changes

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
