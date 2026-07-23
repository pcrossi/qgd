# Saída — camadas por Hessiana angular reduzida Q51

Classificação: derivação reduzida / teste de consistência.

## Operador sem torção

O operador angular isotrópico sem cisão spin--torção dá:

$$
2,8,20,40,70,112,168,240,
$$

obtido pela soma dos degenerados do oscilador 3D:

$$
g_N=(N+1)(N+2).
$$

Fechamentos calculados: `[2, 8, 20, 40, 70, 112, 168, 240]`.

Isso não gera \(28,50,82,126\). Portanto, a parte sem torção falha para a estrutura nuclear pesada.

## Operador angular com cisão spin--torção

No setor de superfície, a Hessiana Dirac--Bismut reduzida tem a forma esquemática:

$$
K_{\rm ang}^{B}
=
K_{\rm osc}
+K_{L^2}
-K_{B}\,\mathbf L\cdot\mathbf S.
$$

A torção de Bismut separa \(j=l+1/2\) de \(j=l-1/2\). Contando a capacidade \(2j+1\) dos subníveis ordenados, obtém-se:

| orbital | capacidade | soma acumulada |
| --- | ---: | ---: |
| 1s1/2 | 2 | 2 ✓ |
| 1p3/2 | 4 | 6 |
| 1p1/2 | 2 | 8 ✓ |
| 1d5/2 | 6 | 14 |
| 2s1/2 | 2 | 16 |
| 1d3/2 | 4 | 20 ✓ |
| 1f7/2 | 8 | 28 ✓ |
| 2p3/2 | 4 | 32 |
| 1f5/2 | 6 | 38 |
| 2p1/2 | 2 | 40 |
| 1g9/2 | 10 | 50 ✓ |
| 1g7/2 | 8 | 58 |
| 2d5/2 | 6 | 64 |
| 2d3/2 | 4 | 68 |
| 3s1/2 | 2 | 70 |
| 1h11/2 | 12 | 82 ✓ |
| 1h9/2 | 10 | 92 |
| 2f7/2 | 8 | 100 |
| 2f5/2 | 6 | 106 |
| 3p3/2 | 4 | 110 |
| 3p1/2 | 2 | 112 |
| 1i13/2 | 14 | 126 ✓ |

Fechamentos gerados: `[2, 8, 20, 28, 50, 82, 126]`.

## Uso na Q51

A força de fechamento usada no background reduzido pode ser computada por:

$$
s_{\rm shell}(Z,N)
=
\frac{C_*}{d_Z^2+d_N^2+C_*},
\qquad
d_Z=\min_C|Z-C|,
\quad
d_N=\min_C|N-C|.
$$

Aqui \(C\) percorre os fechamentos gerados pelo espectro angular reduzido, não uma lista inserida manualmente.

## Veredito

A rota reduzida mostra por que a variável de fechamento de camada não deve ser tratada como etiqueta externa: ela corresponde à contagem de degenerescências do operador angular com torção. Ainda falta diagonalizar a Hessiana nuclear completa da ação oficial para transformar esta redução em derivação final.
