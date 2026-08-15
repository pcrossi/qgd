---
title: "Output — simulate S+A+E decoherence"
---

# Output — simulate S+A+E decoherence

Classification: effective reduction of measurement.

## Initial coefficients

- $|c_0|^2 = 0.370000000000$
- $|c_1|^2 = 0.630000000000$

## Suppression by environmental orthogonalization

| environmental overlap eta | reduced coherence | p0 | p1 |
|---:|---:|---:|---:|
| 1.000 | 0.482804308183 | 0.370000000000 | 0.630000000000 |
| 0.500 | 0.241402154091 | 0.370000000000 | 0.630000000000 |
| 0.100 | 0.048280430818 | 0.370000000000 | 0.630000000000 |
| 0.010 | 0.004828043082 | 0.370000000000 | 0.630000000000 |
| 0.000 | 0.000000000000 | 0.370000000000 | 0.630000000000 |

## Decay by sectorial gap

Using $|\Gamma_{01}(\tau)|\le C e^{-\Delta_{\rm meas}\tau}$ with
$C=1.000$ and $\Delta_{\rm meas}=1.750$:

| tau | bound for $|\Gamma_{01}|$ |
|---:|---:|
| 0.000 | 1.000000000000e+00 |
| 0.500 | 4.168620196785e-01 |
| 1.000 | 1.737739434504e-01 |
| 2.000 | 3.019738342232e-02 |
| 4.000 | 9.118819655545e-04 |

## Ideal repeatability

After conditioning on record 0:

| test | value |
|---|---:|
| $p_0=\operatorname{Tr}(\rho_S P_0)$ | 0.370000000000 |
| $\operatorname{Tr}(\rho_{S|0}P_0)$ | 1.000000000000 |
| repeatability error | 0.000000000000e+00 |

## Interpretation

When the environmental overlap tends to zero, the interference terms
disappear, but the diagonal weights remain equal to the operational
Born weights. The sectorial gap provides asymptotic exponential suppression.
After conditioning on a record, the ideal repetition of the same projector gives
probability 1.

This still does not select the individual event on its own; ontological selection
requires real basins of the apparatus/environment.
