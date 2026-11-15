# Novelty search: databases, 2026-11-14

Bounded, read-only, public GET requests only. Not a worldwide novelty claim.
Screening was at title level; abstracts were read only where stated.
Raw responses are in the agent scratchpad, not in the repository.

## Verdict

No source found in zbMATH Open, OpenAlex citation lists, the arXiv API or
five web searches states or implies R1 (every-cap log-periodic counterexample
and width of order theta), R2 (type-census transfer) or R3 (continued-fraction
law lambda_j ~ 6 log 2/(pi^2 j) for the common-cylinder kernel). Closest
neighbours (below) treat different operators (Laplacians on metric trees,
Hardy/summation operators with order or entropy estimates, Krein-Feller
operators, the Gauss-Kuzmin-Wirsing transfer operator). Coverage is thin:
zbMATH search is conjunctive and many multi-word queries returned 0, and
Google Scholar and MathSciNet were not performed. Residuals are listed at the end.

## Overlap table

| Source | What it proves | Contains or implies R1/R2/R3? | Access |
|---|---|---|---|
| Evans-Harris-Lang 2001, "The approximation numbers of Hardy-type operators on trees" (Proc. LMS 83, OpenAlex W2069687788) | Approximation-number estimates for Hardy-type operators on trees | No R1/R2/R3. Operator is a weighted Hardy (summation) operator, estimates not exact asymptotics of a nested-set Gram operator. Not read beyond title. | title |
| Naimark-Solomyak 2000, "Eigenvalue estimates for the weighted Laplacian on metric trees" (Proc. LMS 80, W1967531259) | Eigenvalue estimates for Laplacians on metric trees | No. Laplacian, not Gram of nested cylinder indicators; no log-periodic tree-count law seen. | title |
| Lifshits-Linde, "Compactness properties of weighted summation operators on trees" (zbMATH 5836411; arXiv 1006.3867) and "...critical case" (zbMATH 5959231) | Two-sided entropy-number estimates for weighted summation operators l1 to lq on trees; Gaussian summation schemes | No. Order-of-magnitude estimates in entropy numbers, not exact eigenvalue asymptotics or oscillation. | abstract (arXiv) |
| Evans-Harris-Lang citers: Strict s-numbers of weighted Hardy type operators on trees (2024, W4411451176); two-weight summation operator norm and width papers (W2592597920, W2532077043, W1497880633) | s-number equalities; norm and width estimates | No. | abstract (first three), title (last) |
| Kigami-Lapidus 1993 (zbMATH 490661) | Weyl asymptotics on p.c.f. fractals, with oscillating factor in general | No R1/R2/R3 (Laplacian on a fractal). Already in PRIOR-ART. Positive control hit. | title and zbMATH review snippet |
| Kajino, log-periodic expansions on p.c.f. sets (web hit, Bielefeld SFB 701 preprint) | Log-periodic terms in spectral partition functions | No. Self-similar Laplacian setting. Not opened. | search snippet |
| Krein-Feller operators for V-variable Cantor measures (arXiv 1808.06950) | Eigenvalue counting function asymptotics for d/dmu d/dx, random Cantor measures | No. Operator is Krein-Feller, not a tree Gram operator. | abstract |
| Ornstein-Uhlenbeck semigroup on rooted trees (arXiv 2606.31713, 2026; cites Naimark-Solomyak) | Linear eigenvalue asymptotics for OU operators on metric trees with Gaussian measure | No. Differential operator on metric tree. | abstract (OpenAlex) |
| Alkauskas, GKW eigenvalue asymptotics (web hit); zbMATH 5656556 (Minkowski ? function dyadic period function) | Gauss-Kuzmin-Wirsing transfer operator eigenvalue and moment results | No R3. Transfer operator, not the Gram kernel of CF cylinders. | search snippet only |
| Zbmath Croydon-Hambly 2008, 2010 (5268522, 5946950) | Spectral asymptotics for continuum random and stable trees | No. Laplacians on random real trees. | title |

## Search log

All dated 2026-11-14. zbMATH base: `https://api.zbmath.org/v1/document/_search?search_string=<q>&page=0&results_per_page=20`.
Note the API returns HTTP 404 with "No results found" for zero hits, 502/503 under load.
Screened means titles read.

| # | Database | Query / URL | Total | Screened | Result |
|---|---|---|---|---|---|
| 1 | zbMATH | `ti:Weyl's problem for the spectral distribution of Laplacians on p.c.f. self-similar fractals` | 1 | 1 | Positive control: Kigami-Lapidus 1993 found |
| 2 | zbMATH | `ti:Compactness properties of weighted summation operators on trees` | 2 | 2 | Positive control: Lifshits-Linde, both papers found |
| 3 | zbMATH | `eigenvalue asymptotics tree nested sets` | 0 (404) | 0 | Zero hits |
| 4 | zbMATH | `cylinder eigenvalue tree covariance` | 0 (404) | 0 | Zero hits |
| 5 | zbMATH | `Carleson embedding tree eigenvalue` | 0 (404) | 0 | Zero hits |
| 6 | zbMATH | `summation operator tree singular numbers` | 0 (404) | 0 | Zero hits |
| 7 | zbMATH | `continued fraction cylinder eigenvalue` | 3 | 3 | Mathieu/oscillator numerics; none relevant |
| 8 | zbMATH | `continued fraction cylinder kernel` | 2 | 2 | Alkauskas Minkowski ? paper; none relevant |
| 9 | zbMATH | `log-periodic spectral asymptotics regularly varying` | 0 (404) | 0 | Zero hits |
| 10 | zbMATH | `hierarchical Gaussian Karhunen-Loeve eigenvalue tree` | NOT PERFORMED | - | HTTP 502 on request |
| 11 | zbMATH | `Gauss measure kernel eigenvalues continued fraction` | NOT PERFORMED | - | HTTP 502 on request |
| 12 | zbMATH | `Karhunen-Loeve tree eigenvalue` | 1 | 1 | A conference volume; not relevant |
| 13 | zbMATH | `Gauss measure continued fraction eigenvalues` | 1 | 1 | Arnold, orbit statistics; not relevant |
| 14 | zbMATH | `hierarchical Gaussian eigenvalue tree` | 3 | 3 | None relevant |
| 15 | zbMATH | `Carleson embedding tree` | 11 | 11 | Bellman function / bi-tree Carleson embedding (Arcozzi, Holmes, Mozolyako, Volberg; Pereyra); none about eigenvalues |
| 16 | zbMATH | `summation operator tree singular` | 0 (404) | 0 | Zero hits |
| 17 | zbMATH | `cylinder sets eigenvalues tree` | 1 | 1 | Equadiff proceedings volume; not relevant |
| 18 | zbMATH | `log-periodic eigenvalue asymptotics` | 0 (404) | 0 | Zero hits |
| 19 | zbMATH | `oscillating eigenvalue asymptotics tree` | 1 | 1 | Same proceedings volume; not relevant |
| 20 | zbMATH | `tree-indexed Gaussian small deviation eigenvalue` | 0 (404) | 0 | Zero hits |
| 21 | zbMATH | `Gram operator nested sets eigenvalue` | 0 (404) | 0 | Zero hits |
| 22 | zbMATH | `continued fraction kernel eigenvalues` | 2 | 2 | Stesin 1959; Debosscher 1998; not relevant |
| 23 | zbMATH | `continued fraction Gram eigenvalue` | NOT PERFORMED | - | 404 body was not parsed as JSON in my script; result file unusable, not recorded as "no hits" |
| 24 | zbMATH | `eigenvalue asymptotics tree` | 22 | 20 | Sobolev-Solomyak, Croydon-Hambly, Kigami-Lapidus, quantum-tree papers; none about nested-set Gram operators |
| 25 | zbMATH | `Hardy inequality tree approximation numbers` | NOT PERFORMED | - | Response unusable (same parse failure as #23) |
| 26 | MathSciNet | - | NOT PERFORMED | - | Subscription required; no login attempted |
| 27 | Google Scholar | WebFetch `https://scholar.google.com/scholar?q="eigenvalues"+"continued fraction"+"cylinder sets"+kernel` | NOT PERFORMED | - | Blocked: 302 redirect to google.com/sgsync, not followed |
| 28 | WebSearch | `"eigenvalues" "continued fraction" "cylinder sets" kernel operator common prefix` | n/a | 10 | GKW operator pages, Alkauskas; no kernel with common-prefix structure |
| 29 | WebSearch | `"mass count" eigenvalue counting function tree operator nested sets log-periodic` | n/a | 10 | Krein-Feller V-variable Cantor, Sobolev-Solomyak, Kajino; none match |
| 30 | WebSearch | `Karhunen-Loeve hierarchical tree covariance eigenvalues "log-periodic" oscillation asymptotics` | n/a | 10 | OU tree models (1306.1322), fBm KL asymptotics; none match |
| 31 | WebSearch | `"small deviations" Gaussian tree-indexed "summation operator" eigenvalue asymptotics` | n/a | 10 | Lifshits-Linde 1006.3867, small-ball surveys; none give exact eigenvalue asymptotics |
| 32 | OpenAlex | `https://api.openalex.org/works/doi:10.1112/plms/83.2.390` | 1 | 1 | Resolves to W2069687788 (Evans-Harris-Lang), 32 citing works |
| 33 | OpenAlex | `works?filter=cites:W2069687788&sort=publication_date:desc&per-page=25` | 32 | 25 (newest) | Hardy/summation/width papers; abstracts read for 4; none relevant |
| 34 | OpenAlex | search "Eigenvalue estimates for the weighted Laplacian on metric trees" | n/a | 6 | Resolves Naimark-Solomyak 2000 to W1967531259 |
| 35 | OpenAlex | `works?filter=cites:W1967531259&sort=publication_date:desc&per-page=25` | 86 | 25 (newest) | Metric-tree Laplacians/quantum graphs; abstract read for the 2026 OU-tree paper; none relevant |
| 36 | arXiv API | `all:"tree-indexed" AND all:"Karhunen"` | 0 | 0 | Zero hits |
| 37 | arXiv API | `all:"summation operator" AND all:tree AND all:asymptotics` | 0 | 0 | Zero hits |
| 38 | arXiv API | `all:"hierarchical" AND all:"Gaussian" AND all:"eigenvalue asymptotics"` | 0 | 0 | Zero hits |
| 39 | arXiv API | `all:"continued fraction" AND all:"Gram"` | 1 | 1 | 2606.10141, 't Hooft model exceptional points; not relevant |

## Residuals

- OpenAlex citing lists were screened for the 25 newest of 32 and 86 works only.
- The zbMATH search engine is conjunctive and many zero results (404) reflect
  strict term matching, so they are weak evidence. Queries #23 and #25 and
  #10, #11 produced no usable result.
- Google Scholar and MathSciNet were not searched.
- Web-search hits (Kajino, Alkauskas) were seen as snippets only.
- Carleson-embedding-on-trees literature was screened at title level only; no
  spectral theorem was checked.
