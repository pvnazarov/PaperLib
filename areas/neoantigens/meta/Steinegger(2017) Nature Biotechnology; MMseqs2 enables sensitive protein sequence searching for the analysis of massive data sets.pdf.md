---
# --- identity ------------------------------------------------
id: 2017-01-01_steinegger-2017-nature-biotechnology-mms
id_basis: filename-year
source: Steinegger(2017) Nature Biotechnology; MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets.pdf
sha256: 827363d9af09e1c60981d1d46afdc78cb2eebcf04528365e558ce4ac7a2fe5d2
size_bytes: 480423
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 59804

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nbt.3988"
year: 2017
title: "MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nbt.3988.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

MMseqs2 performs sensitive protein sequence searching at speeds that make massive datasets tractable: annotating 1.1 billion hypothetical protein sequences against 16,479 Pfam profiles took 8.3 hours on one server, roughly 4,000-14,000 times faster than HMMER3 while finding comparable or more annotations.

## Summary

Infrastructure, present in this collection because sequence search underpins several things done here routinely - building the reference proteome that defines 'self', finding a neoepitope's closest human or microbial match, and the homology screens used to check engineered TCRs for off-target risk.

The speed matters practically: dissimilarity-to-self metrics require searching every candidate peptide against a whole proteome, and doing that at the scale of a patient cohort is only feasible with a search tool of this class.

## Key points

- Roughly 4,000-14,000x faster than HMMER3 on Pfam annotation at comparable or better sensitivity.
- Matched 78% of sequences to eggNOG in 1.5% of the CPU time BLAST needed to match 67%.
- Makes proteome-scale homology screening - the basis of dissimilarity-to-self metrics - routine.
- Sensitivity is tunable, so the speed/sensitivity trade can be set per application.

## Limitations

Not an immunology paper: it supplies a capability, and any biological claim built on it needs its own evidence. Sensitivity is a tunable setting and the reported comparisons hold at the settings chosen; a lower setting is faster and misses more. Benchmarks are from 2017 hardware and against the tools of that time.

## Provenance

Located in the published literature, dropped into `inbox/` as `nbt.3988.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nbt.3988`; the prose sections were written here from the paper itself.

## Citation

Steinegger et al. Nature Biotechnology 2017. MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. doi: 10.1038/nbt.3988
