# Q43 — extração de canais transversais

- entrada: `questoes/q43/associados/hessiana_oficial_galerkin_nua_q43.npz`
- classificação: Galerkin oficial reduzido sem fonte magnética externa
- dimensão: `5`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `-0.000000000000000e+00`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | -5.337217757551488e+01 | 3.987859080130285e+01 | 0.000000000000000e+00 | 0.000000000000000e+00 | -5.337217757551485e+01 |
| 2 | 6.276683090818080e+00 | -1.039515698794529e-01 | 0.000000000000000e+00 | 0.000000000000000e+00 | 6.276683090818081e+00 |
| 3 | 2.501267296771635e+01 | 5.740065781233854e+00 | 0.000000000000000e+00 | 0.000000000000000e+00 | 2.501267296771632e+01 |
| 4 | 1.534017132776371e+02 | 3.228383449748677e+02 | 0.000000000000000e+00 | 0.000000000000000e+00 | 1.534017132776371e+02 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de \(K_i,J_i,\mu_i\).
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
