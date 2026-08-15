# Output — reduced GDQ black hole pipeline

Classification: reduced evaluation / spectral and coupling diagnostics.

## 1. Parameters and status

- lambda_T = `3.000000`
- eta = `8.000000`
- eta_crit = `5.188522012681e+00`
- mu = `-1.067957044153e-01`
- central mass exponent = `3.00002651`
- status: tested effective reduction; complete 8D covariant remains future.

## 2. Core and energy conditions

- epsilon_core = `9.934478711421e-03`
- p_r_core = `-9.934477941512e-03`
- p_t_core = `-9.934158191133e-03`
- epsilon+p_r = `7.699090011359e-10`
- epsilon+p_t = `3.205202880000e-07`
- epsilon+p_r+2p_t = `-1.986831561236e-02`
- max |p_r_metric - p_r_input| core = `2.506468990693e-12`
- core conservation RMS = `2.104757829586e-16`
- static patches conservation RMS = `9.997320016076e-18`

Interpretation: NEC/WEC are saturated in the core and SEC is violated.

## 3. Finite curvature invariants

- R_core = `9.987066970693e-01`
- Ricci2_core = `2.493537672591e-01`
- Kretschmann_core = `1.662358472304e-01`

## 4. Horizons and temperatures

| horizon | r_H | kappa_H | T_H=kappa_H/(2pi) |
|---:|---:|---:|---:|
| 1 | 4.222352820613e+00 | 1.465301433319e-01 | 2.332099662324e-02 |
| 2 | 1.595712272799e+01 | 3.044070699662e-02 | 4.844788989724e-03 |

## 5. Virial and collective mode

- K = `3.167552271297e-01`
- U_T = `9.808336775055e-02`
- W = `-9.274781821674e-01`
- 2K+3U_T+W = `2.823753435869e-04`
- relative residue = `1.522043161064e-04`
- d2E/da2 at a=1 = `1.193971365853e+00`

## 6. Projector radial and reduced Hessian

- lambda_raw[1] = `-1.927437459951e-01`
- lambda_phys[1] after projection = `-5.982003087324e-13`
- lambda_phys[2] = `3.651456961676e-02`

| sector | smallest reduced physical mode |
|---|---:|
| projected radial amplitude | 3.651456961676e-02 |
| inhomogeneous scalar amplitude | 1.909625790263e-03 |
| non-zero phase/circulation | 6.572554660398e-02 |
| reduced torsion | 1.475541776890e-01 |
| exterior axial metric | 1.493545907614e-01 |

## 7. Cross-couplings by Schur

- reduced ||K_gf|| = `6.166879064740e-04`
- reduced ||K_gH|| = `8.076881453156e-06`
- chi_gf = `1.333410946325e-03`
- chi_gH = `2.960174621482e-09`

Interpretation: the reduced couplings are small and do not close the diagonal gaps.

## 8. Toy Page curve

- weights = `[0.9999980969946938, 1.90300515759935e-06, 8.794135715905771e-14, 6.064588145332285e-14]`
- entropy of the weights = `2.696953704284e-05`
- classification: toy unitary, not physical covariant Page curve.

## Verdict

The effective reduction shows a regular core, horizons, effective conservation, positive gaps, and controlled Schur.
The complete 8D covariant closure requires the polar metric sector, horizon-crossing coordinates, coupled 8D matrix, and physical Page curve.
