---
title: "GDQ Construction of Stern-Gerlach"
---

# GDQ Construction of Stern-Gerlach

## 1. Statement

Stern--Gerlach is a classical magnetic boundary problem applied to a soliton that already possesses circulation/spin.

The chain is:

$$
J_{\rm SG}^{\rm classical}
\to
\Phi_\ast^{\rm SG}
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm SG}
\to
P_{\mathbf n}^{\pm}
\to
\Delta z_\pm
\to
\text{register}.
$$

## 2. Magnetic Source

The field of the apparatus defines:

$$
\mathbf n(\mathbf x)
=
\frac{\mathbf B(\mathbf x)}{|\mathbf B(\mathbf x)|}.
$$

It enters as a source or boundary. It does not alter the official action.

At the variational level, the physical information provided by the apparatus is external: field profile, interaction region, material, and transit time. We denote these data by $J_{\rm SG}^{\rm classical}$. The geometric response is not inserted by hand; it is obtained via the linearized solution:

$$
K_{\rm phys}^{\rm obj}\,\delta\Phi_{\rm SG}
=
J_{\rm SG}^{\rm classical},
$$

where $K_{\rm phys}^{\rm obj}$ is the physical Hessian of the object before the reading of the apparatus. The classical field selects the direction $\mathbf n$; the theory calculates how the defect responds to this selection.

## 3. Background and Hessian

The stationary background with the apparatus satisfies:

$$
\left.
\frac{\delta}
{\delta\Phi}
\left(
\mathcal S_{\rm GDQ}
+
\mathcal S_{\rm SG}
\right)
\right|_{\Phi_\ast^{\rm SG}}
=
0.
$$

The physical stiffness is:

$$
K_{\rm phys}^{\rm SG}
=
P_{\rm phys}^{\dagger}
K_{\rm GDQ}[\Phi_\ast^{\rm SG}]
P_{\rm phys}.
$$

Eliminating internal degrees of freedom:

$$
\mathsf R_{\rm SG}
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}.
$$

Here $Y$ represents the interface degrees of freedom observed by the apparatus and $I$ represents the unmonitored internal degrees of freedom of the object. The Schur complement is the precise way to state that the apparatus does not directly measure the entire bulk: it sees an effective impedance at the boundary. Thus, $\mathsf R_{\rm SG}$ is an interface response, not a new fundamental parameter.

## 4. Projectors

The axis of the apparatus defines the projectors:

$$
P_{\mathbf n}^{\pm}
=
\frac12
\left(
I\pm\mathbf n\cdot\sigma
\right).
$$

They do not state that the apparatus created the spin. They state that the apparatus chose the observable decomposition.

## 5. Force and Deflection

In the fixed channel:

$$
F_z^\pm
=
\pm\mu\frac{\partial B_z}{\partial z}.
$$

For a region of length $L$ and longitudinal velocity $v_y$:

$$
\Delta z_\pm
=
\pm
\frac{\mu L^2}{2mv_y^2}
\frac{\partial B_z}{\partial z}.
$$

## 6. Weights

For preparation $\mathbf a$:

$$
p_\pm(\mathbf n|\mathbf a)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

This part uses operational Born in the reconstructed Hilbert space. The GDQ construction provides the axis, the interface response, and the channels.

## 7. Metrological Status

The formulas of this chapter separate three levels:

1. universal structure of the channels, given by Hopf/Clifford;
2. center-of-mass motion in a fixed channel, given by the classical field of the apparatus;
3. fine metrology of a real instrument, given by $\mathsf R_{\rm SG}$, losses, causal mobility, and effective geometry of the detector.

The chapter closes the first two levels and defines the third as a metrological application. This does not re-open the conceptual structure of the Stern--Gerlach; it merely indicates which experimental data are necessary to reproduce a specific real apparatus.
