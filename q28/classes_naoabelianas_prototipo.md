# Q28 — Classes não abelianas pelo clutching no elo $S^3$

## 1. Construção global mínima

Cole dois preenchimentos

$$
B_N^4
$$

e

$$
B_S^4
$$

ao longo da borda comum:

$$
S^4=B_N^4\cup_{S^3}B_S^4.
$$

Um fibrado principal $SU(r)$ sobre $S^4$ é determinado por uma função de
transição

$$
g:S^3\longrightarrow SU(r).
$$

Sua classe é o winding

$$
\boxed{
k(g)
=\frac1{24\pi^2}
\int_{S^3}
\operatorname{tr}
\left(g^{-1}dg\right)^3
\in\mathbb Z,
}
$$

até o sinal fixado pela orientação e pela convenção anti-Hermitiana dos
geradores.

O segundo número de Chern é

$$
\boxed{c_2(E)[S^4]=k(g).}
$$

## 2. Gerador mínimo de $SU(2)$

Identifique

$$
S^3\simeq SU(2)
$$

por

$$
g_2(x)
=x_0I+i\sum_{a=1}^3x_a\sigma_a,
\qquad
\sum_{\mu=0}^3x_\mu^2=1.
$$

Esse mapa é a identidade de $S^3$ e possui grau unitário:

$$
\boxed{k(g_2)=1.}
$$

Logo, o fibrado fraco mínimo satisfaz

$$
\boxed{c_2(E_W)[S^4]=1.}
$$

Não foi usada uma configuração de Yang--Mills como ação fundamental. O mapa
de clutching apenas classifica o fibrado global permitido pela geometria.

## 3. Elevação mínima a $SU(3)$

Use a inclusão canônica

$$
\iota:SU(2)\hookrightarrow SU(3),
$$

$$
\iota(g_2)
=
\begin{pmatrix}
g_2&0\\
0&1
\end{pmatrix}.
$$

Como a inclusão induz um isomorfismo no gerador de $\pi_3$,

$$
\pi_3(SU(2))\simeq\mathbb Z
\longrightarrow
\pi_3(SU(3))\simeq\mathbb Z,
$$

temos

$$
\boxed{k(\iota\circ g_2)=1.}
$$

Assim, o fibrado de cor mínimo satisfaz

$$
\boxed{c_2(E_C)[S^4]=1.}
$$

O dual $E_C^*$ possui o mesmo $c_2$ e representação conjugada.

## 4. Por que $c_3(E_C)$ não aparece neste protótipo

O terceiro número de Chern é detectado por uma classe de grau seis:

$$
c_3(E_C)\in H^6(X,\mathbb Z).
$$

Mas

$$
H^6(S^4,\mathbb Z)=0.
$$

Portanto,

$$
\boxed{c_3(E_C)[S^4]=0}
$$

por razão dimensional. Isso não prova que $c_3(E_C)$ global da GDQ seja zero.
Prova apenas que o elo de um único estômato e seu preenchimento 4D não podem
medi-lo.

Para calcular $c_3(E_C)$ é necessário identificar um 6-ciclo

$$
\Sigma_6\subset M_{\rm global}
$$

e avaliar

$$
c_3(E_C)[\Sigma_6]
=\frac1{48\pi^3}
\int_{\Sigma_6}
\operatorname{tr}(F_C^3)
$$

na convenção Hermitiana apropriada.

## 5. Índice equivarante local

Com a linha geracional $L_G$ já calculada, os fibrados não abelianos mínimos
produzem

$$
\operatorname{Ind}_{SU(2)}
(D_G^+\otimes E_W)
=[\mathbf2],
$$

e

$$
\operatorname{Ind}_{SU(3)}
(D_G^+\otimes E_C)
=[\mathbf3].
$$

O valor $c_2=1$ mostra que esses fibrados são globalmente não triviais depois
da colagem dos dois patches, fortalecendo a elevação que antes havia sido
testada apenas para uma conexão local trivial.

## 6. Limite lógico

Foi demonstrada a existência de classes mínimas unitárias compatíveis com o
elo:

$$
\boxed{
c_2(E_W)=1,
\qquad
c_2(E_C)=1
}
$$

no protótipo $S^4$.

Ainda falta mostrar que a solução estacionária da GDQ seleciona precisamente
esses mapas de clutching, em vez de $k=0$ ou $|k|>1$. O critério candidato é
estabilidade/energia mínima dentro do setor topológico não trivial.

## 7. Status

$$
\boxed{
\text{classes }c_2\text{ mínimas calculadas; }c_3(E_C)
\text{ requer um 6-ciclo global.}
$$
