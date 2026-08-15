# Chapter 9 — Verification Output

## 1. Riccati Consistency

- analytical response: `1.887922614249`
- RK4 response: `1.887922614249`
- absolute error: `2.220e-15`

## 2. Convergence of the Schur complement

| elements | Schur response | absolute error |
|---:|---:|---:|
| 20 | 1.888375695449 | 4.531e-04 |
| 40 | 1.888035885469 | 1.133e-04 |
| 80 | 1.887950932112 | 2.832e-05 |
| 160 | 1.887929693720 | 7.079e-06 |
| 320 | 1.887924384111 | 1.770e-06 |

## 3. Synthetic calibration and separate validation

- true lambda of the fixture: `0.930000`
- calibrated lambda: `0.930500`
- calibration error: `+5.000e-04`
- calibration chi²: `1.969047`
- local Fisher information: `7.085600e+05`
- RMSE on the frozen test set: `1.566936e-04`

## 4. Classification

Consistency + convergence + synthetic calibration test. Not a physical prediction or experimental comparison.
