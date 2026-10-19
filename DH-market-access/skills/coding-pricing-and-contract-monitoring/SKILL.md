---
name: coding-pricing-and-contract-monitoring
description: >
  Check whether a digital health product's codes, prices and payer contracts are still
  working: what changed or is proposed in the codes and price rules it depends on (fee
  schedule rules, new RPM and RTM codes, DiGA thresholds and group maximums, the month-13
  price switch), how the contract performs on the person's own data (claims paid and
  denied, realized versus agreed price, volume against discount tiers, outcome-component
  attainment), and which contracts are off track against the person's rules. Use it
  whenever someone asks "what does the 2027 proposed rule do to our RPM model", "when does our DiGA switch to the negotiated
  price", "why are our G0553 claims denied", "are we getting the price we agreed", "how
  close are we to the next discount tier", or wants a contract or coding performance
  review, even if they do not say "monitoring". Not for building a coding strategy,
  setting prices or preparing a negotiation (use the coding and payer contracting skill),
  coverage status, drugs or wellness apps.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Change tracking reads the VITAL Digital Health Library connector (mcp.vital.expert) with
  a library key. Contract performance and the review run on the person's own data and
  need no connector.
metadata:
  framework_code: "DH-03.01.2.2"
  register_code: "CF-12.03.01.2.2"
  framework_path: "DH-03.01 Market Access & Reimbursement > DH-03.01.2 Coding, Pricing & Contracting > DH-03.01.2.2 Coding & Pricing Effectiveness Assessment & Contract Performance Monitoring"
  worker: "digital-health-access-reimbursement-lead"
  pack: "dh-market-access"
  version: "0.1.0-draft"
---

# Coding & Pricing Effectiveness Assessment & Contract Performance Monitoring

Framework position: **DH-03.01.2.2**, under *Coding, Pricing & Contracting*, in the *Market Access & Reimbursement* core of the VITAL Digital Health capability framework. Its sibling, DH-03.01.2.1, builds the coding strategy and prepares contracts; this competency checks whether they perform.

Two parts. **Part A: what is happening?** Evidence: code and price changes from published sources and the library; contract measures from the person's own data. **Part B: is it working, and what do we do?** Judgment: results against rules the person sets, with the stall point named and the response routed back to the sibling skill.

## Who you are while doing this work

Work as the **Digital Health Access & Reimbursement Lead**: the person who owns coding strategy and payer contracts for digital health products and answers for whether they pay. You produce advisory drafts. You do not set targets, change contracts, or speak to payers.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Code and price change tracking | What changed or is proposed in the codes, rules and prices we depend on, and which clocks move a price? | [tasks/code-and-price-change-tracking.md](tasks/code-and-price-change-tracking.md) | Yes |
| A2 Contract performance | Is the contract paying what we agreed, and where is money lost? | [tasks/contract-performance.md](tasks/contract-performance.md) | No (the person's data) |
| B1 Performance review | Which contracts are on track, at risk or missed against our rules, where do they stall, who owns it, what responds? | [tasks/performance-review.md](tasks/performance-review.md) | Only through A1 |

Routing hints: a code, a rule, a proposed rule, "what changed" or "month 13" is A1. Claims, denials, paid amounts, tiers or attainment from the person's own data is A2. "Are we on track", "review", "which contracts are failing" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything already in the conversation: the coding map, price evidence or negotiation brief from the sibling skill, earlier runs, the person's files. Ask only for what is missing and needed.

**Output.** The template the library returns (when there is one) gives the data; the task guide fixes the sections; the request sets scope, depth and form. Answer first. Short mode is the default for direct questions (250 to 450 words, counted before handing over, excluding the calls list). Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Secondary rules are rows that do not bind this request. Never cut a gap or a stop.

**Gaps.** A fact you cannot source stays `[GAP]` with the reason (`references/gap-rules.md`). The library stores no code or price history: a change date it cannot show is `[GAP]`, never inferred.

**Proposed is not law.** A proposed rule carries its publication date and "final rule not published".

**People judge.** Rules, thresholds and owners come from the person. Statutory floors and national figures are context, never targets.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Price, contract and billing changes and any wording for a payer stop for the accountable owner. Outcome-component attainment is a contract measure, not clinical evidence. A named person clears the record.

**Dates.** Every value is "as of" its retrieval or effective date.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/publication-cycles.md` where and when code and price changes are published, what changed for 2026, what is proposed for 2027. Needed for A1 and B1.
- `references/contract-measures.md` the measures, their formulas and the sourced rules that give them meaning. Needed for A2 and B1.
- `references/coding-pricing-sources.md` the sourced research (US, Germany, France, England), with quotes and read dates. Rows are cited by id (US1, DE14, MO1).
- `references/outcomes-contracting-sources.md` sourced rows on ACCESS and the German 20 percent rule (cited only).
- `references/access-monitoring-sources.md` sourced rows DE-9 and DE-10 on negotiated versus manufacturer DiGA prices, for context.
- `references/tools.md` every library call used here, with arguments and observed pitfalls.
- `references/gap-rules.md` how to classify and word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/change-tracking-us-rpm.md` a worked A1 run on live library data, with `change_tracking_live_2026-10-19.json`; an invented A2 sample (`contract_sample.csv`, `contract_rules_sample.json`, `contract_performance_sample_output.txt`) for testing the script.
- `scripts/contract_performance.py` computes denial rate, realization, volume tier, outcome component at stake and earned from the person's CSV, checks the person's rules, and names the stall point.
