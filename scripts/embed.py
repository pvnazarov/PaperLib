#!/usr/bin/env python3
"""library.json -> data/similarity.json  (vectors, top-k neighbours, 2D map)

Implements CLAUDE.md §7 and decision D3. Tier 0 = TF-IDF + TruncatedSVD.

    python3 scripts/embed.py                 # incremental: frozen model, new papers only
    python3 scripts/embed.py --refit         # refit everything; bumps model+layout version
    python3 scripts/embed.py --eval          # score against eval/queries.md, no writes
    python3 scripts/embed.py --no-strip      # for the C1 diagnostic only

Ownership: `build.py` owns `data/library.json` and this script never touches it.
This script owns `data/similarity.json`; `render.py` merges the two. A defect in a
summary is still fixed upstream (§2).

Three things here are load-bearing rather than incidental:

  1. NEIGHBOURS ARE COMPUTED IN THE FULL EMBEDDING SPACE, never off the 2D
     coordinates (§7.1 Trap 1). Neighbours read off a projection look plausible and
     are wrong in ways that correlate with where a paper happened to land.
  2. EVERY COORDINATE IS CACHED BY sha256 AND REUSED (§7.1 Trap 2), but the cache
     also stores a hash of the EMBEDDING TEXT and recomputes when that changes.
     Keying on the source sha256 alone was a gap: it detects a new or altered
     PDF, and misses a change in how the text is DERIVED from it. Normalising
     `venue` in build.py changed the embedding input for 19 papers whose source
     bytes were untouched, and a source-keyed cache would have served their old
     vectors forever, silently. Freezing the
     model is necessary but NOT sufficient, which the C2 gate in eval/queries.md
     caught: `umap.transform()` is batch-coupled, so transforming 234 papers gives
     different positions than transforming 233 of the same papers -- measured, the
     pre-existing points moved by up to 3.49 units when one paper was added. A
     frozen model alone would therefore have reshuffled the map on every update,
     exactly the failure Trap 2 describes, while looking like it had been
     prevented. So an existing paper's coordinates are READ FROM CACHE, never
     recomputed, and only genuinely new papers are transformed.
     The TF-IDF vocabulary and IDF weights are frozen for the same reason one
     layer down: refitting them would move every existing vector.
  3. THE CIRCULATION SENTENCES ARE STRIPPED from the input (§7). 138 of 234
     summaries name a colleague, and embedding that makes *who shared a paper* a
     feature of its vector.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pickle
import re
import sys
from pathlib import Path

import numpy as np
import sklearn
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

# PAPERLIB: ROOT is the AREA being worked on (scripts/paperlib.py).
ROOT = paperlib.resolve_root()
DATA = ROOT / "data"
MODEL_PKL = DATA / "embed_model.pkl"
CACHE_NPZ = DATA / "embed_cache.npz"
OUT = DATA / "similarity.json"

SEED = 20260903
N_COMPONENTS = 128
TOP_K = 8
N_SHARED_TERMS = 4

# Below this cosine, a "related paper" is generic methodological vocabulary rather
# than a subject match -- the eval run showed pairs joined by nothing but "machine
# learning", "foundation model" or "real world data". Measured over the 1872 top-8
# links: a 0.25 floor keeps 53% of them and still leaves 228 of 234 papers with at
# least one neighbour, so the six that lose all of theirs genuinely have none, and
# saying so is better than offering a thin one. The UI shows the score and the
# shared terms next to every neighbour, so a weak match stays visibly weak rather
# than being hidden behind this number.
MIN_SIM = 0.25

# ── the circulation sentences ─────────────────────────────────────────────────
#
# Matching on colleague NAMES over-captures badly: "From Tsinghua University ...
# (corresponding authors Wanwen Zeng and Rui Jiang)" contains a colleague's
# surname and is a statement about the paper's authorship, not about how it
# arrived. So match the ACT instead.
#
# Every alternative below is deliberately narrow. In particular `shared` is only
# matched when followed by a provenance preposition, because "shared
# representation", "shared embedding" and "shared terms" are all real subject
# vocabulary in this corpus and must survive.
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
      | (?: the \s+ )? (?: team \s+ )? thread          # "in the team thread"
      | webex
    )\b""",
    re.I | re.X,
)

# Sentence splitter that does not break on an initial-plus-surname ("A. Byron"),
# "et al.", "Fig. 2" or a
# decimal. Splits on .!? followed by whitespace and a capital, unless the token
# before the period is a single initial or a known abbreviation.
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(‘“])")
ABBREV = re.compile(r"(?:\b[A-Z]|\bet\sal|\bvs|\bcf|\bFig|\bNo|\bDr|\bProf|\bapprox)\.$")


def sentences(text: str) -> list[str]:
    parts, buf = [], ""
    for chunk in SENT.split(text or ""):
        buf = (buf + " " + chunk).strip() if buf else chunk
        if not ABBREV.search(buf.strip()):
            parts.append(buf)
            buf = ""
    if buf:
        parts.append(buf)
    return parts


def strip_circulation(summary: str) -> tuple[str, list[str]]:
    kept, dropped = [], []
    for s in sentences(summary or ""):
        (dropped if CIRCULATION.search(s) else kept).append(s.strip())
    return " ".join(kept).strip(), dropped


# ── the bibliographic preamble ────────────────────────────────────────────────
#
# Found by the eval set doing its job. The summaries follow a template that
# front-loads bibliography, and TF-IDF was treating it as subject matter:
#
#   scGPT   -> "Segment anything in medical images"  via `vector institute`
#   ctDNA   -> "atlas of tumour metabolism"          via `weill cornell`
#   methyl. -> "deconvolution methods"               via `reviews genetics`
#
# Measured 2026-09-03: 206 of 234 summaries name their own venue IN THE FIRST
# SENTENCE, 169 carry an affiliation or authorship sentence, and 156 name one of
# their own authors. So this is not a handful of stragglers, it is the shape of
# the corpus, and a similarity map built on it partly clusters by journal and
# institution -- invisibly, and with plausible-looking results.
#
# Every removal below is PER-DOCUMENT and driven by that document's own
# structured fields (`venue`, `authors`). Nothing is removed from the global
# vocabulary, so a word that is bibliographic noise in one paper stays available
# as subject vocabulary in another. That distinction is why single-word venues
# are safe: "Cell" is dropped only from the template opening, never from
# "single-cell" or "cell type".

# "A Nature Medicine (2025) article arguing that ..." / "A Genome Medicine (2026)
# research article presenting ..."
PREAMBLE = (
    r"^\s*(?:A|An|The)\s+{venue}\s*(?:\(\d{{4}}\))?\s*"
    r"(?:research\s+|review\s+|news\s+|perspective\s+)?"
    r"(?:article|paper|preprint|report|review|perspective|comment|"
    r"news\s+feature|study|letter|editorial)\b[:,]?\s*"
)

AUTHORSHIP = re.compile(
    r"""(?:
        ^\s*From\s+[A-Z]                     # "From Stanford (Quake, Leskovec) ..."
      | ^\s*Authors?\s+include
      | ^\s*A\s+senior\s+author\s+list
      | ^\s*This\s+is\s+LIH
      | corresponding\s+author
      | senior\s+author
      | author\s+list
      | first\s+author
      | \bfrom\s+(?:the\s+)?(?:group|lab|team)\s+of\b
      # --- added 2026-09-03, after measuring what SURVIVED -----------------
      # _strip_authors removes the NAMES from an affiliation sentence but left
      # the sentence, so 105 of them in 100 papers reached the vectors as pure
      # institution text -- "Authors are from the LIH Cardiovascular Research
      # Unit and the LIH Bioinformatics Platform, ." and "Led from CRCT
      # Toulouse; the LIH contribution is the Computational Biomedicine group
      # ( , )". The team's own papers were therefore clustering partly by WHICH
      # LIH UNIT WROTE THEM, which is the leak ADR 0002 section 2 measured and
      # only half closed. These are the template shapes the 2026-09-03 corpus
      # actually uses; enumerated rather than generalised, for the same reason
      # as every other alternative here.
      | ^\s*Authors?\s+(?:are\s+from|span|is\s+from|are\s+at)
      | ^\s*Led\s+from\b
      | \bLIH['\u2019]?s?\s+(?:contribution|connection|own\s+work)\b
      | \bthe\s+(?:LIH\s+)?contribution\s+is\b
      | ^\s*[^.]{0,80}\bwith\s+LIH['\u2019]?s\b
      # archival bookkeeping, not subject matter: "This is not a team
      # publication: it entered the base through the root inbox."
      | \bteam\s+publication\b
      | \bentered\s+the\s+base\b
      | \broot\s+inbox\b
      | \bdeposited\s+(?:twice|by\s+the\s+data\s+owner)\b
    )""",
    re.I | re.X,
)


# The 73 affiliation sentences that survived the shapes above share ONE form: a
# bare list of proper nouns with no verb.
#
#     "LIH Department of Infection and Immunity with the National Cytometry
#      Platform and LCSB."
#     "LIH Bioinformatics Platform with the University of Zilina and the
#      University of Maribor."
#
# Enumerating institutions would be endless and would misfire on cohorts, which
# ARE subject-relevant -- two papers drawing on NCER-PD really are alike. So the
# test is structural instead: drop a sentence whose content words are almost all
# capitalised. Subject prose fails it immediately ("DNA methylation patterns
# facilitate tracing ..." is 1 capital in 4), and a sentence naming several tools
# survives it ("MEBOCOST, CellPhoneDB and CellChat are compared" is 3 in 5),
# which is why the bar is 80% and not a simple majority.
CONNECTIVE = {
    "with", "and", "the", "of", "in", "for", "a", "an", "at", "on", "to", "from",
    "also", "plus", "its", "their", "s",
}


def is_institution_list(s: str) -> bool:
    words = re.findall(r"[A-Za-z][\w'\u2019-]*", s)
    content = [w for w in words if w.lower() not in CONNECTIVE]
    if len(content) < 4:
        return False
    caps = sum(1 for w in content if w[0].isupper())
    return caps / len(content) >= 0.8


def _strip_venue(text: str, venue: str | None) -> str:
    if not venue:
        return text
    v = re.escape(venue).replace(r"\ ", r"\s+")
    # the template opening, for any venue including a one-word one
    text = re.sub(PREAMBLE.format(venue=v), "", text, count=1, flags=re.I)
    # a multi-word venue is unambiguous wherever it appears; a one-word venue
    # ("Cell", "Nature", "Bioinformatics") is NOT, and is left alone
    if len(venue.split()) > 1:
        text = re.sub(v, " ", text, flags=re.I)
    return text


def _strip_authors(text: str, authors: list[str] | None) -> str:
    """Remove this paper's own author names. Full names only.

    A bare surname is not removed: several in this corpus are ordinary words or
    coincide with a colleague's name, and dropping them per-document would be a
    silent edit of subject vocabulary for no measurable gain.
    """
    for name in authors or []:
        parts = [p for p in name.split() if len(p) > 1]
        if len(parts) < 2:
            continue
        pat = r"\b" + r"\s+".join(re.escape(p) for p in parts) + r"\b"
        text = re.sub(pat, " ", text, flags=re.I)
        # "Fabian Theis" also appears as "F. Theis"
        pat2 = r"\b" + re.escape(parts[0][0]) + r"\.\s*" + re.escape(parts[-1]) + r"\b"
        text = re.sub(pat2, " ", text, flags=re.I)
    return text


def embed_text(paper: dict, *, strip: bool, key_points: bool) -> tuple[str, dict]:
    """title + Summary (one step from the source), optionally + Key points.

    §7: prefer `## Summary` over `## Abstract` -- the Summary is one step from the
    source's own extracted text, the Abstract is condensed from the Summary. There
    is nothing to gain from the more derived text.
    """
    summary = paper.get("summary") or ""
    stats = {"circulation": [], "authorship": [], "venue": False, "authors": False}
    if strip:
        kept = []
        for s in sentences(summary):
            if CIRCULATION.search(s):
                stats["circulation"].append(s.strip())
            elif AUTHORSHIP.search(s) or is_institution_list(s):
                stats["authorship"].append(s.strip())
            else:
                kept.append(s.strip())
        summary = " ".join(kept).strip()

        before = summary
        summary = _strip_venue(summary, paper.get("venue"))
        stats["venue"] = summary != before

        before = summary
        summary = _strip_authors(summary, paper.get("authors"))
        stats["authors"] = summary != before
        summary = re.sub(r"\s{2,}", " ", summary).strip()

    bits = [paper.get("title") or "", summary]
    if key_points:
        bits += paper.get("key_points") or []
    return "  ".join(b for b in bits if b), stats


# ── the model ────────────────────────────────────────────────────────────────

# --------------------------------------------------------------------------- #
# Tier 1 -- a neural sentence encoder, behind the SAME interface (D3)
# --------------------------------------------------------------------------- #
#
# THE SLATE IS DECLARED HERE, IN CODE, BEFORE ANY OF IT WAS SCORED. Trying
# several encoders and shipping whichever wins on 55 pre-committed points is the
# same sin eval/queries.md exists to prevent, one level up. So the candidates and
# the reason for each are fixed in advance and EVERY result is reported, losers
# included.
#
#   specter        allenai/specter -- purpose-built for scientific PAPER
#                  similarity from title + abstract, which is exactly this task.
#                  The strongest prior, and the one to beat.
#   pubmedbert     NeuML/pubmedbert-base-embeddings -- biomedical vocabulary.
#                  Tier 0's named failure is generic methodological vocabulary
#                  ("machine learning", "foundation model"), so a domain encoder
#                  is where the improvement should come from if it comes at all.
#   mpnet          all-mpnet-base-v2 -- the strong general-purpose baseline. If a
#                  domain model cannot beat it, that is worth knowing.
TIER1_MODELS = {
    "specter": "allenai/specter",
    "pubmedbert": "NeuML/pubmedbert-base-embeddings",
    "mpnet": "sentence-transformers/all-mpnet-base-v2",
}
TIER1_DEFAULT = "specter"


def encode_st(name: str, texts: list[str]) -> np.ndarray:
    """Sentence-transformer embeddings, L2-normalised.

    Single-threaded and in a fixed order so the result is reproducible: §10
    requires byte-identical output for identical input, and a model that
    reshuffled its own vectors between runs would make the cache meaningless.
    """
    import torch
    from sentence_transformers import SentenceTransformer

    torch.manual_seed(SEED)
    torch.set_num_threads(max(1, min(8, (__import__("os").cpu_count() or 1))))
    model = SentenceTransformer(name, device="cpu")
    model.eval()
    with torch.no_grad():
        v = model.encode(texts, batch_size=16, convert_to_numpy=True,
                         normalize_embeddings=True, show_progress_bar=False)
    return np.asarray(v, dtype=np.float64)


def versions(tier: int = 0, st_name: str | None = None) -> dict:
    import umap
    v = {"sklearn": sklearn.__version__, "numpy": np.__version__,
         "umap": umap.__version__, "n_components": N_COMPONENTS, "seed": SEED,
         "tier": tier}
    if tier == 1:
        import sentence_transformers
        import torch
        v.update({"st": st_name, "sentence_transformers": sentence_transformers.__version__,
                  "torch": torch.__version__})
    # A tier switch changes every vector while leaving the embedding TEXT
    # untouched, so the text hash cannot see it. Putting the tier in here is what
    # makes load_model() refit instead of serving Tier 0 vectors under a Tier 1
    # label -- silently, and with the map unchanged.
    return v


def fit_model(texts: list[str], prev: dict | None = None, *, tier: int = 0,
              st_name: str | None = None) -> dict:
    # The TF-IDF vectorizer is fitted in BOTH tiers, and in Tier 1 it is kept for
    # one job only: shared_terms(), the little "matched on: pd, parkinson, motor"
    # line the UI prints beside every neighbour.
    #
    # Say plainly what that costs. In Tier 0 those terms ARE the reason the model
    # matched two papers -- the similarity is a function of them. In Tier 1 they
    # are only what the two papers happen to share lexically, which is still true
    # and still useful to a reader, but is no longer an explanation of the
    # model's decision. Losing that is a real cost of the swap, and the page must
    # not imply otherwise.
    vec = TfidfVectorizer(
        sublinear_tf=True, stop_words="english", ngram_range=(1, 2),
        min_df=2, max_df=0.55, strip_accents="unicode", lowercase=True,
    )
    tfidf = vec.fit_transform(texts)
    svd = None
    if tier == 1:
        name = TIER1_MODELS.get(st_name, st_name)
        print(f"embed: Tier 1 -- encoding {len(texts)} texts with {name} …")
        vecs = encode_st(name, texts)
    else:
        # `max(1, ...)` is not defensive padding, it is the difference between a
        # small collection working and crashing. min_df=2 with max_df=0.55 keeps
        # only terms in 2..55% of documents, and on a 12-paper collection that
        # left ONE surviving feature -- so min(shape)-1 was 0 and TruncatedSVD
        # refused. A new collection IS small; that is the state this toolkit is
        # handed in. Measured on the 12-paper example: shape (12, 1).
        k = max(1, min(N_COMPONENTS, min(tfidf.shape) - 1))
        if tfidf.shape[1] < 20:
            print(f"embed: WARNING -- only {tfidf.shape[1]} term(s) survived "
                  f"min_df/max_df across {tfidf.shape[0]} document(s). The map will "
                  f"be built, but it is not telling you anything about the subject "
                  f"matter yet. Below roughly 30 papers, read the map as a "
                  f"demonstration of the mechanism.")
        svd = TruncatedSVD(n_components=k, random_state=SEED)
        vecs = normalize(svd.fit_transform(tfidf))

    import umap
    # n_neighbors must be < n_samples. UMAP clamps it with a warning; saying so
    # here is the difference between "the layout looks odd" and knowing why.
    nn = max(2, min(15, len(texts) - 1))
    if nn != 15:
        print(f"embed: n_neighbors {nn} (not 15) -- only {len(texts)} papers.")
    reducer = umap.UMAP(n_neighbors=nn, min_dist=0.12, metric="cosine",
                        random_state=SEED, init="spectral")
    xy = reducer.fit_transform(vecs)
    # The versions INCREMENT from whatever was fitted before. They used to be
    # hardcoded to 1, which made load_model()'s "BUMPING layout_version" message
    # a false statement about the code: a refit moved every coordinate on the map
    # and then told the reader it was still layout v1. The version is the only
    # signal a reader gets that the map they had learned has been redrawn, so it
    # has to be true.
    return {"vec": vec, "svd": svd, "umap": reducer, "tier": tier, "st": st_name,
            "versions": versions(tier, st_name),
            "model_version": (prev or {}).get("model_version", 0) + 1,
            "layout_version": (prev or {}).get("layout_version", 0) + 1}


def transform(model: dict, texts: list[str]) -> tuple[np.ndarray, np.ndarray]:
    """Frozen model: new text is projected INTO the existing space and layout."""
    if model.get("tier") == 1:
        # A sentence encoder has no fitted state to freeze -- the same text gives
        # the same vector forever, which makes Tier 1 STRICTLY better behaved
        # here than Tier 0, whose vocabulary and IDF weights are corpus-derived.
        vecs = encode_st(TIER1_MODELS.get(model["st"], model["st"]), texts)
    else:
        vecs = normalize(model["svd"].transform(model["vec"].transform(texts)))
    xy = model["umap"].transform(vecs)
    return vecs, np.asarray(xy)


def text_hash(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def load_cache() -> dict:
    """sha256 -> {vec, xy, txt}. The reason existing coordinates cannot drift."""
    if not CACHE_NPZ.exists():
        return {}
    try:
        z = np.load(CACHE_NPZ, allow_pickle=False)
        shas, vecs, xys = z["sha"], z["vec"], z["xy"]
        txts = z["txt"] if "txt" in z.files else None
    except Exception as e:                                   # noqa: BLE001
        print(f"embed: coordinate cache will not load ({type(e).__name__}); starting over")
        return {}
    if txts is None:
        print("embed: cache predates embedding-text hashing; every paper will be "
              "re-placed once so the two are back in step")
        return {}
    return {str(s): {"vec": vecs[i], "xy": xys[i], "txt": str(txts[i])}
            for i, s in enumerate(shas)}


def save_cache(cache: dict) -> None:
    shas = sorted(cache)
    np.savez_compressed(
        CACHE_NPZ,
        sha=np.array(shas),
        vec=np.array([cache[s]["vec"] for s in shas], dtype=np.float32),
        xy=np.array([cache[s]["xy"] for s in shas], dtype=np.float32),
        txt=np.array([cache[s]["txt"] for s in shas]),
    )


def load_model() -> dict | None:
    if not MODEL_PKL.exists():
        return None
    try:
        model = pickle.loads(MODEL_PKL.read_bytes())
    except Exception as e:                                   # noqa: BLE001
        print(f"embed: cached model will not load ({type(e).__name__}); refitting")
        return None
    want_all = versions(model.get("tier", 0), model.get("st"))
    if model.get("versions") != want_all:
        print("embed: the numeric stack changed since the model was fitted:")
        for k, want in want_all.items():
            got = (model.get("versions") or {}).get(k)
            if got != want:
                print(f"         {k}: model {got!r} -> now {want!r}")
        print("embed: refitting, and BUMPING layout_version -- the map will reshuffle.")
        return None
    return model


# ── neighbours, in the full space ────────────────────────────────────────────

def neighbours(vecs: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray]:
    sim = vecs @ vecs.T
    np.fill_diagonal(sim, -np.inf)
    idx = np.argsort(-sim, axis=1)[:, :k]
    return idx, np.take_along_axis(sim, idx, axis=1)


def shared_terms(model: dict, texts: list[str], i: int, j: int, n: int) -> list[str]:
    """What Tier 0 buys that a neural encoder does not: an explanation."""
    tf = model["vec"].transform([texts[i], texts[j]])
    a, b = tf[0].toarray()[0], tf[1].toarray()[0]
    both = np.minimum(a, b)
    if not both.any():
        return []
    names = model["vec"].get_feature_names_out()
    return [names[t] for t in np.argsort(-both)[:n] if both[t] > 0]


# ── diagnostics from eval/queries.md ─────────────────────────────────────────

def c1_leakage(papers: list[dict], vecs: np.ndarray) -> tuple[float, float, float]:
    """Mean cosine among papers sharing a circulator, vs over all pairs."""
    sim = vecs @ vecs.T
    n = len(papers)
    iu = np.triu_indices(n, 1)
    overall = float(sim[iu].mean())
    same = []
    for a in range(n):
        sa = set(papers[a]["provenance"]["sharers"])
        if not sa:
            continue
        for b in range(a + 1, n):
            if sa & set(papers[b]["provenance"]["sharers"]):
                same.append(sim[a, b])
    same_mean = float(np.mean(same)) if same else float("nan")
    return same_mean, overall, same_mean - overall


# The seed papers for `--eval` are COLLECTION data, not tool configuration: a
# different collection has different seeds, and a hardcoded list of one library's
# paper ids is dead weight in every other one. eval/seeds.json holds them, and its
# absence simply means there is nothing to check.
def load_seeds() -> list[tuple[str, str]]:
    path = ROOT / "eval" / "seeds.json"
    if not path.exists():
        return []
    spec = json.loads(path.read_text(encoding="utf-8"))
    return [(s["id"], s["expect"]) for s in spec.get("seeds", [])]


def run_eval(papers, vecs, xy, model, texts, idx, sims) -> None:
    by_id = {p["id"]: i for i, p in enumerate(papers)}
    print("\n" + "=" * 78)
    print("EVAL against eval/queries.md -- top 5 in the FULL space")
    print("=" * 78)
    seeds = load_seeds()
    if not seeds:
        print("\n(no eval/seeds.json -- no seed expectations to check. See "
              "docs/templates/eval_README.md.)")
    for pid, expectation in seeds:
        i = by_id.get(pid)
        if i is None:
            print(f"\n!! seed not in the corpus: {pid}")
            continue
        p = papers[i]
        print(f"\n### {p['title'][:72]}")
        print(f"    topic: {p['topic']}")
        print(f"    expect: {expectation}")
        for rank, (j, s) in enumerate(zip(idx[i][:5], sims[i][:5]), 1):
            q = papers[j]
            terms = shared_terms(model, texts, i, int(j), 3)
            print(f"    {rank}. [{s:.3f}] {(q['title'] or q['source'])[:64]}")
            print(f"           topic: {q['topic']}")
            if terms:
                print(f"           shared: {', '.join(terms)}")

    # C3: does the projection keep the structure the embedding found? Reported as a
    # diagnostic rather than a gate -- there was no pre-committed criterion for it,
    # and inventing one now would be the sin eval/queries.md is about.
    print("\n" + "=" * 78)
    print("C3 -- structure retained (fraction of the 6 nearest sharing a label)")
    import collections as _c

    # UNLABELLED PAPERS ARE EXCLUDED, not folded into a "?" bucket.
    #
    # 96 of 338 papers have no topic yet (the team's own output, awaiting the next
    # review). Labelling them all "?" made them count as sharing a label with each
    # other, which inflated BOTH the measured purity and the chance baseline -- "?"
    # became the largest class at 28% of the corpus, contributing 0.081 of a 0.113
    # chance figure on its own. The number stopped meaning "neighbours share a
    # topic" and started meaning "neighbours are both unfiled", which is a fact
    # about the review's backlog, not about the projection.
    #
    # So each label is measured over the subset that HAS it, with neighbours drawn
    # from that same subset. That is also what makes the figure comparable with the
    # 234-paper measurement in ADR 0002, where every paper was labelled.
    def _purity(coords, labels, k=6, cos=False):
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

    def _chance(labels):
        vals = [x for x in labels if x]
        return sum((c / len(vals)) ** 2 for c in _c.Counter(vals).values())

    part = [p["part_letter"] for p in papers]
    topic = [p["topic"] for p in papers]
    print(f"                          part     topic")
    print(f"    labelled papers   :   {sum(1 for x in part if x):>5}    "
          f"{sum(1 for x in topic if x):>5}   of {len(papers)}")
    print(f"    full {vecs.shape[1]}-d space  :   "
          f"{_purity(vecs, part, cos=True):.3f}    {_purity(vecs, topic, cos=True):.3f}")
    print(f"    2-D layout        :   {_purity(xy, part):.3f}    {_purity(xy, topic):.3f}")
    print(f"    chance            :   {_chance(part):.3f}    {_chance(topic):.3f}")

    same, overall, excess = c1_leakage(papers, vecs)
    print("\n" + "=" * 78)
    print("C1 -- circulator leakage")
    print(f"    mean cosine, papers sharing a circulator : {same:.4f}")
    print(f"    mean cosine, all pairs                   : {overall:.4f}")
    print(f"    excess                                   : {excess:+.4f}"
          f"   (pass criterion: <= +0.0200)")
    print(f"    verdict: {'PASS' if excess <= 0.02 else 'FAIL'}")


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refit", action="store_true", help="refit; bumps model+layout version")
    ap.add_argument("--eval", action="store_true", help="score and diagnose; no writes")
    ap.add_argument("--no-strip", action="store_true",
                    help="do NOT strip circulation sentences (C1 diagnostic only)")
    ap.add_argument("--key-points", action="store_true",
                    help="include Key points in the embedded text")
    ap.add_argument("--check-layout", action="store_true",
                    help="C2: transform N-1 then N papers; existing coords must not move")
    ap.add_argument("--tier", type=int, default=0, choices=(0, 1),
                    help="0 = TF-IDF + SVD (default). 1 = a sentence encoder (D3)")
    ap.add_argument("--st-model", default=TIER1_DEFAULT,
                    help="which Tier 1 encoder: " + ", ".join(TIER1_MODELS)
                         + ", or any sentence-transformers name")
    ap.add_argument("--probe", metavar="OUT.npz",
                    help="fit, write ONLY this npz of vectors, and touch nothing "
                         "else -- no model pickle, no cache, no similarity.json. "
                         "How a candidate is evaluated without becoming the "
                         "shipped one.")
    args = ap.parse_args()

    lib_path = DATA / "library.json"
    if not lib_path.exists():
        print("embed: data/library.json not found -- run `make build` first.", file=sys.stderr)
        return 1
    lib = json.loads(lib_path.read_text(encoding="utf-8"))
    papers = lib["papers"]

    strip = not args.no_strip
    pairs = [embed_text(p, strip=strip, key_points=args.key_points) for p in papers]
    texts = [t for t, _ in pairs]
    stats = [s for _, s in pairs]
    n_circ = sum(len(s["circulation"]) for s in stats)
    n_circ_p = sum(1 for s in stats if s["circulation"])
    n_auth = sum(len(s["authorship"]) for s in stats)
    n_auth_p = sum(1 for s in stats if s["authorship"])
    n_venue = sum(1 for s in stats if s["venue"])
    n_names = sum(1 for s in stats if s["authors"])
    print(f"embed: {len(papers)} papers · input = title + summary"
          f"{' + key points' if args.key_points else ''}")
    if strip:
        print(f"embed: removed from the EMBEDDING INPUT only "
              f"(library.json and the page are untouched):")
        print(f"         {n_circ:>4} circulation sentence(s)   in {n_circ_p} paper(s)   (§7)")
        print(f"         {n_auth:>4} authorship/affiliation    in {n_auth_p} paper(s)")
        print(f"         venue name removed from {n_venue} paper(s) · "
              f"own author names from {n_names}")
    else:
        print("embed: --no-strip: ALL bibliographic preamble LEFT IN (diagnostic only)")

    # ---- probe: evaluate a candidate without shipping it -------------------
    if args.probe:
        out = Path(args.probe)
        model = fit_model(texts, None, tier=args.tier, st_name=args.st_model)
        vecs, xy = transform(model, texts)
        # Determinism is a §10 requirement and a sentence encoder is the one
        # place it could plausibly fail, so it is CHECKED rather than assumed.
        again, _ = transform(model, texts)
        same = bool(np.array_equal(vecs, again))
        print(f"embed: probe tier {args.tier}"
              + (f" ({args.st_model})" if args.tier == 1 else "")
              + f" · {vecs.shape[1]}-d · re-encoding is bit-identical: {same}")
        if not same:
            worst = float(np.abs(vecs - again).max())
            print(f"embed: WARNING -- not reproducible; max element difference "
                  f"{worst:.3e}. §10 requires identical output for identical input.")
        np.savez_compressed(
            out,
            sha=np.array([p["sha256"] for p in papers]),
            vec=vecs.astype(np.float32),
            xy=xy.astype(np.float32),
            txt=np.array([text_hash(x) for x in texts]),
        )
        print(f"embed: probe -> {out}  (nothing else was written)")
        return 0

    scratch = args.no_strip or args.key_points          # diagnostic runs: never persist
    model = None if (args.refit or scratch) else load_model()
    fresh = model is None
    # What the DISCARDED model was numbered, so a refit counts on from there
    # rather than resetting to 1 and claiming nothing moved.
    prev = None
    if fresh and not scratch and MODEL_PKL.exists():
        try:
            prev = pickle.loads(MODEL_PKL.read_bytes())
        except Exception:                                    # noqa: BLE001
            prev = None
    cache = {} if (fresh or scratch) else load_cache()

    hashes = [text_hash(x) for x in texts]

    if fresh:
        print(f"embed: fitting Tier 0 (TF-IDF + TruncatedSVD, {N_COMPONENTS}d) + UMAP …")
        model = fit_model(texts, prev, tier=args.tier, st_name=args.st_model)
        if prev:
            print(f"embed: REFIT -- model v{prev.get('model_version')} -> "
                  f"v{model['model_version']}, layout "
                  f"v{prev.get('layout_version')} -> v{model['layout_version']}. "
                  f"EVERY coordinate is recomputed and the map will look different; "
                  f"neighbour lists change too. This is the one thing the sha256 "
                  f"cache exists to prevent, so it happens only when asked for.")
        vecs, xy = transform(model, texts)
        cache = {p["sha256"]: {"vec": vecs[i], "xy": xy[i], "txt": hashes[i]}
                 for i, p in enumerate(papers)}
    else:
        new_i, stale_i = [], []
        for i, p in enumerate(papers):
            hit = cache.get(p["sha256"])
            if hit is None:
                new_i.append(i)
            elif hit.get("txt") != hashes[i]:
                stale_i.append(i)
        todo = new_i + stale_i
        print(f"embed: frozen model v{model['model_version']} / layout "
              f"v{model['layout_version']} · {len(papers) - len(todo)} unchanged · "
              f"{len(new_i)} new · {len(stale_i)} re-placed (embedding text changed)")
        if stale_i:
            # Loud on purpose: these papers MOVE on the map, and a reader who had
            # learned where they sat is entitled to know that was not a glitch.
            for i in stale_i[:10]:
                print(f"  re-placed: {papers[i]['source'][:72]}")
            if len(stale_i) > 10:
                print(f"  re-placed: ... and {len(stale_i) - 10} more")
        if todo:
            v_new, xy_new = transform(model, [texts[i] for i in todo])
            for n, i in enumerate(todo):
                cache[papers[i]["sha256"]] = {"vec": v_new[n], "xy": xy_new[n],
                                              "txt": hashes[i]}
        # Order matters and is by paper, not by cache order.
        vecs = np.array([cache[p["sha256"]]["vec"] for p in papers], dtype=np.float32)
        xy = np.array([cache[p["sha256"]]["xy"] for p in papers], dtype=np.float32)

    idx, sims = neighbours(vecs, TOP_K)

    if args.check_layout:
        # C2 (eval/queries.md): freeze, then add a paper. The pre-existing points
        # must not move -- a map that drifts on every update destroys the one
        # thing a map is for, which is that a reader learns where things are.
        if fresh:
            print("check-layout: no frozen model on disk to test against.", file=sys.stderr)
            return 1
        full = load_cache()
        if len(full) < len(papers):
            print("check-layout: run `make embed` first so every paper is cached.",
                  file=sys.stderr)
            return 1
        # Simulate the real update: drop the last paper from the cache, as if it
        # had just been copied in, then go through the ordinary placement path.
        victim = papers[-1]["sha256"]
        before = np.array([full[p["sha256"]]["xy"] for p in papers[:-1]], dtype=np.float32)
        partial = {k: v for k, v in full.items() if k != victim}
        v_new, xy_new = transform(model, [texts[-1]])
        partial[victim] = {"vec": v_new[0], "xy": xy_new[0]}
        after = np.array([partial[p["sha256"]]["xy"] for p in papers[:-1]], dtype=np.float32)

        same = np.array_equal(before, after)
        delta = float(np.abs(before - after).max())
        # And the counter-example the cache exists to prevent:
        _, xy_batch233 = transform(model, texts[:-1])
        _, xy_batch234 = transform(model, texts)
        naive = float(np.abs(xy_batch233 - xy_batch234[:-1]).max())

        print("C2 -- layout stability under growth")
        print(f"    233 cached papers + 1 newly placed")
        print(f"    max movement of the pre-existing points : {delta:.3e}")
        print(f"    bit-identical                           : {same}")
        print(f"    verdict: {'PASS' if same else 'FAIL'}")
        print(f"\n    for contrast, WITHOUT the cache -- re-transforming the whole")
        print(f"    corpus through the same frozen model moves them by {naive:.3f}.")
        print(f"    umap.transform() is batch-coupled, so freezing the model is")
        print(f"    necessary but not sufficient; the sha256 cache is what makes")
        print(f"    the map stable.")
        return 0 if same else 1

    if args.eval:
        run_eval(papers, vecs, xy, model, texts, idx, sims)
        return 0

    if not scratch:
        if fresh:
            MODEL_PKL.write_bytes(pickle.dumps(model))
            print(f"embed: model saved -> {MODEL_PKL.relative_to(ROOT)}")
        save_cache(cache)
        print(f"embed: {len(cache)} coordinate(s) cached by sha256 -> "
              f"{CACHE_NPZ.relative_to(ROOT)}")

    # 2D coordinates, normalised to [0,1] on the FITTED extent so the page does not
    # have to know the raw scale. Recorded so a later transform lands consistently.
    lo, hi = xy.min(axis=0), xy.max(axis=0)
    span = np.where(hi - lo == 0, 1.0, hi - lo)
    norm = (xy - lo) / span

    out = {
        "data_as_of": lib["data_as_of"],
        "tier": ("0 (TF-IDF + TruncatedSVD)" if model.get("tier", 0) == 0
                 else f"1 ({TIER1_MODELS.get(model['st'], model['st'])})"),
        "model_version": model["model_version"],
        "layout_version": model["layout_version"],
        "n_components": int(model["svd"].n_components),
        "explained_variance": round(float(model["svd"].explained_variance_ratio_.sum()), 4),
        "seed": SEED,
        "min_sim": MIN_SIM,
        "top_k": TOP_K,
        "stripped": {
            "circulation_sentences": n_circ, "circulation_papers": n_circ_p,
            "authorship_sentences": n_auth, "authorship_papers": n_auth_p,
            "venue_removed": n_venue, "author_names_removed": n_names,
        },
        "extent": {"lo": lo.tolist(), "hi": hi.tolist()},
        "notice": (
            "This map is built from the summaries, not from the papers. Two papers can "
            "sit next to each other because they were summarised in the same vocabulary "
            "rather than because they resemble each other. Nearest neighbours are computed "
            "in the full embedding space, not from these 2-D positions."
        ),
        "papers": {},
    }
    for i, p in enumerate(papers):
        out["papers"][p["id"]] = {
            "xy": [round(float(norm[i][0]), 5), round(float(norm[i][1]), 5)],
            "near": [
                {"id": papers[int(j)]["id"], "sim": round(float(s), 4),
                 "terms": shared_terms(model, texts, i, int(j), N_SHARED_TERMS)}
                for j, s in zip(idx[i], sims[i]) if s >= MIN_SIM
            ],
        }

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    same, overall, excess = c1_leakage(papers, vecs)
    print(f"embed: explained variance {out['explained_variance']:.1%} over "
          f"{out['n_components']} components")
    # `nan <= 0.02` is False, so an UNDEFINED statistic printed as "FAIL" -- which
    # is what a collection with no circulator recorded on any paper produced. A
    # criterion that cannot be evaluated has not been failed; saying otherwise
    # teaches the operator to ignore the line.
    if excess != excess:      # NaN
        print("embed: circulator-leakage NOT APPLICABLE -- no paper records a "
              "circulator, so there are no same-circulator pairs to compare")
    else:
        print(f"embed: circulator-leakage excess {excess:+.4f} "
              f"({'PASS' if excess <= 0.02 else 'FAIL'}, criterion <= +0.0200)")
    print(f"embed: wrote {OUT.relative_to(ROOT)} · "
          f"{sum(len(v['near']) for v in out['papers'].values())} neighbour links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
