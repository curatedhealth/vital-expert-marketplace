---
name: dh-02-01-2-1-market-segmentation-go-to-market-strategy-developme
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.01.2.1 Market Segmentation & Go-to-Market Strategy Development. Use when the user asks for Segment definition, Go-to-market motion, Positioning line, Screen commercial peers, Commercial landscape report, List commercial sources. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.2.1 Market Segmentation & Go-to-Market Strategy Development

Heading: DH-02.01.2 GTM Strategy.
Core: DH-02.01 Commercial & GTM Strategy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.01.2.1.1 Segment definition

Worker: Digital Marketing Manager (`digital-marketing-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.2.1.1 Segment definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.2.1. The other skills under this competency do a different job.

### What it does
Define the segments this go-to-market will serve.

### Method
1. Name each segment by buyer, setting, and the job they hire the product for.
2. State the segment that is in scope for this plan and the segment that is not.
3. Give each in-scope segment one reason it is first, second, or later.

### Do not
Do not define a segment only by specialty.

### Output
A segment list with sequence and exclusions.

A missing fact stays [GAP].

## DH-02.01.2.1.2 Go-to-market motion

Worker: Digital Marketing Manager (`digital-marketing-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.2.1.2 Go-to-market motion.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.2.1. The other skills under this competency do a different job.

### What it does
Choose the motion for each in-scope segment.

### Method
1. For each segment, name the channel (direct, partner, access-led) and the offer.
2. Name the proof the segment needs before a meeting.
3. Drop a motion that has no owner.

### Do not
Do not assign every segment the same motion.

### Output
A motion per segment: channel, offer, proof, owner.

A missing fact stays [GAP].

## DH-02.01.2.1.3 Positioning line

Worker: Digital Marketing Manager (`digital-marketing-manager`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.2.1.3 Positioning line.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.2.1. The other skills under this competency do a different job.

### What it does
Write the positioning line the motion will repeat.

### Method
1. Write one line per in-scope segment: who it is for, what changes, and what it is not.
2. Check the line against the claim list if one exists; otherwise mark claims [GAP].
3. Reject a line that could describe a competitor without a change.

### Do not
Do not write a line for an out-of-scope segment.

### Output
One positioning line per in-scope segment.

A missing fact stays [GAP].

## DH-02.01.2.1.4 Screen commercial peers

Worker: not bound.
Skill: CF-12.02.01.2.1.4 Screen commercial peers.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.screen_commercial_peers`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for a segment. Limit is 1 to 25. Coverage names which of the three feeds answered. A peer a feed did not return is a gap.

Catalogue job: `competitor-landscape`.

## DH-02.01.2.1.5 Commercial landscape report

Worker: not bound.
Skill: CF-12.02.01.2.1.5 Commercial landscape report.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.generate_report`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Render the public report from sections already held. Templates are memo, identity, regulatory, reimbursement, or commercial. Do not treat it as a regulatory opinion.

Catalogue job: `competitor-landscape`.

## DH-02.01.2.1.6 List commercial sources

Worker: not bound.
Skill: CF-12.02.01.2.1.6 List commercial sources.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.list_commercial_dh_sources`. This call is not counted. Do not close it with Verify.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Free list of the diligence, regulatory, and market-access feeds this suite reads. Do not recount those feeds as new calls.

Catalogue job: `competitor-landscape`.
