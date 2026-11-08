# Claim card (render this shape)

Use **one card per atomic claim**. Atomic = one checkable proposition (RAGAS / FActScore practice).

```text
┌─ Claim #N ─────────────────────────────────────────
│ Claim:     <exact wording from the draft>
│ Status:    <plain words>     enum: supported|partial|unsupported|contradicted|unverifiable|out_of_scope|not_checked
│ Passage:   "<quoted deciding words, ≤1200 chars>"
│ Locator:   <page / § / URL fragment / "supplied text">
│ Action:    Keep | Rewrite to match | Remove | Ask person
│ Label:     tool-checked | not tool-checked
└────────────────────────────────────────────────────
```

## Plain-word status map

| Enum | Say to the person |
|---|---|
| supported | Found in the passage |
| partial | Partly found — name what matches and what does not |
| unsupported | Not found after checking admitted sources |
| contradicted | Passage says something different |
| unverifiable | Cannot check (missing / empty / inadmissible passage) |
| out_of_scope | Normative or definitional — leave out of faithfulness % |
| not_checked | No admitted source was checked — do not call this unsupported |

## Rules

1. Quote the passage; do not paraphrase the deciding words.
2. A match means the passage says it — **not** that it is true in the world (IFPMA/ABPI substantiation is a human/MLR step).
3. Offline / no key → every card **Label: not tool-checked**.
4. Never invent a figure to fill a gap (TR-H1).
