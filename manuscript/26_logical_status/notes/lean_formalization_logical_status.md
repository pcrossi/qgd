---
title: "Lean Formalization of the Logical Status"
---

# Lean Formalization of the Logical Status

The module [LogicalStatus.lean](../../../formal/GDQ/LogicalStatus.lean) does not introduce a physical equation. It formalizes the grammar used to prevent different categories from being confused.

## 1. Claim Classes

The `ClaimClass` type distinguishes:

1. axiom;
2. definition;
3. derivation;
4. conditional theorem;
5. effective reduction;
6. numerical evidence;
7. reverse engineering;
8. phenomenological comparison;
9. future program.

Since these classes are distinct constructors, Lean certifies, for example:

$$
\text{numerical evidence}\ne\text{axiom},
$$

$$
\text{effective reduction}\ne\text{axiom}.
$$

## 2. Axioms and Problem Data

The `CoreAxioms` record contains only:

1. official action;
2. Hermitian/Bismut class.

The `ProblemData` record separately contains:

1. causal boundary;
2. admissible topology;
3. boundary conditions;
4. metrological calibration.

This typed separation expresses an important physical decision: changing the apparatus, boundary, or calibration does not silently change the fundamental action.

## 3. Minimal Closure Chain

A strong prediction is defined by the conjunction:

$$
\begin{aligned}
&\text{official action}
\land
\text{admissible background}
\land
\text{physical Hessian}\\
&\land
\text{operator and domain}
\land
\text{boundary conditions}
\land
\text{stable spectrum}\\
&\land
\text{observable without post-fitting}.
\end{aligned}
$$

Lean proves that the absence of an admissible background or the use of post-fitting prevents classification as a strong prediction. This does not declare the result false; it merely prevents a classification stronger than the demonstrated chain.

## 4. Controlled Reduction

A reduction is controlled only when:

$$
\text{preserves the action}
\land
\text{declares the domain}
\land
\text{declares the boundary}
\land
\text{uses the physical projector}.
$$

If the action is changed, the reduction formally ceases to be a GDQ reduction. This criterion protects the manuscript against the silent import of an external ontology.

## 5. Meaning of “Zero Structural Backlog”

In the current inventory, this expression has a restricted meaning:

> the sorting of the questions does not record an unclassified structural contradiction that prevents the continuation of the program.

It does not mean:

1. that every admissible background has already been constructed;
2. that every 8D Hessian has already been diagonalized;
3. that every conditional theorem has become an unconditional theorem;
4. that every metrology or real apparatus has already been calculated.

These items remain in their proper status of conditional, reduction, refinement, or future program.
