# Worked example: A2 agency questions and decision tracking on live library data

Run on 19 October 2026 against the VITAL Digital Health Library. The product is a hypothetical prescription CBT app for insomnia filed as a 510(k) in product code QVO with predicate K233577 (as the person's regulatory owner decided). The event dates are the person's (sample file `examples/events-sample.csv`). Trimmed outputs: `examples/live/`.

## The request

"Our insomnia app 510(k) was received 4 May 2026. We got an AI letter on 26 June 2026 (questions on software testing and labeling) and answered on 14 September 2026. Where are we, and how long did similar apps take?"

## Calls made (7 counted, 1 free, plus the script)

1. `regulatory-dh.list_jurisdictions()` (free): US 1,226 decisions loaded, last load 19 October 2026.
2. `regulatory-dh.search_devices(query="Somryst", jurisdiction="US", limit=5)`: K191716, QVO.
3. `regulatory-dh.get_pathway_precedents(product_code="QVO", jurisdiction="US")`: 2 510(k)s, median 271 calendar days.
4. `regulatory-dh.find_predicates(product_code="QVO")`: K233577 names K191716; K191716 names DEN160018.
5. `regulatory-dh.get_authorization(reference="K233577")`.
6. `regulatory-dh.get_authorization(reference="DEN160018")`.
7. `regulatory-dh.get_pathway_precedents(product_code="PWE", jurisdiction="US")`: the De Novo's own code, 2 decisions.
8. `regulatory-dh.generate_report(reference="K191716", template="regulatory")`: predicate chain; EU status shown as `false` (not used; see `tools.md`).
9. `scripts/review_clock.py events` and `comparables` on the saved rows.

## The answer (short mode)

**Answer.** As of 19 October 2026 your 510(k) has used 88 FDA days of the 90-day goal, with the clock running again since your response on 14 September 2026. You spent 80 days on hold. The next sourced trigger: if there is no decision by 100 FDA days, FDA gives written feedback on all outstanding issues (S-27).

**Clock**

| Measure | Value | Basis | Row |
|---|---|---|---|
| FDA days | 88 | Calendar days under FDA review, clock stopped 26 June to 14 September | S-25, S-26 |
| Sponsor days | 80 | Calendar days on hold | S-26 |
| Total | 168 | Calendar days since receipt | |
| Decision goal | 90 FDA days for 95% | MDUFA V goal | RP US-46 |
| FDA actual | 97.94% within 90 FDA days; 141.24 average total days | FY 2025 cohort | RP US-57, RP US-58 |

The day counts are calendar-day differences between your dates; FDA's own same-day counting is not sourced here.

**Open questions.** One AI letter (26 June 2026): software testing and labeling. Answered. No open letter recorded.

**Comparables in QVO and its De Novo origin (records only)**

| Device | Pathway | Received | Decided | Calendar days |
|---|---|---|---|---|
| K191716 Somryst | 510(k) | 26 June 2019 | 23 March 2020 | 271 |
| K233577 Sleepio | 510(k) | 7 November 2023 | 5 August 2024 | 272 |
| DEN160018 reSet | De Novo (code PWE) | 16 May 2016 | 14 September 2017 | 486 |

Calendar days between the dates FDA's records state, including time on hold; not FDA days, so not comparable with the 90-day goal. Decided devices only. These describe what happened to other devices, not a forecast for yours.

**Record.** Uncleared draft, AI-assisted.

Full version available: adds the event log, the full goal-versus-actual table and the response routes.

## What the run showed about the tools

- `get_pathway_precedents` gives a calendar-day median that mixes pathways (QFT: one De Novo with three 510(k)s); splitting needs `get_authorization` per record.
- De Novo status is returned as the raw code "DENG".
- `generate_report` marks EU authorization `false` where the EUDAMED copy simply holds no decision data (register C2 evidence).
