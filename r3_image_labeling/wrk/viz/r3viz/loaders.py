"""Load each rater's files into tidy per-image frames.

pass2 frame : image_name, arm (A/B), day, raw_<item>, score_<item>, hit_<item>, level_<item>,
              cpe_score_sum, healthy_score_sum, cpe_hits_strict, healthy_hits_strict
pass1 frame : image_name, arm, day, p1_<lexkey> (0/1), p1_cpe_count, p1_healthy_count,
              p1_cpe7_count (the 7 checklist CPE items only)
cro frame   : image_name, arm, day, Dy..Re (0/1) [+ BE,Sy,CS,ND if present], n6
cro_healthy : image_name, arm, day, CRO_H_<term> (0/1), hit_/score_/level_<checklist healthy item>,
              healthy_score_sum (3 checklist-matched items), healthy_share7 (share of the 7 Pass-1
              healthy lexicon keys; Mitotic OR Bright = H_Mitotic_Bright); CRO frames with their own
              single-image description only (cro-results/cro_cpe_detections.csv)

Inputs may be CSV / XLSX, or the repo's *_gk.json deposits (ir-results/cpe_detection_results_ir*_gk.json:
`image_id`, `full_response_text` = Pass 1, `pass2_checklist` = Pass 2 raw marks).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

from . import items as I

IMG_RE = re.compile(r"Culture([AB])_day([1-5])_(\d{2})")


# *_gk.json pass2_checklist keys -> checklist item keys
GK_CHECKLIST = {"look_healthy": "H_Look_Healthy", "nuclei": "H_well_defined_nuclei",
                "cytoplasmic_extensions": "H_Cytoplasmic_extensions", "vacuolation": "CPE_Vacuolation_V",
                "granularity": "CPE_Granularity_G", "ballooned_enlarged": "CPE_Ballooned_Enlarged_BE",
                "syncytia": "CPE_Syncytia_Sy", "cytoplasmic_strands": "CPE_Cytoplasmic_strands_CS",
                "cell_death": "CPE_Cell_death_Dy", "nonspecific_degeneration": "CPE_Nonspecific_degeneration_ND"}


def _read_gk_json(p: Path) -> pd.DataFrame:
    """Flatten a *_gk.json deposit: image_name, description (Pass 1 text), raw_<item> (Pass 2 marks)."""
    d = json.loads(p.read_text(encoding="utf-8"))
    rows = []
    for key, v in d.items():
        img = v.get("image_id") or ""
        if not img and v.get("path") and v.get("id"):
            pid = int(v["id"])
            img = f"Culture{'AB'[int(v['path']) - 1]}_day{pid // 100}_{pid % 100:02d}"
        row = {"image_name": img, "description": v.get("full_response_text") or ""}
        for gk, item in GK_CHECKLIST.items():
            row[f"raw_{item}"] = (v.get("pass2_checklist") or {}).get(gk, "") or ""
        rows.append(row)
    return pd.DataFrame(rows, dtype=str)


def _read_table(src) -> pd.DataFrame:
    p: Path = src.file
    if p.suffix.lower() == ".json":
        return _read_gk_json(p)
    if p.suffix.lower() in (".xlsx", ".xlsm", ".xls"):
        return pd.read_excel(p, sheet_name=src.sheet or 0, dtype=str)
    return pd.read_csv(p, dtype=str, encoding="utf-8-sig", keep_default_na=False)


def _image_names(df: pd.DataFrame) -> pd.Series:
    cols = {c.lower().strip(): c for c in df.columns}
    for key in ("image_name", "blinded_id", "filename"):
        if key in cols:
            s = df[cols[key]].astype(str).str.replace(r"\.tif+$", "", regex=True, flags=re.I).str.strip()
            if s.str.match(IMG_RE).mean() > 0.5:
                return s
    if "image_id" in cols:
        s = df[cols["image_id"]].astype(str).str.replace(r"Culture([AB])_D(\d)_(\d{2})", r"Culture\1_day\2_\3", regex=True)
        if s.str.match(IMG_RE).mean() > 0.5:
            return s
    if "culture" in cols and "day" in cols:
        img = cols.get("image") or cols.get("image_no") or cols.get("field") or cols.get("field_id")
        if img:
            def mk(r):
                try:
                    return f"Culture{str(r[cols['culture']]).strip().upper()[-1]}_day{int(float(r[cols['day']]))}_{int(float(r[img])):02d}"
                except (ValueError, TypeError):
                    return ""
            return df.apply(mk, axis=1)
    raise ValueError(f"cannot find an image id column in {list(df.columns)}")


def _add_arm_day(df: pd.DataFrame) -> pd.DataFrame:
    m = df["image_name"].str.extract(IMG_RE)
    df = df[m[0].notna()].copy()
    m = m[m[0].notna()]
    df["arm"] = m[0].values
    df["day"] = m[1].astype(int).values
    return df


# ------------------------------------------------------------------ pass 2
def load_pass2(src) -> pd.DataFrame:
    df = _read_table(src)
    df["image_name"] = _image_names(df)
    raw_cols = {}
    if any(c.startswith("raw_") for c in df.columns):
        for k in I.ITEM_KEYS:
            raw_cols[k] = f"raw_{k}"
    else:
        for c in df.columns:
            m = re.match(r"^\s*(\d{1,2})\.", str(c))
            if m and int(m.group(1)) in I.CHECKLIST_NUM:
                raw_cols[I.CHECKLIST_NUM[int(m.group(1))]] = c
    missing = [k for k in I.ITEM_KEYS if k not in raw_cols or raw_cols[k] not in df.columns]
    if missing:
        raise ValueError(f"{src.file.name}: missing checklist items {missing}")
    out = pd.DataFrame({"image_name": df["image_name"]})
    for k in I.ITEM_KEYS:
        out[f"raw_{k}"] = df[raw_cols[k]].fillna("").astype(str).str.strip()
    # keep only fully-marked rows (partial delivery => fewer rows, flagged by coverage)
    filled = (out[[f"raw_{k}" for k in I.ITEM_KEYS]] != "").all(axis=1)
    out = _add_arm_day(out[filled])
    for k in I.ITEM_KEYS:
        raw = out[f"raw_{k}"]
        out[f"score_{k}"] = raw.map(lambda a, k=k: I.score(k, a))
        out[f"hit_{k}"] = raw.map(I.strict_present)
        out[f"level_{k}"] = raw.map(I.level)
    out["cpe_score_sum"] = out[[f"score_{k}" for k in I.CPE_KEYS]].sum(axis=1)
    out["healthy_score_sum"] = out[[f"score_{k}" for k in I.HEALTHY_KEYS]].sum(axis=1)
    out["cpe_hits_strict"] = out[[f"hit_{k}" for k in I.CPE_KEYS]].sum(axis=1)
    out["healthy_hits_strict"] = out[[f"hit_{k}" for k in I.HEALTHY_KEYS]].sum(axis=1)
    return out.drop_duplicates("image_name").reset_index(drop=True)


# ------------------------------------------------------------------ pass 1
def _text_col(df: pd.DataFrame) -> str:
    cols = {c.lower().strip(): c for c in df.columns}
    for key in ("description", "morphology_description", "text", "free_text", "comment"):
        if key in cols:
            return cols[key]
    return df.columns[-1]


def load_pass1(src) -> pd.DataFrame:
    df = _read_table(src)
    df["image_name"] = _image_names(df)
    tcol = _text_col(df)
    df["text"] = df[tcol].fillna("").astype(str).str.replace(r"\s+", " ", regex=True).str.strip()
    df = df[(df["text"] != "") & (df["text"].str.lower() != "none")]
    out = _add_arm_day(df[["image_name", "text"]].copy())
    for k, rx in I.P1_HEALTHY + I.P1_CPE:
        out[f"p1_{k}"] = out["text"].map(lambda t, rx=rx: int(bool(rx.search(t))))
    out["p1_cpe_count"] = out[[f"p1_{k}" for k in I.P1_CPE_KEYS]].sum(axis=1)
    out["p1_healthy_count"] = out[[f"p1_{k}" for k in I.P1_HEALTHY_KEYS]].sum(axis=1)
    out["p1_cpe7_count"] = out[[f"p1_{k}" for k in I.CPE_KEYS]].sum(axis=1)
    return out.drop(columns=["text"]).drop_duplicates("image_name").reset_index(drop=True)


# ------------------------------------------------------------------ CRO-comparable
def load_cro_comparable(src, image_map: pd.DataFrame) -> pd.DataFrame:
    df = _read_table(src)
    pre = src.prefix
    if "blinded_id" in df.columns or "image_name" in df.columns:
        df["image_name"] = _image_names(df)
    else:
        key = image_map.assign(k=image_map["path"].astype(str) + "_" + image_map["id"].astype(str)).set_index("k")["image_name"]
        df["image_name"] = (df["path"].astype(str) + "_" + df["id"].astype(str)).map(key)
    cols = [c for c in ["Dy", "Ro", "V", "D", "G", "Re", "BE", "Sy", "CS", "ND"] if f"{pre}{c}" in df.columns]
    out = pd.DataFrame({"image_name": df["image_name"]})
    for c in cols:
        out[c] = pd.to_numeric(df[f"{pre}{c}"], errors="coerce").fillna(0).astype(int)
    out = _add_arm_day(out.dropna(subset=["image_name"]))
    out["n6"] = out[[c for c in I.CRO_SIX if c in out.columns]].sum(axis=1)
    return out.reset_index(drop=True)


# ------------------------------------------------------------------ CRO healthy-type (binary presence)
CRO_H_TO_ITEM = {"CRO_H_Look_Healthy": "H_Look_Healthy", "CRO_H_well_defined_nuclei": "H_well_defined_nuclei",
                 "CRO_H_Cytoplasmic_extensions": "H_Cytoplasmic_extensions"}
CRO_H_TO_P1 = {"H_Look_Healthy": ["CRO_H_Look_Healthy"], "H_Mitotic_Bright": ["CRO_H_Mitotic", "CRO_H_Bright"],
               "H_Adherent": ["CRO_H_Adherent"], "H_Elongated": ["CRO_H_Elongated"], "H_Polygonal": ["CRO_H_Polygonal"],
               "H_Cytoplasmic_extensions": ["CRO_H_Cytoplasmic_extensions"], "H_well_defined_nuclei": ["CRO_H_well_defined_nuclei"]}


def load_cro_healthy(src) -> pd.DataFrame:
    """cro_cpe_detections.csv (CRO_H_* columns) -> per-frame healthy-type coding on the checklist's 3 healthy
    items (binary: named = 'yes' level, score 1; not named = score 0) plus the 7-key Pass-1-equivalent share."""
    df = _read_table(src)
    df["image_name"] = _image_names(df)
    hcols = [c for c in df.columns if c.startswith("CRO_H_")]
    out = df[["image_name"] + hcols].copy()
    for c in hcols:
        out[c] = pd.to_numeric(out[c], errors="coerce").fillna(0).astype(int)
    out = _add_arm_day(out)
    for c, k in CRO_H_TO_ITEM.items():
        if c in out.columns:
            out[f"hit_{k}"] = out[c]
            out[f"score_{k}"] = out[c].astype(float)
            out[f"level_{k}"] = out[c].map({1: "yes", 0: "absent"})
            out[f"raw_{k}"] = out[c].map({1: "present (CRO)", 0: "not named (CRO)"})
    out["healthy_score_sum"] = out[[f"score_{k}" for k in I.HEALTHY_KEYS if f"score_{k}" in out.columns]].sum(axis=1)
    p1 = {k: out[[c for c in cs if c in out.columns]].max(axis=1) for k, cs in CRO_H_TO_P1.items()}
    out["healthy_share7"] = pd.DataFrame(p1).sum(axis=1) / len(CRO_H_TO_P1)
    return out.drop_duplicates("image_name").reset_index(drop=True)


def _load_image_map(path: Path) -> pd.DataFrame:
    """image_name,path,id from either a simple map or images_rater_blinded_mapping.csv."""
    if not path.exists():
        return pd.DataFrame(columns=["image_name", "path", "id"])
    m = pd.read_csv(path, dtype=str, encoding="utf-8-sig")
    if {"image_name", "path", "id"} <= set(m.columns):
        return m
    if {"blinded_filename", "original_filename"} <= set(m.columns):
        name = m["blinded_filename"].str.replace(r"\.tif+$", "", regex=True, flags=re.I)
        ex = m["original_filename"].str.extract(r"path(\d)_passage\d+_(\d{3})")
        return pd.DataFrame({"image_name": name, "path": ex[0], "id": ex[1]}).dropna()
    raise ValueError(f"{path.name}: unrecognized image map layout")


# ------------------------------------------------------------------ bundle
class Data:
    """All loaded frames, keyed by rater code."""

    def __init__(self, cfg):
        self.cfg = cfg
        self.pass1: dict[str, pd.DataFrame] = {}
        self.pass2: dict[str, pd.DataFrame] = {}
        self.cro: dict[str, pd.DataFrame] = {}
        self.cro_healthy: dict[str, pd.DataFrame] = {}
        self.warnings: list[str] = []
        self.image_map = _load_image_map(cfg.root / cfg.settings.get("image_map", "data/image_map.csv"))
        for r in cfg.raters:
            for attr, fn, store in (("pass1", load_pass1, self.pass1), ("pass2", load_pass2, self.pass2)):
                src = getattr(r, attr)
                if src is None:
                    continue
                if not src.exists:
                    self.warnings.append(f"{r.code} {attr}: file not found ({src.file.name}) -> pending")
                    continue
                df = fn(src)
                if len(df):
                    store[r.code] = df
            for attr, fn, store, args in (("cro_comparable", load_cro_comparable, self.cro, (self.image_map,)),
                                          ("cro_healthy", load_cro_healthy, self.cro_healthy, ())):
                src = getattr(r, attr)
                if src is None:
                    continue
                if not src.exists:
                    self.warnings.append(f"{r.code} {attr}: file not found ({src.file.name})")
                    continue
                store[r.code] = fn(src, *args)

    # item-level frames (Pass-2 checklist + CRO healthy-type coding) ---
    def item_frames(self) -> dict[str, pd.DataFrame]:
        """Frames carrying hit_/score_/level_ item columns: every Pass-2 rater, plus CRO healthy-type
        coding (3 healthy items, binary) for raters without a Pass-2 checklist."""
        out = {}
        for r in self.cfg.raters:
            if r.code in self.pass2:
                out[r.code] = self.pass2[r.code]
            elif r.code in self.cro_healthy:
                out[r.code] = self.cro_healthy[r.code]
        return out

    def item_raters(self, pending: bool = False) -> list:
        """Raters for item-level figures, in config order (pending Pass-2 raters optional)."""
        fr = self.item_frames()
        out = []
        for r in self.cfg.raters:
            if r.code in fr:
                out.append(r)
            elif pending and self.cfg.settings.get("show_pending_raters", True) and r.pass1 is not None:
                out.append(r)
        return out

    def is_binary(self, code: str) -> bool:
        """True when the rater's item-level data is binary CRO coding (not graded Pass-2 marks)."""
        return code not in self.pass2 and code in self.cro_healthy

    # coverage helpers -------------------------------------------------
    def n_arm(self, df: pd.DataFrame) -> tuple[int, int]:
        return int((df["arm"] == "A").sum()), int((df["arm"] == "B").sum())

    def is_partial(self, df: pd.DataFrame, code: str | None = None) -> bool:
        exp = self.cfg.settings.get("expected_frames", 100)
        if code is not None and self.cfg.rater(code).expected_frames:
            exp = self.cfg.rater(code).expected_frames
        return len(df) < self.cfg.settings.get("partial_threshold", 0.9) * exp

    def ntag(self, df: pd.DataFrame, code: str | None = None) -> str:
        a, b = self.n_arm(df)
        t = f"n = {a} A / {b} B"
        return t + " (PARTIAL)" if self.is_partial(df, code) else t

    def raters_with(self, kind: str) -> list:
        store = getattr(self, kind)
        return [r for r in self.cfg.raters if r.code in store]

    def raters_configured(self, kind: str) -> list:
        """Raters that have data, plus (optionally) those configured as pending for this kind."""
        store = getattr(self, kind)
        out = []
        for r in self.cfg.raters:
            if r.code in store:
                out.append(r)
            elif self.cfg.settings.get("show_pending_raters", True) and kind == "pass2" and r.pass1 is not None:
                out.append(r)  # a pass-1 rater without pass-2 yet is 'pending'
        return out
