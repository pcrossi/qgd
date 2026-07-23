---
title: "Scripts — Capítulo 15"
---

# Scripts — Capítulo 15

| Script | Objetivo | Classificação |
|---|---|---|
| `tensao_intrinseca_mu_tau.py` | Calcular $R_\mu$ pela rota intrínseca e $R_\tau$ pela saturação tridimensional. | Avaliação direta da construção reduzida. |
| `derivacao_simbolica_hierarquia_leptonica.py` | Derivar simbolicamente $R_\mu$ e os ramos geométricos da terceira razão. | Derivação simbólica autocontida. |
| `koide_saturacao.py` | Verificar a condição geométrica $Q=2/3$ e os dois ramos. | Teste simbólico-numérico reduzido. |
| `perelman_reducao_3d_bulk8.py` | Verificar a redução condicional de singularidades ao fator curvo $B_3$. | Verificação simbólico-numérica de identidade geométrica. |
| `background_8d_estacionario.py` | Avaliar $a_W,a_f,a_H,\varepsilon,\lambda_B^{\rm gap}$ no background produto. | Avaliação direta de quantidade derivada. |
| `hessiana_8d_schur.py` | Verificar Schur produto e critério warped/misto. | Teste de consistência da Hessiana 8D reduzida. |
| `criterio_warped_misto.py` | Calcular o limiar subcrítico de Schur para misturas warped/mistas. | Teste de consistência. |
| `hierarquia_8d_schur_resposta.py` | Avaliar resposta das razões leptônicas sob complemento de Schur. | Avaliação simbólico-numérica da fórmula efetiva. |
| `rosen_morse_benchmark.py` | Reproduzir benchmark Rosen--Morse com status auxiliar. | Benchmark numérico, não ontologia. |
| `verificar_calibracao_metrologica.py` | Verificar que autovalores normalizados viram energias somente após calibração e que razões não dependem da régua. | Verificação simbólico-numérica de relações dimensionais. |

Todos os scripts são autocontidos e escrevem saída Markdown na mesma pasta.
