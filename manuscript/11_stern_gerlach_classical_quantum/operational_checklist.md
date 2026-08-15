---
title: "Operational Checklist — Chapter 11"
---

# Operational Checklist — Chapter 11

## 1. Statement

Explain Stern--Gerlach as a classical-quantum interaction in GDQ: the apparatus provides the field/boundary, selects the axis, separates two channels, and registers Born weights.

## 2. Logical Status

| Block | Status | Observation |
|---|---|---|
| Apparatus axis | Operational definition | $\mathbf n=\mathbf B/|\mathbf B|$. |
| Two projectors | Structurally closed | Local Hopf/Pauli. |
| Hopf--Bismut triplet | Structurally closed | The complex structure selects $SU(2)_+$; the apparatus selects a direction. |
| Deflection | Effective reduction | Fixed channel, adiabatic regime. |
| Angular weights | Operationally closed | Born from Chap. 9. |
| Incompatible sequences | Closed in the effective sector | No pre-existing table. |
| Adiabaticity | Hypothesis of validity | Transitions occur outside it. |
| Real $\mathsf R_{\rm SG}$ | Metrological program | Depends on the apparatus. |

## 3. Deductive Chain

$$
\mathcal S_{\rm GDQ}
\to
J_{\rm SG}^{\rm classical}
\to
\Phi_\ast^{\rm SG}
\to
K_{\rm phys}^{\rm SG}
\to
\mathsf R_{\rm SG}
\to
\text{spin/Hopf}
\to
\mathbf n_{\rm app}
\to
P_{\mathbf n}^{\pm}
\to
E_\pm
\to
\mathbf F_\pm
\to
\Delta z_\pm
\to
p_\pm.
$$

Technical construction named:

- [[notes/gdq_construction_stern_gerlach|GDQ Construction of Stern-Gerlach]]
- [[notes/chiral_selection_hopf_bismut|Chiral selection Hopf--Bismut]]

## 4. Scripts

| Script | Classification |
|---|---|
| `calculate_sg_weights.py` | Operational consistency test. |
| `simulate_sg_deflection.py` | Effective reduction/apparatus. |
| `test_sg_sequences.py` | Symbolic test of sequential measurements. |
| `verify_sg_hopf_bismut_triplet.py` | Verification of the self-dual Hopf triplet. |

## 5. Key Points to Remember

- Spin belongs to the object; the axis belongs to the apparatus.
- $\kappa$ is relative to $\mathbf n$.
- Trajectory in a fixed channel is deterministic; population is statistical.
- The apparatus is a boundary/source, not an alteration of the official action.
- Pauli matrices are a local representation, not a new ontology.
