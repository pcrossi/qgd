# Q43 — extração de canais transversais

- entrada: `questoes/q43/associados/background_leptonico_h1mix_mu_q43.npz`
- classificação: H1 reduzido por mistura harmônica; sem alvo experimental
- dimensão: `3`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `1.161414653717858e-03`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610189101753911e+02 | -9.999999896528980e-01 | -9.999999896528980e-01 | 9.999999896528980e-01 | 8.610189101753909e+02 |
| 2 | 1.780317972803687e+05 | 1.438548013832150e-04 | 1.438548013832150e-04 | 1.438548013832150e-04 | 1.780317972803687e+05 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de \(K_i,J_i,\mu_i\).
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
