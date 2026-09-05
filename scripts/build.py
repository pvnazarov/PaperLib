#!/usr/bin/env python3
"""meta/ + the newest literature review  ->  data/library.json + data/manifest.json

CLAUDE.md §6 is the specification for everything here; §4 is the contract this
implements. Read those before changing a regex.

STANDARD LIBRARY ONLY, deliberately: a fresh clone must be able to produce
library.json before numpy exists (README "Environment").

Deterministic: same inputs -> byte-identical outputs, with NO exception. There is
deliberately no wall-clock timestamp in either output file. Both carry
`data_as_of`, derived from the inputs (the newest review's date and the newest
sidecar `processed:` date), because:

  - it makes an unchanged rebuild a no-op for git, so a dirty tree means the data
    really moved rather than that somebody ran make;
  - it is the number a reader actually wants. "Rebuilt 03:14 today" says nothing
    about staleness if the last copy was in March; "data as of 2026-08-06" does
    (§4.2 obligation 2).

The wall clock belongs to the render step and to reports/, not to the contract.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

# PAPERLIB: ROOT is an AREA, not the project. Upstream this was
# `Path(__file__).parent.parent` — the one assumption that made the toolkit
# single-collection. scripts/paperlib.py resolves it from PAPERLIB_AREA (or the
# only area, when there is only one) and everything below is unchanged, so an
# area directory has exactly the shape the toolkit's root had.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

ROOT = paperlib.resolve_root()
AREA = paperlib.current_area_name(ROOT)
META, RAW, OUTPUTS, DATA, REPORTS = (
    ROOT / "meta", ROOT / "raw", ROOT / "outputs", ROOT / "data", ROOT / "reports"
)
GROUP = ROOT / "wiki" / "group.md"
ANNOT = ROOT / "annotations" / "topics.json"
ANNOT_BIB = ROOT / "annotations" / "bibliography.json"
EDIT_LEDGER = ROOT / "annotations" / "upstream_edits.json"
PROJECT = ROOT / "project.json"

# ------------------------------------------------------------------ project --
# What this INSTANCE calls itself, as opposed to what the TOOL is. Pointing the
# toolkit at a different field is then a data edit (project.json) rather than a
# hunt through six scripts and a template for the string "TeamLibrary" --
# RETARGETING.md is the runbook and this is the one file it says to edit.
#
# Defaults are deliberately generic and deliberately NOT "TeamLibrary": a clone
# with no project.json should look unnamed, not look like somebody else's
# library. Everything here is presentation; nothing here changes a record.
PROJECT_DEFAULTS = {
    "name": "Library",
    "tagline": "a reading list and its own papers",
    "subtitle": "",
    "footer_scope": "this library",
    "upstream_noun": "the source collection",
    "contact_name": "",
    "contact_email": "",
    "uplink_label": "",
    "uplink_href": "/",
    "site_dir": "library",
    "user_agent": "LibraryBrowser/0.1 (internal research tool)",
}


def load_project(path: Path | None = None) -> dict:
    """project.json over PROJECT_DEFAULTS. Keys beginning `_` are comments."""
    cfg = dict(PROJECT_DEFAULTS)
    # PAPERLIB: three layers. paperlib.json carries what every area shares (the
    # user_agent sent to Crossref, the contact); the area's project.json carries
    # what makes it that area. Shared-in-one-place means a corrected contact
    # address does not have to be found in five files.
    cfg.update(paperlib.load_config())
    path = path or PROJECT
    if path.exists():
        raw = json.loads(path.read_text(encoding="utf-8"))
        cfg.update({k: v for k, v in raw.items() if not k.startswith("_")})
    return cfg

PROJECT_CFG = load_project()

# The two non-literature sidecars are excluded by TYPE, never by filename (§12).
NON_LITERATURE_TYPES = {"other", "synthesis"}

# The exact label the review uses. Reproduced verbatim rather than paraphrased:
# it is a content requirement (§9), so drift here is a defect.
FILENAME_TITLE_LABEL = "title from the filename; no registered record exists to check it against"


# --------------------------------------------------------------------------- #
# sidecars
# --------------------------------------------------------------------------- #

# NOT a split on '---'. The frontmatter block itself contains comment rules
# like `# --- identity ------`, and splitting yields an empty parse for all 236
# files while reporting success (§12, first pitfall).
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)

SCALAR_KEYS = (
    "id id_basis source sha256 size_bytes media processed processor status "
    "type classification classification_basis doi year provenance "
    "duplicate_of duplicate_of_area title venue topic "
    "area"
).split()

# `authors` moved out of SCALAR_KEYS on 2026-09-03. It had been sitting in that
# list since the first build and could never have worked: the scalar reader takes
# whatever follows the colon on the SAME line, so a YAML block sequence yields an
# empty value and is dropped, and an inline flow list yields the literal string
# `["A", "B"]`. Nothing noticed because no sidecar carried the field -- upstream
# leaves it empty on all 340 (§3). D15 lets us write it, so it has to parse.
LIST_KEYS = ("authors", "also_in_areas")
FLOW_LIST = re.compile(r"^\[(?P<body>.*)\]$", re.S)

# `- **Reka Toth**, 2025-01-16 07:19 — [link](https://...)`
# The time is optional; the em dash and link are not always present in the same
# shape, so only the name and date are required to match.
PROV_BULLET = re.compile(
    r"^- \*\*(?P<name>[^*]+)\*\*,\s*(?P<date>\d{4}-\d{2}-\d{2})(?:\s+(?P<time>\d{2}:\d{2}))?"
    r"(?:\s*[—-]\s*(?P<rest>.*))?$",
    re.M,
)
PROV_LINK = re.compile(r"\[link\]\((?P<url>[^)]+)\)")
PROV_JOIN_COMMENT = re.compile(r"<!--\s*join:\s*(?P<join>.*?)\s*-->")

# frontmatter grammar: "... ; matched to the message by <join>" / "... NOT traceable ..."
PROV_JOIN_FM = re.compile(r";\s*matched[^;]*?\bby\s+(?P<join>.+?)\s*$", re.S)


def parse_frontmatter(text: str) -> dict:
    mo = FRONTMATTER.match(text)
    if not mo:
        return {}
    head = mo.group(1)
    out = {}
    for key in SCALAR_KEYS:
        km = re.search(rf"^{re.escape(key)}:[ \t]*(.*)$", head, re.M)
        if km:
            val = km.group(1).strip()
            # strip one layer of matching quotes; YAML in this base uses both
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            if val:
                out[key] = val
    for key in LIST_KEYS:
        items = _fm_list(head, key)
        if items:
            out[key] = items
    # nested block we care about: extraction.chars
    em = re.search(r"^extraction:\n(?:[ \t]+.*\n)*", head + "\n", re.M)
    if em:
        cm = re.search(r"^[ \t]+chars:[ \t]*(\d+)", em.group(0), re.M)
        if cm:
            out["extraction_chars"] = int(cm.group(1))
    return out


def _unquote(v: str) -> str:
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


def _fm_list(head: str, key: str) -> list[str]:
    """A frontmatter list, in either YAML shape a hand or a tool might write.

    Both are accepted because both are valid YAML and this field is now written
    by `scripts/edit_upstream.py` AND potentially by KBase later; refusing one
    shape would turn a formatting choice upstream into missing data here.

        authors:              authors: ["A. One", "B. Two"]
          - "A. One"
          - "B. Two"
    """
    m = re.search(rf"^{re.escape(key)}:[ \t]*(?P<inline>.*)\n(?P<block>(?:[ \t]+-[ \t]*.*\n)*)",
                  head + "\n", re.M)
    if not m:
        return []
    inline = m.group("inline").strip()
    if inline:
        fm = FLOW_LIST.match(inline)
        if not fm:
            return []                      # a scalar where a list belongs
        parts, buf, q = [], "", None       # split on commas OUTSIDE quotes
        for ch in fm.group("body"):
            if q:
                if ch == q:
                    q = None
                buf += ch
            elif ch in "\"'":
                q = ch
                buf += ch
            elif ch == ",":
                parts.append(buf)
                buf = ""
            else:
                buf += ch
        parts.append(buf)
        return [x for x in (_unquote(p) for p in parts) if x]
    out = []
    for line in m.group("block").splitlines():
        im = re.match(r"^[ \t]+-[ \t]*(.*)$", line)
        if im:
            v = _unquote(im.group(1))
            if v:
                out.append(v)
    return out


def body_sections(text: str) -> dict:
    """Split the markdown body into its `## Heading` sections."""
    mo = FRONTMATTER.match(text)
    body = text[mo.end():] if mo else text
    out = {}
    for m in re.finditer(r"^## (?P<h>.+?)[ \t]*\n(?P<b>.*?)(?=^## |\Z)", body, re.S | re.M):
        out[m.group("h").strip()] = m.group("b").strip()
    return out


def parse_key_points(block: str) -> list[str]:
    return [
        re.sub(r"\s+", " ", m.group(1)).strip()
        for m in re.finditer(r"^[-*]\s+(.*(?:\n(?![-*]|\s*$).*)*)", block, re.M)
    ]


def parse_provenance(fm: dict, sections: dict) -> dict:
    """Provenance parses two ways and both are needed (§6.1).

    The body gives one bullet per sharing event -- a paper shared twice has two
    colleagues and two dates. The frontmatter gives the join strength.
    """
    one_liner = fm.get("provenance", "")
    traceable = "not traceable" not in one_liner.lower()

    join = None
    if traceable:
        jm = PROV_JOIN_FM.search(one_liner)
        if jm:
            join = re.sub(r"\s+", " ", jm.group("join")).strip().rstrip(".")

    events = []
    block = sections.get("Provenance", "")
    for m in PROV_BULLET.finditer(block):
        rest = m.group("rest") or ""
        lm = PROV_LINK.search(rest)
        # the join note is an HTML comment on the line AFTER the bullet
        tail = block[m.end():m.end() + 400]
        cm = PROV_JOIN_COMMENT.search(tail.split("\n- ")[0])
        events.append({
            "who": m.group("name").strip(),
            "date": m.group("date"),
            "time": m.group("time"),
            "url": lm.group("url") if lm else None,
            "join_note": re.sub(r"\s+", " ", cm.group("join")).strip() if cm else None,
        })
    events.sort(key=lambda e: (e["date"], e["time"] or "", e["who"]))
    return {
        "one_liner": one_liner,
        "traceable": traceable,
        "join": join,
        "events": events,
        "sharers": sorted({e["who"] for e in events}),
    }


# --------------------------------------------------------------------------- #
# local topic annotation -- a stopgap the review always overrides (§6.6)
# --------------------------------------------------------------------------- #
#
# D1 puts the taxonomy upstream and §4.3 forbids guessing a topic. The owner
# instructed otherwise on 2026-09-03 ("do annotation of the topics yourself"),
# because 104 papers with no topic made a third of the library unnavigable and
# the next review regeneration has no date.
#
# So the annotation exists, and three properties stop it becoming a second
# taxonomy:
#
#   1. THE REVIEW WINS, ALWAYS. An assignment applies only where there is no
#      review entry. A regenerated review makes every line of the file inert on
#      the next build -- nothing to delete, and no way for it to contradict
#      upstream.
#   2. IT IS LABELLED. `topic_source` is "review" or "curated", the page badges
#      the difference, and the counts are reported separately. §9's register is
#      that the page says what is known AND how; this is the how.
#   3. NOTHING UPSTREAM IS TOUCHED. It lives in annotations/, which this project
#      owns, and §2 still holds for raw/ meta/ outputs/ wiki/.


def load_annotations(path: Path, problems: list) -> dict:
    if not path.exists():
        return {"parts": [], "topics": [], "assignments": {}}
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        problems.append(f"{path.name}: not valid JSON ({e}) -- no local topics applied")
        return {"parts": [], "topics": [], "assignments": {}}
    known = {t["name"] for t in doc.get("topics", [])}
    return {
        "parts": doc.get("parts", []),
        "topics": doc.get("topics", []),
        "assignments": doc.get("assignments", {}),
        "declared": known,
    }


# The same three properties as load_annotations above, applied to the BIBLIOGRAPHY
# instead of the taxonomy: upstream always wins, it is labelled, and nothing
# upstream is touched. See annotations/bibliography.json's own `_about` block.
#
# Keyed by sha256, not by filename, for two reasons that both bit elsewhere in this
# project: a byline is a fact about THESE BYTES, and the key has to survive an
# upstream rename. `source` is carried anyway, and CHECKED -- an entry whose
# filename has drifted is reported rather than quietly still applying.


def load_bib_annotations(path: Path, problems: list) -> dict:
    if not path.exists():
        return {}
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        problems.append(
            f"{path.name}: not valid JSON ({e}) -- no local bibliography applied"
        )
        return {}
    entries = doc.get("entries") or {}
    for sha, e in entries.items():
        if not isinstance(e, dict) or not e.get("source"):
            problems.append(f"{path.name}: entry {sha[:12]} has no `source`")
        au = e.get("authors")
        if au is not None and (not isinstance(au, list) or not all(au)):
            problems.append(
                f"{path.name}: {e.get('source', sha[:12])!r} has an `authors` value "
                f"that is not a non-empty list of names -- D2 forbids a partial list, "
                f"so it is ignored"
            )
            e.pop("authors", None)
    return entries


# D15 (owner, 2026-09-03): `meta/`, `outputs/` and `wiki/` MAY be edited here,
# after asking every time. `raw/` still may not. That retires §2's blanket ban
# and replaces it with something that has to be built rather than promised:
#
#   every edit is RECORDED, ATTRIBUTABLE and REVERSIBLE.
#
# Three mechanisms together, and none of them works alone:
#
#   1. `meta/` is tracked in git, so an edit has a real reversible diff.
#   2. manifest.json carries each SIDECAR'S OWN sha256, so a change to one is
#      visible at all. It was not before -- the manifest recorded the hash of the
#      PDF *as declared by* the sidecar, so adding a field to a sidecar was
#      invisible to the build. .gitignore even claimed otherwise.
#   3. this ledger says which changes were OURS. Without it, mechanism 2 can only
#      say "something moved", and a re-exported sidecar from the laptop would be
#      indistinguishable from an edit made here.
#
# The ledger records the sidecar's sha256 AFTER each edit, so "is this file as we
# left it" is one comparison rather than a re-parse and a guess.


def load_edit_ledger(path: Path, problems: list) -> dict:
    """-> {relative path: the most recent edit we recorded for it}."""
    if not path.exists():
        return {}
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        problems.append(
            f"{path.name}: not valid JSON ({e}) -- EVERY upstream edit now reads as "
            f"unexplained, which is the safe direction to fail but needs fixing"
        )
        return {}
    latest: dict = {}
    for e in doc.get("edits", []):
        f = e.get("file")
        # A recorded REMOVAL has no `sha256_after` because there is no file left to
        # hash, and that is the correct shape for it -- not a malformed entry. The
        # add-only rule means these are rare and each one carries its reason; they
        # are skipped here because this map answers "which CURRENT file carries an
        # edit made in this project", and a removed file carries nothing.
        if e.get("removed"):
            continue
        if not f or not e.get("sha256_after"):
            problems.append(f"{path.name}: an edit entry has no `file`/`sha256_after`")
            continue
        prev = latest.get(f)
        if prev is None or e.get("seq", 0) >= prev.get("seq", 0):
            latest[f] = e
    return latest


def merge_bib_annotations(records: list, entries: dict, problems: list) -> dict:
    """Fold PDF-read DOIs and bylines in, only where upstream has nothing.

    Every branch here is `if not already known`, which is what makes a later
    upstream fix silently retire a line in the file rather than fight it. Where
    both sources exist the REGISTRATION wins and a disagreement is REPORTED --
    the annotation then earns its keep as an independent cross-check (§2.2).
    """
    by_sha = {r["sha256"]: r for r in records}
    st = {"doi": 0, "authors": 0, "agree": 0, "disagree": 0,
          "redundant_doi": 0, "redundant_authors": 0, "orphan": 0}

    for sha, e in sorted(entries.items()):
        rec = by_sha.get(sha)
        if rec is None:
            st["orphan"] += 1
            problems.append(
                f"annotations/bibliography.json: sha256 {sha[:12]}… "
                f"({e.get('source', '?')!r}) matches no paper -- stale entry, or the "
                f"file it describes is no longer in the corpus"
            )
            continue
        if e.get("source") and e["source"] != rec["source"]:
            problems.append(
                f"annotations/bibliography.json: entry {sha[:12]}… names "
                f"{e['source']!r} but that sha256 is {rec['source']!r} -- the "
                f"annotation still applies (the hash is the key), but one of the two "
                f"names is stale"
            )

        # ---- DOI: only where the sidecar has none ----
        if e.get("doi"):
            if rec.get("doi"):
                st["redundant_doi"] += 1
                if normdoi(rec["doi"]) != normdoi(e["doi"]):
                    problems.append(
                        f"DOI disagreement for {rec['source']}: sidecar "
                        f"{rec['doi']!r} vs the DOI printed in the PDF {e['doi']!r}"
                    )
            else:
                rec["doi"] = e["doi"]
                rec["doi_source"] = "pdf"
                st["doi"] += 1

        # ---- authors: only where the registration has none ----
        if e.get("authors"):
            if rec.get("authors"):
                st["redundant_authors"] += 1
                if _same_byline(rec["authors"], e["authors"]):
                    st["agree"] += 1
                else:
                    st["disagree"] += 1
                    problems.append(
                        f"byline disagreement for {rec['source']}: the registration "
                        f"({rec.get('authors_source')}) lists {len(rec['authors'])} "
                        f"author(s), the PDF's printed byline {len(e['authors'])} -- "
                        f"registration kept; first differing surname "
                        f"{_first_diff(rec['authors'], e['authors'])!r}"
                    )
            else:
                rec["authors"] = list(e["authors"])
                rec["authors_source"] = "pdf-byline"
                if not rec.get("first_author"):
                    rec["first_author"] = e["authors"][0]
                st["authors"] += 1

    return st


def _surnames(names: list) -> list:
    """Last name token, with every kind of hyphen turned into a space FIRST.

    Not cosmetic: Crossref deposits `Dalla‐Torre` with U+2010 while the PDF prints
    an ASCII hyphen, and `fold()` keeps `-` but not U+2010 -- so without this the
    two forms tokenise differently and the cross-check reports a disagreement that
    does not exist. The same pair (`Pires‐Afonso`) already produced a false hit in
    an earlier audit of this corpus.
    """
    out = []
    for n in names:
        flat = re.sub(r"[-\u2010\u2011\u2012\u2013\u2014]", " ", n)
        toks = name_tokens(flat)
        out.append(toks[-1] if toks else "")
    return out


def _same_byline(a: list, b: list) -> bool:
    return _surnames(a) == _surnames(b)


def _first_diff(a: list, b: list) -> str | None:
    sa, sb = _surnames(a), _surnames(b)
    for i in range(max(len(sa), len(sb))):
        x = sa[i] if i < len(sa) else None
        y = sb[i] if i < len(sb) else None
        if x != y:
            return f"{x} vs {y}"
    return None


def merge_annotated_taxonomy(taxonomy: list, annot: dict, records: list,
                             problems: list) -> dict:
    """Fold curated topics into the taxonomy so the page can browse them.

    A curated topic that no paper ended up in is dropped rather than rendered as
    an empty row, and an assignment naming a topic that is neither in the review
    nor declared in the annotation file is a PROBLEM -- a typo there would
    otherwise create a phantom topic of one paper.
    """
    by_letter = {p["letter"]: p for p in taxonomy}
    review_topics = {t["name"] for p in taxonomy for t in p["topics"]}
    declared = annot.get("declared", set())

    used: dict[str, int] = {}
    for r in records:
        if r.get("topic_source") == "curated":
            used[r["topic"]] = used.get(r["topic"], 0) + 1

    for name in sorted(used):
        if name not in review_topics and name not in declared:
            problems.append(
                f"annotations/topics.json assigns {used[name]} paper(s) to "
                f"{name!r}, which is neither a review topic nor declared in the "
                f"file's own `topics` list"
            )

    # new parts first, so a new topic can be hung on one
    new_parts = 0
    for part in annot["parts"]:
        if part["letter"] in by_letter:
            continue
        entry = {"letter": part["letter"], "name": part["name"],
                 "description": part.get("description"), "curated": True,
                 "topics": []}
        taxonomy.append(entry)
        by_letter[part["letter"]] = entry
        new_parts += 1

    added = 0
    for topic in annot["topics"]:
        if topic["name"] in review_topics or topic["name"] not in used:
            continue
        part = by_letter.get(topic["part"])
        if part is None:
            problems.append(f"annotations/topics.json: topic {topic['name']!r} "
                            f"names part {topic['part']!r}, which does not exist")
            continue
        part["topics"].append({
            "name": topic["name"], "description": topic.get("description"),
            "count": used[topic["name"]], "curated": True,
        })
        added += 1

    # every topic's count has to include the curated papers, review topics too
    for part in taxonomy:
        for t in part["topics"]:
            if not t.get("curated"):
                t["count"] = t.get("count", 0) + used.get(t["name"], 0)

    # An empty part would render as a colour in the key with nothing under it.
    taxonomy[:] = [p for p in taxonomy if p["topics"]]

    # BACKFILL part_letter/part onto the curated records. Setting `topic` alone
    # left them with no part, which is not cosmetic: the Topic facet's per-part
    # counts read 0, and partColour() fell through to its grey fallback, so all
    # 104 would have been grey dots on a map whose entire colour scheme is parts.
    where = {t["name"]: (part["letter"], part["name"])
             for part in taxonomy for t in part["topics"]}
    orphan = []
    for r in records:
        if r.get("topic_source") == "curated":
            hit = where.get(r["topic"])
            if hit:
                r["part_letter"], r["part"] = hit
            else:
                orphan.append(r["source"])
    if orphan:
        problems.append(
            f"{len(orphan)} curated paper(s) have a topic that is in no part, so "
            f"they would be uncoloured on the map; first: {orphan[0]}"
        )

    return {"assigned": sum(used.values()), "new_topics": added,
            "new_parts": new_parts,
            "into_existing": sum(n for k, n in used.items() if k in review_topics)}

# --------------------------------------------------------------------------- #
# one person, one name (§6.4)
# --------------------------------------------------------------------------- #
#
# Author strings come from Crossref verbatim, and Crossref is not consistent
# about a given person. Measured 2026-09-03, before this ran:
#
#     Petr Nazarov      6 strings  'Petr V. Nazarov'x29, 'Petr V Nazarov'x8,
#                                  'P. Nazarov', 'Petr Nazarov', 'P. V. Nazarov',
#                                  and one with a NON-BREAKING SPACE
#     Maryna Chepeleva  4 strings  incl. 'Marina Chepeleva' and 'M. Chepeleva'
#     Oliver Hunewald   2 strings
#
# The Author facet lists these strings, so it was splitting one person across six
# rows and reporting 29 papers for someone with 41 -- a confident wrong count, of
# exactly the kind this project treats as a defect everywhere else.
#
# THE FIX IS NARROW ON PURPOSE. app.js's reasoning stands: 93 papers here carry an
# author surnamed Wang and they are not one person, so surnames are never merged
# in general. What is merged is only this: a ROSTER member's surname, and only
# when EVERY string ending in it is compatible with that member's given name --
# equal to it, or an initial of it. `Jeff Zhang` is not compatible with Lu Zhang,
# so `zhang` is left alone, all 83 of them. For everyone not on the roster there
# is no authoritative full name to canonicalise towards, so nothing is touched.
#
# The surviving form is the corpus's own most frequent one, not the roster's
# spelling: `Petr V. Nazarov` (29 uses) says more than `Petr Nazarov` and is what
# the publishers actually registered.

# Corrections to third-party name strings that the OWNER has confirmed. Needed
# because a misspelling cannot be told from a different person by measurement --
# it takes someone who knows. Each entry records who said so and when.
CONFIRMED_NAME_FIXES = {
    # owner, 2026-09-03: "Maryna CHEPELEVA is the correct name. Marina is a
    # misspelling." Until this was settled the build declined to decide, which
    # also cost her the initial-only match on Rinaldetti(2026) -- a second given
    # name made the surname look ambiguous.
    ("chepeleva", "marina"): "Maryna Chepeleva",
}

# Crossref deposits U+00A0 and other exotic spaces. Normalising them is not a
# judgement about anybody's name and applies to every author.
BSLASH = chr(92)
QUOTE = chr(34)
WS = re.compile(r"[\s\u00a0\u2007\u202f]+")


def canonical_authors(records: list, members: list, problems: list) -> dict:
    """Rewrite author strings in place so one person reads as one name."""
    stats = {"ws": 0, "confirmed": 0, "merged": 0, "people": [], "declined": []}

    # pass 1 -- whitespace, then the owner's confirmed corrections
    for r in records:
        out = []
        for a in r.get("authors") or []:
            fixed = WS.sub(" ", a).strip()
            if fixed != a:
                stats["ws"] += 1
            tok = name_tokens(fixed)
            if len(tok) >= 2:
                key = (" ".join(tok[1:]), tok[0])
                alt = CONFIRMED_NAME_FIXES.get(key) or CONFIRMED_NAME_FIXES.get((tok[-1], tok[0]))
                if alt and alt != fixed:
                    fixed = alt
                    stats["confirmed"] += 1
            out.append(fixed)
        if r.get("authors"):
            r["authors"] = out

    if not members:
        return stats

    # pass 2 -- per roster member, all-or-nothing
    for mem in members:
        surname = mem["surname"]
        n = len(surname)
        seen: dict[str, int] = {}
        for r in records:
            for a in r.get("authors") or []:
                tok = name_tokens(a)
                if len(tok) > n and tok[-n:] == surname:
                    seen[a] = seen.get(a, 0) + 1
        if len(seen) < 2:
            continue

        def compatible(a: str) -> bool:
            first = name_tokens(a)[0]
            return any(first == g or (len(first) == 1 and first == g[0])
                       for g in mem["given"])

        odd = sorted(a for a in seen if not compatible(a))
        if odd:
            # Someone else wears this surname. Merging would attribute their work
            # to a colleague, so the variants stay separate and this is reported.
            stats["declined"].append((mem["name"], odd, sorted(seen)))
            continue

        # The corpus's own most frequent form -- but on a TIE, never an
        # abbreviated one. Frequency settles it in this corpus ('Petr V. Nazarov'
        # 29 times), yet with one use each a plain alphabetical tie-break picks
        # 'P. Nazarov' over 'Petr V. Nazarov', which throws away the name. So:
        # frequency, then the most non-initial name parts, then the longest,
        # then alphabetical to stay deterministic.
        def rank(a: str) -> tuple:
            tok = name_tokens(a)
            return (-seen[a], -sum(1 for x in tok if len(x) > 1), -len(a), a)

        keep = sorted(seen, key=rank)[0]
        changed = 0
        for r in records:
            if not r.get("authors"):
                continue
            r["authors"] = [keep if (a in seen and a != keep) else a for a in r["authors"]]
            changed += sum(1 for a in seen if a != keep)
        moved = sum(v for a, v in seen.items() if a != keep)
        if moved:
            stats["merged"] += moved
            stats["people"].append((keep, sorted(a for a in seen if a != keep), moved))
    return stats

# --------------------------------------------------------------------------- #
# circulation sentences: excluded from SEARCH, kept in the displayed prose
# --------------------------------------------------------------------------- #
#
# 150 of the summaries end with a sentence like "Circulated by P. Nazarov as an
# 'Arxiv paper from Curie group'". That sentence is about how the paper ARRIVED,
# not about what it says, and the owner's instruction (D5) is that who shared a
# paper does not matter.
#
# Left in the haystack it makes the search lie by conflating two different
# things: `nazarov` matched 83 papers, of which only 41 he co-wrote and 42 he
# merely forwarded. That is the same defect that once made `chepeleva` match 34
# papers, returning after the earlier fix removed the structured sharer list but
# not this prose.
#
# So the spans are computed here and the PAGE cuts them out of the text it
# searches -- while still displaying the summary whole, because the sentence is
# upstream's prose and this project does not rewrite it (§2).
#
# DELIBERATE DUPLICATION: embed.py carries the same two patterns for its own
# input. They are not shared because embed.py's copy is what ADR 0002's measured
# 14 -> 18 improvement rests on, and refactoring it to import from here would put
# that result at risk for no gain. The guard is that both scripts PRINT their
# count on every `make update` -- 150 papers here, 150 there -- so a drift shows
# up as two numbers that stopped agreeing.
CIRCULATION = re.compile(
    r"""\b(
        # `circulated`, NOT `circulat\w*`. The wider form also matched
        # `circulating` (11 uses, every one subject vocabulary: "circulating
        # tumour DNA", "circulating immune cells") and `circulation` (3, all
        # "return of spontaneous circulation" after cardiac arrest). Those 14
        # sentences are what their papers are ABOUT, and stripping them hurt
        # exactly the ctDNA and cardiac-arrest papers where the words carry the
        # most meaning. Measured 2026-09-03: no form other than `circulated`
        # is ever used for the sharing act in this corpus.
        circulated
      | forwarded
      | reshared
      | shared \s+ (?: by | twice | into | it | independently | in \s+ the )
      | (?: the \s+ )? (?: team \s+ )? thread
      | webex
    )\b""",
    re.I | re.X,
)
# Does not break on "P. Nazarov", "et al.", "Fig. 2" or a decimal.
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(‘“])")
ABBREV = re.compile(r"(?:\b[A-Z]|\bet\sal|\bvs|\bcf|\bFig|\bNo|\bDr|\bProf|\bapprox)\.$")


def sentence_spans(text: str) -> list[tuple[int, int]]:
    """[start, end) of every sentence, rejoining ones split at an initial."""
    if not text:
        return []
    spans, start = [], 0
    for mo in SENT_SPLIT.finditer(text):
        end = mo.start()
        if ABBREV.search(text[start:end].rstrip()):
            continue                      # "P." -- not a sentence end
        spans.append((start, end))
        start = mo.end()
    spans.append((start, len(text)))
    return [(a, b) for a, b in spans if b > a]


def circulation_spans(text: str) -> list[list[int]]:
    """Spans of `text` the page must not search. Empty for most papers."""
    return [[a, b] for a, b in sentence_spans(text) if CIRCULATION.search(text[a:b])]

# --------------------------------------------------------------------------- #
# the group roster: which papers are the team's OWN work (§6.4)
# --------------------------------------------------------------------------- #

# `01, PN, Petr NAZAROV, 50/50%, CDI` -- the surname is the ALL-CAPS run at the
# end, which is what makes "Sebastian ALLARD DOHM-HANSEN" parse into a two-token
# surname instead of a given name and a surname.
GROUP_ROW = re.compile(r"^\s*(?P<nn>\d+|xx)\s*,\s*(?P<ini>[A-Z]{2})\s*,\s*(?P<name>[^,]+?)\s*,")


def fold(s: str) -> str:
    """Accent- and case-insensitive comparison form. `Müller` and `Muller` are
    the same surname, and Crossref is not consistent about which it deposits."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z\- ]", " ", s.lower())


def name_tokens(s: str) -> list[str]:
    return [t for t in fold(s).split() if t]


def parse_group(path: Path) -> list[dict]:
    """wiki/group.md -> the roster, current and past members alike."""
    if not path.exists():
        return []
    members = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = GROUP_ROW.match(line)
        if not m:
            continue
        toks = m.group("name").split()
        i = len(toks)
        while i > 0 and toks[i - 1].isupper() and re.search(r"[A-Z]", toks[i - 1]):
            i -= 1
        if i == 0 or i == len(toks):     # all-caps or no-caps: no surname to find
            continue
        members.append({
            "initials": m.group("ini"),
            # display form: `Petr Nazarov`, not the roster's `Petr NAZAROV`
            "name": " ".join(toks[:i] + [t.title() for t in toks[i:]]),
            "given": name_tokens(" ".join(toks[:i])),
            "surname": name_tokens(" ".join(toks[i:])),
        })
    return members


def surname_owners(records: list) -> dict:
    """Every given name each surname is worn by, across all author lists here.

    This is what licenses a weak match. `Nazarov` belongs to exactly one person
    in this corpus, so `P. Nazarov` is that person; `Zhang` is worn by 80-odd
    people, so `L. Zhang` is a coin flip and must not be guessed at. Measured
    from the corpus rather than assumed, because the answer is a property of
    this library and not of the surname.
    """
    owners: dict[str, set[str]] = {}
    for r in records:
        for a in r.get("authors") or []:
            t = name_tokens(a)
            if len(t) >= 2:
                for surname in (t[-1], " ".join(t[1:])):
                    owners.setdefault(surname, set()).add(t[0])
    return owners


def match_author(author: str, mem: dict, distinctive: bool) -> str | None:
    """How strongly one author string identifies one member -- or not at all.

    `author` -> `given ... surname`, so the surname must be the TRAILING tokens.
    A given name that positively disagrees ("Jeff Zhang" vs Lu Zhang) is a
    different person and returns None: matching on a surname alone would put
    82 strangers' papers in the team's own list.
    """
    t = name_tokens(author)
    n = len(mem["surname"])
    if len(t) <= n or t[-n:] != mem["surname"]:
        return None
    first = t[0]
    for g in mem["given"]:
        if first == g:
            return "author"
        # An initial is only an identifier where the surname is one too.
        if len(first) == 1 and first == g[0]:
            return "author-initial" if distinctive else None
    return None


def annotate_ownership(records: list, members: list, problems: list) -> dict:
    """Mark each record `own` (a roster member is a co-author) or shared.

    Nothing is inferred from who CIRCULATED a paper (D5) and nothing from the
    sidecar's `provenance:` line, which was measured to over-claim -- see
    reports/upstream_findings.md. Co-authorship is the criterion, as asked.
    """
    stats = {
        "own": 0, "shared": 0, "by_basis": {}, "by_member": {},
        "near_misses": [], "unknowable": 0,
    }
    if not members:
        for r in records:
            r["own"] = None
            r["own_members"] = []
            r["own_basis"] = None
        return stats

    owners = surname_owners(records)
    distinct = {}
    for mem in members:
        key = " ".join(mem["surname"])
        others = {
            g for g in owners.get(key, ())
            if g not in mem["given"] and not (len(g) == 1 and any(g == x[0] for x in mem["given"]))
        }
        distinct[mem["initials"]] = not others
        mem["_others"] = sorted(others)

    for r in records:
        hits: dict[str, str] = {}
        for a in r.get("authors") or []:
            for mem in members:
                kind = match_author(a, mem, distinct[mem["initials"]])
                if kind and hits.get(mem["initials"]) != "author":
                    hits[mem["initials"]] = kind
                # A member's surname on a given name that is neither theirs nor
                # plainly someone else's -- `Marina Chepeleva` against a roster
                # that says Maryna. Reported for the owner to settle upstream,
                # never guessed at here.
                #
                # Only for a surname that is otherwise near-unique in this corpus.
                # For `Zhang`, `Kim` and `Müller` a different given name is simply
                # a different person, 55 times over, and reporting those would
                # bury the one case worth looking at.
                t = name_tokens(a)
                n = len(mem["surname"])
                if (not kind and len(mem["_others"]) <= 2 and len(t) > n
                        and t[-n:] == mem["surname"]
                        and len(t[0]) > 1 and t[0] not in mem["given"]):
                    stats["near_misses"].append((r["source"], a, mem["name"]))

        # Last resort, and only where there is no author list to consult at all:
        # the filename's first-author surname, accepted ONLY for a surname that
        # is distinctive here. Labelled, because a surname is not a person.
        if not hits and not r.get("authors"):
            fn = name_tokens(r["source"].split("(")[0])
            for mem in members:
                if fn and fn == mem["surname"] and distinct[mem["initials"]]:
                    hits[mem["initials"]] = "filename"
            if not hits:
                stats["unknowable"] += 1

        r["own"] = bool(hits)
        r["own_members"] = sorted(hits)
        r["own_basis"] = ("author" if "author" in hits.values() else
                          "author-initial" if "author-initial" in hits.values() else
                          "filename" if hits else None)
        if hits:
            stats["own"] += 1
            stats["by_basis"][r["own_basis"]] = stats["by_basis"].get(r["own_basis"], 0) + 1
            for ini in hits:
                stats["by_member"][ini] = stats["by_member"].get(ini, 0) + 1
        else:
            stats["shared"] += 1
    return stats

# --------------------------------------------------------------------------- #
# the literature review: taxonomy + bibliography (§6.2)
# --------------------------------------------------------------------------- #

REVIEW_GLOB = "*_literature_review.md"
PART_RE = re.compile(r"^# (?P<letter>[A-Z])\.[ \t]*(?P<name>.+?)[ \t]*$", re.M)
TOPIC_RE = re.compile(r"^## (?P<name>.+?)[ \t]*$", re.M)
ENTRY_RE = re.compile(r"^### (?P<head>.+?)[ \t]*$", re.M)
SRC_RE = re.compile(r"\[src\]\(<\.\./raw/(?P<src>.+?)>\)")

# `### Rosen, Y. et al. (2026). *Nature.* Universal cell embedding provides ...`
HEAD_RE = re.compile(
    r"^(?P<author>.+?)\s*\((?P<year>\d{4})\)\.\s*\*(?P<venue>.+?)\.?\*\s*(?P<title>.*?)\s*$"
)
# `[doi:10.x](https://doi.org/10.x) · `paper` · also in **Bioinformatics**`
META_DOI = re.compile(r"\[doi:(?P<doi>[^\]]+)\]")
META_ARXIV = re.compile(r"\[arXiv:(?P<arxiv>[^\]]+)\]")
META_TYPE = re.compile(r"`(?P<type>[a-z]+)`")
META_ALSO = re.compile(r"also in \*\*(?P<area>[^*]+)\*\*")
NO_ID = "*no DOI or arXiv ID*"


# The `## Contents` table declares every part and topic with its paper count. It is
# the review's own checksum on its taxonomy, and parsing it turns the body walk from
# a trusting parse into a CHECKED one -- the same discipline as the roster-sha guard
# in the upstream tl_review.py. It also excludes the epilogue (`## What this document
# does not say`, `## Sources`, `## Related`), which are `##` headings with no entries
# and would otherwise be absorbed into the last part as three phantom topics.
TOC_PART = re.compile(r"^\*\*(?P<letter>[A-Z])\.\s*(?P<name>.+?)\*\*\s*[—-]\s*(?P<n>\d+)\s+papers?", re.M)
TOC_TOPIC = re.compile(r"^\s*·\s*\[(?P<name>.+?)\]\(#[^)]*\)\s*\((?P<n>\d+)\)", re.M)


def norm_heading(s: str) -> str:
    """Compare headings without being defeated by quote style or whitespace."""
    s = unicodedata.normalize("NFKC", unescape_md(s))
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"\s+", " ", s).strip().lower()


def parse_contents(text: str) -> list[dict]:
    """-> [{letter, name, count, topics: [{name, count}]}] as DECLARED by the review."""
    toc_start = text.find("## Contents")
    first_part = PART_RE.search(text)
    if toc_start < 0 or not first_part:
        return []
    toc = text[toc_start:first_part.start()]
    parts, bounds = [], [(m.start(), m) for m in TOC_PART.finditer(toc)]
    for i, (pos, m) in enumerate(bounds):
        end = bounds[i + 1][0] if i + 1 < len(bounds) else len(toc)
        parts.append({
            "letter": m.group("letter"),
            "name": m.group("name").strip(),
            "count": int(m.group("n")),
            "topics": [
                {"name": unescape_md(tm.group("name").strip()), "count": int(tm.group("n"))}
                for tm in TOC_TOPIC.finditer(toc, pos, end)
            ],
        })
    return parts


def newest_review(outputs: Path) -> Path | None:
    """Newest by the DATE IN THE FILENAME, not by mtime.

    mtime is set by the copy, so every file that arrives looks equally new.
    """
    dated = []
    for p in sorted(outputs.glob(REVIEW_GLOB)):
        dm = re.match(r"(\d{4}-\d{2}-\d{2})_", p.name)
        if dm:
            dated.append((dm.group(1), p))
    return max(dated)[1] if dated else None


def parse_review(path: Path) -> tuple[dict, list, dict]:
    """-> (bib_by_source, parts, stats)

    Only the BODY is parsed -- everything from the first `# A. ` heading. The
    "How to read this" prose contains a sentence that reproduces the
    filename-title label, and counting it as an entry is how the "8 papers"
    miscount happens (§12).
    """
    text = path.read_text(encoding="utf-8")
    first_part = PART_RE.search(text)
    if not first_part:
        die(f"{path.name}: no `# A. ...` part heading found; not a review file?")
    body = text[first_part.start():]

    declared = parse_contents(text)
    if not declared:
        die(f"{path.name}: no parseable `## Contents` table. It is the taxonomy's "
            f"checksum (§6.2) and the build will not guess the tree without it.")
    declared_topics = {
        p["letter"]: {norm_heading(t["name"]) for t in p["topics"]} for p in declared
    }

    # Index part and topic boundaries so each entry can be attributed to both.
    parts = []
    for pm in PART_RE.finditer(body):
        letter = pm.group("letter")
        if letter not in declared_topics:
            continue  # a `# X. ` heading the Contents table does not declare
        parts.append({
            "letter": letter,
            "name": pm.group("name").strip(),
            "start": pm.start(),
            "topics": [],
        })
    for i, part in enumerate(parts):
        end = parts[i + 1]["start"] if i + 1 < len(parts) else len(body)
        part["end"] = end
        for tm in TOPIC_RE.finditer(body, part["start"], end):
            name = tm.group("name").strip()
            # Only headings the Contents table declares are topics. This is what
            # keeps the epilogue out of the tree.
            if norm_heading(name) not in declared_topics[part["letter"]]:
                continue
            part["topics"].append({"name": name, "start": tm.start(), "papers": []})
        for j, topic in enumerate(part["topics"]):
            if j + 1 < len(part["topics"]):
                topic["end"] = part["topics"][j + 1]["start"]
            else:
                # The LAST topic of a part must stop at the next `##` of any kind,
                # declared or not -- otherwise it swallows the epilogue's entries.
                nxt = TOPIC_RE.search(body, topic["start"] + 1, end)
                topic["end"] = nxt.start() if nxt else end
            # the italic lead paragraph: `*7 papers.* Large self-supervised models ...`
            head = body[topic["start"]:topic["end"]]
            dm = re.search(r"^\*\d+ papers?\.\*\s*(?P<d>.+?)(?=\n\n|\n### |\Z)", head, re.S | re.M)
            topic["description"] = re.sub(r"\s+", " ", dm.group("d")).strip() if dm else None

    def locate(pos: int) -> tuple[str, str, str]:
        for part in parts:
            if part["start"] <= pos < part["end"]:
                for topic in part["topics"]:
                    if topic["start"] <= pos < topic["end"]:
                        return part["letter"], part["name"], topic["name"]
                return part["letter"], part["name"], None
        return None, None, None

    entries = list(ENTRY_RE.finditer(body))
    bib, stats = {}, {"entries": 0, "filename_titles": 0, "no_id": 0, "dup_src": []}
    for i, em in enumerate(entries):
        block = body[em.start():entries[i + 1].start() if i + 1 < len(entries) else len(body)]
        sm = SRC_RE.search(block)
        if not sm:
            die(f"{path.name}: review entry with no [src] link:\n  {em.group('head')[:100]}")
        # The join key is the [src] filename, never a title or a position (§6.2).
        src = unescape_md(sm.group("src"))

        head = em.group("head")
        filename_title = FILENAME_TITLE_LABEL in head
        if filename_title:
            stats["filename_titles"] += 1
            head = re.sub(r"\s*\*\[" + re.escape(FILENAME_TITLE_LABEL) + r"\]\*\s*$", "", head)

        hm = HEAD_RE.match(head)
        if not hm:
            die(f"{path.name}: unparseable entry heading:\n  {head[:120]}")
        venue = clean_venue(hm.group("venue"))

        meta_line = block.split("\n")[1] if "\n" in block else ""
        doim, axm, tym = META_DOI.search(meta_line), META_ARXIV.search(meta_line), META_TYPE.search(meta_line)
        if NO_ID in meta_line:
            stats["no_id"] += 1

        # the abstract paragraph follows the [src] line
        after = block[sm.end():].strip()
        summary = re.sub(r"\s+", " ", after.split("\n\n")[0]).strip() if after else None

        letter, part_name, topic_name = locate(em.start())
        rec = {
            "review_title": unescape_md(hm.group("title").strip()),
            "title_from_filename": filename_title,
            "review_author": hm.group("author").strip(),
            "review_year": int(hm.group("year")),
            "venue": venue,
            "review_doi": doim.group("doi").strip() if doim else None,
            "arxiv": axm.group("arxiv").strip() if axm else None,
            "review_type": tym.group("type") if tym else None,
            "also_in": [m.group("area").strip() for m in META_ALSO.finditer(meta_line)],
            "part_letter": letter,
            "part": part_name,
            "topic": topic_name,
            "review_summary": summary,
        }
        if src in bib:
            stats["dup_src"].append(src)
        bib[src] = rec
        stats["entries"] += 1
        for part in parts:
            for topic in part["topics"]:
                if topic["name"] == topic_name and part["letter"] == letter:
                    topic["papers"].append(src)

    # ---- the checked parse: body must agree with the Contents table ----
    mismatches = []
    dmap = {p["letter"]: p for p in declared}
    if {p["letter"] for p in parts} != set(dmap):
        mismatches.append(
            f"parts declared {sorted(dmap)} but found {sorted(p['letter'] for p in parts)}"
        )
    for part in parts:
        dp = dmap[part["letter"]]
        if norm_heading(dp["name"]) != norm_heading(part["name"]):
            mismatches.append(
                f"part {part['letter']}: declared {dp['name']!r}, body {part['name']!r}"
            )
        got_total = sum(len(t["papers"]) for t in part["topics"])
        if got_total != dp["count"]:
            mismatches.append(
                f"part {part['letter']}: declared {dp['count']} papers, parsed {got_total}"
            )
        dtopics = {norm_heading(t["name"]): t["count"] for t in dp["topics"]}
        if len(part["topics"]) != len(dp["topics"]):
            mismatches.append(
                f"part {part['letter']}: declared {len(dp['topics'])} topics, "
                f"parsed {len(part['topics'])}"
            )
        for t in part["topics"]:
            want = dtopics.get(norm_heading(t["name"]))
            if want != len(t["papers"]):
                mismatches.append(
                    f"topic {t['name']!r}: declared {want}, parsed {len(t['papers'])}"
                )
    if mismatches:
        die(
            f"{path.name}: the body disagrees with its own `## Contents` table. The "
            f"taxonomy is not safe to trust; the review's format has probably changed.\n  "
            + "\n  ".join(mismatches)
        )
    stats["parts"] = len(parts)
    stats["topics"] = sum(len(p["topics"]) for p in parts)

    taxonomy = [
        {
            "letter": p["letter"],
            "name": p["name"],
            "topics": [
                {"name": t["name"], "description": t["description"], "count": len(t["papers"])}
                for t in p["topics"]
            ],
        }
        for p in parts
    ]
    return bib, taxonomy, stats


# The review puts the arXiv ID where the journal name goes -- `*arXiv:2506.03373.*`
# -- so arXiv arrives as 19 distinct one-paper "venues" instead of one venue with
# 19 papers. A venue facet built on that would show 19 useless singletons and hide
# the second-largest publisher in the corpus. The ID is not lost: it is already in
# the `arxiv` field, parsed from the same line.
ARXIV_VENUE = re.compile(r"^arxiv(?:[:\s].*)?$", re.I)


def clean_venue(venue: str) -> str | None:
    v = unescape_md(venue).strip()      # `Cell Death &amp; Disease` -> `Cell Death & Disease`
    if not v or v == "venue not recorded":
        return None
    if ARXIV_VENUE.match(v):
        return "arXiv"
    return v


def unescape_md(s: str) -> str:
    """The review escapes `&` as `&amp;` in headings (e.g. 'H&amp;E Images')."""
    return (s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))


# --------------------------------------------------------------------------- #
# assembly
# --------------------------------------------------------------------------- #

def die(msg: str) -> None:
    print(f"build: FATAL: {msg}", file=sys.stderr)
    sys.exit(1)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    argv = set(sys.argv[1:])
    verify_bytes = "--verify-bytes" in argv   # re-hash 2.1 GB; opt-in, see §P2 verify

    if not META.is_dir():
        die(f"{META} not found. One sidecar per source file lives there -- see "
            f"RETARGETING.md step 3, or CLAUDE.md §2 for how it is filled in this "
            f"instance.")

    review_path = newest_review(OUTPUTS)  # noqa: E501 - see data_as_of below
    if review_path is None:
        die(f"no {REVIEW_GLOB} in {OUTPUTS}. The taxonomy comes from it (D1, §4.3).")
    bib, taxonomy, rstats = parse_review(review_path)

    bib_cache = {}
    cache_path = DATA / "bib_cache.json"
    if cache_path.exists():
        bib_cache = json.loads(cache_path.read_text(encoding="utf-8")).get("by_sha256", {})

    records, non_lit, problems, all_fm = [], [], [], []
    annot = load_annotations(ANNOT, problems)
    annot_bib = load_bib_annotations(ANNOT_BIB, problems)
    edits = load_edit_ledger(EDIT_LEDGER, problems)
    for path in sorted(META.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        all_fm.append(fm)
        if not fm:
            problems.append(f"{path.name}: no parseable frontmatter")
            continue
        for required in ("id", "source", "sha256", "type"):
            if required not in fm:
                problems.append(f"{path.name}: missing `{required}:`")
        src = fm.get("source")
        if not src:
            continue

        sections = body_sections(text)
        rec = {
            "id": fm.get("id"),
            "source": src,
            "sha256": fm.get("sha256"),
            "size_bytes": int(fm["size_bytes"]) if fm.get("size_bytes", "").isdigit() else None,
            "media": fm.get("media"),
            "type": fm.get("type"),
            "classification": fm.get("classification"),
            "year": int(fm["year"]) if (fm.get("year") or "").isdigit() else None,
            "doi": fm.get("doi"),
            # Where the DOI came from, on the same honesty rule as `authors`
            # (§2.0.2): four of these were read off a PDF by this project and
            # written into the sidecar, and a label saying "the sidecar, as
            # upstream shipped it" for one of those would be false. Refined
            # below for the review fallback and by merge_bib_annotations.
            "doi_source": ("sidecar-written-here" if "doi" in (
                (edits.get(f"meta/{src}.md") or {}).get("keys") or [])
                else ("sidecar" if fm.get("doi") else None)),
            "duplicate_of_area": fm.get("duplicate_of_area"),
            # PAPERLIB: which collection this is, and which others hold the same
            # bytes. `area` is written by the ingest and is not the reader's to
            # change; a missing one means a sidecar written before areas existed.
            "area": fm.get("area") or AREA,
            "also_in_areas": fm.get("also_in_areas") or [],
            "extraction_chars": fm.get("extraction_chars"),
            "abstract": sections.get("Abstract"),
            "summary": sections.get("Summary"),
            "key_points": parse_key_points(sections.get("Key points", "")),
            "limitations": sections.get("Limitations"),
            "provenance": parse_provenance(fm, sections),
            # See "circulation sentences" above. Offsets, not a second copy of
            # the prose: 150 short arrays instead of 150 duplicated summaries.
            "hay_drop": circulation_spans(sections.get("Summary") or ""),
            # The SIDECAR'S OWN bytes, so an edit to it is visible at all (D15).
            # Set here rather than after the review join, because the two
            # non-literature sidecars `continue` past that point and an edit to
            # one of them is exactly as much of an event as an edit to a paper's.
            "sidecar_sha256": sha256_of(path),
        }

        if rec["type"] in NON_LITERATURE_TYPES:
            non_lit.append(rec)
            continue

        # ---- the review join, on the [src] filename (§6.2) ----
        r = bib.get(src)
        if r:
            # The review is the title of record (D1). The one exception is the
            # review's own filename fallback: where it says so in as many words
            # (FILENAME_TITLE_LABEL) and the sidecar carries a real title, the
            # sidecar wins -- a labelled non-answer should not outrank an answer.
            if r["title_from_filename"] and fm.get("title"):
                r_title, r_from_fn, r_tsrc = fm["title"], False, "sidecar"
            else:
                r_title = r["review_title"]
                r_from_fn = r["title_from_filename"]
                r_tsrc = "filename" if r_from_fn else "review"
            rec.update({
                "title": r_title,
                "title_from_filename": r_from_fn,
                "title_source": r_tsrc,
                "first_author": r["review_author"],
                "venue": r["venue"],
                "venue_source": "review" if r["venue"] else None,
                "arxiv": r["arxiv"],
                "part_letter": r["part_letter"],
                "part": r["part"],
                "topic": r["topic"],
                "topic_source": "review",
                "unfiled": False,
                "review_summary": r["review_summary"],
            })
            if r["review_doi"] and rec["doi"] and normdoi(r["review_doi"]) != normdoi(rec["doi"]):
                problems.append(
                    f"DOI disagreement for {src}: sidecar {rec['doi']!r} vs review "
                    f"{r['review_doi']!r}"
                )
            if not rec["doi"] and r["review_doi"]:
                rec["doi"], rec["doi_source"] = r["review_doi"], "review"
            if r["review_type"] and r["review_type"] != rec["type"]:
                problems.append(
                    f"type disagreement for {src}: sidecar {rec['type']!r} vs review "
                    f"{r['review_type']!r}"
                )
            if r["also_in"] and rec["duplicate_of_area"] not in r["also_in"]:
                problems.append(
                    f"also-in disagreement for {src}: sidecar "
                    f"{rec['duplicate_of_area']!r} vs review {r['also_in']!r}"
                )
        else:
            # Unfiled: no review entry yet. Transient, and the TOPIC is never guessed
            # at (§4.3) -- but the bibliography need not be missing too. The
            # publisher's registration is already in bib_cache.json, fetched by the
            # sidecar's own DOI, so a newly copied paper can carry a real title and
            # a real venue immediately instead of showing its filename until the
            # next review arrives. Only the topic actually requires the review.
            cached_now = bib_cache.get(rec["sha256"]) or {}
            fn_venue = venue_from_filename(src)
            reg_title = cached_now.get("registered_title")
            reg_authors = cached_now.get("authors")
            if fm.get("title"):
                # The sidecar's OWN `title:`. Preferred over the registration
                # because it is upstream's recorded value for this file, checked
                # against the DOI at ingest, and it is present offline -- so a
                # newly copied paper reads correctly with no network at all.
                title, from_fn, tsrc = fm["title"], False, "sidecar"
            elif reg_title:
                title, from_fn, tsrc = reg_title, False, cached_now.get("source")
            else:
                # Nothing registered: fall back to the filename, and SAY SO. The
                # page renders `title` directly, so an unlabelled fallback here is
                # exactly the failure §9 exists to prevent.
                title, from_fn, tsrc = title_from_filename(src), True, "filename"
            rec.update({
                "title": title,
                "title_from_filename": from_fn,
                "title_source": tsrc,
                "first_author": reg_authors[0] if reg_authors else None,
                "venue": cached_now.get("registered_venue") or fn_venue,
                "venue_source": ("crossref" if cached_now.get("registered_venue")
                                 else ("filename" if fn_venue else None)),
                "arxiv": None, "part_letter": None, "part": None,
                "topic": None, "topic_source": None,
                "unfiled": True, "review_summary": None,
            })
            # A local annotation fills the topic, and ONLY here -- a paper with
            # a review entry never reaches this branch, so the review can never
            # be overridden (§6.6).
            curated = annot["assignments"].get(src)
            if curated:
                rec["topic"] = curated
                rec["topic_source"] = "curated"
                rec["unfiled"] = False

        # ---- full author lists, from the cache only; never fabricated (D2) ----
        cached = bib_cache.get(rec["sha256"])
        rec["authors"] = (cached.get("authors") if cached else None) or None
        # Only where there IS a list. A cached record can exist with no `author`
        # field at all (Crossref has two such here: an unsigned Nature Methods
        # briefing, and a book with editors), and claiming `authors_source:
        # "crossref"` for an absent byline says the registrar answered when it
        # did not -- which then made `authors_source` disagree with `authors`
        # about how many papers have a list.
        rec["authors_source"] = (cached.get("source")
                                 if (cached and rec["authors"]) else None)
        # The sidecar's own `authors:`, BELOW the registrar deliberately. D2's
        # reason has not changed: a publisher's deposit is a better record than
        # anyone's reading of a page. So writing a byline into a sidecar helps
        # KBase and the next reader, and does not overrule Crossref here.
        #
        # And the label stays HONEST. Where the ledger shows WE wrote that field,
        # `authors_source` says so rather than saying "sidecar" -- otherwise this
        # project would launder its own reading of a PDF into something that
        # looks like upstream data, which is the one thing §9 exists to prevent.
        if fm.get("authors"):
            led = edits.get(f"meta/{src}.md")
            # `keys`, plural -- the ledger records every field one edit touched.
            # Reading `key` here silently labelled our own byline as upstream's,
            # which is exactly the laundering §2.0.2 forbids. Caught by selftest 15.
            wrote_it = "authors" in ((led or {}).get("keys") or [])
            if rec["authors"]:
                # BOTH exist. The registration wins, and the disagreement is
                # REPORTED -- the same discipline D2 already imposes on the
                # filename-vs-registration case (§2.2: report every
                # disagreement, apply none silently).
                #
                # This branch was unreachable while `authors:` was five files
                # with no DOI between them. D16 makes the field standing policy,
                # so it WILL be reached: a DOI added upstream later lets Crossref
                # answer for a paper whose sidecar already carries a byline, and
                # a silent mismatch there is a fact quietly disagreeing with
                # itself in two files.
                if not _same_byline(rec["authors"], fm["authors"]):
                    problems.append(
                        f"byline disagreement for {src}: the registration "
                        f"({rec['authors_source']}) lists {len(rec['authors'])} "
                        f"author(s), the sidecar's own `authors:` "
                        f"{len(fm['authors'])}"
                        + (" -- and WE wrote that sidecar field, so one of the "
                           "two readings is wrong" if wrote_it else "")
                        + f"; registration kept, first differing surname "
                          f"{_first_diff(rec['authors'], fm['authors'])!r}"
                    )
            else:
                rec["authors"] = list(fm["authors"])
                rec["authors_source"] = ("sidecar-written-here" if wrote_it
                                         else "sidecar")

        # ---- the PDF must actually be there ----
        raw_path = RAW / src
        if not raw_path.exists():
            problems.append(f"{src}: sidecar `source:` does not resolve in raw/")
            rec["file_ok"] = False
        else:
            rec["file_ok"] = True
            if verify_bytes and sha256_of(raw_path) != rec["sha256"]:
                problems.append(f"{src}: sha256 MISMATCH against the file's own bytes")

        records.append(rec)

    records.sort(key=lambda r: (r["source"] or ""))

    # ---- PDF-read DOIs and bylines, only where upstream has nothing -----------
    # BEFORE ownership on purpose: §6.4 decides own/shared from co-authorship, and
    # `authors` is where it reads it. Measured consequence of getting this wrong --
    # both Lukashiv papers are the OWNER'S OWN and had no author list at all, so
    # ownership fell back to the first-author surname and credited `TL` alone,
    # silently dropping `PN` from his own two papers.
    bib_annot_stats = merge_bib_annotations(records, annot_bib, problems)

    # ---- own vs shared, from the roster in wiki/group.md (§6.4) ----
    # After the author lists are attached, because co-authorship is the criterion
    # and `authors` is where it is read from.
    members = parse_group(GROUP)
    if not members and PROJECT_CFG.get("has_roster", True):
        problems.append(
            f"{GROUP.relative_to(ROOT)} not found or unparseable -- `own` left null on "
            f"every paper and the own/shared switch will not appear (§6.4)"
        )
    # PAPERLIB: `has_roster: false` in paperlib.json makes the absence DECLARED
    # rather than reported. This project collects published literature and writes
    # none of it, so there is no own/shared distinction to draw -- and a warning
    # that fires on every build forever is how people learn to stop reading them.
    # Deleting the check instead would hide a genuinely missing roster from anyone
    # who later does want one.
    # Before ownership, because ownership matches on these strings and a
    # confirmed correction can decide a match the raw string could not.
    annot_stats = merge_annotated_taxonomy(taxonomy, annot, records, problems)
    name_stats = canonical_authors(records, members, problems)
    own_stats = annotate_ownership(records, members, problems)

    # ---- review entries with no sidecar: the join must be total both ways ----
    seen = {r["source"] for r in records}
    for src in sorted(set(bib) - seen):
        problems.append(f"review entry with no sidecar in meta/: {src}")

    # ---- the diff against the previous manifest (§4.2 obligation 1) ----
    prev_path = DATA / "manifest.json"
    prev = json.loads(prev_path.read_text(encoding="utf-8")) if prev_path.exists() else None
    # Sidecar drift, split into ours and not-ours. `changed` below stays what it
    # always was -- a change to the PDF a sidecar POINTS AT, which is still a
    # violation of add-only and is still not something D15 permits.
    prev_side = (prev or {}).get("sidecars", {})
    now_side = {r["source"]: r["sidecar_sha256"] for r in records + non_lit}
    side_moved = sorted(s_ for s_ in set(now_side) & set(prev_side)
                        if now_side[s_] != prev_side[s_])
    side_ours, side_foreign = [], []
    for s_ in side_moved:
        led = edits.get(f"meta/{s_}.md")
        (side_ours if led and led.get("sha256_after") == now_side[s_]
         else side_foreign).append(s_)
    # A file the ledger claims we edited, whose bytes no longer match what we
    # left: either someone edited it again, or an edit was reverted by hand.
    side_reverted = sorted(
        f[len("meta/"):-len(".md")] for f, led in edits.items()
        if f.startswith("meta/") and f[len("meta/"):-len(".md")] in now_side
        and now_side[f[len("meta/"):-len(".md")]] != led.get("sha256_after"))

    prev_sha = (prev or {}).get("sources", {})
    now_sha = {r["source"]: r["sha256"] for r in records + non_lit}
    new = sorted(set(now_sha) - set(prev_sha))
    gone = sorted(set(prev_sha) - set(now_sha))
    changed = sorted(s for s in set(now_sha) & set(prev_sha) if now_sha[s] != prev_sha[s])
    unfiled = sorted(r["source"] for r in records if r["unfiled"])

    DATA.mkdir(exist_ok=True)
    REPORTS.mkdir(exist_ok=True)

    # Derived from the inputs, never from the clock (see the module docstring).
    review_date = re.match(r"(\d{4}-\d{2}-\d{2})_", review_path.name).group(1)
    processed = [p for p in (r.get("processed") for r in all_fm) if p]
    data_as_of = max([review_date, *processed])

    manifest = {
        "data_as_of": data_as_of,
        "review_date": review_date,
        "review_file": review_path.name,
        "counts": {
            "sidecars": len(records) + len(non_lit),
            "papers": len(records),
            "non_literature": len(non_lit),
            "review_entries": rstats["entries"],
            "parts": rstats["parts"],
            "topics": rstats["topics"],
            "unfiled": len(unfiled),
            "with_doi": sum(1 for r in records if r["doi"]),
            "with_arxiv": sum(1 for r in records if r["arxiv"]),
            "with_title": sum(1 for r in records if r["title"]),
            # registered = has a title AND it is not the filename fallback. Keeping
            # these separate is a §9 content requirement, not a statistic.
            "title_registered": sum(
                1 for r in records if r["title"] and not r["title_from_filename"]
            ),
            "title_from_filename": sum(1 for r in records if r["title_from_filename"]),
            "with_authors": sum(1 for r in records if r["authors"]),
            "with_venue": sum(1 for r in records if r.get("venue")),
            "distinct_venues": len({r["venue"] for r in records if r.get("venue")}),
            "traceable": sum(1 for r in records if r["provenance"]["traceable"]),
            "untraceable": sum(1 for r in records if not r["provenance"]["traceable"]),
            "also_in_topic_area": sum(1 for r in records if r["duplicate_of_area"]),
            "topic_from_review": sum(1 for r in records if r.get("topic_source") == "review"),
            "topic_curated": sum(1 for r in records if r.get("topic_source") == "curated"),
            "curated_new_topics": annot_stats["new_topics"],
            "curated_new_parts": annot_stats["new_parts"],
            "circulation_sentences": sum(len(r["hay_drop"]) for r in records),
            "circulation_papers": sum(1 for r in records if r["hay_drop"]),
            "authors_from_registration": sum(
                1 for r in records
                if r["authors"] and r.get("authors_source") != "pdf-byline"
            ),
            "authors_from_pdf": bib_annot_stats["authors"],
            "authors_from_sidecar": sum(
                1 for r in records
                if r.get("authors_source") in ("sidecar", "sidecar-written-here")),
            # A STATE, not a diff. `diff.sidecars_edited_here` only fires on the
            # build right after an edit -- but the copy still diverges from KBase
            # on every build after that, and D15's whole cost is that the
            # divergence is permanent and silent (§2.0.1). So this counts what
            # the ledger currently accounts for, and it is reported every run.
            "sidecars_carrying_our_edits": sum(
                1 for f, e in edits.items()
                if f.startswith("meta/")
                and now_side.get(f[len("meta/"):-len(".md")]) == e.get("sha256_after")),
            "upstream_edits_recorded": len(edits),
            "sidecars_edited_since_last_build": len(side_ours),
            "doi_from_pdf": bib_annot_stats["doi"],
            "bib_annot_crosschecked": bib_annot_stats["redundant_authors"],
            "bib_annot_agree": bib_annot_stats["agree"],
            "bib_annot_disagree": bib_annot_stats["disagree"],
            "venue_from_filename": sum(
                1 for r in records if r.get("venue_source") == "filename"
            ),
            "author_names_merged": name_stats["merged"],
            "author_names_confirmed_fixes": name_stats["confirmed"],
            "own": own_stats["own"],
            "shared": own_stats["shared"],
            "own_by_basis": own_stats["by_basis"],
        },
        "diff": {"new": new, "changed": changed, "gone": gone, "unfiled": unfiled,
                 "sidecars_edited_here": side_ours,
                 "sidecars_changed_not_ours": side_foreign,
                 "sidecars_no_longer_as_we_left_them": side_reverted},
        "bytes_verified": verify_bytes,
        # sha256 per source: this is what makes the next build's diff possible (§4.2)
        "sources": dict(sorted(now_sha.items())),
        # ...and per SIDECAR, which is what makes an edit to one visible (D15)
        "sidecars": dict(sorted(now_side.items())),
    }
    library = {
        "data_as_of": data_as_of,
        "review_file": review_path.name,
        "taxonomy": taxonomy,
        # The roster, so the page can label `own_members: ["PN"]` with a name.
        # Only members who actually co-authored something here are shipped.
        "group": [
            {"initials": m["initials"], "name": m["name"],
             "papers": own_stats["by_member"][m["initials"]]}
            for m in members if own_stats["by_member"].get(m["initials"])
        ],
        "colleagues": colleague_counts(records),
        "papers": records,
        "notice": {
            # §9: these are content requirements, carried in the data so the page
            # cannot render without them.
            "not_a_source": (
                "The summaries are paraphrases written when each paper was ingested, not "
                "quotations. This page is not a source: a claim you intend to rely on must "
                "be checked in the paper itself."
            ),
            "provenance": (
                "This library is defined by provenance, not subject: a paper is here because "
                "a named colleague recommended it on a named date. Being here is not an "
                "endorsement -- circulated, read, trusted and used are four different things."
            ),
            "titles": (
                "Titles come from the publisher's registration. Where no registered record "
                "exists, the title is taken from the filename and is labelled as such -- "
                "filenames were truncated at 98 characters upstream, invisibly."
            ),
        },
    }

    (DATA / "library.json").write_text(
        json.dumps(library, ensure_ascii=False, indent=1, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    prev_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )

    report(manifest, rstats, problems, own_stats, name_stats)
    # `gone` fails the build: under add-only it means a hand deletion (§4.4).
    if gone:
        print(f"build: FATAL: {len(gone)} source(s) gone. Add-only updates never remove "
              f"a source; someone deleted from raw/ or meta/ by hand (§2).", file=sys.stderr)
        for s in gone:
            print(f"  gone: {s}", file=sys.stderr)
        return 1
    return 0


def title_from_filename(source: str) -> str:
    """Last-resort display title: `Rosen(2026) Nature; Universal cell embedding.pdf`
    -> `Universal cell embedding`. Always labelled as such by the caller."""
    stem = re.sub(r"\.(pdf|docx|txt|md)$", "", source, flags=re.I)
    return (stem.split("; ", 1)[1] if "; " in stem else stem).strip()


# Companion to title_from_filename. `Heyndrickx(2026) bioRxiv; OmicsFM ...` -> `bioRxiv`.
#
# Why this exists: for an UNFILED paper the venue came from `registered_venue`
# alone, and Crossref registers NO container-title for `posted-content` -- 27 of
# the 329 cached records have `registered_venue: null`. A paper the review has
# filed falls back on the review's venue, so the gap only shows on a preprint
# copied in since the last review: measured at 3 papers (both Lukashiv, and
# Heyndrickx bioRxiv), all three with the venue sitting in plain sight in their
# own filename. Labelled `venue_source: "filename"` because §9 forbids an
# unlabelled fallback.
#
# Declines rather than guesses on the two shapes that carry no venue: a filename
# with no `; ` separator, and the literal `unknown` that upstream writes when it
# could not tell.
VENUE_NOT_RECORDED = {"unknown", "unknown venue", "n/a", "na", "none", ""}


def venue_from_filename(source: str) -> str | None:
    stem = re.sub(r"\.(pdf|docx|txt|md)$", "", source, flags=re.I)
    head = stem.split("; ", 1)[0] if "; " in stem else ""
    # `Heyndrickx(2026) bioRxiv` -> everything after the (year)
    m = re.match(r"^[^(]*\(\s*\d{4}[a-z]?\s*\)\s*(?P<venue>.*)$", head)
    if not m:
        return None
    v = m.group("venue").strip(" .,;-")
    if v.lower() in VENUE_NOT_RECORDED:
        return None
    return clean_venue(v)


def normdoi(d: str) -> str:
    return unicodedata.normalize("NFKC", d).strip().lower().removeprefix("https://doi.org/")


def colleague_counts(records: list) -> list:
    tally: dict[str, int] = {}
    for r in records:
        for who in r["provenance"]["sharers"]:
            tally[who] = tally.get(who, 0) + 1
    return [{"who": w, "count": c} for w, c in sorted(tally.items(), key=lambda kv: (-kv[1], kv[0]))]


def report(manifest: dict, rstats: dict, problems: list, own_stats: dict | None = None,
           name_stats: dict | None = None) -> None:
    c, d = manifest["counts"], manifest["diff"]
    print(f"build: review = {manifest['review_file']} · data as of {manifest['data_as_of']}")
    print(f"build: {c['papers']} papers · {c['non_literature']} non-literature · "
          f"{c['review_entries']} review entries · the REVIEW's taxonomy "
          f"{c['parts']} parts / {c['topics']} topics (checked against its own "
          f"Contents table)")
    if c.get("curated_new_topics") or c.get("curated_new_parts"):
        print(f"build: the SHIPPED taxonomy {c['parts'] + c['curated_new_parts']} parts / "
              f"{c['topics'] + c['curated_new_topics']} topics, after the local "
              f"annotation (§6.6)")
    print(f"build: titles {c['title_registered']} registered + {c['title_from_filename']} from "
          f"filename = {c['with_title']} · doi {c['with_doi']} · arxiv {c['with_arxiv']} "
          f"· authors {c['with_authors']}")
    if c.get("authors_from_pdf") or c.get("doi_from_pdf"):
        print(f"build: annotations/bibliography.json supplied "
              f"{c['authors_from_pdf']} byline(s) and {c['doi_from_pdf']} DOI(s) "
              f"upstream did not have · {c['bib_annot_crosschecked']} more "
              f"cross-checked against the registration "
              f"({c['bib_annot_agree']} agree, {c['bib_annot_disagree']} differ)")
    if c.get("venue_from_filename"):
        print(f"build: {c['venue_from_filename']} venue(s) fell back to the filename "
              f"(no registered container-title; labelled venue_source=filename)")
    print(f"build: {c['circulation_sentences']} circulation sentence(s) in "
          f"{c['circulation_papers']} paper(s) excluded from SEARCH, kept in the "
          f"displayed prose (compare embed.py's own count)")
    print(f"build: venues {c['with_venue']}/{c['papers']} on {c['distinct_venues']} "
          f"distinct journals · provenance {c['traceable']} traceable / "
          f"{c['untraceable']} not")
    if c.get("topic_curated"):
        print(f"build: topics {c['topic_from_review']} from the review + "
              f"{c['topic_curated']} CURATED HERE (§6.6) -- adding "
              f"{c['curated_new_topics']} topic(s) and {c['curated_new_parts']} part(s). "
              f"A regenerated review overrides every one of them.")
    if name_stats and (name_stats["people"] or name_stats["confirmed"]
                       or name_stats["ws"] or name_stats["declined"]):
        print(f"build: author names -- {name_stats['ws']} whitespace, "
              f"{name_stats['confirmed']} owner-confirmed correction(s), "
              f"{name_stats['merged']} string(s) merged onto a roster member (§6.4)")
        for keep, gone, n in name_stats["people"]:
            print(f"  one person:  {keep!r}  <- {', '.join(repr(g) for g in gone)}"
                  f"   ({n} author slot(s))")
        for who, odd, allv in name_stats["declined"]:
            print(f"  NOT merged:  {who} -- {len(allv)} form(s) of this surname, but "
                  f"{', '.join(repr(o) for o in odd[:3])} "
                  f"{'is' if len(odd) == 1 else 'are'} someone else")
    if own_stats and own_stats.get("own") is not None:
        basis = " + ".join(f"{n} by {k}" for k, n in sorted(own_stats["by_basis"].items()))
        print(f"build: own {c['own']} · shared {c['shared']} "
              f"({basis or 'no roster match'}) · roster "
              f"{len(own_stats['by_member'])} member(s) co-author something here")
        if own_stats.get("unknowable"):
            # Deliberately no longer says "run make bib". As of 2026-09-03 the two
            # papers in this bucket are BOTH permanent: Crossref's record for the
            # Nature Methods research briefing has no `author` field at all, and
            # Colliot(2023) is registered as a `book` with editors and no authors.
            # `make bib` cannot help either, and telling the operator to run it
            # sends them after a fix that does not exist. `make audit` explains
            # each one instead.
            print(f"build: note -- {own_stats['unknowable']} paper(s) have no author list "
                  f"and no member surname in the filename, so own vs shared could not be "
                  f"decided for them; they count as shared. `make audit` says why for "
                  f"each -- some are permanent (an editor-only book, an unsigned "
                  f"briefing) and `make bib` cannot fix those.")
        for src, author, who in own_stats.get("near_misses", [])[:10]:
            print(f"  near-miss: {author!r} vs roster {who!r} -- same surname, different "
                  f"given name; NOT counted as own")
            print(f"             {src}")
    if c.get("upstream_edits_recorded"):
        print(f"build: {c['sidecars_carrying_our_edits']} sidecar(s) carry an edit made "
              f"HERE, all accounted for in annotations/upstream_edits.json "
              f"({c['upstream_edits_recorded']} file(s) in the ledger, sidecars and "
              f"outputs/ together). "
              f"This copy DIVERGES from KBase until the owner carries them back (D15, §2.2).")
    for s_ in d.get("sidecars_changed_not_ours", []):
        print(f"  SIDECAR CHANGED AND NOT BY US: {s_}\n"
              f"      Its bytes differ from the last build and no ledger entry explains "
              f"it. Either upstream re-sent it (D0 says nothing should be overwritten) "
              f"or it was edited outside the tool. `git diff -- meta/` shows what moved.")
    for s_ in d.get("sidecars_no_longer_as_we_left_them", []):
        print(f"  OUR EDIT IS GONE OR CHANGED: {s_}\n"
              f"      The ledger records an edit here, but the file no longer matches "
              f"what we left. Re-apply it or delete the ledger entry -- do not leave "
              f"the two disagreeing.")
    print(f"build: DIFF  new {len(d['new'])} · changed {len(d['changed'])} · "
          f"gone {len(d['gone'])} · unfiled {len(d['unfiled'])}")
    for s in d["new"][:20]:
        print(f"  new:      {s}")
    if len(d["new"]) > 20:
        print(f"  new:      ... and {len(d['new']) - 20} more")
    for s in d["changed"]:
        print(f"  CHANGED:  {s}   <- not expected under add-only; a copy was edited in place (§2)")
    for s in d["unfiled"]:
        print(f"  unfiled:  {s}   <- no review entry yet; topic left null (§4.3)")
    if problems:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        out = REPORTS / f"build_{stamp}.txt"
        out.write_text("\n".join(problems) + "\n", encoding="utf-8")
        print(f"build: {len(problems)} problem(s) -> {out.relative_to(ROOT)}")
        for p in problems[:15]:
            print(f"  ! {p}")
        if len(problems) > 15:
            print(f"  ! ... and {len(problems) - 15} more")
    else:
        print("build: no problems")


if __name__ == "__main__":
    sys.exit(main())
