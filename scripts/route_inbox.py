#!/usr/bin/env python3
"""inbox/ -> areas/<area>/inbox/ — decide WHICH collection a dropped paper joins.

The shared inbox is the one place papers arrive. Routing is the step that says
which area a paper belongs to, and it is separate from ingestion on purpose:

    inbox/<area>/paper.pdf   ──route──▶   areas/<area>/inbox/paper.pdf
                             ──ingest──▶  areas/<area>/raw/Surname(2024) Venue; Title.pdf
                                          areas/<area>/meta/<same>.md

THE AREA IS NEVER GUESSED. A subdirectory names it, or --area does; a loose file
with neither is reported and left alone. The toolkit's rule that the vectors may
propose but must not decide applies with more force here than to topics: filing a
paper in the wrong area does not misplace it in a list, it puts it in a different
collection with a different taxonomy and a different map.

Ingestion itself is unchanged — the area's own inbox is fed to the toolkit's
ingest_inbox.py, which still refuses a paper with no Crossref-registered DOI,
still names it from the registration, and still refuses to overwrite raw/.

    python3 scripts/route_inbox.py                    # DRY RUN, every area
    python3 scripts/route_inbox.py --area neoantigens # loose files go here too
    python3 scripts/route_inbox.py --apply

Standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def collect(inbox: Path, default_area: str | None) -> tuple[list, list]:
    """(routable, unroutable). A subdirectory names the area; --area is the rest."""
    routable, unroutable = [], []
    known = set(paperlib.list_areas())
    for p in sorted(inbox.rglob("*")):
        if not p.is_file() or p.name.startswith("."):
            continue
        rel = p.relative_to(inbox)
        if len(rel.parts) > 1:
            area = rel.parts[0]
            if area in known:
                routable.append((p, area))
            else:
                unroutable.append((p, f"inbox/{area}/ is not an area "
                                      f"(have: {', '.join(sorted(known)) or 'none'})"))
        elif default_area:
            routable.append((p, default_area))
        else:
            unroutable.append((p, "loose file and no --area given"))
    return routable, unroutable


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--area", default=None,
                    help="area for files sitting loose at the top of inbox/")
    ap.add_argument("--apply", action="store_true", help="actually move the files")
    args = ap.parse_args()

    if args.area and args.area not in paperlib.list_areas():
        paperlib.die(f"no such area: {args.area!r}. "
                     f"Have: {', '.join(paperlib.list_areas()) or 'none'}")
    if not paperlib.INBOX.is_dir():
        print(f"route_inbox: no inbox/ — nothing to do.")
        return 0

    routable, unroutable = collect(paperlib.INBOX, args.area)
    if not routable and not unroutable:
        print("route_inbox: inbox/ is empty.")
        return 0

    # What every area already holds, by bytes. Rescanned from meta/ rather than read
    # from index/registry.json: the registry is derived and may be stale, and the
    # sidecars are what `make verify` re-proves against the bytes.
    held = paperlib.scan_all_areas(paperlib.frontmatter_parser())

    mode = "MOVING" if args.apply else "DRY RUN — nothing moved"
    print(f"route_inbox: {mode}\n")

    moved = skipped = 0
    for src, area in routable:
        dest_dir = paperlib.area_path(area) / "inbox"
        dest = dest_dir / src.name
        sha = sha256_of(src)
        rel = src.relative_to(paperlib.PROJECT)

        elsewhere = paperlib.held_elsewhere(held, sha, area)
        note = ""
        if sha in held and area in held[sha]["areas"]:
            # Same bytes, same area: the ingest would refuse this anyway. Say so here
            # rather than let it look like a routing failure two commands later.
            print(f"  SKIP  {rel}")
            print(f"        already in {area} as {held[sha]['areas'][area]!r}")
            skipped += 1
            continue
        if elsewhere:
            # Allowed and recorded: the areas are worked on independently, so a
            # paper can genuinely matter in two. The sidecar records the other area
            # and the page shows it; the bytes are stored twice, which is the price
            # of an area staying separable.
            note = f"  [also held in: {', '.join(elsewhere)}]"

        if dest.exists():
            print(f"  SKIP  {rel}")
            print(f"        areas/{area}/inbox/{src.name} already exists")
            skipped += 1
            continue

        print(f"  ->    {rel}")
        print(f"        areas/{area}/inbox/{src.name}{note}")
        if args.apply:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
        moved += 1

    for src, why in unroutable:
        print(f"  ?     {src.relative_to(paperlib.PROJECT)}")
        print(f"        {why} — left where it is")

    print(f"\nroute_inbox: {moved} to route, {skipped} skipped, "
          f"{len(unroutable)} unroutable.")
    if not args.apply and moved:
        print("             Re-run with --apply to move them.")
    if args.apply and moved:
        areas = sorted({a for _, a in routable})
        print("\n  next, per area — read the dry run before applying:")
        for a in areas:
            print(f"    make inbox AREA={a}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
