"""Rigorous enclosure of the oscillation coefficient c_1 for the trees T_k.

Tree T_k: alpha = log(4/3)/log 3, P = log 3. Depth d uses rule A (ratios 3/4, 1/4)
if {d alpha} in [0, 1/4), else rule B (N = 4*3^(k-1) equal children).
Comparison profiles (paper/main.tex, concrete examples):
  B-nodes: xi0_B = 1_(0,1)                                  -> M0_B(z) = 1/z
  A-nodes: xi0_A = 1_(3/4, mu0) + 1_(1/4, mu1), mu = 1 +- sqrt(7)/4
           M0_A(z) = (mu0^z - (3/4)^z + mu1^z - (1/4)^z)/z
  c1_0 = (M0_A(z1) - 1/z1) * int_0^{1/4} e^{-2 pi i t} dt,   z1 = 1 + 2 pi i / P
Error: |c_1 - c1_0| <= E_N = 3*C_N/(2*N) + (1+C_N/N)/(2*N),
where C_N = mu0/(1-3/(4*N)). All certificate operations, including
error subtraction and width comparisons, use mpmath.iv.
Run with the existing shared virtual environment; mpmath==1.3.0.
"""
import sys
from mpmath import iv

assert sys.prefix != sys.base_prefix
iv.dps = 40


def ipow(r, tau):
    """r^(1 + i tau) for real r > 0 as (re, im) intervals."""
    lr = iv.log(r)
    ang = tau * lr
    return r * iv.cos(ang), r * iv.sin(ang)


P = iv.log(iv.mpf(3))
tau = 2 * iv.pi / P
s7 = iv.sqrt(iv.mpf(7))
mu0 = 1 + s7 / 4
mu1 = 1 - s7 / 4
terms = [(mu0, 1), (iv.mpf(3) / 4, -1), (mu1, 1), (iv.mpf(1) / 4, -1)]
re = iv.mpf(0); im = iv.mpf(0)
for r, sg in terms:
    a, b = ipow(r, tau)
    re += sg * a; im += sg * b
# divide numerator (re + i im) by z1 = 1 + i tau, then subtract 1/z1: (num - 1)/z1
nre, nim = re - 1, im
den = 1 + tau ** 2
qre = (nre * 1 + nim * tau) / den
qim = (nim * 1 - nre * tau) / den
# times (1 + i)/(2 pi i) = (1 + i)(-i)/(2 pi) = (1 - i)/(2 pi)
fre = (qre + qim) / (2 * iv.pi)
fim = (qim - qre) / (2 * iv.pi)
abs2 = fre ** 2 + fim ** 2
absc = iv.sqrt(abs2)
print('mu0, mu1 =', mu0, mu1)
print('c1_0 real part  in', fre)
print('c1_0 imag part  in', fim)
print('|c1_0|          in', absc)
assert absc > iv.mpf('0.10158610335')
assert absc < iv.mpf('0.10158610336')
for k in range(2, 11):
    N = 4 * 3 ** (k - 1)
    norm_bound = mu0 / (1 - iv.mpf(3) / (4 * N))
    err = 3 * norm_bound / (2 * N) + (1 + norm_bound / N) / (2 * N)
    lower = absc - err
    width_lower = iv.pi * lower
    print('k=%d N=%d' % (k, N))
    print('  E_N enclosure:', err)
    print('  |c1_0|-E_N enclosure:', lower)
    print('  pi*(|c1_0|-E_N) enclosure:', width_lower)
    if k >= 3:
        assert lower > 0
    if k == 3:
        assert err < iv.mpf('0.08524300')
        assert width_lower > iv.mpf('0.0513')
    if k == 4:
        assert err < iv.mpf('0.02793825')
        assert width_lower > iv.mpf('0.2313')
print('PASS: scalar enclosure, k>=3 nonvanishing, and stated width bounds.')
