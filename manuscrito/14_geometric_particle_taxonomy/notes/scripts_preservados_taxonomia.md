---
title: "Scripts preservados da taxonomia geométrica"
---

# Scripts preservados da taxonomia geométrica

## 1. Critério

A construção da taxonomia geométrica possui muitos testes históricos. Para o
capítulo, foram preservados apenas os scripts finais ou reduzidos necessários
para confirmar a construção central, sem carregar tentativas intermediárias.

Scripts incorporados:

| Script no capítulo | Origem conceitual preservada | Função |
|---|---|---|
| `hipercargas_z6.py` | busca diofantina de hipercargas inteiras | Verifica hipercargas, primitividade e cancelamento de anomalias. |
| `indice_aps_hopf_bismut.py` | índice APS local no elo Hopf--Bismut | Verifica fluxo primitivo, eta reduzida, kernel torsional e índice local unitário. |
| `elevacao_indice_representacoes.py` | elevação do índice às representações internas | Verifica $15$ componentes de Weyl por geração e $45$ para três estômatos. |
| `global_produto_tres_estomatos.py` | auditoria do produto global e seleção local | Confirma que o produto plano não gera três e que três estômatos geram $N_G=3$. |
| `hessiana_tres_centros.py` | Hessiana vinculada do background de três centros | Verifica estabilidade reduzida do setor $C_3$. |
| `hessiana_fisica_c3_gap.py` | Hessiana física projetada do junction $C_3$ | Verifica projetor físico, Schur e gap reduzido positivo. |
| `acoplamentos_normas.py` | normas geométricas dos subfibrados efetivos | Calcula razões de acoplamento e $\sin^2\theta_W$ reduzido. |
| `selecao_junction_N.py` | seleção por equilíbrio torcional de estômatos | Testa a seleção $N=3$ e modos nulos para $N>3$. |

## 2. Material não incorporado

Testes de orbifold, K3, retroação anisotrópica, módulos e rotas alternativas
não entram no corpo principal porque são exploratórios ou pertencem a capítulos
posteriores. O teste de Berry plano foi preservado apenas na forma reduzida
necessária para mostrar que o produto global trivial não gera três gerações.

## 3. Status

Nenhum script final necessário ao fechamento estrutural do Capítulo 14 foi
deixado para trás. Scripts exploratórios permanecem fora do corpo do manuscrito
para não misturar evolução histórica com a construção positiva.
