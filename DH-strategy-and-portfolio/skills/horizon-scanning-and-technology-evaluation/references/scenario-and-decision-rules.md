# Scenarios, implications and the person's choice

Interpretive reference for task B1. Rows: SP (`strategy-and-portfolio-sources.md`). [PAPER] rows carry their DOI in every table cell; [WF] rows are flagged each time.

## 1. Scenarios are built on the person's drivers

No source in this skill sets a scenario method (SP research, "Not sourced": no WHO or OECD method document). The structure below is therefore "proposed" and the person may replace it.

- **Drivers and their states** come from the person. If they name none, the skill proposes drivers drawn from A1 signals (for example "EU AI Act high-risk date for Annex I devices", EU-19), each labeled "proposed driver" with its signal id.
- **Each assumption** in a scenario is tied to a signal id from A1 or marked "your assumption". An assumption with neither is removed.
- **What would be observed** if the scenario were unfolding: name the record type that would show it (a clearance under a product code, an Official Journal act, a trial registration). These become the watch items for `foresight-signal-monitoring` (this pack).
- **No probabilities, no dates of arrival, no market sizes** from the model. Scenarios are not ranked by likelihood unless the person scores likelihood; then the ranking is their scores, computed.

## 2. Implications and disruption: against the person's current play

- The current play is stated by the person (product, market, timing, partner). If not stated: "current play not given `[GAP]`"; no implication is written.
- **Strategic implication** per scenario: which part of the play a scenario would touch (evidence plan, pathway, data access, partner, timing), with the signal ids behind it. Phrased as "would touch", never "will".
- **Disruption assessment** (old task DH-01.08.4.1.3): which signals, if confirmed, would change the play, by the person's own criteria for "disruptive". No source defines a disruption index; the model never scores disruption.

## 3. Benchmarks are context, never targets

| Benchmark | What it measured, by which method | Row |
|---|---|---|
| 13.8% of drug development programs reached approval | 406,038 trial entries, 2000 to 2015, "path-by-path" method ([PAPER] Wong, Siah and Lo 2019, DOI 10.1093/biostatistics/kxx069) | SP-082, SP-085 |
| Oncology 3.4% in the sample versus 5.1% in prior studies | Same paper and method ([PAPER] DOI 10.1093/biostatistics/kxx069) | SP-083 |
| Trials using biomarkers for selection had higher success probabilities | Same paper ([PAPER] DOI 10.1093/biostatistics/kxx069) | SP-084 |
| Oncology and immunology studies averaged 3.9 years | Top 30 pharma, ClinicalTrials.gov, 2000 to 2020 ([PAPER] Büssgen and Büssgen 2023, DOI 10.1186/s40545-023-00612-6) | SP-086 |
| Higher phases correlated with longer studies | Same paper ([PAPER] DOI 10.1186/s40545-023-00612-6) | SP-087 |

Rules:
- These are drug development figures. No source gives success rates for digital health products, software devices or AI tools: write "no digital health success rate in the sources `[GAP]`".
- Quote a figure only with its counting method, dataset and row. Never present it as the person's probability, never apply it to the person's technology, and never mix path-by-path and phase-by-phase figures in one model (SP-085).
- If the person asks to "use 13.8% as our probability", say what the figure counts, decline to set it as theirs, and offer to run `analytics.scenario-modeler` with a probability the person states, labeled as theirs.

## 4. Ranking the person's options (MCDA rules)

ISPOR MCDA task force, Report 2 ([PAPER] Marsh 2016, DOI 10.1016/j.jval.2015.12.016, [WF]: read through a summarizer):
- Eight steps: define the problem, select and structure criteria, measure performance, score, weight, aggregate, deal with uncertainty, report and examine (SP-074).
- Build validation into each step and report it (SP-075); test consistency, for example by eliciting preferences more than once and presenting results back (SP-081).
- MCDA helps decision makers reach their own decision, not the tool's (SP-080).
- Criteria should capture all factors relevant to the decision (SP-076). Before ranking, ask whether the person's criteria cover every factor they care about. Where an option is a license from a competitor, name dependency on the licensor as a factor the person may want to score, labeled "proposed"; the score is theirs.

How the skill applies them: the person defines the problem, criteria, weights and scores; `analytics.mcda` aggregates (EVIDEM weighted sum on 0 to 4 scores, `tools.md`); `scripts/horizon_helpers.py swap` recomputes, checks the tool and shows where adjacent options swap (the uncertainty step); the result is "your scores, ranked", never a choice. Any statement of what would change the order is computed, never estimated: quote the swap weights the script prints, or show the arithmetic on the person's scores (for example "License 2.60 x 25 = 65; Watch 2.00 x 25 = 50"). `analytics.rice` is a calculator the person may choose; its method citation is a vendor article, not a sourced rule (`tools.md`).

## 5. UK public-sector appraisal terms (label them when used for a company)

The Green Book 2026 (HM Treasury, updated 5 February 2026, earlier editions withdrawn, SP-088) is UK government guidance. When a company uses its terms, say "UK public-sector guidance, applied here by your choice".

| Term | As the Green Book states it | Row |
|---|---|---|
| Appraisal | Assessing costs, benefits and risks of options for achieving objectives; before approval | SP-089, SP-090 |
| ROAMEF | Rationale, objectives, appraisal, monitoring, evaluation, feedback | SP-091 |
| SMART objective | Specific, measurable, achievable, realistic, time-limited | SP-092 |
| Business as usual | The outcome expected if current arrangements continue | SP-093 |
| Longlist to shortlist | A wide longlist, assessed against objectives and critical success factors, then a shortlist and a "preferred way forward"; the options framework filter is recommended, not mandated | SP-094, SP-095 |
| Optimism bias | Appraisals adjust explicitly: raise costs and timeframes, lower benefits | SP-096 |
| Five Case Model | Strategic, economic, commercial, financial and management cases | SP-097 |

Including a business-as-usual option in B1 is "proposed" (SP-093), never imposed.

### Optimism bias values (UK public-sector guidance; context, never the person's number)

The Green Book 2026 says that a public body without its own evidence on historical optimism bias can use the generic values in HM Treasury's supplementary guidance (Green Book 2026, SP-171). That guidance page dates from 21 April 2013, is not withdrawn, and the document itself dates from 2003 and rests on a 2002 Mott MacDonald review (HM Treasury optimism bias guidance, SP-170). Say all three facts whenever a value is quoted.

| Project type (as the guidance names it) | Works duration upper / lower (%) | Capital expenditure upper / lower (%) | Row |
|---|---|---|---|
| Standard buildings | 4 / 1 | 24 / 2 | SP-172 |
| Non-standard buildings | 39 / 2 | 51 / 4 | SP-172 |
| Standard civil engineering | 20 / 1 | 44 / 3 | SP-172 |
| Non-standard civil engineering | 25 / 3 | 66 / 6 | SP-172 |
| Equipment/development (includes software, systems and ICT development, SP-173) | 54 / 10 | 200 / 10 | SP-172, SP-173 |
| Outsourcing | n/a | 41 / 0 (operating expenditure) | SP-172 |

Rules:
- The upper bounds are the average historic bias at outline business case stage for traditionally procured projects; they are "indicative starting values", not extremes (SP-174).
- Method as stated: start at the upper bound, reduce it by a mitigation factor between 0.0 and 1.0 for each contributory factor managed, aiming for the lower bound by contract award (SP-175). The mitigation factors are the person's.
- No sound bounds exist for operating costs (except outsourcing) or for benefits shortfall; the guidance says to use sensitivity analysis and switching values instead (SP-176). That is `analytics.risk-tornado` and the swap points on the person's numbers.
- For a company these are UK public-sector values applied by the person's choice. The model never applies an uplift on its own; any adjusted figure is "computed on your inputs" with the arithmetic shown (for example "your cost 1.0 million x (1 + 2.00) = 3.0 million at the equipment/development upper bound, SP-172").

## 6. Sensitivity on the person's numbers

- `analytics.scenario-modeler` computes a formula over the person's parameters per period; `analytics.risk-tornado` varies each parameter one at a time (`tools.md`).
- Pass the person's ranges for every parameter; the tornado's default is plus or minus 20 percent, which is not theirs. List parameters are skipped by the tornado. Do not tornado a ratio (`scripts/horizon_helpers.py tornado-check`).
- Every output is "computed on your inputs"; none is a forecast.

## 7. Options that involve a partner, a license or a deal

Facts to flag for the owner the person names for legal matters, or owner not named. Never write that a license is exempt, safe or lawful.

**Thresholds side by side, without leaning.** When a market-share threshold applies, put the threshold as the source states it next to the person's own figure, and stop: "TTBER 2026 threshold for competitors: combined share up to 20% on any relevant market (Regulation (EU) 2026/877, SP-136). Your figure: [as given, or not given]. For your legal owner." The same for the DOJ and FTC safety zone (20% of each relevant market significantly affected, SP-144) and the R&D-market test (four or more independent entities, SP-145). Never say which side of the line the person is on, and never compute a market share for them; market definition is the legal owner's.

**Every flag the rows support.** Flag all that apply, not only the competition facts: a license that includes data (TTBER can apply to data licensing where the data qualifies as a technology right, SP-142); training or validation data that are health data (GDPR Article 4(15), DL-099; Article 9(1) prohibition unless an Article 9(2) ground applies, DL-101 (inference); a DPIA for large-scale special-category processing, Article 35(3)(b), DL-106); a material contract a public partner may have to file (SP-130 to SP-133).

| Fact | Rows |
|---|---|
| EU TTBER 316/2014 expired 30 April 2026; Regulation (EU) 2026/877 in force 1 May 2026, expires 30 April 2038 | SP-134, SP-135 |
| TTBER 2026 thresholds: combined share up to 20% for competitors; each party up to 30% for non-competitors, on any relevant market | SP-136 |
| Transition to 30 April 2027 for agreements in force on 30 April 2026 that met the old rules | SP-137 |
| Restricting a party's own R&D is hardcore for competitors unless indispensable to protect licensed know-how; technology pools are outside the regulation | SP-139, SP-140 |
| 2026 Guidelines (C/2026/2323) replace the 2014 Guidelines and add data licensing guidance | SP-141, SP-142 |
| US DOJ and FTC IP licensing guidelines (12 January 2017): no presumption of market power; safety zone at 20% of each affected market; R&D markets need four or more independent entities; outside the zone is not presumed unlawful | SP-143 to SP-147 |
| A public company files material contracts, including licenses its business depends on, as exhibits; redaction rules apply | SP-130 to SP-133 |

Partnership design routes to `dh-go-to-market` channel-and-partner-design. Questions about investing in or acquiring a company route to `market-and-target-screening`, `company-and-evidence-assessment` or `investment-memo-and-decision-record` (this pack).
