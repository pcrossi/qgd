# Q29 — Berger nos três estômatos: modos comum e relativos

## 1. Decomposição universal

Escreva

$$
q_a=1+s_a,
\qquad a=1,2,3.
$$

O acoplamento conservativo mais geral de segunda ordem com simetria cíclica
$C_3$ contém o Laplaciano do triângulo:

$$
L_{C_3}
=\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix}.
$$

A Hessiana de squashing tem a forma

$$
H_{3q}
=h_qI_3+\kappa_qL_{C_3},
$$

onde o cálculo de Berger após Schur radial forneceu

$$
h_q=-2{,}6709085613.
$$

## 2. Espectro

O Laplaciano possui espectro

$$
\operatorname{spec}L_{C_3}=\{0,3,3\}.
$$

Consequentemente,

$$
\boxed{
\operatorname{spec}H_{3q}
=\{h_q,h_q+3\kappa_q,h_q+3\kappa_q\}.
}
$$

O autovetor do primeiro autovalor é o modo comum

$$
s_{\rm com}
=\frac1{\sqrt3}(1,1,1).
$$

Como

$$
L_{C_3}s_{\rm com}=0,
$$

nenhuma rigidez puramente relativa modifica $h_q$. Portanto,

$$
\boxed{
\text{os modos relativos não estabilizam o runaway comum de Berger.}
}
$$

## 3. O que eles podem estabilizar

Os dois modos relativos tornam-se positivos se

$$
\kappa_q>\kappa_q^{\rm crit}
=-\frac{h_q}{3}
=0{,}8903028538.
$$

Esse critério é útil, mas $\kappa_q$ não pode ser identificado automaticamente
com a rigidez angular $\kappa_{\rm rel}T^2$ da Q28: rotação de circulação e
squashing métrico são direções diferentes da Hessiana.

## 4. Possível remoção do modo comum

O modo negativo somente desaparece se existir um vínculo global independente,
por exemplo

$$
\sum_{a=1}^3s_a=0,
$$

que remova $s_{\rm com}$ do espaço físico. O vínculo de fluxo de Noether já
testado não impõe essa igualdade: ele permite que a densidade torsional se
ajuste durante o squashing comum.

Impor $\sum s_a=0$ sem derivá-lo de uma condição cosmológica de volume ou
holonomia seria ad hoc. Além disso, ele impediria três gargantas de adquirirem
o mesmo $q>1$, de modo que o transporte eletrofraco teria de ser calculado
como média de uma configuração anisotrópica, não pela fórmula homogênea.

## 5. Veredito

Os três estômatos não fornecem automaticamente a estabilização ausente:

$$
\boxed{
\text{$C_3$ pode estabilizar diferenças, mas não o squashing comum.}
}
$$

Para salvar Berger é necessária uma rigidez absoluta de cisalhamento ou um
vínculo global que retire o modo comum, ambos derivados da ação/contorno
cosmológico.
