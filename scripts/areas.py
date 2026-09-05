#!/usr/bin/env python3
"""What areas exist and what each one holds. Reads only; writes nothing."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402
import portal  # noqa: E402


def main() -> int:
    areas = paperlib.list_areas()
    if not areas:
        print("areas: none yet.  make new-area NAME=<lowercase-name> APPLY=1")
        return 0

    reg = paperlib.scan_all_areas(paperlib.frontmatter_parser())
    shared = {sha: r for sha, r in reg.items() if len(r["areas"]) > 1}

    rows = [portal.area_stats(a) for a in areas]
    w = max(len(a) for a in areas)
    print(f"{'area'.ljust(w)}  {'src':>4} {'meta':>4} {'papers':>6} {'topics':>6}  "
          f"{'map':<3} {'prose':<9} data as of")
    print("-" * (w + 52))
    for s in rows:
        # "not built" and "zero papers" are different states; a dash says which.
        papers = "-" if not s["built"] else str(s["papers"])
        topics = "-" if not s["built"] else str(s["topics"])
        pending = f"{s['pending']} pending" if s["pending"] else "complete"
        print(f"{s['area'].ljust(w)}  {s['sources']:>4} {s['sidecars']:>4} "
              f"{papers:>6} {topics:>6}  {'yes' if s['has_map'] else 'no':<3} "
              f"{pending:<9} {s['data_as_of'] or 'not built'}")

    print(f"\n{len(reg)} distinct papers across {len(areas)} areas.")
    if shared:
        print(f"{len(shared)} held in more than one area:")
        for sha, r in sorted(shared.items(), key=lambda kv: kv[1]["title"]):
            print(f"  {r['title'][:60]!r}")
            print(f"    {', '.join(sorted(r['areas']))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
