# Chapter 16 — extraction of transverse channels

- input: `manuscript/16_fine_structure_zeeman_gminus2/scripts/official_galerkin_bare_hessian_gminus2.npz`
- classification: reduced Galerkin of the official action without magnetic source; consistency test
- dimension: `5`
- gamma0: `1.000000000000000e+00`
- reconstructed a_geom: `-0.000000000000000e+00`

| channel | K_i | J_i | mu_i | |mu_i| | transverse eigenvalue |
|---:|---:|---:|---:|---:|---:|
| 1 | -5.337217757551488e+01 | 3.987859080130285e+01 | 0.000000000000000e+00 | 0.000000000000000e+00 | -5.337217757551485e+01 |
| 2 | 6.276683090818080e+00 | -1.039515698794529e-01 | 0.000000000000000e+00 | 0.000000000000000e+00 | 6.276683090818081e+00 |
| 3 | 2.501267296771635e+01 | 5.740065781233854e+00 | 0.000000000000000e+00 | 0.000000000000000e+00 | 2.501267296771632e+01 |
| 4 | 1.534017132776371e+02 | 3.228383449748677e+02 | 0.000000000000000e+00 | 0.000000000000000e+00 | 1.534017132776371e+02 |

## Reading

If the input is an official projected Hessian, these coefficients are the numerical derivation of $K_i, J_i, \mu_i$.
If the input is a `required` block, these coefficients only recover the reverse engineering parameters already embedded in the block.
