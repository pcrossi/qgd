---
title: "Checklist operacional — Capítulo 17"
---

# Checklist operacional — Capítulo 17

## 1. Enunciado

Consolidar próton, nêutron e estrutura bariônica como soluções trimodais da
GDQ, preservando massa de bulk, torção de superfície, carga inteira, spin,
paridade, raio, momentos, fatores de forma e beta livre.

## 2. Cadeia construtiva

$$
\mathcal S_{\rm GDQ}
\to
\Phi_B
\to
K_B^{\rm phys}
\to
P_{\rm topo}
\to
\mathcal I_B
\to
Q_B,J^P,r_B,\mu_B,G_{E,M},\Gamma_n.
$$

## 3. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| sóliton trimodal | construção reduzida condicional | três estômatos colados; sela suave 8D futura |
| volume $6\pi^5$ | identidade exata sob o background | seleção e normalização são hipóteses |
| torção de superfície | redução condicional | Stokes é exato; coeficientes de interface ainda requerem Hessiana |
| carga | teorema condicional | resíduo inteiro sob meromorfia/contorno |
| spin/paridade | fechados no setor reduzido | holonomia/involução declaradas |
| raio/momentos | redução condicional de superfície | Hessiana completa para metrologia fina |
| fatores de forma | estrutural/reduzido | dados completos de espalhamento são refinamento |
| $H_n(\chi)$ | solução exata do problema reduzido declarado | fonte dipolar e largura são hipóteses de superfície |
| impedância coletiva | ajuste/benchmark de superfície | Schur de três modos ajustado à forma de Galster |
| espectro/estabilidade | proteção topológica + teste líder | positividade dinâmica completa requer Hessiana 8D |
| beta contínuo | fechado | endpoint não é energia fixa do antineutrino |
| Regra de Ouro | teorema condicional de redução | derivada do limite de tempo longo do gerador físico GDQ |
| Ward/overlap beta | fechado estruturalmente | Noether fixa seleção; quarta variação ainda deve calcular a magnitude |
| vida média | ansatz fenomenológico avaliado | $\alpha^{-11}$ e $32/15$ não derivados da Hessiana |

## 4. Scripts finais/reduzidos

| Script | Classificação |
|---|---|
| `calcular_massas_barioes.py` | Avaliação direta de massa reduzida. |
| `convergencia_raio_superficie.py` | Teste de consistência do raio como observável de superfície. |
| `calcular_raios_momentos_barioes.py` | Avaliação direta de raio e momentos reduzidos. |
| `calcular_fatores_forma_reduzidos.py` | Teste de normalização dos fatores de forma. |
| `perfil_torcional_neutron.py` | Avaliação direta do perfil $H_n(\chi)$ e de $G_E^n$ líder. |
| `modos_coletivos_superficie.py` | Ajuste/benchmark da impedância coletiva por Schur contra Galster. |
| `espectro_estabilidade_barioes.py` | Avaliação do espectro líder e estabilidade estrutural. |
| `validar_beta_livre.py` | Teste do endpoint beta e espectro contínuo. |
| `verificar_limite_regra_ouro.py` | Teste do kernel temporal, normalização e convergência distribucional. |
| `resolver_modos_dirac_bismut_beta.py` | Avaliação dos modos tangenciais de saída. |
| `verificar_overlap_quatro_modos_beta.py` | Verificação da base angular $S,T$ e do Gram $2,6$. |
| `verificar_liberdade_noether_beta.py` | Teste de que Noether não fixa a normalização transversal. |
| `verificar_jatos_causais_beta.py` | Teste simbólico dos jatos causais de ordem três. |
| `verificar_projecao_fluxo_quartica_beta.py` | Teste do projetor de fluxo e Schur quártico. |
| `comparar_tau_neutron.py` | Avaliação do ansatz histórico de vida média e comparação. |

## 5. Pontos preservados

- Modos internos dos três estômatos não são quarks pontuais fundamentais.
- $T^5\times S^3$ é ciclo efetivo/espectral, não bulk local oficial.
- A carga fundamental do bárion é inteira no contorno global.
- A massa do nêutron não é energia fixa do antineutrino.
- A vida média fica em fechamento total reduzido, não diferencial completo.

## 6. Nota técnica consolidada

A dedução autocontida das massas, do equilíbrio torsional, de $\delta_B$, do
perfil $H_n$, da corrente simplética, do beta contínuo e da vida média está reunida em
[[notes/baryons/provas_lemas_definicoes|Provas, lemas e definições do setor bariônico]].

A separação entre teoremas, reduções, ajustes e hipóteses está em
[[notes/baryons/status_hessiana_e_poder_preditivo|Status derivacional, Hessiana e poder preditivo]].
