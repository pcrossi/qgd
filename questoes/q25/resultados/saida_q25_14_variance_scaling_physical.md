# Q25.14 — Escala de variância/autocorrelação

Classificação: teste de escala numérico no benchmark reduzido.

| L | N | tau_corr | stderr_eff | acceptance |
|---:|---:|---:|---:|---:|
| 4 | 16 | 8.241905 | 3.313050687431e-03 | 0.751829 |
| 6 | 36 | 17.523244 | 3.053721546693e-03 | 0.756871 |
| 8 | 64 | 30.118337 | 2.933880755648e-03 | 0.760686 |

Ajuste observado: `tau_corr ~ N^0.934`.

Interpretação: no intervalo testado não aparece explosão exponencial. Isto ainda não é prova assintótica; é filtro numérico inicial para a classe reduzida.
