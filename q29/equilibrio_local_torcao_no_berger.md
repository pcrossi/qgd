# Q29 — Equilíbrio local de torção no setor Berger

## 1. Vínculo vetorial

No junction estacionário,

$$
\mathbf T_a=t(q_a)\mathbf u_a,
$$

onde


$$
\mathbf u_1+\mathbf u_2+\mathbf u_3=0
$$

para as três direções separadas por $120^\circ$. O equilíbrio local é

$$
\mathbf C_{\rm loc}
=\sum_{a=1}^3t(q_a)\mathbf u_a=0.
$$

## 2. Modo comum

Na trajetória comum

$$
q_1=q_2=q_3=q,
$$

temos identicamente

$$
\mathbf C_{\rm loc}(q,q,q)
=t(q)\sum_a\mathbf u_a=0
$$

para todo $q$. Portanto,

$$
\frac{d^k}{dq^k}\mathbf C_{\rm loc}(q,q,q)=0
$$

em todas as ordens. O vínculo local não gera força nem curvatura ao longo do
squashing comum.

## 3. Modos relativos

Linearizando em $q_a=1+s_a$,

$$
D\mathbf C_{\rm loc}\,s
=t'(1)\sum_as_a\mathbf u_a.
$$

A matriz das três direções possui posto dois e kernel

$$
\ker D\mathbf C_{\rm loc}
=\operatorname{span}\{(1,1,1)\}.
$$

Assim, se as orientações $\mathbf u_a$ forem mantidas fixas, o equilíbrio
local elimina justamente os dois squashings relativos e deixa o modo comum —
que é o modo negativo de Berger.

Se as orientações também variarem, os modos relativos podem reaparecer como
combinações acopladas $(\delta q_a,\delta\theta_a)$, mas o modo comum continua
no kernel porque a identidade $\sum\mathbf u_a=0$ permanece válida.

## 4. Consequência

O equilíbrio local de torções é essencial para selecionar e manter o junction
$C_3$, mas não fornece rigidez absoluta contra uma deformação idêntica das três
gargantas:

$$
\boxed{
\mathbf C_{\rm loc}=0
\text{ restringe os modos relativos, não o modo comum.}
}
$$

Ele não estabiliza sozinho o squashing de Berger responsável pelo transporte
uniforme das normas $W/Y$.
