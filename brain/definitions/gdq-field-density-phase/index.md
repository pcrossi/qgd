---
title: GDQ field, density, and phase
status: defined
concepts:
  - f field
  - density
  - phase
  - Madelung
---

# GDQ field, density, and phase

## Definition

The complex field `f` is parametrized by:

$$
f=-\frac{S_I}{\hbar}+i\frac{S_R}{\hbar},
\qquad
\bar f=-\frac{S_I}{\hbar}-i\frac{S_R}{\hbar}.
$$

Therefore:

$$
S_I=-\frac{\hbar}{2}(f+\bar f),
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

The density is:

$$
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar}.
$$

The Madelung reconstruction is:

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

Equivalently:

$$
f=-\ln\rho+i\frac{S_R}{\hbar}.
$$

## Status

Exact identity from definitions. The physical interpretation of `S_R` as
circulation requires topological conditions on the domain and is not automatic
for every complex field.

## Source

`manuscrito/02_geometrization/02.4 - Campo complexo, densidade e fase.md`

