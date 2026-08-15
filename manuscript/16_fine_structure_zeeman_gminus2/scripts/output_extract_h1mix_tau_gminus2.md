# Chapter 16 — extraction of transverse channels

- input: `manuscript/16_fine_structure_zeeman_gminus2/scripts/leptonic_h1mix_background_tau_gminus2.npz`
- classification: reduced H1 mixture of the tau; allowed, not final metrology
- dimension: `3`
- gamma0: `1.000000000000000e+00`
- reconstructed a_geom: `1.161414653717859e-03`

| channel | K_i | J_i | mu_i | |mu_i| | transverse eigenvalue |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610189268577806e+02 | -9.999999993903506e-01 | -9.999999993903506e-01 | 9.999999993903506e-01 | 8.610189268577807e+02 |
| 2 | 2.994159867298912e+06 | 3.491845990336826e-05 | 3.491845990336826e-05 | 3.491845990336826e-05 | 2.994159867298912e+06 |

## Reading

If the input is an official projected Hessian, these coefficients are the numerical derivation of $K_i, J_i, \mu_i$.
If the input is a `required` block, these coefficients only recover the reverse engineering parameters already embedded in the block.
