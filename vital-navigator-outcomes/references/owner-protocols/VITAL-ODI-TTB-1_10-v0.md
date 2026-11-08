# Owner protocol draft — Top-two-box proportions → locked 1–10 I/S

**Protocol id:** `VITAL-ODI-TTB-1_10-v0`  
**Status:** **SIGNED — Option A (no conversion)** (8 November 2026)  
**Conflict:** SC-C1C2-R2-03  
**Authority:** VITAL owner constitution + Strategyn 2019 as Lane A context (not automatic equivalence)

---

## 1. Purpose

Allow a **documented** bridge when a study collected Strategyn-style **top-two-box proportions** (or similar proportion shares) and the team needs cells on the Navigator **whole-number 1–10 Importance and Satisfaction** contract — without silent auto-conversion in code.

Signed **Option A** (8 November 2026): top-two-box proportions are **not** converted into Navigator 1–10 cells. `outcome_priority_check` continues to **refuse** top-two-box→1–10 bridges (this id is **not** on the Option B conversion allow-list). Test fixtures may still use `allow_unsigned_protocol_for_fixture: true` only for legacy draft-path tests.

---

## 2. Locked compute (unchanged by this protocol)

```
opportunity = importance + max(0, importance − satisfaction)
```

Inputs to that formula remain **integers 1–10**. This protocol does **not** authorize `I × S`, unclamped `I+(I−S)` ranking, or opportunity→money.

---

## 3. Required provenance (always)

Before any normalized 1–10 cells are submitted:

| Field | Required content |
|---|---|
| `raw_scale_kind` | e.g. `top_two_box_proportion` |
| `aggregation` | e.g. `top_two_box_share` |
| `owner_protocol_ref` | This protocol id once signed |
| `owner_protocol_ref` / study id | Instrument version, wording, anchors |
| Population / recruitment | Who was invited; who responded |
| Denominator | Base for each proportion |
| Missingness | Item-level reasons; no impute-as-minimum |
| Dates / mode | Field period; channel |
| `normalization_to_I_S` | `owner_protocol_ref` |

---

## 4. Mapping formula — deliberately empty until signed

**No default mapping is approved.**

Do **not** use:

- proportion × 10 as Importance/Satisfaction  
- arbitrary binning of % into 1–10  
- averaging top-two-box with ordinal ratings as if identical  

When signing, the owner must fill **one** of:

### Option A — No conversion (preferred)

Studies remain on their native scale for reporting; Navigator rooms collect **fresh** 1–10 people scores. Protocol used only to document that native proportions were **not** fed into `outcome_priority_check`.

### Option B — Study-specific mapping (must be written here)

```
[Owner fills: exact mapping from proportion / category → integer 1–10,
 including treatment of ties, missing, and multi-wave comparability.]
```

Option B requires a named statistician/owner reviewer and does **not** generalize to other studies without a new protocol version.

---

## 5. Signature block (HITL)

| | |
|---|---|
| Status after signature | `signed` in `REGISTRY.md` — Option A does **not** join conversion allow-list |
| Owner name | Hicham |
| Date | 8 November 2026 |
| Chosen option | **A** |
| Option B mapping attached | n/a |

**Option A signed = no runtime conversion bridge.** Option B would require a new protocol version + `SIGNED_OWNER_PROTOCOLS` entry.
