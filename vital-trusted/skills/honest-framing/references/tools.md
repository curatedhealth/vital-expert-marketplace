# Tools and companion slot

## Companion slot

No companion exists for this skill. VERIFY tests sentences against supplied passages;
it does not judge certainty, framing or charts, and this skill does not hand off to it.

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Uncertainty at its real size | Read the supplied paper's results table and limitations section and return, per result, the estimate, interval, n, follow-up and whether it was primary, so the result card is filled from the source rather than from the assistant's reading | No companion yet | Method runs; the result card is filled by reading the material; check line says "not tool-checked" |
| Numbers and charts | Read a chart image or file and return the axis start and end, scale per panel, series plotted and the values behind each mark, then compute the distortion | No companion yet | Method and `scripts/chart_scale.py` run on what the person supplies or describes; where the chart's values or axis are not supplied, `[GAP: not checkable here — whether the chart matches its data — supply the data or the chart file]` |
| Conflict disclosure | Read the source's funding and disclosure sections and return the sponsor, its stated role and author ties, quoted | No companion yet. Related: `source-assessment` records what a source discloses, with VERIFY `qualify_source` when connected | Method runs from the supplied material; "not tool-checked" |

Never describe any of the above as having run (TR-H4).

## Scripts

Run them where the host can execute code. Where it cannot, do the same arithmetic by
hand and show it. Every output is labeled "derived from supplied values"; nothing is
looked up.

### `scripts/chart_scale.py`

How much a chart's construction enlarges or shrinks a difference.

```
python scripts/chart_scale.py --axis-min 80 --value 84 --value 88
python scripts/chart_scale.py --axis-min 80 --axis-max 90 --value 84 --value 88
python scripts/chart_scale.py --value 10 --value 20 --icon-scaling both
python scripts/chart_scale.py --cumulative 410,805,1193
python scripts/chart_scale.py --axis-min 80 --value 84 --value 88 --json
```

Outputs:

- actual ratio of the two values and the ratio of the drawn bar lengths with the given
  axis start; how many times larger the difference looks (displayed ratio of change over
  actual ratio of change); the share of the plotted range the difference fills when an
  axis end is given;
- for pictograms: the apparent size ratio when icons are scaled in height only (as
  drawn) or in both height and width (area grows with the square);
- for cumulative series: the per-period increments.

Pitfalls:

- It measures the drawing, not the meaning. A narrow axis on a line chart can be
  reasonable if stated; say what the reader sees, do not call it wrong.
- Values must be on the axis scale (percent axis, percent values).
- For a value axis that does not start at zero on a bar chart, the result is the
  distortion; for a line chart, report it and describe the stated range.

### `scripts/find_framing_cues.py`

Lists words to look at, by line, in four groups: certainty ("proves", "dramatic",
"clearly"), hedging (with a count per sentence, so stacked hedges show), minimizing
("only 2%", "just", "rare") and independence or sponsor words ("independent",
"experts agree", "data on file", "funded by").

```
python scripts/find_framing_cues.py draft.txt
python scripts/find_framing_cues.py draft.txt --json
cat draft.txt | python scripts/find_framing_cues.py -
```

It finds words, not meaning. "Clearly labeled" is not overclaiming; "funded by" may
already be the disclosure. Read every hit against the material.

### Reused: `../grounded-statements/scripts/risk_metrics.py`

For relative and absolute effects of a binary outcome from arm rates or counts, use the
script in `grounded-statements` by its path. Do not copy it into this skill.

```
python ../grounded-statements/scripts/risk_metrics.py --treat-rate 0.01 --ctrl-rate 0.02
```

Use it here to set benefit and harm in the same format (pattern NF1), not to correct a
figure; correcting figures is `grounded-statements`.

### Tests

```
python scripts/test_scripts.py
```

Runs both scripts on fixed inputs and checks the outputs.
