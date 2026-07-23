---
title: "Scripts — Capítulo 12"
---

# Scripts — Capítulo 12

| Script | Objetivo | Classificação |
|---|---|---|
| `hartman_saturacao_reduzida.py` | Avaliar $D_{\rm prop}(L)$ e $\tau_{\rm GDQ}(L)$ no canal evanescente reduzido. | Avaliação direta de fórmula reduzida. |
| `dupla_fenda_reduzida.py` | Gerar padrão reduzido coerente/incoerente. | Redução efetiva. |
| `detector_schur_visibilidade.py` | Avaliar $\mathsf R_{\rm det}$ e visibilidade. | Redução efetiva/aparelho. |
| `escolha_retardada_kernel.py` | Integrar resposta temporal causal do aparelho. | Transporte reduzido. |
| `dupla_fenda_detector_dtn.py` | Avaliar a dupla fenda com detector DtN específico, refinamento de malha e tabela de coerência. | Avaliação direta de detector reduzido. |
| `comparar_gdq_padrao_dupla_fenda.py` | Comparar limite coerente, limite incoerente e curva GDQ reduzida por $\exp(-\Gamma_{\rm det})$. | Comparação fenomenológica/controlada. |
| `interferometro_eo_mzi_resposta.py` | Calcular $\mathsf R_{\rm app}(t)$, $\Gamma_{\rm det}$ e coerência residual em EO-MZI com dados congelados. | Avaliação direta de modelo reduzido com dados externos de aparelho. |
| `hessiana_material_eo_mzi.py` | Calcular MZI ideal e imperfeições equivalentes a $-30\,{\rm dB}$. | Modelo material reduzido de engenharia. |

Os scripts novos são autocontidos: não importam arquivos das questões nem
módulos auxiliares externos ao próprio script.
