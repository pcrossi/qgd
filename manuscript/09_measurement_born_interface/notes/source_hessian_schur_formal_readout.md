---
title: "Classical source, Hessian, Schur and spectral readout"
status: "conditional structural theorem"
---

# Classical source, Hessian, Schur and spectral readout

## 1. Statement

Consider an admissible GDQ background $\Phi_*$ in the presence of classical data from an apparatus. After fixing constraints, gauge, domain, and boundary, let

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}
$$

be the physical Hessian and $J_{\rm app}$ the linear source produced by the apparatus. If $K_{\rm phys}$ is invertible in the relevant subspace, then

$$
\delta\Phi_{\rm app}
=
K_{\rm phys}^{-1}J_{\rm app}
$$

exactly solves

$$
K_{\rm phys}\delta\Phi_{\rm app}
=
J_{\rm app}.
$$

When internal degrees of freedom are eliminated on-shell, the boundary response is the Schur complement. If its channels form a spectral orthonormal basis and the response state is normalized, the record weights are positive and sum to one.

## 2. Classical source

The apparatus does not provide a fundamental quantum operator. It provides fields, materials, supports, and boundary conditions. In the linear approximation, its contribution appears as a source functional:

$$
\delta S_{\rm app}
=
-\langle J_{\rm app},\delta\Phi\rangle.
$$

The linearized variational equation is

$$
K_{\rm phys}\delta\Phi
-J_{\rm app}
=0.
$$

Thus, $J_{\rm app}$ is external data of the experimental problem, while $K_{\rm phys}$ continues to come from the second variation of the official action on the background with that physical domain.

## 3. Linear solution

If a physical Green's function $G_{\rm phys}$ exists such that

$$
K_{\rm phys}G_{\rm phys}=I,
$$

define

$$
\delta\Phi_{\rm app}
=
G_{\rm phys}J_{\rm app}.
$$

Then

$$
K_{\rm phys}\delta\Phi_{\rm app}
=
K_{\rm phys}G_{\rm phys}J_{\rm app}
=
J_{\rm app}.
$$

This identity does not demonstrate the existence of the Green's function. Existence requires a closed domain, boundary conditions, removal of zero modes, and control of the spectrum.

## 4. Elimination of the interior

Decompose the perturbation into boundary trace and interior:

$$
\delta\Phi
=
\begin{pmatrix}
b\\
i
\end{pmatrix},
$$

and write

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{bb}&K_{bi}\\
K_{ib}&K_{ii}
\end{pmatrix}.
$$

The homogeneous internal equation is

$$
K_{ib}b+K_{ii}i=0.
$$

If $K_{ii}^{-1}$ exists,

$$
i_*(b)
=
-K_{ii}^{-1}K_{ib}b.
$$

The boundary residue becomes

$$
\begin{aligned}
r_b(b)
&=
K_{bb}b+K_{bi}i_*(b)
\\
&=
\left(
K_{bb}
-K_{bi}K_{ii}^{-1}K_{ib}
\right)b.
\end{aligned}
$$

Therefore,

$$
\boxed{
\text{R}_{\rm app}
=
K_{bb}
-K_{bi}K_{ii}^{-1}K_{ib}.
}
$$

This operator is the effective Schur/DtN impedance. No additional coefficient was inserted to obtain it.

## 5. Record channels

After the reconstruction of the physical Hilbert space, suppose that the complexified Hessian possesses a finite orthonormal basis of channels:

$$
K_{\rm phys}\phi_i
=
E_i\phi_i.
$$

If the normalized response state is

$$
\psi_{\rm app}
=
G_{\rm phys}J_{\rm app},
\qquad
\|\psi_{\rm app}\|=1,
$$

the weight of channel $i$ is

$$
p_i
=
\left|
\langle\phi_i,\psi_{\rm app}\rangle
\right|^2.
$$

Parseval provides

$$
\sum_i p_i
=
\|\psi_{\rm app}\|^2
=1,
$$

and Cauchy--Schwarz provides

$$
0\leq p_i\leq1.
$$

Here the projectors were not inserted before the dynamics. They are the spectral representation of the channels selected by the Hessian and by the apparatus boundary.

## 6. What the isolated spectral layer does not prove

Diagonalization and Born provide channels and operational frequencies. An individual event still requires a capture dynamics. If $\mathcal B_i$ is the microscopic basin of record $i$, the closure condition is

$$
\mu_{\rm micro}(\mathcal B_i)
=
p_i.
$$

This equality does not follow solely from Parseval or the Schur complement. In the general `ApparatusBornReadout` module, the realization by basins remains a structure with this obligation explicitly visible.

In the Gaussian QND sector, the obligation is discharged separately: the normalization of likelihoods, the conservation of the expectation of the weights, and the terminal absorption imply the Born-basin equality. The human proof is in
[[born_theorem_gaussian_qnd_basins|Born-basin theorem for Gaussian QND apparatuses]].

## 7. Lean certification

The module
[ClassicalApparatusResponse.lean](../../../formal/GDQ/ClassicalApparatusResponse.lean)
proves:

1. $K_{\rm phys}^{-1}J_{\rm app}$ solves the linearized equation;
2. the internal response solves its stationary equation;
3. the boundary residue coincides exactly with the Schur complement;
4. the inversion of the reduced response solves the interface equation.

The module
[ApparatusBornReadout.lean](../../../formal/GDQ/ApparatusBornReadout.lean)
proves:

1. the response state solves the equation with source;
2. the weights of the spectral channels are non-negative;
3. the weights sum to exactly one;
4. each weight is less than or equal to one;
5. basins that realize these weights also form a normalized distribution.

The module
[QNDBornBasins.lean](../../../formal/GDQ/QNDBornBasins.lean)
additionally proves:

1. the QND condition is preserved by the Schur complement;
2. the off-diagonal blocks vanish between orthogonal projectors;
3. the normalized likelihoods produce positive and normalized posteriors;
4. the physical expectation of each posterior is exactly its initial weight;
5. the covariance is Gram, positive, and tangent to the simplex;
6. under terminal absorption, the measure of each basin is exactly the initial weight.

## 8. Status

The result is structurally closed under the stated hypotheses. The following remain conditional per apparatus:

- concrete derivation of $J_{\rm app}$;
- stationary background;
- physical Hessian and its domain;
- invertibility of the internal block;
- stable spectral basis;
- QND verification and signal separation in the concrete apparatus;
- material and environmental parameters.

These data belong to the experiment and to the application of the official action; they are not new axioms of GDQ.
