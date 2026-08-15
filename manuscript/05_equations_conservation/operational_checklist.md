---
title: "Operational checklist — Chapter 5"
---

# Operational checklist — Chapter 5

This checklist follows the methodological protocol of Chapter 27.

The chapter must be pedagogical: open the first variation of the official action and show which equations follow directly from it, without turning QGD into ordinary quantum mechanics.

## 1. Objective of the chapter

Chapter 5 must demonstrate:

1. how the variation of $\mathcal U\mathcal L_0dV_g$ should be performed;
2. how $f$ is rewritten in terms of $\rho$ and $S_R$;
3. why the variation in phase produces a conserved current;
4. why the variation in density produces the Bohm operator;
5. why the metric variation produces a weighted equation, not Einstein renamed;
6. how Noether appears explicitly;
7. how the boundary momenta enter;
8. what is direct from the official action and what depends on the physical reconstruction;
9. why $\Pi_{S_R}=\rho$ is not a universal off-shell identity.

Chapter status: **closed for the first bulk variation and conditional for laboratory canonical dynamics**.

## 2. Main body status

| Section | Status | Observation |
|---|---|---|
| `05.1` | ready in first version | Explains product rule, integration by parts, and bulk/boundary separation. |
| `05.2` | ready in first version | Rewrites the action in $\rho$ and $S_R$. |
| `05.3` | ready in first version | Derives phase current and flux conservation. |
| `05.4` | ready in first version | Derives amplitude/Bohm operator and HJ-Bohm as reduction. |
| `05.5` | ready in first version | Derives weighted metric equation. |
| `05.6` | ready in first version | Proves Noether and discusses constraints/boundaries. |
| `05.7` | conditionally ready | Separates what was demonstrated from subsequent canonical reconstruction. |

## 3. Called notes and logical function

| Note | Function |
|---|---|
| `Derivation of the phase current` | Compact calculation of the variation in $S_R$. |
| `From amplitude energy to the Bohm term` | Variational identity that recognizes the Bohm operator in physical reduction. |
| `Audit of the canonical term rho d_t S_R` | Shows that $\Pi_{S_R}=\rho$ is not a universal off-shell identity of the official action. |
| `First variation of the QGD action - complete structure` | Global algebraic support for the first variation. |
| `Well-posedness of the GDQ geometric flow in gauge` | Demonstrates strong parabolicity, local existence, uniqueness, continuous dependence, and continuation of the flow in $\tau$ after gauge. |

Evaluation: the notes support the strong assertions and preserve the distinction between QGD bulk and the Madelung sector.

## 4. Incorporated consolidated results

The chapter incorporates, in a self-contained form, the following technical blocks:

1. conservation of the phase current;
2. Hamilton–Jacobi–Bohm equation as a reduction of the density sector;
3. weighted metric variation;
4. constitutive relationship between $\rho$ and $\mathcal U$;
5. decomposition of the complex field into phase and density;
6. distinction between QGD bulk and Madelung representation;
7. diffusion and flow as reduction language, not as a substitute action;
8. analysis of the canonical term $\rho\,\partial_tS_R$;
9. local well-posedness of the geometric flow in $\tau$ after gauge.

Main notes called by the chapter:

- [[../notes/equations/index|Equations of motion and conservation laws]];
- [[../notes/action/First variation of the QGD action - complete structure|First variation of the QGD action — complete structure]].

## 5. Direct results of the official action

Directly demonstrated:

1. the transformation $f\leftrightarrow(\rho,S_R)$ in the sector $\rho>0$;
2. $\delta_{S_R}\mathcal U=0$;
3. $\delta_\rho\mathcal U=\mathcal U\,\delta\rho/\rho$;
4. phase current:

$$
\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U g^{\mu\bar\nu}\partial_{\bar\nu}S_R;
$$

5. on-shell conservation:

$$
\nabla_\mu\widehat J_S^\mu=0;
$$

6. density equation with ratio $\Delta_g\sqrt\rho/\sqrt\rho$;
7. weighted metric equation with derivatives of $\mathcal U$;
8. off-shell Noether identity;
9. normal momenta and boundary conditions originating from the variation itself.

## 6. Conditional or reduced results

Depend on physical reconstruction:

1. identification of the laboratory local continuity equation;
2. kinetic normalization with physical mass;
3. canonical term $\rho\partial_tS_R$;
4. condition $\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}$;
5. complete canonical Madelung form;
6. operational probabilistic interpretation of measured events.

The canonical condition requires a physical polarization:

$$
p_\rho=0,
\qquad
\Pi_{S_R}=\sqrt h\rho.
$$

This polarization does not alter the official action. It selects the ordinary hydrodynamic physical sector within the larger space of QGD data.

## 7. What should not be asserted in this chapter

Do not assert that:

1. QGD is just quantum mechanics in Madelung variables;
2. $\Pi_{S_R}=\rho$ holds off-shell;
3. Perelman alone selects the canonical sector;
4. the Bohm equation in the laboratory is complete without the global–local bridge;
5. every solution of the official action is observable matter;
6. apparatus constraints can be inserted without a variational declaration.

## 8. Numerical and symbolic scripts

Mandatory scripts for closing Chapter 5: **none**.

Reason: the chapter is variational and analytical. The most useful checks are symbolic or illustrative.

Optional scripts created in [[scripts/README|scripts/]]:

1. [[scripts/verify_phase_current_1d.py|verify_phase_current_1d.py]]  
   Verify on a 1D grid that a constant current satisfies zero divergence and that lateral flux changes the integrated charge.

2. [[scripts/verify_bohm_fisher_variation.py|verify_bohm_fisher_variation.py]]  
   Numerically check the variation of the Fisher energy and the operator $\Delta\sqrt\rho/\sqrt\rho$.

3. [[scripts/verify_noether_phase_shift.py|verify_noether_phase_shift.py]]  
   Illustrate that a Lagrangian dependent only on $\partial S_R$ is invariant under $S_R\mapsto S_R+S_0$.

4. [[scripts/verify_canonical_polarization_toy.py|verify_canonical_polarization_toy.py]]  
   Show the Cauchy–Schwarz/Routh saturation for $\Pi=(Q_S/N_\rho)\rho$ in a positive toy model.

5. [[scripts/verify_parabolic_symbol_qgd.py|verify_parabolic_symbol_qgd.py]]  
   Verify pointwise that the principal symbol in gauge is $\sigma_{\rm pr}(\xi)=|\xi|_g^2I$ and is positive for a Riemannian metric.

Classification: symbolic test/pedagogical illustration, not physical prediction.

## 9. Pedagogical points to review in the final reading

Before considering Chapter 5 editorially ready:

1. ensure that long derivations remain readable;
2. verify that each equation has a nearby hypothesis;
3. clearly separate "QGD bulk" from "Madelung laboratory";
4. reinforce that boundaries are part of the variation;
5. maintain the result $\Pi_{S_R}\ne\rho$ off-shell as a point of rigor, not as an insoluble problem;
6. connect what remains conditional to Chapter 6 and measurement theory;
7. check links and Quartz rendering.

## 10. Operational verdict

Chapter 5 is **structurally assembled and mathematically central**.

It closes:

1. phase current;
2. density/Bohm operator in the bulk;
3. weighted metric equation;
4. Noether;
5. role of boundaries.

It leaves conditional:

1. the canonical Madelung term;
2. the laboratory physical polarization;
3. the dynamic/operational selection of the measured sector.

These conditions are treated in the global–local bridge and in measurement theory, without reopening the first variation of the official action.

## Didactic review of 2026-07-19

Chapter 5 was checked in the scientific/didactic review phase. The checklist was adjusted to remove historical traceability dependencies: technical blocks now appear as results incorporated into the manuscript rather than external references. The internal index [[../notes/equations/index|Equations of motion and conservation laws]] was created, which lists the called notes on phase current, Bohm term, and canonical polarization.

The five scripts of the chapter must remain as pedagogical verifications: 1D phase current, Fisher–Bohm variation, global phase symmetry, and canonical toy polarization. None of them is a metrological prediction.
