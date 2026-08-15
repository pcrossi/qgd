---
title: "Proofs, lemmas and definitions — Chapter 1"
---

# Proofs, lemmas and definitions — Chapter 1

This note records what must remain associated with Chapter 1 without transforming the introduction into a technical chapter.

| Item | Method of insertion | Status |
|---|---|---|
| Difference between Feynman's oscillatory integral and Wiener's positive integral | Pedagogical explanation with minimal equations | Conceptual/demonstrative |
| Wick rotation as conditional continuation | Statement with domain and contour caveats | Conditional |
| Madelung transformation | Initial operational definition | Preparatory |
| Madelung continuity equation | Short proof or reference to Chapter 5 | Proven later |
| Bohm term as amplitude derivative | Formula and secure interpretation | Proven in the regular sector |
| Nelson/Wiener diffusion | Conditional bridge, not definitive axiom | Conditional |
| Bohm osmotic identity | Note and self-contained script | Symbolic-numerical verification |
| Wiener/Feynman contrast | Body of text and self-contained script | Pedagogical consistency test |

The local differential identity of Bohm also has complementary certification in [BohmIdentity.lean](../../../formal/GDQ/BohmIdentity.lean). The module proves, for a regular one-dimensional log-density $q$ and $R=\exp(q/2)$:

$$
\frac{R''}{R}
=
\frac{q''}{2}
+
\frac{(q')^2}{4}.
$$

It also certifies the algebraic form of the Fisher–Bohm identity. The extension with $\nabla$ and $\Delta_g$ on a Riemannian manifold remains the same human proof of Chapter 5; it has not yet been internalized in Lean.

## Do not anticipate here

- complete proof of the official action;
- proof of the polarization $\Pi_{S_R}=\rho$;
- Born rule;
- Wallstrom;
- spin;
- spectra or masses.

Chapter 1 must formulate the problem. The technical proofs enter in the chapters where their domains and hypotheses have already been defined.

## State after didactic review

The chapter already contains the minimal transitions between:

1. positive integral and oscillatory integral;
2. Wick rotation and boundary data;
3. gauge/boundary and Madelung decomposition;
4. Nelson/diffusion and the need for geometry;
5. geometric flow and the introduction of the domain of GDQ in Chapter 2.

The extensive demonstrations remain in called notes. The scripts of the chapter serve only as pedagogical verification, not as independent physical evidence.
