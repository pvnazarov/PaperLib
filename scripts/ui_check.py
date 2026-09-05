#!/usr/bin/env python3
"""Drive the built page in a real browser and assert what a reader sees.

    make ui                      # against http://localhost/library/  (deploy first)
    python3 scripts/ui_check.py file:///mnt/data/ai/TeamLibrary/dist/index.html

WHY THIS EXISTS, given that `make audit` already checks 5,990 things: audit reads
DATA. It cannot see that a facet is 2,124 px of list behind a 232 px window, or
that a filter is hidden inside a collapsed section, and both of those shipped --
the owner found them, twice (§12). Every check here is a claim about the RENDERED
page, so it can only be made by rendering it.

NOT part of `make update`. `playwright` is pinned in requirements.txt so `make venv`
installs it, but PLAYWRIGHT SHIPS ITS BROWSERS SEPARATELY -- the last ~115 MB is one
more command, kept explicit so a fresh clone that only wants to build the library
never downloads a browser by surprise:

    .venv/bin/playwright install chromium

Both failures are handled by name below, because they look nothing alike: a missing
package fails at import, a missing browser fails at launch with a stack trace.

Exit 1 on any failed check, and print every check either way -- a pass list is
the only way to see that a check still tests what its name says.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

URL_DEFAULT = "http://localhost/library/"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

# PAPERLIB: ROOT is the AREA being worked on (scripts/paperlib.py).
ROOT = paperlib.resolve_root()


def shape() -> dict:
    """What THIS collection looks like, read from the build rather than hardcoded.

    The first version of this file asserted "nine parts", "45 topics" and
    "letters A..I" -- true of one library on one day. Run against a different
    collection it did not report a difference, it CRASHED, clicking for a ninth
    part that was not there. A check that only works on the corpus it was written
    against is not a check of the page; it is a check of the corpus.
    """
    lib = json.loads((ROOT / "data" / "library.json").read_text(encoding="utf-8"))
    tax = lib["taxonomy"]
    return {
        "papers": len(lib["papers"]),
        "parts": len(tax),
        "topics": sum(len(p["topics"]) for p in tax),
        "letters": "".join(p["letter"] for p in tax),
    }


def main() -> int:
    try:
        from playwright.sync_api import Error as PlaywrightError, sync_playwright
    except ImportError:
        print("ui_check: playwright is not installed. It IS pinned in "
              "requirements.txt, so:\n"
              "    make venv        # or: .venv/bin/pip install -r requirements.txt\n"
              "    .venv/bin/playwright install chromium", file=sys.stderr)
        return 2

    url = sys.argv[1] if len(sys.argv) > 1 else URL_DEFAULT
    want = shape()
    oks: list[str] = []
    bad: list[str] = []

    def ck(cond: bool, msg: str) -> None:
        (oks if cond else bad).append(("ok    " if cond else "FAIL  ") + msg)

    with sync_playwright() as pw:
        try:
            br = pw.chromium.launch()
        except PlaywrightError as e:
            if "Executable doesn't exist" not in str(e):
                raise
            print("ui_check: playwright is installed but its Chromium is not -- the "
                  "browsers are a separate download:\n"
                  "    .venv/bin/playwright install chromium", file=sys.stderr)
            return 2
        # 1400x900: TALL enough that the unfiltered view does not already scroll,
        # which is the only viewport in which the map's height feedback loop (§12)
        # is visible at all.
        pg = br.new_page(viewport={"width": 1400, "height": 900})
        errs: list[str] = []
        pg.on("console", lambda m: errs.append(m.type + ": " + m.text)
              if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
        pg.goto(url, wait_until="load")
        pg.wait_for_timeout(600)
        ck(not errs, "the page loads with no console errors"
                     + ("" if not errs else " -> " + "; ".join(errs[:4])))

        def topic_facet():
            # Re-located on purpose after anything that re-renders: renderSidebar()
            # rebuilds the <details> from scratch, so a held handle is a stale node.
            return pg.locator("details.facet",
                              has=pg.locator("summary", has_text="Topic")).first

        tf = topic_facet()
        ck(tf.count() > 0, "the Topic facet is present")
        badge = tf.locator("> summary .facetn").first.inner_text().strip()
        ck(badge == str(want["topics"]),
           "its summary counts all %d topics while shut (got %r)"
           % (want["topics"], badge))
        ck(not tf.evaluate("d => d.open"), "it starts closed (D12)")
        tf.locator("> summary").click()
        pg.wait_for_timeout(150)
        ck(tf.evaluate("d => d.open"), "and opens on a click")

        parts = tf.locator(".part")
        ck(parts.count() == want["parts"],
           "it holds %d collapsible part(s), one per part of the taxonomy (got %d)"
           % (want["parts"], parts.count()))
        ck(tf.evaluate("d => [...d.querySelectorAll('.part')].every(p => !p.open)"),
           "all of them start closed")
        letters = "".join(n[0] for n in tf.evaluate(
            "d => [...d.querySelectorAll('.part summary .part-name')].map(e => e.textContent)"))
        ck(letters == want["letters"],
           "part letters %r, in the taxonomy's own order (got %r)"
           % (want["letters"], letters))
        ck(tf.evaluate("""d => [...d.querySelectorAll('.part')].every(p => {
               var s = p.querySelector('summary .swatch');
               return s && getComputedStyle(s).backgroundColor !== 'rgba(0, 0, 0, 0)';
             })"""),
           "every part carries the map's colour for that part")

        # The whole point of collapsing: the list must fit, not scroll.
        body = tf.locator(".facet-body").first
        h_shut = body.evaluate("e => e.scrollHeight")
        over = body.evaluate("e => e.scrollHeight - e.clientHeight")
        ck(over <= 1, "collapsed, the list is NOT clipped (%d px, every part "
                      "visible at once)" % h_shut)

        allb = tf.locator("button.partall")
        ck(allb.inner_text().strip() == "Expand all",
           "the control reads 'Expand all' (got %r)" % allb.inner_text().strip())
        allb.click()
        pg.wait_for_timeout(200)
        tf = topic_facet()
        ck(tf.evaluate("d => [...d.querySelectorAll('.part')].every(p => p.open)"),
           "Expand all opens every part -- the whole taxonomy in one gesture")
        h_open = tf.locator(".facet-body").first.evaluate("e => e.scrollHeight")
        ck(h_open > h_shut,
           "and folding is worth doing: %d px open vs %d px shut" % (h_open, h_shut))
        n = tf.locator(".part-body .opt.child").count()
        ck(n == want["topics"], "%d topic buttons, all inside a part (got %d)"
                                % (want["topics"], n))
        ck(tf.locator("button.partall").inner_text().strip() == "Collapse all",
           "the control flips to 'Collapse all'")
        tf.locator("button.partall").click()
        pg.wait_for_timeout(200)
        tf = topic_facet()
        ck(tf.evaluate("d => [...d.querySelectorAll('.part')].every(p => !p.open)"),
           "Collapse all shuts every part")

        # THE check that makes collapsing safe: a filter must never be invisible.
        tf.locator(".part").last.locator("> summary").click()
        pg.wait_for_timeout(150)
        opt = tf.locator(".part").last.locator(".opt.child").first
        picked = opt.locator("span").first.inner_text()
        opt.click()
        pg.wait_for_timeout(300)
        p9 = topic_facet().locator(".part").last
        ck(p9.evaluate("p => p.open"), "a part holding a live filter is open after re-render")
        on = p9.locator("> summary .facetn.on")
        ck(on.count() == 1 and on.inner_text().strip() == "1 on",
           "its summary says '1 on' (got %r)" % (on.inner_text() if on.count() else None))
        ck(p9.evaluate("""p => { var b = p.querySelector('summary .facetn.on');
               return getComputedStyle(b).backgroundColor; }""")
           not in ("rgba(0, 0, 0, 0)", "transparent"),
           "and says it in the accent colour, not as plain grey text")
        p9.locator("> summary").click()
        pg.wait_for_timeout(200)
        ck(not p9.evaluate("p => p.open"),
           "the reader can still close a part that is filtering")
        ck(p9.locator("> summary .facetn.on").is_visible(),
           "and the badge stays visible while it is closed -- so the filter never hides")
        head = pg.locator(".resulthead h2").first.inner_text()
        shown = int(head.split()[0])
        ck(0 < shown < want["papers"],
           "the filter really filtered: %r (topic %r)" % (head, picked))

        # §12 regression: a width-derived height on a page whose height changes.
        #
        # Only if there IS a map. `make embed` is optional -- build + render work
        # with no numpy at all, and that is the documented FIRST path through the
        # runbook. A check that fails on the tool's own supported path is a broken
        # check, and this one did: found by following the runbook from the archive
        # and watching it time out waiting for a canvas that was never going to
        # exist.
        if (ROOT / "data" / "similarity.json").exists():
            pg.locator("button", has_text="Map").first.click()
            pg.wait_for_timeout(500)
            h1 = pg.locator("canvas.map").evaluate(
                "c => c.getBoundingClientRect().height")
            p = topic_facet().locator(".part").last
            p.locator("> summary").click()
            pg.wait_for_timeout(150)
            p.locator(".opt.child").first.click()
            pg.wait_for_timeout(600)
            h2 = pg.locator("canvas.map").evaluate(
                "c => c.getBoundingClientRect().height")
            ck(abs(h1 - h2) < 1,
               "the map keeps its height when filtered: %.0f -> %.0f px" % (h1, h2))
        else:
            ck(pg.locator("canvas.map").count() == 0,
               "no data/similarity.json and no map on the page -- consistent; "
               "map checks skipped (run `make embed` for them)")

        # A short viewport is the one where the .facet-tall clamp bottoms out.
        pg.set_viewport_size({"width": 1400, "height": 700})
        pg.wait_for_timeout(200)
        over = topic_facet().locator(".facet-body").first.evaluate(
            "e => e.scrollHeight - e.clientHeight")
        ck(over <= 1, "at 1400x700 the collapsed list still fits (overflow %d px)" % over)

        br.close()

    for line in oks:
        print(line)
    for line in bad:
        print(line)
    print("\nui_check: %d checks, %d failed  (%s)" % (len(oks) + len(bad), len(bad), url))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)
    sys.exit(main())
