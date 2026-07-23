# Plano executivo — migração de questões preservando chamadas internas

Este plano complementa `questoes_migracao_plano.md`. Aqui o foco é operacional:
como criar `questoes/` e mover os arquivos sem quebrar os documentos que os
chamam.

## 1. Regra operacional

Cada migração deve obedecer à sequência:

$$
\text{inventariar chamadas}
\to
\text{criar destino}
\to
\text{mover com git mv}
\to
\text{atualizar chamadores}
\to
\text{validar referências antigas}
\to
\text{atualizar memória}
$$

Nenhum arquivo chamado por outro documento deve ser movido sem uma das duas
ações:

1. atualizar todos os chamadores para o novo caminho; ou
2. manter um redirecionador temporário no caminho antigo.

## 2. Estratégia de preservação de links

### 2.1 Chamadas diretas em texto

Exemplos atuais:

```text
q29/modo_ordem_eletrofraco.md
q30/conexao_su3_wilson_gap.md
q38/derivacao_causal_residuo_q38.md
questão_38_final.md
numerico/q39_leptons/evaluate_H_J_q39.py
```

Após migração, esses caminhos devem virar:

```text
questoes/q29/associados/modo_ordem_eletrofraco.md
questoes/q30/associados/conexao_su3_wilson_gap.md
questoes/q38/associados/derivacao_causal_residuo_q38.md
questoes/q38/questao_38_final.md
numerico/q39_leptons/evaluate_H_J_q39.py
```

Nota: `numerico/` não será movido na primeira etapa.

### 2.2 Links Markdown

Links do tipo:

```markdown
[questão_39.md](questão_39.md)
[q28/indice_global_t5_s3.md](q28/indice_global_t5_s3.md)
```

devem ser reescritos para:

```markdown
[questao_39.md](questoes/q39/questao_39.md)
[indice_global_t5_s3.md](questoes/q28/associados/indice_global_t5_s3.md)
```

### 2.3 Links `file:///`

Links absolutos do tipo:

```text
file:///home/pedro/Dropbox/obs/todo/q39/compare_boundaries_q39.py
```

devem ser tratados com cuidado. Há duas opções:

1. manter como histórico quando aparecerem em transcrições antigas;
2. substituir por caminho relativo quando aparecerem em documento canônico.

Regra:

- documento canônico: atualizar;
- rascunho/histórico: não precisa atualizar na primeira rodada.

### 2.4 Redirecionadores temporários

Para documentos muito citados, criar redirecionador temporário no caminho antigo
quando a atualização global for arriscada.

Exemplo:

```markdown
# Documento migrado

Este arquivo foi movido para:

`questoes/q38/questao_38_final.md`

Use o novo caminho como referência canônica.
```

Redirecionadores são úteis para:

- `questão_28_final.md`;
- `questão_29_final.md`;
- `questão_38_final.md`;
- `questão_39.md`;
- `questão_40.md`;
- `questão_41.md`;
- `questão_42.md`;
- pastas densas como `q29/`, `q30/`, `q38/`, `q40/`.

Mas redirecionadores não devem ser permanentes. Após validação e atualização
dos links, podem ser arquivados ou removidos somente com autorização.

## 3. Estrutura a criar

Criar:

```text
questoes/
  README.md
  mapa.md
  q02/
  q03/
  ...
  q42/
```

Cada questão terá:

```text
questoes/qNN/
  index.md
  questao_NN.md
  associados/
  historico/
```

Quando houver documento final:

```text
questoes/qNN/questao_NN_final.md
```

Quando houver variante importante:

```text
questoes/q30/questao_30_yang_mills.md
questoes/q40/questao_40_faltas.md
questoes/q40/questao_40_obs.md
```

## 4. Arquivos canônicos de raiz

### 4.1 Questões simples

Mover:

```text
questoes/q02/questao_02.md  -> questoes/q02/questao_02.md
questoes/q03/questao_03.md  -> questoes/q03/questao_03.md
...
questoes/q27/questao_27.md -> questoes/q27/questao_27.md
```

### 4.2 Questões com finais explícitos

Usar como canônico:

```text
questão_28_final.md -> questoes/q28/questao_28_final.md
questão_29_final.md -> questoes/q29/questao_29_final.md
questão_38_final.md -> questoes/q38/questao_38_final.md
```

Mover para histórico:

```text
questão_28.md -> questoes/q28/historico/questao_28.md
questão_29.md -> questoes/q29/historico/questao_29.md
questão_38.md -> questoes/q38/historico/questao_38.md
questão_38_2.md -> questoes/q38/historico/questao_38_2.md
```

### 4.3 Questões com variantes

Q30:

```text
questão_30.md -> questoes/q30/questao_30.md
questão_30_yang_mills.md -> questoes/q30/questao_30_yang_mills.md
```

Q40:

```text
questão_40.md -> questoes/q40/questao_40.md
questão_40_faltas.md -> questoes/q40/questao_40_faltas.md
questão_40_obs.md -> questoes/q40/questao_40_obs.md
```

## 5. Pastas associadas

Mover com `git mv`:

```text
q28/ -> questoes/q28/associados/
q29/ -> questoes/q29/associados/
q30/ -> questoes/q30/associados/
q31/ -> questoes/q31/associados/
q32/ -> questoes/q32/associados/
q34/ -> questoes/q34/associados/
q35/ -> questoes/q35/associados/
q38/ -> questoes/q38/associados/
q39/ -> questoes/q39/associados/
q40/ -> questoes/q40/associados/
q41/ -> questoes/q41/associados/
q42/ -> questoes/q42/associados/
```

Importante: se a pasta for movida inteira, todos os chamados `qNN/arquivo.md`
devem ser reescritos para `questoes/qNN/associados/arquivo.md`.

## 6. Numéricos

Não mover na primeira execução.

Manter:

```text
numerico/q28_tres_estomatos/
numerico/q28_q29_eletrofraco/
numerico/q29_wz/
numerico/q30_confinamento/
numerico/q31_cp_forte/
numerico/q34_q35_u1/
numerico/q37_alpha/
numerico/q38_gravidade/
numerico/q39_leptons/
numerico/q40_barions/
```

Cada `questoes/qNN/index.md` deve apontar para os diretórios numéricos
correspondentes.

Motivo: os scripts e relatórios numéricos possuem histórico próprio e são
chamados por `numerico/status_numerico_auditado.md`, `faltas.md`,
`questão_*.md` e relatórios. Migrá-los junto adicionaria risco desnecessário.

## 7. Chamadores que devem ser atualizados

O levantamento detectou chamadas importantes em:

```text
memory.md
faltas.md
faltas_mapa.md
faltas_plano.md
numerico.md
numerico/status_numerico_auditado.md
auditorias/RELATORIO_STATUS_TEORIA_GDQ.md
auditorias/RELATORIO_TORCAO_SPIN_S3_R4T4.md
topicos/ponte_global_local/teorema_heranca_espectral_global_local_gdq.md
brain/**/*.md
questão_*.md
qNN/*.md
```

Após cada bloco migrado, rodar busca por caminhos antigos.

Exemplo para Q29:

```bash
rg -n "questão_29|q29/" -g "*.md"
```

O bloco só está validado quando:

1. documentos canônicos apontam para caminhos novos;
2. `memory.md` aponta para caminhos novos;
3. `brain/` aponta para caminhos novos;
4. `faltas.md` aponta para caminhos novos ou está explicitamente marcado como
   histórico;
5. nenhum documento canônico chama caminho antigo sem redirecionador.

## 8. Ordem executiva segura

### Etapa 1 — criar infraestrutura

1. criar `questoes/README.md`;
2. criar `questoes/mapa.md`;
3. criar `questoes/q02` até `questoes/q42`;
4. criar `index.md` mínimo para cada questão apontando ainda para os caminhos
   antigos.

Essa etapa não quebra nada.

### Etapa 2 — migrar Q2--Q9

São menos densas e já estão bem registradas em `brain/`.

Atualizar:

- `memory.md`;
- `brain/**/source`;
- `planejamento/manuscrito/plano_primeiros_capitulos_gdq.md`, se necessário.

### Etapa 3 — migrar Q10--Q27

Mover documentos principais.

Sem mover `bkp/`.

Atualizar chamadas em:

- `brain/`;
- `memory.md`;
- `faltas.md`, se houver.

### Etapa 4 — migrar Q28--Q30

Bloco crítico.

Antes de mover:

```bash
rg -n "questão_28|questão_29|questão_30|q28/|q29/|q30/" -g "*.md"
```

Mover:

- documentos finais;
- pastas associadas;
- variantes.

Atualizar chamadas imediatamente.

### Etapa 5 — migrar Q31--Q35

Bloco médio, com forte interdependência Q34/Q35.

Não duplicar `numerico/q34_q35_u1/`.

### Etapa 6 — migrar Q36--Q42

Bloco recente e mais sensível.

Cuidados:

- Q38 tem histórico longo;
- Q39 mistura `q39/` antigo e `numerico/q39_leptons/` auditado;
- Q40 tem documentos auxiliares e observacionais;
- Q41 tem conflito de diretórios maiúsculas/minúsculas;
- Q42 ainda está em desenvolvimento.

## 9. Procedimento padrão por bloco

Para cada bloco:

### 9.1 Antes

Executar:

```bash
git status --short
rg -n "qNN/|questão_NN|questao_NN" -g "*.md"
```

Salvar o resultado em seção própria de `questoes/mapa.md`.

### 9.2 Durante

Usar `git mv` para preservar histórico.

Exemplo:

```bash
git mv questão_39.md questoes/q39/questao_39.md
git mv q39 questoes/q39/associados
```

### 9.3 Depois

Atualizar links com substituições explícitas.

Exemplo:

```text
q39/fechamento_variacional_q39.md
->
questoes/q39/associados/fechamento_variacional_q39.md
```

Rodar:

```bash
rg -n "q39/|questão_39.md" -g "*.md"
```

Se ainda aparecer em documento canônico, corrigir ou justificar.

## 10. Política de redirecionadores

Usar redirecionador temporário quando:

- há muitos links antigos;
- o arquivo é muito citado;
- a atualização global aumenta risco de erro;
- o arquivo aparece em rascunhos ou transcrições históricas.

Não usar redirecionador para arquivos internos pouco citados se todos os links
forem atualizados no mesmo bloco.

## 11. Atualização de `memory.md`

Após cada bloco migrado, adicionar nota curta:

```markdown
Atualização: os documentos da QNN foram migrados para `questoes/qNN/`.
O documento canônico é `questoes/qNN/questao_NN.md`. Os materiais associados
estão em `questoes/qNN/associados/`. O status teórico permanece inalterado.
```

Se a revisão mudar status, registrar a mudança separadamente e justificar.

## 12. Atualização do `agent-memory`

Registrar somente fato consolidado:

```text
QNN migrada para questoes/qNN; documento canônico X; status inalterado Y;
associados em Z; numéricos permanecem em numerico/...
```

Não registrar lista longa de todos os arquivos no agent-memory. Essa lista fica
em `questoes/mapa.md`.

## 13. Critério de aceite

A migração de uma questão está aceita quando:

1. `questoes/qNN/index.md` existe;
2. o documento canônico está em `questoes/qNN/`;
3. associados relevantes estão em `questoes/qNN/associados/` ou explicitamente
   referenciados;
4. numéricos estão referenciados;
5. `memory.md` aponta para o novo caminho;
6. `brain/` aponta para o novo caminho;
7. os chamadores canônicos foram atualizados;
8. busca por caminhos antigos não retorna chamadas canônicas quebradas;
9. `git status` mostra apenas mudanças esperadas.

## 14. Primeiro passo recomendado

Executar apenas a Etapa 1:

1. criar `questoes/`;
2. criar `questoes/README.md`;
3. criar `questoes/mapa.md`;
4. criar `questoes/q02` até `questoes/q42`;
5. criar `index.md` mínimo para cada uma apontando para o estado atual.

Depois disso, revisar o mapa antes do primeiro `git mv`.

