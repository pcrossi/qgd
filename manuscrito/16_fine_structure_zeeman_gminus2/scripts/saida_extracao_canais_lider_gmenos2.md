# Capítulo 16 — extração de canais transversais

- entrada: `manuscrito/16_fine_structure_zeeman_gminus2/scripts/hessiana_lider_gmenos2.npz`
- classificação: termo líder derivado por Noether e forma harmônica
- dimensão: `2`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `1.161409732097665e-03`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610225765836003e+02 | 1.000000000000000e+00 | 1.000000000000000e+00 | 1.000000000000000e+00 | 8.610225765836003e+02 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de $K_i,J_i,\mu_i$.
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
