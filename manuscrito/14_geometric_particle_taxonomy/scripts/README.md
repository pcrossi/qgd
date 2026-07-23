---
title: "Scripts — Capítulo 14"
---

# Scripts — Capítulo 14

## Verificações finais

- `verificar_soliton_gaussiano.py`
  - Classificação: verificação simbólico-numérica de solução explícita neutra.
  - Verifica a equação do solíton gaussiano, $\mathcal W_{\rm gauss}=0$ e o
    gap reduzido do operador de Ornstein--Uhlenbeck.
  - Saída: `saida_verificar_soliton_gaussiano.md`.

- `monotonicidade_vs_hessiana.py`
  - Classificação: ilustração simbólico-numérica de critério de estabilidade.
  - Mostra que um funcional pode ser monotônico ao longo do fluxo mesmo quando
    o ponto crítico é sela; por isso a Hessiana física é indispensável.
  - Saída: `saida_monotonicidade_vs_hessiana.md`.

| Script | Objetivo | Classificação |
|---|---|---|
| `hipercargas_z6.py` | Buscar hipercargas inteiras $y=6Y$ compatíveis com $\mathbb Z_6$, anomalias e primitividade. | Verificação simbólico-numérica exata. |
| `indice_aps_hopf_bismut.py` | Verificar $c_1=m$, $\bar\eta$ fracionária, kernel torsional e índice APS primitivo. | Verificação topológica discreta. |
| `elevacao_indice_representacoes.py` | Contar componentes de Weyl por geração e por três unidades de índice. | Verificação simbólica discreta. |
| `global_produto_tres_estomatos.py` | Confirmar Betti/Euler do produto global, Berry plano e contagem local por três estômatos. | Teste de consistência topológica. |
| `hessiana_tres_centros.py` | Calcular Hessiana vinculada do junction $C_3$ e complemento de Schur. | Verificação direta de construção reduzida. |
| `hessiana_fisica_c3_gap.py` | Calcular projetor físico, Schur e gap reduzido do junction $C_3$. | Avaliação direta de operador reduzido. |
| `acoplamentos_normas.py` | Calcular $I_3$, $I_2$, $I_Y$, $g'^2/g^2$ e $\sin^2\theta_W$. | Avaliação direta de norma geométrica. |
| `selecao_junction_N.py` | Testar seleção $N=3$ e modos nulos para $N>3$ no modelo horizontal reduzido. | Teste de consistência da prova de seleção. |

Todos os scripts são autocontidos e escrevem uma saída Markdown na mesma pasta.
