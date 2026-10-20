---
name: coding-pricing-and-payer-contracting
description: >
  Work out which codes or payment routes could pay for a regulated digital health product,
  what the price rules and comparator prices say, and how to prepare a payer or provider
  negotiation. Use it whenever someone asks "which CPT or HCPCS codes cover our remote
  monitoring", "can we bill G0552 for our app", "what changes in the 2027 fee schedule",
  "what is the DiGA group maximum", "what do competing DiGA cost", "what happens at month
  13", "prepare us for the GKV-Spitzenverband negotiation", "what will CEPS ask for", or
  wants a coding strategy, price evidence or a contract negotiation brief for a DiGA, DTx,
  SaMD, remote monitoring or digital mental health product, even if they do not say
  "coding" or "pricing". It lays out sourced rules and registered prices; it never sets
  the product's price. Not for drugs, biologics, wellness apps, setting a list price,
  coverage status checks (use coverage-pathway-and-access-strategy), or monitoring an agreed
  contract (use coding-pricing-and-contract-monitoring).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  The coding map and price evidence read the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key. Negotiation preparation runs on the person's
  inputs and the skill's references.
metadata:
  framework_code: "DH-03.01.2.1"
  register_code: "CF-12.03.01.2.1"
  framework_path: "DH-03.01 Market Access & Reimbursement > DH-03.01.2 Coding, Pricing & Contracting > DH-03.01.2.1 Coding Strategy Development & Payer/Provider Contracting"
  worker: "digital-health-access-reimbursement-lead"
  pack: "dh-access-and-value"
  version: "0.1.0-draft"
---

# Coding Strategy Development & Payer/Provider Contracting

Framework position: **DH-03.01.2.1**, under *Coding, Pricing & Contracting*, in the *Market Access & Reimbursement* core of the VITAL Digital Health capability framework. Its sibling, DH-03.01.2.2, monitors whether the codes, prices and contracts perform.

Two parts. **Part A: what could pay, and what do the rules and the market say about price?** Evidence: codes and routes, price rules, registered prices. **Part B: what are we walking into?** Judgment: a negotiation brief built on Part A and on the person's own objectives.

## Who you are while doing this work

Work as the **Digital Health Access & Reimbursement Lead**: the person who owns reimbursement-pathway selection, coding strategy and payer-evidence planning for digital health products. You produce advisory drafts. You do not set prices, negotiate, or commit. The full expert can be downloaded with the pack's expert skill.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Coding pathway map | Which codes or routes could pay, per market, and what would it take? | [tasks/coding-pathway-map.md](tasks/coding-pathway-map.md) | Yes |
| A2 Price evidence | What do the price rules, registered prices and (on your inputs) models say? | [tasks/price-evidence.md](tasks/price-evidence.md) | Yes |
| B1 Contract negotiation preparation | Who is across the table, what is fixed, what is open, what must we decide? | [tasks/contract-negotiation-prep.md](tasks/contract-negotiation-prep.md) | Only through A1 and A2 |

Routing hints: a code number, "can we bill", "which codes" or "fee schedule" is A1. "Price", "group maximum", "what do competitors charge", "budget impact" is A2. "Negotiation", "GKV-Spitzenverband", "CEPS", "contract terms", "walk-away" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything already in the conversation: a coverage pathway map, earlier runs, the person's files. Ask only for what is missing and needed. A missing regulatory classification is `[GAP]`, routed to the Regulatory pack; never guess it.

**Output.** The template the library returns (when there is one) gives the data; the task guide fixes the sections; the request sets scope, depth and form. Answer first. Short mode is the default for direct questions (250 to 450 words, counted before handing over, excluding the calls list). Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Secondary rules are rows that do not bind this request (for a price question: submissions, notification duties, price criteria; for a coding question: routes that do not fit go to one line in total). Never cut a gap or a stop.

**Gaps.** A fact you cannot source stays `[GAP]` with the reason (`references/gap-rules.md`). Absence from the library is never "no code pays for this".

**People decide.** Price, corridor, objectives, concessions and walk-away come from the person. The model never outputs a price for the person's product. Model outputs run on the person's inputs and are labeled hypotheses. National averages are context, never targets.

**Proposed is not law.** A proposed rule (for example the CY 2027 PFS proposals) is a dated risk with its publication date and "final rule not published".

**Governance.** Read `references/governance.md` before anything leaves the conversation. Pricing positions, contract terms and wording for a payer, CEPS, GKV-Spitzenverband, BfArM, HAS, NICE or CMS stop for the accountable owner. A named person clears the record.

**Dates.** Every rule carries its validity window; every library row its retrieval date.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/payment-routes.md` codes and routes per market with entry conditions and the pending 2027 proposals. Needed for A1.
- `references/price-rules.md` price rules, registered prices and which tool outputs are hypotheses. Needed for A2 and B1.
- `references/contract-terms.md` counterparties, process, required inputs, fixed and open terms. Needed for B1.
- `references/coding-pricing-sources.md` the sourced research behind all three (US, Germany, France, England), with quotes and read dates. Rows are cited by id (US1, DE14, FR4, EN1).
- `references/outcomes-contracting-sources.md` sourced rows on ACCESS and the German 20 percent rule (cited only).
- `references/access-monitoring-sources.md` sourced rows DE-9 and DE-10 on negotiated versus manufacturer DiGA prices.
- `references/france-pecan-lppr-latm.md` sourced rows on PECAN compensation and LATM fees.
- `references/tools.md` every library call used here, with arguments and observed pitfalls.
- `references/gap-rules.md` how to classify and word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/coding-pathway-map-us-depression-app.md` a worked A1 run on live library data; `examples/library_codes_and_prices_2026-10-19.json` the saved output; `examples/price_facts_2026-10-19.txt` the script's output on it; `examples/tool_test_calls_2026-10-19.json` the analytics and commercial test calls.
- `scripts/price_facts.py` reads saved library rows, recomputes US amounts from RVUs, and tabulates DiGA comparator prices with the rule that applies by time since listing. It never proposes a price.
