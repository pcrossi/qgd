# Q25 — Validação algorítmica mínima

Classificação global: teste de consistência + preparação de benchmark. Não é previsão cega e não fecha a complexidade assintótica geral.

## Execução

| script | status | saída |
|---|---:|---|
| `q25_01_domain_interface.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_01_domain_interface.md` |
| `q25_02_estimador_holonomia.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_02_estimador_holonomia.md` |
| `q25_03_autocorrelacao_variancia.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_03_autocorrelacao_variancia.md` |
| `q25_04_referencias_experimentais.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_04_referencias_experimentais.md` |
| `q25_05_compare_experiment.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_05_compare_experiment.md` |

## Resultados agregados


---

# Q25.01 — Domínios, interface e holonomia

Classificação: teste de consistência algorítmica GDQ.

| item | valor |
|---|---:|
| dominios | 4 |
| min rho_a | 1.605707873689e-01 |
| Hol(P_ij) | -1.0 |
| erro unitariedade fechado | 0.000000000000e+00 |
| min eig(I-S†S) aberto | 8.000000000000e-02 |
| erro conservacao norma | 5.551115123126e-17 |

Veredito: **aprovado**.

Interpretação: a medida local é positiva, a fase de troca fica em `Hol(P_ij)=-1`, a interface fechada conserva fluxo e a interface aberta é contrativa. Isto ainda não prova variância polinomial.


---

# Q25.02 — Estimador positivo de holonomia

Classificação: teste de consistência e comparação com solução exata finita.

| item | valor |
|---|---:|
| amostras | 200000 |
| média MC | 2.067129852407e-01 |
| valor exato finito | 2.059607668113e-01 |
| variância amostral | 5.337537043483e-01 |
| erro padrão | 1.633636594149e-03 |
| erro absoluto | 7.522184293929e-04 |
| erro relativo | 3.652241351781e-03 |

Interpretação: o sinal fermiônico aparece como holonomia no observável. Não há denominador de fase pequeno nesta classe finita. Isto não prova complexidade assintótica para sistemas genéricos.


---

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


---

# Q25.04 — Referências experimentais locais

Classificação: preparação de benchmark experimental.

| item | valor |
|---|---:|
| arquivo | `/home/pedro/Dropbox/obs/todo/questoes/q25/dados/q25_referencias_experimentais.csv` |
| linhas | 4 |
| linhas quantitativas | 0 |
| erros de parse | 0 |

Nenhum dado quantitativo foi extraído ainda; o arquivo contém apenas metadados e DOIs. A comparação experimental fica bloqueada até a extração manual dos valores das figuras/tabelas.


---

# Q25.05 — Comparação experimental

Classificação: comparação fenomenológica externa.

Não há comparação quantitativa ainda. Motivo: os dados experimentais locais ainda não têm valores numéricos extraídos e/ou a predição GDQ do observável correspondente ainda não foi implementada. O script está correto como bloqueio reprodutível, não como resultado negativo.


## Status conservador

O pacote prova que a rota positiva por domínios/holonomias é implementável em uma classe reduzida e reproduz solução exata finita sem reweighting de fase. A Q25 permanece aberta como fechamento computacional forte até existirem operador GDQ físico por benchmark, dados experimentais locais extraídos, estudo de escala por classe e cota de variância/complexidade.
