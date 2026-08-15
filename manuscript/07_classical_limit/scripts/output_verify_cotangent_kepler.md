---
title: "Output — cotangent to Kepler"
---

# Output — cotangent to Kepler

Classification: asymptotic consistency verification.

Fixed local radius: $r=1$.

| $R$ | $R^{-1}\cot(r/R)$ | error against $1/r$ | error with correction $-r/(3R^2)$ | error$\cdot R^2$ |
|---:|---:|---:|---:|---:|
| 5 | 0.986630975117 | 1.336902e-02 | 3.569155e-05 | 0.33422562 |
| 10 | 0.996664442326 | 3.335558e-03 | 2.224341e-06 | 0.33355577 |
| 20 | 0.999166527745 | 8.334723e-04 | 1.389220e-07 | 0.33338890 |
| 50 | 0.999866663111 | 1.333369e-04 | 3.555691e-09 | 0.33334222 |
| 100 | 0.999966666444 | 3.333356e-05 | 2.222245e-10 | 0.33333556 |
| 200 | 0.999991666653 | 8.333347e-06 | 1.388889e-11 | 0.33333389 |

Conclusion: the cotangent kernel tends locally to the Kepler potential,
with leading correction of order $R^{-2}$.
