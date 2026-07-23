---
title: "Checklist operacional — Capítulo 9"
---

# Checklist operacional — Capítulo 9

## 1. Enunciado

Explicar a regra de Born e a teoria de medida na GDQ sem reduzir a teoria a
mecânica quântica padrão e sem inserir colapso externo na ação oficial.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Densidade positiva | Demonstrada/constitutiva | $\rho=e^{-(f+\bar f)/2}$. |
| Representação $\rho=|\Psi|^2$ | Setor regular | Necessária, mas não suficiente. |
| Born operacional | Fechada estruturalmente | Usa Hilbert reconstruído e projetores. |
| Aparelho como contorno | Estrutural | Fonte/contorno clássico, não nova ação. |
| Decoerência | Redução efetiva | Explica diagonalização de registros. |
| Resultado único | Condicional | Depende de bacias reais da microgeometria $A+E$. |
| Stern--Gerlach | Protótipo estrutural | Aparelho seleciona eixo. |
| Escolha retardada | Fechada estruturalmente | Problema de contorno, sem retrocausalidade física. |
| Emaranhamento | Estrutural/condicional | Não fatoração geométrica; no-signalling metrológico futuro. |

## 3. Cadeia dedutiva

$$
\mathcal S_{\rm GDQ}
\to
\rho,S_R
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\mathcal H_{\rm phys}
\to
\mu(P)=\operatorname{Tr}(\varrho P)
\to
\text{registro}.
$$

Construção técnica chamada:

- [[notes/construcao_gdq_medida|Construção GDQ da medida]]

## 4. Scripts opcionais

| Script | Classificação |
|---|---|
| `verificar_born_projetores.py` | Teste de consistência operacional: positividade, aditividade, bases unitárias, composição e marginais. |
| `verificar_emaranhamento_no_signalling.py` | Teste de consistência operacional reduzido: não fatoração, marginais e CHSH ideal. |
| `simular_decoerencia_sae.py` | Redução efetiva $S+A+E$, gap assintótico e repetibilidade ideal. |
| `resposta_detector_schur.py` | Toy model de resposta por complemento de Schur. |

## 5. Pontos que não podem ser esquecidos

- Não declarar $\rho=R^2$ como prova completa de Born.
- Não tratar o aparelho como operador quântico inserido manualmente.
- Não chamar decoerência de resultado único sem bacia real.
- Não usar escolha retardada como retrocausalidade.
- Não afirmar no-signalling metrológico para aparelhos reais sem cálculo.

## Revisão didática de 2026-07-19

O Capítulo 9 foi conferido na fase de revisão científica/didática. A cadeia
central permanece:

$$
J_{\rm app}^{\rm classico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm app}
\to
\text{resposta espectral}
\to
\text{registro}.
$$

O capítulo está autocontido e não depende de rótulos históricos. Os scripts
foram revisados para apontar apenas para fontes internas precisas do próprio
capítulo: Born por projetores, decoerência $S+A+E$ e resposta reduzida de
detector por complemento de Schur. Todos permanecem classificados como
verificações reduzidas/pedagógicas, não previsões metrológicas.
