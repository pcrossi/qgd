---
title: "Output — CP Hessian and susceptibility"
---

# Output — CP Hessian and susceptibility

Reduced potential:

$$
V(\theta)=\chi(1-\cos\theta).
$$

Used $\chi=1$ and finite difference step `h=1.0e-04` only to verify the identity.

| $\theta$ | Analytical Hessian | Numerical Hessian | Classification |
|---:|---:|---:|---|
| `0.000000000000` | `1.000000000000` | `0.999999993923` | stable minimum |
| `1.570796326795` | `0.000000000000` | `0.000000011102` | flat point of the angular projection |
| `3.141592653590` | `-1.000000000000` | `-0.999999993923` | unstable maximum |
| `6.283185307180` | `1.000000000000` | `0.999999993923` | stable minimum |

Conclusion: in the torsional channel, $\chi_{\rm top}^{\rm GDQ}>0$ is exactly the positive curvature of the CP minimum.
