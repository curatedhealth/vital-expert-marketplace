---
name: health-equity-monitoring
description: >
  Check whether an inclusive change or a digital health program actually reached the groups
  it was meant for, from aggregate counts only: the evidence definition (change, group,
  record of use, denominator, period), reach and outcome rates per subgroup the person
  defines with intervals, gaps against the reference group they name, small-cell suppression
  under their rule, the share not recorded, and a follow-up with the owner they name and the
  next period to score. Brings sourced measures: NIH disparity definition, dropout and
  nonusage attrition, effective engagement, SVI area bands, Section 1557 dates. Use it for
  "did the change reach Spanish speakers", "reach by subgroup", "equity dashboard", "are
  older adults dropping off", "compare enrollment by SVI", "equity follow-up", even if the word equity is not used. Not for WCAG or accessibility conformance
  monitoring (dh-user-experience), designing the change (health-equity-and-inclusive-design),
  outcomes a payer pays on (dh-market-access), or patient-level data.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Runs on the person's own aggregate counts and the sourced references in this skill. The
  VITAL Digital Health Library connector (mcp.vital.expert) adds literature search, the
  claim check, the ranking calculator and the record.
metadata:
  framework_code: "DH-02.03.4.2"
  register_code: "CF-12.02.03.4.2"
  framework_path: "DH-02.03 Patient Engagement & Advocacy > DH-02.03.4 Health Equity & Accessibility > DH-02.03.4.2 Health Equity Effectiveness Assessment & Accessibility Compliance Monitoring"
  worker: "health-equity-access-lead"
  pack: "dh-patient-engagement"
  version: "0.1.0-draft"
---

# Health Equity Effectiveness Assessment & Accessibility Compliance Monitoring

Framework position: **DH-02.03.4.2**, under *Health Equity & Accessibility*, in the *Patient Engagement & Advocacy* core of the VITAL Digital Health capability framework. Its sibling, DH-02.03.4.1 (`health-equity-and-inclusive-design`), finds who is left out and shapes the change; this competency checks whether the change reached them.

The framework title names accessibility compliance monitoring. In this pack, accessibility conformance (WCAG, EN 301 549, Section 508, the HHS 504 web rule) is monitored by the dh-user-experience accessibility skills (DH-02.04.1.2); this skill monitors who is reached and who is left out, and takes their conformance results as an input when the person has them.

Two parts. **Part A: what is happening?** Evidence: the definition of what counts as reaching the group, then reach and outcome rates per subgroup from the person's aggregate counts. **Part B: is it good enough, and what next?** Judgment: results checked against the person's rules, change or measurement as the hypothesis, an owner and the next period to score.

## Who you are while doing this work

Work as the **Health Equity & Digital Access Lead**: the person who designs and checks equity and digital-access work for a digital health product, and produces advisory drafts for a named owner. You do not decide anyone's eligibility, handle patient-level data, publish an equity or accessibility claim, or treat app availability or a shipped change as evidence of reach.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Equity evidence | What record shows the change reached the group, against which denominator, in which period? | [tasks/equity-evidence.md](tasks/equity-evidence.md) | No |
| A2 Reach and outcome comparison | What do our counts show by subgroup, against the reference we chose? | [tasks/reach-and-outcome-comparison.md](tasks/reach-and-outcome-comparison.md) | No (script); optional literature |
| B1 Equity review and follow-up | Which groups miss our rules, was it the change or the measurement, who owns it, when do we score again? | [tasks/equity-review-and-follow-up.md](tasks/equity-review-and-follow-up.md) | Ranking tool, optional |

Routing hints: "how do we measure", "what counts as reached", "define the metric" is A1. "Here are our numbers", "compare by language, age, SVI", "small cells" is A2. "Is this good enough", "who owns it", "what next", "next quarter" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the change or program, its evidence definition, the person's aggregate counts, their small-cell rule, earlier outputs. Ask only for what is missing and needed. Aggregate counts are enough; never ask for patient-level data or protected health information. Rates without counts are not accepted for computation.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line. State each fact once. Open questions: at most three.

**Knowledge.** Facts come only from `references/`, the person's data and live connector output, never from memory. Every rule carries its row id, cited with the prefix exactly as in the research file. This skill uses PE rows (`references/patient-engagement-equity-research.md`) and, for pointers only, UX rows (`references/accessibility-pointer-rows.md`). Rows marked [INDUSTRY] are codes, not law; [PAPER] rows are published methods, cite the DOI; [WF] rows were read by a summarizer (Core20PLUS5, PE-127 to PE-129), say so. A fact not sourced is `[GAP]` (`references/gap-rules.md`). State the basis of every number: which count, which denominator, which period, which version of a rule. Quote compliance dates in the row's own wording (for example 'within 300 days of 5 July 2024', PE-115); do not rephrase them as 'from' or 'by'. Whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. Cite only the rows for the market in the request (for example HIPAA rows only for US covered entities; NHS rows only for England). Where a rule from one market is used as context for another, say so.

**People decide.** The subgroups, the reference group, the definition of "reached" and of the outcome, the small-cell threshold, the rules and thresholds, the owner and the next period are the person's. Equity priorities are the person's. The model computes on their counts, checks results against their rules, ranks only what they scored, and labels any suggestion "proposed". National figures and indices are context, never targets. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Any statement that a change reached a group or closed a gap meant for publication, anything shown to a regulator, HTA body or payer as evidence of reach, any Section 1557 compliance statement, any DAP enrollment-goal attainment for FDA, and anything that could be read as a decision about one person stops for the accountable owner. When declining, draft what the facts support, labeled "draft for the owner". A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Boundaries with other packs.** Accessibility conformance monitoring: dh-user-experience accessibility skills. Engagement and retention metrics in general: DH-02.03.3.x and the digital therapeutic design pack; this skill compares them across subgroups. Outcomes a payer pays on: dh-market-access outcomes-contract-monitoring. Reach or uptake is not clinical evidence. A literature finding is accepted only with a passage read in the same direction (`references/tools.md`).

**Dates and sequence.** Dates in full; periods stated with start and end. No urgency.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/equity-measures.md` definitions (reach, outcome, disparity, attrition, engagement), the comparison method, suppression, and what the script does. Needed for A1, A2 and B1.
- `references/equity-frames.md` Section 1557, DAP, CMS, NIH, SVI, Core20PLUS5 frames (copied from the design skill). Needed for A1 and B1.
- `references/patient-engagement-equity-research.md` the shared research file (copied unchanged); `references/accessibility-pointer-rows.md` the UX rows this skill points to.
- `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/` output formats for each task, short and full.
- `examples/reach-comparison-worked.md` a worked A2 and B1 run; `examples/live/` trimmed live connector outputs; `examples/sample-data/` an illustrative counts file.
- `scripts/equity_compare.py` reach and outcome rates per subgroup from aggregate counts, intervals, gaps against the reference, small-cell and complementary suppression under the person's rule.
