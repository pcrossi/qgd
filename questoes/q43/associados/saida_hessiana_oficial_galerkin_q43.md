# Q43 — Hessiana oficial Galerkin reduzida

## Classificação

Galerkin oficial reduzido / teste de consistência. Não é previsão metrológica.

## Coordenadas

| índice | modo |
|---:|---|
| 0 | circulação/fase linear no ciclo |
| 1 | modo harmônico líder `sin(theta)` |
| 2 | modo fase superior `sin(2 theta)` |
| 3 | modo de densidade `cos(theta)` em `Re f` |
| 4 | modo métrico conformal `cos(theta)` |

## Autovalores da Hessiana bruta

| i | lambda_i |
|---:|---:|
| 0 | -1.062008119137641e+02 |
| 1 | -4.347916715816304e+01 |
| 2 | 6.276712765070020e+00 |
| 3 | 2.507972449201663e+01 |
| 4 | 5.752734465739256e+02 |

## Vetor de circulação

`c = [1. 0. 0. 0. 0.]`

## Fonte transversal da ação nua

A ação oficial sem fonte externa/aparelho não contém o funcional magnético `M[Phi;B]`.
Portanto, no setor nu:

$$
m_{\perp}^{\rm naked}=0.
$$

- `a_geom_naked = -0.0`

### Canais extraídos com fonte nua

| canal | K_i | J_i | mu_i | autovalor transversal |
|---:|---:|---:|---:|---:|
| 1 | -5.337217757551483e+01 | 3.987859080130288e+01 | 0.000000000000000e+00 | -5.337217757551483e+01 |
| 2 | 6.276683090818080e+00 | -1.039515698794529e-01 | 0.000000000000000e+00 | 6.276683090818081e+00 |
| 3 | 2.501267296771633e+01 | 5.740065781233856e+00 | 0.000000000000000e+00 | 2.501267296771631e+01 |
| 4 | 1.534017132776370e+02 | 3.228383449748675e+02 | 0.000000000000000e+00 | 1.534017132776371e+02 |

## Fonte líder de aparelho/contorno

A fonte líder usada na Q43 vem de Noether + projeção harmônica e não é termo novo da ação fundamental.
Neste teste, ela é representada pelo vetor unitário no modo 1:

`m_perp_leader = [0. 1. 0. 0. 0.]`

- `a_geom_raw_with_leader_source = -0.00046795114777494786`

### Canais extraídos com fonte líder

| canal | K_i | J_i | mu_i | autovalor transversal |
|---:|---:|---:|---:|---:|
| 1 | -5.337217757551483e+01 | 3.987859080130288e+01 | -2.056371014553084e-03 | -5.337217757551483e+01 |
| 2 | 6.276683090818080e+00 | -1.039515698794529e-01 | 9.999738775495080e-01 | 6.276683090818081e+00 |
| 3 | 2.501267296771633e+01 | 5.740065781233856e+00 | 1.597714508062543e-03 | 2.501267296771631e+01 |
| 4 | 1.534017132776370e+02 | 3.228383449748675e+02 | 6.742615605441424e-03 | 1.534017132776371e+02 |

## Veredito

A segunda variação da ação oficial reduzida fornece `H` e `c`.
Ela não fornece `m_perp` magnético sem especificar a fonte externa ou condição de contorno do aparelho.
Assim, os coeficientes `K_i` e `J_i` podem ser extraídos da Hessiana oficial Galerkin, mas `mu_i` exige o mapa físico `M[Phi;B]`.

A previsão metrológica completa de `g-2` continua dependente da construção do acoplamento magnético externo no background leptônico oficial.
