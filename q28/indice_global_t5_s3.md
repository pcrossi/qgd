# Q28 — Índice global no background $T^5\times S^3$

## 1. Tangente e classe $\widehat A$

O toro é paralelizável e $S^3\simeq SU(2)$ também é paralelizável. Portanto,

$$
T(T^5\times S^3)
$$

é trivial como fibrado real estável. Em particular,

$$
p_i(TM)=0
$$

e

$$
\boxed{
\widehat A(TM)=1.
}
$$

Assim, para um fibrado geracional complexo $E_G$,

$$
\boxed{
\operatorname{Ind}D_{E_G}^+
=\int_{T^5\times S^3}\operatorname{ch}_4(E_G),
}
$$

onde $\operatorname{ch}_4$ designa a componente de grau real oito do caráter
de Chern.

## 2. Resultado para a linha local $L_G$

O protótipo local definiu $L_G$ pela linha de Hopf sobre $S^2$. Entretanto,

$$
H^2(S^3,\mathbb Z)=0,
$$

e não existe um mapa global já construído que estenda essa classe como uma
linha não trivial sobre todo $T^5\times S^3$.

Mesmo que se escolha uma linha global com

$$
c_1(L_G)=x\in H^2(T^5,\mathbb Z),
$$

temos

$$
\operatorname{ch}_4(L_G)=\frac{x^4}{24}.
$$

Como $x$ vive inteiramente no fator real 5-dimensional,

$$
x^4=0.
$$

Logo,

$$
\boxed{
\operatorname{Ind}D_{L_G}^+=0
}
$$

para qualquer linha que seja apenas pullback de $T^5$ ou de $S^3$.

Portanto, a linha local de Hopf não produz índice global três por simples
produto ou pullback.

## 3. Fibrado $SU(2)$ com classe mista

O primeiro mecanismo global capaz de produzir uma classe de grau oito usa um
fibrado de posto dois com

$$
c_1(E_G)=0,
$$

e

$$
c_2(E_G)=a_4+b_1\smile u_3.
$$

Aqui

$$
a_4\in H^4(T^5,\mathbb Z),
$$

$$
b_1\in H^1(T^5,\mathbb Z),
$$

e

$$
u_3\in H^3(S^3,\mathbb Z)
$$

é o gerador orientado.

Como $a_4^2=0$ por dimensão e $u_3^2=0$,

$$
c_2(E_G)^2
=2a_4\smile b_1\smile u_3.
$$

Para um fibrado $SU(2)$, $c_3=c_4=0$ e

$$
\operatorname{ch}_4(E_G)
=\frac1{12}c_2(E_G)^2.
$$

Consequentemente,

$$
\boxed{
\operatorname{Ind}D_{E_G}^+
=\frac16
\left\langle
a_4\smile b_1,
[T^5]
\right\rangle.
}
$$

Defina

$$
N_{ab}
=\left\langle
a_4\smile b_1,
[T^5]
\right\rangle
\in\mathbb Z.
$$

Então

$$
\operatorname{Ind}D_{E_G}^+=\frac{N_{ab}}6.
$$

A existência de um fibrado genuíno e a integralidade do índice restringem os
valores admissíveis de $N_{ab}$.

## 4. Condição para três gerações

O índice será três se e somente se

$$
\boxed{
N_{ab}=18.
}
$$

Por exemplo, para uma base integral $e^1,\ldots,e^5$ de $H^1(T^5)$,

$$
a_4=18\,e^1\smile e^2\smile e^3\smile e^4,
$$

$$
b_1=e^5
$$

produzem formalmente o valor requerido. Mas escolher o coeficiente $18$ para
obter o alvo não é uma derivação.

A GDQ precisa mostrar que a conexão global estacionária possui precisamente

$$
\left\langle a_4\smile b_1,[T^5]\right\rangle=18.
$$

## 5. Papel da torção de Bismut

A substituição da conexão de Levi--Civita pela conexão de Bismut não altera o
índice topológico de um operador elíptico sob deformação contínua, desde que o
símbolo e o domínio permaneçam na mesma classe. A torção pode redistribuir
modos e alterar termos locais/APS, mas não cria por si só a classe global
$a_4\smile b_1$ ausente.

Assim, Perelman e Bismut garantem estabilidade e invariância do índice depois
que o fibrado global é dado. Eles não fixam o inteiro $N_{ab}$.

## 6. Resultado do cálculo

O cálculo global produz dois resultados exatos:

$$
\boxed{
\operatorname{Ind}D_{L_G}^+=0
\text{ para linhas obtidas por pullback simples.}
}
$$

$$
\boxed{
\operatorname{Ind}D_{E_G}^+
=\frac16
\left\langle a_4\smile b_1,[T^5]\right\rangle
}
$$

para o primeiro fibrado $SU(2)$ misto capaz de produzir índice não nulo.

Portanto,

$$
\boxed{
N_G=3
\Longleftrightarrow
\left\langle a_4\smile b_1,[T^5]\right\rangle=18.
}
$$

## 7. Veredito

O índice foi avaliado até os dados topológicos globais efetivamente
especificados. O background produto e a linha local não fornecem três; dão
zero. Uma classe mista pode fornecer três, mas seu número característico ainda
não foi derivado da solução estacionária.

$$
\boxed{
\text{o problema }N_G=3\text{ foi reduzido à derivação geométrica do número
característico }N_{ab}=18.
}
$$
