# Plano de migração e revisão das questões GDQ

> Objetivo: organizar as questões e seus materiais associados em uma pasta
> `questoes/`, sem quebrar os links internos, sem perder o histórico de
> derivações e mantendo coerência com `memory.md`, `brain/` e o protocolo
> `AGENTS.md`.

## 1. Diagnóstico inicial

A organização atual não é apenas uma coleção de arquivos soltos. Ela contém
um grafo de chamadas internas:

- `questão_*.md` chama arquivos em `qNN/`;
- `faltas.md` chama muitos arquivos `q28/`, `q29/`, `q30/`, `q34/`, `q35/`,
  `q38/`, `q40/`;
- `memory.md` registra o status consolidado das questões e aponta para
  documentos finais;
- `brain/` já contém entradas estruturadas por questão;
- `numerico/` contém scripts e saídas auditadas que não devem ser misturados
  com rascunhos;
- há arquivos finais ou canônicos com nomes diferentes do padrão, por exemplo
  `questão_28_final.md`, `questão_29_final.md` e `questão_38_final.md`;
- há arquivos históricos e rascunhos que ainda podem ser citados, mas não
  devem se tornar fontes canônicas automaticamente.

Portanto, mover arquivos sem mapa prévio quebraria referências e poderia
apagar distinções importantes entre prova, hipótese, evidência numérica e
rascunho.

## 2. Regra central da migração

Nenhum arquivo deve ser movido antes de existir um mapa explícito:

$$
\text{arquivo atual}
\to
\text{destino proposto}
\to
\text{arquivos que chamam}
\to
\text{status canônico}
$$

Esse mapa deve preservar:

1. documento canônico da questão;
2. documentos associados chamados pelo canônico;
3. relatórios numéricos auditados;
4. rascunhos úteis, mas não canônicos;
5. links que precisam ser atualizados;
6. status vigente em `memory.md`;
7. ponteiro correspondente em `brain/` e `agent-memory`.

## 3. Estrutura-alvo

A pasta final deve ser:

```text
questoes/
  README.md
  mapa.md
  q02/
    index.md
    questao_02.md
    associados/
    numerico/
    historico/
  q03/
  ...
  q42/
```

### 3.1 Função dos arquivos

Cada `questoes/qNN/index.md` deve conter:

- enunciado da questão;
- documento canônico;
- status vigente;
- hipótese central;
- resultado fechado;
- limitações;
- pendências reais;
- arquivos associados;
- arquivos numéricos;
- arquivos históricos;
- links para `brain/`;
- status no `agent-memory`.

### 3.2 Regra para documentos principais

O documento principal deve ser nomeado sem acento:

```text
questoes/qNN/questao_NN.md
```

Quando houver final explícito, preservar isso:

```text
questoes/q28/questao_28_final.md
questoes/q29/questao_29_final.md
questoes/q38/questao_38_final.md
```

O `index.md` da questão deve declarar qual deles é canônico.

## 4. Classificação dos materiais

### 4.1 Canônico

Vai para a raiz da questão:

```text
questoes/qNN/questao_NN.md
questoes/qNN/index.md
```

Exemplos:

- `questoes/q02/questao_02.md`;
- `questão_28_final.md`;
- `questão_29_final.md`;
- `questão_38_final.md`;
- `questão_39.md`;
- `questão_40.md`;
- `questão_41.md`;
- `questão_42.md`.

### 4.2 Associado

Vai para:

```text
questoes/qNN/associados/
```

Exemplos:

- `q28/*.md`;
- `q29/*.md`;
- `q30/*.md`;
- `q34/*.md`;
- `q35/*.md`;
- `q38/*.md`;
- `q39/*.md`;
- `q40/*.md`;
- `q41/*.md`;
- `q42/*.md`.

### 4.3 Numérico

Preferência inicial: não mover imediatamente.

Manter em:

```text
numerico/qNN_*/
```

e referenciar em:

```text
questoes/qNN/index.md
```

Motivo: muitos scripts e saídas já foram auditados nesse caminho. A migração
dos numéricos deve ser fase posterior, pois exige atualização de caminhos de
execução e histórico de resultados.

### 4.4 Histórico

Vai para:

```text
questoes/qNN/historico/
```

Somente depois de confirmar que não é chamado como fonte vigente.

Exemplos:

- `questão_38.md`;
- `questão_38_2.md`;
- `R38.md`;
- `R38_2.md`;
- `r38_3.md`;
- relatórios antigos que foram superados por `questão_38_final.md`.

### 4.5 Backups e lixo

Não mover na primeira rodada:

```text
bkp/
lixo/
```

Esses diretórios devem permanecer como arquivo histórico externo, sem entrar
na organização canônica das questões.

## 5. Fases de execução

## Fase 0 — congelamento e inventário

Criar:

```text
questoes_migracao_mapa.md
```

Com a tabela:

```text
Questão | Arquivo atual | Tipo | Chamado por | Destino proposto | Ação | Observação
```

Tipos:

- `canonico`;
- `associado`;
- `numerico`;
- `historico`;
- `externo`;
- `ignorar por enquanto`.

Essa fase não move arquivos.

## Fase 1 — mapa de chamados

Para cada arquivo `.md` candidato à migração, registrar quem o chama:

```bash
rg -n "nome_do_arquivo|qNN/|questão_NN|questao_NN" -g "*.md"
```

O mapa deve priorizar:

1. `memory.md`;
2. `brain/**/*.md`;
3. `faltas.md`, `faltas_mapa.md`, `faltas_plano.md`;
4. `questão_*.md`;
5. `manuscrito/**/*.md`;
6. relatórios locais;
7. rascunhos.

## Fase 2 — criação da estrutura sem remoção

Criar:

```text
questoes/
questoes/README.md
questoes/mapa.md
questoes/q02/index.md
...
questoes/q42/index.md
```

Nesta fase, os `index.md` podem apontar para os arquivos antigos. Isso cria a
camada de navegação sem risco.

Exemplo:

```markdown
# Questão 39 — Hierarquia de massas leptônicas

Documento canônico atual: ../../questão_39.md
Associados: ../../q39/
Numéricos auditados: ../../numerico/q39_leptons/
Status vigente: resolvida como espectro global de massa de repouso.
```

## Fase 3 — migração canônica com `git mv`

Depois do mapa revisado:

1. mover documentos principais;
2. atualizar links diretos;
3. manter redirecionadores temporários quando necessário.

Exemplo de redirecionador temporário:

```markdown
# Documento movido

Este arquivo foi migrado para:

`questoes/q39/questao_39.md`
```

Isso evita quebra imediata em links antigos.

## Fase 4 — migração dos associados

Mover gradualmente:

```text
q28/*.md -> questoes/q28/associados/
q29/*.md -> questoes/q29/associados/
...
```

Antes de cada bloco:

1. listar chamados;
2. mover;
3. reescrever links;
4. rodar busca de referências antigas;
5. atualizar `questoes/qNN/index.md`.

## Fase 5 — revisão dos teoremas contra `memory.md`

Para cada questão, revisar:

1. o que é demonstrado;
2. o que é fechado estruturalmente;
3. o que é condicional;
4. o que é evidência numérica;
5. o que é ajuste ou comparação;
6. o que permanece em aberto;
7. se o `brain/` está coerente;
8. se `memory.md` precisa de atualização.

Essa revisão deve usar a cadeia mínima:

$$
\text{ação oficial}
\to
\text{background admissível}
\to
\text{Hessiana física}
\to
\text{operador e domínio}
\to
\text{condições de contorno}
\to
\text{espectro estável}
\to
\text{observável sem pós-ajuste}.
$$

## Fase 6 — atualização de memória

Atualizar:

```text
memory.md
brain/
agent-memory
```

Somente quando houver mudança material:

- mudança de status;
- identificação de documento canônico;
- contradição corrigida;
- pendência redefinida;
- migração de caminho canônico.

## Fase 7 — validação final

Verificar:

```bash
rg -n "questão_|q[0-9]+/|Q[0-9]+|R38|RELATORIO_Q38" -g "*.md"
```

Objetivo: localizar links antigos que ainda apontam para arquivos migrados.

Também verificar:

```bash
git status --short
```

Depois, criar commit local:

```text
Organiza questões GDQ em estrutura canônica
```

## 6. Ordem recomendada de migração

### Bloco A — fundação

- Q2;
- Q3;
- Q4;
- Q5;
- Q6;
- Q7;
- Q8;
- Q9.

Motivo: definem ação, bulk, causalidade, tempo, campos e reconstrução.

### Bloco B — equações e reconstrução

- Q10;
- Q11;
- Q12;
- Q13;
- Q14;
- Q15;
- Q16;
- Q17;
- Q18;
- Q19;
- Q20;
- Q21;
- Q22;
- Q23;
- Q24;
- Q25.

Motivo: derivam continuidade, Hamilton-Jacobi-Bohm, OS, Born, quantização,
medida e problema do sinal.

### Bloco C — setores de interação

- Q26;
- Q27;
- Q28;
- Q29;
- Q30;
- Q31;
- Q32;
- Q33;
- Q34;
- Q35.

Motivo: há muitos documentos associados e chamadas em `faltas.md`.

### Bloco D — calibração, massas, bárions e testes

- Q36;
- Q37;
- Q38;
- Q39;
- Q40;
- Q41;
- Q42.

Motivo: dependem fortemente de numéricos, relatórios e refinamentos recentes.

## 7. Pontos que exigem cuidado especial

### 7.1 Q28

Possui documento final e muitos associados:

- `questão_28_final.md`;
- `q28/*.md`;
- `numerico/q28_tres_estomatos/`;
- `numerico/q28_q29_eletrofraco/`.

Não mover sem mapear as chamadas em `faltas.md` e `memory.md`.

### 7.2 Q29

Possui documento final, muitos testes e várias rotas rejeitadas.

Separar:

- fechamento estrutural eletrofraco;
- normalização absoluta de `alpha`;
- colar dinâmico;
- rotas no-go;
- simulações W/Z;
- materiais que pertencem a Q37 ou Q42.

### 7.3 Q30

Possui muitos lemas em `q30/` chamados por `faltas.md`.

Não resumir nem apagar: esses arquivos são a trilha de fechamento do setor
confinamento/Wilson/mass gap efetivo.

### 7.4 Q34/Q35

São interdependentes. Há arquivo numérico comum:

```text
numerico/q34_q35_u1/
```

Não duplicar resultado. Criar referência cruzada nos dois índices.

### 7.5 Q38

É o caso mais sensível.

Documento canônico atual:

```text
questão_38_final.md
```

Arquivos antigos devem ser preservados como histórico:

- `questão_38.md`;
- `questão_38_2.md`;
- `R38.md`;
- `R38_2.md`;
- `r38_3.md`;
- `RELATORIO_Q38_3.md`;
- `q38/*.md`;
- `numerico/q38_gravidade/`.

### 7.6 Q39

Separar:

- fechamento espectral global de massas;
- efeitos de contorno Robin;
- correção térmica;
- avaliação direta `H/J`;
- scripts antigos em `q39/`;
- scripts auditados em `numerico/q39_leptons/`.

### 7.7 Q40

Separar:

- resposta principal em `questão_40.md`;
- observações/faltas em `questão_40_obs.md` e `questão_40_faltas.md`;
- adendos em `q40/`;
- numéricos em `numerico/q40_barions/`.

### 7.8 Q41

Há diretórios com conflito de maiúsculas/minúsculas:

```text
Q41 (Conflitos entre maiúsculas e minúsculas)
Q41 (Conflitos entre maiúsculas e minúsculas 1)
```

Não mover automaticamente. Primeiro auditar o conteúdo e decidir se são cópias
de conflito, backups ou lixo do sistema de arquivos.

## 8. Resultado esperado

Ao final:

1. `questoes/` será a porta de entrada canônica das questões;
2. `memory.md` continuará sendo o mapa técnico compacto;
3. `brain/` continuará sendo a memória estruturada;
4. `numerico/` continuará sendo a área auditável de cálculos, ao menos até
   segunda migração;
5. links antigos estarão redirecionados ou atualizados;
6. rascunhos não serão confundidos com documentos finais;
7. cada questão terá status, prova, limitações e pendências visíveis em um
   único `index.md`.

## 9. Próxima ação recomendada

Executar a Fase 0:

1. gerar `questoes_migracao_mapa.md`;
2. mapear chamados para Q28--Q42 primeiro, pois são as mais densas;
3. depois mapear Q2--Q27;
4. revisar o mapa antes de qualquer `git mv`.

