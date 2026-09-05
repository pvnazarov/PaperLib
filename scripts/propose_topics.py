#!/usr/bin/env python3
"""The unfiled papers -> reports/<date>_proposed_topics.md

WHAT THIS IS FOR. Topics come from the literature review upstream (CLAUDE.md D1,
§4.3) and are never invented here. But when a copy brings many papers at once,
the owner has to file them all upstream, and this script makes that cheaper by
saying what the papers themselves cluster into.

WHAT IT IS NOT. It writes ONE file, into reports/. It does not touch
library.json, similarity.json or the page, and nothing downstream reads its
output. If it ever becomes an input to the build, that is a second taxonomy and
D1 has been broken.

    .venv/bin/python scripts/propose_topics.py [-k 10]

Needs `make embed` to have run: it reads the shipped vectors so that its notion
of similarity is exactly the page's.
"""
from __future__ import annotations

import argparse
import collections
import json
import pickle
import statistics
import sys
from pathlib import Path

import numpy as np
from sklearn.cluster import KMeans

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

# PAPERLIB: ROOT is the AREA being worked on (scripts/paperlib.py).
ROOT = paperlib.resolve_root()
DATA, REPORTS = ROOT / "data", ROOT / "reports"

# Accept an existing topic only when the nearest filed neighbour is this close
# AND the winning topic holds this share of the weighted vote.
NEAR, SHARE = 0.40, 0.50
# The taxonomy's own catch-all. eval/queries.md: "a residual, not a subject" --
# so landing here is not being filed, and it is reported separately.
RESIDUAL = "Adjacent to the team's work"
SEED = 20260903


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-k", type=int, default=10, help="clusters for the unplaced papers")
    args = ap.parse_args()

    lib_path = DATA / "library.json"
    cache_path, model_path = DATA / "embed_cache.npz", DATA / "embed_model.pkl"
    for f in (lib_path, cache_path, model_path):
        if not f.exists():
            print(f"propose_topics: {f.relative_to(ROOT)} not found -- run `make update` "
                  f"(and `make embed`) first.", file=sys.stderr)
            return 1

    papers = json.loads(lib_path.read_text(encoding="utf-8"))["papers"]
    z = np.load(cache_path, allow_pickle=True)
    vec = {s: v for s, v in zip(z["sha"], z["vec"])}
    model = pickle.loads(model_path.read_bytes())
    terms = np.array(model["vec"].get_feature_names_out())
    svd = model["svd"]

    unf = [p for p in papers if not p.get("topic")]
    filed = [p for p in papers if p.get("topic")]
    if not unf:
        print("propose_topics: nothing is unfiled -- the review covers every paper. "
              "No report written.")
        return 0
    missing = [p["source"] for p in unf + filed if p["sha256"] not in vec]
    if missing:
        print(f"propose_topics: {len(missing)} paper(s) have no vector; run `make embed`.",
              file=sys.stderr)
        return 1

    V = np.array([vec[p["sha256"]] for p in unf])
    FV = np.array([vec[p["sha256"]] for p in filed])
    S = V @ FV.T

    # ---- does an existing topic fit? similarity-WEIGHTED vote over 5 --------
    # Unweighted, four near-random neighbours outvote one true match at 0.96 --
    # measured: it put a stochastic-systems paper in `Single-cell analysis`,
    # which is a big topic, so random neighbours land there often.
    fits, residual = [], []
    for r, p in enumerate(unf):
        w: dict[str, float] = collections.Counter()
        for j in np.argsort(-S[r])[:5]:
            w[filed[j]["topic"]] += max(float(S[r, j]), 0.0)
        total = sum(w.values()) or 1.0
        win, weight = w.most_common(1)[0]
        if float(S[r].max()) >= NEAR and weight / total >= SHARE:
            (residual if win == RESIDUAL else fits).append(
                (float(S[r].max()), weight / total, win, p))

    placed = {id(p) for *_, p in fits + residual}
    rest = [p for p in unf if id(p) not in placed]

    L = [f"# Proposed topics for the {len(unf)} unfiled papers — a report, not a change", "",
         "> written by `scripts/propose_topics.py`. **Nothing here has been applied.** Topics come",
         "> from the literature review upstream (CLAUDE.md D1, §4.3); this file exists only to make",
         "> regenerating that review cheaper. Nothing in `data/` or on the page reads it.", ""]

    best = S.max(1)
    L += ["## Why the topics cannot just be inferred", "",
          "The obvious idea — read each paper's topic off its nearest filed neighbour — is measured",
          "here, and for most of these papers it fails, because the taxonomy has no topic for them:",
          "", f"| | of {len(unf)} |", "|---|---:|",
          f"| nearest filed neighbour, median cosine | **{statistics.median(best):.3f}** |",
          f"| no filed neighbour above 0.30 at all | **{sum(1 for x in best if x < 0.30)}** |",
          f"| a real existing topic fits (§A) | **{len(fits)}** |",
          f"| only the residual catch-all fits (§B) | {len(residual)} |",
          f"| **needs a topic that does not exist yet** (§C) | **{len(rest)}** |", "",
          f"Accepted for §A/§B when the nearest filed neighbour is ≥ {NEAR:.2f} **and** the winning",
          f"topic holds ≥ {SHARE:.0%} of a similarity-weighted vote over the 5 nearest.", "",
          f"## A. {len(fits)} papers an existing topic already fits", "",
          "| cosine | share | existing topic | paper |", "|---:|---:|---|---|"]
    for s, sh, win, p in sorted(fits, key=lambda x: -x[0]):
        L.append(f"| {s:.3f} | {sh:.0%} | {win} | {p['title'][:66]} |")

    L += ["", f"## B. {len(residual)} papers whose only fit is the residual", "",
          f"These land in **“{RESIDUAL}”**, which `eval/queries.md` calls *\"a residual, not a",
          "subject\"*. Putting them there says only that nothing fits, so treat them as part of §C.",
          "", "| cosine | paper |", "|---:|---|"]
    for s, sh, win, p in sorted(residual, key=lambda x: -x[0]):
        L.append(f"| {s:.3f} | {p['title'][:76]} |")

    L += ["", f"## C. {len(rest)} papers needing new topics", ""]
    if rest:
        RV = np.array([vec[p["sha256"]] for p in rest])
        k = max(1, min(args.k, len(rest)))
        km = KMeans(n_clusters=k, n_init=30, random_state=SEED).fit(RV)
        groups = []
        for c in range(k):
            idx = [i for i, lab in enumerate(km.labels_) if lab == c]
            if not idx:
                continue
            centre = RV[idx].mean(0)
            weights = svd.components_.T @ centre
            top = [t for t in terms[np.argsort(-weights)[:16]]
                   if len(t) > 2 and t not in ("stated", "article")][:7]
            sims = RV[idx] @ FV.T
            lean = collections.Counter(filed[j]["topic"] for j in sims.argmax(1))
            groups.append({
                "idx": idx, "terms": top, "lean": lean.most_common(2),
                "coh": float(np.mean(RV[idx] @ centre / np.linalg.norm(centre))),
                "best": float(sims.max()),
            })
        groups.sort(key=lambda g: -len(g["idx"]))
        L += ["k-means on the vectors the page itself uses. `cohesion` is the mean cosine to the",
              "cluster centre: above ~0.8 one tight subject, near 0.45 a broader area. **The headings",
              "are the weakest thing here** — the terms and the paper lists are the evidence.", ""]
        for n, g in enumerate(groups, 1):
            L += [f"### C{n}. {len(g['idx'])} papers · cohesion {g['coh']:.2f}", "",
                  "**Terms:** " + ", ".join(f"`{t}`" for t in g["terms"]), "",
                  "**Nearest existing topics:** "
                  + ", ".join(f"{t} ({c})" for t, c in g["lean"])
                  + f" — best single cosine {g['best']:.2f}", ""]
            for i in sorted(g["idx"], key=lambda i: rest[i]["title"]):
                p = rest[i]
                L.append(f"- {p['title']}  ·  *{p.get('venue') or 'venue not recorded'}* "
                         f"{p.get('year') or ''}")
            L.append("")

    L += ["## What this file is not", "",
          "Machine clustering of **summaries**, not of papers: two papers can group because they",
          "were summarised in the same vocabulary. It has no view on where a topic sits in the",
          "8-part structure, it cannot tell a topic from a sub-topic, and it does not know which",
          "distinctions the team cares about. It is a draft for someone who does.", ""]

    # Dated from the DATA, never the clock -- same rule as the build (§10).
    stamp = json.loads(lib_path.read_text(encoding="utf-8"))["data_as_of"]
    out = REPORTS / f"{stamp}_proposed_topics.md"
    REPORTS.mkdir(exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"propose_topics: {len(unf)} unfiled · {len(fits)} fit an existing topic · "
          f"{len(residual)} only the residual · {len(rest)} need new ones")
    print(f"propose_topics: -> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
