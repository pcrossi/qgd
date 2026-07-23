# Saída — Q55 Hessiana radial Schur

Classificação: avaliação direta de Hessiana reduzida / teste de estabilidade radial.

## Configuração

- lambda_T = `3.0`
- r_min = `0.0001`
- r_max = `25.0`
- n_grid interior = `650`
- h = `3.840230414747e-02`
- solve_bvp success = `True`
- mu = `-1.067957044153e-01`

## Espectro bruto


- lambda_raw[1] = `-1.927437459951e-01`
- lambda_raw[2] = `4.449094335401e-02`
- lambda_raw[3] = `8.783879478364e-02`
- lambda_raw[4] = `1.443371880926e-01`
- lambda_raw[5] = `2.180463070340e-01`
- lambda_raw[6] = `3.073881382512e-01`
- lambda_raw[7] = `4.119703922529e-01`
- lambda_raw[8] = `5.318224471612e-01`
- lambda_raw[9] = `6.670664468390e-01`
- lambda_raw[10] = `8.178124701853e-01`
- lambda_raw[11] = `9.841393427282e-01`
- lambda_raw[12] = `1.166099438502e+00`

## Espectro físico radial projetado


- lambda_phys[1] = `-5.982003087324e-13`
- lambda_phys[2] = `3.651456961676e-02`
- lambda_phys[3] = `8.720224552033e-02`
- lambda_phys[4] = `1.442188279910e-01`
- lambda_phys[5] = `2.180338702177e-01`
- lambda_phys[6] = `3.073876163499e-01`
- lambda_phys[7] = `4.119703872042e-01`
- lambda_phys[8] = `5.318224237610e-01`
- lambda_phys[9] = `6.670664374415e-01`
- lambda_phys[10] = `8.178124684697e-01`
- lambda_phys[11] = `9.841393424326e-01`
- lambda_phys[12] = `1.166099438466e+00`

## Contagem

- modos zero numéricos = `1`
- autovalores físicos negativos = `0`
- menor autovalor físico não-zero = `3.651456961676e-02`

## Convergência de malha


| n_grid | h | negativos | zeros | menor físico não-zero |
|---:|---:|---:|---:|---:|
| 300 | 8.305615e-02 | 0 | 1 | 3.650859450588e-02 |
| 450 | 5.543215e-02 | 0 | 1 | 3.651280931120e-02 |
| 650 | 3.840230e-02 | 0 | 1 | 3.651456961676e-02 |
| 850 | 2.937709e-02 | 0 | 1 | 3.651524343579e-02 |

## Veredito


O bloco radial de amplitude com Schur gravitacional não-local não possui autovalor físico negativo após remover a normalização.

Este resultado cobre apenas o setor radial de amplitude. Ele não substitui os setores métrico, torsional, fase e horizonte de `K_BH^phys`.