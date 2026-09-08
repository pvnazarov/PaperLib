---
# --- identity ------------------------------------------------
id: 2022-01-01_lin-2022-nature-cancer-p2ry2-akt-activat
id_basis: filename-year
source: Lin(2022) Nature Cancer; P2RY2-AKT activation is a therapeutically actionable consequence of XPO1 inhibition in acute myeloid leukemia.pdf
sha256: b367a2c6a6d79cb8d2a53a1a50927d2c6ec7c4e5d483024d99d8e0a261e6d2a2
size_bytes: 14156582
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 251146

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s43018-022-00394-x"
year: 2022
title: "P2RY2-AKT activation is a therapeutically actionable consequence of XPO1 inhibition in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lin(2022) Nat Cancer; P2RY2-AKT activation is a therapeutically actionable consequence of XPO1 inhibition in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Systematically cataloguing the pro- and anti-fitness consequences of selinexor treatment in AML, the authors find that the XPO1 inhibitor activates PI3K-gamma-dependent AKT signalling by upregulating the purinergic receptor P2RY2. Inhibiting this axis potentiates selinexor's anti-leukemic effects in cell lines, patient-derived primary cultures and multiple mouse models. In a syngeneic MLL-AF9 model, selinexor plus the AKT inhibitor ipatasertib outperformed both standard-of-care chemotherapy and chemotherapy plus selinexor, and reduced leukemia-initiating cell burden.

## Summary

Built on a premise that deserves wider adoption: a pleiotropic drug like selinexor, which sequesters many substrates in the nucleus, will have both helpful and harmful consequences, and cataloguing the harmful ones systematically identifies rational combinations. Most combination studies screen for synergy; this one predicts it from the drug's own resistance mechanism.

What it finds is that selinexor induces its own escape route - transcriptional upregulation of P2RY2 driving PI3K-gamma-dependent AKT signalling - and blocking that converts a partially effective drug into a substantially better one. The comparison chosen for the in vivo test is the demanding one: selinexor plus ipatasertib against maximally tolerated standard-of-care chemotherapy, not against vehicle, and it wins on survival and on leukemia-initiating cell burden.

## Key points

- Selinexor activates PI3K-gamma-dependent AKT signalling in AML by transcriptionally upregulating P2RY2 - a drug-induced resistance mechanism.
- The approach is to catalogue a pleiotropic drug's pro-fitness consequences and target them, rather than screen empirically for synergy.
- Co-inhibiting AKT potentiates selinexor across cell lines, patient-derived primary cultures and three mouse models.
- In a syngeneic MLL-AF9 model, selinexor plus ipatasertib beat maximally tolerated standard-of-care chemotherapy on survival.
- The combination also reduced leukemia-initiating cell burden, not only bulk disease.

## Limitations

Preclinical. Selinexor's own clinical record in AML is of a tolerable but modestly active agent, and adding an AKT inhibitor compounds toxicity - selinexor causes substantial gastrointestinal and hematologic adverse effects, and AKT inhibitors bring hyperglycaemia and rash, so the combination's tolerability in patients is the unaddressed question. Synergy is measured largely by short-term viability assays with interpolated GI50 values, which is sensitive to assay and dose choice. The syngeneic MLL-AF9 model is one genetic context; whether the P2RY2-AKT response occurs across AML genotypes is not established at the same depth. Efficacy readouts are survival in mice, not the disease-free durability the comparison with chemotherapy implies.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lin(2022) Nat Cancer; P2RY2-AKT activation is a therapeutically actionable consequence of XPO1 inhibition in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s43018-022-00394-x`; the prose sections were written here from the paper itself.

## Citation

Lin et al. Nature Cancer 2022. P2RY2-AKT activation is a therapeutically actionable consequence of XPO1 inhibition in acute myeloid leukemia. doi: 10.1038/s43018-022-00394-x
