---
title: "Output — 8D hierarchy by Schur"
---

# Output — 8D hierarchy by Schur

## Reduced Values

- $R_\mu^{(0)} = 206.768593470628673$
- $R_\tau^{(0)} = 3477.446405098381092$
- $Q(R_\mu^{(0)},R_\tau^{(0)}) = 0.666666666666667$

## Linear Response of Saturation

- $\partial Q/\partial R_\mu = -4.426729664581531e-04$
- $\partial Q/\partial R_\tau = 2.884779013665275e-05$
- $(dR_\tau/dR_\mu)_Q = 15.345125722323942$

## Schur Bounds

| scenario | $j_{\rm mix}$ | $m_\perp^2$ | $\Delta_{\rm Schur}$ | $|\delta R_\mu|_{\max}$ | direct $|\delta R_\tau|_{\max}$ |
|---|---:|---:|---:|---:|---:|
| product | 0 | 1 | 0 | 0 | 0 |
| subcritical_weak | 0.1 | 0.99 | 0.010101010101 | 0.010101010101 | 0.010101010101 |
| subcritical_4channels | 0.4 | 0.96 | 0.166666666667 | 0.166666666667 | 0.166666666667 |

## 8D Formula

$$
R_\mu^{(8)}
=
R_\mu^{(0)}-\sigma_\mu.
$$

$$
|\sigma_\ell|\le\Delta_{\rm Schur}.
$$

Maintaining the saturation $Q=2/3$:

$$
dR_\tau
=
-\frac{\partial_\mu Q}{\partial_\tau Q}dR_\mu.
$$
