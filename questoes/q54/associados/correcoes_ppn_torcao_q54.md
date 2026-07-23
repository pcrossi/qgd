# Q54 — Correções PPN e resíduos torsionais

## Objetivo

Registrar o que a Q54 prevê além da Relatividade Geral pura sem misturar
setores.

## Regime em que a RG é recuperada

A recuperação exata da forma de Einstein exige:

$$
\langle H\rangle_L=0,
\qquad
\langle \Pi_{\mu\nu}^{\rm tor}\rangle_L=0,
\qquad
\nabla_\mu f_R
\ \text{macroscopicamente suave}.
$$

Nesse regime:

$$
\gamma_{\rm PPN}=1,
\qquad
\beta_{\rm PPN}=1.
$$

## Possíveis correções

A conexão efetiva contém

$$
\Gamma^\mu{}_{\nu\rho}
=
\Gamma^{LC\,\mu}{}_{\nu\rho}
+\frac12H^\mu{}_{\nu\rho}.
$$

Se a média de $H$ não for nula, o movimento efetivo contém força torsional:

$$
a_H^\mu
=
-\frac12H^\mu{}_{\nu\rho}u^\nu u^\rho
+\text{termos de spin/polarização}.
$$

Para torção totalmente antissimétrica, o termo puramente geodésico simétrico
$H^\mu{}_{\nu\rho}u^\nu u^\rho$ se anula por antissimetria. As correções
observáveis exigem spin, polarização, rotação, borda ou anisotropia coletiva.

Assim, a expansão PPN efetiva deve ser escrita como:

$$
\gamma_{\rm PPN}
=
1+\delta\gamma_{\rm spin}
+\delta\gamma_{\rm rot}
+\delta\gamma_f
+\delta\gamma_{\partial},
$$

$$
\beta_{\rm PPN}
=
1+\delta\beta_{\rm spin}
+\delta\beta_{\rm rot}
+\delta\beta_f
+\delta\beta_{\partial}.
$$

## Interpretação física

- Corpos macroscópicos não polarizados: média de spin e torção tende a zero.
- Objetos compactos rotantes: torção residual pode sobreviver como correção
  de arrasto, precessão ou anisotropia.
- Interfaces e aparelhos: termos de borda podem alterar a resposta local,
  mas não redefinem $G$ global.
- Cosmologia: $\Lambda$ e $G$ pertencem à normalização global do espaço de
  Einstein, conforme Q38.

## Status

Este arquivo fecha a forma das correções permitidas, mas não fornece ainda
coeficientes metrológicos solares. Para obter esses coeficientes é necessário
construir o background estacionário do Sistema Solar na GDQ, projetar a
Hessiana física e extrair os termos de campo fraco.

