# Capítulo 16 — extração de canais transversais

- entrada: `manuscrito/16_fine_structure_zeeman_gminus2/scripts/hessiana_oficial_galerkin_lider_gmenos2.npz`
- classificação: Galerkin reduzido com fonte líder de contorno; teste, não previsão metrológica
- dimensão: `5`
- gamma0: `1.000000000000000e+00`
- a_geom reconstruído: `-4.679511477749478e-04`

| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |
|---:|---:|---:|---:|---:|---:|
| 1 | -5.337217757551488e+01 | 3.987859080130285e+01 | -2.056371014553084e-03 | 2.056371014553084e-03 | -5.337217757551485e+01 |
| 2 | 6.276683090818080e+00 | -1.039515698794529e-01 | 9.999738775495080e-01 | 9.999738775495080e-01 | 6.276683090818081e+00 |
| 3 | 2.501267296771635e+01 | 5.740065781233854e+00 | 1.597714508062545e-03 | 1.597714508062545e-03 | 2.501267296771632e+01 |
| 4 | 1.534017132776371e+02 | 3.228383449748677e+02 | 6.742615605441424e-03 | 6.742615605441424e-03 | 1.534017132776371e+02 |

## Leitura

Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de $K_i,J_i,\mu_i$.
Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.
