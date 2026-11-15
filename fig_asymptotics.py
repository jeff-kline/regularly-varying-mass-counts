"""Figure: mass count flattens, eigenvalue/mass ratio approaches Q_k (tree T_k).

Floating-point illustration only; nothing here is used in the proofs.

Profiles.  For a vertex of phase phi, the profile is xi_phi(u) = 1{F_phi(u) > 1},
where F_phi(u) = <1, (u - Bhat_phi)^{-1} 1> satisfies the exact recursion
    F_phi(u) = sum_children g(F_{phi+alpha}(u / ratio)),   g(x) = x / (1 - x).
The finite-tree version is checked against dense resolvents and eigenvalue
counts by scripts/verify_numerics.py. For u > V0 the
two-term expansion F ~ 1/u + E1/u^2 is used, with E1 = <1, Bhat 1>.

Counts.  With log_3(1/t) = X, a depth-d vertex with j smaller-A steps has
log_3(1/m) = S = d*alpha + k*b_d + j and size-biased weight Bin(a_d, j; 1/4).
Then  t*D(t) = sum w * 3^(S-X) over S < X,  and  t*N(T;t) = sum w * 3^(S-X) * xi.
Q_k(X) = P * int_R 3^y xi_{{y+X}}(3^y) dy  (Theorem 5.2 of the paper).
Terms with relative threshold u = 3^(S-X) < U0 are dropped. Since xi <= 1 and
each walk path gains at least log(4/3) per step, they change t*N by at most
4*U0; in Q_k the dropped part is at most U0.
"""
import math
import sys

assert sys.prefix != sys.base_prefix

import numpy as np
from scipy.special import gammaln

ALPHA = math.log(4 / 3) / math.log(3)
P = math.log(3)
U0 = 1e-6
V0 = 1e7


def is_a(phi):
    return (phi - np.floor(phi)) < 0.25


def e1(phi, k, depth=80):
    """<1, Bhat_phi 1> = sum over strict descendants of squared normalised masses."""
    n = 4 * 3 ** (k - 1)
    acc = np.ones_like(phi)
    for lvl in range(depth, 0, -1):
        s = np.where(is_a(phi + lvl * ALPHA), 10 / 16, 1 / n)
        acc = 1 + s * acc
    s0 = np.where(is_a(phi), 10 / 16, 1 / n)
    return s0 * acc


def F(phi, u, k):
    n = 4 * 3 ** (k - 1)
    out = np.empty_like(u)
    big = u > V0
    if big.any():
        out[big] = 1 / u[big] + e1(phi[big], k) / u[big] ** 2
    rest = ~big
    a = rest & is_a(phi)
    b = rest & ~is_a(phi)
    if a.any():
        ph = phi[a] + ALPHA
        x1 = F(ph, u[a] / 0.75, k)
        x2 = F(ph, u[a] / 0.25, k)
        out[a] = x1 / (1 - x1) + x2 / (1 - x2)
    if b.any():
        x = F(phi[b] + ALPHA, u[b] * n, k)
        out[b] = n * x / (1 - x)
    return out


def xi(phi, u, k):
    return (F(phi, u, k) > 1.0).astype(float)


def mubar(k):
    return math.log(4 / 3) + (3 * k / 4 + 1 / 16) * P


def counts(k, X):
    """Return (mubar*t*D, mubar*t*N) at log_3(1/t) = X."""
    step = mubar(k) / P
    dmax = int(X / step + 40 * math.sqrt(X) + 100)
    a = np.zeros(dmax + 1, dtype=np.int64)
    for d in range(dmax):
        a[d + 1] = a[d] + int(is_a(np.array(d * ALPHA)))
    b = np.arange(dmax + 1) - a
    tD = 0.0
    phis, us, ws = [], [], []
    for d in range(dmax + 1):
        base = d * ALPHA + k * b[d]
        na = int(a[d])
        jhi = min(math.floor(X + math.log(4, 3) - base), na)
        jlo = max(math.ceil(X + math.log(1e-14, 3) - base), 0)
        if jhi < 0 or jlo > jhi:
            continue
        js = np.arange(jlo, jhi + 1)
        lw = (gammaln(na + 1) - gammaln(js + 1) - gammaln(na - js + 1)
              + js * math.log(0.25) + (na - js) * math.log(0.75))
        w = np.exp(lw)
        S = base + js
        u = np.power(3.0, S - X)
        tD += float((w * u)[S < X].sum())
        keep = (u >= U0) & (w > 1e-18)
        phis.append(np.full(keep.sum(), d * ALPHA))
        us.append(u[keep])
        ws.append(w[keep])
    phi = np.concatenate(phis)
    u = np.concatenate(us)
    w = np.concatenate(ws)
    tN = float((w * u * xi(phi, u, k)).sum())
    m = mubar(k)
    return m * tD, m * tN


def Q(k, X, ngrid=40000):
    """Q_k(X) = P * int 3^y xi_{{y+X}}(3^y) dy over 3^y in [U0, 4]."""
    lo, hi = math.log(U0, 3), math.log(4, 3)
    y = lo + (np.arange(ngrid) + 0.5) * (hi - lo) / ngrid
    u = np.power(3.0, y)
    val = u * xi(y + X, u, k)
    return P * val.sum() * (hi - lo) / ngrid


SCALES = (3, 4, 5, 6)      # panels at log_3(1/t) = 10^n + phase
NPH = 64                   # phases per panel
DATA = "fig_asymptotics.npz"
FIG = "paper/fig-asymptotics.pdf"


def compute(k=4):
    ph = np.arange(NPH) / NPH
    qph = np.arange(512) / 512
    q = np.array([Q(k, x) for x in qph])
    tD = np.zeros((len(SCALES), NPH))
    tN = np.zeros((len(SCALES), NPH))
    for i, n in enumerate(SCALES):
        for j, p in enumerate(ph):
            tD[i, j], tN[i, j] = counts(k, 10.0 ** n + p)
        print(f"10^{n}: mubar tD in [{tD[i].min():.4f},{tD[i].max():.4f}], "
              f"N/D in [{(tN[i] / tD[i]).min():.4f},{(tN[i] / tD[i]).max():.4f}]",
              flush=True)
    np.savez(DATA, k=k, scales=SCALES, ph=ph, tD=tD, tN=tN, qph=qph, q=q)


def plot():
    import matplotlib
    matplotlib.use("pdf")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family": "serif", "font.size": 8,
                         "mathtext.fontset": "cm", "axes.linewidth": 0.5,
                         "xtick.major.width": 0.5, "ytick.major.width": 0.5,
                         "xtick.major.size": 2.5, "ytick.major.size": 2.5})
    z = np.load(DATA)
    ph, tD, tN, qph, q = z["ph"], z["tD"], z["tN"], z["qph"], z["q"]
    fig, axes = plt.subplots(1, len(SCALES), figsize=(6.3, 2.0), sharey=True)
    for i, (ax, n) in enumerate(zip(axes, z["scales"])):
        ax.axhline(1.0, color="0.85", lw=0.5, zorder=0)
        ax.plot(qph, q, color="0.35", lw=0.8, zorder=1)
        ax.plot(ph, tD[i], "o", ms=1.6, mfc="none", mec="0.55", mew=0.5, zorder=2)
        ax.plot(ph, tN[i] / tD[i], "o", ms=1.6, color="black", mew=0, zorder=3)
        ax.set_xlim(0, 1)
        ax.set_ylim(0.6, 1.4)
        ax.set_xticks([0, 0.5, 1])
        ax.set_xticklabels(["0", "", "1"])
        ax.set_title(rf"$\log_3(1/t)\approx10^{{{n}}}$", fontsize=8, pad=3)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        if i:
            ax.spines["left"].set_visible(False)
            ax.tick_params(left=False)
    axes[0].set_yticks([0.6, 0.8, 1.0, 1.2, 1.4])
    last = axes[-1]
    last.annotate(r"$\mathsf{n}/D$ (dots)", xy=(0.66, 1.31), fontsize=7,
                  ha="center")
    last.annotate(r"$Q_4$ (line)", xy=(0.33, 0.67), fontsize=7, ha="center",
                  color="0.35")
    last.annotate(r"$\bar\mu_4\,tD$", xy=(0.45, 1.065), fontsize=7,
                  ha="center", color="0.45")
    fig.supxlabel(r"fractional part of $\log_3(1/t)$", fontsize=8, y=0.02)
    fig.tight_layout(pad=0.3, w_pad=0.6)
    fig.savefig(FIG, metadata={"CreationDate": None, "ModDate": None})


if __name__ == "__main__":
    if "--plot-only" not in sys.argv:
        compute()
    plot()
