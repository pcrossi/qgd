---
title: "Bem-postura do fluxo geométrico GDQ em gauge"
---

# Bem-postura do fluxo geométrico GDQ em gauge

Esta nota registra o resultado técnico usado no Capítulo 5: o fluxo geométrico
da GDQ em $\tau$ é localmente bem posto depois de fixadas as degenerescências de
calibre. O enunciado não identifica $\tau$ com o tempo físico $t$ e não altera
a ação oficial.

## 1. O problema

O problema é estudar a evolução auxiliar de relaxamento geométrico

$$
\partial_\tau U=\mathcal P(U),
$$

com

$$
U=(g,H,\phi,\chi),
\qquad
f=\phi+i\chi.
$$

Aqui $g$ é a métrica Hermitiana/Riemanniana do bulk, $H$ é a torção de Bismut
quando a classe Hermitiana considerada a inclui, $\phi=\operatorname{Re}f$ e
$\chi=\operatorname{Im}f$.

A densidade continua sendo

$$
\rho=e^{-\phi}=e^{-(f+\bar f)/2}.
$$

O sistema estacionário associado à ação oficial é elíptico após calibre. O
fluxo em $\tau$ é parabólico após calibre. A evolução física reconstruída em
$t$ é outro problema.

## 2. Forma esquemática do fluxo

No setor torsional compatível com a conexão de Bismut, a parte geométrica pode
ser escrita, em notação real, como

$$
\partial_\tau g_{ij}
=
-2
\left(
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right)
+\text{termos de bordo ou normalização}.
$$

Para a torção, a parte principal é de Laplace--Hodge:

$$
\partial_\tau H
=
\Delta_{d,g}H
+\mathcal L_{\nabla\phi}H
+\text{termos de menor ordem}.
$$

Para os escalares:

$$
\partial_\tau\phi
=
\Delta_g\phi+\text{termos de menor ordem},
\qquad
\partial_\tau\chi
=
\Delta_g\chi+\text{termos de menor ordem},
$$

após escolher a convenção de sinal parabólica.

Os termos quadráticos $H_{ik\ell}H_j{}^{k\ell}$, $|H|^2$, $|\nabla\phi|^2$ e
os termos de transporte são de menor ordem para a classificação principal.

## 3. Por que é preciso fixar calibre

A equação de Ricci não é fortemente parabólica antes do calibre, porque a
ação é invariante por difeomorfismos. Essa degenerescência é geométrica, não
uma patologia física.

Escolhe-se uma métrica de referência fixa $\bar g$ e define-se o vetor de
DeTurck:

$$
W^k
=
g^{pq}
\left(
\Gamma^k_{pq}(g)-\Gamma^k_{pq}(\bar g)
\right).
$$

O fluxo métrico em gauge é

$$
\partial_\tau g_{ij}
=
-2
\left(
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right)
+\mathcal L_Wg_{ij}.
$$

O cancelamento de DeTurck troca a parte principal degenerada por

$$
\partial_\tau g_{ij}
=
g^{ab}\partial_a\partial_bg_{ij}
+\text{termos de menor ordem}.
$$

Para $H$, usa-se gauge de Hodge. Se $H=dA$ localmente, impõe-se

$$
d_g^\dagger A=0.
$$

Então a parte principal torsional é

$$
\partial_\tau H
=
g^{ab}\nabla_a\nabla_bH
+\text{termos de menor ordem}.
$$

## 4. Símbolo principal

No gauge fixado, o sistema tem a forma quase-linear

$$
\partial_\tau U
=
\mathcal A^{ab}(U)\partial_a\partial_bU
+\mathcal B(U,\partial U),
$$

com símbolo principal

$$
\sigma_{\rm pr}(\xi)
=
|\xi|_g^2 I.
$$

Como o bulk é Riemanniano no problema de fluxo,

$$
|\xi|_g^2=g^{ab}\xi_a\xi_b>0
\qquad
\text{para }\xi\ne0.
$$

Logo o sistema em gauge é fortemente parabólico enquanto $g$ permanecer
uniformemente positiva.

## 5. Espaços funcionais

Uma formulação em Hölder parabólico usa dados

$$
g_0,H_0,\phi_0,\chi_0\in C^{k,\alpha},
\qquad
k\ge2,
\qquad
0<\alpha<1,
$$

com

$$
g_0\ge\lambda\bar g
\qquad
\text{para algum }\lambda>0,
$$

e compatibilidades

$$
dH_0=0,
\qquad
\int_Me^{-\phi_0}dV_{g_0}=1,
\qquad
\rho_0=e^{-\phi_0}>0.
$$

Então a solução em gauge pertence localmente a

$$
U\in C^{1+\alpha/2,\,2+\alpha}([0,T]\times M).
$$

Em Sobolev, para $d=\dim_{\mathbb R}M=8$, pode-se tomar

$$
U_0\in H^s,
\qquad
s>\frac d2+2=6,
$$

por exemplo $s\ge7$.

## 6. Teorema local

Sob as hipóteses acima, existe $T>0$ e uma solução única em gauge

$$
U(\tau)=(g(\tau),H(\tau),\phi(\tau),\chi(\tau)),
\qquad
0\le\tau\le T.
$$

Além disso:

1. se $U_0$ é suave, então $U(\tau)$ é suave para $\tau>0$;
2. o mapa $U_0\mapsto U(\tau)$ depende continuamente dos dados;
3. no sistema geométrico sem gauge, a unicidade é módulo difeomorfismos.

Para desfazer o gauge, resolve-se

$$
\frac{d}{d\tau}\Phi_\tau
=
-W(g(\tau))\circ\Phi_\tau,
\qquad
\Phi_0=\operatorname{id},
$$

e transporta-se

$$
\tilde g=\Phi_\tau^*g,
\qquad
\tilde H=\Phi_\tau^*H,
\qquad
\tilde f=\Phi_\tau^*f.
$$

## 7. Critério de continuação

A solução pode ser continuada além de $T$ enquanto a geometria permanecer
uniformemente controlada. Um critério suficiente é

$$
0<\lambda\bar g\le g(\tau)\le\Lambda\bar g<\infty,
$$

e

$$
\sup_{[0,T)\times M}
\left(
|{\rm Rm}(g)|
+|H|^2
+|\nabla H|^2
+|\nabla\phi|^2
+|\nabla^2\phi|
+|\nabla\chi|^2
+|\nabla^2\chi|
\right)
<\infty.
$$

Também se mantém

$$
\rho=e^{-\phi}>0
$$

e as condições de bordo/gauge do setor.

Portanto, falha em tempo finito significa perda de uma dessas condições:
degeneração métrica, explosão de curvatura, explosão torsional, perda de
regularidade de $f$, aparecimento de zero de densidade ou incompatibilidade de
bordo.

## 8. Relação com monotonicidade

A monotonicidade de Perelman--Bismut, quando válida no setor, fornece controle
de estabilidade e atratores. Ela não substitui a bem-postura local.

Assim, a cadeia correta é:

$$
\text{calibre}
\to
\text{símbolo parabólico forte}
\to
\text{existência, unicidade e dependência contínua}
\to
\text{critério de continuação}.
$$

Só depois entram funcionais de Lyapunov, monotonicidade e análise assintótica.

