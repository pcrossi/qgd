---
title: "Alpha as Einstein mean"
---

# Alpha as Einstein mean

This note records the self-contained derivation of the geometric normalization of $\alpha$ used in Chapter 16. It replaces the need to consult historical external files outside the manuscript.

## 1. Statement

The fine structure constant must be obtained as the effective normalization of the primitive electromagnetic channel, not as an inserted experimental value.

In the Einstein cosmological space:

$$
K_E=T^5\times S^3,
$$

the electrical channel is represented by a primitive generator $U(1)_Q$. The official local bulk remains:

$$
M=\mathbb R^4\times T^4.
$$

The Einstein space provides the global normalization; the global-local bridge transports this normalization to the laboratory chart under the already declared hypotheses of flux compatibility, symplectic current, and absence of leakage from the photonic channel.

## 2. Effective Hessian of the electrical channel

The second variation of the official action restricted to the horizontal mode $U(1)_Q$ generates a direct coefficient:

$$
Z_{Q,\rm dir}^E
=
\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma
\left[
\tau
\int_{K_E}
\mathcal U_*
\lVert\xi_Q\rVert_{q_*}^2
dV_{q_*}
\right].
$$

Here $\xi_Q$ is the primitive internal charge field and $\mathfrak P_\gamma$ indicates the causal pullback to the boundary $\gamma$.

Since the orthogonal modes respond linearly to the electrical source, the observed stiffness is not just $Z_{Q,\rm dir}^E$. It is the Schur complement of the physical Hessian:

$$
Z_Q^E
=
v^T
\left(
Z_{QQ}
-
Z_{Q\perp}Z_{\perp\perp}^{-1}Z_{\perp Q}
\right)
v.
$$

In natural units:

$$
\alpha_E
=
\frac{1}{4\pi Z_Q^E}.
$$

This is the point where QGD replaces the language of free coupling with a calculable geometric impedance.

## 3. Chamber ensemble and origin of $1920$

Let $W(D_5)$ be the Weyl group:

$$
W(D_5)\simeq(\mathbb Z_2)^4\rtimes S_5,
\qquad
|W(D_5)|=2^4 5!=1920.
$$

The number $1920$ is neither local holonomy nor a fit. It enters as the cardinality of the complete cosmological orbit when the entire background is transported by pullback:

$$
\Phi_a=(g_a,J_a,H_a,f_a,\mathcal U_a,Q_a),
\qquad
\Phi_{\gamma a}=\gamma^*\Phi_a.
$$

Since the official action is covariant under pullback,

$$
\mathcal S_{\rm GDQ}[\Phi_{\gamma a}]
=
\mathcal S_{\rm GDQ}[\Phi_a].
$$

In the isotropic ensemble, all chambers of the orbit have the same weight:

$$
w_a=\frac1{|W(D_5)|}.
$$

Therefore, the angular weight of a fundamental chamber in the five angles is:

$$
\mathcal V_{\rm chamber}
=
\frac{\pi^5}{1920}.
$$

The restriction is important: if an external axis is frozen before the average, the physical group reduces to the stabilizer of that axis and one cannot divide by $1920$ without double counting. The formula below uses the complete transported orbit.

## 4. Fourth root as geometric mean

The physical response observed in four directions should not be the sum of eigenvalues nor the raw volume. For a positive compliance tensor $\mathsf C_E$, the multiplicative scale invariant under base change is:

$$
C_E
=
\left(
\det\mathsf C_E
\right)^{1/4}.
$$

In the isotropic ensemble, the orbit distributes the chamber weight equally among the four physical directions. Therefore:

$$
\det\mathsf C_E
=
\frac{\pi^5}{1920},
$$

and:

$$
C_E
=
\left(
\frac{\pi^5}{1920}
\right)^{1/4}.
$$

Thus, the fourth root is not a dimensional artifice: it is the geometric mean of the physical compliance in four directions.

## 5. Isotropic projector as Hessian contraction

Pullback covariance implies:

$$
[K_{\rm phys},\gamma]=0,
\qquad
\gamma\in W(D_5).
$$

After averaging over the complete orbit, the physical subspace of four directions is isotropic. By Schur's lemma:

$$
K_{\rm phys}\big|_{\mathscr H_{\rm phys}^{(4)}}
=
\lambda_E\mathbf 1_4,
\qquad
\lambda_E>0.
$$

Therefore:

$$
K_{\rm phys}^{-1}\big|_{\mathscr H_{\rm phys}^{(4)}}
=
\lambda_E^{-1}\mathbf 1_4.
$$

In the projective ratio that defines the electrical channel, $\lambda_E^{-1}$ cancels. The remainder is an angular/torsional contraction:

$$
\mathcal P_{\rm iso}
=
\frac{1}{\pi^4}
\left\langle
\Pi_{\rm circ}^2
\right\rangle_{\rm Hopf}.
$$

On the unit Hopf axis $u\in S^3$, the Haar moment used is:

$$
\left\langle
(n\cdot u)^4
\right\rangle_{S^3}
=
\frac18.
$$

The coherent contraction of the three Cartan-Schouten directions preserved by parallelizing torsion enters as $3^2$. Therefore:

$$
\mathcal P_{\rm iso}
=
\frac1{\pi^4}
\frac18
3^2
=
\frac9{8\pi^4}.
$$

## 6. Result

The resulting expression is:

$$
\alpha_E^{\rm mean}
=
\frac{9}{8\pi^4}
\left(
\frac{\pi^5}{1920}
\right)^{1/4}.
$$

It combines two factors:

1. the geometric mean of the four physical eigenvalues of the global compliance;
2. the isotropic projector of the electrical channel.

The fundamental chamber of the cosmological torus has weight:

$$
\mathcal V_{\rm chamber}
=
\frac{\pi^5}{1920}.
$$

The geometric mean in the four observable directions is:

$$
C_E
=
\left(
\mathcal V_{\rm chamber}
\right)^{1/4}.
$$

The isotropic projector is:

$$
\mathcal P_{\rm iso}
=
\frac{9}{8\pi^4}.
$$

Therefore:

$$
\alpha_E^{\rm mean}
=
\mathcal P_{\rm iso}C_E.
$$

Numerically:

$$
\left(
\alpha_E^{\rm mean}
\right)^{-1}
=
137.036082448164\ldots.
$$

And the equivalent impedance is:

$$
Z_Q^E
=
\frac1{4\pi\alpha_E^{\rm mean}}
=
10.904984951787\ldots.
$$

Metrological comparison, without using the accepted value in the construction:

$$
\alpha_{\rm ref}^{-1}\simeq137.035999,
\qquad
\frac{
137.036082448164-137.035999
}{
137.035999
}
\simeq
6.1\times10^{-7}.
$$

## 7. DtN/Schur round diagnostic

A local round approximation uses a radial photonic kernel $K_0$ coupled to a Dirichlet-to-Neumann impedance of the first harmonic on a 4-ball:

$$
K_\partial^{\rm DtN}
=
\pi^2R^2.
$$

The reduced Schur complement is:

$$
Z_{Q,\rm red}^E
=
\frac{
K_0K_\partial^{\rm DtN}
}{
K_0+K_\partial^{\rm DtN}
}.
$$

With the preserved values from the round test:

$$
K_0=15.162605758555,
\qquad
K_\partial^{\rm DtN}=39.415718607388,
$$

one obtains:

$$
\left(
\alpha_{\rm DtN}^{\rm red}
\right)^{-1}
=
137.604601778653.
$$

This result is diagnostic, not a final closure: it shows the correct scale of the boundary impedance, but it still belongs to the local round class, not the isotropic cosmological mean.

## 8. Status

Classification: theorem conditional. The number of $\alpha$ is derived within the Einstein isotropic ensemble class, with global-local transport of the photonic channel. The remaining condition is to verify whether the actual global background belongs to this class or if it requires a less symmetric average.
