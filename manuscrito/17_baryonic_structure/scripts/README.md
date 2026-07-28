---
title: "Scripts — Capítulo 17"
---

# Scripts — Capítulo 17

| Script | Objetivo | Classificação |
|---|---|---|
| `derivar_delta_barioes.py` | Derivar o invariante reduzido $\delta_B=\ln(2\pi^2)3\sqrt2/5$. | Avaliação direta de derivação reduzida condicional. |
| `derivacao_simbolica_massas_barioes.py` | Derivar simbolicamente $M_p/M_e$, $\delta_B$ e $M_n/M_e$. | Derivação simbólica das hipóteses condicionais. |
| `calcular_massas_barioes.py` | Avaliar massas reduzidas de próton/nêutron. | Avaliação direta condicional. |
| `convergencia_raio_superficie.py` | Verificar que a casca regularizada converge para o raio de superfície $r_p$. | Teste de consistência. |
| `calcular_raios_momentos_barioes.py` | Avaliar raio do próton e momentos magnéticos reduzidos. | Avaliação direta condicional. |
| `calcular_fatores_forma_reduzidos.py` | Testar normalizações de Sachs e raio quadrático do nêutron. | Teste de consistência. |
| `perfil_torcional_neutron.py` | Resolver numericamente o perfil $H_n(\chi)$ líder e $G_E^n(q^2)$. | Avaliação direta de perfil variacional reduzido. |
| `modos_coletivos_superficie.py` | Ajustar a impedância coletiva de superfície por Schur em três modos contra Galster. | Ajuste/benchmark de forma. |
| `espectro_estabilidade_barioes.py` | Avaliar espectro rotacional líder e estabilidade estrutural. | Avaliação direta reduzida. |
| `validar_beta_livre.py` | Verificar endpoint beta e caráter contínuo. | Teste de consistência. |
| `verificar_limite_regra_ouro.py` | Verificar o kernel de tempo finito e sua convergência distribucional para a casca de energia. | Teste de consistência e convergência. |
| `resolver_modos_dirac_bismut_beta.py` | Avaliar os kernels tangenciais eletrônico e neutro torsional. | Avaliação direta do operador declarado. |
| `verificar_overlap_quatro_modos_beta.py` | Verificar a base angular $S,T$, Gram $2,6$ e Fierz. | Verificação simbólico-numérica estrutural. |
| `verificar_liberdade_noether_beta.py` | Demonstrar que Ward--Noether preserva uma liberdade de escala transversal. | Teste algébrico de não identificabilidade. |
| `verificar_jatos_causais_beta.py` | Verificar a composição cúbica dos jatos causais do overlap. | Verificação simbólica estrutural. |
| `verificar_projecao_fluxo_quartica_beta.py` | Verificar o projetor de fluxo e o complemento de Schur quártico. | Verificação simbólica estrutural. |
| `validar_beta_livre_completo.py` | Calcular endpoint, espaço de fase analítico/Simpson e avaliar o ansatz histórico de vida média. | Teste de convergência e comparação fenomenológica condicional. |
| `escala_eletronica_beta.py` | Determinar $M_ec^2$ a partir de $Q_\beta$ e $\delta_B$. | Determinação metrológica reduzida. |
| `comparar_tau_neutron.py` | Avaliar o ansatz $\tau_n\propto\alpha^{-11}$ e comparar com referência. | Comparação fenomenológica; não é derivação da Hessiana. |
| `verificar_corrente_green_hessiana.py` | Verificar a identidade de Green da corrente bilinear da Hessiana. | Verificação simbólica estrutural. |

Todos os scripts são autocontidos e escrevem saída Markdown na mesma pasta.

Nenhum script deve ser interpretado como mais forte que a classificação acima.
Em particular, `modos_coletivos_superficie.py` usa o benchmark como alvo do
ajuste, e os scripts de vida média assumem a lei histórica
$\alpha^{-11}$.
