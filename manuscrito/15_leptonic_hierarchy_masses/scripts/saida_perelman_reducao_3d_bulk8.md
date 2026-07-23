---
title: "Saída — redução Perelman 3D no bulk 8D"
---

# Saída — redução Perelman 3D no bulk 8D

## Entrada

| quantidade | valor |
|---|---:|
| dimensão do fator curvo $B_3$ | `3` |
| dimensão do fator espectador $K_5$ | `5` |
| $\|\operatorname{Ric}(g_K)\|$ | `0.0` |
| $\|\nabla_K f\|$ | `0.0` |
| $\|H_{BK}\|$ | `0.0` |

## Identidade verificada

Para $g_8=g_B\oplus g_K$, vale:

$$
\operatorname{Ric}(g_8)
=
\operatorname{Ric}(g_B)\oplus\operatorname{Ric}(g_K).
$$

Com $\operatorname{Ric}(g_K)=0$, o fluxo no fator espectador congela:

$$
\partial_\tau g_K=0.
$$

A singularidade admissível tem forma produto:

$$
\Sigma_{\rm sing}^{(8)}
=
\Sigma_{\rm sing}^{(3)}\times K_5.
$$

## Veredito

- setor produto válido: `True`;
- Perelman é usado apenas no fator tridimensional curvo;
- o toro classifica holonomia/carga/fase, mas não gera a cirurgia.
