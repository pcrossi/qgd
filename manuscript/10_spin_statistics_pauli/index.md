---
title: "10. Spin, circulation, statistics and Pauli"
---

# 10. Spin, circulation, statistics and Pauli

In GDQ, spin is not treated as a point particle spinning on its own axis.
The correct physical image is that of circulation, holonomy, and torsion of an extended geometric defect. However, this image does not replace the mathematical structure necessary for half-integer spin.

The central point of this chapter is:

$$
\text{circulation manifests spin;}
\qquad
\text{the spinor structure realizes spin.}
$$

Therefore, the chapter follows two layers. First, it presents the GDQ reading: vorticity, stoma, Hopf, residues, and torsion. Then, it shows the mathematical closure in the effective sector: spin structure, Clifford algebra, spinor operator, $2\pi\mapsto -1$ transformation, fermionic statistics, and Pauli exclusion.

## Outline

- [[10.1 - What spin means in GDQ]]
- [[10.2 - Circulation, defects and torsion]]
- [[10.3 - Why scalar circulation is not enough]]
- [[10.4 - Spin structure and double covering]]
- [[10.5 - Clifford algebra and effective spinor operator]]
- [[10.6 - Rotation of 2pi and 4pi]]
- [[10.7 - Exchange, holonomy and fermionic sign]]
- [[10.8 - CAR, graded locality and positive energy]]
- [[10.9 - Pauli exclusion as a node and geometric barrier]]
- [[10.10 - Scope and limitations of the chapter]]

## Central Result

The logical chain of the chapter is:

$$
\text{geometric defect}
\to
\text{circulation/Hopf/torsion}
\to
\text{spin structure}
\to
\text{Clifford}
\to
\text{representation of }\mathrm{Spin}(3,1)
\to
\text{CAR}
\to
\text{Pauli}.
$$

The effective spinor sector uses:

$$
\psi\in\Gamma(S\otimes E),
$$

with:

$$
\text{\{}\gamma^a,\gamma^b\text{\}}=2\eta^{ab}I.
$$

A spatial rotation of $2\pi$ acts on the spinor lift as:

$$
U(2\pi)=-I,
$$

and a rotation of $4\pi$ returns:

$$
U(4\pi)=I.
$$

For half-integer spin fields in the Lorentzian, positive, and graded-local effective sector, the correct statistics is fermionic:

$$
\text{\{}\widehat\psi_\alpha(t,\mathbf x),
\widehat\psi_\beta^\dagger(t,\mathbf y)\text{\}}
=
\delta_{\alpha\beta}\delta^{(3)}(\mathbf x-\mathbf y).
$$

From CAR, it immediately follows:

$$
(a_i^\dagger)^2=0.
$$

This is the Pauli exclusion principle.

## Status of the Result

| Block | Status | Observation |
|---|---|---|
| Spin as circulation/torsion | GDQ interpretation preserved | Does not replace spin bundle. |
| Spin $1/2$ | Structurally closed | Via spin structure and double covering. |
| Residue/Hopf | Compatible geometric reading | Explains half-monodromy. |
| Spinor operator | Effective/reconstructed | Not a fundamental action. |
| Fermionic statistics | Conditionally closed | Lorentzian, spinor, positive energy, and graded locality sector. |
| Pauli | Closed in the CAR sector | Bohm barrier is a geometric manifestation. |
| Dynamic selection of spin sector | Future program | Does not reopen the effective structure. |

## Editorial Control

- [[operational_checklist|Operational checklist of the chapter]]
- [[notes/proofs_lemmas_definitions|Associated proofs, lemmas and definitions]]
- [[notes/gdq_spin_statistics_construction|GDQ construction of spin, statistics and Pauli]]
- [[notes/spin_structure_in_R4_T4|Spin structure in $\mathbb R^4\times T^4$]]
- [[notes/rotation_2pi_4pi_su2|Rotation of $2\pi$ and $4\pi$ in $SU(2)$]]
- [[notes/spin_hopf_cauchy_residue|Spin, Hopf and Cauchy residue]]
- [[notes/fermionic_exchange_holonomy|Fermionic exchange holonomy]]
- [[notes/conditional_spin_statistics_theorem|Conditional spin-statistics theorem in GDQ]]
- [[notes/pauli_car_bohm_barrier|Pauli, CAR and Bohm barrier]]

[[../index|← Home]] | [[10.1 - What spin means in GDQ|Next →]]
