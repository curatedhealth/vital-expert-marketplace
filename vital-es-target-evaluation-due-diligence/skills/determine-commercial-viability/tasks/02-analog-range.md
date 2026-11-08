Input:    the analog rows; optional addressable population from skill G and the year-spread limit
Atom:     none
Tool:     python3 scripts/analog_range.py input.json --pretty (fixture: evals/fixtures/good-analog-input.json)
Template: none
Output:   low, median, high, n; leave-one-out ranges; peak-year span flag; optional scaled view labelled as an unvalidated assumption; the not-a-forecast statement; the disabled error-band [CHECK] message
Check:    exit 0; n of 3 or more or a GAP with no range; the range is never presented as a point. Rule: the human confirms the analog set; no error band is applied
Human:    the named reviewer with commercial experience reviews the output
