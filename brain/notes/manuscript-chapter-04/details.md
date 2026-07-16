---
title: Manuscript chapter 04 details
status: active
---

# Manuscript chapter 04 details

## 1. Role of the chapter

Chapter 4 is the point where GDQ stops being a list of compatible ideas and
becomes a variational theory. Its role is not to derive every equation yet,
but to specify the functional, the fields, the measure, the domains, the
boundary terms, the symmetries and the Hessian that later chapters must use.

The chapter’s central rule is:

$$
\text{official action}
\to
\text{first variation}
\to
\text{bulk equations plus boundary momenta}
\to
\text{second variation/Hessian}
\to
\text{physical operator and loops}.
$$

Any claimed reduction must be traceable back to this chain.

## 2. Official action and what is axiomatic

The action is adopted as fundamental:

$$
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(
\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
$$

Status: axiom/dynamic definition of the theory.

Consequences:

- the action is not replaced by Einstein-Hilbert;
- Perelman functionals remain auxiliary or historical context unless derived
  as reductions;
- Yang-Mills, Dirac, Pauli, BRST and ghost fields can appear as comparison
  languages or effective sectors, not as new ontology;
- sources and apparatuses are allowed only as declared source, boundary,
  interface or constraint data.

## 3. Dimensional convention for `Lambda_C`

The chapter resolves the previous dimensional ambiguity:

$$
z^a=\ell_C\widehat z^a,
\qquad
\tau=\ell_C^2\widehat\tau,
\qquad
z_\tau=\ell_C^2\widehat z_\tau.
$$

Then

$$
\mathcal R=\ell_C^{-2}\widehat{\mathcal R},
\qquad
\mathcal U=\ell_C^{-2n}\widehat{\mathcal U},
\qquad
dV_g=\ell_C^{2n}dV_{\widehat g},
$$

so the integrated functional is dimensionless.

Therefore the symbol in the official action is

$$
\Lambda_C=\ell_C k_C=1
$$

in normalized coordinates, and

$$
\left[\frac{\hbar}{\Lambda_C^2}\right]=[\hbar].
$$

Status: convention/conditional resolution of dimensional consistency. It
preserves the official action and forbids reusing `Lambda_C` as a dimensional
length, momentum or energy. Physical scales must be denoted separately:
`ell_C`, `k_C`, `E_C`.

## 4. Fields and measure

The central fields are

$$
\Phi=(g,f,\bar f).
$$

They can be rewritten as density and phase:

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
$$

with

$$
f=-\ln\rho+\frac{i}{\hbar}S_R.
$$

The measure is constitutive:

$$
\mathcal U[f,\bar f,z_\tau]
=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=\frac{\rho}{(4\pi z_\tau)^n}.
$$

It is not an independent field and not a free multiplier.

For fixed `z_tau`:

$$
\frac{\delta\mathcal U}{\mathcal U}
=-\frac12(\delta f+\delta\bar f)
=\frac{\delta\rho}{\rho}.
$$

Thus:

- phase variations do not change `U`;
- density variations do change `U`;
- omitting this variation changes the Euler-Lagrange equations.

## 5. Normalization constraint

The section measure satisfies

$$
\int_M\mathcal U\,dV_g=1.
$$

The constrained action is

$$
\mathcal S_{\rm restrita}
=\mathcal S_{\rm GDQ}
-\int_\gamma
C\lambda(\tau)
\left[
\int_M\mathcal U\,dV_g-1
\right]
\frac{d\tau}{\tau}.
$$

`lambda(tau)` is not a new interaction. It selects the normalized-measure
subspace and contributes to both density and metric equations.

## 6. Variation structure

Writing

$$
C=\frac{\hbar}{\Lambda_C^2},
\qquad
\mathcal L_0
=\tau\left(
\mathcal R
+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}-n,
$$

the product rule is

$$
\delta S
=\operatorname{Re}
\int_\gamma\int_M C
\left[
\mathcal U\,\delta\mathcal L_0
+\mathcal L_0\,\delta\mathcal U
+\mathcal U\mathcal L_0
\frac{\delta dV_g}{dV_g}
\right]
dV_g\frac{d\tau}{\tau}.
$$

The metric variation of weighted curvature produces the characteristic GDQ
terms

$$
g_{AB}\Delta_g\mathcal U-\nabla_A\nabla_B\mathcal U,
$$

in addition to Ricci and volume terms. Therefore the bulk equation is
metric-dilatonic and weighted. An Einstein-like equation can only be a
reduction, not the fundamental equation.

After integration by parts:

$$
\delta S_{\rm restrita}
=\int_\gamma\int_M
\left[
\mathcal E_g^{AB}\delta g_{AB}
+\mathcal E_f\delta f
+\mathcal E_{\bar f}\delta\bar f
\right]
+\int_\gamma\int_{\partial M}\Theta.
$$

The bulk terms give equations; `Theta` gives boundary/interface momenta.

## 7. Symmetries and boundaries

Global phase symmetry:

$$
f\mapsto f+i\alpha,
\qquad
\bar f\mapsto\bar f-i\alpha
$$

leaves `U`, `L_0` and the action invariant. In phase variables:

$$
S_R\mapsto S_R+\hbar\alpha.
$$

This yields the phase Noether current on shell. It does not by itself create a
local gauge connection; local gauge structure must be derived or declared as
an effective reduction.

Boundary logic:

- spatial boundary: stomata, excisions, horizons, apparatuses, non-compact
  falloff;
- causal boundary: endpoints, branches and residues of `gamma`;
- local conservation does not imply global charge conservation unless lateral
  flux is absent or included;
- a Dirichlet-to-Neumann map represents a solved internal domain and cannot be
  fitted after the fact as a spectrum-fixing parameter.

The curvature term needs its own GDQ-compatible boundary completion if metric
Dirichlet data are used. Standard Gibbons-Hawking-York is not automatically
imported because the action is weighted by `U` and is not Einstein-Hilbert.

## 8. Hessian and loop meaning

For an admissible background

$$
\Phi_*=(g_*,f_*,\bar f_*),
$$

the second variation defines

$$
\mathbb H_*
=\operatorname{Hess}\operatorname{Re}\mathcal S_{\rm GDQ}\big|_{\Phi_*}.
$$

The physical operator is not the raw Hessian. It is

$$
\mathbb H_*^{\rm phys}
=P_{\rm phys}\mathbb H_*P_{\rm phys},
$$

on the domain satisfying regularity, constraints, quotient conditions and
boundary/interface conditions.

The fundamental one-loop object is

$$
\Gamma_{\rm GDQ}^{(1)}
=\frac12\operatorname{Tr}_{\rm phys}
\ln\operatorname{Hess}\mathcal S_{\rm GDQ}.
$$

This replaces imported propagators as the primary GDQ perturbative object.

## 9. Heat kernel and damping

If the physical elliptic second-order operator is `L^(2)`, the Hessian scale
and heat semigroup are separated:

$$
\mathcal O_{\rm Hess}^{(2)}=\tau L^{(2)},
\qquad
e^{-\tau L^{(2)}}.
$$

In the flat limit:

$$
e^{-\tau L^{(2)}}\to e^{-\tau(p_E^2+V_{\rm eff})}.
$$

This gives Gaussian ultraviolet damping, not a fourth-order damping. The
chapter explicitly rejects using `exp[-(tau L)^2]` because it would produce
`exp[-tau^2 p^4]` and correspond to a different operator.

The result is conditional: it proves ultraviolet improvement in the declared
quadratic sector, not all-orders finiteness of the full theory.

## 10. Ghosts, Ward and Slavnov-Taylor

The intrinsic physical space is

$$
\mathcal V_{\rm phys}
=\ker C\cap\mathcal D_{\rm bordo}/\operatorname{Im}R.
$$

A gauge section introduces a Faddeev-Popov determinant as a Jacobian:

$$
\Delta_{\rm FP}[A]
=\det\left(\frac{\delta F[A^g]}{\delta g}\right)_{g=1}.
$$

Grassmann ghosts can represent this determinant, but they are not GDQ matter.

If the reduced operator satisfies spectral covariance,

$$
L_{A^g}=g^{-1}L_Ag,
$$

then trace cyclicity gives Ward identities. In the abelian sector:

$$
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
$$

The non-abelian analogue is the geometric Slavnov-Taylor identity for the
quotient/effective functional.

## 11. U(1) polarization and Landau pole status

The chapter separates:

1. the GDQ loop of the phase of `f` on a toroidal cycle, derived from the
   official Hessian;
2. the external U(1) heat-kernel translation used only to discuss the Landau
   pole in familiar language.

In the comparison sector:

$$
\Pi_\tau(q^2)
=\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\left[
E_1(\tau m^2)
-E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)
\right].
$$

It satisfies:

$$
\Pi_\tau(0)=0,
\qquad
\Pi_\tau(\infty)=\frac{\alpha_0}{3\pi}E_1(\tau m^2).
$$

Thus no pole occurs in the comparison coupling if

$$
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
$$

Status: conditional sector result. It does not prove all-order or
non-perturbative finiteness of GDQ.

## 12. Current limitations

Chapter 4 does not prove:

- existence and stability of every material background;
- positivity of every physical Hessian;
- all-order damping of all vertices;
- absence of all measure anomalies;
- convergence of the perturbative series;
- non-perturbative finiteness;
- extension of the heat-kernel calculation to arbitrary singular backgrounds.

These remain sector-specific tasks.
