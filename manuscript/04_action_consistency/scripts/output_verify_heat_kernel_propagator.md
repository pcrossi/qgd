---
title: "Output — heat kernel and GDQ propagator"
---

# Output — heat kernel and GDQ propagator

Test parameters, without adjustment:

- $\\tau=0.25$
- $\\widehat\\Lambda_\\tau=\\tau^{-1/2}=2.000000000000$
- $m=0.7$

| $p_E$ | $G_\\tau=e^{-\\tau p^2}/(p^2+m^2)$ | wrong form $e^{-\\tau^2p^2}/(p^2+m^2)$ | wrong/correct ratio |
|---:|---:|---:|---:|
| `0.000000` | `2.040816326531e+00` | `2.040816326531e+00` | `1.000000000000e+00` |
| `0.500000` | `1.252988188166e+00` | `1.233519800762e+00` | `9.844624968032e-01` |
| `1.000000` | `5.226848141203e-01` | `4.954753046764e-01` | `9.479422820625e-01` |
| `2.000000` | `8.261271165181e-02` | `7.054363242095e-02` | `8.539076897103e-01` |
| `4.000000` | `1.109159048382e-03` | `6.726880036070e-04` | `6.064849313271e-01` |
| `8.000000` | `1.722646270513e-09` | `1.579450849646e-13` | `9.168747477543e-05` |

## Poles

The numerator $e^{-\\tau p^2}$ is always positive on the Euclidean real axis.
Thus it does not create poles. The denominator vanishes only when $p_E^2+m^2=0$,
that is, off the Euclidean real axis for $m^2>0$.

## Classification

Consistency test of the flat limit of the heat semigroup; not a metrological prediction.
