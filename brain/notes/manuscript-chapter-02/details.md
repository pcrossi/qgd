---
title: Manuscript chapter 02 details
status: active
concepts:
  - geometrization of matter
  - official action
  - local bulk
  - Bismut torsion
  - material soliton
  - clock form
---

# Manuscript chapter 02 details

## 1. From rigid background to dynamic geometry

The chapter starts from the observation that a metric is already physical
before equations of motion are written. It defines:

$$
|\nabla S_R|_g^2=g^{ab}\partial_aS_R\partial_bS_R,
$$

the volume:

$$
dV_g=\sqrt{\det g}\,d^dx,
$$

and the Laplacian:

$$
\Delta_g\sqrt\rho.
$$

Therefore a fixed metric is a physical restriction. GDQ asks whether the pair

$$
(g,f)
$$

should be treated as one variational system.

The chapter defines a candidate material configuration as:

$$
\Phi_*=(g_*,f_*,\bar f_*),
$$

and requires stationarity, boundary conditions, finite action, conserved
class, Hessian stability, and observable response before calling it matter.

Status:

Constructive hypothesis and closure protocol, not proof of existence.

## 2. Local bulk and dimension

The local bulk is:

$$
M=\mathbb R^4\times T^4.
$$

Since:

$$
T^4=S^1_1\times S^1_2\times S^1_3\times S^1_4,
$$

one has:

$$
\dim_{\mathbb R}M=8.
$$

With an admitted complex structure:

$$
\dim_{\mathbb C}M=n=4.
$$

This makes the heat-kernel power four a consequence of the chosen bulk, not a
separate axiom.

Since `R^4` and `T^4` are parallelizable:

$$
TM\cong M\times\mathbb R^8,
\qquad
w_2(TM)=0.
$$

Spin structures exist. On the torus there are:

$$
H^1(T^4;\mathbb Z_2)\cong(\mathbb Z_2)^4
$$

and thus `16` spin choices. Physical selection is additional.

Status:

Bulk choice is structural. Dimension and spin existence are demonstrated
consequences.

## 3. Hermitian structure and Bismut connection

The geometry uses:

$$
J:TM\to TM,
\qquad
J^2=-I.
$$

Metric compatibility:

$$
g(JX,JY)=g(X,Y).
$$

Fundamental form:

$$
\omega_H(X,Y)=g(JX,Y).
$$

Kähler strict condition:

$$
d\omega_H=0.
$$

GDQ allows torsion:

$$
H=d_J^c\omega_H.
$$

Therefore:

$$
H\neq0
\Longrightarrow
\text{not Kähler strict}.
$$

Status:

Definition and geometric theorem of Bismut uniqueness under Hermitian
integrability. In the current official action, `H` is not independently
varied.

## 4. Complex field, density, and phase

The field is decomposed as:

$$
f=-\frac{S_I}{\hbar}+i\frac{S_R}{\hbar},
\qquad
\bar f=-\frac{S_I}{\hbar}-i\frac{S_R}{\hbar}.
$$

Thus:

$$
S_I=-\frac{\hbar}{2}(f+\bar f),
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

The density is:

$$
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar}.
$$

The reconstructed Madelung field is:

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

The inverse map is:

$$
f=-\ln\rho+i\frac{S_R}{\hbar}.
$$

Status:

Exact algebraic identity. The historical shorthand `f=-S/hbar` is rejected
because it mixes the logarithmic density part and phase.

## 5. Weighted measure and heat-kernel power

The measure is:

$$
\mathcal U[f,\bar f,z_\tau]
=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=\frac{\rho}{(4\pi z_\tau)^n}.
$$

For `n=4`:

$$
\mathcal U=\frac{\rho}{(4\pi z_\tau)^4}.
$$

The dimensional chain is:

$$
[\mathcal R]=L^{-2},
\qquad
[\tau]=L^2,
$$

so the action integrand is dimensionless. Also:

$$
[\mathcal U]=L^{-2n},
\qquad
[dV_g]=L^{2n},
$$

hence:

$$
[\mathcal U\,dV_g]=1.
$$

Variation with fixed `z_tau`:

$$
\delta\mathcal U
=-\frac12\mathcal U(\delta f+\delta\bar f).
$$

Status:

Definition plus dimensional identity. `U` is derived, not independently
varied.

## 6. Perelman as auxiliary geometric matrix

Perelman's functional contains the pattern:

$$
\text{curvature}
+
\text{gradient}
+
\text{weighted measure}
+
\text{flow parameter}.
$$

GDQ borrows this architecture but changes the problem:

- `f` is complex;
- the measure uses `f+bar f`;
- the domain is Hermitian and may have Bismut torsion;
- the external integration is over a causal contour `gamma`;
- the physical stationary quantity is the real part of the complex action.

The distinction is:

$$
\boxed{
\mathcal W
\text{ is auxiliary; }
\mathcal S_{\rm GDQ}
\text{ is fundamental.}
}
$$

Status:

Perelman is a reference grammar, not a replacement action.

## 7. Official action

The official action is:

$$
\mathcal{S}_{\text{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
$$

The scalar integrand is:

$$
\mathcal L_0
=\tau\left(
\mathcal R
+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}-n.
$$

Since `Lambda_C` is dimensionless in Cartan-normalized coordinates:

$$
\left[\frac{\hbar}{\Lambda_C^2}\right]=[\hbar].
$$

Physical stationarity uses:

$$
S_{\rm phys}=\operatorname{Re}\mathcal S_{\rm GDQ},
\qquad
\delta S_{\rm phys}=0.
$$

Status:

Dynamic axiom.

## 8. From geometry to material background

With fields:

$$
\Phi=(g,f,\bar f),
$$

a candidate is:

$$
\Phi_*=\Phi_\infty+\delta\Phi_*.
$$

The relative action is:

$$
S_{\rm rel}[\Phi_*]
=S_{\rm phys}[\Phi_*]-S_{\rm phys}[\Phi_\infty].
$$

With normalization and charge constraints:

$$
\widetilde S
=S_{\rm phys}
+\lambda_N\left(\int_M\mathcal U\,dV_g-1\right)
+\lambda_Q\left(Q[\Phi]-Q_0\right).
$$

Background equation:

$$
\delta\widetilde S[\Phi_*]=0.
$$

Hessian:

$$
\widetilde S[\Phi_*+\varepsilon\eta]
=\widetilde S[\Phi_*]
+\frac{\varepsilon^2}{2}
\langle\eta,\mathbb H_*\eta\rangle
+O(\varepsilon^3).
$$

Physical projection:

$$
\mathbb H_*^{\rm phys}
=P^{\rm phys}\mathbb H_*P^{\rm phys}.
$$

Strict stability asks:

$$
\langle\eta,
\mathbb H_*^{\rm phys}\eta\rangle
\ge\Delta_*\|\eta\|^2,
\qquad
\Delta_*>0.
$$

Status:

Criterion for materiality. Not a universal existence theorem.

## 9. Circulation, torsion, and defects

If `S_R` is globally smooth on a simply connected region:

$$
d(dS_R)=0,
\qquad
\oint_CdS_R=0
$$

for contractible cycles.

Nonzero circulation requires excision, local phases, or bundle holonomy. On
`M \ N`, `dS_R` may be closed but not exact:

$$
\Gamma_C=\oint_CdS_R.
$$

If

$$
e^{iS_R/\hbar}
$$

is globally single-valued, then:

$$
\Gamma_C=2\pi n\hbar=nh,
\qquad
n\in\mathbb Z.
$$

For spinorial holonomy `-1`:

$$
\Gamma_C=2\pi\hbar\left(n+\frac12\right).
$$

The stoma interface is:

$$
Y=\partial\mathcal N.
$$

For a local normal slice `C^2`, the link is `S^3`.

The correct chain is:

$$
\text{local phase}
\to
\text{holonomy or period}
\to
\text{interface datum}
\to
\text{torsional geometric response}.
$$

Status:

Topological conditional. Phase, torsion, and charge are linked but not
identical.

## 10. From Riemannian bulk to physical spacetime

For an immersion:

$$
X:N^4\to M^8,
$$

the pullback:

$$
q=X^*g
$$

is positive. It cannot by itself be Lorentzian.

Given a nonzero clock one-form `u`:

$$
s=q^{-1}(u,u)>0,
$$

define:

$$
h=q-2\frac{u\otimes u}{s}.
$$

In a `q`-orthonormal frame with `u=sqrt(s)e^0`, this gives:

$$
h=-(e^0)^2+(e^1)^2+(e^2)^2+(e^3)^2.
$$

Thus:

$$
\operatorname{sign}(h)=(-,+,+,+).
$$

In the adopted cosmological background:

$$
T^5\times S^3=T^4\times S_E^1\times S^3,
$$

the distinguished circle supplies:

$$
\omega_E=R_Ed\Theta_E.
$$

In the pointed local limit:

$$
\omega_0
=\lim_{R_E\to\infty}\Phi_{R_E}^*\omega_E
=dx^0.
$$

Then:

$$
u=X^*\omega_0.
$$

Synchronization at the common event:

$$
\iota^*\omega_E=u.
$$

The causal contour `gamma` selects orientation between `u` and `-u`.

Status:

Clock-form selection is closed within the adopted Einstein cosmological
background.

## 11. Final status of Chapter 2

Established:

- local bulk and dimension;
- Hermitian-Bismut structure;
- exact field-density-phase decomposition;
- weighted measure and its variation;
- Perelman as auxiliary matrix;
- official action as axiom;
- material soliton criterion;
- conditional circulation and defect interface;
- Lorentzian clock form selected by cosmological simultaneity.

Still axiomatic or input:

- official action;
- local geometric class;
- causal contour class;
- global and boundary sector data;
- cosmological Einstein background;
- physical scales not yet derived.

Still sector dependent:

- existence of each soliton;
- holonomy selection;
- physical Hessian stability;
- quantitative observables.

