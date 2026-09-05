#!/usr/bin/env python3
"""Fill the four prose sections of a sidecar — recorded, reversible, refusable.

The ingest writes `## Abstract`, `## Summary`, `## Key points` and `## Limitations`
as marked placeholders with `status: prose-pending`, because they are read off the
paper by something that read the paper. This installs that prose once it exists.

`scripts/edit_upstream.py` is the sanctioned path for `meta/`, but it edits
FRONTMATTER fields and whole files; it has no notion of a markdown section. Rather
than widen it — its refusals are tuned to identity fields and it should keep
being about those — this does the one job, with the same three mechanisms behind
it: a git-tracked diff, a sidecar hash in the manifest, and the shared ledger in
`annotations/upstream_edits.json`.

WHAT IT REFUSES, and why:

  * a sidecar whose status is not `prose-pending`, without --allow-overwrite.
    Prose already written was written by somebody; silently replacing it is the
    one thing this must never do.
  * any file outside meta/, and any path with a `..` in it.
  * a section that is not one of the four. The Provenance and Citation sections
    are the ingest's account of where the file came from, not commentary.
  * running at all without the owner's approving words in --approved.
  * a file with mixed line endings, and it round-trips whatever it finds. A
    careless read-modify-write once turned nine one-line additions into a
    663-insertion diff by normalising CRLF across a whole collection.

    python3 scripts/write_prose.py --prose p.json                 # DRY RUN, a diff
    python3 scripts/write_prose.py --prose p.json --apply --approved "..."

The prose file is keyed by source filename or sha256:

    {"Surname(2024) Venue; Title.pdf": {
        "abstract": "...", "summary": "...",
        "key_points": ["...", "..."], "limitations": "..."}}

Standard library only.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import paperlib  # noqa: E402

ROOT = build.ROOT
META = build.META
LEDGER = ROOT / "annotations" / "upstream_edits.json"

SECTIONS = {"abstract": "Abstract", "summary": "Summary",
            "key_points": "Key points", "limitations": "Limitations"}


def section_span(text: str, heading: str) -> tuple[int, int] | None:
    """(start, end) of a section's BODY, exclusive of its heading and the next."""
    m = re.search(rf"^## {re.escape(heading)}[ \t]*$", text, re.M)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r"^## ", text[start:], re.M)
    return (start, start + nxt.start()) if nxt else (start, len(text))


def render(key: str, value) -> str:
    if key == "key_points":
        items = [str(v).strip() for v in (value or []) if str(v).strip()]
        return "\n".join(f"- {i}" for i in items)
    return str(value or "").strip()


def apply_prose(text: str, prose: dict) -> tuple[str, list[str]]:
    """Replace the four section bodies. Returns (new text, sections touched)."""
    touched = []
    # Last section first: every replacement shifts the offsets of everything after
    # it, and walking backwards means the spans computed earlier stay valid.
    for key in ("limitations", "key_points", "summary", "abstract"):
        if key not in prose:
            continue
        body = render(key, prose[key])
        if not body:
            continue
        span = section_span(text, SECTIONS[key])
        if span is None:
            continue
        text = text[:span[0]] + f"\n\n{body}\n\n" + text[span[1]:]
        touched.append(key)
    return text, list(reversed(touched))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prose", required=True,
                    help="JSON keyed by source filename or sha256")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--allow-overwrite", action="store_true",
                    help="replace prose that is already written (status is not "
                         "prose-pending). Somebody wrote that; be sure.")
    ap.add_argument("--approved", default=None,
                    help="the owner's words, recorded in the ledger; required with --apply")
    ap.add_argument("--quiet", action="store_true", help="counts, not diffs")
    args = ap.parse_args()

    if args.apply and not args.approved:
        print("write_prose: --apply needs --approved with the owner's words.",
              file=sys.stderr)
        return 2

    prose_all = json.loads(Path(args.prose).read_text(encoding="utf-8"))

    # sha256 -> sidecar, so the prose file can be keyed by either.
    by_sha, by_src = {}, {}
    for side in sorted(META.glob("*.md")):
        fm = build.parse_frontmatter(side.read_text(encoding="utf-8"))
        if fm.get("source"):
            by_src[fm["source"]] = side
        if fm.get("sha256"):
            by_sha[fm["sha256"]] = side

    written = refused = 0
    entries = []
    for key, prose in prose_all.items():
        side = by_src.get(key) or by_sha.get(key)
        if side is None:
            print(f"  REFUSED: no sidecar for {key!r}")
            refused += 1
            continue

        raw = side.read_bytes()
        crlf, lf = raw.count(b"\r\n"), raw.count(b"\n")
        if crlf and crlf != lf:
            print(f"  REFUSED: {side.name} has MIXED line endings; not touching it.")
            refused += 1
            continue
        text = raw.decode("utf-8")
        if crlf:
            text = text.replace("\r\n", "\n")

        fm = build.parse_frontmatter(text)
        if fm.get("status") != "prose-pending" and not args.allow_overwrite:
            print(f"  REFUSED: {side.name} is status {fm.get('status')!r}, not "
                  f"prose-pending. Its prose was written by somebody; pass "
                  f"--allow-overwrite if you mean to replace it.")
            refused += 1
            continue

        new, touched = apply_prose(text, prose)
        if not touched:
            print(f"  REFUSED: {side.name} — no section matched.")
            refused += 1
            continue
        new = re.sub(r"^status: prose-pending$", "status: ok", new, count=1, flags=re.M)
        if new == text:
            continue

        if not args.quiet:
            print(f"\n=== {side.name}")
            for line in difflib.unified_diff(
                    text.splitlines(), new.splitlines(),
                    fromfile="before", tofile="after", lineterm="", n=1):
                print("  " + line)

        out = new.replace("\n", "\r\n").encode("utf-8") if crlf else new.encode("utf-8")
        if args.apply:
            side.write_bytes(out)
        entries.append({
            "date": date.today().isoformat(),
            "file": str(side.relative_to(ROOT)),
            "keys": touched + ["status"],
            "reason": "the four prose sections, written by reading the paper",
            "evidence": "the paper itself, in raw/",
            "approved": args.approved,
            "sha256_after": hashlib.sha256(out).hexdigest(),
        })
        written += 1

    if args.apply and entries:
        # The ledger is an OBJECT with an `edits` list, not a bare list. Unwrapping
        # it to the list and writing that back silently destroys the wrapper, and
        # build.py's `doc.get("edits")` then raises on a list -- which is how this
        # was found, on 2026-09-05, after 60 sidecars had already been written.
        led = json.loads(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else {}
        if isinstance(led, list):
            led = {"edits": led}
        prior = led.get("edits", [])
        seq = max([e.get("seq", 0) for e in prior] or [0])
        for e in entries:
            seq += 1
            e["seq"] = seq
        led["edits"] = prior + entries
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text(json.dumps(led, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")

    verb = "written" if args.apply else "would be written"
    print(f"\nwrite_prose: {written} sidecar(s) {verb} · {refused} refused")
    if not args.apply and written:
        print("write_prose: nothing written. Re-run with --apply --approved \"...\".")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
