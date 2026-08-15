---
title: "Output — QGD parabolic symbol in gauge"
---

# Output — QGD parabolic symbol in gauge

## Classification

Symbolic-numerical verification of the positivity of the principal symbol after gauge. Not a physical prediction.

## Test data

- Real bulk dimension: $d=8$
- Symmetric metric components: $36$
- 3-form components: $56$
- Scalars $(\phi,\chi)$: $2$
- Total components in the main block: $94$
- Covector $\xi$ samples: $256$

## Verified identity

$$
\sigma_{\rm pr}(\xi)=|\xi|_g^2 I.
$$

with

$$
|\xi|_g^2=g^{ab}\xi_a\xi_b.
$$

## Numerical values

| quantity | value |
|---|---:|
| smallest eigenvalue of $g$ | 8.062645009310e+00 |
| smallest eigenvalue of $g^{-1}$ | 3.759296727177e-02 |
| smallest sampled $|\xi|_g^2$ | 1.861348219259e-02 |
| largest sampled $|\xi|_g^2$ | 1.589073353619e+00 |

## Verdict

The metric is positive-definite and the principal symbol $|\xi|_g^2I$ is positive for the sampled non-zero covectors. This illustrates strong parabolicity after gauge.
