---
title: "Saída — solíton gaussiano neutro"
---

# Saída — solíton gaussiano neutro

## Classificação

Verificação simbólico-numérica de uma solução explícita neutra. Não é previsão metrológica.

## Dados

- Dimensão real: $d=8$
- Escala geométrica: $\sigma=1.3$
- Amostras Monte Carlo: $500000$

## Equação de sóliton

$$
\phi=\frac{|x|^2}{4\sigma},
\qquad
\nabla_i\nabla_j\phi=\frac{1}{2\sigma}\delta_{ij}.
$$

| quantidade | valor |
|---|---:|
| $1/(2\sigma)$ | 3.846153846154e-01 |
| norma do resíduo de sóliton | 0.000000000000e+00 |

## Energia livre reduzida

$$
\mathcal W_{\rm gauss}
=
\left\langle\sigma|\nabla\phi|^2+\phi-d\right\rangle.
$$

| quantidade | analítico | Monte Carlo |
|---|---:|---:|
| $\langle |x|^2\rangle$ | 2.080000000000e+01 | 2.079299729017e+01 |
| $\langle\phi\rangle$ | 4.000000000000e+00 | 3.998653325033e+00 |
| $\langle\sigma|\nabla\phi|^2\rangle$ | 4.000000000000e+00 | 3.998653325033e+00 |
| $\mathcal W$ | 0.000000000000e+00 | -2.693349933821e-03 |
| erro padrão MC de $\mathcal W$ | — | 5.645521460939e-03 |

## Espectro escalar reduzido de Ornstein--Uhlenbeck

$$
\lambda_k=\frac{k}{2\sigma}.
$$

| $k$ | $\lambda_k$ |
|---:|---:|
| 0 | 0.000000000000e+00 |
| 1 | 3.846153846154e-01 |
| 2 | 7.692307692308e-01 |
| 3 | 1.153846153846e+00 |
| 4 | 1.538461538462e+00 |
| 5 | 1.923076923077e+00 |
| 6 | 2.307692307692e+00 |

Gap após remover o modo constante: $3.846153846154e-01$.

## Veredito

A solução gaussiana satisfaz exatamente a equação de sóliton neutro, tem $\mathcal W=0$ analiticamente e apresenta gap positivo no setor OU reduzido após remover o modo zero. Ela é referência neutra; carga, spin e massa de partículas reais exigem a ficha solitônica do setor correspondente.
