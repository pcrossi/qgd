# Saída — teste da sobreposição Hopf--campo

## Parâmetros

Foi usada a mesma métrica anisotrópica de teste:

\[
(R_1,R_2,R_3,R_4)=(1,1{,}2,0{,}8,1{,}5).
\]

Foram gerados 10.000 vetores aleatórios de Hopf, campos e rotações em
\(SO(3)\).

## Resultados

| Verificação | Erro máximo |
|---|---:|
| \(\langle\Omega(n),\Omega(B)\rangle-n\cdot B\) | \(1{,}776\times10^{-15}\) |
| norma do modo de Hopf | \(8{,}882\times10^{-16}\) |
| invariância sob rotações simultâneas | \(2{,}665\times10^{-15}\) |

O teste confirma que a matriz de Gram absorve corretamente a anisotropia dos
raios e preserva a contração física \(\boldsymbol n\cdot\boldsymbol B\).

## Perfil centrado

Para perfil gaussiano com \(\sigma=0{,}17\), a quadratura encontrou:

\[
\langle z\rangle=0,
\]

\[
\langle z^2\rangle=0{,}0289=\sigma^2,
\]

com erro \(3{,}47\times10^{-18}\). Isso confirma o cancelamento da correção
linear para um estômato centrado e a primeira correção quadrática de tamanho
finito.

## Status

Teste algébrico concluído. Ele não fixa \(I_H\), \(\ell_B\) nem o momento
magnético físico.

