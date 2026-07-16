# AGENTS.md — Protocolo de trabalho no projeto GDQ

## 1. Missão

Este workspace contém o manuscrito, as auditorias, as derivações e os testes
numéricos da Geometrodinâmica Quântica (GDQ).

O agente deve colaborar com continuidade técnica e honestidade científica,
preservando a identidade própria da GDQ e distinguindo rigorosamente:

- axioma;
- definição;
- derivação;
- teorema condicional;
- redução efetiva;
- hipótese;
- evidência numérica;
- ajuste ou engenharia inversa;
- comparação fenomenológica;
- trabalho futuro.

O objetivo não é fazer toda ideia “bater”, mas determinar exatamente o que
segue da ação oficial, sob quais hipóteses e com qual poder preditivo.

---

## 2. Regra fundamental: preservar a ação oficial

A ação física fundamental da GDQ é:

\[
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
\]

O agente não deve alterar, substituir ou completar silenciosamente essa ação.

Em particular:

- não substituir a GDQ por Einstein--Hilbert, Yang--Mills, Dirac, Pauli,
  Lindblad ou pelo Modelo Padrão;
- não introduzir novos termos fundamentais apenas porque reproduzem um dado;
- não tratar funcionais auxiliares de Perelman como nova ação física;
- não importar fantasmas, BRST ou renormalização como ontologia da teoria;
- quando essas estruturas forem usadas, identificá-las como auditoria,
  comparação, redução efetiva ou linguagem externa.

Fontes, sondas e termos de bordo são permitidos quando exigidos pelo problema,
mas devem ser derivados pelo princípio variacional ou declarados explicitamente
como dados externos do aparelho.

---

## 3. Leitura obrigatória e hierarquia documental

### 3.1 Antes de trabalhar

Para tarefas substantivas:

1. ler `memory.md`;
2. identificar a questão e os documentos consolidados correspondentes;
3. consultar os capítulos relevantes em `pt-br/`;
4. consultar `faltas.md`, `faltas_mapa.md` e `faltas_plano.md` quando a tarefa
   envolver status ou pendências;
5. consultar o relatório numérico auditado quando houver cálculos.

Não é necessário reler todo o corpus para uma alteração local simples.

### 3.2 Ordem de autoridade

Se houver divergência, usar esta precedência:

1. instrução atual e explícita do usuário;
2. ação oficial e axiomas vigentes nas Questões 2, 3, 4 e 9;
3. documento final/consolidado da questão;
4. `memory.md` e documentos mestres de faltas;
5. relatório numérico auditado;
6. manuscrito original em `pt-br/`, como fonte de ideias e derivações a
   reaproveitar;
7. adendos e relatórios locais;
8. rascunhos, backups e scripts exploratórios.

Uma instrução do usuário pode mudar o trabalho a executar, mas uma mudança de
axioma ou ação deve ser destacada explicitamente antes de ser incorporada.

### 3.3 Arquivos históricos

Arquivos em `bkp/`, rascunhos numerados, versões antigas e relatórios locais
não são fontes canônicas. Eles podem conter ideias valiosas, mas não devem
reabrir automaticamente uma conclusão mais recente.

---

## 4. Geometrias e convenções que exigem cuidado

### 4.1 Bulk local oficial

A reconstrução vigente usa:

\[
M=\mathbb R^4\times T^4,
\qquad \dim_{\mathbb R}M=8,
\qquad \dim_{\mathbb C}M=4.
\]

O bulk é Hermitiano/Riemanniano, com estrutura complexa e conexão de Bismut.
O espaço-tempo lorentziano físico é reconstruído ou projetado.

### 4.2 Espaço cosmológico/espectral

\(T^5\times S^3\) aparece como espaço cosmológico de Einstein e domínio
auxiliar de cálculos globais. Não o identificar automaticamente com o bulk
local oficial.

Quando um resultado depender dessa geometria, o agente deve indicar:

1. em qual espaço o cálculo foi feito;
2. se existe mapa de redução para o bulk oficial;
3. se o resultado é fundamental, cosmológico, espectral ou apenas auxiliar.

### 4.3 Convenções fundamentais

Manter, salvo correção explicitamente justificada:

\[
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
\]

Não confundir:

- tempo físico \(t\);
- parâmetro de fluxo \(\tau\);
- variável causal complexa \(z_\tau\);
- geometria Kähler estrita com geometria Hermitiana/KT de torção não nula;
- circulação de Maslov com prova de spin intrínseco;
- rotação global isométrica com resposta localizada a uma sonda.

---

## 5. Método obrigatório de análise científica

### 5.1 Começar pelo enunciado exato

Antes de derivar, registrar:

- o que se pretende provar ou calcular;
- quais dados são fornecidos;
- qual é o domínio;
- quais são as condições iniciais e de contorno;
- quais parâmetros são universais e quais pertencem ao experimento;
- qual resultado distinguiria a GDQ de uma simples parametrização.

### 5.2 Cadeia mínima de fechamento

Uma afirmação preditiva forte exige:

\[
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
\]

Se algum elo faltar, informar precisamente qual é, sem declarar a questão
integralmente resolvida.

### 5.3 Provas e derivações

Em cálculos matemáticos:

1. definir todos os símbolos;
2. verificar dimensões e sinais;
3. declarar regularidade e domínio dos operadores;
4. separar identidades exatas de aproximações;
5. tratar modos zero, gauge, bordo e normalização;
6. verificar existência, unicidade e estabilidade quando relevantes;
7. não inferir uma identidade variacional apenas por coincidência numérica;
8. não chamar uma fórmula de teorema se um coeficiente foi escolhido pelo alvo.

### 5.4 Resultado negativo também é resultado

Se um ansatz falhar, registrar o que foi excluído. Não interpretar o fracasso
de um modelo simples como prova automática de um mecanismo alternativo.

---

## 6. Protocolo numérico

### 6.1 Classificação obrigatória

Todo resultado numérico deve ser classificado como:

1. avaliação direta de quantidade já derivada;
2. teste de convergência;
3. teste de consistência;
4. engenharia inversa;
5. ajuste/calibração;
6. comparação fenomenológica;
7. previsão cega.

### 6.2 Requisitos mínimos

Antes de declarar sucesso:

- informar equação, operador, domínio e contorno;
- registrar unidades e normalizações;
- congelar parâmetros antes da comparação quando houver pretensão preditiva;
- executar refinamento de malha ou tolerância;
- apresentar erro numérico e sensibilidade a parâmetros;
- comparar com solução analítica quando disponível;
- preservar saídas que contradigam a hipótese;
- distinguir erro de discretização de discrepância física;
- informar se o alvo experimental participou da construção.

### 6.3 Proibições

Não:

- ajustar um parâmetro e depois chamá-lo de derivado;
- absorver resíduo em “loop”, “térmico”, “Fano” ou “contorno” sem calcular o
  termo correspondente;
- usar proximidade com CODATA como prova da ontologia;
- omitir resultados ruins;
- considerar uma única malha como estudo de convergência;
- chamar um mock ou fixture sintética de background físico.

### 6.4 Código e resultados

- manter scripts históricos quando o usuário desejar rastreabilidade;
- criar novas versões claramente nomeadas em vez de apagar a história;
- manter parâmetros físicos separados dos parâmetros numéricos;
- salvar saídas relevantes em Markdown;
- atualizar o status conservador, não apenas o relatório local do solver.

---

## 7. Status das questões

Usar as seguintes categorias:

- **fechada**;
- **fechada estruturalmente**;
- **fechada condicionalmente**;
- **parcialmente resolvida**;
- **aberta**;
- **programa futuro**.

Ao fechar uma questão, incluir:

1. enunciado respondido;
2. hipóteses;
3. cadeia dedutiva;
4. resultado;
5. verificações;
6. limitações que não reabrem a questão;
7. pendências que de fato a mantêm condicional;
8. arquivos e scripts de apoio.

Não usar “oficialmente fechada” para ocultar uma hipótese essencial ainda não
demonstrada.

---

## 8. Teoria da medida e interação clássico--quântico

Este é um eixo prioritário do projeto.

O aparelho não deve receber operadores quânticos inseridos manualmente. A
cadeia desejada é:

\[
J_{\rm app}^{\rm clássico}
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
\]

Na análise de Stern--Gerlach, lembrar:

- spin, circulação e módulo de Hopf pertencem ao objeto antes da medição;
- o aparelho seleciona um eixo e quebra a degenerescência;
- \(\Lambda_{\Phi}\) é o operador DtN do objeto;
- \(\mathsf R_{\rm app}\) é a carga/impedância de interface;
- Hessiana fornece rigidez, não tempo;
- o tempo exige mobilidade causal;
- monotonicidade de Perelman não prova sozinha irreversibilidade;
- Born para um evento exige dinâmica condicionada, não apenas projetores;
- emaranhamento, pontes e condições futuras permanecem hipóteses até prova de
  Bell, no-signalling e causalidade.

---

## 9. Edição de documentos

### 9.0 Matemática no manuscrito Quartz

Nos arquivos de `manuscrito/`, usar `$...$` para matemática
inline e blocos `$$ ... $$` com cada delimitador em sua própria linha. Não
usar `\(...\)` ou `\[...\]` nesses arquivos e nunca colocar a equação na mesma
linha dos delimitadores `$$`.

### 9.1 Preservação

- não apagar alterações do usuário;
- não sobrescrever documentos consolidados sem verificar seu status;
- evitar mudanças no manuscrito principal enquanto o trabalho estiver apenas
  nas questões, salvo pedido explícito;
- não arquivar ou excluir rascunhos sem autorização;
- ao consolidar, indicar quais arquivos o novo documento substitui.

### 9.2 Estilo científico

Preferir:

- linguagem dedutiva e precisa;
- equações com hipóteses próximas;
- tabelas de status quando úteis;
- termos “proposta”, “condicional” e “efetivo” quando apropriados.

Evitar:

- linguagem triunfalista;
- ataques ao Modelo Padrão ou à história da física;
- analogias usadas como demonstração;
- citações inventadas;
- afirmar consenso científico para ideias internas da GDQ.

### 9.3 Manuscrito, FAQ e auditoria

- manuscrito principal: teoria positiva e dedutiva;
- apêndices: provas e cálculos extensos;
- FAQ: objeções e respostas;
- `questão_*.md`: auditoria e rastreabilidade;
- `memory.md`: mapa técnico e estado vigente;
- `possibilidades.md`: ideias ainda não usadas como fundamento;
- `faltas.md`: backlog conservador.

---

## 10. Atualização de `memory.md`

`memory.md` é a memória técnica central, mas não substitui os documentos de
prova.

Atualizá-lo quando houver mudança material:

- novo axioma ou convenção;
- fechamento ou reabertura de questão;
- derivação direta nova;
- mudança no status numérico;
- nova contradição identificada;
- decisão arquitetural/documental;
- nova prioridade de pesquisa.

Não é necessário atualizá-lo para correções ortográficas, inspeções sem nova
conclusão ou mudanças locais sem impacto conceitual.

Toda atualização deve indicar a fonte e preservar a distinção entre estado
vigente e histórico.

---

## 11. Ferramentas e MCPs

Usar as ferramentas disponíveis que sejam adequadas à tarefa. MCPs são
opcionais e dependem da sessão; não assumir que um conector citado em versões
anteriores está instalado.

Prioridades:

- arquivos locais para o conteúdo canônico do projeto;
- Git para histórico e diferenças, sem operações destrutivas;
- busca local para localizar definições e contradições;
- web e artigos apenas quando a tarefa exigir verificação externa;
- fontes primárias e documentação oficial para matemática, física e software.

Ao usar fontes externas, não permitir que elas substituam silenciosamente os
axiomas da GDQ. Elas servem para verificar teoremas, contexto, dados e
compatibilidade experimental.

---

## 12. Fluxo recomendado de trabalho

Para uma tarefa substantiva:

1. ler `memory.md` e este arquivo;
2. localizar os documentos canônicos do tema;
3. conferir se já existe derivação equivalente;
4. declarar o enunciado e o status inicial;
5. derivar ou implementar;
6. testar em proporção ao risco;
7. confrontar o resultado com as hipóteses;
8. atualizar o documento da questão;
9. sincronizar `faltas.md` e documentos numéricos quando necessário;
10. atualizar `memory.md` se houve mudança material;
11. entregar um resumo conciso com arquivos alterados, resultado e limitações.

---

## 13. Critérios de qualidade

Ordem de prioridade:

1. consistência com a ação oficial;
2. correção matemática e científica;
3. honestidade sobre hipóteses e ajustes;
4. reprodutibilidade;
5. continuidade documental;
6. clareza;
7. eficiência computacional;
8. elegância.

Quando rigor e concordância numérica entrarem em conflito, preservar o rigor e
documentar a discrepância.
