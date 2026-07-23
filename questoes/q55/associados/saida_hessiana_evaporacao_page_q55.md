# Saída — Q55 Hessiana proxy, evaporação e Page curve

Classificação: infraestrutura/consistência numérica. Não é a Hessiana
física completa da ação oficial.

## Espectro proxy exterior

| modo | lambda |
|---:|---:|
| 0 | 1.353032114277e-02 |
| 1 | 5.227880843521e-02 |
| 2 | 1.160420815956e-01 |
| 3 | 2.049041310475e-01 |
| 4 | 3.189339303145e-01 |
| 5 | 4.581746972141e-01 |
| 6 | 6.226513566782e-01 |
| 7 | 8.123771531212e-01 |
| 8 | 1.027357941649e+00 |
| 9 | 1.267594795017e+00 |
| 10 | 1.533085568272e+00 |
| 11 | 1.823825843120e+00 |

- menor autovalor proxy: `1.353032114277e-02`
- autovalores negativos proxy: `0`

## Temperatura do background M=1

| horizonte | r_H | T_H |
|---:|---:|---:|
| 1 | 2.687007885126e-01 | 4.729466919877e-01 |
| 2 | 1.967716165985e+00 | 3.848312781534e-02 |

## Evaporação efetiva por família M variável

- temperatura máxima na trilha: `5.372576469017e-02`
- primeira massa sem horizonte na trilha: `4.658227848101e-01`

## Page curve toy

- S_out inicial = `0.000000000000e+00`
- S_out máximo = `9.798171109842e-01`
- S_out final = `0.000000000000e+00`

## Veredito

A infraestrutura espectral/evaporativa roda e produz um comportamento
compatível com remanescente: temperatura cai a zero quando não há horizonte
na família efetiva. A Page curve aqui é apenas toy unitário; a curva física
exige os modos de saída de $K_{BH}^{phys}$ e o canal de informação GDQ.
