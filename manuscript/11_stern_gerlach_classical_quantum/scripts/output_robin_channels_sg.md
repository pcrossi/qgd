# Robin spectrum of the two channels — Chapter 11

## Reduced model

$$
H_\pm=-\frac{d^2}{dr^2}+V(r),\qquad R_\pm=R_0\pm r_B.
$$

- domain: [0.1, 8.0]
- R0: 1.0
- separation rB: 0.25
- mass2: 1.0
- well: 0.2
- well width: 0.8
- modes in sums: 16

## Convergence

| N | channel | R | lambda1 | lambda2 | positive gap | Gamma_red | kappa_red | symmetry error | residue |
|---:|:---:|---:|---:|---:|:---:|---:|---:|---:|---:|
| 200 | + | 1.250000 | 1.030703386e+00 | 1.283095454e+00 | True | 2.427939051e-01 | 1.001161571e-01 | 0.000e+00 | 3.119e-13 |
| 200 | - | 0.750000 | 1.025837880e+00 | 1.251088402e+00 | True | 2.951149492e-01 | 1.418164615e-01 | 0.000e+00 | 3.212e-13 |
| 400 | + | 1.250000 | 1.030703256e+00 | 1.283086577e+00 | True | 2.426993583e-01 | 1.000463732e-01 | 0.000e+00 | 1.335e-12 |
| 400 | - | 0.750000 | 1.025837749e+00 | 1.251080902e+00 | True | 2.949938799e-01 | 1.417218272e-01 | 0.000e+00 | 1.420e-12 |
| 800 | + | 1.250000 | 1.030703223e+00 | 1.283084370e+00 | True | 2.426758372e-01 | 1.000290168e-01 | 0.000e+00 | 4.992e-12 |
| 800 | - | 0.750000 | 1.025837716e+00 | 1.251079038e+00 | True | 2.949637637e-01 | 1.416982900e-01 | 0.000e+00 | 5.475e-12 |
| 1600 | + | 1.250000 | 1.030703215e+00 | 1.283083820e+00 | True | 2.426699727e-01 | 1.000246896e-01 | 0.000e+00 | 2.040e-11 |
| 1600 | - | 0.750000 | 1.025837708e+00 | 1.251078574e+00 | True | 2.949562551e-01 | 1.416924219e-01 | 0.000e+00 | 2.116e-11 |

## Diagnosis on the finest mesh

- fundamental mode separation lambda1+ - lambda1-: 4.865507054e-03
- both gaps positive: True
- the matrices are symmetric by variational construction;
- Gamma_red and kappa_red are dimensionless spectral proxies;
- a physical value requires the radial background and the time normalization of GDQ.
