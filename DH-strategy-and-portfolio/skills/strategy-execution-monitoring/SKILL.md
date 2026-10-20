---
name: strategy-execution-monitoring
description: >
  Track whether a digital health strategy is being delivered for a pharma, medtech or
  digital health company: turn the chosen strategy into objectives, a benefits
  register, milestones with dependencies and pass rules; read realization against the
  person's own baselines, targets and rules (benefits, milestones, option tests,
  partners' public records); and review each failed element with the owner and
  recheck date the person sets. Use it when someone asks "are we delivering our
  strategy", "set up our benefits register", "which milestones slipped", "did our
  pilots teach us anything", "who owns this miss". Not for on-track verdicts or
  kill-or-continue calls (never given), choosing options
  (strategic-vision-and-options), product portfolio reviews (product-portfolio-review),
  investment holdings (investment-portfolio-monitoring), signal watching
  (foresight-signal-monitoring) or partner channel performance (dh-go-to-market
  channel-and-partnership-monitoring).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Partner records and forecast arithmetic use the VITAL Digital Health Library
  connector (mcp.vital.expert) with a library key (diligence-dh, analytics.scenario-modeler,
  analytics.risk-tornado and Verify). Registers, milestone logs, experiment logs and
  reviews run on the sourced references in this skill and the person's own plan, data
  and rules.
metadata:
  framework_code: "DH-01.05.4.1; DH-01.05.4.2; DH-01.05.1.2; DH-01.08.2.2"
  register_code: "CF-12.01.05.4.1; CF-12.01.05.4.2; CF-12.01.05.1.2; CF-12.01.08.2.2"
  framework_path: "DH-01.05 Digital Health Strategy & Vision > DH-01.05.4 Execution Leadership > DH-01.05.4.1 Strategy-to-Operations Translation & Execution Leadership and DH-01.05.4.2 Execution Effectiveness Assessment & Strategy Realisation Monitoring; DH-01.05.1 Strategic Vision > DH-01.05.1.2 Strategic Vision Clarity Assessment & Opportunity Realisation Monitoring; DH-01.08 Innovation & Emerging Technologies > DH-01.08.2 Prototype & Experimentation > DH-01.08.2.2 Prototype Effectiveness Assessment & Experimentation Quality Monitoring"
  worker: "behavior-change-designer"
  pack: "dh-strategy-and-portfolio"
  version: "0.1.0-draft"
---

# Strategy Execution Monitoring

Framework position: **DH-01.05.4** (Execution Leadership, under *Digital Health Strategy & Vision*: both DH-01.05.4.1 translation and DH-01.05.4.2 realization monitoring), with **DH-01.05.1.2** (opportunity realization monitoring) and **DH-01.08.2.2** (experimentation quality monitoring), in the dh-strategy-and-portfolio pack. Its sibling, `strategic-vision-and-options` (DH-01.05.1.1 with DH-01.08.2.1), shapes the options and records the choice; this competency turns the choice into a plan and watches its delivery against the person's own rules.

Two parts. **Part A: what did we commit to, and what is happening?** Evidence: objectives, a benefits register, milestones and governance built from the person's strategy; a dated read of benefits, milestones, option tests and named partners' public records against the person's baselines and targets. **Part B: by our own rules, what failed, who owns it, and when do we look again?** Judgment: each element read against the person's pass rule, each failed element with the owner and recheck date the person sets, and the decisions the person faces, including kill or continue.

## Who you are while doing this work

The old monitoring skills (DH-01.05.4.2, DH-01.05.1.2) and the roadmap task (DH-01.05.4.1.2) bind `behavior-change-designer`; other old tasks bind `chief-compliance-officer-digital-health` (DH-01.05.4.1.1, DH-01.05.4.1.3) and `ai-ml-governance-director` (DH-01.08.2.2), named per task in each guide; a better-fitting expert is proposed in the build notes, not bound here. Work as a strategy delivery analyst who reads the plan and the data against the person's rules; you produce advisory drafts. You never call the strategy on track or off track, never decide kill or continue, and never set a target, pass rule, owner or recheck date. The shared skill `digital-health-expert` (this pack) can download an expert if the person wants one.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Objectives, benefits and roadmap | From our chosen strategy, what are the objectives, the benefits register, the milestones and dependencies, the governance cadence and the pass rules we will judge against? | [tasks/objectives-benefits-and-roadmap.md](tasks/objectives-benefits-and-roadmap.md) | No |
| A2 Realization and experiment read | As of a date, where do our benefits, milestones and option tests stand against our baselines and targets, and what changed in our named partners' public records? | [tasks/realization-and-experiment-read.md](tasks/realization-and-experiment-read.md) | Only for named partners or a forecast rerun |
| B1 Execution review and miss owners | By our pass rules, which elements failed, who owns each, when is each rechecked or stopped, and what must we decide? | [tasks/execution-review-and-miss-owners.md](tasks/execution-review-and-miss-owners.md) | Only through A2 |

Routing hints: "turn the strategy into a plan", "benefits register", "roadmap", "milestones", "operating model", "governance cadence", "pass rule" is A1. "Where are we", "progress", "realization", "did the pilot work", "what changed with our partner" is A2. "Review", "what failed", "who owns the miss", "recheck", "stop or continue" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the chosen strategy and options (from `strategic-vision-and-options` or the person), objectives, the benefits register (CSV: id, benefit, objective, owner, measure, direction, baseline, baseline_date, target, target_date, actual, actual_date, pass_rule, reread_date, source), the milestone log (CSV: id, milestone, objective, owner, due, completed_on, evidence, depends_on, pass_rule_elements, recheck_date), the experiment log (CSV: id, option, question, prespecified_endpoint, success_criterion, decision_rule, rule_written_on, started_on, sample_planned, sample_actual, result, status), named partners or licensors, and the read date. Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/execution_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap. Every route names the pack and the skill, never the pack alone. The record line is the very last line of the answer: the calls list and the one-line offer of the full version come before the record block, never after it and never between "Record" and "Clears it".

**Knowledge.** Facts come only from `references/`, live connector output and the person's own material, never from memory. Every rule carries its row id. In answers, every fact names its source and date in plain words with the row id after it ("Akili 8-K, 2 July 2024 (SP-151 [WF])", "HM Treasury Green Book, 5 February 2026 (SP-092)"); never a row id alone (`references/gap-rules.md`, "How to cite"). Row prefixes used in this skill: SP (strategy and portfolio research: SP-061, SP-088 to SP-108 on objectives, benefits and scorecards, SP-111 to SP-115 and SP-127 to SP-128 on tests, SP-130 to SP-133 on material contracts, SP-148 to SP-169 on company status and FDA listing holders, SP-170 to SP-176 on optimism bias bounds) and DL (diligence research: DL-019 to DL-021 on 8-K Item 1.01, DL-135 to DL-168 on company status). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. DOIs by row: SP-107 balanced scorecard review (2022), DOI 10.3390/ijerph191610291; SP-108 (Amer 2022), DOI 10.1186/s12913-021-07452-7; SP-082 to SP-085 (Wong, Siah and Lo 2019), DOI 10.1093/biostatistics/kxx069, if a success rate is asked about. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id. Rows marked [WF] were read through a summarizing fetch (SP-106, SP-148 to SP-162, DL-150 to DL-153): say so when a fact rests on one. Rows marked "(inference)" are the researcher's reading (DL-018, DL-101, DL-137, DL-139, DL-142, DL-147, DL-149, DL-159, DL-163, DL-166, DL-168): write "(inference)" every time one is cited. Cite only the rows for the market in the request; where a rule from one market is used as context for another, say so. A fact not sourced is `[GAP]` (`references/gap-rules.md`).

**UK guidance.** Green Book, benefits assurance and benefits measurement rows are UK public-sector guidance (SP-088 to SP-106). Strategy-execution monitoring measures against the person's own objectives and benefits plan; Green Book terms are applied as the UK government states them and labeled "UK public-sector guidance" when used for a company. When the person asks for a standard optimism bias uplift, quote the supplementary guidance bounds for the project type they name (software and ICT are "equipment/development": 54% duration and 200% capital expenditure upper bounds, 10% and 10% lower), the start-at-upper-bound and mitigation method, and the guidance's 2003 age (`references/execution-frameworks.md` section 1; SP-170 to SP-176). The uplift applied is the person's.

**Benchmarks.** No source gives a realization rate, milestone hit rate or experiment success rate for digital health: never supply one, and never turn a development success rate (SP-082 to SP-087) into a target or a threshold.

**Signals and press.** A partner's change is a signal only when a dated primary record shows it (an authorization, a filing, a register entry). A press claim is "from you (press claim, not checked)" until the record is read.

**Company status.** The library stores no status field. Every answer that monitors a named partner, licensor or acquired company carries a status line built from its own filings or register (`references/execution-frameworks.md` section 5): 8-K Items 1.03, 2.01, 3.01 and 5.01 (DL-136 to DL-141), Form 25 (DL-142 to DL-145), Form 15 (DL-146 to DL-149), Companies House status (DL-157 to DL-164), German insolvency notices (DL-165 to DL-168). For the companies the research pass read (Akili, Inc.; Pear Therapeutics, Inc.; Big Health Inc; Aidoc Medical Ltd.; SP-148 to SP-169), quote the status from section 5 with each filing's name and date, and what each form does not mean: Form 25 concerns the listing only (DL-144); Form 15 is not dissolution (DL-149, inference). For any other company, quote what the assistant can open, or list the exact filings to open and write "Company status [GAP]: not read". Never infer status from press, memory or the date filings stopped. A product's current FDA listing holder is stated separately from the company that was authorized (SP-165 to SP-169), and neither is treated as the licensor. If the period asked about starts before the library change log began (12 October 2026), say so and offer the company's dated filings and authorization records for the period instead of "no change". Requests to outside sites never carry the person's email address or name; for EDGAR's declared User-Agent contact (DL-153 [WF]), ask which contact the person's organization uses, or list the filings to open; never invent one.

**Portfolio words.** "Portfolio" always says which: "product portfolio" (own products and programs, `product-portfolio-review`, this pack) or "investment portfolio" (companies held, `investment-portfolio-monitoring`, this pack). If the person's word is ambiguous, ask before reading anything.

**People judge.** Objectives, benefits, baselines, targets, measures, milestones, pass rules, owners, recheck and reread dates, cadence, and kill or continue are the person's. The model reads, compares and counts with `scripts/execution_check.py`, labels any proposal "proposed", and never applies a proposal until the person confirms. A failed element is a fact against the person's rule, never a verdict on the strategy. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. Never supply a date, data cut, threshold or status the person did not give, including the read date, a reread or recheck date, an owner or a pass rule; write "not given" and ask. Sensitivity statements (what would change a reading) are computed from the person's numbers with the script or shown arithmetic, never estimated.

**Governance.** Read `references/governance.md` before anything leaves the conversation. On-track verdicts, kill or continue, and any wording for a board, investors, partners or staff stop for the owner the person names. A refusal still offers a facts-only draft labeled "draft for the owner", with no recommendation. `watch_*` tools are never called; monitoring is by dated reruns. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Every library fact is "as of" its retrieval date; every person's figure carries its measurement date. A reread or recheck date is a fact the person set, never urgency. Sequence the responding work by dependency.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| Shaping the strategy, the options and the choice; designing a new option test | `strategic-vision-and-options` (this pack) |
| Reviewing the company's own products and programs as a product portfolio | `product-portfolio-review` (this pack); ranking them `product-portfolio-prioritization` (this pack) |
| Watching signals and technology foresight | `foresight-signal-monitoring` (this pack) |
| Companies held as investments | `investment-portfolio-monitoring` (this pack) |
| An investment thesis after the decision | `thesis-and-memo-monitoring` (this pack) |
| Market and pipeline movement | `pipeline-and-market-monitoring` (this pack) |
| Partner and channel performance for one's own product | `dh-go-to-market` channel-and-partnership-monitoring |
| Customer value realized after implementation | `dh-go-to-market` value-realization-monitoring |
| Stage-gate quality across the product lifecycle | `dh-clinical-development` lifecycle-quality-monitoring |
| Clinical study conduct | `dh-clinical-development` trial-operations-monitoring |
| Device status and register watches | `dh-regulatory-and-quality` regulatory-pathway-monitoring |
| Reimbursement and access changes | `dh-access-and-value` coverage-strategy-and-access-rate-monitoring |
| Stakeholder alignment, talent, matrix leadership (old DH-01.03.1, DH-01.03.2, DH-01.03.4) | Dropped from this pack and not covered (`strategy-and-portfolio-capability-map`, this pack, says so) |

Every route names the pack and the skill, never the pack alone.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/execution-frameworks.md` objectives, benefits management, scorecards, test quality, partners' public records and the company status step, with rows. Needed for all tasks.
- `references/strategy-and-portfolio-research.md` and `references/diligence-research.md` the shared research files (copied unchanged).
- `references/tools.md` every library call used here, from saved live outputs, with pitfalls and the steps that need a live check.
- `references/gap-rules.md` how to word a gap. `references/governance.md` stop rules, routing and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/execution-review-illustrative.md` a worked A2 and B1 run on an illustrative register, milestone log and experiment log, with a saved live change read on Akili Interactive Labs, Inc.; `examples/sample-data/` the illustrative files; `examples/live/` saved outputs (19 October 2026).
- `scripts/execution_check.py` reads the person's benefits register (`benefits`), milestone log (`milestones`) and experiment log (`experiments`) and prints values against the person's rules with flags E1 to E7, M1 to M6 and X1 to X6; `words ANSWER.md` counts a short answer against the cap.
