---
title: "Operational checklist — Chapter 10"
---

# Operational checklist — Chapter 10

## 1. Statement

Show how GDQ interprets spin as circulation/torsion and, at the same time, mathematically recovers spin $1/2$, fermionic statistics, and Pauli exclusion in the correct effective sector.

## 2. Logical Status

| Block | Status | Observation |
|---|---|---|
| Circulation/torsion | GDQ interpretation | Does not replace spinor structure. |
| Spin structure of $\mathbb R^4\times T^4$ | Proven | $w_2=0$. |
| Spin $1/2$ | Structurally closed | Covering $SU(2)\to SO(3)$. |
| Residue/Hopf | Closed as geometric reading | Half-monodromy by square root. |
| Clifford/Dirac--Bismut | Effective | Reconstructed operator, not fundamental action. |
| Fermionic statistics | Conditionally closed | Lorentzian, positive and local sector. |
| Pauli | Closed in the CAR sector | Bohm barrier is manifestation. |
| Dynamic selection of spin sector | Future program | does not reopen the spin-statistics construction. |

## 3. Deductive Chain

$$
M=\mathbb R^4\times T^4
\to
w_2=0
\to
\Phi_\ast^{\rm stoma}
\to
K_{\rm phys}^{\rm spin}
\to
P_{\rm Spin}
\to
\mathrm{Spin}(3,1)
\to
\mathrm{Clifford}
\to
U(2\pi)=-I
\to
\text{CAR}
\to
\text{Pauli}.
$$

Technical construction called:

- [[notes/gdq_spin_statistics_construction|GDQ construction of spin, statistics and Pauli]]

## 4. Optional Scripts

| Script | Classification |
|---|---|
| `verify_su2_rotation.py` | Symbolic test of $2\pi$ and $4\pi$. |
| `verify_hopf_cauchy_residue.py` | Symbolic-numerical test of the $1/2$ residue. |
| `verify_exchange_holonomy.py` | Symbolic/topological test of $-1$ holonomy. |
| `verify_car_pauli.py` | Algebraic test of CAR and exclusion. |

## 5. Points that must not be forgotten

- Do not reduce spin $1/2$ to scalar circulation.
- Do not treat Dirac--Bismut as a fundamental action.
- Do not use Pauli as an independent postulate.
- Do not confuse fermionic sign with negative weight of the measure.
- Do not import the Standard Model as ontology.
