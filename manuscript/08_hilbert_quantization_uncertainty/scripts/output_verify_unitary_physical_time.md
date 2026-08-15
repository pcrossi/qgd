---
title: "Output — verify unitariety in physical time"
---

# Output — verify unitariety in physical time

Classification: algebraic/numerical consistency test.

## Data

- dimension of the closed sector: 3
- eigenvalues of $H$: 0.329602635099, 1.087742645439, 2.332654719462
- physical time used: $t=2.7$
- Euclidean parameter used: $a=1.3$

## Results

| Quantity | Value | Interpretation |
|---|---:|---|
| error $\|U^\dagger U-I\|$ | 8.153e-16 | must be close to zero |
| initial norm $\|\psi\|^2$ | 1.000000000000 | normalized |
| norm after $U(t)$ | 1.000000000000 | preserved |
| spectral norm of $T_E(a)$ | 0.651496388608 | Euclidean contraction |
| norm after $T_E(a)$ | 0.231268588835 | dampening in Euclidean parameter |
| projected non-Hermitian survival | 0.296710014294 | decays in the partial sector |
| $\exp(-\Gamma t/\hbar)$ | 0.296710014294 | analytical reference |
| total norm error in the extended Hermitian model | 2.220e-16 | total closed preserves norm |
| probability in channel $P$ | 0.449368694702 | observed channel |
| probability leaked to $Q$ | 0.550631305298 | unobserved channel |
| balance error $P+Q=1$ | 0.000e+00 | total conservation |

## Physical Reading

The test separates three facts. The group $U(t)$ preserves the norm when $H$ is Hermitian. The Euclidean semigroup $T_E(a)$ is contractive when $H\ge0$. A projected sector can decay without the total closed dynamics ceasing to be unitary.
