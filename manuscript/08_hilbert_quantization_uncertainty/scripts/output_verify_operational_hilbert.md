---
title: "Output — operational Hilbert"
---

# Output — operational Hilbert

Classification: algebraic-numerical consistency test.

This test is not a metrological prediction. It verifies, in finite dimension, the minimum expected algebra after the operational reconstruction: quotienting by null states, states, observables, unitary evolution, and tensor composition.

## Results

| Quantity | Value | Criterion |
|---|---:|---|
| null dimension removed | 1 | $\ge 1$ in this toy model |
| physical dimension of the quotient | 2 | `2` |
| orthonormalization error in the quotient | 2.220e-16 | close to zero |
| $\operatorname{Tr}\varrho$ | 1.000000000000 | `1` |
| smallest eigenvalue of $\varrho$ | -2.776e-17 | non-negative |
| smallest spectral probability | 0.166666666667 | non-negative |
| error in the sum of probabilities | 2.220e-16 | close to zero |
| imaginary part of $\langle A\rangle$ | 4.586e-19 | close to zero |
| unitariety error of $U(t)$ | 4.527e-16 | close to zero |
| norm preservation error | 2.220e-16 | close to zero |
| tensor factorization error | 2.776e-17 | close to zero |

## Interpretation

The test confirms that once the positive physical space is obtained by quotienting, the usual operational language follows: normalized states, positive density matrices, spectral probabilities, unitary evolution via a Hermitian Hamiltonian, and composition via a tensor product.

In QGD, this layer is reconstructed from geometry and does not replace the official action.
