---
title: "Output — EO-MZI delayed choice"
---

# Output — EO-MZI delayed choice

Classification: direct evaluation of reduced model with external apparatus data.

## Frozen parameters

- wavelength: `1.550000e-06 m`
- push-pull voltage Vpi: `2.445000 V`
- switching time: `1.810000e-11 s`
- crosstalk used: `-30.0 dB`
- power leakage: `1.000000e-03`
- expected residual coherence: `3.162277660168e-02`
- assumed path: `1.000000 m`
- causal delay: `3.335640951982e-09 s`

## Reduced impedance

- `Gamma_on = 3.453877639491`
- `R_on = 3.453877639491` for `||DeltaPhi||^2 = 2.0`
- `R_off = 0.000000000000`
- EO phase at Vpi: `3.141592653590 rad`

## Causal evolution

| `(t_f-delay)/tau_switch` | `Gamma_det` | `C=exp(-Gamma)` | coherence loss |
|---:|---:|---:|---:|
| -4.0 | 0.031811344537 | 9.686893133728e-01 | 0.031310686627 |
| -2.0 | 0.215152226297 | 8.064186727048e-01 | 0.193581327295 |
|  0.0 | 1.060108177874 | 3.464183335042e-01 | 0.653581666496 |
|  1.0 | 1.785210290344 | 1.677617786084e-01 | 0.832238221392 |
|  2.0 | 2.460088572183 | 8.542738414229e-02 | 0.914572615858 |
|  4.0 | 3.199724966749 | 4.077341648169e-02 | 0.959226583518 |
|  8.0 | 3.444610757527 | 3.191718314836e-02 | 0.968082816852 |
|  12.0 | 3.453623103089 | 3.163082677395e-02 | 0.968369173226 |
|  16.0 | 3.453871418618 | 3.162297332359e-02 | 0.968377026676 |

## Late limit

- `Gamma_inf = 3.453877639491`
- `C_inf = 3.162277660168e-02`

## Comparison with the apparatus limit

- `sqrt(p_leak) = 3.162277660168e-02`
- `exp(-Gamma_inf) = 3.162277660168e-02`

The reduced calculation exactly reproduces the amplitude coherence imposed
by the crosstalk used as frozen external data.
