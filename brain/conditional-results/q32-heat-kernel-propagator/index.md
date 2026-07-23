---
title: "Q32 — propagador como kernel de calor da Hessiana GDQ"
status: structural-closed
source: "manuscrito/04_action_consistency/notes/hessiana_kernel_calor_propagador.md"
updated: 2026-07-21
---

# Q32 — propagador como kernel de calor da Hessiana GDQ

## Estado vigente

A origem estrutural do propagador modificado está fechada no setor declarado.
O fator gaussiano não é um regulador externo inserido manualmente; ele é o
limite plano do semigrupo de calor gerado pela Hessiana normalizada da ação
oficial da GDQ.

## Fórmulas canônicas

Ao redor de um background estacionário
$\Phi_*=(g_*,f_*,\bar f_*)$:

$$
\mathcal O_{\rm Hess}^{(2)}
=
\tau L_{\rm GDQ}^{(2)}.
$$

Portanto:

$$
K_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}.
$$

No limite plano euclidiano:

$$
G_\tau(p_E)
=
\frac{e^{-\tau p_E^2}}{p_E^2+m^2}
=
\frac{e^{-p_E^2/\widehat\Lambda_\tau^2}}{p_E^2+m^2},
\qquad
\widehat\Lambda_\tau=\tau^{-1/2}.
$$

## Consequência

Como $e^{-z}$ é uma função inteira e nunca se anula, o fator de calor não cria
polos novos. A ausência completa de fantasmas físicos continua condicionada ao
projetor físico, ao domínio autoadjunto e à reconstrução causal apropriada.

## Verificações

Scripts autocontidos:

1. `manuscrito/04_action_consistency/scripts/verificar_kernel_calor_propagador.py`;
2. `manuscrito/04_action_consistency/scripts/verificar_hessiana_escalar_reduzida.py`.

