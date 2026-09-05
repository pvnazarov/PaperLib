#!/usr/bin/env python3
"""Score a set of vectors against eval/expectations.json. No hand-scoring.

    .venv/bin/python scripts/score_eval.py                 # the shipped vectors
    .venv/bin/python scripts/score_eval.py --vecs a.npz --label "tier 1"
    .venv/bin/python scripts/score_eval.py --compare a.npz b.npz

WHY THIS EXISTS. ADR 0002 scored Tier 0 by hand from printed output, and recorded
the problem with that honestly: two seeds were judged too strictly, and the ADR's
own instruction was that a fairer set be committed BEFORE the next embedder ran.
Hand-scoring also means the person who built the model decides what counts as a
hit after seeing its answers. This removes that: the expectations are committed
JSON, and this file is the only thing that turns neighbours into a number.

THE POOL IS PINNED TO A REVIEW FILE, not to a predicate. It is the 234 papers the
`2026-08-06` review covers -- the corpus these expectations were written against,
and the one ADR 0004's Tier 0 vs Tier 1 numbers were measured on. The 2026-09-04
review files all 338, so a predicate would have grown the pool on its own and
moved every one of those numbers; `pool_review` in the spec prevents that. See
scored_pool() for what happened when it did. How many unfiled papers a tier would
surface from the full corpus is reported separately, because a large difference
there is itself a finding.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  -- to resolve the pinned pool by re-parsing its review

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

# PAPERLIB: ROOT is the AREA being worked on (scripts/paperlib.py).
ROOT = paperlib.resolve_root()
DATA, EVAL, OUTPUTS = ROOT / "data", ROOT / "eval", ROOT / "outputs"


def load_vectors(path: Path, papers: list[dict]) -> np.ndarray:
    z = np.load(path, allow_pickle=True)
    by = {s: v for s, v in zip(z["sha"], z["vec"])}
    missing = [p["source"] for p in papers if p["sha256"] not in by]
    if missing:
        raise SystemExit(f"score_eval: {len(missing)} paper(s) have no vector in "
                         f"{path.name}, e.g. {missing[0]!r}")
    V = np.array([by[p["sha256"]] for p in papers], dtype=float)
    n = np.linalg.norm(V, axis=1, keepdims=True)
    return V / np.where(n == 0, 1, n)


def pinned_topics(papers: list, spec: dict) -> dict:
    """source -> topic AS THE PINNED REVIEW ASSIGNS IT, not as the newest one does.

    The pool was pinned first, and that was only half the job. Every `hit_topics`,
    `must_not_topics` and `no_credit_topics` clause in the expectation file is
    written as a TOPIC NAME from the 2026-08-06 taxonomy. The 2026-09-04
    re-clustering split, renamed and retired topics, so four of those clauses
    stopped resolving and this scorer refused to run -- correctly, since it
    refuses on any topic not in the corpus rather than scoring it as a miss.

    The wrong fix would be to rewrite the clauses to match the new taxonomy: that
    is editing the ground truth after seeing the model's answers, which is the
    whole thing pre-registration exists to prevent. So the LABELS come from the
    pinned review as well. The scored evaluation is then entirely a function of
    one committed file, and no future re-clustering can move ADR 0004's numbers.
    """
    want = spec.get("pool_review")
    if not want:
        return {p["source"]: p.get("topic") for p in papers}
    path = OUTPUTS / want
    if not path.exists():
        return {p["source"]: p.get("topic") for p in papers}
    bib, _, _ = build.parse_review(path)
    return {src: rec.get("topic") for src, rec in bib.items()}


def scored_pool(papers: list, spec: dict) -> tuple[list, str]:
    """The scored pool, pinned to the REVIEW FILE the expectations were written for.

    This was `topic_source == "review"` and that is no longer the same thing.
    The reasoning was right and the implementation only looked right: a curated
    topic (§6.6) does not count as filed, so the predicate kept the pool at the
    234 papers the 2026-08-06 review covers, exactly as the pre-registration says.

    Then on 2026-09-04 a review covering all 338 was installed, every paper became
    `topic_source == "review"`, and the pool silently grew to 338 -- the precise
    failure §6.6 warned about, arriving by the one route it did not anticipate.
    Measured: Tier 0 went 38/55 -> 37/55 with no vector changed. That is not a
    regression, it is a different question being asked, and ADR 0004's numbers
    stop being comparable the moment it happens.

    So the pool is now pinned to a FILE, not to a predicate: the review named in
    `pool_review` is re-parsed and its `[src]` list IS the pool. `outputs/` is
    add-only (D0), so that file does not go away, and the pin holds across any
    number of future regenerations.
    """
    want = spec.get("pool_review")
    if want:
        path = OUTPUTS / want
        if path.exists():
            bib, _, _ = build.parse_review(path)
            srcs = set(bib)
            return [i for i, p in enumerate(papers) if p["source"] in srcs], want
        print(f"score_eval: WARNING -- pool_review {want!r} is not in outputs/. "
              f"Falling back to `topic_source == 'review'`, which is the CURRENT "
              f"review's pool and is NOT comparable to ADR 0004.", file=sys.stderr)
    return ([i for i, p in enumerate(papers) if p.get("topic_source") == "review"],
            "topic_source == 'review'")


def score(papers: list[dict], V: np.ndarray, spec: dict) -> dict:
    by_id = {p["id"]: i for i, p in enumerate(papers)}
    filed = scored_pool(papers, spec)[0]
    topic_of = pinned_topics(papers, spec)
    k = spec["k"]
    out = {"per_seed": [], "hits": 0, "max": 0, "violations": 0, "unfiled_slots": 0}

    for s in spec["seeds"]:
        i = by_id.get(s["id"])
        if i is None:
            out["per_seed"].append({"name": s["name"], "error": "seed not in corpus"})
            continue
        out["max"] += k

        # --- the scored ranking: filed papers only, identical pool per tier ---
        pool = [j for j in filed if j != i]
        sims = V[i] @ V[pool].T
        order = [pool[j] for j in np.argsort(-sims)[:k]]

        hit_t = set(s.get("hit_topics", []))
        bad_t = set(s.get("must_not_topics", []))
        none_t = set(s.get("no_credit_topics", []))
        rows, hits, viol = [], 0, []
        for j in order:
            topic = topic_of.get(papers[j]["source"])
            if topic in bad_t:
                verdict = "MUST-NOT"
                viol.append(papers[j]["title"])
            elif topic in none_t:
                verdict = "no credit"
            elif topic in hit_t:
                verdict = "hit"
                hits += 1
            else:
                verdict = "miss"
            rows.append({"sim": float(V[i] @ V[j]), "title": papers[j]["title"],
                         "topic": topic, "verdict": verdict})

        rank1_ok = None
        if s.get("rank1_id"):
            rank1_ok = bool(order) and papers[order[0]]["id"] == s["rank1_id"]
        min_ok = None
        if s.get("min_hits") is not None:
            min_ok = hits >= s["min_hits"]

        # --- how many unfiled papers the FULL corpus would have put in the top k
        full = [j for j in range(len(papers)) if j != i]
        fsims = V[i] @ V[full].T
        forder = [full[j] for j in np.argsort(-fsims)[:k]]
        unfiled = sum(1 for j in forder if not topic_of.get(papers[j]["source"]))
        out["unfiled_slots"] += unfiled

        out["hits"] += hits
        out["violations"] += 1 if viol else 0
        out["per_seed"].append({
            "name": s["name"], "hits": hits, "k": k, "rows": rows,
            "violations": viol, "rank1_ok": rank1_ok, "min_ok": min_ok,
            "unfiled_in_full_topk": unfiled,
            "full_topk": [{"sim": float(V[i] @ V[j]), "title": papers[j]["title"],
                           "topic": topic_of.get(papers[j]["source"])} for j in forder],
        })
    return out


def c1(papers: list[dict], V: np.ndarray) -> tuple[float, float, float]:
    """Circulator leakage: same-sharer mean cosine vs the overall mean."""
    groups: dict[str, list[int]] = {}
    for i, p in enumerate(papers):
        for who in (p.get("provenance") or {}).get("sharers", []) or []:
            groups.setdefault(who, []).append(i)
    same = []
    for idx in groups.values():
        for a in range(len(idx)):
            for b in range(a + 1, len(idx)):
                same.append(float(V[idx[a]] @ V[idx[b]]))
    S = V @ V.T
    iu = np.triu_indices(len(papers), 1)
    overall = float(S[iu].mean())
    m = float(np.mean(same)) if same else float("nan")
    return m, overall, m - overall


def c1_topic_controlled(papers: list[dict], V: np.ndarray) -> tuple[float, float, int, int]:
    """Does sharing a circulator still matter once SUBJECT is held fixed?

    POST HOC, and labelled as such wherever it is printed. The pre-registered C1
    is an absolute delta on the mean cosine, calibrated on Tier 0, whose pairwise
    cosines average 0.048. A sentence encoder's average 0.20-0.77, so the same
    absolute delta means something completely different -- and eval/queries.md
    already conceded that *some* excess is legitimate, "because colleagues have
    subject interests, so one person's papers really are more alike than random".

    This measures the part that is NOT that: among pairs already sharing a topic,
    the extra similarity from also sharing a circulator. That is the quantity C1
    was always trying to get at.
    """
    S = V @ V.T
    same_t, same_tc = [], []
    n = len(papers)
    sh = [set((p.get("provenance") or {}).get("sharers", []) or []) for p in papers]
    tp = [p.get("topic") if p.get("topic_source") == "review" else None
          for p in papers]
    for i in range(n):
        if not tp[i]:
            continue
        for j in range(i + 1, n):
            if tp[j] != tp[i]:
                continue
            (same_tc if (sh[i] & sh[j]) else same_t).append(S[i, j])
    if not same_t or not same_tc:
        return float("nan"), float("nan"), len(same_t), len(same_tc)
    a, b = np.array(same_t), np.array(same_tc)
    ex = float(b.mean() - a.mean())
    return ex, ex / float(a.std()), len(a), len(b)


def purity(coords: np.ndarray, labels: list, k: int = 6, cos: bool = False) -> float:
    keep = np.array([bool(x) for x in labels])
    if keep.sum() <= k:
        return float("nan")
    c, lab = coords[keep], np.array(labels, dtype=object)[keep]
    if cos:
        s = c @ c.T
        np.fill_diagonal(s, -np.inf)
        nb = np.argsort(-s, axis=1)[:, :k]
    else:
        d = ((c[:, None, :] - c[None, :, :]) ** 2).sum(-1)
        np.fill_diagonal(d, np.inf)
        nb = np.argsort(d, axis=1)[:, :k]
    return float(np.mean([(lab[nb[i]] == lab[i]).mean() for i in range(len(lab))]))


def chance(labels: list) -> float:
    """P(two distinct labelled papers share a label) under random pairing.

    sum_i n_i(n_i-1) / N(N-1) over the label classes -- the null a purity figure
    has to be read against, and it depends on how many classes there are and how
    unevenly they are filled. Both change every time the taxonomy does.
    """
    from collections import Counter
    c = Counter(x for x in labels if x)
    N = sum(c.values())
    if N < 2:
        return float("nan")
    return sum(n * (n - 1) for n in c.values()) / (N * (N - 1))


def report(label: str, res: dict, papers: list[dict], V: np.ndarray, verbose: bool) -> None:
    print("=" * 78)
    print(f"{label}   {res['hits']} / {res['max']} hits · "
          f"{res['violations']} seed(s) violating a must-not clause")
    print("=" * 78)
    for s in res["per_seed"]:
        if "error" in s:
            print(f"  !! {s['name']}: {s['error']}")
            continue
        extra = []
        if s["rank1_ok"] is not None:
            extra.append("rank-1 " + ("MET" if s["rank1_ok"] else "FAILED"))
        if s["min_ok"] is not None:
            extra.append("own bar " + ("met" if s["min_ok"] else "MISSED"))
        if s["violations"]:
            extra.append(f"MUST-NOT x{len(s['violations'])}")
        tail = ("   [" + " · ".join(extra) + "]") if extra else ""
        print(f"  {s['hits']}/{s['k']}  {s['name']}{tail}")
        if verbose:
            for r in s["rows"]:
                print(f"        {r['sim']:.3f}  {r['verdict']:<9} {r['title'][:52]}")
                print(f"               topic: {r['topic']}")
    m, o, ex = c1(papers, V)
    gate = "PASS" if ex <= 0.005 else "FAIL"
    sd = float(np.std((V @ V.T)[np.triu_indices(len(papers), 1)]))
    print(f"\n  C1 (the GATE, pre-registered): same {m:.4f} · overall {o:.4f} · "
          f"excess {ex:+.4f}  -- {gate} against <= +0.005")
    print(f"     scale-free effect size d = {ex / sd:+.3f}   (excess / sd of all "
          f"pairwise cosines, sd = {sd:.4f})")
    tex, td, na, nb = c1_topic_controlled(papers, V)
    print(f"  C1 topic-controlled (POST HOC, not the gate): among pairs already "
          f"sharing a topic,")
    print(f"     also sharing a circulator adds {tex:+.4f}, d = {td:+.3f}  "
          f"({nb} vs {na} pairs)")
    print(f"  C3 purity (DIAGNOSTIC, no pre-committed criterion):")
    rev = [p.get("topic_source") == "review" for p in papers]
    part = [p.get("part_letter") if r else None for p, r in zip(papers, rev)]
    topic = [p.get("topic") if r else None for p, r in zip(papers, rev)]
    # Chance is COMPUTED, not quoted. It was hardcoded at `0.146 / 0.039`, which
    # was right for the label distribution of the day -- 234 labelled papers over
    # 8 parts and 31 topics. The 2026-09-04 review labels all 338 over 9 parts and
    # 39 topics, so both baselines moved and the printed pair silently became a
    # comparison against the wrong nulls. A purity figure next to a stale chance
    # line is worse than no chance line: it reads as calibrated and is not.
    print(f"     full space: part {purity(V, part, cos=True):.3f} · "
          f"topic {purity(V, topic, cos=True):.3f}   "
          f"(chance {chance(part):.3f} / {chance(topic):.3f}, "
          f"computed over {sum(1 for x in part if x)} labelled)")
    print(f"  unfiled papers in the full-corpus top-5, summed over seeds: "
          f"{res['unfiled_slots']} of {res['max']}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vecs", default=str(DATA / "embed_cache.npz"))
    ap.add_argument("--label", default=None)
    ap.add_argument("--compare", nargs=2, metavar=("A", "B"))
    ap.add_argument("-v", "--verbose", action="store_true")
    ap.add_argument("--json", help="write the full result to this path")
    args = ap.parse_args()

    spec = json.loads((EVAL / "expectations.json").read_text(encoding="utf-8"))
    papers = json.loads((DATA / "library.json").read_text(encoding="utf-8"))["papers"]

    # An id that matches nothing is a TYPO, not a failed expectation. Scoring it
    # as a miss is how a mistyped `rank1_id` came to look like a model defect;
    # the whole point of a pre-registered file is that it is checked, not
    # trusted. Same for the topic names -- a renamed topic upstream must break
    # loudly rather than quietly score zero.
    ids = {p["id"] for p in papers}
    # Validated against the PINNED review's taxonomy, because that is what the
    # clauses are written in and what score() now judges against. Checking them
    # against the newest review's topics is what made this refuse to run after
    # the 2026-09-04 re-clustering.
    topics = {t for t in pinned_topics(papers, spec).values() if t}
    problems = []
    for s in spec["seeds"]:
        if s["id"] not in ids:
            problems.append(f"seed id not in the corpus: {s['id']!r}")
        if s.get("rank1_id") and s["rank1_id"] not in ids:
            problems.append(f"rank1_id not in the corpus: {s['rank1_id']!r} "
                            f"(seed {s['name']!r})")
        for key in ("hit_topics", "must_not_topics", "no_credit_topics"):
            for name in s.get(key, []):
                if name not in topics:
                    problems.append(f"{key} names a topic that does not exist: "
                                    f"{name!r} (seed {s['name']!r})")
    if problems:
        for m in problems:
            print(f"score_eval: FATAL: {m}", file=sys.stderr)
        return 2
    pool_idx, pool_src = scored_pool(papers, spec)
    n_now = sum(1 for p in papers if p.get("topic_source") == "review")
    print(f"score_eval: {len(papers)} papers · scored pool {len(pool_idx)}, pinned to "
          f"{pool_src} · k={spec['k']} · max {len(spec['seeds']) * spec['k']}")
    if n_now != len(pool_idx):
        print(f"score_eval: note -- the CURRENT review files {n_now} papers, but the "
              f"pool stays at {len(pool_idx)} so these numbers remain comparable with "
              f"ADR 0004. A pool of {n_now} is a different question.")
    print()

    runs = []
    if args.compare:
        for path in args.compare:
            runs.append((Path(path).stem, Path(path)))
    else:
        runs.append((args.label or Path(args.vecs).stem, Path(args.vecs)))

    results = []
    for label, path in runs:
        V = load_vectors(path, papers)
        res = score(papers, V, spec)
        report(label, res, papers, V, args.verbose)
        print()
        results.append((label, res, V))

    if len(results) == 2:
        (la, ra, Va), (lb, rb, Vb) = results
        print("=" * 78)
        print(f"HEAD TO HEAD   {la}  vs  {lb}")
        print("=" * 78)
        print(f"  {'seed':<44} {la[:14]:>14} {lb[:14]:>14}")
        for a, b in zip(ra["per_seed"], rb["per_seed"]):
            if "error" in a or "error" in b:
                continue
            fa = f"{a['hits']}/{a['k']}" + (" !" if a["violations"] else "")
            fb = f"{b['hits']}/{b['k']}" + (" !" if b["violations"] else "")
            arrow = "  " if a["hits"] == b["hits"] else ("<-" if a["hits"] > b["hits"] else "->")
            print(f"  {a['name'][:44]:<44} {fa:>14} {fb:>14}  {arrow}")
        print(f"  {'TOTAL':<44} {str(ra['hits']) + '/' + str(ra['max']):>14} "
              f"{str(rb['hits']) + '/' + str(rb['max']):>14}")
        print(f"  {'seeds violating a must-not':<44} {ra['violations']:>14} "
              f"{rb['violations']:>14}")
        print("  ! = that seed violates its must-not clause")

    if args.json:
        Path(args.json).write_text(json.dumps(
            {l: {k: v for k, v in r.items()} for l, r, _ in results},
            indent=1), encoding="utf-8")
        print(f"\nscore_eval: wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
