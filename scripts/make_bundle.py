#!/usr/bin/env python3
"""raw/ + meta/ + outputs/ -> one downloadable archive in dist/.

TEMPORARY BY DESIGN. render.py links it from the page footer only while the file
is present, so taking the offer down is:

    make bundle-clean AREA=<area> && make render AREA=<area>

The archive lands in dist/ rather than being copied there, because it is hundreds
of megabytes and dist/ is gitignored -- a build product that must never enter the
history. It carries raw/ as it stands, which is publisher PDFs; the same bytes are
already served individually under /pdf/, so this bundles what is reachable rather
than exposing anything new.

    python3 scripts/make_bundle.py            # DRY RUN: says what it would write
    python3 scripts/make_bundle.py --apply

Standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import tarfile
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import paperlib  # noqa: E402

ROOT = build.ROOT
DIST = ROOT / "dist"
PARTS = ("raw", "meta", "outputs")
# render.py looks for exactly this shape, so the two agree in one place.
GLOB = "*_raw-meta-outputs.tar.gz"


def human(n: int) -> str:
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024 or u == "GB":
            return f"{n:.0f} {u}" if u == "B" else f"{n/1:.1f} {u}".replace(".0 ", " ")
        n /= 1024
    return f"{n:.1f} GB"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="actually write the archive")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--level", type=int, default=1,
                    help="gzip level (default 1). Measured on this collection: PDFs "
                         "compress to about 89%% at level 6, so the extra time buys "
                         "roughly a tenth and level 1 gets most of it.")
    args = ap.parse_args()

    area = paperlib.current_area_name(ROOT)
    members, total = [], 0
    for part in PARTS:
        d = ROOT / part
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*")):
            if f.is_file() and f.name != ".gitkeep":
                members.append((f, f"{area}/{part}/{f.relative_to(d)}"))
                total += f.stat().st_size

    out = DIST / f"{args.date}_{area}_raw-meta-outputs.tar.gz"
    if not args.apply:
        print(f"make_bundle: DRY RUN — nothing written.")
        for part in PARTS:
            n = sum(1 for f, _ in members if f.is_relative_to(ROOT / part))
            sz = sum(f.stat().st_size for f, _ in members if f.is_relative_to(ROOT / part))
            print(f"  {part:8} {n:>4} files  {human(sz)}")
        print(f"  {'TOTAL':8} {len(members):>4} files  {human(total)} uncompressed")
        print(f"\n  would write dist/{out.name}")
        print(f"  and render.py would link it from the page footer.")
        print("\nRe-run with --apply.")
        return 0

    DIST.mkdir(exist_ok=True)
    for stale in DIST.glob(GLOB):
        if stale.name != out.name:
            stale.unlink()
            print(f"make_bundle: removed stale dist/{stale.name}")
    t0 = time.time()
    tmp = out.with_suffix(".tar.gz.partial")
    # Written to a .partial and renamed, so a page rendered mid-build never links
    # a half-written archive.
    with tarfile.open(tmp, "w:gz", compresslevel=args.level) as tar:
        for f, arc in members:
            tar.add(f, arcname=arc)
    tmp.rename(out)

    h = hashlib.sha256()
    with out.open("rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    size = out.stat().st_size
    print(f"make_bundle: wrote dist/{out.name}")
    print(f"             {len(members)} files · {human(total)} -> {human(size)} "
          f"({100*size//max(total,1)}%) in {time.time()-t0:.0f}s")
    print(f"             sha256 {h.hexdigest()}")
    print(f"\nrun `make render AREA={area}` to put the link on the page,")
    print(f"and `make bundle-clean AREA={area} && make render AREA={area}` to take it down.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
