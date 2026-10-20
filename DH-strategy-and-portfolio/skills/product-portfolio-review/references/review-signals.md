# Review signals for a product portfolio forum

Interpretive reference. Every rule cites its row in `strategy-and-portfolio-sources.md` (SP rows, read 20 October 2026) or the old skill's method (register codes CF-12.01.03.3.2.1 to .3). Rows marked [PAPER] carry their DOI; rows marked [WF] were read through a summarizer and are said to be so whenever applied. No source sets a decision-quality score, a benefits realization rate or a target: those are the person's.

## 1. The pass rule for an auditable decision

The old method (CF-12.01.03.3.2.1, "Decision quality check"):
- "A pass has the rule, the rank, the decision, and the person."
- "A fail is a continue with no rule, or a stop with no record."
- "Do not pass a decision that lives only in a slide."
- Name the forum to be scored.

This is offered as the default pass rule; the person confirms it, changes it or writes their own. A decision that carries all four in a record (minutes, a decision register, a signed paper) passes; a decision recorded only in a slide or a deck fails on that ground. Each decision is reported on its own; no score is averaged across decisions.

What the review adds from the sources, as questions to the person, not as pass conditions unless they adopt them:
- Was validation built into each step and reported (SP-075, [PAPER] [WF], DOI 10.1016/j.jval.2015.12.016)?
- Were preferences elicited more than once or results presented back for confirmation (SP-081, [PAPER] [WF], same DOI)?
- Were criteria complete and free of double counting (SP-076, SP-077, [PAPER] [WF], same DOI)?
- Was the rule written before the rank? The sibling skill's method: "Do not change the rule after you see the rank you prefer" (CF-12.01.03.3.1.2). A rule dated after the forum cannot be used to score it.

## 2. Reading decisions against the rule (forum score)

The old method (CF-12.01.03.3.2.2, "Forum score"): read each decision against the rule; mark match or drift; note a continue that exceeded the named capacity; "Do not rescore the rule to match what was decided."

In this skill:
- **Recompute**, do not trust a recorded rank: value = 25 x sum of weight x 0 to 4 score, the EVIDEM weighted sum the library's `analytics.mcda` returns (`tools.md`). A recorded rank that differs from the recomputed rank is a finding in its own right.
- **Match**: the recorded decision is what the person's decision rule implies. **Drift**: a continue the rule does not imply ("continue beyond the rule") or a stop or delay where the rule implies continue ("held back against the rule"). Where the rule does not say whether a non-continue item is stopped or delayed, either counts as a match and the output says the rule is silent.
- **Capacity**: continue items summed in rank order against the capacity the person named, in their unit and period; the first continue item past it is named.
- A drift is a reading against the rule as written. It may be right: the forum may have had a reason. The reason is the person's, recorded in B1.

## 3. Benefits against the person's plan (UK public-sector guidance, applied by analogy)

The UK benefits guidance is written for government major projects. When used for a company, label it "UK public-sector guidance, applied by analogy".
- Benefits management "spans five different interrelated stages": "identification, valuation, planning, realisation and review" (SP-100, verbatim, UK spelling kept; Assurance of Benefits Realisation in Major Projects v2.1, August 2026, NISTA, SP-099).
- By the full business case, the plan "select[s] which benefits the project team will concentrate on realising; allocat[es] responsibility for delivering each benefit; and determin[es] the best metric for tracking progress" (SP-102).
- A benefits register lists each benefit with "a short description, the objective the benefit links/contributes to, the Benefit Owner, the beneficiaries, the baseline, target and measurement methodology" (SP-104; Benefits Measurement Guidance Note, May 2021, written for commercial benefits). These fields are what `scripts/forum_check.py benefits` checks for.
- Benefits reports compare baseline, target and actuals; the guidance sets a first review at 12 months of contract delivery and at least every 12 months after, on a "comply or explain" basis (SP-105). For a company, the review date is the person's.
- "No project which fails to deliver what is planned of it can ever be considered a success, no matter how cheap or fast" (SP-103). Quoted as the guidance's stance; whether an item succeeded is the person's call against their own plan.
- A benefits management collection (quick guide, practitioner workbook, templates aligned to the Teal Book, case studies) was published on 30 July 2026 (SP-106, [WF]).

The share of planned change achieved is (actual minus baseline) divided by (target minus baseline). Without the person's threshold it is a number, not a verdict.

## 4. Appraisal against evaluation

Green Book 2026 (HM Treasury, 5 February 2026; earlier editions withdrawn, SP-088), UK public-sector guidance:
- Appraisal is before approval; evaluation is after implementation (Magenta Book), and evaluation is planned from the outset (SP-090). A forum review of decisions taken is closer to evaluation; it reads what the appraisal (the prioritization) assumed against what happened.
- ROAMEF: rationale, objectives, appraisal, monitoring, evaluation and feedback (SP-091). The repair in B1 is the feedback step: it names where the correction shows.
- SMART objectives: "specific, measurable, achievable, realistic, and time-limited" (SP-092). A benefit with no measure or no review date cannot be read; say so.
- Optimism bias: appraisals adjust by increasing costs and timeframes and decreasing benefits (SP-096). If continue items run late or under their benefits, the person may ask whether the rule's inputs carried an adjustment. The Green Book 2026 points to generic values where a body has no historical evidence of its own (SP-171). HM Treasury's supplementary guidance (gov.uk page of 21 April 2013, not withdrawn; a 2003 document on 2002 data, SP-170) puts software, systems and ICT development under "equipment/development" (SP-173), with upper and lower bounds of 54% and 10% on works duration and 200% and 10% on capital expenditure (SP-172). The upper bounds are average historic bias at outline business case stage and "indicative starting values" (SP-174), reduced by a mitigation factor between 0.0 and 1.0 per factor managed (SP-175). There are no sound bounds for operating costs or benefits shortfall; the guidance says to use sensitivity analysis and switching values instead (SP-176). A review compares what the person's rule assumed with what happened; it never applies these values to the person's items unless the person chooses to, and then the adjustment is labeled theirs.

## 5. Scorecards: what the evidence says and does not say

If the person's forum uses a balanced scorecard, two systematic reviews set its limits: studies focus on design more than use or review, with "no agreement about the perspectives to be adopted in healthcare" (SP-107, [PAPER], DOI 10.3390/ijerph191610291); 20 studies showed positive outcomes for patient satisfaction and financial performance and a mild effect on staff satisfaction, with many at high risk of bias (SP-108, [PAPER], DOI 10.1186/s12913-021-07452-7). These describe healthcare organizations, not product portfolio forums: context only.

## 6. Dated changes that can touch reviewed items

Signals to check since the forum date, each with its instrument and date. A change is a signal for the person to weigh, never a verdict that a decision is wrong.

| Change | Date | Rows | Which items it can touch |
|---|---|---|---|
| EU TTBER 316/2014 expired; Regulation (EU) 2026/877 in force | 30 April 2026; 1 May 2026 | SP-134, SP-135 | Licensed or partnered items |
| TTBER transition for agreements in force on 30 April 2026 that met the old rules but not the new | ends 30 April 2027 | SP-137 | Licensed items signed before 1 May 2026 |
| New Technology Transfer Guidelines (C/2026/2323) | OJ 21 April 2026 | SP-141 | Licensed items, data licensing (SP-142) |
| Green Book 2026 edition; earlier editions withdrawn | 5 February 2026 | SP-088 | Any rule that cites the Green Book |
| FDA TAP expanded to all OHTs for Breakthrough and STeP devices | 1 July 2026 | SP-122 | Items delayed pending FDA interaction |
| CMS and FDA RAPID coverage pathway announced | 23 April 2026 | SP-123 | Breakthrough-designated items; coverage routes to `dh-access-and-value` coverage-pathway-and-access-strategy |
| MHRA IDAP pilot closed to new applicants | as read 20 October 2026 | SP-124 | UK items that planned on IDAP |
| EHDS general application | 26 March 2027 (most duties 2029 and 2031) | SP-068 to SP-071 | Items using EU health data |
| WHO Global Strategy on Digital Health extended to 2027 | WHA78, 27 May 2025 | SP-066 | Rules that cite the WHO strategy |

For a named counterparty (licensor, partner), check its company status (`licensing-and-deal-flags.md` section 3). The library change log began 12 October 2026; a period before then is not covered by `get_deltas` (`tools.md`).

## 7. Repair (old method)

The old method (CF-12.01.03.3.2.3, "Governance repair"): name whether the rule or the decision is corrected; name the owner; name the next forum that must show the correction; "Do not leave both the rule and a contradicting decision in force." In B1 these are the person's choices; the model lays out the options and what each would mean, labeled "proposed".
