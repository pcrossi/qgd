---
title: Question 05 - Fundamental fields of GDQ
status: closed
source: questoes/q05/questao_05.md
updated: 2026-07-16
---

# Question 05 - Fundamental fields of GDQ

## Enunciation

Q5 asks what the fundamental fields of GDQ are, and requires a stable
dictionary so that no symbol changes meaning between chapters without an
explicit map.

## Current answer

The minimal fundamental fields of the official action are

$$
\mathcal F_{\rm fund}
=
\{g_{\mu\bar\nu}, f, \bar f\}.
$$

The weighted measure is not an independent field:

$$
\mathcal U[f,\bar f,z_\tau]
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
$$

The defining structures are

$$
\mathcal B
=
\{M,J,\gamma,\tau,t,z_\tau,\Lambda_C,\nu_0\}.
$$

Here $\Lambda_C$ must be read with the later dimensional convention: it is the
dimensionless Cartan cutoff number in normalized coordinates. Dimensional
quantities are $\ell_C$, $k_C=\ell_C^{-1}$ and $E_C=\hbar c k_C$.

The hydrodynamic derived variables are

$$
\mathcal D
=
\{S_I,S_R,\rho,R,\Psi\}.
$$

The physical effective fields in the reduced spacetime $N^4$ are

$$
\mathcal E
=
\{X,h,B,A^a,\psi\}.
$$

Auxiliary perturbative audit variables are

$$
\mathcal A_{\rm aux}
=
\{c^a,\bar c^a,b^a\},
\qquad
\mathcal A_{\rm aux}\cap\mathcal F_{\rm fund}=\varnothing.
$$

## Mandatory maps

The official field $f$ decomposes as

$$
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar}.
$$

Thus

$$
S_I=-\hbar\,\operatorname{Re}f,
\qquad
S_R=\hbar\,\operatorname{Im}f,
$$

and

$$
\rho=e^{S_I/\hbar}=e^{-(f+\bar f)/2},
\qquad
R=\sqrt\rho,
\qquad
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

$\Psi$ is an effective Madelung/quantum representation, not a replacement for
$f$ in the official action.

## Clarifications

- $g$ is the bulk Hermitian/Riemannian metric.
- $h$ is the physical Lorentzian constitutive metric in $N^4$.
- $J$ is fixed structure in the current formulation, not a varied field.
- The general geometry is Hermitian with Bismut torsion; strict Kähler
  geometry is a special limit, local approximation or auxiliary gauge.
- $B$ is the effective physical torsional 3-form in $N^4$; $H$ may appear only
  as local synonym or external-literature notation.
- $A^a$ and $\psi$ belong to the effective physical layer, not to the minimal
  official ontology.
- Ghosts/BRST variables are optional audit language, not GDQ ontology.

## Status

Q5 is closed as the formal dictionary of GDQ fields. It does not close:

1. geometric beta-functions;
2. perturbative all-orders regularity;
3. explicit proof that the Sudarshan prescription projects all non-physical
   modes without ghost ontology;
4. effective couplings and observable constants from geometry.

