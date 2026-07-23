# Q28 — Colagem projetiva $\mathbb Z_6$ e classe mista

## 1. Cociclo projetivo no toro

Se $U_i$ são os transportes nos ciclos de $T^5$, uma representação
projetiva permite

$$
U_iU_j=\omega^{n_{ij}}U_jU_i,
\qquad
\omega=e^{2\pi i/6},
$$

com

$$
n_{ij}\in\mathbb Z_6,
\qquad
n_{ij}=-n_{ji}.
$$

Para um cociclo primitivo, por exemplo $n_{12}=1$, as matrizes relógio e
deslocamento mínimas são

$$
C=\operatorname{diag}(1,\omega,\omega^2,\ldots,\omega^5),
$$

$$
S e_k=e_{k+1\pmod6},
$$

e satisfazem

$$
CS=\omega SC.
$$

Logo, a representação projetiva irredutível mínima possui dimensão seis.
Ela não pode agir apenas no kernel local de dimensão

$$
h_1=2.
$$

O primeiro espaço já presente na Q28 que comporta naturalmente esse cociclo
é o multiplet interno

$$
\mathbb C^3\otimes\mathbb C^2,
$$

de dimensão seis. Incluindo os dois modos zero, a família completa teria
fibra mínima

$$
\ker D_{S^3}\otimes\mathbb C^3\otimes\mathbb C^2,
$$

de dimensão doze.

## 2. O que o cociclo determina

Os inteiros $n_{ij}$ definem uma obstrução discreta ao levantamento do
fibrado projetivo para um fibrado vetorial ordinário. Essa obstrução pertence
a

$$
H^2(T^5,\mathbb Z_6).
$$

Ela não é, por si só, uma forma de curvatura de Berry e não determina
unicamente uma classe integral

$$
c_2(E_G)\in H^4(T^5\times S^3,\mathbb Z).
$$

Portanto, não é matematicamente válido identificar diretamente o número seis
do quociente com o coeficiente $a_4$, nem concluir

$$
N_{ab}=18
$$
apenas pela presença do grupo $\mathbb Z_6$.

## 3. Construção da componente $b_1\smile u_3$

A componente mista pode ser construída por uma colagem ao longo de um ciclo
$S^1_5\subset T^5$. Corte esse ciclo em um intervalo e cole suas extremidades
por um mapa

$$
g:S^3\longrightarrow SU(2).
$$

Seu grau é

$$
\nu(g)
=\frac{1}{24\pi^2}
\int_{S^3}\operatorname{tr}(g^{-1}dg)^3
\in\mathbb Z.
$$

O fibrado sobre $S^1_5\times S^3$ obtido por essa colagem satisfaz

$$
\left\langle c_2(E_G),[S^1_5\times S^3]\right\rangle
=\nu(g).
$$

Assim, nessa construção,

$$
b_1=\nu(g)e^5.
$$

Para a identidade $S^3\simeq SU(2)$,

$$
\nu(g)=1.
$$

Essa é uma derivação topológica da componente mista, sem ajuste numérico.

## 4. Construção da componente $a_4$

A componente

$$
a_4\in H^4(T^5,\mathbb Z)
$$

exige curvatura em pelo menos quatro direções toroidais. Em uma conexão
constante compatível com dois planos, escreva

$$
\mathcal F_T
=2\pi i\left(M_{12}\,e^1\wedge e^2
+M_{34}\,e^3\wedge e^4\right),
$$

onde as matrizes de fluxo obedecem às condições de quantização e de colagem
do fibrado escolhido. Então

$$
a_4
=-\frac{1}{8\pi^2}
\operatorname{tr}(\mathcal F_T\wedge\mathcal F_T)
=\operatorname{tr}(M_{12}M_{34})
e^{1234},
$$

até a convenção global de orientação.

Definindo

$$
A=\operatorname{tr}(M_{12}M_{34})\in\mathbb Z,
$$

temos

$$
a_4=Ae^{1234}.
$$

O cociclo $\mathbb Z_6$ restringe os fluxos admissíveis módulo seis, mas não
fixa sozinho o levantamento integral $A$.

## 5. Avaliação de $N_{ab}$

Com

$$
a_4=Ae^{1234},
\qquad
b_1=\nu(g)e^5,
$$

segue

$$
\boxed{
N_{ab}
=\left\langle a_4\smile b_1,[T^5]\right\rangle
=A\nu(g).
}
$$

Para a colagem mínima de Hopf,

$$
\nu(g)=1,
$$

e portanto

$$
N_{ab}=A.
$$

O alvo de três gerações passa a exigir

$$
A=18.
$$

O valor de $A$ ainda não foi derivado. Ele deve emergir da conexão de Berry
da Hessiana GDQ global, ou de uma regra geométrica de colagem que selecione
os fluxos $M_{12}$ e $M_{34}$.

## 6. Diagnóstico

A colagem projetiva $\mathbb Z_6$ resolve uma parte estrutural importante:
ela mostra por que a construção deve envolver conjuntamente os setores
$SU(3)$ e $SU(2)$, e não apenas o kernel bidimensional. Contudo, o quociente
discreto não produz automaticamente o inteiro de Chern requerido.

O resultado atual é

$$
\boxed{
N_{ab}=A\nu(g),
\qquad
\nu(g)=1,
\qquad
A\text{ ainda deve ser calculado da Hessiana global.}
}
$$

Assim, a próxima etapa não é escolher $A=18$, mas extrair $M_{12}$ e
$M_{34}$ do projetor espectral dos modos zero da ação oficial.
