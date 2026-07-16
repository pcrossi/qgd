---
title: Universal diffusion and inertial response
status: conditionally_demonstrated
concepts:
  - Nelson
  - diffusion
  - inertia
  - osmotic velocity
  - Ito correction
  - geometric mass
---

# Universal diffusion and inertial response

## Statement

A universal reference diffusion `nu_0` can reproduce the Nelson coefficient
`hbar/(2m)` if local inertial response enters through a positive scale factor
`Omega=m/m_0`.

## Demonstrated part

With

$$
\nu_0=\frac{\hbar}{2m_0}
$$

and

$$
\Omega=\frac{m}{m_0},
$$

the effective coefficient

$$
\nu_{\rm eff}=\nu_0\Omega^{-1}
$$

gives

$$
\nu_{\rm eff}=\frac{\hbar}{2m}.
$$

For spatially varying `Omega`, the diffusion tensor is

$$
D^{ij}=\nu_0\Omega^{-1}h^{ij}
$$

and the Fokker-Planck equation includes the corresponding Ito terms. In the
isotropic case,

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\nu_0\Delta_h(\Omega^{-1}\rho).
$$

The compatible forward/backward construction gives

$$
u^i
=\nu_0\Omega^{-1}
\left(\nabla^i\ln\rho-\nabla^i\ln\Omega\right).
$$

## Open part

The GDQ still has to identify `Omega` with a specific functional of the
official background, boundary data, and solitonic topology. Until then, this
is a conditional bridge, not a derived mass theorem.

## Source

`manuscrito/01_initial_problem/01.8 - Difusão universal e inércia geométrica.md`

