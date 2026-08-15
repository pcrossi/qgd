# Chapter 16 — official reduced Galerkin Hessian

## Classification

Official reduced Galerkin / consistency test. It is not a metrological prediction.

## Coordinates

| index | mode |
|---:|---|
| 0 | circulation/linear phase on the cycle |
| 1 | leading harmonic mode `sin(theta)` |
| 2 | upper phase mode `sin(2 theta)` |
| 3 | density mode `cos(theta)` in `Re f` |
| 4 | conformal metric mode `cos(theta)` |

## Eigenvalues of the raw Hessian

| i | lambda_i |
|---:|---:|
| 0 | -1.062008119137641e+02 |
| 1 | -4.347916715816304e+01 |
| 2 | 6.276712765070020e+00 |
| 3 | 2.507972449201663e+01 |
| 4 | 5.752734465739256e+02 |

## Circulation vector

`c = [1. 0. 0. 0. 0.]`

## Transverse source of the bare action

The official action without external source/apparatus does not contain the magnetic functional `M[Phi;B]`. Therefore, in the bare sector:

$$
m_{\perp}^{\rm naked}=0.
$$

- `a_geom_naked = -0.0`

### Channels extracted with bare source

| channel | K_i | J_i | mu_i | transverse eigenvalue |
|---:|---:|---:|---:|---:|
| 1 | -5.337217757551483e+01 | 3.987859080130288e+01 | 0.000000000000000e+00 | -5.337217757551483e+01 |
| 2 | 6.276683090818080e+00 | -1.039515698794529e-01 | 0.000000000000000e+00 | 6.276683090818081e+00 |
| 3 | 2.501267296771633e+01 | 5.740065781233856e+00 | 0.000000000000000e+00 | 2.501267296771631e+01 |
| 4 | 1.534017132776370e+02 | 3.228383449748675e+02 | 0.000000000000000e+00 | 1.534017132776371e+02 |

## Leading source of apparatus/boundary

The leading source used in Chapter 16 comes from Noether + harmonic projection and is not a new term in the fundamental action. In this test, it is represented by the unit vector in mode 1:

`m_perp_leader = [0. 1. 0. 0. 0.]`

- `a_geom_raw_with_leader_source = -0.00046795114777494786`

### Channels extracted with leading source

| channel | K_i | J_i | mu_i | transverse eigenvalue |
|---:|---:|---:|---:|---:|
| 1 | -5.337217757551483e+01 | 3.987859080130288e+01 | -2.056371014553084e-03 | -5.337217757551483e+01 |
| 2 | 6.276683090818080e+00 | -1.039515698794529e-01 | 9.999738775495080e-01 | 6.276683090818081e+00 |
| 3 | 2.501267296771633e+01 | 5.740065781233856e+00 | 1.597714508062543e-03 | 2.501267296771631e+01 |
| 4 | 1.534017132776370e+02 | 3.228383449748675e+02 | 6.742615605441424e-03 | 1.534017132776371e+02 |

## Verdict

The second variation of the official reduced action provides `H` and `c`. It does not provide magnetic `m_perp` without specifying the external source or boundary condition of the apparatus. Thus, the coefficients `K_i` and `J_i` can be extracted from the official Galerkin Hessian, but `mu_i` requires the physical map `M[Phi;B]`.

The complete metrological prediction of `g-2` remains dependent on the construction of the external magnetic coupling in the official leptonic background.
