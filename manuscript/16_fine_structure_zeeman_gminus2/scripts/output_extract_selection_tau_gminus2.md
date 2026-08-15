# Chapter 16 — extraction of transverse channels

- input: `manuscript/16_fine_structure_zeeman_gminus2/scripts/leptonic_selection_background_tau_gminus2.npz`
- classification: Hodge selection of the tau; universal direct upper source null
- dimension: `3`
- gamma0: `1.000000000000000e+00`
- reconstructed a_geom: `1.161409732097665e-03`

| channel | K_i | J_i | mu_i | |mu_i| | transverse eigenvalue |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610225765836003e+02 | 1.000000000000000e+00 | 1.000000000000000e+00 | 1.000000000000000e+00 | 8.610225765836003e+02 |
| 2 | 2.994159863649186e+06 | -0.000000000000000e+00 | 0.000000000000000e+00 | 0.000000000000000e+00 | 2.994159863649186e+06 |

## Reading

If the input is an official projected Hessian, these coefficients are the numerical derivation of $K_i, J_i, \mu_i$.
If the input is a `required` block, these coefficients only recover the reverse engineering parameters already embedded in the block.
