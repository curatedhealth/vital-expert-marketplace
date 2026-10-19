# Review clocks, agency questions and outcomes: what to track and how to read it

Row prefixes: `RP` = `REG_PATHWAYS_SUBMISSIONS.md`, `AI` = `AI_ML_REGULATION.md`, `S` = `submission-sources-supplement.md`. Read 19 October 2026. Goals are commitments in the MDUFA V letter; actual performance is FDA's report of 26 August 2026 covering actions through 30 June 2026 (RP US-56). Receipt cohorts FY 2023, FY 2024, FY 2025; the FY 2026 cohort is still open and not comparable yet (RP "Changes and conflicts").

## Two kinds of day

- **FDA days**: calendar days the submission is under review at FDA, from receipt of the accepted (or filed) submission (S-26). An Additional Information or Major Deficiency letter stops the clock (S-25). MDUFA decision goals are in FDA days.
- **Calendar (total) days**: receipt to decision, including time with the sponsor. The 510(k) shared total-time goal is in calendar days, measured on a trimmed closed cohort (S-28, S-29).
- **Regulatory clocks**: separate from MDUFA: De Novo 120 days after acceptance (RP US-11), PMA 180 days after filing (RP US-14).

Always say which kind a figure is. Never set a calendar-day figure against a FDA-day goal.

## Goals against actual performance

| Pathway | Goal (MDUFA V) | Actual, FY 2023 / FY 2024 / FY 2025 | Rows |
|---|---|---|---|
| 510(k) acceptance | Accepted or not within 15 calendar days | Not accepted or failed screening on first cycle: 20.52% / 5.40% / 7.20% | S-23, S-38 |
| 510(k) first interaction | SI within 60 calendar days for 95% | 96.08% / 95.80% / 97.17%; average 52.70 / 52.47 / 52.48 FDA days | S-24, S-39, S-40 |
| 510(k) decision | 90 FDA days for 95% | 99.32% / 98.81% / 97.94% | RP US-46, RP US-57 |
| 510(k) total time | Shared goal 112 calendar days (FY 2025 to FY 2027 cohorts), trimmed cohort | Average total days 141.46 / 143.64 / 141.24; 80th percentile 238 / 243 / 237 | S-28, S-29, RP US-58, S-43 |
| 510(k) review cycles | none | 1.67 / 1.69 / 1.69 | S-41 |
| 510(k) outcomes | none | SE rate 95.45% / 95.34% / 95.77%; withdrawn 6.11% / 6.64% / 5.92%; deleted 5.27% / 5.63% / 4.06% | RP US-59, S-42 |
| De Novo acceptance | none sourced | Not accepted or failed screening on first cycle: 30.11% / 14.29% / 10.61% | S-44 |
| De Novo decision | 150 FDA days; 70%, shown as 80% for FY 2026 and 90% for FY 2027 | 93.98% / 98.61% / 92.00% | RP US-47, RP US-60 |
| De Novo time | none | Average FDA days 130.60 / 121.26 / 132.16; industry days 139.47 / 126.25 / 145.96; total days 270.07 / 247.51 / 278.12; review cycles 1.69 / 1.61 / 1.68 | RP US-61, S-45 |
| De Novo outcomes | none | Granted 44.58% / 40.28% / 56.00%; declined 21.69% / 25.00% / 14.00%; withdrawn 20.48% / 18.06% / 10.00%; deleted 13.25% / 16.67% / 20.00% | S-46 |
| PMA decision | 180 FDA days for 90% (320 with advisory committee) | 98.55% / 96.88% / 97.26% | RP US-48, RP US-63 |
| Pre-Sub feedback | 90% within 70 days or 5 days before the meeting | 98.84% / 98.66% / 97.49%; average 62.20 / 62.25 / 61.89 FDA days | RP US-35, S-47 |
| Pre-Sub minutes | Sponsor sends minutes within 15 days | Past 15 days: 434 of 2,015 / 369 of 2,218 / 380 of 2,338 meetings | S-30, S-48 |

Reading rules:
- The 510(k) total-time goal and the report's average are computed differently (the goal on a trimmed cohort, S-29). Show both, say they are not the same measure, and do not call the gap a miss.
- The FY 2025 De Novo cohort was still open at the report date (RP US-62), so its rates may move.
- National or agency averages are context for the person's own rules, never their target.

## Agency questions while under review

| Event | What it means | What the sponsor can do | Rows |
|---|---|---|---|
| eSTAR technical screening deficiency | The 510(k) is on hold until a complete replacement eSTAR arrives | Replace within 180 days or the 510(k) is withdrawn | S-15, S-16 |
| Additional Information or Major Deficiency letter | FDA clock stops; the letter is based on a complete review and lists all deficiencies | Answer within the letter's timeline; a SIR can test the approach (21 days if sent within 60 days of the letter) | S-25, S-33 to S-35 |
| De Novo additional-information request | Clock stops | Complete response within 180 days or the request is withdrawn | RP US-13 |
| 510(k) past 100 FDA days | FDA gives written feedback on all outstanding issues | Meeting or teleconference | S-27 |
| De Novo past 180 FDA days | On request, FDA discusses outstanding issues | Request the discussion | S-32 |
| 510(k) Additional Information deadline | `[GAP]` in the files read | Read the letter; the letter's timeline governs | |

## Decision outcomes for comparables

- `regulatory-dh.get_pathway_precedents(product_code=...)` counts decisions by pathway and year and gives a median of calendar days between the stored submission and decision dates, mixing pathways in one product code (for example QFT: one De Novo and three 510(k)s in one median). Split by pathway with `get_authorization` per record and `scripts/review_clock.py comparables`.
- Describe each comparable only by what its record states (pathway, decision date, product code, predicates named in its summary, status code). Never infer why it took that long or what class or claims it has beyond the record.
- The library's US scope is FDA decisions (`list_jurisdictions`, 19 October 2026); a withdrawn or deleted submission is not a decision, so comparables found this way show decided devices only. Say so, and use the agency-wide rates above for the other outcomes.
- EU: the library's EUDAMED copy has no decision dates (3,142 of 3,142 empty), so EU time to certificate cannot come from the library. Use the notified body survey as context, labeled.

## Notified body timelines (context only)

From the 20th notified body survey, a contractor study commissioned by the Commission (data to 28 February 2026, published 2 July 2026; RP EU-40). Always label it so.

- Application to written agreement: under 2 months in 65% of cases (S-71).
- Written agreement to a new MDR certificate: 62% of notified bodies report 13 to 18 months for QMS certificates; for QMS plus product, 51% report 13 to 18 months and 31% report 19 to 24 months (RP EU-44, basis S-74).
- Refusals: 989 MDR applications since designation; main reasons outside designation scope (30%) and incomplete applications (25%) (RP EU-42, S-72).
- Completeness: 14 of 52 notified bodies report more than half of submissions complete (S-73).
- No software-specific breakdown (RP "Not sourced").

## Quality signals a team can watch in its own record

These are measures the sources define. Whether they matter, and what counts as good, is the person's rule.

- First-cycle acceptance or screening pass (S-15, S-23, S-38, S-44).
- Number of hold letters and review cycles (S-25, S-41, S-45).
- Sponsor days on hold versus FDA days (S-26, S-45).
- Pre-Sub minutes sent within 15 days (S-30, S-48).
- For the EU: application completeness and refusal reasons (S-72, S-73).
