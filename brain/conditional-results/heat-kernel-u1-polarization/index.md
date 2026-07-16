---
title: Heat-kernel U(1) polarization
status: active
concepts:
  - heat kernel
  - U(1)
  - Landau pole
  - Ward
---

# Heat-kernel U(1) polarization

## Statement

In the declared heat-kernel comparison sector, the U(1) polarization preserves
Ward, satisfies `Pi_tau(0)=0`, saturates in the ultraviolet and has no Landau
pole if an explicit spectral inequality holds.

## Formula

For the effective comparison operator:

$$
\Pi_\tau(q^2)
=\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\left[
E_1(\tau m^2)
-E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)
\right].
$$

Then

$$
\Pi_\tau(0)=0,
$$

and

$$
\Pi_\tau(\infty)
=\frac{\alpha_0}{3\pi}E_1(\tau m^2).
$$

No pole occurs in

$$
\alpha_{\rm eff}(q^2)
=\frac{\alpha_0}{1-\Pi_\tau(q^2)}
$$

if

$$
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
$$

## Status

This is a conditional sector result. It is not a proof of full
non-perturbative finiteness of GDQ and does not make renormalization
fundamental.

## Sources

- `manuscrito/04_action_consistency/04.7 - O que significa consistência em loops.md`
- `manuscrito/notes/action/Polarização heat-kernel e ausência do polo de Landau.md`
