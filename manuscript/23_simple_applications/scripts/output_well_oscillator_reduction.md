---
title: "Output — Well and Oscillator as Reduction"
---

# Output — Well and Oscillator as Reduction

Classification: correspondence test of the flat reduced Hessian.

## Numerical parameters

- well: `2400` internal points, $L=1$, $\hbar^2/(2mL^2)=1$;
- oscillator: `3200` internal points in $[-8,8]$, $\hbar=m=\omega=1$;
- no experimental value is used.

## infinite well

| mode | numerical | analytic | relative error |
|---:|---:|---:|---:|
| 1 | `9.869602995677` | `9.869604401089` | `1.424e-07` |
| 2 | `39.478395074621` | `39.478417604357` | `5.707e-07` |
| 3 | `88.826325556091` | `88.826439609804` | `1.284e-06` |
| 4 | `157.913309945731` | `157.913670417430` | `2.283e-06` |
| 5 | `246.739229966292` | `246.740110027234` | `3.567e-06` |

## harmonic oscillator

| mode | numerical | analytic | relative error |
|---:|---:|---:|---:|
| 0 | `0.499999219240` | `0.500000000000` | `1.562e-06` |
| 1 | `1.499996096173` | `1.500000000000` | `2.603e-06` |
| 2 | `2.499989850052` | `2.500000000000` | `4.060e-06` |
| 3 | `3.499980480839` | `3.500000000000` | `5.577e-06` |
| 4 | `4.499967988532` | `4.500000000000` | `7.114e-06` |

## Reduced Morse indices

| mode | ideal well | oscillator |
|---:|---:|---:|
| 1 / 0 | `0` | `0` |
| 2 / 1 | `1` | `1` |
| 3 / 2 | `2` | `2` |
| 4 / 3 | `3` | `3` |
| 5 / 4 | `4` | `4` |

## Reading

- the well retrieves $E_n=(n\pi)^2$ under the ideal boundary;
- the oscillator retrieves $E_n=n+1/2$ in the flat background;
- remaining errors are due to discretization/truncation;
- the reduced Hessian has a Morse index equal to the number of levels below the chosen state;
- the calculation verifies correspondence, not a new metrological prediction.
