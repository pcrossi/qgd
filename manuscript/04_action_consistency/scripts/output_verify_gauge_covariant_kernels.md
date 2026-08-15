---
title: "Output — gauge covariant kernels"
---

# Output — gauge covariant kernels

Parameters: `q_n=1.0`, `m=1.0`, `s0=0.2`, `eta=0.2`, `Q^2=25.0`.

| kernel | $\\Pi_K(0)$ | $\\Pi_K(Q^2)$ | saturation $q_n^2\\mathcal E_K(\\eta)/(48\\pi^2)$ | Ward tensor |
|---|---:|---:|---:|---|
| `canonico` | `0.000000000000e+00` | `1.856980486022e-03` | `2.580436814983e-03` | preserved by covariance |
| `mistura` | `0.000000000000e+00` | `1.468249826315e-03` | `2.046900609712e-03` | preserved by covariance |
| `inteiro_plus` | `0.000000000000e+00` | `3.488344795240e-03` | `4.292900762957e-03` | preserved by covariance |

## Interpretation

All tested kernels preserve $\\Pi_K(0)=0$ and the transverse form.
Saturated values differ because different kernels represent different spectral resolutions.
The canonical GDQ kernel is the semigroup of the physical Hessian, $K_0=e^{-sH}$.
