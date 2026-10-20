> Copied from the sibling skill evidence-translation-and-communication (references/certainty-wording.md, 19 October 2026) so this package stands alone. Row ids refer to the research files copied into this skill.

# Certainty: who rates it and how it is worded

Interpretive reference. Every rule cites a row in `evidence-synthesis-research.md` (ES rows, read 19 October 2026). Where the rows are silent, the rule says `[GAP]`.

## Who rates certainty

- Certainty is a judgment about a body of evidence for one outcome, made by people: review authors, a guideline panel, an HTA body or a rater the person names. GRADE is judgment-based and "not a quantitative system" (ES-94).
- The model does not rate certainty. It lays out what each domain needs and records the rating the person gives, with who gave it and when.
- `literature.grade_evidence` with `standard: "grade"` returns a starting level taken from the design label, with every downgrade and upgrade factor empty ("downgrade factors left empty for a human reviewer"; live output in `examples/live/literature_calls.json`). That is ES-90's starting point, not a rating. Never print it as "certainty: high".
- An EU joint clinical assessment report states relative effects and "the degree of certainty", without value judgments (ES-149). Its "uncertainty" in the quantitative evidence synthesis guideline is not GRADE certainty (ES-166). When quoting a JCA, use its own words and do not convert them to GRADE levels.

## The GRADE frame (what a rating rests on)

| Element | Rule | Row |
|---|---|---|
| Levels | Four: High, Moderate, Low, Very low. Handbook wording for the ends: High, "We are very confident that the true effect lies close to that of the estimate of the effect"; Very low, "We have very little confidence in the effect estimate". The handbook wording for Moderate and Low is not quoted in the research row `[GAP]`; quote it from the GRADE handbook before using it. | ES-89 |
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
5. Plain-language phrasings that tie certainty to verbs ("probably", "may") are not in the sourced rows `[GAP]`. Until a sourced rule exists, a lay version states the level and the handbook definition in plain words and names the rater.
6. A single study is a single study. Its result is "in one randomized trial of N participants", never "the evidence shows".
