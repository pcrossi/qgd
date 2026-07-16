---
title: GDQ weighted measure
status: defined
concepts:
  - weighted measure
  - heat kernel
  - U
  - z_tau
---

# GDQ weighted measure

## Definition

The official weighted density is:

$$
\mathcal U[f,\bar f,z_\tau]
=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=\frac{\rho}{(4\pi z_\tau)^n}.
$$

For the local bulk, `n=4`, hence:

$$
\mathcal U=\frac{\rho}{(4\pi z_\tau)^4}.
$$

## Dimensional reason

The flat heat kernel in real dimension `d` has prefactor:

$$
(4\pi\tau)^{-d/2}.
$$

Since the bulk has real dimension `d=2n=8`, the power is `d/2=n=4`.

## Variation

For fixed `z_tau`:

$$
\delta\mathcal U
=-\frac12\mathcal U(\delta f+\delta\bar f).
$$

The volume variation is separate.

## Status

Definition plus dimensional verification. A future uniqueness theorem for the
measure would require additional hypotheses.

## Source

`manuscrito/02_geometrization/02.5 - Medida ponderada e kernel de calor.md`

