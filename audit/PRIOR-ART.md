# Prior-art record — version 0.1.0

Consolidated 2026-11-14. This is a bounded comparison, not a worldwide
novelty claim. The raw reports are:

- [reports/prior-art.md](reports/prior-art.md): the first bounded audit,
  stopped when release work was paused. It covers anchor sources, citation
  lists, GitHub, arXiv and Crossref.
- [reports/novelty-theorem-comparison-2026-11-14.md](reports/novelty-theorem-comparison-2026-11-14.md):
  theorem-level comparison with tree Carleson embeddings, Hardy and
  summation operators on trees, metric-tree Laplacians, self-similar
  Sturm–Liouville problems and ultrametric operators (primary texts read
  for Arcozzi–Rochberg–Sawyer, Evans–Harris–Lang, Naimark–Solomyak,
  Lifshits–Linde and Khrennikov–Kozyrev).
- [reports/novelty-databases-2026-11-14.md](reports/novelty-databases-2026-11-14.md):
  zbMATH Open API, OpenAlex citing works of Evans–Harris–Lang and
  Naimark–Solomyak, arXiv API and web searches; MathSciNet and Google
  Scholar NOT PERFORMED (subscription; blocked).
- [reports/prior-art-scan-2026-11-14.md](reports/prior-art-scan-2026-11-14.md):
  the fast-follow scan after the positive section was added. It covers Zenodo,
  GitHub, arXiv, OpenAlex citation lists and web searches.
- The supplementary Zenodo queries and the source checks below.

## Claims compared

| ID | Claim | Closest sources compared | Outcome |
|---|---|---|---|
| R1 | Every-cap counterexample: bounded branching, ratios at most $\theta$, $D(t)\sim C/t$, and $\mathsf n(T;t)/D(t)$ asymptotically a nonconstant log-periodic function (Theorem 1.2), with periodic law, Fourier test and boundary limits (Theorem 5.2, Corollaries 5.3–5.4) | Kline 2026 (source of the question); Kigami–Lapidus 1993; Rastegaev 2024; Lapidus–van Frankenhuijsen 2013; Evans–Harris–Lang; Naimark–Solomyak; Lifshits–Linde; Bendikov–Grigor'yan–Pittet–Woess | Not found in the screened sources. Log-periodic, nonconstant leading spectral terms are known for self-similar operators: Kigami–Lapidus, and Rastegaev, whose arXiv text (introduction and Theorem 2) was checked. They are credited. The new point is oscillation of the eigenvalue count of one operator while its own mass count has a constant leading term. |
| R1″ | The operator itself | Arcozzi–Rochberg–Sawyer 2002 (tree Carleson measures), primary text of the 2007 simple-proof version read | $V$ is their discrete Hardy operator into $L^2$ of a boundary measure, and $T=VV^*$; their tree condition characterizes boundedness. They give no eigenvalue asymptotics. Credited in the paper's Setting and the README |
| R1‴ | Renewal-driven periodic eigenvalue counts on trees | Naimark–Solomyak 2000, Example 8.1, primary text read | Eigenvalue count $\lambda^{-\delta}w(\ln\lambda^{-1})$ with $w$ periodic for symmetric weighted Laplacians on homogeneous metric trees; nonconstancy not asserted; the operator splits into one-dimensional problems. Credited in Section 10 and the README |
| R1′ | Largest oscillation width of order $\theta$ (Corollary 6.3) | Same | No formulation of this extremal problem found. |
| R2 | Type-census transfer (Theorem 9.1) | Kline 2026, Theorem A.4 (finitely many classes, approximate profiles) and Proposition B.1 (stationary trees) | A continuum-of-types counterpart of Theorem A.4. The method (weak convergence) is standard and no priority is claimed for it. Proposition B.1 already shows that nonvanishing ratios are compatible with the law; the paper and README credit this. |
| R3 | Continued-fraction law $\lambda_j\sim6\log2/(\pi^2j)$ (Theorem 9.2) | Clément–Flajolet–Vallée 2001 (INRIA RR-3645, §8.3, printed pp. 55–57, read in full text); Einsiedler–Ward Ch. 3 (contents only); Gauss–Kuzmin–Wirsing transfer-operator literature | CFV treat the cylinder lengths, their Dirichlet series (related to $\zeta(2s-1)/\zeta(2s)$), and the entropy $\pi^2/(6\log2)$; these are credited. Transfer-operator eigenvalues concern a different operator. No statement of the eigenvalue law for this cylinder operator was found. |

## Supplementary Zenodo queries (2026-11-14)

Zenodo search is OR by default, so plain multi-word queries return recent
unrelated records. These queries use required terms (`+`) and
`sort=bestmatch` against `https://zenodo.org/api/records`.

| Query | Total | Result |
|---|---|---|
| `+"cylinder" +"rank-one" +eigenvalue +tree` | 1 | Kline 2026 (record 23621017), the predecessor. Positive control for the syntax. |
| `+"log-periodic" +eigenvalue +tree` | 0 | — |
| `+"continued fraction" +eigenvalue +cylinder` | 0 | — |
| `+"Carleson embedding" +eigenvalue` | 0 | — |
| `+"spectral asymptotics" +tree` | 0 | — |
| `+"continued fraction" +"covariance operator"` | 0 | — |
| `+"continued fraction" +eigenvalues` | 24 | 15 titles screened; physics and numerology records, none relevant |
| `+"log-periodic" +spectral` | 86 | 15 titles screened; physics records, none relevant |
| `+"regularly varying" +eigenvalue` | 2 | both screened; neither relevant |

## Residuals (named, not counted as negative evidence)

- MathSciNet (subscription) and Google Scholar (blocked): NOT PERFORMED.
  zbMATH Open was searched through its public API. Its conjunctive search
  makes zero-hit queries weak evidence, and two requests failed with
  HTTP 502 before a retry.
- **Carleson embeddings on trees.** Compared at theorem level with
  Arcozzi–Rochberg–Sawyer (boundedness only). No Schatten-class or
  exact-asymptotic theorem for tree embeddings was found; a Luecking-type
  Schatten criterion, if one exists, would give membership only.
- **Kigami–Lapidus.** The comparison is at the level of Theorem 2.4 and
  Corollary 2.5, as recorded by an earlier audit; this pass did not re-read
  the full text.
- **Lapidus–van Frankenhuijsen.** The chapter pinpoint (Chapters 2–3)
  comes from the table of contents. The substance was checked against the
  authors' primary paper on self-similar strings.
- **Abstract-only screening.** Most citing-work and search hits were
  screened at title or abstract level only. The code-search hits in
  `linas/fractal` were not opened.
- **Freshness.** The fast-follow scan is dated 2026-11-14 and must be
  repeated if tagging happens after 2026-11-21.

## Verdict

**P1: PARTIAL.** No source read contains or implies R1, R1′, R2 or R3. The
residuals above are named, and a tag requires the author to accept them.
