---
title: "Scripts — Capítulo 13"
---

# Scripts — Capítulo 13

| Script | Objetivo | Classificação |
|---|---|---|
| `ab_holonomia_simbolica.py` | Verificar simbolicamente $dA_{\rm harm}=0$, $\oint A=\Phi$ e a holonomia. | Teste simbólico de consistência da holonomia ideal. |
| `ab_fase_ideal.py` | Calcular fase AB ideal em função do fluxo. | Avaliação direta de holonomia ideal. |
| `sagnac_luz_materia.py` | Calcular Sagnac para luz e matéria. | Avaliação direta ideal. |
| `cow_estimativa_reduzida.py` | Estimar fase COW reduzida. | Estimativa fenomenológica reduzida. |
| `verificar_schur_projetor.py` | Verificar a construção $P_{\rm phys}^{\dagger}KP_{\rm phys}$ e $\mathsf R=K_{YY}-K_{YI}K_{II}^{-1}K_{IY}$ em matriz autocontida. | Teste de consistência simbólico-numérico. |

## Observação sobre autocontenção

Os scripts deste diretório não dependem dos arquivos de questões. Cada script
declara a equação avaliada, os parâmetros físicos usados, a classificação do
cálculo e o arquivo de saída correspondente.
