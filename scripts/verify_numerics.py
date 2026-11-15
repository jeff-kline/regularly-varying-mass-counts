"""Small independent dense checks of the secular profile, plus figure summaries.

Floating-point validation, not a proof or an error certificate for the figure.
Run from the repository root in the explicitly selected isolated environment.
"""
import math
import sys
from pathlib import Path

assert sys.prefix != sys.base_prefix
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import fig_asymptotics as fig


def finite_f(phase, u, k, depth):
    if depth == 0:
        return 1 / u
    ratios = [(0.75, 1), (0.25, 1)] if phase % 1 < 0.25 else [(1 / (4 * 3 ** (k - 1)), 4 * 3 ** (k - 1))]
    ans = 0.0
    for rho, multiplicity in ratios:
        f = finite_f(phase + fig.ALPHA, u / rho, k, depth - 1)
        ans += multiplicity * f / (1 - f)
    return ans


def dense_matrices(phase, k, depth):
    nodes = [(0.0, 1.0)]
    leaves = nodes[:]
    for d in range(depth):
        ratios = [0.75, 0.25] if (phase + d * fig.ALPHA) % 1 < 0.25 else [1 / (4 * 3 ** (k - 1))] * (4 * 3 ** (k - 1))
        new = []
        for lo, hi in leaves:
            start = lo
            for rho in ratios:
                stop = start + (hi - lo) * rho
                new.append((start, stop))
                start = stop
        nodes.extend(new)
        leaves = new
    mid = np.array([(a + b) / 2 for a, b in leaves])
    mass = np.array([b - a for a, b in leaves])
    vectors = np.array([np.sqrt(mass) * ((mid >= a) & (mid < b)) for a, b in nodes])
    t = vectors.T @ vectors
    b = vectors[1:].T @ vectors[1:]
    return t, b, np.sqrt(mass)


maximum_error = 0.0
comparisons = 0
for phase in (0.0, 0.1, 0.3, 0.6):
    t, b, root = dense_matrices(phase, 2, 2)
    et = np.linalg.eigvalsh(t)
    eb = np.linalg.eigvalsh(b)
    for u in (0.019, 0.073, 0.217, 0.413, 0.811, 1.231, 1.917):
        f = finite_f(phase, u, 2, 2)
        reference = float(root @ np.linalg.solve(u * np.eye(len(b)) - b, root))
        error = abs(f - reference) / max(1, abs(reference))
        maximum_error = max(maximum_error, error)
        assert error < 1e-10, (phase, u, f, reference)
        assert int((et > u).sum() - (eb > u).sum()) == int(f > 1)
        comparisons += 1
print(f'PASS: {comparisons} dense finite-tree resolvent/profile comparisons; max relative error {maximum_error:.3g}')

z = np.load('fig_asymptotics.npz')
assert z['tD'].shape == z['tN'].shape == (4, 64)
assert z['q'].shape == (512,)
assert np.isfinite(z['q']).all() and (z['tD'] > 0).all()
q, d, n = z['q'], z['tD'][-1], z['tN'][-1]
sampled_q = q[::8]
print(f"Figure sampled Q range [{q.min():.10f}, {q.max():.10f}], mean {q.mean():.10f}")
print(f"Final-panel mass range [{d.min():.10f}, {d.max():.10f}], mean {d.mean():.10f}")
print(f"Final-panel maximum sampled ratio error {np.max(abs(n/d-sampled_q)):.10f}")
assert 0.7305 < q.min() < 0.7315 and 1.2045 < q.max() < 1.2055
assert 0.0295 < np.max(abs(n/d-sampled_q)) < 0.0305
print('PASS: saved figure summaries agree with the paper; these checks do not certify the extrema.')
