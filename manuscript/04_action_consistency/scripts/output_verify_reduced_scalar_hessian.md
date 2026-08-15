---
title: "Output — reduced scalar Hessian"
---

# Output — reduced scalar Hessian

Test case: flat background, constant $f_0$, $R_0=0$, periodic domain.

$$
L_\\varphi=2(-\\Delta).
$$

Mesh: `N=128`, length `2π`.

| index | expected $2k^2$ | numerical | error |
|---:|---:|---:|---:|
| `0` | `0.000000000000e+00` | `-4.896684725916e-16` | `-4.896684725916e-16` |
| `1` | `2.000000000000e+00` | `1.999497554316e+00` | `-5.024456839356e-04` |
| `2` | `2.000000000000e+00` | `1.999497554316e+00` | `-5.024456839356e-04` |
| `3` | `8.000000000000e+00` | `7.991963248694e+00` | `-8.036751306354e-03` |
| `4` | `8.000000000000e+00` | `7.991963248694e+00` | `-8.036751306354e-03` |
| `5` | `1.800000000000e+01` | `1.795934651341e+01` | `-4.065348658826e-02` |
| `6` | `1.800000000000e+01` | `1.795934651341e+01` | `-4.065348658826e-02` |
| `7` | `3.200000000000e+01` | `3.187123999966e+01` | `-1.287600003442e-01` |
| `8` | `3.200000000000e+01` | `3.187123999966e+01` | `-1.287600003442e-01` |

Conclusion: in the flat background, the reduced scalar Hessian has a positive principal symbol proportional to $p_E^2$.
The finite difference converges to the continuous spectrum when the mesh is refined.
