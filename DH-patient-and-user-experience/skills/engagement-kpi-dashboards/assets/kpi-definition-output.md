# Output format: KPI definition

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the card(s) asked for, one line each: KPI, decision, numerator over denominator, period, definition row.
2. **Card table (compact):** KPI · Numerator · Denominator · Period · Grain · Source · Definition (row).
3. **Choices left to you:** the dose, days without use, threshold or denominator the person still has to set, one line each.
4. **Gaps:** fields missing, as `[GAP]`.
5. **Record:** "KPI card draft. Clears: NAME, the owner you named (or 'owner not named'; ask). Uncleared draft: once NAME clears it, the record is built with `verify.build_record`."
6. One line offering the full version.

## Full mode

### Answer

### KPI tree
| Decision (and who takes it) | KPIs that serve it |
|---|---|

### KPI cards
| Field | KPI 1 | KPI 2 |
|---|---|---|
| Decision | | |
| Numerator | | |
| Denominator | | |
| Period | | |
| Grain | | |
| Source table | | |
| Missing-data rule | | |
| Definition source (row) | | |
| Threshold and who set it | | |

### Where definitions overlap
One line per KPI where two frameworks define the word differently, with the person's choice or "to choose".

### Instrument-based KPIs
| KPI | Instrument | Measurement properties to check (COSMIN, reliability skill) | Gaps |
|---|---|---|---|

### Considered, not shown
| KPI | Why not |
|---|---|

### Gaps

### Record
KPI card draft. Definitions from the rows cited; every rule is yours. AI-assisted. Clears: NAME, the owner the person named, or "owner not named". Uncleared draft until NAME clears it; the record is then built with `verify.build_record`.
