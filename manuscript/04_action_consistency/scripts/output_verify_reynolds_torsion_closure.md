---
title: "Output — torsion-Reynolds closure"
---

# Output — torsion--Reynolds closure

| scenario | $\\alpha$ | $R$ | $\\tau_{\\rm EM}$ | $\\widehat\\Lambda_{\\rm EM}$ | $L/\\ell_C$ | residual |
|:---|---:|---:|---:|---:|---:|---:|
| low energy — $1/137$ approximation | `7.299270072992701e-03` | `1.037007998638` | `0.274880942502` | `1.907338165518` | `1.644917992983` | `0.000e+00` |
| external metrological reference | `7.297352566416170e-03` | `1.037074352341` | `0.274900522500` | `1.907270174112` | `1.644976579899` | `0.000e+00` |
| high energy effective benchmark — $1/128$ | `7.812500000000000e-03` | `1.019553755490` | `0.269784572238` | `1.925249567954` | `1.629631776963` | `0.000e+00` |

Each row numerically satisfies:

$$
\\operatorname{Re}_{\\rm Q}=\\alpha,
\\qquad
x^3-4\\tau x^2+\\frac{\\tau n_B^2}{\\pi^2}=0.
$$

The $1/128$ row is a high energy effective benchmark, not a fundamental
input of the low energy closure.
