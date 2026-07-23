---
title: "Saída — fechamento torsão-Reynolds"
---

# Saída — fechamento torsão--Reynolds

| cenário | $\alpha$ | $R$ | $\tau_{\rm EM}$ | $\widehat\Lambda_{\rm EM}$ | $L/\ell_C$ | resíduo |
|:---|---:|---:|---:|---:|---:|---:|
| baixa energia — aproximação $1/137$ | `7.299270072992700e-03` | `1.037074352286` | `0.274900522514` | `1.907270174135` | `1.647167085290` | `8.674e-17` |
| referência metrológica externa | `7.297352569283802e-03` | `1.037142472813` | `0.274935020564` | `1.907150511011` | `1.647270435895` | `9.714e-17` |
| benchmark efetivo de alta energia — $1/128$ | `7.812500000000000e-03` | `1.019605676219` | `0.266136508154` | `1.938419512271` | `1.620698013873` | `-1.665e-16` |

Cada linha satisfaz numericamente:

$$
\operatorname{Re}_{\rm Q}=\alpha,
\qquad
x^3-4\tau x^2+\frac{\tau n_B^2}{\pi^2}=0.
$$

A linha $1/128$ é benchmark efetivo de alta energia, não entrada
fundamental do fechamento de baixa energia.
