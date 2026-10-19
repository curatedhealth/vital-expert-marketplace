# Output format: definition quality and drift

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the KPIs that cannot be recomputed as written (fails), the KPIs whose dashboard formula drifted, and any data gap that changes a number.
2. **Findings (compact):** KPI · Finding (fail, check, drift, no card) · Field · Row.
3. **Questions for you:** the checks that need your reading, at most three.
4. **Data notes:** missing and inconsistent rows, one line.
5. **Record:** "Definition check draft. Clears: NAME, the owner you named (or 'owner not named'; ask). Uncleared draft: once NAME clears it, the record is built with `verify.build_record`."
6. One line offering the full version.

## Full mode

### Answer

### Card quality
| KPI | Check | Status (pass, fail, check) | Note | Row |
|---|---|---|---|---|

### Drift: card against dashboard
| KPI | Finding (match, drift, renamed, no card, not shown) | Field | Card | Dashboard |
|---|---|---|---|---|

### Event data
| Item | Count |
|---|---|
| Blank user_id / event_date / event_type | |
| Invalid dates | |
| Duplicates | |
| Events after the as-of date | |
| Events before a start | |
| People with no start event | |
Events per month: list; months with none flagged as "feed outage or real stop".

### Instrument-based KPIs
| KPI | Instrument | Evidence named | COSMIN properties covered |
|---|---|---|---|

### What it means for you

### Gaps

### Record
Definition check draft. Checks say whether a card is computable, not whether its value is good. AI-assisted. Clears: NAME, the owner the person named, or "owner not named". Uncleared draft until NAME clears it; the record is then built with `verify.build_record`.
