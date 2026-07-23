---
title: "Saída — kernels covariantes de calibre"
---

# Saída — kernels covariantes de calibre

Parâmetros: `q_n=1.0`, `m=1.0`, `s0=0.2`, `eta=0.2`, `Q^2=25.0`.

| kernel | $\Pi_K(0)$ | $\Pi_K(Q^2)$ | saturação $q_n^2\mathcal E_K(\eta)/(48\pi^2)$ | Ward tensorial |
|---|---:|---:|---:|---|
| `canonico` | `0.000000000000e+00` | `1.566659054231e-03` | `2.580841673285e-03` | preservada por covariância |
| `mistura` | `0.000000000000e+00` | `1.318042358895e-03` | `2.031733180500e-03` | preservada por covariância |
| `inteiro_plus` | `0.000000000000e+00` | `2.191605433540e-03` | `4.309066027165e-03` | preservada por covariância |

## Interpretação

Todos os kernels testados preservam $\Pi_K(0)=0$ e a forma transversal.
Os valores saturados diferem porque kernels diferentes representam resoluções espectrais diferentes.
O kernel canônico da GDQ é o semigrupo da Hessiana física, $K_0=e^{-sH}$.
