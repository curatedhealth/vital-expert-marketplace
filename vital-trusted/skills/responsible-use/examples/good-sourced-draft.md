# Rendered example: HCP email drafted with AI (sourced draft)

Invented teaching case. Repaired greeting, use note, finding cards, gap list,
check-line stamp. Human gate and authorship made explicit; AI not listed as author.

## Original ask

"Polish this reply to Dr Chen and send it — she'll know I used ChatGPT."

Draft said: "As your AI clinical partner, I confirm Brand A is the safest choice with no
important risks."

## Fixed reply (person still must review before send)

> Dear Dr Chen,
>
> Thank you for your question about Brand A in adults with [indication per supplied label
> excerpt]. I am sharing a draft reply prepared with AI writing assistance; a medical
> colleague will review it before it reaches you. The summary below uses only the
> material attached in this thread: [GAP: SmPC section for risks not supplied — attach
> before stating safety frequencies].
>
> [No send until named reviewer clears — see use note.]

## Use note (`templates/use-note.md`, full)

Responsible use: who reads it, disclosure, authorship, language (draft)

Audience: HCP (Dr Chen); stakes: leaving the company if sent as-is.

Human oversight
1. Named medical reviewer required before send — not done in this conversation.
2. Request to "send without review" declined; route to medical information if needed.

AI use disclosure
1. Person intends to mention AI help; suggested plain line included in draft.
2. Whether your company requires a fixed disclaimer — ask publication / medical
   information policy `[GAP: policy not supplied]`.

Authorship
1. AI is not the author; named employee signs after review.
2. "AI clinical partner" removed — overstates AI role.

Language
1. Removed "safest" and "no important risks" — not supported in supplied excerpt; see
   FDA Bad Ad pattern for unsupported benefit/safety tone.

Next step: medical information or medical review per company procedure.

## Finding cards (shared `../../templates/finding-card.md`)

### Finding 1
- **Draft line:** "Send without review."
- **Issue:** Human gate missing for HCP-bound material.
- **Action:** Hold send; name reviewer role in use note.

### Finding 2
- **Draft line:** "As your AI clinical partner… safest… no important risks."
- **Issue:** AI role overclaimed; unsupported superiority and safety absolutes.
- **Action:** Disclosure wording + gap for risk data from label.

## Open items (`../../templates/gap-list.md`)

```text
Open items
1. SmPC or MI-approved risk wording — not supplied — next: Attach label section
2. Company AI disclosure text — policy not supplied — next: Medical information / publications

Not yet checked
- Whether Dr Chen question is solicited or unsolicited (MI routing)
```

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / responsible-use: not tool-checked (offline tools) · oversight: send blocked; disclosure: draft line; authorship: 1 overclaim repaired; language: 2 absolutes removed
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
Ethical · human oversight: HCP reply held for named reviewer (not tool-checked)
Ethical · AI disclosure: suggested plain disclosure, policy gap open (not tool-checked)
Ethical · authorship: AI-as-partner wording removed (not tool-checked)
Ethical · equity and inclusion: 0 stigmatizing phrases in supplied draft (not tool-checked)
```
