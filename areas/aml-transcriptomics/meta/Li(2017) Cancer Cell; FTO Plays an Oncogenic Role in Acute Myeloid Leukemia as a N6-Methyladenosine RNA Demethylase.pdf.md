---
# --- identity ------------------------------------------------
id: 2017-01-01_li-2017-cancer-cell-fto-plays-an-oncogen
id_basis: filename-year
source: Li(2017) Cancer Cell; FTO Plays an Oncogenic Role in Acute Myeloid Leukemia as a N6-Methyladenosine RNA Demethylase.pdf
sha256: ebcd9fd94ce82e8f49e9f214a4045e9f85398ee01dcaddd7c820d4a0f0d29280
size_bytes: 6512194
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 93341

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2016.11.017"
year: 2017
title: "FTO Plays an Oncogenic Role in Acute Myeloid Leukemia as a N6-Methyladenosine RNA Demethylase"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Li(2017) Cancer Cell; FTO Plays an Oncogenic Role in Acute Myeloid Leukemia as a N-Methyladenosine RNA Demethylase.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

FTO, the first identified m6A RNA demethylase, is shown to have a critical oncogenic role in AML. It is highly expressed in AML with MLL rearrangement, PML-RARA, FLT3-ITD and/or NPM1 mutations, enhances leukemic oncogene-mediated transformation and leukemogenesis, and inhibits all-trans-retinoic acid-induced differentiation, by reducing m6A levels on target transcripts including ASB2 and RARA and thereby lowering their expression.

## Summary

The paper that established m6A as a cancer-relevant regulatory layer in AML, and did so on the eraser side - showing that removing a mark, not just placing it, can be oncogenic. FTO is upregulated downstream of several unrelated oncogenic lesions, which is what makes it a convergence point rather than a subtype-specific finding.

The ATRA connection is the clinically pointed part: FTO represses RARA, the receptor ATRA acts through, so an RNA modification enzyme sets the sensitivity of APL cells to differentiation therapy, and knocking it down enhances differentiation at a tenth of the usual ATRA concentration. The authors are also careful about what they have not resolved - they test YTHDF1 and YTHDF2 as candidate readers, find neither explains the mRNA stability effect, and state plainly that the relevant reader remains unidentified.

## Key points

- FTO, an m6A demethylase, is oncogenic in AML - establishing that erasing an RNA mark can drive cancer.
- Upregulated downstream of several unrelated lesions: MLL rearrangement, PML-RARA, FLT3-ITD, NPM1 mutation.
- Acts by demethylating ASB2 and RARA transcripts, reducing their expression.
- Represses RARA and thereby blocks ATRA-induced differentiation; FTO knockdown enhances differentiation at low ATRA.
- The m6A reader responsible for the stability effect is explicitly not identified - YTHDF1 and YTHDF2 were excluded.

## Limitations

The mechanistic chain has an acknowledged gap: the reader that recognises these m6A sites and promotes transcript stability is unknown, so how demethylation changes mRNA fate is not explained. m6A mapping of this era is antibody-based (MeRIP-seq) with limited resolution, so individual methylation sites on ASB2 and RARA are not precisely localised. Much of the functional work uses forced overexpression and knockdown in cell lines and transformation assays rather than physiological models. FTO is a broadly expressed enzyme with roles in metabolism and obesity - the gene is named for its obesity association - so systemic inhibition raises off-tumour concerns the paper does not address, and no inhibitor is tested here. The ATRA result is in APL lines (NB4), a subtype already curable, rather than in the AML subtypes where FTO is most relevant.

## Provenance

Located in the published literature, dropped into `inbox/` as `Li(2017) Cancer Cell; FTO Plays an Oncogenic Role in Acute Myeloid Leukemia as a N-Methyladenosine RNA Demethylase.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2016.11.017`; the prose sections were written here from the paper itself.

## Citation

Li et al. Cancer Cell 2017. FTO Plays an Oncogenic Role in Acute Myeloid Leukemia as a N6-Methyladenosine RNA Demethylase. doi: 10.1016/j.ccell.2016.11.017
