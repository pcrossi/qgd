---
title: "Saída — cotangente para Kepler"
---

# Saída — cotangente para Kepler

Classificação: verificação assintótica de consistência.

Raio local fixo: $r=1$.

| $R$ | $R^{-1}\cot(r/R)$ | erro contra $1/r$ | erro com correção $-r/(3R^2)$ | erro$\cdot R^2$ |
|---:|---:|---:|---:|---:|
| 5 | 0.986630975117 | 1.336902e-02 | 3.569155e-05 | 0.33422562 |
| 10 | 0.996664442326 | 3.335558e-03 | 2.224341e-06 | 0.33355577 |
| 20 | 0.999166527745 | 8.334723e-04 | 1.389220e-07 | 0.33338890 |
| 50 | 0.999866663111 | 1.333369e-04 | 3.555691e-09 | 0.33334222 |
| 100 | 0.999966666444 | 3.333356e-05 | 2.222245e-10 | 0.33333556 |
| 200 | 0.999991666653 | 8.333347e-06 | 1.388889e-11 | 0.33333389 |

Conclusão: o kernel cotangente tende localmente ao potencial de Kepler,
com correção principal de ordem $R^{-2}$.
