# Output — total and flux Klein--Nishina

Classification: consistency test of asymptotic reduction.

## Constants frozen in the verifier

- alpha = `7.2973525643000e-03`
- hbar = `1.0545718170000e-34 J s`
- c = `299792458.0 m/s`
- m_e = `9.1093837015000e-31 kg`

## Classical radius and Thomson

- r_e = `2.817940322556009e-15 m`
- calculated sigma_T = `6.652458714945131e-29 m^2`
- usual accepted sigma_T = `6.652458732100000e-29 m^2`
- relative difference = `-2.578726e-09`

## Angular integration versus total formula

| x | sigma_KN num/r_e^2 | sigma_KN anal/r_e^2 | rel. error | sigma_KN/sigma_T |
|---|---:|---:|---:|---:|
| 1e-06 | 8.377563654456 | 8.377563654456 | +2.968524e-15 | 0.999998000005 |
| 0.001 | 8.360868701023 | 8.360868688508 | +1.496825e-09 | 0.998005185239 |
| 0.1 | 7.048378000178 | 7.048378000179 | -7.485098e-14 | 0.841338149631 |
| 1 | 3.608457130285 | 3.608457130285 | +2.584449e-15 | 0.430727841915 |
| 10 | 1.028429796455 | 1.028429796455 | +1.187485e-13 | 0.122759764297 |

## Interpretation

The angular integration reproduces the analytical total cross section. For small x, sigma_KN/sigma_T tends to 1, validating the flux normalization of the asymptotic reduction.
