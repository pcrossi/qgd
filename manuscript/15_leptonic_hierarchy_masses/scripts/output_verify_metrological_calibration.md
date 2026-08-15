---
title: "Output — metrological calibration"
---

# Output — metrological calibration

## 1. Scale-independent Ratio

| scale $E_0$ | reconstructed $M_\mu/M_e$ |
|---:|---:|
| `1.000000` | `206.768593470629` |
| `7.300000` | `206.768593470629` |

The ratio does not change when the dimensional ruler is changed.

## 2. Calibration by $M_e$

| quantity | value |
|---|---:|
| $M_e$ used as metrological standard | `0.51099895000` MeV |
| $R_\mu^{\rm GDQ}$ | `206.768593470629` |
| $M_\mu=M_eR_\mu$ | `105.658534156` MeV |
| posterior reference $M_\mu$ | `105.658375500` MeV |
| relative error | `1.501598593930e-06` |

## 3. Beta Bridge as Calibration

$$
\delta_B=\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

| quantity | value |
|---|---:|
| $\delta_B$ | `2.530825921868` |
| $(\delta_B-1)M_e$ | `0.782250439` MeV |
| comparative $Q_\beta$ | `0.782333000` MeV |
| $M_e=Q_\beta/(\delta_B-1)$ | `0.51105288252` MeV |
| relative error of reconstructed $M_e$ | `1.055433002134e-04` |

## Classification

Verification of metrological calibration. The script does not derive the MeV unit without dimensional input; it shows how pure geometric numbers become energies after a declared physical ruler.
