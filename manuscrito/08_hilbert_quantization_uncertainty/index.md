---
title: "08. Espaço de Hilbert físico, quantização e incerteza"
---

# 08. Espaço de Hilbert físico, quantização e incerteza

A GDQ não começa postulando um espaço de Hilbert abstrato. Ela começa com
geometria, medida, ação, vínculos, contornos e setores físicos. Mesmo assim, a
camada operacional de Hilbert precisa aparecer: sem ela não há espectro,
produto interno positivo, operadores autoadjuntos, evolução unitária, regra de
Born ou tratamento controlado de incerteza.

O objetivo deste capítulo é explicar essa reconstrução sem inverter a
ontologia da teoria. O espaço de Hilbert é uma camada operacional reconstruída
a partir da geometria; não é o palco fundamental da GDQ.

## Roteiro

- [[08.1 - Por que a GDQ ainda precisa de Hilbert operacional]]
- [[08.2 - Reconstrução por reflexão positiva]]
- [[08.3 - Produto interno, quociente físico e domínios]]
- [[08.4 - Evolução unitária em tempo físico]]
- [[08.5 - Fase circular e a objeção de Wallstrom]]
- [[08.6 - Nós, holonomia e setores spinoriais]]
- [[08.7 - Incerteza por Cauchy-Schwarz no fluido de Madelung]]
- [[08.8 - Robertson-Schrödinger por positividade Hermitiana]]
- [[08.9 - O que fica para extensões entrópicas e GUP]]

## Resultado central

A cadeia operacional deste capítulo é:

$$
\text{GDQ geométrica}
\to
\text{setores regulares}
\to
\text{reflexão positiva}
\to
\mathcal H_{\rm phys}
\to
\text{operadores autoadjuntos}
\to
\text{unitariedade em }t
\to
\text{fase }S^1\text{-valued}
\to
\text{Wallstrom resolvido}
\to
\text{incerteza por positividade}.
$$

O espaço de Hilbert físico é:

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

O produto interno é:

$$
\langle [F],[G]\rangle_{\mathcal H}
=
\langle \Theta F\,G\rangle_E.
$$

No setor regular de uma partícula, essa estrutura reduz-se ao espaço
operacional familiar:

$$
L^2(N,E,d\Sigma_h).
$$

Essa redução é útil, mas não deve ser confundida com o fundamento ontológico da
GDQ.

Em termos lógicos, a mecânica quântica usual aparece aqui como setor
projetivo-operacional da GDQ. A cadeia é:

$$
\mathcal S_{\rm GDQ}
\to
\text{setor regular de Madelung}
\to
\mathcal H_{\rm phys}
\to
\text{projetores espectrais}.
$$

Portanto:

$$
\boxed{
\text{MQ projetiva}
\subset
\text{GDQ}.
}
$$

Essa inclusão não significa que a GDQ abandone a mecânica quântica. Significa
que a MQ é recuperada quando a geometria é observada no domínio regular,
Hilbertiano e projetivo. Fora desse domínio — por exemplo em contornos
dinâmicos, domínios variáveis, Hessianas efetivas não hermitianas, interfaces
clássico--quânticas e respostas de aparelho — a GDQ conserva graus de liberdade
geométricos que a formulação projetiva usual não descreve como fundamentais.

## Estatuto do resultado

O capítulo fecha estruturalmente três pontos:

1. reconstrução operacional do espaço de Hilbert físico, condicionada à
   positividade setorial;
2. resolução de Wallstrom pela fase circular/fibrado $U(1)$;
3. desigualdades de incerteza no setor regular reduzido.

Permanece condicional a reconstrução lorentziana completa para todo setor,
porque ela exige as hipóteses de positividade, domínio, cluster e reflexão
adequadas. Extensões entrópicas, GUP e correções torsionais metrológicas são
programa futuro.

## Controle editorial

- [[checklist_operacional|Checklist operacional do capítulo]]
- [[notes/provas_lemas_definicoes|Provas, lemas e definições associados]]
- [[notes/construcao_gdq_hilbert_quantizacao|Construção GDQ do Hilbert físico e da quantização]]
- [[notes/estados_observaveis_composicao_hilbert|Estados, observáveis e composição no Hilbert reconstruído]]
- [[notes/quantizacao_relativa_acao_exponenciada|Quantização relativa, ação exponenciada e termo de extremidade]]
- [[../formalizacao|Mapa estrutural das provas e formalizações]]

[[../index|← Home]] | [[08.1 - Por que a GDQ ainda precisa de Hilbert operacional|Next →]]
