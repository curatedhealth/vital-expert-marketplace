# Engagement read on the illustrative usage file (script output)

ILLUSTRATIVE. Invented data (`evals/files/usage_illustrative.csv`, `evals/files/engagement_definitions_illustrative.json`); no real product. Run on 20 October 2026 with the data cut the invented person gave (15 October 2026):

`python3 scripts/engagement_read.py --definitions evals/files/engagement_definitions_illustrative.json --data evals/files/usage_illustrative.csv --version 1.4 --as-of 2026-10-15`

```
Version: 1.4 | Data cut: 2026-10-15 | Users: 10 | Rows excluded (other version or after cut): 2
Discontinuation rule: three consecutive weeks without use (period of 90 days or more), SE72
Discontinued: 4 of 10 (0.4) | Completed: 5 (0.5) | In progress: 1 | Not determinable: 0
Discontinuations by week (first day without use): {'week 1': 1, 'week 3': 1, 'week 6': 1, 'week 9': 1}
Mean days to discontinuation: 31.0 (days from first use to the last use before the qualifying gap; the DiGAV text does not say which day counts, so the person confirms or replaces this reading)
Weekly usage, discontinued users included (SE71):
  week 1: users 10, mean minutes 141.6, mean sessions 6.7
  week 2: users 10, mean minutes 124.3, mean sessions 5.4
  week 3: users 10, mean minutes 122.5, mean sessions 5.2
  week 4: users 10, mean minutes 110.6, mean sessions 4.4
  week 5: users 10, mean minutes 121.3, mean sessions 5.0
  week 6: users 10, mean minutes 114.4, mean sessions 4.6
  week 7: users 10, mean minutes 114.7, mean sessions 4.7
  week 8: users 10, mean minutes 106.2, mean sessions 4.2
  week 9: users 10, mean minutes 108.9, mean sessions 4.3
  week 10: users 9, mean minutes 116.4, mean sessions 4.44
  week 11: users 9, mean minutes 120.1, mean sessions 4.67
  week 12: users 9, mean minutes 114.0, mean sessions 4.33
  week 13: users 9, mean minutes 103.1, mean sessions 4.0
Mean weekly minutes: 116.9 | Mean weekly sessions: 4.78
Per-user mean weekly minutes: median 38.5; highest U09 at 830.8 (one heavy user can carry the mean; the median is shown beside it. A very high level is reported as a level and handed to A4 only if the design named an overuse or screen-time risk.)
Threshold comparisons:
  discontinued_share: 0.4 vs <= 0.3: outside the person's threshold
  mean_weekly_minutes: 116.9 vs >= 60: within the person's threshold
Note: Usage is the 'used' link, never the outcome (SE26; SE82, DOI 10.1007/s13142-016-0453-1).
Note: Called 'usage', not adherence, unless the person gives an intended use with its justification (SE92, DOI 10.2196/jmir.8578).
Note: No benchmark or retention target is sourced; none is applied.
```

Without `--as-of` the same run prints "data cut not given; ask the person", marks 9 of 10 users "not determinable" (only the internal gap of U03 is visible), reports weekly means over observed weeks only, and compares nothing with the thresholds.

Reading: 4 of 10 users met the DiGAV discontinuation rule (SE72), outside the person's threshold of 0.3; the mean of 116.9 weekly minutes is within the person's threshold of 60, but one user (U09, 830.8 minutes a week) carries it and the per-user median is 38.5. Both are usage levels, not outcomes (SE26; SE82, DOI 10.1007/s13142-016-0453-1). No benchmark is applied.
