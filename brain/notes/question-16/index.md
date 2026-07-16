---
title: Question 16 - Diffusion coefficient
status: closed
source: questão_16.md
updated: 2026-07-16
---

# Question 16 - Diffusion coefficient

Q16 asks whether GDQ uses $\nu=\hbar/(2m)$ or a universal $\nu_0$.

The answer separates two layers:

$$
\nu_0=\frac{\hbar}{2m_0}
$$

is the universal vacuum/bulk diffusion scale, while the effective diffusion
seen by an excitation of inertial mass $m$ is

$$
\nu_{\rm eff}
=
\nu_0\Omega^{-1}
=
\frac{\hbar}{2m},
\qquad
\Omega=\frac{m}{m_0}.
$$

$\Omega$ is operationally defined in the stochastic sector and must be derived
geometrically from the soliton in each physical species.

For variable $\Omega(x,t)$, the Itô Fokker--Planck equation is

$$
\partial_t\rho
=
-\nabla_i(b^i\rho)
+\nu_0\Delta_h(\Omega^{-1}\rho).
$$

Equivalently, the osmotic velocity is

$$
u^i
=
\nu
\left(
\nabla^i\ln\rho-\nabla^i\ln\Omega
\right).
$$

The older formula without the $\nabla\Omega$ term is valid only when
$\Omega$ is constant.

## Status

Q16 is closed in the stochastic/Madelung reduction. The derivation of
$\Omega$ from each soliton remains a later spectral/solitonic task.

