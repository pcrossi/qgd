---
title: "Construção GDQ do Hilbert físico e da quantização"
---

# Construção GDQ do Hilbert físico e da quantização

## 1. Enunciado

O espaço de Hilbert não é axioma primário da GDQ. Ele é reconstruído como a
camada operacional de um setor geométrico regular.

A construção é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm GDQ}
\to
P_{\rm phys}
\to
K_{\rm phys}
\to
\mathcal H_{\rm phys}
\to
\text{operadores autoadjuntos}.
$$

## 2. Background admissível

Escolhe-se um background estacionário:

$$
\Phi_\ast=(g_\ast,J_\ast,H_\ast,f_\ast).
$$

Ele satisfaz a primeira variação da ação oficial no domínio considerado:

$$
\left.
\frac{\delta\mathcal S_{\rm GDQ}}{\delta\Phi}
\right|_{\Phi_\ast}
=
0.
$$

Este passo é condicional ao setor: sem background admissível, não há
reconstrução operacional daquele setor.

## 3. Hessiana e setor físico

A segunda variação define:

$$
K_{\rm GDQ}
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi}
\right|_{\Phi_\ast}.
$$

A Hessiana bruta contém vínculos, modos nulos e direções de calibre. O setor
físico é obtido por projeção:

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
K_{\rm GDQ}
P_{\rm phys}.
$$

O projetor preserva as variações compatíveis com carga, fluxo, normalização e
condições de bordo.

## 4. Produto interno

No setor Euclidiano refletido, a positividade de reflexão fornece:

$$
\langle [F],[G]\rangle_{\mathcal H}
=
\langle \Theta F\,G\rangle_E.
$$

Estados nulos e modos de calibre são quocientados:

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

No setor regular local, a representação reduzida é:

$$
\mathcal H_{\rm phys}
\simeq
L^2(N,E,d\Sigma_h).
$$

## 5. Operadores e quantização

Operadores físicos são formas fechadas da Hessiana ou geradores de simetrias
no setor projetado. A autoadjunticidade não é assumida por notação; ela exige:

1. domínio denso;
2. condições de bordo;
3. remoção de modos nulos;
4. positividade do produto interno físico.

Assim:

$$
\text{operador físico}
=
\text{gerador/forma quadrática em }
\mathcal H_{\rm phys}.
$$

## 6. Wallstrom e circulação

A fase é circular:

$$
e^{iS_R/\hbar}\in U(1).
$$

Portanto, em laço fechado:

$$
\oint dS_R
=
2\pi\hbar k,
\qquad
k\in\mathbb Z.
$$

Essa quantização não é acrescentada à hidrodinâmica. Ela vem da topologia do
fibrado de fase.

## 7. Incerteza

No setor regular, Cauchy--Schwarz no produto interno físico fornece:

$$
\Delta A\,\Delta B
\ge
\frac12
\left|
\langle [A,B]\rangle
\right|.
$$

Logo a incerteza é consequência de positividade Hermitiana e domínio de
operadores, não axioma isolado.

## 8. Limitação

Esta construção fecha o setor operacional regular. A reconstrução universal de
todos os backgrounds permanece condicionada à existência, positividade e
domínio de cada setor.
