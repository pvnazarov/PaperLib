#!/usr/bin/env python3
"""Edit an upstream file under `meta/`, `outputs/` or `wiki/` — recorded, attributable, reversible.

D15 (owner, 2026-09-03: *"I allow you to modify sidecar. Change the rules. Only -
always ask if you modify"*) retires §2's blanket ban on writing to the copied
KBase area. What replaces it is not a promise to be careful; it is this tool plus
two other mechanisms, and none of the three is sufficient alone:

  1. `meta/` is tracked in git       -> every edit has a real, reversible diff
  2. manifest.json hashes each SIDECAR's own bytes  -> a change to one is visible
  3. this tool writes `annotations/upstream_edits.json`  -> which changes were OURS

Mechanism 3 is why the tool exists rather than just using an editor. Without a
ledger, mechanism 2 can only say "something moved", and a sidecar re-exported
from the laptop would be indistinguishable from an edit made here.

**`raw/` is still refused.** Those are publisher PDFs and their sha256 is the
chain `make verify` checks; nothing good comes of editing them.

**Dry run by default.** It prints a unified diff and writes nothing. `--apply`
writes, and `--apply` is what the owner's "always ask" gates: the plan must carry
their approval in `approved`, and the diff should have been shown to them first.

    python3 scripts/edit_upstream.py --plan plan.json            # show the diff
    python3 scripts/edit_upstream.py --plan plan.json --apply     # write it

Plan format:

    {"approved": "owner, 2026-09-03: \\"...their words...\\"",
     "edits": [{"file": "outputs/2026-09-04_literature_review.md",
                "add_from":  "reports/2026-09-04_literature_review.md",
                "reason":   "...", "evidence": "..."},
               {"file": "meta/X.pdf.md",
                "set":      {"doi": "10.1234/x"},
                "set_list": {"authors": ["A. One", "B. Two"]},
                "reason":   "why this belongs in the sidecar",
                "evidence": "where the fact was read from"}]}

Standard library only, like the rest of the build.
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
import paperlib  # noqa: E402

# PAPERLIB: ROOT is the AREA being worked on (scripts/paperlib.py).
ROOT = paperlib.resolve_root()
LEDGER = ROOT / "annotations" / "upstream_edits.json"

# Where an edit may land. `raw/` is deliberately absent and is refused by name.
EDITABLE = ("meta", "outputs", "wiki")

# Fields that identify the record or the file it describes. Changing any of these
# breaks a join that other code trusts: `source` is the review's join key and the
# path to the PDF, `sha256`/`size_bytes` are the byte chain `make verify` checks,
# `id` is the page's route. A correction to one of these is upstream's to make.
PROTECTED = {"id", "id_basis", "source", "sha256", "size_bytes", "media",
             "processed", "processor", "status"}

def b(n: int) -> bytes:
    return bytes([n])


BSLASH = chr(92)
QUOTE = chr(34)
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
# The section comments the sidecars use, e.g. `# --- bibliographic ------------`
SECTION = re.compile(r"^# --- (?P<name>[a-z][^-]*?)\s*-+\s*$", re.M)


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_preserving(path: Path) -> tuple[str, str]:
    """-> (text with LF endings, the file's actual newline) — or raise on mixed.

    KBase writes these sidecars with **CRLF**. The first version of this tool used
    `read_text()`/`write_text()`, whose universal-newline handling silently
    rewrote all 64 line endings of every file it touched: `git diff` showed
    "663 insertions, 590 deletions" for 9 added fields. That is a whole-file
    reformat of upstream's bytes dressed up as an edit, and it defeats the point
    of tracking meta/ in git -- the diff no longer shows what changed.

    So endings are round-tripped exactly. A file with MIXED endings is refused
    rather than normalised: normalising is a decision about upstream's formatting
    that is not ours to take silently.
    """
    raw = path.read_bytes().decode("utf-8")
    crlf = raw.count("\r\n")
    lf = raw.count("\n") - crlf
    if crlf and lf:
        raise ValueError(f"mixed line endings ({crlf} CRLF, {lf} LF); "
                         f"refusing to normalise upstream's formatting")
    if "\r" in raw.replace("\r\n", ""):
        raise ValueError("bare CR line endings; refusing to guess")
    return raw.replace("\r\n", "\n"), ("\r\n" if crlf else "\n")


def write_preserving(path: Path, text: str, newline: str) -> None:
    out = text.replace("\n", newline) if newline != "\n" else text
    path.write_bytes(out.encode("utf-8"))


def fm_scalar(head: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:[ \t]*(.*)$", head, re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v or None


def fm_has_key(head: str, key: str) -> bool:
    return re.search(rf"^{re.escape(key)}:", head, re.M) is not None


def fm_list(head: str, key: str) -> list[str] | None:
    """The current value of a list field, or None if it is absent/empty."""
    m = re.search(rf"^{re.escape(key)}:[ \t]*(?P<inline>.*)\n"
                  rf"(?P<block>(?:[ \t]+-[ \t]*.*\n)*)", head + "\n", re.M)
    if not m:
        return None
    inline = m.group("inline").strip()
    if inline:
        return [inline]                       # a scalar sitting where a list goes
    out = []
    for line in m.group("block").splitlines():
        im = re.match(r"^[ \t]+-[ \t]*(.*)$", line)
        if im:
            v = _unquote_val(im.group(1))
            if v:
                out.append(v)
    return out or None


def _unquote_val(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        q, v = v[0], v[1:-1]
        # Un-escape what quote() escapes. YAML double quotes take backslash
        # escapes; single quotes take a doubled quote instead. Without this, the
        # one author in this corpus with a nickname -- `Xuhai "Orson" Xu` -- read
        # back as `Xuhai \\"Orson\\" Xu` and would have rendered with visible
        # backslashes on the page, AND made the value fail its own round-trip so
        # a re-run of the same edit looked like a conflicting overwrite.
        if q == '"':
            v = v.replace(BSLASH + QUOTE, QUOTE).replace(BSLASH + BSLASH, BSLASH)
        else:
            v = v.replace("''", "'")
    return v.strip()


def quote(v: str) -> str:
    """Double-quote and escape. Everything is quoted rather than only what YAML
    requires: a bare value containing `: ` or a leading `[` changes meaning, and
    titles in this corpus contain both."""
    return QUOTE + (v.replace(BSLASH, BSLASH + BSLASH)
                     .replace(QUOTE, BSLASH + QUOTE)) + QUOTE


def section_bounds(head: str, name: str) -> tuple[int, int] | None:
    """Character span of one `# --- name ---` block within the frontmatter."""
    marks = list(SECTION.finditer(head))
    for i, m in enumerate(marks):
        if m.group("name").strip().startswith(name):
            start = m.end() + 1
            end = marks[i + 1].start() if i + 1 < len(marks) else len(head)
            return start, end
    return None


def _span_holding(head: str, keys: tuple) -> tuple[int, int] | None:
    """Span of the section that already contains one of `keys`."""
    marks = list(SECTION.finditer(head))
    for i, m in enumerate(marks):
        start = m.end() + 1
        end = marks[i + 1].start() if i + 1 < len(marks) else len(head)
        block = head[start:end]
        if any(re.search(rf"^{k}:", block, re.M) for k in keys):
            return start, end
    return None


def insert_into(head: str, key: str, rendered: str) -> str:
    """Place a NEW key where upstream would have put it.

    Sidecars are organised by comment-delimited sections, and `doi`/`authors`
    belong to `bibliographic`. Appending to the end of the frontmatter instead
    would drop a bibliographic field into the provenance block, which reads as
    carelessness in a file whose whole point is being auditable.
    """
    span = section_bounds(head, "bibliographic")
    if span is None:
        # No section with that label. Find the one that actually HOLDS the
        # bibliographic fields instead -- the label is a comment, the fields are
        # the fact. Without this the fallback appended after the LAST section,
        # which dropped `doi` and `authors` into the provenance block; the real
        # sidecars all carry the label so it went unnoticed until a fixture
        # without one was tested.
        span = _span_holding(head, ("title", "year", "doi"))
    if span is None:
        # Still nothing: make the section rather than trailing the fields off
        # the end of unrelated ones.
        body = head.rstrip("\n")
        return (body + "\n\n# --- bibliographic ---------------------------"
                       "----------------\n" + rendered.rstrip("\n"))
    start, end = span
    block = head[start:end]
    # `doi` first in the block (upstream's own order is doi, year, title);
    # anything else after the last line already there.
    if key == "doi":
        return head[:start] + rendered + block + head[end:]
    # Preserve the block's trailing blank line. The sidecars separate sections
    # with one, and swallowing it reformats a file we were only asked to add to.
    body = block.rstrip("\n")
    tail = block[len(body):]          # the newlines that were already there
    return head[:start] + body + "\n" + rendered.rstrip("\n") + tail + head[end:]


def apply_one(text: str, sets: dict, set_lists: dict,
              allow_overwrite: bool) -> tuple[str, list, list]:
    """-> (new text, applied [(key, before, after)], refusals [str])."""
    mo = FRONTMATTER.match(text)
    if not mo:
        return text, [], ["no parseable frontmatter (`---` … `---`)"]
    head = mo.group(1)
    applied, refused = [], []

    for key, val in list(sets.items()) + [(k, v) for k, v in set_lists.items()]:
        is_list = key in set_lists
        if key in PROTECTED:
            refused.append(f"{key!r} identifies the record or its bytes; "
                           f"a correction there is upstream's to make")
            continue
        before = fm_scalar(head, key)
        if is_list:
            if fm_list(head, key) == list(val):
                continue                       # already exactly this: no-op
            rendered = f"{key}:\n" + "".join(f"  - {quote(x)}\n" for x in val)
            present = fm_has_key(head, key)
            # A key with no value (`authors:` alone) counts as absent -- that is
            # the shape upstream ships, and filling it is an addition.
            occupied = present and (before is not None
                                    or re.search(rf"^{key}:[ \t]*\n[ \t]+-",
                                                 head, re.M))
        else:
            # Idempotence BEFORE the overwrite gate: writing a field the value it
            # already holds is not an overwrite, it is nothing. Checked in the
            # other order, a second `--apply` of the same plan came back
            # "REFUSED: already ..." and exited 1, which makes the tool unsafe to
            # re-run -- and re-running is exactly what happens when a plan covers
            # nine files and one of them needed a second look.
            if before is not None and str(before) == str(val):
                continue
            rendered = f"{key}: {quote(str(val))}\n"
            occupied = before is not None

        if occupied and not allow_overwrite:
            cur = before if before is not None else "<a list>"
            refused.append(f"{key!r} is already {cur!r}; adding a MISSING field and "
                           f"changing one upstream filled in are different acts. "
                           f"Pass --allow-overwrite and say so when you ask.")
            continue
        if fm_has_key(head, key):
            # replace the key, list body and all
            head = re.sub(rf"^{re.escape(key)}:[ \t]*.*\n(?:[ \t]+-[ \t]*.*\n)*",
                          rendered, head, count=1, flags=re.M)
        else:
            head = insert_into(head, key, rendered)
        applied.append((key, before, val))

    return text[:mo.start(1)] + head + text[mo.end(1):], applied, refused


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True, help="JSON plan (see the module docstring)")
    ap.add_argument("--apply", action="store_true",
                    help="write the files and the ledger. Without it, nothing is written.")
    ap.add_argument("--allow-overwrite", action="store_true",
                    help="permit changing a field upstream already filled in")
    args = ap.parse_args()

    plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    approved = (plan.get("approved") or "").strip()
    if not approved:
        print("edit_upstream: the plan has no `approved`. D15 permits these edits "
              "ONLY after asking the owner; the ledger records their words, so a "
              "plan without them cannot be applied.", file=sys.stderr)
        return 2

    ledger = {"edits": []}
    if LEDGER.exists():
        ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    seq = max([e.get("seq", 0) for e in ledger.get("edits", [])] or [0])

    total_applied, total_refused, entries = 0, 0, []
    for spec in plan["edits"]:
        rel = spec["file"]
        path = ROOT / rel
        top = Path(rel).parts[0] if Path(rel).parts else ""
        print("=" * 78)
        print(rel)
        if top == "raw":
            print("  REFUSED: raw/ holds publisher PDFs and their sha256 is the chain "
                  "`make verify` checks. Not editable, D15 or not.")
            total_refused += 1
            continue
        if top not in EDITABLE:
            print(f"  REFUSED: {top!r} is not one of {EDITABLE} (D15's scope).")
            total_refused += 1
            continue
        # `add_from` is the one op whose target is SUPPOSED to be absent.
        if not path.is_file() and not spec.get("add_from"):
            print("  REFUSED: no such file.")
            total_refused += 1
            continue

        # ---- adding a WHOLE FILE (a regenerated review, a new roster) --------
        # Distinct from a field edit and kept distinct: there is no frontmatter to
        # parse, the whole point is that the file does not exist yet, and refusing
        # to overwrite by default matters more here than anywhere -- silently
        # replacing outputs/<date>_literature_review.md would destroy the taxonomy
        # of record with no diff to read.
        if spec.get("add_from"):
            srcp = ROOT / spec["add_from"]
            if not srcp.is_file():
                print(f"  REFUSED: add_from {spec['add_from']!r} does not exist.")
                total_refused += 1
                continue
            if path.exists() and not args.allow_overwrite:
                print(f"  REFUSED: {rel} already exists. Replacing an upstream file "
                      f"wholesale needs --allow-overwrite and a separate ask.")
                total_refused += 1
                continue
            body = srcp.read_bytes()
            print(f"  + NEW FILE from {spec['add_from']}  "
                  f"({len(body) / 1024:.0f} KB, {body.count(b(10))} lines)")
            total_applied += 1
            if args.apply:
                before_sha = sha256_of(path) if path.exists() else None
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(body)
                seq += 1
                entries.append({
                    "seq": seq, "date": date.today().isoformat(), "file": rel,
                    "keys": ["<whole file>"],
                    "before": {"<whole file>": before_sha},
                    "after": {"<whole file>": spec["add_from"]},
                    "reason": spec.get("reason"), "evidence": spec.get("evidence"),
                    "approved": approved,
                    "sha256_before": before_sha, "sha256_after": sha256_of(path),
                })
            continue

        try:
            old, newline = read_preserving(path)
        except (ValueError, UnicodeDecodeError) as exc:
            print(f"  REFUSED: {exc}")
            total_refused += 1
            continue
        new, applied, refused = apply_one(
            old, spec.get("set") or {}, spec.get("set_list") or {},
            args.allow_overwrite)
        for r in refused:
            print(f"  REFUSED: {r}")
            total_refused += 1
        if not applied:
            if not refused:
                print("  nothing to do (already as requested)")
            continue

        diff = list(difflib.unified_diff(
            old.splitlines(keepends=True), new.splitlines(keepends=True),
            fromfile=rel + "  (upstream)", tofile=rel + "  (proposed)", n=3))
        sys.stdout.writelines(diff)
        print(f"  ({'CRLF' if newline == chr(13) + chr(10) else 'LF'} line endings, "
              f"preserved)")
        for key, before, after in applied:
            n = len(after) if isinstance(after, list) else 1
            print(f"  + {key}: {'%d entries' % n if isinstance(after, list) else after!r}"
                  f"   (was {before!r})")
        total_applied += len(applied)

        if args.apply:
            before_sha = sha256_of(path)
            write_preserving(path, new, newline)
            seq += 1
            entries.append({
                "seq": seq,
                "date": date.today().isoformat(),
                "file": rel,
                "keys": [k for k, _, _ in applied],
                "before": {k: b for k, b, _ in applied},
                "after": {k: a for k, _, a in applied},
                "reason": spec.get("reason"),
                "evidence": spec.get("evidence"),
                "approved": approved,
                "sha256_before": before_sha,
                "sha256_after": sha256_of(path),
            })

    print("=" * 78)
    if args.apply and entries:
        ledger.setdefault("_about", [
            "Every edit this project has made to the copied KBase area (D15).",
            "",
            "This is the file that makes an upstream edit ATTRIBUTABLE. manifest.json",
            "can see that a sidecar's bytes moved; only this can say the move was ours",
            "-- without it, an edit made here and a sidecar re-exported from the laptop",
            "look identical to the build.",
            "",
            "`sha256_after` is the sidecar's hash as we left it. build.py compares the",
            "file against it on every run and shouts in two directions: a sidecar that",
            "changed with no entry here, and an entry here whose file no longer matches.",
            "",
            "Append-only by hand. Written by scripts/edit_upstream.py, which refuses to",
            "run without the owner's approval recorded in the plan's `approved` field,",
            "because D15's condition was 'always ask if you modify'.",
        ])
        ledger["edits"] = ledger.get("edits", []) + entries
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
        print(f"edit_upstream: APPLIED {total_applied} field(s) across "
              f"{len(entries)} file(s) · {total_refused} refused")
        print(f"edit_upstream: recorded in {LEDGER.relative_to(ROOT)} "
              f"(seq {entries[0]['seq']}–{entries[-1]['seq']})")
        print("edit_upstream: run `make build` next, then `git diff -- meta/` to read "
              "exactly what changed upstream.")
    elif args.apply:
        # --apply was given and nothing came of it. Saying "DRY RUN" here was
        # actively misleading: it read as "we did not try", when the truth is
        # "we tried and every edit was refused or already in place".
        print(f"edit_upstream: NOTHING APPLIED · {total_refused} refused, "
              f"{len(plan['edits']) - total_refused} already as requested")
    else:
        print(f"edit_upstream: DRY RUN · {total_applied} field(s) would change across "
              f"{len(plan['edits'])} file(s) · {total_refused} refused")
        print("edit_upstream: nothing was written. Re-run with --apply once the owner "
              "has seen this diff and said yes.")
    return 1 if total_refused else 0


if __name__ == "__main__":
    sys.exit(main())
