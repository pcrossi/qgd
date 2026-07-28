---
title: "Checklist operacional — Capítulo 8"
---

# Checklist operacional — Capítulo 8

Este checklist registra o estado do Capítulo 8.

## 1. Enunciado

Mostrar que o espaço de Hilbert físico, a quantização de circulação e as
desigualdades de incerteza aparecem como reconstruções operacionais setoriais
da GDQ, não como axiomas primários.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Espaço de Hilbert físico | Fechado estruturalmente | Condicionado à reflexão positiva setorial. |
| Produto interno | Estrutural | $\langle [F],[G]\rangle=\langle\Theta F\,G\rangle_E$. |
| Estados, observáveis e composição | Fechado estruturalmente | Vetores, raios, matrizes densidade, projetores espectrais e produto tensorial após o quociente físico. |
| Unitariedade em $t$ | Teorema condicional | Se $H=H^\dagger$, então $U(t)=e^{-itH/\hbar}$ é unitário; decaimento em setor projetado é teoria aberta efetiva. |
| Wallstrom | Fechado estruturalmente | Integralidade vem de fase $S^1$ e fibrado $U(1)$. |
| Quantização relativa | Fechada condicionalmente | Ação exponenciada e carga conservada fornecem $Q_S\Delta S_R\in h\mathbb Z$; a simetria local contínua não basta. |
| Heisenberg | Fechado no setor regular | Cauchy-Schwarz aplicado ao fluido de Madelung. |
| Robertson--Schrödinger | Fechado no Hilbert reconstruído | Positividade Hermitiana. |
| BBM/GUP/Fubini--Study global | Programa futuro | Não usar como prova fechada. |

## 3. Cadeia dedutiva

$$
\mathcal S_{\rm GDQ}
\to
\text{setor efetivo positivo}
\to
\mathcal H_{\rm phys}
\to
\text{operadores autoadjuntos}
\to
\text{unitariedade}
\to
\text{fase circular}
\to
\text{Wallstrom}
\to
\text{incerteza}.
$$

## 4. Pontos de preservação

- Hilbert é operacional, não ontologia primária.
- Não usar $t=-i\tau$ como prova do tempo físico.
- Poisson não deriva a quantização; ela pressupõe setores inteiros.
- O deslocamento constante de toda a história tem $\Delta I=0$ para qualquer
  incremento real; a integralidade relativa exige identificação global dos
  extremos.
- Estados não inteiros não são seções globais admissíveis.
- Kähler estrito só no setor sem torção; a geometria geral é Hermitiana/KT.
- Fubini--Study pertence ao Hilbert reconstruído.
- GUP e BBM ficam como extensões condicionais.

## 5. Scripts opcionais

Os scripts em `scripts/` são ilustrações de consistência, não provas novas.

| Script | Classificação |
|---|---|
| `testar_incerteza_gaussianas.py` | Avaliação direta de Heisenberg em gaussianas. |
| `verificar_wallstrom_circulacao.py` | Teste simbólico/topológico de circulação inteira e fluxo de Chern inteiro. |
| `verificar_positividade_hilbert.py` | Toy model de positividade e quociente por norma nula. |
| `verificar_hilbert_operacional.py` | Toy model de estados, observáveis, evolução unitária e tensorização no quociente físico. |
| `verificar_unitariedade_tempo_fisico.py` | Toy model de unitariedade em $t$, contração euclidiana e decaimento projetado. |

## 6. Provas técnicas chamadas

- [[notes/construcao_gdq_hilbert_quantizacao|Construção GDQ do Hilbert físico e da quantização]]
- [[notes/estados_observaveis_composicao_hilbert|Estados, observáveis e composição no Hilbert reconstruído]]
- [[notes/unitariedade_tempo_fisico_e_setores_abertos|Unitariedade em tempo físico e setores abertos]]
- [[notes/wallstrom_fibrado_linha_u1|Prova da quantização de circulação por fibrado U(1)]]
- [[notes/quantizacao_relativa_acao_exponenciada|Quantização relativa, ação exponenciada e termo de extremidade]]

## Revisão didática de 2026-07-19

O Capítulo 8 foi conferido na fase de revisão científica/didática. A seção
`08.9` foi reescrita para apresentar BBM, GUP, Fubini--Study global e
correções torsionais como extensões futuras do próprio manuscrito, sem exigir
conhecimento de versões históricas. A nota de Wallstrom foi ajustada para
evitar a impressão de que a GDQ acrescenta uma condição externa de
univocidade: a integralidade vem da admissibilidade geométrica global de uma
seção de fibrado $U(1)$.

Os scripts do capítulo permanecem como ilustrações de consistência:
positividade/quociente de Hilbert, circulação inteira e incerteza em
gaussianas. Nenhum deles substitui a reconstrução setorial nem usa alvo
experimental.
