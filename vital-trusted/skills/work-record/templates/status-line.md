# Output format: status line

One line, used in the record note and, where the person wants it, on the work itself.
Only the person can raise a status above draft; the assistant records what they say
(TR-H5). This file is the one definition of the status forms for every TRUSTED skill.

## The status forms, and only these

| Situation | Status |
|---|---|
| Nothing stated | `Uncleared draft` |
| The person said a named person reviewed it, without clearing it | `Uncleared draft, reviewed by <name>, as you told me` |
| The person said who cleared it, with role and date | `Cleared by <name>, <role>, <date>` |
| A placeholder for a clearance still to come | `Uncleared draft (to be cleared by <name>, <role if given>)`, or with no name given, `Uncleared draft (to be cleared by a reviewer not named yet)` |
| The person says a named person cleared it, without role or date | `Uncleared draft (you said <name> cleared it; add role and date to record the clearance)` |

No other form is written: no "[Cleared by: name, role, date]", no "To be cleared by:" as
a status of its own, no standalone "Reviewed by" line, no "approved" in TRUSTED's voice.

- **A clearance reported in the past without role or date** is written `Uncleared draft
  (you said <name> cleared it; add role and date to record the clearance)`. A clearance
  still to come keeps any role given: `Uncleared draft (to be cleared by <name>, <role if
  given>)`. Never write "Cleared by <name>" with a part missing or left in brackets.
- **Comments received** are a note under the status, not a status: `Comments from <name>
  received <date>, as you told me.`
- **Process and reference** go on their own line after a cleared status: `Process: <your
  process>; reference: <as given>; as you told me.` Leave out a reference that was not
  given.
- **Final, confirmed:** draft markings removed; the status reads `Cleared by <name>,
  <role>, <date>` with the process line.

## Rules

- Every record output shows a status line, at every size: the one-line note, the short
  note, the full note and the reply to "mark this as final". Never leave it out. It is
  written `Status: <one of the forms above>.`
- The status line sits in the record note, or in a note after the text. It never stands
  alone at the top of an email body or of a reply.
- Every name, role and date comes from the person. Never fill one in.
- Dates in full: "16 October 2026".
- "As you told me" stays in the record note. On the work itself the person may drop it,
  since the statement is now theirs.
