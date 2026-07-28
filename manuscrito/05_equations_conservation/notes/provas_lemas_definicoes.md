---
title: "Provas, lemas e definições — Capítulo 5"
---

# Provas, lemas e definições — Capítulo 5

Esta nota registra o conteúdo técnico associado às equações de movimento e às
leis de conservação.

| Item | Forma de inserção | Status |
|---|---|---|
| Variação em $f,\bar f$ ou $\rho,S_R$ | Prova no corpo/notas | Demonstrada setorialmente |
| Continuidade da fase | Derivação variacional/Noether | Demonstrada no setor |
| Hamilton--Jacobi--Bohm | Derivação reduzida | Condicional ao setor Madelung |
| Termo de Bohm | Derivado da variação da densidade/Fisher | Demonstrado no setor regular |
| Noether geral | Prova completa | Demonstrada |
| Corrente por deslocamento de fase $S_R$ | Aplicação de Noether | Demonstrada |
| Variação métrica ponderada | Prova com dependência da medida | Demonstrada/condicional ao domínio |
| Tratamento covariante dos vínculos | Restrição ao espaço tangente e projeção da Hessiana | Método vigente; Dirac--Bergmann é reformulação opcional |

## Resultado condicionado

$$
\Pi_{S_R}=\rho
$$

não é identidade off-shell universal da ação oficial. Ela entra como
polarização/redução física do setor de Madelung, conectada ao Cap. 6 e à teoria
da medida.

O núcleo algébrico dessa redução possui certificação complementar em
[RouthMadelung.lean](../../../formal/GDQ/RouthMadelung.lean). Para uma
discretização finita com $\rho_i>0$, o módulo define

$$
\mathcal E[\Pi,\rho]
=
\sum_i\frac{\Pi_i^2}{\rho_i}
$$

e prova por completação exata do quadrado que, quando
$\sum_i\rho_i=\sum_i\Pi_i=1$,

$$
\mathcal E
=
1+
\sum_i\frac{(\Pi_i-\rho_i)^2}{\rho_i}.
$$

Logo o excesso é não negativo e se anula se, e somente se,
$\Pi_i=\rho_i$ em todo ponto da discretização. Isso certifica a unicidade
algébrica do mínimo normalizado. Não formaliza ainda o limite contínuo nem a
dinâmica dissipativa que leva o sistema físico a esse mínimo.

## Certificação da identidade de Noether

O módulo [NoetherIdentity.lean](../../../formal/GDQ/NoetherIdentity.lean)
formaliza a etapa algébrica universal

$$
\delta L
=
E(\Phi)\cdot\delta\Phi+\operatorname{div}\Theta
=
\operatorname{div}B
$$

e deduz, sem usar as equações de movimento,

$$
\operatorname{div}(\Theta-B)
=
-E(\Phi)\cdot\delta\Phi.
$$

No setor on-shell, $E(\Phi)=0$, segue a conservação. As duas fórmulas de
primeira variação e o desaparecimento do fluxo lateral continuam sendo
verificados na ação oficial e no contorno físico; o certificado Lean não os
postula silenciosamente.

## Revisão didática de 2026-07-19

O status do capítulo permanece: primeira variação de bulk fechada e dinâmica
canônica de laboratório condicional. A corrente de fase, o operador
Fisher--Bohm, a variação métrica ponderada e Noether estão demonstrados no
corpo/notas. A identificação $\Pi_{S_R}=\rho$ é mantida como polarização
física reduzida, não como identidade off-shell da ação oficial.
