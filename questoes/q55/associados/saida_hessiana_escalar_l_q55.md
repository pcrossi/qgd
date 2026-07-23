# Saída — Q55 Hessiana escalar por harmônicos

Classificação: avaliação direta de Hessiana reduzida / teste de estabilidade escalar.

## Configuração

- lambda_T = `3.0`
- n_grid = `650`
- ell_max = `8`
- solve_bvp success = `True`
- mu = `-1.067957044153e-01`

## Resumo espectral


| ell | negativos físicos | zeros | menor físico não-zero |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 3.651456961676e-02 |
| 1 | 0 | 0 | 1.909625790263e-03 |
| 2 | 0 | 0 | 5.421300837083e-02 |
| 3 | 0 | 0 | 7.990922839410e-02 |
| 4 | 0 | 0 | 1.000824073959e-01 |
| 5 | 0 | 0 | 1.197517080975e-01 |
| 6 | 0 | 0 | 1.402655798448e-01 |
| 7 | 0 | 0 | 1.620974556422e-01 |
| 8 | 0 | 0 | 1.854523830588e-01 |

## Primeiros autovalores por ell


### ell = 0
- lambda[1] = `-5.982003087324e-13`
- lambda[2] = `3.651456961676e-02`
- lambda[3] = `8.720224552033e-02`
- lambda[4] = `1.442188279910e-01`
- lambda[5] = `2.180338702177e-01`
- lambda[6] = `3.073876163499e-01`

### ell = 1
- lambda[1] = `1.909625790263e-03`
- lambda[2] = `6.849785083508e-02`
- lambda[3] = `1.144513732029e-01`
- lambda[4] = `1.787628402848e-01`
- lambda[5] = `2.596798033833e-01`
- lambda[6] = `3.562648429794e-01`

### ell = 2
- lambda[1] = `5.421300837083e-02`
- lambda[2] = `9.197333162224e-02`
- lambda[3] = `1.447367577481e-01`
- lambda[4] = `2.157961821380e-01`
- lambda[5] = `3.035501443921e-01`
- lambda[6] = `4.072899584984e-01`

### ell = 3
- lambda[1] = `7.990922839410e-02`
- lambda[2] = `1.183090533974e-01`
- lambda[3] = `1.773838608278e-01`
- lambda[4] = `2.549680381933e-01`
- lambda[5] = `3.496039431643e-01`
- lambda[6] = `4.605541164394e-01`

### ell = 4
- lambda[1] = `1.000824073959e-01`
- lambda[2] = `1.457612431379e-01`
- lambda[3] = `2.117491118995e-01`
- lambda[4] = `2.962025901193e-01`
- lambda[5] = `3.979080985781e-01`
- lambda[6] = `5.161545111106e-01`

### ell = 5
- lambda[1] = `1.197517080975e-01`
- lambda[2] = `1.741849544538e-01`
- lambda[3] = `2.477786722269e-01`
- lambda[4] = `3.394991903481e-01`
- lambda[5] = `4.484819491463e-01`
- lambda[6] = `5.741212729197e-01`

### ell = 6
- lambda[1] = `1.402655798448e-01`
- lambda[2] = `2.038687069067e-01`
- lambda[3] = `2.855163395926e-01`
- lambda[4] = `3.848347706290e-01`
- lambda[5] = `5.012942580858e-01`
- lambda[6] = `6.344326201327e-01`

### ell = 7
- lambda[1] = `1.620974556422e-01`
- lambda[2] = `2.350300462380e-01`
- lambda[3] = `3.250069235017e-01`
- lambda[4] = `4.321779919196e-01`
- lambda[5] = `5.562943422281e-01`
- lambda[6] = `6.970422170294e-01`

### ell = 8
- lambda[1] = `1.854523830588e-01`
- lambda[2] = `2.678052945642e-01`
- lambda[3] = `3.662885272799e-01`
- lambda[4] = `4.815038826393e-01`
- lambda[5] = `6.134326726013e-01`
- lambda[6] = `7.618982045330e-01`

## Veredito

Nenhum harmônico escalar testado possui autovalor físico negativo.

Este teste cobre o bloco de amplitude escalar. Não cobre métrica, torção, fase/circulação nem modos de horizonte.