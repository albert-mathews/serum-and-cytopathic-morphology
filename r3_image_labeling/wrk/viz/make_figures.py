#!/usr/bin/env python3
"""Regenerate every R3 figure, the summary metrics CSVs, GALLERY.md and index.html.

    python make_figures.py --no-overlay     # public set from tracked deposits only (rewrites GALLERY.md)
    python make_figures.py                  # + local overlay if present (gallery -> local/GALLERY_local.md)
    python make_figures.py --only c0 h      # subset by name prefix
    python make_figures.py --config other.toml
"""
from __future__ import annotations

import argparse
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from r3viz import config, gallery, loaders, metrics, style  # noqa: E402
from r3viz.figures import delta, heat, incidence, likert, passes, briefing, profile, table, time  # noqa: E402

FIGS = [
    ("a_diverging_likert_marks", likert.fig_a), ("b1_incidence_grouped_bars", incidence.fig_b1),
    ("b2_cpe_composition_stacked", incidence.fig_b2), ("c0_global_direction_by_rater", delta.fig_c0),
    ("c1_dumbbell_A_to_B_by_item", delta.fig_c1), ("c2_delta_dotplot_by_item", delta.fig_c2),
    ("d_heatmap_mean_score", heat.fig_d), ("e_agreement_heatmap_kappa", heat.fig_e),
    ("f_daily_time_course", time.fig_f), ("g1_pass1_vs_pass2_by_item", passes.fig_g1),
    ("g2_pass1_vs_pass2_summary_slope", passes.fig_g2), ("h_briefing_condition_contrast", briefing.fig_h),
    ("i1_radar_profile_use_with_care", profile.fig_i1), ("i2_profile_small_multiples", profile.fig_i2),
    ("j_styled_summary_table", table.fig_j),
]


def write_metrics(cfg, data):
    out = cfg.out_dir / "metrics"; out.mkdir(parents=True, exist_ok=True)
    if data.pass2:
        metrics.item_deltas(data.item_frames()).to_csv(out / "item_deltas.csv", index=False)
        p2 = {c: df[["image_name"] + [f"hit_{k}" for k in metrics.I.ITEM_KEYS]].rename(columns={f"hit_{k}": k for k in metrics.I.ITEM_KEYS})
              for c, df in data.pass2.items()}
        metrics.pair_agreement(p2, metrics.I.ITEM_KEYS).to_csv(out / "pass2_pair_agreement.csv", index=False)
    rows = []
    for kind in ("pass1", "pass2", "cro", "cro_healthy"):
        for code, df in getattr(data, kind).items():
            a, b = data.n_arm(df)
            rows.append(f"{code},{kind},{a},{b},{data.is_partial(df, code)}")
    (out / "coverage.csv").write_text("rater,dataset,n_A,n_B,partial\n" + "\n".join(rows) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(HERE / "raters.toml"))
    ap.add_argument("--only", nargs="*", default=None, help="figure-name prefixes, e.g. c0 h")
    ap.add_argument("--no-overlay", action="store_true", help="ignore settings.local_overlay (public set only)")
    args = ap.parse_args()
    cfg = config.load(args.config, use_overlay=not args.no_overlay)
    print("config:", Path(args.config).name, "+ overlay " + ", ".join(p.name for p in cfg.overlays) if cfg.overlays else "(no overlay)")
    style.setup()
    data = loaders.Data(cfg)
    for w in data.warnings:
        print("WARN", w)
    write_metrics(cfg, data)
    outputs, failed = {}, []
    for name, fn in FIGS:
        if args.only and not any(name.startswith(p) for p in args.only):
            continue
        try:
            outputs[name] = fn(cfg, data)
            print("ok  ", name)
        except Exception:  # keep going; report at end
            failed.append(name); traceback.print_exc()
    if not args.only:
        g = gallery.write(cfg, data, outputs)
        print("gallery ->", g, "and", cfg.out_dir / "index.html")
        print("coverage:", gallery.coverage_line(cfg, data))
    if failed:
        print("FAILED:", failed); sys.exit(1)


if __name__ == "__main__":
    main()
