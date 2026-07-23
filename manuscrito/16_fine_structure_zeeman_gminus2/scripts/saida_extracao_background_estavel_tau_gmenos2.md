# Capítulo 16 — extração de canais transversais

- entrada: `manuscrito/16_fine_structure_zeeman_gminus2/scripts/background_leptonico_estavel_tau_gmenos2.npz`
- classificação: background efetivo mínimo do tau; termo líder apenas
- dimensão: `3`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `1.161409732097665e-03`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610225765836003e+02 | 1.000000000000000e+00 | 1.000000000000000e+00 | 1.000000000000000e+00 | 8.610225765836003e+02 |
| 2 | 2.994159863649186e+06 | -0.000000000000000e+00 | 0.000000000000000e+00 | 0.000000000000000e+00 | 2.994159863649186e+06 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de $K_i,J_i,\mu_i$.
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
