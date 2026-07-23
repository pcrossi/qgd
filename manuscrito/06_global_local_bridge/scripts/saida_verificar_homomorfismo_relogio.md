---
title: "Saída — homomorfismo causal do relógio"
---

# Saída — homomorfismo causal do relógio

Classificação: verificação simbólico-numérica de consistência.

Parâmetros didáticos: $\tau_0=2.0$, $\kappa=0.37$.

| $t_1$ | $t_2$ | $f(t_1+t_2)$ | $f(t_1)f(t_2)$ | defeito |
|---:|---:|---:|---:|---:|
| -1.00 | 0.25 | 0.757675564603 | 0.757675564603 | 0.000e+00 |
| 0.10 | 0.90 | 1.447734614663 | 1.447734614663 | 2.220e-16 |
| 1.00 | 2.00 | 3.034358394436 | 3.034358394436 | 0.000e+00 |
| -0.40 | 1.70 | 1.617691284902 | 1.617691284902 | 2.220e-16 |

Derivada numérica de $\log\tau_\gamma(t)$ em $t=0.8$: `0.370000000000`.

Conclusão: o pullback da forma logarítmica satisfaz
$\gamma^*(d\tau/\tau)=\kappa dt$ no relógio exponencial.
Isto verifica a forma matemática do teorema condicional; não deriva por
si só a dinâmica física completa do aparelho.
