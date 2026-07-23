---
title: "Conexão de Ehresmann como ponte didática para calibre efetivo"
---

# Conexão de Ehresmann como ponte didática para calibre efetivo

Esta nota preserva uma forma intuitiva de ler campos de calibre como geometria
de colagem interna. Ela é uma ponte didática, não uma nova ação fundamental.

Considere localmente uma fibra toroidal com coordenadas angulares $\theta^a$.
Sem acoplamento, as 1-formas verticais são simplesmente

$$
d\theta^a.
$$

Uma conexão de Ehresmann separa direções horizontais e verticais por meio de
formas modificadas

$$
\boxed{
\Theta^a=d\theta^a+g_aA^a.
}
$$

Aqui $A^a=A_\mu^adx^\mu$ é a componente local da conexão efetiva vista no
espaço projetado, e $g_a$ é a normalização do respectivo canal. Sob mudança
local de trivialização da fibra,

$$
\theta^a\mapsto\theta^a-\lambda^a(x),
$$

temos

$$
d\theta^a\mapsto d\theta^a-d\lambda^a.
$$

Para que $\Theta^a$ permaneça geometricamente bem definida, a conexão deve
transformar como

$$
A^a\mapsto A^a+\frac{1}{g_a}d\lambda^a.
$$

Essa é a transformação usual de calibre no setor abeliano reduzido. No caso
não abeliano, a mesma ideia é substituída por uma conexão em um fibrado
vetorial interno:

$$
A_\mu
=
G_\mu^aT_a
+
W_\mu^it_i
+
B_\mu Y.
$$

O ponto físico é que calibre aparece como liberdade de escolher frames e
horizontais internas sem alterar os observáveis geométricos. Isso se ajusta à
definição usada no capítulo:

$$
G_{\rm eff}
=
\operatorname{Aut}_{\rm GDQ}(E_{\rm int}).
$$

Portanto, a linguagem de Ehresmann pode ajudar a visualizar a origem
geométrica de $A_\mu$, mas o fundamento continua sendo:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\text{conexões efetivas reconstruídas}.
$$

