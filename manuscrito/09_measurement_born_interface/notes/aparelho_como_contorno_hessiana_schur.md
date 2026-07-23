---
title: "Aparelho como contorno e complemento de Schur"
---

# Aparelho como contorno e complemento de Schur

## Enunciado

Um aparelho clássico entra na GDQ como fonte, vínculo ou contorno. Na redução
linear em torno de um background admissível, seus graus internos geram uma
impedância efetiva de fronteira:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## Status

Redução efetiva variacional. Não altera a ação oficial.

## Construção

Considere flutuações físicas divididas em:

$$
\delta\Phi
=
(\delta\Phi_\partial,\delta\Phi_I).
$$

A segunda variação projetada da ação oficial no setor do aparelho tem a forma:

$$
\delta^2\mathcal S_{\rm eff}
=
\frac12
\begin{pmatrix}
\delta\Phi_\partial \\
\delta\Phi_I
\end{pmatrix}^{\!*}
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}
\begin{pmatrix}
\delta\Phi_\partial \\
\delta\Phi_I
\end{pmatrix}.
$$

Os graus internos não observados satisfazem a equação estacionária:

$$
K_{I\partial}\delta\Phi_\partial
+
K_{II}\delta\Phi_I
=0.
$$

Se $K_{II}$ é inversível no setor físico:

$$
\delta\Phi_I
=
-K_{II}^{-1}K_{I\partial}\delta\Phi_\partial.
$$

Substituindo de volta:

$$
\delta^2\mathcal S_{\rm eff}
=
\frac12
\delta\Phi_\partial^{*}
\left(
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}
\right)
\delta\Phi_\partial.
$$

Portanto:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## Interpretação física

$\mathsf R_{\rm app}$ é a resposta efetiva que o sistema medido sente na
fronteira. Ela contém rigidez, perdas, geometria do aparelho e acoplamento de
interface. Em aparelhos reais, seus valores dependem de material e fabricação.

Isso não é ajuste da ação oficial. É a escolha do problema físico de contorno.
