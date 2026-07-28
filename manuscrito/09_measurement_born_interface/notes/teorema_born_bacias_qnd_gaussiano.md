---
title: "Teorema Born–bacias para aparelhos QND gaussianos"
---

# Teorema Born–bacias para aparelhos QND gaussianos

Esta nota demonstra, numa classe física precisa de aparelhos, que a medida
das bacias de registro coincide com o peso espectral inicial. O resultado não
altera a ação oficial: ele usa sua Hessiana física no background conjunto do
sistema, aparelho e ambiente.

O teorema vale para aparelhos:

1. não demolíveis nos canais medidos;
2. descritos pela redução quadrática da Hessiana;
3. dotados de canais gaussianos causais de saída;
4. capazes de distinguir assintoticamente todos os registros.

Fora dessa classe, a correspondência deve ser demonstrada novamente.

## 1. Dados variacionais

Seja $\Phi_*$ um background estacionário admissível. Depois da remoção dos
modos de gauge, a segunda variação conjunta possui a forma:

$$
\delta^2\mathcal S_{\rm GDQ}
=
\frac12\langle x,K_Sx\rangle
+
\frac12\langle y,K_Ay\rangle
+
\langle y,Jx\rangle.
$$

$x$ representa os modos físicos do objeto e $y$ os modos não monitorados do
aparelho e ambiente. Eliminando $y$ pela resposta linear, obtém-se o
complemento de Schur:

$$
K_{\rm eff}
=
K_S-J^\dagger K_A^{-1}J.
$$

Os canais de registro são projetores espectrais ortogonais:

$$
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I_{\rm reg}.
$$

## 2. Condição QND e conservação por canal

Uma medição é não demolível, QND, quando:

$$
[K_S,P_i]=0,
\qquad
[J^\dagger K_A^{-1}J,P_i]=0.
$$

Consequentemente:

$$
[K_{\rm eff},P_i]=0
$$

e:

$$
P_iK_{\rm eff}P_j=0,
\qquad i\ne j.
$$

Não existe corrente determinística entre canais distintos. No tempo físico
reconstruído, a evolução interna diagonal apenas modifica fases e respostas
dentro de cada bloco. A corrente de fase de Noether fornece:

$$
\left.\frac{dp_i}{dt}\right|_{\rm det}=0,
\qquad
p_i=\operatorname{Tr}(\varrho P_i).
$$

Esse resultado é mais forte que a conservação da soma
$\sum_i p_i=1$: cada bloco QND é conservado separadamente pela parte
determinística.

## 3. Canais abertos produzidos pela Hessiana

Diagonalize o bloco macroscópico do aparelho em modos de saída $y_a$. Para
cada modo:

$$
S_{A,a}^{(2)}
=
\frac{\zeta_a}{2}
\int dt\int_0^\infty dx
\left[
\frac1{c_a^2}(\partial_ty_a)^2
-
(\partial_xy_a)^2
\right].
$$

Os coeficientes são produtos internos da Hessiana:

$$
\frac{\zeta_a}{c_a^2}
=
\langle T_a,K_tT_a\rangle_{\mathcal U_*},
\qquad
\zeta_a
=
\langle T_a,K_xT_a\rangle_{\mathcal U_*}.
$$

Com condição causal de radiação de saída, o operador
Dirichlet-to-Neumann retardado é:

$$
\Lambda_a^{\rm ret}(\omega)
=
-i\omega\gamma_a,
\qquad
\gamma_a=\frac{\zeta_a}{c_a}>0.
$$

O sinal branqueado produzido pelo canal $i$ no modo $a$ é:

$$
s_i^a(t)
=
\frac{
\langle T_a,K_A^{-1}JP_ix_*\rangle_{\mathcal U_*}
}{
\sqrt{N_a(t)}
}.
$$

$N_a$ é a densidade espectral do ruído do próprio aparelho. Portanto os
sinais não são constantes fundamentais: pertencem ao background, ao material
e ao contorno do detector.

## 4. Medida gaussiana dos históricos

Como a ação reduzida é quadrática nos modos $y_a$, sua integração é
gaussiana. Se $d\mathbb Q$ denota a medida do ruído branqueado, a
verossimilhança do histórico $Y_{[0,t]}$ no canal $i$ é:

$$
Z_i(t)
=
\exp
\left[
\sum_a\int_0^t s_i^a\,dY^a
-
\frac12
\sum_a\int_0^t(s_i^a)^2du
\right].
$$

Cada densidade é normalizada:

$$
\int Z_i(t;Y)\,d\mathbb Q(Y)=1.
$$

A ortogonalidade QND elimina os termos cruzados. A medida física dos
históricos torna-se:

$$
d\mathbb P_t(Y)
=
\sum_i p_i(0)Z_i(t;Y)\,d\mathbb Q(Y),
$$

onde:

$$
p_i(0)=\operatorname{Tr}(\varrho_0P_i).
$$

Esses coeficientes são as normas dos blocos espectrais do estado-resposta
antes da classificação terminal; não são volumes de bacias inseridos
manualmente.

## 5. Filtro condicionado e martingal

O peso condicionado do canal é:

$$
p_i(t)
=
\frac{p_i(0)Z_i(t)}
{\sum_jp_j(0)Z_j(t)}.
$$

Defina:

$$
\bar s^a(t)
=
\sum_jp_j(t)s_j^a(t)
$$

e a inovação:

$$
d\widetilde W_t^a
=
dY_t^a-\bar s^a(t)\,dt.
$$

Aplicando a fórmula de Itô ao quociente normalizado, os termos de deriva
cancelam:

$$
\boxed{
dp_i
=
p_i
\sum_a
(s_i^a-\bar s^a)
d\widetilde W_t^a.
}
$$

Logo:

$$
\mathbb E[dp_i\mid\mathcal F_t]=0
$$

e:

$$
\boxed{
\mathcal L_{\rm meas}p_i=0.
}
$$

Cada $p_i(t)$ é, portanto, um martingal limitado.

## 6. Covariância absorvente

A variação quadrática é:

$$
d[p_i,p_j]_t
=
a_{ij}(p,t)\,dt,
$$

com:

$$
\boxed{
a_{ij}
=
p_ip_j
\sum_a
(s_i^a-\bar s^a)
(s_j^a-\bar s^a).
}
$$

Essa matriz é positiva semidefinida porque é uma matriz de Gram. Além disso:

$$
\sum_i a_{ij}=0,
$$

de modo que o ruído é tangente ao simplex. Se $p_i=0$, o canal permanece na
face $p_i=0$; num vértice puro, toda a covariância desaparece. Assim, os
registros puros são absorventes.

## 7. Informação acumulada e captura

Para dois canais distintos, defina:

$$
\mathcal I_{ij}(t)
=
\frac12
\sum_a
\int_0^t
|s_i^a(u)-s_j^a(u)|^2du.
$$

Se:

$$
\mathcal I_{ij}(\infty)=\infty
$$

para todo $i\ne j$, as razões de verossimilhança separam
assintoticamente todos os registros. Os pesos convergem quase certamente
para um único vértice:

$$
p_i(t)
\longrightarrow
\mathbf1_{\{I_\infty=i\}}.
$$

Para um aparelho estacionário, basta que cada par seja distinguido por pelo
menos um modo:

$$
\sum_a|s_i^a-s_j^a|^2
\ge\epsilon_{ij}>0.
$$

Então:

$$
\mathcal I_{ij}(t)
\ge
\frac{\epsilon_{ij}}2t
\longrightarrow\infty.
$$

## 8. Teorema Born–bacias

Como $p_i(t)$ é um martingal limitado:

$$
\mathbb E[p_i(\infty)]
=
p_i(0).
$$

Na captura:

$$
p_i(\infty)
=
\mathbf1_{\{I_\infty=i\}}.
$$

Portanto:

$$
\begin{aligned}
\mu_{\rm path}(\mathcal B_i)
&=
\mathbb P(I_\infty=i)
\\
&=
\mathbb E[
\mathbf1_{\{I_\infty=i\}}
]
\\
&=
\mathbb E[p_i(\infty)]
\\
&=
p_i(0).
\end{aligned}
$$

Finalmente:

$$
\boxed{
\mu_{\rm path}(\mathcal B_i)
=
\operatorname{Tr}(\varrho_0P_i).
}
$$

Essa identidade não define as bacias pelo valor de Born. Ela resulta da
conservação martingal dos pesos espectrais e da captura produzida pelo
aparelho.

## 9. Duração finita

Captura exata é um resultado assintótico. Para uma janela finita $T$, resta
um erro de discriminação controlado pela informação acumulada:

$$
\epsilon_{\rm det}(T)
\sim
\exp
\left[
-
\min_{i\ne j}\mathcal I_{ij}(T)
\right].
$$

Esse erro pertence ao aparelho, ao material e ao tempo de leitura. Não é uma
correção da ação fundamental.

## 10. Estatuto

O resultado está fechado condicionalmente para o setor QND gaussiano:

$$
\boxed{
\text{Hessiana QND}
+
\text{saída gaussiana causal}
+
\text{separação acumulada}
\Longrightarrow
\text{Born–bacias}.
}
$$

Para um detector concreto ainda é necessário calcular $K_A$, $J$, $N_a$ e
$s_i^a$, verificar os comutadores QND e confirmar a separação dos sinais.
Aparelhos não gaussianos, não markovianos, demolíveis ou com projetores
móveis não estão cobertos automaticamente.

## 11. Certificação Lean

O módulo canônico
[QNDBornBasins.lean](../../../formal/GDQ/QNDBornBasins.lean)
certifica a versão finita exata dos históricos gaussianos. Ele prova:

1. preservação da comutação QND pelo complemento de Schur;
2. anulação dos blocos fora da diagonal entre canais ortogonais;
3. positividade e normalização dos pesos condicionados;
4. conservação exata da esperança do posterior;
5. positividade de Gram e tangência da covariância ao simplex;
6. igualdade entre medida da bacia absorvente e peso inicial.

A convergência do processo contínuo para um vértice usa a demonstração
analítica das Seções 5--7. Assim, Lean não substitui a hipótese física de que
um detector concreto satisfaz QND, causalidade gaussiana e separação
assintótica; ele certifica a dedução depois que esses dados são verificados.
