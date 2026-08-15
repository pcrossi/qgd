---
title: "Background, Hessian, and DtN in Stern-Gerlach"
---

# Background, Hessian, and DtN in Stern--Gerlach

## 1. What this note proves

This note completes the Stern--Gerlach chain at the GDQ level, separating three layers:

1. the stationary bulk background;
2. the variational domain on the stoma;
3. the interface response measured by the apparatus.

The official action is not modified. The apparatus enters as an external classical source and as a physical boundary datum.

## 2. Normal Background in $\mathbb C^2$

In the slice normal to the stoma, we use the radial metric:

$$
ds_\perp^2=dr^2+a(r)^2d\Omega_3^2,
$$

with real dilaton:

$$
f=F(r).
$$

The metric-dilatonic stationary equation of the weighted Perelman sector assumes the form:

$$
\operatorname{Ric}+\nabla^2F=\frac{1}{2\tau}g.
$$

For the metric above, the two independent blocks are:

$$
-3\frac{a''}{a}+F''=\frac{1}{2\tau},
$$

$$
\frac{2(1-a'^2)-aa''}{a^2}
+\frac{F'a'}{a}
=\frac{1}{2\tau}.
$$

The exact bulk solution is:

$$
a_\ast(r)=r,
\qquad
F_\ast(r)=\frac{r^2}{4\tau}+F_0.
$$

For an excised exterior $r\ge r_c$, the normalization of the measure determines:

$$
x_c=\frac{r_c^2}{4\tau},
$$

$$
F_0=\log\left(e^{-x_c}(1+x_c)\right).
$$

The script `construct_sg_stationary_background.py` numerically verifies that the maximum residue of these two equations is zero, within machine precision, in the truncated domain used in the test.

## 3. Boundary Obstruction and Free Variational Condition

At the inner boundary of the excised exterior, the normal points into the hole:

$$
n=-\partial_r.
$$

Therefore:

$$
n(F_\ast)=-\frac{r_c}{2\tau}.
$$

The isolated bulk does not fix the Robin matrix of the stoma by itself. For a free stoma, the weighted boundary completion imposes the weighted mean curvature:

$$
K-n(F)=0.
$$

Since, on the hypersphere of radius $r_c$,

$$
K=-\frac{3}{r_c},
$$

the free condition yields:

$$
-\frac{3}{r_c}
-\left(-\frac{r_c}{2\tau}\right)
=0.
$$

Therefore:

$$
r_c^2=6\tau,
\qquad
r_c=\sqrt{6\tau}.
$$

The verifier `verify_sg_variational_boundary.py` confirms, for $\tau=1$:

$$
K-n(F)=-2.22\times10^{-16}.
$$

This condition defines the common geometric domain of the Hessian. It is not yet the specific axial response of the apparatus.

## 4. Classical Stern--Gerlach Source

The apparatus provides an external field $\mathbf B(x,t)$. The local direction is:

$$
\mathbf n(x,t)=\frac{\mathbf B(x,t)}{|\mathbf B(x,t)|}.
$$

The reduced probe coupling is:

$$
S_{\rm probe}[\Phi;\mathbf B]
=
-\mu
\int_{\Sigma_{\rm SG}}
d\mu_\Sigma(\Phi)
\operatorname{Tr}
\left(P(\Phi)\,\boldsymbol\sigma\cdot\mathbf B\right).
$$

Here $\Phi=(g,f,\bar f)$ and $P(\Phi)$ is the axial projector reconstructed from the geometry. The linear source entering the Hessian is:

$$
J_{\rm SG}
=
-\left.
\frac{\delta S_{\rm probe}}{\delta\Phi}
\right|_{\Phi_\ast}.
$$

Separating the variation of the projector from the variation of the volume:

$$
J_{\rm SG}
=
\mu(\mathcal D_\Phi P)^*
\left(\boldsymbol\sigma\cdot\mathbf B\right)
+J_{\rm vol}.
$$

For purely orientational fluctuations that preserve volume to first order, $J_{\rm vol}=0$.

## 5. Physical Hessian and Linear Response

If $K_{\rm GDQ}[\Phi_\ast]$ is the second variation of the official action in the background with a fixed boundary domain, we remove diffeomorphisms, global phase, and isometries via the physical projection:

$$
K_{\rm phys}
=
P_{\rm phys}^\dagger
K_{\rm GDQ}[\Phi_\ast]
P_{\rm phys}.
$$

The linear response to the apparatus is:

$$
K_{\rm phys}\,\delta\Phi_{\rm SG}
=
J_{\rm SG}.
$$

In the complement of the zero modes, if the gap is positive, the solution is:

$$
\delta\Phi_{\rm SG}
=
K_{\rm phys}^{-1}J_{\rm SG}.
$$

Decomposed into eigenfunctions:

$$
K_{\rm phys}\Psi_\nu=\lambda_\nu\Psi_\nu,
\qquad
\lambda_\nu>0,
$$

we have:

$$
\delta\Phi_{\rm SG}
=
\sum_\nu
\frac{\langle\Psi_\nu,J_{\rm SG}\rangle}{\lambda_\nu}
\Psi_\nu.
$$

This is the correct way to obtain the deformation of the stoma by the apparatus. There is no external quantum operator inserted as a new ontology.

## 6. Interface Impedance by Schur/DtN

Divide the degrees of freedom into interface $Y$ and interior $I$:

$$
\delta\Phi=(\delta\Phi_Y,\delta\Phi_I).
$$

The block Hessian is:

$$
K=
\begin{pmatrix}
K_{YY} & K_{YI}\\
K_{IY} & K_{II}
\end{pmatrix}.
$$

Eliminating the internal stationary degrees of freedom:

$$
\delta\Phi_I=-K_{II}^{-1}K_{IY}\delta\Phi_Y.
$$

The stiffness seen by the apparatus is the Schur complement:

$$
\mathsf R_{\rm SG}
=
K_{YY}
-K_{YI}K_{II}^{-1}K_{IY}.
$$

This is also the DtN interpretation: the apparatus imposes boundary data and the geometry returns the effective normal derivative.

## 7. Induced Textural Stiffness

Projecting the source onto physical modes:

$$
j_{\nu A}=\langle\Psi_\nu,J_A\rangle,
$$

and writing the tangential symbol as:

$$
\lambda_\nu+Z_\nu k^2+O(k^4),
$$

the induced action is:

$$
S_{\rm ind}^{(2)}
=
-\frac12
\langle J_{\rm SG},K_{\rm phys}^{-1}J_{\rm SG}\rangle.
$$

Expanding in $k$:

$$
\frac{1}{\lambda_\nu+Z_\nu k^2}
=
\frac{1}{\lambda_\nu}
-\frac{Z_\nu}{\lambda_\nu^2}k^2
+O(k^4).
$$

Comparing with the texture energy in $\mathbb{CP}^1$:

$$
S_{\rm eff}^{(2)}
\supset
\frac12
\int
\kappa_{AB}^{\rm SG}
\partial_aq^A\partial^aq^B\,dV,
$$

we obtain:

$$
\kappa_{AB}^{\rm SG}
=
\sum_\nu
\frac{Z_\nu}{\lambda_\nu^2}
j_{\nu A}^\ast j_{\nu B}.
$$

In the isotropic background:

$$
\kappa_H^{\rm SG}
=
\frac12
(G_{\rm FS})^{AB}
\sum_\nu
\frac{Z_\nu}{\lambda_\nu^2}
j_{\nu A}^\ast j_{\nu B}.
$$

Thus:

$$
\lambda_\nu>0,
\quad
Z_\nu>0,
\quad
j_{\nu A}\ne0
\quad
\Longrightarrow
\quad
\kappa_H^{\rm SG}>0.
$$

## 8. Gaussian Negative Result and cylindrical Hopf Branch

The exterior Gaussian shrinker is an exact bulk solution, but the axial DtN test shows:

$$
Z_H^{\rm Gaussian}=0.
$$

Physically, this means that the global orientation escapes to the exterior with no textural cost. Therefore, the pure Gaussian is not the complete physical stoma for Stern--Gerlach.

The cylindrical Hopf branch:

$$
\mathbb R_+\times S^3_{2\sqrt\tau}
$$

has axial harmonic $l=2$ and potential:

$$
V_H=\frac{2}{\tau}.
$$

The reduced DtN problem is:

$$
-\eta''+\frac{x}{2}\eta'+2\eta=0,
\qquad
\eta(0)=1,
\qquad
\eta(\infty)=0.
$$

The numerical solution yields:

$$
z_H=-\eta'(0)
=
1.329340388179\ldots
=
\frac{3\sqrt\pi}{4}.
$$

Furthermore, in the normalized cylindrical family:

$$
\mathcal W''(2\sqrt\tau)
=
\frac{3}{2\tau}>0.
$$

Therefore, the homogeneous radius mode of the Hopf cylinder is stable in the reduced sector. The complete tensorial/radial stability of a real apparatus geometry belongs to the metrological closure, not to the conceptual closure of the two channels.

## 9. Dimensional Coefficients of Non-Adiabatic Passage

In the reduced two-level sector:

$$
H_2
=
\frac{\hbar}{2}
\left(\omega_\parallel\sigma_z+\omega_\perp\sigma_x\right),
$$

with:

$$
H_Z
=
-\frac{g_{\rm geom}\mu_B}{2}
\boldsymbol\sigma\cdot\mathbf B.
$$

The Landau--Zener parameters are:

$$
\Delta
=
\frac{|g_{\rm geom}|\mu_B}{\hbar}
|B_\perp|,
$$

$$
v
=
\frac{|g_{\rm geom}|\mu_B}{\hbar}
\left|
\partial_tB_\parallel
+\mathbf u\cdot\nabla B_\parallel
\right|.
$$

The asymptotic transition probability is:

$$
P_{\rm LZ}
=
\exp\left(
-\frac{\pi\Delta^2}{2v}
\right).
$$

These quantities are calculable when the apparatus profile is provided. The field is an experimental boundary datum; it is not an internal parameter of the action.

## 10. Contract for a Complete Metrological Prediction

To calculate $\kappa_H^{\rm SG}$ and $\Gamma_{\rm SG}$ of a real apparatus without post-adjustment, the numerical background must provide:

$$
\{\lambda_\nu,\ Z_\nu,\ j_{\nu1},\ j_{\nu2},\ \gamma_\nu,\ C_\nu\}.
$$

Then:

$$
\Gamma_{\rm SG}
=
\frac{\mu^2}{\hbar^2}
\sum_\nu
\frac{C_\nu}{\gamma_\nu}.
$$

Here $\gamma_\nu$ is the causal relaxation rate, not a static eigenvalue. The bridge between both requires the causal mobility of the apparatus.

## 11. Status

The Stern--Gerlach is closed as a geometric-operational reconstruction:

- the object carries spin/circulation before the apparatus;
- the apparatus selects the axis;
- Hopf provides two projectors;
- operational Born provides the weights;
- the classical force separates the centers of mass;
- the non-adiabatic sector has an explicit criterion;
- the interface response is Schur/DtN of the official Hessian.

What remains as applied metrology is the calculation of a specific real detector, with material, losses, temperature, mobility, and profile $\mathbf B(x,t)$.
