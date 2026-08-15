---
title: "11. Stern-Gerlach and classical--quantum interaction"
---

# 11. Stern-Gerlach and classical--quantum interaction

Stern--Gerlach is the first experiment in which GDQ's measurement theory can be seen in a concrete form. The object already possesses circulation and a spinorial sector; the apparatus does not create spin. The apparatus provides a classical field, selects an axis, and transforms the internal orientation into two spatially separated channels.

The central idea is:

$$
\text{spin belongs to the object;}
\qquad
\text{the axis belongs to the apparatus.}
$$

Therefore, the label $\kappa=\pm1$ must never be read as a simultaneous absolute value for all axes. It is relative to the local direction of the field:

$$
\mathbf n(\mathbf x)=\frac{\mathbf B(\mathbf x)}{|\mathbf B(\mathbf x)|}.
$$

## Roadmap

- [[11.1 - What the experiment actually requires]]
- [[11.2 - The soliton with circulation before measurement]]
- [[11.3 - The apparatus as source and magnetic boundary]]
- [[11.4 - Hopf, apparatus axis and two projectors]]
- [[11.5 - Force and deflection of center of mass]]
- [[11.6 - Angular probabilities and operational Born]]
- [[11.7 - Sequential measurements and axis incompatibility]]
- [[11.8 - Adiabatic condition and transitions between channels]]
- [[11.9 - What remains for metrology of real devices]]

## Central Result

The GDQ chain for Stern--Gerlach is:

$$
J_{\rm app}^{\rm magnetic}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm SG}
\to
P_{\mathbf n}^{\pm}
\to
\text{two beams}
\to
\text{register}.
$$

The two channel projectors are:

$$
P_{\mathbf n}^{\pm}
=
\frac12
\left(I\pm\mathbf n\cdot\sigma\right).
$$

For preparation $\mathbf a$, the weights are:

$$
p_\pm(\mathbf n|\mathbf a)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

In a fixed channel, the deflection is mechanical:

$$
\Delta z
=
\kappa
\frac{\mu L^2}{2mv_y^2}
\frac{\partial B_z}{\partial z}.
$$

Thus, the experiment is split into two problems:

1. channel dynamics, which is mechanical and geometric;
2. population of the channels, which is operational Born in the reconstructed Hilbert space.

## Status of the Result

| Block | Status | Observation |
|---|---|---|
| Two channels | Structurally closed | Hopf/apparatus axis projectors. |
| Hopf--Bismut triplet | Structurally closed | Complex orientation selects the self-dual sector; apparatus selects direction. |
| Deflection in a fixed channel | Classical effective reduction | Uses field and gradient of the apparatus. |
| Angular weights | Operationally closed | Born in the reconstructed Hilbert space. |
| Sequential measurements | Closed in the effective sector | Incompatible axes do not reveal a pre-existing table. |
| Apparatus as source/boundary | Structural | Does not alter the official action. |
| Adiabatic condition | Necessary | Outside of it, transitions occur between channels. |
| Real metrology | Applied program | Requires $\mathsf R_{\rm SG}$, material, geometry, and causal mobility. |

## Editorial Control

- [[operational_checklist|Operational checklist of the chapter]]
- [[notes/proofs_lemmas_definitions|Associated proofs, lemmas, and definitions]]
- [[notes/gdq_construction_stern_gerlach|GDQ Construction of Stern-Gerlach]]
- [[notes/classical_source_noether_zeeman_sg|Classical source and Noether--Zeeman]]
- [[notes/hopf_derivation_sg_projectors|Hopf derivation of Stern-Gerlach projectors]]
- [[notes/chiral_selection_hopf_bismut|Chiral selection Hopf--Bismut]]
- [[notes/force_deflection_sg_reduced_sector|Force and deflection in the reduced sector]]
- [[notes/born_weights_sg|Born weights in Stern-Gerlach]]
- [[notes/adiabatic_condition_sg|Adiabatic condition]]
- [[notes/background_hessian_and_dtn_sg|Background, Hessian, and DtN in Stern-Gerlach]]
- [[notes/numeric_audit_sg|Numeric audit of Stern-Gerlach]]

[[../index|← Home]] | [[11.1 - What the experiment actually requires|Next →]]
