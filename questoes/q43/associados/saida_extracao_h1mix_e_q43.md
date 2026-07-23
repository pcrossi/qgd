# Q43 — extração de canais transversais

- entrada: `questoes/q43/associados/background_leptonico_h1mix_e_q43.npz`
- classificação: H1 reduzido por mistura harmônica; sem alvo experimental
- dimensão: `3`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `1.161414653717859e-03`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.592501227326946e+02 | -7.071067811865475e-01 | -7.071067811865475e-01 | 7.071067811865475e-01 | 8.592501227326948e+02 |
| 2 | 8.627950304345057e+02 | 7.071067811865475e-01 | 7.071067811865475e-01 | 7.071067811865475e-01 | 8.627950304345059e+02 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de \(K_i,J_i,\mu_i\).
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
