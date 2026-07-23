# Q25.19 — Derivação Schur do bloco térmico/aparelho

Classificação: derivação reduzida e teste de consistência.

Modo observado: diferença de circulação no primeiro vínculo da rede. O complemento ortogonal é tratado como aparelho/banho reduzido.

| quantidade | valor |
|---|---:|
| K_H | 1.930000000000e+00 |
| chi_A=J K_A^-1 J^T | 2.229537798681e-01 |
| K_schur | 1.707046220132e+00 |
| chi_2=J K_A^-2 J^T | 1.593233959409e-01 |

| candidato Schur | mu_A | Theta_A | RMSE beta | erro relativo RMS |
|---|---:|---:|---:|---:|
| `second_response` | 5.54521554e-01 | 6.16921719e-01 | 1.02808630e-01 | 4.42758755e-01 |
| `schur_symmetric` | 6.55973166e-01 | 6.55973166e-01 | 1.47102400e-01 | 6.05137732e-01 |
| `schur_geometric` | 6.55973166e-01 | 6.16921719e-01 | 1.72753199e-01 | 6.38041444e-01 |
| `bare_response` | 1.93000000e+00 | 1.70704622e+00 | 3.90128915e-01 | 1.72790290e+00 |
| `bare_schur` | 2.22953780e-01 | 1.70704622e+00 | 4.15812481e-01 | 7.43693650e-01 |
| `referencia_ajustada` | 5.73747482e-01 | 7.21527850e-01 | 8.95660057e-02 | 4.25293304e-01 |

Comparação ponto a ponto:

| kBT/t | beta invertido | beta Schur melhor | beta ajustado |
|---:|---:|---:|---:|
| 0.000 | 7.63442723e-01 | 8.98852378e-01 | 7.95184111e-01 |
| 0.450 | 5.19445430e-01 | 5.19739681e-01 | 4.89742930e-01 |
| 0.550 | 5.91747963e-01 | 4.75200303e-01 | 4.51226831e-01 |
| 0.900 | 2.93897795e-01 | 3.65557133e-01 | 3.53831408e-01 |
| 1.500 | 1.36273764e-01 | 2.61947123e-01 | 2.58267067e-01 |

Veredito: o complemento de Schur fornece uma derivação reduzida não ajustada para a escala de admitância térmica. O melhor candidato Schur melhora a forma e é fisicamente interpretável, mas ainda não reproduz o mapa térmico invertido com precisão metrológica. A diferença restante deve vir de geometria de aparelho mais rica, modos de banho não incluídos, mobilidade causal ou contorno térmico real.
