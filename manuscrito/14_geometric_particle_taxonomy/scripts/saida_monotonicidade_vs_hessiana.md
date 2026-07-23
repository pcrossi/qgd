---
title: "Saída — monotonicidade versus Hessiana"
---

# Saída — monotonicidade versus Hessiana

## Classificação

Ilustração simbólico-numérica de critério de estabilidade. Não é previsão física.

## Modelos

$$
E_{\rm min}=\frac12(x^2+2y^2),
\qquad
E_{\rm sela}=\frac12(x^2-y^2).
$$

Fluxo usado:

$$
\dot X=-\nabla E=-HX.
$$

## Hessianas

| caso | autovalores da Hessiana | interpretação |
|---|---:|---|
| mínimo | [1.0, 2.0] | estável |
| sela | [-1.0, 1.0] | instável por direção negativa |

## Evolução

| caso | energia inicial | energia final | energia monotônica? | razão final/inicial da norma |
|---|---:|---:|---|---:|
| mínimo | 3.600000000000e-01 | 1.888484348023e-06 | True | 2.356769805584e-03 |
| sela | 3.000000000000e-01 | -3.006324021355e+03 | True | 9.403259799496e+01 |

## Veredito

A energia pode ser monotônica ao longo do fluxo mesmo quando o ponto crítico é uma sela. Portanto, para a GDQ, monotonicidade de Perelman--Bismut é condição de Lyapunov, mas estabilidade de sóliton exige Hessiana física sem autovalores negativos após projetar gauge, simetrias e moduli.
