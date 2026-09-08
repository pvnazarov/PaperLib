---
# --- identity ------------------------------------------------
id: 2021-01-01_duy-2021-cancer-discovery-chemotherapy-i
id_basis: filename-year
source: Duy(2021) Cancer Discovery; Chemotherapy Induces Senescence-Like Resilient Cells Capable of Initiating AML Recurrence.pdf
sha256: 15b1875d5101b6148c13945b1b9a132cc633fcd9ba53668e43bebaff3080a253
size_bytes: 12653941
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 357785

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-20-1375"
year: 2021
title: "Chemotherapy Induces Senescence-Like Resilient Cells Capable of Initiating AML Recurrence"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Duy(2021) Cancer Discov; Chemotherapy Induces Senescence-Like Resilient Cells Capable of Initiating AML Recurrence.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Primary AML cells are shown to enter a senescence-like phenotype after chemotherapy in vitro and in vivo, with induction of senescence/inflammatory and embryonic diapause transcriptional programs and downregulation of MYC and leukemia stem cell genes. Single-cell RNA sequencing suggests depletion of leukemia stem cells and enrichment of distinct senescence-like subpopulations. The state is transient and confers superior colony-forming and engraftment potential; entry into it depends on ATR, and ATR inhibitors severely impair persistence of AML cells. Recovered post-senescence cells give rise to relapsed AML with increased stem cell potential.

## Summary

A direct challenge to the standard account of AML relapse. The prevailing model is that relapse comes from pre-existing chemoresistant leukemia stem cells; here the cells that survive chemotherapy have their stem cell programs turned down, not up, and acquire resilience by entering a transient senescence-like, diapause-like state instead. Stem cell potential is a consequence of surviving, not the reason for it.

The methodological point the authors make is sharp and explains why this was missed: most studies compare diagnosis with relapse and never sample the nadir, which is precisely when this state exists. The ATR dependency turns the observation into a strategy - if entry into the state requires ATR, an ATR inhibitor given alongside chemotherapy should prevent the reservoir from forming.

## Key points

- Chemotherapy-surviving AML cells enter a transient senescence-like state with senescence/inflammatory and embryonic diapause programs.
- MYC and leukemia stem cell genes are downregulated in these cells - the opposite of the pre-existing-LSC model of relapse.
- The state is reversible and confers superior colony-forming and engraftment potential on recovery, with increased stem cell potential afterwards.
- Entry depends on ATR, and ATR inhibitors severely impair the persistence of AML cells.
- Sampling at nadir rather than only at diagnosis and relapse is what makes the phenomenon visible.

## Limitations

Matched-pair patient numbers are small - four pairs for bulk expression, nine for single-cell nadir comparison - and nadir marrow is scarce and low in cellularity, so both the sampling and the cell-type assignment in those samples are difficult. 'Senescence-like' is defined by signature scores rather than by the standard senescence criteria, and the diapause program is a transcriptional resemblance to a mouse embryonic state, which is suggestive rather than mechanistic. The claim that these cells rather than LSCs cause relapse rests on signature depletion and functional potential in xenografts, not on lineage tracing from nadir cell to relapse. ATR inhibition impairs persistence in models; whether it can be combined safely with induction chemotherapy, which itself depends on DNA damage responses in normal tissue, is untested.

## Provenance

Located in the published literature, dropped into `inbox/` as `Duy(2021) Cancer Discov; Chemotherapy Induces Senescence-Like Resilient Cells Capable of Initiating AML Recurrence.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-20-1375`; the prose sections were written here from the paper itself.

## Citation

Duy et al. Cancer Discovery 2021. Chemotherapy Induces Senescence-Like Resilient Cells Capable of Initiating AML Recurrence. doi: 10.1158/2159-8290.CD-20-1375
