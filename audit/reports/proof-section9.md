# Cold proof audit: Section sec:positive and related prose (2026-11-14)

Source: `paper/main.tex` (read lines 1-900 and 1280-1720). Nothing in main.tex was edited.
Scratch scripts (not part of the paper; not retained in the release, so these numerical spot checks are unreproduced here): cf_check.py, gram_check.py, lattice_check2.py, split31.py, run in a shared isolated virtual environment. [Local paths redacted for release.]

## Verdicts by claim

### 1. Theorem thm:census (transfer under a type census): VERIFIED
- (F4)+(T1): atoms of mu_t sit at z = t/m_v, which lies in (0,M) because m_v > t/M is strict. Vertices with m_v <= t/M contribute xi_hat_v(t/m_v) = 0 by (F3)/the hypothesis xi(r,u)=0 for u>=M. So n(T;t)/D(t) = ∫ xi dmu_t holds exactly. Neither endpoint z=0 nor z=M carries mass.
- Regular variation is used correctly. For 0<u<=M, the event {t/m_v < u} is {m_v > t/u}, which already implies m_v > t/M. Then D(t/u)/D(t) -> u (index -1, with b=1/u), and (T2) is applied at s=t/u -> 0. Only finitely many u are needed for each step function, so pointwise regular variation is enough.
- Step function to continuous function to Stone-Weierstrass: valid. Use half-open steps 1_[a,b) on [0,M) (the slice z=M is null for both mu_t and lambda). The total masses D(t/M)/D(t) -> M are eventually bounded. Products f(r)g(z) span a unital point-separating algebra, so weak convergence holds on the compact space S×[0,M].
- Envelopes: discontinuity sets are F_sigma, hence Borel. On S×(0,M), continuity on S×(0,∞) is the same as continuity on S×[0,M]. The slices z=0 and z=M are lambda-null. An upper semicontinuous function equals the infimum of a decreasing sequence of continuous functions. With mu_t >= 0 and monotone convergence under the finite measure lambda, the limsup/liminf sandwich is valid. ∫xi dlambda = 1 follows from Fubini (xi Borel and bounded) and (T3).
- Remark (not an error): the regular-variation hypothesis cannot be removed; see item 6a.

### 2. "The counterexamples fail (T2)": VERIFIED
- From Lemma lem:walk with f(S) = e^S 1{S<x} f(theta_d), we get s·Σ_{m_v>s} f(theta_|v|) = Σ_d E[f(theta_d) h(x-S_d)]. So F_theta(u) = f(theta)h(u) is right.
- (H1) holds with C = ||f||_∞ and u_0 = 0. (H2): Gamma_x(theta) = f(theta) psi(x/P - theta). For f >= 0, multiplying the continuous brackets psi^± by f (and a small uniform slack for finitely many translates) gives (H2). The paragraph assumes f >= 0, and the step is valid only for f >= 0 (or after adding a constant).
- Fourier coefficient: psi is the periodization of h(Pw), so psi_hat(n) = ∫_0^∞ e^{-Pw - 2πinw} dw = 1/(P+2πin). VERIFIED.
- The comparison term is the circle convolution (f*psi)(x/P), with coefficients f_hat(n) psi_hat(n). It is a nonconstant continuous periodic function unless f is constant. Since sD(s) -> 1/mu_bar, (1/D(s))Σ f oscillates, so (T2) fails.
- Note: this only shows that the *phase* typing fails (T2). That *no* typing satisfies (T1)-(T3) follows from Theorem thm:main and Theorem thm:census by contraposition. The text could say so in one clause (optional).

### 3. Lemma lem:coprime: VERIFIED
Möbius inversion; Riemann sums with mesh d/R for each fixed d; a uniform tail bound ||H||C²/d² (at most (CR/d)² lattice points); the order of limits is right.

### 4. Theorem thm:cf: VERIFIED (minor presentational gaps only)
Each item below was checked by hand. Items marked [num] were also checked numerically.
- m_w = ∫_0^1 (q+py)^{-2} dy = 1/(q(q+p)). The child ratio is (1+r)/((a+r)(a+1+r)), decreasing in a, and equal to 1/(2+r) ∈ [1/3,1/2] at a=1. r_{wa} = 1/(a+r). [num: every child of every word with m > 1e-6 matches the formula to 1e-12; the a=1 ratio lies in [1/3,1/2]; exact rational checks of |h_w(0)-h_w(1)| = 1/(q(q+p)) and r_w = [0;a_n,...,a_1] for all words of length ≤ 4 with digits ≤ 5.]
- theta = 1/2 and M_theta = 2. D finite: q ≤ t^{-1/2}, and there are finitely many words per q.
- Multiplicity: each coprime pair 1 ≤ p < q comes from exactly 2 words. The only exceptions are (1,1) (word "1") and (1,0) (empty word). Why it holds: gcd(q_n, q_{n-1}) = 1, so the ratio fixes the pair, and the two CF expansions of p/q are reversed. [num: s=1e-6, about 4.2·10^5 vertices; zero exceptions; every coprime pair with q(q+p) < 10^6 appears exactly twice.]
- Every rational in [0,1] is a vertex type (0 from the empty word, 1 from "1", and the rest by the multiplicity argument). VERIFIED.
- Unitary equivalence: under x = h_w(y), dx/m_w becomes (1+r)/(1+ry)² dy = g_r² dy, and h_w(I_v) = I_{wv}. The identities U R_f U* = R_{Uf} and R_{gf} = M_g R_f M_g give U T_hat_w U* = A_{r_w} and U B_hat_w U* = B_{r_w}. VERIFIED.
- ||A_r|| ≤ 2 for all r: the bound holds at the dense set of rationals by (F1), and r ↦ A_r is norm-continuous because sup|g_r - g_r'| -> 0. Values in {0,1} by rank-one interlacing (A_r compact, B_r ≥ 0). xi(r,u) = 0 for u ≥ 2 because B_r ≤ A_r. VERIFIED.
- Area one for irrational r: Weyl convergence of the counts off the countable spectra, then dominated convergence on (0,2). VERIFIED.
- Local constancy off the eigenvalue graphs: lambda_k(A_r) and lambda_k(B_r) are 1-Lipschitz in operator norm, and only finitely many indices can exceed u/2 near r. The discontinuity set is therefore contained in countably many graphs of continuous functions plus {u=0}, which is null for dr⊗du, so (T3) holds for any kappa ≪ dr. VERIFIED.
- Small gaps (optional to fix): (i) Borel measurability of xi on [0,1]×(0,∞) is not stated. It follows because each 1{lambda_k(r) > u} is the indicator of an open set. (ii) The phrase "only finitely many eigenvalues near r exceed u/2" should read "there is K such that lambda_k(A_{r'}), lambda_k(B_{r'}) < u/2 for all k ≥ K and all r' near r".
- Riemann integrability of H: H is bounded, and is continuous off the boundary of a Jordan-measurable region and the origin. VERIFIED.
- Jacobian: d(u,r)/d(x,y) = 2(1+r), so dx dy = du dr/(2(1+r)) and ∫H = (1/2)∫_0^1 f(r)dr/(1+r). VERIFIED.
- Census limit: the limit is s Σ f(r_w) -> (6/π²)∫_0^1 f(r)dr/(1+r). [num, s=1e-6: s·D = 0.42139 vs 6 log 2/π² = 0.421383; f=r² gives 0.117411 vs 0.117419.]
- The Gauss-measure normalization dr/((1+r) log 2) is right. 1/h = 6 log 2/π² is right, with h = π²/(6 log 2) the entropy of the Gauss map. Regular variation of D_CF holds. lambda_j ~ C/j follows by inversion.
- Not numerically confirmed: n(T_CF;t)/D_CF(t) -> 1. Truncated Gram matrices (about 2800 vertices, t ∈ [0.009,0.09]) give ratios scattered in 0.75-1.25, with D only 4-48. That is consistent with slow convergence but carries no evidential weight.

### 5. zeta_D identity for the CF tree: VERIFIED; wording and citation need care
- zeta_D(z) = 1 + 2^{-z} + 2Σ_{coprime 1≤p<q}(q(q+p))^{-z}. Writing each pair q > p ≥ 1 as d·(coprime pair) gives Σ_all = zeta(2z)·Σ_coprime, so the displayed formula holds for Re z > 1 (where Σ_{q>p}(q(q+p))^{-σ} converges iff σ > 1). [num at z=2: 1.3511312 (truncated sum over vertices; tail about 4e-7) vs 1.3511315.]
- Wording: "Sorting coprime pairs by their greatest common divisor" is wrong as written. The sorting is of *all* pairs q > p ≥ 1.
- zeta_T sentence: correct. The vertex formula zeta_T = z Σ_v m_v^z M_v(z) uses only Tonelli, (F4) and n(T;t) = O(1/t), all of which hold for the CF tree. M_{p/q} depends only on the ratio, so gcd sorting applies. But Corollary cor:zeta is stated only for T_{r,k}, so the text should say the same proof applies.
- CFV attribution: not checked (no access). Fact: the series that is exactly expressible through zeta(2z-1)/zeta(2z) is Σ_w q_w^{-2z} = 2Σ_{q≥1} φ(q) q^{-2z} = 2 zeta(2z-1)/zeta(2z), using 2φ(q) words per q ≥ 2 and 2 words with q = 1, as checked above. zeta_D itself carries the extra factor (1+r_w)^{-z}. The current sentence ("Essentially this series ... is expressed through zeta(2z-1)/zeta(2z)") is hedged, but it should name the exact identity.

### 6. Prose claims

a. **Abstract (lines 58-62), intro (lines 289-293), section opener (lines 1297-1301): OVERSTATED (must fix).**
None of these three states that D must be regularly varying. None mentions the regularity hypothesis (T3). The intro says "no condition on the ratios", but eq:tree (a_v ≤ theta < 1) is itself a ratio condition.

The regular-variation omission is a real error, not pedantry. Counterexample: the self-similar tree that splits every interval into children of relative lengths 1/2, 1/4, 1/4. Every normalized subtree is identical, so (T1) holds with a one-point S, (T2) holds trivially, and (T3) holds because a {0,1} profile with countably many jumps is continuous a.e. But D is a step function with jumps at 2^{-k}, so it is not regularly varying. Truncated Gram matrices (2730 vertices; the Weyl brackets ±2ε are tight for k=5,6,7) give, at every scale k=5,6,7:
- n/D ≈ 1.52 at t = 1.02·2^{-k};
- n/D ≈ 1.00 at t = 1.25·2^{-k};
- n/D ≈ 0.76 at t = 1.75·2^{-k}.

For example, at k=7: D = 85 throughout, while n = 128, 85, 64. Since D is constant on (2^{-k-1}, 2^{-k}) while n halves inside that interval, the ratio cannot converge.

The abstract's first paragraph sets D(t) ~ C/t as context, so a charitable reader may carry that over. The intro paragraph and the section opener do not restate it.

b. **Line 1503-1505: OVERSTATED (should fix).** The text reads: "So vanishing child ratios are not necessary for the law, even in a natural arithmetic tree. The tree has infinitely many children per vertex; the counterexamples ... have finitely many."
- The first sentence is true, but it invites the reading that the CF tree is the first or simplest such example, and that no finitely-branching positive example is known.
- Any fixed-split *nonlattice* self-similar tree is a simpler example: one type, and D ~ C/t by the nonlattice renewal theorem. For instance, every interval split 3:1: two children, ratio 3/4, log-ratios log(4/3) and log 4 are incommensurable. Theorem thm:census with a one-point S gives n ~ D at once. It is plausibly already covered by K26 Thm A.4 with a single class (inference: I have not read K26).
- My truncated numerics for the 3:1 tree are inconclusive (ratios 0.88-1.08, brackets wide), but the deduction needs no numerics.
- The CF tree's real distinction is that its types vary over a continuum and the census needs arithmetic.

c. **Roadmap sentence (lines 326-328): VERIFIED.**

d. **Remarks, "Relation to self-similar spectral asymptotics"**
- CF sentence: VERIFIED as hedged; the CFV section number was not checked.
- Rastegaev sentence: not verified (no web access). As written, "the eigenvalue count is a power ... times a continuous periodic function" should say "is asymptotically". Whether the periodic function is continuous in Rastegaev's setting is unchecked.
- KL theorem numbers: not checked.

e. **Remarks, "Zeta functions"**: see item 5.

f. **Open question (3): VERIFIED** (fair statement).

g. **Open question (5): wording ambiguous (optional fix).**
- "Does Theorem thm:cf hold for the Gauss measure" collides with the theorem's own statement, in which the Gauss measure is the limiting type distribution. It should say that Lebesgue measure on the cylinders is replaced by the Gauss measure or another density.
- Substance (inference, not proved here): for the Gauss measure the normalized subtree is still determined *exactly* by a type in a compact set, namely (q_{n-1}/q_n, p_n/q_n, p_{n-1}/q_{n-1}), because the pulled-back density is ∝ 1/((q+py)((q+p_n)+(p+p_{n-1})y)). So Theorem thm:census applies once the joint census of (r_w, position) converges. That reduces to equidistribution of modular inverses (p_n ≡ ±q_{n-1}^{-1} mod q_n), which Weil/Kloosterman bounds or lattice-point counts in GL_2(Z) should supply.
- For a general continuous density, exact types fail, and one needs approximate types (OQ3), not only joint equidistribution.

## Must-fix
1. **Abstract, lines 58-59.** Replace "In the other direction, the law holds whenever the shapes of the subtrees, counted at each small threshold, have a limiting distribution." with:
   "In the other direction, when $D$ is regularly varying (for example $D(t)\sim C/t$), the law holds whenever the shapes of the subtrees, counted at each small threshold, have a limiting distribution and the spectral profile depends almost everywhere continuously on the shape."
2. **Intro, lines 289-293.** Replace with:
   "If $D$ is regularly varying, the normalized subtree at each vertex is determined by a type in a compact space, the profile depends almost everywhere continuously on the type, and the types of the vertices of mass above $t$ have a limiting distribution as $t\downarrow0$, then $\ncount(T;t)\sim D(t)$, with no condition on the ratios beyond~\eqref{eq:tree} (Theorem~\ref{thm:census})."
3. **Section opener, lines 1297-1301.** Add "and $D$ is regularly varying with index $-1$" and "the profile depends almost everywhere continuously on the type". Optionally add one sentence: "Regular variation cannot be dropped: a tree that splits every interval into parts $\frac12,\frac14,\frac14$ has a single type, yet $\ncount(T;t)/D(t)$ oscillates." The numerics above support this; a proof would need the profile, so phrase it as an observation or omit it.
4. **Zeta paragraph, line 1594.** Replace "Sorting coprime pairs by their greatest common divisor gives" with "Writing each pair $q>p\ge1$ as $d$ times a coprime pair gives".

## Should-fix / optional
5. **Lines 1503-1505.** Replace with something like: "Vanishing child ratios are therefore not necessary for the law. The simplest examples are self-similar: a tree that splits every interval $3:1$ has a single type and a nonlattice mass count, so Theorem~\ref{thm:census} applies with $S$ a point. The continued-fraction tree is an example in which the types vary over a continuum and the census is arithmetic." Check K26 Thm A.4 and cite it if it already covers the single-class case.
6. **CFV sentence (lines 1599-1603).** Make it exact: "The closely related series $\sum_wq_w^{-2z}=2\sum_{q\ge1}\varphi(q)q^{-2z}=2\zeta(2z-1)/\zeta(2z)$ ..."; then state what CFV do with $\zeta_D$ only after checking the source.
7. **zeta_T sentence.** Add "(the proof of the vertex formula in Corollary~\ref{cor:zeta} uses only (F4) and $\ncount(T;t)=O(1/t)$, and applies here)".
8. **Proof of thm:cf.** State that xi is Borel. Tighten the "only finitely many eigenvalues near r exceed u/2" sentence as in item 4(ii).
9. **(T2)-failure paragraph.** Add one clause: "By Theorems~\ref{thm:main} and~\ref{thm:census}, no choice of types satisfies (T1)--(T3) for these trees."
10. **OQ(5).** Reword to "Does $\ncount\sim D$ hold for the continued-fraction cylinders when Lebesgue measure is replaced by the Gauss measure, or by any continuous positive density?" Optionally note the exact-type reduction for the Gauss measure.
11. **Rastegaev sentence.** Insert "asymptotically" and verify "continuous" against the source.

## Not checked
- K26 facts (F1)-(F4) were taken as given, per instructions. The content of K26 Thm A.4, and whether its single-class case already gives item 6b, was not checked.
- Citations: CFV §8.3 (including the zeta(2z-1)/zeta(2z) and zeros statement), EW Ch. 3, KL Thm 2.4/Cor 2.5, and the content of Rastegaev 2024.
- Earlier sections (Lemma lem:brackets, Theorem thm:periodic, Corollary cor:zeta proofs) were read only as far as needed to check the hypotheses used. They were not re-audited.
- The built PDF was not inspected.
- n(T_CF;t)/D_CF(t) -> 1 was not confirmed numerically (sizes too small to show anything).
- The 1/2,1/4,1/4 oscillation is numerical evidence (tight Weyl brackets at k=5-7), not a proof.
