# Adendo Q26 — Spin, Hopf e resíduo de Cauchy

## 1. Enunciado

Este adendo responde à falta residual da Questão 26:

$$
\text{formular spin }1/2\text{ como circulação/Hopf/resíduo sem substituir a prova spinorial.}
$$

A prova principal da Q26 permanece a rota spinorial:

$$
P_{\rm Spin}(N)\to N,
\qquad
\psi\in\Gamma(S\otimes E),
\qquad
U(2\pi)=-I,
\qquad
U(4\pi)=I.
$$

O objetivo aqui é mostrar que a linguagem de resíduos de Cauchy fornece a
mesma meia-monodromia como leitura geométrica do estômato.

---

## 2. Dados geométricos usados

Assume-se uma vizinhança normal complexa do estômato. Localmente, escolhe-se
uma coordenada complexa transversal $z$ em um disco perfurado:

$$
D^\ast=\{0<|z|<\varepsilon\}.
$$

O ponto $z=0$ representa o núcleo removido do defeito topológico. O contorno
de circulação é um laço simples:

$$
\gamma_r:\ |z|=r.
$$

Na descrição de Hopf, a fatia normal completa é compatível com

$$
S^3\subset\mathbb C^2,
\qquad
S^1\hookrightarrow S^3\to S^2\simeq\mathbb{CP}^1.
$$

O estado de orientação física é o projetor:

$$
P=uu^\dagger,
\qquad
u\in S^3.
$$

Como

$$
u\sim -u
$$

representa o mesmo projetor físico, a orientação observável vive no quociente
projetivo. Esta é a origem geométrica do recobrimento duplo.

---

## 3. Forma meromorfa de meia-monodromia

Um setor spinorial local pode ser representado por uma seção com comportamento
de raiz quadrada ao redor do defeito:

$$
s(z)=z^{1/2}s_0(z),
$$

onde $s_0$ é holomorfa e não nula no disco. A conexão logarítmica associada é:

$$
\Omega_S=d\log s
=\frac12\frac{dz}{z}+d\log s_0.
$$

Como $d\log s_0$ é holomorfa no interior de $\gamma_r$, seu resíduo é nulo.
Logo:

$$
\operatorname{Res}_{z=0}\Omega_S=\frac12.
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
=\frac12.
$$

Esse valor é topológico: deformações de $\gamma_r$ que não cruzem o núcleo do
estômato não alteram o resíduo.

---

## 4. Conversão para fase física

Na convenção física, a circulação da ação real é:

$$
\oint_{\gamma_r} dS_R
=
h\,N_S(\gamma_r)
=
\frac{h}{2}
=
\pi\hbar.
$$

A holonomia de fase é:

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

Este é exatamente o comportamento de spin $1/2$.

---

## 5. Interpretação via Hopf

A fibração de Hopf realiza geometricamente a mesma estrutura.

O spinor $u\in S^3\simeq SU(2)$ projeta-se em uma direção física:

$$
P=uu^\dagger\in\mathbb{CP}^1\simeq S^2.
$$

O mapa

$$
SU(2)\to SO(3)
$$

é duplo. Uma rotação física de $2\pi$ fecha em $SO(3)$, mas seu levantamento
em $SU(2)$ leva:

$$
u\mapsto -u.
$$

Somente uma rotação de $4\pi$ retorna:

$$
u\mapsto u.
$$

Em coordenada local, esse levantamento duplo aparece como a seção de raiz
quadrada $z^{1/2}$; a conexão logarítmica dessa raiz é precisamente a forma
meromorfa com resíduo $1/2$.

Logo:

$$
\text{Hopf/double cover}
\quad\Longleftrightarrow\quad
\text{raiz quadrada local}
\quad\Longleftrightarrow\quad
\operatorname{Res}\Omega_S=\frac12.
$$

---

## 6. Relação com a GDQ

Na GDQ, a densidade de fase vem de:

$$
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

O estômato fornece um defeito de contorno. Se o setor físico admite uma carta
normal em que a fase spinorial possui meia-monodromia, então a circulação de
$dS_R$ ao redor do defeito é:

$$
\oint dS_R=\frac{h}{2}.
$$

Assim, a leitura por resíduos não altera a ação oficial. Ela identifica a
classe de contorno/spinorial admissível do estômato.

Em particular:

$$
\boxed{
\text{o teorema de Cauchy prova a quantização topológica da meia-circulação,
uma vez fixada a classe Hopf/spinorial do defeito.}
}
$$

---

## 7. O que foi provado e o que não foi provado

Foi provado:

1. se a seção local ao redor do estômato é spinorial/Hopf, então sua forma
   logarítmica tem resíduo $1/2$;
2. pelo teorema de Cauchy, a circulação normalizada é rigidamente $1/2$;
3. a fase física satisfaz $2\pi\mapsto -1$ e $4\pi\mapsto +1$;
4. a interpretação por circulação é compatível com a prova spinorial da Q26.

Não foi provado aqui:

1. qual das 16 estruturas spin de $T^4$ é selecionada dinamicamente;
2. qual solíton específico realiza o setor de Dirac do elétron;
3. o espectro completo de massas, cargas e modos espinoriais.

Esses itens pertencem ao problema dinâmico posterior de seleção de setor, não
à falta Hopf/resíduos da Q26.

---

## 8. Status

Com este adendo, a falta “Hopf e resíduos” da Q26 fica fechada como teorema
estrutural condicional:

$$
\boxed{
\text{Q26: spin }1/2\text{ fechado estruturalmente por fibrado spinorial e
equivalentemente formulado por Hopf--Cauchy.}
}
$$

O caráter condicional é apenas a hipótese geométrica explícita de que o
estômato realiza a classe spinorial/Hopf simples no contorno normal.
