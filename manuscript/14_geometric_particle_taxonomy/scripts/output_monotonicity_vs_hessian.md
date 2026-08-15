---
title: "Output — Monotonicity versus Hessian"
---

# Output — Monotonicity versus Hessian

## Classification

Symbolic-numerical illustration of stability criterion. Not a physical prediction.

## Models

$$
E_{\rm min}=\frac12(x^2+2y^2),
\qquad
E_{\rm saddle}=\frac12(x^2-y^2).
$$

Flow used:

$$
\dot X=-\nabla E=-HX.
$$

## Hessians

| case | Hessian eigenvalues | interpretation |
|---|---:|---|
| minimum | [1.0, 2.0] | stable |
| saddle | [-1.0, 1.0] | unstable due to negative direction |

## Evolution

| case | initial energy | final energy | monotonic energy? | final/initial norm ratio |
|---|---:|---:|---|---:|
| minimum | 3.600000000000e-01 | 1.888484348023e-06 | True | 2.356769805584e-03 |
| saddle | 3.000000000000e-01 | -3.006324021355e+03 | True | 9.403259799496e+01 |

## Verdict

Energy can be monotonic along the flow even when the critical point is a saddle. Therefore, for GDQ, Perelman--Bismut monotonicity is a Lyapunov condition, but soliton stability requires a physical Hessian without negative eigenvalues after projecting gauge, symmetries, and moduli.
