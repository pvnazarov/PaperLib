---
# --- identity ------------------------------------------------
id: 2026-01-01_fetsch-2026-blood-menin-inhibition-enhan
id_basis: filename-year
source: Fetsch(2026) Blood; Menin inhibition enhances graft-versus-leukemia effects by T-cell activation and endogenous retrovirus induction in AML.pdf
sha256: 94d564fdfb857bfa2f4bcdf97ffbde36f389e692632357fb81306d0366c4108c
size_bytes: 71760
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 2916

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2025029712"
year: 2026
title: "Menin inhibition enhances graft-versus-leukemia effects by T-cell activation and endogenous retrovirus induction in AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Fetsch(2026) Blood [abstract]; Menin inhibition enhances graft-versus-leukemia effects by T-cell activation and endogenous retrovirus induction in AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Menin inhibition is shown to have an immunological mechanism in addition to its antileukemic one. In KMT2A-rearranged and NPM1-mutated AML cells, in vitro and in vivo, it induces class II transactivator and MHC-II expression, sensitising cells to T-cell-mediated elimination after allogeneic transplant in mice and enhancing the graft-versus-leukemia effect in human xenografts. Mechanistically it increases expression of multiple human endogenous retroviruses, driving interferon-stimulated gene upregulation and MHC-II expression. It also acts directly on donor T cells, raising TNF-alpha, interferon-gamma, perforin and granzyme A/B production and cytolytic activity, and reducing T-cell exhaustion and menin-KMT2A binding at genes encoding negative regulators of T-cell activation.

## Summary

A two-sided mechanism for a drug class already in the clinic, aimed at the specific problem that KMT2A-rearranged AML relapses after allogeneic transplant. The leukemia side is viral mimicry - derepressed endogenous retroviruses triggering interferon signalling and MHC-II - which makes the blast visible to donor T cells. The T cell side is separate and arguably more surprising: menin inhibition acts on the donor T cells themselves, reducing exhaustion and increasing cytotoxic output.

If both hold, the clinical implication is specific and testable - menin inhibition as post-transplant maintenance, which is what the authors propose.

## Key points

- Menin inhibition induces CIITA and MHC-II on KMT2A-rearranged and NPM1-mutated AML cells, sensitising them to donor T cells.
- The mechanism is viral mimicry: derepressed human endogenous retroviruses drive interferon-stimulated genes and MHC-II.
- A separate, direct effect on donor T cells increases TNF-alpha, IFN-gamma, perforin and granzyme A/B and reduces exhaustion.
- Menin-KMT2A binds genes encoding negative regulators of T-cell activation, and inhibition reduces that binding.
- Provides a rationale for menin inhibition as maintenance therapy after allogeneic transplant.

## Limitations

THE FILE IN raw/ IS NOT THE PAPER. It states so itself: a bibliographic record carrying the PubMed abstract, generated on 2026-09-08 by make_abstract_pdf.py for the AML review literature base because no full text could be obtained. Everything recorded here comes from that abstract, so no figure, method, effect size, statistical test or control can be checked, and the ingest flagged the file as short and thin. Beyond that, and judging only from the abstract: the models are mouse transplant and human xenograft systems, in which graft-versus-leukemia is reconstructed rather than observed clinically, and xenograft T-cell biology is an imperfect model of allogeneic immunity in patients. Whether MHC-II induction also increases graft-versus-host disease - the mirror risk of any intervention that enhances GVL - is not addressed in the abstract. The clinical trial is proposed, not performed.

## Provenance

Located in the published literature, dropped into `inbox/` as `Fetsch(2026) Blood [abstract]; Menin inhibition enhances graft-versus-leukemia effects by T-cell activation and endogenous retrovirus induction in AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2025029712`; the prose sections were written here from the paper itself.

## Citation

Fetsch et al. Blood 2026. Menin inhibition enhances graft-versus-leukemia effects by T-cell activation and endogenous retrovirus induction in AML. doi: 10.1182/blood.2025029712
