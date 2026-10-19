# Worked example: A1 on the recent German DiGA cohort

Live library calls on 19 October 2026. The library's DE_DIGA copy holds 82 listings, last loaded 15 October 2026.

**Request:** "We are about to get a DiGA trial listing. Before the board meeting I want to see how the most recent DiGA have fared: who is still on trial, who got through, who was deleted, and how long it took."

**Calls made**

1. `market-access-dh.list_schemes`: DE_DIGA loaded with 82 listings, last load 15 October 2026.
2. `market-access-dh.find_scheme_precedents` `{scheme: "DE_DIGA", limit: 25}`: the 25 most recent listings. A trimmed copy is saved as `de_diga_precedents_2026-10-19.json`.
3. `market-access-dh.get_status_history` for two rows, to check how history is stored. For Uroletics it returned two rows (trial from 16 December 2024, deleted 23 March 2026). For Vera-App it returned one row (permanent, dated 20 January 2026, "transition history not published").
4. `scripts/coverage_clocks.py de_diga_precedents_2026-10-19.json --as-of 2026-10-19` gave the table in `de_diga_clocks_2026-10-19.md`.

## Answer (short mode)

**What stands out.** Of the 25 most recent DiGA listings in the library, 12 are on trial, 7 are permanent and 6 were deleted. Five of the 12 trial listings have passed the 12-month trial period: hiToco and ORIKO at 15 months, elona explore at 20, companion shoulder and eCovery at 21. That means an extension or a pending decision, not a lapse. An expired trial stays listed and reimbursable until BfArM decides (BfArM DiGA guide v3.6).

**Deleted, with time from listing to deletion** (dates from the stored register text):

| Product | Listed | Deleted | Months |
|---|---|---|---|
| My Dose Coach | 16 June 2024 | 10 January 2025 | 6 |
| Uroletics | 16 December 2024 | 23 March 2026 | 15 |
| MindDoc auf Rezept | 8 February 2024 | 25 June 2025 | 16 |
| Vantis KHK und Herzinfarkt | 19 January 2024 | 10 June 2025 | 16 |
| actensio | 30 December 2023 | 1 October 2025 | 21 |
| Una Health für Diabetes | 9 February 2024 | 28 September 2026 | 31 |

Una Health was listed for 31 months, beyond the 24-month legal maximum. Treat that as a case to check (court route or pending decision), not as a pattern.

**National context.** To the end of 2025, 60 DiGA started on trial: 34 became permanent, 16 were deleted and 10 were still on trial. Trials averaged 20 months to a decision against the 12 the rules provide. About one in five that became permanent did so with a narrower scope. Source: GKV-Spitzenverband DiGA report of 1 April 2026, which is the payer's statutory report. These are what happened to other products, not a forecast for yours.

**Check at the authority.**
1. Vera-App: the library says permanent, but its stored register text says "vorläufig aufgenommen" (provisional). Check the BfArM directory.
2. The date each permanent DiGA moved from trial to permanent is not in the library `[GAP]`. The dates shown are listing dates.
3. Trial end dates are not stored. Clocks are counted from the listing date.

**Record:** Uncleared draft. Board-facing wording stops for the accountable owner.

## What this example shows

- Comparables come from the scheme's own rows, not memory.
- A passed trial period is stated as a signal to check, with the rule that the DiGA stays listed.
- The library's data quirks are shown to the person, not hidden: a status that disagrees with the passage, and listing dates that are not change dates.
