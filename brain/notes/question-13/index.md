---
title: Question 13 - Relation between U and rho
status: closed
source: questoes/q13/questao_13.md
updated: 2026-07-16
---

# Question 13 - Relation between U and rho

Q13 asks why the measure $\mathcal U$ is equal to the density $\rho$.

The corrected answer is that the literal equality $\mathcal U=\rho$ is not the
official form. The official relation is

$$
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=
\frac{\rho}{(4\pi z_\tau)^n}.
$$

Thus

$$
(4\pi z_\tau)^n\mathcal U=\rho.
$$

If the kernel-free measure is defined as

$$
\widetilde{\mathcal U}
:=
(4\pi z_\tau)^n\mathcal U,
$$

then

$$
\widetilde{\mathcal U}=\rho.
$$

## Reason

$\mathcal U$ and $\rho$ are not independent solutions of the same transport
equation. They are both defined from the same fundamental field:

$$
\rho=e^{-(f+\bar f)/2}.
$$

The heat-kernel factor belongs to the geometric/diffusive causal measure.

## Born reading

In the effective Madelung layer,

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar},
\qquad
|\Psi|^2=\rho.
$$

The local probability density is $\rho$; the full action measure is
$\rho(4\pi z_\tau)^{-n}$.

## Status

Q13 is closed as a definitional clarification. Any text saying
$\mathcal U=\rho$ must specify whether the heat-kernel factor has been
removed.

