# Chapter 16 — extraction of transverse channels

- input: `manuscript/16_fine_structure_zeeman_gminus2/scripts/leptonic_h1mix_background_mu_gminus2.npz`
- classification: reduced H1 mixture of the muon; allowed, not final metrology
- dimension: `3`
- gamma0: `1.000000000000000e+00`
- reconstructed a_geom: `1.161414653717858e-03`

| channel | K_i | J_i | mu_i | |mu_i| | transverse eigenvalue |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610189101754544e+02 | -9.999999896529351e-01 | -9.999999896529351e-01 | 9.999999896529351e-01 | 8.610189101754544e+02 |
| 2 | 1.780324307730558e+05 | 1.438545429561274e-04 | 1.438545429561274e-04 | 1.438545429561274e-04 | 1.780324307730559e+05 |

## Reading

If the input is an official projected Hessian, these coefficients are the numerical derivation of $K_i, J_i, \mu_i$.
If the input is a `required` block, these coefficients only recover the reverse engineering parameters already embedded in the block.
