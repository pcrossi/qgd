---
title: "Proofs, lemmas and definitions — Chapter 6"
---

# Proofs, lemmas and definitions — Chapter 6

This note records the clean mathematical line of the global-local bridge. It should be read as a technical supplement to Chapter 6: the body of the chapter explains the construction; this note preserves the hypotheses, operators, proofs, and reduced tests in a self-contained form.

The objective is not to identify Einstein's Universe with the laboratory. The objective is to prove that certain localized sectors can be transported between the cosmological/spectral space and the official local bulk without losing the metric, measure, physical Hessian, gap, and spectral projectors.

## Data and conventions

The official local space of GDQ is

$$
M_0=\mathbb R^4\times T^4.
$$

The cosmological/spectral space used in this bridge is a pointed family

$$
M_R=T^4\times S^1_R\times S^3_R,
\qquad R\to\infty.
$$

Here $R$ is the geometric radius. Equivalently, one can write $R=\varepsilon^{-1}$ and take $\varepsilon\to0^+$.

The transported fields are

$$
X=(g,J,H,f,\mathcal U),
\qquad
H=d_J^c\omega_g,
\qquad
\rho=e^{-(f+\bar f)/2},
\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
$$

No step alters the official action. Sources, constraints, and interface terms enter only as data of a variational problem or as physical restrictions on the background.

## Lemma 1 — Pointed limit

**Statement.** In a neighborhood of fixed proper radius around a basepoint, the family $T^4\times S^1_R\times S^3_R$ converges smoothly to $T^4\times\mathbb R^4$ as $R\to\infty$.

**Proof.** In the $S^1_R$ factor, the arc coordinate already makes the metric locally flat:

$$
ds^2_{S^1_R}=du^2.
$$

In the $S^3_R$ factor, use geodesic normal coordinates at the basepoint. The local expansion of the metric is

$$
g_{ij}^{(R)}(x)
=\delta_{ij}
-\frac13R_{ikjl}^{(R)}(0)x^kx^l
+O(|x|^3/R^3).
$$

Since the sectional curvature of the sphere of radius $R$ is $R^{-2}$,

$$
\mathcal R_{ikjl}^{(R)}=O(R^{-2}).
$$

Therefore, in any fixed ball $|x|\le L$,

$$
\left\|g^{(R)}-\delta\right\|_{C^k(B_L)}
=O(R^{-2})
$$

for all finite $k$, after choosing compatible normal charts. The $T^4$ factor is preserved. Therefore

$$
T^4\times S^1_R\times S^3_R
\xrightarrow[R\to\infty]{\rm pointed}
T^4\times\mathbb R^4.
$$

The reduced numerical test `scripts/verify_pointed_limit_torus_sphere.py` calculates the local angular error in $S^3_R$ and confirms the scale $O(R^{-2})$:

| $R$ | maximum error | $E_RR^2$ |
|---:|---:|---:|
| 5 | $1.326242503606\times10^{-2}$ | $0.33156063$ |
| 100 | $3.333288889207\times10^{-5}$ | $0.33332889$ |
| 200 | $8.333305555719\times10^{-6}$ | $0.33333222$ |

This test is a verification of geometric consistency, not an independent numerical proof of the lemma.

## Lemma 2 — Transport of fields and measure

**Statement.** If the fields $g_R,J_R,H_R,f_R$ converge in pointed charts and the weighted densities are dominated by a common integrable function, then the weighted spaces and the local functionals converge after the correct unitary transport of the measure.

**Proof.** Let $\Phi_R:U_0\to U_R$ be the pointed identification chart. The naive transport of functions does not preserve the norm when the measure changes. The physical measure is

$$
d\mu_R=\mathcal U_R\,dV_{g_R}.
$$

Define the relative Jacobian $J_R$ by

$$
\Phi_R^*d\mu_R=J_R\,d\mu_0.
$$

The unitary transport between weighted spaces is

$$
(I_R\psi)(\Phi_R(x))=J_R(x)^{-1/2}\psi(x).
$$

Then

$$
\int_{U_R}|I_R\psi|^2\,d\mu_R
=\int_{U_0}|\psi|^2\,d\mu_0.
$$

Since $g_R,J_R,H_R,f_R$ converge in $C^k_{\rm loc}$ and $\mathcal U_RdV_{g_R}$ is dominated, the dominated convergence theorem yields the convergence of the integral terms of the action and the local quadratic forms.

The script `scripts/verify_weighted_measure_transport.py` verifies the critical point: without the Jacobian, the norm scales artificially; with the Jacobian, the norm remains equal to $1$ for scales $a=0.5,1,2,4$.

## Lemma 3 — Physical Hessian and convergence of forms

**Statement.** Under local convergence of the fields, constraints, and physical projectors, the quadratic forms of the physical Hessian converge in the Mosco sense on the common core of localized perturbations.

**Construction.** Gather the relevant fields into $X=(g,J,f)$, with $H=d_J^c\omega_g$. The physical constraints are grouped in

$$
\mathcal C(X)=0.
$$

They include measure normalization, charge, interface flux, and Noether charges kept fixed. The augmented functional is

$$
\mathscr L(X,\lambda)
=S_{\rm phys}(X)-\langle\lambda,\mathcal C(X)\rangle.
$$

The admissible background satisfies

$$
D_X\mathscr L(X_*,\lambda_*)=0,
\qquad
\mathcal C(X_*)=0.
$$

If $C_*=D\mathcal C(X_*)$ linearizes the constraints and $R_*$ generates the gauge redundancies, the physical space is obtained by imposing

$$
C_*\eta=0,
\qquad
R_*^\dagger\mathbb G_*\eta=0.
$$

Define

$$
A_*=
\begin{pmatrix}
C_*\\
R_*^\dagger\mathbb G_*
\end{pmatrix}.
$$

The joint projector is

$$
P^{\rm phys}
=I-\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+A_*.
$$

The constrained Hessian is

$$
\mathbb H_*
=D_X^2\mathscr L(X_*,\lambda_*)
=D^2S_{\rm phys}(X_*)
-\sum_a\lambda_*^aD^2\mathcal C_a(X_*).
$$

The physical operator is

$$
K_*^{\rm phys}
=P^{{\rm phys}\dagger}\mathbb H_*P^{\rm phys;.
$$

It is this operator, with its domain and boundary conditions, that must be compared along the pointed family.

When there is an interface $Y$, the elimination of the exterior or complementary modes is done by Schur complement:

$$
K_Q^{\rm eff}
=K_{QQ}-K_{Q\perp}K_{\perp\perp}^{-1}K_{\perp Q}.
$$

This inverse is only valid after removing symmetry zeroes and proving the gap in the complementary sector.

**Proof.** In the pointed charts and unitary transports $I_R$, consider the physical forms

$$
q_R^{\rm phys}[\eta]
=\langle \eta,K_R^{\rm phys}\eta\rangle_R.
$$

On the common core of compactly supported perturbations, the operator coefficients, measures, constraints, and projectors converge. Therefore

$$
q_R^{\rm phys}[I_R\eta]\to q_0^{\rm phys}[\eta].
$$

The global lower semicontinuity is provided by the exterior control and the gap of Lemma 4. With the dense approximation by localized functions and the liminf estimate, Mosco convergence is obtained.

## Lemma 4 — Localization and uniform gap

**Statement.** If the local physical operator has an isolated cluster below the exterior threshold and if the forms converge locally, then the corresponding cluster of the pointed family remains uniformly isolated and its modes are localized.

**Proof.** Let $I$ be an interval containing the local cluster. Define

$$
\Delta_0
=\operatorname{dist}
\left(
I,\sigma(K_0^{\rm phys})\setminus I
\right)>0.
$$

Choose $0<\delta<\Delta_0/3$. An IMS partition with cutoff $\chi$ separates the core and the exterior:

$$
q_R[\eta]
=q_R[\chi\eta]
+q_R[\sqrt{1-\chi^2}\eta]
-\mathcal E_{\rm IMS}[\eta].
$$

The error depends on $|d\chi|^2$ and can be made smaller than $\delta$ by choosing the cutoff transition wide enough. In the core, the local convergence of the forms gives an error smaller than $\delta$ for large $R$. In the exterior, the vacuum threshold prevents modes below the cluster from escaping. Therefore

$$
\operatorname{dist}
\left(
I_R,\sigma(K_R^{\rm phys})\setminus I_R
\right)
\ge\Delta_0-2\delta>0.
$$

For localization, use an Agmon weight $e^{ar}$, with $a$ smaller than the value allowed by the gap. The weighted identity yields

$$
\int e^{2ar}
\left(
|\nabla\eta_R|^2+|\eta_R|^2
\right)d\mu_R
\le C.
$$

Thus the norm does not spread over the increasing volume.

The script `scripts/verify_localization_gap_toy.py` illustrates the distinction between the physical gap and the artificial compactification gap. In the reduced model, increasing the domain from $L=4$ to $L=18$, the bound eigenvalue remains $-6.6361862202$ and the gap stabilizes at $3.7425977750$, while the mass outside $|x|>2$ remains on the order of $10^{-3}$.

## Lemma 5 — Resolvents and Riesz projectors

**Statement.** With Mosco convergence and a uniform gap, the resolvents converge outside the spectrum and the Riesz projectors of the isolated clusters converge.

**Proof.** By the theory of closed forms, Mosco convergence implies strong convergence of the resolvents:

$$
(K_R^{\rm phys}+1)^{-1}\to(K_0^{\rm phys}+1)^{-1;.
$$

If $\Gamma$ is a closed curve in the complex plane enclosing only the isolated cluster, the spectral projector is

$$
P_{R,I}
=\frac{1}{2\pi i}\int_\Gamma
(z-K_R^{\rm phys})^{-1}\,dz.
$$

The uniform gap prevents the spectrum from crossing $\Gamma$. Therefore, the projectors converge. In finite localized clusters, the convergence is strong and preserves multiplicity.

The script `scripts/verify_riesz_resolvent_toy.py` verifies the finite form of this argument: when $\varepsilon$ drops from $0.2$ to $0.01$, the projector error drops from $6.722577\times10^{-2}$ to $3.278796\times10^{-3}$.

## Lemma 6 — Separation between topological inheritance and continuous normalization

**Statement.** The bridge transports localized sectors, multiplicities, topological classes, and isolated spectral clusters. It does not automatically determine continuous normalizations, metrological constants, or apparatus responses.

**Proof.** Lemmas 1--5 control local limits, quadratic forms, and spectral subspaces. These objects are stable under pointed convergence and gap. However, a continuous normalization depends on global flux integrals, boundary impedances, and source couplings, for example

$$
Z^{-1}\sim\int |\xi|^2\,d\mu,
\qquad
\mathsf R=K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

These expressions can change if the canal is massless, if there is leakage to the bulk, if the physical boundary changes, or if the apparatus changes the DtN. Therefore, the bridge does not authorize deducing $\alpha$, $G$, masses, moments, or detector responses solely by topological transport. Each normalization requires its own calculation.

## Causal clock and Madelung reduction

The flux parameter $\tau$ is not the physical time $t$. The compatibility between the logarithmic form of the flux and the macroscopic clock is expressed by

$$
\gamma^*\left(\frac{d\tau}{\tau}\right)=\kappa\,dt.
$$

This is equivalent to requiring that the relative dilation

$$
F(t)=\frac{\tau_\gamma(t)}{\tau_0}
$$

be a homomorphism between time translations and positive dilations:

$$
F(t_1+t_2)=F(t_1)F(t_2).
$$

Under physical continuity or monotonicity, Cauchy's functional equation yields

$$
F(t)=e^{\kappa t},
\qquad
\tau_\gamma(t)=\tau_0e^{\kappa t}.
$$

The script `scripts/verify_clock_homomorphism.py` verifies this identity for $\tau_0=2.0$ and $\kappa=0.37$, with numerical defects on the order of $10^{-16}$.

The canonical Madelung identity

$$
\Pi_{S_R}=\rho
$$

is not a universal off-shell identity of the official action. It is the hydrodynamic response in the reduced sector in which:

1. the causal clock fixes constant $\kappa$ in the laboratory;
2. the probabilistic normalization selects $N_\rho=1$;
3. the phase charge selects $Q_S=1$;
4. fast modes of amplitude and shift have been damped by the apparatus;
5. the system has relaxed to the Routh minimum;
6. the Cauchy--Schwarz inequality is saturated.

At least,

$$
\left(
\int_\Sigma\frac{\Pi_{S_R}^2}{\rho}\,d\Sigma
\right)
\left(
\int_\Sigma\rho\,d\Sigma
\right)
\ge
\left(
\int_\Sigma\Pi_{S_R}\,d\Sigma
\right)^2.
$$

With $Q_S=N_\rho=1$, equality requires $\Pi_{S_R}=\rho$. Physically, this means that projective quantum mechanics appears as the observable hydrodynamics of the thermalized and measured sector of GDQ, not as a replacement for the fundamental action.

## Applied $C_3$ sector

In the reduced stationary background with three centers, local torsion equilibrium, and cyclic symmetry $C_3$, the common mode is removed by Noether and the two relative modes remain in the physical sector. The lowest physical eigenvalue has the form

$$
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}.
$$

In the primitive normalization of the sector,

$$
\Delta_0=\frac12.
$$

This result closes the bridge as an applied theorem for this background: the trimodal cluster is localized, has a gap, and has a projector transportable by the pointed limit. It does not prove that all GDQ backgrounds have three centers, nor does it calculate masses or continuous normalizations by itself.

## Routes excluded from the positive manuscript

The following routes were useful historically, but do not enter as a foundation of the manuscript:

- artificial collars adjusted to produce a saddle;
- antipodal shooting without a complete variational chain;
- cancellation by scalar noise without a source derived from the action;
- homogeneous Beltrami mode when the interface coupling becomes null;
- solver without an admissible saddle background;
- normalization of constants by experimental target;
- direct identification between $T^5\times S^3$ and $\mathbb R^4\times T^4$ without pointed limit, measure transport, and projectors.

These items may remain in audit records, but must not be used as proofs in the main text.

## Summary of status

| Item | Status | Observation |
|---|---|---|
| Pointed limit | Demonstrated | Local error $O(R^{-2})$. |
| Measure transport | Demonstrated under regularity/domination | Requires unitary Jacobian. |
| Physical Hessian | Conditional | Requires admissible background, constraints, and projector. |
| Mosco/resolvent/Riesz | Conditional | Requires gap and controlled domain. |
| $C_3$ sector | Closed as an applied theorem | Primitive gap $\Delta_0=1/2$. |
| Continuous normalizations | Separated | Must be calculated in each physical sector. |
