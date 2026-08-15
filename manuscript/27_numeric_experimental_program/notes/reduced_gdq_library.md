---
title: "Note — Reduced GDQ library"
---

# Note — Reduced GDQ library

This note documents the reusable reduced blocks used in the numerical program scripts. They are tools for verification and prototyping. They are not a new physical action and do not replace the full GDQ Hessian.

## 1. DtN in a massive interval

Consider the reduced operator:

$$
K_{\rm red}
=
-\frac{d^2}{ds^2}
+\lambda_{\rm eff}^2
$$

on $s\in[0,L]$, with:

$$
\varphi(0)=\varphi_0,
\qquad
\varphi(L)=0.
$$

The stationary solution is:

$$
\varphi(s)
=
\varphi_0
\frac{\sinh(\lambda_{\rm eff}(L-s))}
{\sinh(\lambda_{\rm eff}L)}.
$$

The normal momentum at the boundary $s=0$ is:

$$
-\varphi'(0)
=
\lambda_{\rm eff}\coth(\lambda_{\rm eff}L)\,\varphi_0.
$$

Therefore, the reduced DtN operator is:

$$
\mathsf R_{\rm DtN}
=
\lambda_{\rm eff}\coth(\lambda_{\rm eff}L).
$$

This block appears when a detector, wall, or material channel is approximated by a linear mode with effective length $L$ and stiffness $\lambda_{\rm eff}$.

## 2. Schur complement

For a finite Hessian partitioned into boundary $\partial$ and interior $I$:

$$
K
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix},
$$

the variational elimination of the interior yields:

$$
K_{\rm eff}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

This formula is the discrete version of the DtN calculation above. The negative sign is important: relaxable internal degrees of freedom reduce the apparent stiffness of the boundary.

## 3. Quadratic response

If a classical source imposes a boundary difference $\Delta_\partial$ and the effective impedance is $\mathsf R$, the quadratic cost is:

$$
E_{\rm resp}
=
\frac{1}{2}
\langle \Delta_\partial,\mathsf R\Delta_\partial\rangle.
$$

In detector problems, this cost defines the decoherence loss exponent:

$$
\Gamma_{\rm det}
=
\frac{1}{2}
\langle \Delta_\partial,\mathsf R_{\rm det}\Delta_\partial\rangle.
$$

Then the reduced interference becomes:

$$
V_{\rm out}
=
V_{\rm in}e^{-\Gamma_{\rm det}}.
$$

## 4. Two-alternative density

For two reduced intensities $I_1$ and $I_2$, relative phase $\varphi$, and damping $\Gamma$, the observed density is:

$$
\rho
=
I_1+I_2
+2e^{-\Gamma}\sqrt{I_1I_2}\cos\varphi.
$$

This block does not postulate collapse. It represents the effective response of the detector after eliminating its internal degrees of freedom.

## 5. Correct usage

These blocks can be used when:

- the background has already been fixed or reduced;
- the classical source of the apparatus has been declared;
- the full Hessian has been approximated by a controlled linear channel;
- the comparison is classified as structural, phenomenological, or metrological, as the case may be.

They must not be used to declare a blind prediction if $\lambda_{\rm eff}$, $L$, or the source were chosen after looking at the target.
