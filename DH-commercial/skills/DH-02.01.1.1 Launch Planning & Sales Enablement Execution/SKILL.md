---
name: "DH-02.01.1.1 Launch Planning & Sales Enablement Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.01.1.1 Launch Planning & Sales Enablement Execution. Use when the user asks for Launch claim list, Sales leave-behind, Enablement roster, Read the launch sequence, Read launch readiness, Commercial brief. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.1.1 Launch Planning & Sales Enablement Execution

Heading: DH-02.01.1 Commercial Execution.
Core: DH-02.01 Commercial & GTM Strategy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.01.1.1.1 Launch claim list

Worker: Digital Adoption Lead (`digital-adoption-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.1.1.1 Launch claim list.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.1.1. The other skills under this competency do a different job.

### What it does
List the claims this launch is allowed to make, each tied to evidence.

### Method
1. Name the product, the country, and the audience for this launch.
2. Write each claim and the source that supports it (study, label, or contract).
3. Leave off any claim that has no source.

### Do not
Do not carry a claim forward from a previous product.

### Output
A claim list with a source on every row.

A missing fact stays [GAP].

## DH-02.01.1.1.2 Sales leave-behind

Worker: Digital Adoption Lead (`digital-adoption-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.1.1.2 Sales leave-behind.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.1.1. The other skills under this competency do a different job.

### What it does
Produce the one artifact the sales team will leave behind.

### Method
1. Choose one format (one-pager or short deck) and the audience role.
2. Place only claims from the claim list onto it.
3. Mark any required section that has no approved claim as [GAP].

### Do not
Do not add a new claim while writing the leave-behind.

### Output
One leave-behind and the claim ids it uses.

A missing fact stays [GAP].

## DH-02.01.1.1.3 Enablement roster

Worker: Digital Adoption Lead (`digital-adoption-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.1.1.3 Enablement roster.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.1.1. The other skills under this competency do a different job.

### What it does
Name who must be able to deliver the leave-behind before launch day.

### Method
1. List the roles (field, medical, access) that will use it.
2. State the date each role is briefed and who briefs them.
3. Record a role that will not be briefed, and why.

### Do not
Do not treat a file in a shared folder as enablement.

### Output
A roster: role, briefing date, briefer.

A missing fact stays [GAP].

## DH-02.01.1.1.4 Read the launch sequence

Worker: not bound.
Skill: CF-12.02.01.1.1.4 Read the launch sequence.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.get_launch_sequence`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Dates come from stored authorization and listing dates. A date the source does not state stays blank.

Catalogue job: `competitor-landscape`.

## DH-02.01.1.1.5 Read launch readiness

Worker: not bound.
Skill: CF-12.02.01.1.1.5 Read launch readiness.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.get_launch_readiness`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Seven criteria, each met, attested, or [GAP]. This is a count, not a score. Do not invent a met criterion.

Catalogue job: `competitor-landscape`.

## DH-02.01.1.1.6 Commercial brief

Worker: not bound.
Skill: CF-12.02.01.1.1.6 Commercial brief.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.generate_commercial_brief`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Same arguments as the commercial report, template memo. The first line states it is not a regulatory opinion.

Catalogue job: `competitor-landscape`.
