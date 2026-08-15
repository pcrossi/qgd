# Output — variable Nelson--Itô diffusion

## Classification

Symbolic-numerical test of differential identity in periodic domain. Not a physical prediction.

## Tested identities

$$
D=\nu_0\Omega^{-1}.
$$

$$
\partial_x^2(D\rho)
=D\rho''+2D'\rho'+\rho D''.
$$

$$
u=D\partial_x\ln\rho+\partial_xD
=D(\partial_x\ln\rho-\partial_x\ln\Omega).
$$

## Numerical parameters

- Periodic domain: $[0,2\pi)$
- Grid: $N=2048$
- $\nu_0=0.5$ in reduced units

## Maximum errors

| test | maximum error |
|---|---:|
| Itô expansion | 1.691021e-10 |
| conservative vs expanded Fokker--Planck | 1.691021e-10 |
| variable osmotic velocity | 9.168838e-14 |

## Size of omitted terms if $\Omega$ is treated as constant

| quantity | value |
|---|---:|
| $\lVert\partial_x^2(D\rho)-D\rho''\rVert_\infty$ | 3.171848e-01 |
| fraction relative to complete term | 1.111239e+00 |

## Verdict

The identities passed. The terms with gradients of $\Omega$ are necessary when $\Omega$ varies.

No experimental target was used.
