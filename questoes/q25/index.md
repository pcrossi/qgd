# Q25 — Problema do sinal

Documento canônico: [questao_25.md](questao_25.md)

Status vigente: parcialmente resolvida/fechada estruturalmente como rota
geométrica, mas algoritmo geral permanece programa futuro.

Resumo: a GDQ resolve conceitualmente a origem geométrica do sinal; a prova
computacional forte exige algoritmo, variância, autocorrelação e benchmarks.

Plano operacional:
[plano_algoritmo_validacao_q25.md](associados/plano_algoritmo_validacao_q25.md)

Plano do benchmark físico:
[plano_benchmark_fisico_q25.md](associados/plano_benchmark_fisico_q25.md)

Validação mínima executada:
[saida_q25_validacao.md](resultados/saida_q25_validacao.md)

Scripts autocontidos:

1. [q25_01_domain_interface.py](associados/q25_01_domain_interface.py)
2. [q25_02_estimador_holonomia.py](associados/q25_02_estimador_holonomia.py)
3. [q25_03_autocorrelacao_variancia.py](associados/q25_03_autocorrelacao_variancia.py)
4. [q25_04_referencias_experimentais.py](associados/q25_04_referencias_experimentais.py)
5. [q25_05_compare_experiment.py](associados/q25_05_compare_experiment.py)
6. [q25_run_all.py](associados/q25_run_all.py)

Benchmark físico reduzido executado:
[saida_q25_benchmark_fisico.md](resultados/saida_q25_benchmark_fisico.md)

Scripts físicos:

1. [q25_10_extract_experimental_data.py](associados/q25_10_extract_experimental_data.py)
2. [q25_11_build_physical_domains.py](associados/q25_11_build_physical_domains.py)
3. [q25_12_derive_interface_from_hessian.py](associados/q25_12_derive_interface_from_hessian.py)
4. [q25_13_spin_correlations_gdq.py](associados/q25_13_spin_correlations_gdq.py)
5. [q25_14_variance_scaling_physical.py](associados/q25_14_variance_scaling_physical.py)
6. [q25_15_compare_experiment_physical.py](associados/q25_15_compare_experiment_physical.py)
7. [q25_16_thermal_ensemble_map.py](associados/q25_16_thermal_ensemble_map.py)
8. [q25_17_hessian_thermal_map_candidates.py](associados/q25_17_hessian_thermal_map_candidates.py)
9. [q25_18_thermal_apparatus_block.py](associados/q25_18_thermal_apparatus_block.py)
10. [q25_19_schur_apparatus_derivation.py](associados/q25_19_schur_apparatus_derivation.py)
11. [q25_20_compare_schur_curve.py](associados/q25_20_compare_schur_curve.py)
12. [q25_21_bath_width_correction.py](associados/q25_21_bath_width_correction.py)
13. [q25_run_physical_benchmark.py](associados/q25_run_physical_benchmark.py)

Memória estruturada: `brain/open-problems/q25-sign-problem-algorithm/`.
