# Output — reduced GDQ vs standard comparison

Classification: phenomenological/controlled comparison in the Madelung sector on a fixed background.

## What was compared

1. standard coherent: two Gaussians with full cross-term;
2. standard incoherent: `I1+I2` mixture;
3. reduced GDQ: cross-term multiplied by `exp(-Gamma_det)`.

## Parameters

- `lambda_det = 1.1`
- `L = 1.0`
- `R_det = 1.374142841025`
- `C_path = 1.0`

## Table

| zeta_det | Gamma_det | exp(-Gamma_det) |
|---:|---:|---:|
| 0 | 0.000000000 | 1.000000000 |
| 0.5 | 0.171767855 | 0.842174657 |
| 1.25 | 1.073549095 | 0.341793305 |
| 2.5 | 4.294196378 | 0.013647535 |

## Figure

![Reduced GDQ vs standard comparison](comparacao_gdq_padrao_dupla_fenda.png)

## Interpretation

The reduced GDQ coincides with the coherent standard when `zeta_det=0` and tends to the incoherent standard when `Gamma_det` grows. The distinctive feature is not the existence of fringes, but the geometric law of coherence loss via DtN/Schur impedance:

$$
\Gamma_{\rm det}=\frac12\zeta_{\rm det}^2C_{\rm path}\lambda_{\rm det}\coth(\lambda_{\rm det}L).
$$
