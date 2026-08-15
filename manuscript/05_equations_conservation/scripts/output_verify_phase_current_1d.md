# Output — phase current in 1D

## Classification

Current conservation illustration. Not a physical prediction.

## Verified identity

In an interval:

$$
\int_0^1\partial_xJ\,dx=J(1)-J(0).
$$

Therefore:

$$
\frac{dQ}{dt}=-J(1)+J(0).
$$

## Results

| case | $\int\partial_xJdx$ | $J(1)-J(0)$ | $dQ/dt$ |
|---|---:|---:|---:|
| constant | -1.136868377216e-16 | 0.000000000000e+00 | -0.000000000000e+00 |
| linear | 3.000000000000e-01 | 3.000000000000e-01 | -3.000000000000e-01 |
| no_net_flux | -1.942890293094e-16 | 0.000000000000e+00 | -0.000000000000e+00 |

## Verdict

The check passed.

This output illustrates integrated conservation; the real QGD current depends on $\mathcal U$, $g$, and $S_R$.
