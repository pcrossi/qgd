---
title: "Saída — limite apontado torus/esfera"
---

# Saída — limite apontado torus/esfera

Classificação: verificação de consistência / toy model geométrico.

Janela local fixa: $0<r\le 1$.

| $R$ | erro máximo angular em $S^3_R$ | erro reescalado $E_R R^2$ |
|---:|---:|---:|
| 5 | 1.326242503606e-02 | 0.33156063 |
| 10 | 3.328892062082e-03 | 0.33288921 |
| 20 | 8.330556051532e-04 | 0.33322224 |
| 50 | 1.333262224253e-04 | 0.33331556 |
| 100 | 3.333288889207e-05 | 0.33332889 |
| 200 | 8.333305555719e-06 | 0.33333222 |

Conclusão: o erro local decai como $O(R^{-2})$, compatível com a
convergência apontada usada no Capítulo 6.

Nota: o círculo grande $S^1_R$ em coordenada de arco local já possui
métrica local plana; a não trivialidade global desaparece apenas no
limite apontado, não por identificação global.
