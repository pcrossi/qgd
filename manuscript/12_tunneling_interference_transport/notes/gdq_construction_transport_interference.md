---
title: "GDQ construction of transport and interference"
---

# GDQ construction of transport and interference

## 1. Statement

Tunneling, double slit, detector, and delayed choice are domain, boundary, and transport problems. They do not require a change to the official action.

The general chain is:

$$
J_{\rm app}^{\rm classical}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\rho,S_R
\to
\text{current}
\to
\text{readout}.
$$

## 2. Barrier and tunneling

In the reduced model, the barrier specifies a one-dimensional domain and an effective deformation. The ansatz used in the chapter is:

$$
g_{xx}\propto\rho.
$$

It is not a general theorem of the official action. It defines a conditional reduced sector that allows studying the proper distance saturation.

## 3. Double slit

The plate with two slits defines the boundary:

$$
\partial M_{\rm plate}
=
\partial M_{\rm open}
\cup
\partial M_{\rm closed}.
$$

In the flat Madelung sector, the following evolve:

$$
\rho,
\qquad
S_R,
\qquad
J^\mu=\rho\nabla^\mu S_R/m.
$$

The fringes come from the coherent sum of the two boundary solutions.

## 4. Detector

A detector coupled to a slit alters the interface impedance:

$$
\mathsf R_{\rm det}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

The loss of visibility is:

$$
\mathcal C_{\rm det}
=
e^{-\Gamma_{\rm det}},
$$

with:

$$
\Gamma_{\rm det}
=
\frac12
\left\langle
\Delta\Phi_\partial,
\mathsf R_{\rm det}
\Delta\Phi_\partial
\right\rangle.
$$

## 5. Delayed choice

The time-dependent apparatus changes the boundary:

$$
\mathsf R_{\rm old}(t)
\to
\mathsf R_{\rm new}(t).
$$

The final solution depends on the causal transport problem effectively realized before readout. There is no physical signal sent to the past.

## 6. Limitation

For a real apparatus, it is necessary to calculate $\Phi_\ast$, $K_{\rm phys}$, and $\mathsf R_{\rm app}$ using the geometry, material, losses, and response times of the concrete device.
