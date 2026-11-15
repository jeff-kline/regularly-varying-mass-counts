# Corrections, withdrawals, and supersession

This repository keeps a visible record of material corrections to released
claims and artifacts.

## Policy

- Minor typographical or navigational fixes may be made on the living default
  branch without changing an archived release.
- A change to a theorem statement, hypothesis, proof dependency, citation that
  affects priority or scope, or verification artifact creates a new version.
  The earlier tag and permanent archive remain unchanged and identifiable.
- A material error that invalidates a principal claim will be marked
  prominently in the README and in this file. The affected release will not be
  deleted or silently replaced.
- A withdrawn result remains findable with the reason, date, affected
  versions, and any replacement or correction linked here.
- Public tags and archived files are immutable. Corrections are made in a new
  commit and, when material, a new tagged release.
- If earlier work is found that anticipates a result here, the novelty
  statements will be narrowed and the source credited in a new version.

Suspected errors may be reported through the repository's issue tracker:
<https://github.com/jeff-kline/regularly-varying-mass-counts/issues>.

## Relation to earlier releases

This paper continues
[*The eigenvalue decay of the limiting kernel of a sparse Mertens matrix*](https://doi.org/10.5281/zenodo.23621017),
version 0.1.0. That release remains correct as stated. Its Question 7.1 asked
whether its transfer theorem for cylinder operators needs vanishing child
ratios or a profile hypothesis. This paper shows that regular variation of
the mass count does not suffice, even together with any fixed ratio cap, and
gives a different sufficient condition: a convergent census of subtree types.

## Version history

### 0.1.0 — released 2026-11-14

- Tag `v0.1.0` at commit `51417a3`; version DOI
  [`10.5281/zenodo.24237731`](https://doi.org/10.5281/zenodo.24237731), concept DOI `10.5281/zenodo.24237730`. Zenodo
  records the publication date as 2026-11-15 (UTC).
- The tagged snapshot retains its prepublication “release candidate” wording
  and carries no DOI, because the DOI was minted by Zenodo after the GitHub
  Release. The living repository and paper now carry the active DOI; the
  archived files were not changed.
- Release preparation, before the tag: the dispositions of all audit findings
  are in `audit/LEDGER.md`. They include added hypotheses in the abstract and
  introduction, and credits to Arcozzi–Rochberg–Sawyer, Naimark–Solomyak,
  Rastegaev, Clément–Flajolet–Vallée and the earlier paper's Proposition B.1.
