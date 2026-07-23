---
title: "Saída — circulação Wallstrom"
---

# Saída — circulação Wallstrom

Classificação: teste simbólico/topológico.

## Mapas $S^1\to S^1$

| parâmetro $\alpha$ | fase fecha? | defeito $|e^{i2\pi\alpha}-1|$ | enrolamento formal |
|---:|---:|---:|---:|
| -2 | True | 4.898587e-16 | -2 |
| -1 | True | 2.449294e-16 | -1 |
| 0 | True | 0.000000e+00 | 0 |
| 1 | True | 2.449294e-16 | 1 |
| 2 | True | 4.898587e-16 | 2 |
| 0.5 | False | 2.000000e+00 | 0.5 |
| 1.3 | False | 1.618034e+00 | 1.3 |

Conclusão: a integral pode ser formalmente calculada para qualquer
$\alpha$, mas apenas inteiros fecham o mapa global regular
$S^1\to S^1$.

## Exemplo de fluxo de Chern em $T^2$

Para $F=N(2\pi)^{-1}dx\wedge dy$ em $[0,2\pi)^2$:

| parâmetro $N$ | $(2\pi)^{-1}\int_{T^2}F$ | fluxo inteiro? |
|---:|---:|---:|
| -2 | -2.000000000000 | True |
| -1 | -1.000000000000 | True |
| 0 | 0.000000000000 | True |
| 1 | 1.000000000000 | True |
| 3 | 3.000000000000 | True |
| 0.5 | 0.500000000000 | False |

Conclusão adicional: a curvatura pode ser escrita formalmente com qualquer
$N$, mas apenas classes inteiras representam a primeira classe de Chern de
um fibrado de linha $U(1)$ globalmente admissível.
