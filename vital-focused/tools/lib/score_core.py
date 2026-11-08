"""Local weighted score + ±10 robustness (FOCUSED offline).

SYNC: formula family matches mcps/decision_companion/score.py (content pack 0.4.0+).
Never names a winner. No network.
"""

from __future__ import annotations

from typing import Any

LABEL = "Your own weights and ratings, added up. This does not choose for you."
ROBUSTNESS_FRACTION = 0.10
TIE_TOLERANCE = 0.005
_EPS = 1e-9
DEFAULT_SCALE = {"min": 1.0, "max": 5.0, "name": "playbook_1_5"}


def _scale(row: dict[str, Any]) -> dict[str, Any]:
    scale = row.get("scale") if isinstance(row.get("scale"), dict) else DEFAULT_SCALE
    return {
        "min": float(scale.get("min", 1)),
        "max": float(scale.get("max", 5)),
        "name": str(scale.get("name") or "custom"),
    }


def _criteria(row: dict[str, Any]) -> list[dict[str, Any]]:
    return [c for c in (row.get("criteria") or []) if isinstance(c, dict) and c.get("name")]


def _scaled(value: float, scale: dict[str, Any], *, invert: bool) -> float:
    lo, hi = scale["min"], scale["max"]
    if invert:
        value = hi + lo - value
    return ((value - lo) / (hi - lo)) * 100.0


def _same_option(cell: dict[str, Any], option: dict[str, Any]) -> bool:
    tokens = {str(cell.get("option_id") or "").strip(), str(cell.get("option") or "").strip()}
    tokens.discard("")
    names = {str(option.get("id") or "").strip(), str(option.get("name") or "").strip()}
    names.discard("")
    if tokens & names:
        return True
    lowered = {n.lower() for n in names}
    return any(t.lower() in lowered for t in tokens)


def _raw_totals(
    cells: list[dict[str, Any]],
    options: list[dict[str, Any]],
    names: list[str],
    weights: list[float],
    invert: list[bool],
    scale: dict[str, Any],
) -> dict[str, float]:
    total_w = sum(abs(w) for w in weights) or 1.0
    out: dict[str, float] = {}
    for opt in options:
        oid = str(opt.get("id") or opt.get("name"))
        acc = 0.0
        for i, crit in enumerate(names):
            match = next(
                (
                    c
                    for c in cells
                    if _same_option(c, opt) and str(c.get("criterion")) == crit and c.get("value") is not None
                ),
                None,
            )
            if match is None:
                continue
            acc += (abs(weights[i]) / total_w) * _scaled(float(match["value"]), scale, invert=invert[i])
        out[oid] = acc
    return out


def _shifted(weights: list[float], index: int, delta: float) -> list[float]:
    total = sum(weights)
    rest = total - weights[index]
    new_w = list(weights)
    new_w[index] = weights[index] + delta
    if rest > _EPS:
        factor = (total - new_w[index]) / rest
        for j, _ in enumerate(new_w):
            if j != index:
                new_w[j] = weights[j] * factor
    return new_w


def _robustness(
    cells: list[dict[str, Any]],
    options: list[dict[str, Any]],
    names: list[str],
    weights: list[float],
    invert: list[bool],
    scale: dict[str, Any],
    top_id: str,
) -> dict[str, Any]:
    total_w = sum(weights)
    span = ROBUSTNESS_FRACTION * total_w
    base = _raw_totals(cells, options, names, weights, invert, scale)
    name_of = {str(o.get("id") or o.get("name")): str(o.get("name") or o.get("id")) for o in options}
    changes: list[dict[str, Any]] = []
    for index, crit in enumerate(names):
        rest = total_w - weights[index]
        if rest <= _EPS:
            continue
        lo = max(-span, -weights[index])
        hi = min(span, rest)
        for direction, limit in (("down", lo), ("up", hi)):
            if abs(limit) <= _EPS:
                continue
            end = _raw_totals(cells, options, names, _shifted(weights, index, limit), invert, scale)
            best: tuple[float, str] | None = None
            for other, value in end.items():
                if other == top_id:
                    continue
                d0 = base[top_id] - base[other]
                d1 = end[top_id] - value
                if d1 < -_EPS:
                    point = limit * d0 / (d0 - d1)
                    if best is None or abs(point) < best[0]:
                        best = (abs(point), other)
            if best is not None:
                changes.append(
                    {
                        "criterion": crit,
                        "direction": direction,
                        "smallest_shift_points": round(best[0] * 100.0 / total_w, 2),
                        "then_top": name_of.get(best[1], best[1]),
                    }
                )
    changes.sort(key=lambda c: c["smallest_shift_points"])
    return {
        "range_points": round(ROBUSTNESS_FRACTION * 100.0, 2),
        "rule": (
            "One priority moves up or down by up to 10 points of 100; the others "
            "rescale so the weights still add up to the same total."
        ),
        "top_option_holds": not changes,
        "changes": changes,
        "smallest_shift_points": changes[0]["smallest_shift_points"] if changes else None,
    }


def score_session(row: dict[str, Any]) -> dict[str, Any]:
    """Return ranked totals and robustness. Never invents ratings or names a winner."""
    scale = _scale(row)
    gaps: list[dict[str, str]] = []
    out: dict[str, Any] = {
        "label": LABEL,
        "method": {
            "name": "weighted_sum_0_100",
            "scale": scale,
            "normalization": "weights / sum; rating maps to 0–100; lower_better inverted",
        },
        "raters": [],
        "scored": False,
        "gaps": gaps,
    }
    crit_rows = _criteria(row)
    if not crit_rows or any(c.get("weight") is None for c in crit_rows):
        gaps.append({"code": "weights_missing", "message": "every criterion needs a numeric weight", "field": "criteria.weight"})
        return out
    try:
        weights = [float(c["weight"]) for c in crit_rows]
    except (TypeError, ValueError):
        gaps.append({"code": "invalid_weight", "message": "weights must be numeric", "field": "criteria.weight"})
        return out
    if any(w < 0 for w in weights) or sum(abs(w) for w in weights) <= 0:
        gaps.append({"code": "invalid_weight", "message": "weights must be >= 0 with at least one > 0", "field": "criteria.weight"})
        return out

    names = [str(c["name"]) for c in crit_rows]
    invert = [str(c.get("direction") or "higher_better") == "lower_better" for c in crit_rows]
    options = [o for o in (row.get("options") or []) if isinstance(o, dict) and (o.get("id") or o.get("name"))]
    if len(options) < 2:
        gaps.append({"code": "too_few_options", "message": "need at least two options", "field": "options"})
        return out

    # Normalize option ids
    for o in options:
        o.setdefault("id", str(o.get("name")))
        o.setdefault("name", str(o.get("id")))

    ratings = [c for c in (row.get("ratings") or []) if isinstance(c, dict)]
    raters = sorted({str(c.get("rater") or "").strip() for c in ratings if str(c.get("rater") or "").strip()})
    if not raters:
        gaps.append({"code": "rater_missing", "message": "ratings need a named rater", "field": "ratings.rater"})
        return out

    total_weight = sum(abs(w) for w in weights)
    out["weights_used"] = {n: round(w / total_weight, 4) for n, w in zip(names, weights)}
    out["weights_sum"] = float(sum(weights))

    for rater in raters:
        cells = [c for c in ratings if str(c.get("rater") or "").strip() == rater]
        missing = False
        for opt in options:
            for crit in names:
                if not any(
                    _same_option(c, opt) and str(c.get("criterion")) == crit and c.get("value") is not None
                    for c in cells
                ):
                    missing = True
                    gaps.append(
                        {
                            "code": "rating_missing",
                            "message": f"missing rating for {opt.get('name')} / {crit} by {rater}",
                            "field": "ratings",
                        }
                    )
        if missing:
            continue
        totals = _raw_totals(cells, options, names, weights, invert, scale)
        ranked = sorted(
            (
                {
                    "option": str(o.get("name")),
                    "option_id": str(o.get("id")),
                    "total": round(totals[str(o.get("id"))], 4),
                }
                for o in options
            ),
            key=lambda r: (-r["total"], r["option"]),
        )
        # Tie note — do not declare a winner
        if len(ranked) >= 2 and abs(ranked[0]["total"] - ranked[1]["total"]) <= TIE_TOLERANCE:
            ranked_note = "top totals within tie tolerance; person decides"
        else:
            ranked_note = "ranked by the person's inputs only; not a recommendation"
        top_id = ranked[0]["option_id"]
        robust = _robustness(cells, options, names, weights, invert, scale, top_id)
        out["raters"].append(
            {
                "rater": rater,
                "ranked": ranked,
                "note": ranked_note,
                "robustness": robust,
            }
        )

    out["scored"] = bool(out["raters"]) and not any(g["code"] == "rating_missing" for g in gaps)
    if out["scored"]:
        out["gaps"] = [g for g in gaps if g["code"] not in {"rating_missing"}]
    return out
