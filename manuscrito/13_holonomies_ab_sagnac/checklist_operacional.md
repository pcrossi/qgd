---
title: "Checklist operacional — Capítulo 13"
---

# Checklist operacional — Capítulo 13

## 1. Enunciado

Explicar AB, Sagnac e extensões interferométricas como holonomias físicas de
conexões distintas, preservando a leitura GDQ sem inventar força local oculta.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Holonomia | Definição operacional | Integral de conexão em laço. |
| AB ideal | Fechado estruturalmente | Domínio perfurado e conexão plana. |
| Invariância de calibre | Demonstrada | Holonomia de laço fechado. |
| Colagem `U(1)` e Stokes celular | Demonstrados em Lean | Núcleo algébrico finito; Stokes suave mantém regularidade, orientação e domínio como hipóteses. |
| Potencial como conexão | Interpretação GDQ | Cisalhamento/colagem efetiva. |
| Solenoide real | Programa metrológico construído | Correções por Hessiana física, projetor e $\mathsf R_{\rm sol}$. |
| Sagnac ideal | Fechado estruturalmente | Holonomia de relógio. |
| COW | Extensão reduzida | Não núcleo do capítulo. |

## 3. Cadeia dedutiva

$$
\text{domínio com ciclo}
\to
\text{conexão}
\to
\text{colagem}
\to
\oint\mathcal A
\to
\text{fase ou tempo observável}.
$$

Para aparelho real, a cadeia GDQ usada no capítulo é:

$$
J_{\rm app}^{\rm clássico}
\to
\Phi_\ast
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\delta A_{\rm surf}
\to
\Delta\varphi.
$$

## 4. Scripts

| Script | Classificação |
|---|---|
| `ab_holonomia_simbolica.py` | Teste simbólico de consistência da holonomia ideal. |
| `ab_fase_ideal.py` | Avaliação direta de holonomia ideal. |
| `sagnac_luz_materia.py` | Avaliação direta de Sagnac ideal. |
| `cow_estimativa_reduzida.py` | Estimativa reduzida/interferométrica. |
| `verificar_schur_projetor.py` | Teste simbólico-numérico de projetor físico e complemento de Schur. |

## 5. Pontos que não podem ser esquecidos

- AB não é força local onde $B=0$.
- Sagnac não é AB eletromagnético.
- O fator quatro de Sagnac resulta de dois fatores dois, não de ajuste.
- Potencial real significa conexão/holonomia real.
- Solenoide/fibra/aparelho real é metrologia.
- Casimir não pertence ao núcleo deste capítulo.
