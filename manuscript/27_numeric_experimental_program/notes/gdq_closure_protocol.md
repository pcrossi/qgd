---
title: "Note — GDQ closure protocol"
---

# Note — GDQ closure protocol

This note establishes the minimal standard to transform a GDQ calculation into a preservable result in the manuscript. It does not replace the official action; it organizes how to use the action, the constraints, the Hessian, and the external data of the apparatus.

## 1. Minimal statement

Every calculation must begin by declaring:

- which observable will be calculated;
- which stationary background is used;
- which domain and which boundaries enter;
- which constraints are imposed;
- which parameters are universal constants of GDQ;
- which parameters belong to the apparatus, material, or experimental preparation;
- which experimental data will be used solely for comparison.

Without this separation, a good numerical fit does not distinguish prediction, phenomenological comparison, and reverse engineering.

## 2. Variational chain

The full chain is:

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

Here:

- $\Phi_*$ is an admissible stationary solution;
- $C_a[\Phi]=0$ represents constraints on charge, flux, normalization, gauge, and boundary;
- $P_{\rm phys}$ removes gauge modes and forbidden variations;
- $K_{\rm phys}$ is the physical Hessian of the official action in the allowed sector;
- $J_{\rm app}$ is a classical source, probe, constraint, or boundary condition;
- $\mathsf R_{\rm app}$ is the impedance obtained by variational elimination;
- $\mathcal O_{\rm obs}$ is the comparable observable.

The central link is:

$$
K_{\rm phys}
=
P_{\rm phys}^\dagger
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

If a result uses only an effective reduction of this operator, this must be stated in the text itself.

## 3. Physical projector

If $D C$ is the matrix of linearized constraints and $G$ is the quadratic metric on the fluctuation space, the physical projector is:

$$
P_{\rm phys}
=
I
-
G^{-1}D C^\dagger
\left(D C\,G^{-1}D C^\dagger\right)^{-1}
D C.
$$

It satisfies:

$$
D C\,P_{\rm phys}=0,
\qquad
P_{\rm phys}^2=P_{\rm phys}.
$$

The physical meaning is simple: one only diagonalizes the Hessian after removing directions that correspond to redundancies, coordinate changes, violation of normalization, or unauthorized alteration of charge/flux.

## 4. Schur complement and DtN

When the observable lives on a boundary, detector, or interface, internal degrees of freedom can be eliminated. Writing:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix},
$$

the effective impedance is:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

This formula is the matrix version of the Dirichlet-to-Neumann operator. It appears in detectors, slits, magnetic interfaces, proton surfaces, horizons, nuclear channels, and cosmological boundaries. In all cases, it must be understood as the elimination of degrees of freedom from the Hessian, not as a new fundamental term.

## 5. Numerical classification

Every script must declare one of the categories:

1. direct evaluation of a derived quantity;
2. convergence test;
3. consistency test;
4. reverse engineering;
5. fit or calibration;
6. phenomenological comparison;
7. blind prediction.

For predictive claims, the parameters must be frozen prior to comparison with the accepted data.

## 6. Minimal acceptance criteria

A result is preservable in the manuscript when it reports:

- the equation or functional evaluated;
- domain;
- operator;
- boundary conditions;
- constraints;
- normalization;
- units;
- numerical classification;
- tolerance or mesh study when applicable;
- comparison with the analytical limit when it exists;
- comparison with accepted data when the chapter makes a phenomenological claim;
- remaining limitations.

## 7. What does not close a question

A question is not closed by:

- choosing a coefficient based on the experimental target and calling it derived;
- absorbing discrepancies into thermal effects, boundaries, Fano, loops, or surface effects without calculating the corresponding term;
- omitting a poor mesh result;
- replacing the official action with an external theory;
- calling an analogy a proof;
- using a numerical coincidence to infer a variational identity.

This protocol serves precisely to prevent correct results from being mixed with superseded routes.
