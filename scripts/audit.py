#!/usr/bin/env python3
"""Validate data/library.json against every other source we can reach — and say
which findings are OURS to fix and which are the owner's, upstream.

Why this exists as a script rather than a one-off measurement: the corpus grows by
add-only copy (§4), so every check here is one that has to be re-run on papers that
do not exist yet. A validation done once by hand is a validation that rots.

Two severities, and the distinction is the whole point:

  PROBLEM  something is wrong in THIS project's derivation. Exit 1. Fix it here.
  NOTE     a fact about upstream or about a publisher's registration, for
           reports/upstream_findings.md (§2.2). Expected to persist -- an
           online-first/issue-year gap is never going to reach zero -- so it does
           NOT fail the run. `--strict` makes it fail anyway.

Reads only generated and hand-written state plus `raw/` (read, never write -- §2).
Imports build.py rather than re-deriving anything: a validator with its own copy of
the ownership rule validates its copy, not the product.

Usage:  python3 scripts/audit.py [--strict] [--pdf] [-v]
        --pdf   also re-extract page 1 of every annotated PDF to verify each
                transcribed byline name really occurs in it (slow: ~9 PDFs)
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  -- one source of truth for folding, roster, venue rules

ROOT = build.ROOT
DATA, RAW, META = build.DATA, build.RAW, build.META

# A registration whose FIRST author is an organisation, not a person. Checked
# against the corpus rather than assumed: each of these is a real Crossref record
# where the consortium is deposited first and the filename names a human member,
# so a surname mismatch there is correct behaviour, not a defect.
CORPORATE = re.compile(
    r"\b(consortium|group|team|collaboration|network|initiative|committee|"
    r"center for|centre for|institute|society|working party|labs?)\b", re.I)

# Ligatures survive pdftotext as single code points; NFKD does not split them.
LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl",
             "ﬃ": "ffi", "ﬄ": "ffl"}


def squash(s: str) -> str:
    """Comparison form for 'does this string occur in that page of text'."""
    for k, v in LIGATURES.items():
        s = s.replace(k, v)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def decamel(s: str) -> str:
    """`PriorLabsTeam` -> `Prior Labs Team`.

    Filenames write an organisation as one CamelCase word, so CORPORATE's word
    boundaries never fire on it -- which made `PriorLabsTeam(2026) arXiv` the
    audit's one remaining "problem" when it is a known upstream fact (arXiv
    deposits Léo Grinsztajn first; the filename names the lab).
    """
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", s)


def name_runs(name: str) -> set:
    """Every contiguous run of whole tokens in a name, squashed.

    `Adrien Leite Pereira` -> {adrien, adrienleite, adrienleitepereira, leite,
    leitepereira, pereira}.

    This replaced a surname EXTRACTOR, and the reason is worth keeping. A byline
    reaches this project in two shapes -- the review's `Leite Pereira, A. et al.`,
    where the surname is stated exactly, and a registration's `Adrien Leite
    Pereira`, where it is not recoverable from the string at all. Every heuristic
    for the second shape failed on real data in this corpus:

      * last token          -- `Leite Pereira` -> `Pereira`, a different surname
      * particle walk-back  -- the list needed for `de Groot` and `ter Huurne`
                               also swallows the given name `Bin` in `Bin Duan`
                               (Arabic *bin*) and `Le` in `Le Grand`
      * comma-splitting     -- only the review's shape has a comma

    Asking instead "does the stated surname occur as a run of tokens inside the
    full name" needs no list, no language assumption and no guess: `Duan` sits in
    `Bin Duan`, `Leite Pereira` in `Adrien Leite Pereira`, `Cultrera di
    Montesano` in `Sebastiano Cultrera di Montesano`. All three were false
    problems until this replaced the extractor.
    """
    n = re.sub(r"\bet\s+al\.?", " ", name)
    n = re.sub(r"[-\u2010\u2011\u2012\u2013\u2014,;.]", " ", n)
    toks = [squash(t) for t in n.split()]
    toks = [t for t in toks if t]
    out = set()
    for i in range(len(toks)):
        for j in range(i + 1, len(toks) + 1):
            out.add("".join(toks[i:j]))
    return out


def name_matches(a: str, b: str) -> bool:
    """True when the two strings name the same person as far as either states it.

    Deliberately symmetric: the filename may hold less than the registration
    (`Martins` vs `Martins Conde`) or, once squashed, more than one token of it
    (`LeitePereira` vs `Leite Pereira`).
    """
    ra, rb = name_runs(a), name_runs(b)
    if not ra or not rb:
        return False
    return bool(ra & rb)


def words(s: str) -> set:
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return set(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())


class Audit:
    def __init__(self) -> None:
        self.problems: list[str] = []
        self.notes: list[str] = []
        self.checks = 0

    def problem(self, msg: str) -> None:
        self.problems.append(msg)

    def note(self, msg: str) -> None:
        self.notes.append(msg)

    def check(self, n: int = 1) -> None:
        self.checks += n


# --------------------------------------------------------------------------- #
# the checks
# --------------------------------------------------------------------------- #

def check_join(a: Audit, papers: list) -> None:
    """meta/ <-> raw/ <-> library.json, total in every direction."""
    srcs = {p["source"] for p in papers}
    sidecars = {f.name[:-3] for f in META.glob("*.md")}
    rawfiles = {f.name for f in RAW.iterdir() if f.is_file()}
    a.check(3)

    for s in sorted(srcs - rawfiles):
        a.problem(f"join: {s!r} is a paper but has no file in raw/")
    for s in sorted(srcs - sidecars):
        a.problem(f"join: {s!r} is a paper but has no sidecar in meta/")
    # A sidecar that is not a paper is EXPECTED for the non-literature types (§12)
    # and for the two out-of-scope resources (§6.7). Anything else is a real hole.
    extra = sidecars - srcs
    known = set()
    for name in sorted(extra):
        fm = (META / f"{name}.md").read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^type:\s*(\S+)", fm, re.M)
        typ = (m.group(1).strip('"\'') if m else "?")
        if typ in build.NON_LITERATURE_TYPES:
            known.add(name)
        else:
            a.problem(f"join: sidecar {name!r} (type {typ!r}) produced no paper")
    if known:
        a.note(f"join: {len(known)} non-literature sidecar(s) excluded by type, "
               f"as designed: {', '.join(sorted(known))}")


def check_coverage(a: Audit, papers: list, cache: dict, annot: dict) -> None:
    """Which papers are missing what, and WHY -- an explained gap is not a defect."""
    a.check(len(papers) * 4)
    no_authors, no_ident, no_venue, no_first = [], [], [], []
    for p in papers:
        ident = p.get("doi") or p.get("arxiv")
        if not p.get("authors"):
            no_authors.append(p)
        if not ident:
            no_ident.append(p)
        if not p.get("venue"):
            no_venue.append(p)
        if not p.get("first_author"):
            no_first.append(p)

    for p in no_authors:
        c = cache.get(p["sha256"]) or {}
        if c and not c.get("authors"):
            a.note(f"no byline: {p['source'][:64]!r} — the publisher's own record "
                   f"({c.get('registered_type') or '?'}) carries no author list; "
                   f"nothing to fix here or upstream")
        elif p["sha256"] in annot:
            a.problem(f"no byline: {p['source'][:64]!r} is in "
                      f"annotations/bibliography.json but got no authors from it")
        else:
            a.problem(f"no byline: {p['source'][:64]!r} has no identifier and no "
                      f"annotation — read its page 1 and add one")

    for p in no_ident:
        if p["sha256"] in annot:
            a.note(f"no identifier: {p['source'][:56]!r} — checked, the PDF prints "
                   f"none (see annotations/bibliography.json)")
        else:
            a.problem(f"no identifier: {p['source'][:56]!r} — not yet checked "
                      f"against the PDF itself")

    for p in no_venue:
        a.note(f"no venue: {p['source'][:64]!r} — no registered container-title and "
               f"none recoverable from the filename")
    for p in no_first:
        a.problem(f"no first author: {p['source'][:64]!r}")


def check_identity(a: Audit, papers: list) -> None:
    """Things that must be unique, and fields that must agree with each other."""
    a.check(len(papers) * 3)
    for field, label in (("sha256", "sha256"), ("id", "id")):
        dup = [k for k, n in collections.Counter(
            p[field] for p in papers).items() if n > 1]
        for k in dup:
            hits = [p["source"][:52] for p in papers if p[field] == k]
            a.problem(f"duplicate {label} {k[:16]}…: {hits}")

    seen: dict = {}
    for p in papers:
        if p.get("doi"):
            seen.setdefault(build.normdoi(p["doi"]), []).append(p)
    for doi, hits in seen.items():
        if len(hits) > 1:
            a.problem(f"duplicate DOI {doi}: "
                      f"{[h['source'][:44] for h in hits]}")

    for p in papers:
        au, fa = p.get("authors"), p.get("first_author")
        if not au or not fa:
            continue
        if not name_runs(fa):
            continue
        if not any(name_matches(fa, x) for x in au):
            a.problem(f"first_author {fa!r} does not appear in the {len(au)}-name "
                      f"byline of {p['source'][:48]!r}")
        elif not name_matches(fa, au[0]):
            a.note(f"first_author {fa!r} is in the byline of "
                   f"{p['source'][:44]!r} but not first — the registration deposits "
                   f"{au[0]!r} first")


def check_registration(a: Audit, papers: list, cache: dict) -> None:
    """library.json vs what the publisher actually registered."""
    for p in papers:
        c = cache.get(p["sha256"])
        if not c:
            continue
        a.check(3)
        fn = re.match(r"^(?P<sur>[^(]+?)\s*\(\s*(?P<yr>\d{4})", p["source"])

        ry = c.get("registered_year")
        if ry and ry != p["year"]:
            gap = abs(ry - p["year"])
            a.note(f"year: {p['source'][:52]!r} sidecar {p['year']} vs registered "
                   f"{ry}" + ("  (off by one — the ordinary online-first vs "
                              "issue-year gap)" if gap == 1 else
                              f"  ** off by {gap} — CHECK **"))

        au = c.get("authors") or []
        if fn and au:
            want = fn.group("sur")
            if not any(name_matches(want, x) for x in au):
                if CORPORATE.search(au[0]) or CORPORATE.search(decamel(want)):
                    who = (au[0] if CORPORATE.search(au[0])
                           else fn.group("sur").strip())
                    a.note(f"first author: {p['source'][:44]!r} — filename "
                           f"{fn.group('sur').strip()!r} vs registration "
                           f"{au[0]!r}; {who!r} is an ORGANISATION, not a person, "
                           f"so the two are not comparable")
                else:
                    a.problem(f"first author: {p['source'][:44]!r} — filename says "
                              f"{fn.group('sur').strip()!r}, registration says "
                              f"{au[0]!r}, and that surname is nowhere in the "
                              f"{len(au)}-name byline")
            elif not name_matches(want, au[0]):
                a.note(f"first author: {p['source'][:44]!r} — filename says "
                       f"{fn.group('sur').strip()!r}, who is in the byline but not "
                       f"first; the registration deposits {au[0]!r}")

        rt = c.get("registered_title")
        if rt and p.get("title"):
            aw, bw = words(p["title"]), words(rt)
            if aw and bw:
                j = len(aw & bw) / len(aw | bw)
                if j < 0.55:
                    a.problem(f"title: {p['source'][:40]!r} shares only "
                              f"{j:.0%} of its words with the registered title\n"
                              f"        ours: {p['title'][:88]}\n"
                              f"        reg : {rt[:88]}")

        rv, mv = c.get("registered_venue"), p.get("venue")
        if rv and mv:
            a.check()
            x, y = words(build.unescape_md(rv)), words(mv)
            if x != y and not (x <= y or y <= x):
                a.note(f"venue: {p['source'][:40]!r} ours {mv!r} vs registered "
                       f"{build.unescape_md(rv)!r}")


def check_annotations(a: Audit, papers: list, annot: dict, use_pdf: bool) -> None:
    """The local bibliography must stay honest: complete, keyed right, and real."""
    by_sha = {p["sha256"]: p for p in papers}
    a.check(len(annot) * 2)
    for sha, e in sorted(annot.items()):
        p = by_sha.get(sha)
        if p is None:
            a.problem(f"annotation {sha[:12]}… ({e.get('source', '?')!r}) matches "
                      f"no paper")
            continue
        if e.get("source") != p["source"]:
            a.problem(f"annotation {sha[:12]}… names {e.get('source')!r}, corpus "
                      f"says {p['source']!r}")
        if not e.get("evidence"):
            a.problem(f"annotation for {p['source'][:52]!r} records no `evidence` — "
                      f"a bibliographic claim with no stated source is not a record")
        au = e.get("authors")
        if au and (len(au) != len(set(au))):
            a.problem(f"annotation for {p['source'][:52]!r} repeats a name")
        if au and any(CORPORATE.search(x) for x in au):
            a.note(f"annotation for {p['source'][:44]!r} lists what looks like an "
                   f"institution among the authors")

        if use_pdf and au:
            path = RAW / p["source"]
            if not path.exists():
                a.problem(f"annotation for {p['source'][:52]!r}: file missing")
                continue
            try:
                txt = subprocess.run(
                    ["pdftotext", "-f", "1", "-l", "1", "-raw", str(path), "-"],
                    capture_output=True, text=True, timeout=120).stdout
            except (OSError, subprocess.SubprocessError) as exc:
                a.note(f"annotation for {p['source'][:44]!r}: could not re-extract "
                       f"({exc}); byline left unverified")
                continue
            hay = squash(txt)
            a.check(len(au))
            miss = [x for x in au if squash(x) not in hay]
            # A name broken across a line break loses its given-name adjacency;
            # the surname alone is still proof the person is on the page.
            hard = [x for x in miss
                    if squash(build._surnames([x])[0]) not in hay]
            if hard:
                a.problem(f"annotation for {p['source'][:44]!r}: {len(hard)} "
                          f"transcribed name(s) do not occur in the PDF's own "
                          f"page 1: {hard}")


def check_ownership(a: Audit, papers: list) -> None:
    """own/shared — but re-derived with build.py's OWN matcher, deliberately.

    The first version of this check matched on the surname alone and reported
    every `Zhang` and `Kim` in the corpus as the team's work. That is precisely
    the trap `match_author`'s docstring warns about: 87 people wear `Zhang` here,
    so a surname is not an identity and `distinctive` is what licenses a weak
    match. So this does not re-implement the rule — it re-runs it, and checks the
    two things a re-run can actually catch:

      1. library.json CONTRADICTING ITSELF: `own_basis: "author"` on a paper
         whose byline no member matches.
      2. an UNDER-CREDIT: a member the matcher does find who is not in
         `own_members`. This is the failure that was live before today — both
         Lukashiv papers are the owner's own and credited `TL` alone, because
         with no byline at all the decision had fallen back to the filename.
    """
    members = build.parse_group(build.GROUP)
    if not members and not build.PROJECT_CFG.get("has_roster", True):
        # Declared absent in paperlib.json: this project collects published
        # literature and writes none of it, so there is no own/shared distinction
        # to draw. Reported as a note so the state stays visible, not as a problem
        # that fails every audit forever.
        a.note("ownership: no roster (has_roster: false) — `own` is null by design")
        return
    if not members:
        a.problem("ownership: wiki/group.md did not parse — every `own` is null")
        return
    owners = build.surname_owners(papers)
    a.check(len(papers))
    for p in papers:
        au = p.get("authors") or []
        if not au:
            continue
        hit = set()
        for mem in members:
            distinctive = len(owners.get(" ".join(mem["surname"]), set())) <= 1
            if any(build.match_author(x, mem, distinctive) for x in au):
                hit.add(mem["initials"])

        got = set(p.get("own_members") or [])
        if p.get("own_basis") == "author" and not hit:
            a.problem(f"ownership: {p['source'][:52]!r} is own-by-author but "
                      f"re-running match_author over its {len(au)}-name byline "
                      f"finds no roster member")
        if hit and not p["own"]:
            a.problem(f"ownership: {p['source'][:52]!r} has roster member(s) "
                      f"{sorted(hit)} in its byline but is filed as SHARED")
        if hit - got:
            a.problem(f"ownership: {p['source'][:52]!r} credits {sorted(got)} but "
                      f"the byline also matches {sorted(hit - got)}")
        if got - hit and p.get("own_basis") == "author":
            a.problem(f"ownership: {p['source'][:52]!r} credits {sorted(got - hit)}, "
                      f"which match_author does not find in its byline")


def check_upstream_edits(a: Audit, papers: list) -> None:
    """The edit ledger must still describe the files as they are (D15, §2.0.1).

    This is the check that keeps D15 honest. An edit made here survives the next
    add-only copy, so the copy and KBase diverge silently -- the only defence is
    that a divergence nobody recorded, or a record whose file has moved on, is
    noisy. Both directions are checked.
    """
    led = build.load_edit_ledger(build.EDIT_LEDGER, [])
    if not led:
        return
    by_side = {f"meta/{p['source']}.md": p for p in papers}
    a.check(len(led) * 2)
    for rel, e in sorted(led.items()):
        path = ROOT / rel
        top = Path(rel).parts[0]
        if top == "raw":
            # D15 originally excluded raw/ absolutely. Since 2026-09-04 it is
            # ADD-ONLY (§2.0): a new paper may be added, and no existing file may
            # ever be modified, renamed or deleted. The distinction is exactly
            # what keeps `make verify`'s byte chain meaningful for every file
            # that was already there, so it is enforced rather than trusted --
            # an entry that REPLACED something in raw/ had a hash before it.
            if e.get("sha256_before"):
                a.problem(f"edit ledger: {rel!r} REPLACED an existing file in "
                          f"raw/ (it records a sha256_before). raw/ is add-only: "
                          f"no existing file may be modified, renamed or deleted")
            elif not path.is_file():
                a.problem(f"edit ledger: {rel!r} was added to raw/ but is not "
                          f"there now")
            elif build.sha256_of(path) != e.get("sha256_after"):
                a.problem(f"edit ledger: {rel!r} in raw/ no longer matches the "
                          f"bytes we added (seq {e.get('seq')})")
            continue
        if top not in ("meta", "outputs", "wiki"):
            a.problem(f"edit ledger: {rel!r} is outside D15's scope")
            continue

        if not path.is_file():
            a.problem(f"edit ledger: {rel!r} no longer exists, but an edit to it "
                      f"is recorded")
            continue
        now = build.sha256_of(path)
        if now != e.get("sha256_after"):
            a.problem(f"edit ledger: {rel!r} is no longer as we left it "
                      f"(seq {e.get('seq')}) — re-apply the edit or delete the "
                      f"entry, but do not leave the two disagreeing")
        if not e.get("approved"):
            a.problem(f"edit ledger: seq {e.get('seq')} records no approval, and "
                      f"D15 permits an edit only after asking")
        if not e.get("evidence"):
            a.note(f"edit ledger: seq {e.get('seq')} on {rel[5:][:44]!r} records no "
                   f"`evidence` — the fact is in the sidecar with nothing saying "
                   f"where it came from")
        # The claim has to survive into the built data, or the edit did nothing.
        p = by_side.get(rel)
        if p is not None:
            for key, want in (e.get("after") or {}).items():
                if key == "doi" and build.normdoi(p.get("doi") or "") != build.normdoi(want):
                    a.note(f"edit ledger: we wrote doi={want!r} into "
                           f"{rel[5:][:40]!r} but library.json shows "
                           f"{p.get('doi')!r} — something downstream prefers "
                           f"another source, which may be correct")
                if key == "authors" and isinstance(want, list) and p.get("authors"):
                    if not build._same_byline(p["authors"], want):
                        a.note(f"edit ledger: the byline we wrote into "
                               f"{rel[5:][:40]!r} is not the one library.json "
                               f"shows — the registration outranks it (D2), which "
                               f"is intended")


ENTITY = re.compile(r"&(?:[a-zA-Z][a-zA-Z0-9]{1,10}|#\d{1,6});")
# The page escapes every tag except these (app.js fmtTags), so any other one is
# rendered as literal angle brackets rather than as formatting.
PAGE_TAGS = ("i", "em", "b", "strong", "sup", "sub")
OTHER_TAG = re.compile(r"</?(?!(?:%s)\b)[a-zA-Z][a-zA-Z0-9]*\s*/?>" % "|".join(PAGE_TAGS))


def check_sidecar_titles(a: Audit, papers: list) -> None:
    """A `title:` written into a sidecar has to be clean and has to agree.

    Both checks exist because both failed on the way in, on 234 titles taken
    from publisher registrations:

      * `H&amp;E Images` -- Crossref deposits HTML entities and the normalisation
        did not unescape them, so one sidecar carried `&amp;` where the review's
        own title correctly said `&`. build.py has had `unescape_md()` for this
        since the first build; it simply was not applied.
      * `<scp>IDH</scp>` and `<i>Bonsai</i>\n   : Tree` -- Crossref pretty-prints
        its XML, so a newline and indent land beside inline markup, and a tag the
        page does not whitelist reaches the reader as visible angle brackets.
    """
    by_side = {}
    for f in sorted(META.glob("*.md")):
        fm = build.parse_frontmatter(f.read_text(encoding="utf-8", errors="replace"))
        if fm.get("source") and fm.get("title"):
            by_side[fm["source"]] = fm["title"]
    a.check(len(by_side) * 3)
    P = {p["source"]: p for p in papers}
    for src, t in by_side.items():
        if ENTITY.search(t):
            a.problem(f"sidecar title for {src[:50]!r} holds an HTML entity "
                      f"({ENTITY.search(t).group(0)!r}) -- it will render literally")
        if OTHER_TAG.search(t):
            a.problem(f"sidecar title for {src[:50]!r} holds "
                      f"{OTHER_TAG.search(t).group(0)!r}, which the page does not "
                      f"whitelist and so shows as visible angle brackets")
        if re.search(r"\s[:;,]|\s[?!]", t):
            a.note(f"sidecar title for {src[:44]!r} has a space before punctuation "
                   f"-- usually Crossref's pretty-printed XML surviving a collapse")
        p = P.get(src)
        if p and p.get("title_source") == "review":
            # The review is the title of record (D1), so a difference here is not
            # an error -- but a SUBSTANTIVE one means one of the two is wrong.
            aw, bw = words(t), words(p["title"])
            if aw and bw and len(aw & bw) / len(aw | bw) < 0.9:
                a.note(f"title: {src[:40]!r} -- the review and the sidecar disagree "
                       f"beyond punctuation; the review wins (D1)\n"
                       f"        review : {p['title'][:80]}\n"
                       f"        sidecar: {t[:80]}")


def check_taxonomy(a: Audit, lib: dict, papers: list) -> None:
    tax = lib["taxonomy"]
    a.check(len(tax) + len(papers))
    letters = {t["letter"] for t in tax}
    names = {t["name"] for p in tax for t in p["topics"]}
    for part in tax:
        if not part["topics"]:
            a.problem(f"taxonomy: part {part['letter']} {part['name']!r} has no topics")
    for p in papers:
        if p.get("topic") and p["topic"] not in names:
            a.problem(f"taxonomy: {p['source'][:48]!r} is in topic {p['topic']!r}, "
                      f"which is in no part")
        if p.get("part_letter") and p["part_letter"] not in letters:
            a.problem(f"taxonomy: {p['source'][:48]!r} is in part "
                      f"{p['part_letter']!r}, which does not exist")
        if p.get("topic") and not p.get("part_letter"):
            a.problem(f"taxonomy: {p['source'][:48]!r} has a topic but no part — "
                      f"the map will paint it grey and the facet count will read 0")


# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="fail on NOTEs too, not just PROBLEMs")
    ap.add_argument("--pdf", action="store_true",
                    help="re-extract the annotated PDFs and verify every "
                         "transcribed byline name occurs in them")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="print the NOTEs in full rather than the first 40")
    args = ap.parse_args()

    lib_path = DATA / "library.json"
    if not lib_path.exists():
        print("audit: data/library.json not found — run `make build` first.",
              file=sys.stderr)
        return 2
    lib = json.loads(lib_path.read_text(encoding="utf-8"))
    papers = lib["papers"]

    cache_path = DATA / "bib_cache.json"
    cache = {}
    if cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8")).get("by_sha256", {})
    annot = build.load_bib_annotations(build.ANNOT_BIB, [])

    a = Audit()
    check_join(a, papers)
    check_coverage(a, papers, cache, annot)
    check_identity(a, papers)
    check_registration(a, papers, cache)
    check_annotations(a, papers, annot, args.pdf)
    check_ownership(a, papers)
    check_upstream_edits(a, papers)
    check_sidecar_titles(a, papers)
    check_taxonomy(a, lib, papers)

    print(f"audit: {len(papers)} papers · {a.checks} checks · "
          f"{len(cache)} registrations · {len(annot)} local annotation(s)"
          + ("" if args.pdf else "   [--pdf not given: bylines not re-verified]"))

    if a.problems:
        print(f"\naudit: {len(a.problems)} PROBLEM(S) — ours to fix\n")
        for m in a.problems:
            print(f"  ✗ {m}")
    else:
        print("\naudit: no problems")

    shown = a.notes if args.verbose else a.notes[:40]
    if a.notes:
        print(f"\naudit: {len(a.notes)} note(s) — upstream/publisher facts, for "
              f"reports/upstream_findings.md (§2.2)\n")
        for m in shown:
            print(f"  · {m}")
        if len(shown) < len(a.notes):
            print(f"  … {len(a.notes) - len(shown)} more (-v for all)")

    if a.problems:
        return 1
    return 1 if (args.strict and a.notes) else 0


if __name__ == "__main__":
    sys.exit(main())
