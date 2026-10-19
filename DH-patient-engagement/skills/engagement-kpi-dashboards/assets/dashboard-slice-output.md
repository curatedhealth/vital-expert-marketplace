# Output format: dashboard slice and tracking job

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** per audience, the KPIs placed, the refresh cadence and the owner paged on failure.
2. **Slice (compact):** Audience · Decision · KPIs placed · Threshold (set by) · Cadence · Owner paged.
3. **Not placed:** KPIs left off and why, one line.
4. **Stops:** external audiences or claim-like KPIs, one line each, with the owner.
5. **Record:** "Dashboard plan draft. Clears: NAME, the owner you named (or 'owner not named'; ask). Uncleared draft: once NAME clears it, the record is built with `verify.build_record`."
6. One line offering the full version.

## Full mode

### Answer

### Audiences and decisions
| Audience | Decisions it takes (your words) |
|---|---|

### Dashboard per audience
| Audience | KPI (card) | Numerator / denominator | Period and grain | Threshold (set by) | Status (ready / not ready: field) |
|---|---|---|---|---|---|

### Tracking job per dashboard
| Dashboard | Refresh job | Cadence | Owner paged on failure | How a failed refresh shows | Timestamp shown |
|---|---|---|---|---|---|

### Ranking (only with your scores)
| Option | Your numbers | Score | Order |
|---|---|---|---|

### Considered, not placed
| KPI | Audience | Why not |
|---|---|---|

### Stops for the owner

### Gaps

### Record
Dashboard plan draft. Audiences, thresholds and owners are yours. AI-assisted. Clears: NAME, the owner the person named, or "owner not named". Uncleared draft until NAME clears it; the record is then built with `verify.build_record`.
