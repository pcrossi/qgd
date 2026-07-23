# Q25.17 — Candidatos Hessianos para o mapa térmico

Classificação: teste de consistência; resultado negativo útil.

Foram testados mapas construídos apenas com invariantes da Hessiana reduzida, sem usar os valores experimentais para ajustar coeficientes.

| candidato | RMSE beta | erro relativo RMS |
|---|---:|---:|
| `gap_over_T_plus_gap` | 2.22157647e-01 | 4.17572796e-01 |
| `sqrt_gap_kappa_over_T_plus_gap` | 3.09261852e-01 | 4.39542894e-01 |
| `spectral_ratio` | 3.23285854e-01 | 7.09387151e-01 |
| `kappa_over_T_plus_mean` | 3.52323245e-01 | 5.94934784e-01 |
| `offdiag_over_T_plus_gap` | 5.31936569e-01 | 7.38109948e-01 |

Melhor candidato sem alvo:

| kBT/t | beta invertido | beta candidato |
|---:|---:|---:|
| 0.000 | 7.63442723e-01 | 1.00000000e+00 |
| 0.450 | 5.19445430e-01 | 2.85714286e-01 |
| 0.550 | 5.91747963e-01 | 2.46575342e-01 |
| 0.900 | 2.93897795e-01 | 1.66666667e-01 |
| 1.500 | 1.36273764e-01 | 1.07142857e-01 |

Veredito: os candidatos estruturais capturam a forma decrescente esperada, mas não reproduzem quantitativamente o mapa invertido. Logo, o fator térmico do aparelho não é determinado apenas pelos invariantes escalares da Hessiana reduzida. É necessário incluir o bloco térmico/aparelho completo, mobilidade causal ou condições de contorno termodinâmicas.
