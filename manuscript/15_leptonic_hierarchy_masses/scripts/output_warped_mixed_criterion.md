---
title: "Output — warped/mixed criterion"
---

# Output — warped/mixed criterion

## Formulas

$$
m_\perp^2
=
C_\gamma\tau R_{\max}^{-2}
-
\sum_i c_i a_i^2.
$$

$$
j_{\rm mix}=\sum_i b_i a_i.
$$

$$
\Delta_{\rm Schur}
=
\frac{j_{\rm mix}^2}{m_\perp^2}.
$$

Stable/subcritical if:

$$
\Delta_{\rm Schur}<\lambda_B^{\rm gap}.
$$

## Normalized Scenarios

| scenario | $m_\perp^2$ | $j_{\rm mix}$ | $\Delta_{\rm Schur}$ | ratio/gap | status |
|---|---:|---:|---:|---:|---|
| product | 1 | 0 | 0 | 0 | subcritical |
| weak_one_channel_0p1 | 0.99 | 0.1 | 0.010101010101 | 0.010101010101 | subcritical |
| four_channels_0p1 | 0.96 | 0.4 | 0.166666666667 | 0.166666666667 | subcritical |
| one_channel_critical_lambda1 | 0.5 | 0.707106781187 | 1 | 1 | critical |
| one_channel_supercritical_0p8 | 0.36 | 0.8 | 1.77777777778 | 1.77777777778 | supercritical |

## One-channel Threshold

For a single active mixed channel with $\lambda_B^{\rm gap}=1$:

$$
a_{\rm crit}=\frac1{\sqrt2}\simeq0.707106781187.
$$

Below this value, the warped/mixed mixture does not alter the critical index.
Above it, the background may generate an additional mode, which must be
classified as a resonance, boundary state, or composite state
until proof of primitive charge and asymptotic stability.
