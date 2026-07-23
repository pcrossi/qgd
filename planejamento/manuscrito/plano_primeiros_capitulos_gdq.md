# Plano de reestruturação dos primeiros capítulos da GDQ

## 1. Objetivo editorial

Os primeiros capítulos devem permitir que um leitor reconstrua a teoria sem
consultar capítulos posteriores. Entretanto, os quatro primeiros capítulos
preservam deliberadamente a ordem histórica de construção da GDQ:

\[
\text{problema}
\to
\text{geometrização da matéria}
\to
\text{causalidade complexa}
\to
\text{ação}
\to
\text{reconstrução quântica}
\to
\text{primeiro observável}.
\]

Essa ordem narrativa é parte da identidade do manuscrito. A reorganização não
deve apagá-la; deve apenas impedir que cada capítulo use resultados ainda não
definidos sem uma antecipação explícita.

O texto principal deve apresentar a teoria positiva. Auditorias, objeções e
provas longas permanecem nos documentos técnicos e apêndices.

## 2. Nova sequência recomendada

## Capítulo 0 — Convenções, escopo e mapa lógico

Função: impedir ambiguidades antes da primeira equação.

Conteúdo:

1. definição da GDQ e do que ela não assume;
2. ação oficial, apenas enunciada e referenciada;
3. tabela de símbolos fundamentais;
4. distinção entre \(t\), \(\tau\) e \(z_\tau\);
5. distinção entre bulk local \(\mathbb R^4\times T^4\), espaço-tempo físico e
   geometria cosmológica \(T^5\times S^3\);
6. classificação das afirmações: definição, teorema, hipótese, redução e
   previsão;
7. diagrama dos capítulos.

Fonte principal: `00 - Introdução Terminológica.md`, convenções consolidadas
nas Questões 2--4 e `memory.md`.

Não colocar neste capítulo:

- previsões numéricas;
- história detalhada;
- defesa contra o Modelo Padrão;
- derivações.

## Capítulo 1 — O problema de partida e os requisitos da teoria

Função: motivar sem prometer antecipadamente todas as soluções.

Conteúdo:

1. incompatibilidade operacional entre integrais de Wiener e Feynman;
2. Madelung como dicionário inicial, não como ontologia já provada;
3. requisitos: positividade, causalidade, unitariedade, regularidade e matéria
   localizada;
4. proposta central: matéria como configuração geométrica do mesmo substrato;
5. resumo verificável das contribuições, com status.

Fonte principal: atual Capítulo 1.

Mover para capítulos posteriores:

- detalhes de OS e unitariedade;
- fórmulas de regularização;
- resultados fenomenológicos;
- afirmações fortes sobre problemas matemáticos externos.

## Capítulo 2 — Geometrização da matéria

Função: apresentar conjuntamente a mudança ontológica e o domínio geométrico
em que ela se realiza.

Conteúdo:

1. variedade complexa de dimensão \(n=4\);
2. bulk local \(\mathbb R^4\times T^4\);
3. métrica Hermitiana \(g_{\mu\bar\nu}\);
4. estrutura complexa e forma fundamental;
5. conexão de Chern e conexão de Bismut;
6. torção \(H=d^c\omega\) quando aplicável;
7. folha física e reconstrução lorentziana, sem antecipar a prova;
8. papel separado das compactificações cosmológicas.

Fontes: atual Capítulo 2, `questoes/q02/questao_02.md`, `questoes/q03/questao_03.md` e consolidação da
Questão 4.

Regra crítica: não alternar silenciosamente entre Kähler estrita e geometria
Hermitiana com torção.

## Capítulo 3 — Causalidade complexa e estrutura dos campos

Função: preservar a descoberta causal original, introduzindo simultaneamente
o dicionário mínimo necessário para que o argumento seja legível.

Campos fundamentais:

\[
g_{\mu\bar\nu},\qquad f,\qquad\bar f.
\]

Variáveis derivadas:

\[
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
\]

Conteúdo adicional:

1. positividade e normalização de \(\rho\);
2. significado geométrico da fase;
3. velocidades de corrente e osmótica;
4. defeitos, zeros de densidade e condições topológicas;
5. quais objetos são campos e quais são respostas, fontes ou contornos;
6. dimensões físicas.

Regra crítica: não introduzir \(A_\mu\), \(B\), projetores ou operadores de
Pauli como campos fundamentais da ação.

O capítulo pode anunciar a forma da ação que será formalizada no Capítulo 4,
mas não deve afirmar consequências variacionais antes dessa formalização.

## Capítulo 4 — A ação oficial e o princípio variacional

Função: constituir o núcleo matemático do manuscrito.

Abrir com a ação imutável:

\[
\mathcal S_{\rm GDQ}=\int_\gamma\left[\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left\{\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n\right\}
\mathcal U\sqrt{\det g}\,d^{2n}z\right]\frac{d\tau}{\tau}.
\]

Ordem das derivações:

1. espaço admissível de configurações;
2. vínculos de normalização;
3. variação em \(S_R\): continuidade;
4. variação em \(\rho\) ou parte real: Hamilton--Jacobi--Bohm;
5. variação métrica: equação geométrica;
6. termos de bordo e condições naturais;
7. simetrias e correntes de Noether;
8. Hessiana física e modos zero;
9. fontes externas e multiplicadores, sem modificar a ação fundamental.

Incluir como exemplo estrutural curto:

\[
\frac{\partial E_{\rm on}}{\partial C}=\lambda,
\qquad
-\frac{\partial E_{\rm on}}{\partial B}=\mu,
\]

mostrando como vínculos e sondas entram no formalismo.

Fontes: atual Capítulo 4, `questoes/q02/questao_02.md`, `questoes/q04/questao_04.md`, `questoes/q10/questao_10.md` e
`questoes/q11/questao_11.md`.

## Capítulo 5 — Equações, regularidade e reconstrução do tempo físico

Função: retornar à causalidade do Capítulo 3 agora como consequência formal da
ação, distinguindo motivação causal de demonstração variacional.

Conteúdo:

1. variável causal complexa;
2. ramos avançado e retardado;
3. princípio causal de Sudarshan;
4. escolha física do contorno \(\gamma\);
5. relação entre fluxo \(\tau\) e tempo físico;
6. continuação/reconstrução lorentziana;
7. conservação e composição causal;
8. hipóteses necessárias para unitariedade.

Fonte: atual Capítulo 3, atual Capítulo 4 e Questões 4, 7, 8 e 20.

Regra crítica: não apresentar cancelamentos avançado--retardado como
automáticos sem declarar contorno, estado e domínio.

## Capítulo 6 — Regularidade, positividade e reconstrução quântica

Função: provar que a ação define uma teoria quântica admissível antes das
aplicações.

Conteúdo:

1. regularidade fornecida pela estrutura geométrica;
2. operador físico gauge-fixado;
3. positividade da medida e reflexão;
4. reconstrução Osterwalder--Schrader;
5. espaço de Hilbert físico;
6. Hamiltoniano positivo e unitariedade;
7. ausência de polos físicos adicionais;
8. distinção entre finitude geométrica e renormalização convencional;
9. status preciso da ausência de fantasmas.

Fontes: atuais Capítulos 4, 5 e 17; Questões 5--7, 20, 32--35.

## Capítulo 7 — Redução de Madelung e limite operacional da MQ

Função: mostrar que a mecânica quântica usual é uma redução da GDQ.

Conteúdo:

1. equações de continuidade e Hamilton--Jacobi--Bohm;
2. reconstrução de \(\Psi=\sqrt\rho e^{iS_R/\hbar}\);
3. equação de Schrödinger no regime apropriado;
4. corrente e observáveis;
5. regra de Born espacial;
6. hipóteses da extensão a projetores;
7. limite clássico.

Este capítulo deve anteceder spin, medida e experimentos.

## Capítulo 8 — Defeitos, circulação, spin e primeiro teste físico

Função: apresentar a primeira consequência não trivial da teoria.

Ordem interna:

1. defeitos e espaço perfurado;
2. corrente de Noether e circulação;
3. elo normal e fibração de Hopf;
4. dupla cobertura e spin \(1/2\);
5. isotropia do módulo;
6. campo externo como fonte;
7. teorema Noether--Zeeman;
8. Stern--Gerlach;
9. vestido geométrico líder do momento magnético;
10. status dos termos superiores.

Fontes: atuais Capítulos 9, 10, 11 e 19; `questoes/q42/questao_42.md`,
`topicos/medida_interface/teorema_noether_zeeman_gdq.md` e `topicos/geometria_torcao_hopf/projecao_hessiana_noether_g2.md`.

Esse capítulo substitui a atual dispersão do mesmo argumento em quatro
capítulos separados.

## 3. Mapa de migração dos capítulos atuais

| Capítulo atual | Destino principal | Ação editorial |
|---|---|---|
| 00 | novo Capítulo 0 | revisar e reduzir |
| 01 | novo Capítulo 1 | preservar motivação; remover antecipações |
| 02 | novo Capítulo 2 | preservar geometrização; organizar domínio e campos |
| 03 | novos Capítulos 3 e 5 | manter narrativa causal no 3; prova formal no 5 |
| 04 | novos Capítulos 4 e 6 | separar ação de regularidade |
| 05 | novo Capítulo 6 | renomear; evitar “renormalização” ontológica |
| 06 | partes posteriores | retirar do bloco fundacional |
| 09 | novo Capítulo 8 | consolidar topologia do spin |
| 10 | novo Capítulo 8 | consolidar Stern--Gerlach |
| 11 | novo Capítulo 8 e capítulo posterior de férmions | dividir |
| 13 | novo Capítulo 7 e capítulo de medida | dividir |
| 15 | novo Capítulo 8 | usar como objeção técnica à circulação |
| 16 | capítulo posterior de medida | não antecipar |
| 17 | novo Capítulo 6 | usar na estabilidade |
| 19 | novo Capítulo 8 | fundir com Zeeman/Noether |
| 20 | novo Capítulo 5 | integrar à reconstrução temporal |
| 21 | capítulo posterior de medida | manter após fundamentos |

## 4. Regras de redação

Cada capítulo deve começar com:

1. objetivo;
2. dados e hipóteses;
3. resultado principal;
4. dependências anteriores.

Cada capítulo deve terminar com:

1. teoremas efetivamente demonstrados;
2. hipóteses ainda utilizadas;
3. parâmetros livres ou dados externos;
4. consequências usadas pelo capítulo seguinte.

Evitar no corpo principal:

- “como provamos” sem referência exata;
- analogias apresentadas como equações;
- números experimentais antes da fórmula preditiva;
- comparações longas com o Modelo Padrão;
- misturar espaço local e cosmológico;
- usar “exato” para aproximação líder;
- repetir a mesma derivação em capítulos diferentes.

### 4.1 Sintaxe matemática para Obsidian e Quartz

Toda matemática dos novos capítulos deve usar a sintaxe MathJax reconhecida
diretamente pelo Obsidian e pelo Quartz.

Matemática inline:

```md
A densidade é $\rho=e^{-(f+\bar f)/2}$ e permanece positiva.
```

Equação destacada:

```md
$$
\rho=e^{-(f+\bar f)/2}
$$
```

Os delimitadores `$$` devem ficar sempre em linhas próprias e distintas. Não
usar:

```md
$$\rho=e^{-f}$$
```

Também evitar nos arquivos destinados ao Quartz:

- `\[ ... \]`;
- `\( ... \)`;
- bloco `$$` na mesma linha da equação;
- equações multilineares sem ambiente LaTeX interno apropriado.

Para alinhamento:

```md
$$
\begin{aligned}
\rho &= e^{-(f+\bar f)/2}, \\
S_R &= \frac{\hbar}{2i}(f-\bar f).
\end{aligned}
$$
```

Todos os símbolos devem ser definidos no texto imediatamente antes ou depois
do bloco.

### 4.2 Escrita em camadas e desmistificação da matemática

O manuscrito reconhece que a linguagem matemática é restritiva por uma razão:
ela elimina ambiguidades e permite deduções verificáveis. Entretanto, o texto
não deve pressupor que todo leitor já domina geometria diferencial, topologia,
análise funcional, hidrodinâmica e fundamentos quânticos.

A exposição será organizada em três camadas:

1. **texto principal:** apresenta a ideia física, o problema e o resultado em
   linguagem clara;
2. **formulação matemática:** registra definições, hipóteses e equações com o
   rigor necessário;
3. **notas pedagógicas:** explicam os instrumentos matemáticos utilizados,
   desde a intuição até a formulação aplicada na GDQ.

O texto principal não deve abandonar o rigor, mas também não deve interromper
cada dedução para ensinar integralmente uma disciplina matemática. Quando uma
explicação longa for necessária, utilizar um link como:

```md
A definição formal e uma construção intuitiva são apresentadas em
[[Conexões e transporte paralelo]].
```

Cada nota pedagógica deve, quando aplicável, conter:

1. motivação intuitiva;
2. exemplo elementar;
3. definição matemática;
4. interpretação geométrica ou física;
5. notação adotada no manuscrito;
6. aplicação concreta na GDQ;
7. erros de interpretação comuns;
8. referências para aprofundamento.

Princípio editorial:

> Nenhum conceito matemático central será apenas mencionado. Ele será
> explicado no corpo quando indispensável à dedução ou encaminhado a uma nota
> pedagógica autocontida.

As notas serão criadas organicamente, à medida que os conceitos aparecerem.
Não é necessário escrever antecipadamente uma enciclopédia matemática que o
manuscrito talvez não utilize.

## 5. Método seguro de execução

Não substituir imediatamente os arquivos atuais. Criar uma nova árvore
canônica em `manuscrito/`:

```text
manuscrito/
  index.md
  00_conventions/
    index.md
  01_initial_problem/
    index.md
    01.1 - Feynman e Wiener.md
    01.2 - Requisitos da teoria.md
    01.3 - Programa da GDQ.md
  02_geometrization_of_matter/
    index.md
    02.1 - Ontologia geométrica.md
    02.2 - Variedade complexa.md
    02.3 - Estrutura Hermitiana.md
    02.4 - Conexão de Bismut.md
    02.5 - Campos fundamentais.md
  03_complex_causality/
    index.md
    03.1 - Princípio de Sudarshan.md
    03.2 - Tempo complexo.md
    03.3 - Ramos causais.md
    03.4 - Contorno físico.md
  04_official_action/
    index.md
    04.1 - Enunciado da ação.md
    04.2 - Espaço de configurações.md
    04.3 - Variação da fase.md
    04.4 - Variação da densidade.md
    04.5 - Variação métrica.md
    04.6 - Bordo e multiplicadores.md
    04.7 - Noether e Hessiana.md
  05_equations_and_physical_time/
    index.md
  06_quantum_reconstruction/
    index.md
  07_quantum_mechanics_reduction/
    index.md
  08_spin_and_stern_gerlach/
    index.md
  appendices/
  notes/
    index.md
    geometry/
      index.md
    topology/
      index.md
    analysis/
      index.md
    physics/
      index.md
  definitions/
  figures/
  ref/
```

Os nomes de todas as pastas devem usar apenas ASCII, sem espaços e sem
caracteres acentuados. O título apresentado ao leitor é definido no YAML do
`index.md`, portanto não precisa coincidir com o nome físico da pasta.

A pasta `ref/` é reservada às referências bibliográficas, índices de fontes e
notas bibliográficas publicáveis. Rascunhos de auditoria e documentos
`questão_*.md` permanecem fora de `manuscrito/`.

A pasta `notes/` reúne explicações pedagógicas da matemática e da física usadas
no texto. Ela é distinta de `appendices/`: notas ensinam conceitos; apêndices
preservam provas longas, cálculos técnicos e resultados auxiliares específicos
da GDQ.

### 5.1 Função do `index.md` de cada capítulo

O índice local segue o padrão Quartz já usado no projeto de referência:

```yaml
---
title: "01. O problema inicial"
---
```

Depois do frontmatter, contém:

1. objetivo do capítulo;
2. hipóteses usadas;
3. ordem das seções;
4. resultados principais;
5. dependências anteriores;
6. links para provas técnicas;
7. status editorial.

O sumário do capítulo usa links comuns:

```md
- [[01.1 - Feynman e Wiener]]
- [[01.2 - Requisitos da teoria]]
- [[01.3 - Programa da GDQ]]

[[index|Home]] | [[01.1 - Feynman e Wiener|Next →]]
```

Assim, cada seção existe como nota independente, e o `index.md` funciona como
página de entrada e sumário do capítulo. A renderização contínua por
transclusão pode ser criada posteriormente em uma página separada, mas não é
necessária para a navegação Quartz principal.

### 5.2 Granularidade das notas

Uma nota deve conter uma unidade argumentativa completa, não apenas alguns
parágrafos desconectados. Em geral:

- uma definição central;
- uma proposição e sua prova curta;
- uma etapa variacional;
- uma consequência física;
- uma discussão conceitual coesa.

Evitar tanto capítulos monolíticos quanto fragmentação excessiva em uma nota
por equação.

### 5.3 Links e transclusões

Usar:

- `[[nota]]` para dependência conceitual;
- `![[nota]]` apenas em páginas especiais de leitura contínua;
- links com cabeçalho para resultados específicos;
- aliases quando a mesma definição possuir nome curto e nome técnico.

Uma seção fundamental deve possuir um único local canônico. Outros capítulos
devem apontar para ela, não copiar sua derivação.

### 5.4 Metadados mínimos

O `index.md` de cada pasta exige somente:

```yaml
---
title: "Título público em português"
---
```

Notas de seção podem usar propriedades adicionais durante a edição:

```yaml
---
tipo: secao
capitulo: 4
status: rascunho
dependencias:
  - "[[03.4 - Contorno físico]]"
fontes:
  - "[[questão_4]]"
---
```

Valores recomendados para `status`:

- `esqueleto`;
- `rascunho`;
- `auditado`;
- `consolidado`;
- `publicavel`.

Não colocar no YAML conclusões científicas extensas; ele serve apenas para
organização editorial.

### 5.5 Navegação Quartz

Cada seção deve terminar com navegação explícita:

```md
[[index|← Sumário]] | [[02.2 - Próxima seção|Next →]]
```

A última seção retorna ao índice do capítulo e aponta para o capítulo
seguinte. Como vários arquivos se chamam `index.md`, links ambíguos devem usar
o caminho relativo ou um alias suficientemente específico quando necessário.

### 5.6 Notas canônicas e notas de trabalho

Separar:

```text
manuscrito/                 texto canônico em construção
questão_*.md                auditoria e rastreabilidade
q*/                         cálculo e desenvolvimento
ideias/possibilidades.md           ideias futuras
faltas.md                   pendências
```

O manuscrito pode linkar uma auditoria durante a escrita, mas a versão final
não deve depender de o leitor navegar pelos rascunhos para compreender uma
prova.

Fluxo de trabalho por capítulo:

1. copiar apenas proposições ainda vigentes;
2. marcar a origem de cada bloco em comentário editorial temporário;
3. reconciliar notação;
4. remover duplicações;
5. verificar dependências para trás;
6. auditar dimensões e hipóteses;
7. comparar com os documentos consolidados;
8. somente depois substituir ou arquivar o capítulo antigo.

## 6. Ordem prática recomendada

Preservando a ordem conceitual dos quatro primeiros capítulos, a ordem de
revisão passa a ser:

1. Capítulo 1 — problema inicial;
2. Capítulo 2 — geometrização da matéria;
3. Capítulo 3 — causalidade complexa e dicionário mínimo;
4. Capítulo 4 — ação e variação;
5. Capítulo 5 — consequências formais da causalidade;
6. Capítulo 6 — reconstrução;
7. Capítulo 7 — redução quântica;
8. Capítulo 8 — spin e Stern--Gerlach;
9. Capítulo 0 — convenções finais e índice remissivo.

O Capítulo 0 pode ser finalizado por último, mas será colocado antes do
Capítulo 1 na versão publicada.
