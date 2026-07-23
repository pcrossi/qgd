---
title: "Saída — ausência de polo de Landau U(1)"
---

# Saída — ausência de polo de Landau $U(1)$

## Entrada

$$
\alpha_0=0.0072973525692838,\qquad \eta=\tau m^2=1.000000e-06.
$$

$\eta$ é cenário de teste para verificar a fórmula; não é ajustado.

## Polarização

| $r=q_E^2/m^2$ | $\Pi_\eta(r)$ | refinado | diferença |
|---:|---:|---:|---:|
| `0.000e+00` | `0.000000000000e+00` | `0.000000000000e+00` | `0.000e+00` |
| `1.000e-04` | `1.548528170568e-08` | `1.548528170551e-08` | `1.780e-19` |
| `1.000e+00` | `1.403667635586e-04` | `1.403667635568e-04` | `1.772e-15` |
| `1.000e+04` | `5.839829955199e-03` | `5.839819263783e-03` | `1.069e-08` |
| `1.000e+08` | `1.024958035521e-02` | `1.024957951792e-02` | `8.373e-10` |
| `1.000e+12` | `1.025005713135e-02` | `1.025005713135e-02` | `8.674e-18` |

## Saturação e condição sem polo

$$
\Pi_\eta(\infty)=1.025005713135e-02,\qquad \alpha_{\rm eff}^{-1}(\infty)=135.631372264.
$$

- monotonicidade: `True`;
- limitado pelo valor assintótico: `True`;
- condição sem polo no cenário: `True`;
- resíduo tensorial de Ward: `1.863e-20`.

## Refinamento em $r=10^4$

| pontos Simpson | $\Pi_\eta(10^4)$ |
|---:|---:|
| `100` | `5.83983398909937e-03` |
| `200` | `5.83983021324379e-03` |
| `400` | `5.83982997048119e-03` |
| `800` | `5.83982995519932e-03` |
| `1600` | `5.83981926378274e-03` |

Erro entre as duas últimas ordens: `1.069e-08`.

## Limite de baixa energia

| $r$ | $\eta=10^{-12}$ | limite $\eta\to0$ | diferença |
|---:|---:|---:|---:|
| `1.000e-04` | `1.548529719117e-08` | `1.548529719196e-08` | `7.863e-19` |
| `1.000e+00` | `1.403669184112e-04` | `1.403669184116e-04` | `4.122e-16` |
| `1.000e+04` | `5.841328318906e-03` | `5.841328484792e-03` | `1.659e-10` |

## Classificação

Avaliação direta da fórmula derivada. O teste demonstra saturação para
$\eta>0$ e recuperação do limite logarítmico em baixa energia.
