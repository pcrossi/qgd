# Q43 — extração de canais transversais

- entrada: `questoes/q43/associados/hessiana_lider_q43.npz`
- classificação: avaliação direta do bloco líder derivado
- dimensão: `2`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `1.161409732097665e-03`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610225765836003e+02 | 1.000000000000000e+00 | 1.000000000000000e+00 | 1.000000000000000e+00 | 8.610225765836003e+02 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de \(K_i,J_i,\mu_i\).
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
