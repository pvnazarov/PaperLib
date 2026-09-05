---
# --- identity ------------------------------------------------
id: 1999-01-01_rammensee-1999-immunogenetics-syfpeithi
id_basis: filename-year
source: Rammensee(1999) Immunogenetics; SYFPEITHI database for MHC ligands and peptide motifs.pdf
sha256: 6c7aad8abb23736e30d49e4d8e96e40c19d7e89ac26eadfb29343d9b88cccec7
size_bytes: 85898
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 41206

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1007/s002510050595"
year: 1999
title: "SYFPEITHI: database for MHC ligands and peptide motifs"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s002510050595.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

SYFPEITHI is a public database of MHC class I and class II ligands and peptide motifs across humans, apes, cattle, chicken and mouse, searchable by allele, motif, natural ligand, T-cell epitope, source protein and reference, with hyperlinks to EMBL and PubMed and ligand predictions for a number of allelic products.

## Summary

One of the founding resources of computational immunology, and the one that made motif-based prediction reproducible by others. Its stated editorial policy is the notable part: content is restricted to published data only.

That restriction is a deliberate quality bound and also the source of its bias - it inherits everything about what gets published, which is the same limitation the later and much larger IEDB carries.

## Key points

- Ligands and motifs for human and several non-human species, with cross-species coverage unusual for its time.
- Searchable by allele, motif, ligand, epitope, source protein and reference, with EMBL and PubMed links.
- Provides ligand predictions alongside the data, an early integration of resource and tool.
- Content restricted to published data only - a stated editorial policy, and the source of its selection bias.

## Limitations

Published data only means publication bias is built in by design, and negatives are essentially absent. Coverage is uneven across alleles, following research attention rather than population frequency. It predates mass-spectrometry immunopeptidomics, so its ligands come largely from earlier, lower-throughput methods, and modern resources such as IEDB and CEDAR have long since exceeded its scale.

## Provenance

Located in the published literature, dropped into `inbox/` as `s002510050595.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1007/s002510050595`; the prose sections were written here from the paper itself.

## Citation

-GRammensee et al. Immunogenetics 1999. SYFPEITHI: database for MHC ligands and peptide motifs. doi: 10.1007/s002510050595
