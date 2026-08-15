# Output — Schur/projector verification

Classification: symbolic-numerical consistency test.

This script verifies the construction:

$$
K_{\rm phys}
=
P_{\rm phys}^T K_{\rm GDQ}P_{\rm phys},
\qquad
\mathsf R
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

## Projector diagnostics

| quantity | value |
|---|---:|
| physical rank | 3 |
| idempotency error `||P^2-P||` | 1.359739955511e-16 |
| constraint error `||CP||` | 1.922962686384e-16 |

## Reduced physical spectrum

| eigenvalue | value |
|---:|---:|
| 1 | 2.238526251288e+00 |
| 2 | 2.715698081194e+00 |
| 3 | 5.345775667518e+00 |

## Internal gap

| eigenvalue of K_II | value |
|---:|---:|
| 1 | 2.248338852158e+00 |
| 2 | 2.751661147842e+00 |

## Schur response

| quantity | value |
|---|---:|
| R_app toy | 5.252882543103e+00 |

Interpretation: the physical projection and Schur reduction algebra is consistent.
To obtain a real solenoid, this toy matrix must be replaced by the Hessian
of the official action evaluated on the physical background of the apparatus.
