## How to read this

Every paper in the collection, clustered by subject. {n} papers, {t} topics in {parts} parts,
each paper in exactly one topic.

**The clustering is the only judgement in this document.** It was drawn by reading each paper's
title, abstract and key points and deciding where it belongs. The similarity vectors may
*propose* — per-topic cohesion, centroid overlap, papers that sit closer to another topic than
to their own — but proposing is all they do: they are TF-IDF over the summaries, so they group
by shared vocabulary rather than by subject, and vocabulary and subject part company more often
than is comfortable. Some topics here are deliberately low on vocabulary cohesion because their
subject is genuinely diverse.

**This is the FIRST clustering of this collection**, so there is no before-and-after to report.
When it is re-drawn, that revision belongs in `reports/` with the criteria written down *before*
any candidate taxonomy exists, and this block should be replaced with one that says so.

**What the parts follow.** The five parts trace the pathway a candidate neoantigen has to survive,
because that is the order in which the field's failures happen. **A** is presentation — does the
peptide reach the surface at all. **B** is recognition — of the peptides that are presented, which
ones does a T cell actually see. **C** is the two-sided discrimination problem — how the repertoire
was shaped before it met the tumour, what happens when a receptor confuses self for non-self, and
what tumours do to stop being visible. **D** is what happened when this was tried in patients.
**E** is the substrate everything else stands on: the databases, the pipelines, and the papers that
benchmark the rest.

**Two deliberate choices worth stating.** First, *presentation* and *immunogenicity* are separated
into different parts rather than filed together as "prediction", because the collection's own
evidence says they are different problems: measured T cell avidity correlates poorly with in silico
affinity, stability and processing scores, and well with an immunogenicity score. Filing them
together would hide the one distinction the papers keep insisting on.

Second, **Benchmarking, bias and generalisation** is a topic rather than a note attached to the
methods it evaluates. Four papers here independently find that reported performance is not what it
appears — that ranking by predicted affinity is unsupported, that immunogenicity models learn the
HLA rather than the peptide, that machine-learning TCR models fail on unseen peptides where
biophysical ones do not, and that pan-allele extrapolation holds for human alleles and breaks
elsewhere. Scattering those across the topics they criticise would leave each looking like a
caveat instead of a finding.

**Where the seams are.** Three papers could defensibly sit elsewhere. McGranahan (2017) introduces
an HLA typing tool but is filed under *Tumour immune escape*, because allele-specific loss is what
the paper is about. Culka (2026) is the clearest statement of the generalisation problem but is
filed under *TCR specificity*, because it is also a method paper and its evidence is TCR data.
AlphaFold 3 is filed under *TCR specificity and structural recognition* although it is not an
immunology paper; it is here because the structure-based TCR predictors in that topic inherit its
accuracy ceiling.

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
papers, in `data/bib_cache.json` and searchable in the browser; they are not repeated here
because an entry heading is a citation, not a byline.
