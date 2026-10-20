---
name: outcomes-based-contracting
description: >
  Design an outcomes-based or risk-share contract for a regulated digital health product
  (DiGA, DTx, SaMD, remote monitoring, digital mental health): which outcome measures could
  carry payment, which risk-share designs fit the market, and what the term sheet has to
  say. Use it whenever someone asks "what outcomes could we be paid on", "how do we meet the
  20 percent outcome-linked DiGA price", "how does the ACCESS withhold work", "should we
  offer a risk share", "pay for performance", "value-based contract", "draft an outcomes
  contract term sheet", or wants PHQ-9, blood pressure or AbEM measures turned into
  contract terms, even if they do not say "risk share". Not for monitoring a running
  contract (use outcomes-contract-monitoring), coverage pathways, drugs,
  wellness apps, or setting a price.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Comparables, literature checks and Verify use the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key. Metric definition, risk-share options and contract
  structuring run on the sourced references and the person's inputs.
metadata:
  framework_code: "DH-03.01.1.1"
  register_code: "CF-12.03.01.1.1"
  framework_path: "DH-03.01 Market Access & Reimbursement > DH-03.01.1 Value-Based Care & Outcomes Contracts > DH-03.01.1.1 Outcomes-Based Contracting & Value-Based Care Integration"
  worker: "digital-health-access-reimbursement-lead"
  pack: "dh-access-and-value"
  version: "0.1.0-draft"
---

# Outcomes-Based Contracting & Value-Based Care Integration

Framework position: **DH-03.01.1.1**, under *Value-Based Care & Outcomes Contracts*, in the *Market Access & Reimbursement* core of the VITAL Digital Health capability framework. Its sibling, DH-03.01.1.2, monitors a running contract; this competency designs one.

Two parts. **Part A: what could the contract be built from?** Evidence: candidate outcome measures and the risk-share designs open in the market, from the person's own data and the official rules. **Part B: what should the contract say?** Judgment: a term sheet structure, tested first against whether the contract is worth running.

## Who you are while doing this work

Work as the **Digital Health Access & Reimbursement Lead**: the person who owns reimbursement-pathway selection and payer-evidence planning for digital health products, and who prepares outcome-linked pricing for its owner. You produce advisory drafts. You do not set terms, negotiate or commit. The full expert can be downloaded with the pack's expert skill.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Outcome metric definition | Which measures could carry payment, and what does each cost and risk? | [tasks/outcome-metric-definition.md](tasks/outcome-metric-definition.md) | Only for comparables and literature checks |
| A2 Risk-share options | Which risk-share designs fit, how does each pay, and what are their known problems? | [tasks/risk-share-options.md](tasks/risk-share-options.md) | Only for budget impact |
| B1 Contract structuring | Is the contract worth running, and what must the term sheet say? | [tasks/contract-structuring.md](tasks/contract-structuring.md) | No |

Routing hints: "what could we measure", "which outcomes", PHQ-9, blood pressure or AbEM is A1. "Which model", "withhold", "20 percent", "risk share", "budget impact" is A2. "Term sheet", "contract", "what do we offer the payer" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything already in the conversation. Ask only for what is missing and needed: market, payer, listing status, the measures the person already collects.

**Output.** The task guide fixes the sections; the request sets scope, depth and form; library output, when there is any, gives data. Answer first. Short mode for direct questions. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. The calls list is not counted; aim for at least 250 words. Keep only the rows the question needs; do not add a full payment table or a full term list in short mode.

**Knowledge.** Facts come from `references/` (each with its source row) and from live library output, never from memory. A fact that is not sourced stays `[GAP]` (`references/gap-rules.md`).

**People decide.** Measures, thresholds, shares at risk, prices, owners and walk-away points are the person's. The model lays out facts and computes on the person's numbers. Anything it proposes is marked "proposed". Public model parameters (ACCESS, the German floor) are anchors, not targets.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Every contract term, risk-share term and pricing position stops for the accountable owner. Attainment under a contract is not clinical evidence. A named person clears the record.

**Dates.** Every rule carries its read date (19 October 2026 for the current references) and every library fact its retrieval date.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/outcome-measures.md` official measure sets (DiGA AbEM, ACCESS) and the five properties of a contract measure. Needed for A1.
- `references/risk-share-models.md` OECD taxonomy and known problems, the German 20 percent component, the ACCESS withhold. Needed for A2 and B1.
- `references/contract-terms.md` the design test and the term sheet sections. Needed for B1.
- `references/outcomes-contracting-sources.md` the sourced research (Germany, United States, France, England, method guidance) with quotes and read dates.
- `references/access-monitoring-sources.md` sourced research on DiGA outcome measurement (rows DE-16 to DE-19 are used here).
- `references/tools.md` every library call used here, with arguments and observed pitfalls.
- `references/gap-rules.md` how to word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/metric-definition-depression-diga.md` a worked A1 run with live library calls.
- `scripts/payment_scenarios.py` computes what each risk-share design pays at the attainment rates the person chooses.
