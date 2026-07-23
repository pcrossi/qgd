---
title: "Derivação de Hopf dos projetores de Stern-Gerlach"
---

# Derivação de Hopf dos projetores de Stern-Gerlach

## Enunciado

O elo normal $S^3\subset\mathbb C^2$ do estômato induz projetores de posto um
em $\mathbb C^2$:

$$
P(u)=uu^\dagger.
$$

Eles podem ser escritos como:

$$
P(u)=\frac12(I+\mathbf n\cdot\sigma).
$$

## Prova

Seja:

$$
u=
\begin{pmatrix}
z_1\\
z_2
\end{pmatrix},
\qquad
u^\dagger u=1.
$$

Então:

$$
P=uu^\dagger
$$

satisfaz:

$$
P^2=P,
\qquad
P^\dagger=P,
\qquad
\operatorname{Tr}P=1.
$$

Toda matriz hermitiana $2\times2$ pode ser decomposta na base:

$$
I,\sigma_1,\sigma_2,\sigma_3.
$$

Como $\operatorname{Tr}P=1$, existe $\mathbf n$ tal que:

$$
P=\frac12(I+\mathbf n\cdot\sigma).
$$

Da condição $P^2=P$ segue:

$$
|\mathbf n|^2=1.
$$

Logo $\mathbf n\in S^2$.

O projetor complementar é:

$$
I-P=\frac12(I-\mathbf n\cdot\sigma).
$$

Assim, para o eixo do aparelho:

$$
P_{\mathbf n}^{\pm}
=
\frac12(I\pm\mathbf n\cdot\sigma).
$$

## Alcance

Essa é uma derivação local da estrutura de dois canais. A seleção metrológica
do eixo vem do campo magnético do aparelho.
