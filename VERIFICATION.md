# Verification record — version 0.1.0

Recorded 2026-11-14.

## What is verified here

This record covers artifact consistency and reproducibility. It shows that
the document builds deterministically, that its labels, citations and log are
clean, that the computations used or illustrated in the paper run, and that
every tracked file matches the manifest. It does not verify proofs. The proof
audits, the source comparisons and their dispositions are in
[audit/LEDGER.md](audit/LEDGER.md) and `audit/reports/`.

One theorem uses a computation. Theorem 1.4 rests on the interval-arithmetic
certificate `c1_certificate.py` (paper Appendix A). All other computations are
floating-point evidence or illustrations: Table 1, Figure 1, and the finite
continued-fraction checks.

## Environment

| Tool | Version |
|---|---|
| pdfTeX | 3.141592653-2.6-1.40.22 (TeX Live 2021, MacPorts 2021.58693_2) |
| Python (isolated virtual environment) | 3.9.6 |
| mpmath, numpy, scipy, matplotlib | 1.3.0, 2.0.2, 1.13.1, 3.9.4 (`requirements.txt`) |
| Poppler `pdfinfo` / `pdftotext` | 26.07.0 |
| OS | macOS (Darwin 25.6.0) |

The Makefile sets `SOURCE_DATE_EPOCH=1794614400` (2026-11-14 00:00 UTC) and
`FORCE_SOURCE_DATE=1`, which fixes the PDF creation date and identifiers.

## Commands and outputs

`PYTHON` must be the absolute path of an isolated virtual-environment
interpreter. The Makefile refuses a base interpreter.

```sh
make paper                       # four pdfLaTeX passes; fails on any warning
make check  PYTHON=/abs/path/to/venv/bin/python
make verify PYTHON=/abs/path/to/venv/bin/python
shasum -a 256 -c MANIFEST.sha256
```

`make check` (2026-11-14): `"status": "PASS"`, 25 pages, 43 labels, 103
references, 14 bibliography entries, all 14 cited, no errors.

`make verify` (2026-11-14) prints the following summary lines:

```text
PASS: scalar enclosure, k>=3 nonvanishing, and stated width bounds.
PASS: 28 dense finite-tree resolvent/profile comparisons; max relative error 1.36e-13
Figure sampled Q range [0.7310249476, 1.2049162491], mean 0.9999935261
Final-panel mass range [1.0035196804, 1.0234485048], mean 1.0136521230
Final-panel maximum sampled ratio error 0.0300270588
PASS: saved figure summaries agree with the paper; these checks do not certify the extrema.
words with mass > 1e-05: 42140; every coprime pair occurs twice (root and [1] once)
s*D(s) = 0.421400   limit 6 log2/pi^2 = 0.421383
s*sum r^2 = 0.117387   Gauss-census limit = 0.117419
zeta_D(2) truncated at q <= 3000: direct 1.3511315, via 1/zeta(4) 1.3511315
PASS: continued-fraction counting checks (evidence, not proof).
```

The certificate's enclosures for $k=3$ and $k=4$ are
$\pi(|c_1^0|-E_N)\in[0.05134338676\ldots]$ and $[0.23137158290\ldots]$. These
match the bounds $0.0513$ and $0.2313$ in Theorem 1.4.

## Longer recomputation (not part of `make verify`)

`make numerics` reruns `checks.py`, `large_x.py 4`, `secular_c1.py` and
`fig_asymptotics.py`, which regenerates `fig_asymptotics.npz` and the figure.
The full figure computation takes several minutes. The release uses the saved
data. `make figure` redraws the figure from it, and `make verify` checks the
saved summaries against the paper.

## Clean build

The clean-extraction rebuild and the PDF hash are recorded at the candidate
freeze. See the R1 rows of [ADMISSION.md](ADMISSION.md).
