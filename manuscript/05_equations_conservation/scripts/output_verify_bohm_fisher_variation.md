# Output — Fisher-Bohm variation

## Classification

Numerical/symbolic variation test. Not a physical prediction.

## Verified identity

$$
\frac{\delta}{\delta\rho}\int\frac{|\nabla\rho|^2}{\rho}\,dx
=-4\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

## Periodic grid results

| N | maximum error | relative error |
|---:|---:|---:|
| 200 | 4.626814656239e-05 | 5.303095815359e-05 |
| 400 | 1.158038310345e-05 | 1.326992296575e-05 |
| 800 | 2.895440856521e-06 | 3.317479751867e-06 |
| 1600 | 7.239507249235e-07 | 8.294609553843e-07 |

## Verdict

The check passed at the refinement used.

This output verifies the differential identity in 1D periodic; the general QGD form uses $\Delta_g$ and its own domain/boundary.
