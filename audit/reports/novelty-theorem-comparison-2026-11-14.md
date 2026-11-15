# Theorem-level prior-art comparison, 2026-11-14

Target: `paper/main.tex` (abstract, Section 1, Theorems 9.1 `thm:census` and 9.2 `thm:cf`, Section 10 related-work remark). Claims compared:

- **R1**: for every theta, bounded-branching interval trees with D(t) ~ C/t where n(T;t)/D(t) tends to a nonconstant log-periodic function; the largest possible oscillation width is Theta(theta).
- **R2**: n(T;t) ~ D(t) under a convergent census of subtree types (Thm 9.1).
- **R3**: continued-fraction cylinder tree, n(T;t) ~ D(t) ~ 6 log 2/(pi^2 t) (Thm 9.2).

Scope: bounded (~25 min). Primary texts are public arXiv/author copies; "full text" below means the PDF was downloaded and the theorem statements were read with `pdftotext`. This is not a worldwide novelty clearance.

## Overall verdict

No source read **contains or implies** R1, R2 or R3. Every source is either (a) a boundedness or compactness criterion, (b) two-sided order-of-magnitude bounds (entropy numbers, Schatten classes, small-deviation asymptotics at log level), (c) an exact Weyl-type asymptotic for a *different* operator class with a different decay exponent, or (d) an exact spectral calculus for *difference-form* ultrametric operators. Those operators are diagonal in a Haar basis for any measure. T is not, as soon as the splits are unequal.

Two items should be credited more specifically than the present generic "`\cite{EHL,NS,LL,BGPW}`":

1. **Identification of T** (must add). Up to unitary equivalence, T is the p = 2, rho = 1 case of the Arcozzi–Rochberg–Sawyer tree Carleson embedding: T = I I*_mu, where I: l^2(tree) -> L^2(tree-bar, mu) is the tree Hardy (path-summation) operator, mu is the pushed-forward measure, and I*_mu g(alpha) = ∫_{S(alpha)} g dmu. ARS's tree condition then reads Σ_{beta>=alpha} m_beta^2 <= C m_alpha, which is the boundedness of T. The intro sentence "We know of no standard name for T elsewhere" is therefore too strong. Suggested replacement: "Up to unitary equivalence, T = I I^*, where I is the tree Hardy operator into L^2 of the boundary measure; the boundedness of I is the tree Carleson condition of Arcozzi–Rochberg–Sawyer [ARS02, ARS07]. We know of no prior work on its exact eigenvalue asymptotics."
2. **Naimark–Solomyak 2000, Example 8.1** (should add). It already obtains a log-periodic leading term n(λ) = λ^{-δ} w(ln λ^{-1}) + o(λ^{-δ}) for an operator on a tree, via the renewal equation. Their trees are (b,q)-regular with symmetric weights, so the operator splits into an orthogonal sum of 1-D problems (their Thm 7.2), and the tree geometry itself is lattice self-similar. The paper's renewal-plus-periodicity mechanism is therefore not new on trees either. What still separates R1 is that its own mass count D(t) ~ C/t does not oscillate while n(T;t) does, on a non-symmetric tree. NS also do not prove that w is nonconstant.

The existing related-work remark (Kigami–Lapidus, Rastegaev, fractal strings, "no priority across operator classes") stays accurate. With items 1–2 added, the surviving novelty statement is the one the paper already makes: a within-operator comparison in which n(T;t)/D(t) oscillates while D(t) ~ C/t, plus the census transfer and the CF constant. Nothing read states the CF eigenvalue law (R3). Thm 9.1 (R2) is a transfer theorem of a kind not found in any of these sources. Its closest analogues are the K26 profile theorems the paper already credits.

## Family 1: Carleson embeddings / Hardy operators on trees (ARS, Wick, multi-tree)

Sources:
- Arcozzi–Rochberg–Sawyer, "The characterization of the Carleson measures for analytic Besov spaces: a simple proof", arXiv 0706.1936. Full text. Thm 1 (Car ⇔ VarCar ⇔ TreeCar ⇔ TC); Section 3, Thm 4. With I: L^p(T, rho) -> L^p(T-bar, mu) and I*_mu g(alpha) = ∫_{S(alpha)} g dmu, boundedness holds iff the tree condition Σ_{beta>=alpha} mu(S(beta))^{p'} rho^{1-p'}(beta) <= C mu(S(alpha)) holds. Boundary measures on ∂T are explicitly allowed (§2).
- ARS, "Carleson measures for analytic Besov spaces", Rev. Mat. Iberoam. 18 (2002). Abstract and the 0706.1936 summary only. Reduction to a discrete tree problem; boundedness characterization.
- Arcozzi–Rochberg–Sawyer–Wick, NYJM 17a (2011) Dirichlet-space survey. The download failed (the server returned HTML), so it was **not read**.
- Mozolyako–Psaromiligkos–Volberg–Zorin-Kranich, "Carleson embedding on tri-tree and on tri-disc", arXiv 2001.02373. Abstract. Boundedness characterization of multi-tree Hardy embeddings.

Theorem type: boundedness (and, by the usual vanishing variant, compactness) of the embedding. No eigenvalue counting, no exact asymptotics, no oscillation.

Relation to T: exact identification. In ARS notation take p = 2 and rho ≡ 1. Points of A_v not covered by children correspond to mu-mass at vertex v; mass carried by infinite paths corresponds to boundary mass. Then V = I and T = V V* = I I*_mu on L^2(mu).

A Schatten-class (Luecking-type) criterion for tree embeddings was searched for (1 query) and **not found**. Even if one exists, it would give S_p membership only (Σ m_v^p < ∞ type conditions, consistent with K26's sandwich). It cannot give exact asymptotics or oscillation.

**Verdict: RELATED-ONLY**, but credit-worthy for the operator identification (see above).

## Family 2: Evans–Harris–Lang and follow-ups

Source: Evans–Harris–Lang, "The approximation numbers of Hardy-type operators on trees", arXiv math/0003215 (= PLMS 83 (2001) 390–418). Full text.

Operator: (T_a f)(x) = v(x) ∫_a^x u(t) f(t) dt on L^p(Γ), where Γ is a **metric** tree with 1-D Lebesgue measure on the edges, and the input and output live on the same edge measure. Main results: Thm 5.3 gives lim ε N(Γ,ε,u,v) = α_p ∫|u||v|. The main theorem (the "(*)" of the abstract, proved after Thm 5.3, and Thm 6.4 under alternative hypotheses) gives lim_{n→∞} n a_n(T_a) = α_p ∫_Γ |uv| dt for 1 < p < ∞, with u, v in L^p-type classes. Thms 6.5–6.6 give l^q and weak-l^q bounds. For p = 2, α_2 = 1/π, which is the Naimark–Solomyak / Newman–Solomyak law.

Why it does not cover T:
- **Decay exponent.** Under EHL hypotheses a_n ~ c/n with c = α_p∫|uv| < ∞, i.e. weak-S_1. Our V has s_r(V) = sqrt(λ_r(T)), and in R3 λ_r ~ C/r, so s_r(V) ~ sqrt(C/r). V is not even in S_2 when children cover parents (trace T = Σ_v m_v = ∞). No operator in the EHL class with finite ∫|uv| has this decay, so no EHL theorem can produce R3's constant.
- **Measure.** EHL's target is Lebesgue measure on the edges. Our target measure ν sits on the boundary (ends) of the combinatorial tree. A change of variables along the edges cannot move it there.
- **Statement type.** EHL's limit is always a constant Weyl-type density integral. They give no oscillating case and no comparison with a vertex-mass count.

Follow-ups surfaced by search (Lang 2003, Edmunds–Lang–Nekvinda 2009, Solomyak math/0206235 on metric graphs) concern the same metric-graph Hardy/Volterra class (abstract or snippet level; not read in full). **Verdict: RELATED-ONLY.**

## Family 3: Naimark–Solomyak 2000 and Solomyak's tree papers

Source: Naimark–Solomyak, "Eigenvalue estimates for the weighted Laplacian on metric trees", PLMS 80 (2000) 690–724. Full text, public author-hosted copy at math.ucdavis.edu/~saito/data/LapEig/naimark-solomyak-lapeig-metrictree.pdf.

Operator: A(G;V), a realization of (−Δ)^{-1}V on a metric tree with a Dirichlet condition at the root. Thm 3.2 is boundedness; Thm 3.3 is a trace-class criterion; Thm 4.1 gives Σ_k λ_k^p upper bounds via partitions and the Weyl law lim λ^{1/2} n(λ) = π^{-1}∫ V^{1/2} under the finiteness condition (4.2); Thm 4.6 is a converse for special trees; Thms 5.1/5.5 give an orthogonal decomposition; Thm 7.2 treats regular trees with symmetric V, where the operator is an orthogonal sum of 1-D second-order problems. **Example 8.1** uses (b,q)-regular trees with V(t) = t^{-a}: a renewal equation gives n(λ) = λ^{-δ} w(ln λ^{-1}) + o(λ^{-δ}) with w γ-periodic, bounded and bounded away from 0 (non-Weyl case). Nonconstancy of w is not proved there.

Relation: different operator (second-order, metric tree, Lebesgue edge measure). Example 8.1 is a precedent for renewal-driven log-periodic spectral counting **on trees**, but only for homogeneous trees and symmetric data. There the periodicity is inherited from the lattice geometry, and there is no non-oscillating comparison count. Solomyak's "On the spectrum of the Laplacian on regular metric trees" (snippet only) uses the same symmetric reduction. **Verdict: RELATED-ONLY; add a specific citation to Example 8.1** (see the overall verdict).

## Family 4: Lifshits–Linde summation operators and Gaussian sums on trees

Sources:
- Lifshits–Linde, "Compactness properties of weighted summation operators on trees", arXiv 1006.3867 (Studia Math. 202 (2011)). Full text.
- Lifshits–Linde, "… the critical case", arXiv 1009.2339 (Studia Math. 206 (2011)). Abstract, plus PDF downloaded.
- Lifshits–Linde, "Random Gaussian sums on trees", arXiv 1012.2683 (EJP 16 (2011)). Abstract.
- Han–Qiu–Wang, "Boundedness of Gaussian random sums on trees", arXiv 2107.04177 (Moscow Math. J. 24 (2024), "…on rooted homogeneous trees"). Abstract.

LL operator: (V_{α,σ}x)(t) = α(t) Σ_{s⪯t} σ(s) x(s) (sum over ancestors), as a map **l^1(T) -> l^q(T)**. Thm 4.4 and Thm 5.3 give two-sided estimates for entropy numbers e_n from covering numbers of (T,d) (≈ only, sharp only for q <= 2). Thm 6.4/6.5 cover moderate and binary trees. Prop 9.1 gives small deviations −log P(sup|X_t| < ε) ≈ ε^{-a}|log ε|^b. The critical-case paper gives upper bounds only. The Gaussian-sum papers characterize a.s. boundedness.

Is V* (or V) a weighted summation operator in their sense? Partly, and only on truncations.
- V*V on l^2(T) has entries (V*V)_{uv} = m_{deeper of u,v} when u, v are comparable and 0 otherwise. This equals the LL product V_{α,1}* V_{α,1} on l^2 with σ ≡ 1 and α(t)^2 = m_t − Σ_children m_c. That identity holds exactly when ν-almost every point lies in finitely many A_v (e.g. finite trees). In the paper's main setting, where children partition parents, α ≡ 0 and the mass sits on ∂T. V is then the boundary-valued limit of LL operators: on the depth-n truncation, α_n(w)^2 = m_w at the depth-n leaves.
- The covariance of T (kernel #common ancestors w.r.t. ν) has LL's form E X_t X_s = σσ Σ_{r⪯t∧s} α(r)^2 with α = σ = 1, but indexed by the boundary with measure ν rather than by vertices with counting measure.
- In any case LL's results concern l^1 -> l^q entropy numbers and log-level small deviations. They give orders of magnitude, never exact eigenvalue asymptotics and never oscillation.

**Verdict: RELATED-ONLY.**

## Family 5: exact log-periodic spectral asymptotics for covariance operators (Nazarov, Nikitin, Sheipak, Vladimirov, Rastegaev)

Sources:
- Rastegaev, arXiv 2011.13064 (= JST 14 (2024)). Abstract; already cited as [Ras].
- Vladimirov–Sheipak, arXiv math/0405410. Abstract.
- Nazarov–Sheipak, arXiv 1009.1252 (BLMS 44 (2012)). Abstract.
- Rastegaev, arXiv 1804.00187. Abstract.

Theorem type: exact asymptotics of the eigenvalue counting function of Sturm–Liouville problems with self-similar singular weights. The leading term is a power times a periodic function of the logarithm, and Rastegaev proves nonconstancy for a wide class. Applications are to L^2 small-ball asymptotics of Green Gaussian processes (Brownian motion, Ornstein–Uhlenbeck, integrated versions) with respect to self-similar measures.

Relation: one structural analogy is worth stating. The Wiener covariance min(s,t) = ∫ 1_{[r,1]}(s) 1_{[r,1]}(t) dr is a continuous sum of rank-one indicator operators of a **chain** of nested sets, while T is the same construction over a **tree** of nested sets. The SL results are for chains (second-order ODEs) with exponents set by the self-similar dimension. No source read treats tree-indexed or cylinder-set covariances. **Verdict: RELATED-ONLY**, already handled correctly by the paper's Rastegaev sentence. No tree-indexed analogue was found (1 targeted search).

## Family 6: ultrametric kernels K(x,y) = f(|x∧y|); Kozyrev, Khrennikov–Kozyrev, BGPW, Pearson–Bellissard

Sources:
- Khrennikov–Kozyrev, "Ultrametric pseudodifferential operators and wavelets for the case of non homogeneous measure", arXiv math-ph/0412082. PDF read (definition and abstract).
- Kozyrev, arXiv math-ph/0412062. Abstract.
- Bendikov–Grigor'yan–Pittet–Woess, arXiv 1304.6271. Abstract; already cited as [BGPW].
- Bendikov et al., "Oscillating heat kernels on ultrametric spaces", arXiv 1610.03292. Abstract.
- Pearson–Bellissard, arXiv 0802.1336. Abstract.
- Vladimirov–Pearson operators, arXiv 2504.20753. Abstract.

Theorem type: operators of **difference form** Lf(x) = ∫ J(x∧y)(f(x) − f(y)) dν(y) (Khrennikov–Kozyrev eq. (1); BGPW isotropic generators; hierarchical Laplacians) are diagonal in ultrametric Haar wavelets for **arbitrary** measures. The eigenvalue is indexed by the ball, and pure point spectrum follows. 1610.03292 obtains log-periodic heat-kernel behaviour under a transitive isometry group (homogeneous case).

Why this does not handle T. T has kernel K(x,y) = #{v : x,y ∈ A_v}, which is an ultrametric kernel, but T is the **integral** form, not the difference form. The exact identity is

  T = M_w − L_K,  w(x) = ∫K(x,y)dν(y) = Σ_{v∋x} m_v,  L_K f(x) = ∫K(x,y)(f(x)−f(y))dν(y).

L_K is Haar-diagonal for any ν (Khrennikov–Kozyrev/BGPW). M_w commutes with it only when w is constant on each ball modulo ancestors, i.e. when Σ_{v⊆B, x∈A_v} m_v is independent of x ∈ B (the uniform or balanced-split case). In that case T = w − L_K and n(T;t) is explicit. With unequal splits T is not Haar-diagonal.

Numerical check (a shared isolated virtual-environment interpreter [local path redacted for release], scratch script haar_check.py (not retained; unreproduced here) [local path redacted for release], binary tree, depth 6). T = M_w − L_K holds to machine precision. For the root Haar vector, the eigen-residual of L_K is 3e-16 for both splits. The eigen-residual of T is 0 for 1:1 splits and 0.61 (relative) for 3:1 splits. This is consistent with the paper's own toy example, where the 3:1 tree's eigenvalues are 1 ± sqrt(7)/4 rather than the masses.

No source found handles the integral (covariance) form with non-uniform splits. **Verdict: RELATED-ONLY.** Optionally the paper could add one sentence: "Difference-form ultrametric operators [BGPW, Khrennikov–Kozyrev] are diagonal in Haar wavelets for any measure; T = M_w − L_K is not, unless the splits are balanced."

## Not checked / residual risk

- ARSW NYJM survey (download failed); Lang 2003; Edmunds–Lang–Nekvinda 2009; Solomyak's regular-tree papers in full; any Luecking-type Schatten criterion on trees.
- Kigami's Cantor-set/tree Dirichlet-form papers and the Pearson–Bellissard spectral asymptotics were seen at abstract level only. They are difference-form, so the family-6 argument applies by inference.
- No search of MathSciNet/zbMATH (no access). Literature on Karhunen–Loève expansions of hierarchical or GREM-type Gaussian fields was not systematically searched.

## Downloaded material

A local scratch folder [path redacted for release; not retained] contains math_0003215 (EHL), 1006.3867 and 1009.2339 (LL), 0706.1936 (ARS), ns2000 (Naimark–Solomyak), kk0412082 (Khrennikov–Kozyrev), and arXiv API abstract XML files.
