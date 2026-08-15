# Output — beta decay validation GDQ

Classification: direct evaluation, convergence test, and phenomenological comparison.

## Parameters

- `m_e = 0.51099895069 MeV`
- `DeltaM = 1.29333251 MeV`
- `Q_beta endpoint = 0.782333559310 MeV`
- `Q_beta` is maximum available energy, not a fixed antineutrino energy.

## Phase space

- `I_beta analytical = 5.700456936530352e-17 GeV^5`
- `I_beta Simpson = 5.700456308550165e-17, 5.700456714505864e-17, 5.700456858032888e-17 GeV^5`
- `mesh spread = 5.495e-24 GeV^5`
- `fine Simpson relative error = 1.377e-08`

## Total rate

- `alpha^-1 = 137.035999177000`
- `2|C_S|^2+6|C_T|^2 = 8.142351666635048e-10 GeV^-4`
- `sqrt(2|C_S|^2+6|C_T|^2) = 2.853480623139931e-05 GeV^-2`
- `Gamma = 1.137140542406870e-03 s^-1`
- `tau_n = 879.398775004012 s`
- `T_1/2 = 609.552781481901 s`

## Comparison

| reference | tau_ref s | difference s | relative difference | simple sigma |
|---|---:|---:|---:|---:|
| average used 2026 | 878.300000000000 | 1.098775004013 | 1.251024711388e-03 | 2.746938 |
| average used 2024/2025 | 878.400000000000 | 0.998775004012 | 1.137038938994e-03 | 1.997550 |

## Reduced spectral shape

| E_e MeV | E_antineutrino recoil-zero MeV | normalized spectral shape |
|---:|---:|---:|
| 0.510998950690 | 0.782333559310 | 0.000000000000 |
| 0.706582340518 | 0.586750169482 | 1.000000000000 |
| 0.902165730345 | 0.391166779655 | 0.864576508054 |
| 1.097749120172 | 0.195583389828 | 0.343679377483 |
| 1.293332510000 | 0.000000000000 | 0.000000000000 |

Interpretation: the calculation closes the total reduced rate and the minimal continuous spectrum. Fine differential shape, recoil, surface, and angular correlations require the individual separation of the coefficients `C_S` and `C_T` by the physical fourth variation.
