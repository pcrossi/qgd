# Saída — sela torsional conformal normalizada

Classificação: avaliação direta de quantidade analiticamente derivada, teste
de consistência e refinamento de tolerância. Não é ajuste nem previsão
metrológica.

O limiar é:

$$
q_c=\frac85=1.6.
$$

| $q$ | $u_*$ | $a_*\sqrt{\tau}$ | resíduo | $d^2\mathcal A/du^2$ | $K_{aa}/\tau$ |
|---:|---:|---:|---:|---:|---:|
| 2 | $6.09305738678128\times10^{-3}$ | $7.80580385788759\times10^{-2}$ | $1.248\times10^{-11}$ | $4.717199032584\times10^3$ | $1.149686576416\times10^2$ |
| 3 | $1.69609668096626\times10^{-2}$ | $1.30234276631241\times10^{-1}$ | $5.201\times10^{-12}$ | $4.837836786632\times10^3$ | $3.282175566745\times10^2$ |
| 5 | $3.02314201305214\times10^{-2}$ | $1.73871849735722\times10^{-1}$ | $7.475\times10^{-12}$ | $5.025178541310\times10^3$ | $6.076731348529\times10^2$ |
| 10 | $4.73432159438978\times10^{-2}$ | $2.17584962586797\times10^{-1}$ | $1.228\times10^{-11}$ | $5.369106554961\times10^3$ | $1.016763084229\times10^3$ |

## Refinamento por tolerância para $q=2$

| tolerância da bisseção | $u_*$ | resíduo |
|---:|---:|---:|
| $10^{-6}$ | $6.09307062058222\times10^{-3}$ | $6.243\times10^{-5}$ |
| $10^{-8}$ | $6.09305997689565\times10^{-3}$ | $1.222\times10^{-5}$ |
| $10^{-10}$ | $6.09305739912781\times10^{-3}$ | $5.823\times10^{-8}$ |
| $10^{-12}$ | $6.09305738656812\times10^{-3}$ | $1.018\times10^{-9}$ |
| $10^{-14}$ | $6.09305738678128\times10^{-3}$ | $1.248\times10^{-11}$ |

As pequenas não monotonicidades do resíduo final resultam do arredondamento
de ponto flutuante. A raiz converge e a curvatura reduzida permanece
estritamente positiva.

A última coluna avalia diretamente:

$$
\frac{K_{aa}}{\tau}
=
4u_*\frac{d^2\mathcal A}{du^2}.
$$

Ela é a rigidez da direção conformal normalizada. Não é ainda o menor
autovalor da Hessiana física 8D, porque a norma cinética do modo e os blocos
mistos ainda precisam ser avaliados.
