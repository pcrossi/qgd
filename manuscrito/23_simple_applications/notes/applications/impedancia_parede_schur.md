---
title: "Impedância de parede por Schur"
---

# Impedância de parede por Schur

Status: derivação variacional reduzida.

## Partição da Hessiana

Se o modo do poço vive na interface $Y$ e os graus da parede vivem em $I$,
escrevemos a forma quadrática:

$$
Q[y,u]
=
\frac12
\begin{pmatrix}
y\\u
\end{pmatrix}^{\!T}
\begin{pmatrix}
K_{YY} & K_{YI}\\
K_{IY} & K_{II}
\end{pmatrix}
\begin{pmatrix}
y\\u
\end{pmatrix}.
$$

Variação em $u$ dá:

$$
K_{II}u+K_{IY}y=0.
$$

Se $K_{II}$ é inversível no subespaço físico:

$$
u_\ast=-K_{II}^{-1}K_{IY}y.
$$

Substituindo:

$$
Q_{\rm eff}[y]
=
\frac12y^T
\left(
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}
\right)y.
$$

Logo:

$$
\mathsf R_{\rm wall}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

## Parede homogênea unidimensional

Na parede:

$$
-u''+(V_0-E)u=0.
$$

Com face externa Dirichlet em espessura $d$:

$$
u(s)=A\sinh\left(\kappa(d-s)\right),
\qquad
\kappa=\sqrt{V_0-E}.
$$

O mapa Dirichlet--Neumann na interface é:

$$
\lambda(E)
=
\kappa\coth(\kappa d).
$$

Essa é a impedância usada no script numérico.

## Condição espectral simétrica

Para um poço de comprimento $L=1$ com impedância igual nas duas faces:

$$
\left(\lambda^2-k^2\right)\sin k
+
2k\lambda\cos k
=0,
\qquad
k=\sqrt E.
$$

As raízes dão o espectro Robin/DtN.
