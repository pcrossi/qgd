# Saída — Q55 Hessiana do setor de fase/circulação

Classificação: avaliação direta de Hessiana reduzida / teste de estabilidade de fase.

## Forma quadrática


$$
Q_\theta[\delta\theta]
=
\frac12\int\rho\,|\nabla\delta\theta|^2dV
$$

Operador:

$$
K_\theta=-\nabla\cdot(\rho\nabla)
$$

## Configuração

- lambda_T = `3.0`
- n_grid = `900`
- ell_max = `8`
- solve_bvp success = `True`

## Resumo espectral


| ell | negativos físicos | zeros | menor físico não-zero |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1.056785821936e-01 |
| 1 | 0 | 0 | 6.572554660398e-02 |
| 2 | 0 | 0 | 1.186610494145e-01 |
| 3 | 0 | 0 | 1.615578938606e-01 |
| 4 | 0 | 0 | 2.005246164996e-01 |
| 5 | 0 | 0 | 2.395909207183e-01 |
| 6 | 0 | 0 | 2.805539648285e-01 |
| 7 | 0 | 0 | 3.242011125002e-01 |
| 8 | 0 | 0 | 3.709073585082e-01 |

## Primeiros autovalores por ell


### ell = 0
- lambda[1] = `8.536256780627e-13`
- lambda[2] = `1.056785821936e-01`
- lambda[3] = `1.826473698155e-01`
- lambda[4] = `2.886338425683e-01`
- lambda[5] = `4.284610788606e-01`
- lambda[6] = `6.008785865757e-01`

### ell = 1
- lambda[1] = `6.572554660398e-02`
- lambda[2] = `1.451621816014e-01`
- lambda[3] = `2.323144266348e-01`
- lambda[4] = `3.542385056663e-01`
- lambda[5] = `5.096624460566e-01`
- lambda[6] = `6.976236684310e-01`

### ell = 2
- lambda[1] = `1.186610494145e-01`
- lambda[2] = `1.885366726910e-01`
- lambda[3] = `2.898514667221e-01`
- lambda[4] = `4.266565032446e-01`
- lambda[5] = `5.970902475199e-01`
- lambda[6] = `8.002402511568e-01`

### ell = 3
- lambda[1] = `1.615578938606e-01`
- lambda[2] = `2.380753161646e-01`
- lambda[3] = `3.535288300642e-01`
- lambda[4] = `5.048252938444e-01`
- lambda[5] = `6.900605957069e-01`
- lambda[6] = `9.082584308323e-01`

### ell = 4
- lambda[1] = `2.005246164996e-01`
- lambda[2] = `2.917118448277e-01`
- lambda[3] = `4.219048906012e-01`
- lambda[4] = `5.879168829865e-01`
- lambda[5] = `7.880377882369e-01`
- lambda[6] = `1.021304409855e+00`

### ell = 5
- lambda[1] = `2.395909207183e-01`
- lambda[2] = `3.482272404520e-01`
- lambda[3] = `4.941405554420e-01`
- lambda[4] = `6.753635077108e-01`
- lambda[5] = `8.906213734036e-01`
- lambda[6] = `1.139084601348e+00`

### ell = 6
- lambda[1] = `2.805539648285e-01`
- lambda[2] = `4.075492506559e-01`
- lambda[3] = `5.699127037593e-01`
- lambda[4] = `7.668396303530e-01`
- lambda[5] = `9.975371421924e-01`
- lambda[6] = `1.261377830705e+00`

### ell = 7
- lambda[1] = `3.242011125002e-01`
- lambda[2] = `4.698976637612e-01`
- lambda[3] = `6.491660332220e-01`
- lambda[4] = `8.621905622301e-01`
- lambda[5] = `1.108613750369e+00`
- lambda[6] = `1.388025844593e+00`

### ell = 8
- lambda[1] = `3.709073585082e-01`
- lambda[2] = `5.354847152117e-01`
- lambda[3] = `7.319443757888e-01`
- lambda[4] = `9.613598196140e-01`
- lambda[5] = `1.223752845772e+00`
- lambda[6] = `1.518920554711e+00`

## Veredito

O setor de fase/circulação não possui autovalores físicos negativos nos harmônicos testados.

O zero em ell=0 é a fase global protegida por Noether e não representa instabilidade.