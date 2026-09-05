---
# --- identity ------------------------------------------------
id: 2023-01-01_li-2023-briefings-in-bioinformatics-pros
id_basis: filename-year
source: Li(2023) Briefings in Bioinformatics; ProsperousPlus a one-stop and comprehensive platform for accurate protease-specific substrate cleavage prediction and machine-learning model construction.pdf
sha256: c56e9e3137f33b7255b35fd553cf582649e6fce468d7b85fc07e767d0aacc91a
size_bytes: 2586715
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 81034

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bib/bbad372"
year: 2023
title: "ProsperousPlus : a one-stop and comprehensive platform for accurate protease-specific substrate cleavage prediction and machine-learning model construction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as bbad372.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

ProsperousPlus is a platform that lets users build their own protease-specific substrate cleavage site predictors rather than shipping a fixed model per protease. The rationale is that substrate cleavage data now exist for over 100 protease types and are growing faster than predictors can be published for them.

## Summary

The design argument is about the publication model rather than the algorithm: since data accumulate faster than papers, a tool that helps users train and assess a predictor for the protease they care about is more durable than another fixed predictor.

It is aimed at users with little or no programming background, which is what makes the argument practical rather than theoretical - the alternative is that new protease types simply go unserved.

## Key points

- Users build, benchmark and deploy predictors for a protease of their choosing instead of using a fixed model.
- Motivated by data for 100+ protease types outpacing what can be published as individual predictors.
- Multiple scoring functions are combined, with benchmarking built into the workflow.
- Relevant here as general infrastructure for the proteolysis steps upstream of MHC binding.

## Limitations

The authors note that predictive performance may vary substantially across protease families because cleavage site characteristics differ, and that selecting an optimal feature and model set remains a challenge for some proteases - so the platform's convenience does not guarantee a good model. It is general protease work, not immunoproteasome-specific, so its relevance to antigen processing is indirect. A user-built model is only as good as the data the user supplies.

## Provenance

Located in the published literature, dropped into `inbox/` as `bbad372.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bib/bbad372`; the prose sections were written here from the paper itself.

## Citation

Li et al. Briefings in Bioinformatics 2023. <i>ProsperousPlus</i>
                    : a one-stop and comprehensive platform for accurate protease-specific substrate cleavage prediction and machine-learning model construction. doi: 10.1093/bib/bbad372
