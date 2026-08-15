---
title: "Physical Hessian C3 and reduced gap"
---

# Physical Hessian C3 and reduced gap

This note details the stability block used in the selection of three stomata. The calculation is reduced, but derives from the correct variational procedure of GDQ: official action, Noether constraint, Hessian, physical projection, and Schur complement.

## 1. Collective variables

In the $C_3$ junction, write the horizontal tensions as:

$$
\mathbf T_a
=
T(\cos\theta_a,\sin\theta_a),
\qquad
a=1,2,3.
$$

The flux constraint is:

$$
\mathcal C(\theta)
=
\sum_{a=1}^{3}\mathbf T_a.
$$

The symmetric equilibrium is:

$$
\theta_a=\theta_0+\frac{2\pi(a-1)}{3}.
$$

## 2. Constrained Hessian

The augmented functional is:

$$
\widetilde{\mathcal S}
=
\mathcal S_{\rm GDQ}
+\boldsymbol\lambda\cdot\mathcal C.
$$

Linearizing the constraint:

$$
D\mathcal C
=
T
\begin{pmatrix}
-\sin\theta_1&-\sin\theta_2&-\sin\theta_3\\
\cos\theta_1&\cos\theta_2&\cos\theta_3
\end{pmatrix}.
$$

The second constrained variation in the angular sector is:

$$
H_\theta
=
\kappa_{\rm rel}
(D\mathcal C)^\dagger D\mathcal C.
$$

At the $C_3$ point:

$$
\operatorname{spec}H_\theta
=
\kappa_{\rm rel}T^2
\left\{
0,\frac32,\frac32
\right\}.
$$

The zero eigenvalue is the simultaneous global rotation. The physical projector removes this mode:

$$
P_{\rm phys}
=
I
-
\frac13
\mathbf 1\mathbf 1^\top.
$$

Hence:

$$
P_{\rm phys}^\top H_\theta P_{\rm phys}
=
\frac32\kappa_{\rm rel}T^2 I_2.
$$

## 3. Homogeneous radial mode and Schur

The homogeneous radial mode preserving the primitive class has rigidity:

$$
K_\perp^{(r,0)}
=
\frac{3}{2\tau}I_3.
$$

The conservation of the flux class eliminates the angular-radial coupling in the physical sector:

$$
J_{\theta r}=0.
$$

Thus, the Schur complement is:

$$
H_{\rm eff}
=
H_{\rm rel}
-
J_{\theta r}
\left(K_\perp^{(r,0)}\right)^{-1}
J_{\theta r}^{\dagger}
=
H_{\rm rel}.
$$

## 4. Inhomogeneous modes

In the reduced Gaussian filling, the inhomogeneous modes of the metric-dilatonic Hessian operator enter via the Ornstein--Uhlenbeck operator:

$$
L_f=-\Delta_f.
$$

Its normalized spectrum is:

$$
\operatorname{spec}L_f
=
\left\{
\frac{m}{2\tau}
:
m=0,1,2,\ldots
\right\}.
$$

After removing the symmetry and normalization modes, the first physical inhomogeneous mode is:

$$
\lambda_{\rm nh}
=
\frac{1}{2\tau}.
$$

Therefore, in the normalization $T=1$, $\kappa_{\rm rel}=1$:

$$
\lambda_{\rm gap}^{C_3}
=
\min
\left\{
\frac32,
\frac{1}{2\tau}
\right\}.
$$

For $\tau=1$:

$$
\lambda_{\rm gap}^{C_3}=\frac12.
$$

## 5. Status

The result closes the stability in the horizontal reduced sector and in the projected physical Gaussian filling. It does not claim that every mixed cosmological background has been diagonalized; it claims that the local count by three stomata has no instability in the block that selects it.

## 6. Computational verification

The script:

$$
{\tt scripts/physical_hessian_c3_gap.py}
$$

explicitly calculates the angular spectrum, the physical projector, the radial block, the Schur complement, and the reduced gap.
