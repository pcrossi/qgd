---
title: "Saída — separação de escalas"
---

# Saída — separação de escalas

## 1. Escala do kernel de calor

| $\tau$ | $\widehat\Lambda_\tau=\tau^{-1/2}$ |
|---:|---:|
| `1.000000e+00` | `1.000000000000e+00` |
| `2.500000e-01` | `2.000000000000e+00` |
| `1.000000e-02` | `1.000000000000e+01` |
| `1.000000e-04` | `1.000000000000e+02` |

## 2. Por que $m_e$ não pode ser corte universal duro

A tabela mostra $\log_{10}\{\exp[-(E/\Lambda)^2]\}$.

| energia externa $E$ [GeV] | corte $m_e$ | corte $1$ GeV |
|---:|---:|---:|
| `5.109989500e-04` | `-4.342945e-01` | `-1.134029e-07` |
| `1.000000000e-02` | `-1.663199e+02` | `-4.342945e-05` |
| `1.000000000e+00` | `-1.663199e+06` | `-4.342945e-01` |
| `1.000000000e+02` | `-1.663199e+10` | `-4.342945e+03` |
| `1.300000000e+04` | `-2.810807e+14` | `-7.339577e+07` |

Valores muito negativos significam supressão efetivamente nula.
Assim, $m_e$ ou $1$ GeV não podem ser lidos como parede universal de energia externa.

## 3. Massa como deslocamento espectral

Para $p_E=10.0$ GeV, com $\lambda_i=p_E^2+m_i^2$:

| setor | $m_i$ [GeV] | $p_E^2$ | $m_i^2$ | $\lambda_i$ | fração $m_i^2/\lambda_i$ |
|---|---:|---:|---:|---:|---:|
| `eletron` | `5.109989500e-04` | `1.000000000e+02` | `2.611199269e-07` | `1.000000003e+02` | `2.611199262e-09` |
| `hadronico_1GeV` | `1.000000000e+00` | `1.000000000e+02` | `1.000000000e+00` | `1.010000000e+02` | `9.900990099e-03` |
| `eletrofraco_100GeV` | `1.000000000e+02` | `1.000000000e+02` | `1.000000000e+04` | `1.010000000e+04` | `9.900990099e-01` |

## Conclusão

$\Lambda_C$, $\widehat\Lambda_\tau$ e $m_i$ têm funções distintas.
A massa altera o espectro do setor; a resolução vem de $\tau$; a ação usa $\Lambda_C$ como número adimensional normalizado.
