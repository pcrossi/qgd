---
title: "Saída — calibração metrológica"
---

# Saída — calibração metrológica

## 1. Razão independente de escala

| escala $E_0$ | $M_\mu/M_e$ reconstruído |
|---:|---:|
| `1.000000` | `206.768593470629` |
| `7.300000` | `206.768593470629` |

A razão não muda quando a régua dimensional é trocada.

## 2. Calibração por $M_e$

| quantidade | valor |
|---|---:|
| $M_e$ usado como padrão metrológico | `0.51099895000` MeV |
| $R_\mu^{\rm GDQ}$ | `206.768593470629` |
| $M_\mu=M_eR_\mu$ | `105.658534156` MeV |
| referência posterior $M_\mu$ | `105.658375500` MeV |
| erro relativo | `1.501598593930e-06` |

## 3. Ponte beta como calibração

$$
\delta_B=\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

| quantidade | valor |
|---|---:|
| $\delta_B$ | `2.530825921868` |
| $(\delta_B-1)M_e$ | `0.782250439` MeV |
| $Q_\beta$ comparativo | `0.782333000` MeV |
| $M_e=Q_\beta/(\delta_B-1)$ | `0.51105288252` MeV |
| erro relativo de $M_e$ reconstruído | `1.055433002134e-04` |

## Classificação

Verificação de calibração metrológica. O script não deriva a unidade MeV
sem entrada dimensional; ele mostra como números geométricos puros viram
energias após uma régua física declarada.
