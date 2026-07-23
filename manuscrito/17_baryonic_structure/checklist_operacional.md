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
| sóliton trimodal | fechado estruturalmente | três estômatos colados |
| volume $6\pi^5$ | fechado reduzido | razão de massa |
| torção de superfície | fechado reduzido | Stokes/transgressão |
| carga | fechada | resíduo inteiro |
| spin/paridade | fechados | holonomia/involução |
| raio/momentos | fechados em redução de superfície | Hessiana completa para metrologia fina |
| fatores de forma | estrutural/reduzido | dados completos de espalhamento são refinamento |
| $H_n(\chi)$ | fechado em perfil variacional líder | carga nula e inclinação de baixa energia |
| impedância coletiva | fechada em modelo reduzido de superfície | Schur de três modos; Hessiana completa é metrologia fina |
| espectro/estabilidade | fechado estruturalmente | $\Delta(1232)$ apenas teste líder |
| beta contínuo | fechado | endpoint não é energia fixa do antineutrino |
| Ward/overlap beta | fechado estruturalmente | Noether fixa seleção; quarta variação fixa magnitude |
| vida média | fechada condicionalmente | nível $10^{-3}$ |

## 4. Scripts finais/reduzidos

| Script | Classificação |
|---|---|
| `calcular_massas_barioes.py` | Avaliação direta de massa reduzida. |
| `convergencia_raio_superficie.py` | Teste de consistência do raio como observável de superfície. |
| `calcular_raios_momentos_barioes.py` | Avaliação direta de raio e momentos reduzidos. |
| `calcular_fatores_forma_reduzidos.py` | Teste de normalização dos fatores de forma. |
| `perfil_torcional_neutron.py` | Avaliação direta do perfil $H_n(\chi)$ e de $G_E^n$ líder. |
| `modos_coletivos_superficie.py` | Teste reduzido da impedância coletiva por Schur. |
| `espectro_estabilidade_barioes.py` | Avaliação do espectro líder e estabilidade estrutural. |
| `validar_beta_livre.py` | Teste do endpoint beta e espectro contínuo. |
| `resolver_modos_dirac_bismut_beta.py` | Avaliação dos modos tangenciais de saída. |
| `verificar_overlap_quatro_modos_beta.py` | Verificação da base angular $S,T$ e do Gram $2,6$. |
| `verificar_liberdade_noether_beta.py` | Teste de que Noether não fixa a normalização transversal. |
| `verificar_jatos_causais_beta.py` | Teste simbólico dos jatos causais de ordem três. |
| `verificar_projecao_fluxo_quartica_beta.py` | Teste do projetor de fluxo e Schur quártico. |
| `comparar_tau_neutron.py` | Avaliação da vida média reduzida e comparação. |

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
