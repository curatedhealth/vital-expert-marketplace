# Task TR-8.1.2 Decide support for each claim against a quoted passage (Part B)

Absorbs the support-decision method of the earlier vital-verify plugin.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Confirm each source was admitted, check each claim against its quoted passage, read each result in plain words, act on it, recheck any rewrite |
| Skill | TR-8.1.2 |
| Knowledge | `references/rules.md` (R1–R6), `references/patterns.md` (C5–C12, C15) |
| Tool | VERIFY `check_claim` (one claim, one passage) or `verify_text` (first pass on supplied text with named sources) |
| Prompt | This guide |
| Template | `assets/support-result.md`, `assets/check-line.md` |
| Input | The claim list from Part A, the quoted passages, the sources as admitted by `source-assessment` |
| Governance | TR-H1, TR-H3, TR-H4, TR-H5, TR-H11 |

## What "supported" means

Tell the person this in plain words every time results are shown:

> A match means the passage you gave says the same thing as the sentence. It does not
> mean the sentence is true, that the source is good, or that the work is ready. VERIFY
> compares words in the sentence with words in the passage.

A sentence can match a weak source, an old source or the wrong source. Source quality is
`source-assessment`. Whether the work may go out is the company's review process.

## Steps

1. **Admit the sources first.** `check_claim` expects the source to have been admitted by
   `qualify_source`. If that has not run, hand to `source-assessment`. If a source came
   back inadmissible, every claim resting on it is out (see "unverifiable" below).
2. **Choose the call.**
   - For a short text with a few named sources: `verify_text` with the text and the
     sources, as a first pass. One counted call; at most 60 findings, so split longer
     text first.
   - For a claim that needs its exact passage tested, or a rewrite: `check_claim` with
     the claim, the quoted passage and its locator, and the admitted source.
   - Exact arguments: `references/tools.md`.
3. **Never send a passage you wrote.** The passage field takes words quoted from the
   source. If there is no passage, do not invent one to make the call work.
4. **Read each result** with the table below and take the action it names.
5. **Recheck every rewrite.** A rewritten sentence is a new claim. Check it again before
   it stays in the text. Without VERIFY, label it "rewritten, not tool-checked".
6. **Hand on.** Status counts go to `confidence-scoring`; sources and passages that stay
   go to `citation-and-record`. Do not compute the confidence figure here.

## Each result in plain words, and what to do

| VERIFY status | Say to the person | Do |
|---|---|---|
| `supported` | "Your passage says this." | **Keep** as written. Show the passage next to it. |
| `partial` | "Your passage says part of this. It does not say <the missing part>." | **Rewrite to match**: keep only what the passage states, drop the rest, recheck. Do not swap the dropped part for another figure. |
| `unsupported` | "Your passage does not say this." | **Remove**, or **ask** for a passage that does. It is not shown to be false, only not supported by what was supplied. |
| `contradicted` | "Your passage says something different: <quote>." | **Ask.** Show both. Do not send the sentence. Rewrite to the passage only if the person confirms, then recheck. |
| `unverifiable` | "This could not be checked: <no source, source not admitted, or no passage>." | **Remove.** The sentence stays out until a checkable passage is supplied. Never replace it with a likely value. |
| `out_of_scope` | "This is an opinion, recommendation or definition, not something a passage can settle." | **Leave to the person** and their review process. It is not counted as checked. |

Reading rules:

- A number, a named person, a quotation, or a compliance or performance claim stays only
  when `check_claim` returned it as supported from a quoted passage (R5). On `partial`,
  the figure, name or quote is the first thing to drop.
- `unsupported` is not "false". `contradicted` needs a passage that says the opposite,
  not one that is silent (C6).
- An unnamed authority ("experts agree", "guidelines recommend") is not a source. Treat
  the claim as having no passage unless the person names and supplies the source.
- Word overlap can mark a weaker or older sentence as supported. When a passage states
  something narrower or dated, say so even on `supported`.
- `[CHECK]` From the earlier vital-verify method, not the schema: a passage from a
  low-tier (bronze) source yields at most `partial`. Report what VERIFY returned; do not
  upgrade or downgrade it yourself.

## Without VERIFY: the same method by hand

Run every step. Compare each claim with its passage yourself and use these result words,
never VERIFY's status words, so no one mistakes a manual reading for a tool result:

| Manual result (not tool-checked) | Do |
|---|---|
| Found in your passage | Keep; show the passage |
| Partly found: <missing part> not in your passage | Rewrite to match |
| Not found in your passage | Remove or ask |
| Your passage says something different | Ask |
| No passage to compare with | Remove |
| Opinion, recommendation or definition | Leave to the person |

Head the result "Not tool-checked: I compared each sentence with your passages by hand."
Add one line: "VERIFY would test each sentence against its passage; connect it if this
needs to be shown." The check line carries `[GAP: not checkable here — …]`. Do not give
a confidence percentage for a manual check.

## When asked to mark claims supported without a check

Decline in plain words, without lecturing: "I can't mark these supported without
comparing them with a passage. A result nobody checked would look the same as one that
was, and a reviewer would rely on it." Offer one of: run the check now; label them "not
checked" so they go to review as open items; or list which passages would be needed.
Never produce the labels anyway (`references/governance.md`).

## Check line

See `assets/check-line.md`.

## Boundaries

- Part B decides support against supplied passages only. It does not search for sources,
  grade them, check currency or build citations.
- It does not judge clinical meaning, fair balance or whether a claim is permitted. Flag
  and route (`balanced-evidence`, `claims-and-label`).
- It never says the work is accurate, correct, verified or ready.
