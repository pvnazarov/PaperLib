#!/usr/bin/env python3
"""src/ + data/library.json  ->  dist/

Substitutes the placeholders in src/index.html and copies the static assets. The
index is EMBEDDED in the page (not fetched) because fetch() is blocked over
file://, and CLAUDE.md §8.1 requires the page to work from a clean directory with
no server and no network.

    python3 scripts/render.py [--pdf-base pdf/]

Standard library only. Deterministic: same inputs -> byte-identical dist/.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  -- for load_project() only; one source of truth for it

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

# PAPERLIB: the DATA and the DIST are the area's; src/ is SHARED — one page
# template for every area, so a fix to app.js reaches all of them at once.
ROOT = paperlib.resolve_root()
SRC, DATA, DIST = paperlib.PROJECT / "src", ROOT / "data", ROOT / "dist"
load_project = build.load_project

# Fields the page never reads. Dropping them is not cosmetic: `abstract` is the
# more-derived text (two steps from the source, where `summary` is one -- see
# CLAUDE.md §7), and the page shows the summary, so shipping both would put 60 KB
# of unread prose in front of every visitor. `_hay` is built in the browser.
# `abstract` is the more-derived text (two steps from the source where `summary` is
# one -- CLAUDE.md §7) and the page shows the summary, so shipping both would put
# 60 KB of unread prose in front of every visitor. `duplicate_of_area` was dropped
# by D6: the owner judged "also in AI" useless to a reader, and the page no longer
# renders it. It stays in library.json -- this only stops shipping it.
# `abstract` is the more-derived text (two steps from the source where `summary` is
# one -- CLAUDE.md §7) and the page shows the summary, so shipping both would put
# 60 KB of unread prose in front of every visitor. `duplicate_of_area` went with D6
# and `provenance` with D5+D7: the page neither browses nor displays them any more,
# so shipping them would be dead weight in front of every visitor. BOTH REMAIN IN
# library.json -- this only stops them being sent to the browser, and restoring
# either is a one-line change here.
# `topic_source` went the way of `provenance` on 2026-09-03: the owner's point is
# that the literature review's own topics are machine-assigned too ("same
# model"), so telling a reader which of two machine assignments they are looking
# at informs nothing. IT STAYS IN library.json, and not only for symmetry --
# scripts/score_eval.py pins the pre-registered eval pool to
# `topic_source == "review"`, so deleting the field would silently move every
# number in ADR 0004. The build report still prints the two counts, because the
# OPERATOR does need to know a review regeneration is owed.
DROP_FIELDS = ("abstract", "review_summary", "duplicate_of_area", "provenance",
               "topic_source")


def esc(s: str) -> str:
    """These are substituted into HTML. A name with an `&` or a `<` in it must not
    be able to break the page or, worse, inject markup -- project.json is a local
    file, but so is every file that ever carried a surprise."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def contact_line(cfg: dict) -> str:
    name, mail = cfg.get("contact_name") or "", cfg.get("contact_email") or ""
    if name and mail:
        return f'For any issue contact <a href="mailto:{esc(mail)}">{esc(name)}</a>'
    if mail:
        return f'For any issue write to <a href="mailto:{esc(mail)}">{esc(mail)}</a>'
    if name:
        return f"For any issue contact {esc(name)}."
    return ""


def die(msg: str) -> None:
    print(f"render: FATAL: {msg}", file=sys.stderr)
    sys.exit(1)


def slim(lib: dict) -> dict:
    """Everything the page reads, and nothing else."""
    out = dict(lib)
    out["papers"] = [
        {k: v for k, v in p.items() if k not in DROP_FIELDS and v not in (None, [], "")}
        for p in lib["papers"]
    ]
    return out


DIGEST_GLOB = "*_reading_digest.md"


def newest_digest() -> Path | None:
    """The newest reading digest in outputs/, or None.

    Optional by design, like the map: a collection that has never run
    `make digest` renders a page with no link rather than failing.
    """
    got = sorted((ROOT / "outputs").glob(DIGEST_GLOB))
    return got[-1] if got else None


def digest_link() -> str:
    d = newest_digest()
    if not d:
        return ""
    return ('<p class="digest"><a href="' + esc(d.name) + '">Reading digest</a> '
            '<span>every cluster, then every paper in full &mdash; summary, key '
            'points and limitations</span></p>')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-base", default="pdf/",
                    help="URL prefix under which the source files are served "
                         "(default: pdf/, the symlink deploy.sh makes -- D4)")
    args = ap.parse_args()

    lib_path = DATA / "library.json"
    if not lib_path.exists():
        die("data/library.json not found -- run `make build` first.")
    lib = json.loads(lib_path.read_text(encoding="utf-8"))
    papers = lib["papers"]

    tpl_path = SRC / "index.html"
    if not tpl_path.exists():
        die(f"{tpl_path} not found.")
    tpl = tpl_path.read_text(encoding="utf-8")

    # Cache-busting, because a deploy that a browser ignores is not a deploy.
    # nginx serves app.js with an ETag and a browser may hold the old one for a
    # long time; the owner hit exactly this on 2026-09-03, reporting a change as
    # missing when it had shipped. The query string is a hash of the file's own
    # bytes, so it changes when and only when the file does -- and an unchanged
    # rebuild still produces a byte-identical index.html (§10).
    def asset_v(name: str) -> str:
        return hashlib.sha256((SRC / name).read_bytes()).hexdigest()[:10]

    payload = slim(lib)
    # Nothing reads the colleague tally since D5 removed sharer browsing. Kept in
    # library.json, not shipped to the page.
    payload.pop("colleagues", None)

    # similarity.json is embed.py's output and is OPTIONAL: the page degrades to
    # no map and no neighbour lists rather than failing, because `make update` must
    # work on a clone where `make embed` has never run (P4 came after P3).
    sim_path = DATA / "similarity.json"
    sim = None
    if sim_path.exists():
        sim = json.loads(sim_path.read_text(encoding="utf-8"))
        if sim.get("data_as_of") != lib.get("data_as_of"):
            print(f"render: WARNING -- similarity.json is for data_as_of "
                  f"{sim.get('data_as_of')!r} but library.json is "
                  f"{lib.get('data_as_of')!r}. Run `make embed`.")
        missing = [p["id"] for p in papers if p["id"] not in sim.get("papers", {})]
        if missing:
            print(f"render: WARNING -- {len(missing)} paper(s) have no coordinates; "
                  f"they will not appear on the map. Run `make embed`.")
    payload["similarity"] = sim

    cfg = load_project()
    # The page needs the name at RUNTIME too -- document.title changes as the
    # reader moves between the list, the map and a record -- so it travels in the
    # payload as well as in the template.
    payload["project"] = {"name": cfg["name"]}

    # A `</script>` inside the JSON would end the host <script> block early. Only
    # `<` needs escaping to prevent it, and < is valid JSON, so the browser's
    # JSON.parse restores it verbatim.
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")

    n_authors = sum(1 for p in papers if p.get("authors"))
    subs = {
        "__LIBRARY_JSON__": blob,
        "__PROJECT_NAME__": esc(cfg["name"]),
        "__PROJECT_TAGLINE__": esc(cfg["tagline"]),
        "__PROJECT_SUBTITLE__": esc(cfg["subtitle"]),
        "__FOOTER_SCOPE__": esc(cfg["footer_scope"]),
        # The whole sentence, or nothing. A collection with no contact configured
        # otherwise shipped a footer ending "For any issue contact " followed by an
        # empty link -- seen on the first render of a fresh instance.
        "__CONTACT__": contact_line(cfg),
        "__UPLINK_LABEL__": esc(cfg["uplink_label"]),
        "__UPLINK_HREF__": esc(cfg["uplink_href"]),
        "__PDF_BASE__": args.pdf_base,
        "__CSS_V__": asset_v("app.css"),
        "__JS_V__": asset_v("app.js"),
        "__DATA_AS_OF__": lib["data_as_of"],
        "__REVIEW_FILE__": lib["review_file"],
        "__N_PAPERS__": str(len(papers)),
        "__N_TOPICS__": str(sum(len(part["topics"]) for part in lib["taxonomy"])),
        "__N_OWN__": str(sum(1 for p in papers if p.get("own"))),
        "__N_JOURNALS__": str(len({p["venue"] for p in papers if p.get("venue")})),
        "__N_AUTHORS_TOTAL__": str(len({a for p in papers for a in (p.get("authors") or [])})),
        "__DIGEST_LINK__": digest_link(),
    }
    html = tpl
    for k, v in subs.items():
        html = html.replace(k, v)

    # A placeholder that survived means a template edit added one that render.py
    # does not know about -- which would ship a literal `__N_FOO__` to the page.
    left = sorted(set(re.findall(r"__[A-Z_]+__", html)))
    if left:
        die(f"unsubstituted placeholder(s) in the template: {', '.join(left)}")

    DIST.mkdir(exist_ok=True)
    (DIST / "index.html").write_text(html, encoding="utf-8")
    for name in ("app.css", "app.js"):
        shutil.copyfile(SRC / name, DIST / name)
    # The digest is COPIED into dist/ rather than linked across to outputs/,
    # because §2.7 requires the page to work from a clean directory over file://
    # -- a link to ../outputs/ would resolve on the deployed site and 404 for
    # anyone handed the folder. dist/ is therefore three files plus the digest
    # when one exists, which is what makes the link safe to ship.
    d = newest_digest()
    for stale in DIST.glob(DIGEST_GLOB):
        # Otherwise every regeneration under a new date leaves the previous one
        # behind, and a reader handed the folder can open a digest that is not the
        # one the page links.
        if not d or stale.name != d.name:
            stale.unlink()
    if d:
        shutil.copyfile(d, DIST / d.name)

    total = sum(f.stat().st_size for f in DIST.iterdir() if f.is_file())
    print(f"render: dist/index.html  {(DIST / 'index.html').stat().st_size / 1024:.0f} KB "
          f"(index {len(blob) / 1024:.0f} KB embedded)")
    print(f"render: dist/app.css {(DIST / 'app.css').stat().st_size / 1024:.0f} KB · "
          f"dist/app.js {(DIST / 'app.js').stat().st_size / 1024:.0f} KB")
    print(f"render: {total / 1024:.0f} KB total · {len(papers)} papers · "
          f"pdf base {args.pdf_base!r}")
    if sim:
        placed = sum(1 for p in papers if p["id"] in sim["papers"])
        links = sum(len(v["near"]) for v in sim["papers"].values())
        print(f"render: map tier {sim['tier']} · layout v{sim['layout_version']} · "
              f"{placed} placed · {links} neighbour links")
    else:
        print("render: no data/similarity.json -- no map, no neighbour lists "
              "(run `make embed`)")
    if n_authors < len(papers):
        print(f"render: note -- {len(papers) - n_authors} paper(s) have no author list; "
              f"`make audit` says why for each -- some are permanent (D2)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
