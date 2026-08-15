---
title: "Proofs, lemmas and definitions — Chapter 10"
---

# Proofs, lemmas and definitions — Chapter 10

## 0. GDQ construction of the problem

Status: structural chain from defect to CAR/Pauli.

Note:

[[gdq_spin_statistics_construction|GDQ construction of spin, statistics and Pauli]]

## 1. Spin structure

Status: proven for the official local bulk.

Note:

[[spin_structure_in_R4_T4|Spin structure in $\mathbb R^4\times T^4$]]

## 2. Double covering and rotation

Status: structural theorem.

Note:

[[rotation_2pi_4pi_su2|Rotation of $2\pi$ and $4\pi$ in $SU(2)$]]

## 3. Hopf, residue and half-monodromy

Status: compatible geometric reading.

Note:

[[spin_hopf_cauchy_residue|Spin, Hopf and Cauchy residue]]

## 4. Fermionic exchange

Status: geometric interpretation of antisymmetry.

Note:

[[fermionic_exchange_holonomy|Fermionic exchange holonomy]]

## 5. Pauli

Status: algebraic theorem in the CAR sector.

Note:

[[pauli_car_bohm_barrier|Pauli, CAR and Bohm barrier]]

Complementary Lean certification:
[CARPauli.lean](../../../formal/GDQ/CARPauli.lean). The module proves abstractly, in a linear operator space of characteristic zero, that

$$
a_i^\dagger a_i^\dagger
+
a_i^\dagger a_i^\dagger
=0
$$

implies

$$
(a_i^\dagger)^2=0.
$$

It also proves that an antisymmetric wavefunction satisfies $\Psi(x,x)=0$. The module assumes the CAR; it does not claim they are derived outside the hypotheses of the spin-statistics theorem below.

## 6. Spin-statistics

Status: conditional theorem in the physical effective sector.

Hypotheses:

1. physical Lorentzian spacetime $(N,h)$;
2. spin structure;
3. positive inner product;
4. positive energy;
5. common causal cone;
6. graded locality.

Conclusion:

$$
\text{half-integer spin}
\longrightarrow
\text{fermionic statistics}.
$$

Complete note:

[[conditional_spin_statistics_theorem|Conditional spin-statistics theorem in GDQ]]

Lean certification of the logical interface:
[SpinStatisticsConditional.lean](../../../formal/GDQ/SpinStatisticsConditional.lean).
The module types separately the Lorentzian sector, spin structure, half-integer spin, common causal cone, positivity of the inner product and energy, locality of even observables, and graded locality. A realization of the relativistic bridge produces CAR and, by the `CARPauli` module, Pauli exclusion.

Limit: Lean certifies the conditional composition and its algebraic consequence; the complete analytical proof of the relativistic spin-statistics theorem remains the external result applied under these hypotheses.
