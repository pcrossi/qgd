---
title: "Output — CP periodicity by integer charge"
---

# Output — CP periodicity by integer charge

Test:

$$
\exp(i(\theta+2\pi)Q_C)=\exp(i\theta Q_C),\qquad Q_C\in\mathbb Z.
$$

Test angle: `0.731000000000` rad.

| $Q_C$ | original phase | shifted phase | absolute error |
|---:|---:|---:|---:|
| `-2` | ` 0.108581823279-0.994087515088i` | ` 0.108581823279-0.994087515088i` | `7.078e-16` |
| `-1` | ` 0.744507160234-0.667614475847i` | ` 0.744507160234-0.667614475847i` | `3.140e-16` |
| `0` | ` 1.000000000000+0.000000000000i` | ` 1.000000000000+0.000000000000i` | `0.000e+00` |
| `1` | ` 0.744507160234+0.667614475847i` | ` 0.744507160234+0.667614475847i` | `3.140e-16` |
| `2` | ` 0.108581823279+0.994087515088i` | ` 0.108581823279+0.994087515088i` | `7.078e-16` |
| `3` | `-0.582827270429+0.812596069917i` | `-0.582827270429+0.812596069917i` | `2.956e-15` |

Maximum numerical error: `2.956e-15`.

Conclusion: periodicity comes from the integrity of $Q_C$, not from a fit of the potential.
