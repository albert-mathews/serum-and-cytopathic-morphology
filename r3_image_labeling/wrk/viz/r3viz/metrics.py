"""Summary metrics: per-arm means, B-A deltas with bootstrap CIs, agreement (kappa)."""
from __future__ import annotations

from itertools import combinations

import numpy as np
import pandas as pd

from . import items as I


def arm_mean(df: pd.DataFrame, col: str) -> tuple[float, float]:
    g = df.groupby("arm")[col].mean()
    return float(g.get("A", np.nan)), float(g.get("B", np.nan))


def boot_ci(df: pd.DataFrame, col: str, iters=2000, seed=7, stat="delta"):
    """Bootstrap (resample images within arm). stat: 'delta' (B-A), 'A', 'B'. Returns (est, lo, hi)."""
    rng = np.random.default_rng(seed)
    a = df.loc[df["arm"] == "A", col].to_numpy(float)
    b = df.loc[df["arm"] == "B", col].to_numpy(float)
    if len(a) == 0 or len(b) == 0:
        return (np.nan,) * 3
    fa = lambda x: x.mean()
    est = {"delta": b.mean() - a.mean(), "A": a.mean(), "B": b.mean()}[stat]
    sa = rng.choice(a, (iters, len(a))).mean(1)
    sb = rng.choice(b, (iters, len(b))).mean(1)
    dist = {"delta": sb - sa, "A": sa, "B": sb}[stat]
    lo, hi = np.percentile(dist, [2.5, 97.5])
    return float(est), float(lo), float(hi)


def item_table(p2: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Long table: rater, item, arm, incidence, mean_score, n."""
    rows = []
    for code, df in p2.items():
        for arm in ("A", "B"):
            sub = df[df["arm"] == arm]
            for k in I.ITEM_KEYS:
                if f"hit_{k}" not in df.columns:  # e.g. CRO healthy-type coding has the 3 healthy items only
                    continue
                rows.append(dict(rater=code, item=k, arm=arm, n=len(sub),
                                 incidence=sub[f"hit_{k}"].mean() if len(sub) else np.nan,
                                 mean_score=sub[f"score_{k}"].mean() if len(sub) else np.nan))
    return pd.DataFrame(rows)


def item_deltas(p2: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Per rater x item: inc_A/B, score_A/B, deltas, saturated. Items a rater's frame lacks are absent."""
    t = item_table(p2)
    w = t.pivot_table(index=["rater", "item"], columns="arm", values=["incidence", "mean_score"]).reset_index()
    w.columns = ["rater", "item", "inc_A", "inc_B", "score_A", "score_B"]
    w["inc_delta"] = w["inc_B"] - w["inc_A"]
    w["score_delta"] = w["score_B"] - w["score_A"]
    w["saturated"] = ((w["inc_A"].isin([0.0, 1.0])) & (w["inc_A"] == w["inc_B"]))
    return w


def lookup(d: pd.DataFrame, code: str, item: str):
    """Row of item_deltas for (rater, item), or None when that rater has no coding for the item."""
    m = d[(d.rater == code) & (d.item == item)]
    return None if m.empty else m.iloc[0]


def cohen_kappa(x: np.ndarray, y: np.ndarray):
    """Binary Cohen's kappa; None when either rater is constant (kappa uninformative)."""
    x = np.asarray(x, int); y = np.asarray(y, int)
    if len(x) == 0 or x.min() == x.max() or y.min() == y.max():
        return None
    po = (x == y).mean()
    pe = x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean())
    return float((po - pe) / (1 - pe)) if pe < 1 else None


def pair_agreement(frames: dict[str, pd.DataFrame], cols: list[str], min_overlap=5) -> pd.DataFrame:
    """Per item x rater-pair: n, % agreement, kappa (None if constant), positive counts."""
    rows = []
    for (ra, da), (rb, db) in combinations(frames.items(), 2):
        m = da.merge(db, on="image_name", suffixes=("_a", "_b"))
        if len(m) < min_overlap:
            continue
        for c in cols:
            ca, cb = f"{c}_a", f"{c}_b"
            if ca not in m or cb not in m:
                continue
            x, y = m[ca].to_numpy(int), m[cb].to_numpy(int)
            rows.append(dict(pair=f"{ra}–{rb}", a=ra, b=rb, item=c, n=len(m),
                             pct=100 * (x == y).mean(), kappa=cohen_kappa(x, y),
                             pos_a=int(x.sum()), pos_b=int(y.sum())))
    return pd.DataFrame(rows)


def daily(df: pd.DataFrame, col: str) -> pd.DataFrame:
    g = df.groupby(["arm", "day"])[col]
    out = g.agg(["mean", "count", "std"]).reset_index()
    out["se"] = out["std"] / np.sqrt(out["count"])
    return out
