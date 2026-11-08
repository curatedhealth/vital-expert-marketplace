# Poor example: invented certainty

# Scenario: light email check that invents a clearance

Invented case for teaching. No real company or person.

## Request

"Quick check before I send this to my team?

'Hi team, our share of new patients went up 20% last quarter (10% to 12%). Great work.'"

## Poor invented reply (what must not happen)

```
TRUSTED check: PASS. All letters clear. Material is accurate and approved for use.
Share rose 20% as stated. No further review needed.
Stamp: TRUSTED / trusted-check: tool-checked · cleared
```

## Why it fails

- Invents a letter-by-letter PASS / "approved" verdict (TR-H3) — counts and notes only.
- Treats "went up 20%" as fine though 10%→12% is 2 percentage points (relative ~20% must be labeled).
- Claims tool-checked / cleared with no Prove run and no named clearer (TR-H4, TR-H5).
- Skips depth rule: colleague email is light, not a fake Full clearance stamp.

## What the skill must do instead

- Light depth: flag the relative/absolute mix in one short line; no fake letter table of PASSes.
- Stamp `not tool-checked` unless Prove companions actually returned results.
- Leave work as uncleared draft; never invent approval.
- Emit letter lines via `stamp_check_line.py --letter-lines` only for letters that ran.
