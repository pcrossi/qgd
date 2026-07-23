# Saída — verificação Schur/projetor

Classificação: teste de consistência simbólico-numérico.

Este script verifica a construção:

$$
K_{\rm phys}
=
P_{\rm phys}^T K_{\rm GDQ}P_{\rm phys},
\qquad
\mathsf R
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

## Diagnóstico do projetor

| quantidade | valor |
|---|---:|
| posto físico | 3 |
| erro de idempotência `||P^2-P||` | 1.359739955511e-16 |
| erro de vínculo `||CP||` | 1.922962686384e-16 |

## Espectro físico reduzido

| autovalor | valor |
|---:|---:|
| 1 | 2.238526251288e+00 |
| 2 | 2.715698081194e+00 |
| 3 | 5.345775667518e+00 |

## Gap interno

| autovalor de K_II | valor |
|---:|---:|
| 1 | 2.248338852158e+00 |
| 2 | 2.751661147842e+00 |

## Resposta de Schur

| quantidade | valor |
|---|---:|
| R_app toy | 5.252882543103e+00 |

Interpretação: a álgebra de projeção física e redução de Schur é consistente.
Para obter um solenoide real, deve-se substituir esta matriz toy pela Hessiana
da ação oficial avaliada no background físico do aparelho.
