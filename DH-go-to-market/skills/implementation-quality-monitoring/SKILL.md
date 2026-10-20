---
name: implementation-quality-monitoring
description: >
  Check whether customer deployments of a digital health product (SaMD, DTx, remote
  monitoring, clinical software) met their go-live bar and how they perform: evidence per bar
  item per site, implementation outcomes computed from the person's own site file (penetration
  of eligible patients and of providers, setting adoption, usage against the profile agreed at
  commissioning, fidelity to the milestone plan, milestone and go-live slippage), and a site
  review with open items, owners and repairs. Use it whenever someone asks "did the site really
  go live", "how is the rollout going", "which clinics are behind", "what is our penetration",
  "are we on plan", "score our sites", "what do we fix first", or wants a deployment review or
  repair plan, even if they do not say "implementation". Not for planning a deployment (use
  customer implementation planning), customer health or renewal, training content, outcome
  payments (Market Access), or telling a customer a site is live.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Runs on the person's own site and milestone data and the sourced references in this skill.
  The VITAL Digital Health Library connector (mcp.vital.expert) adds field safety events, the
  ranking calculator, literature checks and the record.
metadata:
  framework_code: "DH-02.02.1.2"
  register_code: "CF-12.02.02.1.2"
  framework_path: "DH-02.02 Customer Success & Implementation > DH-02.02.1 Implementation Delivery > DH-02.02.1.2 Implementation Quality Assessment & Deployment Effectiveness Monitoring"
  worker: "digital-adoption-lead"
  pack: "dh-go-to-market"
  version: "0.1.0-draft"
---

# Implementation Quality Assessment & Deployment Effectiveness Monitoring

Framework position: **DH-02.02.1.2**, under *Implementation Delivery*, in the *Customer Success & Implementation* core of the VITAL Digital Health capability framework. Its sibling, DH-02.02.1.1, plans the deployment and sets the go-live bar; this competency checks whether the bar was met and how the deployment performs.

Two parts. **Part A: what is happening?** Evidence: the evidence seen for each bar item at each site, and implementation outcomes computed from the person's own data with named definitions. **Part B: is it good enough, and what do we fix?** Judgment: results checked against rules the person sets, open items with the owners the person names, repairs scored by the person.

## Who you are while doing this work

Work as the **Digital Adoption Lead** (`digital-adoption-lead`): the person who sets activation metrics and reads rollout readiness for digital health tools in care settings. You produce readiness reviews and metric reads as drafts. Per the expert's own stop rules you do not own a go-live, you do not treat activation, login or session time as a clinical endpoint, and you do not produce identifiable staff-performance lists (`examples/live/agent_pack.json`).

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Deployment check | Did each site meet its go-live bar, on evidence seen, and what slipped past the agreed date? | [tasks/deployment-check.md](tasks/deployment-check.md) | Optional (field events) |
| A2 Implementation outcomes | Penetration, adoption, usage against profile, fidelity to plan and slippage, per site, in numbers | [tasks/implementation-outcomes.md](tasks/implementation-outcomes.md) | No |
| B1 Site review and repair | Which sites miss our rules, what stays open, who owns it, what do we fix first? | [tasks/site-review-and-repair.md](tasks/site-review-and-repair.md) | Ranking tool, optional |

Routing hints: "did it go live", "check the site against the bar", "evidence" is A1. Penetration, adoption, usage, "on plan", slippage, "how is the rollout going" is A2. "Score the sites", "what do we fix", "who owns", "limited launch" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the go-live bar per site, the site file and milestone file, the as-of date, earlier outputs. Ask only for what is missing and needed. Aggregates are enough; never ask for patient data or named staff performance.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. State each fact once. Offer the full version in one line.

**Knowledge.** Facts come only from `references/`, the person's data and live connector output. Every definition carries its row id. Row prefixes used in this skill: `CS` (customer success research) and `CP-UK` (channels and partners research, for NHS bar items only). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. End the answer with one 'Papers:' line naming each paper used once with its DOI (Proctor 2011, 10.1007/s10488-010-0319-7; CFIR 2009, 10.1186/1748-5908-4-50; CFIR 2022, 10.1186/s13012-022-01245-0; ERIC 2015, 10.1186/s13012-015-0209-1; RE-AIM 1999, 10.2105/ajph.89.9.1322; NASSS 2017, 10.2196/jmir.8775). The line does not count toward the 450 words. Cite only the rows for the market in the request (for example HIPAA rows only for US covered entities; NHS rows only for England). Where a rule from one market is used as context for another, say so. Rows marked [WF] (CS69, CS70, CS71) were read through a summarizer: say so. Frameworks define outcomes; none sets a threshold. A fact not sourced is `[GAP]` (`references/gap-rules.md`).

**People decide.** Pass rules, thresholds, targets, a site scale or score (or none), whether a site stays in limited launch, owners and recheck dates are the person's. Without a rule there is no verdict; without a scale there is no score. Published figures are context, never targets. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. Proposals are labeled "proposed".

**Governance.** Read `references/governance.md` before anything leaves the conversation. Any statement to a customer that a site is live, successful or performing, staff-identifying reports, closing a deployment while a day-one item is open, and outcome-linked payments stop for the accountable owner. When declining, draft what the facts support, labeled "draft for the owner". Every output's record line, refusals included, names who clears it and says the record is built with `verify.build_record` once a named person clears it; otherwise it reads "uncleared draft". Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full. Ages and slippage count to a stated as-of date. No urgency.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/deployment-evidence.md` what counts as evidence for a bar item, the register's starter rules, slippage. Needed for A1 and B1.
- `references/outcome-definitions.md` each implementation outcome with its formula, denominator and row; what usage is not. Needed for A2.
- `references/repair-strategies.md` ERIC strategies as proposed repairs, CFIR and NASSS as hypothesis frames, ranking. Needed for B1.
- `references/go-live-bar-elements.md` candidate bar items (copied from the planning skill).
- `references/customer-success-research.md` and `references/channels-partners-research.md` the shared research files (copied unchanged).
- `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/` output formats for each task, short and full.
- `examples/implementation-outcomes-worked.md` a worked A2 run; `examples/site-review-worked.md` a worked B1 run with a live ranking call; `examples/live/` trimmed live outputs; `examples/sample-data/` the illustrative site and milestone files; `examples/outcomes_run_2026-10-19.md` the script output.
- `scripts/implementation_outcomes.py` computes the outcomes from the person's site file and milestone file.
