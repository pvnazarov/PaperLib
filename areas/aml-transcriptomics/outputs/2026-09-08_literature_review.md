# AML transcriptomics — literature review: 186 papers by topic

> 2026-09-08 · area: AML transcriptomics · 186 papers in 21 topics, each paper in exactly one

## How to read this

Every paper in the collection, clustered by subject. 186 papers, 21 topics in 6 parts,
each paper in exactly one topic.

**The clustering is the only judgement in this document.** It was drawn by reading each paper's
title, abstract and key points and deciding where it belongs. The similarity vectors may
*propose* — per-topic cohesion, centroid overlap, papers that sit closer to another topic than
to their own — but proposing is all they do: they are TF-IDF over the summaries, so they group
by shared vocabulary rather than by subject, and vocabulary and subject part company more often
than is comfortable. Some topics here are deliberately low on vocabulary cohesion because their
subject is genuinely diverse.

**This is the FIRST clustering of this collection**, so there is no before-and-after to report.
When it is re-drawn, that revision belongs in `reports/` with the criteria written down *before*
any candidate taxonomy exists, and this block should be replaced with one that says so.

**What the parts follow.** The six parts are ordered by the layer at which the disease is
dysregulated, working outward from the initiating lesion. **A** is the driver itself — the fusion
proteins and recurrent mutations, and the transcriptional networks they build. **B** is the
chromatin those networks act on: the regulators co-opted to hold the differentiation block, the
methylation landscape, and the three-dimensional organisation that decides which element reaches
which promoter. **C** is what happens to the RNA after it is transcribed — splicing, isoform
choice, chemical modification — a layer this collection covers unusually heavily because AML
turns out to be dysregulated there even in the large majority of patients who carry no splicing
factor mutation. **D** is metabolism and cell death, where most of the collection's therapeutic
vulnerabilities are, and where its single most consequential result sits: the cells that survive
chemotherapy are metabolically distinct rather than developmentally primitive. **E** is the
cellular population structure — stem cells, hierarchies, and what changes at relapse. **F** is
the clinical surface: how the disease is diagnosed and stratified, and how it evades the immune
system.

**Three choices worth stating.** First, **t(8;21) is split across two topics** rather than kept
whole. One holds the mechanism of the fusion protein, the other holds what the leukemia needs in
order to persist; they are different questions with different literatures, and merging them would
produce a nineteen-paper topic in which the therapeutic papers disappear among the mechanistic
ones.

Second, **metabolism is separated from the BCL2 family** even though venetoclax resistance is
substantially metabolic. The reason is that the venetoclax papers form a coherent argument with
each other — about who responds, and whether monocytic differentiation predicts it — and that
argument is legible only if they sit together.

Third, **functional genomics screens are a topic rather than a method note.** Five papers here
are read for what they say about screening itself: that an in vivo screen finds targets an in
vitro screen structurally cannot, that primary cells and cell lines give different answers, and
that filtering hits against human loss-of-function genetics before believing them is what
produced the one target in this collection whose therapeutic window is established in humans
rather than in mice.

**Where the seams are.** Six papers could defensibly sit elsewhere, and are named here rather
than left for a reader to notice. **Gerritsen (2019)** studies RUNX1 point mutations, not the
fusion, and is filed under t(8;21) dependencies because what it measures is the difference
between the two. **Saika (2026)** runs from a splicing factor mutation through chromatin to
ferroptosis and is filed under splicing rather than metabolism, because SF3B1 is where its causal
chain starts. **Chang (2024)** is a SETDB1 chromatin paper filed under immunotherapy, because the
dependency it finds exists only in an immunocompetent animal and is about NK recognition.
**Tirtakusuma (2022)** and **Mimura (2026)** are lymphoid diseases — an MLL/AF4 B-ALL and a T-ALL
— kept here for their lineage-switching and enhancer-hijacking mechanisms. **Zhou (2025)** is a
Data in Brief dataset description with no findings at all, filed under long-read transcriptomics
as the resource it is.

**Three files in `raw/` are not the papers.** Boët (2024), Fetsch (2026) and Lin (2017) are
one-page bibliographic records carrying a PubMed abstract, generated on 2026-09-08 by
`make_abstract_pdf.py` because no full text could be obtained. They say so in their own text,
their sidecars say so under Limitations, and nothing in their records can be checked against a
figure, a method or a reference list.

Everything else is mechanical:

| Element | Where it comes from |
|---|---|
| first author, year, journal, title | the publisher's own registration via Crossref or arXiv, keyed on a DOI or arXiv ID verified against the paper's bytes — or, for the papers that register nowhere, the paper's own first page |
| DOI / arXiv ID | the sidecar's `doi:` field |
| summary | the sidecar's `## Abstract` — written once at ingest from the source's own extracted text |
| `[src]` link | the source file in `raw/` |

**The summaries are paraphrases, not quotations, and this document is not a source.** Each entry
links the paper itself; a claim you intend to rely on must be checked there.

**Author lists are deliberately incomplete here.** Each entry names the registered first author
and `et al.`, never a reconstructed list. Full, verified lists exist for 0 of 186
papers, in `data/bib_cache.json` and searchable in the browser; they are not repeated here
because an entry heading is a citation, not a byline.

## Contents

**A. Fusion oncoproteins and rearranged leukaemia** — 54 papers  
  · [RUNX1::RUNX1T1 and the t(8;21) regulatory network](#runx1runx1t1-and-the-t821-regulatory-network) (10)  
  · [t(8;21): dependencies, cooperating lesions and stem cells](#t821-dependencies-cooperating-lesions-and-stem-cells) (9)  
  · [KMT2A rearrangement and the menin-MLL axis](#kmt2a-rearrangement-and-the-menin-mll-axis) (16)  
  · [NPM1 mutation: mislocalisation, chromatin and HOX](#npm1-mutation-mislocalisation-chromatin-and-hox) (9)  
  · [NUP98, DEK::NUP214, EVI1 and other rearrangements](#nup98-deknup214-evi1-and-other-rearrangements) (10)  

**B. Chromatin, transcription and genome architecture** — 26 papers  
  · [Chromatin regulators and readers as therapeutic dependencies](#chromatin-regulators-and-readers-as-therapeutic-dependencies) (12)  
  · [DNA methylation, TET/IDH and the mutational landscape](#dna-methylation-tetidh-and-the-mutational-landscape) (6)  
  · [Chromatin accessibility and 3D genome organisation](#chromatin-accessibility-and-3d-genome-organisation) (8)  

**C. RNA processing: splicing, isoforms and modification** — 38 papers  
  · [Splicing factor mutations and splicing-directed therapy](#splicing-factor-mutations-and-splicing-directed-therapy) (10)  
  · [Splicing regulators and RNA-binding proteins as dependencies](#splicing-regulators-and-rna-binding-proteins-as-dependencies) (12)  
  · [m6A and the epitranscriptome](#m6a-and-the-epitranscriptome) (8)  
  · [Long-read transcriptomics, circular and chimeric RNAs](#long-read-transcriptomics-circular-and-chimeric-rnas) (8)  

**D. Metabolism, mitochondria and cell death** — 32 papers  
  · [Oxidative metabolism and chemoresistance](#oxidative-metabolism-and-chemoresistance) (10)  
  · [BCL2 family dependencies and venetoclax response](#bcl2-family-dependencies-and-venetoclax-response) (7)  
  · [Lipid, amino acid and cofactor metabolism as vulnerabilities](#lipid-amino-acid-and-cofactor-metabolism-as-vulnerabilities) (6)  
  · [TP53 alteration and complex karyotype](#tp53-alteration-and-complex-karyotype) (9)  

**E. Stem cells, heterogeneity and disease evolution** — 14 papers  
  · [Leukaemic stem cells, dormancy and relapse](#leukaemic-stem-cells-dormancy-and-relapse) (7)  
  · [Single-cell atlases of AML heterogeneity](#single-cell-atlases-of-aml-heterogeneity) (7)  

**F. Diagnosis, stratification and immunotherapy** — 22 papers  
  · [Transcriptome-based diagnosis, classification and risk](#transcriptome-based-diagnosis-classification-and-risk) (10)  
  · [Immunotherapy, immune evasion and the microenvironment](#immunotherapy-immune-evasion-and-the-microenvironment) (7)  
  · [Functional genomics screens as target-discovery platforms](#functional-genomics-screens-as-target-discovery-platforms) (5)  

---

# A. Fusion oncoproteins and rearranged leukaemia

## RUNX1::RUNX1T1 and the t(8;21) regulatory network

*10 papers.* How the most common AML fusion rewires transcription: what it binds, which cofactors it brings, and how it activates as well as represses. The subtype with the most complete mechanistic account in this collection, and the one where that account is still being revised.

### Grinev (2021). *Nature Communications.* RUNX1/RUNX1T1 mediates alternative splicing and reorganises the transcriptional landscape in leukemia
[doi:10.1038/s41467-020-20848-z](https://doi.org/10.1038/s41467-020-20848-z) · `paper`  
[src](<../raw/Grinev(2021) Nature Communications; RUNX1 RUNX1T1 mediates alternative splicing and reorganises the transcriptional landscape in leukemia.pdf>)

The fusion oncogene RUNX1/RUNX1T1 is shown to regulate alternative RNA splicing in leukemic cells. Comprehensive analysis of associated splicing events identifies two mechanisms: regulation of alternative transcription start site selection, which produces isoforms with alternative 5'-UTR structures, and direct or indirect control of genes encoding splicing factors, which generates alternative junctions between internal cassette and constitutive exons. The differential splicing affects several functional groups of genes and produces proteins with distinct conserved domain structures, establishing alternative splicing as a component of transcriptome reorganisation by an aberrant transcriptional regulator.

### Rejeski (2021). *Oncogene.* AML1/ETO and its function as a regulator of gene transcription via epigenetic mechanisms
[doi:10.1038/s41388-021-01952-w](https://doi.org/10.1038/s41388-021-01952-w) · `paper`  
[src](<../raw/Rejeski(2021) Oncogene; AML1 ETO and its function as a regulator of gene transcription via epigenetic mechanisms.pdf>)

A review of AML1/ETO in t(8;21) leukemogenesis, focused on aberrant epigenetic regulation of transcription. It covers how genomic breakpoints, splice variants and post-translational modifications shape protein function; how the oncofusion recruits chromatin-modifying enzymes and alters chromatin marks, transcription factor binding and gene expression; the impact of these changes on leukemic growth; the genetic landscape of cooperating mutations in KIT, FLT3, NRAS, ASXL1 and ASXL2; and how the resulting transcriptional alterations create vulnerabilities exploitable by epigenetically active agents.

### Stengel (2021). *Molecular Cell.* Definition of a small core transcriptional circuit regulated by AML1-ETO
[doi:10.1016/j.molcel.2020.12.005](https://doi.org/10.1016/j.molcel.2020.12.005) · `paper`  
[src](<../raw/Stengel(2021) Molecular Cell; Definition of a small core transcriptional circuit regulated by AML1-ETO.pdf>)

Cell models were devised in which the AML1-ETO protein is rapidly degraded on addition of a small molecule. Combining that rapid kinetics with nascent transcript analysis by PRO-seq and genome-wide AML1-ETO binding by CUT&RUN identified the direct gene targets constituting a core AML1-ETO regulatory network, distinguishing them from secondary and compensatory changes. Derepression of this network was associated with RUNX1 DNA binding and triggered a transcriptional cascade ending in myeloid differentiation. GFI1B was reactivated on degradation in differentiating pre-leukemic CD34+ cultures but not in the t(8;21) cell line, where it is marked by H3K27me3.

### Swart (2021). *Experimental Hematology.* The RUNX1/RUNX1T1 network: translating insights into therapeutic options
[doi:10.1016/j.exphem.2020.11.005](https://doi.org/10.1016/j.exphem.2020.11.005) · `paper`  
[src](<../raw/Swart(2021) Experimental Hematology; The RUNX1 RUNX1T1 network translating insights into therapeutic options.pdf>)

A review of the RUNX1/RUNX1T1 regulatory network in the most common fusion gene of AML. It describes how perturbing fusion levels and DNA binding alters chromatin accessibility, transcription factor occupancy and gene expression at many loci; how targeted RNAi screens of that transcriptional program uncovered a crucial role in cell cycle progression through CCND2; and how this dependency creates vulnerability to CDK4 and CDK6 inhibitors. It also covers effects on ribosomal protein and rRNA expression, alternative promoter usage, and miRNA-mediated control of mRNA translation and stability.

### Ptasinska (2019). *Cell Reports.* RUNX1-ETO Depletion in t(8;21) AML Leads to C/EBPα- and AP-1-Mediated Alterations in Enhancer-Promoter Interaction
[doi:10.1016/j.celrep.2019.08.040](https://doi.org/10.1016/j.celrep.2019.08.040) · `paper`  
[src](<../raw/Ptasinska(2019) Cell Reports; RUNX1-ETO Depletion in t(8,21) AML Leads to C EBPα- and AP-1-Mediated Alterations in Enhancer-Promoter Interaction.pdf>)

Promoter-Capture Hi-C, gene expression and transcription factor binding data are combined to construct a RUNX1-ETO-dependent dynamic gene regulatory network in t(8;21) AML. The approach links AML-specific cis-elements to their correct promoters and shows that RUNX1-ETO itself participates in cis-regulatory element interactions. After RUNX1-ETO depletion, gained interactions are associated with increased C/EBPalpha and RUNX1 binding while lost interactions involve loss of JUND and LDB1; gained interactions did not involve LMO2 or PU.1, and lost interactions did not involve CTCF. CITED2 is given as an example of a gene with a new C/EBPalpha-driven interaction, and CCND2 as a downregulated AP-1-dependent example.

### Tian (2018). *Journal of Cellular Biochemistry.* AML1/ETO trans‐activates c‐KIT expression through the long range interaction between promoter and intronic enhancer
[doi:10.1002/jcb.26587](https://doi.org/10.1002/jcb.26587) · `paper`  
[src](<../raw/Tian(2018) Journal of Cellular Biochemistry; AML1 ETO trans‐activates c‐KIT expression through the long range interaction between promoter and intronic enhancer.pdf>)

AML1/ETO is documented mainly as a transcriptional repressor, and this study examines its transactivation mechanism at c-KIT, which is highly expressed in t(8;21) AML. ChIP-seq and motif scanning identified regulatory regions in the c-KIT promoter and an intronic enhancer, both enriched for AML1/ETO co-factors including AML1, CEBPe, c-Jun and c-Fos. Luciferase reporter assays show AML1/ETO transactivates the promoter through the AML1 motif with co-factors present, and that activity is reinforced by the intronic enhancer; ChIP-3C-qPCR verifies that AML1/ETO mediates DNA looping between the promoter and the intronic enhancer.

### Lin (2017). *Advances in Experimental Medicine and Biology.* RUNX1-ETO Leukemia
[doi:10.1007/978-981-10-3233-2_11](https://doi.org/10.1007/978-981-10-3233-2_11) · `review`  
[src](<../raw/Lin(2017) Advances in Experimental Medicine and Biology; RUNX1-ETO Leukemia.pdf>)

A review chapter on AML1-ETO leukemia, the most common cytogenetic subtype of AML, defined by t(8;21). It summarises that proteomic surveys show AML1-ETO forming a stable complex with several transcription factors including E proteins; that transcriptome and ChIP-seq analyses have identified directly regulated genes such as CEBPA; that several lines of evidence indicate AML1-ETO suppresses endogenous DNA repair to promote mutagenesis and thereby facilitate acquisition of cooperating secondary events; and that a delicate balance between AML1-ETO and native AML1 sustains the malignant phenotype. Clinical translation of these findings is described as just beginning.

### Loke (2017). *Cell Reports.* RUNX1-ETO and RUNX1-EVI1 Differentially Reprogram the Chromatin Landscape in t(8;21) and t(3;21) AML
[doi:10.1016/j.celrep.2017.05.005](https://doi.org/10.1016/j.celrep.2017.05.005) · `paper`  
[src](<../raw/Loke(2017) Cell Reports; RUNX1-ETO and RUNX1-EVI1 Differentially Reprogram the Chromatin Landscape in t(8,21) and t(3,21) AML.pdf>)

A comparison of the regulatory landscapes of two AML types driven by fusions of the same transcription factor: RUNX1-ETO in t(8;21) and RUNX1-EVI1 in t(3;21). The two fusion proteins show distinct genomic binding patterns and cooperate with different transcription factors, producing unique gene regulatory networks, yet both downregulate the myeloid differentiation regulator C/EBPalpha. Depleting either fusion initiates C/EBPalpha-dependent myeloid differentiation. Survival of t(8;21) AML depends on RUNX1, whereas t(3;21) AML requires GATA2.

### Zaidi (2017). *Oncotarget.* An AML1-ETO/miR-29b-1 regulatory circuit modulates phenotypic properties of acute myeloid leukemia cells
[doi:10.18632/oncotarget.18127](https://doi.org/10.18632/oncotarget.18127) · `paper`  
[src](<../raw/Zaidi(2017) Oncotarget; An AML1-ETO miR-29b-1 regulatory circuit modulates phenotypic properties of acute myeloid leukemia cells.pdf>)

AML1-ETO and the corepressor NCoR co-occupy the miR-29a/b-1 locus and downregulate its expression in leukemia cells. Conversely, reintroducing miR-29b-1 into AML1-ETO-expressing cells causes significant downregulation of the fusion protein by directly targeting the 3' untranslated region of the chimeric transcript. Restoring miR-29b-1 decreases cell growth, increases apoptosis, and partially reverses the AML1-ETO-dependent differentiation block and transcriptional program, establishing a regulatory circuit between the tumour-suppressive microRNA and the oncogenic fusion.

### Li (2016). *Blood.* Genome-wide studies identify a novel interplay between AML1 and AML1/ETO in t(8;21) acute myeloid leukemia
[doi:10.1182/blood-2015-03-626671](https://doi.org/10.1182/blood-2015-03-626671) · `paper`  
[src](<../raw/Li(2016) Blood; Genome-wide studies identify a novel interplay between AML1 and AML1 ETO in t(8,21) acute myeloid leukemia.pdf>)

Chromatin immunoprecipitation sequencing with computational analysis and experimental validation shows that wild-type AML1 orchestrates the expression of AML1/ETO targets whether they are activated or repressed, by forming a complex with AML1/ETO on chromatin and recruiting the cofactor AP-1. The two proteins largely overlap in occupancy and preferentially bind adjacent, distinct short and long AML1 motifs respectively; they interact through the runt homology domain of both proteins. The relative binding signals of AML1 and AML1/ETO determine whether a target is repressed or activated, with transactivation proceeding through AP-1 recruitment to the complex.

## t(8;21): dependencies, cooperating lesions and stem cells

*9 papers.* What t(8;21) leukemia needs in order to persist. Cure rates exceed 60% and roughly half of patients still relapse, so the papers here are about the preleukemic reservoir and the cooperating events rather than about initial response.

### Whittle (2026). *eLife.* Single-cell atlas of AML reveals age-related gene regulatory networks in t(8;21) AML
[doi:10.7554/eLife.104978](https://doi.org/10.7554/eLife.104978) · `paper`  
[src](<../raw/Whittle(2026) eLife; Single-cell atlas of AML reveals age-related gene regulatory networks in t(8,21) AML.pdf>)

Large-scale integration of published single-cell RNA-seq datasets creates an AML single-cell atlas of 748,679 cells from 159 AML patients and 51 healthy donors across 20 studies, publicly available through cellxgene. Applying it to 20 patients with t(8;21) AML, the authors explored the clinical importance of age given the in-utero origin of pediatric disease, uncovering age-associated gene regulatory network signatures validated in bulk RNA-seq data to delineate groups with divergent biological characteristics. Using an additional multiomic dataset combining scRNA-seq and scATAC-seq, they validated the findings and constructed a de-noised enhancer-driven gene regulatory network reflecting the age-related signatures.

### Derevyanko (2025). *Blood.* Fusion gene depletion eliminates stemness and induces bidirectional differentiation of acute myeloid leukemia
[doi:10.1182/blood.2025028988](https://doi.org/10.1182/blood.2025028988) · `paper`  
[src](<../raw/Derevyanko(2025) Blood; Fusion gene depletion eliminates stemness and induces bidirectional differentiation of acute myeloid leukemia.pdf>)

Primary t(8;21) AML cells are shown to depend critically on RUNX1::RUNX1T1 to suppress differentiation and maintain stemness. Silencing the fusion with fusion-site-specific siRNA delivered in lipid nanoparticles produces substantial changes in chromatin accessibility, redirecting the leukemia-associated transcriptional network toward myeloid differentiation. Single-cell analyses show depletion of immature stem and progenitor-like populations alongside expansion of granulocytic and eosinophilic/mast cell-like populations with impaired self-renewal.

### Liu (2025). *British Journal of Haematology.* Single‐cell transcriptome profiling reveals blast cell heterogeneity and identifies novel therapeutic target IKZF2 in t(8;21) acute myeloid leukaemia
[doi:10.1111/bjh.70077](https://doi.org/10.1111/bjh.70077) · `paper`  
[src](<../raw/Liu(2025) British Journal of Haematology; Single‐cell transcriptome profiling reveals blast cell heterogeneity and identifies novel therapeutic target IKZF2 in t(8,21) acute myeloid leukaemia.pdf>)

Single-cell RNA sequencing of t(8;21) AML characterises intratumoral heterogeneity and identifies an HSC-like subset as the most quiescent and primitive population, with IKZF2 as its master regulator. IKZF2 is upregulated in t(8;21) relative to other AML subtypes and is specifically targeted by AML1-ETO; primary samples and mouse models confirm its enrichment in primitive quiescent leukemic cells. IKZF2 knockout blocked accumulation of aberrant stem cells driven by AML1-ETO and promoted differentiation in vitro and in vivo. Markers of t(8;21) LSCs including IL5RA, CD69 and CPA3 are also reported.

### Thomas (2024). *Leukemia.* Functional characterization of cooperating MGA mutations in RUNX1::RUNX1T1 acute myeloid leukemia
[doi:10.1038/s41375-024-02193-y](https://doi.org/10.1038/s41375-024-02193-y) · `paper`  
[src](<../raw/Thomas(2024) Leukemia; Functional characterization of cooperating MGA mutations in RUNX1RUNX1T1 acute myeloid leukemia.pdf>)

MGA, a dual-specificity transcription factor that negatively regulates MYC-target genes and is part of the non-canonical polycomb repressive complex PRC1.6, carries recurrent loss-of-function mutations in AML with RUNX1::RUNX1T1. Representative patient mutations abolish protein-protein interactions and transcriptional activity. Using human and mouse systems including a new conditional knockout strain, MGA loss upregulates MYC and E2F targets, cell cycle genes, mTOR signalling and oxidative phosphorylation in normal hematopoietic cells, opening chromatin at cell cycle and proliferation gene promoters and enhancing proliferation. RUNX1::RUNX1T1 expression in Mga-deficient cells produces more aggressive AML with significantly shortened latency - median survival 177 days for controls, 146 for heterozygous and 132 for null.

### Ueda (2021). *FASEB BioAdvances.* KDM4B promotes acute myeloid leukemia associated with AML1‐ETO by regulating chromatin accessibility
[doi:10.1096/fba.2021-00030](https://doi.org/10.1096/fba.2021-00030) · `paper`  
[src](<../raw/Ueda(2021) FASEB BioAdvances; KDM4B promotes acute myeloid leukemia associated with AML1‐ETO by regulating chromatin accessibility.pdf>)

KDM4B, a JmjC-domain histone demethylase, is found elevated specifically in t(8;21) AML. shRNA silencing reduced proliferation of t(8;21)-positive but not t(8;21)-negative lines, suppressed AML1-ETO-inducible gene expression, and perturbed chromatin accessibility at AML1-ETO binding sites with altered active enhancer marks. Transduction of murine KDM4B mutants showed that the double PHD or double Tudor methylated-histone binding modules, rather than catalytic function, support proliferation. Kdm4b conditional knockout mice showed attenuated AML1-ETO-mediated clonogenic potential and delayed leukemia progression in vivo.

### Stoner (2020). *Blood Cancer Journal.* The RUNX1-ETO target gene RASSF2 suppresses t(8;21) AML development and regulates Rac GTPase signaling
[doi:10.1038/s41408-020-0282-9](https://doi.org/10.1038/s41408-020-0282-9) · `paper`  
[src](<../raw/Stoner(2020) Blood Cancer Journal; The RUNX1-ETO target gene RASSF2 suppresses t(8,21) AML development and regulates Rac GTPase signaling.pdf>)

Characterising transcriptional regulation by RUNX1-ETO identified RASSF2 as aberrantly repressed in t(8;21) AML. Re-expressing RASSF2 specifically inhibits t(8;21) AML development across multiple models. Its function depends on interaction with the Hippo kinases MST1 and MST2 but is independent of canonical Hippo signalling. Proximity-based biotin labelling defined the RASSF2-proximal proteome and revealed association with Rac GTPase-related proteins including the exchange factor DOCK2; RASSF2 knockdown impairs Rac GTPase activation, and RASSF2 expression correlates broadly with Rac-mediated signalling in AML patients.

### Gerritsen (2019). *Blood Advances.* RUNX1 mutations enhance self-renewal and block granulocytic differentiation in human in vitro models and primary AMLs
[doi:10.1182/bloodadvances.2018024422](https://doi.org/10.1182/bloodadvances.2018024422) · `paper`  
[src](<../raw/Gerritsen(2019) Blood Advances; RUNX1 mutations enhance self-renewal and block granulocytic differentiation in human in vitro models and primary AMLs.pdf>)

The RUNX1-S291fs300X mutation was introduced into human CD34+ stem/progenitor cells and induced pluripotent stem cells. In both models it strongly impaired myeloid commitment while enhancing self-renewal, with increased long-term culture-initiating cell frequency and colony replating capacity; cord blood cultures continued beyond 100 days with an immature CD34+/CD123+/CD45RA+ granulocyte-macrophage progenitor-like phenotype, and the CD34+/CD38- HSC population appeared to be the cell of origin. CEBPA expression was reduced and its re-expression partly restored differentiation. RNA-seq on the models and primary patients confirmed the differentiation block, with upregulated targets enriched for nucleosome assembly and chromatin structure, and showed distinct genomic binding and differential expression for RUNX1mut versus AML1-ETO at genes including TCF4, MEIS1 and HMGA2.

### Martinez-Soria (2018). *Cancer Cell.* The Oncogenic Transcription Factor RUNX1/ETO Corrupts Cell Cycle Regulation to Drive Leukemic Transformation
[doi:10.1016/j.ccell.2018.08.015](https://doi.org/10.1016/j.ccell.2018.08.015) · `paper`  
[src](<../raw/Martinez-Soria(2018) Cancer Cell; The Oncogenic Transcription Factor RUNX1 ETO Corrupts Cell Cycle Regulation to Drive Leukemic Transformation.pdf>)

Using epigenomic profiling data to direct an RNAi screen against the transcriptional network maintaining t(8;21) AML, the authors identify Cyclin D2 (CCND2) as a crucial transmitter of RUNX1/ETO-driven leukemic propagation. RUNX1/ETO cooperates with AP-1 to drive CCND2 expression, acting both directly - including by interfering with an intergenic negative regulatory element 30 kb from the gene - and indirectly through AP-1 family member expression. Knockdown or pharmacological inhibition of CCND2 with the approved CDK4/6 inhibitor palbociclib significantly impairs expansion of patient-derived AML cells and engraftment in immunodeficient mice.

### Lin (2017). *Blood.* A FOXO1-induced oncogenic network defines the AML1-ETO preleukemic program
[doi:10.1182/blood-2016-11-750976](https://doi.org/10.1182/blood-2016-11-750976) · `paper`  
[src](<../raw/Lin(2017) Blood; A FOXO1-induced oncogenic network defines the AML1-ETO preleukemic program.pdf>)

FOXO1, generally regarded as a tumour suppressor, is shown to be consistently upregulated in t(8;21) AML and to drive aberrant self-renewal in preleukemic human CD34+ cells expressing AML1-ETO. Expressing FOXO1 in normal CD34+ cells produces a preleukemic state with enhanced self-renewal and dysregulated differentiation, dependent on its DNA binding domain, and activates a stem cell signature also present in AML1-ETO preleukemia cells and preserved in patient samples. AML1-ETO and FOXO1 share the majority of their binding sites, with FOXO1 required to activate multiple self-renewal genes; genetic and pharmacological ablation of FOXO1 inhibited long-term proliferation and clonogenicity of both preleukemic and t(8;21) leukemia cells.

## KMT2A rearrangement and the menin-MLL axis

*16 papers.* The subtype that produced the field's most advanced targeted therapy and its most instructive failure. Menin inhibition works, responses are incomplete, resistance is fast - and several papers here are about why.

### Aryal (2026). *Leukemia.* A Perturb-seq map of a differentiation hub reveals synergistic vulnerabilities in KMT2A-rearranged acute myeloid leukemia
[doi:10.1038/s41375-026-02917-2](https://doi.org/10.1038/s41375-026-02917-2) · `paper`  
[src](<../raw/Aryal(2026) Leukemia; A Perturb-seq map of a differentiation hub reveals synergistic vulnerabilities in KMT2A-rearranged acute myeloid leukemia.pdf>)

Perturb-seq screening is used to map the functional architecture of the epigenetic network in KMT2A-rearranged AML. The authors identify a compensatory circuit in which KAT6A, Menin and DOT1L converge to silence a core differentiation module they call the Myeloid Program, whose activity correlates with favourable survival in large patient cohorts. Single perturbations only partially derepress the program, whereas simultaneous pharmacological inhibition collapses the circuit's buffering capacity and produces synergistic anti-leukemic activity; loss of the PRC1.1 component PCGF1 confers resistance to DOT1L inhibition, and high baseline Myeloid Program activity marks a state selectively targetable by MEK, AKT and mTOR inhibitors.

### Mahdavi (2026). *Experimental Hematology.* Upfront menin-inhibitor resistance in multiply pretreated leukemias
[doi:10.1016/j.exphem.2025.105268](https://doi.org/10.1016/j.exphem.2025.105268) · `paper`  
[src](<../raw/Mahdavi(2026) Experimental Hematology; Upfront menin-inhibitor resistance in multiply pretreated leukemias.pdf>)

Menin inhibition was evaluated in patient-derived xenografts of KMT2A-rearranged leukemias with high-risk features. Three AMLs with high-risk fusion partners (MLLT10, MLLT4) and two infant ALL samples were sensitive. In serial samples from two patients with multiply relapsed ALL, heavily pretreated KMT2A::AFF1 samples were much less sensitive than cells obtained earlier in the same patients' course - and since none had received a menin inhibitor, this resistance was acquired without menin-inhibitor exposure. Transcriptomic analysis showed sustained on-target efficacy against canonical menin inhibitor targets in resistant cells; genomic analysis found emergent RAS pathway and TP53 comutations, neither sufficient to cause resistance in vitro, with KMT2D downregulation a candidate mechanism in one patient.

### Arellano (2025). *Blood.* Menin inhibition with revumenib for NPM1 -mutated relapsed or refractory acute myeloid leukemia: the AUGMENT-101 study
[doi:10.1182/blood.2025028357](https://doi.org/10.1182/blood.2025028357) · `paper`  
[src](<../raw/Arellano(2025) Blood; Menin inhibition with revumenib for NPM1 -mutated relapsed or refractory acute myeloid leukemia the AUGMENT-101 study.pdf>)

The phase 2 NPM1-mutated cohort of AUGMENT-101 (NCT04065399), testing the oral menin inhibitor revumenib in relapsed or refractory NPM1m AML. 84 patients received at least one dose; the protocol-defined efficacy population was 64 adults, heavily pretreated (35.9% with three or more prior lines, 75.0% with previous venetoclax). The CR + CRh rate was 23.4% (1-sided P = .0014) and overall response rate 46.9%, with median duration of CR + CRh of 4.7 months; 5 of 30 responders proceeded to transplant, and treatment-related adverse events caused discontinuation in 4 patients (4.8%).

### Shi (2025). *Nature Communications.* Guanine nucleotide biosynthesis blockade impairs MLL complex formation and sensitizes leukemias to menin inhibition
[doi:10.1038/s41467-025-57544-9](https://doi.org/10.1038/s41467-025-57544-9) · `paper`  
[src](<../raw/Shi(2025) Nature Communications; Guanine nucleotide biosynthesis blockade impairs MLL complex formation and sensitizes leukemias to menin inhibition.pdf>)

Leukemia stem cells of MLL-rearranged AML show enhanced guanine nucleotide biosynthesis, and inhibiting it causes myeloid differentiation and sensitises cells to menin inhibitors. Targeting IMPDH2 reduces guanine nucleotides and rRNA transcription, lowering LEDGF and menin protein levels; consequently the MLL-fusion complex forms and binds chromatin less well, reducing MLL target gene expression. Inhibiting guanine nucleotide biosynthesis or rRNA transcription further suppresses MLL-rearranged AML when combined with a menin inhibitor.

### Zehtabcheh (2025). *Biomarker Research.* Insights into KMT2A rearrangements in acute myeloid leukemia: from molecular characteristics to targeted therapies
[doi:10.1186/s40364-025-00786-y](https://doi.org/10.1186/s40364-025-00786-y) · `paper`  
[src](<../raw/Zehtabcheh(2025) Biomarker Research; Insights into KMT2A rearrangements in acute myeloid leukemia from molecular characteristics to targeted therapies.pdf>)

A review of KMT2A-rearranged AML, found in 3-10% of adult cases and associated with resistance to standard treatment and high relapse. It covers how the chimeric proteins disrupt epigenetic regulation and activate HOXA and MEIS1 by recruiting menin and DOT1L; diagnostic approaches from FISH and RT-PCR to next-generation sequencing and machine learning models that predict KMT2A rearrangement from transcriptomic data and identify biomarkers such as LAMP5 and SKIDA1; and the therapeutic shift to menin inhibitors (revumenib, ziftomenib), DOT1L inhibitors (pinometostat), WDR5 inhibitors and PROTAC-mediated degradation. Remaining challenges include optimising measurable residual disease monitoring, overcoming resistance and validating biomarkers.

### Heikamp (2024). *Cell Reports.* NUP98 fusion proteins and KMT2A-MENIN antagonize PRC1.1 to drive gene expression in AML
[doi:10.1016/j.celrep.2024.114901](https://doi.org/10.1016/j.celrep.2024.114901) · `paper`  
[src](<../raw/Heikamp(2024) Cell Reports; NUP98 fusion proteins and KMT2A-MENIN antagonize PRC1.1 to drive gene expression in AML.pdf>)

Using menin-KMT2A inhibitors and targeted degradation of NUP98 fusion proteins, the authors define the relationship between NUP98 oncofusions and the non-canonical polycomb repressive complex PRC1.1. Evicting the NUP98 fusion-menin-KMT2A complex from chromatin is not sufficient to silence pro-leukemogenic genes: in the absence of PRC1.1 key oncogenes remain transcriptionally active, and transition to a repressed state requires accumulation of PRC1.1 and repressive histone modifications. PRC1.1 loss confers resistance to small-molecule menin-KMT2A inhibitors in vivo, so a critical function of these oncofusions is antagonising repressive chromatin complexes.

### Janssens (2024). *Nature Communications.* MLL oncoprotein levels influence leukemia lineage identities
[doi:10.1038/s41467-024-53399-8](https://doi.org/10.1038/s41467-024-53399-8) · `paper`  
[src](<../raw/Janssens(2024) Nature Communications; MLL oncoprotein levels influence leukemia lineage identities.pdf>)

Automated CUT&RUN profiling of oncoprotein target sites across 36 representative MLL-rearranged leukemia samples, including three that underwent lymphoid-to-myeloid lineage switching under therapy, shows that genomic enrichment of the oncoprotein is highly variable between samples and dynamically regulated. At high expression the oncoproteins preferentially activate either a pro-B-cell ALL program or a hematopoietic-stem-cell AML program, with fusion-partner-specific binding patterns correlating with each mutation's prevalence in ALL versus AML. In lineage-switching samples oncoprotein levels fall and binding shifts to granulocyte-monocyte progenitor genes; in one sample that switched during revumenib treatment, oncoprotein and menin became undetectable while the cofactor ENL persisted at many target loci including GMP-program genes.

### DiMambro (2023). *Oncogene.* SET-PP2A complex as a new therapeutic target in KMT2A (MLL) rearranged AML
[doi:10.1038/s41388-023-02840-1](https://doi.org/10.1038/s41388-023-02840-1) · `paper`  
[src](<../raw/DiMambro(2023) Oncogene; SET-PP2A complex as a new therapeutic target in KMT2A (MLL) rearranged AML.pdf>)

SET, the endogenous inhibitor of the Ser/Thr phosphatase PP2A, is shown to be overexpressed in AML, with elevated expression correlating with poor prognosis and with MEIS and HOXA expression. Silencing SET specifically abolished clonogenic ability of KMT2A-rearranged leukemic cells and transcription of the KMT2A targets HOXA9 and HOXA10. SET interacts with both wild-type KMT2A and the fusion proteins and is recruited to the HOXA10 promoter. Pharmacological inhibition by FTY720 disrupted the SET-PP2A interaction, causing cell cycle arrest and increased chemosensitivity; phosphoproteomics showed reduced activity of PP2A-regulated kinases ERK1, GSK3beta, AURB and PLK1 and suppression of MYC.

### Tubío-Santamaría (2023). *Molecular Cancer.* Immunoproteasome function maintains oncogenic gene expression in KMT2A-complex driven leukemia
[doi:10.1186/s12943-023-01907-7](https://doi.org/10.1186/s12943-023-01907-7) · `paper`  
[src](<../raw/Tubío-Santamaría(2023) Molecular Cancer; Immunoproteasome function maintains oncogenic gene expression in KMT2A-complex driven leukemia.pdf>)

A proteomic approach identified the catalytic immunoproteasome subunit PSMB8 as a specific vulnerability in KMT2A-rearranged AML. Genetic and pharmacologic inactivation impairs proliferation of murine and human leukemic cells while normal hematopoietic cells are unaffected. Disrupting immunoproteasome function increases the transcription factor BASP1, which represses KMT2A-fusion target genes. Pharmacologic PSMB8 targeting improves menin inhibitor efficacy, synergistically reduces leukemia in human xenografts, and retains activity against menin inhibitor resistance mutations. The dependency extends across KMT2A-complex-dependent leukemias including NPM1c.

### Olsen (2022). *Molecular Cell.* MLL::AF9 degradation induces rapid changes in transcriptional elongation and subsequent loss of an active chromatin landscape
[doi:10.1016/j.molcel.2022.02.013](https://doi.org/10.1016/j.molcel.2022.02.013) · `paper`  
[src](<../raw/Olsen(2022) Molecular Cell; MLLAF9 degradation induces rapid changes in transcriptional elongation and subsequent loss of an active chromatin landscape.pdf>)

Using degradable MLL::AF9 models in which small molecules induce rapid degradation, the authors identify a core subset of target genes where degradation changes transcriptional elongation within 15 minutes, followed subsequently by loss of an active chromatin landscape. They use this ordering to assess small molecules targeting members of the MLL::AF9 complex: combined DOT1L and MENIN inhibition resembles MLL::AF9 degradation, whereas single-agent treatment has more modest effects on occupancy and gene expression. Combined inhibition releases the oncoprotein from chromatin globally.

### Tirtakusuma (2022). *Blood.* Epigenetic regulator genes direct lineage switching in MLL/AF4 leukemia
[doi:10.1182/blood.2021015036](https://doi.org/10.1182/blood.2021015036) · `paper`  
[src](<../raw/Tirtakusuma(2022) Blood; Epigenetic regulator genes direct lineage switching in MLL AF4 leukemia.pdf>)

MLL/AF4 defines a high-risk pro-B acute lymphoblastic leukemia whose relapse can involve a lineage switch to acute myeloid leukemia, conferring resistance to chemotherapy and immunotherapy. Myeloid relapses share oncogene fusion breakpoints with their matched lymphoid presentations and can originate from varying differentiation stages, from immature progenitors through committed B-cell precursors. Lineage switching involves substantial changes in chromatin accessibility and rewiring of transcriptional programmes including alternative splicing, and is recurrently associated with altered expression, splicing or mutation of chromatin modifiers, notably CHD4, the ATPase/helicase of the NuRD complex. Perturbing CHD4 alone or with other mutated epigenetic modifiers induces myeloid gene expression in MLL/AF4 cell models.

### Issa (2021). *Leukemia.* Therapeutic implications of menin inhibition in acute leukemias
[doi:10.1038/s41375-021-01309-y](https://doi.org/10.1038/s41375-021-01309-y) · `paper`  
[src](<../raw/Issa(2021) Leukemia; Therapeutic implications of menin inhibition in acute leukemias.pdf>)

A review of menin biology and menin inhibitors in acute leukemia. Menin acts as a tumour suppressor in endocrine glands - germline MEN1 mutations cause multiple endocrine neoplasia type 1 - yet is required for leukemogenesis in KMT2A-rearranged disease, an apparent contradiction explained by its several roles in gene regulation. The review covers the physiologic and malignant biology of menin, mechanisms in susceptible subsets including KMT2A rearrangement and mutant NPM1, HOX expression patterns as a potential response biomarker, other genotypes with similar transcriptional dependencies, and early clinical results with oral small-molecule menin inhibitors in relapsed acute leukemia.

### Klossowski (2020). *Journal of Clinical Investigation.* Menin inhibitor MI-3454 induces remission in MLL1-rearranged and NPM1-mutated models of leukemia
[doi:10.1172/JCI129126](https://doi.org/10.1172/JCI129126) · `paper`  
[src](<../raw/Klossowski(2020) Journal of Clinical Investigation; Menin inhibitor MI-3454 induces remission in MLL1-rearranged and NPM1-mutated models of leukemia.pdf>)

MI-3454, a subnanomolar, orally bioavailable second-generation inhibitor of the menin-MLL1 interaction, is reported to profoundly inhibit proliferation and induce differentiation in acute leukemia cells and primary patient samples with MLL1 translocations or NPM1 mutations. As a single agent it induced complete remission or regression in mouse models including patient-derived xenografts, through downregulation of key leukemogenesis genes. MEIS1 is identified as a candidate pharmacodynamic biomarker of response, and the compound was well tolerated without impairing normal hematopoiesis in mice.

### Krivtsov (2019). *Cancer Cell.* A Menin-MLL Inhibitor Induces Specific Chromatin Changes and Eradicates Disease in Models of MLL-Rearranged Leukemia
[doi:10.1016/j.ccell.2019.11.001](https://doi.org/10.1016/j.ccell.2019.11.001) · `paper`  
[src](<../raw/Krivtsov(2019) Cancer Cell; A Menin-MLL Inhibitor Induces Specific Chromatin Changes and Eradicates Disease in Models of MLL-Rearranged Leukemia.pdf>)

Structure-based design produced VTP50469, a potent, highly selective, orally bioavailable inhibitor of the menin-MLL interaction. MLL-rearranged cell lines were selectively responsive; the compound displaced menin from protein complexes and reduced MLL chromatin occupancy at select genes, leading to changes in gene expression, differentiation and apoptosis. Patient-derived xenografts of MLL-rearranged AML and ALL showed dramatic reductions in leukemia burden, and multiple mice engrafted with MLL-rearranged ALL remained disease free for more than a year after treatment.

### Kerry (2017). *Cell Reports.* MLL-AF4 Spreading Identifies Binding Sites that Are Distinct from Super-Enhancers and that Govern Sensitivity to DOT1L Inhibition in Leukemia
[doi:10.1016/j.celrep.2016.12.054](https://doi.org/10.1016/j.celrep.2016.12.054) · `paper`  
[src](<../raw/Kerry(2017) Cell Reports; MLL-AF4 Spreading Identifies Binding Sites that Are Distinct from Super-Enhancers and that Govern Sensitivity to DOT1L Inhibition in Leukemia.pdf>)

MLL-AF4 binding is shown to require an unmethylated CpG island and Menin, and at a subset of targets both MLL-AF4 and Menin spread into the gene body, which is associated with high transcription and an aberrant chromatin signature. These spreading targets are distinct from super-enhancers, and the presence of spreading - rather than simply the presence of MLL-AF4 and H3K79me2/3 - predicts sensitivity to DOT1L inhibitors. Spreading correlates with Menin and ENL binding and occurs over low-density unmethylated CpG landscapes in gene bodies close to the promoter.

### Wang (2016). *Current Opinion in Genetics & Development.* The role of DOT1L in the maintenance of leukemia gene expression
[doi:10.1016/j.gde.2016.03.015](https://doi.org/10.1016/j.gde.2016.03.015) · `paper`  
[src](<../raw/Wang(2016) Current Opinion in Genetics & Development; The role of DOT1L in the maintenance of leukemia gene expression.pdf>)

A review of DOT1L, the H3K79 methyltransferase required for maintenance of MLL-rearranged leukemia. It covers the structural basis of chromatin targeting through cofactors AF9 and AF10, proposed as readers of histone modifications that recruit the DOT1L complex to open chromatin; the role of DOT1L in preventing SIRT1-mediated gene silencing in MLL-rearranged cells; and H3K79 methylation as a mechanism of selective gene regulation. No demethylase for H3K79 has been identified, so regulation of DOT1L activity is likely the dominant determinant of the mark.

## NPM1 mutation: mislocalisation, chromatin and HOX

*9 papers.* The most common lesion in adult AML, defined by a protein leaving the nucleus - and recently shown to act on chromatin anyway. Two independent groups overturned the standing loss-of-function model in the same journal issue.

### Damaskou (2025). *Blood.* Posttranscriptional depletion of ribosome biogenesis factors engenders therapeutic vulnerabilities in NPM1 -mutant AML
[doi:10.1182/blood.2024026113](https://doi.org/10.1182/blood.2024026113) · `paper`  
[src](<../raw/Damaskou(2025) Blood; Posttranscriptional depletion of ribosome biogenesis factors engenders therapeutic vulnerabilities in NPM1 -mutant AML.pdf>)

Using conditional knockin Npm1cA/+ mice to isolate the effect of the NPM1c mutation on the proteome of preleukemic HSPCs, the authors find many ribosome biogenesis proteins significantly depleted - without corresponding mRNA changes, indicating posttranscriptional regulation - and confirm the depletion in human NPM1-mutant AML. Preleukemic Npm1cA/+ HSPCs are more sensitive to RNA polymerase I inhibitors including actinomycin D; ActD combined with venetoclax inhibits growth and colony formation of preleukemic and leukemic NPM1c+ cells, and low-dose ActD resensitises resistant NPM1c+ cells to venetoclax. From CRISPR dropout screens they identify TSR3, a 40S ribosomal maturation factor whose knockout preferentially inhibits NPM1c+ AML by activating a p53-dependent apoptotic response and partially restores venetoclax sensitivity.

### Datar (2025). *Cell.* Disparate leukemia mutations converge on nuclear phase-separated condensates
[doi:10.1016/j.cell.2025.10.010](https://doi.org/10.1016/j.cell.2025.10.010) · `paper`  
[src](<../raw/Datar(2025) Cell; Disparate leukemia mutations converge on nuclear phase-separated condensates.pdf>)

Mutant NPM1 (NPM1c) is shown to form nuclear phase-separated condensates - termed coordinating bodies, or C-bodies - in human cell lines, mouse models and primary patient samples. NPM1c phase separation is necessary and sufficient to recruit NUP98 and KMT2A into these condensates. Through extensive mutagenesis and pharmacological destabilisation of phase separation, C-bodies are shown to be necessary for regulating gene expression, promoting leukemic expansion in vivo and maintaining the undifferentiated state. Nucleoporin and KMT2A fusion proteins form condensates biophysically indistinguishable from NPM1c C-bodies, establishing them as a shared feature and therapeutic vulnerability.

### Shimosato (2024). *Leukemia.* NPM1-fusion proteins promote myeloid leukemogenesis through XPO1-dependent HOX activation
[doi:10.1038/s41375-024-02438-w](https://doi.org/10.1038/s41375-024-02438-w) · `paper`  
[src](<../raw/Shimosato(2024) Leukemia; NPM1-fusion proteins promote myeloid leukemogenesis through XPO1-dependent HOX activation.pdf>)

Two rare NPM1-fusion proteins found in pediatric AML, NPM1::MLF1 and NPM1::CCDC28A, are tested for oncogenic capacity. NPM1::MLF1 localises to both nucleus and cytoplasm and occasionally induces AML in mouse transplantation; NPM1::CCDC28A is more cytoplasmic, immortalises mouse bone marrow cells in vitro and efficiently induces AML in vivo. Both bind the HOX gene cluster and, like NPM1c, cause aberrant HOX upregulation in cooperation with XPO1. The XPO1 inhibitor selinexor suppressed HOX activation and colony formation driven by both fusions, and NPM1::CCDC28A cells were also sensitive to menin inhibition.

### Uckelmann (2022). *Cancer Discovery.* Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia
[doi:10.1158/2159-8290.CD-22-0366](https://doi.org/10.1158/2159-8290.CD-22-0366) · `paper`  
[src](<../raw/Uckelmann(2022) Cancer Discovery; Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia.pdf>)

NPM1c is shown to bind directly to specific chromatin targets co-occupied by the histone methyltransferase KMT2A (MLL1). Targeted degradation of NPM1c causes rapid decrease in gene expression with loss of RNA polymerase II and of activating histone modifications at those targets. The work demonstrates that NPM1c directly regulates oncogenic gene expression in collaboration with the MLL1 complex, and defines the mechanism by which MLL1-menin inhibitors produce clinical responses in NPM1-mutated AML.

### Wang (2022). *Cancer Discovery.* Mutant NPM1 Hijacks Transcriptional Hubs to Maintain Pathogenic Gene Programs in Acute Myeloid Leukemia
[doi:10.1158/2159-8290.CD-22-0424](https://doi.org/10.1158/2159-8290.CD-22-0424) · `paper`  
[src](<../raw/Wang(2022) Cancer Discovery; Mutant NPM1 Hijacks Transcriptional Hubs to Maintain Pathogenic Gene Programs in Acute Myeloid Leukemia.pdf>)

NPM1c is shown to bind a subset of active gene promoters in NPM1c AML, including HOXA/B cluster genes and MEIS1. It sustains active transcription of these targets by orchestrating a transcription hub and maintains the active chromatin landscape by inhibiting histone deacetylase activity, thereby preventing the silencing that normally accompanies myeloid differentiation. The authors observe that NPM1c forms condensates significantly smaller than those of wild-type NPM1, and propose that NPM1c acts as a transcriptional amplifier rather than forming mesoscale phase-separated puncta that would exclude transcriptional machinery.

### Falini (2020). *Blood.* NPM1-mutated acute myeloid leukemia: from bench to bedside
[doi:10.1182/blood.2019004226](https://doi.org/10.1182/blood.2019004226) · `paper`  
[src](<../raw/Falini(2020) Blood; NPM1-mutated acute myeloid leukemia from bench to bedside.pdf>)

A review of NPM1-mutated AML by the group that discovered the mutation, covering newly identified functions of wild-type NPM1 in the nucleolus - including its role in liquid-liquid phase separation with R-motif proteins and nascent rRNA - and the biology and clinical management of the mutant entity. It addresses cooperation between NPM1 and other mutations in producing different outcomes, the need to eradicate NPM1-mutated clones for cure, the role of persisting preleukemic clonal hematopoiesis in predisposing to second AML, the contribution of HOX gene expression, unresolved diagnostic issues in the 2017 WHO classification, the place of NPM1 in European LeukemiaNet risk stratification, the value and limits of NPM1-based measurable residual disease assessment, and preclinical results with XPO1 and menin-MLL inhibitors.

### Uckelmann (2020). *Science.* Therapeutic targeting of preleukemia cells in a mouse model of NPM1 mutant acute myeloid leukemia
[doi:10.1126/science.aax5863](https://doi.org/10.1126/science.aax5863) · `paper`  
[src](<../raw/Uckelmann(2020) Science; Therapeutic targeting of preleukemia cells in a mouse model of NPM1 mutant acute myeloid leukemia.pdf>)

In Npm1c/Dnmt3a mutant knock-in mice, leukemia is preceded by extended myeloid progenitor proliferation and self-renewal. Npm1c induces stem-cell-associated gene expression, including Hoxa9, de novo in committed progenitors that normally lack self-renewal, and confers increased replating capacity; Dnmt3a mutation alone does not. This self-renewal is reversed by oral administration of the menin-MLL1 inhibitor VTP-50469, which rapidly represses stem cell genes including Meis1 and Pbx3 and induces differentiation. Meis1 knockout confirms it as a dependency, and Menin chromatin occupancy decreases globally while MLL1 and H3K4me3 are lost only at sites enriched for downregulated genes.

### Brunetti (2018). *Cancer Cell.* Mutant NPM1 Maintains the Leukemic State through HOX Expression
[doi:10.1016/j.ccell.2018.08.005](https://doi.org/10.1016/j.ccell.2018.08.005) · `paper`  
[src](<../raw/Brunetti(2018) Cancer Cell; Mutant NPM1 Maintains the Leukemic State through HOX Expression.pdf>)

NPM1 mutations relocalise the protein to the cytoplasm (NPM1c), but whether that is required to maintain leukemia was unknown. Using allele-specific CRISPR editing of the mutant allele and targeted degradation, the authors show that removing NPM1c from the cytoplasm - by nuclear relocalisation or by degradation - causes immediate downregulation of HOX genes followed by differentiation. XPO1 inhibition relocalises NPM1c to the nucleus, drives differentiation of AML cells and prolongs survival of Npm1-mutated leukemic mice, establishing a dependency of NPM1-mutant AML on NPM1c and a rationale for nuclear export inhibitors.

### Kühn (2016). *Cancer Discovery.* Targeting Chromatin Regulators Inhibits Leukemogenic Gene Expression in NPM1 Mutant Leukemia
[doi:10.1158/2159-8290.CD-16-0237](https://doi.org/10.1158/2159-8290.CD-16-0237) · `paper`  
[src](<../raw/Kühn(2016) Cancer Discovery; Targeting Chromatin Regulators Inhibits Leukemogenic Gene Expression in NPM1 Mutant Leukemia.pdf>)

The histone modifiers MLL1 and DOT1L are shown to control HOX and FLT3 expression and differentiation in NPM1-mutant AML. A CRISPR/Cas9 genome editing domain screen shows NPM1-mutant AML to be exceptionally dependent on the menin binding site in MLL1, and pharmacologic inhibition of the menin-MLL1 interaction had profound antileukemic activity in human and murine models. Combined inhibition of menin-MLL1 and DOT1L dramatically suppressed HOX and FLT3 expression, induced differentiation, and was superior to either alone.

## NUP98, DEK::NUP214, EVI1 and other rearrangements

*10 papers.* Rare fusions, each with its own dependency. Individually these entities are too small to study in a trial, which is why a shared mechanism - XPO1, HOXA activation, enhancer hijacking - matters more here than elsewhere.

### Mimura (2026). *Blood.* BCL11B enhancer hijacking by t(14;16)(q32;q24) translocation defines a novel high-risk subtype of T-ALL
[doi:10.1182/blood.2025031466](https://doi.org/10.1182/blood.2025031466) · `paper`  
[src](<../raw/Mimura(2026) Blood; BCL11B enhancer hijacking by t(14,16)(q32,q24) translocation defines a novel high-risk subtype of T-ALL.pdf>)

Integrated whole-genome and whole-transcriptome analysis of pediatric and adult T-ALL and mixed-phenotype acute leukemias identified 14 patients with predominantly T-lineage disease driven by a t(14;16)(q32;q24) translocation, with universal GATA3 mutations and CDKN2A/B deletions. The translocation repositions the ThymoD locus downstream of BCL11B, causing monoallelic ectopic overexpression of FENDRR and the mesenchymal transcription factors FOXF1 and FOXC2 and activating epithelial-mesenchymal transition signatures. Immunophenotyping and single-cell RNA sequencing show marked lineage ambiguity with myeloid and B-cell differentiation potential, and FOXF1 overexpression in CD34+ cord blood cells promotes myeloid while suppressing T-cell differentiation. The subtype occurs in 0.15% to 4.0% of cases, median age 15, with extremely poor prognosis.

### CharlesCano (2025). *Leukemia.* XPO1-dependency of DEK::NUP214 leukemia
[doi:10.1038/s41375-025-02570-1](https://doi.org/10.1038/s41375-025-02570-1) · `paper`  
[src](<../raw/CharlesCano(2025) Leukemia; XPO1-dependency of DEKNUP214 leukemia.pdf>)

DEK::NUP214 (t(6;9)) AML is evaluated for dependency on the nuclear export protein XPO1. Deleting XPO1 in DN-positive FKH-1 cells revealed strong dependency; the second-generation nuclear export inhibitor eltanexor reduced XPO1 expression, disrupted co-localisation of XPO1 with the fusion protein, and induced apoptosis and cell cycle arrest in primary and FKH-1 cells. XPO1 and DEK::NUP214 co-localise at chromatin, and inhibition strongly reduces that binding, downregulating fusion target genes and cell cycle and self-renewal pathways. In a patient-derived xenograft, eltanexor-treated mice showed molecular clearance in bone marrow after a median of 377 days while controls died after a median of 244 days.

### Kaya (2025). *Leukemia.* DEK::NUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes
[doi:10.1038/s41375-025-02593-8](https://doi.org/10.1038/s41375-025-02593-8) · `paper`  
[src](<../raw/Kaya(2025) Leukemia; DEKNUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes.pdf>)

A multi-omics comparison of 57 cytogenetically poor-risk primary AML samples - whole genome and targeted sequencing, transcriptomics, and drug screening with over 500 compounds - shows that t(6;9)/DEK::NUP214 cases respond selectively to the XPO1 inhibitors selinexor and eltanexor and carry a distinct transcriptomic signature with overexpression of FOXC1 and HOX genes. CUT&RUN demonstrates direct binding of DEK::NUP214 to the promoters of FOXC1 and the HOXA/B clusters, and both the expression of these genes and the fusion's binding at their regulatory regions are selectively reduced by XPO1 inhibition, identifying DEK::NUP214 as an XPO1-dependent transcriptional activator.

### Lv (2025). *Genome Biology.* KAT6A chimeras form a self-reinforcing epigenetic module with NURF and MLL/COMPASS to sustain AML
[doi:10.1186/s13059-025-03743-y](https://doi.org/10.1186/s13059-025-03743-y) · `paper`  
[src](<../raw/Lv(2025) Genome Biology; KAT6A chimeras form a self-reinforcing epigenetic module with NURF and MLL COMPASS to sustain AML.pdf>)

KAT6A-CBP and KAT6A-P300 fusions are recurrent in AML with poor prognosis, but their size has impeded model development. Using a domain-focused truncation strategy, the authors generate de novo murine models that recapitulate the morphological, immunophenotypic and transcriptomic features of KAT6A-rearranged AML. The fusions preferentially localise to H3K4me2/3-marked regions, and KAT6A interacts with the Nucleosome Remodeling Factor (NURF), an H3K4me2/3 reader. Depleting or inhibiting the NURF subunit BPTF impairs fusion recruitment and disrupts MLL/COMPASS-mediated H3K4me2 deposition; CBP/P300 inhibition reduces acetylation and accessibility, further impairing recruitment, and combining the two is more effective than either alone.

### Sollier (2025). *Blood Cancer Discovery.* Enhancer Hijacking Discovery in Acute Myeloid Leukemia by Pyjacker Identifies MNX1 Activation via Deletion 7q
[doi:10.1158/2643-3230.BCD-24-0278](https://doi.org/10.1158/2643-3230.BCD-24-0278) · `paper`  
[src](<../raw/Sollier(2025) Blood Cancer Discovery; Enhancer Hijacking Discovery in Acute Myeloid Leukemia by Pyjacker Identifies MNX1 Activation via Deletion 7q.pdf>)

Pyjacker, a computational tool for systematic detection of enhancer hijacking from whole genome sequencing, RNA-seq and enhancer information, was applied to 39 complex-karyotype AML samples and detected 19 genes putatively activated by structural variants at FDR below 20%. Among them, aberrant MNX1 expression can result from del(7)(q22q36) via hijacking of a CDK6 enhancer; MNX1 activation occurred in 1.4% of AML patients, co-occurred significantly with BCOR mutations, and was required for leukemia cell fitness in a xenograft model. GSX2 and EPO were also identified as putatively activated.

### Troester (2025). *Nature Communications.* Transcriptional and epigenetic rewiring by the NUP98::KDM5A fusion oncoprotein directly activates CDK12
[doi:10.1038/s41467-025-59930-9](https://doi.org/10.1038/s41467-025-59930-9) · `paper`  
[src](<../raw/Troester(2025) Nature Communications; Transcriptional and epigenetic rewiring by the NUP98KDM5A fusion oncoprotein directly activates CDK12.pdf>)

NUP98 fusion-expressing AML carries an epigenetic signature of increased accessibility at hematopoietic stem cell genes and enrichment of activating histone marks. Using an AML model for ligand-induced degradation of NUP98::KDM5A with CUT&Tag and nascent RNA-seq, the authors identify directly regulated epigenetic programmes and transcriptional targets; orthogonal genome-wide CRISPR screening narrows these to 12 direct target genes essential for AML growth. Among them CDK12 is validated as a druggable vulnerability - consistent with its role in transcribing DNA damage repair genes, small-molecule CDK12 inactivation increases DNA damage and kills NUP98::KDM5A AML cells.

### Abla (2024). *Blood Advances.* Structural variants involving MLLT10 fusion are associated with adverse outcomes in pediatric acute myeloid leukemia
[doi:10.1182/bloodadvances.2023010805](https://doi.org/10.1182/bloodadvances.2023010805) · `paper`  
[src](<../raw/Abla(2024) Blood Advances; Structural variants involving MLLT10 fusion are associated with adverse outcomes in pediatric acute myeloid leukemia.pdf>)

A retrospective study of 2080 children and young adults on the Children's Oncology Group AAML0531 and AAML1031 trials, using transcriptome profiling and karyotyping to identify MLLT10 fusions and relate them to outcome. 127 patients (6.1%) carried an MLLT10 fusion - 104 KMT2A::MLLT10, 13 PICALM::MLLT10, 10 with other partners - and all fared badly: 5-year event-free survival 18.6% versus 49%, overall survival 38.2% versus 65.7%, relapse risk 76% versus 38.6%.

### Ma (2024). *Leukemia.* Genomic and global gene expression profiling in pediatric and young adult acute leukemia with PICALM::MLLT10 Fusion
[doi:10.1038/s41375-024-02194-x](https://doi.org/10.1038/s41375-024-02194-x) · `paper`  
[src](<../raw/Ma(2024) Leukemia; Genomic and global gene expression profiling in pediatric and young adult acute leukemia with PICALMMLLT10 Fusion.pdf>)

Genomic and gene expression profiling of 20 PICALM::MLLT10-positive acute leukemias - 10 AML, 8 T-ALL/LLy, 1 mixed-phenotype and 1 acute undifferentiated. Beyond confirming HOXA activation, differential expression against hematopoietic stem cells showed enrichment of proliferation pathways and relatively high XPO1 expression in both PM-AML and PM-T-ALL/LLy. PHF6 disruption emerged as a key cooperating event across immunophenotypes. The two groups form distinct transcriptomic classes with markedly different co-mutation spectra: TP53 and NF1 alterations characterise PM-AML and associate with progression and relapse, while EZH2 alterations are enriched in PM-T-ALL/LLy.

### Tanaka (2022). *Blood.* Aberrant EVI1 splicing contributes to EVI1-rearranged leukemia
[doi:10.1182/blood.2021015325](https://doi.org/10.1182/blood.2021015325) · `paper`  
[src](<../raw/Tanaka(2022) Blood; Aberrant EVI1 splicing contributes to EVI1-rearranged leukemia.pdf>)

A previously unannotated oncogenic splicing-derived isoform of EVI1 is identified, frequently present in inv(3)/t(3;3) AML and directly contributing to leukemic transformation. The isoform is generated by oncogenic mutations in the core splicing factor SF3B1, mutated in over 30% of inv(3)/t(3;3) myeloid neoplasm patients and the single most commonly co-occurring alteration in that group; SF3B1 mutations are statistically uniquely enriched in these patients. Combined expression of the SF3B1 mutation with the human inv(3) allele in mice enhanced myeloid lineage skewing, HSPC expansion and leukemia development, and the mis-splicing event was shared across human and murine SF3B1-mutant samples.

### Michmerhuizen (2020). *Blood.* Mechanistic insights and potential therapeutic approaches for NUP98 -rearranged hematologic malignancies
[doi:10.1182/blood.2020007093](https://doi.org/10.1182/blood.2020007093) · `paper`  
[src](<../raw/Michmerhuizen(2020) Blood; Mechanistic insights and potential therapeutic approaches for NUP98 -rearranged hematologic malignancies.pdf>)

A review of NUP98 fusion oncoproteins, which occur across hematologic malignancies and particularly in pediatric leukemias with poor outcomes. The translocations join the intrinsically disordered N-terminal region of NUP98 to over 30 partner genes, many bearing homeodomains or with roles in transcriptional or epigenetic regulation. Leukemogenesis is mediated by changes in chromatin structure and gene expression, with multiple cofactors associating with the fusions - possibly via phase separation - in a partner-dependent manner. NUP98 fusions co-occur with additional mutations including FLT3-ITD. Therapeutic strategies considered target transcriptional and epigenetic machinery, cooperating alterations, and signalling or cell-cycle pathways.


# B. Chromatin, transcription and genome architecture

## Chromatin regulators and readers as therapeutic dependencies

*12 papers.* Wild-type chromatin proteins co-opted to hold the differentiation block, which the field increasingly prefers as targets over the transcription factors they serve. Several of these papers correct what a drug in trials was thought to be doing.

### Meyerhöfer (2026). *Blood.* Inhibition of p300/CREBBP catalytic activity drives context-dependent transcriptional activation in AML
[doi:10.1182/blood.2025031924](https://doi.org/10.1182/blood.2025031924) · `paper`  
[src](<../raw/Meyerhöfer(2026) Blood; Inhibition of p300 CREBBP catalytic activity drives context-dependent transcriptional activation in AML.pdf>)

The acetyltransferase activity of p300/CREBBP has traditionally been linked to transcriptional activation via marks such as H3K27ac. Here, in AML, inhibiting p300/CREBBP catalysis paradoxically increases transcription at a subset of loci. Combining time-resolved nascent and total transcription with chromatin binding dynamics, chromatin pull-down and acetyl proteomics, motif enrichment, and genome-wide CRISPR dropout plus focused Perturb-seq screens, the authors show that catalytic inhibition traps p300/CREBBP at select regulatory elements, promoting cooperative transcription factor assembly and increased H3K27 acetylation. The effect is most pronounced at IRF motif-enriched loci, where it facilitates STAT1 recruitment and interferon-stimulated gene transcription, and combines synergistically with interferon-alpha.

### Hosseini (2025). *Nature.* Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation
[doi:10.1038/s41586-025-08915-1](https://doi.org/10.1038/s41586-025-08915-1) · `paper`  
[src](<../raw/Hosseini(2025) Nature; Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation.pdf>)

Simultaneous inhibition of the histone demethylase LSD1 and of GSK3, the WNT pathway antagonist kinase, robustly promotes differentiation of AML cell lines and primary human AML cells, reduces tumour burden and significantly extends survival in a patient-derived xenograft model. The mechanism is activation of type I interferon pathway genes: LSD1 inhibition induces transcription factors such as IRF7, GSK3 inhibition induces the co-activator beta-catenin, and the two selectively co-occupy targets including STAT1, which is required for the combination-induced differentiation. The combination also suppresses canonical pro-oncogenic WNT signalling and cell cycle genes, and the induced signature correlates with better prognosis in patient datasets.

### Bauer (2024). *American Journal of Hematology.* BRD4 degraders may effectively counteract therapeutic resistance of leukemic stem cells in AML and ALL
[doi:10.1002/ajh.27385](https://doi.org/10.1002/ajh.27385) · `paper`  
[src](<../raw/Bauer(2024) American Journal of Hematology; BRD4 degraders may effectively counteract therapeutic resistance of leukemic stem cells in AML and ALL.pdf>)

A comparison of the BET inhibitor JQ1 with the BRD4 degraders dBET1 and dBET6 in AML and ALL cell lines and primary patient cells, including CD34+/CD38- and CD34+/CD38+ leukemic stem and progenitor cells. All three suppressed growth and viability regardless of leukemia variant or molecular driver; dBET6 additionally overcame osteoblast-induced drug resistance, combined synergistically with gilteritinib in FLT3-ITD AML and with ponatinib in BCR::ABL1+ ALL, and all three suppressed interferon-gamma- and TNF-alpha-induced PD-L1 expression. dBET6 was the superior agent in every assay.

### Fiskus (2024). *Blood.* BRG1/BRM inhibitor targets AML stem cells and exerts superior preclinical efficacy combined with BET or menin inhibitor
[doi:10.1182/blood.2023022832](https://doi.org/10.1182/blood.2023022832) · `paper`  
[src](<../raw/Fiskus(2024) Blood; BRG1 BRM inhibitor targets AML stem cells and exerts superior preclinical efficacy combined with BET or menin inhibitor.pdf>)

FHD-286, an orally bioavailable selective inhibitor of the mutually exclusive BAF complex ATPases BRG1 (SMARCA4) and BRM (SMARCA2), is shown to induce differentiation and lethality in AML cells with MLL1 rearrangement or mutant NPM1, perturbing chromatin accessibility and repressing c-Myc, PU.1 and CDK4/6. Cotreatment with decitabine, a BET inhibitor, a menin inhibitor or venetoclax was synergistically lethal in vitro. In patient-derived xenografts, FHD-286 reduced AML burden, improved survival and attenuated the leukemia-initiating potential of stem-progenitor cells, and each combination significantly outperformed the single agents without significant toxicity.

### SanJosé-Enériz (2024). *Nature Communications.* Epigenetic-based differentiation therapy for Acute Myeloid Leukemia
[doi:10.1038/s41467-024-49784-y](https://doi.org/10.1038/s41467-024-49784-y) · `paper`  
[src](<../raw/SanJosé-Enériz(2024) Nature Communications; Epigenetic-based differentiation therapy for Acute Myeloid Leukemia.pdf>)

Two lysine deacetylase inhibitors, CM-444 and CM-1758, are identified and characterised as promoting myeloid differentiation across all AML subtypes at low non-cytotoxic doses, unlike other commercial HDAC inhibitors. Acetylome analysis after treatment reveals modulation of non-histone proteins in the enhancer-promoter chromatin regulatory complex, including bromodomain proteins, and this acetylation is essential for enhancing expression of the transcription factors that drive the differentiation response. The compounds are proposed as differentiation-based therapeutic agents applicable across AML subtypes.

### Radzisheuskaya (2023). *The EMBO Journal.* An alternative NURF complex sustains acute myeloid leukemia by regulating the accessibility of insulator regions
[doi:10.15252/embj.2023114221](https://doi.org/10.15252/embj.2023114221) · `paper`  
[src](<../raw/Radzisheuskaya(2023) The EMBO Journal; An alternative NURF complex sustains acute myeloid leukemia by regulating the accessibility of insulator regions.pdf>)

A CRISPRi screen against chromatin factors identified the NURF subunit BPTF as essential for AML cell survival. BPTF forms an alternative NURF complex with SMARCA5 and BAP18 that regulates accessibility at a large set of insulator regions, ensuring efficient CTCF binding and boundary formation between topologically associated domains, which maintains the leukemic transcriptional program - including the interaction between the BENC enhancer and the MYC promoter. The well-studied PHD2-BROMO chromatin reader domains of BPTF contribute to recruitment but are dispensable for leukemic growth.

### Yan (2022). *Cancer Discovery.* KAT6A and ENL Form an Epigenetic Transcriptional Control Module to Drive Critical Leukemogenic Gene-Expression Programs
[doi:10.1158/2159-8290.CD-20-1459](https://doi.org/10.1158/2159-8290.CD-20-1459) · `paper`  
[src](<../raw/Yan(2022) Cancer Discovery; KAT6A and ENL Form an Epigenetic Transcriptional Control Module to Drive Critical Leukemogenic Gene-Expression Programs.pdf>)

A differentiation-focused CRISPR screen in AML cells identified the histone acetyltransferase KAT6A as a regulator of myeloid differentiation driving leukemogenic gene expression programs. KAT6A initiates a transcriptional control module in which KAT6A-catalysed promoter H3K9ac is bound by the acetyllysine reader ENL, which in turn cooperates with chromatin factors to induce transcriptional elongation. KAT6A inhibition has strong anti-AML effects in vitro and in vivo, supporting small-molecule KAT6A inhibitors for mono or combinatorial differentiation-based treatment.

### Barabino (2021). *Cancers.* Transcription Factors, R-Loops and Deubiquitinating Enzymes: Emerging Targets in Myelodysplastic Syndromes and Acute Myeloid Leukemia
[doi:10.3390/cancers13153753](https://doi.org/10.3390/cancers13153753) · `paper`  
[src](<../raw/Barabino(2021) Cancers; Transcription Factors, R-Loops and Deubiquitinating Enzymes Emerging Targets in Myelodysplastic Syndromes and Acute Myeloid Leukemia.pdf>)

A review of three classes of emerging therapeutic target in myelodysplastic syndromes and AML: transcription factors governing myeloid differentiation, RNA splicing factors whose mutations increase R-loop formation, and deubiquitinating enzymes contributing to genome stability in hematopoietic stem cells. It frames myeloid neoplasms as a failure of the equilibrium between HSC self-renewal and differentiated output, traces driver mutations back to HSC/progenitor cells, and describes the clonal mosaic that results as subclones accumulate further mutations.

### Gu (2021). *Nature Genetics.* Silencing of LINE-1 retrotransposons is a selective dependency of myeloid leukemia
[doi:10.1038/s41588-021-00829-8](https://doi.org/10.1038/s41588-021-00829-8) · `paper`  
[src](<../raw/Gu(2021) Nature Genetics; Silencing of LINE-1 retrotransposons is a selective dependency of myeloid leukemia.pdf>)

An epigenetic regulator-focused CRISPR screen identifies MPHOSPH8/MPP8, a component of the human silencing hub (HUSH) complex, as an AML-selective dependency. MPP8 is dispensable for steady-state hematopoiesis, but its loss inhibits AML development by reactivating LINE-1 retrotransposons, inducing a DNA damage response and cell cycle exit. Activating endogenous or ectopic L1s mimics MPP8 loss, while blocking retrotransposition abrogates the phenotype. AML oncogenic mutations promote L1 suppression, and enhanced L1 silencing is associated with poor prognosis in human AML - so retrotransposons act here as tumour suppressors rather than cancer promoters.

### Domingues (2020). *eLife.* Loss of Kat2a enhances transcriptional noise and depletes acute myeloid leukemia stem-like cells
[doi:10.7554/eLife.51754](https://doi.org/10.7554/eLife.51754) · `paper`  
[src](<../raw/Domingues(2020) eLife; Loss of Kat2a enhances transcriptional noise and depletes acute myeloid leukemia stem-like cells.pdf>)

Combining chromatin profiling with single-cell transcriptomics in a conditional knockout mouse, the authors show that the histone acetyltransferase Kat2a supports leukemia propagation by preserving leukemia stem-like cells in MLL-AF9 AML. Kat2a loss alters transcription factor binding and reduces transcriptional burst frequency at a subset of promoters, increasing variability in transcript levels; the resulting destabilisation of target programs shifts leukemia cells out of self-renewal into differentiation. The authors propose that control of transcriptional variability is central to leukemia stem-like cell propagation.

### Maiques-Diaz (2018). *Cell Reports.* Enhancer Activation by Pharmacologic Displacement of LSD1 from GFI1 Induces Differentiation in Acute Myeloid Leukemia
[doi:10.1016/j.celrep.2018.03.012](https://doi.org/10.1016/j.celrep.2018.03.012) · `paper`  
[src](<../raw/Maiques-Diaz(2018) Cell Reports; Enhancer Activation by Pharmacologic Displacement of LSD1 from GFI1 Induces Differentiation in Acute Myeloid Leukemia.pdf>)

LSD1 inhibitors induce differentiation in MLL-translocated AML, and the assumption had been that this works by blocking LSD1's histone demethylase activity. The authors observe rapid, extensive drug-induced transcriptional changes without genome-wide accumulation of the targeted histone modifications. Instead, inhibitors disrupt the GFI1/CoREST complex and release it from enhancers, and this disruption is required for differentiation; loss of enhancer-bound GFI1/LSD1 activates nearby myeloid transcription factor genes. Fusion constructs mimicking constitutively active GFI1 prevent drug-induced differentiation, and mutation of the K661 residue is identified as a resistance mechanism to tranylcypromine-derivative inhibitors.

### Erb (2017). *Nature.* Transcription control by the ENL YEATS domain in acute leukaemia
[doi:10.1038/nature21688](https://doi.org/10.1038/nature21688) · `paper`  
[src](<../raw/Erb(2017) Nature; Transcription control by the ENL YEATS domain in acute leukaemia.pdf>)

A genome-scale CRISPR-Cas9 loss-of-function screen in an MLL-AF4-positive leukemia line identifies ENL as specifically required for proliferation in vitro and in vivo. Using a chemical genetic strategy for targeted protein degradation (dTAG), acute loss of ENL is shown to suppress initiation and elongation of RNA polymerase II at active genes genome-wide, with the most pronounced effects at genes carrying a disproportionate ENL load. An intact YEATS chromatin-reader domain is essential for ENL-dependent leukemic growth, while Enl loss minimally affects normal Lin-Sca-1+c-Kit+ mouse hematopoietic progenitors.

## DNA methylation, TET/IDH and the mutational landscape

*6 papers.* Methylation as cause rather than consequence, and the metabolic lesions that write it. Includes the ageing hematopoietic stem cell, which arrives at an AML-like epigenome before any driver mutation does.

### Heyes (2023). *Nature Communications.* TET2 lesions enhance the aggressiveness of CEBPA-mutant acute myeloid leukemia by rebalancing GATA2 expression
[doi:10.1038/s41467-023-41927-x](https://doi.org/10.1038/s41467-023-41927-x) · `paper`  
[src](<../raw/Heyes(2023) Nature Communications; TET2 lesions enhance the aggressiveness of CEBPA-mutant acute myeloid leukemia by rebalancing GATA2 expression.pdf>)

Combining transcriptomic and epigenomic analysis of CEBPA-TET2 co-mutated patients with mouse models, the authors identify GATA2 as the conserved target of the CEBPA-TET2 mutational axis. Elevated CEBPA levels driven by hypermorphic N-terminal mutations recruit TET2 to the Gata2 distal hematopoietic enhancer, increasing Gata2 expression; concurrent TET2 loss confers a competitive advantage by increasing Gata2 promoter methylation and rebalancing GATA2 levels. Demethylating treatment of Cebpa-Tet2 co-mutated AML restores Gata2 levels and prolongs disease latency.

### Ježek (2020). *Antioxidants & Redox Signaling.* 2-Hydroxyglutarate in Cancer Cells
[doi:10.1089/ars.2019.7902](https://doi.org/10.1089/ars.2019.7902) · `paper`  
[src](<../raw/Ježek(2020) Antioxidants & Redox Signaling; 2-Hydroxyglutarate in Cancer Cells.pdf>)

A review of 2-hydroxyglutarate as an oncometabolite across cancers including AML. Heterozygous mutations at the active sites of IDH1 (R132H) and mitochondrial IDH2 (R140Q) give cells millimolar R-2HG, while side activities of lactate and malate dehydrogenase produce submillimolar S-2HG; even wild-type IDH1/2, under reductive carboxylation glutaminolysis, yields intermediate 0.01-0.1 mM levels against 10^-8 M in non-cancer cells. 2HG inhibits 2-oxoglutarate-dependent dioxygenases, blocking DNA and histone demethylation, interferes with HIF transcriptome reprogramming and mTOR signalling, contributes to oxidative stress, and acts in tumour-immune crosstalk, including directing differentiation of naive T lymphocytes.

### Kishtagari (2020). *Current Opinion in Hematology.* Driver mutations in acute myeloid leukemia
[doi:10.1097/MOH.0000000000000567](https://doi.org/10.1097/MOH.0000000000000567) · `paper`  
[src](<../raw/Kishtagari(2020) Current Opinion in Hematology; Driver mutations in acute myeloid leukemia.pdf>)

A review of recurrently mutated genes in AML and their functional consequences beyond conventional oncogene activation and tumour suppressor loss. It covers the 40-50 genes carrying recurrent somatic mutations, organised around DNA methylation effectors, chromatin modifiers, spliceosomal machinery and transcription factors, and notes that many of these mutations are found across a spectrum from clonal hematopoiesis through myelodysplasia to overt AML. Mutation-based targeted therapy has produced several FDA-approved drugs, and the review argues that understanding the pathophysiologic functions of these genes is what will translate genomics into treatment.

### Adelman (2019). *Cancer Discovery.* Aging Human Hematopoietic Stem Cells Manifest Profound Epigenetic Reprogramming of Enhancers That May Predispose to Leukemia
[doi:10.1158/2159-8290.CD-18-1474](https://doi.org/10.1158/2159-8290.CD-18-1474) · `paper`  
[src](<../raw/Adelman(2019) Cancer Discovery; Aging Human Hematopoietic Stem Cells Manifest Profound Epigenetic Reprogramming of Enhancers That May Predispose to Leukemia.pdf>)

An integrative epigenomic and transcriptomic characterisation of normal human ageing in Lineage-CD34+CD38- HSC-enriched cells, combining histone marks, DNA methylation and single-cell RNA sequencing. Aged cells show redistributed DNA methylation and reduced H3K27ac, H3K4me1 and H3K4me3, losing 4646 active enhancers and 3091 bivalent promoters at developmental and cancer pathways that are comparably altered in AML of all ages. Downregulating KLF6 in vitro impairs differentiation, increases colony-forming potential, and reproduces both ageing and leukemia expression signatures.

### Cimmino (2017). *Cell.* Restoration of TET2 Function Blocks Aberrant Self-Renewal and Leukemia Progression
[doi:10.1016/j.cell.2017.07.032](https://doi.org/10.1016/j.cell.2017.07.032) · `paper`  
[src](<../raw/Cimmino(2017) Cell; Restoration of TET2 Function Blocks Aberrant Self-Renewal and Leukemia Progression.pdf>)

Using a reversible transgenic RNAi mouse to model restoration of endogenous Tet2 expression, the authors show that Tet2 restoration reverses aberrant hematopoietic stem and progenitor cell self-renewal in vitro and in vivo, promoting DNA demethylation, differentiation and cell death. Vitamin C, a cofactor of Fe2+ and alpha-ketoglutarate-dependent dioxygenases, mimics restoration by enhancing 5-hydroxymethylcytosine generation and blocks leukemia progression, and it also sensitises leukemia cells to PARP inhibition.

### Ferreira (2015). *Oncogene.* DNMT3A mutations mediate the epigenetic reactivation of the leukemogenic factor MEIS1 in acute myeloid leukemia
[doi:10.1038/onc.2015.359](https://doi.org/10.1038/onc.2015.359) · `paper`  
[src](<../raw/Ferreira(2015) Oncogene; DNMT3A mutations mediate the epigenetic reactivation of the leukemogenic factor MEIS1 in acute myeloid leukemia.pdf>)

Whole-genome bisulfite sequencing and DNA methylation microarrays of a DNMT3A-mutant AML line (OCI-AML3, R882C) against a wild-type line identify MEIS1, the leukemogenic HOX cofactor, as undergoing promoter hypomethylation-associated transcriptional reactivation. Screening 68 AML patients and validating in an independent cohort of 194, the authors define a 12-gene hypomethylation signature enriched in DNMT3A-mutant cases and associated with shorter overall survival. The conclusion is that in the absence of MLL fusions, DNMT3A mutations provide an alternative route to an oncogenic MEIS1-dependent transcriptional program.

## Chromatin accessibility and 3D genome organisation

*8 papers.* Where the genome is open and what is looped to what. The measurements are recent enough that the largest single-cancer epigenomic dataset ever assembled is in this topic, and it finds subtypes no genetic classification contains.

### Ochi (2026). *Nature.* Chromatin landscape and epigenetic heterogeneity of acute myeloid leukaemia
[doi:10.1038/s41586-026-10703-4](https://doi.org/10.1038/s41586-026-10703-4) · `paper`  
[src](<../raw/Ochi(2026) Nature; Chromatin landscape and epigenetic heterogeneity of acute myeloid leukaemia.pdf>)

ATAC-seq in 1563 individuals with newly diagnosed AML (the eCHROMA cohort) classifies the disease into 16 subgroups by chromatin accessibility. Multiomics analysis of mutations, transcriptome, DNA methylation and histone marks shows these subgroups have distinct driver mutations, differentiation states, expression, methylation and super-enhancer profiles, and are associated with clinical outcomes, validated in independent cohorts. Single-cell ATAC shows all leukemic cells within a subgroup share a common accessibility profile. The subgroups have distinct gene-regulatory networks driven by hematopoietic transcription factors with subgroup-specific super-enhancers, have independent prognostic effect beyond genomic classification, and are associated with particular drug sensitivities.

### Fischer (2024). *Cell Reports.* STAG2 mutations reshape the cohesin-structured spatial chromatin architecture to drive gene regulation in acute myeloid leukemia
[doi:10.1016/j.celrep.2024.114498](https://doi.org/10.1016/j.celrep.2024.114498) · `paper`  
[src](<../raw/Fischer(2024) Cell Reports; STAG2 mutations reshape the cohesin-structured spatial chromatin architecture to drive gene regulation in acute myeloid leukemia.pdf>)

A characterisation of genetic, transcriptional and chromatin conformational changes in a sizable cohort of primary AML samples, addressing why STAG2 but not its paralog STAG1 is frequently mutated in myeloid malignancy. Specific loci show altered cohesin occupancy, gene expression and local chromatin activation that the remaining STAG1-cohesin does not compensate, linked to disrupted spatial chromatin looping. Depleting STAG2 or STAG1 in primary human CD34+ HSPCs reproduces STAG2-mutant AML-specific changes only for STAG2, and STAG2-deficient HSPCs show impaired differentiation and maintain HSPC-like gene expression.

### Sui (2024). *Experimental Hematology & Oncology.* Three-dimensional chromatin landscapes in MLLr AML
[doi:10.1186/s40164-024-00523-5](https://doi.org/10.1186/s40164-024-00523-5) · `paper`  
[src](<../raw/Sui(2024) Experimental Hematology & Oncology; Three-dimensional chromatin landscapes in MLLr AML.pdf>)

An integrative analysis of 3D genome structure, chromatin accessibility and gene expression in gene-edited MLL-AF9 AML cells against normal cord blood CD34+ controls, combining ATAC-seq and RNA-seq with Micro-C at around 800 million paired-end reads per library. The data reveal MLL-rearrangement-specific alterations of chromatin accessibility, A/B compartments, topologically associating domains and chromatin loops, with 5731 healthy donor-specific and 2679 AML-specific loops. Local 3D configuration is rewired at loci associated with AML-specific expression, including inter-chromosomal enhancer- and silencer-hijacking events.

### Li (2022). *Blood.* HMGA1 chromatin regulators induce transcriptional networks involved in GATA2 and proliferation during MPN progression
[doi:10.1182/blood.2021013925](https://doi.org/10.1182/blood.2021013925) · `paper`  
[src](<../raw/Li(2022) Blood; HMGA1 chromatin regulators induce transcriptional networks involved in GATA2 and proliferation during MPN progression.pdf>)

HMGA1 is identified as a driver of myeloproliferative neoplasm progression to myelofibrosis and AML, upregulated in MPN with highest levels after transformation. Depleting HMGA1 in JAK2V617F AML cell lines disrupts proliferation, clonogenicity and leukemic engraftment, and loss of a single Hmga1 allele prevents progression to myelofibrosis in JAK2V617F mice. RNA-seq and ChIP-seq show HMGA1 networks and chromatin occupancy at proliferation genes and at the GATA2 master regulator, which HMGA1 transactivates through sequences near the +9.5 developmental enhancer; silencing GATA2 recapitulates most HMGA1-depletion phenotypes and its re-expression partially rescues leukemogenesis. HMGA1 depletion also enhances responses to ruxolitinib.

### Xu (2022). *Nature.* Subtype-specific 3D genome alteration in acute myeloid leukaemia
[doi:10.1038/s41586-022-05365-x](https://doi.org/10.1038/s41586-022-05365-x) · `paper`  
[src](<../raw/Xu(2022) Nature; Subtype-specific 3D genome alteration in acute myeloid leukaemia.pdf>)

Hi-C and whole-genome sequencing of 25 AML patient samples and 7 healthy donors identified recurrent and subtype-specific alterations in A/B compartments, topologically associating domains and chromatin loops. RNA-seq, ATAC-seq and CUT&Tag for CTCF, H3K27ac and H3K27me3 in the same samples revealed extensive recurrent AML-specific promoter-enhancer and promoter-silencer loops, with the role of repressive loops validated by CRISPR deletion and interference. Structural-variation-induced enhancer-hijacking and silencer-hijacking events were identified; hijacked enhancers contribute to cell growth by CRISPR screening while hijacked silencers downregulate targets. Whole-genome bisulfite sequencing of 20 samples related DNA methylation, CTCF binding and 3D structure, and hypomethylating treatment with triple DNMT knockdown reverted 3D organisation and gene expression.

### Tothova (2021). *JCI Insight.* Cohesin mutations alter DNA damage repair and chromatin structure and create therapeutic vulnerabilities in MDS/AML
[doi:10.1172/jci.insight.142149](https://doi.org/10.1172/jci.insight.142149) · `paper`  
[src](<../raw/Tothova(2021) JCI Insight; Cohesin mutations alter DNA damage repair and chromatin structure and create therapeutic vulnerabilities in MDS AML.pdf>)

Genetic dependency screens in STAG2-mutant AML identified DNA damage repair and replication as dependencies in cohesin-mutant cells, with increased DNA damage and sensitivity to PARP inhibition. A mouse model of MDS in which Stag2 mutations arose as secondary lesions on a background of Tet2-driven clonal hematopoiesis showed selective depletion of cohesin-mutant cells with PARP inhibition in vivo, and talazoparib reduced disease burden and improved survival in STAG2- and RAD21-mutant AML patient-derived xenografts. Mechanistically, cohesin-mutant cells shift from STAG2- to STAG1-containing complexes, producing longer DNA loop extrusion, loss of insulation at TAD boundaries, intermixing of chromatin compartments, and increased interaction with PARP and replication protein A.

### Assi (2018). *Nature Genetics.* Subtype-specific regulatory network rewiring in acute myeloid leukemia
[doi:10.1038/s41588-018-0270-1](https://doi.org/10.1038/s41588-018-0270-1) · `paper`  
[src](<../raw/Assi(2018) Nature Genetics; Subtype-specific regulatory network rewiring in acute myeloid leukemia.pdf>)

A global analysis of cis-regulatory element activity and interaction, transcription factor occupancy and gene expression in purified leukemic blasts from AML patients grouped by mutation - RUNX1, CEBPA, FLT3-ITD, RAS and NPM1. Combining DNaseI footprinting, capture Hi-C promoter interaction mapping and expression profiling, the authors show that each mutant regulator establishes a specific transcriptional and signaling network unrelated to that of normal cells, and that AP-1 activity is a shared growth dependency across multiple subtypes.

### Corces (2016). *Nature Genetics.* Lineage-specific and single-cell chromatin accessibility charts human hematopoiesis and leukemia evolution
[doi:10.1038/ng.3646](https://doi.org/10.1038/ng.3646) · `paper`  
[src](<../raw/Corces(2016) Nature Genetics; Lineage-specific and single-cell chromatin accessibility charts human hematopoiesis and leukemia evolution.pdf>)

Chromatin accessibility and transcriptional landscapes are defined in 13 human primary blood cell types spanning the hematopoietic hierarchy, using Fast-ATAC, an ATAC-seq protocol optimised for blood cells: 137 samples from 9 healthy donors and 12 AML patients covering 16 cell types, with paired transcriptomes for 96. Distal enhancer landscapes reflect cell identity better than mRNA (91% cluster purity versus 78%), enabling 'enhancer cytometry' to enumerate pure cell types from mixtures. In AML, chromatin accessibility reveals regulatory evolution tracking mutation burden, single cells show mixed regulome profiles corresponding to disparate developmental stages, and accounting for that heterogeneity implicates HOX factors as regulators of preleukemic HSC characteristics.


# C. RNA processing: splicing, isoforms and modification

## Splicing factor mutations and splicing-directed therapy

*10 papers.* Mutations in SRSF2, U2AF1 and SF3B1 are always heterozygous and never co-occur, which predicts a synthetic lethality and has driven a whole therapeutic programme. The prediction holds; the therapeutic window is narrower than hoped.

### Khan (2025). *Scientific Reports.* Revealing the role of U2AF1 in splicing regulation and chimeric RNA dynamics
[doi:10.1038/s41598-025-99865-1](https://doi.org/10.1038/s41598-025-99865-1) · `paper`  
[src](<../raw/Khan(2025) Scientific Reports; Revealing the role of U2AF1 in splicing regulation and chimeric RNA dynamics.pdf>)

U2AF1, the splicing factor that recognises 3' splice sites and is recurrently mutated in MDS and AML, is examined for its role in chimeric RNA formation. Using knockdown and overexpression in leukemia and esophageal cancer cell lines with paired-end RNA sequencing and the SOAPfuse algorithm, the authors report significant changes in the chimeric RNA landscape following U2AF1 knockdown, concluding that U2AF1 has a critical role in the formation and regulation of distinct categories of chimeric RNA.

### Kim (2025). *Cell.* Mis-splicing-derived neoantigens and cognate TCRs in splicing factor mutant leukemias
[doi:10.1016/j.cell.2025.03.047](https://doi.org/10.1016/j.cell.2025.03.047) · `paper`  
[src](<../raw/Kim(2025) Cell; Mis-splicing-derived neoantigens and cognate TCRs in splicing factor mutant leukemias.pdf>)

The authors identify neoantigens translated from highly stereotyped splicing alterations caused by neomorphic leukemia-associated splicing factor mutations, and use feature-barcoded peptide-MHC dextramers to isolate neoantigen-reactive T cell receptors from healthy donors, patients with active myeloid malignancy, and patients after curative allogeneic transplant. Neoantigen-reactive CD8+ T cells were present in the blood of patients with active disease but had a phenotype distinct from virus-reactive T cells, with defective NF-kB proinflammatory pathways and impaired cytotoxic function. T cells engineered with TCRs against SRSF2-mutant-induced neoantigens from mis-splicing of CLK3 and RHOT2 specifically recognised and killed SRSF2-mutant leukemia.

### Saika (2025). *International Journal of Hematology.* BRD9 depletion-mediated ALOX5 upregulation via chromatin dysregulation induces ferroptosis in SF3B1-mutant hematopoiesis
[doi:10.1007/s12185-025-04105-x](https://doi.org/10.1007/s12185-025-04105-x) · `paper`  
[src](<../raw/Saika(2025) International Journal of Hematology; BRD9 depletion-mediated ALOX5 upregulation via chromatin dysregulation induces ferroptosis in SF3B1-mutant hematopoiesis.pdf>)

Building on the finding that SF3B1 mutations cause nonsense-mediated decay of BRD9, a core non-canonical BAF component, the authors show that BRD9 depletion markedly upregulates ALOX5, which oxidises polyunsaturated fatty acids. BRD9 and ALOX5 expression are negatively correlated and SF3B1 mutation associates with ALOX5 upregulation in AML datasets, preferentially in mature myeloid lineages rather than stem/progenitor fractions. Integrated RNA-seq, ChIP-seq and Hi-C show BRD9 loss enhances CTCF occupancy at the ALOX5 locus boundary, enabling aberrant chromatin loop formation that activates transcription, increasing lipid peroxidation and ferroptosis susceptibility as shown by BODIPY-C11 oxidation and erastin sensitivity.

### Venkatasubramanian (2025). *Science Translational Medicine.* Splicing regulatory dynamics for precision analysis and treatment of heterogeneous leukemias
[doi:10.1126/scitranslmed.adr1471](https://doi.org/10.1126/scitranslmed.adr1471) · `paper`  
[src](<../raw/Venkatasubramanian(2025) Science Translational Medicine; Splicing regulatory dynamics for precision analysis and treatment of heterogeneous leukemias.pdf>)

OncoSplice, an unsupervised computational workflow, defines tumour molecular landscapes from splicing profiles. In adult and pediatric AML it identified the spectrum of driver genetics from splicing alone, defined over a dozen new recurrent molecular subtypes, and discovered a dominant subtype partially phenocopying U2AF1-mutant splicing. This U2AF1-like subtype spans pediatric and adult AML genetics despite pediatric leukemias lacking splicing factor mutations, and consistently predicts poor prognosis. Long-read single-cell RNA-seq confirmed the splicing programme is shared across cell states, co-opts a healthy circadian gene programme, is stable through relapse, and induces a leukemia stem cell programme. PRMT5 inhibition rescued the mis-splicing and inhibited growth, and deleting IRAK4 blocked leukemia development in xenografts and induced differentiation.

### Liu (2024). *Journal of Clinical Investigation.* A mitochondrial surveillance mechanism activated by SRSF2 mutations in hematologic malignancies
[doi:10.1172/JCI175619](https://doi.org/10.1172/JCI175619) · `paper`  
[src](<../raw/Liu(2024) Journal of Clinical Investigation; A mitochondrial surveillance mechanism activated by SRSF2 mutations in hematologic malignancies.pdf>)

The pathogenic SRSF2 P95H mutation is shown to disrupt splicing of mitochondrial mRNAs, impair complex I function and robustly increase mitophagy. The authors identify a mitochondrial surveillance mechanism whereby mitochondrial dysfunction modifies splicing of the mitophagy activator PINK1 to remove a poison intron, increasing PINK1 mRNA stability and protein abundance; SRSF2 P95H-induced dysfunction raises PINK1 through this route, which is essential for mutant cell survival. Inhibiting splicing with a GSK-3 inhibitor promotes poison intron retention, impairing mitophagy and activating apoptosis in SRSF2 P95H cells.

### vanderWerf (2023). *Cell Reports Medicine.* Detection and targeting of splicing deregulation in pediatric acute myeloid leukemia stem cells
[doi:10.1016/j.xcrm.2023.100962](https://doi.org/10.1016/j.xcrm.2023.100962) · `paper`  
[src](<../raw/vanderWerf(2023) Cell Reports Medicine; Detection and targeting of splicing deregulation in pediatric acute myeloid leukemia stem cells.pdf>)

Pediatric AML has high relapse rates and few somatic mutations, and splicing deregulation had not been studied there. Using single-cell proteogenomics, transcriptome-wide analysis of FACS-purified hematopoietic stem and progenitor cells with differential splicing analysis, dual-fluorescence lentiviral splicing reporter assays and humanized mouse models, the authors found transcriptomic splicing deregulation typified by differential exon usage, downregulation of the splicing regulator RBFOX2, and upregulation of a CD47 splice isoform. The splicing modulator Rebecsinib produced a therapeutic vulnerability in survival, self-renewal and splicing reporter assays.

### Wang (2023). *Cancer Cell.* Modulation of RNA splicing enhances response to BCL2 inhibition in leukemia
[doi:10.1016/j.ccell.2022.12.002](https://doi.org/10.1016/j.ccell.2022.12.002) · `paper`  
[src](<../raw/Wang(2023) Cancer Cell; Modulation of RNA splicing enhances response to BCL2 inhibition in leukemia.pdf>)

CRISPR-Cas9 screens across a range of AML therapies identified a selective dependency on RNA splicing factors whose loss preferentially enhances venetoclax response. Loss of the splicing factor RBM10 augments venetoclax response while being completely dispensable for normal hematopoiesis; combined RBM10 and BCL2 inhibition causes mis-splicing and inactivation of the apoptosis inhibitor XIAP and downregulation of BCL2A1, an anti-apoptotic protein implicated in venetoclax resistance. Inhibiting the CLK and DYRK splicing kinase families produces aberrant splicing of key splicing and apoptotic factors that synergises with venetoclax and overcomes resistance.

### Yoshimi (2019). *Nature.* Coordinated alterations in RNA splicing and epigenetic regulation drive leukaemogenesis
[doi:10.1038/s41586-019-1618-0](https://doi.org/10.1038/s41586-019-1618-0) · `paper`  
[src](<../raw/Yoshimi(2019) Nature; Coordinated alterations in RNA splicing and epigenetic regulation drive leukaemogenesis.pdf>)

Analysis of transcriptomes from 982 AML patients identified frequent overlap of IDH2 and SRSF2 mutations - 47% of SRSF2-mutant patients also had IDH2 mutation and 56% of IDH2-mutant patients had SRSF2 mutation - with high, correlated variant allele frequencies indicating early events. Although each mutation alone imparts distinct splicing changes, co-expressing mutant IDH2 alters the splicing effects of mutant SRSF2 and produces more profound changes than either alone. Co-expression caused lethal myelodysplasia with proliferative features in vivo and enhanced self-renewal not seen with either mutation alone. Double-mutant cells showed aberrant splicing and reduced INTS3, a member of the integrator complex, with increased RNA polymerase II stalling.

### Keightley (2018). *Seminars in Cell & Developmental Biology.* Splicing dysfunction and disease: The case of granulopoiesis
[doi:10.1016/j.semcdb.2017.08.048](https://doi.org/10.1016/j.semcdb.2017.08.048) · `paper`  
[src](<../raw/Keightley(2018) Seminars in Cell & Developmental Biology; Splicing dysfunction and disease The case of granulopoiesis.pdf>)

A review of splicing as a regulator of neutrophil development and of splicing dysfunction in disease. It surveys cis-splicing variation in individual genes and trans-regulation of global splicing outcomes during normal granulopoiesis - including intron retention as a regulator of granulopoietic maturation - and then examines the contribution of splicing dysfunction to diseases of neutrophil number, function and maturation, including severe congenital neutropenia, myelodysplasia and acute myeloid leukemia.

### Lee (2016). *Nature Medicine.* Modulation of splicing catalysis for therapeutic targeting of leukemia with mutations in genes encoding spliceosomal proteins
[doi:10.1038/nm.4097](https://doi.org/10.1038/nm.4097) · `paper`  
[src](<../raw/Lee(2016) Nature Medicine; Modulation of splicing catalysis for therapeutic targeting of leukemia with mutations in genes encoding spliceosomal proteins.pdf>)

Spliceosomal gene mutations in MDS and AML are always heterozygous and rarely co-occur, suggesting cells tolerate only partial deviation from normal splicing. Testing this, mice engineered to express Srsf2P95H in an inducible, hemizygous manner in hematopoietic cells rapidly succumbed to fatal bone marrow failure, showing that Srsf2-mutated cells depend on the wild-type allele. The spliceosome inhibitor E7107 substantially reduced leukemic burden specifically in isogenic mouse leukemias and patient-derived xenograft AMLs carrying spliceosomal mutations; E7107 caused widespread intron retention and exon skipping regardless of genotype, but the magnitude of splicing inhibition was greater in Srsf2-mutant cells.

## Splicing regulators and RNA-binding proteins as dependencies

*12 papers.* The proteins that decide which isoform gets made, and what happens when a leukemia needs one of them more than a normal cell does. This is where most of the collection's genuinely AML-selective targets are.

### Cao (2026). *Leukemia.* PTBP1 controls oncogenic transcript processing and maintenance of acute myeloid leukemia
[doi:10.1038/s41375-026-03098-8](https://doi.org/10.1038/s41375-026-03098-8) · `paper`  
[src](<../raw/Cao(2026) Leukemia; PTBP1 controls oncogenic transcript processing and maintenance of acute myeloid leukemia.pdf>)

A domain-focused CRISPR screen of 3182 sgRNAs targeting 527 RNA-enzymatic and binding domains across 341 RNA-associated proteins identifies several RNA-binding proteins as AML dependencies - including the splicing factor PTBP1 and the m6A reader RBM15 - biased toward KMT2A-rearranged AML. All four RNA-binding domains of PTBP1 are required for KMT2A-r proliferation. PTBP1 is dispensable for myelopoiesis, but its suppression in AML causes cell cycle arrest, apoptosis and myeloid differentiation; transcriptomics shows disruption of the KMT2A-r-essential program and widespread splicing dysregulation, and CLIP-seq shows preferential binding to transcripts critical for KMT2A-r proliferation including IKZF1, MEF2C, EZH2, SIK3 and PBX3.

### Guo (2026). *Nature Cancer.* PAPOLA-mediated hyperactive polyadenylation promotes leukemogenesis and leukemia stem cell self-renewal through metabolic reprogramming
[doi:10.1038/s43018-026-01190-7](https://doi.org/10.1038/s43018-026-01190-7) · `paper`  
[src](<../raw/Guo(2026) Nature Cancer; PAPOLA-mediated hyperactive polyadenylation promotes leukemogenesis and leukemia stem cell self-renewal through metabolic reprogramming.pdf>)

Widespread poly(A) tail elongation and upregulation of poly(A) polymerase alpha (PAPOLA) are identified in AML, with high PAPOLA expression associated with poor outcomes; PAPOLA upregulation is most pronounced in AML among tumour types while its expression in normal blood cells is the lowest among normal controls. Using primary AML samples, cell lines and multiple mouse models, PAPOLA-driven hyperactive polyadenylation is shown to promote leukemogenesis and sustain leukemia stem cell maintenance, acting through upregulation of glutathione S-transferase mu 2 (GSTM2), which activates a 4-hydroxynonenal (HNE)-dihydrolipoamide dehydrogenase (DLD) axis. Pharmacological inhibition of PAPOLA with cordycepin suppresses metabolic reprogramming and impairs leukemogenesis.

### Sgueglia (2026). *Cell Death & Disease.* Dynamic epigenetic regulation of BCLAF1 splicing in acute myeloid leukemia
[doi:10.1038/s41419-026-08594-4](https://doi.org/10.1038/s41419-026-08594-4) · `paper`  
[src](<../raw/Sgueglia(2026) Cell Death & Disease; Dynamic epigenetic regulation of BCLAF1 splicing in acute myeloid leukemia.pdf>)

Two unbalanced isoforms of BCL2-associated transcription factor 1 (BCLAF1) are identified in AML cell lines - a full-length isoform with oncogenic properties and a short isoform that appears tumour-suppressive. Treatment with specific epidrugs re-establishes the physiological balance between them. ChIP analysis after SAHA treatment localised the regulation to exon 5 rather than the promoter, with increased acetylation and H3K4me3 and decreased H3K36me3 at specific regions, and co-immunoprecipitation showed that HDAC1 and DNMT3A interact under basal conditions and that this interaction is disrupted by SAHA, while DNMT3B binding is unchanged.

### Han (2025). *Blood Cancer Discovery.* An Isoform-Specific RUNX1C–BTG2 Axis Governs AML Quiescence and Chemoresistance
[doi:10.1158/2643-3230.BCD-24-0327](https://doi.org/10.1158/2643-3230.BCD-24-0327) · `paper`  
[src](<../raw/Han(2025) Blood Cancer Discovery; An Isoform-Specific RUNX1C–BTG2 Axis Governs AML Quiescence and Chemoresistance.pdf>)

A paired analysis of RNA isoform changes in AML patients before therapy and at relapse identifies intragenic DNA methylation at the proximal RUNX1 promoter, driving elevated expression of the long isoform RUNX1C from its alternative distal promoter. The unique N-terminal region of RUNX1C directs an isoform-specific transcriptional program promoting chemoresistance, with the direct target BTG2 implicated: BTG2 promotes rRNA deadenylation, decreasing mRNA expression and stability, and increasing cellular quiescence. RNA-based targeting of RUNX1C reactivates quiescent leukemia cells and enhances chemotherapy efficacy.

### Zhang (2024). *Genome Biology.* RNA-binding protein RBM5 plays an essential role in acute myeloid leukemia by activating the oncogenic protein HOXA9
[doi:10.1186/s13059-023-03149-8](https://doi.org/10.1186/s13059-023-03149-8) · `paper`  
[src](<../raw/Zhang(2024) Genome Biology; RNA-binding protein RBM5 plays an essential role in acute myeloid leukemia by activating the oncogenic protein HOXA9.pdf>)

Genome-wide CRISPR/Cas9 screening in HOXA9-driven reporter acute leukemia cells identified the poorly characterised RNA-binding protein RBM5 as the top candidate required for leukemia cell fitness. RBM5 is highly overexpressed in AML patients relative to healthy individuals, and its loss by knockout or knockdown impairs leukemia maintenance in vitro and in vivo. Domain CRISPR screening showed RBM5 acts through a non-canonical transcriptional regulation circuitry rather than RNA splicing, dependent on its DNA-binding domains. HOXA9 is the downstream target: ectopic HOXA9 rescues the proliferation defect, and acute RBM5 degradation via an auxin-inducible degron immediately reduces HOXA9 transcription.

### Wu (2023). *PLOS Biology.* Single-cell transcriptome analyses reveal critical roles of RNA splicing during leukemia progression
[doi:10.1371/journal.pbio.3002088](https://doi.org/10.1371/journal.pbio.3002088) · `paper`  
[src](<../raw/Wu(2023) PLOS Biology; Single-cell transcriptome analyses reveal critical roles of RNA splicing during leukemia progression.pdf>)

Serial single-cell transcriptome analyses of preleukemic and leukemic cells construct the cellular and molecular transformation trajectory in a Myc-driven AML mouse model. Myc targets were gradually upregulated along the trajectory, including splicing factors whose expression showed stage-specific prognostic value in patients. The authors dissect a tipping point at which hematopoietic stem and progenitor cells generate initiating preleukemic cells, characterised by dramatically increased splicing factors and unusual RNA velocity, and show that late-stage cells acquire explosive heterogeneity through alternative splicing. An Hsp90aa1-high subpopulation conserved between human and mouse AML associates with poor prognosis, and exon skipping in Tmem134 produces isoforms with opposite effects - the skipped product promotes the cell cycle while the full-length form delays tumorigenesis.

### Szewczyk (2022). *Redox Biology.* PRMT5 regulates ATF4 transcript splicing and oxidative stress response
[doi:10.1016/j.redox.2022.102282](https://doi.org/10.1016/j.redox.2022.102282) · `paper`  
[src](<../raw/Szewczyk(2022) Redox Biology; PRMT5 regulates ATF4 transcript splicing and oxidative stress response.pdf>)

Transcriptomic analysis identified PRMT5 regulation of the ATF4 pathway in AML. PRMT5 inhibition produces an unstable, intron-retaining ATF4 mRNA detained in the nucleus; the accompanying loss of the spliced cytoplasmic transcript lowers ATF4 protein and downregulates its target genes. Cells with low ATF4 after PRMT5 loss show increased oxidative stress, growth arrest and senescence. Leukemia cells overexpressing the EVI1 oncogene depend on PRMT5 function: EVI1-high AML has reduced ATF4, elevated baseline reactive oxygen species and increased sensitivity to PRMT5 inhibition, with EVI1 and ATF4 gene signatures inversely correlated.

### Jin (2020). *Neoplasia.* Prognostic alternative mRNA splicing signatures and associated splicing factors in acute myeloid leukemia
[doi:10.1016/j.neo.2020.06.004](https://doi.org/10.1016/j.neo.2020.06.004) · `paper`  
[src](<../raw/Jin(2020) Neoplasia; Prognostic alternative mRNA splicing signatures and associated splicing factors in acute myeloid leukemia.pdf>)

Using three AML patient datasets, the authors define the landscape of alternative splicing events and identify 7033 associated with survival, from which they build a 15-event prognostic signature that is independent of cytogenetic risk and age and outperforms known gene expression signatures. The signature markedly improves European LeukemiaNet risk classification. A splicing-regulatory network correlates prognostic splicing events with splicing factors, and CRISPR data support the finding that increased RBM39 expression drives higher SETD5 exon inclusion and confers poor outcome.

### Radzisheuskaya (2019). *Nature Structural & Molecular Biology.* PRMT5 methylome profiling uncovers a direct link to splicing regulation in acute myeloid leukemia
[doi:10.1038/s41594-019-0313-z](https://doi.org/10.1038/s41594-019-0313-z) · `paper`  
[src](<../raw/Radzisheuskaya(2019) Nature Structural & Molecular Biology; PRMT5 methylome profiling uncovers a direct link to splicing regulation in acute myeloid leukemia.pdf>)

Using an enzymatically dead PRMT5 and a PRMT5-specific inhibitor, the authors show that PRMT5's catalytic activity is required for AML cell survival. Multiplexed quantitative proteomics identified PRMT5 substrates, and among those essential for AML proliferation, the splicing regulator SRSF1 was confirmed as a direct target whose function depends on PRMT5 methylation of three arginines. Loss of PRMT5 changes alternative splicing of multiple essential genes and alters SRSF1 binding to mRNAs and proteins, which explains the requirement for PRMT5 in leukemia cell survival and provides potential biomarkers of response to PRMT5 inhibitors.

### Wang (2019). *Cancer Cell.* Targeting an RNA-Binding Protein Network in Acute Myeloid Leukemia
[doi:10.1016/j.ccell.2019.01.010](https://doi.org/10.1016/j.ccell.2019.01.010) · `paper`  
[src](<../raw/Wang(2019) Cancer Cell; Targeting an RNA-Binding Protein Network in Acute Myeloid Leukemia.pdf>)

A CRISPR/Cas9 domain-focused screen targeting the RNA-binding domains of 490 classical RNA-binding proteins across human cancers uncovered a network of physically interacting RBPs upregulated in AML relative to normal CD34+ cells and required for RNA splicing and AML survival. Genetic or pharmacologic targeting of one member, RBM39, repressed cassette exon inclusion and promoted intron retention in mRNAs encoding HOXA9 targets and other AML-preferential RBPs. The splicing effects of RBM39 loss produced preferential lethality in spliceosomal-mutant AML, offering a strategy for AML bearing splicing factor mutations.

### Tzelepis (2018). *Nature Communications.* SRPK1 maintains acute myeloid leukemia through effects on isoform usage of epigenetic regulators including BRD4
[doi:10.1038/s41467-018-07620-0](https://doi.org/10.1038/s41467-018-07620-0) · `paper`  
[src](<../raw/Tzelepis(2018) Nature Communications; SRPK1 maintains acute myeloid leukemia through effects on isoform usage of epigenetic regulators including BRD4.pdf>)

Following identification of the splicing kinase SRPK1 as a genetic vulnerability of AML, genetic or pharmacological inhibition is shown to cause cell cycle arrest, differentiation and prolonged survival of mice transplanted with MLL-rearranged AML. RNA-seq shows altered isoform levels of many genes with roles in leukemogenesis including MYB, BRD4 and MED24. SRPK1 inhibition produces a switch from the short to the long BRD4 isoform at mRNA and protein level, associated with BRD4 eviction from loci including BCL2 and MYC, and this switch mediates at least part of the anti-leukemic effect. The inhibitor SPHINX31 was synergistic with the BET inhibitor i-BET-151 without noticeable toxicity in mice.

### Vu (2017). *Nature Genetics.* Functional screen of MSI2 interactors identifies an essential role for SYNCRIP in myeloid leukemia stem cells
[doi:10.1038/ng.3854](https://doi.org/10.1038/ng.3854) · `paper`  
[src](<../raw/Vu(2017) Nature Genetics; Functional screen of MSI2 interactors identifies an essential role for SYNCRIP in myeloid leukemia stem cells.pdf>)

Proteomic analysis of the MSI2-interacting RNA-binding protein network combined with functional shRNA screening identified 24 genes required for in vivo leukemia, with Syncrip the most differentially required between normal and myeloid leukemia cells. SYNCRIP depletion increased apoptosis and differentiation while delaying leukemogenesis, and expression profiling showed loss of the MLL and HOXA9 leukemia stem cell programme. SYNCRIP and MSI2 interact indirectly through shared mRNA targets; SYNCRIP maintains HOXA9 translation, and overexpressing MSI2 or HOXA9 rescues the effects of SYNCRIP depletion.

## m6A and the epitranscriptome

*8 papers.* Writers, erasers and readers of the most abundant internal mRNA modification, all of which turn out to matter in AML. The direction is not conserved across tissues, which is a caution as much as a finding.

### Fu (2025). *Molecular Cancer.* The METTL3-YTHDC1 axis mediates architectural RNA m6A modification to modulate the integrity of chromatin TADs in MLLr + AML genome
[doi:10.1186/s12943-025-02545-x](https://doi.org/10.1186/s12943-025-02545-x) · `paper`  
[src](<../raw/Fu(2025) Molecular Cancer; The METTL3-YTHDC1 axis mediates architectural RNA m6A modification to modulate the integrity of chromatin TADs in MLLr + AML genome.pdf>)

A multi-omics study (RNA-seq, IP-MS, DRIP-seq, ChIP-seq for METTL3, CTCF, H3K4me3 and H3K27ac, RIP-seq, m6A-seq and Hi-C) showing that METTL3 is transcriptionally activated by MLL in MLL-rearranged AML and forms a complex with YTHDC1 and CTCF at promoters and enhancers. METTL3 depletion disrupts CTCF binding sites and reduces chromatin accessibility at leukemic genes including MYB and RUNX1, and YTHDC1 loss compromises CTCF-dependent 3D genome organisation. Mechanistically, YTHDC1 recognises m6A-modified architectural RNAs such as MALAT1, enhancing R-loop formation and sustaining CTCF-mediated TAD activity.

### Pauli (2025). *Blood.* Disrupting tRNA modifications to target mitochondrial vulnerabilities in drug-resistant leukemia cells
[doi:10.1182/blood.2024027822](https://doi.org/10.1182/blood.2024027822) · `paper`  
[src](<../raw/Pauli(2025) Blood; Disrupting tRNA modifications to target mitochondrial vulnerabilities in drug-resistant leukemia cells.pdf>)

CRISPR-based synthetic lethality screens exploring RNA modifications in resistance to antileukemic drugs identify TRMT5-mediated formation of N1-methylguanosine at position 37 of the tRNA anticodon loop as essential for tolerance to cytarabine and venetoclax in AML. TRMT5 methylates nearly all mitochondrial and nuclear tRNAs with a guanosine at position 37, but its role in drug tolerance depends specifically on its mitochondrial function: it is required for the dynamic upregulation of mitochondrial mRNA translation and oxidative phosphorylation that sustains tolerance. Lower expression of electron transport chain components correlates with therapy outcomes in patients, and TRMT5 inhibition prevents the OXPHOS upregulation and synergises with cytarabine and venetoclax.

### Han (2023). *Cell Stem Cell.* METTL16 drives leukemogenesis and leukemia stem cell self-renewal by reprogramming BCAA metabolism
[doi:10.1016/j.stem.2022.12.006](https://doi.org/10.1016/j.stem.2022.12.006) · `paper`  
[src](<../raw/Han(2023) Cell Stem Cell; METTL16 drives leukemogenesis and leukemia stem cell self-renewal by reprogramming BCAA metabolism.pdf>)

CRISPR-Cas9 screening and validation identify METTL16, an m6A methyltransferase, as highly essential for AML cell survival, aberrantly overexpressed in human AML and especially in leukemia stem and initiating cells. Genetic depletion suppresses AML initiation, development and maintenance and attenuates LSC/LIC self-renewal while only moderately affecting normal hematopoiesis in mice. Mechanistically METTL16 promotes expression of the branched-chain amino acid transaminases BCAT1 and BCAT2 in an m6A-dependent manner, reprogramming BCAA metabolism.

### Weng (2022). *Cancer Cell.* The m6A reader IGF2BP2 regulates glutamine metabolism and represents a therapeutic target in acute myeloid leukemia
[doi:10.1016/j.ccell.2022.10.004](https://doi.org/10.1016/j.ccell.2022.10.004) · `paper`  
[src](<../raw/Weng(2022) Cancer Cell; The m6A reader IGF2BP2 regulates glutamine metabolism and represents a therapeutic target in acute myeloid leukemia.pdf>)

IGF2BP2, an m6A binding protein that enhances mRNA stability and translation, is shown to be highly expressed in AML and associated with unfavourable prognosis. It promotes AML development and self-renewal of leukemia stem and initiating cells by regulating MYC, GPT2 and SLC1A5 in the glutamine metabolism pathway in an m6A-dependent manner, fuelling the TCA cycle and maintaining mitochondrial activity. A small-molecule compound, CWI1-2, that directly binds IGF2BP2 and suppresses its m6A reader activity showed anti-leukemia effects in vitro and in vivo with minimal side effects.

### Qing (2021). *Molecular Cell.* R-2-hydroxyglutarate attenuates aerobic glycolysis in leukemia by targeting the FTO/m6A/PFKP/LDHB axis
[doi:10.1016/j.molcel.2020.12.026](https://doi.org/10.1016/j.molcel.2020.12.026) · `paper`  
[src](<../raw/Qing(2021) Molecular Cell; R-2-hydroxyglutarate attenuates aerobic glycolysis in leukemia by targeting the FTO m6A PFKP LDHB axis.pdf>)

R-2-hydroxyglutarate, the metabolite produced by mutant IDH enzymes, is shown to attenuate aerobic glycolysis in sensitive leukemia cells. Mechanistically it abrogates FTO/m6A/YTHDF2-mediated post-transcriptional upregulation of the glycolytic genes PFKP and LDHB. Knocking down FTO, PFKP or LDHB reproduces the glycolytic inhibition in sensitive leukemia cells but not in normal CD34+ hematopoietic stem/progenitor cells, and inhibits leukemogenesis in vivo; overexpression reverses the effect. R-2HG also suppresses glycolysis and downregulates FTO, PFKP and LDHB in human primary IDH-wild-type AML cells.

### Barbieri (2017). *Nature.* Promoter-bound METTL3 maintains myeloid leukaemia by m6A-dependent translation control
[doi:10.1038/nature24678](https://doi.org/10.1038/nature24678) · `paper`  
[src](<../raw/Barbieri(2017) Nature; Promoter-bound METTL3 maintains myeloid leukaemia by m6A-dependent translation control.pdf>)

Two independent CRISPR screens - a genome-wide dropout screen in MLL-AF9/FLT3-ITD mouse primary leukemia cells and a custom domain-focused library - identify METTL3 as essential for AML growth. Knockdown causes cell cycle arrest, differentiation and failure to establish leukemia in immunodeficient mice. METTL3 associates with chromatin independently of METTL14 and localises to transcriptional start sites of active genes, the majority of which carry CEBPZ at the TSS, which is required for its recruitment. Promoter-bound METTL3 induces m6A within the coding region of the associated transcript and enhances translation by relieving ribosome stalling.

### Li (2017). *Cancer Cell.* FTO Plays an Oncogenic Role in Acute Myeloid Leukemia as a N 6 -Methyladenosine RNA Demethylase
[doi:10.1016/j.ccell.2016.11.017](https://doi.org/10.1016/j.ccell.2016.11.017) · `paper`  
[src](<../raw/Li(2017) Cancer Cell; FTO Plays an Oncogenic Role in Acute Myeloid Leukemia as a N 6 -Methyladenosine RNA Demethylase.pdf>)

FTO, the first identified m6A RNA demethylase, is shown to have a critical oncogenic role in AML. It is highly expressed in AML with MLL rearrangement, PML-RARA, FLT3-ITD and/or NPM1 mutations, enhances leukemic oncogene-mediated transformation and leukemogenesis, and inhibits all-trans-retinoic acid-induced differentiation, by reducing m6A levels on target transcripts including ASB2 and RARA and thereby lowering their expression.

### Vu (2017). *Nature Medicine.* The N6-methyladenosine (m6A)-forming enzyme METTL3 controls myeloid differentiation of normal hematopoietic and leukemia cells
[doi:10.1038/nm.4416](https://doi.org/10.1038/nm.4416) · `paper`  
[src](<../raw/Vu(2017) Nature Medicine; The N6-methyladenosine (m6A)-forming enzyme METTL3 controls myeloid differentiation of normal hematopoietic and leukemia cells.pdf>)

shRNA depletion of METTL3 in human hematopoietic stem/progenitor cells promotes differentiation with reduced proliferation, while overexpressing wild-type but not catalytically inactive METTL3 inhibits differentiation and increases growth. METTL3 is more abundant in AML cells than in healthy HSPCs or other tumour types; its depletion in myeloid leukemia lines induces differentiation and apoptosis and delays leukemia progression in mice. Single-nucleotide-resolution m6A mapping with ribosome profiling shows m6A promotes translation of c-MYC, BCL2 and PTEN mRNAs, and loss of METTL3 raises phosphorylated AKT, contributing to the differentiation effect.

## Long-read transcriptomics, circular and chimeric RNAs

*8 papers.* What short reads cannot see. Every increase in sequencing depth reveals more transcripts, which is either evidence of untapped complexity or of an error rate - and the papers here disagree about which.

### Miller (2026). *venue not recorded.* Long-read cDNA sequencing reveals novel isoforms and spliceosome-mutant-enriched transcripts in AML and MDS
[doi:10.64898/2026.05.20.726635](https://doi.org/10.64898/2026.05.20.726635) · `preprint`  
[src](<../raw/Miller(2026) unknown; Long-read cDNA sequencing reveals novel isoforms and spliceosome-mutant-enriched transcripts in AML and MDS.pdf>)

Using the Oxford Nanopore cDNA platform, the authors generated nearly 2 billion long reads (median 25.8 million per sample) from 71 human samples: 48 AML or MDS samples, 25 with SRSF2, U2AF1 or SF3B1 mutations, plus 23 sorted hematopoietic populations from healthy individuals. They identified 174,162 novel isoforms absent from the reference transcriptome alongside 206,601 known Ensembl isoforms, with proteomic validation confirming that many are translated - 307 high-confidence novel peptides. Isoforms enriched in spliceosome-mutant samples were identified, along with proteomic evidence of frequent nonsense-mediated decay regulation of novel transcripts. An interactive portal is provided.

### Ma (2025). *Oncogene.* Super-enhancer-associated long noncoding RNA lnc-SPI1U mediates SPI1 feedback regulation by interacting with HNRNPH1 and HNRNPF
[doi:10.1038/s41388-025-03612-9](https://doi.org/10.1038/s41388-025-03612-9) · `paper`  
[src](<../raw/Ma(2025) Oncogene; Super-enhancer-associated long noncoding RNA lnc-SPI1U mediates SPI1 feedback regulation by interacting with HNRNPH1 and HNRNPF.pdf>)

Profiling APL-specific super-enhancer-associated lncRNAs from H3K27ac ChIP-seq and RNA-seq in TCGA and Beat AML identified 44 candidates, from which the authors characterise RP11-750H9.5 - lnc-SPI1U - transcribed from the super-enhancer upstream of SPI1, which encodes PU.1. lnc-SPI1U suppressed differentiation and apoptosis and blunted ATRA-induced growth inhibition, opposite to SPI1's role, by interacting with HNRNPH1/F to destabilise SPI1 mRNA. Its induction during myeloid differentiation is PU.1-dependent, forming a feedback loop that tunes SPI1 to an optimal level, and in APL the PML/RARalpha fusion blocks PU.1-dependent transactivation of lnc-SPI1U by hijacking the overlapping super-enhancer region.

### Shi (2025). *Cell Reports.* Transcript isoform diversity defines molecular subtypes and prognosis in acute myeloid leukemia through long-read sequencing
[doi:10.1016/j.celrep.2025.116216](https://doi.org/10.1016/j.celrep.2025.116216) · `paper`  
[src](<../raw/Shi(2025) Cell Reports; Transcript isoform diversity defines molecular subtypes and prognosis in acute myeloid leukemia through long-read sequencing.pdf>)

Long-read Oxford Nanopore transcriptome sequencing of 60 primary AML bone marrow samples gives isoform-level resolution of splicing abnormalities, detecting extensive AML-specific anomalies and 119,278 previously unannotated transcript isoforms, of which 80,294 (67.31%) contain complete open reading frames and 9,812 (12.22%) were validated by mass spectrometry. Quantifying these across 175 RNA-seq samples and clustering by non-negative matrix factorisation defines isoform-based molecular subtypes that correlate with prognosis, and a 10-transcript prognostic model predicts outcome within the internal cohort.

### Zhou (2025). *Data in Brief.* Iso-seq and RNA-seq data from ML-2 acute myeloid leukemia cells overexpressing the ZCCHC10 gene
[doi:10.1016/j.dib.2025.112048](https://doi.org/10.1016/j.dib.2025.112048) · `paper`  
[src](<../raw/Zhou(2025) Data in Brief; Iso-seq and RNA-seq data from ML-2 acute myeloid leukemia cells overexpressing the ZCCHC10 gene.pdf>)

A data article describing PacBio single-molecule long-read isoform sequencing and Illumina short-read RNA sequencing of ML-2 AML cells stably overexpressing ZCCHC10, a zinc finger CCHC-type protein reported to act as a tumour suppressor in AML, against cells overexpressing an empty vector. The Iso-seq data provide full-length transcripts allowing identification of mRNA isoforms and of alternative transcription initiation, alternative splicing and alternative polyadenylation; the RNA-seq data provide transcript profiles showing the effects of ZCCHC10 overexpression on gene expression. Both datasets are deposited in the SRA.

### Rufflé (2024). *NAR Genomics and Bioinformatics.* Effective requesting method to detect fusion transcripts in chronic myelomonocytic leukemia RNA-seq
[doi:10.1093/nargab/lqae117](https://doi.org/10.1093/nargab/lqae117) · `paper`  
[src](<../raw/Rufflé(2024) NAR Genomics and Bioinformatics; Effective requesting method to detect fusion transcripts in chronic myelomonocytic leukemia RNA-seq.pdf>)

An integrated k-mer approach querying indexed RNA-seq datasets, combining short- and long-read analysis, is used to detect chimeric RNAs in chronic myelomonocytic leukemia. Applying CRAC tools with basic filters identified 1787 chimeric RNAs in four classes, from which four were selected and validated in CMML cells. The authors focus on NRIP1-MIR99AHG, also recently detected in AML, showing it encodes three isoforms including a novel one. Stringency is placed on tissue specificity of expression rather than on initial filters, using chimeric k-mer counts compared quantitatively across indexed datasets via the transipedia interface.

### Sun (2024). *Cancer Letters.* circRNAs as prognostic markers in pediatric acute myeloid leukemia
[doi:10.1016/j.canlet.2024.216880](https://doi.org/10.1016/j.canlet.2024.216880) · `paper`  
[src](<../raw/Sun(2024) Cancer Letters; circRNAs as prognostic markers in pediatric acute myeloid leukemia.pdf>)

A genome-wide analysis of circular RNAs from RNA-seq data in pediatric AML identified a group associated with inferior outcomes and acting on cancer-related pathways, several transcribed from genes with established AML functions including circRUNX1, circWHSC1 and circFLT3. An increased number of circRNAs and of linear RNA splicing events correlated significantly with worse clinical outcome, implicating splicing dysregulation. Upregulated RNA binding proteins were identified in AMLs with high circRNA numbers, with TROVE2 prominent; TROVE2 binds flanking intron Alu sequences and participates in circRNA processing, and linear TROVE2 expression associated with prognosis, validated in the pediatric TARGET and adult BeatAML2 cohorts.

### Yeh (2023). *International Journal of Molecular Sciences.* Circular RNAs and Untranslated Regions in Acute Myeloid Leukemia
[doi:10.3390/ijms24043215](https://doi.org/10.3390/ijms24043215) · `paper`  
[src](<../raw/Yeh(2023) International Journal of Molecular Sciences; Circular RNAs and Untranslated Regions in Acute Myeloid Leukemia.pdf>)

A review of circular RNAs and non-coding untranslated regions in AML, prompted by the finding that approximately 97.5% of the human genome is transcribed into non-coding RNA. It discusses the cellular mechanisms of circRNAs, summarises studies of their biological roles in AML, reviews the contribution of 3' untranslated regions to disease progression through alternative polyadenylation, 3'UTR splicing and single nucleotide polymorphisms, and considers the potential of both as biomarkers for stratification and treatment response prediction and as targets for RNA-directed therapeutics.

### Rufflé (2017). *F1000Research.* New chimeric RNAs in acute myeloid leukemia
[doi:10.12688/f1000research.11352.1](https://doi.org/10.12688/f1000research.11352.1) · `paper`  
[src](<../raw/Rufflé(2017) F1000Research; New chimeric RNAs in acute myeloid leukemia.pdf>)

Using Crac, a tool that infers splice and chimeric junctions within a single read from genomic locations and local coverage, with CracTools to aggregate, annotate and filter, the authors detect chimeric RNAs in AML RNA-seq irrespective of annotation. Seventeen chimeric RNAs were identified and validated by real-time PCR and sequencing across three AML patients: ten from a t(15;17) patient, four from a normal-karyotype patient and three from an inv(16) patient. The new fusion transcripts fall into four groups by exon organisation, suggesting distinct synthesis mechanisms, and tumour-specific expression was checked against a public dataset using a tag search approach.


# D. Metabolism, mitochondria and cell death

## Oxidative metabolism and chemoresistance

*10 papers.* The finding that reorganised the field: cells surviving chemotherapy are not quiescent stem cells but metabolically distinct ones. Almost everything else in this part descends from it.

### Cuminetti (2026). *Nature Communications.* Succinate receptor 1 restricts hematopoiesis and prevents acute myeloid leukemia progression
[doi:10.1038/s41467-026-68906-2](https://doi.org/10.1038/s41467-026-68906-2) · `paper`  
[src](<../raw/Cuminetti(2026) Nature Communications; Succinate receptor 1 restricts hematopoiesis and prevents acute myeloid leukemia progression.pdf>)

Low SUCNR1 expression is shown to mark reduced overall and progression-free survival in AML. Succinic acid, acting through both Sucnr1-dependent and independent routes, promotes disease in mouse models of pre-leukemic myelopoiesis, AML and AML xenografts expressing low SUCNR1. Global or hematopoietic deletion of Sucnr1 expands hematopoietic stem and progenitor cells, while Sucnr1-tomato+ HSPCs show restricted engraftment. Mechanistically Sucnr1 activation counterbalances intracellular succinate in HSPCs and preserves their transcriptional programs by controlling S100a8/S100a9; blocking S100a9 with tasquinimod rescues Sucnr1 knockout defects, and combined with a Sucnr1 agonist shows therapeutic value in AML mice.

### Nah (2025). *Molecular Cell.* Microprotein SMIM26 drives oxidative metabolism via serine-responsive mitochondrial translation
[doi:10.1016/j.molcel.2025.05.033](https://doi.org/10.1016/j.molcel.2025.05.033) · `paper`  
[src](<../raw/Nah(2025) Molecular Cell; Microprotein SMIM26 drives oxidative metabolism via serine-responsive mitochondrial translation.pdf>)

A genome-wide CRISPR screen targeting small ORF-encoded microproteins found that deleting the LINC00493-encoded microprotein SMIM26 sensitises cells to one-carbon restriction. SMIM26 interacts with the mitochondrial serine transporters SFXN1/2 and the mitoribosome, forming a triad that facilitates translation of the complex I subunit mt-ND5. Its loss impairs serine import, reduces folate intermediates and disrupts mitochondrial tRNA modifications, causing ND5 translation failure and complex I deficiency. SMIM26 deletion is embryonic lethal in mice and impedes tumour growth in a xenograft model of folate-dependent AML.

### Park (2025). *Journal of Experimental & Clinical Cancer Research.* Tetrahydrobenzimidazole TMQ0153 targets OPA1 and restores drug sensitivity in AML via ROS-induced mitochondrial metabolic reprogramming
[doi:10.1186/s13046-025-03372-0](https://doi.org/10.1186/s13046-025-03372-0) · `paper`  
[src](<../raw/Park(2025) Journal of Experimental & Clinical Cancer Research; Tetrahydrobenzimidazole TMQ0153 targets OPA1 and restores drug sensitivity in AML via ROS-induced mitochondrial metabolic reprogramming.pdf>)

OPA1, the mitochondrial fusion protein, is upregulated in AML with adverse mutations and correlates with poor prognosis. The tetrahydrobenzimidazole derivative TMQ0153 reduced OPA1 and mitofusin-2 levels and disrupted mitochondrial morphology and function, increasing reactive oxygen species, inhibiting oxidative phosphorylation, depolarising the membrane potential and inducing caspase-dependent apoptosis. Metabolic profiling showed a shift from mitochondrial respiration to glycolysis with impaired respiratory chain activity and altered GSH/GSSG and NAD+/NADH ratios. TMQ0153 reduced tumour volume and weight in MV4-11 xenografts, and combinations with other AML drugs reduced leukemic burden and prolonged survival in NSG mice xenografted with U937 and MOLM-14 cells.

### Sharma (2025). *Nature.* Taurine from tumour niche drives glycolysis to promote leukaemogenesis
[doi:10.1038/s41586-025-09018-7](https://doi.org/10.1038/s41586-025-09018-7) · `paper`  
[src](<../raw/Sharma(2025) Nature; Taurine from tumour niche drives glycolysis to promote leukaemogenesis.pdf>)

Temporal single-cell RNA sequencing identifies molecular cues from the bone marrow stromal niche that engage leukemia stem-enriched cells during oncogenic progression; integrating these with human LSC RNA-seq and an in vivo CRISPR screen of LSC dependencies identifies the taurine-taurine transporter (TAUT) axis as a critical dependency of aggressive myeloid leukemias. CDO1-driven taurine biosynthesis is restricted to osteolineage cells and increases with disease progression; blocking CDO1 in those cells impairs LSC growth and improves survival. TAUT loss-of-function models and patient-derived AML cells show that TAUT inhibition impairs leukemia progression in vivo, synergises with venetoclax, and acts by blocking RAG-GTP-dependent mTOR activation and downstream glycolysis.

### Stewart (2025). *Nature Metabolism.* Pathway coessentiality mapping reveals complex II is required for de novo purine biosynthesis in acute myeloid leukaemia
[doi:10.1038/s42255-025-01410-x](https://doi.org/10.1038/s42255-025-01410-x) · `paper`  
[src](<../raw/Stewart(2025) Nature Metabolism; Pathway coessentiality mapping reveals complex II is required for de novo purine biosynthesis in acute myeloid leukaemia.pdf>)

A multi-gene pathway coessentiality mapping approach, developed to move beyond gene-gene interaction analysis, reveals that AML depends on a link between electron transport chain complex II and purine metabolism. Stable-isotope metabolomic tracing shows complex II directly supports de novo purine biosynthesis, and exogenous purines rescue AML cells from complex II inhibition. The circuit is that glutamine provides nitrogen for the purine ring, producing glutamate that complex II metabolises to sustain purine synthesis; raising intracellular glutamate suppresses purine production and sensitises cells to complex II inhibition. Targeting complex II caused rapid disease regression and extended survival in a syngeneic AML model, and higher complex II gene expression correlates with BCL-2 inhibitor resistance and worse survival in patients.

### Boët (2024). *Cancer Research.* Targeting Metabolic Dependencies Fueling the TCA Cycle to Circumvent Therapy Resistance in Acute Myeloid Leukemia
[doi:10.1158/0008-5472.CAN-24-0019](https://doi.org/10.1158/0008-5472.CAN-24-0019) · `paper`  
[src](<../raw/Boët(2024) Cancer Research; Targeting Metabolic Dependencies Fueling the TCA Cycle to Circumvent Therapy Resistance in Acute Myeloid Leukemia.pdf>)

A commentary in Cancer Research on two studies of AML dependence on respiratory substrates that feed oxidative phosphorylation: alpha-ketoglutarate and lactate-derived pyruvate. It frames the problem as relapse-initiating cells surviving through nongenetic, metabolic adaptation - leukemic stem cells relying on mitochondrial metabolism where hematopoietic stem cells rely on glycolysis, with cytarabine-persisting cells further enriched for mitochondrial dependence. Interfering with lactate utilisation through MCT1/SLC16A1 or lactate dehydrogenase sensitised cells to the BET inhibitor INCB054329 in vitro and in vivo, while the imipridone ONC-213 acted on alpha-KGDH to induce an ATF4-mediated mitochondrial stress response that lowered MCL1 and promoted apoptosis.

### Larrue (2023). *venue not recorded.* Ferritinophagy is a Druggable Vulnerability of Quiescent Leukemic Stem Cells
[doi:10.1101/2023.12.18.572101](https://doi.org/10.1101/2023.12.18.572101) · `preprint`  
[src](<../raw/Larrue(2023) unknown; Ferritinophagy is a Druggable Vulnerability of Quiescent Leukemic Stem Cells.pdf>)

Investigating quiescence in AML using patient-derived xenografts and primary patient cells, the authors find that the LSC-enriched quiescent population carries a distinct gene set of prognostic significance and shows heightened autophagic activity with a specific reliance on ferritinophagy - the selective autophagy of ferritin mediated by NCOA4, which controls iron bioavailability. Inhibiting NCOA4 genetically or chemically had potent antileukemic effects, particularly against the LSC compartment.

### Bosc (2021). *Nature Cancer.* Mitochondrial inhibitors circumvent adaptive resistance to venetoclax and cytarabine combination therapy in acute myeloid leukemia
[doi:10.1038/s43018-021-00264-y](https://doi.org/10.1038/s43018-021-00264-y) · `paper`  
[src](<../raw/Bosc(2021) Nature Cancer; Mitochondrial inhibitors circumvent adaptive resistance to venetoclax and cytarabine combination therapy in acute myeloid leukemia.pdf>)

The authors define a 'MitoScore' signature identifying high mitochondrial oxidative phosphorylation in vivo and in patients with AML. Primary AML cells resistant to cytarabine with a high MitoScore depend on mitochondrial BCL2 and are highly sensitive to venetoclax plus cytarabine but not venetoclax plus azacitidine. Single-cell transcriptomics of cells surviving venetoclax + cytarabine shows adaptive resistance involving oxidative phosphorylation, electron transport chain complexes and the TP53 pathway; treating those resistant cells with ETC complex inhibitors, pyruvate dehydrogenase inhibitors or mitochondrial ClpP protease agonists substantially delays relapse.

### Aroua (2020). *Cancer Discovery.* Extracellular ATP and CD39 Activate cAMP-Mediated Mitochondrial Stress Response to Promote Cytarabine Resistance in Acute Myeloid Leukemia
[doi:10.1158/2159-8290.CD-19-1008](https://doi.org/10.1158/2159-8290.CD-19-1008) · `paper`  
[src](<../raw/Aroua(2020) Cancer Discovery; Extracellular ATP and CD39 Activate cAMP-Mediated Mitochondrial Stress Response to Promote Cytarabine Resistance in Acute Myeloid Leukemia.pdf>)

The ectonucleotidase CD39 (ENTPD1) is shown to be upregulated in cytarabine-resistant leukemic cells in AML cell lines and patient samples, both in vitro and in vivo. CD39 surface expression and activity rise in patients after chemotherapy compared with diagnosis, and enrichment for CD39-expressing blasts marks adverse prognosis. High CD39 activity promotes cytarabine resistance by driving mitochondrial activity and biogenesis through a cAMP-mediated adaptive mitochondrial stress response, via a P2RY13-cAMP-PKA and ATF4 axis; genetic and pharmacologic inhibition of CD39 ecto-ATPase activity blocks that reprogramming and markedly increases cytarabine cytotoxicity in vitro and in xenografts.

### Farge (2017). *Cancer Discovery.* Chemotherapy-Resistant Human Acute Myeloid Leukemia Cells Are Not Enriched for Leukemic Stem Cells but Require Oxidative Metabolism
[doi:10.1158/2159-8290.CD-16-0441](https://doi.org/10.1158/2159-8290.CD-16-0441) · `paper`  
[src](<../raw/Farge(2017) Cancer Discovery; Chemotherapy-Resistant Human Acute Myeloid Leukemia Cells Are Not Enriched for Leukemic Stem Cells but Require Oxidative Metabolism.pdf>)

Using a clinically relevant, well-tolerated cytarabine regimen in patient-derived xenografts, the authors show that residual AML cells after treatment are enriched in neither immature nor quiescent cells nor leukemic stem cells, formally assessed by limiting dilution into secondary recipients. Instead, resistant preexisting and persisting cells show high reactive oxygen species, increased mitochondrial mass and active polarised mitochondria consistent with high oxidative phosphorylation, together with increased fatty-acid oxidation and upregulated CD36, and a high OXPHOS gene signature predictive of treatment response in PDX and patients. High-OXPHOS but not low-OXPHOS cell lines were chemoresistant in vivo, and targeting mitochondrial protein synthesis, electron transfer or fatty-acid oxidation shifted cells to low OXPHOS and enhanced cytarabine's effect.

## BCL2 family dependencies and venetoclax response

*7 papers.* Venetoclax changed AML treatment and is not curative. These papers are about who responds, why the others do not, and whether the standard explanation - monocytic differentiation - survives contact with patient data.

### Lee (2026). *Cell Death & Disease.* OT-55 reshapes tolerogenic BH3-mimetic-induced apoptosis toward immunogenic cell death in acute myeloid leukemia, potentiating PD-1/Tim-3 blockade
[doi:10.1038/s41419-026-09000-9](https://doi.org/10.1038/s41419-026-09000-9) · `paper`  
[src](<../raw/Lee(2026) Cell Death & Disease; OT-55 reshapes tolerogenic BH3-mimetic-induced apoptosis toward immunogenic cell death in acute myeloid leukemia, potentiating PD-1 Tim-3 blockade.pdf>)

BH3 mimetics are apoptogenic but rarely cause immunogenic cell death. The hydroxycoumarin OT-55 was combined with the BCL-xL inhibitor A-1331852 in BCL-xL-dependent murine prophylactic and bilateral AML vaccination models. A nine-gene AML immunogenic-cell-death score (ATG5, CALR, CD8A, CD8B, IFNGR1, IL1B, PDIA3, PIK3CA, TLR4) was derived from three patient cohorts; high scores associated with an immune-activated state, more CD8+ T cells, activated dendritic cells and higher Tim-3 expression. OT-55 reduced C1498 viability, induced calreticulin exposure and ATP release, and conferred calreticulin/ATP-dependent but HMGB1-independent vaccine protection; combined with A-1331852 it enhanced DAMP release and CD8+ effector function, and with PD-1/Tim-3 blockade achieved local and distant tumour control.

### Cerella (2023). *Leukemia.* ATP1A1/BCL2L1 predicts the response of myelomonocytic and monocytic acute myeloid leukemia to cardiac glycosides
[doi:10.1038/s41375-023-02076-8](https://doi.org/10.1038/s41375-023-02076-8) · `paper`  
[src](<../raw/Cerella(2023) Leukemia; ATP1A1 BCL2L1 predicts the response of myelomonocytic and monocytic acute myeloid leukemia to cardiac glycosides.pdf>)

Myelomonocytic and monocytic AML are intrinsically resistant to venetoclax-based regimens. The authors report that ex vivo response of AML patient blasts and in vitro sensitivity of cell lines to the hemi-synthetic cardiac glycoside UNBS1450 correlates with the ATP1A1/BCL2L1 expression ratio. Public AML datasets identify myelomonocytic/monocytic differentiation as the most robust prognostic feature for this response, alongside CBFB and KMT2A rearrangements and missense FLT3 mutations. Mechanistically BCL2L1 protects against cell death from the glycoside's stepwise ionic perturbation, protein synthesis inhibition and MCL1 downregulation; in vivo the compounds were tolerable and produced tumour growth inhibition to regression.

### Kuusanmäki (2023). *Blood.* Erythroid/megakaryocytic differentiation confers BCL-XL dependency and venetoclax resistance in acute myeloid leukemia
[doi:10.1182/blood.2021011094](https://doi.org/10.1182/blood.2021011094) · `paper`  
[src](<../raw/Kuusanmäki(2023) Blood; Erythroid megakaryocytic differentiation confers BCL-XL dependency and venetoclax resistance in acute myeloid leukemia.pdf>)

Using combined ex vivo drug sensitivity testing, genetic perturbation and transcriptomic profiling, AML with erythroid or megakaryocytic differentiation is shown to depend on BCL-XL rather than BCL-2. High-throughput screening of more than 500 compounds identified the BCL-XL-selective inhibitor A-1331852 and navitoclax as highly effective against erythroid/megakaryoblastic leukemia cell lines, while these subtypes were resistant to venetoclax. Genome-scale CRISPR-Cas9 and RNAi screening data confirmed essentiality of BCL2L1 but not BCL2 or MCL1, and A-1331852 reduced tumour burden in a xenograft model, though cells persisted in some animals and regrew after drug withdrawal.

### Waclawiczek (2023). *Cancer Discovery.* Combinatorial BCL2 Family Expression in Acute Myeloid Leukemia Stem Cells Predicts Clinical Response to Azacitidine/Venetoclax
[doi:10.1158/2159-8290.CD-22-0939](https://doi.org/10.1158/2159-8290.CD-22-0939) · `paper`  
[src](<../raw/Waclawiczek(2023) Cancer Discovery; Combinatorial BCL2 Family Expression in Acute Myeloid Leukemia Stem Cells Predicts Clinical Response to Azacitidine Venetoclax.pdf>)

Integrating transcriptomic, proteomic, functional and clinical data to find predictors of azacitidine/venetoclax response, the authors found that although cultured monocytic AML cells showed upfront resistance, monocytic differentiation was not clinically predictive in their patient cohort. Leukemic stem cells were the primary targets whose elimination determined outcome, and LSCs of refractory patients showed perturbed apoptotic dependencies. A flow cytometry-based Mediators of Apoptosis Combinatorial score (MAC-Score), combining BCL2, BCL-xL and MCL1 protein expression in LSCs, predicted initial response with positive predictive value above 97% and was associated with increased event-free survival, validated across four patient cohorts including salvage therapy.

### Pei (2020). *Cancer Discovery.* Monocytic Subclones Confer Resistance to Venetoclax-Based Therapy in Patients with Acute Myeloid Leukemia
[doi:10.1158/2159-8290.CD-19-0710](https://doi.org/10.1158/2159-8290.CD-19-0710) · `paper`  
[src](<../raw/Pei(2020) Cancer Discovery; Monocytic Subclones Confer Resistance to Venetoclax-Based Therapy in Patients with Acute Myeloid Leukemia.pdf>)

Responses to venetoclax plus azacitidine correlate closely with developmental stage: phenotypically primitive AML is sensitive while monocytic AML is resistant. Resistant monocytic AML has a distinct transcriptomic profile, loses expression of the venetoclax target BCL2, and relies on MCL1 to mediate oxidative phosphorylation and survival. This differential sensitivity drives selection favouring outgrowth of monocytic subpopulations at relapse. The authors conclude that resistance can arise from biological properties intrinsic to monocytic differentiation, and that AML therapies should be designed to target subclones arising at different developmental stages independently.

### Zhang (2020). *Nature Cancer.* Integrated analysis of patient samples identifies biomarkers for venetoclax efficacy and combination strategies in acute myeloid leukemia
[doi:10.1038/s43018-020-0103-x](https://doi.org/10.1038/s43018-020-0103-x) · `paper`  
[src](<../raw/Zhang(2020) Nature Cancer; Integrated analysis of patient samples identifies biomarkers for venetoclax efficacy and combination strategies in acute myeloid leukemia.pdf>)

Integrating clinical characteristics, exome and RNA sequencing, and inhibitor data from primary AML patient samples in the Beat AML cohort, the authors determined that myelomonocytic leukemia, upregulation of BCL2A1 and CLEC7A, and mutations of PTPN11 and KRAS conferred resistance to venetoclax and to multiple venetoclax combinations. Venetoclax combined with the MCL1 inhibitor AZD5991 induced synthetic lethality and circumvented that resistance, shown in cell line models engineered for each resistance factor, in xenografts, and in a KRAS-mutant primary AML model with survival benefit.

### Nechiporuk (2019). *Cancer Discovery.* The TP53 Apoptotic Network Is a Primary Mediator of Resistance to BCL2 Inhibition in AML Cells
[doi:10.1158/2159-8290.CD-19-0125](https://doi.org/10.1158/2159-8290.CD-19-0125) · `paper`  
[src](<../raw/Nechiporuk(2019) Cancer Discovery; The TP53 Apoptotic Network Is a Primary Mediator of Resistance to BCL2 Inhibition in AML Cells.pdf>)

A genome-wide CRISPR/Cas9 screen for gene knockouts conferring venetoclax resistance in AML validated TP53, BAX and PMAIP1. Resistance arose from inability to execute apoptosis after BAX loss, decreased BCL2 expression, and reliance on alternative family members such as BCL2L1, accompanied by changes in mitochondrial homeostasis and cellular metabolism. Screening TP53 knockout cells against a panel of small-molecule inhibitors revealed gained sensitivity to TRK inhibitors, associated with increased NTRK3 and decreased NTRK1 expression. Findings were related to patient drug responses and expression in the Beat AML dataset.

## Lipid, amino acid and cofactor metabolism as vulnerabilities

*6 papers.* Metabolic dependencies beyond the respiratory chain, several of them created by the leukemia's own adaptations. The recurring problem is that the pathway is usually essential in normal cells too.

### Lewis (2026). *Cell.* Inhibition of heme biosynthesis triggers cuproptosis in acute myeloid leukemia
[doi:10.1016/j.cell.2025.10.028](https://doi.org/10.1016/j.cell.2025.10.028) · `paper`  
[src](<../raw/Lewis(2026) Cell; Inhibition of heme biosynthesis triggers cuproptosis in acute myeloid leukemia.pdf>)

Integrating mouse models, human cell lines and primary patient samples, de novo heme biosynthesis is identified as a selective dependency in AML. The dependency arises because AML cells, and especially leukemic stem cells, downregulate heme biosynthesis enzymes, which promotes self-renewal. Inhibiting these enzymes collapses mitochondrial Complex IV and dysregulates the copper-chaperone system, inducing cuproptosis - programmed cell death caused by copper-driven oligomerisation of lipoylated proteins. Pathways synthetic lethal with heme biosynthesis, including glycolysis, are identified for combination strategies.

### Schäfer (2026). *Cell Reports.* ACSL4-associated lipid metabolism is a distinct therapeutic vulnerability in KMT2A-rearranged acute myeloid leukemia
[doi:10.1016/j.celrep.2026.117010](https://doi.org/10.1016/j.celrep.2026.117010) · `paper`  
[src](<../raw/Schäfer(2026) Cell Reports; ACSL4-associated lipid metabolism is a distinct therapeutic vulnerability in KMT2A-rearranged acute myeloid leukemia.pdf>)

Analysis of large-scale CRISPR-Cas9 screening data identified ACSL4 as a selective vulnerability in KMT2A-rearranged AML. CRISPR interference and shRNA knockdown confirmed that ACSL4 loss impairs growth of KMT2A-rearranged but not other AML cells, reduces colony formation in patient-derived and murine MLL-AF9 cells, and delays leukemia onset in MLL-AF9 mice. Multi-omics - transcriptomics, proteomics and lipidomics - showed depletion of polyunsaturated lipid species and compensatory activation of lipid metabolic pathways, and supplementing exogenous polyunsaturated fatty acids rescued the growth defect, linking the dependency to defective PUFA utilisation. A KMT2A-ACSL4 dependency signature (KRADS12) correlates with KMT2A-rearranged status and predicts poor survival.

### Liu (2025). *Scientific Reports.* Lactylation modulation identifies key biomarkers and therapeutic targets in KMT2A-rearranged AML
[doi:10.1038/s41598-025-86136-2](https://doi.org/10.1038/s41598-025-86136-2) · `paper`  
[src](<../raw/Liu(2025) Scientific Reports; Lactylation modulation identifies key biomarkers and therapeutic targets in KMT2A-rearranged AML.pdf>)

A computational study of lactylation-related gene expression in KMT2A-rearranged AML, using microarray data from CN-AML (n = 70) and KMT2Ar-AML (n = 52) cohorts. Twelve lactylation-dependent differentially expressed genes were identified, from which machine learning selected six (PFN1, S100A6, CBR1, LDHB, LGALS1, PRDX1) as prognostically relevant and linked to disease pathways. Unsupervised clustering distinguished two lactylation subtypes with differing pathway enrichment and immune cell infiltration, and the analysis suggested PI3K inhibitors and pevonedistat as candidate agents.

### Skuli (2025). *Leukemia.* Chemoresistance of TP53 mutant acute myeloid leukemia requires the mevalonate byproduct, geranylgeranyl pyrophosphate, for induction of an adaptive stress response
[doi:10.1038/s41375-025-02668-6](https://doi.org/10.1038/s41375-025-02668-6) · `paper`  
[src](<../raw/Skuli(2025) Leukemia; Chemoresistance of TP53 mutant acute myeloid leukemia requires the mevalonate byproduct, geranylgeranyl pyrophosphate, for induction of an adaptive stress response.pdf>)

RNA sequencing of purified AML patient samples showed higher mevalonate pathway gene expression in TP53-mutant disease. Using isogenic TP53-mutant cell lines and primary samples, resistance to cytarabine correlated with increased mevalonate pathway activity, lower induction of reactive oxygen species, and a mitochondrial response with increased mass and oxidative phosphorylation; statin pretreatment reversed these and chemosensitised the cells. The geranylgeranyl pyrophosphate branch was required, with a newly identified role in regulating glutathione for managing cytarabine-induced ROS. However, statins alone were inadequate to fully reverse chemoresistance in vivo and in a retrospective study of 364 TP53-mutant AML patients who received chemotherapy with a concurrent statin.

### Sabatier (2023). *Cancer Discovery.* C/EBPα Confers Dependence to Fatty Acid Anabolic Pathways and Vulnerability to Lipid Oxidative Stress–Induced Ferroptosis in FLT3 -Mutant Leukemia
[doi:10.1158/2159-8290.CD-22-0411](https://doi.org/10.1158/2159-8290.CD-22-0411) · `paper`  
[src](<../raw/Sabatier(2023) Cancer Discovery; C EBPα Confers Dependence to Fatty Acid Anabolic Pathways and Vulnerability to Lipid Oxidative Stress–Induced Ferroptosis in FLT3 -Mutant Leukemia.pdf>)

Multiomics analyses uncover coordinated activation of C/EBPalpha and FLT3 that increases lipid anabolism in vivo and in patients with FLT3-mutant AML. C/EBPalpha regulates the FASN-SCD axis to promote fatty acid biosynthesis and desaturation; inactivating FLT3 or C/EBPalpha decreases monounsaturated fatty acid incorporation into membrane phospholipids through SCD downregulation, with compensatory import and storage of polyunsaturated fatty acids. The resulting susceptibility to lipid redox stress is exploited by combining FLT3 and GPX4 inhibition to trigger ferroptotic death of FLT3-mutant AML cells.

### Yang (2021). *Cancer Discovery.* Transcriptional Silencing of ALDH2 Confers a Dependency on Fanconi Anemia Proteins in Acute Myeloid Leukemia
[doi:10.1158/2159-8290.CD-20-1542](https://doi.org/10.1158/2159-8290.CD-20-1542) · `paper`  
[src](<../raw/Yang(2021) Cancer Discovery; Transcriptional Silencing of ALDH2 Confers a Dependency on Fanconi Anemia Proteins in Acute Myeloid Leukemia.pdf>)

Domain-focused CRISPR screening of the ubiquitination machinery across cancer cell lines revealed the Fanconi anemia proteins UBE2T and FANCL as unique dependencies in AML. These dependencies arise from a synthetic lethal interaction between FA proteins and aldehyde dehydrogenase 2 (ALDH2), which function in parallel pathways counteracting the genotoxicity of endogenous aldehydes. DNA hypermethylation and silencing of ALDH2 occurs recurrently in human AML and is sufficient to confer FA pathway dependency, suggesting that targeting the ubiquitination reaction catalysed by FA proteins could eliminate ALDH2-deficient AML.

## TP53 alteration and complex karyotype

*9 papers.* The group every other strategy in this collection excludes. Median survival is six to nine months, p53-restoring approaches have failed in trials, and the papers here are mostly about working around p53 rather than through it.

### Spinella (2026). *Science Advances.* TP53 -mutant AML with ribosomal gene loss exhibits impaired protein translation and sensitivity to HSP90 inhibition
[doi:10.1126/sciadv.aed7122](https://doi.org/10.1126/sciadv.aed7122) · `paper`  
[src](<../raw/Spinella(2026) Science Advances; TP53 -mutant AML with ribosomal gene loss exhibits impaired protein translation and sensitivity to HSP90 inhibition.pdf>)

Using the Leucegene dataset of 691 AML specimens from 656 patients, the authors identify a subset of TP53-altered AML marked by recurrent deletions on chromosome 3p, present in over 20% of TP53-mutated cases. These frequently co-occur with del(5q) and encompass ribosomal protein genes, causing network-wide downregulation of the ribosome and reduced protein synthesis - a ribosomopathy-like phenotype most pronounced when RPG deletions occur on both 3p and 5q, suggesting cooperation. Chemical screening identified HSP90 inhibition as a selective vulnerability in AML with low ribosomal protein gene expression.

### Carter (2025). *Blood.* Restoring p53 wild-type conformation in TP53 -Y220C–mutant acute myeloid leukemia
[doi:10.1182/blood.2025028935](https://doi.org/10.1182/blood.2025028935) · `paper`  
[src](<../raw/Carter(2025) Blood; Restoring p53 wild-type conformation in TP53 -Y220C–mutant acute myeloid leukemia.pdf>)

PC14586 (rezatapopt), a small molecule designed to bind the structural pocket created by the TP53-Y220C hotspot mutation, is shown to convert p53-Y220C to a wild-type conformation and activate p53 transcriptional targets - but to induce little apoptosis in TP53-Y220C AML. Two mechanisms limit it: MDM2 induced by the reactivated protein and XPO1-mediated nuclear export reduce transcriptional activity, and unlike native p53 the reactivated protein does not bind BCL-2, BCL-xL or MCL-1, so the transcription-independent apoptotic route is missing. Venetoclax compensates for the latter, inducing massive death of AML cells and stem/progenitor cells in vitro and prolonging survival of xenografts; a clinical trial in TP53-Y220C AML/MDS has begun (NCT06616636).

### Pottier (2025). *Cancer Letters.* TP53-agnostic lethality through combined pan-HDAC and CDK inhibition in acute myeloid leukemia
[doi:10.1016/j.canlet.2025.218011](https://doi.org/10.1016/j.canlet.2025.218011) · `paper`  
[src](<../raw/Pottier(2025) Cancer Letters; TP53-agnostic lethality through combined pan-HDAC and CDK inhibition in acute myeloid leukemia.pdf>)

Simultaneous inhibition of cyclin-dependent kinases and histone deacetylases with dinaciclib and CAY10603 is reported to eliminate the therapeutic response gap between TP53-mutant and TP53 wild-type AML. Biochemical profiling showed CAY10603 has pan-HDAC activity similar to SAHA rather than being HDAC6-selective as assumed. Across parental wild-type lines and isogenic TP53 mutants the combination suppressed clonogenic growth, induced caspase-dependent apoptosis, downregulated CDK2, CDK4/6 and their cyclins along with MYC and E2F1, and restored CDKN1A/p21. In an orthotopic NSG model it reduced leukemia burden and extended survival without adverse toxicity.

### Leppä (2024). *Nature Genetics.* Single-cell multiomics analysis reveals dynamic clonal evolution and targetable phenotypes in acute myeloid leukemia with complex karyotype
[doi:10.1038/s41588-024-01999-x](https://doi.org/10.1038/s41588-024-01999-x) · `paper`  
[src](<../raw/Leppä(2024) Nature Genetics; Single-cell multiomics analysis reveals dynamic clonal evolution and targetable phenotypes in acute myeloid leukemia with complex karyotype.pdf>)

Combining structural variant discovery and nucleosome occupancy profiling with transcriptomic and immunophenotypic measurement in single cells, the authors study intratumoral heterogeneity in complex-karyotype AML. Individual cells show complex structural variant landscapes with linear and circular breakage-fusion-bridge cycles and chromothripsis. Three clonal evolution patterns are identified at diagnosis or salvage - monoclonal, linear and branched polyclonal - with 75% harbouring multiple subclones frequently undergoing ongoing karyotype remodeling. Patient-derived xenografts show varied clonal evolution of leukemic stem cells, and subclone-specific drug-response profiling identifies LSC-targeting therapies including BCL-xL inhibition; paired longitudinal samples reveal both genetic evolution and cell-type plasticity as mechanisms of progression.

### Klever (2023). *Blood Advances.* AML with complex karyotype: extreme genomic complexity revealed by combined long-read sequencing and Hi-C technology
[doi:10.1182/bloodadvances.2023010887](https://doi.org/10.1182/bloodadvances.2023010887) · `paper`  
[src](<../raw/Klever(2023) Blood Advances; AML with complex karyotype extreme genomic complexity revealed by combined long-read sequencing and Hi-C technology.pdf>)

An integrative workflow combining Oxford Nanopore genomic long-read sequencing with high-throughput chromosome conformation capture (Hi-C) was applied to a defined cohort of complex-karyotype AML, identifying regions with extreme density of structural variants. These consist largely of focal amplifications enriched near mammalian-wide interspersed repeat elements, often producing oncogenic fusion transcripts such as USP7::MVD or deregulating driver genes, as confirmed by RNA-seq and direct cDNA sequencing. The authors name this pattern chromocataclysm, and show that combining the two technologies resolves complex rearrangements in regions that conventional sequencing handles poorly.

### Nishida (2023). *Science Advances.* Enhanced TP53 reactivation disrupts MYC transcriptional program and overcomes venetoclax resistance in acute myeloid leukemias
[doi:10.1126/sciadv.adh1436](https://doi.org/10.1126/sciadv.adh1436) · `paper`  
[src](<../raw/Nishida(2023) Science Advances; Enhanced TP53 reactivation disrupts MYC transcriptional program and overcomes venetoclax resistance in acute myeloid leukemias.pdf>)

Cotargeting MDM2 and the nuclear exporter XPO1 accumulates nuclear p53 and elicits a 25- to 60-fold increase in its transcriptional targets, disrupting the c-MYC-regulated transcriptome and synergistically inducing apoptosis in AML. Venetoclax-resistant AML expresses high c-MYC and is vulnerable to MDM2/XPO1 inhibition in vivo. Cells persisting after that treatment show a quiescence and stress-response phenotype - high p21, low Ki-67, raised ATF4 and LC3B - which venetoclax overcomes, as shown by single-cell mass cytometry. Triple inhibition of MDM2, XPO1 and BCL2 was highly effective against venetoclax-resistant AML in vivo.

### Rodriguez-Meira (2023). *Nature Genetics.* Single-cell multi-omics identifies chronic inflammation as a driver of TP53-mutant leukemic evolution
[doi:10.1038/s41588-023-01480-1](https://doi.org/10.1038/s41588-023-01480-1) · `paper`  
[src](<../raw/Rodriguez-Meira(2023) Nature Genetics; Single-cell multi-omics identifies chronic inflammation as a driver of TP53-mutant leukemic evolution.pdf>)

Allelic-resolution single-cell multi-omic analysis of hematopoietic stem and progenitor cells from myeloproliferative neoplasm patients who transformed to TP53-mutant secondary AML. All patients showed dominant TP53 'multihit' HSPC clones at transformation, carrying a leukemia stem cell transcriptional signature strongly predictive of adverse outcomes in independent cohorts across both TP53-mutant and wild-type AML. Through serial samples, antecedent TP53-heterozygous clones and in vivo perturbation, the authors demonstrate that chronic inflammation suppresses TP53 wild-type HSPCs while enhancing the fitness advantage of TP53-mutant cells and promoting genetic evolution.

### Spinella (2023). *Leukemia.* DELE1 haploinsufficiency causes resistance to mitochondrial stress-induced apoptosis in monosomy 5/del(5q) AML
[doi:10.1038/s41375-023-02107-4](https://doi.org/10.1038/s41375-023-02107-4) · `paper`  
[src](<../raw/Spinella(2023) Leukemia; DELE1 haploinsufficiency causes resistance to mitochondrial stress-induced apoptosis in monosomy 5 del(5q) AML.pdf>)

Using the Leucegene dataset of 48 -5/del(5q) AML specimens against 367 controls, DELE1 - located in the common deleted region - was identified as the most consistently downregulated gene. DELE1 encodes the mitochondrial protein that relays mitochondrial stress to the cytosol through the OMA1-DELE1-HRI pathway, activating ATF4 and the integrated stress response. The partial loss of DELE1 expression seen in patients was sufficient to significantly reduce sensitivity to mitochondrial stress in AML cells, suggesting DELE1 haploinsufficiency as a new driver mechanism.

### Moison (2019). *Blood Advances.* Complex karyotype AML displays G2/M signature and hypersensitivity to PLK1 inhibition
[doi:10.1182/bloodadvances.2018028480](https://doi.org/10.1182/bloodadvances.2018028480) · `paper`  
[src](<../raw/Moison(2019) Blood Advances; Complex karyotype AML displays G2 M signature and hypersensitivity to PLK1 inhibition.pdf>)

RNA sequencing of the 68 complex-karyotype AML samples in the Leucegene 415-patient cohort confirms frequent TP53 alteration and characterises its allele expression and transcript changes, and documents frequent RAS pathway alteration (N/KRAS, NF1, PTPN11, BRAF) as the second most affected pathway. Chemical interrogation of genetically characterised primary samples identifies PLK1 inhibitors as the most selective agents for this subgroup, with sensitivity independent of TP53 status. CK AML specimens show a G2/M transcriptomic signature including higher PLK1 expression that correlates with inhibitor sensitivity, and volasertib shows strong anti-AML activity in xenotransplantation models.


# E. Stem cells, heterogeneity and disease evolution

## Leukaemic stem cells, dormancy and relapse

*7 papers.* The cancer stem cell model of relapse, and the primary work that contests it. Whether the relapse-initiating cell is a stem cell or a transient state that any cell can enter is not settled inside this topic.

### Larrue (2026). *Cell Reports Medicine.* Non-genetic remodeling drives leukemia propagation and reveals actionable vulnerabilities in acute myeloid leukemia
[doi:10.1016/j.xcrm.2026.103017](https://doi.org/10.1016/j.xcrm.2026.103017) · `paper`  
[src](<../raw/Larrue(2026) Cell Reports Medicine; Non-genetic remodeling drives leukemia propagation and reveals actionable vulnerabilities in acute myeloid leukemia.pdf>)

Serial patient-derived xenotransplantation establishes a longitudinal model in which leukemia-initiating capacity progressively increases. Integrated single-cell transcriptomics and multi-omics reveal a predominantly non-genetic trajectory following a conserved pattern across models, with coordinated changes across epigenetic, transcriptional and proteomic layers; ribosome profiling and rRNA 2'-O-methylation analysis show a stage-specific increase in translational activity with ribosome remodeling in advanced xenografts. A screen of 3247 compounds uncovers a limited set of vulnerabilities emerging during progression, including CRBN-dependent degradation of GSPT1 (CC-885) and IAP antagonism (AZD5582), both of which reduce burden, impair propagation and enhance cytarabine activity in vivo.

### Worker (2025). *Blood Neoplasia.* How to drug a leukemic stem cell: deciphering heterogeneity for better specificity
[doi:10.1016/j.bneo.2025.100146](https://doi.org/10.1016/j.bneo.2025.100146) · `paper`  
[src](<../raw/Worker(2025) Blood Neoplasia; How to drug a leukemic stem cell deciphering heterogeneity for better specificity.pdf>)

A review of leukemic stem cell biology framed around the problem of therapeutic specificity. It sets out that relapse is the single most important cause of treatment failure in AML, with more than half of intensively treated patients relapsing within a year, and that relapse originates from quiescent LSCs sheltering in the marrow that escape chemotherapy aimed at proliferating blasts. It surveys global and subtype-specific LSC traits, how heterogeneity between AML subtypes and within the LSC compartment has frustrated target discovery, how single-cell sequencing is resolving that, and which aspects of LSC biology admit targeted treatment.

### Lambo (2023). *Cancer Cell.* A longitudinal single-cell atlas of treatment response in pediatric AML
[doi:10.1016/j.ccell.2023.10.008](https://doi.org/10.1016/j.ccell.2023.10.008) · `paper`  
[src](<../raw/Lambo(2023) Cancer Cell; A longitudinal single-cell atlas of treatment response in pediatric AML.pdf>)

Single-cell RNA and ATAC sequencing of 28 pediatric AML patients from the AAML1031 trial, representing different subtypes, profiled at diagnosis, remission and relapse. Cellular composition differed between genetic subgroups at diagnosis; upon relapse, cellular hierarchies transitioned toward a more primitive state regardless of subtype. Primitive cells at relapse were distinct from those at diagnosis, with under-representation of myeloid transcriptional programs and over-representation of other lineage programs, in some patients including the appearance of a B-lymphoid-like hierarchy.

### Stelmach (2023). *Haematologica.* Leukemic stem cells and therapy resistance in acute myeloid leukemia
[doi:10.3324/haematol.2022.280800](https://doi.org/10.3324/haematol.2022.280800) · `paper`  
[src](<../raw/Stelmach(2023) Haematologica; Leukemic stem cells and therapy resistance in acute myeloid leukemia.pdf>)

A review of leukemic stem cell biology and its relationship to therapy resistance in AML. It presents the cancer stem cell concept in which LSCs sit at the top of each genetically defined subclone forming epigenetically controlled downstream hierarchies, and emphasises their phenotypic and epigenetic plasticity under therapy stress. It argues that targeted strategies must be incorporated into first-line regimens to prevent LSC-mediated relapse, discusses venetoclax plus azacitidine as the current promising approach, and surveys LSC vulnerabilities, current clinical trial activity and the contribution of single-cell multi-omics to characterising relapse-initiating populations.

### Zeng (2022). *Nature Medicine.* A cellular hierarchy framework for understanding heterogeneity and predicting drug response in acute myeloid leukemia
[doi:10.1038/s41591-022-01819-x](https://doi.org/10.1038/s41591-022-01819-x) · `paper`  
[src](<../raw/Zeng(2022) Nature Medicine; A cellular hierarchy framework for understanding heterogeneity and predicting drug response in acute myeloid leukemia.pdf>)

Leukemia cell hierarchy composition was determined from bulk transcriptomes of more than 1000 patients by deconvolution using single-cell reference profiles of leukemia stem, progenitor and mature cell types. Hierarchy composition was associated with functional, genomic and clinical properties and converged into four classes - Primitive, Mature, GMP and Intermediate. Variation along the Primitive versus GMP axis was associated with chemotherapy response, and along the Primitive versus Mature axis with drug sensitivity profiles of targeted therapies; a seven-gene biomarker derived from the latter axis was associated with response to 105 investigational drugs.

### Zhai (2022). *Molecular Cancer.* Longitudinal single-cell transcriptomics reveals distinct patterns of recurrence in acute myeloid leukemia
[doi:10.1186/s12943-022-01635-4](https://doi.org/10.1186/s12943-022-01635-4) · `paper`  
[src](<../raw/Zhai(2022) Molecular Cancer; Longitudinal single-cell transcriptomics reveals distinct patterns of recurrence in acute myeloid leukemia.pdf>)

Whole-exome sequencing for somatic mutations and copy number variations was combined with single-cell RNA-seq to investigate clonal heterogeneity in diagnosis-relapse pairs. Extensive expression differences were found between patients and between paired samples, even for those with the same presumed initiating events, and the differences were associated with clonal composition and evolution - most strikingly in patients acquiring large-scale copy number variations at relapse. In a DNMT3A/FLT3-ITD patient the leukemia switched from an AP-1-regulated clone at diagnosis to an mTOR signalling-driven clone at relapse, while two AML1-ETO pairs shared genes related to hematopoietic stem cell maintenance and cell migration, suggesting relapse LSC-like cells evolved from diagnosis cells.

### Duy (2021). *Cancer Discovery.* Chemotherapy Induces Senescence-Like Resilient Cells Capable of Initiating AML Recurrence
[doi:10.1158/2159-8290.CD-20-1375](https://doi.org/10.1158/2159-8290.CD-20-1375) · `paper`  
[src](<../raw/Duy(2021) Cancer Discovery; Chemotherapy Induces Senescence-Like Resilient Cells Capable of Initiating AML Recurrence.pdf>)

Primary AML cells are shown to enter a senescence-like phenotype after chemotherapy in vitro and in vivo, with induction of senescence/inflammatory and embryonic diapause transcriptional programs and downregulation of MYC and leukemia stem cell genes. Single-cell RNA sequencing suggests depletion of leukemia stem cells and enrichment of distinct senescence-like subpopulations. The state is transient and confers superior colony-forming and engraftment potential; entry into it depends on ATR, and ATR inhibitors severely impair persistence of AML cells. Recovered post-senescence cells give rise to relapsed AML with increased stem cell potential.

## Single-cell atlases of AML heterogeneity

*7 papers.* Resources rather than results, and the reason several other topics here could be written. Expression alone cannot tell a malignant cell from a normal one in a disease that recapitulates hematopoiesis, so genotype has to be read from the same cell.

### Zhang (2026). *Journal of Advanced Research.* Dynamic heterogeneity towards drug resistance in AML cells is primarily driven by epigenomic mechanism unveiled by multi-omics analysis
[doi:10.1016/j.jare.2025.05.038](https://doi.org/10.1016/j.jare.2025.05.038) · `paper`  
[src](<../raw/Zhang(2026) Journal of Advanced Research; Dynamic heterogeneity towards drug resistance in AML cells is primarily driven by epigenomic mechanism unveiled by multi-omics analysis.pdf>)

A multi-omics approach integrating single-cell RNA sequencing, chromatin accessibility profiling, DNA methylation analysis and whole-exome sequencing was applied to AML cell lines (KG-1a, Kasumi-1, HL-60) treated with standard chemotherapeutics. Drug exposure induced a transition to stem-like states; cytarabine-resistant KG-1a cells predominantly originated from G2/M phase subpopulations, indicating cell-cycle-specific mechanisms; and rapid acquisition of drug resistance was driven primarily by epigenomic regulation of the transcriptome, with minimal contribution from genetic mutations.

### Baronas (2025). *venue not recorded.* High-throughput single cell -omics using semi-permeable capsules
[doi:10.1101/2025.03.14.642805](https://doi.org/10.1101/2025.03.14.642805) · `preprint`  
[src](<../raw/Baronas(2025) unknown; High-throughput single cell -omics using semi-permeable capsules.pdf>)

A technology based on semi-permeable capsules (SPCs) - uniform compartments with a liquid core inside a thin, tunable semi-permeable shell - for high-throughput nucleic acid assays including digital PCR, genome sequencing, single-cell RNA-seq and FACS-based isolation of transcriptomes by nucleic acid marker. SPCs retain nucleic acid fragments longer than 300 bp while admitting enzymes up to 160 kDa, are biocompatible enough to support single-cell cultivation and clonal expansion, and survive freezing, thawing, thermocycling and FACS. Applied as CapSeq to white blood cells from patients with hematopoietic disorders, they give superior transcript capture, and in AML samples reveal changes in mature granulocyte and monocyte transcriptomes associated with blast and progenitor phenotypes.

### Lilljebjörn (2025). *Nature Communications.* The AML cellular state space unveils NPM1 immune evasion subtypes with distinct clinical outcomes
[doi:10.1038/s41467-025-66546-6](https://doi.org/10.1038/s41467-025-66546-6) · `paper`  
[src](<../raw/Lilljebjörn(2025) Nature Communications; The AML cellular state space unveils NPM1 immune evasion subtypes with distinct clinical outcomes.pdf>)

Genomic and transcriptomic characterisation of 120 AMLs including single-cell RNA sequencing reveals cellular heterogeneity that distorts bulk transcriptomic profiles. Examining the signatures of more than 90,000 immature AML cells selectively identifies four main clusters, extending current genomic classification. NPM1-mutated AML stratifies into two clinically relevant classes: NPM1 class I shows downregulation of MHC class II and excellent survival after hematopoietic stem cell transplantation, while NPM1 class II is resistant to allogeneic T cells in ex vivo co-culture and has dismal survival after transplant.

### Tian (2025). *Science Bulletin.* Integrative scATAC-seq and mtDNA mutation analysis reveals disease-driven regulatory aberrations in AML
[doi:10.1016/j.scib.2025.07.009](https://doi.org/10.1016/j.scib.2025.07.009) · `paper`  
[src](<../raw/Tian(2025) Science Bulletin; Integrative scATAC-seq and mtDNA mutation analysis reveals disease-driven regulatory aberrations in AML.pdf>)

Mitochondrial single-cell ATAC-seq with single-cell RNA-seq was used to characterise AML cells, mapping them onto a constructed single-cell hematopoiesis reference to identify altered chromatin accessibility at cis-regulatory elements. Using an in-house algorithm, cisGRN, the authors found that mutations in the WT1 zinc finger domain associate with decreased accessibility and hypermethylation at target gene regulatory regions, validating five mutations (R467Q, R467L, R467W, H470Y, H470R). They identified a cis-regulatory element mutation arising early in hematopoiesis that creates a new CEBPB binding motif, activating enhancer activity and GATA4 expression to promote proliferation, confirmed by luciferase reporter and prime editing. Mitochondrial DNA lineage tracing with machine learning identified relapse-associated clones resembling leukemia stem cells and 27 marker genes predicting relapse.

### Wu (2020). *Journal of Hematology & Oncology.* A single-cell survey of cellular hierarchy in acute myeloid leukemia
[doi:10.1186/s13045-020-00941-y](https://doi.org/10.1186/s13045-020-00941-y) · `paper`  
[src](<../raw/Wu(2020) Journal of Hematology & Oncology; A single-cell survey of cellular hierarchy in acute myeloid leukemia.pdf>)

Using Microwell-seq, 191,727 cells from bone marrow of 40 AML patients and 3 healthy donors were analysed, with single-molecule real-time sequencing used to investigate clonal heterogeneity. The authors established a single-cell AML landscape, identified an AML progenitor cell cluster with novel markers, and found that patients with ribosomal protein-high progenitor cells had a low remission rate, deducing two types of AML with diverse clinical outcomes. Combining Microwell-seq with SMRT sequencing to trace mitochondrial mutations showed a lack of association between AML clones and transcriptomic phenotypes, prompting the proposal of a phenotypic 'cancer attractor' defining a common AML progenitor phenotype.

### Petti (2019). *Nature Communications.* A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing
[doi:10.1038/s41467-019-11591-1](https://doi.org/10.1038/s41467-019-11591-1) · `paper`  
[src](<../raw/Petti(2019) Nature Communications; A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing.pdf>)

An approach integrating enhanced whole genome sequencing with single-cell RNA sequencing to detect expressed mutations in individual cells. Applied to five cryopreserved AML samples, it identified hundreds to thousands of cells carrying tumour-specific mutations in each case, allowing AML cells - including normal-karyotype AML cells - to be distinguished from normal cells, expression signatures to be associated with subclonal mutations, and cell surface markers to be identified for purifying subclones. The cases averaged 26 coding mutations, with subclones inferred by SciClone, and at least one subclone identified in every case.

### vanGalen (2019). *Cell.* Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity
[doi:10.1016/j.cell.2019.01.031](https://doi.org/10.1016/j.cell.2019.01.031) · `paper`  
[src](<../raw/vanGalen(2019) Cell; Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity.pdf>)

Combining single-cell RNA sequencing with genotyping, 38,410 cells were profiled from 40 bone marrow aspirates including 16 AML patients and five healthy donors, and a machine learning classifier applied to distinguish malignant cell types whose abundances varied between patients and over disease progression. Six malignant cell types along the HSC-to-myeloid axis were identified; primitive AML cells aberrantly co-express stemness and myeloid priming genes; and differentiated AML cells express immunomodulatory factors and suppress T cells. Unsupervised clustering of TCGA bulk profiles by the derived signatures yielded seven AML groups with distinct cell-type compositions, each strongly enriched for characteristic genetic lesions.


# F. Diagnosis, stratification and immunotherapy

## Transcriptome-based diagnosis, classification and risk

*10 papers.* The argument that one RNA-seq assay should replace the current patchwork of cytogenetics, FISH and targeted panels - with the validation work that claim requires, and the populations for whom the existing panels were never built.

### Salah (2026). *European Journal of Haematology.* Epigenetics and In Silico Transcriptome Analysis of Pediatric Acute Myeloid Leukemia
[doi:10.1111/ejh.70230](https://doi.org/10.1111/ejh.70230) · `paper`  
[src](<../raw/Salah(2026) European Journal of Haematology; Epigenetics and In Silico Transcriptome Analysis of Pediatric Acute Myeloid Leukemia.pdf>)

A review of the molecular and epigenetic landscape of pediatric AML, which accounts for 15-20% of childhood leukemias and where survival for high-risk patients remains below 60%. It covers the distinct genetic profile of pediatric relative to adult disease - FLT3-ITD, NPM1, KMT2A rearrangements and core-binding factor fusions - alongside aberrant DNA methylation, histone modifications and non-coding RNA expression. It surveys how computational RNA-seq pipelines and pathway analyses have highlighted DNMT3A, TET2 and HDACs as candidate targets, and how multi-omics combining transcriptomic, methylomic and chromatin accessibility data is being used to define biomarkers.

### Huang (2025). *Annals of Hematology.* Transcriptome-based molecular subgroup identification and prognosis stratification in pediatric AML
[doi:10.1007/s00277-025-06634-1](https://doi.org/10.1007/s00277-025-06634-1) · `paper`  
[src](<../raw/Huang(2025) Annals of Hematology; Transcriptome-based molecular subgroup identification and prognosis stratification in pediatric AML.pdf>)

A computational analysis of public AML transcriptome data from the GDC Data Portal with MSigDB gene sets, reclassifying AML into 8 molecular subgroups and characterising their expression profiles, immune microenvironment, biological pathways and clinical features. Four machine learning algorithms (random forest, SVM, XGBoost, decision tree) were compared for classification, with XGBoost performing best; HSD17B10, NDUFS8, ASCL5, FADS2 and COX8A emerged as important features, of which only NDUFS8 and FADS2 had been previously reported in AML. A 62-gene prognostic model is proposed with retrospective validation.

### Richard-Carpentier (2025). *Biomarker Research.* High IL1R1 expression predicts poor survival and benefit from stem cell transplant in intermediate-risk acute myeloid leukemia from the Leucegene cohort
[doi:10.1186/s40364-025-00827-6](https://doi.org/10.1186/s40364-025-00827-6) · `paper`  
[src](<../raw/Richard-Carpentier(2025) Biomarker Research; High IL1R1 expression predicts poor survival and benefit from stem cell transplant in intermediate-risk acute myeloid leukemia from the Leucegene cohort.pdf>)

Transcriptomic analysis of 316 Leucegene patients with intermediate-risk cytogenetic AML treated with intensive chemotherapy identified high IL1R1 expression as both prognostic and predictive. IL1R1-high was associated with older age, monocytic differentiation, more FLT3-ITD and RUNX1 mutations and fewer IDH1/2 and bZIP CEBPA mutations, and with lower 5-year overall survival (10% versus 38%) and higher relapse incidence (76% versus 59%), independently in multivariable analysis (HR 1.78). In landmark analysis, transplant in first remission significantly improved 5-year survival in IL1R1-high patients (67% versus 27%, HR 0.33) but not in IL1R1-low patients (62% versus 54%, HR 0.72), and the poor prognosis of IL1R1-high was abrogated by transplant.

### Voss (2025). *Leukemia.* Clinical experience of using integrated whole genome and transcriptome sequencing as a framework for pediatric and adolescent acute myeloid leukemia diagnosis and risk assessment
[doi:10.1038/s41375-025-02774-5](https://doi.org/10.1038/s41375-025-02774-5) · `paper`  
[src](<../raw/Voss(2025) Leukemia; Clinical experience of using integrated whole genome and transcriptome sequencing as a framework for pediatric and adolescent acute myeloid leukemia diagnosis and risk assessment.pdf>)

A systematic review of real-time clinical experience with integrated whole genome and whole transcriptome sequencing (iWGS-WTS) for pediatric AML diagnostic workup at a single institution, comparing results against whole genome sequencing, whole exome sequencing, whole transcriptome sequencing, cytogenetics and targeted panel NGS. The integrated approach improved identification of clinically relevant alterations, enhancing disease classification and risk assessment; 18 AML-driver gene fusions found by iWGS-WTS were missed by karyotyping owing to their cryptic or complex nature, and combining copy number analysis with soft-clipped reads identified 12 small CNVs under 10 kb that SNP arrays would miss. It also streamlines sample acquisition and reduces testing redundancy.

### Stiff (2024). *Nature Genetics.* Multiomic profiling identifies predictors of survival in African American patients with acute myeloid leukemia
[doi:10.1038/s41588-024-01929-x](https://doi.org/10.1038/s41588-024-01929-x) · `paper`  
[src](<../raw/Stiff(2024) Nature Genetics; Multiomic profiling identifies predictors of survival in African American patients with acute myeloid leukemia.pdf>)

Exomes and transcriptomes of 100 AML patients with genomically confirmed African ancestry were compared with 323 self-reported white patients. Of 162 gene mutations recurrent in Black patients, 73% - including a previously unreported PHIP alteration in 7% - were found in one white patient or not at all. Black patients with myelodysplasia-related AML were younger. On multivariable analysis, NPM1 and NRAS mutations were associated with inferior disease-free survival and IDH1 and IDH2 with reduced overall survival. Inflammatory profiles, cell type distributions and transcriptional profiles differed between Black and white patients with NPM1 mutations, and incorporating ancestry-specific risk markers into ELN 2022 stratification changed risk group for one-third of Black patients and improved outcome prediction.

### Rosenquist (2023). *Journal of Internal Medicine.* Novel precision medicine approaches and treatment strategies in hematological malignancies
[doi:10.1111/joim.13697](https://doi.org/10.1111/joim.13697) · `paper`  
[src](<../raw/Rosenquist(2023) Journal of Internal Medicine; Novel precision medicine approaches and treatment strategies in hematological malignancies.pdf>)

A review of precision diagnostics in hematological malignancies, covering how genetic testing has been implemented to guide treatment selection and improve survival in myeloid disease (myelodysplastic syndromes and AML) and lymphoid disease (acute lymphoblastic leukemia, diffuse large B-cell lymphoma and chronic lymphocytic leukemia). It discusses monitoring measurable residual disease with ultra-sensitive techniques - flow cytometry, quantitative and droplet digital PCR, and next-generation sequencing, each with stated advantages and limitations - to assess therapy response and detect early relapse, and surveys functional precision medicine combining ex vivo drug screening with omics technologies for patients with advanced disease.

### Docking (2021). *Nature Communications.* A clinical transcriptome approach to patient stratification and therapy selection in acute myeloid leukemia
[doi:10.1038/s41467-021-22625-y](https://doi.org/10.1038/s41467-021-22625-y) · `paper`  
[src](<../raw/Docking(2021) Nature Communications; A clinical transcriptome approach to patient stratification and therapy selection in acute myeloid leukemia.pdf>)

A clinical transcriptome-based assay for AML stratification, developed and validated against whole genome and exome sequencing, which shows that standalone RNA-seq gives the greatest diagnostic return - expressed gene fusions, SNVs and short indels, and whole-transcriptome expression together. Expression data from 154 AML patients yield a prognostic score strongly associated with outcome across 620 patients in three independent cohorts and 42 in a prospective cohort. Combined with molecular risk guidelines it re-stratifies 22.1% to 25.3% of patients into correct risk groups, and within the adverse-risk subgroup identifies patients with dysregulated integrin signalling and RUNX1 or TP53 mutation who may benefit from focal adhesion kinase (PTK2) inhibitors.

### Flensburg (2021). *Bioinformatics.* Detecting copy number alterations in RNA-Seq using SuperFreq
[doi:10.1093/bioinformatics/btab440](https://doi.org/10.1093/bioinformatics/btab440) · `paper`  
[src](<../raw/Flensburg(2021) Bioinformatics; Detecting copy number alterations in RNA-Seq using SuperFreq.pdf>)

SuperFreq is adapted to call absolute and allele-sensitive copy number alterations from RNA-seq, using an error-propagation framework to combine read counts and B-allele frequencies. Assessed against TCGA DNA SNP-arrays, it agreed for over 98% of the genome in AML (n = 116) and 87% in colorectal cancer (n = 377) when ploidy estimates were consistent. Sensitivity depended on gene density: 78% of CNA calls covering 100 or more genes were detected at 94% precision, with recall dropping for focal events - all 7 high-level ERBB2 amplifications were found but only 1 of 17 moderate IGF2 amplifications. It offers an integrated platform for CNAs and point mutations, and reproduced the known relationship between mutation load and CNA profile in CRC from RNA-seq alone.

### Arindrarto (2020). *Leukemia.* Comprehensive diagnostics of acute myeloid leukemia by whole transcriptome RNA sequencing
[doi:10.1038/s41375-020-0762-8](https://doi.org/10.1038/s41375-020-0762-8) · `paper`  
[src](<../raw/Arindrarto(2020) Leukemia; Comprehensive diagnostics of acute myeloid leukemia by whole transcriptome RNA sequencing.pdf>)

HAMLET (Human AML Expedited Transcriptomics), a bioinformatics pipeline that calls fusion genes, small variants, tandem duplications and gene expression from a single whole-transcriptome RNA-seq run, with results assembled into one annotated output file. Applied to 100 AML cases and validated against reference assays and targeted resequencing, it detected all fusion genes and EVI1 overexpression irrespective of 3q26 aberration, called small variants in 13 recurrently mutated genes at 99.2% sensitivity and 100% specificity, and detected FLT3 and KMT2A tandem duplications at 100% sensitivity and 97.1% specificity using a soft-clipped-read algorithm.

### Audemard (2019). *Life Science Alliance.* Targeted variant detection using unaligned RNA-Seq reads
[doi:10.26508/lsa.201900336](https://doi.org/10.26508/lsa.201900336) · `paper`  
[src](<../raw/Audemard(2019) Life Science Alliance; Targeted variant detection using unaligned RNA-Seq reads.pdf>)

km, a method for targeted variant detection that decomposes RNA-seq reads into k-mers and identifies mutations without mapping reads to a reference. Given any sequence as an expected reference, it reports all alternative forms sharing that reference's extremities, and so detects single-base substitutions, insertions, deletions, duplications, inversions and fusions with one mechanism. Evaluated on two independent cohorts, TCGA and Leucegene, across 10,844 samples, detection is shown to be fast, accurate and mainly limited by sequencing depth.

## Immunotherapy, immune evasion and the microenvironment

*7 papers.* AML has one approved therapeutic antibody and a low mutational burden. These papers look for antigens, for the reasons T cells fail here, and for ways to make a cold tumour visible.

### Fetsch (2026). *Blood.* Menin inhibition enhances graft-versus-leukemia effects by T-cell activation and endogenous retrovirus induction in AML
[doi:10.1182/blood.2025029712](https://doi.org/10.1182/blood.2025029712) · `paper`  
[src](<../raw/Fetsch(2026) Blood; Menin inhibition enhances graft-versus-leukemia effects by T-cell activation and endogenous retrovirus induction in AML.pdf>)

Menin inhibition is shown to have an immunological mechanism in addition to its antileukemic one. In KMT2A-rearranged and NPM1-mutated AML cells, in vitro and in vivo, it induces class II transactivator and MHC-II expression, sensitising cells to T-cell-mediated elimination after allogeneic transplant in mice and enhancing the graft-versus-leukemia effect in human xenografts. Mechanistically it increases expression of multiple human endogenous retroviruses, driving interferon-stimulated gene upregulation and MHC-II expression. It also acts directly on donor T cells, raising TNF-alpha, interferon-gamma, perforin and granzyme A/B production and cytolytic activity, and reducing T-cell exhaustion and menin-KMT2A binding at genes encoding negative regulators of T-cell activation.

### Métois (2025). *Biomarker Research.* IL1RAP is an immunotherapeutic target for normal karyotype triple-mutated acute myeloid leukemia
[doi:10.1186/s40364-025-00769-z](https://doi.org/10.1186/s40364-025-00769-z) · `paper`  
[src](<../raw/Métois(2025) Biomarker Research; IL1RAP is an immunotherapeutic target for normal karyotype triple-mutated acute myeloid leukemia.pdf>)

Seeking surface antigens for immunotherapy in normal-karyotype triple-mutated AML (NPM1c with FLT3-ITD and DNMT3A), the authors performed surface proteome enrichment on 100 primary AML samples including 12 NKt-AML, transcriptome analysis on 691 samples, and single-cell RNA sequencing on 23. IL1RAP is identified as expressed on primitive AML cells resembling leukemic stem cells in NKt-AML while relatively low on normal bone marrow HSCs. Elevated IL1RAP associates with poor overall and relapse-free survival and predicts non-response to hematopoietic stem cell transplantation, and IL1RAP protein internalises after antibody exposure, supporting antibody-drug conjugate development.

### Bordeleau (2024). *Cell Reports.* Immunotherapeutic targeting of surfaceome heterogeneity in AML
[doi:10.1016/j.celrep.2024.114260](https://doi.org/10.1016/j.celrep.2024.114260) · `paper`  
[src](<../raw/Bordeleau(2024) Cell Reports; Immunotherapeutic targeting of surfaceome heterogeneity in AML.pdf>)

A surface proteome analysis of 100 genetically diverse primary human AML specimens, combined with single-cell transcriptomics on a subset to assess antigen expression at sub-population level. The effort identifies numerous antigens and markers preferentially expressed by primitive AML cells, many of them already targeted by therapeutic antibodies in clinical evaluation for other cancers, and characterises AML heterogeneity at the surfaceome level by identifying antigens and candidate primitive-cell markers specific to genetic subgroups including KMT2A-r, NPM1-mut, NK triple-mut, inv(16), complex karyotype and RUNX1-mut. The dataset is released publicly through LASA.

### Chang (2024). *Cell Reports.* SETDB1 suppresses NK cell-mediated immunosurveillance in acute myeloid leukemia with granulo-monocytic differentiation
[doi:10.1016/j.celrep.2024.114536](https://doi.org/10.1016/j.celrep.2024.114536) · `paper`  
[src](<../raw/Chang(2024) Cell Reports; SETDB1 suppresses NK cell-mediated immunosurveillance in acute myeloid leukemia with granulo-monocytic differentiation.pdf>)

In vivo and in vitro CRISPR-Cas9 library screens in a mouse monocytic AML model identify SETDB1 and its partners ATF7IP and TRIM33 as tumour promoters in vivo. The growth inhibition from Setdb1 depletion depends mainly on NK cell-mediated cytotoxicity: SETDB1 loss demethylates H3K9 at enhancers, upregulating interferon-stimulated genes and NKG2D ligands, raising immunogenicity to NK cells and intrinsic apoptosis. The effects are absent in non-monocytic leukemia cells, and MNDA (murine Ifi203) expression predicts which AML is sensitive to SETDB1 depletion.

### Yang (2023). *Blood.* C1Q labels a highly aggressive macrophage-like leukemia population indicating extramedullary infiltration and relapse
[doi:10.1182/blood.2022017046](https://doi.org/10.1182/blood.2022017046) · `paper`  
[src](<../raw/Yang(2023) Blood; C1Q labels a highly aggressive macrophage-like leukemia population indicating extramedullary infiltration and relapse.pdf>)

Single-cell RNA sequencing of bone marrow and extramedullary infiltration samples from an AML patient with pervasive leukemia cutis identified a complement C1Q-positive macrophage-like leukemia subset, enriched in skin and present in marrow before extramedullary manifestations, then verified in multiple patients. C1Q expression, modulated by the transcription factor MAFB, conferred tissue infiltration ability sufficient to establish cutaneous and gastrointestinal nodules in xenograft models, and was independently associated with adverse prognosis. Fibroblasts attracted C1Q+ leukemia cells through C1Q-gC1QR recognition and subsequent TGF-beta1 stimulation, which also supported survival of these cells under chemotherapy stress.

### Ellegast (2022). *Cancer Discovery.* Unleashing Cell-Intrinsic Inflammation as a Strategy to Kill AML Blasts
[doi:10.1158/2159-8290.CD-21-0956](https://doi.org/10.1158/2159-8290.CD-21-0956) · `paper`  
[src](<../raw/Ellegast(2022) Cancer Discovery; Unleashing Cell-Intrinsic Inflammation as a Strategy to Kill AML Blasts.pdf>)

Genome-wide screens for genetic vulnerabilities in inflammatory pathways identify the immune modulator IRF2BP2 as a selective AML dependency, validated genetically and by targeted protein degradation in vitro and genetically in vivo. Chromatin and expression studies show that IRF2BP2 represses IL-1beta/TNFalpha signalling via NF-kB, binding enhancers and promoters, with gain of H3K27ac at upregulated targets after its degradation. Perturbing IRF2BP2 produces an acute inflammatory state that kills AML cells, establishing IRF2BP2-mediated transcriptional repression as a mechanism of blast survival.

### Ho (2022). *Blood.* Targeting MDM2 enhances antileukemia immunity after allogeneic transplantation via MHC-II and TRAIL-R1/2 upregulation
[doi:10.1182/blood.2022016082](https://doi.org/10.1182/blood.2022016082) · `paper`  
[src](<../raw/Ho(2022) Blood; Targeting MDM2 enhances antileukemia immunity after allogeneic transplantation via MHC-II and TRAIL-R1 2 upregulation.pdf>)

AML relapse after allogeneic transplant is driven by leukemia cells resistant to allogeneic T cells through decreased MHC class II expression and apoptosis resistance. MDM2 inhibition is shown to counteract this immune evasion, inducing MHC class I and II expression in murine and human AML and upregulating TRAIL-R1/R2 in a p53-dependent manner, which was confirmed in primary human AML and post-transplant relapse samples. Blocking TRAIL, using TRAIL-deficient donor T cells, or knocking out TRAIL-R2 each reduced the protective effect in vivo, and depletion of CD8+ T cells but not NK cells abrogated it.

## Functional genomics screens as target-discovery platforms

*5 papers.* Screens read as method rather than as result: what changes when you screen in vivo instead of in culture, in primary cells instead of lines, or filter hits against human genetics before believing them.

### Cao (2026). *Molecular Cell.* CRISPR-based functional genomics for dissecting therapeutic dependency in primary acute myeloid leukemia samples
[doi:10.1016/j.molcel.2026.02.003](https://doi.org/10.1016/j.molcel.2026.02.003) · `paper`  
[src](<../raw/Cao(2026) Molecular Cell; CRISPR-based functional genomics for dissecting therapeutic dependency in primary acute myeloid leukemia samples.pdf>)

An optimized CRISPR platform for functional genomics directly in patient-derived xenograft and primary AML samples carrying diverse pathogenic mutations. Integrated in vitro and in vivo CRISPR-Cas9 knockout and CRISPR interference dropout screens validated known AML-biased targets and identified cis-regulatory elements essential for leukemic growth, while coupling pooled perturbations with single-cell RNA sequencing (Perturb-seq) resolved perturbation-induced changes in regulatory networks, cell cycle states and cellular hierarchies. The system achieved successful editing in about 88% (22 of 25) of samples tested, across 3 PDX and 22 primary patient samples.

### Jin (2022). *Clinical Cancer Research.* Large-Scale In Vitro and In Vivo CRISPR-Cas9 Knockout Screens Identify a 16-Gene Fitness Score for Improved Risk Assessment in Acute Myeloid Leukemia
[doi:10.1158/1078-0432.CCR-22-1618](https://doi.org/10.1158/1078-0432.CCR-22-1618) · `paper`  
[src](<../raw/Jin(2022) Clinical Cancer Research; Large-Scale In Vitro and In Vivo CRISPR-Cas9 Knockout Screens Identify a 16-Gene Fitness Score for Improved Risk Assessment in Acute Myeloid Leukemia.pdf>)

Integrating genome-wide CRISPR-Cas9 data from more than 1000 in vitro and in vivo knockout screens, the authors identify 280 AML-specific fitness genes and derive a 16-gene fitness score (AFG16) by sparse regression in a training cohort of 618 cases, validated in five public cohorts (n = 1570) and their own RJAML cohort (n = 157) with matched RNA and targeted sequencing - more than 2300 patients in total. AFG16 distils the downstream consequences of several genetic abnormalities and substantially improves ELN classification; high scores predicted poor response to induction chemotherapy, and ex vivo drug screening showed high-AFG16 patients were more sensitive to the cell-cycle inhibitors flavopiridol and SNS-032, with strongly activated cell-cycle signalling.

### Lin (2022). *Nature Cancer.* P2RY2-AKT activation is a therapeutically actionable consequence of XPO1 inhibition in acute myeloid leukemia
[doi:10.1038/s43018-022-00394-x](https://doi.org/10.1038/s43018-022-00394-x) · `paper`  
[src](<../raw/Lin(2022) Nature Cancer; P2RY2-AKT activation is a therapeutically actionable consequence of XPO1 inhibition in acute myeloid leukemia.pdf>)

Systematically cataloguing the pro- and anti-fitness consequences of selinexor treatment in AML, the authors find that the XPO1 inhibitor activates PI3K-gamma-dependent AKT signalling by upregulating the purinergic receptor P2RY2. Inhibiting this axis potentiates selinexor's anti-leukemic effects in cell lines, patient-derived primary cultures and multiple mouse models. In a syngeneic MLL-AF9 model, selinexor plus the AKT inhibitor ipatasertib outperformed both standard-of-care chemotherapy and chemotherapy plus selinexor, and reduced leukemia-initiating cell burden.

### Yamauchi (2018). *Cancer Cell.* Genome-wide CRISPR-Cas9 Screen Identifies Leukemia-Specific Dependence on a Pre-mRNA Metabolic Pathway Regulated by DCPS
[doi:10.1016/j.ccell.2018.01.012](https://doi.org/10.1016/j.ccell.2018.01.012) · `paper`  
[src](<../raw/Yamauchi(2018) Cancer Cell; Genome-wide CRISPR-Cas9 Screen Identifies Leukemia-Specific Dependence on a Pre-mRNA Metabolic Pathway Regulated by DCPS.pdf>)

Genome-wide CRISPR-Cas9 screening in AML cell lines, followed by a second screen in vivo, identified the mRNA decapping enzyme scavenger gene DCPS as essential for AML survival. Mass spectrometry showed DCPS interacting with components of pre-mRNA metabolic pathways including spliceosomes. RG3039, a DCPS inhibitor originally developed for spinal muscular atrophy, showed anti-leukemic activity by inducing pre-mRNA mis-splicing. Humans with germline biallelic DCPS loss-of-function mutations have no aberrant hematologic phenotype, indicating DCPS is dispensable for human hematopoiesis.

### Tzelepis (2016). *Cell Reports.* A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia
[doi:10.1016/j.celrep.2016.09.079](https://doi.org/10.1016/j.celrep.2016.09.079) · `paper`  
[src](<../raw/Tzelepis(2016) Cell Reports; A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia.pdf>)

An optimised genome-wide CRISPR-Cas9 screening platform for recessive genetic screens is applied to human AML cell lines, producing a catalogue of genetic vulnerabilities. It recovers known therapeutic targets including BRD4, DOT1L and MEN1 alongside numerous additional candidates. KAT2A is proposed as a therapeutic target: its inhibition induces myeloid differentiation and apoptosis and arrests growth of primary AML cells while sparing normal progenitors.


## What this document does not say

- **It does not rank or evaluate.** A paper's presence records that the team read or wrote it,
  nothing more.
- **It does not say who circulated what.** That is recorded per paper in the sidecars, and is
  deliberately not browsable.
- **It does not resolve disagreements between papers.** Two entries in one topic may contradict
  each other; the topic groups subjects, not conclusions.
- **The counts in `## Contents` are the checksum, not decoration.** `scripts/build.py` refuses to
  build if the body disagrees with them.
