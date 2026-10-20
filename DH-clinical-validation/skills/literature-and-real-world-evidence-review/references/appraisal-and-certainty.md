# Appraisal, synthesis and certainty

Interpretive reference. ES rows are in `EVIDENCE_SYNTHESIS_METHODS.md`, read 19 October 2026; section 15 rows (ES-171 to ES-234) read 20 October 2026. Every judgment named here (risk of bias, pooling, certainty) is the reviewers'. The model lays out the tool, the domains and the evidence for each, and labels any proposal "proposed".

## 1. Pick the risk-of-bias tool by design and by target body

| Study design (checked against the paper) | Cochrane-style review | EU JCA dossier |
|---|---|---|
| Individually randomized parallel-group trial | RoB 2, version of 22 August 2019 (ES-69) | Cochrane RoB 1, per outcome in scope (ES-163) |
| Cluster or crossover randomized trial | RoB 2 variants exist (ES-69) | RoB 1 (ES-163) |
| Comparative non-randomized study (cohort, controlled before-after) | ROBINS-I 2016 (ES-75 [PAPER] doi 10.1136/bmj.i4919) | ROBINS-I, per outcome (ES-164) |
| Uncontrolled before-after (single pre and post) | Usually serious or critical risk of bias (ES-78) | `[GAP]` in the rows read |
| Systematic review | Not a risk-of-bias tool question: see AMSTAR 2 in `evidence-quality-and-signal-monitoring` | |

Conflict, stated in the research file: Cochrane uses RoB 2 while the HTACG validity guidance (adopted 19 September 2024) asks for RoB 1 for RCTs. A JCA dossier should be ready to present RoB 1; a Cochrane-style review uses RoB 2, which remains Cochrane's current tool (ES-69). RoB 1 domains, levels and criteria are in section 2a, sourced from Handbook version 5.1.0 chapter 8 and Higgins et al. 2011 (ES-171 to ES-193).

## 2. RoB 2 in brief

- Unit: a specific result, not a whole trial (ES-70).
- Five domains: randomization process; deviations from intended interventions; missing outcome data; measurement of the outcome; selection of the reported result (ES-71).
- Signalling answers: Yes, Probably yes, Probably no, No, No information (ES-72).
- Domain and overall levels: Low risk of bias, Some concerns, High risk of bias; the algorithm proposes, reviewers may override with justification (ES-73).
- Overall: the least favorable domain; several "some concerns" can add up to high (ES-74).

For digital interventions, the passages reviewers usually need are the ones on blinding of an app comparator, adherence and deviations, and missing data from drop-out; give the reviewers the exact passages and locators, not a judgment.

## 2a. RoB 1 for an EU JCA

Source: Cochrane Handbook version 5.1.0 (updated March 2011) chapter 8, and Higgins et al. BMJ 2011;343:d5928 (ES-177 to ES-179, ES-189 to ES-193 [PAPER] doi 10.1136/bmj.d5928). Use it only where the target body asks for it (ES-163); it is the earlier Cochrane tool.

- Two parts per entry: a description of what happened, with verbatim quotes where appropriate and an explicit statement when no information is available; then a judgment of Low, High or Unclear risk (ES-172, ES-174, ES-189). "Probably done" or "Probably not done" may supplement an ambiguous quote, with the rationale (ES-175).
- Judgments concern material bias. Insufficient detail usually means Unclear; so does a known event with unknown risk, or an entry not relevant to the study (ES-176).
- Seven domains (ES-171). Sequence generation, allocation concealment and selective reporting take one entry per study; the two blinding domains and incomplete outcome data may need one per outcome; other bias uses pre-specified entries, only exceptionally (ES-173, ES-188, ES-193).

| Domain | Low | High | Unclear |
|---|---|---|---|
| Random sequence generation | A random component is described (random number table, computer generator, coin, cards or envelopes, dice, lots, minimization) (ES-180) | Non-random rule (date of birth, admission date, record number) or allocation by judgment or preference (ES-181) | Insufficient information (ES-181) |
| Allocation concealment | Central allocation, identical numbered containers, or sequentially numbered opaque sealed envelopes (ES-182) | Open schedule, unsafeguarded envelopes, alternation, date of birth, record number (ES-182) | Method not described in enough detail (ES-182) |
| Blinding of participants and personnel | Blinding ensured, or no blinding but the outcome is not likely influenced (ES-183) | No or broken blinding and the outcome is likely influenced (ES-183) | Insufficient information, or the study did not address the outcome (ES-183) |
| Blinding of outcome assessment | Assessment blinded, or not blinded but measurement unlikely to be influenced (ES-184) | Not blinded and measurement likely influenced (ES-184) | Insufficient information (ES-176) |
| Incomplete outcome data | No missing data, reasons unrelated to outcome, balanced missingness, impact not clinically relevant, or appropriate imputation (ES-185) | Outcome-related reasons with imbalance, clinically relevant impact, as-treated analysis with substantial departure, inappropriate simple imputation (ES-185) | Attrition or exclusions reported too poorly to judge (ES-185) |
| Selective reporting | Protocol available and all pre-specified outcomes of interest reported as planned (ES-186) | Pre-specified primary outcomes missing, changed or added, or outcomes reported too incompletely to meta-analyze (ES-186) | Insufficient information; expected for most studies (ES-186) |
| Other bias | Apparently free of other bias (ES-187) | At least one important risk, for example a design-specific bias or a claim of fraud (ES-187) | Insufficient information or rationale that a problem will introduce bias (ES-187) |

Summary per outcome: Low if all key domains are low; Unclear if low or unclear for all key domains; High if any key domain is high. Across trials, it depends on the share of information from high-risk trials (ES-192 [PAPER] doi 10.1136/bmj.d5928). Two people judge independently, discrepancies resolved first by discussion (ES-190). Do not use quality scales or scores (ES-191). Which domains are key, and every judgment, are the reviewers'.

## 3. ROBINS-I in brief

- Seven domains: confounding and selection of participants (pre-intervention); classification of interventions; deviations, missing data, measurement of outcomes, selection of the reported result (ES-75 [PAPER] doi 10.1136/bmj.i4919).
- Levels: Low (comparable to a well-performed randomized trial), Moderate, Serious, Critical, No information (ES-76).
- A study at critical risk in any domain should not be included in any synthesis (ES-77).
- Low risk for confounding is exceptional (ES-79).
- ROBINS-I V2 (November 2025 release) is still a draft and covers cohort studies; it adds algorithms, a triage section and immortal-time questions and drops the deviations domain (ES-80, ES-81, ES-82). The 2016 version is the published tool and the one HTACG cites (research "Changes and conflicts").

## 4. Retracted and corrected papers

- Examine retraction notices and errata for new and already-included studies (MECIR C48, mandatory) (ES-119); at update, re-search MEDLINE and Embase for the latest version (ES-120).
- Errata correct errors that do not invalidate conclusions; retractions follow COPE (ES-121). COPE guidance version 3 (August 2025) is a [WF] row: editors may retract when they no longer have confidence in the results, and use an expression of concern while deciding (ES-125).
- Do not discard "comments" unread (ES-122); retracted status is displayed inconsistently (ES-123); search "expression of concern" as a phrase before 2018 (ES-124).
- IQWiG may flag untrustworthy studies and test their influence by sensitivity analysis (ES-144).
- The library checks Crossref only (`tools.md`); a "none" is "none in Crossref as of the date", not proof.

## 5. Pool or not

- A systematic review need not contain a meta-analysis; with inconsistent direction of effect, an average can mislead (ES-83). NICE: synthesis is not essential (ES-127); pooling fits when there are enough relevant, valid data on comparable outcome measures, and pooling comes with a heterogeneity assessment (ES-132).
- Very diverse studies (for example different forms of control) can mislead in a meta-analysis (ES-88). Lay out each study's control (for example waitlist, sham app, health education, therapist-led treatment, as the papers state them) before any pooling decision. In the live run of 19 October 2026, one published review of fully automated digital CBT for insomnia reported that control group type moderated outcomes (abstract passage in `examples/live/passages_2026-10-19.json`).
- Heterogeneity must shape interpretation; fixed-effect intervals ignore it and random-effects results describe a mean effect (MECIR C69) (ES-84). I-squared rough guide, overlapping bands: 0 to 40% might not be important; 30 to 60% moderate; 50 to 90% substantial; 75 to 100% considerable; thresholds can mislead (ES-85).
- Check extraction first: severe heterogeneity can come from data errors such as standard errors entered as SDs (ES-86).
- Only pre-specified subgroup analyses support reliable conclusions about causes (ES-87).
- EU JCA: exchangeability (similarity, homogeneity, consistency); random effects usually appropriate; fixed effect needs rigorous justification (ES-165). The JCA guideline's "uncertainty" is not GRADE certainty (ES-166).
- Rapid reviews: synthesize narratively; meta-analyze only if appropriate (ES-114).

## 6. GRADE certainty, per outcome

- Four levels: High, Moderate, Low, Very low (ES-89). They apply to a body of evidence, not to single studies (ES-199, abstract only, doi 10.1016/j.jclinepi.2010.07.015). Definitions, GRADE handbook Table 5.1: High, "very confident that the true effect lies close to that of the estimate" (ES-195); Moderate, "moderately confident", the true effect "is likely to be close" but may be substantially different (ES-196); Low, "confidence in the effect estimate is limited", the true effect "may be substantially different" (ES-197); Very low, "very little confidence", the true effect "is likely to be substantially different" (ES-198).
- Start: randomized evidence high, non-randomized low (ES-90). Sound non-randomized studies are generally low even with ROBINS-I (ES-100). The research file notes Cochrane's Figure 14.2.a lists ROBINS-I-assessed studies with RCTs at high; state which convention you apply.
- Rate down 1 or 2 levels each for risk of bias, inconsistency, indirectness, imprecision, publication bias (ES-91); usually one level per factor, at most three overall, never below very low (ES-95).
- Rate up for large effect (1 or 2), plausible confounding that would reduce the effect (1), dose-response (1) (ES-92). Large effect: RR above 2 or below 0.5; very large: above 5 or below 0.2 (ES-93).
- Not a score: judgment-based (ES-94). Certainty is per outcome (ES-96); PRISMA item 22 asks for it per outcome (ES-14).
- The library's GRADE output is a per-record starting level with empty factors (`tools.md`). Never present it as the certainty of an outcome.

### Wording a finding by its certainty

Use the reviewers' rating, then the wording of Cochrane Handbook 6.5 Table 15.6.b (chapter 15, last updated August 2023). GRADE guidelines 26 bases such statements on effect size and certainty (ES-201, ES-202, abstract only, doi 10.1016/j.jclinepi.2019.10.014).

| Certainty (reviewers') | Verb pattern | Example for a moderate effect | Row |
|---|---|---|---|
| High | State it directly | "X reduces outcome"; no important effect: "X results in little to no difference in outcome" | ES-203 |
| Moderate | "likely" or "probably" | "X likely reduces outcome" | ES-204 |
| Low | "may" or "the evidence suggests" | "X may reduce outcome" | ES-205 |
| Very low | "the evidence is very uncertain", any effect size | "The evidence is very uncertain about the effect of X on outcome" | ES-206 |

A wide interval that includes no effect does not show "no effect"; if one possibility is named, name the other too (ES-207). Never choose the verb before the reviewers rate certainty: unrated, write "certainty not yet rated".

## 7. Summary of Findings table

Columns and content (ES-97, ES-98, ES-99): population and setting; the comparison; up to seven critical or important outcomes, desirable and undesirable; the comparator's typical burden (illustrative risk or mean); absolute and relative effects; numbers of participants and studies; certainty per outcome; comments; explanations for every rating other than high.

## 8. PRISMA 2020 flow diagram

Essential counts (ES-20 [PAPER] doi 10.1136/bmj.n160): records identified; records removed before screening (duplicates, machine classifiers, other reasons); records screened; records excluded; reports sought; reports not retrieved; reports assessed; reports excluded with reasons; studies and reports included. For updates, the number of studies in the previous version; human versus automation exclusions where applicable (ES-21). Cite excluded studies that seem eligible, with reasons (item 16b, ES-13). `scripts/prisma_flow.py` computes and reconciles these from the person's log.
