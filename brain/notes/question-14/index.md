---
title: Question 14 - Perelman-Madelung map
status: conditionally_closed
source: questão_14.md
updated: 2026-07-16
---

# Question 14 - Perelman-Madelung map

Q14 asks for the map between the Perelman formulation of GDQ and the Madelung
formulation.

The map is local, regular and sectorial:

$$
f
=
-\ln\rho+i\frac{S_R}{\hbar},
\qquad
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

The effective wavefunction is

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

## Domain

The regular domain is

$$
\rho>0,
\qquad
S_R\text{ locally single-valued},
\qquad
f,g\in C^2.
$$

In this domain, the map preserves the Madelung equations:

$$
\delta_{S_R}I=0
\Longleftrightarrow
\text{continuity},
$$

and

$$
\delta_\rho I=0
\Longleftrightarrow
\text{Hamilton--Jacobi--Bohm}.
$$

## Limits of the map

The map is not a global bijection. Nodes $\rho=0$, multivalued phases,
superpositions, spinorial sectors, gauge sectors and topological sectors
require charts, branches, bundles or additional data.

## Status

Q14 is conditionally closed as a local correspondence theorem in the regular
Madelung sector.

