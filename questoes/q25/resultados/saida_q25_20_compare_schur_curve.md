# Q25.20 — Comparação direta da curva Schur

Classificação: comparação fenomenológica externa usando o mapa Schur não ajustado de Q25.19.

| kBT/t | C_s(1) exp | erro exp | beta_Schur | C_s(1) GDQ-Schur | erro MC | z |
|---:|---:|---:|---:|---:|---:|---:|
| 0.000 | -3.50000000e-01 | 2.000e-02 | 8.98852378e-01 | -4.50850000e-01 | 1.083e-03 | -5.042 |
| 0.450 | -2.10000000e-01 | 2.000e-02 | 5.19739681e-01 | -2.10714286e-01 | 8.026e-04 | -0.036 |
| 0.550 | -2.40000000e-01 | 2.000e-02 | 4.75200303e-01 | -1.80110714e-01 | 7.531e-04 | 2.994 |
| 0.900 | -1.10000000e-01 | 2.000e-02 | 3.65557133e-01 | -1.29633929e-01 | 7.075e-04 | -0.982 |
| 1.500 | -5.00000000e-02 | 2.000e-02 | 2.61947123e-01 | -9.36107143e-02 | 6.923e-04 | -2.181 |

Veredito: a rota Schur acerta muito bem o ponto intermediário `kBT/t=0.45`, mantém sinal correto em toda a série digitizada, mas superestima a correlação em `T=0` e em alta temperatura. O ponto `kBT/t=0.55` permanece suspeito por violar monotonicidade da própria digitização.
