# Q25 — Benchmark físico reduzido

Classificação global: benchmark físico reduzido + preparação de comparação experimental. Não é ainda previsão metrológica, pois faltam dados experimentais quantitativos locais.

## Execução

| script | status | saída |
|---|---:|---|
| `q25_10_extract_experimental_data.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_10_extract_experimental_data.md` |
| `q25_11_build_physical_domains.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_11_build_physical_domains.md` |
| `q25_12_derive_interface_from_hessian.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_12_derive_interface_from_hessian.md` |
| `q25_13_spin_correlations_gdq.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_13_spin_correlations_gdq.md` |
| `q25_14_variance_scaling_physical.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_14_variance_scaling_physical.md` |
| `q25_15_compare_experiment_physical.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_15_compare_experiment_physical.md` |
| `q25_16_thermal_ensemble_map.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_16_thermal_ensemble_map.md` |
| `q25_17_hessian_thermal_map_candidates.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_17_hessian_thermal_map_candidates.md` |
| `q25_18_thermal_apparatus_block.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_18_thermal_apparatus_block.md` |
| `q25_19_schur_apparatus_derivation.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_19_schur_apparatus_derivation.md` |
| `q25_20_compare_schur_curve.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_20_compare_schur_curve.md` |
| `q25_21_bath_width_correction.py` | 0 | `/home/pedro/Dropbox/obs/todo/questoes/q25/resultados/saida_q25_21_bath_width_correction.md` |

## Resultados


---

# Q25.10 — Dados experimentais locais

Classificação: preparação de benchmark experimental.

| item | valor |
|---|---:|
| arquivo bruto | `/home/pedro/Dropbox/obs/todo/questoes/q25/dados/q25_referencias_experimentais.csv` |
| arquivo limpo | `/home/pedro/Dropbox/obs/todo/questoes/q25/dados/q25_experimental_clean.csv` |
| linhas totais | 15 |
| linhas quantitativas | 11 |
| erros de validação | 0 |

Há dados quantitativos locais prontos para comparação.


---

# Q25.11 — Domínios físicos reduzidos

Classificação: construção de benchmark GDQ reduzido.

| item | valor |
|---|---:|
| config | {'L': 4, 'beta_eff': 0.45, 'kappa_H': 0.35, 'mass_gap': 0.18, 'doping': 0.0, 'seed': 2510} |
| n_edges | 32 |
| rho_min | 6.250000000000e-02 |
| rho_sum | 1.000000000000e+00 |
| holonomy_exchange | -1.000000000000e+00 |
| hessian_min_eig | 1.800000000000e-01 |
| hessian_max_eig | 2.980000000000e+00 |
| eta_balance | 0.000000000000e+00 |

Interpretação: a rede física do aparelho foi fixada antes da comparação, a medida local é positiva e a Hessiana reduzida é positiva. O setor usa circulação escalonada para representar correlação antiferro sem pesos negativos.


---

# Q25.12 — Interface por Hessiana GDQ reduzida

Classificação: derivação numérica de operador/interface reduzido.

| item | valor |
|---|---:|
| n_interfaces | 32 |
| max_unitarity_error | 2.611090194369e-16 |
| mean_unitarity_error | 2.611090194369e-16 |
| holonomy_exchange | -1.000000000000e+00 |

A matriz de espalhamento local foi obtida pela transformada de Cayley da impedância Hermitiana extraída da Hessiana reduzida. Como a impedância é Hermitiana, a interface fechada é unitária por construção; o erro acima mede apenas erro de máquina.


---

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


---

# Q25.14 — Escala de variância/autocorrelação

Classificação: teste de escala numérico no benchmark reduzido.

| L | N | tau_corr | stderr_eff | acceptance |
|---:|---:|---:|---:|---:|
| 4 | 16 | 8.241905 | 3.313050687431e-03 | 0.751829 |
| 6 | 36 | 17.523244 | 3.053721546693e-03 | 0.756871 |
| 8 | 64 | 30.118337 | 2.933880755648e-03 | 0.760686 |

Ajuste observado: `tau_corr ~ N^0.934`.

Interpretação: no intervalo testado não aparece explosão exponencial. Isto ainda não é prova assintótica; é filtro numérico inicial para a classe reduzida.


---

# Q25.15 — Comparação experimental física

Classificação: comparação fenomenológica externa.

Fonte quantitativa local: `questoes/q25/dados/q25_referencias_experimentais.csv`.

| paper | obs | exp | erro | GDQ | z |
|---|---|---:|---:|---:|---:|
| parsons_2016_spin_corr | C_s_r1 | -1.90000000e-01 | 8.000e-03 | -1.69871734e-01 | 2.516 |
| parsons_2016_spin_corr | C_s_r1 | -1.54000000e-01 | 3.000e-03 | -1.69871734e-01 | -5.291 |
| parsons_2016_spin_corr | C_s_r1 | -5.20000000e-02 | 6.000e-03 | -1.69871734e-01 | -19.645 |
| parsons_2016_fig2d_digitized | C_s_r1 | -3.50000000e-01 | 2.000e-02 | -1.69871734e-01 | 9.006 |
| parsons_2016_fig2d_digitized | C_s_r1 | -2.10000000e-01 | 2.000e-02 | -1.69871734e-01 | 2.006 |
| parsons_2016_fig2d_digitized | C_s_r1 | -2.40000000e-01 | 2.000e-02 | -1.69871734e-01 | 3.506 |
| parsons_2016_fig2d_digitized | C_s_r1 | -1.10000000e-01 | 2.000e-02 | -1.69871734e-01 | -2.994 |
| parsons_2016_fig2d_digitized | C_s_r1 | -5.00000000e-02 | 2.000e-02 | -1.69871734e-01 | -5.994 |
| parsons_2016_spin_corr | xi_corr | 5.10000000e-01 | 4.000e-02 | 9.17937517e-01 | 10.198 |
| parsons_2016_spin_corr | xi_corr | 3.90000000e-01 | 2.000e-02 | 9.17937517e-01 | 26.397 |
| parsons_2016_spin_corr | xi_corr | 2.40000000e-01 | 9.000e-02 | 9.17937517e-01 | 7.533 |

χ² total: `1.42012262e+03`.

χ² reduzido bruto: `1.29102056e+02`.

Comparação principal fria `C_s_r1`: o sinal antiferromagnético e a ordem de grandeza batem; o desvio é `2.516σ`. Isso é compatibilidade fenomenológica parcial, não acordo metrológico.

Veredito: a comparação externa foi executada. O modelo reduzido não passa como descrição metrológica de todos os dados de Parsons; ele passa apenas como teste de sinal/ordem de grandeza para o correlator frio de primeiro vizinho. A discrepância em `xi_corr` indica que falta o mapa térmico/aparelho completo ou uma Hessiana GDQ menos reduzida.


---

# Q25.16 — Mapa térmico do ensemble GDQ reduzido

Classificação: calibração/inversão fenomenológica do mapa térmico.

O script varre por Monte Carlo reprodutível o ensemble positivo reduzido da GDQ e inverte a curva `C_s(1)(beta_eff)` para os pontos digitizados da Fig. 2D de Parsons.

| kBT/t exp | C_s(1) exp | beta_eff GDQ | T_eff GDQ | C_s(1) GDQ | residual |
|---:|---:|---:|---:|---:|---:|
| 0.000 | -3.50000000e-01 | 7.63442723e-01 | 1.30985596e+00 | -3.50000000e-01 | 0.00000000e+00 |
| 0.450 | -2.10000000e-01 | 5.19445430e-01 | 1.92513004e+00 | -2.10000000e-01 | 0.00000000e+00 |
| 0.550 | -2.40000000e-01 | 5.91747963e-01 | 1.68990865e+00 | -2.40000000e-01 | 2.77555756e-17 |
| 0.900 | -1.10000000e-01 | 2.93897795e-01 | 3.40254340e+00 | -1.10000000e-01 | 1.38777878e-17 |
| 1.500 | -5.00000000e-02 | 1.36273764e-01 | 7.33816966e+00 | -5.00000000e-02 | -6.93889390e-18 |

Ajuste fenomenológico do mapa térmico reduzido:

$$
\beta_{\rm eff} \simeq \frac{0.291786}{k_BT/t+0.050000}
$$

MSE em beta: `4.52656229e-03`.

Interpretação: a curva experimental pode ser representada por uma família de ensembles GDQ reduzidos com `beta_eff` variável. Isto resolve a comparação operacional da curva no modelo reduzido, mas a derivação do mapa térmico a partir da Hessiana completa do aparelho continua pendente.


---

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


---

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


---

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


---

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


---

# Q25.21 — Correção da largura térmica residual

Classificação: derivação reduzida e comparação.

A largura Schur anterior foi:

$$
\Theta_A^{\rm Schur}\simeq0.616921719.
$$

O ajuste efetivo pedia:

$$
\Theta_A^{\rm fit}\simeq0.721527850.
$$

Logo o resíduo alvo era:

$$
\Delta\Theta_A\simeq 1.046061310000e-01.
$$

Testei correções espectrais do banho usando os autovalores de `K_A` e os acoplamentos `J_k` do modo medido aos modos do aparelho:

| candidato | DeltaTheta | Theta total | erro vs fit |
|---|---:|---:|---:|
| `sum_J2_over_lam_plus_Ks_sq` | 3.123562407989e-02 | 6.481573430799e-01 | -7.337050692011e-02 |
| `sum_J2_over_lam_lam_plus_Ks` | 6.907130480224e-02 | 6.859930238022e-01 | -3.553482619776e-02 |
| `sqrt_gap_times_delta1` | 7.498274691141e-02 | 6.919044659114e-01 | -2.962338408859e-02 |
| `delta1_over_sqrt_KH` | 2.248389419717e-02 | 6.394056131972e-01 | -8.212223680283e-02 |

Veredito: o banho espectral discreto gera uma correção positiva da largura térmica, com ordem de grandeza correta mas ainda abaixo do resíduo necessário. Portanto a direção está correta, porém o modelo reduzido ainda omite canais dissipativos/causais ou pesos térmicos de aparelho que amplifiquem `DeltaTheta_A`.


## Veredito conservador

A cadeia física reduzida foi executada: rede/aparelho, domínios positivos, Hessiana reduzida positiva, interfaces unitárias por impedância, correlações de circulação/spin comparadas com enumeração exata finita e teste inicial de escala. A comparação externa com Parsons et al. foi executada com dados locais extraídos. O resultado é parcial: sinal e ordem de grandeza do correlator frio de primeiro vizinho são reproduzidos, mas o conjunto completo, especialmente o comprimento de correlação, não é descrito metrologicamente pelo modelo reduzido. A Q25 ainda exige mapa térmico/aparelho e Hessiana GDQ completa para fechamento experimental.
