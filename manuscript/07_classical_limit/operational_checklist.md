---
title: "Operational checklist — Chapter 7"
---

# Operational checklist — Chapter 7

This checklist records the status of Chapter 7, dedicated to the classical limit and the correspondence principle in QGD.

The chapter must remain educational, but without selling the classical limit as a formal replacement $\hbar\to0$. The constant $\hbar$ does not vanish. What becomes small is a dimensionless ratio between the reduced de Broglie wavelength and the scale of variation of the density.

## 1. Chapter statement

In the regular Madelung sector selected in Chapters 5 and 6, with

$$
p_\rho=0,
\qquad
\Pi_{S_R}=\sqrt h\,\rho,
$$

we define

$$
\varepsilon_{\rm cl}
=\frac{\hbar}{pL_\rho}.
$$

When $\varepsilon_{\rm cl}\ll1$, far from nodes, sharp boundaries, and caustics, the Bohm term is subdominant:

$$
\frac{|Q_B|}{T_{\rm cl}}
=O(\varepsilon_{\rm cl}^2).
$$

Thus, Hamilton–Jacobi–Bohm reduces to classical Hamilton–Jacobi; its characteristics yield Hamilton/Newton equations; continuity induces Liouville's equation in the monokinetic ensemble.

## 2. Logical status

| Block | Status | Observation |
|---|---|---|
| Hamilton–Jacobi limit | Conditionally closed | Holds in the regular Madelung sector with $\varepsilon_{\rm cl}\ll1$. |
| Hamilton/Newton characteristics | Demonstrated in the sector | Follows from the limit Hamilton–Jacobi equation. |
| Liouville | Demonstrated before caustics | After caustics, requires multiple branches or general measure. |
| WKB/stationary phase | Effective correspondence | Checks with the usual form, but does not replace the QGD derivation. |
| Cotangent $\to$ Kepler | Demonstrated as local limit | Coupling normalization remains sectoral. |
| Classical Noether | Conditionally demonstrated | Conserved if reduction and boundary preserve the symmetry. |
| Macroscopic Maxwell | Conditionally closed | The form $F=dA$ and the source equation come from the effective $U(1)_Q$ sector. |
| Macroscopic Einstein/Newton | Conditionally closed | Classical metric form requires torsional average and hydrodynamic closure. |

## 3. Scalar deductive chain

The scalar chain of the chapter is:

$$
\mathcal S_{\rm QGD}
\to
\text{Madelung sector}
\to
(\rho,S_R)
\to
\text{Hamilton–Jacobi–Bohm}
\to
\varepsilon_{\rm cl}\ll1
\to
\text{Hamilton–Jacobi}
\to
\text{Hamilton/Newton}
\to
\text{Liouville}.
$$

The chapter does not re-prove the Madelung polarization. This selection belongs to Chapters 5 and 6.

## 4. Points that must remain explicit

- The classical limit is not $\hbar=0$.
- QGD is not ontologically reduced to usual quantum mechanics.
- The Schrödinger/WKB form is an effective representation of the Madelung sector.
- The single classical trajectory requires additional localization in phase space; the natural limit is first an ensemble.
- Nodes, sharp boundaries, caustics, stomata cores, and torsional regions can invalidate the simple scalar limit.
- Torsion does not need to vanish in experiments sensitive to spin, polarization, vorticity, or boundaries.
- Maxwell and Einstein appear as macroscopic sectoral correspondences, not as new fundamental actions.

## 5. Incorporated historical content

The preservation map records the incorporation of the historical material:

[[preservation_map|Preservation map of Chapter 7]]

The following were preserved and corrected:

- relative vanishing of the Bohm term;
- Hamilton–Jacobi and Newton;
- Liouville and ensemble;
- WKB and stationary phase;
- global cotangent potential and local Kepler limit;
- classical Noether;
- Maxwell correspondence;
- metric Einstein/Newton correspondence;
- caveat regarding $g-2$ and mesons as future phenomenology, not as a proof of the classical limit.

## 6. Notes and long calculations

The main body must remain educational. Long proofs can be kept in the notes:

- [[../notes/classical/Energy-momentum tensor via Hessian of f]];
- [[../notes/classical/Dimensional analysis of gravitational coupling]].

These notes preserve long calculations without inflating the main educational path.

## 7. Recommended optional scripts

The chapter's scripts must be self-contained and classified as educational verifications. They do not calculate new fundamental constants.

Recommended folder:

`manuscript/07_classical_limit/scripts/`

with:

| Script | Function |
|---|---|
| `verify_bohm_epsilon_cl.py` | Numerically shows $|Q_B|/T_{\rm cl}\sim\varepsilon_{\rm cl}^2$. |
| `verify_hamilton_newton.py` | Verifies that Hamilton's characteristics reproduce Newton's equations for a test potential. |
| `verify_monokinetic_liouville.py` | Verifies the conservation of a transported density before caustics. |
| `verify_cotangent_kepler.py` | Shows the local limit of the cotangent potential to $1/r$. |
| `verify_classical_noether.py` | Tests conservation of energy and angular momentum in systems with preserved symmetries. |

## 8. Extensions that do not reopen the chapter

The following are not internal gaps in Chapter 7:

- metrological derivation of $\alpha$;
- final derivation of $G$;
- response of real apparatuses;
- Lamb shift, hyperfine structure, or magnetic anomalies;
- complete particle sector;
- proof of all admissible backgrounds.

These problems use classical or macroscopic correspondences, but belong to their own chapters and sectoral appendices.

## 9. Closure criteria

Chapter 7 is ready when:

1. the scalar limit is formulated in terms of $\varepsilon_{\rm cl}$;
2. the regularity and domain hypotheses are placed near the equations;
3. Hamilton/Newton and Liouville equations are presented as consequences;
4. WKB is treated as an effective verification, not a foundation;
5. Maxwell and Einstein are presented as sectoral correspondences;
6. continuous normalizations are separated from classical forms;
7. the historical material is preserved without reintroducing unproven statements.

## Educational review of 2026-07-19

Chapter 7 was checked during the scientific/educational review phase. The main body was cleaned of unnecessary historical language: the vector and metric correspondence sections now present the constructions in a positive and self-contained manner, without depending on the reader knowing previous versions of the text.

The chapter's scripts must remain as educational verifications: scale of the Bohm term, Hamilton–Newton, monokinetic Liouville, cotangent–Kepler potential, and classical Noether. They verify correspondence steps and are not metrological predictions.
