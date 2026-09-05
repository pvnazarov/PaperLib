#!/usr/bin/env python3
"""Every area -> index/registry.json + dist/index.html — the front door.

Two outputs, both DERIVED and both safe to delete:

  index/registry.json   sha256 -> the areas holding those bytes, rebuilt by
                        scanning every area's meta/. It is a published fact, never
                        a source: anything that needs to know whether a paper is
                        already held rescans the sidecars, because a registry that
                        is written to incrementally drifts from them silently.
  dist/index.html       one card per area with its counts, linking into the
                        per-area pages that `make render` produced.

Same constraints as the area pages (CLAUDE.md): no framework, no CDN, no web
fonts, no network, works over file://. Standard library only.
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402


def area_stats(area: str) -> dict:
    """What an area's own build says about it. Never recomputed here.

    An area that has never been built reports as such rather than as empty: zero
    papers and "not built yet" are different states and the portal must not
    render them the same way.
    """
    root = paperlib.area_path(area)
    cfg = {}
    pj = root / "project.json"
    if pj.exists():
        cfg = {k: v for k, v in json.loads(pj.read_text(encoding="utf-8")).items()
               if not k.startswith("_")}
    st = {"area": area, "name": cfg.get("name", area), "tagline": cfg.get("tagline", ""),
          "site_dir": cfg.get("site_dir", f"paperlib/{area}"),
          "sidecars": len(list((root / "meta").glob("*.md"))),
          "sources": sum(1 for f in (root / "raw").iterdir() if f.is_file()
                         and not f.name.startswith(".")) if (root / "raw").is_dir() else 0,
          "built": False, "papers": None, "topics": None, "parts": None,
          "data_as_of": None, "has_map": False, "pending": 0}

    st["pending"] = sum(1 for f in (root / "meta").glob("*.md")
                        if "status: prose-pending" in f.read_text(
                            encoding="utf-8", errors="replace"))

    lib = root / "data" / "library.json"
    if lib.exists():
        d = json.loads(lib.read_text(encoding="utf-8"))
        st["built"] = True
        st["papers"] = len(d.get("papers", []))
        st["data_as_of"] = d.get("data_as_of")
        topics = {p.get("topic") for p in d.get("papers", []) if p.get("topic")}
        st["topics"] = len(topics)
        st["parts"] = len({p.get("part") for p in d.get("papers", []) if p.get("part")})
    st["has_map"] = (root / "data" / "similarity.json").exists()
    return st


CSS = """
:root{--bg:#f7f7f8;--panel:#fff;--ink:#16181d;--muted:#5c6270;--line:#d9dce3;
--accent:#2f63e0;--warn-ink:#a34a11;--warn-bg:#fdf3e3;--warn-line:#d79b31;
--shadow:0 1px 2px rgba(16,18,24,.06),0 6px 16px rgba(16,18,24,.05);
--font:system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme='light']){
--bg:#14161a;--panel:#1b1e24;--ink:#e8eaf0;--muted:#9aa1b1;--line:#2b3038;
--accent:#7aa2f7;--warn-ink:#e8b866;--warn-bg:#2a2318;--warn-line:#6b5528;
--shadow:0 1px 2px rgba(0,0,0,.3),0 6px 16px rgba(0,0,0,.25)}}
:root[data-theme='dark']{--bg:#14161a;--panel:#1b1e24;--ink:#e8eaf0;--muted:#9aa1b1;
--line:#2b3038;--accent:#7aa2f7;--warn-ink:#e8b866;--warn-bg:#2a2318;--warn-line:#6b5528;
--shadow:0 1px 2px rgba(0,0,0,.3),0 6px 16px rgba(0,0,0,.25)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 var(--font)}
.wrap{max-width:52rem;margin:0 auto;padding:3rem 1.25rem 4rem}
h1{font-size:1.7rem;margin:0 0 .3rem;letter-spacing:-.01em}
.sub{color:var(--muted);margin:0 0 2rem}
.grid{display:grid;gap:1rem;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr))}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;
padding:1.1rem 1.2rem;box-shadow:var(--shadow);text-decoration:none;color:inherit;display:block}
a.card:hover{border-color:var(--accent)}
.card h2{font-size:1.05rem;margin:0 0 .25rem}
.card .tag{color:var(--muted);font-size:.88rem;margin:0 0 .8rem}
.n{font-variant-numeric:tabular-nums;font-weight:600}
.stats{color:var(--muted);font-size:.85rem;margin:0}
.warn{color:var(--warn-ink);background:var(--warn-bg);border:1px solid var(--warn-line);
border-radius:6px;padding:.15rem .45rem;font-size:.8rem;display:inline-block;margin-top:.55rem}
footer{margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--line);
color:var(--muted);font-size:.85rem}
"""


def render_card(st: dict) -> str:
    name = html.escape(st["name"])
    tag = html.escape(st["tagline"])
    if st["built"]:
        stats = (f'<p class="stats"><span class="n">{st["papers"]}</span> papers · '
                 f'<span class="n">{st["topics"]}</span> topics in '
                 f'<span class="n">{st["parts"]}</span> parts'
                 f'{" · map" if st["has_map"] else " · no map yet"}<br>'
                 f'data as of {html.escape(st["data_as_of"] or "unknown")}</p>')
        inner = f'<h2>{name} →</h2><p class="tag">{tag}</p>{stats}'
        if st["pending"]:
            inner += (f'<span class="warn">{st["pending"]} awaiting prose</span>')
        return f'<a class="card" href="{html.escape(st["area"])}/">{inner}</a>'
    # Not built is not the same as empty, and must not look like it.
    stats = (f'<p class="stats"><span class="n">{st["sources"]}</span> sources, '
             f'<span class="n">{st["sidecars"]}</span> sidecars — not built yet</p>')
    return (f'<div class="card"><h2>{name}</h2><p class="tag">{tag}</p>{stats}'
            f'<span class="warn">run: make update AREA={html.escape(st["area"])}</span></div>')


def main() -> int:
    areas = paperlib.list_areas()
    if not areas:
        paperlib.die("no areas yet. Create one: python3 scripts/new_area.py <name> --apply")

    reg = paperlib.scan_all_areas(paperlib.frontmatter_parser())
    shared = {sha: r for sha, r in reg.items() if len(r["areas"]) > 1}
    paperlib.INDEX.mkdir(parents=True, exist_ok=True)
    (paperlib.INDEX / "registry.json").write_text(
        json.dumps({"areas": areas, "papers": reg}, indent=2,
                   ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")

    stats = [area_stats(a) for a in areas]
    cfg = paperlib.load_config()
    title = html.escape(cfg.get("name", "PaperLib"))
    total = sum(s["papers"] or s["sidecars"] for s in stats)

    shared_line = ""
    if shared:
        shared_line = (f' · <span class="n">{len(shared)}</span> held in more than '
                       f'one area')

    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{CSS}</style></head><body>
<div class="wrap">
<h1>{title}</h1>
<p class="sub">{len(areas)} area{"s" if len(areas) != 1 else ""} ·
<span class="n">{total}</span> papers{shared_line}</p>
<div class="grid">
{chr(10).join(render_card(s) for s in stats)}
</div>
<footer>
Each area is a separate collection with its own topics and its own similarity map.
The summaries are paraphrases written by reading the papers, not quotations, and
this is not a source: every record links the paper itself.
</footer>
</div></body></html>
"""
    paperlib.DIST.mkdir(parents=True, exist_ok=True)
    out = paperlib.DIST / "index.html"
    out.write_text(doc, encoding="utf-8")
    print(f"portal: {len(areas)} areas, {len(reg)} distinct papers, "
          f"{len(shared)} held in more than one area")
    print(f"portal: -> index/registry.json, dist/index.html ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
