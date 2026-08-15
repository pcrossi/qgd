---
title: "Output — leptonic backreaction and muonic hydrogen"
---

# Output — leptonic backreaction and muonic hydrogen

| Quantity | Value |
|---|---:|
| $(\mu_{ep}/\mu_{\mu p})^3$ | `1.555489846615637e-07` |
| $\Delta E_{\rm fs}^H(2s)$ | `5.715065961503e-10` eV |
| $\Delta E_{\rm fs}^{\mu H}(2s)$ | `3.674126175711` meV |
| amplification $\mu H/H$ | `6.428842992294e+06` |

## Diagnostic table of radius backreaction

The table below does not fix the absolute contraction of the proton. It only
propagates the contact variational ratio between the electronic probe and the
muonic probe:

$$
\frac{\delta r_p[e]}{\delta r_p[\mu]}
=
\left(\frac{\mu_{ep}}{\mu_{\mu p}}\right)^3.
$$

| assumed muonic contraction | estimated electronic contraction |
|---:|---:|
| `-0.010000` fm | `-1.555489846616e-09` fm |
| `-0.030000` fm | `-4.666469539847e-09` fm |
| `-0.034000` fm | `-5.288665478493e-09` fm |

The absolute value of $\delta r_p[\mu]$ requires the surface Hessian
of the proton, i.e., $H_p^{\rm surf}$ and the source $J_\mu$ calculated
directly from the official action.

Conclusion: electronic backreaction exists, but it is about seven orders of magnitude smaller than the muonic one.
