# Output format: risk control effectiveness from post-market data

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line.

## Short mode (default for a direct question)

Limits: the Answer is at most 60 words; each "Signal for the owner" cell at most 35 words; open items one line each. The hazard table carries no source column; put one line under it naming the source and retrieval date (for example "All comparable rows: FDA recall via library, retrieved <date>").

1. **Answer:** two or three sentences: how many own and comparable events were read (events, not rows), how many map to hazards in the file, how many map to none, and where observed severity exceeds the file. Coverage caveat (EU vigilance and Swiss field safety actions not in the library).
2. **By hazard:** Hazard · Own events · Comparable events · Highest observed vs file (your scale) · Signal for the owner.
3. **Not foreseen candidates:** events that map to no hazard, one line each.
4. **Open items:** mappings still "proposed", with observed severity asked on the person's scale (for a dose display or entry fault, severity turns on whether the pump received the displayed, the intended or a different amount: ask them to compare delivery history with app logs for each complaint); own events with no recorded reporting decision (for the vigilance owner).
5. **Record:** "Draft for the owner. Mapping, severity and effectiveness are yours. Uncleared AI-assisted draft." or the clearer's name.

## Full mode

### Coverage
The `list_jurisdictions` line; calls made with arguments; period; own data received.

### Events
| Event id | Origin (own / comparable) | Date | Firm, product line | Recall class or alert type | Failure as recorded | Hazard (confirmed / proposed: basis) | Observed harm | Severity (yours) | Source, retrieved |
|---|---|---|---|---|---|---|---|---|---|

### Against the risk file
| Hazard | File severity | File probability | Controls | Own events | Comparable events | Highest observed | Flag |
|---|---|---|---|---|---|---|---|

Possible outcomes per hazard (foreseen within estimate; foreseen, worse; foreseen, control did not prevent; not foreseen) are listed for the owner, not chosen.

### Not foreseen candidates
Each unmapped event with the hazard chain it suggests, labeled proposed.

### Reporting questions for the vigilance owner
Own events that may meet a definition, with the clock that would apply and the awareness date to confirm. No deadline computed from an unconfirmed date.

### Gaps and sources
Store gaps; rows without recall numbers; numbered sources with retrieval dates.

### Record
Risk file updates, CAPA and reporting decisions stop for the owner. Cleared by NAME, or uncleared. AI-assisted draft.
