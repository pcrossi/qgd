---
title: "Hartman as saturated proper length"
---

# Hartman as saturated proper length

Status: conditional reduced theorem.

## Hypotheses

1. stationary one-dimensional barrier;
2. dominant evanescent mode;
3. frozen transverse coordinates;
4. real propagating flux suppressed inside the barrier;
5. longitudinal gauge fixed by density;
6. normalization at the interface.

## Proof

The evanescent mode has:

$$
\rho(x)=\rho_0e^{-2\kappa x}.
$$

In the reduced sector:

$$
g_{xx}(x)=g_0\rho(x)/\rho_0.
$$

Therefore:

$$
ds=\sqrt{g_0}e^{-\kappa x}dx.
$$

Integrating:

$$
D_{\rm prop}(L)
=
\int_0^Lds
=
\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right).
$$

Therefore:

$$
\lim_{L\to\infty}D_{\rm prop}(L)
=
\frac{\sqrt{g_0}}{\kappa}.
$$

If the reduced proper velocity is bounded by $v_0\le c$:

$$
\tau_{\rm GDQ}(L)
=
\frac{D_{\rm prop}(L)}{v_0}
$$

also saturates.

## Scope

This explains the geometric saturation. It does not prove that a causal front crosses the barrier faster than light. The experimental comparison depends on the chosen temporal observable.
