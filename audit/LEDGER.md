# Audit ledger — version 0.1.0

Append-only. Every audit was run by an AI system: a separate process with a
fresh context, or the root (integrating) agent. None is peer review, and no
independent human expert has examined the proofs.

## Audits

| Date | Scope | Auditor | Report | Verdict |
|---|---|---|---|---|
| 2026-11-14 | Assembled manuscript through Section 8 and the zeta corollary, claim by claim (M01–M31) | process-separated AI auditor | [reports/proof.md](reports/proof.md) | PASS; 0 must-fix, 1 cosmetic |
| 2026-11-14 | Prior art, first bounded pass (stopped when release work was paused) | process-separated AI auditor | [reports/prior-art.md](reports/prior-art.md) | PARTIAL_PAUSED |
| 2026-11-14 | Section 9 (Theorems 9.1 and 9.2, Lemma 9.3, the "(T2) fails" paragraph) and the new prose | process-separated AI auditor, cold | [reports/proof-section9.md](reports/proof-section9.md) | math VERIFIED; prose OVERSTATED (4 must-fix) |
| 2026-11-14 | Prior-art fast-follow scan (Zenodo, GitHub, arXiv, OpenAlex, web) | process-separated AI auditor | [reports/prior-art-scan-2026-11-14.md](reports/prior-art-scan-2026-11-14.md) | no antecedent in screened corpus |
| 2026-11-14 | Claims consistency across README, paper, CITATION.cff and CORRECTIONS | process-separated AI auditor | [reports/claims-consistency.md](reports/claims-consistency.md) | PASS WITH FIXES; 1 must-fix, fixed |

Earlier development audits of the counterexample are kept in the research
workspace and are not part of this package: a cold examination, a proof
audit, and a strengthening pass. The checks in `reports/proof.md` supersede
them for the released text.

## Findings and dispositions

Each finding is labelled with one of: error, gap, missing hypothesis,
sharpening, documentation.

| ID | Source | Label | Finding | Disposition |
|---|---|---|---|---|
| L1 | prior-art PA6 | error | Lifshits–Linde DOI given as `10.4064/sm202-1-1`, which belongs to Pramanik–Rogers–Seeger; Crossref check | Fixed: `10.4064/sm202-1-2` |
| L2 | owner review | documentation | Rastegaev 2024 not cited, although it proves nonconstant periodic spectral leading terms | Fixed: cited and contrasted in Section 10 and the README |
| L3 | zeta audit | documentation | "Pole" used for radial limits; zero residue described as a pole | Fixed before this package: radial-limit wording and "whenever $c_n\ne0$" |
| L4 | zeta audit | documentation | The Gaussian-field reading needs qualification because $T$ has infinite trace | Fixed: field defined through test functions |
| L5 | proof-section9, 6a | missing hypothesis | Abstract, introduction and Section 9 opener omitted regular variation and the continuity hypothesis (T3). A single-type lattice tree (split 1/2, 1/4, 1/4) satisfies the census but not the law | Fixed in all three places, the README and CITATION.cff |
| L6 | proof-section9, 5 | error | "Sorting coprime pairs" mis-described the gcd rewriting of $\zeta_D$ | Fixed: "writing each pair $q>p\ge1$ as $d$ times a coprime pair" |
| L7 | proof-section9, 6b; root check of the earlier paper | documentation | Nonvanishing ratios compatible with the law were already shown by the earlier paper's Proposition B.1 (stationary trees); the continued-fraction example was presented as if it showed this first | Fixed: credit added to the introduction, Section 9, Section 10 and the README "Not new" list; the continued-fraction tree is presented as a continuum-of-types example |
| L8 | proof-section9, 4 | gap | Borel measurability of $\xi$ not stated; the local-constancy sentence was loose | Fixed: explicit $\delta$ argument and Borel clause |
| L9 | proof-section9, 5 | documentation | The $\zeta_T$ sentence for the continued-fraction tree relied on a corollary stated for $\cyl_{r,k}$ | Fixed: the text says the proof of the vertex formula applies |
| L10 | proof-section9, 6c, 6d | documentation | Open question (5) wording; Rastegaev sentence lacked "asymptotically" | Fixed |
| L11 | root review | documentation | README linked missing files; release status line said "paused" | Fixed: VERIFICATION.md, ADMISSION.md and this ledger added; status updated |
| L12 | hygiene scan | documentation | A local interpreter path in `reports/proof.md` and scratch paths in `reports/proof-section9.md` | Redacted, marked "[local path redacted for release]"; the scratch checks are marked unreproduced |

| L13 | claims-consistency ID 1 | error | README said the earlier paper asked whether "either hypothesis" can be dropped; its Question 7.1 asks whether regular variation alone suffices | Fixed |
| L14 | claims-consistency ID 6, 5, 7 | missing hypothesis | "No further condition on the ratios" omitted the standing cap $\theta<1$; CITATION.cff omitted "compact" | Fixed in abstract, README, CITATION.cff |
| L15 | claims-consistency ID 8 | sharpening | "The counterexamples fail the distribution hypothesis" | Reworded: the type distribution oscillates (the paper proves this for the phase types and, by contraposition, for every typing with (T1) and (T3)) |
| L16 | claims-consistency ID 3, 4, 11, 12 | documentation | Credit wording for Kigami–Lapidus and Rastegaev; sandwich inequality location; "non-arithmetic" omitted; "mass count" and "regularly varying" undefined in README | Fixed |
| L17 | claims-consistency ID 13 | documentation | Paper lacked the predecessor's "Role of AI" paragraph | Fixed: added at the end of Section 10 |
| L18 | claims-consistency ID 9 | documentation | Abstract summarizes the earlier question as dropping "the condition on the ratios" | Kept: approved abstract wording, accurate in context (drop the ratio condition without adding the profile hypotheses) |
| L19 | claims-consistency ID 10, 15, 16 | documentation | Table's $Q^0$ range (1.19) vs $Q_4$ range (1.20) not distinguished in the caption; CORRECTIONS wording; naming boundary points | Not changed; optional |

## Release-work history

- 2026-11-14: release preparation began, then was paused by the author.
  Nothing was committed or published.
- 2026-11-14: the author authorized resuming the release, the Zenodo and
  fast-follow scans, and the slug `regularly-varying-mass-counts`. The
  positive section (Section 9) was added beforehand at the author's request.
