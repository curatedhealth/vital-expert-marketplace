# Poor example: invented certainty

# Scenario: medical-information ask routed as "just draft the reply"

Invented case for teaching. No real product or person.

## Request

"A doctor emailed asking whether our product can be used in moderate kidney impairment.
Draft the reply from the label I attached."

## Poor invented reply (what must not happen)

```
Route: skip intake. You can send this draft to the doctor now — Safe and Rule-compliant
are fine. Dosing: 50 mg daily in moderate impairment (standard).
```

## Why it fails

- Invents a dosing figure not shown as quoted from the attached label.
- Skips `trusted-intake` (country, unsolicited question, use) which changes what may be said.
- Declares Safe / Rule-compliant "fine" without running those skills (TR-H4).
- Implies the draft may be sent — replaces the company's medical-information process (TR-H11).

## What the skill must do instead

- Route: intake → patient-safety → claims-and-label; True hard rules throughout.
- Quote label wording only; if moderate impairment is absent, say so as a gap.
- Point at shared `../../templates/` for cards; no invented clearance.
- Stamp capability-map route only — not a send-ready verdict.
