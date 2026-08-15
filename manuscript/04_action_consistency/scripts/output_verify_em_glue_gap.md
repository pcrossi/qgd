---
title: "Output — stoma electromagnetic gap"
---

# Output — stoma electromagnetic gap

| $L$ | zero mode | $\\lambda_1^{\\rm num}$ | $\\pi^2/L^2$ | relative error |
|---:|---:|---:|---:|---:|
| `1.0` | `0.000e+00` | `9.8695913256e+00` | `9.8696044011e+00` | `1.325e-06` |
| `2.0` | `0.000e+00` | `2.4673978314e+00` | `2.4674011003e+00` | `1.325e-06` |
| `4.0` | `0.000e+00` | `6.1684945785e-01` | `6.1685027507e-01` | `1.325e-06` |
| `8.0` | `0.000e+00` | `1.5421236446e-01` | `1.5421256877e-01` | `1.325e-06` |
| `16.0` | `0.000e+00` | `3.8553091116e-02` | `3.8553142192e-02` | `1.325e-06` |

## Refinement for $L=1$

| cells | $\\lambda_1^{\\rm num}$ | relative error |
|---:|---:|---:|
| `50` | `9.8663529329e+00` | `3.294e-04` |
| `100` | `9.8687913346e+00` | `8.238e-05` |
| `200` | `9.8694011152e+00` | `2.060e-05` |
| `400` | `9.8695535785e+00` | `5.149e-06` |
| `800` | `9.8695913256e+00` | `1.325e-06` |

Since $L^2\\lambda_1\\to\\pi^2$, it follows that

$$
\\lambda_1=\\frac{\\pi^2}{L^2}\\to0
\\quad\\text{when}\\quad L\\to\\infty.
$$

The infinite local stoma does not yield a positive electromagnetic scale;
the scale depends on global gluing or sectorial resolution.
