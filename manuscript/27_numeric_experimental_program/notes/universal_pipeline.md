---
title: "Note — Universal pipeline"
---

# Note — Universal pipeline

The standard form is:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*
\to
C_a[\Phi]=0
\to
P_{\rm phys}
\to
K_{\rm phys}
\to
J_{\rm app}
\to
\delta\Phi
\to
\mathsf R_{\rm app}
\to
\mathcal O_{\rm obs}.
$$

The critical point is that the Hessian must always be projected:

$$
K_{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

Without a projector, gauge modes and coordinate modes can be mistaken for physical instabilities.

## Minimal algebraic construction

If $K$ is the second variation of the official action on the background $\Phi_*$ and $D C$ is the matrix of linearized constraints, the allowed sector satisfies:

$$
D C\,\delta\Phi=0.
$$

With a positive quadratic metric $G$ on the space of fluctuations, the physical projector is:

$$
P_{\rm phys}
=
I
-
G^{-1}D C^\dagger
\left(D C\,G^{-1}D C^\dagger\right)^{-1}
D C.
$$

The compression:

$$
K_{\rm phys}
=
P_{\rm phys}^\dagger K P_{\rm phys}
$$

is the operator that must be diagonalized. When the observable lives only on the boundary or in the apparatus, the physical space is decomposed into an observed sector $\partial$ and an internal sector $I$:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}.
$$

Eliminating $I$:

$$
K_{\rm eff}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

This Schur complement is the abstract form of the DtN operator, the apparatus impedance, and the linear surface response. It is not a new term in the action; it is what the action already implies after imposing constraints and eliminating unobserved degrees of freedom.
