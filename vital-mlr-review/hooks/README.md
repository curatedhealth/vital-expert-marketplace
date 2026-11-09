# READY hooks (routing triggers)

These are **skill-routing hooks** for Cowork / Agent Skills hosts — not OS automation. When the person's words match a trigger, prefer the named skill before chairs.

| Hook id | Trigger phrases (examples) | Route to |
|---|---|---|
| `H-channel` | scientific exchange, unsolicited request, med info letter, non-promotional | `mlr-channel-intent` |
| `H-claims` | claims matrix, annotate references, evidence locator, claim inventory | `mlr-claims-matrix` |
| `H-isi` | fair balance, ISI, important safety information, brief summary, net impression | `mlr-fair-balance-isi` |
| `H-intake` | jurisdictions, markets, open MLR intake | `mlr-intake` |
| `H-board` | board pack, prep record, named human for MLR | `mlr-board-prep` |
| `H-reconcile` | reconcile findings, re-queue chairs, revision loop | `mlr-compile` + `workflows/reconcile-after-findings.md` |
| `H-refuse` | approve / mlr_reviewed / cleared for promotion / file Form 2253 / submit to FDA | Refuse — never-approve; post-clearance filing deferred |

Machine-readable twin: `routing-hints.json` (not named `hooks.json`: Claude Code loads `hooks/hooks.json` as event hooks, and this routing table is not in that schema). Post-clearance: `references/post-clearance-deferred.md`.
