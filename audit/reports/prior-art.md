# Bounded prior-art audit — paused at user request

Date: 2026-11-14. Target: `paper/main.tex` and `README.md`, version 0.1.0 release preparation. This report records completed work only. Research stopped when the coordinator relayed the user's instruction to hold off on release. No manuscript, git, release, or public-site changes were made by this auditor. No email was accessed or sent. No Python workload was executed.

**Verdict: PARTIAL_PAUSED.** No exact antecedent of the every-cap cylinder-operator counterexample was found in the bounded material screened. That is not worldwide novelty clearance. The two topical Zenodo queries were not performed after access escalation was rejected; the separate Zenodo positive control did succeed. Several source comparisons remain at abstract or inherited-audit level. This report should not be treated as a completed P1 gate.

## Mechanisms and claims

The target is the unweighted positive operator `T = sum_v R_(1_Av)` on a laminar tree of measurable sets, with raw mass count `D(t) = #{v:nu(A_v)>t}`. Its principal claim combines: covering interval partitions, bounded finite branching, every prescribed child-ratio cap theta>0, D(t)~C/t, and a continuous nonconstant logarithmically periodic asymptotic for n(T;t)/D(t). The quantitative sequel takes the supremum of limit-set widths over admissible trees and obtains order theta as theta tends to zero.

| ID | Claim or comparison | Outcome | Decisive evidence / limit | Must-fix? |
|---|---|---|---|---|
| PA1 | Every-cap counterexamples in this exact unweighted operator class | No exact antecedent located in screened material | K26 is the explicit source of the question and credited operator facts; retrieved LL and fractal sources have different operators/observables. Search scope below is limited. | No mathematical defect established; P1 unfinished |
| PA2 | Continuous unsmoothed periodic law and harmonic cancellation criterion | Distinct within screened scope; generic periodicity is classical | KL and Rastegaev already supply periodic spectral asymptotics in other classes. The target explicitly restricts its Fourier criterion to its constructed phase-renewal family. | Preserve narrow wording |
| PA3 | Worst-case oscillation width Theta(theta) | No antecedent found, limited search | Retrieved sources do not formulate the same raw-mass ratio-cap extremal problem. No theorem-level literature sweep of all tree embeddings was completed. | Residual, not clearance |
| PA4 | Earlier cylinder compactness, sandwich and profile identities credited to K26 | Proper scope in the target | README credits Section 2; TeX F1–F4 cite K26. Prior draft audit had checked predecessor TeX. This auditor did not re-prove those facts. | No |
| PA5 | Log-periodicity/renewal and zeta correspondence are not generic new discoveries | CONFIRMED scope distinction | TeX related-work paragraph explicitly credits KL and fractal strings, disclaims cross-class priority, and distinguishes radial boundary limits from meromorphic continuation. | No |
| PA6 | Lifshits–Linde anchor DOI | ERROR in task packet, correction needed wherever used | Correct publisher DOI is **10.4064/sm202-1-2**, Studia Math. 202 (2011), 17–47. Requested `10.4064/sm202-1-1` is not the DOI of this paper. Corrected DOI used below and coordinator notified. This finding does not assert the manuscript still has the wrong DOI. | Check integrated bibliography |
| PA7 | Carleson/tree-Hardy results cannot simply be excluded by vocabulary | OPEN comparison | Identity `sum |integral_A f|^2 = sum m_A^2 |average_A f|^2` is precisely a Carleson embedding quadratic form. Norm/Schatten estimates alone do not determine the pointwise leading coefficient. A complete theorem-level comparison was not reached. | Named residual |
| PA8 | Search coverage meets full release P1 | GAP / incomplete | Successful GitHub controls, recent arXiv, Crossref, OpenAlex citation lists, AI-oriented searches and Zenodo control; topical Zenodo searches rejected and audit paused. | Yes if claiming P1 complete |

## Closest mechanisms actually inspected

1. **Kline 2026**, [version DOI](https://doi.org/10.5281/zenodo.23621017), [repository](https://github.com/jeff-kline/sparse-mertens-eigenvalue-law). The release README and TeX correctly identify this as the source of the cylinder operator, transfer results, and Question 7.1. The local predecessor `audit/PRIOR-ART.md` and prior-draft `claims-audit.md` were read as historical audit records, not substituted for primary verification. OpenAlex resolves the version DOI to a record whose canonical DOI is the concept DOI `23621016`; its locations include both DOIs. This is an indexing merge, not evidence that the version citation is wrong. K26 is explicitly AI-assisted in the established project context and was included rather than excluded for that reason.

2. **Lifshits–Linde**, [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/89345?download.pdf=), [correct DOI](https://doi.org/10.4064/sm202-1-2), [arXiv:1006.3867](https://arxiv.org/abs/1006.3867). The primary abstract and opening text were read. The operator maps ell_1(T) into ell_q(T), `(V_(alpha,sigma)x)(t)=alpha(t) sum_(s>=t) sigma(s)x(s)`. Its main stated objective is two-sided estimates for dyadic entropy numbers from a tree metric; it also treats Gaussian summation schemes. These are related summation mechanisms, but not directly an eigenvalue-count asymptotic for the target positive Hilbert-space operator. Entropy numbers must not be silently identified with singular values or their squares. PDF downloaded and text extracted to scratch, but further theorem-level reading was interrupted by the pause.

3. **Kigami–Lapidus 1993**, [DOI](https://doi.org/10.1007/BF02097233), *Weyl's problem for the spectral distribution of Laplacians on P.C.F. self-similar fractals*. The present target and prior draft audit distinguish lattice/nonlattice spectral scales combining energy and measure weights from raw cylinder masses. The prior audit reports primary inspection of Theorem 2.4 and Corollary 2.5; this auditor did not repeat that full primary check. [Gu–Qiu arXiv:2507.14858](https://arxiv.org/html/2507.14858v1), *BGD domains in p.c.f. self-similar sets II*, was opened as a recent follow-up but not fully screened before pause. Do not make a cross-class priority claim from differing terminology alone.

4. **Rastegaev 2024**, [publisher article](https://ems.press/content/serial-article-files/48815), [DOI](https://doi.org/10.4171/JST/528), [arXiv:2011.13064](https://arxiv.org/abs/2011.13064), *On the spectrum of the Sturm–Liouville problem with arithmetically self-similar weight*. Primary publisher search text for the introduction, Definition 2.3 and Theorem 2.4 was inspected. The spectral problem is `-y''=lambda mu y`; arithmeticity concerns products of measure weights and interval lengths. It gives a continuous periodic leading coefficient and proves nonconstancy for a broad self-similar ladder class with positive intermediate gaps. Thus continuity and nonconstancy of logarithmic spectral oscillation are established prior phenomena. It does not in the inspected text give the target's unweighted cylinder sum, the same raw-mass count, every-cap construction, or extremal order-theta width. Adding this source to a fuller related-work discussion would strengthen context, but absence is not presently established as a theorem-attribution defect. PDF downloaded and text extracted, then further review paused.

5. **Evans–Harris–Lang, Naimark–Solomyak, Bendikov–Grigor'yan–Pittet–Woess.** [EHL arXiv:math/0003215](https://arxiv.org/abs/math/0003215), [BGPW arXiv:1304.6271](https://arxiv.org/abs/1304.6271). Comparisons here are inherited from the predecessor audit, not independently completed in this run. Important distinctions to preserve: metric-tree edge measures versus boundary-supported measures; approximation/weak-Schatten estimates versus exact leading terms; hierarchical Laplacians with their own Haar-type diagonalization versus an unweighted indicator sum. Finite branching alone is not a universal exclusion argument. A full bridge or impossibility theorem between classes was not established.

6. **Carleson embedding.** The target's quadratic form is genuinely in this orbit. Crossref retrieved *Carleson embedding on the tri-tree and on the tri-disc*, [DOI 10.4171/rmi/1378](https://doi.org/10.4171/rmi/1378); title-level screening only. Searches retrieved analytic Hardy/Bergman embedding and Schatten criteria, but no inspected theorem implied the target law or counterexample. This remains an accepted candidate residual only if explicitly recorded; not a proved non-implication for all Carleson results.

7. **Public online mechanism note**, [MrlyProd, Weighted designs, raw source](https://mrly.net/raw/research/notes/weights.md), fully read as a public primary note. It studies fixed probability vectors on self-similar cells, distinguishes mass-stopping counts from length observables, and attributes the lattice/nonlattice mass-count dichotomy to [Lalley 1989](https://doi.org/10.1007/BF02392732). No cylinder-rank-one spectral count or every-cap theorem appears in the note read. Its AI authorship and first-publication date were not established; do not label it AI-generated or assign priority from crawl dates. It is relevant context for separating a raw-mass law from other observables, but not an exact antecedent found here.

## Dated search log

All requests below were made 2026-11-14. Counts are returned hits or bounded results, not claims of an exhaustive corpus. Web search totals are not exposed reliably; those rows say so. No keys, accounts or email were requested for OpenAlex.

| Service / query | Returned and screened scope | Result / access status |
|---|---|---|
| `gh search repos '"cylinder operator"' --limit 30` | 0 | Successful, weak exact-name negative |
| `gh search repos '"sparse-mertens"' --limit 30` | 3/3 descriptions | Positive repository control: jeff-kline/selberg-riccati-flow, sparse-mertens-singular-spectrum, sparse-mertens-eigenvalue-law |
| `gh search repos '"spectral asymptotics" tree' --limit 30` | 0 | Successful bounded negative |
| `gh search repos '"spectral" "AI" "tree"' --limit 10` | 0 | Successful, narrow AI-oriented negative |
| `gh search code '"cylinder operator"' --limit 30` | 12/12 result paths | VisIt help copies and engineering/UI files; no mathematical antecedent identified at path/context level; full files not read |
| `gh search code '"log-periodic" "mass"' --limit 30` | 0 | Successful bounded negative |
| `gh search code '"Carleson" "Schatten"' --limit 10` | 0 | Successful bounded negative |
| `gh search code '"numpy" repo:numpy/numpy path:README.md' --limit 3` | 0 | Failed positive control; not evidence of absence |
| `gh search code numpy --repo numpy/numpy --limit 3` | 3/3 paths | Successful replacement positive control: tools/list_numpy_dlls.sh and two documentation files. Demonstrates code search functioning, not complete indexing |
| Zenodo API `q="sparse Mertens"&size=10&sort=mostrecent` | total 4; response partially truncated after successful retrieval | Successful positive control includes K26 23621017 and older author records; not all metadata fully reviewed |
| Zenodo API `q="cylinder operator"&size=10&sort=mostrecent` | NOT PERFORMED | Initial DNS failure; subsequent escalation rejected by user; no retry |
| Zenodo API `q="log-periodic" AND tree&size=10&sort=mostrecent` | NOT PERFORMED | Escalation rejected by user; no retry |
| arXiv API `all:"tree" AND all:"spectral asymptotics"`, submittedDate descending, max_results=10 | total 5, all 5 abstracts screened | 2603.00344, 1503.06028, 1210.6190, 1006.1570, 0806.2014; random walks/graph Laplacians/random fractals/discrete tori, not exact operator |
| arXiv API `all:"log-periodic" AND (all:spectrum OR all:spectral)`, submittedDate descending, max_results=10 | total 63, 10 returned; display truncated, 8 entries substantially visible | Mostly physics/antennas. 2610.08487, *Kuznecov formulas for domains with fractal boundary*, is related log-periodic second-order Laplace-eigenfunction integral asymptotics; different observable. Do not claim all 10 abstracts screened |
| Crossref `query=Carleson embedding spectral asymptotics tree&rows=8&select=DOI,title,published` | total-results 554774; first 8 titles screened | Very noisy ranking; tri-tree Carleson title and continuum random tree paper identified. Other six results are broad spectral-asymptotic chapters. Not an exact phrase search |
| Web: `"Carleson embedding" "eigenvalues" tree spectral asymptotics`; `"tree" "mass" "log-periodic" spectrum`; `"Lifshits" "Linde" "202" "1" summation operators trees` | total unavailable; displayed results screened | LL primary PDF and MrlyProd note found; unrelated numerical/physics results excluded |
| Web: `"dyadic" "Schatten" "Carleson" embedding eigenvalues`; `"log-periodic" "tree" "Claude"`; `"regularly varying" "spectral" "mass" tree operator`; exact Rastegaev title | total unavailable; displayed results screened | Analytic-space Schatten criteria and Rastegaev; no exact target found |
| Web: `"cylinder operator" mathematics AI`; `"tree" "spectral asymptotics" "AI-assisted"`; `"Carleson" "eigenvalue asymptotics"`; `"weighted summation" "eigenvalues" tree` | total unavailable; displayed results screened | AI-math catalogue and Post-Cutoff indexes discovered; only result-page descriptions screened, underlying catalogue not searched before pause. Elliptic cylinder-operator hit arXiv:2611.01619 is a different operator |
| OpenAlex DOI resolutions | 3/3 successful | KL W1992478204; corrected LL W2073642689; K26 W7223444525 |
| OpenAlex citing KL: `filter=cites:W1992478204&sort=publication_date:desc&per-page=20&select=id,doi,title,publication_date` | count 259; newest 20 titles screened | Listed below. Anchor record's cached cited_by_count was 257; live query returned 259; use query count for this log |
| OpenAlex citing LL: `filter=cites:W2073642689&sort=publication_date:desc&per-page=25&select=id,doi,title,publication_date` | count 20; all 20 titles screened | Listed below; many function-space/entropy papers, not all source texts read |
| OpenAlex citing K26: `filter=cites:W7223444525&per-page=20&select=id,doi,title,publication_date` | count 0 | Successful empty indexed citation list; recent release/indexing lag is an obvious limitation |

The arXiv URLs are `https://export.arxiv.org/api/query` with the stated search query and sorting parameters. OpenAlex uses `https://api.openalex.org/works`; Crossref uses `https://api.crossref.org/works`; Zenodo uses `https://zenodo.org/api/records`. All were public read-only GET requests. A service notice suggested obtaining a key through email; that suggestion was ignored.

## Citation-list screening: Kigami–Lapidus

Bounded newest-first title screen, 20 of 259 indexed citing works. No claim that the remaining 239 were screened. DOI links identify exactly the returned records; primary text follow-up completed only to the extent noted above.

| Year | Returned title | DOI / screen disposition |
|---|---|---|
| 2026 | A Fractal Laplace Neural Transformation on Fractal Hilbert Space: An Application to the Oxygenation Cable Equation in Breast Cancer Dynamic Contrast-Enhanced Magnetic Resonance Imaging | [10.1016/j.apm.2026.117419](https://doi.org/10.1016/j.apm.2026.117419), application; title-screen excluded |
| 2026 | The growth of eigenfunction extrema on p.c.f. fractals | [10.1016/j.jfa.2026.111636](https://doi.org/10.1016/j.jfa.2026.111636), eigenfunction growth; source not inspected |
| 2026 | Construction of p-energy measures associated with strongly local p-energy forms | [10.1016/j.jfa.2026.111489](https://doi.org/10.1016/j.jfa.2026.111489), energy forms; source not inspected |
| 2026 | Krein-Feller operators on Riemannian manifolds: Compactness of embedding and Hodge's theorem | [10.1090/tran/9767](https://doi.org/10.1090/tran/9767), related compact embeddings; deferred |
| 2025 | Revisiting Microlocal Analysis: A Bridge Between Fractal Cohomology and Classical Function Spaces | [10.1177/09217134251335442](https://doi.org/10.1177/09217134251335442), title-screen only |
| 2025 | Spectral Exponents of Gap Diffusions on Random Homogeneous Cantor-Sets | [10.1007/978-3-031-80453-3_3](https://doi.org/10.1007/978-3-031-80453-3_3), related spectral exponents; deferred |
| 2025 | Green's function and eigenfunctions on random Sierpinski gaskets | [10.1090/conm/828/16595](https://doi.org/10.1090/conm/828/16595), related Laplacians; deferred |
| 2024 | Energy forms on fractals | [10.1360/ssm-2024-0275](https://doi.org/10.1360/ssm-2024-0275), title-screen only |
| 2024 | On the spectrum of the Sturm–Liouville problem with arithmetically self-similar weight | [10.4171/jst/528](https://doi.org/10.4171/jst/528), followed to primary text; comparison above |
| 2024 | Spectral triples and Dixmier trace representations of Gibbs measures: theory and examples | [10.1088/1361-6544/ad7009](https://doi.org/10.1088/1361-6544/ad7009), related spectral encoding; deferred |
| 2024 | A connection between discrete and regularized Laplacian determinants on fractals | [10.1088/1751-8121/ad59e3](https://doi.org/10.1088/1751-8121/ad59e3), determinants; title-screen only |
| 2023 | Gaps labeling theorem for the bubble-diamond self-similar graphs | [10.1088/1751-8121/ad03a4](https://doi.org/10.1088/1751-8121/ad03a4), graph spectral gaps; title-screen only |
| 2023 | Measurability, spectral densities, and hypertraces in noncommutative geometry | [10.4171/jncg/511](https://doi.org/10.4171/jncg/511), title-screen only |
| 2023 | Estimates for negative eigenvalues of Schrödinger operators on unbounded fractal spaces | [10.1090/tran/9005](https://doi.org/10.1090/tran/9005), different signed/unbounded problem |
| 2023 | Counting periodic orbits on fractals weighted by their Lyapounov exponents | [10.1017/s0013091523000287](https://doi.org/10.1017/s0013091523000287), different counting observable |
| 2023 | Weyl's asymptotic formula for fractal Laplacians defined by a class of self-similar measures with overlaps | [10.1007/s10476-023-0222-6](https://doi.org/10.1007/s10476-023-0222-6), relevant broader class; deferred |
| 2023 | Equivalence of Besov spaces on p.c.f. self-similar sets | [10.4153/s0008414x23000330](https://doi.org/10.4153/s0008414x23000330), function spaces |
| 2023 | L2-small ball asymptotics for Gaussian random functions: A survey | [10.1214/23-ps20](https://doi.org/10.1214/23-ps20), relevant survey; deferred |
| 2023 | Heat Kernel Fluctuations for Stochastic Processes on Fractals and Random Media | [10.1007/978-3-031-37800-3_12](https://doi.org/10.1007/978-3-031-37800-3_12), related fluctuations; deferred |
| 2022 | Existence of weak solutions to a p-Laplacian system on the Sierpinski gasket on R2 | [10.1007/s40590-022-00475-y](https://doi.org/10.1007/s40590-022-00475-y), nonlinear existence; title-screen excluded |

## Citation-list screening: Lifshits–Linde

All 20 returned indexed titles screened; source-level comparison is incomplete. The list includes duplicate preprint/published manifestations, and is not a deduplicated worldwide bibliography.

| Year | Returned title | DOI / screen disposition |
|---|---|---|
| 2024 | Boundedness of Gaussian Random Sums on Rooted Homogeneous Trees | [10.17323/1609-4514-2024-24-4-587-601](https://doi.org/10.17323/1609-4514-2024-24-4-587-601), closest probabilistic follow-up; deferred |
| 2021 | Sobolev improving for averages over curves in R4 | [10.1016/j.aim.2021.108089](https://doi.org/10.1016/j.aim.2021.108089), title-screen excluded |
| 2021 | Variation bounds for spherical averages | [10.1007/s00208-021-02218-2](https://doi.org/10.1007/s00208-021-02218-2), title-screen excluded |
| 2020 | Lp-Sobolev Estimates for a Class of Integral Operators with Folding Canonical Relations | [10.1007/s12220-020-00388-0](https://doi.org/10.1007/s12220-020-00388-0), title-screen excluded |
| 2019 | Boundedness of pseudo-differential operators of type (0,0) on Triebel–Lizorkin and Besov spaces | [10.1112/blms.12298](https://doi.org/10.1112/blms.12298), title-screen excluded |
| 2018 | Entropy Numbers of Embeddings of Function Spaces on Sets with Tree-Like Structure: Some Generalized Limiting Cases | [10.1134/s1061920818020103](https://doi.org/10.1134/s1061920818020103), relevant entropy setting; deferred |
| 2018 | On the boundedness of pseudo-differential operators on Triebel–Lizorkin and Besov spaces | [10.1016/j.jmaa.2017.12.065](https://doi.org/10.1016/j.jmaa.2017.12.065), title-screen excluded |
| 2016 | Entropy numbers of embedding operators of function spaces on sets with tree-like structure | [10.4213/im8555](https://doi.org/10.4213/im8555), relevant entropy setting; deferred |
| 2016 | Estimates for the widths of discrete function classes generated by a two-weight summation operator | [10.1134/s0081543816060201](https://doi.org/10.1134/s0081543816060201), relevant approximation setting; deferred |
| 2016 | Estimates for the entropy numbers of embedding operators of function spaces on sets with tree-like structure: Some limiting cases | [10.1016/j.jco.2016.05.001](https://doi.org/10.1016/j.jco.2016.05.001), relevant entropy setting; deferred |
| 2015 | Estimates for entropy numbers of embedding operators of function spaces on sets with tree-like structure: some limiting cases | [10.48550/arxiv.1506.03260](https://doi.org/10.48550/arxiv.1506.03260), preprint version; deferred |
| 2015 | Entropy numbers of embedding operators of weighted Sobolev spaces with weights that are functions of distance from some h-set | [10.48550/arxiv.1503.00144](https://doi.org/10.48550/arxiv.1503.00144), entropy setting; deferred |
| 2015 | Estimates for norms of two-weighted summation operators on a tree under some restrictions on weights | [10.1002/mana.201300355](https://doi.org/10.1002/mana.201300355), norm estimates; deferred |
| 2015 | Widths of weighted Sobolev classes with weights that are functions of the distance to some h-set: Some limit cases | [10.1134/s1061920815010136](https://doi.org/10.1134/s1061920815010136), approximation setting; deferred |
| 2014 | Embedding theorem for weighted Sobolev classes with weights that are functions of the distance to some h-set | [10.1134/s1061920814010075](https://doi.org/10.1134/s1061920814010075), embedding setting; deferred |
| 2013 | Widths of weighted Sobolev classes on a John domain: strong singularity at a point | [10.1007/s13163-013-0132-4](https://doi.org/10.1007/s13163-013-0132-4), approximation setting; deferred |
| 2013 | Embedding theorem for weighted Sobolev classes on a John domain with weights that are functions of the distance to some h-set | [10.1134/s1061920813030102](https://doi.org/10.1134/s1061920813030102), embedding setting; deferred |
| 2012 | Lebesgue space estimates for a class of Fourier integral operators associated with wave propagation | [10.1002/mana.201100256](https://doi.org/10.1002/mana.201100256), title-screen excluded |
| 2011 | Compactness properties of weighted summation operators on trees—the critical case | [10.4064/sm206-1-6](https://doi.org/10.4064/sm206-1-6), closest entropy follow-up; deferred |
| 2011 | Random Gaussian Sums on Trees | [10.1214/ejp.v16-871](https://doi.org/10.1214/ejp.v16-871), closest covariance context; deferred |

## Remaining work if the user resumes

- Finish the bounded source comparisons, especially LL's critical-case and Gaussian follow-ups, Carleson/tree-Hardy spectral asymptotics, and the most relevant titles above. A title-screen is a triage step, not proof of non-implication.
- Resolve the topical Zenodo search gap only within whatever authorization the user gives later. The earlier rejection is recorded; it was not bypassed.
- Check the corrected LL DOI in integrated citation surfaces; the independent citation auditor owns that lane.
- Review the new Rastegaev context and decide whether an explicit citation is useful. It narrows any broad novelty rhetoric but does not presently undermine the exact target theorem.
- A future completed novelty sentence may say: “Within the sources and searches recorded here, we did not locate this every-cap counterexample for the unweighted cylinder operator or the order-theta extremal width. Log-periodic spectral asymptotics themselves are classical.” It must retain the named residual comparisons and search limits.
- Repeat a fast-follow scan within seven days before tagging; this report does not authorize or recommend tagging now.

Not performed: MathSciNet, zbMATH, Google Scholar citing lists, a full AI-math-catalogue content scan, complete primary KL rereading, all 259 KL citations, full Carleson/Hardy theorem coverage, proof verification of the new manuscript, numerical reproduction, archive byte identity. Continued-fraction work was explicitly excluded and not pursued.

## Structured verdict

- `verdict: PARTIAL_PAUSED`
- `claim_groups_total: 8`
- `claim_groups_reported: 8`
- `exact_antecedents_identified: 0` (bounded inspected scope only)
- `bibliographic_error_identified: 1` (task-packet LL DOI; manuscript status not asserted)
- `open_process_gap: 1` (P1 incomplete)
- `open_comparison_group: 1` (Carleson/tree-Hardy/general related literature)
- `github_repository_positive_control: successful`
- `github_code_positive_control: successful_after_one_failed_scoped_control`
- `zenodo_positive_control: successful`
- `zenodo_topic_queries: NOT_PERFORMED_rejected`
- `citing_titles_screened: 40` (KL 20 of 259; LL 20 of 20; K26 0 of 0)
- `new_theorem_correctness_audited: false`
- `release_gate_closed: false`
- `stop_reason: user_requested_hold`
