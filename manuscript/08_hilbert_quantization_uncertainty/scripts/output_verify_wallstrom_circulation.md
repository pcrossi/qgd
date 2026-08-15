---
title: "Output — Wallstrom circulation"
---

# Output — Wallstrom circulation

Classification: symbolic/topological test.

## Maps $S^1\to S^1$

| parameter $\alpha$ | phase closes? | defect $|e^{i2\pi\alpha}-1|$ | formal winding |
|---:|---:|---:|---:|
| -2 | True | 4.898587e-16 | -2 |
| -1 | True | 2.449294e-16 | -1 |
| 0 | True | 0.000000e+00 | 0 |
| 1 | True | 2.449294e-16 | 1 |
| 2 | True | 4.898587e-16 | 2 |
| 0.5 | False | 2.000000e+00 | 0.5 |
| 1.3 | False | 1.618034e+00 | 1.3 |

Conclusion: the integral can be formally calculated for any $\alpha$, but only integers close the regular global map $S^1\to S^1$.

## Example of Chern Flux on $T^2$

For $F=N(2\pi)^{-1}dx\wedge dy$ on $[0,2\pi)^2$:

| parameter $N$ | $(2\pi)^{-1}\int_{T^2}F$ | integer flux? |
|---:|---:|---:|
| -2 | -2.000000000000 | True |
| -1 | -1.000000000000 | True |
| 0 | 0.000000000000 | True |
| 1 | 1.000000000000 | True |
| 3 | 3.000000000000 | True |
| 0.5 | 0.500000000000 | False |

Additional conclusion: the curvature can be formally written with any $N$, but only integer classes represent the first Chern class of a globally admissible $U(1)$ line bundle.
