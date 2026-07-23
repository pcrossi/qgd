# Saída — benchmark físico reduzido do problema do sinal

Classificação: benchmark reduzido + comparação fenomenológica externa.

## Parâmetros congelados do benchmark

| parâmetro | valor |
|---|---:|
| L | 4 |
| N | 16 |
| beta_eff | 0.45 |
| kappa_H | 0.35 |
| mass_gap | 0.18 |
| lambda_min(K_red) | 1.800000000000e-01 |
| lambda_max(K_red) | 2.980000000000e+00 |
| erro máximo de unitariedade Cayley | 2.316005379206e-16 |

## Enumeração exata e Monte Carlo positivo

| quantidade | exato | MC positivo |
|---|---:|---:|
| configurações | 65536 | 100000 amostras úteis |
| C_s(1) | -0.1698717343244 | -0.1683600000000 |
| erro padrão C_s(1) | — | 6.296328e-04 |
| C_s(2) | 0.0571480277850 | 0.0551700000000 |
| energia média | 10.7374365755796 | 10.7543680000000 |
| aceitação | — | 0.755150 |

## Comparação externa reduzida

| kBT/t | C_s(1) experimental | erro | C_s(1) GDQ-Schur | z |
|---:|---:|---:|---:|---:|
| 0.00 | -0.350000 | 0.020000 | -0.450850000 | -5.042 |
| 0.45 | -0.210000 | 0.020000 | -0.210714286 | -0.036 |
| 0.55 | -0.240000 | 0.020000 | -0.180110714 | 2.994 |
| 0.90 | -0.110000 | 0.020000 | -0.129633929 | -0.982 |
| 1.50 | -0.050000 | 0.020000 | -0.093610714 | -2.181 |

## Veredito

A medida usada no cálculo é positiva. A antissimetria fermiônica entra como holonomia de troca, não como peso negativo. O benchmark reduzido reproduz sinal e ordem de grandeza do correlator antiferromagnético frio, mas não constitui prova de algoritmo geral nem ajuste metrológico completo.
