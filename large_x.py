"""Large-x evidence for T_k: mubar * e^{-x} D(e^{-x}) -> 1 (Lemma L1) and
mubar * e^{-x} n0(e^{-x}) -> predicted log-periodic profile Lambda (n0 uses the
closed-form approximant profiles, so it illustrates the limit theorem, not the
O(1/N) profile error). Only depths whose mean M_d is within 12 sd of x are summed;
terms with x - S_d > 45 are dropped (relative size e^-45).
"""
import math, sys, json
import numpy as np
from scipy.stats import binom

assert sys.prefix != sys.base_prefix
P = math.log(3.0); s = math.log(4 / 3); alpha = s / P
mu0 = 1 + math.sqrt(7) / 4; mu1 = 1 - math.sqrt(7) / 4
k = int(sys.argv[1]) if len(sys.argv) > 1 else 4
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 4_000_000
mubar = s + P * (0.75 * k + 1 / 16)
d = np.arange(DMAX + 1)
isA = ((d * alpha) % 1.0) < 0.25
a = np.concatenate([[0], np.cumsum(isA)[:-1]])          # A-levels among depths < d
b = d - a
base = d * s + P * k * b
M = base + P * a / 4
sd = P * np.sqrt(3 * a / 16)


def xiA(r):
    return (((r > 0.75) & (r < mu0)) | ((r > 0.25) & (r < mu1))).astype(float)


def xiB(r):
    return ((r > 0) & (r < 1)).astype(float)


def counts(x):
    lo = np.searchsorted(M, x - 12 * sd.max() - 50); hi = np.searchsorted(M, x + 12 * sd.max() + 50)
    tD = 0.0; tn = 0.0
    for dd in range(lo, min(hi, DMAX)):
        J0 = max(0, math.ceil((x - 45 - base[dd]) / P)); J1 = min(a[dd], math.floor((x + 3 - base[dd]) / P))
        if J1 < J0:
            continue
        J = np.arange(J0, J1 + 1)
        S = base[dd] + P * J
        pm = binom.pmf(J, a[dd], 0.25)
        u = x - S
        tD += float((pm * np.where(u > 0, np.exp(-u), 0.0)).sum())
        r = np.exp(-u)
        tn += float((pm * r * (xiA(r) if isA[dd] else xiB(r))).sum())
    return tD * mubar, tn * mubar


def Lambda(x, nth=4000):
    """Predicted limit of mubar * e^{-x} n0(e^{-x}): P * int_0^1 Psi_theta(x - theta P) dtheta."""
    x = x % P
    th = (np.arange(nth) + 0.5) / nth
    y = x - th * P
    tot = np.zeros(nth)
    for kk in range(-60, 4):
        u = y - kk * P
        r = np.exp(-u)
        val = np.where(th < 0.25, xiA(r), xiB(r)) * r
        tot += val
    return P * tot.mean()


out = {'k': k, 'mubar': mubar, 'rows': []}
for x0 in (1e4, 1e5, 1e6, 3e6 * mubar / 2):
    if x0 > M[-1] - 1000:
        continue
    ts = np.linspace(0, P, 13)
    rows = []
    for t in ts:
        dD, dn = counts(x0 + t)
        rows.append((float(t), dD, dn, Lambda(x0 + t)))
    arr = np.array(rows)
    print('k=%d x0=%.3g  mubar*tD in [%.4f, %.4f]   mubar*tn0 - Lambda in [%.4f, %.4f]   Lambda in [%.4f, %.4f]'
          % (k, x0, arr[:, 1].min(), arr[:, 1].max(), (arr[:, 2] - arr[:, 3]).min(), (arr[:, 2] - arr[:, 3]).max(),
             arr[:, 3].min(), arr[:, 3].max()), flush=True)
    out['rows'].append({'x0': x0, 'samples(t, mubar*tD, mubar*tn0, Lambda)': rows})
json.dump(out, open(f'large_x_k{k}.json', 'w'), indent=1)
