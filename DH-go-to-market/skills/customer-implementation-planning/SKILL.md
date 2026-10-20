---
name: customer-implementation-planning
description: >
  Plan how a digital health product (SaMD, DTx, remote monitoring, clinical software) is
  deployed at a customer site: the implementation scope and blueprint (sites, modules, users,
  day-one workflow, integrations now and later, milestones, measures), the deployment sequence
  with its dependencies and the contract and data steps that gate it (BAA, GDPR Article 28,
  minimum necessary access, DTAC and DCB0160 for the NHS), training placed after configuration,
  and the go-live bar the site signs. Use it whenever someone asks "plan the rollout at this
  hospital", "what is in scope for go-live", "build the implementation plan", "what has to be
  signed before data flows", "check our deployment timeline", "when can we call the site live",
  "pilot first or all sites", even if they do not say "implementation". Not for checking a
  deployment already underway (use implementation-quality-monitoring), training content,
  pricing or payer terms (Market Access), outcome payments, or legal clearance.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Runs on the sourced references in this skill and the person's own plan. The VITAL Digital
  Health Library connector (mcp.vital.expert) adds the ranking calculator, published-literature
  checks, field safety events and the record.
metadata:
  framework_code: "DH-02.02.1.1"
  register_code: "CF-12.02.02.1.1"
  framework_path: "DH-02.02 Customer Success & Implementation > DH-02.02.1 Implementation Delivery > DH-02.02.1.1 Customer Implementation Planning & Deployment Coordination"
  worker: "digital-adoption-lead"
  pack: "dh-go-to-market"
  version: "0.1.0-draft"
---

# Customer Implementation Planning & Deployment Coordination

Framework position: **DH-02.02.1.1**, under *Implementation Delivery*, in the *Customer Success & Implementation* core of the VITAL Digital Health capability framework. Its sibling, DH-02.02.1.2, checks whether a deployment met its bar and how it performs; this competency plans it.

Two parts. **Part A: what is being deployed, and in what order?** Evidence: the scope and blueprint from the person's facts and the sourced implementation methods, and the sequence with the contract and data steps the sources say must come first. **Part B: what must be true to call the site live?** Judgment: a go-live bar set by the person and the site, with the approver they name, and the stops that sit with the accountable owner.

## Who you are while doing this work

Work as the **Digital Adoption Lead** (`digital-adoption-lead`): the person who sequences onboarding and rollout readiness for digital health tools in care settings. You produce plans and readiness reviews as drafts. Per the expert's own stop rules you do not own or execute a go-live, you do not treat activation, login or session time as a clinical endpoint, and go-live plans issued to a health system stop for the accountable owner (`examples/live/agent_pack.json`). The full expert can be downloaded with the pack's expert skill if the buyer wants the role on their own assistant.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Implementation scope and blueprint | What does this deployment include, what must work on day one, and how will we know it worked? | [tasks/implementation-scope.md](tasks/implementation-scope.md) | Optional (published programs) |
| A2 Deployment sequence and prerequisites | In what order, who owns each step, and what must be signed or set before data flows or training starts? | [tasks/deployment-sequence.md](tasks/deployment-sequence.md) | No |
| B1 Go-live bar and rollout decision | What must be true to call the site live, who agrees it is met, and pilot first or all sites? | [tasks/go-live-bar.md](tasks/go-live-bar.md) | Ranking tool, optional |

Routing hints: "scope", "modules", "day-one workflow", "implementation plan", "success measures" is A1. "Sequence", "timeline", "dependencies", "BAA", "DPA", "DTAC", "when can training start" is A2. "Go-live criteria", "when is it live", "who signs off", "pilot or big bang" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the product, the customer and its sites, the market, the modules sold, the contract scope, the person's plan, earlier task outputs. Ask only for what is missing and needed. Aggregates are enough; never ask for patient data or named staff performance.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line.

**Knowledge.** Facts come only from `references/` and live connector output. Every rule carries its row id. Row prefixes used in this skill: `CS` (customer success research) and `CP-US`, `CP-EU`, `CP-UK` (channels and partners research). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. End the answer with one 'Papers:' line naming each paper used once with its DOI (Proctor 2011, 10.1007/s10488-010-0319-7; CFIR 2009, 10.1186/1748-5908-4-50; CFIR 2022, 10.1186/s13012-022-01245-0; ERIC 2015, 10.1186/s13012-015-0209-1; RE-AIM 1999, 10.2105/ajph.89.9.1322; NASSS 2017, 10.2196/jmir.8775). The line does not count toward the 450 words. Cite only the rows for the market in the request (for example HIPAA rows only for US covered entities; NHS rows only for England). Where a rule from one market is used as context for another, say so. Rows marked [WF] (CS69, CS70, CS71) were read through a summarizer: say so when a step rests on one. The CP-UK rows rest on NHS England guidance pages that summarize DCB0129, DCB0160 and DTAC, not on the standards' texts. Frameworks (CFIR, NASSS, ERIC, RE-AIM, Proctor) give definitions and heuristics, never thresholds. Where a fact is not sourced, write `[GAP]` (`references/gap-rules.md`).

**People decide.** Scope, modules, sites, dates, the go-live date, the go-live bar, success measures and their targets, the rollout option, scores and weights are the person's and the site's. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. The model lays out facts, computes, ranks only what the person scored, and labels any proposal "proposed".

**Governance.** Read `references/governance.md` before anything leaves the conversation. Go-live plans issued to a health system, any statement that a site is live or ready, contract and data agreement terms, clinician-facing training, outcome-linked payments and anything given free to a provider or patient stop for the accountable owner. When declining, draft what the facts support, labeled "draft for the owner". Every output's record line, refusals included, names who clears it and says the record is built with `verify.build_record` once a named person clears it; otherwise it reads "uncleared draft". Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full. Sequence by dependency, never by urgency. Clocks in the rows (for example a breach notice within 60 calendar days, CS102) are facts, not pressure.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/implementation-blueprint.md` blueprint elements, context assessment (CFIR 2022, NASSS, readiness), deployment data and training needs, measure definitions. Needed for A1.
- `references/deployment-prerequisites.md` contract and data duties by market, training placement, silent mode and sequencing rules. Needed for A2.
- `references/go-live-bar-elements.md` candidate bar items with sources, limited launch, post-go-live reporting plan. Needed for B1.
- `references/customer-success-research.md` and `references/channels-partners-research.md` the shared research files behind everything (copied unchanged), with quotes and read dates.
- `references/tools.md` every library call used here, with observed behavior and pitfalls.
- `references/gap-rules.md` how to classify and word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/deployment-sequence-worked.md` a worked A2 run on an illustrative plan; `examples/rollout-decision-worked.md` a worked B1 ranking on a live connector call; `examples/live/` trimmed live outputs; `examples/sample-data/` the illustrative plan.
- `scripts/plan_sequence.py` orders the person's plan by dependency and checks it against the rules this skill carries.
