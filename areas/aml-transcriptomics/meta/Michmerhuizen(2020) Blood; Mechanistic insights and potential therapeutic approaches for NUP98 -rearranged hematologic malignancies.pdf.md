---
# --- identity ------------------------------------------------
id: 2020-01-01_michmerhuizen-2020-blood-mechanistic-ins
id_basis: filename-year
source: Michmerhuizen(2020) Blood; Mechanistic insights and potential therapeutic approaches for NUP98 -rearranged hematologic malignancies.pdf
sha256: fe4976f85a31ff0e253eb86cfd025ac396d6024ebe26f0d6fa93be49bfeb6b78
size_bytes: 1565693
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 131057

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2020007093"
year: 2020
title: "Mechanistic insights and potential therapeutic approaches for NUP98 -rearranged hematologic malignancies"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Michmerhuizen(2020) Blood; Mechanistic insights and potential therapeutic approaches for NUP98-rearranged hematologic malignancies.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of NUP98 fusion oncoproteins, which occur across hematologic malignancies and particularly in pediatric leukemias with poor outcomes. The translocations join the intrinsically disordered N-terminal region of NUP98 to over 30 partner genes, many bearing homeodomains or with roles in transcriptional or epigenetic regulation. Leukemogenesis is mediated by changes in chromatin structure and gene expression, with multiple cofactors associating with the fusions - possibly via phase separation - in a partner-dependent manner. NUP98 fusions co-occur with additional mutations including FLT3-ITD. Therapeutic strategies considered target transcriptional and epigenetic machinery, cooperating alterations, and signalling or cell-cycle pathways.

## Summary

The reference account of a fusion family defined by its N-terminal partner rather than its C-terminal one - over 30 partners share the same intrinsically disordered NUP98 region, which is what supplies the phase-separation behaviour developed elsewhere in this collection.

The review is useful for the cofactor dissection, which is more careful than a summary usually is. CREBBP and EP300 both bind the FG/GLFG repeats, but they are not equivalent: losing CREBBP in NUP98-HOXD13 transgenic mice does not affect disease, and an elegant swap experiment - replacing the NUP98 portion with the EP300-interaction domain of adenovirus E1a - showed that EP300's acetyltransferase activity alone does not account for transformation. The authors are also explicit that a core transcriptional signature is shared across NUP98 fusions while partner-specific targets, which may explain lineage specificity, require further study.

## Key points

- Over 30 partner genes fuse to the same intrinsically disordered N-terminal NUP98 region, many bearing homeodomains.
- Leukemogenesis proceeds through chromatin and transcriptional change, possibly involving phase separation, with cofactor recruitment depending on the partner.
- CREBBP and EP300 are not interchangeable: CREBBP loss does not affect disease in NUP98-HOXD13 mice, and EP300 acetyltransferase activity alone does not explain transformation.
- NUP98 fusion binding sites overlap those of KMT2A and WDR-SET1-COMPASS complexes, and with H3K4 methylation and H4K16 acetylation.
- Co-occurring FLT3-ITD and other proliferative lesions are part of the disease, and are themselves candidate therapeutic targets.

## Limitations

A narrative review from 2020 without systematic search or evidence appraisal, and it predates the NUP98-specific menin inhibitor work in this collection. The authors note repeatedly that experimental systems for NUP98-rearranged disease are inadequate and that more faithful models are needed - so much of the mechanistic account rests on transgenic mouse models and transduced progenitors of uncertain fidelity. Partner-specific targets, which the review suggests explain lineage specificity, are flagged as requiring further study rather than established. Therapeutic strategies are surveyed as rationales; none had clinical efficacy data in NUP98-rearranged disease at the time. Some claims are extrapolated across models - MEIS2 upregulation, for instance, has not been directly tested in vivo in NUP98 fusion models.

## Provenance

Located in the published literature, dropped into `inbox/` as `Michmerhuizen(2020) Blood; Mechanistic insights and potential therapeutic approaches for NUP98-rearranged hematologic malignancies.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2020007093`; the prose sections were written here from the paper itself.

## Citation

Michmerhuizen et al. Blood 2020. Mechanistic insights and potential therapeutic approaches for
                    <i>NUP98</i>
                    -rearranged hematologic malignancies. doi: 10.1182/blood.2020007093
