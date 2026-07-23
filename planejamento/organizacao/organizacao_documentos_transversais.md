# Organização dos documentos transversais fora de `questoes/`

> Este documento registra uma lacuna no plano de migração das questões: há
> muitos arquivos `.md` distribuídos que não pertencem diretamente a uma única
> `questão_NN`, mas são chamados por documentos canônicos, por `memory.md`, por
> `faltas.md` ou por relatórios de desenvolvimento. Eles exigem uma organização
> separada.

## 1. Diagnóstico

O plano `questoes_migracao_execucao_links.md` cobre:

- documentos `questão_*.md`;
- pastas `qNN/`;
- relatórios numéricos em `numerico/qNN_*`;
- arquivos associados diretamente a questões.

Mas o workspace também contém muitos `.md` transversais, por exemplo:

- documentos de ponte global--local;
- documentos de teoria da medida e interação clássico--quântico;
- documentos de nêutron e decaimento;
- relatórios gerais de status;
- relatórios de auditoria;
- documentos de ideias;
- documentos de reorganização do manuscrito;
- arquivos `zz*.md`;
- arquivos `Sem título*.md`;
- arquivos de resposta e rascunho;
- arquivos de extensões futuras.

Esses arquivos não devem ser movidos automaticamente para `questoes/`, porque
muitos deles atravessam várias questões ou pertencem ao manuscrito, à memória
estruturada ou a programas futuros.

## Atualização de execução — 2026-07-16

A organização transversal foi executada após a migração das questões.

Ficaram deliberadamente na raiz:

- `AGENTS.md`;
- `README.md`;
- `LICENSE.md`;
- `memory.md`;
- `faltas.md`;
- `faltas_mapa.md`;
- `faltas_plano.md`;
- `numerico.md`;
- enunciados futuros `43-0.md`--`49-0.md`.

Os demais documentos soltos foram movidos para:

- `topicos/ponte_global_local/`;
- `topicos/medida_interface/`;
- `topicos/neutron_decaimento/`;
- `topicos/geometria_torcao_hopf/`;
- `auditorias/`;
- `ideias/`;
- `planejamento/manuscrito/`;
- `triagem/sem_titulo/`.

O antigo `plano1.md` foi preservado em
`planejamento/organizacao/plano1.md`.

## 2. Problema separado

A organização correta exige duas migrações distintas:

1. **Migração das questões**

   ```text
   questão_*.md + qNN/ + associados diretos
   -> questoes/qNN/
   ```

2. **Organização transversal**

   ```text
   ponte_global_local_*.md
   teoria_interface_*.md
   neutron/*.md
   RELATORIO_*.md
   zz*.md
   Sem título*.md
   ideias e rascunhos
   -> estruturas temáticas separadas
   ```

Misturar essas duas migrações criaria perda de contexto.

## 3. Classes de documentos transversais

## 3.1 Ponte global--local

Arquivos:

```text
ponte_global_local_*.md
topicos/ponte_global_local/teorema_heranca_espectral_global_local_gdq.md
topicos/ponte_global_local/teorema_heranca_normalizacao_eletromagnetica.md
topicos/ponte_global_local/impacto_ponte_global_local_q37_q39_q40.md
topicos/ponte_global_local/plano_ponte_global_local_gdq.md
```

Destino proposto:

```text
topicos/ponte_global_local/
```

Função:

- lemas globais;
- herança espectral;
- transporte global--local;
- existência de sela/interface;
- impacto em Q37, Q39, Q40 e capítulos do manuscrito.

Regra:

- não mover para uma única questão;
- os índices de Q37, Q39, Q40 e Capítulo 6 devem apontar para esse tópico.

## 3.2 Teoria da medida e interface clássico--quântica

Arquivos:

```text
topicos/medida_interface/teoria_interface_classico_quantica_gdq.md
topicos/medida_interface/modelo_aparelho_minimo_gdq.md
topicos/medida_interface/detector_ohmico_gdq.md
topicos/medida_interface/derivacao_fonte_classica_interface_sg.md
topicos/medida_interface/derivacao_kernels_cH_iH.md
topicos/medida_interface/auditoria_rota_stern_gerlach_gdq.md
topicos/medida_interface/auditoria_gamma_magnetica_ZH.md
topicos/medida_interface/reducao_hessiana_torcional_aparelho.md
topicos/medida_interface/teorema_captura_born_interface_gdq.md
topicos/medida_interface/teorema_noether_zeeman_gdq.md
interface_medida/
```

Destino proposto:

```text
topicos/medida_interface/
```

Função:

- teoria da medida;
- Stern--Gerlach;
- impedância de aparelho;
- resposta de contorno;
- dissipação efetiva;
- Born condicionado.

Regra:

- não misturar com Q42 apenas;
- Q24, Q41, Q42 e capítulos futuros de medida devem referenciar esse tópico.

## 3.3 Nêutron, decaimento e processos nucleares

Arquivos:

```text
topicos/neutron_decaimento/mecanismo_neutron_decaimento.md
topicos/neutron_decaimento/fechamento_meia_vida_neutron_gdq.md
topicos/neutron_decaimento/fechamento_condicional_mecanismo_neutron.md
topicos/neutron_decaimento/fechamento_terceiros_jatos_neutron_gdq.md
topicos/neutron_decaimento/auditoria_coeficientes_wkb_neutron.md
topicos/neutron_decaimento/determinacao_coeficientes_cirurgia_neutron.md
topicos/neutron_decaimento/operador_ressonante_cirurgia_neutron.md
topicos/neutron_decaimento/taxa_decaimento_neutron_overlap_gdq.md
topicos/neutron_decaimento/ward_noether_cirurgia_neutron.md
neutron/
```

Destino proposto:

```text
topicos/neutron_decaimento/
```

Função:

- decaimento do nêutron;
- WKB/cirurgia;
- jatos causais;
- overlap;
- Noether/ward;
- relatórios numéricos associados.

Regra:

- não classificar como uma única questão sem revisar se pertence a Q40,
  fenomenologia nuclear ou futuro.

## 3.4 Relatórios gerais e auditorias globais

Arquivos:

```text
auditorias/RELATORIO_AUDITORIA_COMPLETA_GDQ.md
auditorias/RELATORIO_STATUS_TEORIA_GDQ.md
auditorias/RELATORIO_STATUS_TEORIA_GDQ_REVISADO.md
auditorias/RELATORIO_TORCAO_SPIN_S3_R4T4.md
auditorias/RESPOSTAS_NECESSARIAS_GDQ.md
auditorias/resposta_auditoria.md
auditorias/Omissões.md
auditorias/constantes_status.md
auditorias/auditoria_scripts_alpha.md
topicos/medida_interface/auditoria_background_macroscopico_interface.md
```

Destino proposto:

```text
auditorias/
```

Função:

- auditoria transversal;
- status histórico;
- mapas de omissões;
- consolidações temporárias.

Regra:

- preservar como histórico e auditoria;
- não usar como fonte canônica quando contradisser `memory.md` ou documento
  final da questão.

## 3.5 Ideias, possibilidades e rascunhos conceituais

Arquivos:

```text
ideias/possibilidades.md
ideias/ideiatorcao.md
ideias/ideiatorcao2.md
ideias/ideiatorcao3.md
ideias/rascunho_ideias1.md
ideias/possibilidade_torcao_discriminante_pde.md
ideias/zz.md
ideias/zz1.md
ideias/zz2.md
ideias/zz4.md
```

Destino proposto:

```text
ideias/
```

ou, se forem hipóteses já maturadas:

```text
brain/future/
brain/hypotheses/
```

Regra:

- não promover ideia a resultado;
- cada arquivo deve receber status:
  - exploratório;
  - hipótese;
  - programa futuro;
  - rejeitado;
  - incorporado.

## 3.6 Manuscrito e reestruturação

Arquivos:

```text
planejamento/manuscrito/estrutura_reorganizacao_manuscrito.md
planejamento/manuscrito/plano_primeiros_capitulos_gdq.md
planejamento/manuscrito/mapa_migracao_capitulo_01.md
topicos/geometria_torcao_hopf/justificativa_espacos.md
```

Destino proposto:

```text
manuscrito/meta/
```

ou:

```text
planejamento/manuscrito/
```

Função:

- planejamento editorial;
- recuperação de omissões;
- ordem de capítulos;
- estilo e estratégia de escrita.

## 3.7 Arquivos sem título

Arquivos:

```text
Sem título*.md
aconv/Sem título*.md
```

Destino proposto temporário:

```text
triagem/sem_titulo/
```

Regra:

- não apagar;
- não promover;
- classificar por conteúdo antes de mover para destino final.

Cada arquivo deve receber uma linha de triagem:

```text
arquivo | tema provável | status | destino
```

## 3.8 Extensões

Arquivos:

```text
extensoes/
```

Destino:

Manter como:

```text
extensoes/
```

ou integrar depois a:

```text
brain/future/
```

Regra:

- extensões não devem ser usadas como premissa do manuscrito principal sem
  revisão.

## 4. Estrutura transversal proposta

Criar depois da migração inicial das questões:

```text
topicos/
  ponte_global_local/
  medida_interface/
  neutron_decaimento/
auditorias/
ideias/
planejamento/
  manuscrito/
triagem/
  sem_titulo/
```

Essa estrutura é separada de:

```text
questoes/
brain/
manuscrito/
numerico/
pt-br/
en/
```

## 5. Como preservar chamadas

Antes de mover qualquer documento transversal:

```bash
rg -n "nome_do_arquivo" -g "*.md"
```

Depois de mover:

1. atualizar links em documentos canônicos;
2. deixar redirecionador temporário se houver chamadas históricas;
3. atualizar `memory.md` somente se o arquivo for fonte vigente;
4. atualizar `brain/` se for prova, hipótese, definição ou problema aberto.

## 6. Prioridade de organização

Ordem recomendada:

1. `questoes/` com documentos canônicos e associados diretos;
2. `topicos/ponte_global_local/`;
3. `topicos/medida_interface/`;
4. `topicos/neutron_decaimento/`;
5. `auditorias/`;
6. `ideias/`;
7. `planejamento/manuscrito/`;
8. `triagem/sem_titulo/`.

## 7. Relação com `memory.md`

`memory.md` não deve listar todos esses arquivos. Ele deve registrar apenas:

- quais tópicos transversais existem;
- quais são fontes vigentes;
- quais são históricos;
- quais tópicos alimentam quais questões ou capítulos.

Exemplo:

```text
O tópico transversal `ponte_global_local/` contém os lemas e resultados de
herança espectral usados por Q37, Q39, Q40 e pelo Capítulo 6.
```

## 8. Relação com `agent-memory`

O `agent-memory` deve guardar apenas resumos estáveis:

```text
Ponte global-local: fonte canônica em topicos/ponte_global_local/; usada por
Q37/Q39/Q40 e Cap. 6; status condicional conforme memory.md.
```

Não registrar listas completas de arquivos no `agent-memory`.

## 9. Decisão atual

O problema dos `.md` transversais é reconhecido como separado da migração das
questões.

O plano de `questoes/` deve continuar, mas com a ressalva:

> nem todo `.md` deve ir para `questoes/`; documentos que atravessam várias
> questões devem ir para `topicos/`, `auditorias/`, `ideias/`,
> `planejamento/` ou `triagem/`.
