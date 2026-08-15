---
title: "Proof of circulation quantization by U(1) bundle"
---

# Proof of circulation quantization by $U(1)$ bundle

This note records the technical proof used in Sections 08.5 and 08.6.

The goal is to show that the integrality of circulation is not an external postulate of Madelung/Nelson and does not come from the Poisson summation. It comes from the global existence of the physical phase as a section of a Hermitian line bundle.

## 1. Regular Sector Data

Consider a regular GDQ sector in which:

1. the density is positive outside the nodal set;
2. the local phase $S_R$ is smooth in each chart;
3. the reconstructed state is admissible as a global section of the physical sector;
4. the physical domain removes the density nodes.

We define:

$$
Z_\rho=\{x:\rho(x)=0\},
\qquad
M^\ast=M\setminus Z_\rho.
$$

On $M^\ast$, the amplitude $\sqrt\rho$ is non-zero. Therefore, the phase is well-defined as an angular variable:

$$
\chi=\frac{S_R}{\hbar}.
$$

The physical phase function is not an arbitrary global real function $\chi:M^\ast\to\mathbb R$. The physical function is:

$$
e^{i\chi}:M^\ast\to S^1.
$$

This difference is the central point.

## 2. Local Form of the State

If $L\to M^\ast$ is a Hermitian line bundle, in each chart $U_a\subset M^\ast$ we choose a local unitary section $s_a$ and write:

$$
\Psi_a
=
\sqrt\rho\,e^{i\chi_a}s_a.
$$

On an intersection $U_a\cap U_b$, the local sections are related by a transition function:

$$
s_a=g_{ab}s_b,
\qquad
g_{ab}:U_a\cap U_b\to U(1).
$$

Since $\Psi$ is a global section, we must have:

$$
\Psi_a=\Psi_b.
$$

Thus:

$$
\sqrt\rho\,e^{i\chi_a}s_a
=
\sqrt\rho\,e^{i\chi_b}s_b.
$$

Since $\rho>0$ on $M^\ast$:

$$
e^{i\chi_a}g_{ab}
=
e^{i\chi_b}.
$$

Writing:

$$
g_{ab}=e^{i\lambda_{ab}},
$$

we have:

$$
\chi_b-\chi_a
=
\lambda_{ab}
\pmod{2\pi}.
$$

Therefore, the local phase can change across charts by angular functions, but the global object $e^{i\chi}$ remains well-defined.

## 3. Cocycle and Integrality

On a triple intersection $U_a\cap U_b\cap U_c$, the transition functions must satisfy the cocycle condition:

$$
g_{ab}g_{bc}g_{ca}=1.
$$

In phases:

$$
\lambda_{ab}+\lambda_{bc}+\lambda_{ca}
=
2\pi n_{abc},
\qquad
n_{abc}\in\mathbb Z.
$$

The integers $n_{abc}$ represent the global topological obstruction. They define the first Chern class:

$$
c_1(L)\in H^2(M^\ast,\mathbb Z).
$$

If $A$ is a unitary connection on $L$ and $F_A=dA$ is its local curvature, then:

$$
c_1(L)
=
\left[
\frac{F_A}{2\pi}
\right]
\in
H^2(M^\ast,\mathbb Z).
$$

Consequently, for any closed 2-cycle $\Sigma$:

$$
\frac1{2\pi}
\int_\Sigma F_A
\in
\mathbb Z.
$$

This is the global form of the quantization.

## 4. Circulation in a Closed Loop

Now consider a closed loop $C\subset M^\ast$.

If $C$ is in a single chart and the phase is written locally, then:

$$
\oint_C d\chi
=
\chi(2\pi)-\chi(0).
$$

Since the physical quantity is $e^{i\chi}$, upon completing the loop we must have:

$$
e^{i\chi(2\pi)}
=
e^{i\chi(0)}.
$$

Thus:

$$
\chi(2\pi)-\chi(0)=2\pi N,
\qquad
N\in\mathbb Z.
$$

Therefore:

$$
\frac1{2\pi}\oint_Cd\chi=N.
$$

Multiplying by $\hbar$:

$$
\oint_CdS_R
=
2\pi\hbar N
=
Nh.
$$

This is exactly the quantum circulation condition.

## 5. Why Non-Integer Circulation is Not a Global State

Suppose one attempts to write:

$$
\chi(\theta)=\alpha\theta
$$

on an angular loop $\theta\sim\theta+2\pi$.

Then:

$$
e^{i\chi(\theta+2\pi)}
=
e^{i\alpha(\theta+2\pi)}
=
e^{i\alpha\theta}e^{i2\pi\alpha}.
$$

For this to represent the same physical point of $S^1$ after one turn:

$$
e^{i2\pi\alpha}=1.
$$

This implies:

$$
\alpha\in\mathbb Z.
$$

If $\alpha\notin\mathbb Z$, the expression does not define a regular global map $S^1\to S^1$. It can be written locally on an open interval, but does not close on the loop.

Thus, non-integer circulation is not a global physical state of the sector. It is a local expression that fails the gluing condition.

## 6. Correct Role of the Poisson Summation

The identity:

$$
\sum_{m\in\mathbb Z}e^{im\epsilon}
=
2\pi
\sum_{n\in\mathbb Z}\delta(\epsilon-2\pi n)
$$

is true as a distribution.

But it already presupposes:

$$
m\in\mathbb Z.
$$

Therefore, it does not prove that the sectors are integer. It only expresses the harmonic analysis after the phase group has already been identified as $S^1$.

The foundation is:

$$
\text{global phase }S^1
\quad\Longrightarrow\quad
\text{integer characters}
\quad\Longrightarrow\quad
\text{Poisson summation}.
$$

Not the reverse.

## 7. Relationship with GDQ

In GDQ, the phase comes from:

$$
S_R
=
\frac{\hbar}{2i}(f-\bar f).
$$

Locally, the Madelung equations use $S_R$ as a phase potential. Globally, however, the admissible physical sector requires that:

$$
e^{iS_R/\hbar}
$$

be a well-defined global section.

Thus, GDQ does not need to add an external single-valuedness condition on the wavefunction. It requires global geometric admissibility of the reconstructed state.

The condition:

$$
\oint_CdS_R=Nh
$$

is a consequence of this admissibility.

## 8. Limitations of the Proof

This proof closes Wallstrom in the regular scalar sector with a $U(1)$ phase.

It does not replace:

- the construction of antiperiodic spinorial sectors;
- the proof of spin as circulation/Hopf;
- the fermionic statistics;
- the spin response to apparatuses;
- the analysis of states with singular nodes beyond the removal of $Z_\rho$.

These topics require their own structures.

## 9. Conclusion

The quantization of circulation follows from the chain:

$$
\rho>0\text{ on }M^\ast
\to
e^{iS_R/\hbar}:M^\ast\to S^1
\to
\Psi\in\Gamma(L)
\to
g_{ab}:U_a\cap U_b\to U(1)
\to
c_1(L)\in H^2(M^\ast,\mathbb Z)
\to
\frac1{2\pi}\oint_C d(S_R/\hbar)\in\mathbb Z.
$$

Therefore:

$$
\boxed{
\oint_CdS_R=Nh,
\qquad
N\in\mathbb Z.
}
$$
