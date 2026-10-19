---
name: "DH-02.02.2.1 Account Growth Strategy & Renewal Management Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.02.2.1 Account Growth Strategy & Renewal Management Execution. Use when the user asks for Renewal horizon, Growth offer, Renewal risk note. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02.2.1 Account Growth Strategy & Renewal Management Execution

Heading: DH-02.02.2 Expansion & Renewal.
Core: DH-02.02 Customer Success & Implementation.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.02.2.1.1 Renewal horizon

Worker: Digital Partnerships Director (`digital-partnerships-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.2.1.1 Renewal horizon.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.2.1. The other skills under this competency do a different job.

### What it does
List accounts whose renewal is inside the horizon.

### Method
1. Set the horizon (for example 120 days) and the date of the list.
2. Include each account with the renewal date and the current unit.
3. Mark accounts with an open implementation bar as not ready to expand.

### Do not
Do not propose expansion to an account that missed go-live.

### Output
A renewal list with readiness.

A missing fact stays [GAP].

## DH-02.02.2.1.2 Growth offer

Worker: Digital Partnerships Director (`digital-partnerships-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.2.1.2 Growth offer.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.2.1. The other skills under this competency do a different job.

### What it does
Name the expansion offer for accounts that are ready.

### Method
1. For each ready account, name the additional module, site, or population.
2. Tie the offer to a result the account has already seen, or mark the result [GAP].
3. Name the internal owner of the conversation.

### Do not
Do not offer a module the account has not used the current one of.

### Output
An offer per ready account.

A missing fact stays [GAP].

## DH-02.02.2.1.3 Renewal risk note

Worker: Digital Partnerships Director (`digital-partnerships-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.2.1.3 Renewal risk note.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.2.1. The other skills under this competency do a different job.

### What it does
Write the risk on accounts that may not renew.

### Method
1. State the reason (value unseen, champion gone, price, implementation open).
2. State the action before the renewal date.
3. Name the owner of that action.

### Do not
Do not mark an account healthy because the contract has not expired.

### Output
A risk note per account that may not renew.

A missing fact stays [GAP].
