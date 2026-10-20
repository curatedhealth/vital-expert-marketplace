# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it rests
on. All examples are invented for teaching; no real product, trial or person. Product
names used here ("Velostra", "Corvane", "KELNA-1", "drug D") are fictional.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13). Rules R1 to R10 are in `references/rules.md`; where a rule is
outside its scope for the piece, it is good practice, not a requirement.

## Contents

- Uncertainty overstated UC1–UC9
- Over-hedging OH1–OH5
- Numbers framed NF1–NF7
- Charts CH1–CH8
- Interests IN1–IN7

## Uncertainty overstated

**UC1 "Proves" on one study.** One trial, however good, is described as proof.
Why: a single result can fail to replicate; "proves" leaves no room for that.
Before: "KELNA-1 proves Velostra is superior to Corvane."
After: "In KELNA-1, a single randomized trial of 640 patients, Velostra reduced flares
more than Corvane over 24 weeks (rate ratio 0.78, 95% CI 0.64 to 0.95)." (R4, R7, R10)
Note: whether a superiority claim may be made at all is for `claims-and-label`.

**UC2 The intensity word.** "Dramatic", "remarkable", "breakthrough", "game-changing",
"unprecedented", "strong", "robust" attached to a result.
Why: the word sets the size in the reader's mind before the number does.
After: drop the word; give the estimate with both arms. (R5, R7)

**UC3 "Clearly" and "undeniably".** Adverbs that close the question.
After: remove; let the interval show how clear it is. (R10)

**UC4 Significance as importance.** "A highly significant reduction" meaning a large or
important one.
After: "a reduction of 3.0 percentage points (6.0% versus 9.0%; p = 0.01)". Do not say
whether 3 points matters clinically (TR-H6). (R4, R10)

**UC5 The missing interval.** An estimate given alone when the material gives its range.
After: "hazard ratio 0.66 (95% CI 0.45 to 0.97): the data fit an effect anywhere from
a large reduction to a small one". (R4, R10)

**UC6 The unnamed small sample.** "Patients improved" from a 24-patient pilot.
After: "In a pilot study of 24 patients, 15 improved." (R4, R10)

**UC7 The unnamed short follow-up.** "Long-term benefit", "durable response" from 12
weeks of data.
After: "over 12 weeks; longer-term data [GAP: not supplied — results beyond week 12 —
supply the extension data if any]". (R10)

**UC8 Limitations moved away.** The authors' limitations sit in a footnote, an appendix
slide or nowhere, while the result is on the headline slide.
After: one plain sentence of the authors' main limitations on the slide that uses the
result. (R5, R10)

**UC9 The authors' conclusion as the draft's own.** "Drug D improves outcomes and is well
tolerated" restated without attribution when the primary endpoint was not met.
After: "The authors concluded that … . The primary endpoint did not differ between
groups." (R10)

## Over-hedging

**OH1 The buried primary result.** A met primary endpoint with a clear interval is
reported as "may offer a possible benefit".
Why: the reader concludes the evidence is weak when it is not; that is a misstatement in
the other direction.
Before: "Results may suggest that Velostra could potentially reduce flares in some
patients, although further research may be needed."
After: "Velostra reduced flares compared with placebo in KELNA-2, the trial's primary
endpoint (32% versus 47% of patients with a flare by week 24; difference 15 percentage
points, 95% CI 9 to 21). The trial ran for 24 weeks." (R10)

**OH2 Stacked hedges.** Two or more hedges on one result ("may possibly", "could
potentially suggest").
After: one hedge, placed on the real uncertainty (the follow-up, the subgroup), or none.

**OH3 The blanket caveat.** "Results should be interpreted with caution" with no reason.
After: name the actual limitation ("open-label", "24 weeks", "one center"), or drop it.

**OH4 Equal hedging for unequal evidence.** The met primary endpoint and an exploratory
subgroup are described with the same "may".
After: say the primary plainly; label the subgroup as exploratory. (R10)

**OH5 The hedge that hides a harm.** "Some patients may possibly experience nausea" when
the material gives 18% versus 6%.
After: "Nausea occurred in 18% of patients on drug D and 6% on placebo." (R1, R2)

## Numbers framed

These assume each number is right. Whether it is right, and the relative and absolute
arithmetic, are for `grounded-statements`.

**NF1 Mismatched formats.** Benefit as a relative change, harm as an absolute rate.
Before: "Cuts strokes by 50%. Major bleeding: 2%."
After: "Strokes: 1% versus 2% (absolute reduction 1 percentage point; relative reduction
50%). Major bleeding: 2% versus 1%." (R1, R2, R5)

**NF2 The absolute figure in the footnote.** The relative figure is the headline; the
absolute is small print on another slide.
After: both in the same sentence, same prominence. (R1, R5)

**NF3 The missing or mismatched comparator.** The treatment arm only, or a comparator
from a different trial, population, dose or timepoint.
After: name the comparator from the same study; a cross-trial figure is labeled as
"from a different study, not a direct comparison". (R1, R4)

**NF4 Different denominators.** "12 in 100 versus 1 in 20."
After: "12 in 100 versus 5 in 100". (R2)

**NF5 Rounding that moves the difference.** 0.4% shown as "less than 1%"; 4.4% versus
4.6% both shown as "5%" or as "4% versus 5%".
After: report as the source does. (R2)

**NF6 Cumulative as per-period.** "Prescriptions keep climbing" from a cumulative total
that rises whenever any prescription is written.
After: give the per-period figures: "new prescriptions per month were 410, 395 and
388". (R4)

**NF7 The minimizing qualifier.** "Only 2%", "just 1 in 50", "as few as", "rarely"
beside a serious harm.
After: "2% of patients on drug D and 1% on placebo had bleeding that needed hospital
care." (R2, R7)

## Charts

**CH1 The cropped axis.** A bar chart whose value axis starts at 80%, so bars of 84%
and 88% look like one is twice the other.
After: axis from 0%; or, if the narrow range is kept for a line chart, the range stated
and the axis break visible. `scripts/chart_scale.py` gives the size of the distortion.
(R3, R4, R6)

**CH2 The broken axis without a mark.** A break in the axis that the reader cannot see.
After: show the break, or redraw from zero. (R3, R6)

**CH3 Different scales on compared panels.** Two side-by-side panels with different
axis ranges, so a smaller effect looks the same size or larger.
After: the same scale on both panels. (R3, R6)

**CH4 The cherry-picked window.** A line chart from month 3 to month 6 when the material
covers 0 to 12 months and the curves converge later.
After: the full period, or the shorter window stated with the reason. If whole
timepoints are dropped from the draft altogether, that is selective reporting
(`balanced-evidence`). (R4, R6)

**CH5 The missing arm.** Only the treatment arm plotted.
After: both arms, comparator labeled. (R1, R3)

**CH6 The unlabeled chart.** No title, units, n or source.
After: title saying what it shows, labeled axes and units, n per group, source. (R3, R6)

**CH7 The growing pictogram.** An icon drawn twice as tall and twice as wide to show
twice the value, so it reads as four times larger.
After: icons by count (an icon array), or bars. `scripts/chart_scale.py
--icon-scaling both` gives the apparent ratio. (R3, R6)

**CH8 The icon array without the denominator.** Ten filled figures for ten patients who
improved, with no picture of the hundred studied.
After: show all 100, with the 10 marked. (R3)

## Interests

**IN1 The sponsored study as independent.** "An independent study found…" when the
funding statement names the company.
After: "A study funded by [company], the maker of Velostra, found…". (R8, R9)

**IN2 Company data as the literature.** "Data show…" or "real-world evidence shows…"
for an internal analysis or data on file.
After: "Company data on file (internal analysis of [data set as supplied], [date])
show…". (R8)

**IN3 The paid panel as consensus.** "Experts agree" from a company-funded advisory
board.
After: "At an advisory board organized and funded by [company], 7 of 10 participants
said…". (R8)

**IN4 The company survey as physicians' views.** "Physicians prefer Velostra" from
company-commissioned market research.
After: "In market research commissioned by [company] among 150 dermatologists, 61%
said…". (R8)

**IN5 Authors' ties dropped.** The summary omits that three authors are company
employees when the disclosures say so.
After: "Three of the eight authors are employees of [company], as the paper states."
(R9)

**IN6 The disclosure at the end.** The sponsor is named only on the last slide or in a
footnote, while the result is on the first.
After: the sponsor named where the result appears; the full statement can stay at the
end. (R8)

**IN7 "No role" in the draft's voice.** "The sponsor had no influence on the results."
After: "The authors state that the funder had no role in the design, analysis or
writing." If the material says nothing about the sponsor's role:
"[GAP: not supplied — sponsor's role in design, analysis and writing — see the funding
or disclosures section]". (R9)
