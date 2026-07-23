---
title: "Scripts — Capítulo 16"
---

# Scripts — Capítulo 16

| Script | Objetivo | Classificação |
|---|---|---|
| `calcular_alpha_media_einstein.py` | Avaliar $\alpha_E^{\rm mean}$ sem CODATA. | Avaliação direta de quantidade derivada. |
| `calcular_projetor_iso_hessiana.py` | Avaliar $\mathcal P_{\rm iso}=9/(8\pi^4)$ como contração angular/torsional da Hessiana média. | Avaliação direta de quantidade derivada. |
| `teste_schur_dtn_alpha.py` | Registrar o diagnóstico DtN/Schur redondo e sua diferença diante da média de Einstein. | Teste de consistência / diagnóstico geométrico. |
| `zeeman_resposta_linear.py` | Verificar canais Zeeman de uma fonte magnética fraca. | Teste simbólico-numérico reduzido. |
| `gmenos2_termo_lider.py` | Calcular $a^{(1)}=\alpha/(2\pi)$ e comparar com referências registradas. | Avaliação direta do termo líder. |
| `avaliar_hessiana_anomalia.py` | Verificar a contração Hessiana que produz $\alpha/(2\pi)$. | Teste de consistência do operador reduzido. |
| `teste_hierarquia_nao_substitui_gmenos2.py` | Confirmar que a hierarquia leptônica fornece background, mas não fecha $g-2$. | Diagnóstico de não substituição. |
| `calcular_residuos_superiores_gmenos2.py` | Calcular resíduos depois de subtrair $\alpha/(2\pi)$. | Comparação metrológica externa. |
| `construir_blocos_hessiana_gmenos2.py` | Construir bloco líder e blocos `required`. | Líder derivado; `required` diagnóstico inverso. |
| `avaliar_hessiana_gdq_gmenos2.py` | Avaliar $a_\ell$ a partir de um NPZ com $H,c,m_\perp$. | Avaliador de operador. |
| `extrair_canal_superior_gmenos2.py` | Extrair $K_i,J_i,\mu_i$ do complemento transversal. | Ferramenta de diagnóstico/derivação. |
| `auditar_nao_unicidade_canal_superior_gmenos2.py` | Mostrar que blocos `required` não são únicos. | Resultado negativo. |
| `hessiana_oficial_galerkin_gmenos2.py` | Calcular Hessiana Galerkin reduzida da ação oficial. | Teste de consistência; não previsão. |
| `construir_background_fonte_leptonico_gmenos2.py` | Construir backgrounds efetivos mínimos e mapa magnético linear. | Redução efetiva positiva. |
| `derivar_canal_superior_fisico_gmenos2.py` | Testar regra de Hodge para fonte superior direta. | Resultado negativo: $\mu_2=0$. |
| `derivar_h1_mistura_gmenos2.py` | Avaliar mistura harmônica $H_1$. | Mecanismo permitido, não metrologia final. |
| `calcular_variacoes_superiores_gdq_gmenos2.py` | Avaliar tensores cúbicos/quárticos reduzidos. | Diagnóstico variacional. |
| `contrair_canal_densidade_gmenos2.py` | Contrair $\Delta H_{12}=\eta_\ell T_{123}$. | Avaliação condicional. |
| `calcular_eta_pela_sela_gmenos2.py` | Resolver sela angular normalizada para $\eta_\ell$. | Resultado negativo reduzido. |

Todos os scripts são autocontidos, comentados e escrevem saída Markdown na
mesma pasta.
