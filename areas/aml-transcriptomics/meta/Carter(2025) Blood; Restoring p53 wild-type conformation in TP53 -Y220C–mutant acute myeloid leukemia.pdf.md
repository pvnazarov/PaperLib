---
# --- identity ------------------------------------------------
id: 2025-01-01_carter-2025-blood-restoring-p53-wild-typ
id_basis: filename-year
source: Carter(2025) Blood; Restoring p53 wild-type conformation in TP53 -Y220C–mutant acute myeloid leukemia.pdf
sha256: eca47b39c8800ffb46c6bd93318be027b10f67996ea3766dc3a4bb857be4f577
size_bytes: 3302941
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 84462

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2025028935"
year: 2025
title: "Restoring p53 wild-type conformation in TP53 -Y220C–mutant acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Carter(2025) Blood; Restoring p53 wild-type conformation in TP53-Y220C-mutant acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

PC14586 (rezatapopt), a small molecule designed to bind the structural pocket created by the TP53-Y220C hotspot mutation, is shown to convert p53-Y220C to a wild-type conformation and activate p53 transcriptional targets - but to induce little apoptosis in TP53-Y220C AML. Two mechanisms limit it: MDM2 induced by the reactivated protein and XPO1-mediated nuclear export reduce transcriptional activity, and unlike native p53 the reactivated protein does not bind BCL-2, BCL-xL or MCL-1, so the transcription-independent apoptotic route is missing. Venetoclax compensates for the latter, inducing massive death of AML cells and stem/progenitor cells in vitro and prolonging survival of xenografts; a clinical trial in TP53-Y220C AML/MDS has begun (NCT06616636).

## Summary

A paper whose value lies in explaining a partial failure rather than announcing a success. Restoring the wild-type conformation of mutant p53 does what it says on the tin - the conformation converts, the transcriptional targets switch on - and the cells largely do not die. The authors pursue why, and the answer is that p53 kills through two routes and only one is restored.

The transcription-independent route is the interesting half: native p53 binds BCL-2 and competes with BAX in its BH3 pocket, and also binds BCL-xL and MCL-1, and the reactivated protein does none of this. That is a structural difference between native and pharmacologically restored p53 which the authors say remains unexplained, and it is the reason the venetoclax combination is not an add-on but a mechanistic complement. They are also frank about a risk that follows from the drug's specificity: PC14586 has no activity against other TP53 mutants, so it may select for non-Y220C subclones, exactly as MDM2 inhibition does.

## Key points

- PC14586 restores the wild-type p53 conformation and transcriptional activity in TP53-Y220C AML but induces little apoptosis on its own.
- MDM2 induction and XPO1-mediated nuclear export blunt the restored transcriptional activity; inhibiting either restores it fully.
- Reactivated p53, unlike native p53, fails to bind BCL-2, BCL-xL and MCL-1, so the transcription-independent apoptotic mechanism is absent.
- Venetoclax substitutes for that missing function, producing extensive killing including of stem/progenitor cells, and prolonging xenograft survival.
- The drug is inactive against other TP53 mutations, supporting Y220C as a selection biomarker but raising the risk of selecting non-Y220C subclones.

## Limitations

Preclinical throughout, with the clinical trial only just initiated at publication. The specificity that makes Y220C a clean biomarker also narrows the population sharply - the authors report about 25% of TP53-Y220C AML/MDS carry only that mutation - and they show directly that a TP53-Y220C/P151A co-mutant PDX responds poorly because the P151A subclone is untouched. Subclone selection under treatment is raised as a real risk and demonstrated by scDNA-seq, not merely speculated. Two authors received research funding from PMV, two are PMV employees and one sits on its board, which is disclosed; the drug is PMV's. Survival prolongation is in xenografts, and the structural basis for reactivated p53's failure to bind BCL-2 family proteins - the paper's most novel mechanistic claim - is left unresolved.

## Provenance

Located in the published literature, dropped into `inbox/` as `Carter(2025) Blood; Restoring p53 wild-type conformation in TP53-Y220C-mutant acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2025028935`; the prose sections were written here from the paper itself.

## Citation

Carter et al. Blood 2025. Restoring p53 wild-type conformation in
                    <i>TP53</i>
                    -Y220C–mutant acute myeloid leukemia. doi: 10.1182/blood.2025028935
