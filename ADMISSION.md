# Admission record

**Current state:** ADMITTED

**Version:** 0.1.0

**Tag:** `v0.1.0` → `51417a3a60fd0d8f4108a32737b053c6d43ae53a`

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Current verdict: ADMITTED (2026-11-14)

**Version DOI:** [`10.5281/zenodo.24237731`](https://doi.org/10.5281/zenodo.24237731) · **Concept DOI:** `10.5281/zenodo.24237730` · **Record:** <https://zenodo.org/records/24237731>

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** On 2026-11-14 the author authorized resuming
release preparation and the read-only prior-art scans, and chose the
repository name `regularly-varying-mass-counts`. On 2026-11-14 the author
authorized a further novelty search and step 1: a private GitHub
repository with `main` pushed. The author then instructed making it
public, enabled the repository in Zenodo, and authorized the tag `v0.1.0`
and the GitHub Release. The author then approved the site entry (title and
blurb), which authorized the admission bundle: the site listing and this
admitted-status update.

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

**P1 gate:** PARTIAL; the residuals are named. **The author accepted these
named residuals on 2026-11-14** by instructing the tag after being told that
acceptance was required.

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
| Metadata | PASS | Title, author, version 0.1.0 and admitted status agree across README, PDF title page, `CITATION.cff`, the Zenodo record and this file |
| Adversarial check | PASS | process-separated AI audits listed in `audit/LEDGER.md`; must-fix findings resolved |

**A1 gate:** PASS. Any material claim edit reopens this gate.

## R1 — release and stewardship

| Check | Status | Evidence or residual |
|---|---|---|
| Reproduction | PASS | `git archive` extraction of the tagged commit `51417a3`, with the PDF deleted, rebuilt by `make paper` to the archived PDF byte for byte (SHA-256 `701ed90c3ebf6ce0c4f6f36c851fc2d5c36db34fa59695aa769bd452843bc21e`); `make check`, `make verify` and the manifest pass in the extraction |
| Artifact integrity | PASS | deterministic PDF (fixed `SOURCE_DATE_EPOCH`); `MANIFEST.sha256` covers every tracked file |
| Hygiene | PASS | tracked tree scanned for local paths and private data (ledger L12). README rendered with `gh api markdown` (GFM) on 2026-11-14: 62 inline and 1 display math elements, matching the source, and no `$` outside math |
| Stewardship | PASS | `CORRECTIONS.md` |
| Immutable semantic tag | PASS | annotated `v0.1.0` (object `c779684`) → `51417a3`; tagger is the GitHub noreply identity |
| Public permanent archive with provider byte identity | PASS | two pinned GitHub `zipball/v0.1.0` downloads and two Zenodo downloads are byte-identical: 587,816 bytes, SHA-256 `2af3c646528ea6a6975ee7047127581679b804b3bac05c5f3067713474fa9ad9`; Zenodo MD5 `48725caf3293c3d70def395eb0b3dde7` |
| DOI resolves; living repository identifies the version | PASS | `doi.org/10.5281/zenodo.24237731` redirects to the Zenodo record; README, `CITATION.cff` and the living paper carry the version DOI |
| Archive metadata matches repository | PASS | title, creator Kline, Jeffery, version v0.1.0, publication date 2026-11-15 (UTC), license `gpl-3.0`, resource type software, related identifier the `v0.1.0` tree |
| Machine-readable citation | PASS | `CITATION.cff` with version DOI, concept DOI and `date-released: 2026-11-15` (Zenodo's date) |

**R1 gate:** PASS.

**Admission verdict:** ADMITTED (2026-11-14), with the named P1 residuals
accepted by the author. AI reviews only; no independent human expert has
examined the proofs.

## External actions

| Action | Owner | Status |
|---|---|---|
| Local candidate commit | root agent | done 2026-11-14 (local only; noreply identity) |
| Private GitHub repository and push | author authorization | done 2026-11-14: `jeff-kline/regularly-varying-mass-counts` (private); `main` pushed at `7766b62`; issues on, wiki off |
| Public visibility; secret scanning and push protection | author authorization | done 2026-11-14 (made public at the author's instruction; security settings match the predecessor) |
| Zenodo enablement before the Release | author, in the Zenodo portal | done 2026-11-14; Zenodo release webhook present and active |
| Annotated tag `v0.1.0`, GitHub Release | author authorization | done 2026-11-14 (02:36 UTC 2026-11-15): Release "Version 0.1.0" |
| Public-site listing | author authorization (admission bundle) | done 2026-11-14: landing entry "Mass counts and spectral oscillations" at <https://jeff-kline.github.io/> (site commit `6dc4e98`); Pages build and live HTML checked for title, blurb, repository link and version DOI |
| Living-metadata update (this commit) | author authorization (admission bundle) | done 2026-11-14, pushed after the site listing was verified live |

## Archive verification

- Route: Zenodo GitHub integration; no manual deposit.
- Pinned before the GitHub Release: GitHub API `zipball/v0.1.0`, downloaded
  twice, identical, 587,816 bytes, SHA-256 `2af3c646528ea6a6975ee7047127581679b804b3bac05c5f3067713474fa9ad9`.
- Zenodo file `jeff-kline/regularly-varying-mass-counts-v0.1.0.zip`, downloaded
  twice through the record's file link: identical to the pinned zipball. Its
  contents equal the tagged tree, and every file passes its `MANIFEST.sha256`.
- Separate determinism check: `git archive --format=zip
  --prefix=regularly-varying-mass-counts-v0.1.0/ v0.1.0`, generated twice,
  identical, 586,952 bytes, SHA-256 `786318ddb2b0fe4168d756c5abff9e4979f19d485ec20f0703ba68ef26e05f22`. This is a different file from
  the provider zipball and is not compared with it.
- Mechanical audit at the archived state, on the unchanged tagged tree:
  12 pass, 0 warnings, 0 fail.
