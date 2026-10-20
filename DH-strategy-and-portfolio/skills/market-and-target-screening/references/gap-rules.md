# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Library and register facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Found | A company, product, authorization or filing row exists | Fact, date, source URL, "as of" retrieval date | None |
| Lookup missed | The name or identifier used found nothing, but another record suggests the company exists (for example a screen row with authorizations) | "The lookup by NAME returned no row" | Try the exact legal name, a brand, or an FDA, LEI, EUDAMED or SEC number |
| Covered, absent | The source is loaded and searched, and holds no row for this company | "Not in the library's copy of SOURCE (N records, as of DATE)" | Check the authority directly |
| Not covered | The source is not loaded (listed as not loaded, or the segment or jurisdiction is not in the perimeter) | "The library does not load SOURCE: REASON" | The library cannot answer; check the authority |
| Not published by the authority | The register itself does not publish the fact (DiGA refusals, DE32; Form D investor names and valuation, DL-018; breaches under 500, DL-092) | "SOURCE does not publish this (row)" | Ask the company, through the person's process |

## Company status

| Situation | How to word it | Next step |
|---|---|---|
| A primary filing or register entry was read | "Status: FORM or ITEM, filed DATE (source URL, read DATE)", with its "does not mean" line (`screening-rules.md` section 5) | None |
| Not read (no access, no SEC contact given, PACER account needed) | "Status: [GAP]: not read. Filings to open: COMPANY, IDENTIFIER, FORM or ITEM, where" | The person opens them, or gives the SEC contact their organization uses |
| Only a missing filing or a quiet log | Never a status. "Status: [GAP]: not read" | As above |

## Change-log window

This skill does not read the change log. If the person's period starts before the log began (12 October 2026), say so and offer the company's dated primary filings and authorization records for that period; never report "no change" for it.

Never turn any of these into "not authorized", "no competitor", "no breach", "no funding" or "empty market". `none_found` and `not_assessable` in a library response are not zero.

## Requirement facts

| Situation | How to word it |
|---|---|
| A row states it | The rule plus the row id |
| Not in this skill's sources (national FDI laws, 2025 HSR figures, FTC HBNR rows, Companies House PSC rules, state health privacy laws) | "Not in this skill's sources `[GAP]`" and name the owner who would know |
| Row marked "(inference)" | State the rule and "the research reader's inference across sources" |
| Rule adopted but not in force (EU 2026/1386 before 17 January 2028; Swiss IPG) | "Adopted, not yet applicable (row)" |

## The person's facts

| Situation | How to word it |
|---|---|
| No segment or jurisdiction for A1 | Ask once; do not pick one |
| No criteria or scores for B1 | No ranking. Lay out the A facts per candidate and ask the person to set criteria and score |
| Data volume, investor nationality, deal size not given | "not given" and list the question for the owner the person names for legal questions; never compute a threshold test |
| No owner | "owner not named" and ask; never suggest a job title |
| A field the record lacks | "not in the record"; never 0, "none" or a country |
| Fact from the person's confidential material | "From your material" beside it; never mixed into a public-record statement |

## Never

- Never fill a company's revenue, runway, valuation, round size, investors, outcomes or intent from memory or from a Form D.
- Never supply a market size, valuation multiple, return benchmark or sector funding total.
- Never treat a missing row as "not there".
