---
title: "Symplectic current of the official Hessian"
---

# Symplectic current of the official Hessian

## 1. Statement

This note preserves the correct construction used to normalize surgery modes, decay, and baryonic channels.

The Noether continuity current and the Hessian symplectic current are related, but they are not the same thing:

$$
\nabla_A J_\theta^A=0
$$

is the conservation of global phase, while:

$$
\nabla_A\omega^A(\delta_1\Phi,\delta_2\Phi)=0
$$

is the bilinear conservation of the linearized Hessian.

## 2. Real Variables

Write:

$$
f=\sigma+i\theta,
\qquad
\sigma=-\log\rho,
\qquad
\theta=\frac{S_R}{\hbar}.
$$

In a fixed causal slice, the local density of the official action has the form:

$$
\mathcal L_z
=
\frac{\hbar}{\Lambda_C^2}
\sqrt g\,\mathcal U
\left[
\tau
\left(
\mathcal R
+
|\nabla\sigma|^2
+
|\nabla\theta|^2
\right)
+
\sigma
-
4
\right],
$$

where $4$ is $n=\dim_{\mathbb C}M$ in the official local bulk.

## 3. Pre-symplectic Potential

For a general variation,

$$
\delta\mathcal L_z
=
\sqrt g
\left[
\mathcal E_I\delta\Phi^I
+
\nabla_A\Theta_z^A(\Phi;\delta\Phi)
\right].
$$

If $h^{AB}=\delta g^{AB}$ and $h=g_{AB}h^{AB}$, the weighted curvature part contributes:

$$
\begin{aligned}
\Theta_{g,z}^A
=
\frac{\hbar\tau}{\Lambda_C^2}
\big[
&\mathcal U(\nabla_Bh^{AB}-\nabla^Ah)\\
&-(\nabla_B\mathcal U)h^{AB}
+(\nabla^A\mathcal U)h
\big].
\end{aligned}
$$

The density–phase part contributes:

$$
\Theta_{f,z}^A
=
\frac{2\hbar\tau}{\Lambda_C^2}
\mathcal U
\left(
\nabla^A\sigma\,\delta\sigma
+
\nabla^A\theta\,\delta\theta
\right).
$$

Thus,

$$
\Theta_z^A=\Theta_{g,z}^A+\Theta_{f,z}^A.
$$

## 4. Symplectic Current

For two perturbations,

$$
\omega_z^A(\Phi;\delta_1\Phi,\delta_2\Phi)
=
\delta_1\Theta_z^A(\Phi;\delta_2\Phi)
-
\delta_2\Theta_z^A(\Phi;\delta_1\Phi).
$$

Antisymmetrizing the second variation of the action,

$$
\nabla_A\omega_z^A
=
\delta_1\mathcal E_I\,\delta_2\Phi^I
-
\delta_2\mathcal E_I\,\delta_1\Phi^I.
$$

Thus, in a background that satisfies the official equations, and for perturbations that satisfy the linearized Hessian:

$$
\nabla_A\omega_z^A=0.
$$

Before using this current as a physical inner product, gauge/diffeomorphism directions must be removed and constraints of flux, charge, and APS orientation must be imposed.

## 5. Phase Sector and Continuity

The global symmetry:

$$
\theta\mapsto\theta+\alpha
$$

provides the Noether current:

$$
J_\theta^A
=
\frac{2\hbar\tau}{\Lambda_C^2}
\mathcal U\nabla^A\theta
=
\frac{2\tau}{\Lambda_C^2}
\mathcal U\nabla^A S_R.
$$

The phase equation gives:

$$
\nabla_AJ_\theta^A=0.
$$

After the reconstruction of physical time, this conservation takes the local form of continuity in the laboratory:

$$
\partial_t\mathcal U+\nabla_i(\mathcal U v^i)=0.
$$

## 6. Green's Form of the Hessian

For a physical block written as:

$$
L\psi
=
-\mathcal U^{-1}
\nabla_A
\left(
\mathcal U A^{AB}\nabla_B\psi
\right)
+
V\psi,
$$

Green's identity is:

$$
\nabla_A j^A(\psi_1,\psi_2)
=
\mathcal U
\left(
\psi_2 L\psi_1-\psi_1L\psi_2
\right),
$$

with:

$$
j^A(\psi_1,\psi_2)
=
\mathcal U A^{AB}
\left(
\psi_1\nabla_B\psi_2
-
\psi_2\nabla_B\psi_1
\right).
$$

For two modes of the kernel, $L\psi_1=L\psi_2=0$, we have:

$$
\nabla_Aj^A=0.
$$

This is the practical form used to normalize outgoing modes, since the flux is independent of the slicing hypersurface.

## 7. Causal Pullback

The physical boundary current is obtained by:

$$
\omega_\gamma^A
=
\oint_\gamma
\omega_z^A
\frac{d\tau}{\tau}.
$$

In the Laurent representation, the positive orientation of the contour selects the appropriate coefficient of the causal expansion:

$$
\omega_\gamma^A
=
\frac{2\pi i}{(4\pi)^4}
[z^3]\widehat\omega^A(z),
$$

where $\widehat\omega^A$ includes the pullback weights not shown.

## 8. Normalization of Modes

After reconstructing the physical section, we define:

$$
(\Psi_a,\Psi_b)_\Sigma
=
i
\int_\Sigma
n_A
\omega_\gamma^A(\overline{\Psi_a},\Psi_b)
d\Sigma.
$$

The APS orientation selects the sign of the flux of the outgoing modes. In the physical sector:

$$
(\Psi_a,\Psi_b)_\Sigma=\delta_{ab}.
$$

This removes the freedom to separately rescale the legs of the process, but does not replace the calculation of the physical vertex or the transverse Green's function.

## 9. Status

- pre-symplectic potential: derived from the official action;
- symplectic current: derived by antisymmetrization of the second variation;
- Noether current: derived in the phase sector;
- Green's form: derived for the physical block of the Hessian;
- APS normalization: defined in the reconstructed sector;
- complete evaluation in baryonic modes: depends on the physical modes of the complete surface Hessian.

## 10. Symbolic Verification

The script `scripts/verify_green_current_hessian.py` verifies Green's identity for a representative weighted Sturm–Liouville operator of the Hessian physical block.
