---
title: "Output — Neutral Gaussian soliton"
---

# Output — Neutral Gaussian soliton

## Classification

Symbolic-numerical verification of an explicit neutral solution. Not a metrological prediction.

## Data

- Real dimension: $d=8$
- Geometric scale: $\sigma=1.3$
- Monte Carlo samples: $500000$

## Soliton equation

$$
\phi=\frac{|x|^2}{4\sigma},
\qquad
\nabla_i\nabla_j\phi=\frac{1}{2\sigma}\delta_{ij}.
$$

| quantity | value |
|---|---:|
| $1/(2\sigma)$ | 3.846153846154e-01 |
| soliton residue norm | 0.000000000000e+00 |

## Reduced free energy

$$
\mathcal W_{\rm gauss}
=
\left\langle\sigma|\nabla\phi|^2+\phi-d\right\rangle.
$$

| quantity | analytical | Monte Carlo |
|---|---:|---:|
| $\langle |x|^2\rangle$ | 2.080000000000e+01 | 2.079299729017e+01 |
| $\langle\phi\rangle$ | 4.000000000000e+00 | 3.998653325033e+00 |
| $\langle\sigma|\nabla\phi|^2\rangle$ | 4.000000000000e+00 | 3.998653325033e+00 |
| $\mathcal W$ | 0.000000000000e+00 | -2.693349933821e-03 |
| MC standard error of $\mathcal W$ | — | 5.645521460939e-03 |

## Reduced scalar Ornstein--Uhlenbeck spectrum

$$
\lambda_k=\frac{k}{2\sigma}.
$$

| $k$ | $\lambda_k$ |
|---:|---:|
| 0 | 0.000000000000e+00 |
| 1 | 3.846153846154e-01 |
| 2 | 7.692307692308e-01 |
| 3 | 1.153846153846e+00 |
| 4 | 1.538461538462e+00 |
| 5 | 1.923076923077e+00 |
| 6 | 2.307692307692e+00 |

Gap after removing the constant mode: $3.846153846154e-01$.

## Verdict

The Gaussian solution exactly satisfies the neutral soliton equation, has $\mathcal W=0$ analytically, and exhibits a positive gap in the reduced OU sector after removing the zero mode. It serves as a neutral reference; charge, spin, and mass of real particles require the solitonic record of the corresponding sector.
