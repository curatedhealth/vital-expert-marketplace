# Task TR-2.2.2 Required statements

## Formula

| Slot | For this task |
|---|---|
| Worker | Regulatory and promotional reviewer with a privacy background |
| Workflow | Establish market, reader, use and channel; build the list of statements usually expected; mark each present, missing or for the company's system; never write one from memory |
| Skill | TR-2.2.2 |
| Knowledge | `references/rules.md` (M1 to M19), `references/patterns.md` (S1 to S8) |
| Tool | `scripts/scan_output.py --statements` where code can run. Companion slot: future MLR preparation companion with market templates and job codes (none yet) |
| Prompt | This guide |
| Template | `assets/statements-list.md`, `assets/market-note.md`, `assets/check-line.md` |
| Input | The draft, the context card, the supplied label for the market, any template or element list the person supplies |
| Governance | TR-H1, TR-H2, TR-H3, TR-H7, TR-H8, TR-H11, `references/governance.md` |

## When it runs

Promotional or external material about a product, at "leaving the company" depth: an
email to doctors, a deck for an HCP meeting, a social post, a website page, a leaflet,
an exhibition panel, a journal advertisement. Not for a reply to a doctor's own
unsolicited question (that follows the company's medical information procedure; name
it), internal material, or material that names no product.

If the person supplies their company's template or element list for this market, use
it as the list and do not add to it from the rules below. Their list governs (M0).

## The elements usually expected

Build the list from `references/rules.md` for the market only. Common elements:

| Element | UK (ABPI 2024) | EU (Directive, EFPIA) | Switzerland (AWV) | US |
|---|---|---|---|---|
| Prescribing information or essential information, or where to find it | Yes (M6) | Essential information compatible with the SmPC (M1, M5) | Mandatory items (M11) | Brief summary in advertisements (M14); emails and brochures `[CHECK]` (M15) |
| Date of preparation or last revision | Of the material (M7) and of the PI (M6) | Of the essential information (M5); of documentation (M3) | Not in Article 6 as read | `[CHECK]` |
| Supply or dispensing classification | Legal classification in PI (M6) | Yes (M1, M5) | Dispensing category (M11) | `[CHECK]` |
| Side-effect reporting statement | Yes, set wording (M7); patient version (M8) | National code `[CHECK]` (M19) | `[CHECK]` (M13) | `[CHECK]` |
| Black triangle | When required (M7) | National rules `[CHECK]` | `[CHECK]` | Not applicable as read |
| Audience statement | Usual practice `[CHECK]` (M18) | Usual practice `[CHECK]` | Usual practice `[CHECK]` | Usual practice `[CHECK]` |
| Job code or reference | Company system (M17) | Company system | Company system | Company system |
| Authorisation holder name and address | In PI (M6) | National `[CHECK]` | Yes (M11) | `[CHECK]` |

A market not in this table: say the rules for that market were not read here, list
only the company-system elements (job code, date), and point to the review process.

## Guard (while drafting)

1. **Confirm the market, reader, use and channel** from the context card or the
   jurisdiction task. Without the market, do not build a list; ask.
2. **Build the list** for that market from the table, or from the person's own template.
3. **Place each element as a visible placeholder** where it belongs, never as text you
   wrote: `[Prescribing information: link to the current UK PI — from your PI owner]`,
   `[Job code — from your approval system]`, `[Date of preparation — set at approval]`.
4. **Use set wording only where the rule gives it and the market matches**: the ABPI
   adverse event statement for UK material, the AWV public notice for Swiss category C
   or D public advertising. Even then, the link and company name come from the person.
5. **Never write prescribing information, a safety summary or a dispensing category
   from memory.** Take it word for word from the supplied label for that market, or
   leave the placeholder.
6. **Do not decide the reminder exemption.** If the person says the piece carries only
   the name, note that some markets exempt reminders (M1, M5) and that the review
   process decides.

## Repair (existing draft)

1. **List what the draft carries** at the end, the start and in footers: PI or link,
   safety text, reporting line, audience line, dates, codes, legal entity. Where code can
   run, use `scripts/scan_output.py <draft.txt> --statements --market <UK|EU|CH|US>` to
   find cues, then read each hit.
2. **Mark each expected element**: present; present but from another market; present
   but not traceable to a supplied source (for example a job code nobody supplied);
   missing.
3. **Fix:** add placeholders for missing elements; replace another market's element with
   a placeholder for the right one; turn any untraceable code, date or PI text into a
   placeholder and say so.
4. **Never complete a job code, date or PI from a pattern** ("the other codes look like
   ZL-UK-0123, so this one is ZL-UK-0124"). It belongs to the company's system.
5. **Return the list** with `assets/statements-list.md`.

## Check line

See `assets/check-line.md`.

## Boundaries

- Whether the content of the PI or safety text matches the label is `claims-and-label`
  and `patient-safety`. This task asks whether the element is there and from the right
  market.
- Whether fair balance holds in the body is `balanced-evidence`.
- The list is "usually expected for this kind of material in this market". It is never
  the complete list and never a finding that the material has everything it needs.
