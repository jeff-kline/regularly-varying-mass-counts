"""Independent numerical checks for the T_k counterexample (evidence, not proof).

1. Mass law: x -> e^{-x} D(e^{-x}) computed in floating point from the size-biased binomial
   representation; should approach 1/mubar with no residual log-periodic oscillation.
2. Profile bounds: brute-force eigenvalues of truncated A-node and B-node subtrees;
   L1 distance of xihat to the comparison profile is checked against Lemma 7.1.
3. The n-count built from comparison profiles, showing the predicted
   oscillation of e^{-x} n(e^{-x}) * mubar (illustration only).
"""
import math, sys, json
import numpy as np
from scipy.stats import binom
from scipy.linalg import eigh

assert sys.prefix != sys.base_prefix
P = math.log(3.0); s = math.log(4 / 3); alpha = s / P
out = {}


def rule_is_A(d, phase0=0.0):
    return ((phase0 + d * alpha) % 1.0) < 0.25


# ---------- 1. D count -------------------------------------------------------
def tD(x, k):
    """e^{-x} D(e^{-x}) = sum_d E[e^{-(x - S_d)} 1[S_d < x]]."""
    total = 0.0; a = 0; b = 0; d = 0
    while True:
        # S_d = d s + P (k b + J), J ~ Bin(a, 1/4)
        base = d * s + P * k * b
        if base >= x:
            break
        J = np.arange(a + 1)
        S = base + P * J
        pm = binom.pmf(J, a, 0.25) if a > 0 else np.array([1.0])
        m = S < x
        total += float((pm[m] * np.exp(-(x - S[m]))).sum())
        if rule_is_A(d):
            a += 1
        else:
            b += 1
        d += 1
    return total


res1 = {}
for k in (4, 5, 6):
    mubar = s + P * (0.75 * k + 1 / 16)
    xs = np.linspace(20, 20 + 2 * P, 25)
    rows = {}
    for X0 in (40.0, 160.0, 640.0, 2560.0):
        vals = [tD(X0 + t, k) * mubar for t in np.linspace(0, 2 * P, 41)]
        rows[str(X0)] = [min(vals), max(vals)]
    res1[f'k={k}'] = {'mubar': mubar, 'mubar*tD range over two periods at x0': rows}
    print('L1 k=%d mubar=%.4f' % (k, mubar), {kk: [round(v, 5) for v in vv] for kk, vv in rows.items()}, flush=True)
out['L1'] = res1


# ---------- 2. brute-force profile check -------------------------------------
def subtree_masses(phase0, k, depth, N):
    """Nodes of a subtree (normalized root mass 1) to relative depth `depth`.
    Returns list of (mass, parent_index)."""
    nodes = [(1.0, -1)]; frontier = [0]
    for j in range(depth):
        new = []
        for v in frontier:
            m = nodes[v][0]
            ratios = [0.75, 0.25] if rule_is_A(j, phase0) else [1.0 / N] * N
            for r in ratios:
                nodes.append((m * r, v)); new.append(len(nodes) - 1)
        frontier = new
    return nodes


def gram(nodes):
    """Gram matrix nu(A_u cap A_v) = mass of deeper node if comparable else 0."""
    n = len(nodes); anc = []
    for i in range(n):
        a = set(); j = i
        while j != -1:
            a.add(j); j = nodes[j][1]
        anc.append(a)
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            if j in anc[i]:
                G[i, j] = G[j, i] = nodes[i][0]
            elif i in anc[j]:
                G[i, j] = G[j, i] = nodes[j][0]
    return G


def xihat_L1(phase0, k, depth, approx):
    N = 4 * 3 ** (k - 1)
    nodes = subtree_masses(phase0, k, depth, N)
    G = gram(nodes)
    ev_T = np.sort(eigh(G, eigvals_only=True))[::-1]
    ev_B = np.sort(eigh(G[1:, 1:], eigvals_only=True))[::-1]   # drop the root vertex
    ev_T = ev_T[ev_T > 1e-14]; ev_B = ev_B[ev_B > 1e-14]
    grid = np.linspace(1e-6, 4.5, 450001)
    nT = np.searchsorted(-ev_T, -grid, side='left')
    nB = np.searchsorted(-ev_B, -grid, side='left')
    xi = nT - nB
    diff = np.abs(xi - approx(grid)).sum() * (grid[1] - grid[0])
    return float(diff), float(xi.sum() * (grid[1] - grid[0])), len(nodes), N


mu0 = 1 + math.sqrt(7) / 4; mu1 = 1 - math.sqrt(7) / 4
apA = lambda r: (((r > 0.75) & (r < mu0)) | ((r > 0.25) & (r < mu1))).astype(float)
apB = lambda r: ((r > 0) & (r < 1)).astype(float)
res2 = {}
for k in (3, 4):
    N = 4 * 3 ** (k - 1)
    C = mu0 / (1 - 3 / (4 * N))
    for name, ph, ap, bound in (('A', 0.1, apA, 2 * (1 + C / N) / N), ('B', 0.6, apB, 2 * C / N)):
        depth = {(3, "A"): 3, (3, "B"): 2, (4, "A"): 2, (4, "B"): 1}[(k, name)]
        dist, integ, size, _ = xihat_L1(ph, k, depth, ap)
        res2[f'k={k},{name}'] = {'L1 dist': dist, 'bound': bound, 'int xihat': integ, 'nodes': size}
        print('profile k=%d %s: L1=%.5f bound=%.5f int=%.5f nodes=%d' % (k, name, dist, bound, integ, size), flush=True)
out['profiles'] = res2


# ---------- 3. predicted oscillation of n ------------------------------------
def F0(u, A):
    r = np.exp(-u)
    xi = apA(r) if A else apB(r)
    return r * xi


def tn_approx(x, k):
    total = 0.0; a = 0; b = 0; d = 0
    while True:
        base = d * s + P * k * b
        if base >= x + 3:
            break
        J = np.arange(a + 1)
        S = base + P * J
        pm = binom.pmf(J, a, 0.25) if a > 0 else np.array([1.0])
        total += float((pm * F0(x - S, rule_is_A(d))).sum())
        if rule_is_A(d):
            a += 1
        else:
            b += 1
        d += 1
    return total


res3 = {}
k = 6; mubar = s + P * (0.75 * k + 1 / 16)
for X0 in (400.0, 1600.0):
    ts = np.linspace(0, 2 * P, 61)
    vals = [tn_approx(X0 + t, k) * mubar for t in ts]
    res3[str(X0)] = {'min': min(vals), 'max': max(vals), 'mean': float(np.mean(vals))}
    print('approx mubar*t*n k=6 x0=%g: min %.4f max %.4f mean %.4f' % (X0, min(vals), max(vals), np.mean(vals)), flush=True)
out['n_oscillation_approx'] = res3
json.dump(out, open('checks.json', 'w'), indent=1)
