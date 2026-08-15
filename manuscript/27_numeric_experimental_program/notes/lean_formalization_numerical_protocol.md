---
title: "Note — Lean Formalization of the Numerical Protocol"
---

# Note — Lean Formalization of the Numerical Protocol

The module [`NumericalProtocol.lean`](../../../formal/GDQ/NumericalProtocol.lean) formalizes the logical accounting of the numerical program. It does not certify a physical background, a particular solver, or an experimental comparison.

## 1. Numerical Classes

Seven uses were separated:

1. direct evaluation;
2. convergence test;
3. consistency test;
4. reverse engineering;
5. calibration;
6. phenomenological comparison;
7. blind prediction.

Lean verifies, by construction, that reverse engineering, convergence, and blind prediction are not the same class.

## 2. Reproducible Manifest

The `NumericalManifest` record registers twelve items: equation, background, domain, boundary, constraints, operator, physical projector, normalization and units, source of the apparatus, observable, numerical parameters, and use of experimental data.

The `ReproducibleManifest` predicate requires all items simultaneously. This is a documentary contract: filling out the manifest does not prove the calculation is correct, but its absence prevents auditing it properly.

## 3. Blind Prediction and Strong Comparison

The `BlindPredictionEligible` predicate requires:

$$
\begin{aligned}
&\text{formula derived before comparison},\\
&\text{universal parameters frozen},\\
&\text{apparatus data measured independently},\\
&\text{target absent from construction},\\
&\text{convergence verified},\\
&\text{numerical uncertainty declared},\\
&\text{boundary sensitivity declared}.
\end{aligned}
$$

The theorem `not_blindPredictionEligible_of_target_used` formally proves that using the target in the construction prevents this classification. The corresponding theorem for unfrozen parameters yields the same conclusion.

A metrologically strong comparison still requires experimental uncertainty, numerical error smaller than the examined discrepancy, and the same set of parameters in more than one observable.

## 4. Numerical Error and Physical Discrepancy

For calculated value $u_h$, continuous limit $u$, and physical target $u_{\rm exp}$, the triangle inequality yields:

$$
|u_h-u_{\rm exp}|
\le
|u_h-u|
+
|u-u_{\rm exp}|.
$$

The first term measures discretization; the second measures physical discrepancy of the continuous model. The Lean theorem `numerical_physical_error_decomposition` prevents these errors from being silently added under a single label.

## 5. Scope

This formalization certifies classification rules and error identities. It does not promote prediction:

$$
\text{correct protocol}
\not\Rightarrow
\text{correct background}.
$$

The physical prediction continues to require the chain from the official action to the observable, with domain, boundaries, stability, and absence of post-fitting.
