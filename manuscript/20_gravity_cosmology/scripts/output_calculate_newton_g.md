---
title: "Output — reduced calculation of G"
---

# Output — reduced calculation of G

## Structural inputs

- $\chi_{\rm Fano}=3\sqrt2/5=0.848528137424$
- $M_p=1.672621925950e-27\,{\rm kg}$

## Evaluated formula

$$
\Pi_G^{\rm GDQ}
=
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)}
$$

$$
G_{\rm GDQ}
=
\frac{\hbar c}{M_p^2}\Pi_G^{\rm GDQ}
$$

## Reduced GDQ result

| Case | $\alpha^{-1}$ | $\Pi_G^{\rm GDQ}$ | $G_{\rm GDQ}$ | error in $\Pi_G$ | error in $G$ |
|---|---:|---:|---:|---:|---:|
| Einstein geometric alpha | `137.036082448164` | `5.890395957250e-39` | `6.656497635372e-11` | `-0.266730%` | `-0.266730%` |
| recorded metrological alpha | `137.035999084000` | `5.890655846305e-39` | `6.656791325455e-11` | `-0.262330%` | `-0.262330%` |

## External comparison

| Quantity | Value used only for comparison |
|---|---:|
| $\Pi_G^{\rm obs}$ | `5.906149433384e-39` |
| $G_{\rm acc}$ | `6.674300000000e-11` m³ kg⁻¹ s⁻² |

## Classification

Strong phenomenological comparison. The accepted value does not enter the formula; it enters only in the final comparison.
The complete metrological closure requires the cosmological gravitational Hessian and the spectral calculation of the prefactor.
