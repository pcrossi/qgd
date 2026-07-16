# Plano técnico para reconstrução e teste da GDQ

## 1. Objetivo correto

O objetivo não deve ser “refutar a auditoria” nem provar antecipadamente que
a GDQ está correta. O objetivo deve ser:

> Construir a formulação mínima e precisa da GDQ, testar sua consistência
> matemática e confrontar suas consequências com dados que não tenham sido
> usados em sua construção.

O projeto deve admitir três resultados em cada etapa:

1. **Aprovado:** a hipótese satisfaz os critérios definidos.
2. **Reformulação necessária:** o problema é reparável mediante alteração
   explícita dos axiomas.
3. **Refutado:** a hipótese é incompatível com matemática, consistência
   interna ou observação.

Adicionar capítulos ou explicações verbais não conta como resolução. Cada
objeção deve terminar em uma definição, demonstração, cálculo reproduzível
ou teste experimental.

---

## 2. Regras metodológicas

### 2.1 Registro de axiomas

Criar `AXIOMAS_GDQ.md` contendo:

- versão da teoria;
- variedade base;
- dimensão e assinatura;
- conexão;
- campos fundamentais;
- constantes fundamentais;
- condições de contorno;
- simetrias;
- observáveis;
- dados experimentais usados;
- hipóteses ainda não demonstradas.

Qualquer mudança nesses elementos cria uma nova versão da teoria.

### 2.2 Separação entre entrada e resultado

Para cada cálculo, criar uma tabela:

| Item | Categoria |
|---|---|
| Axioma matemático | Entrada |
| Constante fundamental assumida | Entrada |
| Dado usado para calibração | Entrada |
| Resultado derivado | Saída |
| Dado reservado para teste | Teste cego |

Uma grandeza não pode aparecer simultaneamente como entrada e como previsão.

### 2.3 Congelamento do modelo

Antes de comparar uma previsão com dados:

1. congelar ação, parâmetros e condições de contorno;
2. registrar o valor previsto e sua incerteza;
3. registrar quais dados não foram consultados;
4. somente então realizar a comparação.

Se a teoria for alterada após a comparação, o novo resultado deixa de ser
previsão e passa a ser ajuste.

### 2.4 Linguagem científica

Usar:

- **definição** para escolhas;
- **ansatz** para formas assumidas;
- **lema/teorema** somente com hipóteses e prova;
- **reprodução** quando um resultado conhecido é recuperado;
- **previsão** somente quando o resultado não foi usado como entrada;
- **evidência** somente com comparação estatística.

---

## 3. Arquitetura de documentos

Recomenda-se separar o projeto em:

```text
fundamentos/
  01_axiomas.md
  02_geometria.md
  03_acao.md
  04_equacoes_de_campo.md
  05_problema_de_cauchy.md

quantizacao/
  01_espaco_de_estados.md
  02_observaveis.md
  03_unitariedade.md
  04_regra_de_born.md
  05_wallstrom.md
  06_limite_lorentziano.md

validacao/
  01_limites_conhecidos.md
  02_solucoes_solitonicas.md
  03_previsoes_cegas.md
  04_comparacao_estatistica.md

extensoes/
  modelo_padrao/
  cosmologia/
  navier_stokes/
```

Os capítulos fenomenológicos atuais devem ser tratados como hipóteses em
`extensoes/` até a conclusão dos fundamentos.

---

## 4. Fase 0 — Controle epistemológico

### Objetivo

Impedir circularidade, ajuste retrospectivo e mudança silenciosa da teoria.

### Tarefas

1. Catalogar todas as constantes e fatores usados:
   `6π⁵`, `1920`, `3/(4π²)`, fatores de Fano, `δ`, cortes UV e demais
   normalizações.
2. Marcar sua origem como:
   - axioma;
   - teorema;
   - resultado numérico;
   - dado experimental;
   - ajuste.
3. Remover dos scripts qualquer valor experimental usado para construir o
   operador que deveria prevê-lo.
4. Criar testes automáticos de:
   - unidades;
   - aritmética;
   - normalização;
   - independência entre entrada e resultado.

### Critério de saída

Nenhuma alegação de previsão usa direta ou indiretamente o valor previsto.

### Critério de falha

Se uma escala absoluta não puder ser obtida sem dado experimental, o texto
deve declarar que a teoria prevê apenas razões adimensionais.

---

## 5. Fase 1 — Modelo geométrico mínimo

### Objetivo

Definir exatamente o objeto matemático chamado GDQ.

### 5.1 Dimensão

Não tentar inicialmente “provar” dimensão complexa quatro. Adotar:

> Hipótese D: a variedade fundamental possui dimensão complexa \(n\).

Manter \(n\) simbólico até que o conteúdo de campos e as anomalias estejam
definidos. A seleção dimensional será testada posteriormente.

### 5.2 Variedade e assinatura

Definir:

- variedade hermitiana \((M,J,g)\);
- dimensão real \(2n\);
- assinatura da métrica;
- completude ou compacidade;
- orientação;
- estrutura spin;
- condições de bordo;
- subvariedade física, caso exista.

Uma subvariedade lagrangiana não recebe assinatura lorentziana
automaticamente. A assinatura deve fazer parte da construção.

### 5.3 Conexão

Escolher uma única conexão fundamental. Se for a conexão de Bismut:

\[
\nabla^B g=0,\qquad \nabla^B J=0,\qquad
T^B(X,Y,Z)=H(X,Y,Z),
\]

com \(H\) uma 3-forma real totalmente antissimétrica.

Definir:

- convenção de sinal;
- relação entre \(H\) e contorção;
- se \(dH=0\);
- transformação de calibre de \(H\);
- curvatura e identidades de Bianchi;
- relação com Levi-Civita e Chern.

Não afirmar que Kähler implica torção. Se \(H\neq0\), explicar em qual
sentido a geometria é hermitiana, Kähler com torção ou pluriclosed.

### 5.4 Campos fundamentais

Criar tabela:

| Campo | Tipo | Dimensão física | Dinâmico? |
|---|---|---:|---|
| \(g\) | métrica | definida por convenção | sim |
| \(J\) | estrutura complexa | 1 | fixa/dinâmica |
| \(H\) | 3-forma de torção | determinar | sim |
| \(f\) | escalar/dílaton | determinar | sim |
| \(\rho\) | densidade | \(L^{-d}\) | sim |
| \(S\) | ação/fase | ação | sim |

Não identificar campos diferentes antes de demonstrar equivalência.

### Entregável

`fundamentos/02_geometria.md`, com definições suficientes para que outro
pesquisador reconstrua todos os tensores sem consultar prosa ontológica.

### Critério de saída

Todos os símbolos têm tipo, domínio, unidade e lei de transformação.

---

## 6. Fase 2 — Ação mínima

### Objetivo

Obter toda a dinâmica de um único princípio variacional.

### 6.1 Construção

Começar com a menor ação possível. Uma estrutura candidata, ainda a ser
testada, é:

\[
I[g,H,f,\rho,S]
=\int d\tau\int_M d\mu_g\,
\left[
\rho\,\partial_\tau S
+\frac{\rho}{2m}|\nabla S|^2
+V\rho
+\frac{\hbar^2}{8m}\frac{|\nabla\rho|^2}{\rho}
+aR\rho
+b|H|^2\rho
+\mathcal L_{\mathrm{geom}}
\right].
\]

Essa expressão é apenas um ponto de partida. Cada coeficiente precisa ser
derivado, assumido explicitamente ou eliminado.

O termo \(\rho\partial_\tau S\) é necessário se a variação em \(S\) deve
produzir uma equação de continuidade.

### 6.2 Requisitos

Demonstrar:

- realidade da ação;
- consistência dimensional;
- invariância por difeomorfismos;
- simetrias de calibre;
- termos de bordo;
- variáveis independentes;
- vínculos;
- Hamiltoniano;
- energia limitada inferiormente, quando aplicável.

### 6.3 Variação

Calcular linha por linha:

\[
\frac{\delta I}{\delta S},\quad
\frac{\delta I}{\delta\rho},\quad
\frac{\delta I}{\delta g},\quad
\frac{\delta I}{\delta H},\quad
\frac{\delta I}{\delta f}.
\]

Não inserir depois equações que não resultem da ação.

### Critério de saída

Todas as equações usadas nos capítulos posteriores são consequências da
ação ou estão claramente rotuladas como condições externas.

### Critério de falha

Se o funcional de Perelman não puder atuar como ação física sem introduzir
dinâmica adicional, ele deve ser tratado como funcional auxiliar, não como
ação unificada.

---

## 7. Fase 3 — Teste do mapeamento Perelman–Madelung

### Objetivo

Determinar se existe equivalência, correspondência parcial ou apenas
analogia.

### 7.1 Proposição precisa

Formular um enunciado contendo:

- espaço das soluções Madelung;
- espaço das soluções do fluxo geométrico;
- mapa entre os espaços;
- hipóteses de regularidade;
- condições iniciais e de contorno;
- tratamento de \(\rho=0\);
- preservação de normalização;
- invertibilidade;
- correspondência das equações.

### 7.2 Testes obrigatórios

Verificar o mapa em:

1. partícula livre;
2. poço infinito;
3. oscilador harmônico;
4. estado com nó;
5. domínio multiplamente conexo;
6. estado dependente do tempo.

### 7.3 Resultados admissíveis

- **Equivalência:** mapa bijetivo que preserva a dinâmica.
- **Correspondência parcial:** válido somente em uma classe restrita.
- **Analogia:** sem mapa de soluções.
- **Incompatibilidade:** as equações não podem ser identificadas.

### Critério de saída

Publicar o resultado obtido, inclusive se for negativo.

---

## 8. Fase 4 — Existência, estabilidade e causalidade

### Objetivo

Demonstrar que as equações definem uma dinâmica matematicamente utilizável.

### Tarefas

1. Fixar gauge por método apropriado, como DeTurck quando aplicável.
2. Determinar o tipo das EDPs.
3. Provar existência e unicidade local.
4. Identificar critérios de continuação.
5. Demonstrar preservação de:
   - positividade de \(\rho\);
   - normalização;
   - assinatura;
   - restrições de calibre.
6. Estudar estabilidade linear dos pontos fixos.
7. Calcular espectro do operador de Jacobi.
8. Mostrar quais quantidades são conservadas e quais são monotônicas.

Monotonicidade de \(\mathcal W\) não deve ser interpretada automaticamente
como estabilidade de partículas.

### Critério de saída

Existência de ao menos uma solução não trivial, estável sob perturbações
admissíveis.

---

## 9. Fase 5 — Quantização

### Objetivo

Transformar o modelo geométrico em uma teoria quântica operacional.

### 9.1 Estrutura de estados

Definir:

- espaço de Hilbert;
- produto interno;
- operadores;
- domínios;
- estados físicos;
- observáveis;
- evolução.

### 9.2 Unitariedade

Demonstrar:

\[
\frac{d}{dt}\langle\psi|\psi\rangle=0
\]

para tempo físico. Um fluxo dissipativo em \(\tau\) não é automaticamente
evolução quântica unitária.

### 9.3 Regra de Born

Não definir \(R=\sqrt{\rho}\) e então alegar ter derivado
\(\rho=R^2\). É necessário explicar probabilidades de resultados.

Uma derivação aceitável deve tratar:

- aditividade para alternativas exclusivas;
- normalização;
- contextualidade;
- sistemas compostos;
- repetibilidade;
- base de medição.

### 9.4 Wallstrom

Não usar uma soma sobre setores inteiros como prova de que somente setores
inteiros existem. Demonstrar a quantização a partir da estrutura global do
espaço de estados, fibrado de linhas ou condição de regularidade.

### 9.5 Medida

Construir explicitamente:

- sistema;
- aparelho;
- ambiente;
- interação;
- decoerência;
- probabilidades dos registros.

Dominância de um estado fundamental dissipativo não resolve, sozinha, o
problema da medida.

### Critério de saída

O modelo produz probabilidades normalizadas e resultados para medições em
bases arbitrárias sem inserir a regra de Born como peso.

---

## 10. Fase 6 — Limite lorentziano

### Objetivo

Determinar se a formulação euclidiana admite reconstrução causal.

### Tarefas

Construir funções de Schwinger e verificar:

1. regularidade;
2. invariância euclidiana;
3. simetria;
4. reflexão positiva;
5. propriedade de cluster.

Somente depois aplicar reconstrução Osterwalder–Schrader.

Também demonstrar:

- cone causal;
- propagadores retardados;
- ausência de sinalização superluminal;
- relação dimensional entre \(\tau\) e \(t\).

### Critério de falha

Se reflexão positiva falhar, a continuação não define uma teoria quântica
lorentziana unitária.

---

## 11. Fase 7 — Spin e férmions

### Objetivo

Derivar estrutura espinorial, não apenas circulação.

### Tarefas

1. Construir o fibrado spin.
2. Definir álgebra de Clifford.
3. Definir operador de Dirac com torção:

\[
D_H = \gamma^\mu\nabla_\mu^B.
\]

4. Determinar espectro, quiralidade e transformação sob \(2\pi\) e \(4\pi\).
5. Demonstrar o limite de Dirac conhecido.
6. Verificar condições do teorema spin–estatística.

### Critério de saída

Spin \(1/2\), anticomutação e exclusão surgem da estrutura de estados, sem
serem impostos por \(\kappa=\pm1\).

---

## 12. Fase 8 — Seleção dimensional e anomalias

### Objetivo

Somente agora testar se \(n=4\) é selecionado.

### Pré-requisitos

- conteúdo de campos;
- representações;
- operadores quirais;
- grupo de calibre;
- polinômio de anomalia.

### Tarefas

Para cada dimensão candidata:

1. calcular índice dos operadores;
2. calcular anomalias de calibre, gravitacional e mista;
3. verificar cancelamento local e global;
4. verificar estabilidade e graus de liberdade físicos.

### Resultado possível

Se várias dimensões forem consistentes, \(n=4\) não foi derivado e deve
permanecer axioma ou receber outro mecanismo de seleção.

---

## 13. Fase 9 — Renormalização

### Objetivo

Determinar se a teoria quântica é consistente no ultravioleta.

### Tarefas

1. Expandir a ação em torno de um background.
2. Fixar gauge.
3. Derivar propagadores e vértices.
4. Introduzir fantasmas quando necessários.
5. Calcular correções de um loop.
6. Verificar identidades de Ward ou Slavnov–Taylor.
7. Calcular funções beta.
8. Demonstrar unitariedade e estrutura dos polos.
9. Testar dependência do esquema.

Um fator \(e^{-p^2/\Lambda^2}\) só pode ser usado se resultar do operador
cinético. Inserção manual é um regulador, não uma solução UV.

### Critério de saída

As amplitudes são finitas ou renormalizáveis dentro de uma expansão
controlada e preservam as simetrias.

---

## 14. Fase 10 — Recuperação de resultados conhecidos

### Objetivo

Verificar correspondência antes de procurar novas partículas.

### Sequência

1. partícula livre;
2. oscilador harmônico;
3. átomo de hidrogênio;
4. spin em campo magnético;
5. espalhamento simples.

Para cada caso, registrar:

- parâmetros usados;
- resultado da GDQ;
- resultado conhecido;
- diferença;
- limite responsável pela concordância.

Recuperar a equação conhecida depois de assumi-la não conta como teste.

---

## 15. Fase 11 — Constantes e massas

### Objetivo

Testar se a teoria possui poder preditivo real.

### 15.1 Escala dimensional

Antes de calcular massas, identificar a origem de uma escala \(L_0\):

\[
m_n=\frac{\hbar}{cL_0}F(\lambda_n).
\]

Se \(L_0\) vier de uma massa medida, somente razões de massas poderão ser
consideradas previsões.

### 15.2 Constante de estrutura fina

Para derivar \(\alpha\), é necessário:

1. derivar o setor \(U(1)\);
2. reduzir a ação à forma canônica;
3. identificar o coeficiente do termo \(F_{\mu\nu}F^{\mu\nu}\);
4. normalizar as cargas;
5. obter \(\alpha(\mu)\);
6. especificar a escala \(\mu\).

Um número próximo de 137 obtido de volumes não basta.

### 15.3 Massas

Definir um operador independente dos dados:

\[
\mathcal O\phi_n=\lambda_n\phi_n.
\]

Fixar previamente:

- domínio;
- métrica;
- condições de contorno;
- escala;
- mapa entre \(\lambda_n\) e massa.

Somente então calcular elétron, múon, tau e demais estados.

### Critério de saída

Ao menos um valor não utilizado na construção deve ser previsto com
incerteza antes da comparação.

---

## 16. Fase 12 — Modelo Padrão

Esta fase é um projeto próprio. Deve incluir:

- \(SU(3)_C\times SU(2)_L\times U(1)_Y\);
- representações de todos os férmions;
- hipercargas;
- quiralidade;
- cancelamento de anomalias;
- setor de Higgs ou mecanismo substituto;
- massas;
- CKM;
- PMNS;
- violação CP;
- acoplamentos correntes;
- confinamento;
- limite perturbativo.

Confinamento exige derivar área de tubo, tensão e Wilson loops; não se pode
assumir seção transversal constante e depois concluir \(V(r)=\sigma r\).

---

## 17. Fase 13 — Previsão cega

### Requisitos

A previsão deve:

- não ter sido usada para construir ou ajustar a teoria;
- ser quantitativa;
- possuir incerteza;
- diferir de modo identificável de teorias concorrentes;
- ter condições experimentais definidas;
- admitir refutação.

### Protocolo

Criar um arquivo datado:

```text
previsao:
observavel:
valor:
incerteza:
parametros_de_entrada:
dados_proibidos:
comparacao_modelo_padrao:
criterio_de_refutacao:
```

Não usar como “previsão cega” valores já conhecidos, como o raio do próton
muônico ou ângulos PMNS atualmente medidos.

---

## 18. Projetos que devem permanecer separados

### 18.1 Cosmologia

Somente iniciar após obter equações covariantes e setor gravitacional
consistente. A validação deve ser conjunta com:

- expansão de fundo;
- CMB;
- BAO;
- supernovas;
- lentes;
- crescimento de estrutura;
- BBN.

Explicar isoladamente MOND, Hubble ou lítio com fatores diferentes não
constitui modelo cosmológico.

### 18.2 Navier–Stokes

A suposta resolução do problema Clay deve ser retirada do manuscrito
principal. Ela não é necessária para validar a GDQ.

Um projeto separado precisaria provar uma estimativa uniforme em
\(\epsilon\) sem assumir:

\[
\int_0^T\|\nabla u\|_\infty\,dt<\infty.
\]

Se essa quantidade for assumida, a circularidade permanece.

---

## 19. Ordem prática de execução

```text
Fase 0  Controle epistemológico
   ↓
Fase 1  Geometria mínima
   ↓
Fase 2  Ação e variações
   ↓
Fase 3  Teste Perelman–Madelung
   ↓
Fase 4  Existência e estabilidade
   ↓
Fase 5  Quantização, Born, medida e Wallstrom
   ↓
Fase 6  Reconstrução lorentziana
   ↓
Fase 7  Spin e férmions
   ↓
Fase 8  Dimensão e anomalias
   ↓
Fase 9  Renormalização
   ↓
Fase 10 Limites conhecidos
   ↓
Fase 11 Constantes e massas
   ↓
Fase 13 Previsão cega
```

Modelo Padrão, cosmologia e Navier–Stokes não devem bloquear esse caminho
principal.

---

## 20. Primeira tarefa concreta

O primeiro trabalho não é modificar os 41 capítulos. É escrever um
documento curto contendo:

1. variedade;
2. dimensão provisória;
3. assinatura;
4. conexão de Bismut;
5. campos;
6. unidades;
7. ação mínima;
8. simetrias;
9. condições de contorno;
10. todas as variações.

Esse documento deve usar \(n\) simbólico, não conter massas experimentais,
não conter \(137\), \(6\pi^5\), Koide, MOND ou fatores de Fano e não alegar
resolver nenhum problema físico além da consistência do próprio modelo.

Se essa formulação mínima não puder ser construída, as aplicações
posteriores não possuem fundamento comum. Se puder, ela se torna a base
real para testar quais partes da GDQ sobrevivem.

