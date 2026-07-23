---
title: "Nota — Pipeline universal"
---

# Nota — Pipeline universal

A forma padrão é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*
\to
C_a[\Phi]=0
\to
P_{\rm phys}
\to
K_{\rm phys}
\to
J_{\rm app}
\to
\delta\Phi
\to
\mathsf R_{\rm app}
\to
\mathcal O_{\rm obs}.
$$

O ponto crítico é que a Hessiana sempre deve ser projetada:

$$
K_{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

Sem projetor, modos de gauge e modos de coordenada podem ser confundidos com
instabilidades físicas.

## Construção algébrica mínima

Se $K$ é a segunda variação da ação oficial no background $\Phi_*$ e
$D C$ é a matriz dos vínculos linearizados, o setor permitido satisfaz:

$$
D C\,\delta\Phi=0.
$$

Com uma métrica quadrática positiva $G$ no espaço de flutuações, o projetor
físico é:

$$
P_{\rm phys}
=
I
-
G^{-1}D C^\dagger
\left(D C\,G^{-1}D C^\dagger\right)^{-1}
D C.
$$

A compressão:

$$
K_{\rm phys}
=
P_{\rm phys}^\dagger K P_{\rm phys}
$$

é o operador que deve ser diagonalizado. Quando o observável vive apenas no
bordo ou no aparelho, decompõe-se o espaço físico em setor observado
$\partial$ e setor interno $I$:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}.
$$

Eliminando $I$:

$$
K_{\rm eff}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Esse complemento de Schur é a forma abstrata do operador DtN, da impedância
de aparelho e da resposta linear de superfície. Ele não é um termo novo da
ação; é o que a ação já implica após impor vínculos e eliminar graus de
liberdade não observados.
