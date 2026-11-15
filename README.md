# Regularly varying mass counts and oscillating spectral asymptotics

Jeffery Kline

**Version 0.1.0 — release candidate, not yet published.** No public tag or
DOI exists yet. Admission under the project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html)
is a release decision, not peer review or a correctness certificate. The
release checklist is [ADMISSION.md](ADMISSION.md).

The paper is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex). This is a sequel to
[*The eigenvalue decay of the limiting kernel of a sparse Mertens matrix*](https://doi.org/10.5281/zenodo.23621017)
(version 0.1.0, 2026), which asked the question answered here.

## Introduction

Divide the unit interval into subintervals, divide each of those again, and
keep going, retaining every interval. The *cylinder operator* $T$ of this
tree integrates a function over each interval and adds the integral back on
that interval. Does the number $D(t)$ of intervals longer than $t$ predict
the number $\mathsf n(T;t)$ of eigenvalues of $T$ above $t$? The earlier
paper showed, among other results, that $\mathsf n(T;t)\sim D(t)$ when
$D(t)\sim C/t$ and the child-to-parent length ratios tend to zero. It asked
whether the condition on the ratios can be dropped.

No fixed bound on the ratios, however small, can replace it. For every
$0<\theta<1$ the paper constructs a tree of intervals in which each interval
is partitioned by its children, the number of children is bounded, and every
child is at most $\theta$ times as long as its parent. Here $D(t)\sim C/t$,
but $\mathsf n(T;t)/D(t)$ has no limit as $t\to0$: it approaches a
continuous, nonconstant periodic function of $\log(1/t)$, and its limit
points form the range of that function. Over all trees with $D(t)\sim C/t$
and ratios at most $\theta$, the largest possible oscillation lies between
two constant multiples of $\theta$ as $\theta\to0$.

In the other direction, suppose $D(t)\sim C/t$, each rescaled subtree is
determined by a parameter in a compact space, its *type*, subject to a
continuity condition, and the types of the intervals longer than $t$ have
a limiting distribution as $t\to0$. Then $\mathsf n(T;t)\sim D(t)$, with
no condition on the ratios beyond a uniform bound below one. The tree of continued-fraction
cylinders, whose types range over a continuum, satisfies these
conditions, and there

```math
\mathsf n(T;t)\sim D(t)\sim\frac{6\log 2}{\pi^2\,t}\qquad(t\to0).
```

## What is new

The earlier paper proved $\mathsf n(T;t)\sim D(t)$ for trees whose mass
count $D$ (the number of intervals longer than $t$) is regularly varying
with index $-1$, meaning that halving a small threshold roughly doubles the
count, as when $D(t)\sim C/t$. It needed one of two further hypotheses:
the child ratios tend to zero, or the subtrees fall into finitely many
classes whose spectral profiles converge. It asked whether regular
variation alone is enough. New here:

1. **Principal result: regular variation alone is not enough, whatever
   the ratio cap.** For every
   $0<\theta<1$ there is a tree of intervals with bounded branching and all
   child ratios at most $\theta$, with $D(t)\sim C/t$, for which
   $\mathsf n(T;t)/D(t)$ approaches a continuous, nonconstant function of
   $\log(1/t)$ with period $\log 3$ (Theorem 1.2). The period comes from
   the 3:1 split used in the construction; it is not intrinsic.
2. **The exact form of the oscillation.** For the constructed trees the
   ratio is within $o(1)$ of the periodic function at every threshold, not
   only on average; its limit points form an interval; and a Fourier test
   decides whether the periodic function is constant (Theorem 5.2 and
   Corollary 5.3). In frequency terms, for these trees the series
   $\sum_r\lambda_r^z$ of the eigenvalues has nonzero boundary limits at points of the line
   $\mathrm{Re}\,z=1$ other than $z=1$, which the series $\sum_v m_v^z$ of
   the masses lacks (Corollary 5.4). No continuation past that line is
   claimed.
3. **The size of the oscillation.** Over all trees with $D(t)\sim C/t$ and
   ratios at most $\theta$, the largest possible oscillation width lies
   between two constant multiples of $\theta$ as $\theta\to0$
   (Corollary 6.3).
4. **Small explicit examples.** For trees with child ratios at most $3/4$
   and at most $4\cdot3^{k-1}$ children, the oscillation width exceeds
   $0.0513$ for $k=3$ and $0.2313$ for $k=4$ (Theorem 1.4), using a
   certified interval-arithmetic computation.
5. **When the law holds.** If each rescaled subtree is determined by a type
   in a compact space, the types of the intervals longer than $t$ have a
   limiting distribution, the profiles are continuous almost everywhere, and
   $D$ is regularly varying with index $-1$, then
   $\mathsf n(T;t)\sim D(t)$, with no condition on the ratios beyond a
   uniform cap below one (Theorem 9.1). In the counterexamples the type
   distribution oscillates instead of converging. For the tree of continued-fraction cylinders
   with Lebesgue measure, whose types range over a continuum and whose
   vertices have infinitely many children,
   $\mathsf n(T;t)\sim D(t)\sim 6\log 2/(\pi^2 t)$ and
   $\lambda_j(T)\sim 6\log 2/(\pi^2 j)$ (Theorem 9.2).

Not new:

- The compactness, the sandwich inequality and the profile identity
  (paper Sections 1.2 and 2) are cited from the earlier paper.
- The tools are standard: equidistribution of an irrational rotation,
  binomial local limits, eigenvalue interlacing, the Abelian passage to
  boundary limits in Corollary 5.4, and the weak-convergence argument in
  Theorem 9.1. That theorem is a continuum-of-types counterpart of the
  earlier paper's finite-class transfer theorem.
- That the law can hold with child ratios bounded away from zero is not
  new: the earlier paper proved it for stationary non-arithmetic trees,
  in which every vertex has the same type (its Proposition B.1).
- The continued-fraction cylinder lengths, their Dirichlet series and the
  constant $\pi^2/(6\log 2)$ (the entropy of the Gauss map) are classical
  (Clément–Flajolet–Vallée). The mass-count asymptotic follows from
  counting coprime pairs.
- Log-periodic leading terms of eigenvalue counts are known for
  Laplacians on self-similar fractals (Kigami–Lapidus), and Rastegaev
  proved that they are nonconstant for Sturm–Liouville problems with
  arithmetically self-similar weights. What is new is that the oscillation
  appears in the eigenvalue count of a single operator whose own mass count
  has a constant leading term.

These statements rest on a bounded comparison recorded in
[audit/PRIOR-ART.md](audit/PRIOR-ART.md). We have not found the results above
in the sources checked; this is not a worldwide novelty claim.

## Earlier work

- **Kline (2026)**, the earlier paper (version DOI
  [10.5281/zenodo.23621017](https://doi.org/10.5281/zenodo.23621017)),
  introduced the cylinder operator as a tool for a sparse Mertens kernel,
  proved the compactness, the sandwich inequality, the two transfer
  theorems and the law for stationary non-arithmetic trees, and asked
  Question 7.1, answered here.
- **Kigami and Lapidus (1993)** distinguished lattice and nonlattice
  spectral asymptotics for Laplacians on self-similar fractals. Their
  spectral scales combine energy and measure weights, so their lattice
  condition is not a statement about raw cylinder masses.
- **Rastegaev (2024)** proved that the periodic leading coefficient of the
  eigenvalue count is nonconstant for a wide class of Sturm–Liouville
  problems with arithmetically self-similar weights.
- **Lapidus and van Frankenhuijsen (2013)** relate log-periodic
  oscillations of counting functions to poles of Dirichlet series off the
  real axis (complex dimensions). Here only boundary limits are proved.
- **Clément, Flajolet and Vallée (2001)** studied the Dirichlet series of
  continued-fraction cylinder lengths, its relation to the Riemann zeta
  function, and the Gauss-map entropy.
- **Evans–Harris–Lang (2001), Naimark–Solomyak (2000), Lifshits–Linde
  (2011) and Bendikov–Grigor'yan–Pittet–Woess (2014)** study related
  operators on trees and ultrametric spaces. They concern different operator
  classes (edge weights, Hardy-type operators, hierarchical Laplacians) and
  do not contain the results here.

## Evidence and limits

| Claim | Status |
|---|---|
| Theorem 1.2 (counterexample for every cap) | proved on paper; uses the earlier paper's Section 2 facts |
| Theorem 5.2, Corollaries 5.3 and 5.4 (periodic law, Fourier test, boundary limits) | proved on paper |
| Corollary 6.3 (width of order $\theta$) | proved on paper; the upper bound uses the earlier paper's sandwich inequality |
| Theorem 1.4 (widths above $0.0513$ and $0.2313$) | proved on paper with a certified interval computation, `c1_certificate.py` |
| Theorem 9.1 (type-census transfer) | proved on paper |
| Theorem 9.2 (continued-fraction law) | proved on paper; uses the earlier paper's Section 2 facts and classical continued-fraction identities |
| Table 1 and Figure 1 | floating-point computation only |
| Other splitting ratios (Section 10) | proposal; only the algebra is checked |

- The proofs were checked by process-separated AI reviews. No independent
  human expert has examined them. Agreement among AI checks is evidence
  about a process, not independent validation.
- The exact extrema of the periodic function are not computed; the values
  near $0.73$ and $1.20$ in the figure are numerical evidence.
- No rate of convergence is proved.
- Open: two-child or three-child counterexamples, the smallest case $k=2$,
  meromorphic continuation of the Dirichlet series, and the
  continued-fraction law for the Gauss measure or other densities.

## Reproduce

Requirements: pdfLaTeX and an isolated Python environment with the packages
in `requirements.txt`. Set `PYTHON` to the environment's absolute
interpreter path.

```sh
make paper                                  # four pdfLaTeX passes; fixed SOURCE_DATE_EPOCH
make check PYTHON=/absolute/path/to/venv/bin/python    # labels, citations, TeX log, PDF text
make verify PYTHON=/absolute/path/to/venv/bin/python
shasum -a 256 -c MANIFEST.sha256
```

`make check` checks the document's consistency, and `make verify` runs the
interval certificate used in Theorem 1.4, small floating-point checks, and
finite checks of the continued-fraction counts.
Neither checks proofs. [VERIFICATION.md](VERIFICATION.md)
records the commands, outputs and environment, and the longer
recomputation of the figure and table.

## Repository contents

- `paper/`: LaTeX source `main.tex`, the figure, and the reading copy
  `main.pdf`.
- `c1_certificate.py`: the interval-arithmetic certificate (Appendix A).
- `fig_asymptotics.py`, `fig_asymptotics.npz`: the figure and its data.
- `checks.py`, `large_x.py`, `secular_c1.py`, `scripts/verify_numerics.py`:
  floating-point checks and illustrations.
- `scripts/cf_checks.py`: finite checks of the continued-fraction counts
  used in Theorem 9.2.
- `scripts/check_paper.py`: document consistency checker.
- `audit/`: the prior-art record, the proof-review reports and the audit
  ledger.

## Citation

No permanent identifier exists yet. A version DOI will be added after
publication. Machine-readable metadata is in [CITATION.cff](CITATION.cff).

## License and corrections

The paper, source, prose and code are licensed under
[GPL-3.0-only](LICENSE). See [CORRECTIONS.md](CORRECTIONS.md) for the
correction, withdrawal and supersession policy. AI systems assisted
development, writing, computation and checking under the author's
direction; the author is responsible for the work.
