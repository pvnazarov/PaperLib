## How to read this

Every paper in the collection, clustered by subject. {n} papers, {t} topics in {parts} parts,
each paper in exactly one topic.

**Why it was re-drawn.** The previous taxonomy was 14 topics over 60 papers. A second batch of
57 papers arrived on 2026-09-05 and exposed two specific faults, not a general staleness. First,
Part A ran from MHC binding onward and had nothing upstream of the groove, so nine papers on
proteasomal cleavage, TAP transport and ERAP1 trimming had no home that described them — the
step that decides whether a peptide exists to be bound was missing from a taxonomy about
presentation. Second, seven papers on splicing, indels, noncoding translation and
post-translational protein splicing had no home either: the old taxonomy assumed neoantigens
come from missense mutations, which is what the pipelines assume and what these papers exist to
contradict.

**What proposed and what decided.** Reading decided. Every one of the 117 papers was read and
its four prose sections written before the candidate taxonomy was drawn, and the topics come
from those readings. The similarity vectors proposed nothing here: `make topics` was not run.
The vectors are TF-IDF over the summaries, so they group by shared vocabulary rather than by
subject, and they would have put the infrastructure papers — a nearest-neighbour index, a
sequence search tool — next to whatever else says "search" and "efficient".

**How many moved.** None. Zero of the 60 previously filed papers changed topic; the revision is
an extension, not a re-clustering of the existing collection, and that was a MUST fixed in
advance rather than a happy result. Two topics were renamed to cover what was added:
*Thymic selection and self-discrimination* became *Thymic selection and repertoire
availability*, and *MHC class II presentation* became *MHC class II presentation and CD4
responses*. Four topics are new. The before-and-after measurement is in
`reports/2026-09-05_reclustering_score.txt`, against criteria written in
`eval/reclustering.json` before any candidate existed.

**Which criteria failed.** None failed outright, and two deserve more than a PASS. *Minimum
topic size* passed only through the exception the criterion itself allows: **HLA genotyping
holds 2 papers, below the stated floor of 3**, and is kept because its subject is genuinely
narrow — an escape clause, not a clean result, and the next revision should grow it or fold it
into MHC class I. *Cohesion* was **not measured**: the criteria file states the circularity in
advance, since the vectors that would score within-topic cohesion are built from the same
summaries the clustering was drawn from, so cohesion would measure agreement with the proposer
rather than quality.

**Where the seams are.** Six papers could defensibly sit elsewhere, and are named here rather
than left for a reader to notice. **AlphaFold 3** and **HNSW**, **Faiss**, **MMseqs2** are not
immunology; the first is filed under *TCR specificity and structural recognition* because the
structure-based TCR predictors there inherit its accuracy ceiling, the other three under
*Pipelines and analysis tools* because they are the search infrastructure the sequence and
embedding methods run on. **Jardine (2016)** is an HIV antibody paper, filed under *Thymic
selection and repertoire availability* because what it actually measures is whether a precursor
capable of responding exists in the repertoire — the same question that topic asks for T cells.
**Graber (2025)** is protein–ligand drug design, filed under *Benchmarking, bias and
generalisation* because it is the cleanest demonstration of the train–test leakage this field
has inside it. **McGranahan (2017)** introduces an HLA typing tool but is filed under *Tumour
immune escape*, and **Culka (2026)** is the clearest statement of the generalisation problem but
is filed under *TCR specificity*, both for the reasons given when they were first placed.

Everything else is mechanical:

| Element | Where it comes from |
|---|---|
| first author, year, journal, title | the publisher's own registration via Crossref or arXiv, keyed on a DOI or arXiv ID verified against the paper's bytes — or, for the papers that register nowhere, the paper's own first page |
| DOI / arXiv ID | the sidecar's `doi:` field |
| summary | the sidecar's `## Abstract` — written once at ingest from the source's own extracted text |
| `[src]` link | the source file in `raw/` |

**The summaries are paraphrases, not quotations, and this document is not a source.** Each entry
links the paper itself; a claim you intend to rely on must be checked there.

**Author lists are deliberately incomplete here.** Each entry names the registered first author
and `et al.`, never a reconstructed list. Full, verified lists exist for {with_authors} of {n}
papers, in `data/bib_cache.json` and searchable in the browser.
