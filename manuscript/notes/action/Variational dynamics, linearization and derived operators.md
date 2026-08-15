---
title: "Variational dynamics, linearization and derived operators"
status: "structural theorem under declared analytical hypotheses"
---

# Variational dynamics, linearization and derived operators

## 1. The distinction that must be preserved

GDQ does not start with a quantum operator. It starts with the official action, defined on a class of admissible fields and on a causal contour. If we gather the fields into

$$
\Phi=(g,J,H,f),
$$

with

$$
H=d_J^c\omega_g,
$$

the fundamental problem consists in finding the admissible configurations for which

$$
\delta\mathcal S_{\rm GDQ}[\Phi]=0.
$$

This is an equation for the complete geometry. It exists before the choice of a spectral basis, before the reconstruction of a Hilbert space, and before the introduction of creation and annihilation operators.

The three levels of the construction are:

$$
\boxed{
\text{variational dynamics}
\longrightarrow
\text{linearization at the saddle}
\longrightarrow
\text{restriction to the physical sector}.
}
$$

Confusing these levels would make a tool of linear analysis look like an additional fundamental law.

## 2. Unprojected variational equation

Let $\mathcal V$ be the real space of variations of an admissible family $\Phi(u)$, with $u\in\mathcal V$, and define

$$
S(u)=\operatorname{Re}\mathcal S_{\rm GDQ}[\Phi(u)].
$$

Suppose that the first variation is continuous and admits a Riesz representative. There exists then a field

$$
\mathcal E(u)\in\mathcal V
$$

such that

$$
DS(u)[v]
=
\langle\mathcal E(u),v\rangle
$$

for every direction $v\in\mathcal V$. The field $\mathcal E$ gathers the bulk Euler--Lagrange equations and, after fixing the variational domain, the interface momenta.

If all directions of $\mathcal V$ are allowed, stationarity

$$
DS(u_*)[v]=0
\qquad
\forall v\in\mathcal V
$$

is equivalent to

$$
\mathcal E(u_*)=0.
$$

The proof is immediate, but important. Choosing $v=\mathcal E(u_*)$,

$$
0
=
DS(u_*)[\mathcal E(u_*)]
=
\|\mathcal E(u_*)\|^2,
$$

hence $\mathcal E(u_*)=0$. The converse follows directly from the pairing.

This is the general Lagrangian dynamics. No projector appears at this stage.

## 3. Constraints and physical stationarity

In the presence of normalization, fixed charges, and gauge redundancies, not every direction of $\mathcal V$ is physical. Let

$$
\mathcal V_{\rm phys}
=
\ker D\mathcal C(u_*)\cap\mathcal G^\perp
$$

be the tangent space that preserves the linearized constraints and is orthogonal to the gauge directions. If this subspace is closed, there exists the orthogonal projector

$$
P_{\rm phys}:\mathcal V\longrightarrow\mathcal V_{\rm phys}.
$$

Restricted stationarity means

$$
DS(u_*)[v]=0
\qquad
\forall v\in\mathcal V_{\rm phys}.
$$

Using the self-adjointness of $P_{\rm phys}$,

$$
\langle\mathcal E(u_*),v\rangle
=
\langle P_{\rm phys}\mathcal E(u_*),v\rangle
$$

for all $v\in\mathcal V_{\rm phys}$. Therefore,

$$
\boxed{
DS(u_*)|_{\mathcal V_{\rm phys}}=0
\quad\Longleftrightarrow\quad
P_{\rm phys}\mathcal E(u_*)=0.
}
$$

The projector does not alter the action and does not create a new equation. It expresses that only the component tangent to the physical space needs to vanish. The normal component is balanced by the multipliers of the constraints.

## 4. The Hessian as a derivative of the dynamics

Suppose now that $\mathcal E$ is differentiable at $u_*$. Its derivative is

$$
\mathbb H_*
=
D\mathcal E(u_*)
=
D^2S(u_*).
$$

For a small perturbation $\eta$,

$$
\mathcal E(u_*+\eta)
=
\mathcal E(u_*)
+\mathbb H_*\eta
+o(\|\eta\|).
$$

Thus, the linearized equation

$$
\mathbb H_*\eta=0
$$

is not a law added to GDQ. It is the tangent approximation of the general variational equation around a stationary background.

When there are constraints implemented by multipliers, $\mathbb H_*$ must be the Hessian of the augmented functional:

$$
\mathbb H_*
=
D_X^2
\left[
S(X)-\langle\lambda,\mathcal C(X)\rangle
\right]_{(X_*,\lambda_*)}.
$$

This prevents the curvature of the constraint sheet itself from being discarded.

## 5. Restriction of the linearization

The tangent operator observed in the physical sector is

$$
K_{\rm phys}
=
P_{\rm phys}\mathbb H_*P_{\rm phys}.
$$

For a physical direction $\eta$, we have $P_{\rm phys}\eta=\eta$, hence

$$
K_{\rm phys}\eta
=
P_{\rm phys}\mathbb H_*\eta.
$$

Therefore, the input projection does not modify the physical perturbation; the output projection only removes components normal to the constraints or gauge components produced by a redundant representation.

If the Hessian preserves the physical sector,

$$
P_{\rm phys}\mathbb H_*\eta
=
\mathbb H_*\eta,
$$

then

$$
K_{\rm phys}\eta
=
\mathbb H_*\eta.
$$

In this case, the compression does not even modify the operator on its physical domain: it only makes the restriction explicit.

## 6. Where quantum operators appear

If $K_{\rm phys}$ has a self-adjoint realization, fixed boundary conditions, and a stable spectrum, we can look for normal modes:

$$
K_{\rm phys}u_j=\lambda_j u_j.
$$

A linear perturbation can be expanded in these modes. After the reconstruction of the Hilbert sector, an operator representation writes

$$
\widehat{\delta\Phi}
=
\sum_j
\left(
a_j u_j+a_j^\dagger\overline{u_j}
\right).
$$

The operators $a_j$ and $a_j^\dagger$ encode the amplitudes of the normal modes in the chosen spectral representation. They do not replace:

- the non-linear background;
- the complete variational equation;
- the formation or surgery of defects;
- the physical change of boundary conditions;
- the non-linear interaction between object and apparatus.

Consequently, operator mechanics is a linear and spectral reduction of GDQ dynamics, not its ontological origin.

## 7. What has been certified in Lean

The module [VariationalDynamics.lean](../../../formal/GDQ/VariationalDynamics.lean) certifies:

1. that the first variation is the pairing with the variational equation;
2. that unconstrained stationarity is equivalent to vanishing gradient;
3. that physical stationarity is equivalent to vanishing projected gradient;
4. that the Hessian is the Fréchet derivative of the variational equation;
5. that the restricted linearization is $P_{\rm phys}\mathbb H_*P_{\rm phys}$;
6. that on physical directions invariant under the Hessian, the compression coincides with the raw linear dynamics.

The certification is abstract and functional-analytical. For each concrete background, it is still necessary to provide:

- the domain of variations;
- the regularity of the action;
- the differentiation under integrals;
- the constraints and gauge;
- the boundary conditions;
- the self-adjointness and gap, when used.

These are conditions for applying the theorem, not alterations of the official action.

## 8. Physical meaning

The formulation allows two complementary strategies:

1. directly solve the non-linear variational equations to study backgrounds, solitons, interfaces, and transitions;
2. linearize a solution and use Hessians, projectors, and operators to study stability, spectra, and laboratory observables.

The second strategy is often more economical but remains a controlled particular case of the first.
