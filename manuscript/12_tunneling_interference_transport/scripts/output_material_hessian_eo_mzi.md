---
title: "Output — EO-MZI material Hessian"
---

# Output — Reduced EO-MZI material Hessian

Classification: reduced material engineering model.

## Frozen data

- lambda = `1.550000e-06 m`
- Vpi = `2.445000 V`
- tau_sw = `1.810000e-11 s`
- reference target for comparison: `-30.0 dB`

## Ideal transfer

- phase at Vpi: `3.141592653590 rad`
- ideal dark port power: `3.749399456655e-33`
- ideal bright port power: `1.000000000000e+00`
- ideal crosstalk: `3.749399456655e-33`

## Material imperfections equivalent to -30 dB

- required phase error: `delta_phi = 6.322448399238e-02 rad`
- equivalent voltage error: `delta_V = 4.920557195241e-02 V`
- relative voltage error: `2.012497830364e-02`
- amplitude ratio required in isolation: `0.938693139937`
- amplitude imbalance: `-0.549527119802 dB`
- coupler differential error: `delta_theta = 3.161224199619e-02 rad`
- corresponding power split: `0.531591185416`

## Equivalent effective impedance

- `Gamma_target = 3.453877639491`
- `R_target = 3.453877639491` for `||DeltaPhi||^2=2`

## Interpretation

With ideal Vpi and ideal 3 dB couplers, the stationary crosstalk is zero.
The finite value of -30 dB requires material imperfection: phase, amplitude, coupler or a mixture of them.
Therefore, the crosstalk belongs to delta K_app material/fabrication/losses, not to the fundamental action.
