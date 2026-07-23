---
title: "Saída — gap eletromagnético do colar"
---

# Saída — gap eletromagnético do colar

| $L$ | modo zero | $\lambda_1^{\rm num}$ | $\pi^2/L^2$ | erro relativo |
|---:|---:|---:|---:|---:|
| `1.0` | `0.000e+00` | `9.8695917176e+00` | `9.8696044011e+00` | `1.285e-06` |
| `2.0` | `0.000e+00` | `2.4673979294e+00` | `2.4674011003e+00` | `1.285e-06` |
| `4.0` | `0.000e+00` | `6.1684948235e-01` | `6.1685027507e-01` | `1.285e-06` |
| `8.0` | `0.000e+00` | `1.5421237059e-01` | `1.5421256877e-01` | `1.285e-06` |
| `16.0` | `0.000e+00` | `3.8553092647e-02` | `3.8553142192e-02` | `1.285e-06` |

## Refinamento para $L=1$

| células | $\lambda_1^{\rm num}$ | erro relativo |
|---:|---:|---:|
| `50` | `9.8663578586e+00` | `3.289e-04` |
| `100` | `9.8687926854e+00` | `8.224e-05` |
| `200` | `9.8694014672e+00` | `2.056e-05` |
| `400` | `9.8695536673e+00` | `5.140e-06` |
| `800` | `9.8695917176e+00` | `1.285e-06` |

Como $L^2\lambda_1\to\pi^2$, segue que

$$
\lambda_1=\frac{\pi^2}{L^2}\to0
\quad\text{quando}\quad L\to\infty.
$$

O colar local infinito não fornece uma escala eletromagnética positiva;
a escala depende da colagem global ou da resolução setorial.
