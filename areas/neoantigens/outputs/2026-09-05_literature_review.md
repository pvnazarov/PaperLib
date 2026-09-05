# Neoantigens — literature review: 125 papers by topic

> 2026-09-05 · area: Neoantigens · 125 papers in 19 topics, each paper in exactly one

## How to read this

Every paper in the collection, clustered by subject. 125 papers, 19 topics in 5 parts,
each paper in exactly one topic.

**Why it was re-drawn.** The previous taxonomy was 14 topics over 60 papers. A second batch of
57 papers arrived on 2026-09-05 and exposed two specific faults, not a general staleness. First,
Part A ran from MHC binding onward and had nothing upstream of the groove, so nine papers on
proteasomal cleavage, TAP transport and ERAP1 trimming had no home that described them — the
step that decides whether a peptide exists to be bound was missing from a taxonomy about
presentation. Second, seven papers on splicing, indels, noncoding translation and
post-translational protein splicing had no home either: the old taxonomy assumed neoantigens
come from missense mutations, which is what the pipelines assume and what these papers exist to
contradict.

**What proposed and what decided.** Reading decided. Every one of the 117 papers was read and
its four prose sections written before the candidate taxonomy was drawn, and the topics come
from those readings. The similarity vectors proposed nothing here: `make topics` was not run.
The vectors are TF-IDF over the summaries, so they group by shared vocabulary rather than by
subject, and they would have put the infrastructure papers — a nearest-neighbour index, a
sequence search tool — next to whatever else says "search" and "efficient".

**How many moved.** None. Zero of the 60 previously filed papers changed topic; the revision is
an extension, not a re-clustering of the existing collection, and that was a MUST fixed in
advance rather than a happy result. Two topics were renamed to cover what was added:
*Thymic selection and self-discrimination* became *Thymic selection and repertoire
availability*, and *MHC class II presentation* became *MHC class II presentation and CD4
responses*. Four topics are new. The before-and-after measurement is in
`reports/2026-09-05_reclustering_score.txt`, against criteria written in
`eval/reclustering.json` before any candidate existed.

**What changed in the 125-paper extension.** Eight papers were added and one topic
created: *Generative design of epitopes and vaccines*. The batch was dominated by methods that
DESIGN a peptide or construct rather than rank the ones a tumour produced, and the Hu (2026)
review in it makes exactly that distinction the organising one -- discriminative models score a
fixed candidate list, generative ones explore sequence space under constraints. Three papers sit
there: Hu's review, Zhang (2026)'s NEOM, and Yuan (2026)'s EpiMII, which moved out of *MHC class
II presentation* because generating epitopes is what it does. One paper moved in total.

**Which criteria failed.** None failed outright, and two deserve more than a PASS. *Minimum
topic size* passed only through the exception the criterion itself allows: **HLA genotyping
holds 2 papers, below the stated floor of 3**, and is kept because its subject is genuinely
narrow — an escape clause, not a clean result, and the next revision should grow it or fold it
into MHC class I. *Cohesion* was **not measured**: the criteria file states the circularity in
advance, since the vectors that would score within-topic cohesion are built from the same
summaries the clustering was drawn from, so cohesion would measure agreement with the proposer
rather than quality.

**Where the seams are.** Six papers could defensibly sit elsewhere, and are named here rather
than left for a reader to notice. **AlphaFold 3** and **HNSW**, **Faiss**, **MMseqs2** are not
immunology; the first is filed under *TCR specificity and structural recognition* because the
structure-based TCR predictors there inherit its accuracy ceiling, the other three under
*Pipelines and analysis tools* because they are the search infrastructure the sequence and
embedding methods run on. **Jardine (2016)** is an HIV antibody paper, filed under *Thymic
selection and repertoire availability* because what it actually measures is whether a precursor
capable of responding exists in the repertoire — the same question that topic asks for T cells.
**Graber (2025)** is protein–ligand drug design, filed under *Benchmarking, bias and
generalisation* because it is the cleanest demonstration of the train–test leakage this field
has inside it. **McGranahan (2017)** introduces an HLA typing tool but is filed under *Tumour
immune escape*, and **Culka (2026)** is the clearest statement of the generalisation problem but
is filed under *TCR specificity*, both for the reasons given when they were first placed.

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
and `et al.`, never a reconstructed list. Full, verified lists exist for 125 of 125
papers, in `data/bib_cache.json` and searchable in the browser.

## Contents

**A. Antigen presentation** — 26 papers  
  · [Antigen processing and peptide supply](#antigen-processing-and-peptide-supply) (3)  
  · [Predicting proteolysis, trimming and transport](#predicting-proteolysis-trimming-and-transport) (6)  
  · [MHC class I binding and presentation](#mhc-class-i-binding-and-presentation) (10)  
  · [MHC class II presentation and CD4 responses](#mhc-class-ii-presentation-and-cd4-responses) (5)  
  · [HLA genotyping](#hla-genotyping) (2)  

**B. Immunogenicity and T cell recognition** — 30 papers  
  · [Immunogenicity predictors for neoepitopes](#immunogenicity-predictors-for-neoepitopes) (13)  
  · [Peptide features and neoantigen quality](#peptide-features-and-neoantigen-quality) (9)  
  · [TCR specificity and structural recognition](#tcr-specificity-and-structural-recognition) (8)  

**C. Self-discrimination and repertoire limits** — 13 papers  
  · [Thymic selection and repertoire availability](#thymic-selection-and-repertoire-availability) (6)  
  · [Molecular mimicry and off-target toxicity](#molecular-mimicry-and-off-target-toxicity) (4)  
  · [Tumour immune escape](#tumour-immune-escape) (3)  

**D. Discovery and clinical translation** — 27 papers  
  · [Neoantigen sources beyond point mutations](#neoantigen-sources-beyond-point-mutations) (7)  
  · [Finding and measuring neoantigen-reactive T cells](#finding-and-measuring-neoantigen-reactive-t-cells) (4)  
  · [Neoantigen vaccines and clinical responses](#neoantigen-vaccines-and-clinical-responses) (10)  
  · [Immunotherapy response prediction](#immunotherapy-response-prediction) (3)  
  · [Generative design of epitopes and vaccines](#generative-design-of-epitopes-and-vaccines) (3)  

**E. Resources, pipelines and evaluation** — 29 papers  
  · [Databases and reference resources](#databases-and-reference-resources) (10)  
  · [Pipelines and analysis tools](#pipelines-and-analysis-tools) (12)  
  · [Benchmarking, bias and generalisation](#benchmarking-bias-and-generalisation) (7)  

---

# A. Antigen presentation

## Antigen processing and peptide supply

*3 papers.* How a peptide comes to exist at all: proteolysis, transport and the cell biology of presentation. Upstream of every binding prediction, and assumed away by most of them.

### Roche, P. A. et al. (2016). *Microbiology Spectrum.* Antigen Processing and Presentation Mechanisms in Myeloid Cells
[doi:10.1128/microbiolspec.MCHD-0008-2015](https://doi.org/10.1128/microbiolspec.MCHD-0008-2015) · `paper`  
[src](<../raw/Roche(2016) Microbiology Spectrum; Antigen Processing and Presentation Mechanisms in Myeloid Cells.pdf>)

A review of antigen processing and presentation in myeloid cells, particularly dendritic cells: antigen acquisition, proteolysis into fragments, peptide binding to MHC, and surface display of both MHC class I-peptide and class II-peptide complexes.

### Rock, K. L. et al. (2009). *The Journal of Immunology.* Proteases in MHC Class I Presentation and Cross-Presentation
[doi:10.4049/jimmunol.0903399](https://doi.org/10.4049/jimmunol.0903399) · `paper`  
[src](<../raw/Rock(2009) The Journal of Immunology; Proteases in MHC Class I Presentation and Cross-Presentation.pdf>)

A review of the proteases involved in generating MHC class I presented peptides, in both the classical direct pathway and cross-presentation. Cells continuously degrade their proteins into oligopeptide fragments, a fraction of which are transported by TAP into the ER where those of the right length and sequence bind newly synthesised class I molecules.

### Androlewicz, M. J. et al. (1993). *Proceedings of the National Academy of Sciences.* Evidence that transporters associated with antigen processing translocate a major histocompatibility complex class I-binding peptide into the endoplasmic reticulum in an ATP-dependent manner.
[doi:10.1073/pnas.90.19.9130](https://doi.org/10.1073/pnas.90.19.9130) · `paper`  
[src](<../raw/Androlewicz(1993) Proceedings of the National Academy of Sciences; Evidence that transporters associated with antigen processing translocate a major histocompatibility complex class I-binding peptide into the endoplasmic reticulum in an ATP-depen.pdf>)

Using streptolysin-O-permeabilised cells, the authors show that peptide binding to MHC class I is both TAP-dependent and ATP-dependent, and that short 8-10mer peptides known to bind class I compete efficiently for TAP-dependent translocation while longer peptides and an ER signal-sequence peptide do not.

## Predicting proteolysis, trimming and transport

*6 papers.* Computational models of the steps before the groove - proteasomal cleavage, TAP transport, ERAP1 trimming. A peptide that is never cut out or never transported cannot be presented however well it would bind.

### Al-okaily, A. et al. (2024). *Journal of Immunological Methods.* ERAMER: A novel in silico tool for prediction of ERAP1 enzyme trimming
[doi:10.1016/j.jim.2024.113713](https://doi.org/10.1016/j.jim.2024.113713) · `paper`  
[src](<../raw/Al-okaily(2024) Journal of Immunological Methods; ERAMER A novel in silico tool for prediction of ERAP1 enzyme trimming.pdf>)

ERAMER is a prediction model for the trimming performed by ERAP1, the ER-resident aminopeptidase that shortens precursor peptides from the N-terminus to the 8-10 residues a stable MHC-I complex requires. The authors note that although ERAP1 specificities had been reported, no in silico tool existed for the trimming step.

### Li, F. et al. (2023). *Briefings in Bioinformatics.* ProsperousPlus : a one-stop and comprehensive platform for accurate protease-specific substrate cleavage prediction and machine-learning model construction
[doi:10.1093/bib/bbad372](https://doi.org/10.1093/bib/bbad372) · `paper`  
[src](<../raw/Li(2023) Briefings in Bioinformatics; ProsperousPlus a one-stop and comprehensive platform for accurate protease-specific substrate cleavage prediction and machine-learning model construction.pdf>)

ProsperousPlus is a platform that lets users build their own protease-specific substrate cleavage site predictors rather than shipping a fixed model per protease. The rationale is that substrate cleavage data now exist for over 100 protease types and are growing faster than predictors can be published for them.

### Zhang, X. et al. (2023). *Computers in Biology and Medicine.* DeepTAP: An RNN-based method of TAP-binding peptide prediction in the selection of tumor neoantigens
[doi:10.1016/j.compbiomed.2023.107247](https://doi.org/10.1016/j.compbiomed.2023.107247) · `paper`  
[src](<../raw/Zhang(2023) Computers in Biology and Medicine; DeepTAP An RNN-based method of TAP-binding peptide prediction in the selection of tumor neoantigens.pdf>)

DeepTAP uses a bidirectional gated recurrent unit to predict TAP-binding peptides, alongside an analysis of TAP-binding motifs and N- and C-terminal amino acid preferences. It is reported to achieve a better balance of precision and false positives than TAPPred, TAPREG and KSMM.

### Weeder, B. R. et al. (2021). *Bioinformatics.* pepsickle rapidly and accurately predicts proteasomal cleavage sites for improved neoantigen identification
[doi:10.1093/bioinformatics/btab628](https://doi.org/10.1093/bioinformatics/btab628) · `paper`  
[src](<../raw/Weeder(2021) Bioinformatics; pepsickle rapidly and accurately predicts proteasomal cleavage sites for improved neoantigen identification.pdf>)

pepsickle is an open-source proteasomal cleavage predictor with better in vivo AUC and speed than existing models, and the ability to predict from both constitutive and immunoproteasome profiles. Post hoc filtering of predicted patient neoepitopes with it significantly enriches for immune-responsive epitopes.

### Nielsen, M. et al. (2005). *Immunogenetics.* The role of the proteasome in generating cytotoxic T-cell epitopes: insights obtained from improved predictions of proteasomal cleavage
[doi:10.1007/s00251-005-0781-7](https://doi.org/10.1007/s00251-005-0781-7) · `paper`  
[src](<../raw/Nielsen(2005) Immunogenetics; The role of the proteasome in generating cytotoxic T-cell epitopes insights obtained from improved predictions of proteasomal cleavage.pdf>)

An improved NetChop, using novel sequence encoding, predicts about 10% more proteasomal cleavage sites correctly while lowering false positives by close to 15%. The better predictor is then used to study the proteasome's role: estimating the N-terminal extension of epitope precursors, and how often epitopes are destroyed rather than generated.

### Keşmir, C. et al. (2002). *Protein Engineering, Design and Selection.* Prediction of proteasome cleavage motifs by neural networks
[doi:10.1093/protein/15.4.287](https://doi.org/10.1093/protein/15.4.287) · `paper`  
[src](<../raw/Keşmir(2002) Protein Engineering, Design and Selection; Prediction of proteasome cleavage motifs by neural networks.pdf>)

A neural network predicting proteasomal cleavage - the degradation step that generates the fragments capable of binding MHC class I. Unlike earlier algorithms trained on in vitro digestion by constitutive proteasomes, this one accounts for the immunoproteasome, and the authors combine cleavage, TAP transport and MHC binding into a single quality-of-presentation score.

## MHC class I binding and presentation

*10 papers.* Predicting which peptides a class I molecule binds and displays. The best-served task in the field, and the one whose benchmarks are most entangled with their own training data.

### Niu, R. et al. (2024). *Briefings in Bioinformatics.* Attention-aware differential learning for predicting peptide-MHC class I binding and T cell receptor recognition
[doi:10.1093/bib/bbaf038](https://doi.org/10.1093/bib/bbaf038) · `paper`  
[src](<../raw/Niu(2024) Briefings in Bioinformatics; Attention-aware differential learning for predicting peptide-MHC class I binding and T cell receptor recognition.pdf>)

An attention-based framework in two parts: TranspMHC for pMHC-I binding prediction and TransTCR for TCR-pMHC-I recognition, the latter using transfer learning and a differential learning strategy. Both are reported to outperform existing methods on independent datasets, and attention weights identify amino acids associated with peptide and TCR binding motifs.

### Xu, H. et al. (2024). *Nature Communications.* ImmuneApp for HLA-I epitope prediction and immunopeptidome analysis
[doi:10.1038/s41467-024-53296-0](https://doi.org/10.1038/s41467-024-53296-0) · `paper`  
[src](<../raw/Xu(2024) Nature Communications; ImmuneApp for HLA-I epitope prediction and immunopeptidome analysis.pdf>)

ImmuneApp is an interpretable deep learning framework for HLA-I epitope prediction, neoepitope prioritisation and immunopeptidomics deconvolution. Systematic analysis of 216 multi-allelic immunopeptidomics samples identified 835,551 ligands across more than 100 HLA-I alleles; the composite ImmuneApp-MA integrates mono- and multi-allelic data, and ImmuneApp-Neo is built on it as an immunogenicity predictor.

### Zhang, L. et al. (2024). *Briefings in Bioinformatics.* ConvNeXt-MHC: improving MHC–peptide affinity prediction by structure-derived degenerate coding and the ConvNeXt model
[doi:10.1093/bib/bbae133](https://doi.org/10.1093/bib/bbae133) · `paper`  
[src](<../raw/Zhang(2024) Briefings in Bioinformatics; ConvNeXt-MHC improving MHC–peptide affinity prediction by structure-derived degenerate coding and the ConvNeXt model.pdf>)

ConvNeXt-MHC predicts MHC-I peptide binding affinity using a structure-derived degenerate encoding of amino acids combined with transfer and semi-supervised learning in the ConvNeXt architecture. Benchmarks report accuracy above state-of-the-art methods.

### Albert, B. A. et al. (2023). *Nature Machine Intelligence.* Deep neural networks predict class I major histocompatibility complex epitope presentation and transfer learn neoepitope immunogenicity
[doi:10.1038/s42256-023-00694-6](https://doi.org/10.1038/s42256-023-00694-6) · `paper`  
[src](<../raw/Albert(2023) Nature Machine Intelligence; Deep neural networks predict class I major histocompatibility complex epitope presentation and transfer learn neoepitope immunogenicity.pdf>)

BigMHC is an ensemble of seven pan-allelic deep neural networks trained on peptide-MHC eluted ligand mass spectrometry data, then transfer-learned on antigen-specific immune response assays to predict neoepitope immunogenicity. It significantly improves epitope presentation prediction over four state-of-the-art classifiers.

### Qu, W. et al. (2023). *Bioinformatics.* DeepMHCI: an anchor position-aware deep interaction model for accurate MHC-I peptide binding affinity prediction
[doi:10.1093/bioinformatics/btad551](https://doi.org/10.1093/bioinformatics/btad551) · `paper`  
[src](<../raw/Qu(2023) Bioinformatics; DeepMHCI an anchor position-aware deep interaction model for accurate MHC-I peptide binding affinity prediction.pdf>)

DeepMHCI adds a position-wise gated layer and a residual binding-interaction convolution layer so the model is aware of MHC anchor positions and models peptide-MHC interaction directly rather than by concatenating the two sequences. It is validated by five-fold cross-validation, an independent test set, external HPV vaccine identification and external CD8+ epitope identification, with the largest gains on non-9-mer peptides.

### O’Donnell, T. J. et al. (2020). *Cell Systems.* MHCflurry 2.0: Improved Pan-Allele Prediction of MHC Class I-Presented Peptides by Incorporating Antigen Processing
[doi:10.1016/j.cels.2020.06.010](https://doi.org/10.1016/j.cels.2020.06.010) · `paper`  
[src](<../raw/O’Donnell(2020) Cell Systems; MHCflurry 2.0 Improved Pan-Allele Prediction of MHC Class I-Presented Peptides by Incorporating Antigen Processing.pdf>)

MHCflurry 2.0 trains separate predictors for MHC class I binding and for antigen processing, the latter on mass-spectrometry-identified MHC ligands, and combines them into a presentation predictor that outperforms existing methods. It is an open-source Python package with command-line and library interfaces.

### Reynisson, B. et al. (2020). *Nucleic Acids Research.* NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data
[doi:10.1093/nar/gkaa379](https://doi.org/10.1093/nar/gkaa379) · `paper`  
[src](<../raw/Reynisson(2020) Nucleic Acids Research; NetMHCpan-4.1 and NetMHCIIpan-4.0 improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data.pdf>)

NetMHCpan-4.1 and NetMHCIIpan-4.0 integrate binding-affinity data with mass-spectrometry eluted-ligand data in a single training framework, using NNAlign_MA to assign multi-allelic eluted ligands to individual MHC restrictions during training. This both discovers novel motifs and substantially expands the usable training set.

### Sarkizova, S. et al. (2019). *Nature Biotechnology.* A large peptidome dataset improves HLA class I epitope prediction across most of the human population
[doi:10.1038/s41587-019-0322-9](https://doi.org/10.1038/s41587-019-0322-9) · `paper`  
[src](<../raw/Sarkizova(2019) Nature Biotechnology; A large peptidome dataset improves HLA class I epitope prediction across most of the human population.pdf>)

Mass spectrometry profiling of more than 185,000 peptides eluted from 95 HLA-A, -B, -C and -G mono-allelic cell lines produces training data covering a large fraction of the human population. Predictors trained on it achieve 1.5-2.7x improvements in positive predictive value at the top 0.1% of the dataset, corresponding to 3-12x gains at 40% recall.

### Bulik-Sullivan, B. et al. (2018). *Nature Biotechnology.* Deep learning using tumor HLA peptide mass spectrometry datasets improves neoantigen identification
[doi:10.1038/nbt.4313](https://doi.org/10.1038/nbt.4313) · `paper`  
[src](<../raw/Bulik-Sullivan(2018) Nature Biotechnology; Deep learning using tumor HLA peptide mass spectrometry datasets improves neoantigen identification.pdf>)

EDGE applies deep learning to a large HLA peptide and transcriptome dataset from 74 patients to predict neoantigen presentation, improving on binding-affinity prediction. The stated aim is to remove the need for invasive specimens, screening of thousands of synthetic peptides or tandem minigenes, and HLA-allele-restricted multimer reagents.

### Rammensee, H. (1995). *Current Opinion in Immunology.* Chemistry of peptides associated with MHC class I and class II molecules
[doi:10.1016/0952-7915(95)80033-6](https://doi.org/10.1016/0952-7915(95)80033-6) · `paper`  
[src](<../raw/Rammensee(1995) Current Opinion in Immunology; Chemistry of peptides associated with MHC class I and class II molecules.pdf>)

A review setting out that peptides presented by MHC class I and class II follow stringent, allele-specific rules involving a nine-amino-acid stretch spanning the groove, with anchor side chains held in complementary pockets. The sum of these requirements is described as a motif - the number, spacing and specificity of anchors plus degenerate preferences at non-anchor positions.

## MHC class II presentation and CD4 responses

*5 papers.* The same problem for class II, where the groove is open at both ends, the binding core is not fixed by length, and the data are thinner - together with the evidence that CD4 responses matter more than the field long assumed.

### Nilsson, J. B. et al. (2023). *Science Advances.* Accurate prediction of HLA class II antigen presentation across all loci using tailored data acquisition and refined machine learning
[doi:10.1126/sciadv.adj6367](https://doi.org/10.1126/sciadv.adj6367) · `paper`  
[src](<../raw/Nilsson(2023) Science Advances; Accurate prediction of HLA class II antigen presentation across all loci using tailored data acquisition and refined machine learning.pdf>)

NetMHCIIpan-4.3 closes the performance gap between HLA-DR, -DQ and -DP by combining a refined machine learning framework that accommodates inverted peptide binders with targeted immunopeptidomics assays generating new HLA-DP data. The result is high accuracy and molecular coverage across all class II allotypes.

### Racle, J. et al. (2023). *Immunity.* Machine learning predictions of MHC-II specificities reveal alternative binding mode of class II epitopes
[doi:10.1016/j.immuni.2023.03.009](https://doi.org/10.1016/j.immuni.2023.03.009) · `paper`  
[src](<../raw/Racle(2023) Immunity; Machine learning predictions of MHC-II specificities reveal alternative binding mode of class II epitopes.pdf>)

Curating over 600,000 MHC-II ligands and deconvolving motifs yields high-resolution binding motifs for 88 MHC-II alleles. Structural analysis reveals a widespread reverse binding mode for HLA-DP ligands, and MixMHC2pred improves CD4+ T cell epitope prediction.

### Racle, J. et al. (2023). *venue not recorded.* How to predict binding specificity and ligands for new MHC-II alleles with MixMHC2pred
[doi:10.1101/2023.12.18.572125](https://doi.org/10.1101/2023.12.18.572125) · `preprint`  
[src](<../raw/Racle(2023) unknown; How to predict binding specificity and ligands for new MHC-II alleles with MixMHC2pred.pdf>)

A practical guide to using MixMHC2pred to predict the binding specificity of any MHC-II allele directly from its amino acid sequence, and to predict MHC-II ligands and CD4+ T cell epitopes across species. Available as a web server and as precompiled executables.

### You, R. et al. (2022). *Bioinformatics.* DeepMHCII: a novel binding core-aware deep interaction model for accurate MHC-II peptide binding affinity prediction
[doi:10.1093/bioinformatics/btac225](https://doi.org/10.1093/bioinformatics/btac225) · `paper`  
[src](<../raw/You(2022) Bioinformatics; DeepMHCII a novel binding core-aware deep interaction model for accurate MHC-II peptide binding affinity prediction.pdf>)

DeepMHCII adds a binding-interaction convolution layer that integrates all potential binding cores in a peptide with the MHC class II pseudo-sequence through multiple convolutional kernels, rather than concatenating an estimated core with the MHC sequence. It outperforms four state-of-the-art methods across four large datasets under cross-validation, leave-one-molecule-out, independent test sets and binding-core prediction.

### Kreiter, S. et al. (2015). *Nature.* Mutant MHC class II epitopes drive therapeutic immune responses to cancer
[doi:10.1038/nature14426](https://doi.org/10.1038/nature14426) · `paper`  
[src](<../raw/Kreiter(2015) Nature; Mutant MHC class II epitopes drive therapeutic immune responses to cancer.pdf>)

Across three mouse tumour models with different MHC backgrounds, a considerable fraction of non-synonymous cancer mutations is immunogenic, and the immunogenic mutanome is predominantly recognised by CD4+ T cells. RNA vaccination with a single class II epitope, B16-M30, profoundly retarded B16F10 tumour growth, with efficacy depending on CD4+ and not CD8+ T cells.

## HLA genotyping

*2 papers.* Calling a patient's HLA alleles from sequencing data. A deliberately narrow topic of two method papers: it is one step, it is nearly solved, and every downstream prediction is conditioned on it being right.

### Orenbuch, R. et al. (2019). *Bioinformatics.* arcasHLA: high-resolution HLA typing from RNAseq
[doi:10.1093/bioinformatics/btz474](https://doi.org/10.1093/bioinformatics/btz474) · `paper`  
[src](<../raw/Orenbuch(2019) Bioinformatics; arcasHLA high-resolution HLA typing from RNAseq.pdf>)

arcasHLA infers HLA genotypes from RNA-sequencing data, reporting 100% accuracy at two-field resolution for class I and over 99.7% for class II on the gold-standard benchmark, faster than established tools. It is further evaluated on 447 single-end total RNA samples from nasopharyngeal swabs to establish applicability to metatranscriptomes.

### Szolek, A. et al. (2014). *Bioinformatics.* OptiType: precision HLA typing from next-generation sequencing data
[doi:10.1093/bioinformatics/btu548](https://doi.org/10.1093/bioinformatics/btu548) · `paper`  
[src](<../raw/Szolek(2014) Bioinformatics; OptiType precision HLA typing from next-generation sequencing data.pdf>)

OptiType genotypes HLA from NGS data using integer linear programming, without requiring HLA-specific enrichment. Benchmarked on a purpose-built dataset spanning RNA, exome and whole-genome sequencing, it reports 97% overall accuracy, significantly better than previous in silico approaches.


# B. Immunogenicity and T cell recognition

## Immunogenicity predictors for neoepitopes

*13 papers.* Models that go past presentation to ask which presented peptides a T cell responds to - the step where most predicted candidates are lost, and where the training labels are weakest.

### Liu, G. et al. (2026). *Global Health Care.* Using multimodal foundational models to predict neoantigen immunogenicity and vaccine effectiveness across different tumor types
[doi:10.63808/ghc.v2i3.498](https://doi.org/10.63808/ghc.v2i3.498) · `paper`  
[src](<../raw/Liu(2026) Global Health Care; Using multimodal foundational models to predict neoantigen immunogenicity and vaccine effectiveness across different tumor types.pdf>)

_NOT YET WRITTEN._ This section is read off the paper by a person; `scripts/ingest_inbox.py` does not invent it. `status: prose-pending` in the frontmatter says so, and `make audit` reports it.

### Farriol-Duran, R. et al. (2025). *Genome Medicine.* PredIG: an interpretable predictor of T-cell epitope immunogenicity
[doi:10.1186/s13073-025-01569-8](https://doi.org/10.1186/s13073-025-01569-8) · `paper`  
[src](<../raw/Farriol-Duran(2025) Genome Medicine; PredIG an interpretable predictor of T-cell epitope immunogenicity.pdf>)

PredIG predicts T-cell epitope immunogenicity from 17,448 peptide-HLA-I pairs with reported immunogenicity, combining in silico antigen-processing features (proteasomal cleavage, TAP translocation, binding affinity, presentation) with physicochemical descriptors focused on TCR-facing positions. Three antigen-specific XGBoost models cover neoantigens, non-canonical antigens and pathogens, and SHAP analysis is used to make the predictions interpretable.

### Kim, J. Y. et al. (2025). *Science Advances.* B cell–reactive neoantigens boost antitumor immunity
[doi:10.1126/sciadv.adx8303](https://doi.org/10.1126/sciadv.adx8303) · `paper`  
[src](<../raw/Kim(2025) Science Advances; B cell–reactive neoantigens boost antitumor immunity.pdf>)

_NOT YET WRITTEN._ This section is read off the paper by a person; `scripts/ingest_inbox.py` does not invent it. `status: prose-pending` in the frontmatter says so, and `make audit` reports it.

### Shao, Y. et al. (2025). *Frontiers in Immunology.* NeoTImmuML: a machine learning-based prediction model for human tumor neoantigen immunogenicity
[doi:10.3389/fimmu.2025.1681396](https://doi.org/10.3389/fimmu.2025.1681396) · `paper`  
[src](<../raw/Shao(2025) Frontiers in Immunology; NeoTImmuML a machine learning-based prediction model for human tumor neoantigen immunogenicity.pdf>)

NeoTImmuML is a weighted ensemble of LightGBM, XGBoost and Random Forest trained on physicochemical peptide features computed from TumorAgDB2.0, a consolidated tumour antigen database built by the same authors. Eight algorithms were compared by five-fold cross-validation, SHAP was used for interpretability, and the ensemble outperformed single models on an external dataset.

### Jiang, D. et al. (2024). *Bioinformatics.* NeoaPred: a deep-learning framework for predicting immunogenic neoantigen based on surface and structural features of peptide–human leukocyte antigen complexes
[doi:10.1093/bioinformatics/btae547](https://doi.org/10.1093/bioinformatics/btae547) · `paper`  
[src](<../raw/Jiang(2024) Bioinformatics; NeoaPred a deep-learning framework for predicting immunogenic neoantigen based on surface and structural features of peptide–human leukocyte antigen complexes.pdf>)

NeoaPred builds pHLA-I complex structures (82.37% within 1 Å RMSD) and derives a foreignness score from differences in surface, structural and atom-group features between the mutant peptide and its wild-type counterpart. It reports AUROC 0.81 and AUPRC 0.54 on the test set, above the methods compared.

### O’Brien, H. et al. (2024). *PLOS Computational Biology.* A modular protein language modelling approach to immunogenicity prediction
[doi:10.1371/journal.pcbi.1012511](https://doi.org/10.1371/journal.pcbi.1012511) · `paper`  
[src](<../raw/O’Brien(2024) PLOS Computational Biology; A modular protein language modelling approach to immunogenicity prediction.pdf>)

ImmugenX is a modular protein language modelling approach to CD8+ neoantigen immunogenicity prediction, built for a setting where reactivity rates among called neoantigens are low and training data correspondingly limited. Data are drawn from public sources including VDJdb, CEDAR and McPas-TCR.

### Wan, Y. R. et al. (2024). *NAR Cancer.* A large-scale study of peptide features defining immunogenicity of cancer neo-epitopes
[doi:10.1093/narcan/zcae002](https://doi.org/10.1093/narcan/zcae002) · `paper`  
[src](<../raw/Wan(2024) NAR Cancer; A large-scale study of peptide features defining immunogenicity of cancer neo-epitopes.pdf>)

A comprehensive analysis of peptide features for neo-epitope immunogenicity using CEDAR's experimentally validated annotations, yielding ICERFIRE. The model extracts the predicted ICORE - the nested peptide with the highest MHC binding potential together with its presentation %Rank - and adds the BLOSUM mutation score and wild-type antigen expression level, outperforming existing models in cross-validation and on external data.

### Deng, J. et al. (2023). *Briefings in Bioinformatics.* IEPAPI: a method for immune epitope prediction by incorporating antigen presentation and immunogenicity
[doi:10.1093/bib/bbad171](https://doi.org/10.1093/bib/bbad171) · `paper`  
[src](<../raw/Deng(2023) Briefings in Bioinformatics; IEPAPI a method for immune epitope prediction by incorporating antigen presentation and immunogenicity.pdf>)

IEPAPI uses transformer-based feature extraction for peptides and HLA-I proteins, then feeds the antigen presentation prediction into the input of the immunogenicity branch, explicitly modelling the sequence of biological steps in a T-cell response. It also reveals HLA-restricted motifs for presentation and immunogenicity separately.

### Gfeller, D. et al. (2023). *Cell Systems.* Improved predictions of antigen presentation and TCR recognition with MixMHCpred2.2 and PRIME2.0 reveal potent SARS-CoV-2 CD8+ T-cell epitopes
[doi:10.1016/j.cels.2022.12.002](https://doi.org/10.1016/j.cels.2022.12.002) · `paper`  
[src](<../raw/Gfeller(2023) Cell Systems; Improved predictions of antigen presentation and TCR recognition with MixMHCpred2.2 and PRIME2.0 reveal potent SARS-CoV-2 CD8+ T-cell epitopes.pdf>)

Large curated datasets of HLA-I ligands and neo-epitopes are used to train two tools: MixMHCpred2.2 for antigen presentation and PRIME2.0 for TCR recognition. Applied to SARS-CoV-2, they identify potent CD8+ T-cell epitopes, several cross-reactive with other coronaviruses.

### Li, G. et al. (2021). *Briefings in Bioinformatics.* DeepImmuno: deep learning-empowered prediction and generation of immunogenic peptides for T-cell immunity
[doi:10.1093/bib/bbab160](https://doi.org/10.1093/bib/bbab160) · `paper`  
[src](<../raw/Li(2021) Briefings in Bioinformatics; DeepImmuno deep learning-empowered prediction and generation of immunogenic peptides for T-cell immunity.pdf>)

DeepImmuno derives peptide immunogenic potential from sequence using a beta-binomial model to produce a continuous score, benchmarked across five classical machine learning and three deep learning architectures on dengue, cancer neoantigen and SARS-CoV-2 validation sets. A CNN was selected; a companion GAN generates synthetic immunogenic peptides for given HLA alleles.

### Schmidt, J. et al. (2021). *Cell Reports Medicine.* Prediction of neo-epitope immunogenicity reveals TCR recognition determinants and provides insight into immunoediting
[doi:10.1016/j.xcrm.2021.100194](https://doi.org/10.1016/j.xcrm.2021.100194) · `paper`  
[src](<../raw/Schmidt(2021) Cell Reports Medicine; Prediction of neo-epitope immunogenicity reveals TCR recognition determinants and provides insight into immunoediting.pdf>)

PRIME predicts immunogenic CD8+ T cell epitopes by combining HLA presentation with a learnt model of TCR recognition, improving accuracy on neoepitopes over presentation-only predictors. The learnt determinants of TCR recognition are then used to argue that immunoediting acts on recurrent cancer mutations.

### Bhasin, M. et al. (2004). *Vaccine.* Prediction of CTL epitopes using QM, SVM and ANN techniques
[doi:10.1016/j.vaccine.2004.02.005](https://doi.org/10.1016/j.vaccine.2004.02.005) · `paper`  
[src](<../raw/Bhasin(2004) Vaccine; Prediction of CTL epitopes using QM, SVM and ANN techniques.pdf>)

A direct CTL epitope predictor built from quantitative matrices, support vector machines and neural networks, trained on a non-redundant set including 1,137 experimentally proven MHC class I restricted T cell epitopes. Accuracies were 70.0% (QM), 72.2% (ANN) and 75.2% (SVM), with machine learning ahead of the matrix method on a blind set.

### Zhao, Y. et al. (2003). *Bioinformatics.* Application of support vector machines for T-cell epitopes prediction
[doi:10.1093/bioinformatics/btg255](https://doi.org/10.1093/bioinformatics/btg255) · `paper`  
[src](<../raw/Zhao(2003) Bioinformatics; Application of support vector machines for T-cell epitopes prediction.pdf>)

The first application of support vector machines to T-cell epitope prediction, trained on an MHC class I restricted T-cell clone. Cross-validation shows SVMs can be trained on relatively small datasets to give predictions more accurate than previously published methods or than MHC binding alone.

## Peptide features and neoantigen quality

*9 papers.* What makes one neoepitope more visible than another: TCR-facing composition, novelty against the wild type and against the whole self proteome, and quality models that combine recognition with discrimination from self.

### Zhu, J. et al. (2025). *Communications Biology.* Structure guided analysis of KRAS G12 mutants in HLA-A*11:01 reveals a length encoded immunogenic advantage in G12D
[doi:10.1038/s42003-025-09285-0](https://doi.org/10.1038/s42003-025-09285-0) · `paper`  
[src](<../raw/Zhu(2025) Communications Biology; Structure guided analysis of KRAS G12 mutants in HLA-A 1101 reveals a length encoded immunogenic advantage in G12D.pdf>)

Structural, biophysical and functional analysis of KRAS G12 variants presented by HLA-A*11:01 shows that single substitutions at position 12 induce distinct conformational changes in the MHC groove, with G12D uniquely destabilising the complex through a buried aspartate. G12D peptides adopt both 9-mer and 10-mer registers that differ sharply in structure and immunogenicity.

### Łuksza, M. et al. (2022). *Nature.* Neoantigen quality predicts immunoediting in survivors of pancreatic cancer
[doi:10.1038/s41586-022-04735-9](https://doi.org/10.1038/s41586-022-04735-9) · `paper`  
[src](<../raw/Łuksza(2022) Nature; Neoantigen quality predicts immunoediting in survivors of pancreatic cancer.pdf>)

Neoantigen quality is defined as Q = R x D, combining the probability that a neoantigen is recognised as non-self with the probability it is discriminated from its wild-type counterpart. Cross-reactivity of three TCRs across every single-amino-acid substitution of a model HLA-A*02:01 epitope is used to parameterise discrimination, and the resulting quality measure predicts immunoediting in long-term pancreatic cancer survivors.

### Devlin, J. R. et al. (2020). *Nature Chemical Biology.* Structural dissimilarity from self drives neoepitope escape from immune tolerance
[doi:10.1038/s41589-020-0610-1](https://doi.org/10.1038/s41589-020-0610-1) · `paper`  
[src](<../raw/Devlin(2020) Nature Chemical Biology; Structural dissimilarity from self drives neoepitope escape from immune tolerance.pdf>)

A point mutation at a non-MHC-anchor position in an immunologically active ovarian cancer neoepitope induces structural and dynamic changes that pre-organise the peptide into the conformation optimal for its cognate TCR, allowing high-affinity binding and potent signalling. Immunogenicity here comes from structural and physical dissimilarity to self, not from changed MHC binding.

### Richman, L. P. et al. (2019). *Cell Systems.* Neoantigen Dissimilarity to the Self-Proteome Predicts Immunogenicity and Response to Immune Checkpoint Blockade
[doi:10.1016/j.cels.2019.08.009](https://doi.org/10.1016/j.cels.2019.08.009) · `paper`  
[src](<../raw/Richman(2019) Cell Systems; Neoantigen Dissimilarity to the Self-Proteome Predicts Immunogenicity and Response to Immune Checkpoint Blockade.pdf>)

Dissimilarity of a neoantigen to the non-mutated proteome is identified as a predictor of peptide immunogenicity. Implemented in the antigen.garnish R package, dissimilarity identifies a distinct set of high-quality neoantigens that correlates with survival in clinical checkpoint blockade datasets.

### Wood, M. A. et al. (2018). *BMC Cancer.* Population-level distribution and putative immunogenicity of cancer neoepitopes
[doi:10.1186/s12885-018-4325-6](https://doi.org/10.1186/s12885-018-4325-6) · `paper`  
[src](<../raw/Wood(2018) BMC Cancer; Population-level distribution and putative immunogenicity of cancer neoepitopes.pdf>)

Four peptide novelty metrics are proposed to refine neoantigen prediction - tumour versus paired normal binding affinity difference, tumour versus paired normal sequence similarity, tumour versus closest human peptide similarity, and tumour versus closest microbial peptide similarity - and applied across TCGA, a melanoma cohort, and peptides with neoepitope-specific immune response data.

### PancreaticCancerGenomeInitiative et al. (2017). *Nature.* Identification of unique neoantigen qualities in long-term survivors of pancreatic cancer
[doi:10.1038/nature24462](https://doi.org/10.1038/nature24462) · `paper`  
[src](<../raw/PancreaticCancerGenomeInitiative(2017) Nature; Identification of unique neoantigen qualities in long-term survivors of pancreatic cancer.pdf>)

Comparing long-term pancreatic cancer survivors (median survival 6 years, n=82) with short-term survivors (median 0.8 years, n=68), the authors find that survival is associated not with neoantigen quantity but with neoantigen quality, and identify MUC16 as a candidate immunogenic hotspot.

### Łuksza, M. et al. (2017). *Nature.* A neoantigen fitness model predicts tumour response to checkpoint blockade immunotherapy
[doi:10.1038/nature24473](https://doi.org/10.1038/nature24473) · `paper`  
[src](<../raw/Łuksza(2017) Nature; A neoantigen fitness model predicts tumour response to checkpoint blockade immunotherapy.pdf>)

A fitness model for tumours based on immune interactions of neoantigens, predicting response to checkpoint blockade. Neoantigen fitness has two components: likelihood of MHC presentation, estimated from binding affinity relative to the wild-type peptide, and T cell recognition, estimated from a nonlinear dependence on sequence similarity to known antigens.

### Chowell, D. et al. (2015). *Proceedings of the National Academy of Sciences.* TCR contact residue hydrophobicity is a hallmark of immunogenic CD8 + T cell epitopes
[doi:10.1073/pnas.1500973112](https://doi.org/10.1073/pnas.1500973112) · `paper`  
[src](<../raw/Chowell(2015) Proceedings of the National Academy of Sciences; TCR contact residue hydrophobicity is a hallmark of immunogenic CD8 + T cell epitopes.pdf>)

Interrogating the biochemical properties of 9,888 MHC class I peptides, the authors find a strong bias toward hydrophobic amino acids specifically at TCR contact residues of immunogenic epitopes. They train a hydrophobicity-based neural network (ANN-Hydro) on this signal and validate it blind on 364 peptides from three HIV-1 Gag variants in vivo.

### Calis, J. J. A. et al. (2013). *PLoS Computational Biology.* Properties of MHC Class I Presented Peptides That Enhance Immunogenicity
[doi:10.1371/journal.pcbi.1003266](https://doi.org/10.1371/journal.pcbi.1003266) · `paper`  
[src](<../raw/Calis(2013) PLoS Computational Biology; Properties of MHC Class I Presented Peptides That Enhance Immunogenicity.pdf>)

By assembling a large dataset of immunogenicity measurements for peptides presented on various MHC-I molecules, the authors identify two determinants: positions P4-P6 of the presented peptide matter most, and large aromatic side chains are associated with immunogenicity. These are combined into a simple, published model validated on two independent epitope discovery studies.

## TCR specificity and structural recognition

*8 papers.* Predicting or measuring which receptor sees which peptide-MHC, by sequence model, by structure, or by direct affinity measurement. Generalisation to unseen peptides is still unsolved.

### Culka, M. et al. (2026). *Cell Systems.* Predicting specificity of TCR-pMHC interactions using machine-learning and biophysical models
[doi:10.1016/j.cels.2026.101700](https://doi.org/10.1016/j.cels.2026.101700) · `paper`  
[src](<../raw/Culka(2026) Cell Systems; Predicting specificity of TCR-pMHC interactions using machine-learning and biophysical models.pdf>)

Using a proprietary cancer-patient dataset that profiles TCR binding in previously unexplored regions of peptide space, the authors show that machine-learning TCR specificity models fail to generalise to novel peptides, while physics-based methods using classical energy functions do better on novel peptides and worse on known ones. They then build a model on protein foundation-model representations that matches or beats both, in and out of distribution.

### Abramson, J. et al. (2024). *Nature.* Accurate structure prediction of biomolecular interactions with AlphaFold 3
[doi:10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) · `paper`  
[src](<../raw/Abramson(2024) Nature; Accurate structure prediction of biomolecular interactions with AlphaFold 3.pdf>)

AlphaFold 3 replaces the AlphaFold 2 architecture with a diffusion-based one that predicts the joint structure of complexes containing proteins, nucleic acids, small molecules, ions and modified residues in a single unified framework. It reports substantially higher accuracy than specialised tools for protein-ligand docking, protein-nucleic acid complexes and antibody-antigen prediction.

### Jensen, M. F. et al. (2024). *eLife.* Enhancing TCR specificity predictions by combined pan- and peptide-specific training, loss-scaling, and sequence similarity integration
[doi:10.7554/elife.93934](https://doi.org/10.7554/elife.93934) · `paper`  
[src](<../raw/Jensen(2024) eLife; Enhancing TCR specificity predictions by combined pan- and peptide-specific training, loss-scaling, and sequence similarity integration.pdf>)

NetTCR 2.2 explores architectures and training strategies for TCR specificity prediction on a larger paired-chain dataset, addressing the imbalance caused by a handful of well-studied epitopes dominating available data. Combining pan-specific and peptide-specific modelling, loss-scaling, outlier removal and similarity-based predictions yields acceptable accuracy for peptides with as few as 15 positive TCRs, and state-of-the-art performance on the IMMREP 2022 benchmark.

### Bradley, P. (2023). *eLife.* Structure-based prediction of T cell receptor:peptide-MHC interactions
[doi:10.7554/eLife.82813](https://doi.org/10.7554/eLife.82813) · `paper`  
[src](<../raw/Bradley(2023) eLife; Structure-based prediction of T cell receptorpeptide-MHC interactions.pdf>)

A specialised, template-guided version of AlphaFold is used to model TCR:peptide-MHC complexes, and the resulting models discriminate correct from incorrect peptide epitopes with substantial accuracy. The paper argues that structural modelling is a viable route to generalisable TCR specificity prediction in a regime where training data are scarce.

### Bravi, B. et al. (2023). *eLife.* A transfer-learning approach to predict antigen immunogenicity and T-cell receptor specificity
[doi:10.7554/eLife.85126](https://doi.org/10.7554/eLife.85126) · `paper`  
[src](<../raw/Bravi(2023) eLife; A transfer-learning approach to predict antigen immunogenicity and T-cell receptor specificity.pdf>)

diffRBM applies transfer learning to Restricted Boltzmann Machines to model two properties separately: what makes an antigen immunogenic, and what makes a TCR specific for a given antigen. The learnt patterns predict putative contact sites of the antigen-receptor complex and discriminate immunogenic from non-immunogenic antigens at performance comparable to existing sequence-based predictors.

### Schmidt, J. et al. (2023). *Nature Communications.* Neoantigen-specific CD8 T cells with high structural avidity preferentially reside in and eliminate tumors
[doi:10.1038/s41467-023-38946-z](https://doi.org/10.1038/s41467-023-38946-z) · `paper`  
[src](<../raw/Schmidt(2023) Nature Communications; Neoantigen-specific CD8 T cells with high structural avidity preferentially reside in and eliminate tumors.pdf>)

Functional (antigen sensitivity) and structural (monomeric pMHC-TCR off-rate) avidities were measured for 371 CD8 T cell clones specific for neoantigens, tumour-associated antigens or viral antigens, from tumours and blood of patients and healthy donors. T cells from tumours show stronger avidity on both measures than their blood counterparts, and high structural avidity tracks with tumour residence and killing.

### Moris, P. et al. (2020). *Briefings in Bioinformatics.* Current challenges for unseen-epitope TCR interaction prediction and a new perspective derived from image classification
[doi:10.1093/bib/bbaa318](https://doi.org/10.1093/bib/bbaa318) · `paper`  
[src](<../raw/Moris(2020) Briefings in Bioinformatics; Current challenges for unseen-epitope TCR interaction prediction and a new perspective derived from image classification.pdf>)

An examination of why generic TCR-epitope recognition prediction remains unsolved, focusing on validation strategies that distinguish performance on seen from unseen epitopes. It introduces ImRex, which represents a TCR-epitope pair as an interaction map of pairwise physicochemical properties for a convolutional network, and catalogues data problems specific to this task.

### Almagro, J. C. et al. (1995). *Protein Science.* Molecular modeling of a T-cell receptor bound to a major histocompatibility complex molecule: Implications for T-cell recognition
[doi:10.1002/pro.5560040906](https://doi.org/10.1002/pro.5560040906) · `paper`  
[src](<../raw/Almagro(1995) Protein Science; Molecular modeling of a T-cell receptor bound to a major histocompatibility complex molecule Implications for T-cell recognition.pdf>)

Before any TCR:peptide:MHC crystal structure existed, this paper built a computational 3D model of the 5C.C7 TCR bound to moth cytochrome c peptide 93-103 presented by I-Ek. The modelled complex shows high surface complementarity, and the residues it places at the interface agree with the mutational data available at the time.


# C. Self-discrimination and repertoire limits

## Thymic selection and repertoire availability

*6 papers.* Whether a T cell capable of seeing a given peptide exists at all. Selection shapes the repertoire before it meets a tumour, and both too much and too little similarity to self remove the responding clones.

### Finnigan, J. P. et al. (2024). *Nature Communications.* Structural basis for self-discrimination by neoantigen-specific TCRs
[doi:10.1038/s41467-024-46367-9](https://doi.org/10.1038/s41467-024-46367-9) · `paper`  
[src](<../raw/Finnigan(2024) Nature Communications; Structural basis for self-discrimination by neoantigen-specific TCRs.pdf>)

A multi-level cellular, molecular and structural analysis of one model neoantigen from B16F10 murine melanoma - H2-Db/Hsf2 p.K72N 68-76 - and its cognate TCR 47BE7. The p.K72N mutation improves H2-Db binding and thereby surface presentation, stabilising the epitope, and the TCR shows high functional avidity with a broad, stringent binding footprint that explains its selectivity for mutant over wild-type.

### Li, L. et al. (2023). *Nature Communications.* Crystal structures of MHC class I complexes reveal the elusive intermediate conformations explored during peptide editing
[doi:10.1038/s41467-023-40736-6](https://doi.org/10.1038/s41467-023-40736-6) · `paper`  
[src](<../raw/Li(2023) Nature Communications; Crystal structures of MHC class I complexes reveal the elusive intermediate conformations explored during peptide editing.pdf>)

X-ray crystal structures of HLA-B8 loaded with 20mer peptides show pronounced distortion at the N-terminus of the binding groove, with long stretches of N-terminal residues missing from electron density, creating an open-ended groove. Molecular dynamics simulations show conformational flexibility consistent with the structures, capturing intermediates of peptide editing that had previously been inferred but not observed.

### Koncz, B. et al. (2021). *Proceedings of the National Academy of Sciences.* Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself
[doi:10.1073/pnas.2100542118](https://doi.org/10.1073/pnas.2100542118) · `paper`  
[src](<../raw/Koncz(2021) Proceedings of the National Academy of Sciences; Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself.pdf>)

Positive selection in the thymus keeps only T cells that recognise human peptides on cortical thymic epithelial cells (cTECs). The authors argue this leaves the repertoire systematically blind: TCR-contact motifs rare or absent in the human proteome, or absent from cTEC expression, are unlikely to be recognised at all.

### Jardine, J. G. et al. (2016). *Science.* HIV-1 broadly neutralizing antibody precursor B cells revealed by germline-targeting immunogen
[doi:10.1126/science.aad9195](https://doi.org/10.1126/science.aad9195) · `paper`  
[src](<../raw/Jardine(2016) Science; HIV-1 broadly neutralizing antibody precursor B cells revealed by germline-targeting immunogen.pdf>)

A germline-targeting immunogen, eOD-GT8, is used with human B cell probing to detect naive B cell precursors of VRC01-class broadly neutralising antibodies against HIV-1. Correcting for sorting and PCR losses, the precursor frequency is calculated as roughly 1 in 400,000 naive B cells.

### Nelson, R. W. et al. (2015). *Immunity.* T Cell Receptor Cross-Reactivity between Similar Foreign and Self Peptides Influences Naive Cell Population Size and Autoimmunity
[doi:10.1016/j.immuni.2014.12.022](https://doi.org/10.1016/j.immuni.2014.12.022) · `paper`  
[src](<../raw/Nelson(2015) Immunity; T Cell Receptor Cross-Reactivity between Similar Foreign and Self Peptides Influences Naive Cell Population Size and Autoimmunity.pdf>)

MHC class II-bound nonamer peptides need share only five residues to bind the same TCR. A self peptide can therefore delete T cells specific for a similar foreign peptide, making some naive T cell populations small, and a foreign peptide can provoke autoimmunity against a similar self peptide that was previously ignored.

### Xing, Y. et al. (2013). *Proceedings of the National Academy of Sciences.* Thymoproteasome subunit-β5T generates peptide-MHC complexes specialized for positive selection
[doi:10.1073/pnas.1222244110](https://doi.org/10.1073/pnas.1222244110) · `paper`  
[src](<../raw/Xing(2013) Proceedings of the National Academy of Sciences; Thymoproteasome subunit-β5T generates peptide-MHC complexes specialized for positive selection.pdf>)

The thymoproteasome subunit beta5T, expressed only in cortical thymic epithelial cells, generates a distinct set of peptide-MHC class I complexes specialised for positive selection of CD8 T cells. The peptides produced differ from those generated by the standard and immuno-proteasomes found elsewhere.

## Molecular mimicry and off-target toxicity

*4 papers.* Cross-reactivity as a hazard: engineered receptors that killed the wrong tissue, and self antigens with counterparts in viruses and the microbiome.

### Ben Hamza, A. et al. (2024). *Blood.* Virus-reactive T cells expanded in aplastic anemia eliminate hematopoietic progenitor cells by molecular mimicry
[doi:10.1182/blood.2023023142](https://doi.org/10.1182/blood.2023023142) · `paper`  
[src](<../raw/BenHamza(2024) Blood; Virus-reactive T cells expanded in aplastic anemia eliminate hematopoietic progenitor cells by molecular mimicry.pdf>)

In 15 patients with acquired aplastic anaemia, single-cell sequencing and immunophenotyping showed oligoclonal expansion and effector differentiation of bone marrow CD8+ T cells. Re-expressing 28 dominant TCRs from 9 patients identified specificities for persistent viral antigens, and those same TCRs killed autologous haematopoietic progenitor cells through molecular mimicry.

### Ragone, C. et al. (2022). *Journal of Translational Medicine.* Molecular mimicry between tumor associated antigens and microbiota-derived epitopes
[doi:10.1186/s12967-022-03512-6](https://doi.org/10.1186/s12967-022-03512-6) · `paper`  
[src](<../raw/Ragone(2022) Journal of Translational Medicine; Molecular mimicry between tumor associated antigens and microbiota-derived epitopes.pdf>)

A BLAST-plus-bioinformatics search for homology between published tumour-associated antigens and microbiota-derived epitopes finds numerous homologous pairs, including three at 100% sequence identity. Predicted HLA affinity of the microbiota-derived antigens is high (< 100 nM), and structural conformation - including TCR-facing residue geometry - is in some cases indistinguishable from the paired TAA.

### Raman, M. C. C. et al. (2016). *Scientific Reports.* Direct molecular mimicry enables off-target cardiovascular toxicity by an enhanced affinity TCR designed for cancer immunotherapy
[doi:10.1038/srep18851](https://doi.org/10.1038/srep18851) · `paper`  
[src](<../raw/Raman(2016) Scientific Reports; Direct molecular mimicry enables off-target cardiovascular toxicity by an enhanced affinity TCR designed for cancer immunotherapy.pdf>)

Structural investigation of why a MAGE-A3-specific affinity-enhanced TCR cross-recognised an unrelated Titin epitope presented on cardiac tissue, causing fatal cardiac toxicity in a clinical trial. The authors resolve the mechanism as direct molecular mimicry and use it to design mutants with improved antigen discrimination.

### Cameron, B. J. et al. (2013). *Science Translational Medicine.* Identification of a Titin-Derived HLA-A1–Presented Peptide as a Cross-Reactive Target for Engineered MAGE A3–Directed T Cells
[doi:10.1126/scitranslmed.3006034](https://doi.org/10.1126/scitranslmed.3006034) · `paper`  
[src](<../raw/Cameron(2013) Science Translational Medicine; Identification of a Titin-Derived HLA-A1–Presented Peptide as a Cross-Reactive Target for Engineered MAGE A3–Directed T Cells.pdf>)

An affinity-enhanced TCR against the HLA-A*01-restricted MAGE-A3 peptide EVDPIGHLY passed extensive preclinical off-target testing, then caused a serious adverse event and fatal cardiac toxicity in patients. The cross-reactive target is identified here as a Titin-derived peptide presented on cardiac tissue.

## Tumour immune escape

*3 papers.* What tumours do to stop being seen - losing an HLA allele, downregulating class I, recruiting suppressive T cells - and why a correct prediction can still fail in a patient.

### Sultan, H. et al. (2024). *Nature.* Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy
[doi:10.1038/s41586-024-07752-y](https://doi.org/10.1038/s41586-024-07752-y) · `paper`  
[src](<../raw/Sultan(2024) Nature; Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy.pdf>)

Using vaccines combining MHC-I neoantigens with varying doses of tumour-derived MHC-II neoantigens, the authors find that low doses of class II peptides promote tumour rejection while high doses of the same peptides inhibit it. The inhibitory cells induced at high dose are type 1 regulatory (Tr1) CD4 T cells, which are cytotoxic and neoantigen-specific.

### Taylor, B. C. et al. (2022). *Frontiers in Immunology.* Mechanisms of MHC-I Downregulation and Role in Immunotherapy Response
[doi:10.3389/fimmu.2022.844866](https://doi.org/10.3389/fimmu.2022.844866) · `paper`  
[src](<../raw/Taylor(2022) Frontiers in Immunology; Mechanisms of MHC-I Downregulation and Role in Immunotherapy Response.pdf>)

A mini-review of the mechanisms by which tumours downregulate MHC class I - transcriptional, post-transcriptional, genetic loss and pathway disruption - and how this contributes to intrinsic and acquired resistance to immune checkpoint inhibition. Therapeutic strategies for restoring surface MHC-I, including interferon-mediated upregulation, are surveyed.

### McGranahan, N. et al. (2017). *Cell.* Allele-Specific HLA Loss and Immune Escape in Lung Cancer Evolution
[doi:10.1016/j.cell.2017.10.001](https://doi.org/10.1016/j.cell.2017.10.001) · `paper`  
[src](<../raw/McGranahan(2017) Cell; Allele-Specific HLA Loss and Immune Escape in Lung Cancer Evolution.pdf>)

LOHHLA, a tool for estimating allele-specific HLA copy number from sequencing data, is applied to 327 tumour and 100 matched normal exomes from 100 TRACERx NSCLC patients. Loss of heterozygosity at the HLA locus occurs in 40% of early-stage non-small-cell lung cancers, is associated with elevated subclonal neoantigen burden and immune activity, and is under strong selection.


# D. Discovery and clinical translation

## Neoantigen sources beyond point mutations

*7 papers.* Where else a tumour-specific peptide can come from: splicing, indels and frameshifts, noncoding and noncanonical translation, and post-translational splicing. Window-based pipelines over missense variants cannot represent most of these.

### Ma, Y. et al. (2026). *npj Precision Oncology.* Inferring translational efficiency from transcriptomes improves noncanonical neoantigen prioritization and cancer patient stratification
[doi:10.1038/s41698-026-01567-y](https://doi.org/10.1038/s41698-026-01567-y) · `paper`  
[src](<../raw/Ma(2026) npj Precision Oncology; Inferring translational efficiency from transcriptomes improves noncanonical neoantigen prioritization and cancer patient stratification.pdf>)

A framework evaluating inferred translational profiles across 15 independent datasets shows they outperform conventional RNA-seq proxies at recapitulating ribosome occupancy, and reveal lncRNA translational potential. Integrated into a translation-aware neoantigen pipeline, this identifies high-confidence noncanonical neoantigens missed by expression-based filtering, and corrects high-risk misclassification in glioma stratification.

### Xing, X. et al. (2026). *JHEP Reports.* Mass spectrometry-based de novo sequencing reveals non-canonical neoantigens with antitumor efficacy in hepatocellular carcinoma
[doi:10.1016/j.jhepr.2026.101775](https://doi.org/10.1016/j.jhepr.2026.101775) · `paper`  
[src](<../raw/Xing(2026) JHEP Reports; Mass spectrometry-based de novo sequencing reveals non-canonical neoantigens with antitumor efficacy in hepatocellular carcinoma.pdf>)

Mass-spectrometry de novo sequencing, rather than database search, is used to identify non-canonical neoantigens in hepatocellular carcinoma. Candidates were validated by ELISpot for immunogenicity and PRM targeted proteomics for endogenous expression, then tested as a peptide vaccine in subcutaneous and orthotopic mouse HCC models.

### Jin, P. et al. (2025). *Cancer Letters.* Driver mutation landscape of acute myeloid leukemia provides insights for neoantigen-based immunotherapy
[doi:10.1016/j.canlet.2024.217427](https://doi.org/10.1016/j.canlet.2024.217427) · `paper`  
[src](<../raw/Jin(2025) Cancer Letters; Driver mutation landscape of acute myeloid leukemia provides insights for neoantigen-based immunotherapy.pdf>)

Matched DNA and RNA sequencing of 304 AML patients, integrated with about 2,500 further cases, identifies 49 driver genes with a notably high proportion of indels. Indels yielded more and higher-quality neoantigens than SNVs or fusions; two immunogenicity models were built, 30 neoantigens validated by direct MHC binding and 20 confirmed immunogenic by IFN-gamma ELISpot.

### Lang, F. et al. (2024). *Bioinformatics Advances.* Prediction of tumor-specific splicing from somatic mutations as a source of neoantigen candidates
[doi:10.1093/bioadv/vbae080](https://doi.org/10.1093/bioadv/vbae080) · `paper`  
[src](<../raw/Lang(2024) Bioinformatics Advances; Prediction of tumor-specific splicing from somatic mutations as a source of neoantigen candidates.pdf>)

splice2neo integrates predicted splice effects of somatic mutations with splice junctions detected in tumour RNA-seq and annotates the resulting transcripts and peptides; EasyQuant provides targeted read mapping to candidate junctions. Under a stringent rule, 1.7 splice junctions per patient were predicted as targets at under 5% FDR in a melanoma cohort, with tumour-specificity confirmed against independent healthy tissue.

### Li, G. et al. (2024). *Science Translational Medicine.* Splicing neoantigen discovery with SNAF reveals shared targets for cancer immunotherapy
[doi:10.1126/scitranslmed.ade2886](https://doi.org/10.1126/scitranslmed.ade2886) · `paper`  
[src](<../raw/Li(2024) Science Translational Medicine; Splicing neoantigen discovery with SNAF reveals shared targets for cancer immunotherapy.pdf>)

SNAF (Splicing Neo Antigen Finder) defines tumour-specific and likely immunogenic neoantigens from patient RNA-seq, targeting post-transcriptional regulation as a source of neoantigens. Because splicing alterations recur across patients, it identifies shared rather than purely private targets, supported by long-read sequencing and spike-in mass spectrometry.

### Chong, C. et al. (2021). *Nature Biotechnology.* Identification of tumor antigens with immunopeptidomics
[doi:10.1038/s41587-021-01038-8](https://doi.org/10.1038/s41587-021-01038-8) · `paper`  
[src](<../raw/Chong(2021) Nature Biotechnology; Identification of tumor antigens with immunopeptidomics.pdf>)

A review of mass-spectrometry immunopeptidomics for tumour antigen discovery, covering canonical antigens from protein-coding regions and, increasingly, noncanonical antigens arising from outside coding sequence or from noncanonical processing. Combined with transcriptomics and ribosome profiling it can identify thousands of noncanonical peptides, a substantial fraction detectable only in tumours.

### Hanada, K. et al. (2004). *Nature.* Immune recognition of a human renal cancer antigen through post-translational protein splicing
[doi:10.1038/nature02240](https://doi.org/10.1038/nature02240) · `paper`  
[src](<../raw/Hanada(2004) Nature; Immune recognition of a human renal cancer antigen through post-translational protein splicing.pdf>)

CTLs cloned from a renal cell carcinoma recognise an HLA-A3-presented nine-residue FGF-5 peptide generated by protein splicing - post-translational excision of a polypeptide segment followed by ligation of the newly liberated ends. The process had previously been described only in plants and unicellular organisms.

## Finding and measuring neoantigen-reactive T cells

*4 papers.* The inverse problem: identify the reactive T cells directly by phenotype and read their receptors off, rather than predicting antigens and hunting for the cells. Includes how that reactivity is measured.

### Hanada, K. et al. (2022). *Cancer Cell.* A phenotypic signature that identifies neoantigen-reactive T cells in fresh human lung cancers
[doi:10.1016/j.ccell.2022.03.012](https://doi.org/10.1016/j.ccell.2022.03.012) · `paper`  
[src](<../raw/Hanada(2022) Cancer Cell; A phenotypic signature that identifies neoantigen-reactive T cells in fresh human lung cancers.pdf>)

CITE-seq with paired TCR-seq on T cells from fresh non-small-cell lung tumours identifies neoantigen-reactive T cells by phenotype: CD39 protein-positive, CXCL13-positive, and belonging to a high-frequency clonotype. The signature finds both CD4 and CD8 neoantigen-reactive TCRs.

### Lowery, F. J. et al. (2022). *Science.* Molecular signatures of antitumor neoantigen-reactive T cells from metastatic human cancers
[doi:10.1126/science.abl5447](https://doi.org/10.1126/science.abl5447) · `paper`  
[src](<../raw/Lowery(2022) Science; Molecular signatures of antitumor neoantigen-reactive T cells from metastatic human cancers.pdf>)

Mapping 55 neoantigen-specific TCR clonotypes from 10 metastatic human tumours to their single-cell transcriptomes yields NeoTCR signatures for CD8+ and CD4+ neoantigen-reactive TILs. Prospective testing of 73 signature-derived clonotypes showed half recognised tumour antigens or autologous tumours.

### Zheng, C. et al. (2022). *Cancer Cell.* Transcriptomic profiles of neoantigen-reactive T cells in human gastrointestinal cancers
[doi:10.1016/j.ccell.2022.03.005](https://doi.org/10.1016/j.ccell.2022.03.005) · `paper`  
[src](<../raw/Zheng(2022) Cancer Cell; Transcriptomic profiles of neoantigen-reactive T cells in human gastrointestinal cancers.pdf>)

Single-cell RNA-seq with in vitro immunological screening identifies neoantigen-reactive T cells infiltrating cholangiocarcinoma and pancreatic cancer. Most CD8+ and CD4+ neoantigen-reactive TILs are in an exhausted state, with CD8+ cells enriched for CXCL13 and GZMA co-expression and CD4+ cells for HOPX or ADGRG1.

### Kiesgen, S. et al. (2021). *Nature Protocols.* Comparative analysis of assays to measure CAR T-cell-mediated cytotoxicity
[doi:10.1038/s41596-020-00467-0](https://doi.org/10.1038/s41596-020-00467-0) · `paper`  
[src](<../raw/Kiesgen(2021) Nature Protocols; Comparative analysis of assays to measure CAR T-cell-mediated cytotoxicity.pdf>)

A comparative review of in vitro cytotoxicity assays for engineered T cells - chromium release, bioluminescence, impedance and flow cytometry - covering experimental setup, appropriate uses, advantages, disadvantages and ways to compensate for each one's limitations, together with FDA directives for a potency assay for clinical cell therapy release.

## Neoantigen vaccines and clinical responses

*10 papers.* Trials and translational studies where predicted neoantigens were given to patients, and what was observed in the T cells afterwards - from first-in-human peptide vaccines to a randomised mRNA trial.

### Khattak, A. et al. (2026). *Journal of Clinical Oncology.* Intismeran Autogene Plus Pembrolizumab Versus Pembrolizumab Alone in High-Risk Resected Melanoma: 5-Year Update of the Randomized Phase IIb KEYNOTE-942 Study
[doi:10.1200/JCO-26-00835](https://doi.org/10.1200/JCO-26-00835) · `paper`  
[src](<../raw/Khattak(2026) Journal of Clinical Oncology; Intismeran Autogene Plus Pembrolizumab Versus Pembrolizumab Alone in High-Risk Resected Melanoma 5-Year Update of the Randomized Phase IIb KEYNOTE-942 Study.pdf>)

Five-year outcomes from KEYNOTE-942, a randomised phase IIb trial of the individualised mRNA neoantigen therapy intismeran autogene plus pembrolizumab versus pembrolizumab alone in resected stage IIIB-IV melanoma (n=157, randomised 2:1). At a median 60.3 months, recurrence-free survival HR 0.510 (95% CI 0.294-0.887) and distant metastasis-free survival HR 0.411 (0.200-0.843) favoured the combination.

### Cai, Y. et al. (2025). *Science Advances.* Immunopeptidomics-guided discovery and characterization of neoantigens for personalized cancer immunotherapy
[doi:10.1126/sciadv.adv6445](https://doi.org/10.1126/sciadv.adv6445) · `paper`  
[src](<../raw/Cai(2025) Science Advances; Immunopeptidomics-guided discovery and characterization of neoantigens for personalized cancer immunotherapy.pdf>)

A pan-cancer peptide atlas assembled from immunopeptidomics of 531 samples across 14 cancer and 29 normal tissue types yields 389,165 canonical and 70,270 noncanonical peptides. The authors build MaNeo, a machine-learning screening pipeline over this atlas, and validate three predicted neo-peptides that induce T cell proliferation and killing of cancer cells but not healthy cells.

### Sethna, Z. et al. (2025). *Nature.* RNA neoantigen vaccines prime long-lived CD8+ T cells in pancreatic cancer
[doi:10.1038/s41586-024-08508-4](https://doi.org/10.1038/s41586-024-08508-4) · `paper`  
[src](<../raw/Sethna(2025) Nature; RNA neoantigen vaccines prime long-lived CD8+ T cells in pancreatic cancer.pdf>)

Extended follow-up of the autogene cevumeran PDAC trial shows mRNA-lipoplex neoantigen vaccines induce CD8+ T cell clones that persist as long-lived memory. Clonal histories of more than 9,000 single cells across six patients show most vaccine-induced clones transition into a stable effector memory phase, and the association between vaccine response and recurrence-free survival holds at 3.2 years.

### Weber, J. S. et al. (2024). *The Lancet.* Individualised neoantigen therapy mRNA-4157 (V940) plus pembrolizumab versus pembrolizumab monotherapy in resected melanoma (KEYNOTE-942): a randomised, phase 2b study
[doi:10.1016/S0140-6736(23)02268-7](https://doi.org/10.1016/S0140-6736(23)02268-7) · `paper`  
[src](<../raw/Weber(2024) The Lancet; Individualised neoantigen therapy mRNA-4157 (V940) plus pembrolizumab versus pembrolizumab monotherapy in resected melanoma (KEYNOTE-942) a randomised, phase 2b study.pdf>)

The primary report of KEYNOTE-942, a randomised phase 2b trial of individualised neoantigen therapy mRNA-4157 (V940) plus pembrolizumab versus pembrolizumab alone in resected high-risk melanoma. Recurrence-free survival favoured the combination.

### Rojas, L. A. et al. (2023). *Nature.* Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer
[doi:10.1038/s41586-023-06063-y](https://doi.org/10.1038/s41586-023-06063-y) · `paper`  
[src](<../raw/Rojas(2023) Nature; Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer.pdf>)

A phase I trial of adjuvant autogene cevumeran, an individualised uridine mRNA-lipoplex neoantigen vaccine synthesised in real time from surgically resected pancreatic ductal adenocarcinoma. Vaccine-expanded T cells were induced in half the patients, and vaccine response correlated with delayed recurrence.

### Hu, Z. et al. (2021). *Nature Medicine.* Personal neoantigen vaccines induce persistent memory T cell responses and epitope spreading in patients with melanoma
[doi:10.1038/s41591-020-01206-4](https://doi.org/10.1038/s41591-020-01206-4) · `paper`  
[src](<../raw/Hu(2021) Nature Medicine; Personal neoantigen vaccines induce persistent memory T cell responses and epitope spreading in patients with melanoma.pdf>)

Long-term follow-up of eight melanoma patients given a personal neoantigen vaccine shows persistent memory T cell responses and epitope spreading - responses to neoepitopes that were not in the vaccine - years after immunisation.

### Ott, P. A. et al. (2020). *Cell.* A Phase Ib Trial of Personalized Neoantigen Therapy Plus Anti-PD-1 in Patients with Advanced Melanoma, Non-small Cell Lung Cancer, or Bladder Cancer
[doi:10.1016/j.cell.2020.08.053](https://doi.org/10.1016/j.cell.2020.08.053) · `paper`  
[src](<../raw/Ott(2020) Cell; A Phase Ib Trial of Personalized Neoantigen Therapy Plus Anti-PD-1 in Patients with Advanced Melanoma, Non-small Cell Lung Cancer, or Bladder Cancer.pdf>)

A phase Ib trial of the personalised neoantigen vaccine NEO-PV-01 plus nivolumab in advanced melanoma, NSCLC and bladder cancer. The combination was feasible and safe, induced durable neoantigen-specific T cell reactivity with cytotoxic potential, and produced T cells that trafficked to tumours; epitope spread and major pathologic responses were observed.

### Keskin, D. B. et al. (2018). *Nature.* Neoantigen vaccine generates intratumoral T cell responses in phase Ib glioblastoma trial
[doi:10.1038/s41586-018-0792-9](https://doi.org/10.1038/s41586-018-0792-9) · `paper`  
[src](<../raw/Keskin(2018) Nature; Neoantigen vaccine generates intratumoral T cell responses in phase Ib glioblastoma trial.pdf>)

A phase Ib trial of a personal neoantigen-targeting vaccine in glioblastoma, a tumour with low mutation burden and an immunologically cold microenvironment behind the blood-brain barrier. Vaccine-induced neoantigen-specific T cells were detected within the tumour itself, not only in circulation.

### Ott, P. A. et al. (2017). *Nature.* An immunogenic personal neoantigen vaccine for patients with melanoma
[doi:10.1038/nature22991](https://doi.org/10.1038/nature22991) · `paper`  
[src](<../raw/Ott(2017) Nature; An immunogenic personal neoantigen vaccine for patients with melanoma.pdf>)

One of the first-in-human personal neoantigen vaccine trials, immunising melanoma patients against up to 20 predicted personal neoantigens. Neoantigens are argued to be highly immunogenic because they are absent from normal tissue and so bypass central thymic tolerance, and the trial demonstrates that a personalised vaccine can induce neoantigen-specific T cell responses.

### Sahin, U. et al. (2017). *Nature.* Personalized RNA mutanome vaccines mobilize poly-specific therapeutic immunity against cancer
[doi:10.1038/nature23003](https://doi.org/10.1038/nature23003) · `paper`  
[src](<../raw/Sahin(2017) Nature; Personalized RNA mutanome vaccines mobilize poly-specific therapeutic immunity against cancer.pdf>)

A first-in-human study of individualised RNA mutanome vaccines, targeting each patient's own set of mutations. The premise is that T cells against mutant neo-epitopes drive cancer immunity but spontaneous recognition of mutations is inefficient, so vaccination is used to mobilise poly-specific responses that would not arise on their own.

## Immunotherapy response prediction

*3 papers.* Using the neoantigen landscape to say in advance who will benefit: quality- and clonality-aware scores set against tumour mutation burden.

### Lee, K. et al. (2026). *Nature Communications.* NeoPrecis: enhancing immunotherapy response prediction through integration of qualified immunogenicity and clonality-aware neoantigen landscapes
[doi:10.1038/s41467-026-68651-6](https://doi.org/10.1038/s41467-026-68651-6) · `paper`  
[src](<../raw/Lee(2026) Nature Communications; NeoPrecis enhancing immunotherapy response prediction through integration of qualified immunogenicity and clonality-aware neoantigen landscapes.pdf>)

NeoPrecis predicts immunotherapy response by refining neoantigen characterisation across both MHC-I and MHC-II pathways and incorporating tumour clonality, rather than relying on tumour mutation burden. Its interpretable T-cell-recognition model shows MHC molecules influence TCR recognition beyond presentation, and model-derived 'benefit' HLA alleles predict checkpoint-inhibitor outcomes in melanoma (p = 0.04) and NSCLC (p = 0.01).

### Brown, S. D. et al. (2018). *OncoImmunology.* Neoantigen characteristics in the context of the complete predicted MHC class I self-immunopeptidome
[doi:10.1080/2162402X.2018.1556080](https://doi.org/10.1080/2162402X.2018.1556080) · `paper`  
[src](<../raw/Brown(2018) OncoImmunology; Neoantigen characteristics in the context of the complete predicted MHC class I self-immunopeptidome.pdf>)

The authors computed 134 billion peptide-MHC binding predictions - every unique 8-11mer in the human proteome against every available HLA class I allele - to define each individual's predicted self-immunopeptidome. They find that self-immunopeptidome size varies with HLA genotype, combines with mutational load to predict survival, and shows evidence of immunoediting.

### Ghorani, E. et al. (2018). *Annals of Oncology.* Differential binding affinity of mutated peptides for MHC class I is a predictor of survival in advanced lung cancer and melanoma
[doi:10.1093/annonc/mdx687](https://doi.org/10.1093/annonc/mdx687) · `paper`  
[src](<../raw/Ghorani(2018) Annals of Oncology; Differential binding affinity of mutated peptides for MHC class I is a predictor of survival in advanced lung cancer and melanoma.pdf>)

The differential agretopicity index (DAI) - the difference in predicted MHC-I binding affinity between a mutant peptide and its wild-type counterpart - is tested against immune infiltration and outcome in advanced NSCLC (n=66) and melanoma (n=72) from TCGA, plus three immunotherapy-treated cohorts (melanoma n=131, NSCLC n=31). DAI is associated with survival.

## Generative design of epitopes and vaccines

*3 papers.* Methods that DESIGN a peptide or construct rather than ranking the ones a tumour happened to produce. Separated from the predictors because the task is different: exploring sequence space under constraints, not scoring a fixed candidate list.

### Hu, X. et al. (2026). *Biotechnology Advances.* Generative AI-enabled neoantigen vaccine engineering: From tumor antigen discovery to personalized construct design and translational validation
[doi:10.1016/j.biotechadv.2026.109028](https://doi.org/10.1016/j.biotechadv.2026.109028) · `paper`  
[src](<../raw/Hu(2026) Biotechnology Advances; Generative AI-enabled neoantigen vaccine engineering From tumor antigen discovery to personalized construct design and translational validation.pdf>)

_NOT YET WRITTEN._ This section is read off the paper by a person; `scripts/ingest_inbox.py` does not invent it. `status: prose-pending` in the frontmatter says so, and `make audit` reports it.

### Yuan, J. et al. (2026). *Research.* EpiMII: Structure-Aware Graph Neural Networks for MHC-II Epitope Generation
[doi:10.34133/research.1311](https://doi.org/10.34133/research.1311) · `paper`  
[src](<../raw/Yuan(2026) Research; EpiMII Structure-Aware Graph Neural Networks for MHC-II Epitope Generation.pdf>)

EpiMII applies structure-aware graph neural networks to MHC-II epitope generation, using an inverse-folding formulation: rather than predicting structure from sequence, it starts from a fixed 3D backbone and searches sequence space for residues compatible with that geometry, using atomic-level features such as hydrogen bonding, side-chain packing and electrostatics.

### Zhang, G. et al. (2026). *Scientific Reports.* Multi-strategy embedded framework for neoantigen vaccine maturation
[doi:10.1038/s41598-025-34618-8](https://doi.org/10.1038/s41598-025-34618-8) · `paper`  
[src](<../raw/Zhang(2026) Scientific Reports; Multi-strategy embedded framework for neoantigen vaccine maturation.pdf>)

_NOT YET WRITTEN._ This section is read off the paper by a person; `scripts/ingest_inbox.py` does not invent it. `status: prose-pending` in the frontmatter says so, and `make audit` reports it.


# E. Resources, pipelines and evaluation

## Databases and reference resources

*10 papers.* The curated substrate the field trains and benchmarks on: epitope databases, benign immunopeptidome references, the sequenced MHC itself, and the sequence resources that define what counts as self.

### Vita, R. et al. (2024). *Nucleic Acids Research.* The Immune Epitope Database (IEDB): 2024 update
[doi:10.1093/nar/gkae1092](https://doi.org/10.1093/nar/gkae1092) · `paper`  
[src](<../raw/Vita(2024) Nucleic Acids Research; The Immune Epitope Database (IEDB) 2024 update.pdf>)

The twenty-year update to the IEDB, now holding 6.8 million assays and 1.6 million immune epitopes extracted from over 25,000 publications. Changes since 2018 cover a user-directed search interface, advanced data exports, data quality improvements and better interoperability with related resources.

### Koşaloğlu-Yalçın, Z. et al. (2022). *Nucleic Acids Research.* The Cancer Epitope Database and Analysis Resource (CEDAR)
[doi:10.1093/nar/gkac902](https://doi.org/10.1093/nar/gkac902) · `paper`  
[src](<../raw/Koşaloğlu-Yalçın(2022) Nucleic Acids Research; The Cancer Epitope Database and Analysis Resource (CEDAR).pdf>)

CEDAR is a freely accessible database cataloguing cancer epitope and immune receptor data curated from the literature, built as a companion to the IEDB, which covers infectious, autoimmune and allergic disease. It provides molecular characteristics and associated metadata for epitopes recognised by anti-cancer immune cells.

### Kubiniok, P. et al. (2022). *iScience.* Understanding the constitutive presentation of MHC class I immunopeptidomes in primary tissues
[doi:10.1016/j.isci.2022.103768](https://doi.org/10.1016/j.isci.2022.103768) · `paper`  
[src](<../raw/Kubiniok(2022) iScience; Understanding the constitutive presentation of MHC class I immunopeptidomes in primary tissues.pdf>)

A global analysis of MHC-I immunopeptidomes across 29 human and 19 mouse primary tissues. HLA-A, -B and -C allotypes contribute unevenly to the immunopeptidome; tissue-specific and housekeeping peptides have distinct properties; evolutionarily hyperconserved proteins are the primary source at organism scale; and new antigen-processing components are identified, including carboxypeptidases CPE, CNDP1/2 and CPVL.

### UniProtConsortium et al. (2022). *Nucleic Acids Research.* UniProt: the Universal Protein Knowledgebase in 2023
[doi:10.1093/nar/gkac1052](https://doi.org/10.1093/nar/gkac1052) · `paper`  
[src](<../raw/UniProtConsortium(2022) Nucleic Acids Research; UniProt the Universal Protein Knowledgebase in 2023.pdf>)

The 2023 update to the UniProt Knowledgebase, now over 227 million sequences, describing improvements to the data-processing pipeline, expanded reference proteomes, machine-learning-derived annotation for unreviewed entries, and a new website including AlphaFold structures for more than 85% of entries.

### Wu, J. et al. (2022). *Genomics, Proteomics & Bioinformatics.* TSNAdb v2.0: The Updated Version of Tumor-Specific Neoantigen Database
[doi:10.1016/j.gpb.2022.09.012](https://doi.org/10.1016/j.gpb.2022.09.012) · `paper`  
[src](<../raw/Wu(2022) Genomics, Proteomics & Bioinformatics; TSNAdb v2.0 The Updated Version of Tumor-Specific Neoantigen Database.pdf>)

TSNAdb v2.0 updates the tumour-specific neoantigen database with stricter neoantigen identification criteria, predicted neoantigens from three types of somatic mutation, and a collection of experimentally validated neoantigens stratified by the level of experimental evidence supporting each.

### Marcu, A. et al. (2021). *Journal for ImmunoTherapy of Cancer.* HLA Ligand Atlas: a benign reference of HLA-presented peptides to improve T-cell-based cancer immunotherapy
[doi:10.1136/jitc-2020-002071](https://doi.org/10.1136/jitc-2020-002071) · `paper`  
[src](<../raw/Marcu(2021) Journal for ImmunoTherapy of Cancer; HLA Ligand Atlas a benign reference of HLA-presented peptides to improve T-cell-based cancer immunotherapy.pdf>)

The HLA Ligand Atlas is the first large paired HLA-I and HLA-II immunopeptidome collection from benign human tissue: 227 samples from 16 autopsy subjects plus thymus and ovary donors, over 1200 LC-MS runs, yielding 90,428 HLA-I and 142,625 HLA-II ligands across 51 HLA-I and 86 HLA-II allotypes.

### Vita, R. et al. (2018). *Nucleic Acids Research.* The Immune Epitope Database (IEDB): 2018 update
[doi:10.1093/nar/gky1006](https://doi.org/10.1093/nar/gky1006) · `paper`  
[src](<../raw/Vita(2018) Nucleic Acids Research; The Immune Epitope Database (IEDB) 2018 update.pdf>)

The 2018 update to the Immune Epitope Database, which manually curates experimental epitope data from the literature into a free, searchable resource covering antibody, T cell and MHC binding contexts across infectious, allergic, autoimmune and transplant disease. At this point it held more than 1.6 million experiments from 19,500 publications.

### Kawashima, S. et al. (2007). *Nucleic Acids Research.* AAindex: amino acid index database, progress report 2008
[doi:10.1093/nar/gkm998](https://doi.org/10.1093/nar/gkm998) · `paper`  
[src](<../raw/Kawashima(2007) Nucleic Acids Research; AAindex amino acid index database, progress report 2008.pdf>)

AAindex is a database of numerical indices for physicochemical and biochemical properties of amino acids and amino acid pairs, in three sections: AAindex1 (single amino acid indices), AAindex2 (substitution matrices) and AAindex3 (statistical protein contact potentials, added in this release). All values are derived from published literature.

### MHCsequencingconsortium et al. (1999). *Nature.* Complete sequence and gene map of a human major histocompatibility complex
[doi:10.1038/44853](https://doi.org/10.1038/44853) · `paper`  
[src](<../raw/MHCsequencingconsortium(1999) Nature; Complete sequence and gene map of a human major histocompatibility complex.pdf>)

The first complete sequence and gene map of a human MHC, the chromosome 6 region essential to the immune system. Of 224 identified gene loci, 128 are predicted to be expressed, and the authors estimate about 40% of expressed genes have immune system function. Over 50% of the MHC was sequenced twice in different haplotypes.

### Rammensee, H. et al. (1999). *Immunogenetics.* SYFPEITHI: database for MHC ligands and peptide motifs
[doi:10.1007/s002510050595](https://doi.org/10.1007/s002510050595) · `paper`  
[src](<../raw/Rammensee(1999) Immunogenetics; SYFPEITHI database for MHC ligands and peptide motifs.pdf>)

SYFPEITHI is a public database of MHC class I and class II ligands and peptide motifs across humans, apes, cattle, chicken and mouse, searchable by allele, motif, natural ligand, T-cell epitope, source protein and reference, with hyperlinks to EMBL and PubMed and ligand predictions for a number of allelic products.

## Pipelines and analysis tools

*12 papers.* Software that assembles the parts into something usable - end-to-end pipelines, feature toolboxes, prioritisation interfaces, reviews of the whole workflow, and the sequence-search and nearest-neighbour infrastructure underneath.

### Bakhshian, A. et al. (2026). *Journal of Translational Medicine.* AI-driven neoantigen identification: a comprehensive review from somatic variant calling to T cell recognition
[doi:10.1186/s12967-026-08535-x](https://doi.org/10.1186/s12967-026-08535-x) · `paper`  
[src](<../raw/Bakhshian(2026) Journal of Translational Medicine; AI-driven neoantigen identification a comprehensive review from somatic variant calling to T cell recognition.pdf>)

_NOT YET WRITTEN._ This section is read off the paper by a person; `scripts/ingest_inbox.py` does not invent it. `status: prose-pending` in the frontmatter says so, and `make audit` reports it.

### Brlek, P. et al. (2026). *Frontiers in Genetics.* Artificial intelligence in peptide cancer vaccine design: from neoantigen discovery to immunogenicity prediction
[doi:10.3389/fgene.2026.1875066](https://doi.org/10.3389/fgene.2026.1875066) · `paper`  
[src](<../raw/Brlek(2026) Frontiers in Genetics; Artificial intelligence in peptide cancer vaccine design from neoantigen discovery to immunogenicity prediction.pdf>)

_NOT YET WRITTEN._ This section is read off the paper by a person; `scripts/ingest_inbox.py` does not invent it. `status: prose-pending` in the frontmatter says so, and `make audit` reports it.

### Shapiro, I. E. et al. (2025). *Nature Communications.* Sensitive neoantigen discovery by real-time mutanome-guided immunopeptidomics
[doi:10.1038/s41467-025-62647-4](https://doi.org/10.1038/s41467-025-62647-4) · `paper`  
[src](<../raw/Shapiro(2025) Nature Communications; Sensitive neoantigen discovery by real-time mutanome-guided immunopeptidomics.pdf>)

_NOT YET WRITTEN._ This section is read off the paper by a person; `scripts/ingest_inbox.py` does not invent it. `status: prose-pending` in the frontmatter says so, and `make audit` reports it.

### Wang, Z. et al. (2025). *Biomarker Research.* Computation strategies and clinical applications in neoantigen discovery towards precision cancer immunotherapy
[doi:10.1186/s40364-025-00808-9](https://doi.org/10.1186/s40364-025-00808-9) · `paper`  
[src](<../raw/Wang(2025) Biomarker Research; Computation strategies and clinical applications in neoantigen discovery towards precision cancer immunotherapy.pdf>)

A review of integrated neoantigen prediction algorithms covering task definition, theoretical development, benchmark datasets and applications, with emphasis on HLA-peptide binding and TCR recognition methods, and on the use of neoantigens in personalised vaccines and adoptive cell therapy.

### Chuwdhury, G. S. et al. (2024). *Briefings in Bioinformatics.* ImmuneMirror: A machine learning-based integrative pipeline and web server for neoantigen prediction
[doi:10.1093/bib/bbae024](https://doi.org/10.1093/bib/bbae024) · `paper`  
[src](<../raw/Chuwdhury(2024) Briefings in Bioinformatics; ImmuneMirror A machine learning-based integrative pipeline and web server for neoantigen prediction.pdf>)

ImmuneMirror is an open-source pipeline and web server that wraps a balanced random forest for neoantigen prediction and prioritisation, trained on immunogenic neopeptides collected from 19 published studies (test AUC 0.87). Applied to WES and RNA-seq from 805 gastrointestinal tumours, it identifies an MSI-high colorectal subgroup with high mutation burden but low neoantigen load.

### Xia, H. et al. (2024). *Genome Medicine.* pVACview: an interactive visualization tool for efficient neoantigen prioritization and selection
[doi:10.1186/s13073-024-01384-7](https://doi.org/10.1186/s13073-024-01384-7) · `paper`  
[src](<../raw/Xia(2024) Genome Medicine; pVACview an interactive visualization tool for efficient neoantigen prioritization and selection.pdf>)

pVACview is an interactive visualisation interface for neoantigen prioritisation, presenting variant, transcript, peptide and algorithm-level data together. It is designed to replace tabular pipeline reports that are hard to navigate and are commonly over-simplified - for example by restricting consideration to a single RNA isoform.

### Johnson, J. et al. (2021). *IEEE Transactions on Big Data.* Billion-Scale Similarity Search with GPUs
[doi:10.1109/tbdata.2019.2921572](https://doi.org/10.1109/tbdata.2019.2921572) · `paper`  
[src](<../raw/Johnson(2021) IEEE Transactions on Big Data; Billion-Scale Similarity Search with GPUs.pdf>)

The Faiss approach to approximate k-nearest-neighbour search on GPUs, using product-quantization codes so that billion-scale vector collections can be searched without reconstructing the vectors or holding them uncompressed in memory. The flagship application is building k-NN graphs at a scale where exact indexing and existing methods such as NN-Descent do not fit.

### Lang, F. et al. (2021). *Bioinformatics.* NeoFox: annotating neoantigen candidates with neoantigen features
[doi:10.1093/bioinformatics/btab344](https://doi.org/10.1093/bioinformatics/btab344) · `paper`  
[src](<../raw/Lang(2021) Bioinformatics; NeoFox annotating neoantigen candidates with neoantigen features.pdf>)

NeoFox is an open-source Python package that annotates neoantigen candidates with 16 neoantigen features gathered from the literature, bringing scattered published metrics into one toolbox.

### Sharma, N. et al. (2021). *WIREs Data Mining and Knowledge Discovery.* Computational resources in healthcare
[doi:10.1002/widm.1437](https://doi.org/10.1002/widm.1437) · `paper`  
[src](<../raw/Sharma(2021) WIREs Data Mining and Knowledge Discovery; Computational resources in healthcare.pdf>)

A broad review cataloguing computational resources across informatics-based fields with healthcare applications - medical, bio-, chem-, pharmaco-, immuno- and clinical informatics - grouped into drug discovery, toxicity prediction, vaccine design, disease biomarkers and Internet of Things, with emphasis on freely available functional resources.

### Hundal, J. et al. (2020). *Cancer Immunology Research.* pVACtools: A Computational Toolkit to Identify and Visualize Cancer Neoantigens
[doi:10.1158/2326-6066.CIR-19-0401](https://doi.org/10.1158/2326-6066.CIR-19-0401) · `paper`  
[src](<../raw/Hundal(2020) Cancer Immunology Research; pVACtools A Computational Toolkit to Identify and Visualize Cancer Neoantigens.pdf>)

pVACtools is an extensible toolkit covering computational identification, selection, prioritisation and visualisation of neoantigens, taking somatic variants in VCF and handling gene fusions and insertion/deletion frameshift variants as well as missense mutations.

### Malkov, Y. A. et al. (2020). *IEEE Transactions on Pattern Analysis and Machine Intelligence.* Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs
[doi:10.1109/TPAMI.2018.2889473](https://doi.org/10.1109/TPAMI.2018.2889473) · `paper`  
[src](<../raw/Malkov(2020) IEEE Transactions on Pattern Analysis and Machine Intelligence; Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs.pdf>)

Hierarchical NSW builds a multi-layer structure of proximity graphs over nested subsets of the stored elements, with an element's maximum layer chosen randomly under an exponentially decaying distribution. Searching from the top layer exploits scale separation to achieve logarithmic complexity, and a neighbour-selection heuristic improves performance at high recall and on clustered data.

### Steinegger, M. et al. (2017). *Nature Biotechnology.* MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets
[doi:10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988) · `paper`  
[src](<../raw/Steinegger(2017) Nature Biotechnology; MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets.pdf>)

MMseqs2 performs sensitive protein sequence searching at speeds that make massive datasets tractable: annotating 1.1 billion hypothetical protein sequences against 16,479 Pfam profiles took 8.3 hours on one server, roughly 4,000-14,000 times faster than HMMER3 while finding comparable or more annotations.

## Benchmarking, bias and generalisation

*7 papers.* Papers that measure how well the methods above actually work, and find the answer turns on training-set bias, train-test leakage, and whether the test peptides were ever seen.

### Zhang, Z. et al. (2026). *Cell Genomics.* Cross-task interpretability through unified modeling reveals a universal shortcut bias in neoantigen prediction
[doi:10.1016/j.xgen.2026.101214](https://doi.org/10.1016/j.xgen.2026.101214) · `paper`  
[src](<../raw/Zhang(2026) Cell Genomics; Cross-task interpretability through unified modeling reveals a universal shortcut bias in neoantigen prediction.pdf>)

ImmUni is a unified framework modelling neoantigen binding, presentation and immunogenicity together, enabling cross-task attention analysis. That analysis shows deep learning models systematically learn shortcuts in immunogenicity prediction rather than immunogenic features, driven by intra-HLA imbalance in training data; a mutual-information-guided debiasing strategy mitigates it.

### Graber, D. et al. (2025). *Nature Machine Intelligence.* Resolving data bias improves generalization in binding affinity prediction
[doi:10.1038/s42256-025-01124-5](https://doi.org/10.1038/s42256-025-01124-5) · `paper`  
[src](<../raw/Graber(2025) Nature Machine Intelligence; Resolving data bias improves generalization in binding affinity prediction.pdf>)

Train-test leakage between PDBbind and the CASF benchmarks has severely inflated reported performance of deep-learning protein-ligand binding affinity models. The authors build PDBbind CleanSplit, a structure-based filtered training set removing leakage and internal redundancy; retraining top models on it causes their benchmark scores to drop substantially.

### Shen, L. (2025). *venue not recorded.* AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations
[doi:10.1101/2025.08.05.668750](https://doi.org/10.1101/2025.08.05.668750) · `preprint`  
[src](<../raw/Shen(2025) unknown; AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations.pdf>)

_NOT YET WRITTEN._ This section is read off the paper by a person; `scripts/ingest_inbox.py` does not invent it. `status: prose-pending` in the frontmatter says so, and `make audit` reports it.

### Tadros, D. M. et al. (2025). *Genome Medicine.* Predicting MHC-I ligands across alleles and species: how far can we go?
[doi:10.1186/s13073-025-01450-8](https://doi.org/10.1186/s13073-025-01450-8) · `paper`  
[src](<../raw/Tadros(2025) Genome Medicine; Predicting MHC-I ligands across alleles and species how far can we go.pdf>)

Using an expanded MixMHCpred3.0 architecture, the authors systematically assess how far MHC-I ligand prediction extends to alleles with no known ligand data. Accuracy is high for most human and laboratory-mouse alleles but significantly lower in other species, and the molecular determinants of that drop are characterised.

### Müller, M. et al. (2023). *Immunity.* Machine learning methods and harmonized datasets improve immunogenic neoantigen prediction
[doi:10.1016/j.immuni.2023.09.002](https://doi.org/10.1016/j.immuni.2023.09.002) · `paper`  
[src](<../raw/Müller(2023) Immunity; Machine learning methods and harmonized datasets improve immunogenic neoantigen prediction.pdf>)

WES and RNA-seq from 120 patients across two large external neoantigen immunogenicity screens plus 11 in-house patients were reprocessed uniformly, yielding 46,017 somatic SNVs and 1,781,445 neo-peptides, of which 212 mutations and 178 neo-peptides were immunogenic. Classifiers trained on these harmonised data improved neoantigen ranking by up to 30%, and features beyond the usual ones proved predictive.

### Wells, D. K. et al. (2020). *Cell.* Key Parameters of Tumor Epitope Immunogenicity Revealed Through a Consortium Approach Improve Neoantigen Prediction
[doi:10.1016/j.cell.2020.09.015](https://doi.org/10.1016/j.cell.2020.09.015) · `paper`  
[src](<../raw/Wells(2020) Cell; Key Parameters of Tumor Epitope Immunogenicity Revealed Through a Consortium Approach Improve Neoantigen Prediction.pdf>)

A global consortium ran diverse neoantigen prediction pipelines on shared genomic data with matched experimental immunogenicity measurements. Of 608 tested peptide-MHCs, 37 were bound by patient-matched T cells; presentation and recognition characteristics predicted immunogenicity, and model-based interventions improved prediction.

### Zhao, W. et al. (2018). *PLOS Computational Biology.* Systematically benchmarking peptide-MHC binding predictors: From synthetic to naturally processed epitopes
[doi:10.1371/journal.pcbi.1006457](https://doi.org/10.1371/journal.pcbi.1006457) · `paper`  
[src](<../raw/Zhao(2018) PLOS Computational Biology; Systematically benchmarking peptide-MHC binding predictors From synthetic to naturally processed epitopes.pdf>)

A blind benchmark of 18 MHC binding predictors across 32 HLA class I and 24 class II alleles, using previously untested data covering both synthetic binding measurements and naturally processed, MHC-eluted epitopes. Neural network approaches outperformed regression and structural modelling, with mhcflurry and nn_align best for class I 9-mers and class II 15-mers respectively (AUC 0.911).


## What this document does not say

- **It does not rank or evaluate.** A paper's presence records that the team read or wrote it,
  nothing more.
- **It does not say who circulated what.** That is recorded per paper in the sidecars, and is
  deliberately not browsable.
- **It does not resolve disagreements between papers.** Two entries in one topic may contradict
  each other; the topic groups subjects, not conclusions.
- **The counts in `## Contents` are the checksum, not decoration.** `scripts/build.py` refuses to
  build if the body disagrees with them.
