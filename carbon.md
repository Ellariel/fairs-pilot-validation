---
# carbon.md: FAIR+S sustainability metadata for the dataset "FAIR+S expert survey"
# Companion to: "FAIR+S: An expert-based validation study of a framework for sustainable research data and software"
#
# ⚠ STATUS: DRAFT. Every value tagged [ASSUMED] is a planning assumption inferred from the
# paper and typical LimeSurvey deployments. It is NOT a measurement. Replace each one with a
# measured or confirmed value (see section 9) before publishing.
carbon_md_version: "0.1-draft"
metadata_schema: "FAIR+S (S1-S5), see paper Table 1 and Sec. 2"
created: 2026-10-06
last_updated: 2026-10-06

artefact:
  title: "FAIR+S expert survey: questionnaire, responses and analysis"
  type: ["dataset", "survey instrument", "analysis code"]
  description: >
    Anonymous expert survey (LimeSurvey) assessing the perceived importance, added value and
    feasibility of the FAIR+S principles. 40 valid responses; 27 selected experts.
  repository: "https://github.com/ellariel/fairs-pilot-validation/tree/dev"
  identifier: "TODO: DOI (e.g. Zenodo) [F1: persistent identifier still to be minted]"
  version: "TODO: tag/release of the repository snapshot used in the paper"
  license: "TODO: data CC-BY-4.0 [ASSUMED]; code MIT or Apache-2.0 [ASSUMED]"
  related_publication: "Valko et al., FAIR+S: An expert-based validation study (manuscript, 2026)"
  creators:
    - {name: "Danila Valko", orcid: "0000-0002-8058-7539", affiliation: "University of Oldenburg; OFFIS", role: "corresponding author, responsible for S4 reporting"}
    - {name: "Jan Soeren Schwarz", orcid: "0000-0003-0261-4412", affiliation: "University of Oldenburg; OFFIS"}
    - {name: "Jorge Marx Gomez", orcid: "0000-0002-7833-7549", affiliation: "University of Oldenburg"}
    - {name: "Ralf Isenmann", orcid: "0000-0002-1611-4892", affiliation: "Wilhelm Buechner Hochschule"}
  contact: "danila.valko@offis.de"
  funding: "None (no particular funding)"
  ethics: "Commission for Research Impact Assessment and Ethics, Carl von Ossietzky Universitaet Oldenburg, Drs.EK/2025/103"

# ---------------------------------------------------------------------------
# FAIR+S alignment overview
# ---------------------------------------------------------------------------
fairs_alignment:
  S1_energy_efficiency_attributes: "section 3 (energy, resource use, carbon footprint)"
  S2_sustainability_benchmarks: "section 4"
  S3_framework_alignment: "section 5"
  S4_transparency_accountability: "section 6 (method, assumptions, tools, uncertainty, responsible parties)"
  S5_life_cycle_sustainability: "section 7"
---

# carbon.md: Sustainability metadata of the FAIR+S survey dataset

This file applies the FAIR+S Sustainable principles (S1-S5) [3, 4, 5] on top of FAIR [1] and FAIR4RS [2] to the survey dataset published with the paper [5]. Sources are listed in section 10. The paper announces this as a worked example in its *Limitations and future work* section. The file has three parts:

1. Survey metadata (sections 1-2) that makes the artefact findable and reusable in the FAIR sense.
2. Carbon and energy attributes (sections 3-7), one section per principle S1-S5.
3. Open items (sections 8-9).

> **Convention:** `[PAPER]` means the value is stated in the manuscript. `[ASSUMED]` means the value is an assumption made here. `[TODO]` means the value is unknown and must be supplied by the authors.

---

## 1. Survey metadata (FAIR part)

### 1.1 Instrument and platform

| Attribute | Value |
|---|---|
| Survey tool | LimeSurvey [11] [CONFIRMED by authors] |
| LimeSurvey edition and version | Community Edition, 6.x [ASSUMED] |
| Hosting | University LimeSurvey service of Carl von Ossietzky Universitaet Oldenburg [CONFIRMED by authors] |
| Hosting location | Oldenburg, Lower Saxony, Germany; German power grid [ASSUMED, follows from hosting] |
| Runtime stack | Linux VM, Apache/nginx, PHP 8.x, MySQL/MariaDB [ASSUMED, LimeSurvey default stack] |
| Access mode | Open survey link, anonymous responses, no participant tokens [PAPER: anonymous; ASSUMED: open link] |
| Survey mode | Question-by-question groups, with a structured FAIR+S introduction page before the evaluation section [PAPER: structured introduction] |
| Languages | English [ASSUMED] |
| Consent | Digital informed consent on the first page; "valid" = submitted after consent [PAPER] |
| Piloting | Piloted with a small expert group (OFFIS Energy-efficient Smart Cities; Uni Oldenburg VLBA) before deployment [PAPER] |
| Field period | 2026-02-02 to 2026-04-15 (73 days) [PAPER] |
| Additional dissemination | 3rd NFDI4Energy Conference, 24-25 March 2026 [PAPER] |
| Recruitment | Purposive sampling [8]: OFFIS, L3S, Uni Oldenburg, GSF, NFDI, SSI, de-RSE, LinkedIn [PAPER] |
| Design basis | Design Science Research, ex-ante expert evaluation [9, 10]; survey design after Dillman et al. [6]; Likert analysis after Boone and Boone [7]; web-survey reporting guidance CHERRIES [12] |

### 1.2 Sample

| Attribute | Value |
|---|---|
| Valid responses | 40 (submitted after consent; not necessarily complete) [PAPER] |
| Selected experts | 27 (eligibility: (1a or 1b) and (2a or 2b)) [PAPER] |
| Other participants | 13 [PAPER] |
| Effective n per analysis | Importance S1-S5: 20. Added value: 20 (ratings), 21 (yes/no/unsure). Feasibility: 23. Profiling and Q15: 27 [PAPER] |
| Missing-data handling | Available-case analysis, no imputation [PAPER] |
| Personal data | None collected (anonymous). The IP address and timestamp options of LimeSurvey are switched off [ASSUMED] |

### 1.3 Variables

Only the items disclosed in Appendix B of the paper are described: Q1-Q25, Q28 and Q30 (28 items). Scales are copied from Appendix B. The LimeSurvey question types are assumed:

| Block | Items | Content | LimeSurvey type [ASSUMED] | Scale |
|---|---|---|---|---|
| Profile | Q1 | Primary field | Multiple choice (list, radio) with "Other" | 5 categories |
| Profile | Q2-Q3 | Research experience, education | List (radio) | ordinal categories |
| Profile | Q4-Q6 | Review activity, data experience, software experience | List (radio) | ordinal categories |
| Baseline | Q7, Q10, Q11 | Familiarity: FAIR, sustainability/SDGs, green software | 5-point choice | 1-5 |
| Baseline | Q8, Q9 | Importance and application of FAIR | 5-point choice | 1-5 |
| Evaluation: importance | Q12, Q30 | Importance of energy attributes; importance of S1-S5 | 5-point choice; array (matrix) | 1-5 |
| Evaluation: feasibility | Q13, Q14 | Practicality of energy metadata; feasibility of reporting execution context | 5-point choice | 1-5 |
| Evaluation: practice | Q15, Q21 | Details currently reported; trusted measurement methods | Multiple choice (checkbox) | nominal, multi-select |
| Evaluation: value | Q19, Q20, Q22, Q24 | Benchmarks, certification, transparency | 5-point choice | 1-5 |
| Evaluation: policy | Q17, Q25, Q28 | Required reporting, disclosure, lifecycle statements | Yes/No/Unsure | nominal |
| Open text | Q16, Q18, Q23 | Challenges, metrics, barriers | Long free text | text |

Derived variable: `group` = {selected expert, other participant}, computed from the eligibility criteria 1a/1b/2a/2b [PAPER].

### 1.4 Files and formats [ASSUMED, to be reconciled with the repository]

| File | Format | Content |
|---|---|---|
| `questionnaire.lss` | LimeSurvey structure export (XML) | Full survey definition |
| `questionnaire.pdf` / `Appendix B` | PDF / LaTeX table | Human-readable question list |
| `responses_raw.csv` | CSV, UTF-8, comma separated, one row per response | LimeSurvey export, answer codes |
| `responses_labelled.csv` | CSV, UTF-8 | Same data with answer text instead of codes |
| `codebook.md` or `.csv` | Markdown / CSV | Variable name, label, scale, value labels |
| `analysis/` | Python scripts or notebooks | Descriptive statistics, Mann-Whitney U, Wilcoxon signed-rank, Friedman, 95 % CI |
| `fig*.pdf`, `fig05b.csv` | PDF, CSV | Figures in the paper and their source data |
| `carbon.md` | Markdown + YAML | This file |

---

## 2. FAIR and FAIR4RS mapping for the artefact

| Principle | Status | Note |
|---|---|---|
| F1 persistent ID | Open | Repository URL exists; a DOI (e.g. Zenodo) is still needed [TODO] |
| F2 rich metadata | Partly | This file plus codebook; add `CITATION.cff` and `codemeta.json` [TODO] |
| A1 retrievable by ID | Yes | Public GitHub repository over HTTPS [PAPER] |
| A2 metadata persist | Open | Needs an archive deposit, since GitHub is not a preservation service |
| I1/I2 formal vocabulary | Partly | Use DDI-Lifecycle or DDI-Codebook for variables [36], schema.org/Dataset or DCAT for the dataset record [37]; energy-domain schemas such as OEMetadata [34, 35] as a reference [ASSUMED] |
| F2 (citation metadata) | Open | `CITATION.cff` and CodeMeta [38] |
| R1.1 licence | Open | Choose licence (section 1, `license`) [TODO] |
| R1.2 provenance | Yes | Field period, tool, sampling, eligibility and analysis steps are documented in the paper |
| R1.3 community standards | Partly | Survey reporting guidance, e.g. CHERRIES for web surveys [12] [ASSUMED] |
| S1-S5 | This file | Sections 3-7 |

---

## 3. S1: Energy efficiency attributes

*Boundary of this estimate:* survey operation (server and client), data analysis, and storage and distribution of the published data. Not included: authors' office work, writing the paper, and manufacturing of devices (see section 7).

All figures below are **estimates based on assumptions** [ASSUMED]. Measured values should replace them.

### 3.1 Energy and emissions per activity

| Activity | Assumption [ASSUMED] | Energy (kWh) | Emissions (kg CO2e) |
|---|---|---:|---:|
| LimeSurvey server (share of VM for the whole field period) | 20 W average attributable load x 1,752 h (73 days) x PUE 1.4 | 49.1 | 18.7 |
| Participant devices | 40 sessions (= 40 valid responses, confirmed) x 15 min [ASSUMED] x 30 W | 0.30 | 0.11 |
| Network transfer | Under 2 MB per session, 40 sessions; negligible | under 0.01 | under 0.01 |
| Data analysis and figures | One laptop, about 20 h at 30 W (Python, no GPU) | 0.6 | 0.23 |
| Archive storage and distribution (repository and DOI deposit) | Under 50 MB, 5 years, 100 downloads; negligible | under 0.1 | under 0.05 |
| **Total** | | **about 50** | **about 19** |

Sessions equal the 40 valid responses, as confirmed by the authors, so no separate count of aborted sessions is included.

Grid emission factor used: 380 g CO2e/kWh, an approximate German grid average [ASSUMED, see UBA [20]]. Replace it with the factor of the actual provider or the official yearly value. PUE is defined in ISO/IEC 30134-2 [19]; 1.4 is an assumed typical value. The estimation approach follows Green Algorithms [13] (power x time x PUE x carbon intensity).

### 3.2 Derived indicators

| Indicator | Value |
|---|---|
| Carbon per valid response (40) | about 0.48 kg CO2e |
| Carbon per selected expert (27) | about 0.71 kg CO2e |
| Server share of total | over 95 % |
| Ratio of fixed to variable cost | The server load is almost independent of response count; it is mostly a fixed cost of keeping the survey open |

### 3.3 Hardware and software context (execution context)

The paper shows that this is what respondents already report (Fig. 8b: CPU/GPU, memory, frameworks, OS). The same set is given here.

| Attribute | Server | Analysis machine |
|---|---|---|
| CPU/GPU | 2 vCPU, no GPU [ASSUMED] | Laptop-class x86-64 CPU, no GPU [ASSUMED] |
| Memory | 4 GB [ASSUMED] | 16 GB [ASSUMED] |
| OS / environment | Linux (Debian/Ubuntu or similar) [ASSUMED] | Windows 11 [from authoring environment] |
| Software | LimeSurvey 6.x, PHP 8.x, MySQL/MariaDB [ASSUMED] | Python 3.x, pandas, SciPy, matplotlib [ASSUMED] |
| Cloud provider / region | None (on-premise university data centre) [ASSUMED] | Not applicable |
| Energy logs | None available [ASSUMED] | None; estimated by tool (see 3.4) |

### 3.4 Measurement tools

| Tool | Use | Status |
|---|---|---|
| Hosting provider's power data (university IT) | Server energy | TODO: request, would replace the estimate in 3.1 |
| CodeCarbon [14] | Analysis scripts | TODO: optional, run the analysis notebook once with CodeCarbon (alternatives: Carbontracker [15], PowerAPI [16]) |
| Green Algorithms calculator [13] | Cross-check of 3.1 | TODO: optional |

---

## 4. S2: Sustainability benchmarks

| Attribute | Value |
|---|---|
| Community benchmark used | None. No community benchmark exists for survey hosting or small statistical analyses [ASSUMED] |
| Reference points used for comparison | PUE 1.4 as a typical data-centre value; German grid average [ASSUMED] |
| Intended future benchmark | Benchmarks developed in NFDI4Energy [30] and GSF [29], if available (paper, Sec. 2.2, S2). Domain benchmarks of this kind include SPECpower [26] |
| Normalisation | Per valid response; per field-day (about 0.26 kg CO2e/day) |
| Comparison with SPECpower-style data | Not performed |

---

## 5. S3: Alignment with sustainability frameworks and standards

| Framework / standard | Alignment |
|---|---|
| GHG Protocol [23] | Server and device emissions treated as Scope 2 (purchased electricity) of the operating organisation. Scope 3 (devices, upstream) not covered. Market-based accounting not used (location-based factor only) |
| ISO 14044 (LCA) [22] | Not a full LCA. Functional unit: "operate the survey and publish its data". System boundary in section 3 |
| ISO/IEC 21031 (Software Carbon Intensity, SCI) [21] | Per-response SCI-style intensity given in 3.2, with E = energy, I = grid intensity. The embodied part M is omitted, so it is a partial SCI |
| W3C Web Sustainability Guidelines [24] | Not assessed. The survey uses the default LimeSurvey theme; no media, no tracking scripts [ASSUMED] |
| Green DiSC (SSI) [25] | Not assessed |
| Sustainability awareness framework [27], Karlskrona manifesto [28] | Conceptual basis of S4 transparency; not assessed formally |
| Digital MRV (dMRV) [18] | This file is the human- and machine-readable reporting step. Verification is not performed |

---

## 6. S4: Transparency and accountability

### 6.1 Method and assumptions

- Method: bottom-up estimate, E = power x time x PUE, then CO2e = E x grid intensity.
- Key assumptions: 20 W attributable server load, PUE 1.4, 380 g CO2e/kWh, 15 min per session, 20 h analysis time. Session count is 40 (confirmed). All are marked [ASSUMED] in section 3.
- Excluded: embodied emissions of servers, laptops and participant devices; emissions of survey invitations (e-mail, LinkedIn); travel to the NFDI4Energy conference; authors' working time outside the analysis.

### 6.2 Uncertainty

| Quantity | Central | Range (plausible) | Main driver |
|---|---:|---|---|
| Total energy | 50 kWh | 25-100 kWh | Server load share (10-40 W) and PUE (1.2-1.8) |
| Grid intensity | 380 g/kWh | 300-450 g/kWh | Year and accounting method |
| **Total emissions** | **19 kg CO2e** | **about 8-45 kg CO2e** | Product of the two ranges above |

The range is a judgement-based interval, not a statistical confidence interval [ASSUMED].

### 6.3 Responsible parties

| Role | Party |
|---|---|
| Estimate prepared by | Danila Valko (corresponding author) with Claude (AI assistant) drafting support |
| Server operator / data source for energy figures | University of Oldenburg IT services [TODO: confirm] |
| Verification | None (self-reported). Third-party verification [TODO, optional] |
| Date of estimate | 2026-10-06 |

---

## 7. S5: Life cycle sustainability

| Phase | Information | Value |
|---|---|---|
| Life-cycle basis | Research software lifecycle [31]; LCA practice [22, 32] |
| Development | Questionnaire design, pilot, programming in LimeSurvey | Not quantified. Few person-days at office workstations [ASSUMED] |
| Deployment | Survey open 73 days; server share in section 3 | 18.7 kg CO2e [ASSUMED] |
| Analysis | Python scripts, about 20 h | 0.23 kg CO2e [ASSUMED] |
| Preservation | Public repository plus archive deposit of under 50 MB | Negligible [ASSUMED] |
| Expected maintenance | None planned after publication, other than fixing errors. The survey is closed; the LimeSurvey instance can be archived and shut down [ASSUMED] |
| Update frequency | Not planned. A follow-up survey on S5 and system boundaries is suggested in the paper, which would be a new artefact version [PAPER, future work] |
| Retention | Raw responses retained for at least 10 years following DFG good-practice guidance [33] [ASSUMED] |
| End of life | Archive copy remains; the server-side survey and database are deleted after export [ASSUMED] |
| Cumulative resource need over life (5 years) | Operation 19 kg CO2e, storage under 0.1 kg CO2e [ASSUMED] |
| Upstream dependencies | LimeSurvey, Python libraries, GitHub. No upstream sustainability data is available (see the paper's discussion of derived artefacts and allocation as an open question) |

---

## 8. Reuse notes

- When the dataset is reused, the sustainability cost of the reuse (download, analysis) is the reuser's. A reuser may reference this file as provenance for upstream impact (paper R1.2, R2, S4).
- Survey results should be interpreted with the caveats of the paper: available-case analysis, possible non-response bias, and the ambiguity of Q13 ("practical").
- n differs between analyses, so use the per-item n from section 1.2, not 27 or 40, as the denominator.

## 9. Checklist to turn this draft into a final carbon.md

- [ ] Confirm the LimeSurvey edition and version, plus PHP and database versions (LimeSurvey admin, "Global settings, Overview"). Tool and host are already confirmed.
- [ ] Confirm the average completion time to replace the 15 min assumption (LimeSurvey timing statistics).
- [ ] Obtain the server's real power or VM share from IT services; replace 20 W and PUE.
- [ ] Insert the correct grid emission factor for the year 2026 and hosting provider.
- [ ] Mint a DOI, choose licences, add `CITATION.cff`.
- [ ] Confirm that IP address, timestamp and referrer logging were off in LimeSurvey.
- [ ] Reconcile the file list in 1.4 with the actual repository.
- [ ] Optionally run CodeCarbon on the analysis and replace the 0.6 kWh estimate.
- [ ] Remove all `[ASSUMED]` tags that have been confirmed and update `last_updated`.

---

## 10. References

Sources are numbered as in `[n]`. Entries marked **(bib)** are in the paper's `paper.bib`. Entries marked **(external)** are not in the paper, and their details should be checked before publication.

**FAIR and FAIR+S framework**

- [1] Wilkinson, M. D. et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*. doi:10.1038/sdata.2016.18 (bib: Wilkinson2016)
- [2] Barker, M. et al. (2022). Introducing the FAIR Principles for research software. *Scientific Data*. doi:10.1038/s41597-022-01710-x (bib: Barker2022)
- [3] Valko, D., Schwarz, J. S., Isenmann, R., Marx Gomez, J. (2026). Advancing Energy System Research with the FAIR+S Framework. *Proc. 3rd NFDI4Energy Conference*. doi:10.52825/ocp.v9i.3278 (bib: ValkoFAIRSNFDI4Energy)
- [4] Valko, D. (2025). When FAIR Isn't Enough: Towards Sustainable Research Data and Software. SSRN. doi:10.2139/ssrn.5546379 (bib: ValkoFAIRS)
- [5] Valko, D. et al. (2026). FAIR+S: An expert-based validation study of a framework for sustainable research data and software. Manuscript (this dataset's companion paper), incl. Appendix B (survey questions).

**Survey method and instrument**

- [6] Dillman, D. A., Smyth, J. D., Christian, L. M. (2014). *Internet, Phone, Mail, and Mixed Mode Surveys: The Tailored Design Method*. Wiley. (bib: Dillman2014)
- [7] Boone, H. N., Boone, D. A. (2012). Analyzing Likert Data. *Journal of Extension*. doi:10.34068/joe.50.02.48 (bib: Boone2012)
- [8] Burgman, M. A. et al. (2011). Expert Status and Performance. *PLoS ONE*. doi:10.1371/journal.pone.0022998 (bib: Burgman2011)
- [9] Hevner, A. R. et al. (2004). Design Science in Information Systems Research. *MIS Quarterly*. (bib: hevner2004design)
- [10] Venable, J., Pries-Heje, J., Baskerville, R. (2016). FEDS: a Framework for Evaluation in Design Science Research. *European Journal of Information Systems*. doi:10.1057/ejis.2014.36 (bib: Venable2016)
- [11] LimeSurvey GmbH. LimeSurvey: the open-source survey tool, documentation. https://www.limesurvey.org and https://manual.limesurvey.org (external, check the version used)
- [12] Eysenbach, G. (2004). Improving the quality of web surveys: the Checklist for Reporting Results of Internet E-Surveys (CHERRIES). *Journal of Medical Internet Research* 6(3):e34. doi:10.2196/jmir.6.3.e34 (external)

**Energy and carbon estimation (S1, S4)**

- [13] Lannelongue, L., Grealey, J., Inouye, M. (2021). Green Algorithms: Quantifying the Carbon Footprint of Computation. *Advanced Science*. doi:10.1002/advs.202100707 (bib: Lannelongue2021)
- [14] Courty, B. et al. (2025). CodeCarbon (mlco2/codecarbon v3.0.3). Zenodo. doi:10.5281/zenodo.15870443 (bib: codecarbon)
- [15] Anthony, L. F. W., Kanding, B., Selvan, R. (2020). Carbontracker: Tracking and Predicting the Carbon Footprint of Training Deep Learning Models. (bib: anthony2021carbontracker_2)
- [16] Fieni, G., Acero, D. R., Rust, P., Rouvoy, R. (2024). PowerAPI: A Python framework for building software-defined power meters. *JOSS* 9(98):6670. doi:10.21105/joss.06670 (bib: Fieni2024)
- [17] Schwartz, R., Dodge, J., Smith, N. A., Etzioni, O. (2020). Green AI. *Communications of the ACM*. doi:10.1145/3381831 (bib: schwartz2020green_25)
- [18] Körner, M.-F., Leinauer, C., Ströher, T., Strüker, J. (2025). Digital Measuring, Reporting, and Verification (dMRV) for Decarbonization. *Business & Information Systems Engineering*. doi:10.1007/s12599-025-00953-3 (bib: Korner2025dMRV)
- [19] ISO/IEC 30134-2:2016. Data centres, Key performance indicators, Part 2: Power usage effectiveness (PUE). (external, source of the PUE definition)
- [20] German Environment Agency (Umweltbundesamt, UBA). Emission factors of the German electricity mix ("Strommix"), yearly publication. https://www.umweltbundesamt.de (external, replace the assumed 380 g CO2e/kWh with the figure for the reporting year)

**Benchmarks, standards and frameworks (S2, S3)**

- [21] ISO/IEC 21031:2024. Software Carbon Intensity (SCI) specification. https://www.iso.org/standard/86612.html (bib: ISO_IEC_21031_2024)
- [22] ISO 14044:2006/2021. Environmental management, Life cycle assessment, Requirements and guidelines. BSI. (bib: ISO14044)
- [23] World Resources Institute, WBCSD. Greenhouse Gas Protocol. (bib: ghg)
- [24] World Wide Web Consortium. Web Sustainability Guidelines (WSG). (bib: w3c)
- [25] Software Sustainability Institute. Green DiSC: a Digital Sustainability Certification. (bib: sysinst)
- [26] Huppler, K., Lange, K.-D., Beckett, J. (2012). SPEC: enabling efficiency measurement. *ICPE*. doi:10.1145/2188286.2188331 (bib: SPEC)
- [27] Duboc, L. et al. (2020). Requirements engineering for sustainability: an awareness framework. *Requirements Engineering*. doi:10.1007/s00766-020-00336-y (bib: Duboc2020)
- [28] Becker, C. et al. (2015). Sustainability design and software: the Karlskrona manifesto. *ICSE*. (bib: Becker2015)
- [29] Green Software Foundation. Software Carbon Intensity and organisational framework SOFT. https://soft.greensoftware.foundation/ (bib: soft2026)
- [30] NFDI4Energy Consortium. NFDI4Energy. https://www.nfdi4energy.uol.de (bib: NFDI4Energy2023)

**Life cycle, preservation and retention (S5)**

- [31] Courbebaisse, G. et al. (2023). Research Software Lifecycle. EOSC Association, Zenodo. doi:10.5281/zenodo.8324828 (bib: ResearchSoftwareLifecycle)
- [32] Falk, S. et al. (2025). More than Carbon: Cradle-to-Grave environmental impacts of GenAI training on the Nvidia A100 GPU. (bib: Falk2025)
- [33] Deutsche Forschungsgemeinschaft (DFG). Guidelines for Safeguarding Good Research Practice (Code of Conduct), guideline 17 on archiving (10 years). https://doi.org/10.5281/zenodo.14281892 (external, basis of the assumed 10-year retention; DFG 2025 *Nachhaltigkeit im Forschungsprozess* is in bib as DFG2025)

**Metadata standards (FAIR mapping, section 2)**

- [34] Open Energy Family. OEMetadata. https://github.com/OpenEnergyPlatform/oemetadata (bib: Hulk_Open_Energy_Family_2025)
- [35] Ferenz, S., Werth, O., Nieße, A. (2026). Towards a Metadata Schema for Energy Research Software. (bib: ferenz2026metadataschemaenergyresearch)
- [36] DDI Alliance. Data Documentation Initiative (DDI Codebook / DDI-Lifecycle). https://ddialliance.org (external)
- [37] schema.org. Dataset. https://schema.org/Dataset ; W3C. Data Catalog Vocabulary (DCAT). https://www.w3.org/TR/vocab-dcat-3/ (external)
- [38] Citation File Format (CFF). https://citation-file-format.github.io ; CodeMeta. https://codemeta.github.io (external)
