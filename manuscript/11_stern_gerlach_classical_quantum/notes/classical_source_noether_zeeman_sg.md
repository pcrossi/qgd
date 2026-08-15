---
title: "Classical source and Noether--Zeeman"
---

# Classical source and Noether--Zeeman

This note preserves the correct route for the magnetic coupling in Stern--Gerlach. The field of the apparatus is a given classical source; the object responds via its geometric current and its physical Hessian. The Pauli operator is not inserted as a fundamental interaction.

## 1. Classical Source of the Apparatus

The electromagnet is described in physical space by a prescribed classical current:

$$
j_A^\mu,
\qquad
\nabla_\mu j_A^\mu=0.
$$

It determines:

$$
F_A=dA_A,
\qquad
dF_A=0,
\qquad
d{*F_A}=*j_A.
$$

In the region of the experiment:

$$
\mathbf B_A=\nabla\times\mathbf A_A,
\qquad
\nabla|\mathbf B_A|\ne0.
$$

GDQ must not predict which current the experimentalist chose. It must predict the response of the soliton to the supplied external field.

## 2. Geometric Current of the Object

The object has a geometric current written as the divergence of an antisymmetric density:

$$
j_Q^\mu
=
\nabla_\alpha\mathcal T_Q^{\alpha\mu}.
$$

The density $\mathcal T_Q$ is the spin-torsion projection of the Bismut/Cartan sector. Using the classical current coupling:

$$
S_{\rm int}^{(1)}
=
\frac q c
\int A_{A\mu}j_Q^\mu\,d\mu,
$$

and integrating by parts:

$$
S_{\rm int}^{(1)}
=
\frac q{2c}
\int
\mathcal T_Q^{\mu\nu}F^{\rm app}_{\mu\nu}\,d\mu
+S_{\partial}^{A\mathcal T}.
$$

The global sign depends on the orientation and convention for $F=dA$. The gauge-invariant bilinear structure does not depend on this choice.

In the bulk:

$$
S_{\rm int}[\Phi;F_A]
=
\frac q{2c}
\int_{\Omega_{\rm SG}}
\chi_{\rm SG}\,
\mathcal T^{AB}[\Phi]F^{\rm app}_{AB}\,d\mu_\Phi.
$$

This is a probe source. It is not a new term of the official action.

## 3. Variation and Interface Operator

For a perturbation $\delta\Phi$:

$$
\delta S_{\rm int}
=
\frac q{2c}
\int_{\Omega_{\rm SG}}\chi_{\rm SG}
\left[
\left(D_\Phi\mathcal T\cdot\delta\Phi\right)^{AB}F^{\rm app}_{AB}
+\mathcal T^{AB}F^{\rm app}_{AB}\delta\log d\mu_\Phi
\right]d\mu_\Phi.
$$

Hence, in the inner product of the official measure:

$$
J_A
=
-\frac q{2c}
\left(D_\Phi\mathcal T\right)^*
\left(\chi_{\rm SG}F_A\right)
+J_{\rm measure}.
$$

The linearized equation is:

$$
\mathbb H_{\rm GDQ}^{\rm phys}\delta\Phi
=
J_A.
$$

At the interface, separating the DtN of the object and the Hessian of the apparatus:

$$
(\Lambda_Q+\mathsf R_A)\delta\varphi
=
\delta J_A.
$$

A homogeneous Robin boundary condition appears only when the source has already been absorbed into the stationary background or when fluctuations without further external variation are studied.

## 4. Reduction to the Hopf Modulus

The free modulus of the spin is:

$$
\mathcal O\simeq SU(2)/U(1)\simeq S^2\simeq\mathbb{CP}^1.
$$

In the axial sector, the antisymmetric density is dual to a vector:

$$
t_i(P)
=
\frac12\epsilon_{ijk}\mathcal T^{jk}(P).
$$

Isotropy and equivariance imply:

$$
t_i(P)=t_H n_i(P).
$$

Since:

$$
\frac12\mathcal T^{ij}F^{\rm app}_{ij}
=
\mathbf t(P)\cdot\mathbf B_A,
$$

the axial reduction yields the Zeeman form:

$$
E_{\rm int}
=
-\boldsymbol\mu_{\rm GDQ}\cdot\mathbf B_A.
$$

The matrices $\sigma$ and the projectors $P_{\mathbf n}^{\pm}$ appear only after restricting this modulus to the effective spinorial space. They are not inserted into the fundamental action.

## 5. Noether--Zeeman Theorem

The official action is invariant under a constant shift of the phase:

$$
f\mapsto f+i\varepsilon,
\qquad
\bar f\mapsto\bar f-i\varepsilon.
$$

Promoting $\varepsilon$ locally, one obtains the Noether current:

$$
J_{\rm N}^A
\propto
i\tau\mathcal U
\left(
g^{A\bar B}\partial_{\bar B}\bar f
-g^{B\bar A}\partial_Bf
\right),
\qquad
\nabla_AJ_{\rm N}^A=0.
$$

On the defect, its rotational projection defines:

$$
\boldsymbol{\mathcal C}[\Phi]
=
\int_\Sigma\boldsymbol J_{\rm N}\cdot d\boldsymbol\Sigma.
$$

The elementary sector is:

$$
\boldsymbol C
=
\pm\frac\hbar2\boldsymbol n.
$$

Impose the circulation constraint via a Lagrange multiplier:

$$
\mathscr I[\Phi,\boldsymbol\lambda;\boldsymbol C,\boldsymbol B]
=
\mathcal S_{\rm GDQ}[\Phi]
-\boldsymbol B\cdot\boldsymbol M[\Phi]
-\boldsymbol\lambda\cdot
\left(\boldsymbol{\mathcal C}[\Phi]-\boldsymbol C\right).
$$

If the field couples to the same conserved current that defines the circulation:

$$
\boldsymbol M[\Phi]
=
\gamma_0\boldsymbol{\mathcal C}[\Phi]
+\boldsymbol M_\perp[\Phi].
$$

The protected part satisfies:

$$
-\frac{\partial\lambda_i}{\partial B_j}
=
\gamma_0\delta_{ij}.
$$

Therefore, the minimal component has:

$$
Z_{\rm N}=1.
$$

The total momentum can contain a transverse geometric dressing:

$$
\gamma_{\rm eff}
=
\gamma_0+\Delta\gamma_{\rm geom}.
$$

With the constrained Hessian $H_C$, write:

$$
\gamma_{\rm eff}
=
\frac{\langle c,H_C^{-1}m\rangle}
{\langle c,H_C^{-1}c\rangle},
$$

where $c=\delta\mathcal C/\delta\Phi$ and $m=\delta M/\delta\Phi$. Separating $m=\gamma_0c+m_\perp$:

$$
\Delta\gamma_{\rm geom}
=
\frac{\langle c,H_C^{-1}m_\perp\rangle}
{\langle c,H_C^{-1}c\rangle}.
$$

## 6. Stationary Selection

By isotropy, the reduced energy in a weak field can only contain:

$$
E(\boldsymbol C,\boldsymbol B)
=
E_0(C^2)-\gamma_{\rm eff}\boldsymbol C\cdot\boldsymbol B+O(B^2).
$$

With $|\boldsymbol C|$ fixed:

$$
\delta\boldsymbol C
=
\delta\boldsymbol\theta\times\boldsymbol C.
$$

Hence:

$$
\delta E
=
-\gamma_{\rm eff}\delta\boldsymbol\theta\cdot
(\boldsymbol C\times\boldsymbol B).
$$

The stationary condition is:

$$
\boldsymbol C\times\boldsymbol B=0.
$$

Thus:

$$
\boldsymbol C_\pm
=
\pm\frac\hbar2\frac{\boldsymbol B}{|\boldsymbol B|},
$$

and:

$$
\boldsymbol F_\pm
=
\pm\gamma_{\rm eff}\frac\hbar2\nabla|\boldsymbol B|.
$$

This is the structural closure of the Zeeman channel in Stern--Gerlach. The metrology of the total factor requires evaluating the transverse geometric dressing of the real background.
