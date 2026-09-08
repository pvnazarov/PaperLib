#!/usr/bin/env python3
"""raw/ filename repair — restore the name each sidecar already declares.

WHY THIS EXISTS AND WHY IT IS NOT AN ADD-ONLY VIOLATION (CLAUDE.md 2.2)

`raw/` is add-only: no existing file may be modified, renamed or deleted. That
rule exists for one reason -- the filename is the join key, so renaming a file
silently breaks the `sha256:` claim its sidecar makes, for the whole area, with
no error anywhere.

This script is the inverse case. It runs where the join is ALREADY broken: the
bytes are right, the sidecars are right, and only the names on disk drifted --
typically because `meta/` arrived by `git clone` (which stores NFC) while `raw/`
arrived by some other route that renormalised or truncated the names. INSTALL.md
makes that split routine: a clone carries meta/ and cannot carry raw/.

Every sidecar records `sha256:` and `source:` -- the canonical filename. So the
repair is fully determined by the bytes and invents nothing. A file is renamed
only to the name its own hash proves it should have. No byte changes, no hash
changes, nothing is deleted, and a rename that would overwrite anything is
refused. Run `make verify` afterwards: that is the real proof.

DRY RUN BY DEFAULT. Nothing is touched without --apply.

    python3 scripts/fix_raw_names.py                 # report what drifted
    python3 scripts/fix_raw_names.py --apply         # rename, verified
    PAPERLIB_AREA=<area> python3 scripts/fix_raw_names.py

Standard library only. No network.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

ROOT = build.ROOT
RAW, META = ROOT / "raw", ROOT / "meta"


def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sidecars() -> dict[str, str]:
    """sha256 -> the canonical raw/ filename the sidecar declares."""
    want: dict[str, str] = {}
    for m in sorted(META.glob("*.md")):
        sha = src = None
        with m.open(encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("sha256:"):
                    sha = line.split(":", 1)[1].strip()
                elif line.startswith("source:"):
                    src = line.split(":", 1)[1].strip()
                elif line.startswith("# --- ingest"):
                    break
        if not sha or not src:
            print(f"  WARN   {m.name}: no sha256/source in frontmatter")
            continue
        if sha in want and want[sha] != src:
            print(f"  WARN   two sidecars claim {sha[:12]}: {want[sha]!r} vs {src!r}")
        want[sha] = src
    return want


# `Author(Year) Venue; Title.pdf` -- the convention ingest_inbox.py generates.
NAME_RE = re.compile(r"^(?P<author>.+?)\((?P<year>\d{4})\)\s*(?P<venue>[^;]*);\s*(?P<title>.*)$")


def why(actual: str, canonical: str) -> str:
    """Name the drift, because the cause decides whether it recurs.

    Ordered cheapest-first, and deliberately specific: "renamed" tells you
    nothing you could act on, and every case below has actually occurred.
    """
    if unicodedata.normalize("NFC", actual) == unicodedata.normalize("NFC", canonical):
        a = "NFD" if unicodedata.normalize("NFC", actual) != actual else "NFC"
        c = "NFD" if unicodedata.normalize("NFC", canonical) != canonical else "NFC"
        return f"unicode normalisation ({a} on disk, {c} in meta/)"

    if " ".join(actual.split()) == " ".join(canonical.split()):
        return "whitespace only"

    # Publisher markup leaves a real space inside a token -- `NPM1 -mutated`,
    # `CD8 + T cell`, `N 6 -Methyladenosine`. Correcting the registered title
    # then renames the file, and every such rename differs from the old name by
    # spaces alone. Distinguished from "whitespace only" above, which is a
    # collapsed run of spaces rather than spaces removed outright.
    if actual.replace(" ", "") == canonical.replace(" ", ""):
        return "spacing inside a title (publisher markup artifact)"

    if len(actual) < len(canonical) and canonical.startswith(actual[:-4]):
        return f"truncated ({len(actual.encode())} bytes on disk vs {len(canonical.encode())})"

    # The case seen on the first real import: an older archive generated under an
    # earlier convention that abbreviated venues (`Blood Adv` for `Blood
    # Advances`), sometimes with a different registered year. The bytes are fine
    # and every other segment agrees -- it is a convention drift, not corruption,
    # and it is the one cause that repeats for a whole archive at once.
    a, c = NAME_RE.match(actual), NAME_RE.match(canonical)
    if a and c:
        diff = [k for k in ("author", "year", "venue", "title")
                if a.group(k).strip() != c.group(k).strip()]
        if diff == ["venue"]:
            return f"venue convention ({a.group('venue').strip()!r} -> {c.group('venue').strip()!r})"
        if diff:
            return "differs in " + ", ".join(diff) + " (older naming convention?)"

    return "renamed"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true",
                    help="perform the renames (default: dry run)")
    args = ap.parse_args()

    if not RAW.is_dir():
        print(f"fix_raw_names: no raw/ at {RAW}", file=sys.stderr)
        return 2

    want = sidecars()
    files = [p for p in sorted(RAW.iterdir()) if p.is_file() and not p.name.startswith(".")]
    print(f"fix_raw_names: area {build.AREA} · {len(files)} files in raw/ · "
          f"{len(want)} sidecars\n")

    okc = plans = orphans = 0
    todo: list[tuple[Path, str]] = []
    seen: set[str] = set()

    for f in files:
        sha = sha256_of(f)
        canonical = want.get(sha)
        if canonical is None:
            print(f"  ORPHAN {f.name}\n         its bytes match no sidecar -- left alone")
            orphans += 1
            continue
        seen.add(sha)
        if f.name == canonical:
            okc += 1
            continue
        todo.append((f, canonical))
        plans += 1
        print(f"  RENAME {f.name}\n      -> {canonical}\n         {why(f.name, canonical)}")

    missing = [want[s] for s in want.keys() - seen]
    for name in sorted(missing):
        print(f"  ABSENT {name}\n         a sidecar claims it but no file in raw/ has those bytes")

    print(f"\nfix_raw_names: correct {okc} · to rename {plans} · "
          f"orphan {orphans} · absent {len(missing)}")

    if not todo:
        print("fix_raw_names: nothing to do.")
        return 1 if (orphans or missing) else 0

    if not args.apply:
        print("fix_raw_names: DRY RUN -- nothing was touched. Re-run with --apply.")
        return 0

    # A rename must never clobber. If the target exists, the two files are either
    # the same bytes (already fine) or different bytes under a contested name --
    # and silently overwriting the second case is the exact loss add-only forbids.
    done = 0
    for f, canonical in todo:
        dest = RAW / canonical
        if dest.exists():
            print(f"  REFUSED {f.name} -> {canonical}: target already exists")
            continue
        before = sha256_of(f)
        f.rename(dest)
        after = sha256_of(dest)
        if before != after:
            print(f"  FATAL  {canonical}: hash changed across the rename", file=sys.stderr)
            return 2
        done += 1
        print(f"  renamed {canonical}")

    print(f"\nfix_raw_names: renamed {done}. Run `make verify` -- that is the proof.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
