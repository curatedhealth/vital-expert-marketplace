# Certainty: who rates it and how it is worded

Interpretive reference. Every rule cites a row in `evidence-synthesis-research.md` (ES rows, read 19 October 2026; section 15 rows ES-171 to ES-234 read 20 October 2026). Where the rows are silent, the rule says `[GAP]`.

## Who rates certainty

- Certainty is a judgment about a body of evidence for one outcome, made by people: review authors, a guideline panel, an HTA body or a rater the person names. GRADE is judgment-based and "not a quantitative system" (ES-94).
- The model does not rate certainty. It lays out what each domain needs and records the rating the person gives, with who gave it and when.
- `literature.grade_evidence` with `standard: "grade"` returns a starting level taken from the design label, with every downgrade and upgrade factor empty ("downgrade factors left empty for a human reviewer"; live output in `examples/live/literature_calls.json`). That is ES-90's starting point, not a rating. Never print it as "certainty: high".
- An EU joint clinical assessment report states relative effects and "the degree of certainty", without value judgments (ES-149). Its "uncertainty" in the quantitative evidence synthesis guideline is not GRADE certainty (ES-166). When quoting a JCA, use its own words and do not convert them to GRADE levels.

## The GRADE frame (what a rating rests on)

| Element | Rule | Row |
|---|---|---|
| Levels | Four, applied to a body of evidence, not to single studies (ES-199). GRADE handbook Table 5.1 (it says "quality" where later guidance says "certainty"): High, "We are very confident that the true effect lies close to that of the estimate of the effect" (ES-195); Moderate, "We are moderately confident in the effect estimate: The true effect is likely to be close to the estimate of the effect, but there is a possibility that it is substantially different" (ES-196); Low, "Our confidence in the effect estimate is limited: The true effect may be substantially different from the estimate of the effect." (ES-197); Very low, "We have very little confidence in the effect estimate: The true effect is likely to be substantially different from the estimate of effect" (ES-198). The handbook notes any four-way split of a continuum is somewhat arbitrary (ES-198). | ES-89, ES-195 to ES-199 |
| Start | Randomized trials start high; non-randomized studies start low. Cochrane chapter 14 also shows studies assessed with ROBINS-I starting high in a figure, and adds that sound non-randomized studies are generally graded low even with ROBINS-I. State which convention the rater used. | ES-90, ES-100, Changes and conflicts |
| Down | Risk of bias, inconsistency, indirectness, imprecision, publication bias: 1 or 2 levels each. | ES-91 |
| Limits | Usually one level per factor, at most three overall; nothing below very low. | ES-95 |
| Up | Large effect (1 or 2), plausible confounding that would reduce the effect (1), dose-response (1). Large effect is RR above 2 or below 0.5; very large above 5 or below 0.2. | ES-92, ES-93 |
| Per outcome | Certainty is assessed separately for each outcome and may differ by outcome. | ES-96 |
| Explain | Any rating other than high is explained in a footnote or the comments column. | ES-99 |

## Summary of Findings layout (when the person wants a table)

Population and setting, the comparison, up to seven critical or important outcomes (desirable and undesirable), the comparator's typical burden, absolute and relative effects, numbers of participants and studies, certainty, comments and explanations (ES-97, ES-98). A review reports its certainty method and per-outcome certainty results (PRISMA 2020 items 15 and 22, ES-12, ES-14).

## Wording rules for this skill

1. One statement per outcome. Never pool certainty across outcomes into "the evidence is strong".
2. Each statement names: the outcome as measured, the population, the comparator, the time point, the effect as the passage reports it, the study count, and the certainty with its rater ("certainty rated low by [the rater the person named, in their words], 12 October 2026") or "certainty not rated `[GAP]`".
3. Quote the effect as reported. Do not convert a within-arm change into a between-arm difference, a standardized effect into points, or a p-value into "proven".
4. Not in any output: "proves", "proven", "conclusive", "cost-effective", "safe and effective". Where a source uses them, quote them as the source's words, attributed.
5. Words tied to certainty follow Cochrane Handbook 6.5 Table 15.6.b, keyed to the rating the person gave, never chosen by the model. High: state the effect directly ("X reduces outcome"; "X results in little to no difference in outcome") (ES-203). Moderate: "likely" or "probably" ("X likely reduces outcome"; "X probably reduces outcome") (ES-204). Low: "may" or "the evidence suggests" ("X may reduce outcome") (ES-205). Very low, any effect size: "The evidence is very uncertain about the effect of X on outcome" (ES-206). GRADE guidelines 26 likewise bases statements on effect size and certainty (abstract only, ES-201, ES-202). A wide interval that includes no effect is never "no effect" or "no different"; if one possibility is named, name the other too (ES-207). A lay version uses the same verb, states the level and its Table 5.1 meaning in plain words, and names the rater. With no rating, no certainty verb is used: the effect is quoted as the passage reports it and certainty stays "not rated `[GAP]`".
6. A single study is a single study. Its result is "in one randomized trial of N participants", never "the evidence shows".
