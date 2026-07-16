---
title: Manuscript chapter 05 details
status: active
---

# Manuscript chapter 05 details

## 1. Role of the chapter

Chapter 5 turns the official action into equations. It is not a new action and
does not import the Madelung equations as axioms. Its job is to show which
equations follow from the first variation and which equations require the
later physical reconstruction.

The basic variational identity is:

$$
\delta\left(\mathcal U\mathcal L_0dV_g\right)
=\mathcal U\,\delta\mathcal L_0\,dV_g
+\mathcal L_0\,\delta\mathcal U\,dV_g
+\mathcal U\mathcal L_0\,\delta dV_g.
$$

This is the chapter’s guardrail: the measure and volume must vary when the
fields they depend on vary.

## 2. Direct field variables

The official field is

$$
f=-\ln\rho+\frac{i}{\hbar}S_R,
\qquad
\bar f=-\ln\rho-\frac{i}{\hbar}S_R,
$$

valid on sectors where

$$
\rho>0.
$$

The variations are

$$
\delta f
=-\frac{\delta\rho}{\rho}
+\frac{i}{\hbar}\delta S_R,
\qquad
\delta\bar f
=-\frac{\delta\rho}{\rho}
-\frac{i}{\hbar}\delta S_R.
$$

The measure response is asymmetric:

$$
\delta_{S_R}\mathcal U=0,
\qquad
\delta_\rho\mathcal U
=\mathcal U\frac{\delta\rho}{\rho}.
$$

This asymmetry is why phase variation gives a conservation law while density
variation gives a dynamical equilibrium equation.

## 3. Real form of the integrand

In the real sector:

$$
\operatorname{Re}\left(
g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f
\right)
=|\nabla\ln\rho|_g^2
+\frac{1}{\hbar^2}|\nabla S_R|_g^2.
$$

The internal real density is

$$
\mathcal L_{\rho,S}
=\tau\left[
\mathcal R
+|\nabla\ln\rho|_g^2
+\frac{1}{\hbar^2}|\nabla S_R|_g^2
\right]
-\ln\rho-n.
$$

The wavefunction notation

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}
$$

is only a representation of `(rho,S_R)`, not a new fundamental field.

## 4. Phase variation and current

The phase-dependent part is

$$
\mathcal S_S
=\int_\gamma\int_M
\frac{\hbar}{\Lambda_C^2}
\frac{\tau\mathcal U}{\hbar^2}
g^{\mu\bar\nu}
\partial_\mu S_R\partial_{\bar\nu}S_R
dV_g\frac{d\tau}{\tau}.
$$

Since `U` does not vary with `S_R`, integration by parts gives

$$
\nabla_\mu\widehat J_S^\mu=0,
$$

where

$$
\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U
g^{\mu\bar\nu}\partial_{\bar\nu}S_R.
$$

The reduced convention

$$
J_S^\mu
=\frac{2\tau}{\hbar^2}
\mathcal U
g^{\mu\bar\nu}\partial_{\bar\nu}S_R
$$

has the same local conservation law but differs by a global constant. Charge
normalization must use one convention consistently.

Boundary phase momentum:

$$
\Pi_{S_R}=n_\mu\widehat J_S^\mu.
$$

## 5. Integrated charge and no lateral leakage

For a region bounded by two sections and a lateral wall:

$$
Q_S[\Sigma_2]-Q_S[\Sigma_1]
=-\int_{\mathcal B}\star J_S.
$$

Thus local conservation does not imply conserved charge in an open region.
One needs:

- no lateral leakage; or
- explicit balance with an interface/apparatus.

This is the key bridge to later measurement theory.

## 6. Density variation

Set

$$
q=\ln\rho,
\qquad
K_S=\frac{1}{\hbar^2}|\nabla S_R|_g^2.
$$

Then

$$
\mathcal L_{\rho,S}
=\tau\left(
\mathcal R+|\nabla q|_g^2+K_S
\right)-q-n.
$$

The variation gives

$$
\delta(\mathcal U\mathcal L_{\rho,S})
=\mathcal U(\mathcal L_{\rho,S}-1)\delta q
+2\tau\mathcal U\nabla^aq\nabla_a\delta q.
$$

After weighted integration by parts:

$$
\mathcal L_{\rho,S}-1
-2\tau\left(
\Delta_gq+|\nabla q|_g^2
\right)=\lambda(\tau).
$$

Equivalently:

$$
\tau\left[
\mathcal R+K_S
-2\Delta_gq-|\nabla q|_g^2
\right]-q-n-1
=\lambda(\tau).
$$

The multiplier `lambda(tau)` enforces

$$
\int_M\mathcal U\,dV_g=1.
$$

It is not a phenomenological potential.

## 7. Bohm operator

The identity

$$
\frac{\Delta_g\sqrt\rho}{\sqrt\rho}
=\frac12\Delta_gq
+\frac14|\nabla q|_g^2
$$

implies

$$
-2\Delta_gq-|\nabla q|_g^2
=-4\frac{\Delta_g\sqrt\rho}{\sqrt\rho}.
$$

Thus the density equation becomes:

$$
\tau\left[
\mathcal R
+\frac{1}{\hbar^2}|\nabla S_R|_g^2
-4\frac{\Delta_g\sqrt\rho}{\sqrt\rho}
\right]
-\ln\rho-n-1
=\lambda(\tau).
$$

The differential Bohm structure is derived directly from the official action.
The coefficient `-hbar^2/(2m)` appears only after the physical reduction fixes
the nonrelativistic kinetic normalization.

## 8. Fisher energy check

In the nonrelativistic reduction, if the amplitude energy is

$$
F[\rho]
=\frac{\hbar^2}{8m}
\int_\Sigma\frac{|\nabla\rho|^2}{\rho}\,d^dx,
$$

then

$$
\frac{\delta F}{\delta\rho}
=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

This verifies the operator’s known reduced form, but does not replace the
bulk derivation.

## 9. Hamilton-Jacobi-Bohm reduction

If the physical reduction produces

$$
I_{\rm Mad}
=\int dt\int_\Sigma
\left[
\rho\left(
\partial_tS_R+\frac{|\nabla S_R|^2}{2m}+V
\right)
+\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
\right]d^dx,
$$

then density variation yields

$$
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
$$

Status: conditional reduction. Chapter 5 derives the spatial operator; the
canonical time term belongs to the bridge.

## 10. Metric variation

Using `g^{AB}` as independent variable:

$$
\delta dV_g
=-\frac12g_{AB}\delta g^{AB}dV_g.
$$

The weighted curvature variation produces:

$$
\begin{aligned}
\delta\int_M\mathcal U\mathcal R\,dV_g
={}&\int_M
\left[
\mathcal U\left(
\mathcal R_{AB}-\frac12\mathcal Rg_{AB}
\right)
\\
&\qquad
+g_{AB}\Delta_g\mathcal U
-\nabla_A\nabla_B\mathcal U
\right]
\delta g^{AB}\,dV_g
+B_{\mathcal R}.
\end{aligned}
$$

The normalized metric equation is:

$$
\begin{aligned}
0={}&\tau\mathcal U
\left(
\mathcal R_{AB}+P_{AB}^{(f)}
\right)
\\
&+\tau\left(
g_{AB}\Delta_g\mathcal U
-\nabla_A\nabla_B\mathcal U
\right)
\\
&-\frac12\mathcal U
\left(
\mathcal L_0-\lambda(\tau)
\right)g_{AB}.
\end{aligned}
$$

This equation is metric-dilatonic and weighted; it is not simply Einstein’s
equation renamed.

## 11. Bismut torsion status

In the declared variation, the Hermitian/Bismut structure is fixed or varied
only within a declared class. Torsion is not an arbitrary independent tensor.

If `J` and connection data are varied, one must explicitly enlarge the
variational class and recompute the Hessian/projected equations. This is not a
new fundamental term.

## 12. Noether proof

For a continuous symmetry

$$
\delta_\varepsilon\Phi^A=\varepsilon\Delta_\xi\Phi^A,
$$

with

$$
\delta_\varepsilon\mathscr L
=\varepsilon\nabla_aB_\xi^a,
$$

the first variation gives

$$
\nabla_aJ_\xi^a
=-\mathcal E_A\Delta_\xi\Phi^A,
$$

where

$$
J_\xi^a
=\Theta^a(\Phi,\Delta_\xi\Phi)-B_\xi^a.
$$

On shell:

$$
\nabla_aJ_\xi^a=0.
$$

For the phase shift, this is exactly the current derived by direct variation.

## 13. Boundaries and interfaces

The generic boundary term is

$$
\delta\mathcal S\big|_{\partial M}
=\int_{\partial M}\Pi_A\,\delta\Phi^A.
$$

Legitimate closures:

1. Dirichlet: fix field trace;
2. Neumann: fix/anull normal momentum;
3. interface: include action/source response:

$$
\Pi_A+\frac{\delta\mathcal S_{\rm int}}{\delta\Phi^A}=0.
$$

Robin and DtN conditions are interface responses, not arbitrary spectral
knobs.

## 14. What remains conditional

Chapter 5 does not prove:

- a bulk Riemannian coordinate is physical time;
- normal phase current equals laboratory `rho`;
- the pullback creates `rho partial_t S_R` with correct normalization;
- arbitrary causal contours yield real action;
- any given background is stable;
- global cosmological normalization is transported to the lab.

These are bridge and measurement-theory tasks, not modifications of the
official action.
