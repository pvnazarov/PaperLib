---
# --- identity ------------------------------------------------
id: 2026-01-01_mahdavi-2026-experimental-hematology-upf
id_basis: filename-year
source: Mahdavi(2026) Experimental Hematology; Upfront menin-inhibitor resistance in multiply pretreated leukemias.pdf
sha256: bb5427e23627a17185be9c6805164e3da54253af193c592d3cecc625196099fd
size_bytes: 1240992
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 38682

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.exphem.2025.105268"
year: 2026
title: "Upfront menin-inhibitor resistance in multiply pretreated leukemias"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Mahdavi(2026) Exp Hematol; Upfront menin-inhibitor resistance in multiply pretreated leukemias.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Menin inhibition was evaluated in patient-derived xenografts of KMT2A-rearranged leukemias with high-risk features. Three AMLs with high-risk fusion partners (MLLT10, MLLT4) and two infant ALL samples were sensitive. In serial samples from two patients with multiply relapsed ALL, heavily pretreated KMT2A::AFF1 samples were much less sensitive than cells obtained earlier in the same patients' course - and since none had received a menin inhibitor, this resistance was acquired without menin-inhibitor exposure. Transcriptomic analysis showed sustained on-target efficacy against canonical menin inhibitor targets in resistant cells; genomic analysis found emergent RAS pathway and TP53 comutations, neither sufficient to cause resistance in vitro, with KMT2D downregulation a candidate mechanism in one patient.

## Summary

The most clinically consequential observation in the menin inhibitor literature collected here, and it is a negative one: resistance can be present before the drug is ever given. Serial samples from the same patients show sensitivity early and resistance late, with no menin inhibitor in between, so prior therapy alone drives the leukemia into a resistant state.

The mechanistic dissection is careful in what it rules out. The drug still works on target - canonical menin inhibitor targets respond transcriptionally in resistant cells - so this is not failure of target engagement but downstream indifference. RAS pathway and TP53 mutations emerged but neither was sufficient to confer resistance when tested, and KMT2D downregulation is offered as a candidate in one patient, with KMT2C-edited cells from that patient selected for under drug. The authors are explicit that the broader mechanism is unresolved, and draw the actionable conclusion regardless: give these drugs early.

## Key points

- Resistance to menin inhibition arose in heavily pretreated KMT2A::AFF1 ALL without any prior menin-inhibitor exposure.
- Serial samples from the same patients show sensitivity early and resistance late - prior therapy, not drug pressure, drove it.
- Resistance is not loss of target engagement: canonical menin inhibitor targets still respond transcriptionally in resistant cells.
- Emergent RAS pathway and TP53 mutations were insufficient to confer resistance in vitro; KMT2D downregulation is a candidate in one patient.
- Supports using menin inhibitors upfront or in early lines, before substantial genomic and epigenomic evolution.

## Limitations

Very small: three AML and two infant ALL PDXs for the sensitivity arm, and serial samples from two patients for the central resistance observation, with the KMT2D mechanism proposed for one of them. The authors state plainly that future studies must clarify which genomic or epigenomic alterations drive upfront resistance - so the phenomenon is documented without an established mechanism. Most of the resistance data come from ALL rather than AML, which limits transfer to the AML setting most of this collection concerns. PDX models in immunodeficient mice omit the immune contribution to response. One author is employed by Syndax Pharmaceuticals, which develops revumenib, though the finding here is unfavourable to that drug class's use in late lines.

## Provenance

Located in the published literature, dropped into `inbox/` as `Mahdavi(2026) Exp Hematol; Upfront menin-inhibitor resistance in multiply pretreated leukemias.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.exphem.2025.105268`; the prose sections were written here from the paper itself.

## Citation

Mahdavi et al. Experimental Hematology 2026. Upfront menin-inhibitor resistance in multiply pretreated leukemias. doi: 10.1016/j.exphem.2025.105268
