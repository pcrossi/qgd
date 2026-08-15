# Output — sheet--mode neutral oscillations

Classification: reduced GDQ candidate and operational verification.

## Inputs frozen before comparison

- alpha: `7.297352564331424e-03`
- Q_beta: `7.823335593100e+05 eV`
- S_nu = alpha^7 Q_beta^2: `6.744367477916e-04 eV^2`
- chi_nu = (12/25) exp(-alpha/4): `4.791251159771e-01`
- lambda = `(0, chi_nu^2/2, 6*pi/5)`
- delta_CP used in the test: historical marker `3.84 rad`, not final prediction.

## Eigenvalues and masses

| mode | lambda | m_i^2 (eV^2) | m_i (eV) |
|---:|---:|---:|---:|
| 1 | 0.000000000000e+00 | 0.000000000000e+00 | 0.000000000000e+00 |
| 2 | 1.147804383800e-01 | 7.741214557111e-05 | 8.798417219655e-03 |
| 3 | 3.769911184308e+00 | 2.542566638608e-03 | 5.042386973059e-02 |
| sum | — | — | 5.922228695025e-02 |

## Squared differences

| quantity | Reduced GDQ | reference | relative error |
|---|---:|---:|---:|
| dm21 | 7.741214557111e-05 | 7.490000000000e-05 | +3.353999e-02 |
| dm31 | 2.542566638608e-03 | 2.534000000000e-03 | +3.380678e-03 |

## Sheet–mode angles

| parameter | Reduced GDQ | reference | difference |
|---|---:|---:|---:|
| theta12 | 35.264389683 deg | 33.680000000 deg | +1.584389683 deg |
| theta23 | 45.000000000 deg | 48.500000000 deg | -3.500000000 deg |
| theta13 | 8.772427998 deg | 8.520000000 deg | +0.252427998 deg |
| marker delta_CP | 220.015793330 deg | 177.000000000 deg | +43.015793330 deg |

## Squared moduli of the sheet–mode matrix

| sheet | i=1 | i=2 | i=3 | sum |
|---|---:|---:|---:|---:|
| e | 0.651160413499 | 0.325580206750 | 0.023259379751 | 1.000000000000 |
| mu | 0.119358514096 | 0.392271175780 | 0.488370310124 | 1.000000000000 |
| tau | 0.229481072405 | 0.282148617471 | 0.488370310124 | 1.000000000000 |

## Reconstruction of reduced K^nu

- unitary error of U: `2.390e-16`
- hermiticity error of K: `1.388e-17`
- generalized problem residue with G=I: `8.042e-16`

Real part of K:

- 1.250560347231e-01  -2.667862369375e-01  -3.424113861808e-01
- -2.667862369375e-01  1.886137751741e+00  1.803297501729e+00
- -3.424113861808e-01  1.803297501729e+00  1.873497836223e+00

Imaginary part of K:

- 6.938893903907e-18  2.557318610447e-01  2.557318610447e-01
- -2.557318610447e-01  0.000000000000e+00  -5.306043550174e-03
- -2.557318610447e-01  5.306043550174e-03  0.000000000000e+00

## Sensitivity of the coefficients

| coefficient | reference required | Reduced GDQ | relative error |
|---|---:|---:|---:|
| lambda2 | 1.110556330824e-01 | 1.147804383800e-01 | +3.353999e-02 |
| lambda3 | 3.757209268768e+00 | 3.769911184308e+00 | +3.380678e-03 |
| chi_nu | 4.712868194260e-01 | 4.791251159771e-01 | +1.663169e-02 |
| lambda3/(2*pi) | 5.979784273551e-01 | 6.000000000000e-01 | +3.380678e-03 |

## Operational probabilities P(alpha -> beta)

| L/E (km/GeV) | P(e->e) | P(mu->e) | P(mu->mu) | P(mu->tau) |
|---:|---:|---:|---:|---:|
| 100.000000 | 0.990985756980 | 0.003706006525 | 0.904255542604 | 0.092038450871 |
| 491.666667 | 0.907203712454 | 0.037500272956 | 0.001091989999 | 0.961407737045 |
| 405.000000 | 0.914725192295 | 0.033669914525 | 0.085841976685 | 0.880488108791 |
| 520.000000 | 0.907665881634 | 0.037790595095 | 0.004762534499 | 0.957446870406 |
| 1000.000000 | 0.991472814275 | 0.003297133209 | 0.996466038742 | 0.000236828049 |

## Verdict

The reduced reconstruction is internally consistent: U is unitary, K is Hermitian, and the spectral problem closes with machine numerical residue. The squared differences remain close to the reference values, with the largest error in the solar mode. The result is not yet final metrology, since G^nu, K^nu, Z_nu, delta_CP, and the medium potential must come from the official neutral Hessian and classical matter sources.
