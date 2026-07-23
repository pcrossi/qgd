---
title: "Saída — Hessiana CP e susceptibilidade"
---

# Saída — Hessiana CP e susceptibilidade

Potencial reduzido:

$$
V(\theta)=\chi(1-\cos\theta).
$$

Usado $\chi=1$ e passo de diferença finita `h=1.0e-04` apenas para verificar a identidade.

| $\theta$ | Hessiana analítica | Hessiana numérica | Classificação |
|---:|---:|---:|---|
| `0.000000000000` | `1.000000000000` | `0.999999993923` | mínimo estável |
| `1.570796326795` | `0.000000000000` | `0.000000011102` | ponto plano da projeção angular |
| `3.141592653590` | `-1.000000000000` | `-0.999999993923` | máximo instável |
| `6.283185307180` | `1.000000000000` | `0.999999993923` | mínimo estável |

Conclusão: no canal torsional, $\chi_{\rm top}^{\rm GDQ}>0$ é exatamente a curvatura positiva do mínimo CP.
