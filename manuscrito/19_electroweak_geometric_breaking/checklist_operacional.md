---
title: "Checklist operacional — Capítulo 19"
---

# Checklist operacional — Capítulo 19

## 1. Enunciado

Consolidar a quebra eletrofraca geométrica da GDQ sem transformar a teoria em
Modelo Padrão fundamental.

## 2. Cadeia construtiva

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm phys}
=
P_{\rm phys}\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast]P_{\rm phys}
\to
\Phi_{\rm EW}
\to
a_2,a_4
\to
U(1)_{\rm EM}
\to
m_W,m_Z,m_\gamma.
$$

## 3. Vínculos preservados

| Vínculo | Uso |
|---|---|
| volume de interface | cancela termo quadrático de área |
| fluxo torsional | fornece rigidez superficial |
| gerador $Q=T_3+Y$ | preserva fóton sem massa |
| projetor $P_{\rm phys}$ | remove gauge/modos nulos |
| normalização cinética | converte $\beta_\ast$ em campo canônico reduzido |
| transporte espectral | separa o ponto comum $3/8$ do valor operacional $2/9$ |

## 4. Scripts finais/reduzidos

| Script | Classificação |
|---|---|
| `modo_hopf_eletrofraco.py` | Verificação simbólica do modo de Hopf e do gerador preservado. |
| `potencial_quartico_eletrofraco.py` | Avaliação direta de $a_2$, $a_4$ e $\beta_\ast$. |
| `matriz_massas_neutra.py` | Teste de autovalores $W/Z/\gamma$. |
| `simular_wz_eletrofraco.py` | Diagnóstico reduzido de massas para cenários de transporte. |
| `normalizacao_cinetica_hopf.py` | Avaliação direta da norma interna do modo de Hopf. |
| `transporte_weinberg_condicional.py` | Cálculo condicional de $Z_W/Z_Y=10/21$, $Q_\ast$ e comparação W/Z. |
| `schur_em_interface.py` | Verificação do complemento de Schur eletromagnético. |
| `no_go_berger_colar.py` | No-go produto/Berger/colar e divergência fotônica no colar infinito. |
| `auditar_vk.py` | Confirmação de que $v_K$ não é escala eletrofraca. |
| `verificar_potencias_unidades.py` | Checagem editorial-dimensional de $M^2$ e unidades quadráticas. |
| `yukawa_overlap_demo.py` | Demonstração autocontida da estrutura de overlap. |

## 5. Certificação formal

| Módulo | Alcance |
|---|---|
| `formal/GDQ/ElectroweakStability.lean` | Cancela o termo quadrático da área a volume fixo, prova o coeficiente $5/128$, os mínimos globais da quártica sob $a_2<0<a_4$, o Schur positivo e o kernel neutro. |

## 6. Pontos não migrados como fundamento

- Respiração conformal homogênea como Higgs.
- Estabilização de Berger por ansatz homogêneo, exceto como no-go preservado.
- Ajustes diretos de $\sin^2\theta_W$ pelo alvo; a rota preservada é o transporte espectral condicional.
- Scripts exploratórios com no-go ou engenharia inversa.

Esses itens ficam como histórico metodológico; o manuscrito preserva somente a
cadeia final reduzida e as conclusões que depuraram o caminho.
