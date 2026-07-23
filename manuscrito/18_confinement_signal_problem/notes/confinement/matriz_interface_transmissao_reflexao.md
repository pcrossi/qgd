---
title: "Matriz de interface por Hessiana"
---

# Matriz de interface por Hessiana

Com impedância Hermitiana $\mathsf Z=\mathsf Z^\dagger$, a transformada de
Cayley:

$$
\mathsf S
=
(I-i\mathsf Z)(I+i\mathsf Z)^{-1}
$$

é unitária:

$$
\mathsf S^\dagger\mathsf S=I.
$$

Se há dissipação de aparelho ou canal aberto, substitui-se $\mathsf Z$ por um
operador maximal dissipativo, obtendo:

$$
\mathsf S^\dagger\mathsf S\le I.
$$

Na GDQ, $\mathsf Z$ é a impedância extraída da Hessiana física reduzida na
interface. A construção mínima é:

$$
K_{\rm GDQ}
=
\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast].
$$

O projetor físico separa flutuações observáveis de redundâncias de gauge,
modos nulos de bordo e variações que violam os vínculos conservados:

$$
K_{\rm phys}
=
P_{\rm phys}K_{\rm GDQ}P_{\rm phys}.
$$

No domínio de interface, a solução elíptica com dado de Dirichlet $\varphi$
define o operador Dirichlet--to--Neumann:

$$
\Lambda_{\rm DtN}\varphi
=
\nabla_n\delta\Phi_\varphi\big|_{\Sigma}.
$$

A impedância reduzida é então:

$$
\mathsf Z_\Sigma
=
Z_0^{-1}\Lambda_{\rm DtN}^{\rm phys},
$$

com $Z_0$ apenas normalizando unidades internas do canal reduzido. Em uma
interface fechada sem perda, $\mathsf Z_\Sigma$ é Hermitiana; por isso a
transformada de Cayley gera $\mathsf S$ unitária. Se o aparelho ou banho
macroscópico abre canais, a parte dissipativa torna $\mathsf S$ contrativa.
