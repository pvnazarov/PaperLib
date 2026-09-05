#!/usr/bin/env python3
"""Create an area — a complete, self-contained collection under areas/<name>/.

An area has exactly the shape the upstream toolkit's root had, which is why the
toolkit's scripts run inside one with no change beyond how ROOT is resolved. It
holds its own papers, its own taxonomy, its own similarity map and its own page.

    python3 scripts/new_area.py neoantigens                     # DRY RUN
    python3 scripts/new_area.py neoantigens --apply \
            --tagline "what we read on tumour neoantigens"

DRY RUN BY DEFAULT, like every other writing script here: `make example` and
`make inbox` are dry runs for the same reason, which is that discovering a
directory tree was created is worse than typing --apply.

Standard library only.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

TEMPLATES = paperlib.PROJECT / "docs" / "templates"

# The prose that says HOW the clustering was decided. Shipped generic and meant to
# be rewritten: make_review.py refuses to run without it rather than put somebody
# else's account of somebody else's clustering into your document.
PROSE_SRC = TEMPLATES / "review_prose_first.md"

GITKEEP_NOTE = {
    "raw": "Source files. ADD-ONLY: never modify, rename or delete one.\n",
    "meta": "One sidecar per paper: identity + Abstract/Summary/Key points/Limitations.\n",
    "outputs": "The literature review. THE TAXONOMY LIVES HERE, not in a config file.\n",
    "inbox": "Staging for this area. scripts/route_inbox.py fills it from the shared inbox/.\n",
    "data": "Generated: library.json, similarity.json, bib_cache.json. Safe to delete.\n",
    "reports": "Drafts and measurements. NOTHING READS THIS DIRECTORY.\n",
    "eval": "Expectations written down BEFORE the answers are looked at.\n",
    "dist": "Generated: the three files that are the page, plus the reading digest.\n",
    "annotations": "taxonomy.json, the review prose, the edit ledger.\n",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("name", help="lowercase, digits and hyphens; becomes a URL segment")
    ap.add_argument("--apply", action="store_true", help="actually create it")
    ap.add_argument("--title", default=None, help="display name (default: the name, capitalised)")
    ap.add_argument("--tagline", default=None)
    ap.add_argument("--subtitle", default=None)
    args = ap.parse_args()

    name = args.name
    if not paperlib.NAME_RE.match(name):
        paperlib.die(f"invalid area name {name!r}: lowercase letters, digits and "
                     f"hyphens, starting with a letter (it becomes a directory "
                     f"and a URL segment)")
    root = paperlib.area_path(name)
    if root.exists():
        paperlib.die(f"areas/{name}/ already exists — refusing to touch it")

    cfg = paperlib.load_config()
    title = args.title or name.replace("-", " ").capitalize()
    project = {
        "_comment": [
            "What this AREA calls itself. Inherits paperlib.json; anything set here",
            "wins. site_dir is the path under the web root deploy.sh publishes into.",
        ],
        "name": title,
        "tagline": args.tagline or f"papers on {title.lower()}",
        "subtitle": args.subtitle or cfg.get("subtitle", ""),
        "footer_scope": f"the {title.lower()} literature",
        "site_dir": f"{cfg.get('site_dir_prefix', 'paperlib')}/{name}",
        "uplink_label": cfg.get("name", "PaperLib"),
        "uplink_href": f"/{cfg.get('site_dir_prefix', 'paperlib')}/",
    }

    planned: list[tuple[str, str]] = []
    for d in paperlib.AREA_DIRS:
        planned.append(("mkdir", f"areas/{name}/{d}/"))
        top = d.split("/")[0]
        if d in GITKEEP_NOTE:
            planned.append(("write", f"areas/{name}/{d}/.gitkeep"))
    planned.append(("write", f"areas/{name}/project.json"))
    planned.append(("write", f"areas/{name}/annotations/review_prose/first.md"))

    if not args.apply:
        print(f"new_area: DRY RUN for area {name!r} — nothing written.\n")
        for verb, path in planned:
            print(f"  {verb:6s} {path}")
        print(f"\n  project.json would say:")
        for k, v in project.items():
            if not k.startswith("_"):
                print(f"    {k}: {v!r}")
        print(f"\nRe-run with --apply to create it.")
        return 0

    for d in paperlib.AREA_DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)
    for d, note in GITKEEP_NOTE.items():
        (root / d / ".gitkeep").write_text(f"# {note}", encoding="utf-8")
    (root / "project.json").write_text(
        json.dumps(project, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    dest = root / "annotations" / "review_prose" / "first.md"
    if PROSE_SRC.exists():
        dest.write_text(PROSE_SRC.read_text(encoding="utf-8"), encoding="utf-8")
    else:
        print(f"new_area: WARNING — {PROSE_SRC} missing; write {dest} by hand "
              f"before `make review`.", file=sys.stderr)

    print(f"new_area: created areas/{name}/ ({len(paperlib.AREA_DIRS)} directories)")
    print(f"  next:  drop PDFs into inbox/{name}/")
    print(f"         make ingest AREA={name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
