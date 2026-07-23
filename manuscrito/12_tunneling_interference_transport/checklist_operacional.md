---
title: "Checklist operacional — Capítulo 12"
---

# Checklist operacional — Capítulo 12

## 1. Enunciado

Explicar tunelamento, dupla fenda, detector e escolha retardada como problemas
de densidade, fase, contorno e transporte no setor reduzido da GDQ.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Hartman | Teorema reduzido condicional | $g_{xx}\propto\rho$ vale no canal evanescente declarado, não universalmente. |
| Dupla fenda sem detector | Fechada no setor Madelung plano | Recupera interferência. |
| Nós de Bohm | Redução efetiva | Pressão geométrica em zeros. |
| Detector DtN/Schur | Fechado estruturalmente | Canal linear reduzido. |
| Visibilidade | Fechada condicionalmente | $\mathcal C=e^{-\Gamma_{\rm det}}$. |
| Escolha retardada | Fechada estruturalmente | Contorno/transporte causal. |
| Aparelho real | Programa metrológico | Exige dados de material e Hessiana completa. |

## 3. Cadeia dedutiva

$$
J_{\rm app}^{\rm clássico}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\rho,S_R
\to
\Omega,\partial\Omega
\to
\text{fendas/barreira}
\to
\text{duas contribuições}
\to
\mathsf R_{\rm det}
\to
\Gamma_{\rm det}
\to
\rho_{\rm obs}.
$$

Construção técnica chamada:

- [[notes/construcao_gdq_transporte_interferencia|Construção GDQ do transporte e da interferência]]

## 4. Scripts

| Script | Classificação |
|---|---|
| `hartman_saturacao_reduzida.py` | Avaliação direta de fórmula reduzida. |
| `dupla_fenda_reduzida.py` | Redução efetiva Madelung/paraxial. |
| `detector_schur_visibilidade.py` | Redução efetiva/aparelho. |
| `escolha_retardada_kernel.py` | Transporte causal reduzido. |
| `dupla_fenda_detector_dtn.py` | Detector DtN específico, malha e coerência. |
| `comparar_gdq_padrao_dupla_fenda.py` | Comparação GDQ reduzida vs limites padrão. |
| `interferometro_eo_mzi_resposta.py` | Resposta temporal EO-MZI, $\mathsf R_{\rm app}(t)$, $\Gamma_{\rm det}$ e comparação com crosstalk. |
| `hessiana_material_eo_mzi.py` | Hessiana material reduzida e imperfeições equivalentes a $-30\,{\rm dB}$. |

## 5. Pontos que não podem ser esquecidos

- Não chamar $g_{xx}\propto\rho$ de teorema geral fora do setor evanescente reduzido.
- Não tratar detector como colapso externo.
- Não usar propagador avançado como sinal físico para o passado.
- Não reivindicar evolução métrica completa para dupla fenda.
- Não confundir visibilidade bruta com coeficiente de coerência.
