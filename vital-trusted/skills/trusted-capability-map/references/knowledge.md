# Knowledge: trusted-capability-map

## What this skill owns

Routing and explanation of the TRUSTED kit: which Core/Build/Prove skills apply, which
letters are on, and where shared cards live. It does **not** run letter repairs or Prove
checks itself.

## Default routes (everyday)

| Ask shape | First stop | Then |
|---|---|---|
| Missing market/use/reader | `trusted-intake` | `trusted-check` at the right depth |
| Colleague light note | `trusted-check` (light) | Build letters only if something would mislead |
| External / promotional / payer | `trusted-intake` → `trusted-check` (full) | Prove companions when True needs passage checks |
| Doctor dosing / AE question | `trusted-intake` → `patient-safety` → `claims-and-label` | Company MI process (named, not replaced) |
| "Just mark supported/approved" | Refuse unchecked labels | Offer check now or label not checked |

## Shared cards

Prefer `../../templates/` — claim-card, source-card, confidence-card, evidence-table,
gap-list, verify-brief, check-line-stamp. See `templates/README.md`.

## Honesty rules

- Prefer supplied material over model memory.
- Mark missing inputs `[GAP]`; untraced norms `[CHECK]`.
- No invented skill results; no send-ready verdicts from the map alone.

# Failure modes

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-CM-01 | Skip intake routing | Was a doctor question routed straight to draft-and-send? | Routing | TRUSTED capability-map | VERIFIED practice |
| FM-CM-02 | Invented skill results | Did the map declare Safe/Rule-compliant fine without those skills? | Honesty | TR-H4 | VERIFIED practice |
| FM-CM-03 | Replaced company SOP | Did routing name or replace a company MI/MLR procedure? | Process | TR-H11 | VERIFIED practice |
| FM-08 | Tool status treated as world-truth | Is a local or Verify status described as "true in the world"? | Prove honesty | VERIFY / TRUSTED Prove | VERIFIED |

Skill-specific rows for `trusted-capability-map`. Shared FM-08 is universal Prove honesty.
