---
title: "GDQ construction of measurement"
---

# GDQ construction of measurement

## 1. Statement

A measurement is not a manual introduction of a quantum operator. It is an interface problem between a GDQ object and a classical apparatus.

The chain is:

$$
J_{\rm app}^{\rm classico}
\to
\Phi_\ast
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\text{R}_{\rm app}
\to
\text{effective projectors}
\to
\text{record}.
$$

## 2. Apparatus source or boundary

The apparatus provides classical data:

$$
J_{\rm app},
\qquad
C_{\rm app},
\qquad
\partial M_{\rm app}.
$$

These data select a physical domain. They do not alter the official action.

The background with the apparatus satisfies:

$$
\left.
\frac{\delta}
{\delta\Phi}
\left(
\mathcal S_{\rm GDQ}
+
\mathcal S_{\rm app}
\right)
\right|_{\Phi_\ast}
=
0.
$$

Here $\mathcal S_{\rm app}$ represents the boundary/source imposition of the experiment, not a new fundamental term.

## 3. Hessian and interface response

On the background $\Phi_\ast$:

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi}
\right|_{\Phi_\ast}
P_{\rm phys}.
$$

Separating boundary and interior:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}.
$$

The effective response of the apparatus is:

$$
\Omega = \text{R}_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## 4. Projectors and probabilities

The apparatus defines exclusive macroscopic alternatives. In the reconstructed physical Hilbert space, these alternatives are represented by projectors:

$$
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I.
$$

The operational rule is:

$$
\mu(P_i)=\operatorname{Tr}(\varrho P_i).
$$

For a pure state:

$$
\mu(P_i)=|\langle i|\psi\rangle|^2.
$$

## 5. Individual outcome

Structural GDQ provides probabilities, channels, and response. A unique individual outcome requires a real dynamical basin of the combined object--apparatus--environment system. This point is conditional, not omitted.
