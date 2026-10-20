#!/usr/bin/env python3
"""How much a chart's construction enlarges or shrinks a difference.

Part of the VITAL TRUSTED skill honest-framing (task TR-3.2.2).
Every output is derived from the values passed in; nothing is looked up.
It measures the drawing, not the meaning.

Examples:
  python chart_scale.py --axis-min 80 --value 84 --value 88
  python chart_scale.py --axis-min 80 --axis-max 90 --value 84 --value 88
  python chart_scale.py --value 10 --value 20 --icon-scaling both
  python chart_scale.py --cumulative 410,805,1193

Bars: give the value-axis start (--axis-min, default 0) and two values, the reference
first. The script compares the ratio of the drawn bar lengths with the ratio of the
values and reports how many times larger the difference looks than it is.

Pictograms: --icon-scaling height (icon stretched in one direction) or both (height
and width scaled together, so the area grows with the square of the ratio).

Cumulative: a comma-separated cumulative series; the script returns per-period
increments.
"""
import argparse
import json
import sys


def bars(axis_min, a, b, axis_max=None):
    if a == 0:
        sys.exit("the reference value must not be 0 (ratio not defined)")
    la, lb = a - axis_min, b - axis_min
    if la <= 0 or lb <= 0:
        sys.exit("both values must lie above the axis start, or a bar is not drawn")
    actual_ratio = b / a
    displayed_ratio = lb / la
    actual_change = actual_ratio - 1
    displayed_change = displayed_ratio - 1
    out = {
        "axis_start": axis_min,
        "values": [a, b],
        "actual_ratio": round(actual_ratio, 4),
        "displayed_ratio": round(displayed_ratio, 4),
        "actual_change_pct": round(actual_change * 100, 2),
        "displayed_change_pct": round(displayed_change * 100, 2),
        "looks_larger_by": None,
        "difference_share_of_plotted_range_pct": None,
        "note": "derived from supplied values",
    }
    if actual_change != 0:
        out["looks_larger_by"] = round(displayed_change / actual_change, 2)
    if axis_max is not None:
        if axis_max <= axis_min:
            sys.exit("--axis-max must be above --axis-min")
        out["difference_share_of_plotted_range_pct"] = round(
            abs(b - a) / (axis_max - axis_min) * 100, 2)
    return out


def icons(a, b, scaling):
    if a <= 0 or b <= 0:
        sys.exit("icon values must be above 0")
    r = b / a
    apparent = r if scaling == "height" else r * r
    return {
        "actual_ratio": round(r, 4),
        "icon_scaling": scaling,
        "apparent_size_ratio": round(apparent, 4),
        "looks_larger_by": round(apparent / r, 4),
        "note": "derived from supplied values; 'both' means height and width scaled "
                "together, so area grows with the square of the ratio",
    }


def cumulative(series):
    try:
        vals = [float(x) for x in series.split(",") if x.strip() != ""]
    except ValueError:
        sys.exit("--cumulative takes comma-separated numbers, e.g. 410,805,1193")
    if len(vals) < 2:
        sys.exit("--cumulative needs at least two values")
    inc = [vals[0]] + [round(vals[i] - vals[i - 1], 6) for i in range(1, len(vals))]
    falling = [i + 1 for i in range(1, len(inc)) if inc[i] < inc[i - 1]]
    negative = [i + 1 for i, v in enumerate(inc) if v < 0]
    return {
        "cumulative": vals,
        "per_period": inc,
        "periods_where_per_period_fell": falling,
        "periods_with_negative_increment": negative,
        "note": "derived from supplied values; period 1 is taken as the first value",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--axis-min", type=float, default=0.0)
    p.add_argument("--axis-max", type=float)
    p.add_argument("--value", type=float, action="append", default=[],
                   help="give twice: reference value first, compared value second")
    p.add_argument("--icon-scaling", choices=["height", "both"])
    p.add_argument("--cumulative", type=str)
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    res = {}
    if a.cumulative:
        res["cumulative"] = cumulative(a.cumulative)
    if a.value:
        if len(a.value) != 2:
            sys.exit("give exactly two --value arguments (reference first)")
        v1, v2 = a.value
        if a.icon_scaling:
            res["icons"] = icons(v1, v2, a.icon_scaling)
        else:
            res["bars"] = bars(a.axis_min, v1, v2, a.axis_max)
    if not res:
        p.error("give two --value arguments, or --cumulative")

    if a.json:
        print(json.dumps(res, indent=2))
        return
    print("Derived from supplied values")
    if "bars" in res:
        d = res["bars"]
        print(f"  Axis starts at:        {d['axis_start']}")
        print(f"  Values:                {d['values'][0]} and {d['values'][1]}")
        print(f"  Actual ratio:          {d['actual_ratio']} ({d['actual_change_pct']}% change)")
        print(f"  Drawn bar ratio:       {d['displayed_ratio']} ({d['displayed_change_pct']}% change as drawn)")
        if d["looks_larger_by"] is not None:
            print(f"  Difference looks:      {d['looks_larger_by']} times its real size")
        if d["difference_share_of_plotted_range_pct"] is not None:
            print(f"  Difference fills:      {d['difference_share_of_plotted_range_pct']}% of the plotted range")
    if "icons" in res:
        d = res["icons"]
        print(f"  Actual ratio:          {d['actual_ratio']}")
        print(f"  Icons scaled by:       {d['icon_scaling']}")
        print(f"  Apparent size ratio:   {d['apparent_size_ratio']} (looks {d['looks_larger_by']} times the real ratio)")
    if "cumulative" in res:
        d = res["cumulative"]
        print(f"  Cumulative:            {d['cumulative']}")
        print(f"  Per period:            {d['per_period']}")
        if d["periods_where_per_period_fell"]:
            print(f"  Per-period fell in:    periods {d['periods_where_per_period_fell']}")


if __name__ == "__main__":
    main()
