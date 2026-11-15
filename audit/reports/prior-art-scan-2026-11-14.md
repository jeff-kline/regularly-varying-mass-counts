# Prior-art and fast-follow scan, 2026-11-14

Scope: screen R1 (cylinder operator; log-periodic counterexample), R2 (type-census transfer theorem), R3 (continued-fraction cylinder kernel, lambda_j ~ 6 log 2/(pi^2 j)). Bounded scan; titles and abstracts only unless stated. I did not read the paper; the R1-R3 statements are taken from the task brief.

## Verdict

No antecedent found for R1-R3 in the screened corpus. This is not a claim of worldwide novelty. Search coverage was shallow: most Zenodo and GitHub phrase queries returned 0 hits or noise, and no full texts were read.

## Plausible overlaps (all screened by title/abstract; none contains or implies R1-R3)

| Item | Why surfaced | Disposition |
|---|---|---|
| arXiv 1811.05246 / 1812.01039, kernel 1/2 + floor(1/xy) - 1/xy (Mertens identity) | Gauss-map-flavored kernel eigenvalues | Abstract (read): infinitely many positive and negative eigenvalues; no CF cylinder tree, no asymptotic rate. Different kernel and question. No overlap. |
| arXiv 1210.4083 and 1004.1783, Gauss-Kuzmin-Wirsing transfer operator eigenvalues (via WebSearch) | CF dynamics eigenvalues | Transfer operator, not a covariance/cylinder-Gram operator; eigenvalues decay geometrically. Different object. Excerpts only. |
| arXiv 1006.1570, spectral asymptotics for stable trees (Croydon-Hambly) | Renewal argument, nested-piece eigenvalue comparison | Metric-tree Laplacian; not rank-one cylinder operators. Same flavor as the credited Kigami-Lapidus line. Snippet only. |
| arXiv 2601.03738, "A glimpse into the Ultrametric spectrum" | log-periodic + tree + eigenvalue hit | Hep-th; p-adic derivative eigenvalues with log-periodic modulation of the degeneracy count. Abstract read. No overlap. |
| arXiv 1610.03292, hierarchical Laplacian on ultrametric spaces | Tree/ultrametric spectral asymptotics | Same family as the credited Bendikov-Grigor'yan-Pittet-Woess line (inference from title and snippet). Snippet only. |
| arXiv 1612.01002, ultrametric spectra of weighted tree ensembles | "Weighted census" wording | Adjacency spectra of tree ensembles; not a mass-count transfer theorem. Snippet only. |
| Kajino (CMP 328, 2014), log-periodic expansion of the spectral partition function for self-similar sets | log-periodic counting-function precedent | Self-similar sets; the log-periodicity there comes from exact self-similarity. R1 concerns bounded-branching trees with mass count ~ C/t and a nonconstant limit ratio. Context only. Snippet only. |
| OpenAlex W2053183761 (Clement-Flajolet-Vallee), 102 citing works | credited | Newest 25 citing titles are all trie/algorithms papers. None related to spectra. |

## Observations

- The predecessor K26 has 0 citing works in OpenAlex (fresh). Its DOI 10.5281/zenodo.23621017 resolved to OpenAlex W7223444525, whose recorded DOI is 10.5281/zenodo.23621016, so that is probably the concept/version sibling record.
- Zenodo positive control (quoted "sparse Mertens") returned the 4 Kline records, so the API and quoted-phrase search work. The first, unquoted control returned unrelated recent records.
- arXiv has no "sparse Mertens" records (0 hits). The arXiv control therefore proves nothing about coverage of Kline's work, since those works are on Zenodo and GitHub only.
- GitHub positive control (`gh search repos sparse-mertens`) returned 4 jeff-kline repos.
- Quoted-phrase GitHub code searches returned noisy hits (e.g. TauCeti, linas/fractal). I screened only the beginning of the output (about 5-8 paths per query) and did not inspect them in detail. The `linas/fractal` hit is a generic fractal repository that matched on the CF terms; I did not look inside it.

## Search log (all dated 2026-11-14)

Zenodo: https://zenodo.org/api/records, size=20, sort=mostrecent. "Screened" = titles of the returned 20 (or all, if fewer).

| # | Query | Total | Screened | Result |
|---|---|---|---|---|
| Z0 | sparse Mertens (unquoted) | 49547 | 20 | Control failed in this form (loose OR matching; no Kline records in newest 20). Re-run as Z10. |
| Z10 | "sparse Mertens" | 4 | 4 | Control passed: 4 Kline records (incl. 23621017). |
| Z1 | cylinder operator (unquoted) | 42451 | 20 | Noise; no relevant. |
| Z11 | "cylinder operator" | 0 | 0 | No hits. |
| Z2 | "log-periodic" AND tree AND eigenvalue | 0 | 0 | 0 returned (Boolean syntax may have been parsed oddly; treat as weak). |
| Z16 | "log-periodic" AND tree AND eigenvalue (repeat) | 0 | 0 | Same as Z2. |
| Z12 | "log-periodic" tree eigenvalue | 107463 | 20 | Loose matching; noise; none relevant. |
| Z3 | "continued fraction" AND eigenvalue AND cylinder | 0 | 0 | 0 returned (same caveat). |
| Z13 | "continued fraction" eigenvalue cylinder | 10292 | 20 | Noise; none relevant. |
| Z4 | "Carleson embedding" AND eigenvalue | 0 | 0 | 0 returned (same caveat). |
| Z14 | "Carleson embedding" eigenvalue | 5453 | 20 | Noise; none relevant. |
| Z5 | "spectral asymptotics" AND tree | 0 | 0 | 0 returned (same caveat). |
| Z15 | "spectral asymptotics" tree | 101883 | 20 | Noise; none relevant. |

GitHub (`gh search`, limit 20):

| # | Command | Total | Screened | Result |
|---|---|---|---|---|
| G1 | repos sparse-mertens (control) | 4 | 4 | Control passed. |
| G2 | repos "cylinder operator" eigenvalue | 0 | 0 | No hits. |
| G3 | repos "continued fraction" cylinder eigenvalue | 0 | 0 | No hits. |
| G4 | repos "log-periodic" "eigenvalue count" | 0 | 0 | No hits. |
| G5 | repos "mass count" spectral tree | 0 | 0 | No hits. |
| G6 | code "cylinder operator" eigenvalue | 20 | partial (about 8 paths) | Unrelated (Lean/Floer, physics). |
| G7 | code "continued fraction" "cylinder" eigenvalue | 20 | partial (about 8 paths) | Unrelated (keyword lists, CFD, Special-functions TODO; linas/fractal not inspected). |
| G8 | code "log-periodic" "eigenvalue count" | 20 | partial (about 8 paths) | Unrelated (physics, numerology repos). |
| G9 | code "mass count" spectral tree | 20 | partial (about 6 paths) | Unrelated. |

arXiv: https://export.arxiv.org/api/query, sortBy=submittedDate descending, max_results=20. The first attempt on http:// returned 301 and was NOT PERFORMED; all rows below are the https re-runs.

| # | Query | Total | Screened | Result |
|---|---|---|---|---|
| A1 | all:"continued fraction" AND all:eigenvalue AND all:cylinder | 0 | 0 | No hits. |
| A2 | all:"log-periodic" AND all:eigenvalue AND all:tree | 1 | 1 | 2601.03738 (ultrametric string spectrum); no overlap. |
| A3 | all:"Carleson embedding" AND all:"eigenvalue asymptotics" | 0 | 0 | No hits. |
| A4 | all:"covariance operator" AND all:"continued fraction" | 0 | 0 | No hits. |
| A5 | all:"sparse Mertens" (fast-follow) | 0 | 0 | No hits (arXiv has none of the predecessor work). |
| A6 | all:"cylinder operator" (fast-follow) | 7 | 7 | All physics/engineering; none relevant. |
| A7 | all:Mertens AND all:eigenvalue AND all:kernel | 2 | 2 | 1811.05246, 1812.01039 (see table). |
| A8 | all:nested AND all:"rank-one" AND all:eigenvalue AND all:tree | 0 | 0 | No hits. |

Since 2026-10-24 on arXiv: no work citing or building on "sparse Mertens" or "cylinder operator" appears among A5 and A6. Caveat: arXiv full-text citations are not searchable through this API.

OpenAlex:

| # | Query | Total | Screened | Result |
|---|---|---|---|---|
| O1 | filter=cites:W7223444525 (K26, resolved from DOI 10.5281/zenodo.23621017) | 0 | 0 | No citing works indexed. |
| O2 | filter=cites:W2053183761 (CFV, DOI 10.1007/BF02679623), newest 25 | 102 | 25 | All trie/algorithm/analytic-combinatorics papers; none relevant. |

WebSearch (standard mode):

| # | Query | Result |
|---|---|---|
| W1 | eigenvalues of kernel continued fraction expansions common prefix length eigenvalue asymptotics 6 log 2 / (pi^2 j) | Did not confirm the R3 asymptotic; surfaced only GKW transfer-operator papers (1210.4083, 1004.1783) and CF-statistics papers. No antecedent. |
| W2 | Gauss map covariance operator cylinder sets eigenvalue asymptotics Karhunen-Loeve continued fraction digits | No source defines a covariance kernel on CF cylinders. No antecedent. |
| W3 | eigenvalue counting function tree nested sets rank-one projections log-periodic oscillation dyadic Carleson embedding spectral asymptotics | Fractal log-periodic literature (Kajino, stretched gasket, stable trees); none with rank-one/Carleson formulation. No antecedent for R1. |
| W4 | eigenvalue asymptotics ultrametric kernel hierarchical tree operator counting function weighted census of subtree types | Ultrametric/tree spectra (1610.03292, 1612.01002, math/0109016); no type-census transfer theorem. No antecedent for R2. |

Not done: no full-text reads, no MathSciNet/zbMATH or Google Scholar queries, no GitHub code search beyond the first page.
