---
name: thesis-and-memo-monitoring
description: >
  Watch an investment thesis and the facts in a memo on a digital health company
  (DTx, SaMD, DiGA) after the decision: set which assumptions to re-check and
  the public signal behind each, read what changed in the record since the memo date
  (authorizations, studies, safety events, SEC filings, evidence maturity) and in the
  deal rules (HSR, EU and Swiss screening, Companies House), and review each assumption
  against the person's own triggers with owners and reread dates. Use it when someone
  asks "has anything changed since our memo", "is our thesis on Akili still holding",
  "what should we monitor after the investment", "review our assumptions". Not for writing the memo or decision record
  (investment-memo-and-decision-record), sell, hold or write-down advice (never given),
  market screens (pipeline-and-market-monitoring), evidence maturity over time
  (evidence-maturity-monitoring), portfolio views (investment-portfolio-monitoring), or device
  status (dh-regulatory-and-quality regulatory-pathway-and-classification).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Change reads use the VITAL Digital Health Library connector (mcp.vital.expert) with a
  library key (diligence-dh and Verify). Watch lists and assumption reviews run on the
  sourced references in this skill and the person's memo, assumptions and triggers.
metadata:
  framework_code: "DH-DIL.4.2"
  register_code: "none (diligence suite, not a CF-12 row)"
  framework_path: "DH-DIL Diligence > DH-DIL.4 Investment memo and thesis > DH-DIL.4.2 Thesis and memo monitoring"
  worker: "not bound"
  pack: "dh-strategy-and-portfolio"
  version: "0.1.0-draft"
---

# Thesis & Memo Monitoring

Framework position: **DH-DIL.4.2**, under *Investment Memo & Thesis*, in the diligence suite of the VITAL dh-strategy-and-portfolio pack. This pack is not a CF-12 row. Its sibling, DH-DIL.4.1 (`investment-memo-and-decision-record`), assembles the memo and records the decision; this competency watches the memo's facts and the person's thesis afterwards against the triggers the person sets.

Two parts. **Part A: what do we watch, and what changed?** Evidence: a watch list of the person's thesis assumptions, each tied to a public signal and the source that carries it; a dated read of what changed in the company's record and in the deal rules since the memo date, with what the library cannot see. **Part B: does the thesis still hold by our triggers?** Judgment: each assumption read against the person's own trigger, with the owner the person names, whether the person reopens the decision, and the date it is read again.

## Who you are while doing this work

No worker is bound to this suite ("Worker: not bound" in the old skills). Work as a diligence analyst who re-reads the record and checks it against the person's rules; you produce advisory drafts. You never advise selling, holding, buying more or writing down, never give a valuation, and never reopen or change a decision; that is the person's.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Thesis watch list | Which of our thesis assumptions and memo facts do we re-check, which public signal and source carries each, and which cannot be watched from the record? | [tasks/thesis-watch-list.md](tasks/thesis-watch-list.md) | No |
| A2 Change read since the memo | Since our memo date, what changed in the company's record and in the deal rules, and what can the library not see? | [tasks/change-read-since-memo.md](tasks/change-read-since-memo.md) | Yes |
| B1 Thesis review | Against our triggers, which assumptions hold, which are tripped, which cannot be measured, who owns each, and when do we read them again? | [tasks/thesis-review.md](tasks/thesis-review.md) | Only through A2 |

Routing hints: "what should we monitor", "set up our watch list", "which assumptions" is A1. "What changed since", "anything new on", "new filings", "new clearance", "did the rules change" is A2. "Is the thesis holding", "review our assumptions", "which triggers fired", "who follows up" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the memo or decision record (from `investment-memo-and-decision-record` or the person), its date, the thesis assumptions and memo facts, the person's triggers, owners and reread dates, the company references, earlier saved runs, and an assumption register (CSV: id, assumption, company, signal, value at memo, memo date, trigger, trigger rule, owner, reread date). Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and the Source, Source of now and Rows columns. Before handing over, count the words with `python3 scripts/thesis_check.py --words ANSWER.md` (counts the body above the calls list and leaves out Source, Source of now and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap. Offer the full version in one line. Every route names the pack and the skill, never the pack alone. The record line is the very last line of the answer: the offer of a full version and any calls list come before the record block, never between "Record" and "Clears it".

**Knowledge.** Facts come only from `references/`, live connector output and the person's own material, never from memory. Every rule carries its row id. Row prefixes used in this skill: DL (diligence research, DL-001 to DL-168; DL-135 to DL-168 cover company status) and CP (channels and partners research: CP-US-44 to CP-US-49, CP-US-54 to CP-US-56, CP-EU-01 to CP-EU-09). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. DOIs by row: DL-107 to DL-115 Evidence DEFINED (Silberman 2023), DOI 10.1038/s41746-023-00836-5; DL-116 to DL-118 clinical robustness score (Day 2022), DOI 10.2196/37677; DL-119 (Marshall 2023), DOI 10.2196/41715; DL-120 and DL-121 (Sedhom 2021), DOI 10.1038/s41746-021-00476-7; DL-122 and DL-123 (Goldsack 2025), DOI 10.1038/s41598-025-21996-2; DL-124 and DL-125 (Vinay 2025), DOI 10.1371/journal.pone.0323390. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id. Rows marked "(inference)" are the researcher's reading: say so when a rule rests on one. A fact not sourced is `[GAP]` (`references/gap-rules.md`). No source gives a market size, valuation multiple or return benchmark: never supply one, and never compare the company with one.

**Companies.** Describe a company only by what its record or primary filing states, with reference and retrieval date. Never infer revenue, runway, outcomes, financial health, intent or why filings stopped, and never infer that a product is still marketed or withdrawn. "No change recorded" is a statement about the library's change log, not about the company. When the period asked for starts before the change log began (12 October 2026), say so and offer the company's dated primary filings and authorization records for that period instead of reporting "no change". Form D never shows valuation or investor names (DL-016; DL-018 (inference)).

**Company status.** The library stores no status field: it does not show whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. Every answer that monitors a named company carries a status line (`references/monitoring-signals.md` section 6): read the company's own filings or register where the assistant can open them (8-K Items 1.03, 2.01, 3.01 and 5.01, DL-136 to DL-141; Form 25, DL-142 to DL-145; Form 15, DL-146 to DL-149; Companies House status, DL-157 to DL-164; German insolvency notices, DL-165 to DL-168) and quote the item with its date; otherwise list the exact filings to open and write "Company status [GAP]: not read". Never infer status from press, memory or the date filings stopped. Form 25 or Form 15 is not dissolution (DL-144, DL-149). Requests to outside sites never carry the person's email address or name; for EDGAR's declared User-Agent contact (DL-153), ask which contact the person's organization uses, or list the filings to open; never invent one.

**Named companies already read.** `references/named-company-status.md` holds the filings and FDA records read on 20 October 2026 (SP-148 to SP-169): Pear Therapeutics (chapter 11, Pear 8-K, 7 April 2023; Nasdaq delisting notice, Pear 8-K, 10 April 2023; Form 25-NSE, 2 May 2023), Akili (merger agreement with Virtual Therapeutics, Akili 8-K, 29 May 2024; completion and change in control, Akili 8-K, 2 July 2024; Form 25-NSE, 2 July 2024; Form 15, 12 July 2024), Big Health and Aidoc (no SEC registrant found; active FDA establishment registrations), and the current FDA listing holders of Somryst (Nox Medical), EndeavorRx (Akili Interactive Labs c/o Virtual Therapeutics), reSET and reSET-O (Harvest Bio). For these companies, state status from those rows with what each form does not mean (a Form 25 or Form 15 is not dissolution); keep "Status: [GAP]: not read" only where no row covers the company. State a product's current FDA listing holder separately from the company that was authorized: the 510(k) or De Novo page names the applicant at clearance, not today's holder, and a listing is not the sale record (SP-161, SP-165 to SP-169; DL-133 (inference)).

**Sources a reader can open.** In answers, each fact cites the source name and date in plain words, then the row id: "Pear 8-K, 7 April 2023 (SP-156 [WF])", "BfArM DiGA page, as of 9 September 2026 (DE34)", "VITAL library screen_market, saved 19 October 2026". Never a row id alone. A row the research file marks as an inference is labeled "(inference)" every time it is cited. Never supply a review or reread date, owner or threshold the person did not give: write "not given" and ask. A statement of what would change a ranking or a result is computed, not estimated: run the helper script or show the arithmetic from the person's own scores. Where a market-share or other legal threshold is involved, put the threshold and the person's figure side by side without saying in prose whether the deal is under or over it, for the owner the person names for legal questions, and include every flag the rows support (for example GDPR Article 9, DL-099 to DL-106, where health or training data is licensed or acquired).

**People judge.** Which assumptions to watch, the triggers and thresholds, whether a trigger is tripped when the reading is ambiguous, whether the decision is reopened, owners and reread dates come from the person. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. Never supply a date, data cut, threshold or status the person did not give; write "not given" and ask. The model reads, compares and counts; any proposed signal or trigger is labeled "proposed" and is not applied until the person confirms. A tripped trigger is a fact against the person's rule, never a recommendation.

**Confidential material.** Non-public material (board packs, management accounts) the person supplies is used only for their request, labeled "from you (non-public)", kept apart from record facts and never sent to a library call.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Sell, hold, write-down, valuation and any wording for LPs, a board, the company or the press stop for the owner the person names. Whether a rule change makes a deal or a holding notifiable or non-compliant is for the owner the person names for legal or compliance, or owner not named. A refusal (sell, hold, write-down, valuation, investor or LP wording) still offers a facts-only draft labeled "draft for the owner", with no recommendation. `watch_companies` and every `watch_*` tool are described only, never called. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Every library fact is "as of" its retrieval date; every rule change carries its instrument and date. A reread date is a fact the person set, never urgency. Sequence the responding work by dependency.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| The company's own product portfolio (own products and programs), strategy options, execution against objectives, horizon scanning (investment portfolio questions stay in the diligence skills) | `product-portfolio-prioritization`, `product-portfolio-review`, `strategic-vision-and-options`, `strategy-execution-monitoring`, `horizon-scanning-and-technology-evaluation`, `foresight-signal-monitoring` (this pack); start with `strategy-and-portfolio-capability-map` |
| Writing the memo or the decision record, transaction flags at the deal | `investment-memo-and-decision-record` (this pack); B1 routes reopened decisions there |
| Market and pipeline movement beyond the held company | `pipeline-and-market-monitoring` (this pack) |
| Evidence maturity over time with a named framework | `evidence-maturity-monitoring` (this pack) |
| Several holdings at once, portfolio funding views | `investment-portfolio-monitoring` (this pack) |
| Device status, pathway, classification | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Register watches on devices | `dh-regulatory-and-quality` regulatory-pathway-monitoring |
| AI Act and AI-enabled device questions | `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control |
| Reimbursement or coverage changes | `dh-access-and-value` coverage-strategy-and-access-rate-monitoring |
| Competitive positioning for one's own product | `dh-go-to-market` gtm-positioning-monitoring |
| Literature behind an evidence assumption | `dh-clinical-development` literature-and-real-world-evidence-review |
| Health economic models | `dh-access-and-value` economic-model-development |

Every route names the pack and the skill, never the pack alone.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/monitoring-signals.md` which thesis assumptions a public signal can carry, where each signal comes from, the dated rule changes, and the company status step (section 6), with rows. Needed for all tasks.
- `references/diligence-research.md` and `references/channels-partners-launch-sources.md` the shared research files (copied unchanged).
- `references/tools.md` every library call used here, from saved live outputs, with pitfalls and the steps that need a live check.
- `references/gap-rules.md` how to word a gap. `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/thesis-review-pear.md` a worked A2 and B1 run on an illustrative assumption register and saved live library data; `examples/live/` saved outputs (19 October 2026).
- `scripts/thesis_check.py` reads an assumption register CSV and saved library outputs and prints, per assumption, the value at the memo, the value now, whether the person's trigger rule is met, flags T1 to T6, and the company status filings to open; `--words ANSWER.md` counts a short answer against the cap.
- `references/named-company-status.md` status of named companies (Pear Therapeutics, Akili, Big Health, Aidoc) and current FDA listing holders of named products, as the filings and FDA records state them on 20 October 2026, each with what it does not mean (SP-148 to SP-169).
- `references/strategy-and-portfolio-research.md` the shared strategy and portfolio research file (SP rows, copied unchanged with its origin line); this skill cites the company status rows SP-148 to SP-169.
