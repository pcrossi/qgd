# Q43 — extração de canais transversais

- entrada: `questoes/q43/associados/hessiana_required_mu_q43.npz`
- classificação: diagnóstico inverso do bloco required do múon
- dimensão: `3`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `1.165920590000000e-03`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | 8.610225765836003e+02 | 1.000000000000000e+00 | 1.000000000000000e+00 | 1.000000000000000e+00 | 8.610225765836003e+02 |
| 2 | 1.780317936139604e+05 | 1.000000000000000e+00 | 8.030761230879372e-01 | 8.030761230879372e-01 | 1.780317936139604e+05 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de \(K_i,J_i,\mu_i\).
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
