Origin: authored in value-narrative-and-dossier/references/certainty-and-wording.md (19 October 2026, updated 20 October 2026), copied unchanged below so this package stands alone.
# Certainty and wording

Interpretive reference for tasks A1 and B1. Rows from `evidence-synthesis-research.md` (ES) and `promotion-and-claims-research.md` (PC), read 19 October 2026; ES-195 to ES-207 read 20 October 2026.

## Certainty belongs to a person, per outcome

| Rule | Rows |
|---|---|
| GRADE has four levels, applied to a body of evidence, not to single studies. GRADE handbook Table 5.1 (it says "quality" where later guidance says "certainty"): High, "We are very confident that the true effect lies close to that of the estimate of the effect"; Moderate, "We are moderately confident in the effect estimate: The true effect is likely to be close to the estimate of the effect, but there is a possibility that it is substantially different"; Low, "Our confidence in the effect estimate is limited: The true effect may be substantially different from the estimate of the effect."; Very low, "We have very little confidence in the effect estimate: The true effect is likely to be substantially different from the estimate of effect". | ES-89, ES-195 to ES-199 |
| Statements tie the verb to the rating (Cochrane Handbook 6.5 Table 15.6.b). High: state the effect directly ("X reduces outcome"). Moderate: "likely" or "probably" ("X likely reduces outcome"). Low: "may" or "the evidence suggests" ("X may reduce outcome"). Very low: "The evidence is very uncertain about the effect of X on outcome". GRADE guidelines 26 likewise bases statements on effect size and certainty (abstract only). | ES-203 to ES-206, ES-201 |
| A wide interval that includes no effect is never "no effect" or "no different"; if one possibility is named, name the other too. | ES-207 |
| Randomized evidence starts high, non-randomized starts low; sound non-randomized studies are generally graded low even with ROBINS-I. | ES-90, ES-100 |
| Rate down for risk of bias, inconsistency, indirectness, imprecision, publication bias; up for large effect, opposing confounding, dose-response. | ES-91, ES-92 |
| GRADE is judgment, not a score; usually one level per factor, at most three overall; nothing below very low. | ES-94, ES-95 |
| Certainty is assessed per outcome, not per study or product. | ES-96 |
| Any rating other than high is explained in a footnote or comment. | ES-99 |
| A Summary of Findings table states population, comparison, up to seven outcomes, comparator burden, absolute and relative effects, numbers, certainty, comments. | ES-97, ES-98 |
| EU JCA reports state the degree of certainty of relative effects; the JCA guideline's "uncertainty" is not GRADE certainty. | ES-149, ES-166 |

Practice: the narrative names the level the person or the review assigned, for that outcome, with who assigned it. A `literature.grade_evidence` result is never a certainty: with GRADE it returns only the starting level from the design label, factors empty; with CEBM 2011 it returns a level for a design. The verb follows that rating (Table 15.6.b, ES-203 to ES-206); the model never picks the level to fit the verb. If nobody has rated an outcome, write "certainty not yet rated `[GAP]`" and use no certainty verb: quote the effect as the source reports it, attributed.

## A claim enters only with a passage read in the same direction

Same direction, same population, same comparator, same outcome, same time point. The Verify tool decides on word overlap (register N3). Live on 19 October 2026: a faithful claim scored 67 percent and "supported"; the same result widened to "adults with insomnia" scored 77 percent and "supported"; a claim the passage states the opposite of came back "unsupported", not "contradicted" (`examples/live/verify_dcbti_pregnancy.json`).

If the person's result does not say whether a figure is a difference between arms or a change within one arm, ask, and word it as given until the passage settles it.

## Wording the rows bind

| Wording | Why it is out or needs care | Rows |
|---|---|---|
| "Proves", "cures", "guaranteed", "no side effects" | Misleading by statement or omission; EU cure claims blacklisted; HWG bars guaranteed success and "no harmful effects". | PC-US-01, PC-US-03, PC-EU-10, PC-DE-04 |
| "Cost-effective", "saves money" as a fact | A conclusion that belongs to the person or the HTA body; for a US payor it is HCEI and needs the safe-harbor conditions and context. | PC-US-04, PC-US-06, PC-US-40 |
| A result from a narrower population stated for a wider one | Inconsistent with labeling if outside the cleared population; misleading in the EU. | PC-US-27, PC-EU-02 |
| Positive results only | Unfavorable or inconsistent findings must be disclosed. | PC-US-31 |
| A weak study with a disclaimer | Disclosure of limitations does not cure a study inadequate for the claim. | PC-US-30 |
| "FDA-cleared", "CE-certified", "DiGA-listed" when not so | False approval claims always unfair in the EU. | PC-EU-11 |
| Results of an uncleared use, to payors | Factual results only, no conclusions on safety or effectiveness, with the required statements. | PC-US-44, PC-US-45 |
| A study cited in German advertising | State whether it concerns the advertised product, plus author, date and source; reproduce faithfully. | PC-DE-05 |
