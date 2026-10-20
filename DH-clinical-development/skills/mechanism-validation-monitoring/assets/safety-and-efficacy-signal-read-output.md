# Output format: safety and efficacy signal read (draft for the person)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** version and periods as the person gave them ("not given" otherwise); thresholds and the date set; which signals crossed the person's threshold, which did not, which were not compared and why; reportability is the call of the owner the person names for vigilance reporting, or owner not named.
2. **Signals:** table Signal · Category (as the person assigned it) · Period · Value and basis · Person's threshold · Crossed / not crossed / not compared · Source (file, or record with date).
3. **Rule text for each crossed category:** quoted with its row (SE38 to SE48, SE53, SE59); no finding of "reportable", "serious" or "device-related", and no sentence tying a rule to a named signal; the owner applies the rule.
4. **Public records (named product only):** each recall or report summary as the record states it, with date and class; MAUDE counts are reports; no judgment of bearing on the product. If the connector is unavailable, say in the body: "saved records of 20 October 2026, not rechecked live".
5. **Routes:** reportability and clocks to dh-regulatory-and-quality audit-capa-and-complaints; risk file to dh-regulatory-and-quality design-controls-and-risk-management; claims after an efficacy signal to dh-regulatory-and-quality regulatory-submission-and-dossier; crossed signals to B1.
6. **Owner question (only if the person named no owner):** write "owner not named" and ask, before the record line: "Who owns reportability, the thresholds and the next step on each crossed signal, and who clears this draft? A name or role in your words."
7. **Record (last line of the answer body):** "Signal read draft. AI-assisted. No reportability, seriousness or causality decided; nothing called safe or effective." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
8. **Calls made (after the record line):** list.

## Full mode

### Answer
### Version, periods, denominators (as the person gave them)
### Signals and thresholds (the person's, date set, set before launch or not)
| Signal | Hazard it watches | Category | Threshold | Stop rule (person's words) | Blocks release (person's words) |
|---|---|---|---|---|---|
### Read per period
| Period | Signal | Value | Basis | Threshold | Result | Source |
|---|---|---|---|---|---|---|
### Categories counted without a threshold
### Efficacy measures against the person's thresholds
### Rule text that touches each crossed category (quoted, with rows)
### Public records for named products (as stated, with dates; if the connector is unavailable, "saved records of 20 October 2026, not rechecked live")
### Handed to B1, with routes
### Owner question (only if the person named no owner; before the record line)
"owner not named", then: "Who owns reportability, the thresholds and the next step on each crossed signal, and who clears this draft? A name or role in your words."
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
