---
title: "Checklist operacional — Capítulo 1"
---

# Checklist operacional — Capítulo 1

Este checklist segue o protocolo metodológico do Capítulo 27, sem reabrir a
teoria e sem antecipar resultados dos capítulos posteriores.

## 1. Objetivo do capítulo

O Capítulo 1 deve cumprir uma função fundacional e pedagógica:

1. mostrar a eficácia matemática como problema metodológico;
2. separar integral de Wiener e integral de Feynman;
3. explicar por que Wick é uma continuação condicional, não uma identidade
   física automática;
4. mostrar que termos de contorno e calibre importam;
5. introduzir Madelung como decomposição de densidade e fase;
6. introduzir Nelson como tratamento de caminhos não diferenciáveis;
7. motivar a passagem para geometria ponderada sem declarar ainda a GDQ
   completa como demonstrada.

Status do capítulo: **fundacional e pedagógico**.

Ele não deve provar sozinho:

- a ação oficial;
- a reconstrução lorentziana;
- a regra de Born;
- o espaço de Hilbert físico;
- a ponte global–local;
- a origem completa das massas;
- a emergência variacional de todos os coeficientes estocásticos.

## 2. Situação do corpo principal

| Seção | Status | Observação |
|---|---|---|
| `01.1` | pronta em primeira versão | Introduz Wigner e a motivação metodológica. |
| `01.2` | pronta em primeira versão | Define vocabulário e evita confusão entre GDQ, reduções e termos históricos. |
| `01.3` | pronta em primeira versão | Separa corretamente Wiener e Feynman. |
| `01.4` | pronta em primeira versão | Trata Wick por espectro, domínio e contorno. |
| `01.5` | pronta em primeira versão | Explica derivadas totais, calibre e bordo. |
| `01.6` | pronta em primeira versão | Deriva Madelung como decomposição, não como ontologia final. |
| `01.7` | pronta em primeira versão | Introduz Nelson e caminhos não diferenciáveis com cautela. |
| `01.8` | pronta condicionalmente | A difusão universal é apresentada como hipótese/ponte condicional. |
| `01.9` | pronta em primeira versão | Motiva geometria e Perelman como arena auxiliar, não como ação oficial. |

## 3. Notas chamadas e função lógica

| Nota | Chamada por | Status |
|---|---|---|
| `Medidas e integrais em espaços de caminhos` | `01.3` | Nota pedagógica. |
| `Continuação espectral do grupo unitário ao semigrupo` | `01.4` | Derivação matemática. |
| `Equações elípticas, parabólicas, hiperbólicas e dispersivas` | `01.4`, `01.9` | Nota pedagógica/analítica. |
| `Derivada total, bordo e continuação euclidiana` | `01.5` | Derivação. |
| `Decomposição de Madelung passo a passo` | `01.6` | Derivação. |
| `Derivadas de Nelson e equação de continuidade` | `01.7` | Derivação estocástica. |
| `Identidade entre velocidade osmótica e potencial quântico` | `01.7` | Derivação local. |
| `Difusão universal e inércia geométrica - análise condicional` | `01.8` | Teorema/ponte condicional. |
| `Difusão variável de Nelson na GDQ` | `01.8` | Derivação em redução estocástica. |
| `NESS, fluxo geométrico e irreversibilidade efetiva` | `01.9` | Nota conceitual condicionada. |

Avaliação: as chamadas principais existem. O capítulo já está adequado ao
formato “corpo didático + prova em nota”.

## 4. Material legado preservado

Fonte legada principal:

o capítulo legado correspondente

Blocos preservados no novo capítulo:

1. contraste Wiener/Feynman;
2. rotação de Wick;
3. derivada total e contorno;
4. Madelung;
5. Nelson;
6. decomposição de velocidades;
7. difusão universal;
8. motivação geométrica via fluxo.

Correções de status em relação ao legado:

1. a equivalência por Wick foi rebaixada para continuação condicional;
2. o termo de bordo não é tratado como quebra automática de invariância, mas
   como dado de transformação conjunta de kernel, estados e observáveis;
3. a difusão universal não é declarada como fechada pela ação oficial neste
   capítulo;
4. Perelman é apresentado como matriz geométrica auxiliar/motivação, não como
   ação física fundamental da GDQ.

## 5. Referências necessárias

Fichas já presentes em `manuscrito/ref/`:

- `Wigner 1960 - The Unreasonable Effectiveness of Mathematics.md`;
- `Wiener 1923 - Differential-Space.md`;
- `Feynman 1948 - Space-Time Approach to Non-Relativistic Quantum Mechanics.md`;
- `Kac 1949 - On Distributions of Certain Wiener Functionals.md`;
- `Wick 1954 - Properties of Bethe-Salpeter Wave Functions.md`;
- `Osterwalder and Schrader 1973 - Axioms for Euclidean Green Functions.md`;
- `Madelung 1927 - Quantentheorie in hydrodynamischer Form.md`;
- `Nelson 1966 - Derivation of the Schrodinger Equation from Newtonian Mechanics.md`;
- `Nelson 1967 - Dynamical Theories of Brownian Motion.md`;
- `Hamilton 1982 - Three-manifolds with positive Ricci curvature.md`;
- `Perelman 2002 - The Entropy Formula for the Ricci Flow.md`.

Pendência editorial: quando o OCR completo estiver disponível para todas as
referências, revisar páginas citadas e manter apenas as fichas curtas no texto
público.

## 6. Scripts numéricos e simbólicos

Scripts obrigatórios para fechamento científico do Capítulo 1: **nenhum**.

Motivo: o capítulo é conceitual e fundacional. Ele não faz previsão
metrológica. As contas centrais são analíticas e já estão em notas.

Scripts preservados nesta versão:

1. `scripts/comparar_kernel_wiener_feynman.py`  
   Ilustra a diferença entre peso gaussiano positivo e fase oscilatória.

2. `scripts/verificar_termo_osmotico_bohm.py`  
   Verifica a identidade entre energia osmótica, divergência osmótica e termo
   de Bohm no setor regular.

3. `scripts/verificar_difusao_variavel_ito.py`  
   Verifica a expansão de Itô para difusão variável
   $D=\nu_0\Omega^{-1}$, a equivalência entre Fokker--Planck conservativa e
   expandida, e a velocidade osmótica com o termo
   $-\nu\nabla\ln\Omega$.

Classificação: **verificação pedagógica de consistência**, não previsão
física e não prova independente da GDQ.

Possível script futuro, se for útil didaticamente: uma matriz Hermitiana finita
mostrando a passagem formal de grupo unitário a semigrupo amortecido. Esse
script não é necessário para o fechamento do capítulo porque a dedução
analítica já está na nota espectral.

## 7. Pontos didáticos a revisar na leitura final

Antes de considerar o Capítulo 1 editorialmente pronto:

1. verificar se o texto flui como capítulo, não como apresentação de tópicos;
2. manter as frases de transição entre `01.5`, `01.6`, `01.7`, `01.8` e
   `01.9`;
3. manter a distinção entre “motivação geométrica” e “derivação da ação
   oficial”;
4. garantir que a seção `01.8` não soe como fechamento completo da massa ou da
   difusão universal;
5. revisar se as analogias com fluido, tecido e malha permanecem subordinadas
   às definições;
6. conferir renderização Quartz;
7. conferir links Obsidian.

## 8. Veredito operacional

O Capítulo 1 está **estruturalmente montado e preserva o conteúdo essencial do
legado**.

O que ainda falta é editorial, não conceitual:

1. revisão humana de fluidez fina;
2. conferência final das páginas das referências quando os OCRs forem
   estabilizados;
3. checagem final de links e renderização em Quartz.

Portanto, o capítulo pode ser usado como base para a reescrita final, desde
que as notas chamadas permaneçam associadas ao texto.
