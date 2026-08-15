---
title: "Output — neutral torsional cosmic spectrum"
---

# Neutral Torsional Cosmic Spectrum

Classification: kinematic and conditional cosmological estimate.
The absolute intensity is not a prediction.

## Frozen Inputs

- $T_\nu=1.945354563858\,\mathrm{K}$;
- $k_BT_\nu=1.676376858952e-04\,\mathrm{eV}$;
- masses: `[0.0, 0.008798417219655, 0.05042386973059]` eV;
- $z_{\max}=5.0$.

## Local Comb

| channel | energy (eV) | wavelength (um) | toy width |
|---|---:|---:|---:|
| nu1-antinu1 | 5.282890447502e-04 | 2346.900804353 | 4.082483e-01 |
| nu1-antinu2 | 4.671276097616e-03 | 265.418262193 | 2.891932e-01 |
| nu1-antinu3 | 2.547746306597e-02 | 48.664263818 | 2.886910e-01 |
| nu2-antinu2 | 8.814263150481e-03 | 140.663145959 | 2.446865e-02 |
| nu2-antinu3 | 2.962045011883e-02 | 41.857634812 | 1.756427e-02 |
| nu3-antinu3 | 5.042663708718e-02 | 24.587044778 | 4.276968e-03 |

## Band Comparison

- line 22 versus 140 um: `+0.473676%`;
- line 33 versus 24 um: `+2.446020%`;
- line 22 redshift to 240 um: `0.706204`.

## Extreme Inverse Scale, Mode 2

- $\langle\sigma v\rangle=3.096748279139e-29\,\mathrm{m^3/s}$;
- $\tau_{\rm ann}=1.224936370745e-02$.

This number attributes all of FIRAS to the channel and is not a prediction.

## Numerical Convergence

| points | <sigma v> (m^3/s) | tau |
|---:|---:|---:|
| 2001 | 3.096748481007e-29 | 1.224936402848e-02 |
| 20001 | 3.096748281138e-29 | 1.224936371063e-02 |
| 200001 | 3.096748279139e-29 | 1.224936370745e-02 |

## Sensitivity to Source History

| z_max | <sigma v> (m^3/s) | tau |
|---:|---:|---:|
| 1.0 | 1.306601557591e-28 | 5.602544268273e-03 |
| 3.0 | 4.684163862366e-29 | 9.062447841380e-03 |
| 5.0 | 3.096748279200e-29 | 1.224936370755e-02 |

The quadrature converges, but the inverse scale shifts with the cosmological boundary. This confirms that the amplitude must come from the action.
