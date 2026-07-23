# Q28 — Espectro tangencial no elo $S^3$ com Hopf e Bismut

## 1. Objetivo

Levantar o protótipo $U(1)$ da base $S^2$ para o elo tridimensional do
estômato e determinar o conteúdo do termo APS

$$
\bar\eta
=\frac{\eta(0)+h}{2}.
$$

O cálculo é feito primeiro no $S^3$ redondo e homogêneo. A deformação real do
estômato poderá ser acrescentada depois como perturbação espectral.

## 2. Convenções geométricas

Escreva a métrica redonda de raio $a$ como

$$
ds^2
=\frac{a^2}{4}
\left(
\sigma_1^2+\sigma_2^2+\sigma_3^2
\right),
$$

com

$$
\sigma_3=d\psi+\cos\theta\,d\phi,
\qquad
0\leq\psi<4\pi.
$$

A conexão que puxa o monopolo de grau $m$ é

$$
A_m=-\frac m2\sigma_3.
$$

Sua curvatura é

$$
F_m=dA_m
=\frac m2\sin\theta\,d\theta\wedge d\phi.
$$

Como $A_m$ é uma 1-forma global em $S^3$, $F_m$ é exata no elo. Isso é
compatível com $c_1=0$ em $S^3$ e $c_1=m$ na base $S^2$.

## 3. Operador homogêneo

Na decomposição de Peter--Weyl, seja $L_i^{(j)}$ a representação de spin $j$
de $\mathfrak{su}(2)$. O Dirac redondo pode ser realizado, bloco a bloco, por

$$
D_0^{(j)}
=\frac1a
\left(
2\,\boldsymbol\sigma\cdot\boldsymbol L^{(j)}
+\frac32
\right).
$$

Cada bloco possui multiplicidade espectadora $2j+1$. Essa matriz reproduz
exatamente

$$
\operatorname{spec}D_0
=\left\{
\pm\frac{n+3/2}{a}
\right\}_{n=0}^{\infty},
$$

com degenerescência

$$
d_n=(n+1)(n+2).
$$

O acoplamento de Hopf homogêneo e o deslocamento escalar efetivo da torção são
parametrizados por

$$
D_{m,\beta}^{(j)}
=D_0^{(j)}
-\frac m a\sigma_3
+\frac\beta aI.
$$

Aqui $\beta$ é o deslocamento Hermitiano induzido pela convenção física da
torção de Bismut. Não se identifica $\beta$ com a amplitude de $B$ antes de
fixar todos os fatores de $i$ e a orientação do operador auto-adjunto.

## 4. Verificação do espectro livre

Para $m=\beta=0$, a diagonalização dos blocos fornece:

$$
\frac{3}{2a},
\frac{5}{2a},
\frac{7}{2a},\ldots
$$

e

$$
-\frac{3}{2a},
-\frac{5}{2a},
-\frac{7}{2a},\ldots,
$$

com as degenerescências exatas. Isso valida a realização matricial antes da
introdução de Hopf e torção.

## 5. Chern--Simons e o $eta$-invariante reduzido

Com a orientação

$$
\sigma_3\wedge d\sigma_3
=-\sin\theta\,
d\psi\wedge d\theta\wedge d\phi,
$$

temos

$$
\int_{S^3}\sigma_3\wedge d\sigma_3=-16\pi^2.
$$

Portanto,

$$
\boxed{
\frac1{4\pi^2}
\int_{S^3}A_m\wedge dA_m
=-m^2.
}
$$

Considere uma extensão cilíndrica da conexão entre $A=0$ e $A=A_m$, sem
cruzamentos de zero no intervalo. A fórmula APS implica, módulo fluxo
espectral inteiro,

$$
\boxed{
\bar\eta(A_m)-\bar\eta(0)
\equiv
\frac1{8\pi^2}
\int_{S^3}A_m\wedge dA_m
=-\frac{m^2}{2}
\pmod{\mathbb Z}.
}
$$

Como o Dirac redondo possui $\bar\eta(0)=0$,

$$
\boxed{
\bar\eta(A_m)
\equiv-\frac{m^2}{2}
\pmod{\mathbb Z}.
}
$$

O sinal muda se a orientação de $S^3$ ou a convenção da conexão for
invertida; a parte fracionária em módulo inteiro não muda.

## 6. Consequência para a contagem local

O rascunho anterior definia

$$
n_a=-\frac12\left(\eta_a(0)+h_a\right)=-\bar\eta_a
$$

e impunha $n_a=1$. O protótipo calculado mostra que, para fluxo mínimo
$|m|=1$,

$$
\boxed{
n_a\equiv\frac12\pmod{\mathbb Z}.
}
$$

Portanto, uma contribuição inteira $n_a=1$ não pode vir apenas do termo de
borda de um único fluxo Hopf mínimo. A integral de bulk no índice APS precisa
fornecer a parte complementar, ou a representação física deve combinar dois
canais conjugados.

O índice completo é

$$
\operatorname{ind}D^+
=
\int_{X_4}
\widehat A(TX_4)\operatorname{ch}(L_m)
-\bar\eta(A_m).
$$

Como o lado esquerdo é inteiro, a parte fracionária da integral de bulk deve
cancelar a parte fracionária de $\bar\eta$.

## 7. Papel da torção

Uma deformação contínua por $\beta$ altera $\bar\eta$ suavemente por um termo
local e por saltos inteiros quando um autovalor cruza zero. O fluxo espectral
inteiro pode mudar o representante de

$$
\bar\eta\in\mathbb R/\mathbb Z,
$$

mas não remove arbitrariamente a parte fracionária fixada pela classe de
Chern--Simons sem uma contribuição compensadora do bulk.

Assim, a torção não deve ser ajustada para impor $n_a=1$. Ela deve ser
calculada do background e usada para determinar:

1. quais autovalores cruzam zero;
2. o kernel $h_a$;
3. o representante real de $\bar\eta$;
4. a quiralidade dos modos localizados.

## 8. Status

$$
\boxed{
\text{espectro homogêneo construído e parte fracionária de }\bar\eta
\text{ determinada por Chern--Simons.}
}
$$

O passo seguinte é fixar $\beta$ pela torção estacionária da GDQ e calcular o
fluxo espectral do operador matricial, não escolher $\beta$ pelo índice alvo.

## 9. Normalização Cartan--Schouten: teste dos dois sinais

No referencial ortonormal da métrica

$$
ds^2=\frac{a^2}{4}\sum_i\sigma_i^2,
$$

as constantes de estrutura possuem módulo $2/a$. Para a torção
paralelizante, a convenção usual fornece

$$
B_{abc}=\varepsilon_B\frac2a\varepsilon_{abc},
\qquad
\varepsilon_B=\pm1.
$$

A contração formal do termo

$$
\frac18B_{abc}\gamma^a\gamma^{bc}
$$

tem módulo escalar

$$
\frac34\frac2a=\frac{3}{2a}.
$$

Portanto, depois de fixada uma convenção auto-adjunta, espera-se

$$
|\beta|=\frac32.
$$

Os dois sinais foram testados separadamente em
`resultado_eta_s3_beta_mais.md` e `resultado_eta_s3_beta_menos.md`. Ambos
produzem cruzamentos de zero, mas com kernels e fluxos espectrais distintos.

Não se seleciona um deles pelo valor desejado do índice. A seleção exige
derivar o fator de $i$, a orientação e o sinal de $B$ na continuação
euclidiana do operador oficial. Até essa verificação, o resultado correto é

$$
\boxed{
|\beta|=\frac32\text{ no fundo paralelizante, com sinal físico ainda a
fixar pela auto-adjunticidade e causalidade.}
}
$$

## 10. Fixação do sinal pela auto-adjunticidade euclidiana

Escolha gammas euclidianas Hermitianas e o operador auto-adjunto

$$
D_B
=i\gamma^a
\left(
\nabla_a^{\rm LC}
+\frac18B_{abc}\gamma^{bc}
\right).
$$

Em três dimensões,

$$
\gamma^{123}=iI.
$$

Para

$$
B_{abc}=\frac2a\varepsilon_{abc}
$$

na orientação positiva,

$$
i\gamma^a\frac18B_{abc}\gamma^{bc}
=i\frac{3}{4}\frac2a\gamma^{123}
=-\frac{3}{2a}I.
$$

Portanto,

$$
\boxed{
\beta=-\frac32
}
$$

para a orientação positiva adotada. A orientação oposta fornece
$\beta=+3/2$ e troca a quiralidade física.

Com $\beta=-3/2$, o operador reduz-se a

$$
D_{m,B}^{(j)}
=\frac1a
\left(
2\boldsymbol\sigma\cdot\boldsymbol L^{(j)}
-m\sigma_3
\right).
$$

A diagonalização mostra que, para $m\ne0$, o kernel ocorre em

$$
j=\frac{|m|}{2}
$$

e possui multiplicidade

$$
\boxed{
h_m=|m|+1.
}
$$

Para $m=0$, o bloco $j=0$ possui

$$
h_0=2.
$$

Assim, o fluxo mínimo $|m|=1$ produz

$$
\boxed{h_{\pm1}=2.}
$$

O kernel é derivado da torção paralelizante e não imposto como degenerescência
fenomenológica.

Esse resultado ainda não fixa sozinho o índice APS: a variação torsional de
$\bar\eta$ contém uma transgressão local adicional, e o índice completo exige
a integral de bulk. O passo seguinte é calcular essa densidade no preenchimento
4D compatível com o estômato.
