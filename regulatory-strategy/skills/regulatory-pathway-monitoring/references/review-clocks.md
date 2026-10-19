# Review clocks and how to read them

Interpretive reference for tasks A1 and B1. Row prefixes: RP = `reg-pathways-sources.md` (written there without the prefix), MR and JX = `multi-region-sources.md`. All rows read 19 October 2026.

## Three clocks, never mixed

For the same FDA submission there are three different numbers (RP "Changes and conflicts"):

1. **The regulation clock.** What the regulation says FDA does, in days from receipt, filing or acceptance.
2. **The MDUFA goal.** A performance commitment counted in "FDA days", which exclude the time the file sits with the sponsor (for example while answering an additional-information request), met for a stated share of submissions.
3. **Observed total time.** What FDA's own quarterly report shows on average, FDA days plus sponsor days.

A person's elapsed calendar days can only be compared with number 3 directly. Comparing them with number 2 needs the sponsor-hold days removed, which only the person's own records show. `scripts/review_clock.py` does both when the person gives the hold days.

## FDA routes

| Route | Regulation clock | MDUFA V goal (FDA days) | Observed (report of 26 August 2026, actions to 30 June 2026) |
|---|---|---|---|
| 510(k) | Submit at least 90 days before marketing; no marketing before the order (RP US-04, RP US-07). | 90 FDA days for 95% (RP US-46). | Within goal 99.32%, 98.81%, 97.94% (FY 2023, 2024, 2025); FY 2026 cohort 97.56% and still open. Average total days 141.46, 143.64, 141.24; average FDA days about 75. SE rate 95.45%, 95.34%, 95.77% (RP US-57 to US-59). |
| De Novo | 120 days from acceptance (RP US-11). Withdrawn if an additional-information request is not fully answered within 180 days (RP US-13). | 150 FDA days for 70%, shown as 80% for FY 2026 and 90% for FY 2027 (RP US-47, RP US-60). | Within goal 93.98%, 98.61%, 92.00%. Average total days 270.07, 247.51, 278.12. Received 96, 78, 68; granted 37, 29, 28 (FY 2025 still open) (RP US-60 to US-62). The FY 2026 cohort's 100% rests on very few decisions and is not meaningful yet (RP "Changes and conflicts"). |
| PMA | 180 days from filing; a major amendment can extend by up to 180 days (RP US-14, RP US-15). | 180 FDA days for 90% without an advisory committee; 320 with one (RP US-48). | 180-day goal met 98.55%, 96.88%, 97.26% (RP US-63). |
| Pre-Submission | Written feedback within 70 days of the review clock start; at least 5 days before a meeting (RP US-31, RP US-32); acceptance screening within 15 days (RP US-33). | 90% within goal, up to 4,300 a year (RP US-35). | Not in the rows `[GAP]`. |
| Breakthrough request | Decision letter within 60 calendar days (RP US-42). | Not in the rows. | 1,320 designations to 30 June 2026 (RP US-43). |

Where the reports live: FDA posts MDUFA V performance reports quarterly on its MDUFA Reports page (RP US-64). Each figure carries its report date and cohort; a newer report replaces it.

MDUFA V ends 30 September 2027; MDUFA VI commitments were not read `[GAP]` (RP US-45).

## EU notified body timing

There is no statutory review clock for a notified body assessment in the rows. The only timing evidence is the Commission-commissioned contractor survey (data to 28 February 2026, published 2 July 2026): 62% of notified bodies report 13 to 18 months from written agreement to a new QMS certificate; for QMS plus product certificates 51% report 13 to 18 months and 31% report 19 to 24 months (RP EU-40, RP EU-44). It is self-reported by notified bodies and has no software breakdown (RP "Not sourced").

## GB and Switzerland

No review clocks are in the rows `[GAP]`. GB accepts CE marked MDR devices until 30 June 2030, MDD devices until the sooner of certificate expiry or 30 June 2028, and up-classified self-declared MDD devices until 30 June 2028 (RP UK-02 to UK-04). Swiss recognition rests on EU declarations and EU notified body certificates (MR-19, MR-20).

## How to state a clock

- "Day 210 of a De Novo (calendar days since submission). FDA's average total time for De Novo decisions was 247 to 278 days in FY 2023 to FY 2025. Whether the 150 FDA-day goal is at risk depends on the days the file was on hold with you."
- Place the person's calendar days against the observed averages in words that match the arithmetic: under the lowest yearly average is "below FDA's average total time", between the lowest and highest is "within the range of yearly averages", over the highest is "above". Check the comparison before writing it.
- Never "the FDA is late". A goal is a share of submissions, not a promise for one.
- A clock is a fact. State it without pressure words.
