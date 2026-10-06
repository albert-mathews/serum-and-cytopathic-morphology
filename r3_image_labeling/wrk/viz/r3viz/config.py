"""Load raters.toml into simple dataclasses."""
from __future__ import annotations

try:
    import tomllib  # Python >= 3.11
except ModuleNotFoundError:  # Python 3.10: pip install tomli
    import tomli as tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Source:
    file: Path
    prefix: str = ""
    sheet: str | None = None

    @property
    def exists(self) -> bool:
        return self.file.exists()


@dataclass
class Rater:
    code: str
    label: str
    condition: str
    color: str
    note: str = ""
    expected_frames: int | None = None
    figure_note: str = ""
    pass1: Source | None = None
    pass2: Source | None = None
    cro_comparable: Source | None = None
    cro_healthy: Source | None = None

    @property
    def tag(self) -> str:
        return self.label + ("*" if self.note else "")


@dataclass
class Config:
    root: Path
    settings: dict
    conditions: list[dict]
    raters: list[Rater] = field(default_factory=list)
    overlays: list[Path] = field(default_factory=list)

    @property
    def out_dir(self) -> Path:
        return self.root / self.settings.get("out_dir", "out")

    def cond_label(self, key: str) -> str:
        for c in self.conditions:
            if c["key"] == key:
                return c["label"]
        return key

    def rater(self, code: str) -> Rater:
        return next(r for r in self.raters if r.code == code)


def _src(root: Path, d: dict | None) -> Source | None:
    if not d:
        return None
    return Source(file=(root / d["file"]).resolve(), prefix=d.get("prefix", ""), sheet=d.get("sheet"))


def _rater(root: Path, r: dict) -> Rater:
    return Rater(
        code=r["code"], label=r.get("label", r["code"]), condition=r.get("condition", "unspecified"),
        color=r.get("color", "#333333"), note=r.get("note", ""),
        expected_frames=r.get("expected_frames"), figure_note=r.get("figure_note", ""),
        pass1=_src(root, r.get("pass1")), pass2=_src(root, r.get("pass2")),
        cro_comparable=_src(root, r.get("cro_comparable")), cro_healthy=_src(root, r.get("cro_healthy")),
    )


def load(path: str | Path, use_overlay: bool = True) -> Config:
    """Load a config. `settings.local_overlay` (optional) names an untracked TOML whose [[condition]] and
    [[rater]] blocks are appended (a rater with an existing code replaces it). Paths inside the overlay
    are relative to the overlay file. A missing overlay is skipped silently (fresh checkout)."""
    path = Path(path).resolve()
    root = path.parent
    raw = tomllib.loads(path.read_text(encoding="utf-8"))
    cfg = Config(root=root, settings=raw.get("settings", {}), conditions=raw.get("condition", []))
    for r in raw.get("rater", []):
        cfg.raters.append(_rater(root, r))
    ov = cfg.settings.get("local_overlay")
    if use_overlay and ov and (root / ov).exists():
        op = (root / ov).resolve()
        oraw = tomllib.loads(op.read_text(encoding="utf-8"))
        keys = [c["key"] for c in cfg.conditions]
        for c in oraw.get("condition", []):
            if c["key"] in keys:
                cfg.conditions[keys.index(c["key"])] = c
            else:
                cfg.conditions.append(c)
        if oraw.get("condition_order"):
            order = oraw["condition_order"]
            cfg.conditions.sort(key=lambda c: order.index(c["key"]) if c["key"] in order else len(order))
        for r in oraw.get("rater", []):
            new = _rater(op.parent, r)
            idx = [i for i, x in enumerate(cfg.raters) if x.code == new.code]
            if idx:
                cfg.raters[idx[0]] = new
            else:
                cfg.raters.append(new)
        for k, v in oraw.get("settings", {}).items():
            if k != "local_overlay":
                cfg.settings[k] = v
        cfg.overlays.append(op)
    known = {c["key"] for c in cfg.conditions}
    for r in cfg.raters:
        if r.condition not in known:
            cfg.conditions.append({"key": r.condition, "label": r.condition})
    return cfg
