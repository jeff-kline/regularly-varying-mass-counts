# Admission record

**Current state:** DRAFT (candidate preparation)

**Version:** 0.1.0

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Current verdict: NOT YET ADMITTED (local candidate; no tag, archive or DOI)

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** On 2026-11-14 the author authorized resuming
release preparation and the read-only prior-art scans, and chose the
repository name `regularly-varying-mass-counts`. No push, repository
creation, tag, release, DOI or site change has been authorized yet. Each
external action needs the author's explicit authorization.

## Principal claim

For every $0<\theta<1$ there is a tree of intervals in $[0,1)$, with
children partitioning their parent, uniformly bounded finite branching and
all child-to-parent ratios at most $\theta$, such that $D(t)\sim C/t$ and
$\mathsf n(T;t)/D(t)=Q(\log(1/t))+o(1)$. Here $Q$ is continuous, nonconstant,
$\log 3$-periodic, of mean one, and its range is the limit set (paper
Theorem 1.2).

Further results: the periodic law and Fourier test (Theorem 5.2,
Corollaries 5.3–5.4); width of order $\theta$ (Corollary 6.3); concrete
widths (Theorem 1.4); the type-census transfer (Theorem 9.1); and the
continued-fraction law (Theorem 9.2). No convergence rate, meromorphic
continuation, or certified extrema of $Q$ is claimed.

## P1 — prior work and credit

| Check | Status | Evidence or residual |
|---|---|---|
| Closest mechanisms and parameter families compared | PASS | `audit/PRIOR-ART.md` (R1–R3); theorem-level comparison in `reports/novelty-theorem-comparison-2026-11-14.md`, with Arcozzi–Rochberg–Sawyer and Naimark–Solomyak Example 8.1 now credited |
| Obtainable primary sources checked | PARTIAL | CFV §8.3 and the Rastegaev arXiv text read; the earlier paper's Theorem A.4 and Proposition B.1 read. Kigami–Lapidus via an earlier audit's theorem check; Lapidus–van Frankenhuijsen chapter pinpoint from the table of contents |
| Contribution types distinguished | PASS | README "What is new" and "Not new"; paper Section 10 |
| Novelty bounded to searched corpus | PASS | "not found in the sources checked" in the README, Section 10 and `audit/PRIOR-ART.md` |
| Inaccessible or unperformed searches visible | PASS | MathSciNet (subscription) and Google Scholar (blocked) logged NOT PERFORMED; zbMATH Open searched by API, with failures logged |
| Fast-follow scan within 7 days of tagging | PASS for 2026-11-14 | must be repeated if tagging happens after 2026-11-21 |

**P1 gate:** PARTIAL; the residuals are named. A tag requires the author to
accept them.

## A1 — claim and artifact consistency

| Check | Status | Evidence or residual |
|---|---|---|
| Principal claim precise and no broader than proof | PASS | `reports/proof.md` (M25) and `reports/proof-section9.md` |
| Scope visible near claim | PASS | Theorem statements, Scope subsection, README "Evidence and limits" |
| Proof, computation, literature separated | PASS | README evidence table; VERIFICATION.md |
| Credit | PASS | Ledger L2 and L7 |
| Public prose | PASS | `reports/claims-consistency.md`; fixes in ledger L13–L17 |
| What is new | PASS | README section directly after the introduction, separate from "Earlier work"; known-before sentence, principal result marked, "Not new" list |
| Claims consistency | PASS | one principal result and the same novelty labels on README, abstract, introduction, Section 10 and `audit/PRIOR-ART.md`; theorem numbers checked against the PDF |
| Predecessor mirror | PASS | Modelled on `sparse-mertens-eigenvalue-law` v0.1.0: README layout, status line, CFF, CORRECTIONS, VERIFICATION, ADMISSION, checker, GPL-3.0-only |
| Metadata | PASS | Title, author, version 0.1.0 and candidate status agree across README, PDF title page, `CITATION.cff` and this file |
| Adversarial check | PASS | process-separated AI audits listed in `audit/LEDGER.md`; must-fix findings resolved |

**A1 gate:** PASS. Any material claim edit reopens this gate.

## R1 — release and stewardship

| Check | Status | Evidence or residual |
|---|---|---|
| Reproduction | PASS (local candidate) | `git archive` extraction of the candidate commit, with the PDF deleted, rebuilt by `make paper` to a byte-identical PDF (SHA-256 prefix `161b8f638267b85c`); `make check`, `make verify` and the manifest pass in the extraction. Repeat on the frozen commit |
| Artifact integrity | PASS (local candidate) | deterministic PDF (fixed `SOURCE_DATE_EPOCH`); `MANIFEST.sha256` covers every tracked file; bundled release audit run in candidate state |
| Hygiene | PASS | tracked tree scanned for local paths and private data (ledger L12). README rendered with `gh api markdown` (GFM) on 2026-11-14: 62 inline and 1 display math elements, matching the source, and no `$` outside math |
| Stewardship | PASS | `CORRECTIONS.md` |
| Tag, archive, DOI, metadata | NOT STARTED | require the author's authorization |

**Admission verdict:** NOT YET ADMITTED. The candidate is local only; no tag, archive or DOI exists.

## External actions

| Action | Owner | Status |
|---|---|---|
| Local candidate commit | root agent | done 2026-11-14 (local only; noreply identity) |
| Private GitHub repository and push | author authorization | not authorized |
| Public visibility; Zenodo enablement | author | not authorized |
| Annotated tag `v0.1.0`, GitHub Release | author authorization | not authorized |
| Public-site listing; living-metadata update | author authorization (admission bundle) | not authorized |

Archive route (proposed, as for the predecessor): Zenodo GitHub integration,
with no manual deposit.
