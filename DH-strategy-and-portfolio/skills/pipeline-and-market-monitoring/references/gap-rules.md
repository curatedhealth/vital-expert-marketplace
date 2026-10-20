# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Change reads

| Class | When | How to word it | Next step |
|---|---|---|---|
| Change recorded | The log holds an event-dated row in the window | Event, event date, source URL, "as of" retrieval date | B1 checks it against the person's triggers |
| No change recorded | The log holds no in-window row for a resolved company | "No change recorded in the library's log since DATE (log began 12 October 2026; last sweep DATE; event-dated rows only)" | None; it is not "nothing happened" |
| Before the log | The "since" date is earlier than the log's first entry | "Changes dated before the log began on 12 October 2026 may be missing"; never "no change" for that part | Offer the store's dated filings (`get_funding_signals`) and authorization decision dates (`build_company_profile`) for the earlier window, and the authority |
| Lookup missed | The name did not resolve (needs a live check for how this is reported) | "The lookup by NAME returned no row" | Use the store's exact legal name from the screen |
| Not covered | The source is not loaded (Companies House, Zefix, DiGA directory feed, NICE, private funding on 19 October 2026) | "The library does not load SOURCE: REASON; no change can be seen there" | Check the authority |
| Not published by the authority | The register does not publish the fact (DiGA refusals, DE32; Form D investors and valuation, DL-018; breaches under 500, DL-092) | "SOURCE does not publish this (row)" | Ask through the person's process |

## Company status

| Situation | How to word it | Next step |
|---|---|---|
| A primary filing or register entry was read | "Status: FORM or ITEM, filed DATE (source URL, read DATE)", with its "does not mean" line (`monitoring-signals.md` section 5) | None |
| Not read (no access, no SEC contact given, PACER account needed) | "Status: [GAP]: not read. Filings to open: COMPANY, IDENTIFIER, FORM or ITEM, where" | The person opens them, or gives the SEC contact their organization uses |
| Only a quiet log, an old latest filing or a company not returned in a screen | Never a status. "Status: [GAP]: not read" | As above |

## Screen reruns

| Situation | How to word it |
|---|---|
| Same arguments, company added or not returned | "Added" or "not returned in this run"; check `total_matches` and `limit` before reading "not returned" as anything |
| Different arguments | "Runs not comparable: arguments differ (list them); no change inferred" |
| Perimeter changed (source newly loaded or dropped) | "New coverage, not a market change" |

## Rule changes

| Situation | How to word it |
|---|---|
| A row states it | The change, instrument, date and row id |
| Adopted, not yet applicable | "Adopted DATE; applies from DATE (row)" |
| Status after the read date not found | "Status after DATE not found on the pages read `[GAP]`" (for example the HSR rulemaking after 26 May 2026, DL-054) |
| Not in this skill's sources | "Not in this skill's sources `[GAP]`" and name the owner who would know |
| Row marked "(inference)" | State it and "the research reader's inference across sources" |

## The person's facts

| Situation | How to word it |
|---|---|
| No "since" date | "not given" and ask; never pick one |
| No earlier saved screen | No screen comparison; offer to save this run as the baseline |
| No triggers for B1 | No review verdicts; lay out the changes and ask the person to set triggers |
| No owner or reread date | "owner not named" or "reread date not given" and ask; never suggest a job title or a date |
| A field the record lacks | "not in the record"; never 0, "none" or a country |
| Fact from confidential material | "From your material" beside it |

## Never

- Never read intent, distress, revenue, runway or a valuation into a change, a missing filing or a quiet log.
- Never treat "no change recorded" as "no change".
- Never fill a missing event from memory.
