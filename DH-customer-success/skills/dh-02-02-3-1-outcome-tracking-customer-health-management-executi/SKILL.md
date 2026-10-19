---
name: dh-02-02-3-1-outcome-tracking-customer-health-management-executi
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.02.3.1 Outcome Tracking & Customer Health Management Execution. Use when the user asks for Health signal list, Account health read, Value note to the account. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02.3.1 Outcome Tracking & Customer Health Management Execution

Heading: DH-02.02.3 Customer Health & Value Realization.
Core: DH-02.02 Customer Success & Implementation.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.02.3.1.1 Health signal list

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.3.1.1 Health signal list.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.3.1. The other skills under this competency do a different job.

### What it does
Choose the signals that mean this customer is healthy.

### Method
1. Name signals the product can show (active users, task completed, outcome recorded).
2. Name the threshold for each signal and the period.
3. Drop a signal the product does not store.

### Do not
Do not use a survey score as the only signal if the product has usage data.

### Output
A signal list with thresholds.

A missing fact stays [GAP].

## DH-02.02.3.1.2 Account health read

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.3.1.2 Account health read.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.3.1. The other skills under this competency do a different job.

### What it does
Read each in-scope account against the signals.

### Method
1. Pull the signals for the period.
2. Mark each account above or below each threshold.
3. Keep the account id.

### Do not
Do not mark an account healthy when a day-one workflow is still open.

### Output
A health read per account.

A missing fact stays [GAP].

## DH-02.02.3.1.3 Value note to the account

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.3.1.3 Value note to the account.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.3.1. The other skills under this competency do a different job.

### What it does
Write what the account should be shown.

### Method
1. For an account above the threshold, name the result you can show.
2. For an account below, name the signal and the next action.
3. Do not send a result you cannot trace to a signal.

### Do not
Do not send a value story to an account below every threshold.

### Output
A note per account: result or next action.

A missing fact stays [GAP].
