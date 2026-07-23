# Q39 — Koide como teorema geométrico de fechamento

## 1. Objetivo

Este documento separa duas leituras diferentes da relação de Koide.

Leitura proibida pela Q39:

\[
M_\tau\leftarrow\text{Koide empírica}.
\]

Leitura admissível na GDQ:

\[
\text{Koide}
\leftarrow
\text{condição geométrica de saturação tridimensional}
\]

no espaço de amplitudes de tensão.

Assim, Koide não entra como fórmula externa. Ela aparece como identidade
equivalente à decomposição isotrópica/transversal da GDQ.

## 2. Variáveis corretas

Defina razões de massa:

\[
R_i=\frac{M_i}{M_e},
\]

e amplitudes de tensão:

\[
A_i=\sqrt{R_i}.
\]

O vetor de amplitudes é:

\[
A=(A_1,A_2,A_3)\in\mathbb R^3.
\]

A direção isotrópica é:

\[
u=\frac{1}{\sqrt3}(1,1,1).
\]

Decomponha:

\[
A=A_\parallel+A_\perp,
\qquad
A_\parallel=(A\cdot u)u,
\qquad
A_\perp\perp u.
\]

## 3. Relação com Koide

O quociente de Koide é:

\[
Q(A)
=
\frac{A_1^2+A_2^2+A_3^2}
{(A_1+A_2+A_3)^2}.
\]

Como:

\[
A_1+A_2+A_3
=
\sqrt3\,\|A_\parallel\|,
\]

e:

\[
\|A\|^2
=
\|A_\parallel\|^2+\|A_\perp\|^2,
\]

segue:

\[
Q
=
\frac{\|A_\parallel\|^2+\|A_\perp\|^2}
{3\|A_\parallel\|^2}
=
\frac13
+
\frac{\|A_\perp\|^2}{3\|A_\parallel\|^2}.
\]

Na GDQ, a saturação tridimensional do setor carregado é:

\[
\|A_\perp\|^2=\|A_\parallel\|^2.
\]

Então:

\[
Q
=
\frac13+\frac13
=
\frac23.
\]

Equivalente:

\[
\cos^2\theta
=
\frac{(A\cdot u)^2}{\|A\|^2}
=
\frac12,
\qquad
\theta=\frac{\pi}{4}.
\]

Portanto, Koide é a forma escalar da condição:

\[
\boxed{
\text{o vetor de amplitudes faz }45^\circ\text{ com a direção isotrópica.}
}
\]

## 4. Terceira ressonância a partir de duas

Dados dois setores com amplitudes positivas:

\[
x=\sqrt{R_1},
\qquad
y=\sqrt{R_2},
\]

procura-se:

\[
z=\sqrt{R_3}
\]

tal que:

\[
\frac{x^2+y^2+z^2}{(x+y+z)^2}=\frac23.
\]

Multiplicando por \(3(x+y+z)^2\):

\[
3(x^2+y^2+z^2)
=
2(x+y+z)^2.
\]

Logo:

\[
z^2-4(x+y)z+x^2+y^2-4xy=0.
\]

As duas raízes são:

\[
z_\pm
=
2(x+y)\pm\sqrt{3x^2+12xy+3y^2}.
\]

Assim:

\[
\boxed{
R_{3,\pm}
=
\left[
2(\sqrt{R_1}+\sqrt{R_2})
\pm
\sqrt{3R_1+12\sqrt{R_1R_2}+3R_2}
\right]^2.
}
\]

O ramo físico pesado é \(R_{3,+}\). O ramo \(R_{3,-}\) é uma ressonância
matematicamente admissível da mesma condição angular, mas deve ser tratado
como ramo não saturado, sombra ou estado auxiliar até receber interpretação
pela Hessiana física.

## 5. Aplicação aos léptons carregados

Na normalização:

\[
R_e=1,
\]

e com o setor biespacial reduzido:

\[
R_\mu
=
\frac32\alpha^{-1}
+\frac65
+2\alpha,
\]

o ramo pesado fornece:

\[
R_\tau
\simeq
3477.446405098.
\]

O ponto importante é que a GDQ não usa \(M_\tau\) como entrada. A estrutura é:

\[
R_e,\ R_\mu,\ Q=\frac23
\quad\Longrightarrow\quad
R_\tau.
\]

Portanto, a mesma lei pode ser usada em outros tripletos de ressonâncias:
conhecidas duas massas ou frequências e estabelecida a condição de saturação
tridimensional, a terceira ressonância é prevista pelos dois ramos acima.

## 6. Classificação

Este resultado é:

\[
\boxed{
\text{teorema geométrico reduzido da GDQ.}
}
\]

Ele não é ainda:

\[
\boxed{
\text{teorema universal para qualquer tripleto físico.}
}
\]

Para aplicar a novos sistemas, deve-se demonstrar:

1. que os três modos vivem no mesmo espaço de amplitudes tridimensional;
2. que a direção isotrópica é o modo coletivo correto;
3. que a saturação transversal é física;
4. que os dois modos conhecidos pertencem ao mesmo tripleto;
5. que o ramo escolhido é estável na Hessiana física.
