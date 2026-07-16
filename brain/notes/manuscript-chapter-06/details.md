---
title: Chapter 06 detailed map
status: active
source: manuscrito/06_global_local_bridge/
---

# Chapter 06 detailed map

## 06.1 — The problem

The local official bulk is

$$
M_0=\mathbb R^4\times T^4.
$$

The Einstein cosmological space is

$$
M_E=T^5\times S^3.
$$

They are not globally identical. The bridge must compare fields, measures,
Hessians, domains and spectral sectors, not just declare that a large compact
space is approximately flat.

There is no physical collar between $M_E$ and $M_0$. DtN operators belong to
the material stoma boundary $Y_{\rm st}$, not to a fictitious cosmology--lab
wall.

## 06.2 — Pointed family

The family is

$$
M_\varepsilon
=T^4\times S^1_{\varepsilon^{-1}}\times S^3_{\varepsilon^{-1}}.
$$

On fixed compact charts around a basepoint, $S^1_R$ becomes $\mathbb R$ and
$S^3_R$ becomes $\mathbb R^3$, with metric error $O(\varepsilon^2)$ on fixed
compact sets. This gives pointed Cheeger--Gromov convergence to
$T^4\times\mathbb R^4$.

The defect is kept visible by choosing growing windows
$L_\varepsilon\to\infty$ with $\varepsilon L_\varepsilon\to0$.

## 06.3 — Fields and measure

The local background is

$$
X_0=(g_0,J_0,f_0).
$$

The torsion is not transported as an independent field. It is reconstructed by

$$
H=d_J^c\omega_g.
$$

The measure is transported using

$$
\mathcal U
=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^4}.
$$

The correct identification of Hilbert spaces includes the square-root
Jacobian of the weighted measure, not only pullback of functions.

The cutoff error can be corrected by the implicit-function argument only after
physical invertibility/gap is available.

## 06.4 — Physical Hessian

The raw Hessian contains diffeomorphism, gauge, normalization and charge
directions. The physical tangent space is obtained from constraints and
redundancies. With $A_*=(C_*,R_*^\dagger\mathbb G_*)$, the joint projector is

$$
P^{\rm phys}
=I-
\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+
A_*.
$$

That is, the whole correction term

$$
\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+
A_*
$$

is subtracted from the identity. This is the joint projection away from
constraints and redundancies. Products
of separate projectors can fail when the projectors do not commute.

The Hessian to compare is the Hessian of the augmented functional:

$$
\mathbb H_*
=D_X^2S_{\rm phys}(X_*)
-\sum_a\lambda_*^aD^2\mathcal C_a(X_*).
$$

The physical operator is

$$
K_*^{\rm phys}
=P^{{\rm phys}\dagger}\mathbb H_*P^{\rm phys}.
$$

The boundary response of the same stoma can be encoded by DtN and Schur
complements after zero modes are removed and a gap is proved.

## 06.5 — Localization and gap

Descompactification destroys the naive compact spectral gap. The relevant gap
is local and physical:

$$
\Delta_0
=\operatorname{dist}
\left(
I,\sigma(K_0^{\rm phys})\setminus I
\right)>0.
$$

IMS localization separates the stoma region from the exterior. If the exterior
threshold is above the cluster and the local coefficients converge, the gap
persists uniformly for small $\varepsilon$. Agmon estimates prevent norm
escape.

## 06.6 — Resolvents and projectors

The stable object is not an arbitrarily chosen eigenvector, but the spectral
projector. Mosco convergence plus uniform gap gives resolvent convergence and
then convergence of Riesz projectors:

$$
P_{\varepsilon,I}
=\frac{1}{2\pi i}
\oint_\Gamma
(K_\varepsilon^{\rm phys}-z)^{-1}\,dz.
$$

Rank, multiplicity and spectral class are inherited.

## 06.7 — What is and is not transported

Transported under the hypotheses:

- topological invariants;
- relative classes;
- linked spectral clusters;
- multiplicities;
- internal dimensionless spectral ratios.

Not transported automatically:

- absolute energy units;
- continuous coupling normalizations;
- detector responses;
- full nonlocalized spectrum.

This distinction prevents using topology as a substitute for physical
normalization.

## 06.8 — Clock and laboratory continuity

The transported clock form is obtained from the cosmological cycle:

$$
\omega_E=R_Ed\Theta_E,
\qquad
x^0=R_E\Theta_E.
$$

The pullback to the reconstructed physical slice gives the local clock form
$u=X^*dx^0$. This fixes direction and orientation but does not by itself prove
the canonical Madelung momentum.

The phase current derived in Chapter 5 decomposes after reconstruction into a
standard continuity equation in an approximately inertial lab. The identity
$\varrho=\rho$ and $\Pi_{S_R}=\rho$ remains conditional.

## 06.9 — Bound modes and massless channels

Bound $L^2$ modes use Agmon localization and Riesz projectors. Massless
extended channels, such as the photon, require flux normalization, DtN or
scattering convergence. For continuous couplings the relevant object is a
symplectic current coefficient such as $Z_Q$, not an integer topological
class.

## 06.10 — Applied $C_3$ sector

In the stationary three-center Gaussian background with local torsion balance,
Noether closure and cyclic $C_3$ symmetry, the physical gap is

$$
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}.
$$

In primitive normalization,

$$
\Delta_0=\frac12.
$$

Thus the bridge is applied to the trimodal sector. This does not compute all
continuous normalizations or prove all possible backgrounds.
