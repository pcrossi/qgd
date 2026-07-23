# Saída — Q55 blocos restantes da Hessiana reduzida

Classificação: avaliação reduzida / diagnóstico espectral e de acoplamentos.

Não é Hessiana covariante 8D completa.

## Background

- eta = `8.0`
- lambda_T = `3.0`
- horizontes = `[4.222352820612852, 15.957122727990576]`
- patch exterior usado = `[1.620724e+01, 2.449999e+01]`

## K_HH — setor torsional independente reduzido


| ell | menor autovalor |
|---:|---:|
| 0 | 1.475541776890e-01 |
| 1 | 1.524617139739e-01 |
| 2 | 1.622695375049e-01 |
| 3 | 1.769631958865e-01 |
| 4 | 1.965211277219e-01 |
| 5 | 2.209148144900e-01 |
| 6 | 2.501089991184e-01 |
| 7 | 2.840619851115e-01 |
| 8 | 3.227260289633e-01 |

## K_gg — setor métrico axial exterior reduzido


| ell | menor autovalor |
|---:|---:|
| 2 | 1.493545907614e-01 |
| 3 | 1.523112362920e-01 |
| 4 | 1.562520278601e-01 |
| 5 | 1.611757568377e-01 |
| 6 | 1.670809043133e-01 |
| 7 | 1.739656357498e-01 |
| 8 | 1.818277943550e-01 |

## Acoplamentos cruzados reduzidos


- ||K_gf|| reduzido = `6.166879064740e-04`
- ||K_gH|| reduzido = `8.076881453156e-06`
- gap escalar usado = `1.909625790263e-03`
- gap fase usado = `6.572554660398e-02`
- gap K_HH = `1.475541776890e-01`
- gap K_gg = `1.493545907614e-01`
- razão Schur gf = `1.333410946325e-03`
- razão Schur gH = `2.960174621482e-09`

## Modos de horizonte e Page toy

- horizonte 1: kappa = `1.465301433319e-01`, T = `2.332099662324e-02`
- horizonte 2: kappa = `3.044070699662e-02`, T = `4.844788989724e-03`
- pesos de canais toy = `[0.9999980969946938, 1.90300515759935e-06, 8.794135715905771e-14, 6.064588145332285e-14]`
- S_Page_toy(0) = `0.000000000000e+00`
- max S_Page_toy = `2.696953704284e-05`
- S_Page_toy(1) = `0.000000000000e+00`

## Veredito

- negativos K_HH = `0`
- negativos K_gg = `0`
Os blocos torsional independente e métrico axial exterior reduzidos são positivos nos setores testados.

As razões Schur são diagnósticos de mistura; se pequenas, os acoplamentos cruzados não fecham o gap. Se grandes, exigem diagonalização acoplada completa.

A Page curve aqui é toy unitário de canais positivos; ainda não é cálculo físico final de informação.