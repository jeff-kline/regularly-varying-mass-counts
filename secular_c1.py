"""Floating-point c_1 for T_k from the radial secular recursion (evidence only).
Uses secular equations and low-eigenvalue pruning; phase is in units of 1.
Exact Mellin pieces: M_phi(z) = sum (mu^z - y^z)/z over radial roots mu and poles y."""
import math, sys, json
import numpy as np
assert sys.prefix != sys.base_prefix
P = math.log(3.0); alpha = math.log(4 / 3) / P


def secular(y, w):
    K = len(y); lo = np.empty(K); hi = np.empty(K)
    hi[0] = y[0] + w.sum() + 1.0; lo[0] = y[0]; lo[1:] = y[1:]; hi[1:] = y[:-1]
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        h = (w[None, :] / (mid[:, None] - y[None, :])).sum(axis=1) - 1.0
        pos = h > 0
        lo = np.where(pos, mid, lo); hi = np.where(pos, hi, mid)
    mu = 0.5 * (lo + hi)
    a2 = 1.0 / (w[None, :] / (mu[:, None] - y[None, :]) ** 2).sum(axis=1)
    return mu, a2


def prune(x, a2, c):
    keep = x > c; xs, ws = x[keep], a2[keep]
    if (~keep).any() and a2[~keep].sum() > 0:
        wl = a2[~keep].sum(); xs = np.append(xs, (x[~keep] * a2[~keep]).sum() / wl); ws = np.append(ws, wl)
    o = np.argsort(-xs); return xs[o], ws[o]


def M_phi(ph, N, cut, pad, z):
    GA = [(0.75, 1), (0.25, 1)]; GB = [(1 / N, N)]
    x, a2 = np.array([1.0]), np.array([1.0])
    for d in range(pad, -1, -1):
        G = GA if ((ph + d * alpha) % 1.0) < 0.25 else GB
        y = np.concatenate([rho * x for rho, c in G]); w = np.concatenate([c * rho * a2 for rho, c in G])
        o = np.argsort(-y); y, w = y[o], w[o]
        keep = np.ones(len(y), bool); keep[1:] = np.abs(np.diff(y)) > 1e-12 * y[1:]
        w = np.bincount(np.cumsum(keep) - 1, weights=w); y = y[keep]
        y, w = prune(y, w, cut * 0.5); sel = w > 1e-14 * w.sum(); y, w = y[sel], w[sel]
        mu, a2n = secular(y, w)
        if d == 0:
            return complex((np.sum(mu.astype(complex) ** z) - np.sum(y.astype(complex) ** z)) / z)
        x, a2 = prune(mu, a2n, cut * 0.5)


z1 = 1 + 2j * math.pi / P
res = {}
for k in (3, 4, 5, 6):
    N = 4 * 3 ** (k - 1)
    for cut, pad, NG in ((1e-3, 40, 400), (3e-4, 60, 800)):
        ph = (np.arange(NG) + 0.5) / NG
        Ms = np.array([M_phi(p, N, cut, pad, z1) for p in ph])
        c1 = (np.exp(-2j * math.pi * ph) * Ms).mean()
        res[f'k={k},cut={cut},grid={NG}'] = [c1.real, c1.imag, abs(c1)]
        print('k=%d N=%d cut=%g grid=%d  c1 = %.5f %+.5fi  |c1| = %.5f   (closed form 0.09410+0.03827i, |.|=0.10159, bound %.4f)'
              % (k, N, cut, NG, c1.real, c1.imag, abs(c1), 9.75 / N), flush=True)
json.dump(res, open('secular_c1.json', 'w'), indent=1)
