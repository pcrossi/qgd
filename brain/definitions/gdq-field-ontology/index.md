---
title: GDQ field ontology
status: closed
source: questão_5.md
updated: 2026-07-16
---

# GDQ field ontology

The official GDQ ontology separates fundamental fields, defining structures,
derived hydrodynamic variables, effective physical fields and optional audit
fields.

## Fundamental fields

$$
\mathcal F_{\rm fund}
=
\{g_{\mu\bar\nu}, f, \bar f\}.
$$

These are the fields varied directly in the official action.

## Defining structures

$$
\mathcal B
=
\{M,J,\gamma,\tau,t,z_\tau,\Lambda_C,\nu_0\}.
$$

They define the theory and contour prescription but are not fields varied in
the official action. In the current dimensional convention, $\Lambda_C$ is a
dimensionless cutoff number in Cartan-normalized coordinates.

## Derived hydrodynamic variables

$$
\mathcal D
=
\{S_I,S_R,\rho,R,\Psi\}.
$$

They are obtained from $f$ and $\bar f$ by the map

$$
f
=
-\frac{S_I-iS_R}{\hbar},
\qquad
\rho=e^{-(f+\bar f)/2},
\qquad
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

## Effective physical fields

$$
\mathcal E
=
\{X,h,B,A^a,\psi\}.
$$

They belong to the reduced physical layer in $N^4$ and must be compatible with
the official action, but they do not replace $g,f,\bar f$.

## Optional audit fields

$$
\mathcal A_{\rm aux}
=
\{c^a,\bar c^a,b^a\}.
$$

BRST/Faddeev--Popov variables are optional audit/comparison devices, not
fundamental GDQ ontology.

