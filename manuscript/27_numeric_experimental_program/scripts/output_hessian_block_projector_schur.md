# Output — Hessian block, projector, and Schur

Classification: methodological tool / algebraic verification.

## Matrices used

Hessian example $K$:

```text
 4.000000  0.300000  0.600000  0.100000
 0.300000  3.000000  0.200000  0.400000
 0.600000  0.200000  5.000000  0.700000
 0.100000  0.400000  0.700000  4.500000
```

Linearized constraint $DC$:

```text
 1.000000 -1.000000  0.500000  0.000000
```

## Verifications

| test | value |
|---|---:|
| idempotence norm(P^2-P) | 0.000000000000e+00 |
| constraint norm(DC P) | 7.850462293419e-17 |
| symmetry norm(Kphys-Kphys^T) | 3.510833468577e-16 |
| lowest eigenvalue K_eff | -2.220446049250e-16 |

## Spectrum

| operator | eigenvalues |
|---|---|
| $K_{\rm phys}$ | `[-1.554312234e-15  3.642271729e+00  3.828581072e+00  5.451369421e+00]` |
| $K_{\rm eff}$ | `[-2.220446049e-16  3.750985499e+00]` |

## Verdict

The algebraic block removes the constraint, preserves the symmetry of the Hessian, and produces a non-negative effective Schur operator in this example up to roundoff error. In physical applications, only $K$, $DC$, domain, and boundaries change.
