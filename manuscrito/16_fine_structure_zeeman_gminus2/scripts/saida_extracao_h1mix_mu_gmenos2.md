# Capítulo 16 — extração de canais transversais

- entrada: `manuscrito/16_fine_structure_zeeman_gminus2/scripts/background_leptonico_h1mix_mu_gmenos2.npz`
- classificação: mistura H1 reduzida do múon; permitido, não metrologia final
- dimensão: `3`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `1.161414653717858e-03`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610189101754544e+02 | -9.999999896529351e-01 | -9.999999896529351e-01 | 9.999999896529351e-01 | 8.610189101754544e+02 |
| 2 | 1.780324307730558e+05 | 1.438545429561274e-04 | 1.438545429561274e-04 | 1.438545429561274e-04 | 1.780324307730559e+05 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de $K_i,J_i,\mu_i$.
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
