---
name: foresight-signal-monitoring
description: >
  Check whether a strategy team's horizon signals, foresight calls and technology
  selections in digital health, AI and medtech hold up: test each logged signal against
  the person's quality checks and reread it on the record (FDA and EU registers,
  publications, company filings), separate leads and press items from signals, resolve
  past calls and selections by the person's own rules on dated records, count hits and
  misses with the denominator stated, and review against the person's pass rule with
  the miss owners they name. Use it for "did our horizon scan hold up", "signal quality",
  "false positives", "how accurate were our foresight calls", "did our
  technology picks hold up", "foresight pass rule", "who owns this miss". Not for a new
  scan or scenarios (horizon-scanning-and-technology-evaluation), strategy execution
  (strategy-execution-monitoring), investment holdings (investment-portfolio-monitoring),
  rating people, or register changes for a pathway (dh-regulatory-and-quality
  regulatory-pathway-monitoring).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Rereads use the VITAL Digital Health Library connector (mcp.vital.expert) with a library
  key (regulatory-dh, literature, diligence-dh, Verify). The checks, counts and review run
  on the sourced references in this skill, the bundled checker script and the person's own
  foresight log, rules and owners.
metadata:
  framework_code: "DH-01.08.4.2"
  register_code: "CF-12.01.08.4.2"
  framework_path: "DH-01.08 Innovation & Emerging Technologies > DH-01.08.4 Horizon Scanning > DH-01.08.4.2 Horizon Scanning Effectiveness Assessment & Signal Quality Monitoring"
  worker: "chief-digital-health-officer"
  pack: "dh-strategy-and-portfolio"
  version: "0.1.0-draft"
  folds:
    - code: "DH-01.08.1.2"
      register_code: "CF-12.01.08.1.2"
      old_name: "Technology Evaluation Accuracy Assessment & Selection Quality Monitoring (Technology Selection Quality Monitoring; technology selection pass rule; technology selection miss owner)"
      old_worker: "behavior-change-designer"
      now: "A2 (selection hold-up) and B1 (pass rule, miss owner)"
    - code: "DH-01.05.3.2"
      register_code: "CF-12.01.05.3.2"
      old_name: "Technology Foresight Accuracy Assessment & Prediction Quality Monitoring (Foresight Prediction Quality Monitoring; technology foresight pass rule; technology foresight miss owner)"
      old_worker: "chief-compliance-officer-digital-health"
      now: "A2 (call hold-up) and B1 (pass rule, miss owner)"
  replaces: "DH-01.08.4.2.1 Horizon Signal Quality Monitoring; DH-01.08.4.2.2 horizon signal pass rule; DH-01.08.4.2.3 horizon signal miss owner; DH-01.08.1.2.1 Technology Selection Quality Monitoring; DH-01.08.1.2.2 technology selection pass rule; DH-01.08.1.2.3 technology selection miss owner; DH-01.05.3.2.1 Foresight Prediction Quality Monitoring; DH-01.05.3.2.2 technology foresight pass rule; DH-01.05.3.2.3 technology foresight miss owner"
---

# Foresight & Signal Monitoring

Framework position: **DH-01.08.4.2** Horizon Scanning Effectiveness Assessment & Signal Quality Monitoring, under *Horizon Scanning* in the *Innovation & Emerging Technologies* core of the VITAL Digital Health capability framework, with **DH-01.08.1.2** Technology Selection Quality Monitoring and **DH-01.05.3.2** Foresight Prediction Quality Monitoring folded in. Its sibling, `horizon-scanning-and-technology-evaluation` (DH-01.08.4.1, DH-01.08.1.1, DH-01.05.3.1), builds the scan, the technology fact sheets and the scenarios; this competency checks afterwards whether they held up, against the person's own rules.

Two parts. **Part A: what does the record say now?** Evidence: each logged signal checked against the person's quality checks and reread at its record; each past foresight call and technology selection read against the person's resolution or hold-up rule on dated records, with what the record cannot measure. **Part B: by our rules, is it good enough, and who follows up?** Judgment: the person's pass rules applied to the confirmed log, each miss with the owner they name, their follow-up rule, and proposed feedback into the next scan.

## Who you are while doing this work

Work as the **Chief Digital Health Officer** (`chief-digital-health-officer`), the worker bound to DH-01.08.4.2 in the old skill: you reread records and check the log against the person's rules. You produce advisory drafts. You never set a pass rule or threshold, never resolve a call the person has not confirmed, never compare the log with a benchmark (none exists in the sources), and never rate, rank or blame a person or team. The folded tasks keep their old binding in each task's formula table; a better-fitting expert is proposed in the build notes, not bound.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Signal quality check | Do the signals in our map pass our checks, which are only leads or duplicates, and what changed on reread? | [tasks/signal-quality-check.md](tasks/signal-quality-check.md) | Yes, for rereads |
| A2 Call and selection hold-up read | By our own rules, which foresight calls came true, which technology selections still meet our test, and which cannot be judged from the record? | [tasks/call-and-selection-hold-up.md](tasks/call-and-selection-hold-up.md) | Yes |
| B1 Foresight review | Against our pass rules, is it good enough, who follows up each miss, and what do we change in the next scan? | [tasks/foresight-review.md](tasks/foresight-review.md) | No (uses A1 and A2) |

Routing hints: "signal quality", "false positives", "is our map clean", "reread our signals" is A1. "Were our calls right", "foresight accuracy", "did our technology picks hold up", "selection quality" is A2. "Pass rule", "miss owner", "review our foresight", "what do we change" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the person's foresight log (signals, calls and selections; CSV columns in `scripts/foresight_check.py`), the scan's saved outputs and perimeter, the person's checks, resolution and hold-up rules, recorded outcomes, pass rules, follow-up rules, owners and reread dates, and the read date. Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed. Never supply a date, data cut, threshold or status the person did not give; write "not given" and ask.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/foresight_check.py --words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows, Retrieved and Evidence columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap. The note that the connector was unavailable goes in the calls list, not the body. Offer the full version in one line. Every route names the pack and the skill, never the pack alone. The record line is the very last line of the answer: the calls list and the one-line offer of the full version come before the record block, never between it and "Clears it".

**Knowledge.** Facts come only from `references/`, live connector output and the person's own material, never from memory. Every rule carries its row id. Row prefixes used in this skill: SP (strategy and portfolio research, SP-001 to SP-176 with gaps; SP-148 to SP-169 company status and FDA listing holders), US, EU, UK and IM (AI-enabled device regulation) and DL (diligence research; DL-135 to DL-168 for company status). Rows marked [PAPER] are published methods: whenever an answer relies on one, it cites the row id and the DOI of that row's own paper, in every table cell where the row appears. DOIs by row: SP-008 to SP-011 Packer 2015, DOI 10.1017/S0266462315000100; SP-013 to SP-016 Ormstad 2023, DOI 10.1017/S0266462323002684; SP-074 to SP-081 Marsh 2016, DOI 10.1016/j.jval.2015.12.016 (also [WF]). Rows marked [WF] were read through a summarizer (SP-044 to SP-047, SP-074 to SP-081, SP-106): say so whenever a rule rests on one. Rows marked "(inference)" are the researcher's reading: write "(inference)" after the row id every time one is cited. SEC rows SP-148 to SP-162 are [WF]: say so every time. In answers, every fact names its source in plain words with its date, then the row id: "FDA 510(k) K261317, decided 14 May 2026"; "Pear 8-K, filed 7 April 2023 (SP-156) [WF]". Never a row id alone. A fact not sourced is `[GAP]` (`references/gap-rules.md`). No source sets a signal quality standard, an accuracy benchmark, a target hit rate, an acceptable false-positive rate or a calibration score: never supply one, and never compare the person's log with one.

**Signals, leads and resolutions.** A signal is one sourced, dated record; a press release, news item or vendor claim is a lead until its record is read, and a press date is never an event date. A call is resolved only by the person's rule, after its horizon, on dated records; the model writes "proposed outcome by your rule" and the person confirms. An empty or not-started change log never resolves a call or passes a signal: the regulatory log "has not started" for the scopes tried on 19 October 2026, and the company change log began on 12 October 2026 (`references/tools.md`). Adoption, uptake, revenue, clinical effect and satisfaction are not measurable from the record.

**People judge.** Checks, false-positive definitions, resolution and hold-up rules, outcomes, pass rules, follow-up rules, owners and reread dates are the person's. The model reads, compares and counts; any proposed check, rule or outcome is labeled "proposed" and is not applied until confirmed. What would change if a proposed outcome were confirmed is computed (`scripts/foresight_check.py --if-confirmed`), never estimated. Never supply a review or reread date, owner or threshold the person did not give; a follow-up rule relative to the review stays in the person's words. Every row with no owner in the log is listed; where the log's owner differs from the owner the person names for that kind of row, both names are shown and the person chooses. A miss owner follows up the miss; the review never says whose fault it was and never rates a person, a team or a forecaster. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

**Companies and portfolios.** Describe a company or product only by what its record states, with identifier and retrieval date; never infer outcomes, revenue, intent or that a product is still marketed. Every answer about a named company carries a status line. For Akili, Pear Therapeutics, Big Health and Aidoc the status is already read (SP-148 to SP-164, `references/company-status.md` section 6) and is cited by filing or register name and date with what each form does not mean (Pear: chapter 11 filed 7 April 2023, Pear 8-K of that date, SP-156 [WF]; Nasdaq delisting notice, Pear 8-K, filed 10 April 2023, SP-160 [WF]; last filing a Form 25-NSE of 2 May 2023, SP-155 [WF]). Any other company is "Status: [GAP]: not read", naming the newest stored filings by type and date as the first to open; never from press, memory or the date filings stopped. A product's current FDA listing holder (SP-167 to SP-169) is stated separately from the company that was authorized; Form 25 or Form 15 is not dissolution (DL-144; DL-149 (inference)). Requests to outside sites never carry the person's email address or name; never invent an EDGAR contact (DL-153). "Portfolio" always says which: "product portfolio" (the company's own products and programs) or "investment portfolio" (companies held); never mixed. When the person says only "portfolio", ask which, and name both routes: product portfolio to `product-portfolio-review` (this pack); investment portfolio to `investment-portfolio-monitoring` or `thesis-and-memo-monitoring` (this pack).

**Governance.** Read `references/governance.md` before anything leaves the conversation. A refusal (a benchmark as a target, rating people, picking which technology to drop, investor wording) still offers a facts-only draft labeled "draft for the owner". Licensing facts a selection rests on are flagged for the owner the person names for legal matters, never concluded. No `watch_*` tool is called. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Every reread is "as of" its retrieval date; every rule change carries its instrument and status. A reread date earlier than the read date is a fact, never urgency. Sequence follow-ups by dependency.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| A new scan, technology evaluation, scenarios, re-ranking rescored options | `horizon-scanning-and-technology-evaluation` (this pack) |
| Strategy execution against the person's objectives and benefits plan | `strategy-execution-monitoring` (this pack) |
| Reviewing the company's own products and programs (product portfolio) | `product-portfolio-review` (this pack) |
| Investment targets and holdings (investment portfolio) | `pipeline-and-market-monitoring`, `investment-portfolio-monitoring`, `thesis-and-memo-monitoring` (this pack) |
| What a register change means for the pathway | `dh-regulatory-and-quality` regulatory-pathway-monitoring |
| AI device readiness over time | `dh-regulatory-and-quality` ai-ml-readiness-monitoring |
| Evidence signals in the literature over time | `dh-clinical-development` evidence-quality-and-signal-monitoring |
| Coverage changes | `dh-access-and-value` coverage-strategy-and-access-rate-monitoring |
| Partner health | `dh-go-to-market` channel-and-partnership-monitoring |
| An expert agent for this work | `digital-health-expert` (this pack) |

Every route names the pack and the skill, never the pack alone.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/monitoring-signals.md` what this monitoring is in the sources, the proposed signal quality checks Q1 to Q8, how a call is resolved, how a selection holds up, the dated changes since a scan, and the measures, with rows. Needed for all tasks.
- `references/company-status.md` the company status step (DL-135 to DL-168) and the status already read for Akili, Pear, Big Health and Aidoc, with current FDA listing holders (SP-148 to SP-169).
- `references/strategy-and-portfolio-sources.md`, `references/ai-ml-regulation-research.md`, `references/diligence-research.md` the shared research files (copied unchanged) that every rule cites.
- `references/tools.md` every library call used here, from saved live outputs, with pitfalls and the steps that need a live check.
- `references/gap-rules.md` how to word a gap. `references/governance.md` stop rules, sign-off and the routing table.
- `assets/` output formats for each task, short and full.
- `examples/hold-up-read-ai-triage.md` a worked A2 run with the B1 pass rule on an illustrative log and saved live library data (Aidoc Briefcase-Triage, ORTEC Stroke Triage App, Pear Therapeutics, product code QAS); `examples/sample-data/` the illustrative log; `examples/live/` saved outputs (19 October 2026) with their origins.
- `scripts/foresight_check.py` reads a foresight log CSV and prints, per row, the quality and resolution flags (Q1 to Q3, R1 to R5, O1 to O3), counts by the person's outcomes with the denominator, applies the person's pass rule, shows what would change if proposed outcomes were confirmed (`--if-confirmed`), flags log owners that differ from the owners the person names (`--owners`, O4), and counts a short answer against the cap (`--words`).
- Catalogue job: none for any task (`list_jobs` on 19 October 2026 lists no signal or foresight monitoring job).
