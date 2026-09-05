#!/usr/bin/env python3
"""Which area am I working in? — the one thing the single-collection toolkit lacked.

The upstream toolkit (teamlibrary-toolkit, see docs/PROVENANCE.md) assumes ONE
collection: every script computes `ROOT = Path(__file__).parent.parent` and hangs
`raw/`, `meta/`, `outputs/`, `data/`, `dist/` off it. That assumption is the only
thing standing between it and many collections, so this module replaces it and
changes nothing else. Each area gets its own taxonomy, its own library.json, its
own UMAP layout and its own page, because each is a whole collection in its own
right — `areas/<name>/` has the same shape the toolkit's root had.

    PAPERLIB_AREA=neoantigens        ->  ROOT = <project>/areas/neoantigens
    PAPERLIB_AREA_ROOT=/some/path    ->  ROOT = /some/path   (an area moved or
                                          handed over; it is self-contained)

WHY AN AREA IS A DIRECTORY AND NOT A COLUMN: the areas are worked on
independently. One area is a complete collection you can tar, hand to somebody,
or delete without touching the others — and a paper's neighbours in the map are
the papers in ITS area, not everything ever collected. A column in a shared
library.json would give one taxonomy, one map, and one blast radius.

Standard library only, like build.py: a fresh clone must resolve an area before
pip has run.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
AREAS = PROJECT / "areas"
INBOX = PROJECT / "inbox"
INDEX = PROJECT / "index"
DIST = PROJECT / "dist"
CONFIG = PROJECT / "paperlib.json"

# An area name becomes a directory, a URL path segment and a Makefile variable,
# so it is restricted to what all three carry without quoting.
NAME_RE = re.compile(r"^[a-z][a-z0-9-]{1,40}$")

# The layout every area has. Identical to the toolkit's root layout, which is why
# the toolkit's scripts run inside one unmodified.
AREA_DIRS = ("inbox", "raw", "meta", "outputs", "annotations",
             "annotations/review_prose", "data", "reports", "eval", "dist")


def die(msg: str) -> None:
    print(f"paperlib: {msg}", file=sys.stderr)
    raise SystemExit(2)


def load_config() -> dict:
    """paperlib.json — defaults every area's project.json inherits."""
    if not CONFIG.exists():
        return {}
    raw = json.loads(CONFIG.read_text(encoding="utf-8"))
    return {k: v for k, v in raw.items() if not k.startswith("_")}


def list_areas() -> list[str]:
    """Every directory under areas/ that has been initialised (has meta/)."""
    if not AREAS.is_dir():
        return []
    return sorted(p.name for p in AREAS.iterdir()
                  if p.is_dir() and (p / "meta").is_dir())


def area_path(name: str) -> Path:
    return AREAS / name


def resolve_root(explicit: str | None = None) -> Path:
    """The ROOT every toolkit script should use, in precedence order.

    Falling back to the only area when there is exactly one is not guessing:
    with one area there is nothing to choose between. With two, refusing is the
    whole point — `make build` picking an area for you is how a taxonomy gets
    written into the wrong collection.
    """
    if explicit:
        p = area_path(explicit)
        if not p.is_dir():
            die(f"no such area: {explicit!r}. Have: {', '.join(list_areas()) or 'none'}")
        return p

    env_root = os.environ.get("PAPERLIB_AREA_ROOT")
    if env_root:
        p = Path(env_root).resolve()
        if not p.is_dir():
            die(f"PAPERLIB_AREA_ROOT does not exist: {p}")
        return p

    env_area = os.environ.get("PAPERLIB_AREA")
    if env_area:
        return resolve_root(env_area)

    areas = list_areas()
    if len(areas) == 1:
        return area_path(areas[0])
    if not areas:
        die("no areas yet. Create one: python3 scripts/new_area.py <name> --apply")
    die(f"AREA not set and there are {len(areas)} areas ({', '.join(areas)}).\n"
        f"        Use: make <target> AREA=<name>   or   PAPERLIB_AREA=<name> python3 ...")


def current_area_name(root: Path) -> str:
    """The area a ROOT belongs to, for messages and for the registry."""
    try:
        return root.resolve().relative_to(AREAS.resolve()).parts[0]
    except (ValueError, IndexError):
        return root.name


# --------------------------------------------------------------- registry --
# index/registry.json is DERIVED: rebuilt by scanning every area's meta/, never
# edited and never trusted as a source. An incrementally maintained registry
# drifts from the sidecars silently, and the sidecars are what `make verify`
# re-proves against the bytes. Anything that needs to know whether a paper is
# already held rescans; this file exists so the portal can show it.

def scan_all_areas(parse_frontmatter) -> dict[str, dict]:
    """sha256 -> {doi, title, year, areas: {area: source-filename}}.

    `parse_frontmatter` is passed in rather than imported so this module stays
    free of build.py, which imports nothing from here — the two would otherwise
    form a cycle the moment build.py resolves its own ROOT.
    """
    out: dict[str, dict] = {}
    for area in list_areas():
        for side in sorted((area_path(area) / "meta").glob("*.md")):
            fm = parse_frontmatter(side.read_text(encoding="utf-8", errors="replace"))
            sha = fm.get("sha256")
            if not sha or not fm.get("source"):
                continue
            rec = out.setdefault(sha, {"doi": fm.get("doi") or "",
                                       "title": fm.get("title") or "",
                                       "year": fm.get("year") or "",
                                       "areas": {}})
            rec["areas"][area] = fm["source"]
    return out


def held_elsewhere(sha_index: dict[str, dict], sha: str, this_area: str) -> list[str]:
    """Areas other than this one that already hold these exact bytes."""
    rec = sha_index.get(sha)
    return [] if not rec else sorted(a for a in rec["areas"] if a != this_area)


def frontmatter_parser():
    """`build.parse_frontmatter`, obtained WITHOUT choosing an area.

    A sidecar's frontmatter block contains comment rules like `# --- identity ---`,
    so it cannot be split on `---`; build.py has the one parser that gets this
    right and it must not be reimplemented here. But build.py resolves its ROOT at
    import time, and the project-level scripts (route_inbox, portal) work across
    every area and have no single one to give it.

    So point it at the project root for the duration of the import and take only
    the pure function. The caller must not touch build's path constants after
    this — they are deliberately meaningless. Everything project-level needs the
    area's own paths for goes through resolve_root() instead.
    """
    prior = os.environ.get("PAPERLIB_AREA_ROOT")
    os.environ["PAPERLIB_AREA_ROOT"] = str(PROJECT)
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import build
        return build.parse_frontmatter
    finally:
        if prior is None:
            os.environ.pop("PAPERLIB_AREA_ROOT", None)
        else:
            os.environ["PAPERLIB_AREA_ROOT"] = prior
