---
# --- identity ------------------------------------------------
id: 2024-01-01_bo-t-2024-cancer-research-targeting-meta
id_basis: filename-year
source: Boët(2024) Cancer Research; Targeting Metabolic Dependencies Fueling the TCA Cycle to Circumvent Therapy Resistance in Acute Myeloid Leukemia.pdf
sha256: 018bf82a77402c88e2d56b3230620b36660cf89026ab6b85895504de418cf807
size_bytes: 71460
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 2604

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/0008-5472.CAN-24-0019"
year: 2024
title: "Targeting Metabolic Dependencies Fueling the TCA Cycle to Circumvent Therapy Resistance in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Boët(2024) Cancer Res [abstract]; Targeting Metabolic Dependencies Fueling the TCA Cycle to Circumvent Therapy Resistance in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A commentary in Cancer Research on two studies of AML dependence on respiratory substrates that feed oxidative phosphorylation: alpha-ketoglutarate and lactate-derived pyruvate. It frames the problem as relapse-initiating cells surviving through nongenetic, metabolic adaptation - leukemic stem cells relying on mitochondrial metabolism where hematopoietic stem cells rely on glycolysis, with cytarabine-persisting cells further enriched for mitochondrial dependence. Interfering with lactate utilisation through MCT1/SLC16A1 or lactate dehydrogenase sensitised cells to the BET inhibitor INCB054329 in vitro and in vivo, while the imipridone ONC-213 acted on alpha-KGDH to induce an ATF4-mediated mitochondrial stress response that lowered MCL1 and promoted apoptosis.

## Summary

A short editorial commentary rather than primary research, useful here as a compact statement of the OxPHOS-dependence thesis that several papers in this collection argue from different directions. It names the therapeutic asymmetry the whole strategy rests on - LSCs mitochondrial, normal HSCs glycolytic - which is what makes targeting oxidative metabolism conceivable rather than uniformly toxic.

It also connects two otherwise unrelated interventions, a BET inhibitor and an imipridone, by their shared metabolic consequence, which is the point of the piece: the drugs differ, the dependency they expose is the same.

## Key points

- Frames resistance in AML as substantially nongenetic and metabolic, not only mutational.
- States the asymmetry the strategy depends on: LSCs rely on mitochondrial metabolism, normal HSCs primarily on glycolysis.
- Cytarabine-persisting cells show enhanced mitochondrial reliance, consistent with the Farge and Aroua work in this collection.
- Blocking lactate use via MCT1/SLC16A1 or LDH sensitises AML cells to BET inhibition in vitro and in vivo.
- ONC-213 inhibits alpha-KGDH, triggering an ATF4 mitochondrial stress response that reduces MCL1 and promotes apoptosis.

## Limitations

THE FILE IN raw/ IS NOT THE PAPER. It states so itself: a one-page bibliographic record carrying the PubMed abstract, generated on 2026-09-08 by make_abstract_pdf.py for the AML review literature base because no full text could be obtained. Everything above is drawn from that abstract, so the record cannot be checked against the article's own text, figures or references, and the ingest flagged it as short and thin. Beyond that, the piece is a commentary: it reports no original data, its account of the two underlying studies is second-hand and selective, and commentaries in the same issue are written to advocate for the work they introduce. The mechanistic claims belong to Monteith et al. and Su et al., which should be cited for them.

## Provenance

Located in the published literature, dropped into `inbox/` as `Boët(2024) Cancer Res [abstract]; Targeting Metabolic Dependencies Fueling the TCA Cycle to Circumvent Therapy Resistance in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/0008-5472.CAN-24-0019`; the prose sections were written here from the paper itself.

## Citation

Boët et al. Cancer Research 2024. Targeting Metabolic Dependencies Fueling the TCA Cycle to Circumvent Therapy Resistance in Acute Myeloid Leukemia. doi: 10.1158/0008-5472.CAN-24-0019
