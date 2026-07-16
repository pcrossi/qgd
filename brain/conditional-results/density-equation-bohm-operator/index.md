---
title: Density equation and Bohm operator
status: active
concepts:
  - density
  - Bohm operator
  - Fisher energy
---

# Density equation and Bohm operator

## Statement

The GDQ density variation directly produces the differential operator

$$
\frac{\Delta_g\sqrt\rho}{\sqrt\rho}.
$$

The nonrelativistic Bohm potential coefficient appears only after the physical
kinetic normalization is fixed.

## Bulk equation

With `q=ln rho`:

$$
\tau\left[
\mathcal R
+\frac{1}{\hbar^2}|\nabla S_R|_g^2
-4\frac{\Delta_g\sqrt\rho}{\sqrt\rho}
\right]
-\ln\rho-n-1
=\lambda(\tau).
$$

Here `lambda(tau)` enforces measure normalization.

## Identity

$$
\frac{\Delta_g\sqrt\rho}{\sqrt\rho}
=\frac12\Delta_g\ln\rho
+\frac14|\nabla\ln\rho|_g^2.
$$

## Reduced Bohm potential

If the reduced amplitude energy is

$$
F[\rho]
=\frac{\hbar^2}{8m}
\int\frac{|\nabla\rho|^2}{\rho},
$$

then

$$
\frac{\delta F}{\delta\rho}
=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

## Sources

- `manuscrito/05_equations_conservation/05.4 - Variação da densidade e equilíbrio dinâmico.md`
- `manuscrito/notes/equations/Da energia de amplitude ao termo de Bohm.md`
