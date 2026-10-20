# Task TR-3.2.2 Numbers and charts framed at their real size

## Formula

| Slot | For this task |
|---|---|
| Worker | Medical reviewer with a statistics background |
| Workflow | List every figure and chart, check how each is framed against the material, describe what a plain version shows, then fix or mark |
| Skill | TR-3.2.2 |
| Knowledge | `references/rules.md` (R1–R4, R5, R6), `references/patterns.md` (NF1–NF7, CH1–CH8) |
| Tool | `scripts/chart_scale.py`; `../grounded-statements/scripts/risk_metrics.py` for relative and absolute effects. No companion yet |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/framing-note.md`, `assets/chart-description.md` |
| Input | The draft (text, chart, chart description or slide), the supplied data behind it, the context card |
| Governance | TR-H1, TR-H3, TR-H4, TR-H13 |

## Who owns what

`grounded-statements` owns whether each number is right and whether the arithmetic
holds: matches the source, percent versus percentage points, the absolute figure added
when only a relative one is given, the NNT derived from arm rates. This task owns
whether the **choice and presentation** of correct numbers makes the effect look larger
or smaller than it is. A relative-only figure is counted there, not here, unless its
framing differs from another figure in the same piece (below, step 3).

## Guard (while drafting)

1. **Same format for benefit and harm.** If the benefit is given as a relative change,
   give the harms the same way, and both with absolute figures. Do not give the benefit
   relative ("halves the risk") and the harm absolute ("2% had bleeding").
2. **Absolute figure as prominent as the relative one.** Same sentence, same size, same
   slide. Not in a footnote.
3. **Comparator named and matched.** Give the control group's figure beside the
   treatment's, and say what the comparator was. Compare like with like: same
   population, same timepoint, same dose, same definition. A figure from one trial
   against a figure from another trial is not a comparison; say so if it must appear.
4. **Same denominator and same rounding.** When two frequencies sit side by side, use
   the same base ("12 in 100 versus 8 in 100"). Do not round a figure below 1% up to
   1%, and do not round two close values until their difference vanishes or grows.
5. **Per-period or cumulative, said plainly.** Name which one a figure is. A rising
   cumulative line will rise even if each period is flat or falling; show the
   per-period figures when the message is about change (`scripts/chart_scale.py
   --cumulative`).
6. **Do not shrink a serious risk with words.** "Only", "just", "as few as",
   "rare" beside the rate of a serious harm minimize it. Give the rate and the
   comparator's rate without the qualifier.
7. **Charts.** Every chart for a reader outside the team carries:
   - a title saying what it shows, labeled axes with units, and the n behind each bar
     or point;
   - a value axis that starts at zero for bars and areas; where a line chart uses a
     narrower range to show change, the range is stated and the axis break is visible;
   - the same scale on panels that are compared side by side;
   - the full period the material covers, or a stated reason for a shorter window;
   - both arms, and the comparator labeled;
   - icons or pictograms sized by count, not by height and width together (a picture
     twice as tall and twice as wide reads as four times as large);
   - an icon array that shows both the people affected and the people studied.
8. **Describe what a plain version shows.** When a chart is changed or must be
   changed, write one or two plain sentences on what the same data look like with a
   zero baseline, the full period and both arms (`assets/chart-description.md`). This
   is a description, not a redraw; the person or their agency redraws it.

## Repair (existing draft)

1. **List every figure and chart.** For a chart, write down: chart type, axis start and
   end, units, what each bar or line is, n, period, comparator, any break or
   annotation. If you only have a description of the chart, work from it and say so.
2. **Check each against the guard list.** Classify: framed at its size; looks larger
   than it is; looks smaller than it is (a harm minimized, a competitor's result
   compressed); cannot tell (chart data or axis not supplied).
3. **Measure, do not estimate.** For a cropped axis or a scaled pictogram, run
   `python scripts/chart_scale.py --axis-min 80 --value 84 --value 88` (or do the
   arithmetic and show it). It gives how many times larger the difference looks than it
   is. For relative versus absolute, use
   `python ../grounded-statements/scripts/risk_metrics.py` and keep its labels.
4. **Fix the text** to the guard list. **For each chart**, give the plain description
   and the specific changes ("start the axis at 0%", "add the placebo bar", "show the
   12-month data the table supplies") for the person to make.
5. **Mark what cannot be checked.** If the chart's data, axis or period are not
   supplied, use `[GAP: not supplied — …]` rather than guessing what the chart shows.

## Check line

See `assets/check-line.md` (framing line).

## Boundaries

- The correctness of each number and the relative and absolute arithmetic are
  `grounded-statements`. Reuse its script; do not copy or re-derive its rules.
- Studies, endpoints or timepoints in the material that the draft leaves out entirely
  are `balanced-evidence` (selective reporting). A chart that shows a cropped window of
  data it otherwise uses is framing, here.
- Whether a cross-trial or head-to-head comparison may be made at all is
  `claims-and-label`. This task makes a comparison that is made say what it is.
- Visual style, brand colors and typography are not judged (TR-H9), except where they
  change the apparent size of a result (a harm in pale small type beside a benefit in
  bold).
