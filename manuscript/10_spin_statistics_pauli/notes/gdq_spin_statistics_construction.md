---
title: "GDQ construction of spin, statistics and Pauli"
---

# GDQ construction of spin, statistics and Pauli

## 1. Statement

Spin in GDQ begins as circulation and torsion of the defect, but it must be realized by a spinor structure in the effective sector.

The chain is:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast^{\rm stoma}
\to
\text{normal slice }\mathbb C^2
\to
S^3
\to
\operatorname{Spin}
\to
D_{B,A}
\to
\text{CAR}
\to
\text{Pauli}.
$$

## 2. Stoma background

The stoma is a defect of codimension compatible with a complex normal slice:

$$
N_{\rm normal}\simeq\mathbb C^2.
$$

The link of a small normal ball is:

$$
\partial B_\epsilon(\mathbb C^2)
\simeq
S^3.
$$

This $S^3$ carries the Hopf geometry used for circulation and orientation.

## 3. Angular Hessian and physical sector

The Hessian of the official action around the stoma separates radial, angular, and gauge modes. The physical sector is:

$$
K_{\rm phys}^{\rm spin}
=
P_{\rm phys}^{\dagger}
K_{\rm GDQ}^{\rm stoma}
P_{\rm phys}.
$$

The non-trivial angular fluctuations of the link $S^3$ produce the effective spinor sector.

More explicitly, we write an admissible perturbation of the background as:

$$
\Phi
=
\Phi_\ast
+
\delta\Phi,
\qquad
\delta\Phi
=
\delta\Phi_{\rm phys}
+
\delta\Phi_{\rm gauge}
+
\delta\Phi_{\rm constr}.
$$

The second variation defines the quadratic form:

$$
\left.\delta^2\mathcal S_{\rm GDQ}\right|_{\Phi_\ast}
(\delta\Phi,\delta\Phi)
=
\langle \delta\Phi,K_{\rm GDQ}^{\rm stoma}\delta\Phi\rangle.
$$

The projector $P_{\rm phys}$ removes gauge modes, normalization variations, and directions that violate charge and flux constraints. Thus:

$$
\delta\Phi_{\rm phys}
=
P_{\rm phys}\delta\Phi,
$$

and only the reduced quadratic form:

$$
\langle \delta\Phi_{\rm phys},
K_{\rm phys}^{\rm spin}\delta\Phi_{\rm phys}\rangle
$$

is used to identify observable degrees of freedom. The spinor operator below is, therefore, the effective operator representing the action of $K_{\rm phys}^{\rm spin}$ on the angular half-monodromy subspace. It is not postulated as a new fundamental dynamics.

## 4. Effective spinor operator

The operator that appears is not a new fundamental action. It is the spinor linearization of the projected Hessian:

$$
D_{B,A}
=
\gamma^a
\left(
\nabla_a
+
\frac18H_{abc}\gamma^{bc}
+
A_a
\right).
$$

It acts on:

$$
\psi\in\Gamma(S\otimes E).
$$

## 5. Rotation and exchange

The spin structure provides the covering:

$$
SU(2)\to SO(3).
$$

A rotation of $2\pi$ acts as:

$$
U(2\pi)=-I.
$$

The exchange of two fermions is a holonomy in the reduced configuration space. In the Lorentzian, positive, and graded-local sector, it imposes fermionic statistics.

## 6. CAR and Pauli

The effective operators obey:

$$
\{a_i,a_j^\dagger\}
=
\delta_{ij},
\qquad
\{a_i^\dagger,a_j^\dagger\}=0.
$$

Hence:

$$
(a_i^\dagger)^2=0.
$$

This is Pauli. The Bohm barrier is the geometric manifestation of exclusion in the fluid, not the primary algebraic proof.

## 7. Limitation

The complete dynamical selection of which spinor sector appears in every material background is a future program. The current closure is structural in the regular local sector.

## 8. Preserved computational verification

The computational tests of the chapter do not calculate a new material spectrum. They verify, in a self-contained manner, three structural identities used in the text:

1. the $SU(2)$ lift of spatial rotations yields $U(2\pi)=-I$ and $U(4\pi)=I$;
2. an odd circulation of $\pi\hbar$ produces $-1$ holonomy;
3. the finite exterior algebra realizes the CAR and implies $(a_i^\dagger)^2=0$.

The outputs are recorded in `scripts/output_*.md` and serve as symbolic verification, not as phenomenological fitting.
