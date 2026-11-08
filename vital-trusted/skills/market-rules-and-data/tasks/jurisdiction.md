# Task TR-2.2.1 Jurisdiction

## Formula

| Slot | For this task |
|---|---|
| Worker | Regulatory and promotional reviewer with a privacy background |
| Workflow | Establish the market and the reader, find wording, approvals and rules from another market, check who else could read it, ask what is missing |
| Skill | TR-2.2.1 |
| Knowledge | `references/rules.md` (M1 to M12), `references/patterns.md` (J1 to J8) |
| Tool | None. Companion slot: future MLR preparation companion with market templates (none yet) |
| Prompt | This guide |
| Template | `assets/market-note.md`, `assets/check-line.md` |
| Input | The request, the draft, the context card (reader, market, product status, use), any supplied label |
| Governance | TR-H1, TR-H3, TR-H7, TR-H8, TR-H11, `references/governance.md` |

## What to establish first

| Question | Where the answer comes from | If missing |
|---|---|---|
| Which market will read it? | The person, the context card, the "to" line, the language, a named country | Ask, when the work leaves the company and is about a product |
| Who will read it? | Greeting, channel, request ("for our reps", "for the website") | Ask "Who will read this?" |
| Where is the product approved, for what? | The supplied label for that market, or what the person states | Do not write approval status; leave a gap |
| Which channel? | Email, printed piece, website, social post, congress stand | Ask if it could reach a different reader |

A piece for several markets (a "global" or "EU" deck) has several jurisdictions. Ask
which markets it will actually be used in, and whether each affiliate adapts it.

## Guard (while drafting)

1. **Fix the market before the first product sentence.** If the context card holds it,
   use it. If not and the work leaves the company, ask, with a plain reason: "Which
   country? What can go in an email to doctors differs between countries."
2. **Write in that market's terms.** Use the name of the label document in that market
   (summary of product characteristics in the EU and UK, the Swiss product information,
   US prescribing information) only as the person or the supplied label names it. Never
   carry over another market's headings, approval wording, reporting route or price
   format.
3. **State approval only for the market it was granted in, and only from a source.** "Approved
   in [market] for [indication], per the label you supplied." Without a label or a
   statement from the person, use `[GAP: not supplied — approval status in <market> —
   the approved label for <market>]`.
4. **Check who else can read it.** A public social post, an open web page, a press
   release or a patient leaflet reaches the public. Material about a prescription
   medicine that is meant for doctors must not drift into those channels without the
   review process deciding (M2, M4, M7). Ask where it will be posted when the channel is
   open.
5. **Keep rules in their own market.** Use a rule from `references/rules.md` only for
   the jurisdiction listed against it. A UK industry code line does not belong in a
   Swiss email; a US guidance does not govern an EU deck.

## Repair (existing draft)

1. **Find the market signals** in the draft: regulator names (FDA, EMA, Swissmedic,
   MHRA), approval phrases ("FDA-approved", "EU-approved", "now approved"), label
   headings, reporting routes (MedWatch, Yellow Card), currency and price formats,
   audience lines, legal entity and address.
2. **List each signal against the target market.** For each one: fits the market; from
   another market; approval stated with no source; reaches a reader it was not meant for.
3. **Fix:** replace another market's wording with the target market's term only where
   the person or the supplied label gives it; otherwise mark a gap. Remove approval
   statements for other markets unless the person wants them and the review process
   decides. Move or flag content that could reach the public.
4. **Never rewrite a claim to fit a label you do not have.** Whether a claim is within
   the label is `claims-and-label`; hand it there.
5. **List every change** in the note.

## Check line

See `assets/check-line.md`.

## Boundaries

- Whether a statement is within the approved label or intended use is
  `claims-and-label`. This task asks whether the right market's label and wording are
  being used at all.
- Whether a piece is promotion or scientific exchange is decided by the company's review
  process. Record the use the person states, or the careful assumption from
  `trusted-intake`.
- No market's rules are stated from memory. If the market is not in `references/rules.md`,
  say the rules were not read here and point to the review process.
