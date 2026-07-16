# Q29 — Matriz cinética neutra no modo de Hopf

## 1. Geradores sobre $S^3\subset\mathbb C^2$

No dupleto fundamental,

$$
T_3=\frac12
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
Y=\frac12I_2.
$$

Os vetores de Killing induzidos em $u=(z_1,z_2)$ são

$$
K_3(u)=iT_3u,
\qquad
K_Y(u)=iYu.
$$

Ponto a ponto,

$$
|K_3|^2=\frac14,
\qquad
|K_Y|^2=\frac14,
$$

e

$$
\langle K_3,K_Y\rangle
=
\frac14
\left(|z_1|^2-|z_2|^2\right).
$$

Pela simetria da medida estacionária redonda na ordem líder,

$$
\left\langle|z_1|^2-|z_2|^2\right\rangle=0.
$$

Logo, o Gram cinético é

$$
\boxed{
G_{3Y}
=
\frac14
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
}
$$

O cálculo Monte Carlo em dois milhões de pontos confirmou essa matriz dentro
do erro estatístico.

## 2. Consequência para a norma radial

A quantidade

$$
\mathcal K_{\rm base}=41{,}594825709
$$

foi calculada anteriormente sem inserir a norma matricial do gerador. Cada
gerador normalizado por $T_3=\sigma_3/2$ e $Y=I/2$ recebe, portanto,

$$
\mathcal K_3
=
\mathcal K_Y
=
\frac14\mathcal K_{\rm base}
=10{,}3987064273.
$$

Essa é a origem geométrica lícita do fator próximo de $1/4$ sugerido em
`zz1.md`. Ele não vem do frame de Einstein.

## 3. Teste absoluto

Se essa rigidez comum fosse identificada diretamente com $1/e^2$, obteríamos

$$
\alpha^{-1}_{\rm comum}
=
4\pi\mathcal K_3
=130{,}673998875.
$$

O valor condicional procurado era

$$
132{,}457669022.
$$

O resíduo é

$$
\boxed{
\frac{132{,}457669022}{130{,}673998875}-1
=1{,}364987\%.
}
$$

Portanto, a matriz cinética explica exatamente o fator $1/4$, mas não a
correção adicional de aproximadamente $1{,}365\%$.

## 4. Norma de $Q$

Para

$$
Q=T_3+Y,
$$

temos

$$
\langle|K_Q|^2\rangle
=
\begin{pmatrix}1&1\end{pmatrix}
G_{3Y}
\begin{pmatrix}1\\1\end{pmatrix}
=\frac12.
$$

Essa norma não deve ser identificada diretamente com $1/e^2$, porque o fóton
é o autovetor sem massa depois da normalização cinética separada dos canais
$W^3$ e $Y$. Somar os vetores antes de canonizar os dois campos contaria a
normalização de forma incorreta.

## 5. Berger e termo cruzado

Em uma métrica de Berger ou numa medida não homogênea, o termo

$$
\left\langle|z_1|^2-|z_2|^2\right\rangle
$$

pode deixar de ser zero. Então a matriz geral é

$$
G_{3Y}^{\rm on-shell}
=
\frac14
\begin{pmatrix}
1&\delta_B\\
\delta_B&1
\end{pmatrix},
$$

onde

$$
\delta_B
=
\left\langle|z_1|^2-|z_2|^2\right\rangle_{\mu_*}.
$$

O refinamento seguinte é avaliar $\delta_B$ com a medida warped--Bismut não
homogênea já resolvida, em vez da medida de Haar.

## 6. Avaliação on-shell do termo cruzado

O perfil radial usa o harmônico zonal

$$
Y=\cos\chi=\operatorname{Re}z_2.
$$

Não se pode identificar $Y$ diretamente com o momento de Hopf. Condicionando
à órbita transversal $S^2$ em cada $\chi$, obtém-se

$$
\left\langle
|z_1|^2-|z_2|^2
\right\rangle_{S^2\mid\chi}
=
\frac13-\frac43\cos^2\chi.
$$

Integrando essa função com a medida warped--Bismut on-shell do solver,

$$
\boxed{
\delta_B=-0{,}2709378871.
}
$$

Logo,

$$
\boxed{
G_{3Y}^{\rm on-shell}
=
\begin{pmatrix}
0{,}25&-0{,}0677344718\\
-0{,}0677344718&0{,}25
\end{pmatrix}.
}
$$

Esse termo é muito maior que o resíduo de $1{,}365\%$ e não pode ser tratado
como a pequena correção procurada. Projetá-lo com um ângulo de Weinberg já
escolhido seria circular. É necessário resolver o problema generalizado
completo entre a matriz cinética acima e a matriz de massa de interface.

Assim, a avaliação on-shell exclui a hipótese de que o resíduo seja apenas
uma pequena correção diagonal de Berger. O último cálculo é a diagonalização
generalizada simultânea; não há justificativa para acrescentar o resíduo à
mão.

O teste reproduzível está em `q29/matriz_cinetica_neutra_hopf.py`.
