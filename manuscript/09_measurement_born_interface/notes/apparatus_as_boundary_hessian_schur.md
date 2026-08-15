---
title: "Apparatus as boundary and Schur complement"
---

# Apparatus as boundary and Schur complement

## Statement

A classical apparatus enters GDQ as a source, constraint, or boundary. In the linear reduction around an admissible background, its internal degrees of freedom generate an effective boundary impedance:

$$
\Omega = \text{R}_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## Status

Effective variational reduction. Does not alter the official action.

## Construction

Consider physical fluctuations split into:

$$
\delta\Phi
=
(\delta\Phi_\partial,\delta\Phi_I).
$$

The projected second variation of the official action in the apparatus sector has the form:

$$
\delta^2\mathcal S_{\rm eff}
=
\frac12
\begin{pmatrix}
\delta\Phi_\partial \\
\delta\Phi_I
\end{pmatrix}^{\!*}
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}
\begin{pmatrix}
\delta\Phi_\partial \\
\delta\Phi_I
\end{pmatrix}.
$$

The unobserved internal degrees of freedom satisfy the stationary equation:

$$
K_{I\partial}\delta\Phi_\partial
+
K_{II}\delta\Phi_I
=0.
$$

If $K_{II}$ is invertible in the physical sector:

$$
\delta\Phi_I
=
-K_{II}^{-1}K_{I\partial}\delta\Phi_\partial.
$$

Substituting back:

$$
\delta^2\mathcal S_{\rm eff}
=
\frac12
\delta\Phi_\partial^{*}
\left(
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial
\right)
\delta\Phi_\partial.
$$

Wait, let me fix the parentheses in the display equation above, lines 78-79:
`K_{\partial I}K_{II}^{-1}K_{I\partial}`
Wait, the target has `K_{I\partial}` and then a closing parenthesis. In the view_file:
```latex
77: \left(
78: K_{\partial\partial}
79: -
80: K_{\partial I}K_{II}^{-1}K_{I\partial}
81: \right)
```
Yes, it is `\left( K_{\partial\partial} - K_{\partial I} K_{II}^{-1} K_{I\partial} \right)`. Let's write it cleanly.

Therefore:

$$
\text{R}_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## Physical interpretation

$\text{R}_{\rm app}$ is the effective response that the measured system feels at the boundary. It contains rigidity, losses, apparatus geometry, and interface coupling. In real apparatuses, its values depend on material and fabrication.

This is not an adjustment of the official action. It is the choice of the physical boundary value problem.
