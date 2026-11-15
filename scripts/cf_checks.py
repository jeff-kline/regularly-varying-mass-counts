"""Finite checks for the continued-fraction tree (Theorem 9.2).

Floating-point evidence for the counting inputs of the proof, not a proof.
Words are enumerated directly from their digits, so the two-words-per-pair
count, the child-ratio formula and the mass formula are checked against the
recurrences rather than assumed.
"""
import math
import sys

assert sys.prefix != sys.base_prefix, "Use an isolated virtual-environment interpreter"

S = 1e-5                       # mass threshold
C = 6 * math.log(2) / math.pi ** 2


def words(s):
    """Yield (q, p, mass) for every CF word of mass > s, with q=q_n, p=q_{n-1}."""
    stack = [(1, 0)]
    while stack:
        q, p = stack.pop()
        m = 1 / (q * (q + p))
        if m <= s:
            continue
        yield q, p, m
        a = 1
        while True:
            q2, p2 = a * q + p, q
            if 1 / (q2 * (q2 + p2)) <= s:
                break
            ratio = (q * (q + p)) / (q2 * (q2 + p2))
            r = p / q
            assert abs(ratio - (1 + r) / ((a + r) * (a + 1 + r))) < 1e-12
            if a == 1:
                assert 1 / 3 - 1e-12 <= ratio <= 1 / 2 + 1e-12
            stack.append((q2, p2))
            a += 1


pairs = {}
D = 0
census = 0.0
for q, p, m in words(S):
    D += 1
    census += (p / q) ** 2
    pairs[(q, p)] = pairs.get((q, p), 0) + 1
    assert math.gcd(q, p) == 1

bad = [(k, v) for k, v in pairs.items() if v != (1 if k in ((1, 0), (1, 1)) else 2)]
assert not bad, bad[:5]

limit_census = 6 / math.pi ** 2 * (0.5 - 1 + math.log(2))   # int_0^1 r^2/(1+r) dr
print(f"words with mass > {S:g}: {D}; every coprime pair occurs twice "
      "(root and [1] once)")
print(f"s*D(s) = {S * D:.6f}   limit 6 log2/pi^2 = {C:.6f}")
print(f"s*sum r^2 = {S * census:.6f}   Gauss-census limit = {limit_census:.6f}")

# zeta_D identity at z = 2, truncated at q <= Q on both sides.
Q = 3000
lhs = 1 + 2 ** -2 + 2 * sum(1 / (q * (q + p)) ** 2
                            for q in range(2, Q + 1) for p in range(1, q)
                            if math.gcd(q, p) == 1)
zeta4 = math.pi ** 4 / 90
rhs = 1 + 2 ** -2 + 2 / zeta4 * sum(1 / (q * (q + p)) ** 2
                                    for q in range(2, Q + 1) for p in range(1, q))
print(f"zeta_D(2) truncated at q <= {Q}: direct {lhs:.7f}, via 1/zeta(4) {rhs:.7f}")
assert abs(lhs - rhs) < 1e-6
assert abs(S * D - C) < 5e-3 and abs(S * census - limit_census) < 5e-3
print("PASS: continued-fraction counting checks (evidence, not proof).")
