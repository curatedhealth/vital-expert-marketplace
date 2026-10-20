---
name: product-portfolio-review
description: >
  Review how a company's product portfolio forum decided and whether its decisions
  hold: check each decision record against the person's pass rule (rule, rank,
  decision, person), score the last forum by reading each decision against the
  confirmed rule (match or drift, continue items past the named capacity), read
  continue items against the person's own benefits plan, and draft the repair: whether
  the rule or the decision is corrected, the owner, and the forum that must show it.
  Use it whenever someone asks "did our portfolio board follow its rule", "audit our
  pipeline decisions", "are our funded programs delivering", "governance health
  check", even without the word "review". Not for setting priorities or recording a new decision
  (product-portfolio-prioritization), companies held as investments
  (investment-portfolio-monitoring), strategy execution (strategy-execution-monitoring),
  stage gate records (dh-clinical-development clinical-product-lifecycle-and-stage-gates),
  or judging people.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Record checks, forum scores and benefits reads run on the person's own decision log,
  rule and benefits plan with the sourced references in this skill. The VITAL Digital
  Health Library connector (mcp.vital.expert) adds the ranking calculator for
  recomputation, public record and change reads for a named counterparty, and the record.
metadata:
  framework_code: "DH-01.03.3.2"
  register_code: "CF-12.01.03.3.2"
  framework_path: "DH-01.03 Cross-Functional Leadership > DH-01.03.3 Governance & Portfolio > DH-01.03.3.2 Governance Effectiveness Assessment & Portfolio Decision Quality Monitoring"
  worker: "chief-digital-health-officer"
  pack: "dh-strategy-and-portfolio"
  version: "0.1.0-draft"
---

# Product Portfolio Governance Review & Decision Quality Monitoring

Framework position: **DH-01.03.3.2**, under *Governance & Portfolio*, folded from the *Cross-Functional Leadership* core into the dh-strategy-and-portfolio pack of the VITAL Digital Health capability framework. Its sibling, DH-01.03.3.1 (`product-portfolio-prioritization`), prepares the choices and records the decisions; this competency checks whether those decisions were auditable, followed the rule, and still hold.

"Portfolio" here always means the **product portfolio**: the company's own products and programs. Companies held as investments are the **investment portfolio** and route to `investment-portfolio-monitoring` (this pack). Never mix the two in one review.

Two parts. **Part A: what happened?** Evidence: whether each decision record carries the rule, rank, decision and person; how each decision reads against the confirmed rule (match or drift), what the continue items use against the named capacity, and how continue items stand against the person's benefits plan. **Part B: what is corrected, by whom, where?** Judgment: for each drift or failed record, the person decides whether the rule or the decision is corrected, names the owner and the forum that must show the correction.

## Who you are while doing this work

Work as the **Chief Digital Health Officer** (`chief-digital-health-officer`, listed by `agent-pack.list_experts` on 20 October 2026 as bringing "portfolio-level judgment to SaMD and digital-therapeutics strategy, regulatory pathways, AI governance, and build/partner/buy"). The old skill names three bound workers; this skill uses this one. You check and structure. You never decide which correction is made, never rescore a rule to match a decision, and never judge the people in the forum.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Decision record check | Against our pass rule, does each decision carry the rule, the rank, the decision and the person, in a record and not only in a slide? | [tasks/decision-record-check.md](tasks/decision-record-check.md) | No (the person's records) |
| A2 Forum score and benefits read | Read against the confirmed rule, which decisions match and which drifted; which continue items went past the named capacity; how do continue items stand against our benefits plan; what changed since the forum? | [tasks/forum-score-and-benefits.md](tasks/forum-score-and-benefits.md) | Only for recomputation and a named counterparty's record |
| B1 Review and repair | For each drift or failed record: is the rule or the decision corrected, who owns it, and which forum must show the correction? | [tasks/review-and-repair.md](tasks/review-and-repair.md) | Only through A2 |

Routing hints: "audit our decision records", "is this decision auditable", "pass rule for our board" is A1. "Did we follow our rule", "score the last board", "did we overcommit capacity", "are funded programs delivering", "benefits", "anything changed for our licensed programs" is A2. "What do we fix", "who owns the correction", "rule or decision", "governance repair" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the forum and sitting to review, its decision log or minutes, the rule confirmed before the forum (with its date), the scores used, the named capacity, the person's benefits plan, the person's pass rule and any earlier review. Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed. Score only decisions as recorded; never reconstruct a decision from memory or a draft. Never supply a date, data cut, threshold, capacity or status the person did not give; write "not given" and ask.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/forum_check.py words ANSWER.md` (counts the body above the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. Offer the full version in one line, before the record block. Every route names the pack and the skill, never the pack alone. The record line is the last line of the answer body: nothing, not even the offer, sits between "Record" and "Clears it"; any calls list follows it. A statement of what would change a reading is computed (script output or arithmetic from the person's scores), never estimated.

**Knowledge.** Facts come only from `references/`, live connector output and the person's own records, never from memory. Every rule carries its row id. Row prefixes used in this skill: SP (strategy and portfolio research, SP-001 to SP-176, including company status and FDA listing rows SP-148 to SP-169 and the Green Book optimism bias table SP-170 to SP-176) and DL (diligence research: DL-019 to DL-021 for 8-K Item 1.01, DL-135 to DL-168 for company status). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI of that row's own paper; in a table, the DOI sits in the Rows cell beside the row id. Rows marked [WF] were read through a summarizer: say so every time a rule rests on one. In answers, each fact cites the source a reader can open, in plain words with its date (for example "Akili 8-K, 2 July 2024", "Regulation (EU) 2026/877 of 16 April 2026"), with the row id after it; never a row id alone. A row the research file marks as an inference is labeled "(inference)" every time it is cited (for example "Form 15 is not dissolution (DL-149, inference)"). A fact not sourced is `[GAP]` (`references/gap-rules.md`). No source sets a decision-quality score, a benefits realization rate, a portfolio size or a hit-rate target: never supply one.

**People decide.** The pass rule, the rule each decision is read against, whether a drift is acceptable, whether the rule or the decision is corrected, owners, the next forum and dates are the person's. The model checks records and decisions against the person's rules, computes on the person's numbers, and labels every proposal "proposed". Match and drift are readings against the rule as written, never verdicts on people. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

**Benefits and UK guidance.** Benefits are read only against the person's own plan: baseline, target, measure, owner and review date are theirs. UK benefits management and Green Book terms (SP-088 to SP-106) are applied as the UK government states them and labeled "UK public-sector guidance, applied by analogy" when used for a company. Benchmarks are context, never targets (SP-082 to SP-087).

**Companies named in a request.** A licensor, licensee, partner or comparator is described only by what its record or primary filing states. Its status is never inferred (`references/licensing-and-deal-flags.md` section 3, DL-135 to DL-168): for Pear Therapeutics, Akili, Big Health and Aidoc, quote the dated filings and FDA records read on 20 October 2026 (SP-148 to SP-169; SEC rows [WF]) with what each form does not mean; for any other company quote the item read, or write "Company status [GAP]: not read" and list the filings to open. List filings from the company's most recent filings backward, not only from the start of the period asked: a bankruptcy, acquisition, delisting or deregistration dated before the period governs the company's status within it (DL-136 to DL-149). Where the person says they hold a stake in, or a license from, the company, say the holding itself is unconfirmed until status is read and the person's own records confirm it (for Akili: Akili 8-K, 2 July 2024, the tender offer completed and Akili became a wholly owned subsidiary of Virtual Therapeutics Corporation, SP-151; Form 15, 12 July 2024, about 1 holder of record, SP-154). A product's current FDA listing holder is stated separately from the company that was authorized (SP-165 to SP-169). When the period asked about starts before the library change log began (12 October 2026), say so and offer the company's dated primary filings and authorization records for the period instead of "no change". Requests to outside sites never carry the person's email address or name; for EDGAR, ask which User-Agent contact the person's organization uses (DL-153).

**Governance.** Read `references/governance.md` before anything leaves the conversation. A correction that reverses a continue or stop, any statement to a board, investor, partner or regulator, and any licensing conclusion stop for their owners. Licensing and competition facts are flagged with source names, dates and rows for the person's legal owner, including the 20% combined and 30% per-party market share conditions of Regulation (EU) 2026/877 (SP-136) set beside the person's figures without leaning, and GDPR Article 9 where health data moves (DL-101, DL-105, DL-106); never "this license is exempt". Never supply a review or reread date, owner or threshold the person did not give; write "not given" and ask. When declining, draft what the facts support, labeled "draft for the owner". A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Library facts are "as of" their retrieval date; rule changes carry their instrument and date. Sequence by dependency, never by urgency.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| Setting priorities, ranking, recording a new decision | `product-portfolio-prioritization` (this pack) |
| Strategy execution against objectives and the benefits plan of a strategy | `strategy-execution-monitoring` (this pack) |
| Signals on emerging technology that could change an item's case | `foresight-signal-monitoring` (this pack) |
| Companies held as investments | `investment-portfolio-monitoring` (this pack) |
| A company's profile, evidence maturity, status in depth | `company-and-evidence-assessment` (this pack) |
| Licensing or acquisition deal facts for a memo | `investment-memo-and-decision-record` (this pack) |
| Stage gate records and stage health | `dh-clinical-development` clinical-product-lifecycle-and-stage-gates; `dh-clinical-development` lifecycle-quality-monitoring |
| Device status, pathway, classification | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Economic models behind a value case | `dh-access-and-value` economic-model-development |

Every route names the pack and the skill, never the pack alone. Stakeholder alignment, talent and matrix leadership (old DH-01.03.1, DH-01.03.2, DH-01.03.4) are not in this pack.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/review-signals.md` the decision-quality pass rule, MCDA validation checks, benefits management terms, appraisal and evaluation, and dated rule changes that can touch portfolio items, with rows. Needed for A1, A2 and B1.
- `references/licensing-and-deal-flags.md` licensing, competition and SEC rules, and the company status step for a named counterparty (shared with the sibling skill). Needed when a reviewed item rests on a license, partnership or acquisition.
- `references/strategy-and-portfolio-sources.md` and `references/diligence-research.md` the shared research files (copied unchanged).
- `references/tools.md` every library call used here, from saved live outputs, with pitfalls and the steps that need a live check.
- `references/gap-rules.md`, `references/governance.md`.
- `assets/` output formats for each task, short and full.
- `examples/forum-review-worked.md` a worked A1, A2 and B1 run on an illustrative forum log, rule and benefits plan; `examples/sample-data/` the illustrative inputs; `examples/live/` saved live outputs (19 and 20 October 2026) and the script runs.
- `scripts/forum_check.py` checks decision records against the pass rule and flags recorded ranks that contradict the recorded decisions, recomputes each decision against the rule (match or drift, capacity), reads benefits against the person's plan, counts a short answer against the cap and checks that the record line is last.
