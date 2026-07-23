---
title: "Torção homogênea como fluido rígido"
---

# Torção homogênea como fluido rígido

Esta nota preserva uma redução cosmológica simples. Ela não define a energia
escura da GDQ e não substitui a ação oficial. Seu objetivo é mostrar o que
uma 3-forma espacial homogênea produziria, no limite cosmológico efetivo, se
fosse tratada como setor torsional livre sobre uma métrica FLRW.

Considere

$$
ds^2=-dt^2+a(t)^2\gamma_{ij}dx^idx^j,
$$

e uma 3-forma puramente espacial homogênea

$$
B_{ijk}=b_0\varepsilon_{ijk},
$$

onde $\varepsilon_{ijk}$ é o volume espacial de referência e $b_0$ é constante
no setor homogêneo. Ao levantar índices com a métrica espacial
$a(t)^2\gamma_{ij}$, cada índice espacial contribui com um fator $a^{-2}$.
Portanto

$$
B_{\mu\nu\lambda}B^{\mu\nu\lambda}
=
B_{ijk}B^{ijk}
=
\frac{6b_0^2}{a^6}.
$$

Na redução efetiva com lagrangiano quadrático de 3-forma,

$$
\mathcal L_B
=
-\frac{1}{12}B_{\mu\nu\lambda}B^{\mu\nu\lambda},
$$

a densidade de energia homogênea escala como

$$
\rho_B
=
\frac{b_0^2}{2a^6}.
$$

A conservação de um fluido perfeito em FLRW é

$$
\dot\rho+3H(\rho+P)=0.
$$

Como $\rho_B\propto a^{-6}$,

$$
\dot\rho_B=-6H\rho_B.
$$

Substituindo na equação de conservação:

$$
-6H\rho_B+3H(\rho_B+P_B)=0.
$$

Para $H\neq0$, segue

$$
P_B=\rho_B.
$$

Logo

$$
\boxed{
w_B=\frac{P_B}{\rho_B}=1.
}
$$

Esse é um fluido rígido, ou stiff fluid. Ele dilui como $a^{-6}$ e não possui
a assinatura homogênea de energia escura, que exigiria

$$
w=-1.
$$

Na GDQ, a densidade de energia escura discutida no corpo do capítulo vem do
problema global de contorno, da tensão UV materializada e da projeção
cosmológica. A redução acima é útil para impedir a identificação indevida entre
torção homogênea livre e constante cosmológica.

