---
title: "15. Leptonic Hierarchy and Masses"
---

# 15. Leptonic Hierarchy and Masses

This chapter treats mass as the geometric cost of sustaining a material defect. In GDQ, the primary target is not to directly obtain numbers in MeV. The primary target is to obtain dimensionless ratios between physical eigenvalues.

The thesis of this chapter is:

$$
\text{mass is the geometric stiffness of a physical sector;}
$$

$$
\text{mass ratios are predictive;}
$$

$$
\text{absolute mass requires metrological calibration.}
$$

This distinction prevents circularity. Defining the electron as the scale standard does not explain its absolute mass in MeV, but allows testing whether the theory predicts $M_\mu/M_e$ and $M_\tau/M_e$.

## Roadmap

- [[15.1 - What mass means in GDQ]]
- [[15.2 - Scales, units and dimensionless ratios]]
- [[15.3 - Evolution of construction and conceptual debugging]]
- [[15.4 - Rosen-Morse as an auxiliary benchmark]]
- [[15.5 - Intrinsic sectors of leptonic tension]]
- [[15.6 - Reduced derivation of the muon ratio]]
- [[15.7 - Koide as geometric saturation and tau ratio]]
- [[15.8 - 8D Hessian and inheritance by Schur]]
- [[15.9 - Product background and warped-mixed criterion]]
- [[15.10 - Numerical comparison and scope]]

## Central Result

With $\alpha$ inherited from the global-local bridge:

$$
R_\mu
=
\frac{M_\mu}{M_e}
=
\frac32\alpha^{-1}
+
\frac65
+
2\alpha.
$$

Three-dimensional saturation imposes:

$$
\frac{1+R_\mu+R_\tau}
{(1+\sqrt{R_\mu}+\sqrt{R_\tau})^2}
=
\frac23.
$$

This yields the heavy branch:

$$
R_\tau
\simeq
3477.446405098.
$$

The result is lifted to the 8D product background by the block Hessian:

$$
H_8
=
\begin{pmatrix}
H_B & J\\
J^\dagger & H_\perp
\end{pmatrix},
\qquad
H_B^{\rm eff}
=
H_B-JH_\perp^{-1}J^\dagger.
$$

In the stationary product:

$$
J=0,
\qquad
R_\ell^{(8)}=R_\ell^{(0)}.
$$

## Status of the Result

| Block | Status | Observation |
|---|---|---|
| Mass as geometric cost | Structural GDQ interpretation | Not an inserted point mass. |
| Absolute scale | Metrological calibration | MeV requires a unit standard. |
| Rosen--Morse | Auxiliary benchmark | Not the ontology of the hierarchy. |
| Muon ratio | Closed in the intrinsic reduced model | Uses tension/topology and $\alpha$. |
| Koide-like relation | Reduced geometric theorem | Three-dimensional saturation, not an empirical formula. |
| Tau ratio | Conditionally closed in the charged triplet | Uses the stable heavy branch. |
| Fourth generation | Excluded on the reduced support $R^3$ | No fourth orthogonal projector. |
| 8D product lifting | Closed | Schur preserves ratios when $J=0$. |
| Warped/mixed | Conditional | Evaluate by Schur's criterion. |

## Editorial Control

- [[operational_checklist|Operational checklist of the chapter]]
- [[notes/proofs_lemmas_definitions|Associated proofs, lemmas and definitions]]
- [[notes/gdq_construction_leptonic_hierarchy|GDQ construction of the leptonic hierarchy]]
- [[notes/dimensional_scale_calibration|Dimensional scale and calibration]]
- [[notes/rosen_morse_auxiliary_benchmark|Rosen-Morse as an auxiliary benchmark]]
- [[notes/muon_intrinsic_tension|Muon ratio by intrinsic tension]]
- [[notes/koide_geometric_saturation|Koide as geometric saturation]]
- [[notes/perelman_reduction_3d_bulk8|Perelman 3D reduction in the 8D bulk]]
- [[notes/stationary_8d_background|Stationary 8D background of the hierarchy]]
- [[notes/8d_hessian_schur_hierarchy|8D Hessian and Schur]]
- [[notes/preserved_scripts_hierarchy|Preserved scripts of the leptonic hierarchy]]

[[../index|← Home]] | [[15.1 - What mass means in GDQ|Next →]]
