# Q25.13 — Correlações GDQ reduzidas

Classificação: avaliação direta em benchmark reduzido e comparação com solução exata finita.

| item | valor |
|---|---:|
| n_config_exact | 65536 |
| C_s_r1_exact | -1.698717343244e-01 |
| C_s_r1_mc | -1.683600000000e-01 |
| C_s_r1_stderr | 6.296327845454e-04 |
| C_s_r2_exact | 5.714802778502e-02 |
| C_s_r2_mc | 5.517000000000e-02 |
| C_s_r2_stderr | 8.558081181406e-04 |
| xi_corr_exact | 9.179375168066e-01 |
| energy_exact | 1.073743657558e+01 |
| energy_mc | 1.075436800000e+01 |
| acceptance | 7.551500000000e-01 |

Interpretação: a amostragem usa peso positivo `exp(-beta E_GDQ)`; a correlação antiferro aparece da circulação escalonada e da holonomia, não de peso negativo.
