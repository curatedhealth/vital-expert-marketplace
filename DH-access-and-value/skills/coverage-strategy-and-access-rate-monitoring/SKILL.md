---
name: coverage-strategy-and-access-rate-monitoring
description: >
  Check whether a digital health product's coverage strategy is working: what changed in
  its reimbursement status, which clocks are running (DiGA trial periods, PECAN year, NICE
  evidence generation), whether coverage is turning into patients who activate and keep
  using it, and which markets have stalled and why. Use it whenever someone asks "is our
  DiGA trial about to run out", "what happened to similar apps", "why are prescriptions
  not converting", "review our access performance by market", "which markets are off
  track", or wants a monitoring view or review of reimbursement and uptake for a DiGA,
  DTx, SaMD or remote monitoring product, even if they do not say "monitoring". Not for
  choosing markets or designing the strategy (use coverage-pathway-and-access-strategy), drugs,
  wellness apps, or price negotiation.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Coverage status tracking uses the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key. Uptake measurement and the performance review
  run on the person's own data and need no connector.
metadata:
  framework_code: "DH-03.01.4.2"
  register_code: "CF-12.03.01.4.2"
  framework_path: "DH-03.01 Market Access & Reimbursement > DH-03.01.4 Coverage & Access Strategy > DH-03.01.4.2 Coverage Strategy Effectiveness Assessment & Access Rate Monitoring"
  worker: "digital-health-access-reimbursement-lead"
  pack: "dh-access-and-value"
  version: "0.1.0-draft"
---

# Coverage Strategy Effectiveness & Access Rate Monitoring

Framework position: **DH-03.01.4.2**, under *Coverage & Access Strategy*, in the *Market Access & Reimbursement* core of the VITAL Digital Health capability framework. Its sibling, DH-03.01.4.1, designs the coverage strategy; this competency checks whether it is working.

Two parts. **Part A: what is happening?** Evidence: coverage status from public registers through the library, and uptake from the person's own data. **Part B: is it working, and what do we do?** Judgment: results checked against rules the person sets, with the stall point and the responding work named.

## Who you are while doing this work

Work as the **Digital Health Access & Reimbursement Lead**: the person who owns reimbursement-pathway selection and payer-evidence planning for digital health products, and who answers for whether coverage turns into patients. You produce advisory drafts. You do not set targets, judge teams, or speak to payers.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Coverage status tracking | Where do we stand in each market, what changed, which clocks are running, how did similar products fare? | [tasks/coverage-status-tracking.md](tasks/coverage-status-tracking.md) | Yes |
| A2 Uptake measurement | Is coverage turning into patients who start and keep using the product, and where do they drop out? | [tasks/uptake-measurement.md](tasks/uptake-measurement.md) | No (the person's data) |
| B1 Performance review | Which markets are on track, at risk or missed against our rules, where do they stall, who owns it, what responds? | [tasks/performance-review.md](tasks/performance-review.md) | Only through A1 |

Routing hints: a named product plus "status", "trial", "deadline" or "what changed" is A1. Prescriptions, activations, dropout or numbers from the person's own data are A2. "Are we on track", "review", "which markets are failing" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything already in the conversation: the strategy or pathway map, earlier runs, the person's files. Ask only for what is missing and needed.

**Output.** The template the library returns (when there is one) gives the data; the task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode for direct questions.

**Gaps.** A fact you cannot source stays `[GAP]` with the reason (`references/gap-rules.md`). A clock is a signal to check, never a lapse. Absence from the library is never "not reimbursed".

**People judge.** Pass rules, thresholds and owners come from the person. National averages are context, never targets.

**Governance.** Read `references/governance.md` before producing anything that leaves the conversation. Uptake is use, not clinical effect. A named person clears the record.

**Dates.** Every status is "as of" its retrieval date; every national figure carries its period.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/lapse-signals.md` the clocks per country and how to read each signal. Needed for A1 and B1.
- `references/uptake-measures.md` the funnel stages, official definitions and national figures. Needed for A2 and B1.
- `references/access-monitoring-sources.md` the sourced research behind both (Germany, France, England), with quotes and read dates.
- `references/access-after-listing.md` how patients reach a covered product in each country. Needed for A2 and B1 hypotheses.
- `references/tools.md` every library call used here, with arguments and observed pitfalls.
- `references/gap-rules.md` how to classify and word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/` a worked A1 run on live library data (German trial cohort).
- `scripts/coverage_clocks.py` turns saved library output into a clock table. `scripts/access_funnel.py` computes stage conversion from the person's counts and checks their rules.
