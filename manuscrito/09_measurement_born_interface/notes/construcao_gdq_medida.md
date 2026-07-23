---
title: "Construção GDQ da medida"
---

# Construção GDQ da medida

## 1. Enunciado

Uma medição não é introdução manual de operador quântico. É um problema de
interface entre um objeto GDQ e um aparelho clássico.

A cadeia é:

$$
J_{\rm app}^{\rm clássico}
\to
\Phi_\ast
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\text{projetores efetivos}
\to
\text{registro}.
$$

## 2. Fonte ou contorno do aparelho

O aparelho fornece dados clássicos:

$$
J_{\rm app},
\qquad
C_{\rm app},
\qquad
\partial M_{\rm app}.
$$

Esses dados selecionam um domínio físico. Eles não alteram a ação oficial.

O background com aparelho satisfaz:

$$
\left.
\frac{\delta}
{\delta\Phi}
\left(
\mathcal S_{\rm GDQ}
+
\mathcal S_{\rm app}
\right)
\right|_{\Phi_\ast}
=
0.
$$

Aqui $\mathcal S_{\rm app}$ representa a imposição de contorno/fonte do
experimento, não um novo termo fundamental.

## 3. Hessiana e resposta de interface

No background $\Phi_\ast$:

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi}
\right|_{\Phi_\ast}
P_{\rm phys}.
$$

Separando fronteira e interior:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}.
$$

A resposta efetiva do aparelho é:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## 4. Projetores e probabilidades

O aparelho define alternativas macroscópicas exclusivas. No Hilbert físico
reconstruído, essas alternativas são representadas por projetores:

$$
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I.
$$

A regra operacional é:

$$
\mu(P_i)=\operatorname{Tr}(\varrho P_i).
$$

No estado puro:

$$
\mu(P_i)=|\langle i|\psi\rangle|^2.
$$

## 5. Resultado individual

A GDQ estrutural fornece probabilidades, canais e resposta. Um resultado
individual único exige uma bacia dinâmica real do conjunto
objeto--aparelho--ambiente. Esse ponto é condicional, não omitido.
