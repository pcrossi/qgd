# Chapter 16 — output of the Hessian blocks builder

## Classification

- Leading blocks: direct evaluation of already derived quantity.
- `required` blocks: inverse diagnostic of the missing upper channel.

## Parameters

- `alpha_inv = 137.035999177000`
- `alpha = 7.297352564331424e-03`
- `K1 = 2*pi/alpha = 8.610225765836003e+02`
- `a_leader = alpha/(2*pi) = 1.161409732097664e-03`

## Universal leading block

- file: `leading_hessian_gminus2.npz`
- `a_geom = 1.161409732097665e-03`
- `g_total = 2.002322819464196e+00`
- `eig_min = 9.988372413989819e-01`

## Q39 hierarchy used for diagnostic stiffness

| case | Q39 role | M_l/M_e | K2 used |
|---|---|---:|---:|
| electron | primary torsion | 1.000000000000000e+00 | 8.610225765836003e+02 |
| muon | transverse/bispatial torsion | 2.067685934706287e+02 | 1.780324271066477e+05 |
| tau | three-dimensional saturation | 3.477446405098381e+03 | 2.994159863649186e+06 |

## Required upper blocks

In these blocks the amplitude `mu2_required` is chosen to reach `a_obs`. Therefore, they are diagnostic reverse engineering.

| case | a_obs | residual a_obs-a_leader | mu2_required | reconstructed a | file |
|---|---:|---:|---:|---:|---|
| electron | 1.159652180590109e-03 | -1.757551507554920e-06 | -1.513291527513514e-03 | 1.159652180590110e-03 | `required_hessian_e_gminus2.npz` |
| muon | 1.165920590000000e-03 | 4.510857902335647e-06 | 8.030789806924942e-01 | 1.165920590000000e-03 | `required_hessian_mu_gminus2.npz` |
| tau | — | — | — | — | — |

## Verdict

The leading block constructs $H_C,c,m_\perp$ without an experimental target and reproduces exactly $\alpha/(2\pi)$.

The `required` blocks numerically show the size of the upper transverse response that remains to be derived. They do not metrologically close $g-2$, but they transform the pending task into a precise quantity: to derive from the official action the channel that will replace `mu2_required`.
