---
title: "Saída — Hilbert operacional"
---

# Saída — Hilbert operacional

Classificação: teste de consistência algébrico-numérica.

Este teste não é uma previsão metrológica. Ele verifica, em dimensão
finita, a álgebra mínima esperada após a reconstrução operacional:
quociente por nulos, estados, observáveis, evolução unitária e
composição tensorial.

## Resultados

| Quantidade | Valor | Critério |
|---|---:|---|
| dimensão nula removida | 1 | $\ge 1$ neste toy model |
| dimensão física do quociente | 2 | `2` |
| erro de ortonormalização no quociente | 2.220e-16 | próximo de zero |
| $\operatorname{Tr}\varrho$ | 1.000000000000 | `1` |
| menor autovalor de $\varrho$ | -2.776e-17 | não negativo |
| menor probabilidade espectral | 0.166666666667 | não negativa |
| erro na soma das probabilidades | 2.220e-16 | próximo de zero |
| parte imaginária de $\langle A\rangle$ | 4.586e-19 | próxima de zero |
| erro de unitariedade de $U(t)$ | 4.527e-16 | próximo de zero |
| erro de preservação de norma | 2.220e-16 | próximo de zero |
| erro de fatorização tensorial | 2.776e-17 | próximo de zero |

## Interpretação

O teste confirma que, uma vez obtido o espaço físico positivo por
quociente, a linguagem operacional usual segue: estados normalizados,
matrizes densidade positivas, probabilidades espectrais, evolução
unitária por Hamiltoniano Hermitiano e composição por produto tensorial.

Na GDQ, essa camada é reconstruída a partir da geometria e não substitui
a ação oficial.
