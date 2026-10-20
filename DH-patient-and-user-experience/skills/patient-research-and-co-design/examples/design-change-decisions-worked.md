# Worked example: B1 design change decisions

Run on 19 October 2026. The person's files are illustrative (`sample-data/`; no real product, session or person). The ranking call is a real library call (`live/rice_illustrative.json`, second call); the scores in it are the example person's.

**Request:** "We ran three co-design sessions for our type 2 diabetes logging app. Here are the captures and our insight log. Our rule: a point is repeated if two or more patients or carers raised it. Which of these do we act on? For the open ones, here are our RICE numbers: out-of-range color 1200 reach, impact 2, confidence 80, effort 2; printable summary 300, 1, 50, 3; carer shared view 500, 2, 50, 8."

**Calls and runs**

1. `scripts/insight_tracker.py check sessions.csv captures.csv insights.csv changes.csv`: no identifiers found.
2. `scripts/insight_tracker.py tally sample-data/captures.csv --repeat 2`
3. `scripts/insight_tracker.py status sample-data/insights.csv sample-data/captures.csv --as-of 2026-10-19`
4. `analytics.rice {initiatives: [{id: "I4 out-of-range color wording", reach: 1200, impact: 2, confidence: 80, effort: 2}, {id: "I5 printable weekly summary", reach: 300, impact: 1, confidence: 50, effort: 3}, {id: "I2 carer shared view", reach: 500, impact: 2, confidence: 50, effort: 8}]}`

## Answer (short mode)

**Under your rule, three points repeat: I1 logging takes too many steps (3 patients, 2 sessions), I3 numbers too small (2, 2 sessions), I4 red out-of-range color read as an emergency (3, 3 sessions).** Your log shows I1 and I3 accepted, I4 open.

| Insight | Your decision | Change and version | What is missing |
|---|---|---|---|
| I1 logging steps | Accepted | CH-12, version 2.4 | Nothing |
| I3 number size | Accepted | CH-14, no version | Owner and version (R-12) |
| I4 red color | Open, 76 days since first capture | none | Decision; past the 1 October 2026 date you set |
| I2 carer view (1 carer) | Deferred | none | Owner |
| I6 offline (1 patient) | Refused | none | Reason (R-11) |

**Your RICE order (analytics.rice on your numbers):** I4 960, I2 62.5, I5 50. The order reflects your scores; it is not a recommendation. Note: the tool reads confidence as a percent; it echoed 0.8 and 0.5, as intended.

**Stops:**
- I4 is marked as touching a safety constraint and ranks first on your scores. Changing how out-of-range readings look goes to your clinical safety lead, the owner you named, before it is accepted (R-13).
- I7 (one patient asked to remove dose guidance text) is marked safety-relevant and has no owner: owner not named. Who decides it?
- I5 rests on one staff member's words ("Patients want a weekly summary they can print"); no patient raised it. It is not patient co-design evidence (R-5).

**Kept in view:** these are 11 patients and one carer recruited by your team, not patients in general (PE-06).

**Record:** Decision log draft on your files. Decisions and scores are yours. AI-assisted. Uncleared draft; a named person clears it, then the record is built with verify.build_record.

The full version adds the decisions table with quotes, the open-point list and the log checks.

## What this example shows

- The person's rule produced the "repeated" label; I2 and I6 appear because the log holds decisions on them, not because they repeat.
- A high RICE score did not turn a safety-touching point into an accepted change.
- A staff request was kept apart from patient evidence.
- The tool's confidence scale was checked against what it echoed.
