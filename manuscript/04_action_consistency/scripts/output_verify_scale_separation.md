---
title: "Output — scale separation"
---

# Output — scale separation

## 1. Heat kernel scale

| $\\tau$ | $\\widehat\\Lambda_\\tau=\\tau^{-1/2}$ |
|---:|---:|
| `1.000000e+00` | `1.000000000000e+00` |
| `2.500000e-01` | `2.000000000000e+00` |
| `1.000000e-02` | `1.000000000000e+01` |
| `1.000000e-04` | `1.000000000000e+02` |

## 2. Why $m_e$ cannot be a hard universal cutoff

The table shows $\\log_{10}\\{\\exp[-(E/\\Lambda)^2]\\}$.

| external energy $E$ [GeV] | $m_e$ cutoff | $1$ GeV cutoff |
|---:|---:|---:|
| `5.109989500e-04` | `-4.342945e-01` | `-1.133869e-07` |
| `1.000000000e-02` | `-1.662058e+02` | `-4.342945e-05` |
| `1.000000000e+00` | `-1.662058e+06` | `-4.342945e-01` |
| `1.000000000e+02` | `-1.662058e+10` | `-4.342945e+03` |
| `1.300000000e+04` | `-2.808878e+14` | `-7.339577e+07` |

Very negative values mean effectively zero suppression.
Thus, $m_e$ or $1$ GeV cannot be read as a universal wall of external energy.

## 3. Mass as a spectral shift

For $p_E=10.0$ GeV, with $\\lambda_i=p_E^2+m_i^2$:

| sector | $m_i$ [GeV] | $p_E^2$ | $m_i^2$ | $\\lambda_i$ | fraction $m_i^2/\\lambda_i$ |
|---|---:|---:|---:|---:|---:|
| `electron` | `5.109989500e-04` | `1.000000000e+02` | `2.611199270e-07` | `1.000000003e+02` | `2.611199263e-09` |
| `hadronic_1GeV` | `1.000000000e+00` | `1.000000000e+02` | `1.000000000e+00` | `1.010000000e+02` | `9.900990099e-03` |
| `electroweak_100GeV` | `1.000000000e+02` | `1.000000000e+02` | `1.000000000e+04` | `1.010000000e+04` | `9.900990099e-01` |

## Conclusion

$\\Lambda_C$, $\\widehat\\Lambda_\\tau$ and $m_i$ have distinct functions.
The mass alters the spectrum of the sector; the resolution comes from $\\tau$; the action uses $\\Lambda_C$ as a normalized dimensionless number.
