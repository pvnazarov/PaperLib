#!/usr/bin/env python3
"""Pack the TOOL, without the collection, into a tarball another instance can start from.

    python3 scripts/make_archive.py                 # dry run: the file list and the checks
    python3 scripts/make_archive.py --apply         # -> dist-archive/<name>-<date>.tar.gz

The distinction this script exists to enforce, and the reason it is a script and
not a `tar --exclude` line:

    the TOOL is the scripts, the page, the Makefile and the written-down rules.
    the COLLECTION is raw/, meta/, outputs/, wiki/, data/, and the annotations,
    reports and evals that describe one particular set of papers.

The second must not leave with the first. So the file list here is an ALLOW-LIST.
A deny-list is the wrong shape for this job: it is correct only about the files
that existed when it was written, and every file added afterwards defaults to
being shipped. An allow-list defaults to silence, and the cost of that -- a new
file that has to be added here to travel -- is the cost of being sure.

Belt and braces, because an allow-list still ships whatever is INSIDE an allowed
file: after staging, every file is scanned for the collection's own fingerprints
(source filenames, roster names, DOIs) and the archive is refused if any appear.
Run --apply and read what it prints; both halves are reported, not just the tally.

Standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tarfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

# PAPERLIB: packs the TOOL, so its root is the project, not an area.
# NOT YET multi-area aware: its collection-scanning still assumes a single
# root/meta and root/wiki. Review it before relying on it to pack.
ROOT = paperlib.PROJECT
OUT = ROOT / "dist-archive"

# ---------------------------------------------------------------- the tool ---
# Exact paths, and directories whose *.py / *.md / *.css / *.js are all tool.
FILES = [
    "RETARGETING.md",
    "Makefile",
    "requirements.txt",
    "requirements-tier1.txt",
    "deploy.sh",
    ".gitignore",
]
GLOBS = [
    "scripts/*.py",
    "src/*",
]

# Files written specially for the archive: (path in archive, path here).
# `annotations/review_prose/` is the one place where this instance's own prose
# lives, and shipping it would hand a new collection somebody else's account of
# how its topics were decided -- the exact failure the FATAL in make_review.py
# exists to prevent. Only the generic block travels; the other two go as
# templates, so a re-clustering elsewhere hits that FATAL and writes its own.
# (path IN the archive, path in THIS tree)
#
# The two READMEs and the two CLAUDE.md files are different documents on purpose.
# This repository's are about ONE collection -- they name its papers, its people
# and its decisions -- and handing those to a new field would be handing over the
# collection in prose. The archive gets versions written for a tool with no
# collection yet; the scan below is what proves they stayed that way.
RENAMES = [
    ("README.md", "docs/templates/README-toolkit.md"),
    ("CLAUDE.md", "docs/templates/CLAUDE-toolkit.md"),
    ("project.json", "docs/templates/project.json"),
    ("annotations/review_prose/first.md", "annotations/review_prose/first.md"),
    ("annotations/review_prose/consolidate.md.template",
     "docs/templates/review_prose_consolidate.md"),
    ("annotations/review_prose/recluster.md.template",
     "docs/templates/review_prose_recluster.md"),
    ("wiki/group.md.template", "docs/templates/group.md"),
    ("eval/README.md", "docs/templates/eval_README.md"),
]

# Empty directories the pipeline expects to exist.
KEEPDIRS = ["raw", "meta", "outputs", "wiki", "data", "reports", "inbox",
            "eval", "annotations"]

KEEP_NOTE = {
    "raw": "The source files themselves (PDFs and the like). Add-only: a file may be "
           "added, never modified, renamed or deleted -- every sha256 in meta/ depends "
           "on that.",
    "meta": "One sidecar per source file: frontmatter plus Abstract / Summary / Key "
            "points / Limitations. This is the ground truth the build reads.",
    "outputs": "The literature review. The taxonomy comes from it -- see RETARGETING.md "
               "step 5.",
    "wiki": "Free-form notes about the collection. `group.md` here is the roster that "
            "decides which papers count as your own (docs/templates/group.md).",
    "data": "Generated: library.json, manifest.json, bib_cache.json, similarity.json.",
    "reports": "Generated and hand-written reports. Drafts land here before they are "
               "promoted.",
    "inbox": "Drop new papers here, then `make inbox`.",
    "eval": "Pre-registered expectations, committed BEFORE the answers are looked at "
            "(docs/templates/eval_README.md).",
    "annotations": "Local annotations and the review prose blocks.",
}

# --------------------------------------------------------- the fingerprints --
# A DOI is only evidence of a leak if it is one of OURS. An invented one in a test
# fixture or a worked example in the runbook is not collection data, and flagging
# it would train whoever runs this to skim the report -- which is the one way a
# scan like this actually fails.
DOI = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]{4,}")
# Text files only; a fingerprint scan of a binary is noise.
TEXTY = {".md", ".py", ".json", ".txt", ".html", ".css", ".js", ".sh", ".yml", ".cfg", ""}


def collection_fingerprints() -> tuple[set, set, set]:
    """Strings that exist only because of THIS collection: source filenames, the
    surnames those filenames begin with, the roster's names, and the DOIs actually
    held. All read from the live tree, so the check keeps working as the collection
    grows and cannot go stale the way a hardcoded list would."""
    sources, surnames, dois = set(), set(), set()
    meta = ROOT / "meta"
    if meta.is_dir():
        for p in meta.glob("*.md"):
            stem = p.name[:-3]                       # `<source>.md`
            sources.add(stem)
            m = re.match(r"^([^(]+)\(", stem)        # the surname it starts with
            sur = m.group(1).strip() if m else ""
            # Short tokens are matched as whole words below, but a 3-letter surname
            # is still a coin toss against ordinary English -- and a false positive
            # here costs more than a missed one, because it is what teaches the
            # operator to stop reading the report.
            if len(sur) > 3:
                surnames.add(sur)
            text = p.read_text(encoding="utf-8", errors="replace")
            for dm in DOI.finditer(text):
                dois.add(dm.group(0).rstrip(".,);"))
    names = set()
    group = ROOT / "wiki" / "group.md"
    if group.exists():
        for line in group.read_text(encoding="utf-8").splitlines():
            parts = [c.strip() for c in line.split(",")]
            if len(parts) >= 3 and len(parts[2].split()) >= 2:
                names.add(parts[2])
                names.add(parts[2].split()[-1].title())
    return sources, surnames, names, dois


def scan(stage: Path, sources: set, surnames: set, names: set,
         dois: set) -> tuple[list[str], list[str]]:
    """-> (fatal, noted). Whole-word matches only: `Chang` as a substring lives
    inside `Changed`, and a scan that cries wolf on the word "changes" is a scan
    nobody reads.

    TWO CLASSES, because they are two different questions and collapsing them
    makes the serious one unreadable:

      FATAL -- a whole source FILENAME, or a DOI the collection actually holds.
        Either is a piece of the collection itself and must not travel. This is
        what the owner asked for: the tool, not the literature.

      NOTED -- a bare surname, of an author or of somebody on the roster. These
        occur in worked examples inside docstrings, which are SOURCE CODE and are
        meant to travel; the examples are the most useful comments in the
        codebase precisely because they are real cases. They are still listed in
        full, every occurrence, so that what travels is a decision somebody made
        rather than something nobody looked at.
    """
    fatal, noted = [], []
    for p in sorted(stage.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in TEXTY:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        rel = p.relative_to(stage)
        for s in sorted(sources):
            if s in text:
                fatal.append(f"{rel}: SOURCE FILENAME {s[:70]!r}")
        for d in sorted(dois):
            if d in text:
                fatal.append(f"{rel}: DOI held in the collection {d!r}")
        # EVERY match, not the first: a report that stops at one hit per file
        # turns a single review pass into fifteen, and the fifteenth gets rushed.
        for kind, needles in (("author surname", surnames), ("roster name", names)):
            for s in sorted(needles):
                if re.search(rf"(?<![A-Za-z0-9]){re.escape(s)}(?![A-Za-z0-9])", text):
                    noted.append(f"{rel}: {kind} {s[:60]!r}")
    return fatal, noted


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write the tarball")
    ap.add_argument("--name", default=None, help="archive basename (default from project.json)")
    ap.add_argument("--date", default=date.today().isoformat())
    args = ap.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build
    base = args.name or (build.load_project()["name"].lower().replace(" ", "-") + "-toolkit")

    want: list[tuple[str, Path]] = []
    missing = []
    for rel in FILES:
        src = ROOT / rel
        (want.append((rel, src)) if src.exists() else missing.append(rel))
    for pat in GLOBS:
        found = sorted(ROOT.glob(pat))
        if not found:
            missing.append(pat)
        for src in found:
            if src.is_file():
                want.append((str(src.relative_to(ROOT)), src))
    for rel, src_rel in RENAMES:
        src = ROOT / src_rel
        (want.append((rel, src)) if src.exists() else missing.append(f"{rel} <- {src_rel}"))

    if missing:
        print("make_archive: FATAL: these are on the list but not on disk:",
              file=sys.stderr)
        for m in missing:
            print(f"  {m}", file=sys.stderr)
        return 1

    stage = OUT / f"{base}-{args.date}"
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    for rel, src in want:
        dest = stage / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        shutil.copymode(src, dest)
    for d in KEEPDIRS:
        (stage / d).mkdir(parents=True, exist_ok=True)
        (stage / d / ".gitkeep").write_text(
            f"# {d}/\n#\n# {KEEP_NOTE[d]}\n#\n# This file only keeps the empty directory. "
            f"Delete it once the directory has real content.\n", encoding="utf-8")

    sources, surnames, names, dois = collection_fingerprints()
    fatal, noted = scan(stage, sources, surnames, names, dois)
    n_files = sum(1 for p in stage.rglob("*") if p.is_file())
    size = sum(p.stat().st_size for p in stage.rglob("*") if p.is_file())

    print(f"make_archive: staged {n_files} files, {size / 1024:.0f} KB, in "
          f"{stage.relative_to(ROOT)}")
    print(f"make_archive: fingerprint scan — {len(sources)} source filenames, "
          f"{len(surnames)} author surnames, {len(names)} roster names and "
          f"{len(dois)} held DOIs searched for")
    if fatal:
        print(f"make_archive: FATAL: {len(fatal)} piece(s) of the collection are in "
              f"the staged tool:", file=sys.stderr)
        for h in fatal:
            print(f"  {h}", file=sys.stderr)
        return 1
    print("make_archive: no source filename and no held DOI in any staged file — "
          "the collection is not in the archive")
    if noted:
        print(f"make_archive: {len(noted)} personal name(s) travel, in worked "
              f"examples inside docstrings. Read the list; they are source code, "
              f"not data, but they are real people:")
        for h in noted:
            print(f"  note  {h}")
    else:
        print("make_archive: no personal name from the collection or the roster "
              "appears in any staged file")

    if not args.apply:
        shutil.rmtree(stage)
        print("make_archive: DRY RUN — staging removed, no tarball written. "
              "Re-run with --apply.")
        return 0

    tar_path = OUT / f"{base}-{args.date}.tar.gz"
    # Deterministic: sorted entries, no mtimes, no uid/gid, no per-run gzip stamp.
    import gzip
    buf = OUT / f".{base}.tar"
    with tarfile.open(buf, "w") as tf:
        for p in sorted(stage.rglob("*")):
            ti = tf.gettarinfo(p, arcname=str(Path(stage.name) / p.relative_to(stage)))
            ti.mtime, ti.uid, ti.gid, ti.uname, ti.gname = 0, 0, 0, "", ""
            if p.is_file():
                with p.open("rb") as fh:
                    tf.addfile(ti, fh)
            else:
                tf.addfile(ti)
    with buf.open("rb") as fh, gzip.GzipFile(tar_path, "wb", mtime=0) as gz:
        shutil.copyfileobj(fh, gz)
    buf.unlink()

    sha = hashlib.sha256(tar_path.read_bytes()).hexdigest()
    (OUT / f"{tar_path.name}.sha256").write_text(f"{sha}  {tar_path.name}\n",
                                                 encoding="utf-8")
    print(f"make_archive: {tar_path.relative_to(ROOT)}  "
          f"{tar_path.stat().st_size / 1024:.0f} KB")
    print(f"make_archive: sha256 {sha}")
    print(f"make_archive: staging kept at {stage.relative_to(ROOT)} for inspection")
    return 0


if __name__ == "__main__":
    sys.exit(main())
