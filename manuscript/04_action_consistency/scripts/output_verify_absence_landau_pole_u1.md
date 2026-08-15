---
title: "Output — absence of Landau pole U(1)"
---

# Output — absence of Landau pole $U(1)$

## Input

$$
\\alpha_0=0.00729735256641617,\\qquad \\eta=\\tau m^2=1.000000e-06.
$$

$\\eta$ is a test scenario to verify the formula; it is not fitted.

## Polarization

| $r=q_E^2/m^2$ | $\\Pi_\\eta(r)$ | refined | difference |
|---:|---:|---:|---:|
| `0.000e+00` | `0.000000000000e+00` | `0.000000000000e+00` | `0.000e+00` |
| `1.000e-04` | `2.580434456950e-11` | `2.580434456951e-11` | `1.042e-23` |
| `1.000e+00` | `2.046505085732e-04` | `2.046505085732e-04` | `2.711e-20` |
| `1.000e+04` | `9.479633659223e-03` | `9.479633659223e-03` | `7.822e-17` |
| `1.000e+08` | `1.077270174154e-02` | `1.077270174154e-02` | `4.281e-16` |
| `1.000e+12` | `1.077270174155e-02` | `1.077270174155e-02` | `2.378e-16` |

## Saturation and condition without pole

$$
\\Pi_\\eta(\\infty)=1.077270174155e-02,\\qquad \\alpha_{{\\rm eff}}^{{-1}}(\\infty)=135.560126588.
$$

- monotonicity: `True`;
- bounded by asymptotic value: `True`;
- no-pole condition in scenario: `True`;
- Ward tensorial residue: `0.000e+00`.

## Refinement at $r=10^4$

| Simpson points | $\\Pi_\\eta(10^4)$ |
|---:|---:|
| `100` | `9.47963365935409e-03` |
| `200` | `9.47963365923145e-03` |
| `400` | `9.47963365922378e-03` |
| `800` | `9.47963365922330e-03` |
| `1600` | `9.47963365922327e-03` |

Error between last two orders: `2.951e-16`.

## Low energy limit

| $r$ | $\\eta=10^{-12}$ | $\\eta\\to0$ limit | difference |
|---:|---:|---:|---:|
| `1.000e-04` | `2.580435975001e-11` | `2.580435975003e-11` | `2.148e-23` |
| `1.000e+00` | `2.046522509539e-04` | `2.046522513476e-04` | `3.937e-13` |
| `1.000e+04` | `9.479633659223e-03` | `1.478950850230e-02` | `5.309e-03` |

## Classification

Direct evaluation of derived formula. The test demonstrates saturation for
$\\eta>0$ and recovery of the logarithmic limit at low energy.
