# Saída — matriz de Gram torsional em \(T^4\)

## Parâmetros diagnósticos

Foram usados raios anisotrópicos:

\[
(R_1,R_2,R_3,R_4)=(1,1{,}2,0{,}8,1{,}5).
\]

O objetivo não foi fixar os raios físicos, mas testar as fórmulas para um caso
não trivial.

## Matriz topológica

Na ordem \((12,13,14,23,24,34)\):

\[
\operatorname{diag}G^{\rm top}
=(1,\,2{,}25,\,0{,}64,\,1{,}5625,\,0{,}4444444444,\,1).
\]

Os pares complementares são recíprocos com erro máximo

\[
3{,}33\times10^{-16}.
\]

## Operador de Hodge na base canônica

\[
*=
\begin{pmatrix}
0&0&0&0&0&1\\
0&0&0&0&-1&0\\
0&0&0&1&0&0\\
0&0&1&0&0&0\\
0&-1&0&0&0&0\\
1&0&0&0&0&0
\end{pmatrix}.
\]

## Verificações

| Teste | Erro |
|---|---:|
| \(\|*^2-I\|_\infty\) | \(3{,}33\times10^{-16}\) |
| \(\|G_{\rm can}-I\|_\infty\) | \(2{,}22\times10^{-16}\) |
| autodualidade do triplet \(+\) | \(1{,}11\times10^{-16}\) |
| anti-autodualidade do triplet \(-\) | \(1{,}11\times10^{-16}\) |
| ortonormalidade do triplet \(+\) | \(2{,}22\times10^{-16}\) |
| ortonormalidade do triplet \(-\) | \(2{,}22\times10^{-16}\) |
| ortogonalidade cruzada | \(5{,}55\times10^{-17}\) |
| norma de \(n^i\Sigma_i^+\) | 1,000000000000 |

## Veredito

O teste confirma a matriz de Gram, a transformação para a base canônica e a
decomposição \(3+3\) para raios arbitrários. Ele não seleciona os raios nem a
quiralidade física.

