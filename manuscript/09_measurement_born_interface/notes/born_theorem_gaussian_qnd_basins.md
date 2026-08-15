---
title: "Born-basin theorem for Gaussian QND apparatuses"
---

# Born-basin theorem for Gaussian QND apparatuses

This note demonstrates, in a precise physical class of apparatuses, that the measure of the record basins coincides with the initial spectral weight. The result does not alter the official action: it uses its physical Hessian in the joint background of the system, apparatus, and environment.

The theorem holds for apparatuses that are:

1. non-demolition in the measured channels;
2. described by the quadratic reduction of the Hessian;
3. equipped with causal outgoing Gaussian channels;
4. capable of asymptotically distinguishing all records.

Outside this class, the correspondence must be demonstrated again.

## 1. Variational data

Let $\Phi_*$ be an admissible stationary background. After removing gauge modes, the joint second variation has the form:

$$
\delta^2\mathcal S_{\rm GDQ}
=
\frac{1}{2}\langle x,K_Sx\rangle
+
\frac{1}{2}\langle y,K_Ay\rangle
+
\langle y,Jx\rangle.
$$

$x$ represents the physical modes of the object and $y$ the unmonitored modes of the apparatus and environment. Eliminating $y$ via the linear response, we obtain the Schur complement:

$$
\text{R}_{\rm eff}
=
K_S-J^\dagger K_A^{-1}J.
$$

The record channels are orthogonal spectral projectors:

$$
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I_{\rm reg}.
$$

## 2. QND condition and conservation per channel

A measurement is non-demolition, QND, when:

$$
[K_S,P_i]=0,
\qquad
[J^\dagger K_A^{-1}J,P_i]=0.
$$

Consequently:

$$
[K_{\rm eff},P_i]=0
$$

and:

$$
P_iK_{\rm eff}P_j=0,
\qquad i\ne j.
$$

There is no deterministic current between distinct channels. In the reconstructed physical time, the diagonal internal evolution only modifies phases and responses within each block. The Noether phase current provides:

$$
\left.\frac{dp_i}{dt}\right|_{\rm det}=0,
\qquad
p_i=\operatorname{Tr}(\varrho P_i).
$$

This result is stronger than the conservation of the sum $\sum_i p_i=1$: each QND block is conserved separately by the deterministic part.

## 3. Open channels produced by the Hessian

Diagonalize the macroscopic block of the apparatus into outgoing modes $y_a$. For each mode:

$$
S_{A,a}^{(2)}
=
\frac{\zeta_a}{2}
\int dt\int_0^\infty dx
\left[
\frac{1}{c_a^2}(\partial_ty_a)^2
-
(\partial_xy_a)^2
\right].
$$

The coefficients are inner products of the Hessian:

$$
\frac{\zeta_a}{c_a^2}
=
\langle T_a,K_tT_a\rangle_{\mathcal U_*},
\qquad
\zeta_a
=
\langle T_a,K_xT_a\rangle_{\mathcal U_*}.
$$

With a causal outgoing radiation condition, the retarded Dirichlet-to-Neumann operator is:

$$
\Lambda_a^{\rm ret}(\omega)
=
-i\omega\gamma_a,
\qquad
\gamma_a=\frac{\zeta_a}{c_a}>0.
$$

The whitened signal produced by channel $i$ in mode $a$ is:

$$
s_i^a(t)
=
\frac{
\langle T_a,K_A^{-1}JP_ix_*\rangle_{\mathcal U_*}
}{
\sqrt{N_a(t)}
}.
$$

$N_a$ is the spectral density of the noise of the apparatus itself. Therefore, the signals are not fundamental constants: they belong to the background, material, and boundary of the detector.

## 4. Gaussian measure of histories

Since the reduced action is quadratic in the modes $y_a$, its integration is Gaussian. If $d\mathbb Q$ denotes the measure of the whitened noise, the likelihood of the history $Y_{[0,t]}$ in channel $i$ is:

$$
Z_i(t)
=
\exp
\left[
\sum_a\int_0^t s_i^a\,dY^a
-
\frac{1}{2}
\sum_a\int_0^t(s_i^a)^2du
\right].
$$

Each density is normalized:

$$
\int Z_i(t;Y)\,d\mathbb Q(Y)=1.
$$

The QND orthogonality eliminates cross-terms. The physical measure of the histories becomes:

$$
d\mathbb P_t(Y)
=
\sum_i p_i(0)Z_i(t;Y)\,d\mathbb Q(Y),
$$

where:

$$
p_i(0)=\operatorname{Tr}(\varrho_0P_i).
$$

These coefficients are the norms of the spectral blocks of the response state before the terminal classification; they are not basin volumes inserted manually.

## 5. Conditioned filter and martingale

The conditioned weight of the channel is:

$$
p_i(t)
=
\frac{p_i(0)Z_i(t)}
{\sum_jp_j(0)Z_j(t)}.
$$

Define:

$$
\bar s^a(t)
=
\sum_jp_j(t)s_j^a(t)
$$

and the innovation:

$$
d\widetilde W_t^a
=
dY_t^a-\bar s^a(t)\,dt.
$$

Applying Itô's formula to the normalized quotient, the drift terms cancel:

$$
\boxed{
dp_i
=
p_i
\sum_a
(s_i^a-\bar s^a)
d\widetilde W_t^a.
}
$$

Hence:

$$
\mathbb E[dp_i\mid\mathcal F_t]=0
$$

and:

$$
\boxed{
\mathcal L_{\rm meas}p_i=0.
}
$$

Each $p_i(t)$ is, therefore, a bounded martingale.

## 6. Absorbing covariance

The quadratic variation is:

$$
d[p_i,p_j]_t
=
a_{ij}(p,t)\,dt,
$$

with:

$$
\boxed{
a_{ij}
=
p_ip_j
\sum_a
(s_i^a-\bar s^a)
(s_j^a-\bar s^a).
}
$$

This matrix is positive semi-definite because it is a Gram matrix. Furthermore:

$$
\sum_i a_{ij}=0,
$$

so the noise is tangent to the simplex. If $p_i=0$, the channel remains on the face $p_i=0$; at a pure vertex, all covariance vanishes. Thus, the pure records are absorbing.

## 7. Accumulated information and capture

For two distinct channels, define:

$$
\mathcal I_{ij}(t)
=
\frac{1}{2}
\sum_a
\int_0^t
|s_i^a(u)-s_j^a(u)|^2du.
$$

If:

$$
\mathcal I_{ij}(\infty)=\infty
$$

for all $i\ne j$, the likelihood ratios asymptotically separate all records. The weights converge almost surely to a single vertex:

$$
p_i(t)
\longrightarrow
\mathbf1_{\{I_\infty=i\}}.
$$

For a stationary apparatus, it is sufficient that each pair is distinguished by at least one mode:

$$
\sum_a|s_i^a-s_j^a|^2
\ge\epsilon_{ij}>0.
$$

Then:

$$
\mathcal I_{ij}(t)
\ge
\frac{\epsilon_{ij}}{2}t
\longrightarrow\infty.
$$

## 8. Born-basin theorem

Since $p_i(t)$ is a bounded martingale:

$$
\mathbb E[p_i(\infty)]
=
p_i(0).
$$

Upon capture:

$$
p_i(\infty)
=
\mathbf1_{\{I_\infty=i\}}.
$$

Therefore:

$$
\begin{aligned}
\mu_{\rm path}(\mathcal B_i)
&=
\mathbb P(I_\infty=i)
\\
&=
\mathbb E[
\mathbf1_{\{I_\infty=i\}}
]
\\
&=
\mathbb E[p_i(\infty)]
\\
&=
p_i(0).
\end{aligned}
$$

Finally:

$$
\boxed{
\mu_{\rm path}(\mathcal B_i)
=
\operatorname{Tr}(\varrho_0P_i).
}
$$

This identity does not define the basins by the Born value. It results from the martingale conservation of the spectral weights and the capture produced by the apparatus.

## 9. Finite duration

Exact capture is an asymptotic result. For a finite window $T$, a discrimination error remains, controlled by the accumulated information:

$$
\epsilon_{\rm det}(T)
\sim
\exp
\left[
-
\min_{i\ne j}\mathcal I_{ij}(T)
\right].
$$

This error belongs to the apparatus, the material, and the readout time. It is not a correction to the fundamental action.

## 10. Status

The result is closed conditionally for the Gaussian QND sector:

$$
\boxed{
\text{QND Hessian}
+
\text{causal Gaussian output}
+
\text{accumulated separation}
\Longrightarrow
\text{Born–basins}.
}
$$

For a concrete detector, it is still necessary to calculate $K_A$, $J$, $N_a$, and $s_i^a$, verify the QND commutators, and confirm the separation of the signals. Non-Gaussian, non-Markovian, demolition apparatuses, or those with moving projectors are not automatically covered.

## 11. Lean certification

The canonical module
[QNDBornBasins.lean](../../../formal/GDQ/QNDBornBasins.lean)
certifies the exact finite version of Gaussian histories. It proves:

1. preservation of the QND commutation by the Schur complement;
2. vanishing of the off-diagonal blocks between orthogonal channels;
3. positivity and normalization of the conditioned weights;
4. exact conservation of the expectation of the posterior;
5. positivity of Gram and tangency of the covariance to the simplex;
6. equality between the measure of the absorbing basin and the initial weight.

The convergence of the continuous process to a vertex uses the analytical proof in Sections 5--7. Thus, Lean does not replace the physical hypothesis that a concrete detector satisfies QND, Gaussian causality, and asymptotic separation; it certifies the deduction after these data are verified.
