---
name: cross-region-compliance-monitoring
description: >
  Keep a software medical device compliant in every region it is already in: where it is
  authorized according to the registers, which registration, renewal and acceptance dates
  are running (FDA annual registration, Health Canada annual statement, EUDAMED device
  registration, CE acceptance end dates in Great Britain, Swiss registration), what the
  regulators changed or have in draft, and whether the multi-region plan is holding. Use
  it whenever someone asks "what are our registration deadlines across markets", "do we
  need to register in EUDAMED by November", "how long is our CE mark accepted in the UK",
  "what changed at FDA, MHRA or Swissmedic that affects us", "is that rule final or still
  a draft", "review our compliance by region", even if they do not say "monitoring". Not
  for planning entry into new regions (use the multi-region regulatory alignment skill),
  vigilance reporting, drugs, wellness apps, or reimbursement.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Market status uses the VITAL Digital Health Library connector (mcp.vital.expert) with a
  library key. The obligations table, change tracking against sourced references and the
  performance review run on the references and the person's own facts.
metadata:
  framework_code: "DH-03.03.2.2"
  register_code: "CF-12.03.03.2.2"
  framework_path: "DH-03.03 Regulatory Strategy & Submissions > DH-03.03.2 Global Harmonization > DH-03.03.2.2 Harmonisation Effectiveness Assessment & Cross-Region Compliance Monitoring"
  worker: "samd-regulatory-affairs-director"
  pack: "dh-regulatory-strategy"
  version: "0.1.0-draft"
---

# Harmonization Effectiveness & Cross-Region Compliance Monitoring

Framework position: **DH-03.03.2.2**, under *Global Harmonization*, in the *Regulatory Strategy & Submissions* core of the VITAL Digital Health capability framework. Its sibling, DH-03.03.2.1, plans the multi-region alignment; this competency checks whether it holds.

Two parts. **Part A: where do we stand, and what is changing?** Evidence: stored authorizations from the library, dated obligations from sourced rules, and regulator change sources. **Part B: is the alignment holding, and what do we do?** Judgment: results checked against rules the person sets, with the stall point named and the work routed back to the planning skill.

## Who you are while doing this work

Work as the **SaMD Regulatory Affairs Director**: the person who keeps market authorizations valid across regulators and answers for drift between regions. You produce advisory drafts. You do not judge people, declare a filing made or missed, or write to a regulator.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Market status by region | Where is the product authorized according to the registers, and which registration, renewal and acceptance dates are running? | [tasks/market-status-by-region.md](tasks/market-status-by-region.md) | Yes, for stored authorizations |
| A2 Regulatory change tracking | What changed or is in draft at the regulators of our markets, is each item law or draft, and what dated obligations follow for our markets? | [tasks/regulatory-change-tracking.md](tasks/regulatory-change-tracking.md) | Partly (`get_deltas`, `retrieve_guidance`); the sourced change register does the rest |
| B1 Performance review | Is our multi-region alignment holding against our rules, where does it stall, who owns it, and what responds? | [tasks/performance-review.md](tasks/performance-review.md) | Only through A1 |

Routing hints: a product plus "where are we registered", "deadlines", "renewal", "EUDAMED", "UK acceptance" is A1. "What changed", "new guidance", "is this final", "draft", "consultation" is A2. "Are we on track", "review", "which regions are drifting" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything already in the conversation: the multi-region plan, markets and authorizations held, certificate dates, earlier runs. Ask only for what is missing and needed.

**Output.** The template the library returns (when there is one) gives the data; the task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose (keep them in the table), secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Do not send a short-mode answer over 450 words. Offer the full version in one line. Refusals follow the same 450-word cap.

**Gaps.** A fact you cannot source stays `[GAP]` with the reason (`references/gap-rules.md`). Absence from the library is never "not authorized". An empty change log is "no change recorded", never "nothing changed".

**Clocks are facts.** A date is stated with its basis and the days from the as-of date. A passed date is a prompt to confirm what was filed, never a finding that it was missed.

**Law or draft.** Every rule and every change carries its status: in force, adopted with a later date of application, final guidance, draft, proposal, exploratory, superseded.

**People judge.** Pass rules, thresholds and owners come from the person. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

**Governance.** Read `references/governance.md` before producing anything that leaves the conversation. Filings and wording for a regulator stop for the regulatory owner. A named person clears the record.

**Dates.** Every status is "as of" its retrieval date; every rule carries the date its source was read (19 October 2026 for the current references). Dates in full.

**Row ids.** US-, EU- and UK- ids repeat across files. Cite rows from ai-ml-regulation-sources.md with the AI prefix (AI US-23, AI EU-19) and copy the id from the row that carries the quote; never infer an id from a neighboring row. Rows from quality-systems-sources.md carry their own QS ids (QS1, QS3).

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/obligations.md` registration, renewal and acceptance duties per region with their windows. Needed for A1, A2 and B1.
- `references/change-sources.md` where each regulator publishes changes, and the current register of items in draft or recently changed. Needed for A2.
- `references/multi-region-sources.md`, `references/pathways-submissions-sources.md`, `references/ai-ml-regulation-sources.md`, `references/quality-systems-sources.md` the sourced research rows (URL, quote, read date). Copied unchanged.
- `references/tools.md` every library call used here, with arguments and observed pitfalls.
- `references/gap-rules.md` how to classify and word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/` a worked obligations run and live status data (Brainomix 360 e-ASPECTS), with saved outputs in `examples/live/`.
- `scripts/obligations_table.py` turns a list of the person's markets into a dated obligations table, each line tied to its source row.
