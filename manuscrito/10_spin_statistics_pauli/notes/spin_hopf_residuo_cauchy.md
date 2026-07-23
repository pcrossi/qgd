---
title: "Spin, Hopf e resíduo de Cauchy"
---

# Spin, Hopf e resíduo de Cauchy

## 1. Enunciado

Esta nota formaliza a leitura GDQ do spin $1/2$ como meia-monodromia de Hopf e
resíduo de Cauchy. Ela não substitui a prova principal por estrutura spinorial,
Clifford e recobrimento duplo; ela explica por que a linguagem física de
circulação é compatível com essa prova.

A prova principal do capítulo é:

$$
P_{\rm Spin}(N)\to N,
\qquad
\psi\in\Gamma(S\otimes E),
\qquad
U(2\pi)=-I,
\qquad
U(4\pi)=I.
$$

A leitura desta nota é:

$$
\operatorname{Res}_{z=0}\Omega_S
=
\frac12
\quad
\Longrightarrow
\quad
\oint dS_R
=
\frac h2
\quad
\Longrightarrow
\quad
\operatorname{Hol}=-1.
$$

## 2. Dados geométricos usados

Assume-se uma vizinhança normal complexa do estômato. Localmente, escolhe-se
uma coordenada complexa transversal $z$ em um disco perfurado:

$$
D^\ast
=
\{0<|z|<\varepsilon\}.
$$

O ponto $z=0$ representa o núcleo removido do defeito topológico. O contorno de
circulação é o laço simples:

$$
\gamma_r:
|z|=r.
$$

Na descrição de Hopf, a fatia normal completa é compatível com

$$
S^3\subset\mathbb C^2,
\qquad
S^1\hookrightarrow S^3\to S^2\simeq\mathbb{CP}^1.
$$

O spinor normalizado vive em

$$
u\in S^3\simeq SU(2),
$$

e a direção física observável é o projetor

$$
P=uu^\dagger\in\mathbb{CP}^1\simeq S^2.
$$

Como

$$
u\sim -u
$$

representa o mesmo projetor físico, a orientação observável vive no quociente
projetivo. Esta é a origem geométrica do recobrimento duplo.

## 3. Forma meromorfa de meia-monodromia

Um setor spinorial local pode ser representado por uma seção com comportamento
de raiz quadrada ao redor do defeito:

$$
s(z)=z^{1/2}s_0(z),
$$

onde $s_0$ é holomorfa e não nula no disco. A conexão logarítmica associada é:

$$
\Omega_S
=
d\log s
=
\frac12\frac{dz}{z}
+
d\log s_0.
$$

Como $d\log s_0$ é holomorfa no interior de $\gamma_r$, seu resíduo é nulo:

$$
\operatorname{Res}_{z=0}d\log s_0
=
0.
$$

Logo:

$$
\operatorname{Res}_{z=0}\Omega_S
=
\frac12.
$$

Pelo teorema dos resíduos de Cauchy:

$$
\frac{1}{2\pi i}\oint_{\gamma_r}\Omega_S
=
\operatorname{Res}_{z=0}\Omega_S
=
\frac12.
$$

Assim, o número de circulação spinorial normalizado é:

$$
N_S(\gamma_r)
:=
\frac{1}{2\pi i}\oint_{\gamma_r}\Omega_S
=
\frac12.
$$

Esse valor é topológico: deformações de $\gamma_r$ que não cruzem o núcleo do
estômato não alteram o resíduo.

## 4. Conversão para fase física

Na GDQ,

$$
S_R
=
\frac{\hbar}{2i}(f-\bar f).
$$

Se o setor spinorial normal carrega meia-monodromia, a circulação da fase real
ao redor do estômato é:

$$
\oint_{\gamma_r}dS_R
=
h\,N_S(\gamma_r)
=
\frac h2
=
\pi\hbar.
$$

A holonomia física de fase é:

$$
\operatorname{Hol}_{\gamma_r}
=
\exp\left(
\frac{i}{\hbar}\oint_{\gamma_r}dS_R
\right)
=
\exp(i\pi)
=
-1.
$$

Para duas voltas:

$$
\operatorname{Hol}_{\gamma_r^2}
=
(-1)^2
=
1.
$$

Portanto:

$$
2\pi\mapsto -1,
\qquad
4\pi\mapsto +1.
$$

Esse é exatamente o comportamento de spin $1/2$.

## 5. Relação com Hopf

A fibração de Hopf realiza geometricamente a mesma estrutura. O mapa

$$
SU(2)\to SO(3)
$$

é duplo. Uma rotação física de $2\pi$ fecha em $SO(3)$, mas seu levantamento em
$SU(2)$ leva:

$$
u\mapsto -u.
$$

Somente uma rotação de $4\pi$ retorna:

$$
u\mapsto u.
$$

Em coordenada local, esse levantamento duplo aparece como a seção de raiz
quadrada $z^{1/2}$. A conexão logarítmica dessa raiz é a forma meromorfa com
resíduo $1/2$.

Logo:

$$
\text{Hopf/recobrimento duplo}
\quad\Longleftrightarrow\quad
\text{raiz quadrada local}
\quad\Longleftrightarrow\quad
\operatorname{Res}\Omega_S=\frac12.
$$

## 6. Relação com a ação oficial

A leitura por resíduos não altera a ação oficial da GDQ. Ela identifica uma
classe admissível de contorno e de setor spinorial do estômato.

O papel da ação oficial é selecionar backgrounds e Hessianas físicas. O papel
do resíduo é classificar a monodromia normal permitida quando o defeito já
possui classe Hopf/spinorial.

Portanto:

$$
\boxed{
\text{o teorema de Cauchy prova a quantização topológica da meia-circulação,
uma vez fixada a classe Hopf/spinorial do defeito.}
}
$$

## 7. O que foi provado e o que não foi provado

Foi provado:

1. se a seção local ao redor do estômato é spinorial/Hopf, então sua forma
   logarítmica tem resíduo $1/2$;
2. pelo teorema de Cauchy, a circulação normalizada é rigidamente $1/2$;
3. a fase física satisfaz $2\pi\mapsto -1$ e $4\pi\mapsto +1$;
4. a interpretação por circulação é compatível com a prova spinorial do
   capítulo.

Não foi provado nesta nota:

1. qual das estruturas spin internas é selecionada dinamicamente;
2. qual solíton específico realiza o setor de Dirac do elétron;
3. o espectro completo de massas, cargas e modos espinoriais.

Esses itens pertencem ao problema dinâmico posterior de seleção de setor, não
à falta Hopf/resíduos.
