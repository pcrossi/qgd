---
title: "Scripts — Capítulo 11"
---

# Scripts — Capítulo 11

| Script | Objetivo | Classificação |
|---|---|---|
| `calcular_pesos_sg.py` | Calcular pesos angulares de Stern--Gerlach. | Teste de consistência operacional. |
| `simular_deflexao_sg.py` | Calcular deflexão em canal fixo. | Redução efetiva/aparelho. |
| `testar_sequencias_sg.py` | Testar medições sequenciais incompatíveis. | Teste simbólico. |
| `simular_captura_sg.py` | Integrar o martingal condicionado e comparar com primeiro alcance. | Teste estatístico de Born operacional. |
| `validar_limiar_born_sg.py` | Verificar $P_\varepsilon(+)\to p_0$ quando $\varepsilon\to0$. | Teste de convergência. |
| `simular_feixe_sg_completo.py` | Combinar captura, canal e propagação até a tela. | Redução efetiva completa do feixe. |
| `simular_sequencias_sg.py` | Simular $z\to z$ e $z\to x\to z$. | Teste operacional de incompatibilidade. |
| `simular_nao_adiabatico_sg.py` | Integrar Landau--Zener e calcular deriva fora do regime QND. | Delimitação dinâmica. |
| `resolver_canais_robin_sg.py` | Resolver espectro Robin reduzido de dois canais. | Teste de método, não previsão física. |
| `construir_background_estacionario_sg.py` | Verificar o shrinker gaussiano da fatia normal $\mathbb C^2$. | Avaliação direta de background de bulk. |
| `verificar_contorno_variacional_sg.py` | Verificar $K-n(F)=0$ e $r_c=\sqrt{6\tau}$. | Teste variacional de bordo. |
| `resolver_robin_gaussiano_sg.py` | Testar espectro axial no background gaussiano com Robin diagnóstico. | Diagnóstico reduzido. |
| `testar_zh_gaussiano_sg.py` | Mostrar ínfimo axial zero no gaussiano exterior. | Resultado negativo preservado. |
| `resolver_dtn_hopf_cilindrico_sg.py` | Calcular o DtN axial do cilindro de Hopf. | Cálculo estrutural reduzido. |
| `comparar_acoes_estacionarias_sg.py` | Comparar $\mathcal W$ on-shell gaussiano/cilíndrico. | Comparação reduzida. |
| `verificar_estabilidade_raio_cilindrico_sg.py` | Confirmar $\mathcal W''(2\sqrt\tau)>0$. | Estabilidade homogênea. |
| `verificar_atlas_hopf_sg.py` | Verificar colagem, projetor e métrica de Fubini--Study. | Teste geométrico/simbólico-numérico. |
| `verificar_triplet_hopf_bismut.py` | Verificar que o triplet Hopf da fatia normal $\mathbb C^2$ é auto-dual e ortonormal após normalização. | Teste geométrico/simbólico-numérico. |
| `verificar_noether_zeeman_sg.py` | Verificar a identidade do multiplicador Noether--Zeeman e a seleção paralela/antiparalela. | Teste simbólico-numérico de consistência. |
| `avaliar_background_gdq_sg.py` | Avaliar $\kappa_H^{\rm SG}$ e $\Gamma_{\rm SG}$ a partir de espectro físico. | Avaliador de previsão, sem defaults fenomenológicos. |
| `testar_pipeline_background_sg.py` | Validar o avaliador com fixture sintético. | Teste de código, não físico. |
| `testar_zeeman_fisico_sg.py` | Converter dados de aparelho em $\Delta$ e $v$. | Teste dimensional com dados externos. |

Os arquivos `saida_*.md` preservam as execuções auditadas. Scripts marcados
como “teste de método” ou “fixture” não devem ser citados como previsão
metrológica da GDQ.
