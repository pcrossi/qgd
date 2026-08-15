---
title: "Note — Lean Formalization of the Technical FAQ"
---

# Note — Lean Formalization of the Technical FAQ

The module [`TechnicalFAQ.lean`](../../../formal/GDQ/TechnicalFAQ.lean) certifies logical distinctions used in this chapter. It imports the logical status taxonomy and the numerical protocol, but does not create new physical dynamics.

## 1. Conditional Result

`ConditionalResult H R` is defined as $H\Rightarrow R$. The theorem `conditionalResult_apply` only delivers $R$ after receiving a proof of $H$. Thus, a declared hypothesis does not disappear when the result is reused.

## 2. Numerical Agreement

The theorem `numericalAgreement_does_not_close_missing_background` shows that a numerical agreement, even if accepted as a proposition, does not complete the strong chain if an admissible background is missing.

## 3. Entanglement

For a declared composition map, the `EntangledState` predicate is the negation of state factorization:

$$
\Psi_{AB}\ne\Psi_A\otimes\Psi_B.
$$

Lean certifies this equivalence without asserting that the composite Hilbert space ceases to admit a tensor product.

## 4. Born and Event

`MeasurementStatus` separates:

- operational probabilities;
- individual event dynamics.

Closing the complete dynamics implies operational Born, but the absence of event dynamics prevents declaring the comprehensive measurement theory closed.

## 5. Sectorial Perelman

`ProductSectorConditions` requires simultaneously:

1. flat Ricci-flat factor;
2. constant dilaton on that factor;
3. absence of mixed torsion;
4. product metric.

The no-go theorems show that mixed torsion or non-product metrics prevent using sectorial reduction automatically.

## 6. Scope

The module certifies coherence of the classification. The physical proofs remain in the modules of the corresponding chapters: action, projector, product Perelman, Born, apparatuses, effective Yang--Mills, and numerical protocol.
