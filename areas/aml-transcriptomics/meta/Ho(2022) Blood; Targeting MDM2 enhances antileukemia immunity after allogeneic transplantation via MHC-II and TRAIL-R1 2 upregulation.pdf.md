---
# --- identity ------------------------------------------------
id: 2022-01-01_ho-2022-blood-targeting-mdm2-enhances-an
id_basis: filename-year
source: Ho(2022) Blood; Targeting MDM2 enhances antileukemia immunity after allogeneic transplantation via MHC-II and TRAIL-R1 2 upregulation.pdf
sha256: 6799d9f1cfccb7991b28c875615229ea4c312f83812c09c4d6d2d92de79b0ba2
size_bytes: 1894602
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 172106

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2022016082"
year: 2022
title: "Targeting MDM2 enhances antileukemia immunity after allogeneic transplantation via MHC-II and TRAIL-R1/2 upregulation"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ho(2022) Blood; Targeting MDM2 enhances antileukemia immunity after allogeneic transplantation via MHC-II and TRAIL-R1 2 upregulation.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

AML relapse after allogeneic transplant is driven by leukemia cells resistant to allogeneic T cells through decreased MHC class II expression and apoptosis resistance. MDM2 inhibition is shown to counteract this immune evasion, inducing MHC class I and II expression in murine and human AML and upregulating TRAIL-R1/R2 in a p53-dependent manner, which was confirmed in primary human AML and post-transplant relapse samples. Blocking TRAIL, using TRAIL-deficient donor T cells, or knocking out TRAIL-R2 each reduced the protective effect in vivo, and depletion of CD8+ T cells but not NK cells abrogated it.

## Summary

Directly targets the mechanism by which AML escapes graft-versus-leukemia - loss of MHC-II on the blast, a well-documented cause of post-transplant relapse - and restores it pharmacologically. The two arms are complementary rather than redundant: MHC-II restores recognition, TRAIL-R1/2 restores the ability to be killed once recognised.

The genetic dissection is the strongest part. Anti-TRAIL antibody, TRAIL-deficient donor T cells, CRISPR TRAIL-R2 knockout AML, and selective depletion of CD8+ T cells versus NK cells each remove a specific component and each reduces the effect, so the pathway is established by four independent perturbations rather than asserted from correlation. Confirming TRAIL-R1/2 and p53 induction in actual post-transplant relapse samples anchors it to the clinical setting it is meant for.

## Key points

- MDM2 inhibition restores MHC class I and II on AML cells, reversing a documented mechanism of post-transplant immune escape.
- It also upregulates TRAIL-R1/R2 in a p53-dependent way, restoring susceptibility to T-cell killing.
- Verified in primary human AML and, importantly, in post-transplant relapse samples.
- The pathway is confirmed by four independent perturbations: anti-TRAIL antibody, TRAIL-deficient donor T cells, TRAIL-R2 knockout AML, and CD8 depletion.
- The effect is mediated by CD8+ T cells, not NK cells.

## Limitations

The mechanism is p53-dependent, which excludes TP53-mutant AML - a group with the worst outcomes, and one enriched at relapse and under MDM2-inhibitor pressure, since MDM2 inhibition is itself known to select TP53-mutant clones. That selection risk is not addressed. Efficacy is in mouse transplant models; the human data are ex vivo induction of the relevant molecules rather than clinical benefit. Enhancing allogeneic T-cell activity raises the question of graft-versus-host disease, the mirror image of the desired graft-versus-leukemia effect, which the summary evidence does not resolve. Patient sample numbers for the confirmatory analyses are modest (22 and 12 patients). One author is employed by Novartis, which develops the MDM2 inhibitor HDM201 used here.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ho(2022) Blood; Targeting MDM2 enhances antileukemia immunity after allogeneic transplantation via MHC-II and TRAIL-R1 2 upregulation.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2022016082`; the prose sections were written here from the paper itself.

## Citation

Ho et al. Blood 2022. Targeting MDM2 enhances antileukemia immunity after allogeneic transplantation via MHC-II and TRAIL-R1/2 upregulation. doi: 10.1182/blood.2022016082
