# Q25.03 — Autocorrelação e variância

Classificação: teste de escala numérico em toy GDQ positivo.

| domínios | tau_corr_int | var_erro_media | gap espectral | 1/gap |
|---:|---:|---:|---:|---:|
| 4 | 1.741297 | 2.174997454751e-05 | 4.500000000000e-01 | 2.222222 |
| 8 | 0.830300 | 1.035815449279e-05 | 1.318019484661e-01 | 7.587141 |
| 16 | 0.660689 | 8.280017261690e-06 | 3.425421036992e-02 | 29.193492 |
| 32 | 0.631011 | 8.075217566882e-06 | 8.646623818546e-03 | 115.652077 |
| 64 | 0.615178 | 7.404259068431e-06 | 2.166872997511e-03 | 461.494514 |

Ajuste do observável testado: `tau_corr ~ C N^-0.340`.

Limite espectral de mistura: `1/gap ~ C N^1.933`.

Interpretação: no toy local em anel, o limite de mistura é compatível com escala polinomial quadrática. Isto é evidência numérica de classe reduzida, não prova para Hamiltonianos fermiônicos genéricos.
