# Q25.18 — Bloco térmico/aparelho reduzido

Classificação: modelo efetivo de aparelho; comparação com mapa invertido.

O mapa testado é uma admitância térmica de contorno:

$$
\beta_{\rm eff}(\Theta)=\frac{\mu_A}{\Theta+\Theta_A},\qquad \Theta=k_BT/t.
$$

Primeiro foram testados candidatos sem alvo, usando apenas invariantes da Hessiana reduzida. Em seguida foi calculado o par efetivo de aparelho `(mu_A, Theta_A)` que melhor representa a curva invertida.

| mapa | mu_A | Theta_A | RMSE beta | erro relativo RMS |
|---|---:|---:|---:|---:|
| `gap_sqrt_gap_kappa` | 1.80000000e-01 | 2.50998008e-01 | 2.12545942e-01 | 4.29732164e-01 |
| `lam_min_gap` | 1.80000000e-01 | 1.80000000e-01 | 2.22157647e-01 | 4.17572796e-01 |
| `gap_gap` | 1.80000000e-01 | 1.80000000e-01 | 2.22157647e-01 | 4.17572796e-01 |
| `sqrt_gap_kappa_gap` | 2.50998008e-01 | 1.80000000e-01 | 3.09261852e-01 | 4.39542894e-01 |
| `kappa_gap` | 3.50000000e-01 | 1.80000000e-01 | 5.31936569e-01 | 7.38109948e-01 |
| `mean_gap` | 1.58000000e+00 | 1.80000000e-01 | 3.81235625e+00 | 6.04262294e+00 |
| `aparelho_efetivo_ajustado` | 5.73747482e-01 | 7.21527850e-01 | 8.95660057e-02 | 4.25293304e-01 |

Comparação do aparelho efetivo ajustado:

| kBT/t | beta invertido | beta aparelho ajustado |
|---:|---:|---:|
| 0.000 | 7.63442723e-01 | 7.95184111e-01 |
| 0.450 | 5.19445430e-01 | 4.89742930e-01 |
| 0.550 | 5.91747963e-01 | 4.51226831e-01 |
| 0.900 | 2.93897795e-01 | 3.53831408e-01 |
| 1.500 | 1.36273764e-01 | 2.58267067e-01 |

Veredito: o formato de admitância térmica de contorno é compatível com a inversão fenomenológica. Porém o par `(mu_A, Theta_A)` ainda é dado de aparelho/contorno ajustado, não derivado. Para fechar a Q25 em sentido forte, esses dois números precisam sair da Hessiana completa do aparelho e da mobilidade causal, não da curva de Parsons.
