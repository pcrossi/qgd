# Q29 — Redução eletromagnética de Hopf em dois patches

## 1. Atlas global já verificado

Nas cartas norte e sul de $S^2$, a conexão de Hopf satisfaz

$$
\mathcal A_S
=
\mathcal A_N-d\chi,
$$

enquanto as coordenadas da fibra obedecem

$$
\psi_S=\psi_N+\chi.
$$

Portanto, a $1$-forma

$$
\eta
=
d\psi_N+\mathcal A_N
=
d\psi_S+\mathcal A_S
$$

é global. O script da Q42 verificou a transição e a igualdade dos projetores
com erros inferiores a $3\times10^{-16}$.

## 2. Inserção eletromagnética externa

Introduza a excitação física sem modificar a colagem interna:

$$
\eta_Q
=
\eta+A_Q(x),
$$

onde $A_Q$ é uma $1$-forma externa. Em cada carta,

$$
\eta_{Q,N}
=
d\psi_N+\mathcal A_N+A_Q,
$$

$$
\eta_{Q,S}
=
d\psi_S+\mathcal A_S+A_Q.
$$

Logo,

$$
\eta_{Q,N}=\eta_{Q,S}.
$$

Sua curvatura global é

$$
d\eta_Q
=
\mathcal F_H+F_Q,
$$

com

$$
\mathcal F_H=d\mathcal A_N=d\mathcal A_S,
\qquad
F_Q=dA_Q.
$$

## 3. Ausência de termo cruzado

$\mathcal F_H$ possui índices internos e $F_Q$ possui índices externos.
Para uma métrica Kaluza--Klein ortogonal,

$$
\langle\mathcal F_H,F_Q\rangle=0.
$$

Assim,

$$
|d\eta_Q|^2
=
|\mathcal F_H|^2+|F_Q|^2.
$$

A fórmula de O'Neill fornece ponto a ponto

$$
\boxed{
\mathcal R_8
=
\mathcal R_{\rm base}
-\frac{r_H^2}{4}|F_Q|^2
+\cdots.
}
$$

Essa expressão é a mesma nas duas cartas. As funções de transição cancelam
antes da integração; não existe termo de overlap adicional proporcional a
$F_Q^2$.

## 4. Termos de patch

Ao integrar por partes separadamente em $U_N$ e $U_S$, os termos no overlap
possuem orientações opostas. Como $F_Q$ é global e
$\mathcal A_S-\mathcal A_N$ é exata,

$$
\int_{U_N\cap U_S}d\chi\wedge *_4F_Q^2
-
\int_{U_N\cap U_S}d\chi\wedge *_4F_Q^2
=0.
$$

A colagem preserva o primeiro número de Chern, mas não multiplica a rigidez
par $F_Q^2$. Uma contribuição não cancelada seria Chern--Simons/ímpar e já foi
separada anteriormente da parte real do determinante.

## 5. Consequência para a truncagem radial

Se $r_H$, o warp e o dilatão dependem somente da coordenada radial usada no
solver, a integração horizontal é exata e fornece apenas a medida
condicional. Portanto,

$$
K_Q
=
\left\langle
r_H^2e^{3A}
\right\rangle_{\mu_{\rm int}}
$$

já é a redução global em dois patches para esse ansatz.

Logo,

$$
\boxed{
\text{o atlas de Hopf não fornece o fator numérico faltante.}
}
$$

Ele demonstra que a truncagem radial não perdeu um termo universal de colagem.

## 6. Onde uma correção ainda pode existir

Uma modificação da matriz cinética requer um background verdadeiramente
horizontalmente anisotrópico:

$$
r_H=r_H(\chi,w,\bar w),
\qquad
f=f(\chi,w,\bar w),
$$

ou componentes não ortogonais da métrica Hermitiana. Isso não é recuperado
por refazer o atlas; exige resolver uma EDP no fibrado completo.

O atlas em dois patches define corretamente as condições globais dessa EDP:

$$
\eta_{Q,N}=\eta_{Q,S},
\qquad
P_N=P_S,
\qquad
\mathcal F_N=\mathcal F_S.
$$

## 7. Veredito

A formulação global foi completada sem alterar nenhum resultado anterior. Ela
confirma a topologia e a existência do fóton geométrico, mas exclui a colagem
de patches como origem do fator necessário para $\alpha$.

O próximo nível não é outra normalização algébrica: é a solução anisotrópica
completa da Hessiana Hermitiano--Bismut em $(\chi,w,\bar w)$.
