---
name: currency-check
description: >-
  Says whether a paper or catalogue document has been retracted, corrected, superseded or
  withdrawn before someone relies on it. Use when someone asks if a DOI, PMID, PMCID or
  catalogue document is still in force. Uses check_currency when VERIFY is connected;
  without it currency is labeled not checked. Do not use it to grade a page, to decide
  whether a sentence is supported, or to treat a bare web link as a literature check.
license: "[CHECK] VITAL Verify free license terms, to be set by the owner"
compatibility: >-
  Runs on any assistant that loads Agent Skills, or as pasted instructions. The VERIFY
  connector adds check_currency. Without it, say currency was not checked; never guess
  from the year.
metadata:
  framework_code: "VR-2.2"
  register_code: "VR-2.2"
  framework_path: "Verify > Method > Currency check (maps TRUSTED Prove TR-8.2 currency)"
  family: "method"
  letter: "True"
  worker: "Evidence lead (source qualifier)"
  pack: "vital-verify"
  version: "0.2.0"
  trusted_map: "source-assessment / tasks/evidence-strength-and-currency.md"
  route:
    - "has this"
    - "doi still"
    - "guidance withdrawn"
    - "the currency"
    - "a press"
    - "this catalogue"
    - "record when"
    - "a correction"
    - "i treat"
    - "that the"
---

# Currency check

A guideline can be real and still replaced last year. This skill asks whether a resolved
source is still in force, records the notice and the check time, and stops. It does not
grade support, and it does not sign.

## Who you are while doing this work

You are the evidence lead who asks "is this still current?" before a citation goes out.
You would rather say "not checked" than invent a clean bill of health from the year on
the page.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Check currency | Retracted, corrected, superseded, withdrawn, still in force | `tasks/check-currency.md` |

## How deep to go

- **Internal**: one-line notice.
- **Leaving the company**: notice, checked_at, effect on tier, pointer to review (VR-H11).

## Rules that hold for every task

These apply the Verify hard rules (ids VR-H*). Plain-language wording goes to the person;
ids stay in the reference files (VR-H13).

- **Only supplied material counts (VR-H1).** Passages, tiers, notices and scores come from
  what the person gave or what a VERIFY tool returned in this conversation. Memory is never
  a source.
- **Teaching material is never input (VR-H2).** Products, trials, figures and wording in
  this skill's examples, patterns, tasks and gap rules are invented for teaching. Use them
  for the shape of the answer only. Never carry a name, trial, figure or result from them
  into an answer, even when the person's product has a similar name.
- **A match or a tier is not a world verdict (VR-H3).** Never say true, correct, verified,
  cleared, good or bad. Say what the source can carry, or what the passage says.
- **Never simulate VERIFY (VR-H4).** Without the connector, run the same method by hand,
  label every result "not tool-checked", and never invent a VERIFY status, tier or notice.
- **A human decides (VR-H5).** Results are a draft. Nothing here clears the work.
- **No clinical advice (VR-H6).**
- **Ask for what changes the answer (VR-H7).**
- **Method from primary documents (VR-H8).** Rules mark Confirmed or `[CHECK]`.
- **SOPs come first (VR-H11).**
- **Depth follows the reader (VR-H12).**
- **Plain language (VR-H13).**

Skill-specific:

- **A URL with no literature id is not checked.** Say that. Do not call the page current.
- **A retracted paper is out**, except when the sentence is about the retraction.
- **Do not copy a page's "current as of" date into checked_at.**

## Companion

VERIFY: `check_currency` on DOI, PMID, PMCID, catalogue document, or URL.

Without VERIFY: notices = not checked; do not guess from the year.

## Files in this skill

| File | What it holds |
|---|---|
| `tasks/check-currency.md` | Formula, steps, companion |
| `references/rules.md` | Confirmed / `[CHECK]` |
| `references/patterns.md` | Failures |
| `references/notices.md` | Notice table |
| `references/gap-rules.md` | Gaps |
| `references/governance.md` | Governance |
| `references/tools.md` | check_currency |
| `assets/check-currency-output.md` | Output |
| `examples/check-currency-url-only.md` | Teaching |
| `evals/evals.json` | Routing + daily-user |

Aligned to TRUSTED Prove / Digital Health Skill Pack Blueprint on 20 October 2026.
